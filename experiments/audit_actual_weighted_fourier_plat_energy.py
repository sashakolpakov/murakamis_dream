#!/usr/bin/env python3
"""Original paired factorial gauges, dual Fourier metrics and doubled energy.

These are direct complex finite-matrix checks.  The norm limit of the
one-crossing curl is also covered by the already independently proved
uniform factorial theorem; its samples here are diagnostics only.
"""

import json
from pathlib import Path

import numpy as np


def data(n):
    q = np.exp(1j * np.pi / n)
    Q, d = q * q, n - 1
    x = -1 / q
    fac = np.ones(n, complex)
    for a in range(1, n):
        fac[a] = fac[a - 1] * (1 - Q ** a)
    pivot = np.array([x ** (1 - n) * Q ** (-a) for a in range(n)])
    # Literal positive complete crossing, with the common unit phase external.
    B = np.zeros((n * n, n * n), complex)
    for a in range(n):
        for b in range(n):
            for e in range(a + 1):
                c = a + b - e
                if c < n:
                    B[c * n + e, a * n + b] = (
                        x ** (-b - e) * Q ** (e * b)
                        * fac[c] * fac[a] / (fac[a - e] * fac[b] * fac[e]))
    F = np.array([[Q ** (r * a) / np.sqrt(n) for a in range(n)] for r in range(n)])
    return q, Q, x, fac, pivot, B, F


def close(W, pivot, n):
    return np.einsum('abcb,b->ac', W.reshape((n,) * 4), pivot)


