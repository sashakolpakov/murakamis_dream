#!/usr/bin/env python3
"""Whole actual cap/cup-A contractions, all original source constants."""

import cmath
import json
from pathlib import Path

import numpy as np


def close(A, B, label, tol=3e-8):
    scale = max(1.0, float(np.max(np.abs(B))))
    error = float(np.max(np.abs(A - B)))
    assert error <= tol * scale, (label, error, scale)


def case(N):
    q = cmath.exp(1j * np.pi / N)
    Q, d, x = q * q, N - 1, -1 / q
    F = [1.0 + 0j]
    for a in range(1, N):
        F.append(F[-1] * (1 - Q**a))
    s = np.abs(F)
    B = np.diag([N**.25 / np.sqrt(z) for z in s])
    BB, BBB = np.kron(B, B), np.kron(np.kron(B, B), B)
    binom = lambda n, r: F[n] / (F[r] * F[n - r])

    # Literal physical Borel fusion divided by its ORIGINAL input F_a,
    # independently compared with the complete nilpotent Euler inverse.
    Cfusion = np.zeros((N * N, N * N), complex)
    Cprime, V = np.zeros_like(Cfusion), np.zeros_like(Cfusion)
    for a in range(N):
        for b in range(N):
            for r in range(min(a, d - b) + 1):
                u, v = a - r, b + r
                col, row = a * N + b, u * N + v
                Cfusion[row, col] = x**(-r) * F[a] * F[v] / (F[r] * F[b])
                Cprime[row, col] = x**(-r) * binom(v, r)
            if a and b < d:
                V[(a - 1) * N + b + 1, a * N + b] = x**(-1) * (1 - Q**(b + 1))
    close(Cfusion @ np.kron(np.diag([1 / z for z in F]), np.eye(N)),
          Cprime, "actual primed fusion typing")
    Ci, power = np.eye(N * N, dtype=complex), np.eye(N * N, dtype=complex)
    for r in range(1, N):
        power = power @ V
        Ci += (-1)**r * Q**(r * (r - 1) // 2) * power / F[r]
    close(Ci @ Cprime, np.eye(N * N), "full finite inverse")
    A = np.kron(np.eye(N), Ci) @ np.kron(Cprime, np.eye(N))
    Ai = np.kron(Ci, np.eye(N)) @ np.kron(np.eye(N), Cprime)
    close(A @ Ai, np.eye(N**3), "full reassociation inverse")

    p, ell, marker = np.zeros(N * N, complex), np.zeros(N * N, complex), np.zeros(N * N, complex)
    for u in range(N):
        for v in range(N):
            marker[u * N + v] = x**v / N**2
            if u + v == d:
                p[u * N + v] = N * x**(-v)
                pivot = x**(-d) * Q**(-u)
                ell[u * N + v] = x**v * pivot / N
    phat, ellhat = p / N**1.5, np.sqrt(N) * ell
    close(BB @ phat, phat, "original cup source gauge fixed")
    close(ellhat @ np.linalg.inv(BB), ellhat, "original ordinary cap gauge fixed")
    close(np.vdot(phat, phat), 1, "normalized original cup")
    close(np.vdot(ellhat, ellhat), 1, "normalized original cap")

    Kraw = np.kron(ellhat.reshape(1, -1), np.eye(N)) @ A
    Jraw = Ai @ np.kron(phat.reshape(-1, 1), np.eye(N))
    Mraw = np.kron(marker.reshape(1, -1), np.eye(N)) @ A
    Kpred, Jpred, Mpred = np.zeros_like(Kraw), np.zeros_like(Jraw), np.zeros_like(Mraw)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                col = (a * N + b) * N + c
                if b == d and a + c <= d:
                    n = a + c
                    Kpred[n, col] = ((-1)**a * Q**(a * (a - 1) // 2 - a)
                                     * x**(-2 * a) * binom(n, a) / np.sqrt(N))
                for n in range(c, N):
                    transfer = n - c
                    lo, hi = max(0, transfer - b), min(a, d - b)
                    total = sum(binom(b + r, r) for r in range(lo, hi + 1))
                    Mpred[n, col] = ((-1)**transfer * Q**(transfer * (transfer - 1) // 2)
                                     * x**(b - 2 * transfer) * binom(n, transfer) * total / N**2)
    for n in range(N):
        for a in range(n, N):
            c = n + d - a
            Jpred[(a * N) * N + c, n] = x**(2 * (a - d)) * binom(c, d - a) / np.sqrt(N)
    close(Kraw, Kpred, "complete ordinary cap coherent collapse")
    close(Jraw, Jpred, "complete inverse packet cup collapse")
    close(Mraw, Mpred, "unrestricted original marked current retained")

    Khat = B @ Kraw @ np.linalg.inv(BBB)
    Jhat = BBB @ Jraw @ np.linalg.inv(B)
    Kangle = np.zeros_like(Khat)
    R = np.zeros(N)
    Z = 0.
    for n in range(N):
        for a in range(n + 1):
            c = n - a
            weight = 1 / (s[a] * s[c] * s[d - n])
            col = (a * N + d) * N + c
            Kangle[n, col] = q**(a * (n - N - 1)) * np.sqrt(weight)
            R[n] += weight
            Z += weight
    close(Khat, Kangle, "full phase and ONE angle weight")
    close(Khat @ Khat.conj().T, np.diag(R), "exact cap output Gram")
    close(Jhat.conj().T @ Jhat, np.diag(R[::-1]), "exact cup input Gram")
    close(np.sum(np.abs(Khat)**2), Z, "one-simplex Hilbert Schmidt energy")
    close(np.sum(np.abs(Jhat)**2), Z, "dual one-simplex energy")
    active = [(a * N + d) * N + c for a in range(N) for c in range(N) if a + c <= d]
    gram = Khat[:, active].conj().T @ Khat[:, active]
    expected_gram = Kangle[:, active].conj().T @ Kangle[:, active]
    close(gram, expected_gram, "complete mixed-copy non-diagonal input Gram")
    # Literal original turn normalizers are restored, not replaced by units.
    literal_cap = np.kron(ell.reshape(1, -1), np.eye(N)) @ A
    literal_cup = Ai @ np.kron(p.reshape(-1, 1), np.eye(N))
    close(literal_cap, Kraw / np.sqrt(N), "literal original cap N factor")
    close(literal_cup, N**1.5 * Jraw, "literal original cup N factor")
    return {"N": N, "all_three_head_input_columns": N**3,
            "ordinary_top_and_cup_bottom_selection": True,
            "unrestricted_marked_packet_retained": True,
            "one_weight_energy": float(Z), "exact_boundary_operator_norm_squared": float(max(R))}


def main():
    rows = [case(N) for N in range(2, 9)]
    result = {"status": "PASS", "original_source_cap_cup_packets": rows,
              "scope": "all-exterior local matrix/source identities, not a whole-knot geometric bound"}
    Path(__file__).with_name("actual_pivotal_cap_reassociation_angle_packet_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(rows)} full original cap/cup/current packet families; "
          f"{sum(r['all_three_head_input_columns'] for r in rows)} three-head columns")


if __name__ == "__main__":
    main()
