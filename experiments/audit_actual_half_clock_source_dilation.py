#!/usr/bin/env python3
"""Source-exact 2N dilation; original N, kappa and pivotal cut retained."""

import cmath
import json
from pathlib import Path

import numpy as np


def close(A, B, label, tol=2e-9):
    error = float(np.max(np.abs(np.asarray(A) - np.asarray(B))))
    scale = max(1.0, float(np.max(np.abs(np.asarray(B)))))
    assert error <= tol * scale, (label, error, scale)


def generators(N, copies):
    q = cmath.exp(1j * np.pi / N)
    Q, d = q * q, N - 1
    c, x = q - 1 / q, q**d
    size = copies * N
    J = np.arange(size)
    H = np.diag(d - 2 * J).astype(complex)
    T = np.diag(q**J)
    K = np.diag(x * Q**(-J))
    E, F = np.zeros((size, size), complex), np.zeros((size, size), complex)
    for j in range(size):
        if j % N:
            E[(j - 1) % size, j] = (Q**(-j) - 1) / c**2
        if j % N != d:
            F[(j + 1) % size, j] = 1 - Q**(j + 1)
    return q, Q, x, H, K, E, F, T


def universal_R(N, copies):
    q, Q, x, H, K, E, F, T = generators(N, copies)
    size, d = copies * N, N - 1
    h = np.diag(H)
    c = q - 1 / q
    R = np.zeros((size**2, size**2), complex)
    pref = 1.0 + 0j
    for k in range(N):
        if k:
            qnum = (q**k - q**(-k)) / c
            pref *= q**(k - 1) * c / qnum
        for a in range(size):
            if k > a % N:
                continue
            ea = 1.0 + 0j
            for j in range(k):
                ea *= E[a - j - 1, a - j]
            for b in range(size):
                if k > d - b % N:
                    continue
                fb = 1.0 + 0j
                for j in range(k):
                    fb *= F[b + j + 1, b + j]
                cartan = q**(h[a - k] * h[b + k] / 2)
                R[(b + k) * size + a - k, a * size + b] = pref * ea * fb * cartan
    return R


def original_factorial_R(N):
    q = cmath.exp(1j * np.pi / N)
    Q, d = q * q, N - 1
    x, kappa = q**d, q**(d * d / 2)
    factorial = [1.0 + 0j]
    for j in range(1, N):
        factorial.append(factorial[-1] * (1 - Q**j))
    R = np.zeros((N * N, N * N), complex)
    for a in range(N):
        for b in range(N):
            for k in range(min(a, d - b) + 1):
                coeff = (kappa * x**(-a - b + k) * Q**(b * (a - k))
                         * factorial[b + k] * factorial[a]
                         / (factorial[k] * factorial[b] * factorial[a - k]))
                R[(b + k) * N + a - k, a * N + b] = coeff
    return R


def cut_matrix(W, N, copies, width):
    size = N * copies
    q = cmath.exp(1j * np.pi / N)
    Q, x = q * q, q**(N - 1)
    g = np.array([x**(1 - N) * Q**(-(a % N)) for a in range(size)])
    C = np.zeros((N, N), complex)
    for a in range(N):
        for b in range(N):
            for env in np.ndindex(*([size] * (width - 1))):
                row = np.ravel_multi_index((a,) + env, [size] * width)
                col = np.ravel_multi_index((b,) + env, [size] * width)
                C[a, b] += np.prod([g[j] for j in env]) * W[row, col]
    return C


def word_matrix(R, size, word, width):
    Rinv = np.linalg.inv(R)
    I = np.eye(size)
    W = np.eye(size**width, dtype=complex)
    for letter in word:
        gate = R if letter > 0 else Rinv
        for _ in range(abs(letter) - 1):
            gate = np.kron(I, gate)
        for _ in range(width - abs(letter) - 1):
            gate = np.kron(gate, I)
        W = gate @ W
    return W


