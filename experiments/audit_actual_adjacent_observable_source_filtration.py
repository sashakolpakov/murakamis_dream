#!/usr/bin/env python3
"""Actual interval-observable algebra, full source, and strict filtration."""

import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import inverse_mod, rank_mod


def power_mod(A, k, prime):
    out = np.eye(A.shape[0], dtype=np.int64)
    term = A.copy()
    while k:
        if k & 1:
            out = out@term % prime
        term = term@term % prime
        k >>= 1
    return out


def prime_level(N):
    return N >= 2 and all(N % j for j in range(2, int(N**.5)+1))


def actual_case(N):
    prime, eta, q, E, F, K, pivot, Rplus, Rminus = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    I = np.eye(N, dtype=np.int64)
    E2, F2, K2 = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    K2i = np.diag([pow(int(z), -1, prime) for z in np.diag(K2)])
    Omega2 = (F2@E2+q*K2+pow(q, -1, prime)*K2i) % prime
    ids = [j*N+d-j for j in range(N)]
    A = Omega2[np.ix_(ids, ids)]
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    seed = np.zeros((N*N, N), dtype=np.int64)
    seed[ids, np.arange(N)] = 1
    H = np.zeros((N**3, N), dtype=np.int64)
    epower = seed.copy()
    for c in range(N):
        H[c::N, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*epower % prime
        epower = E2@epower % prime
    highest_ids = [i*N for i in ids]
    J = H[[j*N+d-j for j in range(N)], :]
    Ji = inverse_mod(J, prime)

    # Actual physical Omega23 and R23, with no guessed recoupling relation.
    OH, RH = np.zeros_like(H), np.zeros_like(H)
    for a in range(N):
        block = slice(a*N*N, (a+1)*N*N)
        OH[block] = Omega2@H[block] % prime
        RH[block] = Rplus@H[block] % prime
    B, R2 = OH[highest_ids], RH[highest_ids]
    R1 = Rplus[np.ix_(ids, ids)]
    kappa = int(Rplus[0, 0])
    assert np.array_equal(B, Ji@A % prime@J % prime)
    assert np.array_equal(J@A % prime@Ji % prime, B.T)
    assert np.array_equal(R2, Ji@R1 % prime@J % prime)
    nodes = [(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime for j in range(N)]
    cstar = nodes[0]
    expected_B = np.diag(nodes)
    for j in range(1, N):
        expected_B[j-1, j] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    assert np.array_equal(B, expected_B)

    p = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    ell = np.array([pow(x, -j, prime)*pow(Q, -j, prime)*pow(N, -1, prime) % prime
                    for j in range(N)], dtype=np.int64)
    ed = np.zeros(N, dtype=np.int64)
    ed[d] = 1
    assert np.array_equal(J@p % prime, N*pow(x, -d, prime)*ed % prime)
    expected_row = np.zeros(N, dtype=np.int64)
    expected_row[0] = pow(x, d, prime)*pow(N, -1, prime) % prime
    assert np.array_equal(ell@Ji % prime, expected_row)
    assert int(ell@p) % prime == 0

    # The full c0 normal polynomial, including the N=2 empty product.
    Xi = (A-cstar*I) % prime
    Q0value = 1
    for j in range(1, d):
        Xi = Xi@(A-nodes[j]*I) % prime
        Q0value = Q0value*(cstar-nodes[j]) % prime
    assert Q0value == -N*N*pow(rho*rho % prime, -1, prime) % prime
    Xi = Xi*pow(Q0value, -1, prime) % prime
    theta = pow(-1, N, prime)*rho*rho % prime
    assert theta != 0
    assert np.array_equal(Xi, theta*np.outer(p, ell) % prime)
    assert rank_mod(Xi, prime) == 1
    assert not np.any(Xi@Xi % prime)

    # Construct both source Krylov bases, then every rank-one matrix generator.
    Bpowers = [I]
    for _ in range(d):
        Bpowers.append(Bpowers[-1]@B % prime)
    U = np.column_stack([bp@p % prime for bp in Bpowers])
    V = np.vstack([ell@bp % prime for bp in Bpowers])
    assert rank_mod(U, prime) == rank_mod(V, prime) == N
    for r in range(N):
        for s in range(N):
            assert np.array_equal(Bpowers[r]@Xi % prime@Bpowers[s] % prime,
                                  theta*np.outer(U[:, r], V[s, :]) % prime)
    Ui = inverse_mod(U, prime)
    Aflag = Ui@A % prime@U % prime
    assert not np.any(np.tril(Aflag, -1))
    assert np.array_equal(np.diag(Aflag), np.array(nodes))
    Bflag = Ui@B % prime@U % prime
    for j in range(d):
        expected = np.zeros(N, dtype=np.int64)
        expected[j+1] = 1
        assert np.array_equal(Bflag[:, j], expected)
    source_flag = ell@U % prime
    expected = np.zeros(N, dtype=np.int64)
    top = pow(-1, d, prime)*N*N % prime
    expected[d] = top
    assert np.array_equal(source_flag, expected)

    # Mixed words: arbitrary A powers cannot shorten the strict B traversal.
    mixed_checks = 0
    for count_B in (0, max(0, d-1), d):
        for choice in range(5):
            exponents = [(choice+2*j+j*j) % 4 for j in range(count_B+1)]
            word = power_mod(A, exponents[0], prime)
            for exponent in exponents[1:]:
                word = word@B % prime@power_mod(A, exponent, prime) % prime
            value = int(ell@word % prime@p) % prime
            expected = 0
            if count_B == d:
                expected = top
                for j, exponent in enumerate(exponents):
                    expected = expected*pow(nodes[j], exponent, prime) % prime
            assert value == expected
            mixed_checks += 1
    for r in range(1, d):
        value = int(ell@Bpowers[d-r] % prime@(A-cstar*I) % prime@Bpowers[r] % prime@p) % prime
        assert value == top*(nodes[r]-cstar) % prime
        assert value != 0

    # Literal full-Cartan crossing source and its polynomial top coefficient.
    r2p = R2@p % prime
    expected = np.array([kappa*int(p[j])*fac[d-j] % prime for j in range(N)])
    assert np.array_equal(r2p, expected)
    assert int(ell@r2p) % prime == kappa*pow(x, -d, prime) % prime
    retained_normal = int(ell@R2 % prime@Xi % prime@R2 % prime@p) % prime
    assert retained_normal == theta*pow(x, -d, prime) % prime
    assert retained_normal != 0
    coefficients = Ui@r2p % prime
    assert int(coefficients[d]) == kappa*pow(-1, d, prime)*pow(x, -d, prime)*pow(N*N, -1, prime) % prime
    reconstructed = sum((int(coefficients[j])*Bpowers[j] for j in range(N)), np.zeros_like(B)) % prime
    assert np.array_equal(reconstructed, R2)

    prime_word_checked = False
    if prime_level(N):
        e0 = np.zeros(N, dtype=np.int64)
        e0[0] = 1
        powers = [I]
        for _ in range(d):
            powers.append(powers[-1]@R1 % prime)
        Kword = np.column_stack([rp@e0 % prime for rp in powers])
        assert rank_mod(Kword, prime) == N
        inverse_polynomial = inverse_mod(Kword, prime)@(A@e0 % prime) % prime
        reconstructed_A = sum((int(inverse_polynomial[j])*powers[j] for j in range(N)), np.zeros_like(A)) % prime
        assert np.array_equal(reconstructed_A, A)
        prime_word_checked = True
    return {'N': N, 'original_coproduct_and_physical_chart': True,
            'source_normal_rank': 1, 'two_full_source_Krylov_bases': N,
            'actual_rank_one_observable_generators': N*N,
            'strict_source_filtration_and_mixed_words': mixed_checks,
            'original_crossing_top_degree': d,
            'normal_source_between_two_original_crossings': True,
            'prime_braid_word_recovery': prime_word_checked}


if __name__ == '__main__':
    rows = [actual_case(N) for N in range(2, 13)]
    rows.append(actual_case(14))
    result = {'status': 'PASS', 'complete_original_source_modules': rows,
              'scope': 'Exact adjacent observable algebra and N-scale source filtration; no microlocal norm claim.'}
    Path(__file__).with_name('actual_adjacent_observable_source_filtration_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 12 original complete source modules; all rank-one observable generators/strict filtrations; prime actual-braid recovery')
