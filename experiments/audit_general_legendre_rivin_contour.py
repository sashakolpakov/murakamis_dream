#!/usr/bin/env python3
"""Audits explicit all-rank Legendre/Rivin contour identities.

The general proofs are in notes/general_legendre_rivin_contour.md.
Random symmetric gluing data here are analytic tests, not new knot
examples. The original figure-eight signature is a scope check.
"""

import json
from pathlib import Path
import random

import mpmath as mp
import numpy as np
import sympy as sp


def diag(values):
    return mp.diag(list(values))


def maximum(matrix):
    return max(abs(x) for x in matrix)


def positive_volume(theta, beta, gamma):
    return sum(mp.im(mp.polylog(2, mp.exp(2j * a))) / 2
               for triple in zip(theta, beta, gamma) for a in triple)


def action(C, kappa, rho, theta):
    x = mp.matrix([r + 1j * t for r, t in zip(rho, theta)])
    return (sum(mp.polylog(2, mp.exp(z)) for z in x)
            + (x.T * (mp.eye(len(x)) - C) * x)[0] / 2
            + 1j * ((kappa - mp.pi * mp.matrix([1] * len(x))).T * x)[0])


def sample_case(dimension, rng):
    entries = [[rng.randint(-2, 2) for _ in range(dimension)] for _ in range(dimension)]
    C = mp.matrix([[entries[min(i, j)][max(i, j)] for j in range(dimension)]
                   for i in range(dimension)])
    star = mp.matrix([mp.pi / 3] * dimension)
    kappa = C * star + star
    theta = mp.matrix([mp.pi / 3 + mp.mpf(rng.randint(-30, 30)) / 1000 for _ in range(dimension)])
    gamma = kappa - C * theta
    beta = mp.pi * mp.matrix([1] * dimension) - theta - gamma
    assert min(list(theta) + list(beta) + list(gamma)) > 0
    rho = mp.matrix([mp.log(mp.sin(b) / mp.sin(g)) for b, g in zip(beta, gamma)])
    z = mp.matrix([mp.exp(r + 1j * t) for r, t in zip(rho, theta)])
    F = mp.im(action(C, kappa, rho, theta))
    V = positive_volume(theta, beta, gamma)
    p = mp.matrix([mp.exp(2j * t) for t in theta])
    q = mp.matrix([mp.exp(2j * g) for g in gamma])
    graph_error = max(abs(zj - (1 - pj * qj) / (1 - qj)) for zj, pj, qj in zip(z, p, q))
    norm_errors = []
    for zj, pj, qj in zip(z, p, q):
        zz = 1 - 1 / zj
        norm_errors.extend([abs(zj / mp.conj(zj) - pj), abs(zz / mp.conj(zz) - qj)])
    D = diag([mp.im(v / (1 - v)) for v in z])
    K = mp.eye(dimension) - C + diag([mp.re(v / (1 - v)) for v in z])
    H = K + 1j * D
    R = -(D ** -1) * K
    explicit_R = diag([mp.cot(b) + mp.cot(g) for b, g in zip(beta, gamma)]) * C - diag([mp.cot(b) for b in beta])
    G = D + K * (D ** -1) * K
    JL = R + 1j * mp.eye(dimension)
    volume_hessian = (-diag([mp.cot(t) for t in theta])
                      - (C - mp.eye(dimension)).T * diag([mp.cot(b) for b in beta]) * (C - mp.eye(dimension))
                      - C.T * diag([mp.cot(g) for g in gamma]) * C)
    identity_errors = [abs(F - V), graph_error, max(norm_errors), maximum(R - explicit_R),
                       maximum(H * JL + G), maximum(volume_hessian + G)]
    assert max(identity_errors) < mp.mpf('1e-45')
    assert abs(mp.det(JL)) > mp.mpf('1e-8')
    Hnp = np.array(H.tolist(), dtype=np.complex128)
    schur_eigenvalues = []
    for split in range(1, dimension):
        E, Fblock = Hnp[:split, :split], Hnp[:split, split:]
        S = Hnp[split:, split:] - Fblock.T @ np.linalg.solve(E, Fblock)
        lower = float(np.linalg.eigvalsh(S.imag)[0])
        assert lower > 0
        schur_eigenvalues.append(lower)
    homotopy_slack = []
    F0 = mp.im(action(C, kappa, mp.matrix([0] * dimension), theta))
    vstar = dimension * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    for s in map(mp.mpf, ('0', '.1', '.4', '.7', '1')):
        Fs = mp.im(action(C, kappa, s * rho, theta))
        slack = (1 - s) * F0 + s * V - Fs
        assert slack >= -mp.mpf('1e-45')
        assert Fs <= vstar + mp.mpf('1e-45')
        homotopy_slack.append(float(slack))
    m = [rng.randint(-2, 2) for _ in range(dimension)]
    if not any(m):
        m[0] = 1
    trial_rho = mp.matrix([mp.mpf(rng.randint(-20, 20)) / 10 for _ in range(dimension)])
    derivatives = []
    for r, t, b, mj in zip(trial_rho, theta, beta, m):
        derivatives.append(-mp.arg(1 - mp.exp(r + 1j * t)) - b + 2 * mp.pi * mj)
    escape_derivative = -sum(mp.sign(mj) * value for mj, value in zip(m, derivatives) if mj)
    alias_norm = sum(abs(mj) for mj in m)
    assert escape_derivative <= -mp.pi * alias_norm
    return {'dimension': dimension, 'maximum_identity_error': float(max(identity_errors)),
            'nonzero_Jacobian_modulus': float(abs(mp.det(JL))),
            'Schur_min_Im_eigenvalues': schur_eigenvalues,
            'radial_homotopy_convexity_slacks': homotopy_slack,
            'alias_label': m, 'alias_escape_derivative': float(escape_derivative),
            'proved_test_bound': float(-mp.pi * alias_norm)}


