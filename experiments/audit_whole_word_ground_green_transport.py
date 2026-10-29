#!/usr/bin/env python3
"""Signed clock transport, its actual ground metric, and the retained source."""

import itertools
import json
from pathlib import Path

import numpy as np


def shift(data, x, sign):
    rolled = np.roll(data, -1, axis=0)
    answer = np.zeros_like(data)
    if sign > 0:
        answer[:, :, 1:, 1:, :] = rolled[:, :, :-1, :-1, :] / x
    else:
        answer[:, 1:, :, :, 1:] = x * rolled[:, :-1, :, :, :-1]
    return answer


def green(data, x, sign):
    answer = np.array(data, copy=True)
    term = data
    for _ in range(1, data.shape[0]):
        term = shift(term, x, sign)
        answer += term
    return answer


def actual_families(N):
    q = np.exp(1j * np.pi / N)
    Q, x = q * q, -1 / q
    fac = np.ones(N, dtype=complex)
    for k in range(1, N):
        fac[k] = fac[k - 1] * (1 - Q ** k)
    C = np.zeros((N * N, N * N), dtype=complex)
    U = np.zeros_like(C)
    D = np.zeros_like(C)
    P = np.zeros_like(C)
    for a, b in itertools.product(range(N), repeat=2):
        col = a * N + b
        P[b * N + a, col] = 1
        D[col, col] = (-1) ** b * Q ** (b * (b - 1) // 2) * x ** (-2 * b)
        for u in range(a + 1):
            v = b + a - u
            if v < N:
                C[u * N + v, col] = x ** (u - a) * fac[a] * fac[v] / (fac[a-u] * fac[b])
        for h in range(min(N - 1 - a, b) + 1):
            U[(a+h) * N + b-h, col] = x ** (-h) / fac[h]
    Ci = np.linalg.inv(C)
    K = []
    H = np.zeros((N, N, N, N, N), dtype=complex)
    for m in range(N):
        clock = np.diag([Q ** (m*b) for a, b in itertools.product(range(N), repeat=2)])
        K.append((C @ D @ U @ clock @ Ci).reshape((N,) * 4))
        for a, b in itertools.product(range(N), repeat=2):
            if a+b >= N:
                continue
            # Exact zero detection keeps the root support explicit.
            if a+m >= N:
                continue
            poch = np.prod([1-Q ** (m+1+j) for j in range(a)])
            H[m, a+b, 0, a, b] = Q ** (m*b) * x ** (-b) * fac[a+b] / (fac[a]*fac[b]) * poch
    K = np.array(K)
    Km = np.array([(P @ z.reshape(N*N, N*N).conj() @ P).reshape((N,) * 4) for z in K])
    Hm = np.array([(P @ z.reshape(N*N, N*N).conj() @ P).reshape((N,) * 4) for z in H])
    return x, Q, K, H, Km, Hm


def local_checks():
    rows = []
    rng = np.random.default_rng(92547)
    for N in range(2, 10):
        x, Q, K, H, Km, Hm = actual_families(N)
        for sign, clocks, grounds in [(1, K, H), (-1, Km, Hm)]:
            error = np.linalg.norm(green(grounds, x, sign) - clocks) / max(1., np.linalg.norm(clocks))
            assert error < 2e-9, (N, sign, error)
            R = clocks[0].reshape(N*N, N*N)
            visible_error = abs(np.linalg.norm(grounds) / np.linalg.norm(R) - 1)
            assert visible_error < 2e-9, (N, sign, visible_error)
            assert np.linalg.norm(clocks) <= N * np.linalg.norm(R) * (1+2e-9)
            random = rng.normal(size=(N,)*5) + 1j*rng.normal(size=(N,)*5)
            transported = green(random, x, sign)
            assert np.linalg.norm(transported-shift(transported, x, sign)-random) < 2e-10*np.linalg.norm(random)
            assert np.linalg.norm(transported) <= N*np.linalg.norm(random)*(1+1e-12)
            nil = random
            for _ in range(N):
                nil = shift(nil, x, sign)
            assert not np.any(nil)
            rows.append({'N': N, 'sign': sign, 'actual_gate_relative_error': float(error),
                         'visible_support_metric_error': float(visible_error),
                         'all_clock_norm_ratio': float(np.linalg.norm(clocks)/np.linalg.norm(R))})
        inverse_error = np.linalg.norm(Km[0].reshape(N*N, N*N) @ K[0].reshape(N*N, N*N)-np.eye(N*N))
        assert inverse_error < 2e-8
    return rows


def matrix_green(N, x, sign):
    dim = N ** 5
    result = np.zeros((dim, dim), dtype=complex)
    for j in range(dim):
        unit = np.zeros(dim, dtype=complex)
        unit[j] = 1
        result[:, j] = green(unit.reshape((N,)*5), x, sign).ravel()
    return result


def whole_source_check():
    N = 2
    x, Q, Kp, Hp, Km, Hm = actual_families(N)
    Gp, Gm = matrix_green(N, x, 1), matrix_green(N, x, -1)
    G = np.kron(Gp, Gm)
    dim = N ** 5
    source = np.zeros((dim, dim), dtype=complex)
    # Literal selected first-head 0->0 and original pivotal closure
    # of heads 2,3, for word [1,-2]. Clock zero is retained at both cells.
    pivot = [(x*Q**(-a))**(1-N) for a in range(N)]
    for b, s, d in itertools.product(range(N), repeat=3):
        i = np.ravel_multi_index((0, 0, d, 0, b), (N,)*5)
        j = np.ravel_multi_index((0, b, s, d, s), (N,)*5)
        source[i, j] += pivot[b]*pivot[s]
    source = source.ravel()
    pulled = source @ G
    actual_h = np.kron(Hp.ravel(), Hm.ravel())
    actual_k = np.kron(Kp.ravel(), Km.ravel())
    assert np.linalg.norm(G @ actual_h-actual_k) < 2e-11
    assert abs(source @ actual_k-pulled @ actual_h) < 2e-11
    # Independently multiply the three-head physical operators.
    Rp, Rm = Kp[0].reshape(N*N, N*N), Km[0].reshape(N*N, N*N)
    word = np.kron(np.eye(N), Rm) @ np.kron(Rp, np.eye(N))
    direct = sum(pivot[b]*pivot[s]*word[b*N+s, b*N+s]
                 for b, s in itertools.product(range(N), repeat=2))
    assert abs(direct-source @ actual_k) < 2e-11
    rng = np.random.default_rng(1963)
    tensor = rng.normal(size=dim*dim)+1j*rng.normal(size=dim*dim)
    image = G @ tensor
    assert abs(source @ image-pulled @ tensor) < 2e-11
    norm_ratio = np.linalg.norm(pulled)/np.linalg.norm(source)
    assert 2**(-2)-1e-12 <= norm_ratio <= N**2+1e-12
    d_image = abs(source @ image)/np.linalg.norm(source)
    d_ground = abs(pulled @ tensor)/np.linalg.norm(pulled)
    assert 2**(-2)*d_ground-1e-11 <= d_image <= N**2*d_ground+1e-11
    # A nonzero vector in the actual transported source kernel remains
    # a zero period. This guards against turning conditioning into a
    # spurious scalar lower bound.
    in_kernel = tensor - (pulled @ tensor)*pulled.conj()/np.linalg.norm(pulled)**2
    assert np.linalg.norm(in_kernel) > 1
    assert abs(source @ (G @ in_kernel)) < 2e-11
    return {'N': N, 'word': [1, -2], 'original_selected_cut_and_pivot_equal': True,
            'nonfactorable_tensor_source_transport': True,
            'dual_source_norm_ratio': float(norm_ratio),
            'kernel_distance_bounds': True, 'nonzero_kernel_vector_retained': True}


def main():
    result = {'status': 'PASS', 'local_actual_clock_metric_cases': local_checks(),
              'whole_original_source': whole_source_check(),
              'scope': 'Complete-color signed ambient transport. No geometric source lower bound.'}
    Path(__file__).with_name('whole_word_ground_green_transport_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS sixteen actual signed clock/metric families and a whole original source, '
          'including nonfactorable ambient transport and retained cancellation kernel')


if __name__ == '__main__':
    main()
