#!/usr/bin/env python3
"""Full one-wire Hermitian gauges for the literal original crossings."""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

from actual_convex_gauge_block_energy import wiring
from audit_actual_weighted_fourier_plat_energy import data


def densities(matrix, n):
    norm2 = np.linalg.norm(matrix, "fro") ** 2
    left = (matrix @ matrix.conj().T / norm2).reshape((n,) * 4)
    right = (matrix.conj().T @ matrix / norm2).reshape((n,) * 4)
    return (np.einsum("abcb->ac", right),
            np.einsum("abad->bd", right),
            np.einsum("abcb->ac", left),
            np.einsum("abad->bd", left))


def hermitian(rng, n):
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return .24 * (raw + raw.conj().T) / np.sqrt(n)


def run():
    rng = np.random.default_rng(290731)
    rows = []
    examples = [(4, [1, -2, 3, -2]),
                (6, [1, -2, 3, -4, 5, -4, 3, -2, 1])]
    for n in range(2, 8):
        q, Q, x, fac, pivot, positive, _ = data(n)
        negative = np.linalg.inv(positive)
        pair = {1: positive, -1: negative}
        rho = {sign: densities(R, n) for sign, R in pair.items()}
        for parts in rho.values():
            for part in parts:
                assert np.linalg.norm(part - np.diag(np.diag(part))) < 2e-10
            assert np.linalg.norm(parts[0] - parts[2]) < 2e-10
            assert np.linalg.norm(parts[1] - parts[3]) < 2e-10
        assert np.linalg.norm(rho[1][0] - rho[-1][1]) < 2e-10
        assert np.linalg.norm(np.diag(rho[1][0]) - np.diag(rho[1][1])[::-1]) < 2e-10

        cup = np.zeros((n, n), complex)
        for b in range(n):
            cup[n - 1 - b, b] = x ** (-b)
        ordinary = pivot.conj()[:, None] * cup

        for width, base_word in examples:
            for epsilon in (1, -1):
                word = [epsilon * letter for letter in base_word]
                count, vertices, bottom, top = wiring(width, word)
                assert not set(bottom).intersection(top)
                H = [hermitian(rng, n) for _ in range(count)]
                boundary_checks = []
                for boundary, is_top in ((bottom, False), (top, True)):
                    for j in range(0, width, 2):
                        U = ordinary if is_top and j else cup
                        odd, even = boundary[j:j + 2]
                        H[even] = -U.T @ H[odd].T @ U.conj()
                        assert np.linalg.norm(H[even] - H[even].conj().T) < 1e-12
                        boundary_checks.append((odd, even, U))

                derivative = 0.
                for vertex, letter in zip(vertices, word):
                    parts = rho[1 if letter > 0 else -1]
                    for leg, edge in enumerate(vertex):
                        derivative += (-1 if leg < 2 else 1) * np.trace(H[edge] @ parts[leg]).real
                assert abs(derivative) < 2e-9
                flat = len(word) * np.log(np.linalg.norm(positive, "fro"))
                ray = []
                for t in (-.6, -.2, .2, .6, 1.):
                    P = [expm(t * h) for h in H]
                    Pinv = [expm(-t * h) for h in H]
                    for odd, even, U in boundary_checks:
                        assert np.linalg.norm(P[odd] @ U @ P[even].T - U) < 2e-9
                    value = 0.
                    for vertex, letter in zip(vertices, word):
                        a, b, c, d = vertex
                        R = pair[1 if letter > 0 else -1]
                        transformed = np.kron(P[c], P[d]) @ R @ np.kron(Pinv[a], Pinv[b])
                        value += np.log(np.linalg.norm(transformed, "fro"))
                    assert value >= flat - 2e-9
                    ray.append({"t": t, "log_norm_excess": float(value - flat)})
                rows.append({"N": n, "width": width, "word": word,
                             "full_matrix_derivative_at_flat": float(derivative),
                             "original_endpoint_pairs_preserved": True,
                             "ray_checks": ray})
    return rows


if __name__ == "__main__":
    rows = run()
    target = Path(__file__).with_name("actual_full_matrix_wire_gauge_results.json")
    target.write_text(json.dumps({"families": rows,
                                 "scope": "Finite checks of the all-matrix ray proof; no geometric knot bound."},
                                indent=2) + "\n")
    print(f"PASS {len(rows)} full Hermitian wire-gauge families and {5 * len(rows)} original-source rays")
