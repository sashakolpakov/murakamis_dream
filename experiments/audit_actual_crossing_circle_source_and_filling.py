#!/usr/bin/env python3
"""Literal mixed crossing circles and full original twist/source reconstruction."""

import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct, word_matrix


def ordinary_module(j, q, prime):
    rho = (q-pow(q, -1, prime)) % prime
    number = lambda a: (pow(q, a, prime)-pow(q, -a, prime))*pow(rho, -1, prime) % prime
    E, F = np.zeros((j, j), dtype=np.int64), np.zeros((j, j), dtype=np.int64)
    for a in range(1, j):
        E[a-1, a] = number(a)*number(j-a) % prime
        F[a, a-1] = 1
    H = [j-1-2*a for a in range(j)]
    K = np.diag([pow(q, h, prime) for h in H]).astype(np.int64)
    return {'dim': j, 'E': E, 'F': F, 'H': H, 'K': K}


def mixed_check(A, B, q, eta, prime):
    a, b = A['dim'], B['dim']
    rho = (q-pow(q, -1, prime)) % prime
    I = np.eye(a*b, dtype=np.int64)
    nilpotent = I.copy()
    ep, fp, coefficient = np.eye(a, dtype=np.int64), np.eye(b, dtype=np.int64), 1
    for k in range(1, min(a, b)):
        ep, fp = ep@A['E'] % prime, B['F']@fp % prime
        number = (pow(q, k, prime)-pow(q, -k, prime))*pow(rho, -1, prime) % prime
        coefficient = coefficient*pow(q, k-1, prime)*rho*pow(number, -1, prime) % prime
        nilpotent = (nilpotent+coefficient*np.kron(ep, fp)) % prime
    cartan = np.array([pow(eta, ha*hb, prime) for ha in A['H'] for hb in B['H']], dtype=np.int64)
    uncheck = cartan[:, None]*nilpotent % prime
    check = np.zeros_like(uncheck)
    for u in range(a):
        for v in range(b):
            check[v*a+u, :] = uncheck[u*b+v, :]
    return check


def crossing_circle(target, auxiliary, q, eta, prime, level):
    modules = [target, target, auxiliary]
    total = target['dim']**2*auxiliary['dim']
    W = np.eye(total, dtype=np.int64)
    for place in [1, 0, 0, 1]:
        R = mixed_check(modules[place], modules[place+1], q, eta, prime)
        left = int(np.prod([M['dim'] for M in modules[:place]], dtype=np.int64))
        right = int(np.prod([M['dim'] for M in modules[place+2:]], dtype=np.int64))
        W = np.kron(np.eye(left, dtype=np.int64), np.kron(R, np.eye(right, dtype=np.int64)))@W % prime
        modules[place], modules[place+1] = modules[place+1], modules[place]
    N, j = target['dim'], auxiliary['dim']
    pivot = [pow(int(auxiliary['K'][a, a]), 1-level, prime) for a in range(j)]
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for row in range(N*N):
        for column in range(N*N):
            out[row, column] = sum(pivot[a]*int(W[row*j+a, column*j+a]) for a in range(j)) % prime
    return out


def power(A, exponent, prime, inverse=None):
    if exponent < 0:
        assert inverse is not None
        return power(inverse, -exponent, prime)
    value, factor = np.eye(len(A), dtype=np.int64), A.copy()
    while exponent:
        if exponent & 1:
            value = factor@value % prime
        factor = factor@factor % prime
        exponent //= 2
    return value


def filling_coefficients(N, q, Q, exponent, prime):
    d = N-1
    values, derivatives, nodes = [], [], []
    for k in range(N):
        nu = pow(-1, k, prime)*pow(q, k*(k+1), prime) % prime
        value = pow(nu, exponent, prime)
        values.append(value)
        derivatives.append((-exponent*(d-2*k)*value*pow(2, -1, prime)) % prime)
        nodes.append(pow(q, 2*k+1, prime))
    a = []
    for n in range(N):
        H = sum(values[k]*pow(nodes[k], -n, prime) for k in range(N))*pow(N, -1, prime) % prime
        D = sum(derivatives[k]*pow(nodes[k], -n, prime) for k in range(N))*pow(N, -1, prime) % prime
        a.append(H if n == 0 else (D+(N-n)*H)*pow(N, -1, prime) % prime)
    a += [0, 0]
    return [pow(-1, j-1, prime)*(a[j-1]-a[j+1]) % prime for j in range(1, N+1)]


