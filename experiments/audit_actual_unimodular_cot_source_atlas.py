#!/usr/bin/env python3
"""Exact cot side-current algebra and original source chart reindexing.

This does not test a global small-phase contour. The universal functional
and its holomorphic-hull limitation are proved in the accompanying note.
"""

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from audit_actual_scalar_cardinal_source_completion import knot_routing
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix,partial


def kernel_algebra():
    X,Y = sp.symbols('X Y',nonzero=True)
    k = lambda z:1/(1-z)
    identities = [k(X)*k(Y)-k(X*Y)*k(Y)+k(X*Y)*k(1/X),
                  k(X)*k(Y)-k(X/Y)*k(Y)-k(X)*k(Y/X),
                  k(X)+k(1/X)-1]
    assert all(sp.factor(f)==0 for f in identities)
    main = k(X*Y)*k(Y)
    side = -k(X*Y)*k(1/X)
    assert sp.simplify(sp.residue(main,X,1/Y)+sp.residue(side,X,1/Y))==0
    x,y = sp.symbols('x y')
    old = sp.residue(sp.residue(1/(x*y),x,0),y,0)
    new = sp.residue(sp.residue(1/((x+y)*y),x,0),y,0)
    current = sp.residue(sp.residue(1/(x*(x+y)),x,0),y,0)
    assert (old,new,current)==(1,0,1)
    return dict(exact_periodic_kernel_identities=3,
                artificial_divisor_principal_parts_cancel=True,
                full_unit_side_current_residues=[int(old),int(new),int(current)])


def chart_matrix(D):
    A = sp.eye(D)
    A[0,:] = A[0,:]+A[1,:]
    if D>2:
        A[1,:] = A[1,:]-A[2,:]
    A.row_swap(0,D-1)
    A[0,:] = -A[0,:]
    assert A.det() in (-1,1)
    inverse = A.inv()
    assert all(v.q==1 for v in inverse)
    rows = [tuple(map(int,A.row(j))) for j in range(D)]
    # The entire finite row set has a common N-independent torus chamber.
    forms = rows+[tuple(int(i==j) for i in range(D)) for j in range(D)]
    C = max(abs(v) for row in forms for v in row)
    eps = [Fraction(1,32*D*C)]
    for _ in range(D-1):
        eps.append(eps[-1]/(8*D*C))
    for row in forms:
        first = next(j for j,v in enumerate(row) if v)
        leading = abs(row[first])*eps[first]
        tail = sum(abs(row[j])*eps[j] for j in range(first+1,D))
        assert leading-tail>0
        assert sum(abs(row[j])*eps[j] for j in range(D))<Fraction(1,4)
    return A,inverse


def original_source_chart_case(N,width,word):
    H = HardyNetwork(N,1)
    p,D,d = H.p,len(word)+1,N-1
    A,inverse = chart_matrix(D)
    # Actual vertex t=d,k=0, with the complete affine integer shift retained.
    shift = sp.Matrix([d]+[0]*(D-1))
    offsets,crossings = knot_routing(width,word)
    source = {}
    for u in itertools.product(range(N),repeat=D):
        t,ks = u[0],u[1:]
        color = {n:t+sum(a*b for a,b in zip(row,ks)) for n,row in offsets.items()}
        if any(not 0<=v<N for v in color.values()):
            continue
        weight = 1
        for a,b,c,e,sign in crossings:
            R = H.plus if sign>0 else H.minus
            weight = weight*int(R[color[c]*N+color[e],color[a]*N+color[b]]) % p
        for head in range(1,width):
            weight = weight*int(H.pivot[color[head]]) % p
        source[u] = weight
    reindexed = {}
    for u,weight in source.items():
        y = tuple(map(int,A*(sp.Matrix(u)-shift)))
        recovered = tuple(map(int,shift+inverse*sp.Matrix(y)))
        assert recovered == u
        assert y not in reindexed
        reindexed[y] = weight
    assert len(reindexed)==len(source)
    source_sum = sum(source.values())*pow(N,-1,p) % p
    chart_sum = sum(reindexed.values())*pow(N,-1,p) % p
    assert source_sum == chart_sum
    W = word_matrix(word,H.plus,H.minus,width,N,p)
    cut = partial(W,H.pivot,width,N,p)
    original = sum(int(cut[j,j]) for j in range(N))*pow(N,-1,p) % p
    assert original == chart_sum
    external = H.dimension*pow(H.twist,-sum(1 if w>0 else -1 for w in word),p) % p
    return dict(N=N,width=width,word=list(word),source_dimension=D,
                original_lattice_states=len(source),unimodular_determinant=int(A.det()),
                complete_affine_shift_retained=True,
                original_kappa_pivots_and_external_line_retained=True,
                exact_normalized_period_mod_p=int(chart_sum*external % p))


def main():
    algebra = kernel_algebra()
    cases = [original_source_chart_case(N,width,word)
             for N in (2,3)
             for width,word in [(2,[1,1,1]),(3,[1,-2,1,-2]),
                                (4,[1,-2,1,-2,3]),(4,[1,2,3])]]
    result = dict(status='PASS',cot_current_algebra=algebra,
                  original_affine_source_chart_cases=cases,
                  scope='Exact fixed-coefficient universal cot/current identities and original integer-source atlas. No global phase-small deformation or volume bound.')
    target = Path(__file__).with_name('actual_unimodular_cot_source_atlas_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',kernel_identities=3,
                         compulsory_side_current=True,original_source_charts=len(cases),
                         reindexed_original_states=sum(c['original_lattice_states'] for c in cases)),indent=2))


if __name__=='__main__':
    main()