def local_case(N):
    q, Q, x, H, K, E, F, T = generators(N, 2)
    d, size = N - 1, 2 * N
    c = q - 1 / q
    q0, Q0, x0, H0, K0, E0, F0, T0 = generators(N, 1)
    for name, A, A0 in [("H", H, H0), ("K", K, K0), ("E", E, E0), ("F", F, F0)]:
        close(A[:N, :N], A0, name + " physical restriction")
        close(A[:N, N:], np.zeros((N, N)), name + " upper block")
        close(A[N:, :N], np.zeros((N, N)), name + " lower block")
    close(H[N:, N:], H0 - 2 * N * np.eye(N), "second unrolled color")
    close(E @ F - F @ E, (K - np.linalg.inv(K)) / c, "EF relation")
    close(H @ E - E @ H, 2 * E, "HE relation")
    close(H @ F - F @ H, -2 * F, "HF relation")
    close(np.linalg.matrix_power(E, N), np.zeros_like(E), "E nilpotency")
    close(np.linalg.matrix_power(F, N), np.zeros_like(F), "F nilpotency")

    # Original pairing C_{a,b}=x^a/N delta_{a+b,d}, copied blockwise.
    C = np.zeros((size, size), complex)
    for eps in range(2):
        for a in range(N):
            C[N * eps + a, N * eps + d - a] = x**a / N
    invCT = np.linalg.inv(C.T)
    dual_H = invCT @ (-H).T @ C.T
    dual_K = invCT @ np.linalg.inv(K).T @ C.T
    expected_Hdual = np.diag([d + 2 * N * (j // N) - 2 * (j % N)
                             for j in range(size)])
    close(dual_H, expected_Hdual, "genuine dual unrolled H")
    close(dual_K, K, "genuine dual K")
    dual_E = invCT @ (-E @ np.linalg.inv(K)).T @ C.T
    dual_F = invCT @ (-K @ F).T @ C.T
    close(dual_H @ dual_E - dual_E @ dual_H, 2 * dual_E, "dual HE")
    close(dual_H @ dual_F - dual_F @ dual_H, -2 * dual_F, "dual HF")
    cup = np.linalg.inv(C).reshape(-1)
    ev = C.reshape(-1)
    I = np.eye(size)
    close((np.kron(E, dual_K) + np.kron(I, dual_E)) @ cup,
          np.zeros(size * size), "original dual cup E Ward")
    close((np.kron(F, I) + np.kron(np.linalg.inv(K), dual_F)) @ cup,
          np.zeros(size * size), "original dual cup F Ward")
    close(ev @ (np.kron(dual_E, K) + np.kron(I, E)),
          np.zeros(size * size), "original dual cap E Ward")
    close(ev @ (np.kron(dual_F, I) + np.kron(np.linalg.inv(dual_K), F)),
          np.zeros(size * size), "original dual cap F Ward")
    close(np.kron(T, T) @ cup, q**d * cup, "cup full-clock charge")
    close(ev @ np.kron(T, T), q**d * ev, "cap full-clock charge")
    close(np.linalg.inv(C)[:N, :N], np.linalg.inv(C[:N, :N]), "original N turns")

    R, R0 = universal_R(N, 2), original_factorial_R(N)
    physical = [a * size + b for a in range(N) for b in range(N)]
    close(R[np.ix_(physical, physical)], R0, "full original kappa R")
    close(universal_R(N, 1), R0, "independent universal factorial R")
    close(R @ np.kron(T, T), np.kron(T, T) @ R, "2N charge crossing")
    h = np.diag(H)
    for eps in range(2):
        for eta in range(2):
            for a in range(N):
                for b in range(N):
                    full = q**(h[N * eps + a] * h[N * eta + b] / 2)
                    old = q**((d - 2 * a) * (d - 2 * b) / 2)
                    close(full, (-1)**(d * (eps + eta)) * old, "half-Cartan phase")

    fourier = np.array([[q**(r * a) / np.sqrt(size) for a in range(size)]
                        for r in range(size)])
    P0 = np.diag([1] * N + [0] * N)
    PF = fourier @ P0 @ fourier.conj().T
    expected = np.array([[sum(q**(a * (r - s)) for a in range(N)) / size
                          for s in range(size)] for r in range(size)])
    close(fourier @ fourier.conj().T, np.eye(size), "unitary 2N DFT")
    close(PF, expected, "retained Fourier physical window")
    close(PF @ PF, PF, "rank-N Fourier projector")
    close(np.trace(PF), N, "rank retained")

    # The OLD N-cyclic atom shift has a retained half-clock wall current.
    X = np.zeros((size, size), complex)
    for j in range(size):
        X[(j + 1) % size, j] = 1
    wall = np.diag([int(j in [d, size - 1]) for j in range(size)])
    Xback = np.linalg.matrix_power(X, 1 - N)
    Shat = X @ (np.eye(size) - wall) + Xback @ wall
    close(np.linalg.matrix_power(Shat, N), np.eye(size), "old cyclic order N")
    close(Shat.conj().T @ Shat, np.eye(size), "old cyclic unitary")
    close(T @ T @ Shat, Q * Shat @ T @ T, "old Q Weyl exact")
    close(T @ Shat - q * Shat @ T, -2 * q * Xback @ wall @ T,
          "retained half-clock wall current")
    assert np.linalg.matrix_rank(T @ Shat - q * Shat @ T, tol=1e-8) == 2

    # Original selected matrix cut, all other closed pivots retained.
    word_checks = 0
    for word in [[1], [1, 1, 1], [1, -1, 1], [-1, -1, -1]]:
        old = cut_matrix(word_matrix(R0, N, word, 2), N, 1, 2)
        full = cut_matrix(word_matrix(R, size, word, 2), N, 2, 2)
        close(full, old, f"original selected one-component source {word}", 2e-8)
        close(np.trace(full) / N, np.trace(old) / N, "original 1/N average")
        word_checks += 1
    return {"N": N, "signed_original_knot_sources": word_checks}


def main():
    cases = [local_case(N) for N in range(2, 8)]
    three_head = 0
    for N in [2, 3]:
        word = [1, -2, 1, -2]
        R0, RW = original_factorial_R(N), universal_R(N, 2)
        old = cut_matrix(word_matrix(R0, N, word, 3), N, 1, 3)
        full = cut_matrix(word_matrix(RW, 2 * N, word, 3), N, 2, 3)
        close(full, old, "original figure-eight full selected source", 3e-8)
        three_head += 1
    result = {"status": "PASS", "cases": cases,
              "three_head_original_sources": three_head,
              "source": "original kappa, N turns, closed pivots and P0/N cut retained",
              "scope": "complete-color dilation, not a geometric edge-character theorem"}
    Path(__file__).with_name("actual_half_clock_source_dilation_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(cases)} full half-clock/dual families; "
          f"{sum(c['signed_original_knot_sources'] for c in cases) + three_head} "
          "original signed one-component sources")


if __name__ == "__main__":
    main()
