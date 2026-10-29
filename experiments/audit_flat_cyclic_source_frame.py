#!/usr/bin/env python3
"""Exact finite source-frame algebra and scheme-theoretic wall diagnostics."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field


def recurrence_case(N):
    Q = sp.symbols('Q', nonzero=True)
    variables = sp.symbols(f'b0:{N*N}')
    B = sp.Matrix(N, N, variables)
    P = sp.zeros(N)
    for j in range(N):
        P[(j+1) % N, j] = 1
    A = sp.zeros(N)
    A[0, :] = sp.ones(1, N)
    first = [B[i, 0]-int(i == 0) for i in range(N)]
    commutator = B*P-Q*P*B
    equations = first+[commutator[i, j] for i in range(1, N) for j in range(N)]
    # Square independent system: source first column and all nonzero rows.
    solved = sp.linsolve(equations, variables)
    expected = sp.diag(*[Q**j for j in range(N)])
    assert solved == sp.FiniteSet(tuple(expected))
    defect = sp.zeros(N)
    defect[0, N-1] = 1-Q**N
    assert expected*P-Q*P*expected == defect
    assert expected*A == A and A*P == A and A*A == A
    assert P**N == sp.eye(N)
    return {'N': N, 'source_cyclic_recurrence_unique_over_Q_Q': True,
            'number_independent_linear_equations': len(equations)}


def inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p), dtype=np.int64) % p


def algebra_case(N, root):
    p, eta = root_field(N)
    Q = pow(eta, 4, p)
    if not root:
        Q = next(a for a in range(2, p) if len({pow(a, j, p) for j in range(N+1)}) == N+1)
    nodes = [pow(Q, j, p) for j in range(N)]
    B = np.diag(nodes).astype(np.int64)
    P = np.zeros_like(B)
    A = np.zeros_like(B)
    A[0, :] = 1
    for j in range(N):
        P[(j+1) % N, j] = 1
    E = []
    for j in range(N):
        value = np.eye(N, dtype=np.int64)
        for k in range(N):
            if k != j:
                value = value@(B-nodes[k]*np.eye(N, dtype=np.int64)) % p
                value = value*pow((nodes[j]-nodes[k]) % p, -1, p) % p
        expected = np.zeros_like(B)
        expected[j, j] = 1
        assert np.array_equal(value, expected)
        E.append(value)
    Pi = P.T
    delta = (1-pow(Q, N, p)) % p
    tauB = pow(Q, -1, p)*(B-delta*E[0]) % p
    assert np.array_equal(P@B@Pi % p, tauB)
    matrixunits = {(i, j): E[i]@np.linalg.matrix_power(P, (i-j) % N) % p
                   for i, j in itertools.product(range(N), repeat=2)}
    checks = 0
    for i, j, k, l in itertools.product(range(N), repeat=4):
        expected = matrixunits[i, l] if j == k else np.zeros_like(B)
        assert np.array_equal(matrixunits[i, j]@matrixunits[k, l] % p, expected)
        checks += 1
    assert np.array_equal(E[0]@sum((np.linalg.matrix_power(P, j) for j in range(N)), np.zeros_like(B)) % p, A)
    # Arbitrary invertible conjugate, recover exactly by the source orbit.
    G = np.eye(N, dtype=np.int64)
    for i in range(N-1):
        G[i, i+1] = i+2
    G = G@np.diag(np.arange(1, N+1, dtype=np.int64)) % p
    Gi = inverse(G, p)
    Bg, Pg, Ag = [G@x@Gi % p for x in (B, P, A)]
    v = G[:, 0]
    columns, current = [], v
    for _ in range(N):
        columns.append(current)
        current = Pg@current % p
    orbit = np.column_stack(columns) % p
    assert np.array_equal(orbit, G)
    assert np.array_equal(inverse(orbit, p)@Bg@orbit % p, B)
    assert np.array_equal(inverse(orbit, p)@Ag@orbit % p, A)
    # Scalar freedom exists with identical source frame and normalized source.
    for scalar in (0, 1, 3):
        C = scalar*np.eye(N, dtype=np.int64)
        assert int(np.trace(A@C)) % p == scalar % p
        assert not np.any((C@B-B@C) % p)
        assert not np.any((C@P-P@C) % p)
    return {'N': N, 'primitive_root': root, 'matrix_unit_products': checks,
            'endpoint_corrected_tau_and_source_recovery': True,
            'conjugate_source_orbit_frame_recovered': True,
            'scalar_period_not_fixed': True}


def scheme_defect_case(N):
    delta = sp.symbols('delta')
    variables = sp.symbols(f'r1:{N}')
    R = sp.zeros(N)
    R[0, 0] = 1
    for j in range(1, N):
        R[0, j] = variables[j-1]
    A = sp.zeros(N)
    A[0, :] = sp.ones(1, N)
    E = sp.zeros(N)
    E[0, 0] = 1
    assert R*R == R and sp.trace(R) == 1
    assert A*R == R and R*A == A
    equations = [delta*R[0, j] for j in range(1, N)]
    assert equations == [delta*x for x in variables]
    # Over a square-zero normal base, rho_j=delta*c_j is a genuine
    # nonzero, unresolved defect parameter, killed by delta only.
    for j in range(1, N):
        assert sp.rem(equations[j-1].subs(variables[j-1], delta), delta**2, delta) == 0
    return {'N': N, 'unsaturated_defect_equations': [str(x) for x in equations],
            'projector_alignment_and_flat_saturation_checked': True}


def nonaligned_case():
    Q = sp.symbols('Q', nonzero=True)
    delta, h = 1-Q**2, Q-Q**-1
    t, x = delta/(1-delta**2), delta**2/(1-delta**2)
    P, A = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[1, 1], [0, 0]])
    B = sp.Matrix([[1, t*h], [0, Q+x*h]])
    R = sp.Matrix([[1+x, -t], [t, -x]])
    zero = sp.zeros(2)
    simplify = lambda M: M.applyfunc(sp.factor)
    assert sp.factor(t*t-x*(1+x)) == 0
    assert simplify(R*R-R) == zero and sp.trace(R) == 1
    assert simplify(B*A-A) == zero and A*P == A
    assert simplify(B*P*B.inv()*P-Q*(sp.eye(2)+(Q**-2-1)*R)) == zero
    assert R.subs(Q, -1) == sp.diag(1, 0)
    assert B.subs(Q, -1) == sp.diag(1, -1)
    assert simplify(A*R-R) != zero
    assert sp.factor(B[1, 1]-Q) != 0
    return {'N': 2, 'all_non_aligned_relations_exact': True,
            'same_actual_root_point': True, 'flat_rational_deformation': True,
            'B_eigenvalue_difference': str(sp.factor(B[1, 1]-Q)),
            'source_alignment_failure': str(simplify(A*R-R))}


def main():
    recurrences = [recurrence_case(N) for N in range(2, 8)]
    algebras = [algebra_case(N, root) for N in range(2, 9) for root in (True, False)]
    defects = [scheme_defect_case(N) for N in range(2, 8)]
    result = {'status': 'PASS', 'source_recurrence_cases': recurrences,
              'whole_and_root_crossed_product_cases': algebras,
              'scheme_defect_flat_saturation_cases': defects,
              'nonaligned_flat_counterexample': nonaligned_case(),
              'scope': 'Whole fixed-N aligned source-frame algebra and scalar ambiguity; no selected volume theorem.'}
    path = Path(__file__).with_name('flat_cyclic_source_frame_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'recurrences': len(recurrences),
                      'whole_and_root_algebras': len(algebras),
                      'matrix_unit_products': sum(x['matrix_unit_products'] for x in algebras),
                      'flat_defect_presentations': len(defects),
                      'nonaligned_rational_counterexample': True,
                      'results': str(path)}, indent=2))


if __name__ == '__main__':
    main()
