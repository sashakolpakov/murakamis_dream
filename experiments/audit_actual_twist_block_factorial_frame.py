#!/usr/bin/env python3
"""Actual meridian-continuation fusion and bidiagonal projector formulas.

The generic-color R is evaluated from its defining finite sum, not from
the spectral formula being checked. All frame interfaces are retained.
"""

import json
from pathlib import Path

import numpy as np


def matrices(n, M):
    q = np.exp(1j * np.pi / n)
    Q, d = q * q, n - 1
    x = -M / q
    F = np.ones(n, complex)
    for a in range(1, n):
        F[a] = F[a - 1] * (1 - Q ** a)
    lower = np.zeros((n, n), complex)
    Ecal = np.zeros_like(lower)
    for a in range(1, n):
        lower[a, a - 1] = 1 - Q ** a
        Ecal[a - 1, a] = M * Q ** (-a) - 1 / M
    K = np.diag([x * Q ** (-a) for a in range(n)])
    I = np.eye(n)
    Ft = np.kron(lower, I) + np.kron(np.linalg.inv(K), lower)
    Et = np.kron(Ecal, K) + np.kron(I, Ecal)
    Kt = np.kron(K, K)
    Omega = Ft @ Et + q * Kt + (1 / q) * np.linalg.inv(Kt)
    R = np.zeros((n * n, n * n), complex)
    for a in range(n):
        for b in range(n):
            for h in range(min(a, d - b) + 1):
                e, c = a - h, b + h
                ep = np.prod([M * Q ** (-r) - 1 / M for r in range(e + 1, a + 1)])
                R[c * n + e, a * n + b] = (
                    (-1) ** h * q ** (h * h) * ep
                    * F[c] / (F[b] * F[h]) * x ** (-a - b) * Q ** (e * c))
    return q, Q, x, F, Omega, R


def block_frame(n, M, total):
    q, Q, x, F, Omega, R = matrices(n, M)
    d = n - 1
    labels = list(range(max(0, total - d), min(total, d) + 1))
    physical = [a * n + total - a for a in labels]
    size = len(labels)
    C = np.zeros((size, size), complex)
    Ci = np.zeros_like(C)
    H = np.zeros_like(C)
    for row, u in enumerate(labels):
        for col, a in enumerate(labels):
            if u <= a:
                C[row, col] = x ** (u - a) * F[total - u] / (F[a - u] * F[total - a])
                Ci[row, col] = C[row, col] * (-1) ** (a - u) * Q ** ((a - u) * (a - u - 1) // 2)
        j = total - u
        H[row, row] = (1 / q) * M ** 2 * Q ** (-j) + q * M ** (-2) * Q ** j
        if row + 1 < size:
            H[row + 1, row] = (M * Q ** (-j) - 1 / M) * (1 - Q ** (u + 1))
    assert np.linalg.norm(C @ Ci - np.eye(size)) < 2e-8
    O = Omega[np.ix_(physical, physical)]
    B = R[np.ix_(physical, physical)]
    assert np.linalg.norm(O @ C - C @ H) < 3e-8
    assert np.linalg.norm(np.abs(C) - np.abs(Ci)) < 2e-8
    return q, Q, labels, C, Ci, H, B


def projector(n, M, total, labels, k):
    q = np.exp(1j * np.pi / n)
    Q = q * q
    size = len(labels)
    P = np.zeros((size, size), complex)
    def c(j):
        return (1 / q) * M ** 2 * Q ** (-j) + q * M ** (-2) * Q ** j
    for row, aout in enumerate(labels):
        for col, ain in enumerate(labels):
            if aout < ain:
                continue
            r, s = total - aout, total - ain
            if not r <= k <= s:
                continue
            numerator = np.prod([(M * Q ** (-j) - 1 / M) * (1 - Q ** (total - j + 1))
                                 for j in range(r + 1, s + 1)])
            denominator = np.prod([c(k) - c(j) for j in range(r, s + 1) if j != k])
            P[row, col] = numerator / denominator
            for j in range(r, s + 1):
                if j == k:
                    continue
                factored = (q * M ** (-2) * (Q ** k - Q ** j)
                            * (1 - M ** 4 * Q ** (-(k + j + 1))))
                assert abs(factored - (c(k) - c(j))) < 3e-12
            # There is at most one colliding factor; endpoints/self-pairs included.
            collisions = [j for j in range(r, s + 1) if j != k and (k + j + 1) % n == 0]
            assert len(collisions) <= 1
    return P


def run():
    rows = []
    for n in range(2, 10):
        for ell in (1, 3, -2):
            delta = 1 / (8 * n ** 3 * (1 + abs(ell)))
            M = 1 + delta * np.exp(.73j)
            for total in range(2 * n - 1):
                q, Q, labels, C, Ci, H, B = block_frame(n, M, total)
                size = len(labels)
                jlabels = [total - a for a in labels]
                projections = [projector(n, M, total, labels, j) for j in jlabels]
                assert np.linalg.norm(sum(projections) - np.eye(size)) < 3e-6
                developed = np.zeros_like(H)
                for j, P in zip(jlabels, projections):
                    node = q ** (-1) * M ** 2 * Q ** (-j) + q * M ** (-2) * Q ** j
                    assert np.linalg.norm(H @ P - node * P) < 3e-6
                    value = (-1) ** j * q ** (j * (j + 1)) * M ** (-2 * j)
                    developed += value ** ell * P
                original = np.linalg.matrix_power(B, ell)
                reconstructed = C @ developed @ Ci
                assert np.linalg.norm(original - reconstructed) < 2e-6 * max(1, np.linalg.norm(original))
                # Full original common Cartan continuation, kept explicitly.
                logM = np.log(M)
                kappa_ratio = np.exp((n - 1) * logM + logM ** 2 / (2j * np.pi / n))
                assert abs(kappa_ratio ** ell) < 2
                rows.append({'N': n, 'power': ell, 'degree': total,
                             'actual_generic_R_reconstructed': True,
                             'normalized_fusion_and_exact_inverse': True,
                             'bidiagonal_interval_projectors': True,
                             'one_collision_max_including_endpoints': True,
                             'original_Cartan_continuation_bounded': True})
    return rows


def main():
    result = {'status': 'PASS', 'families': run(),
              'scope': 'Actual factorial frame and meridian-circle projector identities; no volume equality.'}
    Path(__file__).with_name('actual_twist_block_factorial_frame_results.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'actual_signed_meridian_degree_families': len(result['families'])}))


if __name__ == '__main__':
    main()
