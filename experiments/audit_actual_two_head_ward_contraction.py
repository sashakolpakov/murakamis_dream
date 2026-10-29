#!/usr/bin/env python3
"""Check the actual two-head current against its proved path contraction.

The proof, including uniformity in N, is in
notes/actual_two_head_ward_polynomial_contraction.md. Numerical spectra
here check the identification and scope; they are not that proof.
"""

import json
from pathlib import Path

import numpy as np


def physical_current(N, s, x):
    d = N - 1
    incoming = list(range(max(0, s - d), min(d, s) + 1))
    outgoing = list(range(max(0, s + 1 - d), min(d, s + 1) + 1))
    rows = {a: i for i, a in enumerate(outgoing)}
    matrix = np.zeros((len(outgoing), len(incoming)), dtype=complex)
    Q = np.exp(2j * np.pi / N)
    for j, a in enumerate(incoming):
        b = s - a
        if a < d:
            matrix[rows[a + 1], j] += 1 - Q ** (a + 1)
        if b < d:
            matrix[rows[a], j] += Q ** a * (1 - Q ** (b + 1)) / x
    return matrix


def path_current(N, s, x):
    lower = s <= N - 2
    L = s + 1 if lower else 2 * N - 2 - s
    i = np.arange(L)
    a = 2 * np.sin(np.pi * (L - i) / N)
    b = 2 * np.sin(np.pi * (i + 1) / N)
    if lower:
        a /= abs(x)
    else:
        b /= abs(x)
    A = np.zeros((L, L + 1))
    A[i, i] = a
    A[i, i + 1] = -b
    log_eta = np.r_[0., np.cumsum(np.log(a / b))]
    eta = np.exp(log_eta - np.max(log_eta))
    eta /= np.linalg.norm(eta)
    return A, eta, a, b


def check_case(N, s, x, rng, check_inverse=True):
    F = physical_current(N, s, x)
    A, eta, a, b = path_current(N, s, x)
    sf = np.linalg.svd(F, compute_uv=False)
    sa = np.linalg.svd(A, compute_uv=False)
    spectral_error = float(np.max(abs(sf - sa)))
    assert spectral_error < 3e-11 * max(1., 1 / abs(x))
    L = len(a)
    lower_bound = min(1., 1 / abs(x)) * 2 * np.sin(np.pi / N) / np.sqrt(L * (L + 1))
    assert sf[-1] >= lower_bound * (1 - 1e-10)
    assert np.linalg.norm(A @ eta) < 2e-12 * max(1., 1 / abs(x))
    log_ratios = np.log(a / b)
    assert np.max(np.diff(log_ratios), initial=-1.) <= 2e-12
    p = eta ** 2
    w = a ** 2 * p[:-1]
    amin = min(1., 1 / abs(x)) * 2 * np.sin(np.pi / N)
    prefix = np.cumsum(p)[:-1]
    suffix = np.cumsum(p[::-1])[::-1][1:]
    assert np.all(w + 1e-13 >= amin ** 2 / (L + 1) * np.minimum(prefix, suffix))
    g = rng.normal(size=L + 1) + 1j * rng.normal(size=L + 1)
    g -= np.dot(p, g)
    variance = np.dot(p, abs(g) ** 2)
    energy = np.dot(w, abs(np.diff(g)) ** 2)
    assert variance <= L * (L + 1) / amin ** 2 * energy + 1e-10
    row = {'N': N, 'degree': s, 'x_abs': float(abs(x)),
           'spectral_error': spectral_error,
           'minimum_singular_value': float(sf[-1]),
           'proved_lower_bound': float(lower_bound),
           'ratio_to_bound': float(sf[-1] / lower_bound)}
    if check_inverse:
        h = np.linalg.pinv(F)
        source = rng.normal(size=F.shape[1]) + 1j * rng.normal(size=F.shape[1])
        current = F @ source
        solution = h @ current
        residual = np.linalg.norm(F @ solution - current)
        assert residual < 3e-10 * max(1., np.linalg.norm(current))
        assert np.linalg.norm(solution) <= max(1., abs(x)) * N ** 2 / 4 * np.linalg.norm(current) + 1e-10
        assert np.linalg.norm(F @ h @ F - F) < 2e-10 * max(1., np.linalg.norm(F))
        assert np.linalg.norm(h @ F @ h - h) < 2e-10 * max(1., np.linalg.norm(h))
        row['compatible_solve_residual'] = float(residual)
        if s == N - 1:
            powers = np.arange(N) * np.log(complex(x))
            cup = np.exp(powers - np.max(powers.real))
            cup /= np.linalg.norm(cup)
            assert np.linalg.norm(F @ cup) < 1e-10 * max(1., 1 / abs(x))
            projector = np.eye(N) - h @ F
            assert np.linalg.norm(projector - np.outer(cup, cup.conj())) < 2e-10
    return row


