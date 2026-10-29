#!/usr/bin/env python3
"""Exact finite packet phases, mixed-copy Gram and actual-source energy."""

import cmath
import json
from pathlib import Path

import numpy as np

from audit_actual_half_clock_source_dilation import original_factorial_R


def close(A, B, label, tol=5e-8):
    scale = max(1., float(np.max(np.abs(B))))
    assert float(np.max(np.abs(A - B))) <= tol * scale, label


def local_data(N):
    q = cmath.exp(1j * np.pi / N)
    Q, x, d = q * q, -1 / q, N - 1
    F = [1. + 0j]
    for a in range(1, N):
        F.append(F[-1] * (1 - Q**a))
    s = np.abs(F)
    C, Ci = np.zeros((N * N, N * N), complex), np.zeros((N * N, N * N), complex)
    for a in range(N):
        for b in range(N):
            for r in range(min(a, d - b) + 1):
                z = x**(-r) * F[b + r] / (F[r] * F[b])
                row, col = (a - r) * N + b + r, a * N + b
                C[row, col] = z
                Ci[row, col] = (-1)**r * Q**(r * (r - 1) // 2) * z
    close(C @ Ci, np.eye(N * N), "literal inverse")
    B = np.diag(N**.25 / np.sqrt(s))
    BB = np.kron(B, B)
    return q, Q, x, np.asarray(F), s, C, Ci, B, BB


def packet_case(N):
    q, Q, x, F, s, C, Ci, B, BB = local_data(N)
    d = N - 1
    A = np.kron(np.eye(N), Ci) @ np.kron(C, np.eye(N))
    BBB = np.kron(BB, B)
    Ah = BBB @ A @ np.linalg.inv(BBB)
    expected = np.zeros_like(Ah)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                col = (a * N + b) * N + c
                for r in range(min(a, d - b) + 1):
                    for t in range(min(b + r, d - c) + 1):
                        triples = [(r, a - r, d - a), (r, b, d - b - r),
                                   (t, b + r - t, d - b - r), (t, c, d - c - t)]
                        w = np.prod([1 / np.prod([s[j] for j in tri]) for tri in triples])
                        row = ((a - r) * N + b + r - t) * N + c + t
                        expected[row, col] = q**(r * (b - d) + t * (c + t)) * N**2 * np.sqrt(w)
    close(Ah, expected, "complete phase/four ONE-power weights")

    # This trace is an actual positive doubled-energy trace; no claim is
    # made that an arbitrary coherent knot exterior can be traced out.
    rng = np.random.default_rng(7100 + N)
    v = rng.normal(size=N**3) + 1j * rng.normal(size=N**3)
    v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())
    output = Ah @ rho @ Ah.conj().T
    direct = np.einsum('ijkljm->iklm', output.reshape((N,) * 6)).reshape(N * N, N * N)
    kraus = [Ah.reshape(N, N, N, N**3)[:, M, :, :].reshape(N * N, N**3) for M in range(N)]
    reduced = sum(K @ rho @ K.conj().T for K in kraus)
    close(reduced, direct, "literal shared-head Kraus trace")
    for order, root in [(N, Q), (2 * N, q)]:
        transformed = [sum(root**(j * M) * kraus[M] for M in range(N)) / np.sqrt(order)
                       for j in range(order)]
        close(sum(K @ rho @ K.conj().T for K in transformed), direct,
              "coherent Fourier Plancherel Kraus sum")
    weights = rng.random(N**3) + .1
    lhs = Ah.conj().T @ np.diag(weights) @ Ah
    rhs = np.diag(N**2 * (np.abs(Ah)**2).T @ weights)
    diff = (rhs - lhs + (rhs - lhs).conj().T) / 2
    assert np.linalg.eigvalsh(diff).min() >= -2e-7 * max(1., np.linalg.norm(rhs, 2))
    return {"N": N, "full_actual_reassociation": True,
            "both_N_and_2N_shared_head_Fourier_traces": True,
            "diagonal_observable_operator_inequality": True}


