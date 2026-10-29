#!/usr/bin/env python3
"""Exact physical all-channel CD normalization and whole-black magnetic tests.

Finite checks supplement the written covariance/ordinary-module proof.
The growing-level magnitude calibrations use the proved exact odd source.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_trivalent_complete_circle_vertex_kernel import data, vertex_formula


def ordinary(j, q, p):
    n, Q = 2*j+1, q*q % p
    E = np.zeros((n, n), dtype=np.int64)
    F = E.copy()
    K = np.diag([pow(q, 2*j, p)*pow(Q, -r, p) % p for r in range(n)])
    for r in range(1, n):
        E[r-1, r] = pow(q, -2*j-1, p)*(1-pow(Q, 2*j+1-r, p)) % p
        F[r, r-1] = (1-pow(Q, r, p)) % p
    return E, F, K


def physical_columns(N, q, p):
    d, Q = N-1, q*q % p
    x = pow(q, d, p)
    E = np.diag([(pow(Q, -a, p)-1) % p for a in range(1, N)], 1)
    F = np.diag([(1-pow(Q, a, p)) % p for a in range(1, N)], -1)
    K = np.diag([x*pow(Q, -a, p) % p for a in range(N)])
    Et, Ft, Kt = coproduct(E, F, K, 2, N, p)
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    out = {}
    for j in range(d//2+1):
        t = d-j
        W = np.zeros((N*N, 2*j+1), dtype=np.int64)
        for a in range(t+1):
            W[a*N+t-a, 0] = pow(q, a*a, p)*fac[t]*pow(fac[a]*fac[t-a], -1, p) % p
        for r in range(1, 2*j+1):
            W[:, r] = Ft@W[:, r-1] % p*pow(1-pow(Q, r, p), -1, p) % p
        out[j] = W
    return out, fac, (Et, Ft, Kt)


def axis(A, value, index, p):
    moved = np.moveaxis(value, index, 0)
    result = np.tensordot(A, moved, axes=(1, 0)) % p
    return np.moveaxis(result, 0, index)


def triple_action(value, modules, kind, p):
    result = np.zeros_like(value)
    for active in range(3):
        term = value.copy()
        for index, (E, F, K) in enumerate(modules):
            I = np.eye(len(E), dtype=np.int64)
            Ki = np.diag([pow(int(k), -1, p) for k in np.diag(K)])
            matrix = (E if index == active else K if index > active else I) if kind == 'E' else (F if index == active else Ki if index < active else I)
            term = axis(matrix, term, index, p)
        result = (result+term) % p
    return result


def canonical_three_j(js, modules, q, p):
    j1, j2, j3 = js
    J = sum(js)
    E1, F1, K1 = modules[0]
    E2, F2, K2 = modules[1]
    E3, F3, K3 = modules[2]
    n1, n2, n3 = [2*j+1 for j in js]
    Q = q*q % p
    E12 = (np.kron(E1, K2)+np.kron(np.eye(n1, dtype=np.int64), E2)) % p
    current = np.zeros((n1, n2), dtype=np.int64)
    current[2*j1, J-2*j1] = 1
    for a in range(2*j1-1, max(0, J-2*j2)-1, -1):
        ratio = -int(K1[a+1, a+1])*(1-pow(Q, a+1, p))*pow(1-pow(Q, J-a, p), -1, p) % p
        current[a, J-a] = int(current[a+1, J-a-1])*pow(ratio, -1, p) % p
    theta = np.zeros((n1, n2, n3), dtype=np.int64)
    theta[:, :, 0] = current
    for r in range(1, n3):
        current = (-int(K3[r-1, r-1])*pow(int(E3[r-1, r]), -1, p))*(E12@current.reshape(-1) % p) % p
        current = current.reshape(n1, n2)
        theta[:, :, r] = current
    assert not np.any(triple_action(theta, modules, 'E', p))
    assert not np.any(triple_action(theta, modules, 'F', p))
    return theta


def exact_level(N):
    values = data(N)
    p, q, x, R, Ri, L, P, labels, V, Vbar, weights, phases = values
    _, eta, _, *_ = balanced_data(N)
    d, M, Q = N-1, (N-1)//2, q*q % p
    actual, fac, (Et, Ft, Kt) = physical_columns(N, q, p)
    bars, _, _ = physical_columns(N, pow(q, -1, p), p)
    imag = pow(eta, N, p)
    sine = [pow(imag, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p for a in range(N)]
    lookup = {label: i for i, label in enumerate(labels)}
    metrics, all_labels, all_bars, offsets = {}, [], [], {}
    degree_checks = 0
    for j in range(M+1):
        W, Wb = actual[j], bars[j]
        modules = ordinary(j, q, p)
        for physical, single in zip((Et, Ft, Kt), modules):
            assert np.array_equal(physical@W % p, W@single % p)
        G = np.array([sine[2*j]*pow(sine[r]*sine[2*j-r], -1, p) % p for r in range(2*j+1)], dtype=np.int64)
        metrics[j] = G
        h0 = N if 2*j == d else 2*sine[d-j]**2*pow(sine[d-2*j], -1, p) % p
        if 2*j < d:
            assert h0 == 2*N*sine[2*j]*pow(sine[j]**2, -1, p) % p
        pi = np.array([pow(int(g), -1, p) for g in G])[:, None]*Wb.T % p@P % p
        for physical, single in zip((Et, Ft, Kt), modules):
            assert np.array_equal(pi@physical % p, single@pi % p)
        target = np.eye(2*j+1, dtype=np.int64) if 2*j == d else np.zeros((2*j+1, 2*j+1), dtype=np.int64)
        assert np.array_equal(pi@W % p, target)
        offsets[j] = len(all_labels)
        for r in range(2*j+1):
            index = lookup[(d-j+r, j)]
            expected = h0*pow(int(G[r]), -1, p)*np.outer(W[:, r], Wb[:, r]) % p
            canonical = int(weights[index])*np.outer(V[:, index], Vbar[:, index]) % p
            assert np.array_equal(expected, canonical)
            all_labels.append((d-j+r, j))
            all_bars.append(Wb[:, r])
            degree_checks += 1
    U, _, _ = vertex_formula(N, x, p, all_labels, np.column_stack(all_bars))
    triples, forbidden, source_entries = 0, 0, 0
    for js in itertools.product(range(M+1), repeat=3):
        indices = [list(range(offsets[j], offsets[j]+2*j+1)) for j in js]
        block = U[np.ix_(*indices)].copy()
        J = sum(js)
        if J < d:
            assert not np.any(block)
            forbidden += 1
        triangle = all(js[i] <= sum(js)-js[i] for i in range(3))
        if not triangle:
            assert not np.any(block)
            continue
        for k, j in enumerate(js):
            shape = [1, 1, 1]
            shape[k] = 2*j+1
            block = block*np.array([pow(int(g), -1, p) for g in metrics[j]]).reshape(shape) % p
        modules = [ordinary(j, q, p) for j in js]
        theta = canonical_three_j(js, modules, q, p)
        coefficient = int(block[2*js[0], J-2*js[0], 0])
        assert np.array_equal(block, coefficient*theta % p)
        assert not np.any(triple_action(block, modules, 'E', p))
        assert not np.any(triple_action(block, modules, 'F', p))
        source_entries += block.size
        triples += 1
    magnetic = 0
    if N % 2:
        m = M
        z = np.array([sine[m]*pow(sine[k]*sine[m-k], -1, p) % p for k in range(m+1)], dtype=np.int64)
        A = pow(q, m*(2-m), p)*sum(int(a)**4 for a in z) % p
        for k in range(m+1):
            h = pow(q, k*k, p)*fac[m]*pow(fac[k]*fac[m-k], -1, p) % p
            got = int(U[offsets[m]+m+k, offsets[m]+d-k, offsets[m]])
            assert got == N**3*pow(q, -m*m, p)*A*h % p
            magnetic += 1
    return {'N': N, 'full_actual_CD_degree_checks': degree_checks,
            'whole_balanced_triangles': triples, 'source_forbidden_joint_blocks': forbidden,
            'whole_source_magnetic_entries_compared': source_entries,
            'exact_central_magnetic_growth_coefficients': magnetic}


def growth_profile(N):
    mp.mp.dps = 85
    m = (N-1)//2
    sines = [mp.mpf(1)]
    for a in range(1, m+1):
        sines.append(sines[-1]*2*mp.sin(mp.pi*a/N))
    betas = [sines[m]/sines[k]/sines[m-k] for k in range(m+1)]
    scalar = sum(b**4 for b in betas)
    coefficient = N**mp.mpf('4.5')*scalar*betas[m//2]
    j0 = 4*mp.catalan/mp.pi
    prediction = 2**mp.mpf('-2.25')*N**mp.mpf('2.5')*mp.exp(N*mp.mpf('1.25')*j0)
    ratio = coefficient/prediction
    assert abs(ratio-1) < 7/N
    return {'N': N, 'normalized_proved_magnetic_coefficient_prefactor': float(ratio),
            'scaled_N_error': float(N*abs(ratio-1)),
            'arithmetic': '85-digit positive exact-source magnitude calibration'}


if __name__ == '__main__':
    levels = [exact_level(N) for N in range(2, 10)]
    profiles = [growth_profile(N) for N in (33, 65, 129, 257)]
    result = {'status': 'PASS', 'exact_original_all_channel_levels': levels,
              'central_magnetic_growth_profiles': profiles,
              'scope': 'Full original all-degree CD factors and black 3j tensors, plus an unconditional magnetic-growth lower bound. No marked-white norm, full tensor rate limit or graph survival claim.'}
    Path(__file__).with_name('actual_trivalent_full_cd_normalization_and_magnetic_growth_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 8 exact all-channel CD/whole-black levels; 4 actual central magnetic-growth profiles')
