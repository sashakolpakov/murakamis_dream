#!/usr/bin/env python3
"""Literal normalization packet, typed clock couplings, and growing-band bounds."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_terminal_bridge_operator_reduction import terminal_matrix


def original_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % prime, int(K[0, 0]), int(Rp[0, 0])
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    barfac = [pow(-1, j, prime)*pow(Q, -j*(j+1)//2, prime)*fac[j] % prime for j in range(N)]
    _, _, T = terminal_matrix(N, 1, prime, q, E, F, K, Rp)
    e0 = np.zeros(N, dtype=np.int64)
    e0[0] = N
    packet = T@e0 % prime
    expected = np.array([pow(x, -d, prime)*pow(Q, -j, prime)*barfac[j] % prime
                         for j in range(N)], dtype=np.int64)
    assert np.array_equal(packet, expected)

    D = 2
    coefficients = {r: np.array([[r+4, r*r+3], [2*r+7, 5-r]], dtype=np.int64) % prime
                    for r in range(-D, D+1)}
    assert np.any((coefficients[0]@coefficients[1]-coefficients[1]@coefficients[0]) % prime)
    for t in [2, 3, Q]:
        lhs = np.zeros((2, 2), dtype=np.int64)
        for j in range(N):
            exterior = sum((pow(t*pow(Q, r, prime) % prime, j, prime)*A
                            for r, A in coefficients.items()), np.zeros((2, 2), dtype=np.int64)) % prime
            lhs = (lhs+int(packet[j])*exterior) % prime
        rhs = np.zeros((2, 2), dtype=np.int64)
        for r, A in coefficients.items():
            z = t*pow(Q, r, prime) % prime
            G = sum(barfac[j]*pow(z, j, prime) for j in range(N)) % prime
            P = Q*((1-pow(z, -1, prime))*G+pow(z, -1, prime)) % prime
            rhs = (rhs+pow(x, -d, prime)*P*A) % prime
        assert np.array_equal(lhs, rhs)

    # All-input open physical tangle: the scalar lowest-cut row is not
    # silently promoted to a scalar identity off phase one.
    I = np.eye(N, dtype=np.int64)
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    source, target = np.zeros((N**3, N), dtype=np.int64), np.zeros((N**3, N), dtype=np.int64)
    for a in range(N):
        for j in range(N):
            source[(j*N+d-j)*N+a, a] = cup[j]
            target[(a*N+j)*N+d-j, a] = cup[j]
    assert np.array_equal(np.kron(Rp, I)@np.kron(I, Rp) % prime@source % prime, target)
    cap = np.zeros((N, N**3), dtype=np.int64)
    for a in range(N):
        for c in range(N):
            cap[c, (a*N+d-a)*N+c] = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
    ids = [j*N+d-j for j in range(N)]
    L = Rp[np.ix_(ids, ids)]*pow(kappa, -1, prime) % prime
    L2 = L@L % prime
    for t in [1, 2, Q]:
        mask = np.array([pow(t, (j//N) % N, prime) for j in range(N**3)], dtype=np.int64)
        actual = cap@np.kron(I, Rp@Rp % prime) % prime@(mask[:, None]*target % prime) % prime
        expected = np.zeros((N, N), dtype=np.int64)
        for a in range(N):
            expected[a, a] = sum(pow(t, n, prime)*pow(x, n-a, prime)*pow(Q, -a, prime)*int(L2[d-a, n])
                                  for n in range(N)) % prime
        assert np.array_equal(actual, expected)
        if t == 1:
            assert np.array_equal(actual, kappa*kappa*np.eye(N, dtype=np.int64) % prime)
    return {'N': N, 'literal_recorded_packet': True,
            'noncommuting_controlled_clock_exteriors': 3,
            'all_input_physical_tangle_formula': True}


def frobenius(A):
    return mp.sqrt(mp.fsum(abs(z)**2 for z in A))


def complex_case(N, direction):
    with mp.workdps(100+N):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N)
        Q, x = q*q, q**d
        fac = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
        packet = [x**(-d)*Q**(-j)*mp.conj(fac[j]) for j in range(N)]
        D = max(1, int(N**mp.mpf('.4')/4))
        c = mp.sqrt(N)/4
        C = c+2*mp.pi*D
        assert C <= N/2
        t = 1+(c/N)*mp.exp(mp.j*direction)
        coefficients = {r: mp.matrix([[r+4, mp.j*(r*r+3)], [2*r+7, 5-r]])/(D+1)**2
                        for r in range(-D, D+1)}
        mass = mp.fsum(frobenius(A) for A in coefficients.values())
        powers = {r: mp.mpc(1) for r in coefficients}
        lhs = mp.zeros(2)
        for j in range(N):
            exterior = mp.zeros(2)
            for r, A in coefficients.items():
                exterior += powers[r]*A
                powers[r] *= t*Q**r
            lhs += packet[j]*exterior
        rhs = mp.zeros(2)
        for r, A in coefficients.items():
            z = t*Q**r
            G = mp.mpc(0)
            for value in reversed(fac):
                G = G*z+mp.conj(value)
            P = Q*((1-1/z)*G+1/z)
            rhs += x**(-d)*P*A
        assert frobenius(lhs-rhs)/max(1, frobenius(rhs)) < mp.mpf('1e-60')
        B = 2*mp.exp(2*C)*N*N*(1+2*N/(3*C))**(C/4)
        bound = mass*(2+2*C*B/N)
        assert frobenius(lhs) <= bound
        return {'N': N, 'Laurent_bandwidth': D, 'clock_disk_scale': mp.nstr(c, 12),
                'combined_scale': mp.nstr(C, 12),
                'coherent_operator_norm_upper': mp.nstr(frobenius(lhs), 18),
                'explicit_comparison_bound': mp.nstr(bound, 18)}


if __name__ == '__main__':
    result = {'status': 'PASS', 'original_typed_source': [original_case(N) for N in range(2, 9)],
              'growing_bandwidth_disk_checks': [complex_case(N, direction) for N in [16, 32, 64, 128, 256]
                                               for direction in [mp.pi/3, mp.pi]],
              'scope': 'Exposed recorded normalization packets with diagonal clock couplings; no general physical E/F or open-head bound.'}
    Path(__file__).with_name('actual_mesoscopic_clock_packet_currents_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 7 original packet/all-input typing levels; 21 operator-valued exteriors; 10 growing-band disk comparisons')
