#!/usr/bin/env python3
"""Exact original R and source in a scalar Euler/Gaussian kernel network."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_crossing_euler_completion import actual_data
from audit_actual_borel_regular_fusion import fusion
from audit_actual_two_cut_ports import word_matrix, partial


def local(N, M):
    data = actual_data(N, M)
    if data is None:
        return None
    p, q, x, K, pivot, plus, minus, twist, dimension, normalization = data
    Q = q*q % p
    fac = [1]
    for k in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, k, p)) % p)
    u = [pow(t, -1, p) for t in fac]
    v = [pow(-1, k, p)*pow(Q, k*(k-1)//2, p)*u[k] % p for k in range(N)]
    # Exact diagonal scalar kernels F_N(t)=N t^(N-1)v_N(Q/t).
    reflected = [N*v[N-1-k]*pow(Q, N-1-k, p) % p for k in range(N)]
    assert reflected == fac
    S = np.zeros((N, N), dtype=np.int64)
    for a in range(N-1):
        S[a+1, a] = 1
    Xm, Xp = np.kron(S.T, S), np.kron(S, S.T)

    def transfer(X, coefficients, raising_first):
        value, power = np.zeros_like(X), np.eye(N*N, dtype=np.int64)
        for k in range(N):
            value = (value+pow(x, -k, p)*coefficients[k]*power) % p
            power = power@X % p
        # Independently construct the CT projection kernel of (2).
        kernel = np.zeros_like(X)
        for a, b, k in itertools.product(range(N), repeat=3):
            c, d = (a+k, b-k) if raising_first else (a-k, b+k)
            if 0 <= c < N and 0 <= d < N:
                kernel[c*N+d, a*N+b] = pow(x, -k, p)*coefficients[k] % p
        assert np.array_equal(value, kernel)
        return value

    Um, Vm = transfer(Xm, u, False), transfer(Xm, v, False)
    Up, Vp = transfer(Xp, u, True), transfer(Xp, v, True)
    F1 = np.kron(np.diag(fac), np.eye(N, dtype=np.int64))
    F2 = np.kron(np.eye(N, dtype=np.int64), np.diag(fac))
    F1i = np.diag([pow(int(t), -1, p) for t in np.diag(F1)])
    F2i = np.diag([pow(int(t), -1, p) for t in np.diag(F2)])
    C = F2@Um@F1@F2i % p
    Ci = F2@F1i@Vm@F2i % p
    actual_fusion, actual_inverse, *_ = fusion(N, p, Q, [x, x], [0, 0])
    assert np.array_equal(C, actual_fusion)
    assert np.array_equal(Ci, actual_inverse)
    diagonal = [pow(-1, k, p)*pow(Q, k*(k-1)//2, p)*pow(x, -2*k, p) % p for k in range(N)]
    D = np.kron(np.eye(N, dtype=np.int64), np.diag(diagonal))
    Di = np.kron(np.eye(N, dtype=np.int64), np.diag([pow(d, -1, p) for d in diagonal]))
    kappa = int(plus[0, 0])
    reconstructed_plus = kappa*C@D@Up@Ci % p
    reconstructed_minus = pow(kappa, -1, p)*C@Vp@Di@Ci % p
    assert np.array_equal(reconstructed_plus, plus)
    assert np.array_equal(reconstructed_minus, minus)
    # Scalar projection kernels are finite, including their removable point.
    for t in (2, 3, 5):
        kernel = sum(pow(t, a, p) for a in range(N)) % p
        assert kernel == (1-pow(t, N, p))*pow(1-t, -1, p) % p
    gaussian_routes = []
    for k in range(N):
        projection = np.kron(np.eye(N, dtype=np.int64), np.diag([int(j == k) for j in range(N)]))
        gaussian_routes.append((kappa*diagonal[k]*C@projection@Up@Ci % p,
                                pow(kappa, -1, p)*pow(diagonal[k], -1, p)*C@Vp@projection@Ci % p))
    assert np.array_equal(sum((row[0] for row in gaussian_routes), np.zeros_like(plus)) % p, plus)
    assert np.array_equal(sum((row[1] for row in gaussian_routes), np.zeros_like(minus)) % p, minus)
    return {'N': N, 'M': M, 'p': p, 'pivot': pivot, 'plus': plus, 'minus': minus,
            'reconstructed_plus': reconstructed_plus, 'reconstructed_minus': reconstructed_minus,
            'twist': twist, 'dimension': dimension, 'routes': gaussian_routes,
            'normalization': normalization}


def source_case(row, strands, word, expand_gaussians=False):
    N, p, pivot = row['N'], row['p'], row['pivot']
    actual = word_matrix(word, row['plus'], row['minus'], strands, N, p)
    factorized = word_matrix(word, row['reconstructed_plus'], row['reconstructed_minus'], strands, N, p)
    original_cut = partial(actual, pivot, strands, N, p)
    scalar = int(original_cut.sum())*pow(N, -1, p) % p
    # The normalized-average source kernel in (4) contracts to this matrix row.
    source_value = int(partial(factorized, pivot, strands, N, p).sum())*pow(N, -1, p) % p
    assert source_value == scalar
    if expand_gaussians:
        route_value = 0
        for ks in itertools.product(range(N), repeat=len(word)):
            W = np.eye(N**strands, dtype=np.int64)
            for letter, k in zip(word, ks):
                pair = row['routes'][k][0 if letter > 0 else 1]
                slot = abs(letter)-1
                op = np.kron(np.kron(np.eye(N**slot, dtype=np.int64), pair),
                             np.eye(N**(strands-slot-2), dtype=np.int64))
                W = op@W % p
            route_value = (route_value+int(partial(W, pivot, strands, N, p).sum())*pow(N, -1, p)) % p
        assert route_value == scalar
    writhe = sum(1 if letter > 0 else -1 for letter in word)
    external = row['dimension']*pow(row['twist'], -writhe, p) % p
    return {'N': N, 'M': row['M'], 'strands': strands, 'word': list(word),
            'Cauchy_variables': strands*(10*len(word)+1),
            'Gaussian_indices': len(word),
            'Gaussian_route_expansion_checked': expand_gaussians,
            'original_full_period': scalar*external % p}


def main():
    local_rows = []
    words = []
    for N in range(2, 9):
        for M in (1, 3):
            row = local(N, M)
            if row is None:
                continue
            local_rows.append({'N': N, 'M': M, 'field': row['p'], 'original_normalization': row['normalization']})
            if N <= 4:
                words.append(source_case(row, 3, (1, -2, 1, -2), expand_gaussians=N <= 3))
            if N <= 3:
                words.append(source_case(row, 4, (1, 2, 3, -2, -1, 3)))
    result = {'status': 'PASS', 'local_cases': local_rows, 'word_cases': words,
              'scope': 'Exact original Euler/Gaussian Cauchy network and marked source; no geometric saddle noncancellation claim.'}
    Path(__file__).with_name('actual_euler_gaussian_cauchy_network_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'local_cases': len(local_rows), 'whole_word_cases': len(words),
                      'Gaussian_route_expansions': sum(r['Gaussian_route_expansion_checked'] for r in words)}))


if __name__ == '__main__':
    main()
