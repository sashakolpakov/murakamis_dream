#!/usr/bin/env python3
"""Literal terminal projectors on complete original multiplicity modules."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import inverse_mod


def field_case(N, r=1):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d, b = q*q % prime, N-1, 2*r+1
    x = int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ecal = rho*rho*E % prime
    Ep, Fp, Kp = coproduct(Ecal, F, K, 2*r, N, prime)
    Eb, Fb, Kb = coproduct(Ecal, F, K, b, N, prime)
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    prefix_tuples = list(itertools.product(range(N), repeat=2*r))
    degrees = [sum(t) for t in prefix_tuples]
    ids = [i for i, degree in enumerate(degrees) if degree == r*d]
    dim = len(ids)
    seed = np.zeros((N**(2*r), dim), dtype=np.int64)
    seed[ids, np.arange(dim)] = 1
    H = np.zeros((N**b, dim), dtype=np.int64)
    power = seed.copy()
    for c in range(N):
        H[c::N, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = Ep @ power % prime
    highest_ids = [i*N for i in ids]
    assert np.array_equal(H[highest_ids, :], np.eye(dim, dtype=np.int64))
    D = H.copy()
    for _ in range(d):
        D = Fb @ D % prime
    D = D*pow(fac[d], -1, prime) % prime
    cup_pair = np.zeros(N*N, dtype=np.int64)
    cap_pair = np.zeros(N*N, dtype=np.int64)
    for j in range(N):
        cup_pair[j*N+d-j] = N*pow(x, j-d, prime) % prime
        cap_pair[j*N+d-j] = (pow(x, -j, prime)*pow(Q, -j, prime)
                                  *pow(N, -1, prime)) % prime
    cup_prefix = np.array([1], dtype=np.int64)
    cap_prefix = np.array([1], dtype=np.int64)
    for _ in range(r):
        cup_prefix = np.kron(cup_prefix, cup_pair) % prime
        cap_prefix = np.kron(cap_prefix, cap_pair) % prime
    w0, lam = cup_prefix[ids], cap_prefix[ids]
    ed = np.zeros(N, dtype=np.int64)
    ed[d] = 1
    cap = np.kron(cap_prefix, ed)
    Uphys = np.kron(np.eye(N**(b-2), dtype=np.int64), Rp@Rp % prime)
    Ured = (Uphys@H % prime)[highest_ids, :]
    assert np.array_equal(Uphys@H % prime, H@Ured % prime)
    assert np.array_equal(Uphys@D % prime, D@Ured % prime)
    row = cap@Uphys % prime
    T = np.zeros((N, dim), dtype=np.int64)
    for n in range(N):
        physical_ids = [i for i in range(N**b) if (i//N) % N == n]
        T[n, :] = row[physical_ids]@D[physical_ids, :] % prime
    assert np.array_equal(np.sum(T, axis=0) % prime, lam@Ured % prime)

    figure = None
    if r == 1:
        J = H[[j*N+d-j for j in range(N)], :]
        Ji = inverse_mod(J, prime)
        R1 = Rp[np.ix_(ids, ids)]
        I1 = Rm[np.ix_(ids, ids)]
        R2 = Ji@R1 % prime@J % prime
        incoming = I1@R2 % prime@w0 % prime
        expected = np.array([pow(-1, n, prime)*pow(Q, -n*(n+1)//2, prime)
                             *fac[n]**2 % prime for n in range(N)], dtype=np.int64)
        assert np.array_equal(T@incoming % prime, expected)
        assert int(lam@Ured % prime@incoming) % prime == int(np.sum(expected)) % prime
        figure = True
    else:
        # Unrelated original signed prefix; compare all terminal packet sums.
        Rfirst = np.kron(Rm, np.eye(N**(b-2), dtype=np.int64))
        Rlast = np.kron(np.eye(N**(b-2), dtype=np.int64), Rp)
        Wphys = Rlast@Rfirst % prime@Rlast % prime
        Wred = (Wphys@H % prime)[highest_ids, :]
        assert np.array_equal(Wphys@H % prime, H@Wred % prime)
        incoming = Wred@w0 % prime
        assert int(np.sum(T@incoming % prime)) % prime == int(lam@Ured % prime@incoming) % prime
    return {'N': N, 'plat_heads': 2*r+2, 'complete_dimension': dim,
            'every_input_column_terminal_source': True,
            'original_figure_eight_every_packet': figure}


def complex_case(N):
    d = N-1
    q = np.exp(1j*np.pi/N)
    Q, x = q*q, q**d
    fac = [1.+0j]
    for j in range(1, N):
        fac.append(fac[-1]*(1-Q**j))
    E, F = np.zeros((N, N), complex), np.zeros((N, N), complex)
    K = np.diag([x*Q**(-j) for j in range(N)])
    for j in range(1, N):
        E[j-1, j] = Q**(-j)-1
        F[j, j-1] = 1-Q**j
    I = np.eye(N)
    Ki = np.diag(1/np.diag(K))
    E2, F2, K2 = np.kron(E, K)+np.kron(I, E), np.kron(F, I)+np.kron(Ki, F), np.kron(K, K)
    F3 = np.kron(F2, I)+np.kron(np.diag(1/np.diag(K2)), F)
    ids = [j*N+d-j for j in range(N)]
    seed = np.zeros((N*N, N), complex)
    seed[ids, np.arange(N)] = 1
    H = np.zeros((N**3, N), complex)
    power = seed.copy()
    for c in range(N):
        H[c::N, :] = (-x*Q)**c/fac[c]*power
        power = E2@power
    D = H.copy()
    for _ in range(d):
        D = F3@D
    D /= fac[d]
    R = np.zeros((N*N, N*N), complex)
    kappa = q**(d*d/2)
    for a in range(N):
        for b in range(N):
            for k in range(min(a, d-b)+1):
                R[(b+k)*N+a-k, a*N+b] = (kappa*x**(-a-b+k)*Q**(b*(a-k))
                                      *fac[b+k]*fac[a]/(fac[k]*fac[b]*fac[a-k]))
    ell = np.array([x**(-j)*Q**(-j)/N for j in range(N)])
    cup = np.array([N*x**(j-d) for j in range(N)])
    cap = np.zeros(N**3, complex)
    cap[[j*N*N+(d-j)*N+d for j in range(N)]] = ell
    Uphys = np.kron(I, R@R)
    row = cap@Uphys
    T = np.zeros((N, N), complex)
    for n in range(N):
        physical_ids = [i for i in range(N**3) if (i//N) % N == n]
        T[n, :] = row[physical_ids]@D[physical_ids, :]
    J = H[[j*N+d-j for j in range(N)], :]
    R1 = R[np.ix_(ids, ids)]
    R2 = np.linalg.solve(J, R1@J)
    U = R2@R2
    incoming = np.linalg.solve(R1, R2@cup)
    expected = np.abs(fac)**2
    assert np.allclose(T@incoming, expected, rtol=3e-8, atol=3e-8)
    assert np.allclose(np.sum(T, axis=0), ell@U, rtol=3e-8, atol=3e-8)
    # Use a resolvable epsilon to check the all-epsilon positive completion.
    epsilon = .25
    G = T.conj().T@T+epsilon*I
    np.linalg.cholesky(G)
    a = np.sum(T, axis=0)
    dual = (a@np.linalg.solve(G, a.conj())).real
    assert dual <= N*(1+3e-8)
    v = np.array([np.exp(1j*j*j/7)/(j+1) for j in range(N)])
    energy = (v.conj()@G@v).real
    assert abs(a@v)**2 <= dual*energy*(1+3e-8)
    final = np.linalg.solve(U.conj().T, G)@np.linalg.inv(U)
    final_state = U@incoming
    assert np.allclose(final_state.conj()@final@final_state,
                       np.sum(expected**2)+epsilon*np.vdot(incoming, incoming), rtol=3e-8, atol=3e-8)
    return {'N': N, 'original_complex_packet_rows': True,
            'full_rank_positive_completion': True, 'terminal_dual_norm_squared': float(dual),
            'sharp_benchmark_energy_without_regularizer': float(np.sum(expected**2))}


if __name__ == '__main__':
    rows = [field_case(N) for N in range(2, 10)]
    rows += [field_case(2, 2), field_case(3, 2), field_case(2, 3)]
    complex_rows = [complex_case(N) for N in range(2, 8)]
    output = {'status': 'PASS', 'complete_original_modules': rows,
              'positive_completion': complex_rows,
              'scope': 'Sharp benchmark Gram on complete module; no broad-knot sharp energy assertion.'}
    Path(__file__).with_name('actual_terminal_packet_positive_gram_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print('PASS 11 complete terminal modules through eight plat heads; 8 exact figure-eight packet families; 6 positive full-module Grams')