def field_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % prime, int(K[0, 0]), int(Rp[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ec = rho*rho*E % prime
    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
    assert np.array_equal(mixed_check(target, target, q, eta, prime), Rp)
    Et, Ft, Kt = coproduct(Ec, F, K, 2, N, prime)
    Ki = np.diag([pow(int(a), -1, prime) for a in np.diag(Kt)])
    Omega = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(N*N, dtype=np.int64)
    U = [I, Omega]
    for k in range(2, N+1):
        U.append((Omega@U[-1]-U[-2]) % prime)
    loops = []
    for j in range(1, N+1):
        actual = crossing_circle(target, ordinary_module(j, q, prime), q, eta, prime, N)
        expected = pow(-1, j-1, prime)*U[j-1] % prime
        assert np.array_equal(actual, expected)
        loops.append(actual)
    # Full pair center polynomial, not only repeated eigenvalues.
    T0, T1 = 2*I % prime, Omega.copy()
    for k in range(2, N+1):
        T0, T1 = T1, (Omega@T1-T0) % prime
    assert not np.any((T1+2*I) % prime)
    LN = loops[-1]
    assert not np.any(LN[:, 0])
    ids = [a*N+d-a for a in range(N)]
    source = np.array([N*pow(x, a-d, prime) % prime for a in range(N)], dtype=np.int64)
    harmonics, H = [], 0
    for a in range(N):
        if a:
            H = (H+pow(1-pow(Q, a, prime), -1, prime)) % prime
        harmonics.append(H)
    mean = sum(harmonics)*pow(N, -1, prime) % prime
    normal = np.array([pow(-1, N+1, prime)*N*rho*pow(x, a-d, prime)*(harmonics[a]-mean) % prime
                       for a in range(N)], dtype=np.int64)
    Lmiddle = LN[np.ix_(ids, ids)]
    assert not np.any(Lmiddle@source % prime)
    assert np.array_equal(Lmiddle@normal % prime, 2*N*source % prime)
    if N % 2 == 0:
        assert not np.any(LN@LN % prime)
    else:
        projection = LN@LN % prime*pow(N*N, -1, prime) % prime
        assert np.array_equal(projection@projection % prime, projection)
        assert not np.any((Omega+2*I)@projection % prime)
        assert np.array_equal(LN@LN % prime@LN % prime, N*(LN@LN % prime) % prime)
    exponents = [-6, -2, 0, 2, 4, 10]
    all_coefficients = {}
    for exponent in exponents:
        coefficients = filling_coefficients(N, q, Q, exponent, prime)
        reconstructed = sum((int(a)*L for a, L in zip(coefficients, loops)), np.zeros_like(I)) % prime
        original = power(Rp, exponent, prime, inverse=Rm)*pow(kappa, -exponent, prime) % prime
        assert np.array_equal(reconstructed, original)
        all_coefficients[exponent] = coefficients
    whole = False
    if N <= 5:
        p, r = 1, -1
        word = [1, 1, -2, -2, 1, 2]
        W = word_matrix(word, Rp, Rm, 3, N, prime)
        weights = np.array([pivot[b]*pivot[c] % prime for a in range(N) for b in range(N) for c in range(N)], dtype=np.int64)
        # Original sole averaged marked cut, with its actual pivots.
        phi = lambda A: int(np.dot(weights, np.diag(A))) * pow(N, -1, prime) % prime
        alpha = kappa*pow(x, -d, prime) % prime
        chi = pow(alpha, -sum(1 if letter > 0 else -1 for letter in word), prime)
        original = chi*phi(W) % prime
        tail = np.kron(I[:N, :N], Rp)@np.kron(Rp, np.eye(N, dtype=np.int64)) % prime
        # Use literal embedded loop operators (each independently checked above).
        total = 0
        c1, c2 = all_coefficients[2*p], all_coefficients[2*r]
        for j in range(N):
            for k in range(N):
                A = tail@np.kron(np.eye(N, dtype=np.int64), loops[k]) % prime@np.kron(loops[j], np.eye(N, dtype=np.int64)) % prime
                total += c1[j]*c2[k]*phi(A)
        reconstructed = chi*pow(kappa, 2*p+2*r, prime)*total % prime
        assert reconstructed == original
        whole = True
    return {'N': N, 'literal_mixed_circle_colors': N,
            'complete_circle_kernel_and_parity': True, 'original_Hermite_source_normal': True,
            'signed_twist_exponents': exponents, 'whole_original_two_box_source': whole}


if __name__ == '__main__':
    result = {'status': 'PASS', 'original_circle_and_filling': [field_case(N) for N in range(2, 8)],
              'scope': 'Original mixed-color source/filling identities with full jets; no augmented geometric coefficient or survival theorem.'}
    Path(__file__).with_name('actual_crossing_circle_source_and_filling_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 6 original mixed-circle/source levels, 27 auxiliary colors, 36 signed twist reconstructions, 4 whole two-box sources')