def embed(A, first, width, N):
    ans = A
    for _ in range(first):
        ans = np.kron(np.eye(N), ans)
    for _ in range(width - first - 2):
        ans = np.kron(ans, np.eye(N))
    return ans


def original_plat_case(N, word):
    q, Q, x, F, s, C, Ci, B, BB = local_data(N)
    d, width, pairs = N - 1, 4, 2
    swap = np.zeros((N * N, N * N))
    for a in range(N):
        for b in range(N):
            swap[b * N + a, a * N + b] = 1
    C21, Ci21 = swap @ C @ swap, swap @ Ci @ swap
    gauss = np.kron(np.eye(N), np.diag([(-1)**b * Q**(b * (b - 1) // 2) * x**(-2 * b)
                                       for b in range(N)]))
    kappa = q**(d * d / 2)
    R = original_factorial_R(N)
    close(kappa * C @ gauss @ C21 @ Ci, R, "full kappa Euler/Gaussian crossing")
    Rinv = np.linalg.inv(R)
    close(C @ Ci21 @ np.linalg.inv(gauss) @ Ci / kappa, Rinv, "literal negative inverse")

    p, cap, marker = np.zeros(N * N, complex), np.zeros(N * N, complex), np.zeros(N * N, complex)
    g = np.asarray([x**(-d) * Q**(-a) for a in range(N)])
    for a in range(N):
        for b in range(N):
            marker[a * N + b] = x**b / N**2
            if a + b == d:
                p[a * N + b] = N * x**(-b)
                cap[a * N + b] = x**b * g[a] / N
    u = np.kron(p, p) / N**3
    piv = np.kron(np.kron(np.diag(g.conj()), np.eye(N)), np.eye(N * N))
    phi = piv @ u
    Bout = np.kron(BB, BB)
    close(Bout @ u, u, "whole original cup source fixed")
    close(Bout @ phi, phi, "whole pivoted cap source fixed")
    W = np.eye(N**width, dtype=complex)
    positive_path = np.abs(u)**2
    packet_steps = 0
    for letter in word:
        first = abs(letter) - 1
        W = embed(R if letter > 0 else Rinv, first, width, N) @ W
        gates = ([Ci, C21, gauss, C] if letter > 0
                 else [Ci, np.linalg.inv(gauss), Ci21, C])
        for j, gate in enumerate(gates):
            if (letter > 0 and j == 2) or (letter < 0 and j == 1):
                continue  # Exactly unit-modulus diagonal; path transfer is identity.
            gh = BB @ gate @ np.linalg.inv(BB)
            positive_path = embed(np.abs(gh)**2, first, width, N) @ positive_path
            packet_steps += 1
    literal = np.kron(cap, marker) @ W @ np.kron(p, p)
    amplitude = np.vdot(phi, W @ u)
    close(literal, N**(pairs - 1) * amplitude, "full original unrestricted marked source")
    support = np.asarray([int(a + b == d and c + e == d)
                          for a in range(N) for b in range(N) for c in range(N) for e in range(N)])
    Z = float(support @ positive_path)
    budget = N**(2 * pairs - 2 + packet_steps) * Z
    assert abs(literal)**2 <= budget * (1 + 1e-8)
    return {"N": N, "word": word, "original_marked_source_compared": True,
            "all_original_Cartan_and_pivots_retained": True,
            "positive_transfer_steps": packet_steps,
            "original_squared_scalar_before_common_chi": float(abs(literal)**2),
            "proved_positive_path_budget_before_common_chi": float(budget)}


def main():
    packets = [packet_case(N) for N in range(2, 6)]
    plats = [original_plat_case(N, word) for N in [2, 3]
             for word in [[2, -1, 2, 2], [1, -2, 3, -2]]]
    result = {"status": "PASS", "mixed_copy_Gram_and_shared_head": packets,
              "original_full_source_path_inequalities": plats,
              "scope": "exact coherent local identity and coarse full-source majorant; no geometric edge theorem"}
    Path(__file__).with_name("actual_doubled_reassociation_angle_transfer_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(packets)} exact mixed-copy/Fourier packet families; "
          f"{len(plats)} full original-source energy inequalities")


if __name__ == "__main__":
    main()
