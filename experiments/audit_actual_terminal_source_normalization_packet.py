#!/usr/bin/env python3
"""Original all-input cup slide and complete terminal normalization packet."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_terminal_bridge_operator_reduction import terminal_matrix


def field_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % prime, int(K[0, 0]), int(Rp[0, 0])
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    source = np.zeros((N, N, N, N), dtype=np.int64)
    target = np.zeros_like(source)
    for a in range(N):
        for c in range(N):
            source[a, d-a, c, c] = cup[a]
            target[c, a, d-a, c] = cup[a]
    middle = np.zeros_like(source)
    for a in range(N):
        middle[a] = (Rp @ source[a].reshape(N*N, N) % prime).reshape(N, N, N)
    result = (Rp @ middle.reshape(N*N, N*N) % prime).reshape(N, N, N, N)
    assert np.array_equal(result, target)
    # The actual complete highest-chart inverse is last-head color zero.
    adjacent_source = np.array([middle[j, d-j, 0, 0] for j in range(N)], dtype=np.int64)
    expected_adjacent = kappa*cup*np.array(fac[::-1], dtype=np.int64) % prime
    assert np.array_equal(adjacent_source, expected_adjacent)
    ids = [j*N+d-j for j in range(N)]
    R, Rminus = Rp[np.ix_(ids, ids)], Rm[np.ix_(ids, ids)]
    e0 = np.zeros(N, dtype=np.int64); e0[0] = 1
    ed = np.zeros(N, dtype=np.int64); ed[d] = 1
    assert pow(kappa, 2, prime) == pow(x, d, prime)
    assert np.array_equal(adjacent_source, N*(Rminus @ e0) % prime)
    after = R @ adjacent_source % prime
    assert np.array_equal(after, N*e0 % prime)
    _, _, T = terminal_matrix(N, 1, prime, q, E, F, K, Rp)
    P = [1]
    for j in range(1, N):
        P.append(((1-pow(Q, j, prime))**2*P[-1]+pow(Q, j, prime)) % prime)
    first, second = T @ adjacent_source % prime, T @ after % prime
    assert np.array_equal(first, kappa*P[d]*ed % prime)
    conjugate_fac = [pow(-1, j, prime)*pow(Q, -j*(j+1)//2, prime)*fac[j] % prime
                     for j in range(N)]
    exact_second = np.array([pow(x, -d, prime)*pow(Q, -j, prime)*conjugate_fac[j] % prime
                             for j in range(N)], dtype=np.int64)
    assert np.array_equal(second, exact_second)
    assert int(sum(second)) % prime == pow(x, -d, prime)*Q % prime
    G = conjugate_fac+[0]
    for j in range(N):
        assert second[j] == pow(x, -d, prime)*Q*(G[j]-G[j+1]) % prime
    # Operator-valued spectator test: no commuting variable is substituted.
    rows = [np.array([[j+1, j*j+3], [2*j+5, 3*j+7]], dtype=np.int64) % prime
            for j in range(N)]
    if N>1:
        assert np.any((rows[0]@rows[1]-rows[1]@rows[0]) % prime)
    lhs = sum((int(second[j])*rows[j] for j in range(N)), np.zeros((2, 2), dtype=np.int64)) % prime
    rhs = rows[0].copy()
    for j in range(1, N):
        rhs = (rhs+(rows[j]-rows[j-1])*G[j]) % prime
    rhs = pow(x, -d, prime)*Q*rhs % prime
    assert np.array_equal(lhs, rhs)
    jet = sum(j*int(second[j]) for j in range(N)) % prime
    assert jet == pow(x, -d, prime)*Q*(sum(conjugate_fac)-1) % prime
    return {'N': N, 'all_original_physical_cup_slide_columns': N,
            'complete_source_orbit_and_packet_identities': True,
            'original_kappa_marked_source_and_unit_endpoint_retained': True,
            'noncommuting_spectator_current': True}


def complex_case(N):
    with mp.workdps(N+70):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N); Q = q*q; x = q**d
        fac = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
        P = [mp.mpc(1)]
        for j in range(1, N):
            P.append((1-Q**j)**2*P[-1]+Q**j)
        packet = [x**(-d)*Q**(-j)*mp.conj(fac[j]) for j in range(N)]
        Z = mp.fsum(abs(z)**2 for z in fac)
        assert abs(mp.fsum(packet)-x**(-d)*Q)<mp.mpf('1e-45')
        assert abs(mp.fsum(abs(z)**2 for z in packet)-Z)<mp.mpf('1e-45')*Z
        assert abs(mp.fsum(j*packet[j] for j in range(N))-
                   x**(-d)*Q*mp.conj(P[d]-1))<mp.mpf('1e-40')*max(1, abs(P[d]))
        optimized = mp.fsum(abs(z) for z in fac)**2
        for power in (-1, 0, 1, 2):
            weights = [abs(z)**power for z in fac]
            budget = mp.fsum(1/w for w in weights)*mp.fsum(
                weights[j]*abs(packet[j])**2 for j in range(N))
            assert budget>=optimized*(1-mp.mpf('1e-45'))
            if power == -1:
                assert abs(budget/optimized-1)<mp.mpf('1e-45')
        return {'N': N, 'complete_packet_energy_and_raw_unit_scalar': True,
                'exact_optimized_diagonal_Cauchy_budget': True,
                'polynomial_first_jet_identity': True}


if __name__ == '__main__':
    physical = [field_case(N) for N in range(2, 11)]
    complex_rows = [complex_case(N) for N in (2, 3, 4, 5, 8, 12, 24, 48, 96)]
    output = {'status': 'PASS', 'literal_original_source_and_spectators': physical,
              'complex_complete_energy_and_metric_checks': complex_rows,
              'scope': 'Actual p-orbit full-circle/diagonal-clock obstruction; exact coherent normalization pruning; no shrinking-arc or general knot-energy claim.'}
    Path(__file__).with_name('actual_terminal_source_normalization_packet_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 9 all-input original cup slides and full source packets; 9 coherent energy/diagonal-budget levels; spectator currents')
