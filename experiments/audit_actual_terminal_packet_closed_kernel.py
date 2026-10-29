#!/usr/bin/env python3
"""All-input terminal packet, independently from the original physical maps.

The field construction uses literal original E,F,K,R,caps, not the closed
kernel. Complex tests separately verify the three-port angle metric.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import inverse_mod, rank_mod


def field_case(N):
    prime, eta, q, E, F, K, pivot, R, Rminus = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ecal = rho*rho*E % prime
    E2, F2, K2 = coproduct(Ecal, F, K, 2, N, prime)
    E3, F3, K3 = coproduct(Ecal, F, K, 3, N, prime)
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    I = np.eye(N, dtype=np.int64)
    pair_ids = [j*N+d-j for j in range(N)]
    seed = np.zeros((N*N, N), dtype=np.int64)
    seed[pair_ids, np.arange(N)] = 1

    # Original complete highest intertwiner, followed by the actual total F.
    H = np.zeros((N**3, N), dtype=np.int64)
    power = seed.copy()
    for c in range(N):
        H[c::N, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = E2@power % prime
    D = H.copy()
    for _ in range(d):
        D = F3@D % prime
    D = D*pow(fac[d], -1, prime) % prime
    assert not np.any(F3@D % prime)

    # The cap and two checked crossings include the full common Cartan factor.
    kappa = int(R[0, 0])
    assert kappa*kappa % prime == pow(x, d, prime)
    cap = np.zeros(N**3, dtype=np.int64)
    for a in range(N):
        cap[(a*N+d-a)*N+d] = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
    row = cap@np.kron(I, R@R % prime) % prime
    actual = np.zeros((N, N), dtype=np.int64)
    for n in range(N):
        ids = [i for i in range(N**3) if (i//N) % N == n]
        actual[n, :] = row[ids]@D[ids, :] % prime

    # Whole lowest chart and Newton/Euler expression; no assumed eigenframe.
    last_d_ids = [(j*N+d-j)*N+d for j in range(N)]
    L = D[last_d_ids, :]
    R1 = R[np.ix_(pair_ids, pair_ids)]
    assert np.array_equal(L, pow(kappa, -1, prime)*R1 % prime)
    J = H[[j*N+d-j for j in range(N)], :]
    assert np.array_equal(J, J.T)
    phase_source = np.array([pow(x, j, prime) for j in range(N)], dtype=np.int64)
    ed = np.zeros(N, dtype=np.int64)
    ed[d] = 1
    assert np.array_equal(J@phase_source % prime, ed)
    assert np.array_equal(L[0, :], pow(x, -d, prime)*ed % prime)
    low = np.zeros_like(D)
    power = seed@L % prime
    for k in range(N):
        low[d-k::N, :] = power*pow(fac[k], -1, prime) % prime
        power = F2@power % prime
    assert np.array_equal(low, D)
    newton = np.zeros((N*N, N), dtype=np.int64)
    epower = seed.copy()
    for c in range(N):
        term = epower.copy()
        for _ in range(c):
            term = F2@term % prime
        scalar = (pow(-1, c, prime)*pow(q, c*(c+2), prime)
                  *pow(fac[c]**2 % prime, -1, prime)) % prime
        newton = (newton+scalar*term) % prime
        epower = E2@epower % prime
    assert np.array_equal(newton[pair_ids, :], L)

    # Exact forced-transfer coefficients of the final two-crossing tangle.
    for n in range(N):
        for a in range(N):
            c = 2*d-a-n
            if not 0 <= c < N:
                continue
            r = d-a
            expected = (pow(x, -n, prime)*pow(N, -1, prime)*pow(-1, n-r, prime)
                        *pow(Q, -n*(n+1)//2-n+r*(r+1)//2, prime)
                        *fac[n]*pow(fac[r], -1, prime)) % prime
            assert int(row[(a*N+n)*N+c]) == expected

    # Three independent scalar formulas for the retained Green register.
    P = [1]
    for t in range(1, N):
        P.append(((1-pow(Q, t, prime))**2*P[-1]+pow(Q, t, prime)) % prime)
    for t in range(N):
        partial = fac[t]**2*sum(pow(Q, v, prime)*pow(fac[v]**2 % prime, -1, prime)
                                 for v in range(t+1)) % prime
        durfee = fac[t]**2*sum(pow(Q, r*(r+1), prime)
                                *pow(fac[r]**2*fac[t-r] % prime, -1, prime)
                                for r in range(t+1)) % prime
        assert int(P[t]) == partial == durfee
        if t >= 2:
            recurrence = ((1+Q-2*pow(Q, t, prime)+pow(Q, 2*t, prime))*P[t-1]
                          -Q*(1-pow(Q, t-1, prime))**2*P[t-2]) % prime
            assert recurrence == P[t]

    # Squared-Pascal, diagonal Green, reversal, ORIGINAL crossing factorization.
    U = np.zeros((N, N), dtype=np.int64)
    dout, din = [], []
    for n in range(N):
        dout.append(pow(-1, n, prime)*pow(Q, -n*(n+3)//2, prime) % prime)
        din.append(pow(-1, n, prime)*pow(x, n, prime)*pow(Q, n*(n+1)//2, prime) % prime)
        for t in range(n+1):
            choose = fac[n]*pow(fac[t]*fac[n-t] % prime, -1, prime) % prime
            U[n, t] = pow(Q, -n*t, prime)*fac[n-t]*choose**2 % prime
    rev = I[::-1, :]
    factored = (pow(N, -1, prime)*np.diag(dout)@U % prime
                @np.diag(np.array(din)*np.array(P) % prime) % prime@rev % prime@L) % prime
    assert np.array_equal(actual, factored)

    # Closed all-entry expression / symmetric Newton congruence.
    V = np.zeros((N, N), dtype=np.int64)
    for n in range(N):
        V[n, 0] = 1
        for t in range(1, n+1):
            V[n, t] = V[n, t-1]*(1-pow(Q, -n+t-1, prime)) % prime
    hdiag = [pow(Q, t, prime)*P[t]*pow(fac[t]**4 % prime, -1, prime) % prime
             for t in range(N)]
    symmetric = V@np.diag(hdiag) % prime@V.T % prime
    assert np.array_equal(symmetric, symmetric.T)
    dr = [dout[n]*fac[n] % prime for n in range(N)]
    dc = [pow(x, j-d, prime)*pow(fac[d-j], -1, prime) % prime for j in range(N)]
    closed = np.diag(dr)@symmetric % prime@np.diag(dc) % prime
    assert np.array_equal(actual, closed)
    assert rank_mod(actual, prime) == sum(v != 0 for v in P)
    zero_ids = [t for t, v in enumerate(P) if not v]
    for t in zero_ids:
        kernel_vector = inverse_mod(L, prime)@rev[:, t] % prime
        assert not np.any(actual@kernel_vector % prime)

    # Actual whole-source row and benchmark prefix, not used in derivation.
    ordinary = np.array([pow(x, -j, prime)*pow(Q, -j, prime)*pow(N, -1, prime) % prime
                         for j in range(N)], dtype=np.int64)
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    Ji = inverse_mod(J, prime)
    R2 = Ji@R1 % prime@J % prime
    assert np.array_equal(np.sum(actual, axis=0) % prime, ordinary@R2 % prime@R2 % prime)
    prefix = Rminus[np.ix_(pair_ids, pair_ids)]@R2 % prime@cup % prime
    benchmark = [pow(-1, n, prime)*pow(Q, -n*(n+1)//2, prime)*fac[n]**2 % prime
                 for n in range(N)]
    assert np.array_equal(actual@prefix % prime, np.array(benchmark))
    if N == 6:
        assert zero_ids == [1]
        assert rank_mod(actual, prime) == 5
    return {'N': N, 'prime': prime, 'all_original_input_columns': N*N,
            'lowest_newton_crossing_identity': True,
            'green_and_symmetric_factorizations': True,
            'rank': rank_mod(actual, prime), 'zero_green_indices': zero_ids,
            'original_figure_eight_packets': True}


def angle_case(N):
    with mp.workdps(70):
        q = mp.exp(mp.j*mp.pi/N)
        Q, d = q*q, N-1
        fac = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
        sine = [abs(v) for v in fac]
        count = 0
        for n in range(N):
            for t in range(n+1):
                k = n-t
                choose = fac[n]/(fac[t]*fac[k])
                U = Q**(-n*t)*fac[k]*choose**2
                Umetric = sine[n]**(-mp.mpf(3)/2)*sine[t]**(mp.mpf(3)/2)*mp.sqrt(sine[k])*U
                weight = 1/(sine[t]*sine[k]*sine[d-n])
                assert abs(abs(Umetric)**2/N-weight) <= mp.mpf('1e-55')*max(1, weight)
                count += 1
        P = mp.mpc(1)
        for t in range(N):
            if t:
                P = (1-Q**t)**2*P+Q**t
            direct = fac[t]**2*sum(Q**v/fac[v]**2 for v in range(t+1))
            assert abs(P-direct) <= mp.mpf('1e-50')*max(1, abs(direct))
        return {'N': N, 'literal_three_port_angle_entries': count,
                'all_zero_length_slots_retained': True}


if __name__ == '__main__':
    rows = [field_case(N) for N in range(2, 11)]
    rows.append(field_case(12))
    angle = [angle_case(N) for N in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16)]
    output = {'status': 'PASS', 'original_terminal_open_matrices': rows,
              'complex_angle_metrics': angle,
              'scope': 'Entire source-independent T; no broad-prefix sharp energy bound.'}
    Path(__file__).with_name('actual_terminal_packet_closed_kernel_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 10 complete original open terminal matrices; 11 complex three-port angle metrics; all Green/rank/source identities')