def main():
    rng = np.random.default_rng(20261028)
    rows = []
    for N in range(2, 23):
        for x in (np.exp(.37j), .3 * np.exp(.83j), 3.1 * np.exp(-.43j)):
            for s in range(2 * N - 2):
                rows.append(check_case(N, s, x, rng))
    large = []
    for N in (32, 64, 128):
        for x in (np.exp(.23j), .3 * np.exp(.63j), 3.1 * np.exp(-.41j)):
            for s in sorted({0, N // 2, N - 2, N - 1, 3 * N // 2 - 2, 2 * N - 3}):
                large.append(check_case(N, s, x, rng, check_inverse=False))
    holomorphic = []
    for N in (3, 7, 16, 32):
        x0 = np.exp(.29j)
        for s in sorted({0, N - 2, N - 1, 2 * N - 3}):
            F0 = physical_current(N, s, x0)
            h0 = np.linalg.pinv(F0)
            ai = np.arange(max(0, s - (N - 1)), min(N - 1, s) + 1)
            ao = np.arange(max(0, s + 1 - (N - 1)), min(N - 1, s + 1) + 1)
            for u in (-2 + .7j, .3 - 1.1j, 2 + .9j):
                z = np.exp(u / N)
                Di = np.diag(z ** ai)
                Do = np.diag(z ** ao)
                F = physical_current(N, s, z * x0)
                h = z * Di @ h0 @ np.linalg.inv(Do)
                P = Di @ (np.eye(F0.shape[1]) - h0 @ F0) @ np.linalg.inv(Di)
                Cok = Do @ (np.eye(F0.shape[0]) - F0 @ h0) @ np.linalg.inv(Do)
                errors = [np.linalg.norm(F - np.linalg.multi_dot([Do, F0, np.linalg.inv(Di)]) / z),
                          np.linalg.norm(h @ F - (np.eye(F.shape[1]) - P)),
                          np.linalg.norm(F @ h - (np.eye(F.shape[0]) - Cok))]
                assert max(errors) < 2e-10
                norm = np.linalg.norm(h, 2)
                bound = np.exp(2 * abs(u.real) + abs(u.real) / N) * N ** 2 / 4
                assert norm <= bound
                holomorphic.append({'N': N, 'degree': s, 'u': str(u),
                                    'maximum_homotopy_identity_error': float(max(errors)),
                                    'inverse_norm': float(norm), 'proved_bound': float(bound)})
    result = {'status': 'PASS', 'actual_all_degree_cases': rows,
              'larger_level_cases': large,
              'holomorphic_meridian_tube_cases': holomorphic,
              'scope': 'Literal two-head Ward current and its exact charges; no simultaneous many-head or geometric source comparison asserted.'}
    output = Path(__file__).with_name('actual_two_head_ward_contraction_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'actual_all_degree_cases': len(rows),
                      'larger_level_cases': len(large),
                      'holomorphic_meridian_tube_cases': len(holomorphic),
                      'minimum_ratio_to_proved_bound': min(r['ratio_to_bound'] for r in rows + large),
                      'maximum_spectral_error': max(r['spectral_error'] for r in rows + large)}, indent=2))


if __name__ == '__main__':
    main()
