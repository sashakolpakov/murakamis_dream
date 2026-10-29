#!/usr/bin/env python3
"""Exact diagnostics of torsion initial forms and cofinite rank bounds.

All root tests use cyclotomic polynomial division over Q. The actual
operator example is an explicit nonminimal annihilator of the unknot
normal state, demonstrating a genuine isolated rational-rank jump.
No hyperbolic state comparison or volume assertion is made.
"""

from functools import cache
from itertools import combinations
from math import gcd, lcm
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_cyclic_steinberg_lattice import rank


q, Z = sp.symbols('q Z')


@cache
def cyclotomic(level):
    return sp.Poly(sp.cyclotomic_poly(2*level,q),q,domain=sp.QQ)


def root_zero(terms,level,k):
    coefficients = {}
    for (a,b),c in terms:
        e = (a+2*k*b) % (2*level)
        coefficients[e] = coefficients.get(e,0)+c
    polynomial = sp.Poly.from_dict({(e,):c for e,c in coefficients.items() if c},q,domain=sp.QQ)
    return polynomial.rem(cyclotomic(level)).is_zero


def support_bound(P):
    support = [monomial for monomial,_ in sp.Poly(P,q,Z).terms()]
    count = len(support)
    primorial = int(sp.prod(sp.primerange(2,count+1)))
    exceptional_degree, vertical_order = 0, 0
    for left,right in combinations(support,2):
        da,db = left[0]-right[0],left[1]-right[1]
        common = gcd(abs(da),abs(db))
        a,b = da//common,db//common
        powers = [-b*i+a*j for i,j in support]
        width = max(powers)-min(powers)
        exceptional_degree = max(exceptional_degree,width*int(sp.totient(primorial*common)))
        if b == 0:
            vertical_order = max(vertical_order,primorial*common)
    return primorial,exceptional_degree,vertical_order


def coset_roots(level,coset):
    a,b,h,t = coset
    if (2*level)%t:
        return set()
    rhs = 2*level*h//t-a
    predicted_count = gcd(abs(b),level) if rhs%(2*gcd(abs(b),level)) == 0 else 0
    roots = {k for k in range(level) if (2*b*k-rhs)%(2*level) == 0}
    assert len(roots) == predicted_count
    return roots


def verify_contained_coset(terms,coset):
    a,b,h,t = coset
    assert b != 0 and gcd(abs(a),abs(b)) == 1
    d = 0 if abs(b)==1 else pow(a,-1,abs(b))
    c = (a*d-1)//b
    assert a*d-b*c == 1
    w = sp.symbols('w')
    phi = sp.Poly(sp.cyclotomic_poly(t,w),w,domain=sp.QQ)
    coefficients = {}
    for (i,j),value in terms:
        exponent = -b*i+a*j
        phase = (h*(d*i-c*j))%t
        coefficients[exponent] = coefficients.get(exponent,0)+value*w**phase
    assert all(sp.Poly(value,w,domain=sp.QQ).rem(phi).is_zero
               for value in coefficients.values())


def polynomial_case(name,P,cosets):
    P = sp.expand(P)
    terms = sp.Poly(P,q,Z).terms()
    for coset in cosets:
        verify_contained_coset(terms,coset)
    primorial,bound,vertical = support_bound(P)
    records = []
    for level in range(2,51):
        actual = {k for k in range(level) if root_zero(terms,level,k)}
        persistent = set().union(*(coset_roots(level,C) for C in cosets))
        assert persistent <= actual
        beyond_bound = int(sp.totient(2*level)) > bound and 2*level > vertical
        if beyond_bound:
            assert actual == persistent, (name,level,actual,persistent,bound)
        records.append({'level':level,'actual_root_indices':sorted(actual),
                        'persistent_coset_indices':sorted(persistent),
                        'beyond_explicit_exception_bound':beyond_bound})
    return {'name':name,'polynomial':str(P),'Mann_primorial':primorial,
            'exceptional_cyclotomic_degree_bound':bound,
            'vertical_order_bound':vertical,'cosets':cosets,'levels':records}


def actual_operator_case(level):
    prime,generator,root = field(level)
    Q = root*root%prime
    eye = np.eye(level,dtype=np.int64)
    Y = np.zeros_like(eye)
    for j in range(level-1):
        Y[j+1,j] = 1
    Y[0,level-1] = generator
    T = np.diag([pow(Q,j,prime) for j in range(level)]).astype(np.int64)
    B = ((Y-eye)@T-(Q*Y-eye))%prime
    C = ((1-root)*eye+T)%prime
    L = C@B%prime
    v = np.zeros(level,dtype=np.int64)
    v[0],v[1] = -1,1
    assert not np.any(B@v%prime)
    assert not np.any(L@v%prime)
    nullity = level-rank(L,prime)
    assert nullity == (2 if level==3 else 1)
    return {'level':level,'generic_nonunit_central_value':generator,
            'unknot_normal_state_annihilated':True,
            'rational_rank':nullity,'isolated_jump_only_at_level_3':True}


def main():
    cases = [
        ('single_even_character',Z-q**2,[(-2,1,0,1)]),
        ('odd_level_extra_character',(Z-q**2)*(Z+q),[(-2,1,0,1),(-1,1,1,2)]),
        ('two_sign_cosets_cover_all_levels',(Z+1)*(Z+q),[(0,1,1,2),(-1,1,1,2)]),
        ('half_shift_coset_never_occupied',Z-q,[(-1,1,0,1)]),
        ('even_level_double_root_set',Z**2-q**4,[(-2,1,0,1),(-2,1,1,2)]),
        ('cubic_coset',Z**3-q**6,[(-2,1,0,1),(-2,1,1,3),(-2,1,2,3)]),
        ('isolated_triangle_torsion',1-q+Z,[]),
        ('persistent_plus_sporadic',(1-Z)*(1-q+Z),[(0,1,0,1)]),
        ('vertical_exception',(Z-q**2)*(q**2+1),[(-2,1,0,1)]),
        ('no_torsion_roots',1-3*q+Z,[]),
    ]
    records = [polynomial_case(*case) for case in cases]
    print(f'exact cyclotomic torsion grids: {len(records)*49} level cases passed',flush=True)
    operators = [actual_operator_case(n) for n in range(2,31)]
    print(f'actual unknot annihilator with isolated rank jump: {len(operators)} cases passed',flush=True)
    result = {'scope':'Diagnostics of the uniform torsion/initial-rank proof; no hyperbolic volume theorem.',
              'torsion_initial_forms':records,'actual_operator_example':operators}
    Path(__file__).with_name('torsion_initial_rank_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__ == '__main__':
    main()
