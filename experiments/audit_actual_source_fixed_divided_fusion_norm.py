#!/usr/bin/env python3
"""Current-inclusive actual fusion and its source-fixed factorial norm."""

import cmath
import itertools
import json
from pathlib import Path

import numpy as np


def close(A, B, name, tol=3e-8):
    scale = max(1.0, float(np.max(np.abs(B))))
    assert float(np.max(np.abs(A - B))) <= tol * scale, name


def data(N):
    q = cmath.exp(1j * np.pi / N)
    Q, x = q * q, -1 / q
    F = [1.0 + 0j]
    for a in range(1, N):
        F.append(F[-1] * (1 - Q**a))
    s = np.abs(F)
    E = np.zeros((N, N), complex)
    for a in range(1, N):
        E[a - 1, a] = Q**(-a) - 1
    K = np.diag([x * Q**(-a) for a in range(N)])
    G = np.diag(s / np.sqrt(N))
    return q, Q, x, np.asarray(F), s, E, K, G


def factorial_poly(X, F, z):
    P, power = np.eye(len(X), dtype=complex), np.eye(len(X), dtype=complex)
    for a in range(1, len(F)):
        power = power @ X
        P += z**a * power / F[a]
    return P


def pair_case(N):
    q, Q, x, F, s, E, K, G = data(N)
    I = np.eye(N)
    A, B = np.kron(E, K), np.kron(I, E)
    C = A + B
    GG = np.kron(G, G)
    invGG = np.linalg.inv(GG)
    close(A @ B, Q * B @ A, "actual q commutation")
    J = np.zeros_like(C)
    for a in range(1, N):
        J += N * (np.linalg.matrix_power(B, N - a) @ np.linalg.matrix_power(A, a)) / (F[a] * F[N - a])
    close(J @ J, np.zeros_like(J), "complete square-zero normal current")
    close(J @ C, C @ J, "total-current compatibility")
    R = sum(1 / (s[a] * s[N - a]) for a in range(1, N))
    exact_R = sum(1 / abs(1 - Q**a) for a in range(1, N)) / N
    assert abs(R - exact_R) < 1e-10
    harmonic_bound = sum(1 / a for a in range(1, N // 2 + 1)) / 2
    assert R <= harmonic_bound + 1e-10
    current_norm = np.linalg.norm(GG @ J @ invGG / N, 2)
    assert current_norm <= R + 1e-8

    # The literal original turns; no unrestricted marked-row identity is used.
    d = N - 1
    pivot = np.asarray([x**(1 - N) * Q**(-a) for a in range(N)])
    cup, cap = np.zeros(N * N, complex), np.zeros(N * N, complex)
    for a in range(N):
        b = d - a
        cup[a * N + b] = N * x**(-b)
        cap[a * N + b] = x**b * pivot[a] / N
    close(GG @ cup, cup, "original source cup fixed")
    close(cap @ invGG, cap, "original source cap fixed")

    t = cmath.exp((0.3 + 0.2j) / N)
    Theta = np.eye(N * N) + (-t)**N * J / N
    Theta_inv = np.eye(N * N) - (-t)**N * J / N
    close(Theta @ Theta_inv, np.eye(N * N), "retained inverse")
    left = factorial_poly(B, F, -t) @ factorial_poly(A, F, -t)
    packet = factorial_poly(C, F, -t)
    close(left, Theta @ packet, "complete actual factorial fusion")
    budget = 1 + abs(t)**N * R
    norms = [np.linalg.norm(GG @ X @ invGG, 2) for X in (Theta, Theta_inv)]
    assert max(norms) <= budget + 1e-7
    # Pulling back the physical factorial Gram by THIS total-current packet
    # preserves the adapter norm because the exact matrices commute.
    conjugated = GG @ packet @ Theta @ np.linalg.inv(packet) @ invGG
    close(conjugated, GG @ Theta @ invGG, "coherent packet Gram/current compatibility")
    return {"N": N, "actual_weighted_current_norm": float(current_norm),
            "proved_R_N_bound": float(R), "retained_adapter_norms": [float(z) for z in norms]}


def multihead_entry(N, b):
    q, Q, x, F, s, E, K, G = data(N)
    # Near-uniform tuple, total N; each entry <N for b>=2.
    a = [N // b] * b
    for j in range(N % b):
        a[j] += 1
    assert sum(a) == N and max(a) < N
    # Independent literal application of ordered coproduct monomial:
    # (E_b)^a_b ... (E_1 K_2...K_b)^a_1.
    raw = 1.0 + 0j
    for i in range(b):
        for r in range(1, a[i] + 1):
            raw *= Q**(-r) - 1
        for j in range(i + 1, b):
            raw *= (x * Q**(-a[j]))**a[i]
    raw /= np.prod([F[j] for j in a])
    weighted = abs(raw) * np.prod([1 / s[j] for j in a])
    predicted = np.prod([1 / s[j] for j in a])
    assert abs(abs(raw) - 1) < 2e-9
    assert abs(weighted / predicted - 1) < 2e-9
    return {"N": N, "physical_heads": b, "unique_input": a,
            "weighted_degree_N_entry": float(weighted)}


def overlap_case(N):
    q, Q, x, F, s, E, K, G = data(N)
    I = np.eye(N)
    A, B = np.kron(E, K), np.kron(I, E)
    J = np.zeros_like(A)
    for a in range(1, N):
        J += N * (np.linalg.matrix_power(B, N - a) @ np.linalg.matrix_power(A, a)) / (F[a] * F[N - a])
    J12, J23 = np.kron(J, I), np.kron(I, J)
    tags = [cmath.exp(z / N) for z in [.1 + .2j, -.2 + .1j, .3 - .2j]]
    factors = [np.eye(N**3) + (-tags[0])**N * J12 / N,
               np.eye(N**3) - (-tags[1])**N * J23 / N,
               np.eye(N**3) + (-tags[2])**N * J12 / N]
    U = factors[2] @ factors[1] @ factors[0]
    GG = np.kron(np.kron(G, G), G)
    R = sum(1 / (s[a] * s[N - a]) for a in range(1, N))
    budget = np.prod([1 + abs(t)**N * R for t in tags])
    norm = np.linalg.norm(GG @ U @ np.linalg.inv(GG), 2)
    assert norm <= budget + 1e-8
    tuples = 0
    for a in range(1, N):
        for b in range(1, N - a):
            c = N - a - b
            index = np.ravel_multi_index((a, b, c), (N,) * 3)
            assert abs(U[0, index]) < 1e-10
            tuples += 1
    assert tuples
    return {"N": N, "actual_overlapping_adapter_word_norm": float(norm),
            "proved_product_bound": float(budget),
            "positive_degree_N_inputs_excluded_from_bare_pair_words": tuples}


def neighboring_packet_interface(N):
    assert N % 4 == 0
    k = N // 4
    q, Q, x, F, s, E, K, G = data(N)
    I = np.eye(N)
    A, B = np.kron(E, K), np.kron(I, E)
    J = np.zeros_like(A)
    for a in range(1, N):
        J += N * (np.linalg.matrix_power(B, N - a) @ np.linalg.matrix_power(A, a)) / (F[a] * F[N - a])
    # EXACT restriction of the full actual P23 to head3=0.
    P = np.kron(I, factorial_poly(E, F, x))
    Pinv = np.kron(I, np.eye(N, dtype=complex))
    power = np.eye(N, dtype=complex)
    inverse_one = np.eye(N, dtype=complex)
    for r in range(1, N):
        power = power @ E
        inverse_one += (-1)**r * Q**(r * (r - 1) // 2) * x**r * power / F[r]
    Pinv = np.kron(I, inverse_one)
    close(P @ Pinv, np.eye(N * N), "literal neighboring packet/inverse")
    GG = np.kron(G, G)
    transformed = GG @ P @ (J / N) @ Pinv @ np.linalg.inv(GG)
    a, h = 2 * k, k
    b = N - a + h
    actual = abs(transformed[0, a * N + b])
    gaussian_mod = s[a + h - 1] / (s[h] * s[a - 1])
    predicted = gaussian_mod / (s[a] * s[N - a])
    angle_weight = 1 / (s[k] * s[2 * k - 1] * s[k])
    assert abs(actual / predicted - 1) < 2e-8
    assert abs(predicted / (angle_weight / 2) - 1) < 2e-9
    return {"N": N, "literal_actual_current_packet_entry": float(actual),
            "positive_affine_angle_indices": [k, 2 * k - 1, k],
            "half_angle_energy_weight": float(angle_weight / 2)}


def main():
    pairs = [pair_case(N) for N in range(2, 10)]
    multi = [multihead_entry(N, b) for N in [4, 7, 10, 13] for b in [2, 3, 4]]
    overlaps = [overlap_case(N) for N in [3, 4, 5]]
    interfaces = [neighboring_packet_interface(N) for N in [4, 8, 12]]
    result = {"status": "PASS", "two_head_current_inclusive_fusions": pairs,
              "actual_multihead_unique_entries": multi,
              "overlapping_physical_pairs_and_exact_nongeneration": overlaps,
              "neighboring_packet_current_angle_interface": interfaces,
              "scope": "physical source-fixed metric; no length-register identification or global volume bound"}
    Path(__file__).with_name("actual_source_fixed_divided_fusion_norm_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(pairs)} actual current-inclusive two-head operators; "
          f"{len(multi)} exact multihead normal-entry profiles; {len(overlaps)} overlapping words; "
          f"{len(interfaces)} actual neighboring packet interfaces")


if __name__ == "__main__":
    main()
