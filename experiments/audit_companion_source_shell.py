#!/usr/bin/env python3
"""Exact companion highest/Whittaker source shell and polynomial gauge.

Own proofs are the lower-row recurrence and nilpotent polynomial
factorization; these checks cover N=2,...,7 symbolically and actual
primitive/generic finite-field fibres, including the full moment row.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field


def symbolic_case(N):
    Q, z = sp.symbols('Q', nonzero=True), sp.symbols('z')
    tails = list(sp.symbols(f't1:{N}'))
    t = [1-sum(tails)]+tails
    Y, L = sp.zeros(N), sp.zeros(N)
    for j in range(N-1):
        Y[j+1, j] = 1
        L[j, j+1] = 1
    Y[:, N-1] = sp.Matrix(t)
    B = sp.diag(*[Q**j for j in range(N)])
    x = [sp.Integer(1)]
    for m in range(1, N):
        x.append(sp.expand((1-Q**m)*t[N-m]
                           +sum(t[N-m+l]*x[l] for l in range(1, m))))
    X = sp.Matrix(N, N, lambda i, j: Q**i*x[j-i] if j >= i else 0)
    lower = X*Y-Q*Y*X
    assert all(sp.expand(lower[i, j]) == 0 for i in range(1, N) for j in range(N))
    v, ell = sp.eye(N)[:, 0], sp.ones(1, N)
    assert X*v == v
    assert (ell*Y-ell).applyfunc(sp.expand) == sp.zeros(1, N)
    assert sp.factor(Y.det()-(-1)**(N-1)*t[0]) == 0
    assert X.det() == Q**(N*(N-1)//2)
    chi = z**N-sum(t[i]*z**i for i in range(N))
    assert sp.expand(Y.charpoly(z).as_expr()-chi) == 0
    A = 1-sum(t[N-m]*z**m for m in range(1, N+1))
    reduced_coeff = [sp.Integer(1)]
    for m in range(1, N):
        reduced_coeff.append(sp.expand(reduced_coeff[-1]-t[N-m]))
    Ared = sum(reduced_coeff[m]*z**m for m in range(N))
    assert sp.expand(A-(1-z)*Ared) == 0
    assert sp.expand(A-z**N*chi.subs(z, 1/z)) == 0
    xpoly = sum(x[m]*z**m for m in range(N))
    assert sp.rem(sp.expand(A*xpoly-A.subs(z, Q*z)), z**N, z) == 0
    G = sp.eye(N)-sum((t[N-m]*L**m for m in range(1, N)), sp.zeros(N))
    assert (G*B-X*G).applyfunc(sp.expand) == sp.zeros(N)
    assert G*v == v and G.det() == 1
    rightrow = sp.Matrix([reduced_coeff])
    assert (ell*G-rightrow).applyfunc(sp.expand) == sp.zeros(1, N)
    # Actual mixed source/clock moments recover the entire polynomial;
    # pure Y moments are blind by ell Y=ell.
    moments = list(ell*X)
    assert moments[0] == 1
    recovered_x = [sp.Integer(1)]+[sp.expand(moments[j]-Q*moments[j-1])
                                 for j in range(1, N)]
    assert all(sp.expand(recovered_x[j]-x[j]) == 0 for j in range(N))
    recovered_t = {}
    for m in range(1, N):
        numerator = recovered_x[m]-sum(recovered_t[N-m+l]*recovered_x[l]
                                       for l in range(1, m))
        recovered_t[N-m] = sp.cancel(numerator/(1-Q**m))
        assert sp.expand(recovered_t[N-m]-t[N-m]) == 0
    jacobian = sp.Matrix(moments[1:]).jacobian(list(reversed(tails)))
    for i in range(N-1):
        assert sp.expand(jacobian[i, i]-(1-Q**(i+1))) == 0
        assert all(jacobian[i, j] == 0 for j in range(i+1, N-1))
    momentdet = sp.prod(1-Q**m for m in range(1, N))
    assert sp.rem(sp.expand(momentdet-N), sp.cyclotomic_poly(N, Q), Q) == 0
    # The actual periodic source is the exact section t0=1,others0.
    section = {tail: 0 for tail in tails}
    assert Y.subs(section)**N == sp.eye(N)
    assert G.subs(section) == sp.eye(N)
    assert X.subs(section) == B
    return {'N': N, 'symbolic_companion_and_all_lower_moment_rows': True,
            'highest_and_Whittaker_source': True,
            'characteristic_pointing_factor': True,
            'polynomial_gauge_GB_equals_XG_without_root_denominators': True,
            'cosource_ellG_equals_reduced_polynomial_row': True,
            'mixed_source_clock_moments_recover_characteristic_polynomial': True,
            'moment_Jacobian_primitive_root_value': N,
            'actual_periodic_section_G_identity': True}


def inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p), dtype=np.int64) % p


def moment_case(N, root):
    p, eta = root_field(N)
    Q = pow(eta, 4, p) if root else 2
    t = [0]+[j+1 for j in range(1, N)]
    t[0] = (1-sum(t[1:])) % p
    if not t[0]:
        t[-1] += 1
        t[0] = (1-sum(t[1:])) % p
    Y = np.zeros((N, N), dtype=np.int64)
    for j in range(N-1):
        Y[j+1, j] = 1
    Y[:, -1] = t
    x = [1]
    for m in range(1, N):
        x.append(((1-pow(Q, m, p))*t[N-m]
                  +sum(t[N-m+l]*x[l] for l in range(1, m))) % p)
    X = np.array([[pow(Q, i, p)*x[j-i] % p if j >= i else 0
                   for j in range(N)] for i in range(N)], dtype=np.int64)
    moment = (pow(Q, -1, p)*X@Y@inverse(X, p)@inverse(Y, p)-np.eye(N, dtype=np.int64)) % p
    assert not np.any(moment[1:, :])
    row = moment[0, :]
    assert int(row[0]) == (pow(Q, -N, p)-1) % p
    v = np.eye(N, dtype=np.int64)[:, 0]
    assert np.array_equal(np.outer(v, row), moment)
    assert np.array_equal(X@v % p, v)
    assert np.array_equal(np.ones(N, dtype=np.int64)@Y % p, np.ones(N, dtype=np.int64))
    return {'N': N, 'primitive_root': root, 'full_multiplicative_moment_row': True,
            'determinant_constraint_wv': int(row[0]),
            'highest_and_output_source_exact': True}


def main():
    symbolic = [symbolic_case(N) for N in range(2, 8)]
    moments = [moment_case(N, root) for N in range(2, 8) for root in (True, False)]
    result = {'status': 'PASS', 'symbolic': symbolic, 'full_moment_fibres': moments,
              'scope': 'Exact whole companion source shell and canonical polynomial gauge; no knot period comparison.'}
    path = Path(__file__).with_name('companion_source_shell_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'symbolic_levels': len(symbolic),
                      'full_moment_fibres': len(moments), 'results': str(path)}, indent=2))


if __name__ == '__main__':
    main()
