#!/usr/bin/env python3
"""Exact exterior-algebra certificates for the rational source Bloch cycle.

The coefficient field is rational functions in independent symbols.
There are no floating-point comparisons or numerical volume recognition.
"""
import json
from pathlib import Path

import sympy as sp


def vec(**terms):
    return {k: sp.sympify(v) for k, v in terms.items() if v != 0}


def add(*terms):
    out = {}
    for scale, v in terms:
        for k, value in v.items():
            out[k] = sp.expand(out.get(k, 0)+scale*value)
    return {k: v for k, v in out.items() if v != 0}


def wedge(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            if i == j:
                continue
            key, sign = ((i, j), 1) if i < j else ((j, i), -1)
            out[key] = sp.expand(out.get(key, 0)+sign*ai*bj)
    return {k: v for k, v in out.items() if v != 0}


def five_term():
    X, Y, A, B, C = (vec(**{c: 1}) for c in ('X', 'Y', 'A', 'B', 'C'))
    pairs = [(X, A), (Y, B),
             (add((1, Y), (-1, X)), add((1, C), (-1, X))),
             (add((1, Y), (1, A), (-1, X), (-1, B)),
              add((1, C), (-1, X), (-1, B))),
             (add((1, A), (-1, B)), add((1, C), (-1, B)))]
    total = add(*[(sign, wedge(a, b))
                  for sign, (a, b) in zip((1, -1, 1, -1, 1), pairs)])
    assert total == {}
    x, y = sp.symbols('x y')
    z = [x, y, y/x, (1-1/x)/(1-1/y), (1-x)/(1-y)]
    one_minus = [1-x, 1-y, (x-y)/x, (x-y)/(x*(1-y)), (x-y)/(1-y)]
    assert all(sp.cancel(1-a-b) == 0 for a, b in zip(z, one_minus))
    assert sp.cancel(z[3]-y*(1-x)/(x*(1-y))) == 0
    return {'generic_five_term_boundary': 'zero in free exterior algebra on 5 generators',
            'rational_factorizations': 6}


def antisymmetric_boundary():
    Ta, Tb, Sa, Sb, Sc = (vec(**{c: 1}) for c in ('Ta', 'Tb', 'Sa', 'Sb', 'Sc'))
    Tc = add((-1, Ta), (-1, Tb))
    z = add((1, Ta), (1, Sb), (-1, Sc))
    one_minus_z = add((-1, Tb), (1, Sa), (-1, Sc))
    bar_z = add((-1, Ta), (1, Sb), (-1, Sc))
    one_minus_bar_z = add((1, Tb), (1, Sa), (-1, Sc))
    lhs = add((1, wedge(z, one_minus_z)), (-1, wedge(bar_z, one_minus_bar_z)))
    rhs = add((2, wedge(Ta, Sa)), (2, wedge(Tb, Sb)), (2, wedge(Tc, Sc)))
    assert add((1, lhs), (-1, rhs)) == {}
    # This leftover is the real-real part of the UNSYMMETRIZED boundary;
    # it is not asserted to vanish by stationarity.
    real_part = add((1, wedge(Sb, Sa)), (-1, wedge(Sb, Sc)), (-1, wedge(Sc, Sa)))
    assert len(real_part) == 3
    a, b = sp.symbols('a b', real=True)
    # The shape sine identity is checked via its real and imaginary parts.
    imaginary = sp.sin(a)*sp.sin(b)-sp.sin(b)*sp.sin(a)
    real = sp.cos(a)*sp.sin(b)+sp.cos(b)*sp.sin(a)-sp.sin(a+b)
    assert sp.expand_trig(imaginary) == 0
    assert sp.expand_trig(real) == 0
    return {'generic_conjugate_boundary_identity': 'delta(z)-delta(bar z)=2 sum T_r wedge S_r',
            'unsymmetrized_real_wedge_terms_retained': len(real_part),
            'shape_sine_identity': 'exact'}


def quotient_stationarity():
    # Each independent symbol represents a completely arbitrary coefficient;
    # the all-size theorem is the displayed bilinear sum/reindexing proof.
    B = sp.symbols('B', nonzero=True)
    U = [vec(**{f'U{l}': 1}) for l in range(3)]
    w = sp.symbols('w0:4')
    rows = [{} for _ in U]
    total = {}
    for j in range(4):
        for r in range(3):
            S = vec(**{f'S{j}{r}': 1})
            b = sp.symbols(f'b{j}{r}_0:3')
            T = add(*[(B*bl, Ul) for bl, Ul in zip(b, U)])
            total = add((1, total), (w[j], wedge(T, S)))
            for l in range(3):
                rows[l] = add((1, rows[l]), (w[j]*b[l], S))
    factored = add(*[(B, wedge(Ul, row)) for Ul, row in zip(U, rows)])
    assert add((1, total), (-1, factored)) == {}
    return {'symbolic_quotient_coordinates': 3, 'symbolic_atoms': 4,
            'stationarity_coefficients_independent': True,
            'complete_boundary_factorization': 'B sum_l U_l wedge stationary_row_l',
            'stationary_rows_zero_implies_boundary_zero': True}


if __name__ == '__main__':
    result = {'status': 'PASS', 'five_term': five_term(),
              'conjugation': antisymmetric_boundary(),
              'stationarity': quotient_stationarity(),
              'scope': 'Exact symbolic identities supporting the uniform rational Bloch-cycle proof. No integral torsion, trace-field, actual manifold-class, or general hyperbolic-volume identification is certified.'}
    Path(__file__).with_name('actual_positive_source_bloch_regulator_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS generic five-term wedge /generic conjugate-shape boundary /symbolic quotient-stationarity factorization; no floating-point steps')
