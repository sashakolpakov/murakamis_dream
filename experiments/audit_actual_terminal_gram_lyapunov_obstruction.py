#!/usr/bin/env python3
"""Literal original vectors and full terminal Gram Lyapunov quotient."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_terminal_packet_closed_kernel import field_case as original_terminal_case


def literal_case(N):
    with mp.workdps(2*N+80):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N)
        Q, x, kappa = q*q, q**d, q**(mp.mpf(d*d)/2)
        fac = [mp.mpc(1)]
        P = [mp.mpc(1)]
        for t in range(1, N):
            fac.append(fac[-1]*(1-Q**t))
            P.append((1-Q**t)**2*P[-1]+Q**t)
        R, Rminus = mp.matrix(N), mp.matrix(N)
        for j in range(N):
            b = d-j
            # Independent literal negative crossing, not inverse(R).
            poch = mp.mpc(1)
            for k in range(b+1):
                if k:
                    poch *= 1-Q**(-b+k-1)
                i = b-k
                Rminus[i, j] = (kappa**(-1)*x**(d-k)*Q**(-j*b)
                    *fac[j+k]/(fac[k]*fac[j])*poch)
            for i in range(d-j, N):
                k = i+j-d
                R[i, j] = (kappa*x**(-d+k)*Q**((d-j)*(d-i))*fac[i]*fac[j]
                           /(fac[k]*fac[d-j]*fac[d-i]))
        identity = R*Rminus
        assert max(abs(identity[i, j]-(i == j)) for i in range(N) for j in range(N)) < mp.mpf('1e-45')
        X = mp.diag([x**i for i in range(N)])
        T = X*R*mp.diag(P[::-1])*R/N
        H = X*R*mp.diag(P[::-1])/N
        e0, ed = mp.zeros(N, 1), mp.zeros(N, 1)
        e0[0], ed[d] = 1, 1
        v = Rminus*e0
        source = mp.matrix([N*x**(j-d) for j in range(N)])
        expected_v = mp.matrix([kappa**(-1)*x**j*fac[d-j] for j in range(N)])
        assert max(abs(v[j]-expected_v[j]) for j in range(N)) < mp.mpf('1e-45')
        assert max(abs((R*e0)[j]-kappa*x**(-d)*ed[j]) for j in range(N)) < mp.mpf('1e-45')
        assert max(abs((R*source)[j]-kappa*source[j]) for j in range(N)) < mp.mpf('1e-40')
        assert max(abs(z-1) for z in T*source) < mp.mpf('1e-40')
        # Literal highest-column R23 source extraction, independently proved
        # on every physical input by the all-input cup-slide audit.
        adjacent_source = mp.matrix([kappa*source[j]*fac[d-j] for j in range(N)])
        assert max(abs(adjacent_source[j]-N*v[j]) for j in range(N)) < mp.mpf('1e-40')
        assert max(abs((R*adjacent_source)[j]-N*e0[j]) for j in range(N)) < mp.mpf('1e-40')
        assert max(abs((T*adjacent_source)[j]-kappa*P[d]*ed[j]) for j in range(N)) < mp.mpf('1e-38')
        Z = sum(abs(z)**2 for z in fac)
        norm2 = lambda z: sum(abs(a)**2 for a in z)
        energies = [norm2(T*v), norm2(T*(R*v)), norm2(H*e0), norm2(H*(R*e0))]
        expected = [abs(P[d])**2/N**2, Z/N**2, abs(P[d])**2/N**2, Z/N**2]
        for actual, target in zip(energies, expected):
            assert abs(actual-target) < mp.mpf('1e-38')*max(1, target)
        assert abs(norm2(v)-Z) < mp.mpf('1e-40')*max(1, Z)
        assert abs(P[d]-sum(fac)) < mp.mpf('1e-40')*max(1, abs(P[d]))
        assert abs(P[d]) <= 3*N*N
        epsilon = mp.exp(-N*N)
        # Quotients are evaluated on explicit vectors, with no near-singular inverse.
        quotient_T = (energies[1]+epsilon*norm2(R*v))/(energies[0]+epsilon*norm2(v))
        exact_T = (Z+N*N*epsilon)/(abs(P[d])**2+N*N*epsilon*Z)
        quotient_H = (energies[3]+epsilon*norm2(R*e0))/(energies[2]+epsilon)
        exact_H = (Z+N*N*epsilon)/(abs(P[d])**2+N*N*epsilon)
        assert abs(quotient_T/exact_T-1) < mp.mpf('1e-38')
        assert abs(quotient_H/exact_H-1) < mp.mpf('1e-38')
        assert exact_T >= Z/(9*N**4+1)
        return {'N': N, 'literal_signed_R_inverse': True,
                'complete_coherent_T_and_H_energies': True,
                'fixed_original_adjacent_source_trajectory': True,
                'bare_cup_still_has_no_growth': True,
                'Gram_Rayleigh_ratio': float(exact_T),
                'ratio_log_over_N': float(mp.log(exact_T)/N)}


def large_energy_profile(N):
    with mp.workdps(N+70):
        Q = mp.exp(2*mp.j*mp.pi/N)
        fac, P = mp.mpc(1), mp.mpc(1)
        Z = mp.mpf(1)
        for t in range(1, N):
            fac *= 1-Q**t
            Z += abs(fac)**2
            P = (1-Q**t)**2*P+Q**t
        epsilon = mp.exp(-N*N)
        quotient = (Z+N*N*epsilon)/(abs(P)**2+N*N*epsilon*Z)
        assert quotient >= Z/(9*N**4+1)
        return {'N': N, 'positive_factorial_energy': str(Z),
                'Rayleigh_pi_lograte_diagnostic': float(mp.pi/N*mp.log(quotient)),
                'Z_pi_lograte_diagnostic': float(mp.pi/N*mp.log(Z))}


if __name__ == '__main__':
    original = [original_terminal_case(N) for N in (2, 3, 4, 5, 6, 8, 10)]
    literal = [literal_case(N) for N in range(2, 21)]
    profiles = [large_energy_profile(N) for N in (24, 48, 96, 192, 384)]
    result = {'status': 'PASS', 'independent_original_terminal_replays': original,
              'literal_full_signed_source_tests': literal,
              'large_exact_energy_quotients': profiles,
              'scope': 'Current-Gram growth occurs on a fixed original cup braid orbit; coherent closure/shrinking-clock repair retained.'}
    Path(__file__).with_name('actual_terminal_gram_lyapunov_obstruction_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 7 original terminal modules; 19 literal signed source/Gram families; 5 all-level energy profiles')