def original_scope_check():
    M = sp.Matrix([[-sp.Rational(832683, 405769), sp.Rational(1, 52), -sp.Rational(21, 8)],
                   [sp.Rational(1, 52), -sp.Rational(9, 8), sp.Rational(3, 8)],
                   [-sp.Rational(21, 8), sp.Rational(3, 8), sp.Rational(9, 32)]])
    assert M[1, 1] < 0 and M[2, 2] > 0
    return {'original_figure_eight_flow_signature': 'INDEFINITE: positive-chart hypothesis correctly fails',
            'opposite_exact_diagonal_entries': [str(M[1, 1]), str(M[2, 2])],
            'five_crossing_source_scope': 'Its exact bent-source and face/kernel certificate remain separate inputs; no automatic transfer claimed.'}


def radial_boundary_scope_check():
    with mp.workdps(60):
        C = mp.matrix([[0]])
        kappa = mp.matrix([2 * mp.pi / 3])
        theta = mp.matrix([mp.pi / 6])
        rho = mp.matrix([-mp.log(3) / 2])
        v3 = mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
        selected = mp.im(action(C, kappa, rho, theta))
        boundary = mp.im(action(C, kappa, mp.matrix([0]), mp.matrix([mp.pi / 3])))
        assert abs(selected / v3 - mp.mpf(2) / 3) < mp.mpf('1e-45')
        assert abs(boundary / v3 - 1) < mp.mpf('1e-45')
        assert boundary > selected
        return {'positive_analytic_data_only_not_a_knot_model': True,
                'selected_volume_over_v3': float(selected / v3),
                'arbitrary_radius_boundary_over_v3': float(boundary / v3),
                'conclusion': 'Concavity alone does not bound boundary transport from an arbitrary source radius.'}


def main():
    rng = random.Random(20261028)
    with mp.workdps(60):
        rows = [sample_case(d, rng) for d in range(1, 7) for _ in range(6)]
    result = {'status': 'PASS', 'analytic_identity_cases': rows, 'actual_source_scope_checks': original_scope_check(),
              'radial_boundary_scope_check': radial_boundary_scope_check(),
              'scope': 'General positive-chart contour and radial homotopy identities; no original quantum-cycle transport or broad knot theorem asserted.'}
    output = Path(__file__).with_name('general_legendre_rivin_contour_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'all_rank_cases': len(rows),
                      'dimensions': list(range(1, 7)),
                      'maximum_identity_error': max(r['maximum_identity_error'] for r in rows),
                      'scope_checks': result['actual_source_scope_checks']}, indent=2))


if __name__ == '__main__':
    main()