def cases():
    rows = []
    rng = np.random.default_rng(34811)
    for n in range(2, 13):
        q, Q, x, fac, pivot, B, F = data(n)
        d = n - 1
        L = abs(fac) ** 2 / n
        Gamma = np.array([(-1) ** a * Q ** (-a * (a - 1) // 2) * fac[a] ** 2
                          for a in range(n)])
        assert np.max(abs(Gamma - Q ** np.arange(n) * abs(fac) ** 2)) < 2e-9
        assert np.max(abs(Gamma * Gamma[::-1] - n * n / Q)) < 2e-8
        assert np.max(abs(L * L[::-1] - 1)) < 1e-9
        cup = np.array([n * x ** (-b) if a + b == d else 0
                        for a in range(n) for b in range(n)], complex)
        cap = np.array([x ** b * pivot[a] / n if a + b == d else 0
                        for a in range(n) for b in range(n)], complex)
        marker = np.array([x ** b / n ** 2 for a in range(n) for b in range(n)])
        # Both strict physical turns, and the marked row on its actual charge.
        for t in (-1., -.31, .42, 1.):
            G = np.kron(L ** t, L ** t)
            assert np.linalg.norm(G * cup - cup) < 2e-8
            assert np.linalg.norm(cap / G - cap) < 2e-9
            supported = np.array([int(a + b == d) for a in range(n) for b in range(n)])
            assert np.linalg.norm((marker / G - marker) * supported) < 2e-9
            # The ordinary DFT has this exact POSITIVE non-flat dual metric.
            vec = rng.normal(size=n) + 1j * rng.normal(size=n)
            transformed = F @ (L ** t * vec)
            H = (F * L ** (-2 * t)) @ F.conj().T
            assert abs(np.vdot(transformed, H @ transformed) - np.vdot(vec, vec)) < 2e-6
            assert np.linalg.eigvalsh(H)[0] > 0
            # Actual R is symmetric. Same diagonal frame cannot reduce HS norm.
            Bt = G[:, None] * B / G[None, :]
            assert np.linalg.norm(Bt, 'fro') + 1e-9 >= np.linalg.norm(B, 'fro')
        assert np.linalg.norm(B - B.T) < 2e-8
        # Original zero-framed ADO curl: its residual twist is pivot[0].
        curl = B / pivot[0]
        C = close(curl, pivot, n)
        assert np.linalg.norm(C - np.eye(n)) < 2e-8
        curl_negative = np.linalg.inv(B) * pivot[0]
        assert np.linalg.norm(close(curl_negative, pivot, n) - np.eye(n)) < 2e-8
        left = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        right = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        for signed_curl in (curl, curl_negative):
            bounded = np.kron(left, np.eye(n)) @ signed_curl @ np.kron(right, np.eye(n))
            assert np.linalg.norm(close(bounded, pivot, n) - left @ right) < 3e-7
        free_energy = np.linalg.norm(curl, 'fro') ** 2
        probability = np.linalg.norm(C, 'fro') ** 2 / (n * free_energy)
        assert abs(probability * free_energy - 1) < 2e-9
        # Do not assume scalarity for the generic positive projection identity.
        W = rng.normal(size=(n * n, n * n)) + 1j * rng.normal(size=(n * n, n * n))
        Cw = close(W, pivot, n)
        grouped = W.reshape((n,) * 4).transpose(0, 2, 1, 3).reshape((n * n, n * n))
        hg = np.diag(pivot.conj()).reshape(n * n) / np.sqrt(n)
        selected = grouped @ hg.conj()
        assert abs(n * np.linalg.norm(selected) ** 2 - np.linalg.norm(Cw, 'fro') ** 2) < 1e-7
        # A unitary Fourier change of every closed half-edge preserves selection.
        U = np.kron(F, F)
        changed = grouped @ U.T
        source = U @ hg
        assert np.linalg.norm(changed @ source.conj() - selected) < 2e-8
        rows.append({'N': n, 'paired_factorial_turns_fixed': True,
                     'positive_dual_Fourier_metric': True,
                     'generic_nonscalar_doubled_source': True,
                     'curl_coherent_probability': float(probability),
                     'both_signed_curls_contracted_with_arbitrary_exterior': True,
                     'curl_negative_log_probability_over_N': float(-np.log(probability) / n),
                     'same_frame_diagonal_HS_minimum': True})
    return rows


def apply_gate(matrix, slot, state, n):
    shaped = state.reshape((n ** slot, n * n, n ** (2 - slot)))
    return np.einsum('ab,ibk->iak', matrix, shaped).reshape(n ** 4)


def whole_original_plats():
    rows = []
    for n in range(2, 6):
        q, Q, x, fac, pivot, B, F = data(n)
        d = n - 1
        L = abs(fac) ** 2 / n
        cup = np.array([n * x ** (-b) if a + b == d else 0
                        for a in range(n) for b in range(n)], complex)
        cap = np.array([x ** b * pivot[a] / n if a + b == d else 0
                        for a in range(n) for b in range(n)], complex)
        marker = np.array([x ** b / n ** 2 for a in range(n) for b in range(n)])
        ket = np.kron(cup, cup)
        uhat = ket / n ** 3
        gtop = np.kron(pivot, np.ones(n ** 3))
        phi = gtop.conj() * uhat
        Binv = np.linalg.inv(B)
        gbase = np.kron(np.kron(L, L), np.kron(L, L))
        for word in ([2], [2, -1, 2, 2]):
            state = ket.copy()
            for letter in word:
                state = apply_gate(B if letter > 0 else Binv, abs(letter) - 1, state, n)
            original = np.kron(cap, marker) @ state
            paired = n * np.vdot(phi, state / n ** 3)
            assert abs(original - paired) < 2e-6 * max(1, abs(original))
            # Independent endpoint source gauges, arbitrary interior gauges.
            gauges = [gbase ** .4]
            basis = np.array(list(np.ndindex((n,) * 4)))
            for j in range(1, len(word)):
                s = np.sin(np.arange(4) + .37 * j)
                gauges.append(np.exp((basis @ s) / (2 * n)))
            gauges.append(gbase ** (-.2))
            assert np.linalg.norm(gauges[0] * uhat - uhat) < 2e-9
            assert np.linalg.norm(gauges[-1] * phi - phi) < 2e-9
            transformed = gauges[0] * uhat
            bound = 1.
            for j, letter in enumerate(word):
                gate = B if letter > 0 else Binv
                slot = abs(letter) - 1
                transformed = gauges[j + 1] * apply_gate(gate, slot, transformed / gauges[j], n)
                full = np.kron(np.eye(n ** slot), np.kron(gate, np.eye(n ** (2 - slot))))
                scaled = gauges[j + 1][:, None] * full / gauges[j][None, :]
                bound *= np.linalg.norm(scaled, 'fro')
            answer = np.vdot(phi, transformed)
            assert abs(n * answer - original) < 2e-6 * max(1, abs(original))
            assert abs(answer) <= bound * (1 + 1e-10)
            rows.append({'N': n, 'word': word,
                         'entire_original_marked_plat_preserved': True,
                         'independent_paired_endpoint_and_arbitrary_interior_gauges': True,
                         'positive_block_energy_bound': True})
    return rows


def main():
    result = {'status': 'PASS', 'cases': cases(), 'whole_original_plats': whole_original_plats(),
              'scope': 'Exact source-preserving weighted Fourier and positive sewing; no sharp knot-volume estimate.'}
    Path(__file__).with_name('actual_weighted_fourier_plat_energy_results.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print('PASS 11 levels and 8 whole original plats: paired factorial turns, dual Fourier metrics, positive gauged block bounds, nonscalar doubled source and exact curl probability')


if __name__ == '__main__':
    main()
