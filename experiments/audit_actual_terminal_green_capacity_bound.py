#!/usr/bin/env python3
"""Original-source endpoint, full-Cartan terminal sandwich, and capacity.

Field checks replay the original physical terminal construction. Complex
checks keep coherent P before norms; no separate absolute Green sum is used.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_terminal_packet_closed_kernel import field_case as original_terminal_case


def field_sandwich(N):
    # This independently builds physical H,D,R^2 and all projector rows.
    original = original_terminal_case(N)
    prime, eta, q, E, F, K, pivot, R, Rminus = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    ids = [j*N+d-j for j in range(N)]
    Rp, Rm = R[np.ix_(ids, ids)], Rminus[np.ix_(ids, ids)]
    fac = [1]
    P = [1]
    for t in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, t, prime)) % prime)
        P.append(((1-pow(Q, t, prime))**2*P[-1]+pow(Q, t, prime)) % prime)
    assert P[d] == sum(fac) % prime
    V = np.zeros((N, N), dtype=np.int64)
    for n in range(N):
        V[n, 0] = 1
        for t in range(1, n+1):
            V[n, t] = V[n, t-1]*(1-pow(Q, -n+t-1, prime)) % prime
    diagonal = [pow(Q, t, prime)*P[t]*pow(fac[t]**4 % prime, -1, prime) % prime
                for t in range(N)]
    H = V@np.diag(diagonal) % prime@V.T % prime
    dr = [pow(-1, n, prime)*pow(Q, -n*(n+3)//2, prime)*fac[n] % prime for n in range(N)]
    dc = [pow(x, j-d, prime)*pow(fac[d-j], -1, prime) % prime for j in range(N)]
    T = np.diag(dr)@H % prime@np.diag(dc) % prime
    X = np.diag([pow(x, n, prime) for n in range(N)])
    current = np.diag(P[::-1])
    assert np.array_equal(T, pow(N, -1, prime)*X@Rp % prime@current % prime@Rp % prime)
    assert np.array_equal(T@Rm % prime, pow(N, -1, prime)*X@Rp % prime@current % prime)
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    assert np.array_equal(T@cup % prime, np.ones(N, dtype=np.int64))
    return {'N': N, 'original_physical_matrix_replayed': True,
            'entire_full_Cartan_sandwich': True, 'literal_inverse_cancelled': True,
            'rank': original['rank']}


def complex_green(N):
    with mp.workdps(N+65):
        q = mp.exp(mp.j*mp.pi/N)
        Q, d = q*q, N-1
        fac = [mp.mpc(1)]
        P = [mp.mpc(1)]
        for t in range(1, N):
            fac.append(fac[-1]*(1-Q**t))
            P.append((1-Q**t)**2*P[-1]+Q**t)
        sigma = sum(fac)
        assert abs(P[d]-sigma) <= mp.mpf('1e-45')*max(1, abs(sigma))
        # Actual full pivotal Hermite functional, not a positive replacement.
        phi = mp.mpc(0)
        for j in range((N+1)//2):
            a = 2*j+1
            if a >= N:
                break
            c, delta = q**a+q**(-a), q**a-q**(-a)
            nu = (-1)**j*q**(j*(j+1))
            derivative = -nu*(N-a)/(2*delta)
            phi -= c*nu**3+delta**2*3*nu**2*derivative
        if N % 2:
            j = d//2
            phi += ((-1)**j*q**(j*(j+1)))**3
        assert abs(sigma+q*phi) <= mp.mpf('1e-40')*max(1, abs(sigma))
        assert abs(P[d]) <= 3*N*N
        max_ratio = mp.mpf(0)
        for t in range(N):
            bound = N+4*abs(fac[t])**2
            max_ratio = max(max_ratio, abs(P[t])/bound)
            assert abs(P[t]) <= bound*(1+mp.mpf('1e-40'))
        return {'N': N, 'both_original_endpoint_identities': True,
                'all_Green_colors_bounded': N,
                'maximum_finite_bound_ratio': float(max_ratio),
                'endpoint_absolute_value': float(abs(P[d]))}


def finite_operator_bound(N):
    with mp.workdps(N+65):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N)
        Q, x, kappa = q*q, q**d, q**(mp.mpf(d*d)/2)
        fac = [mp.mpc(1)]
        P = [mp.mpc(1)]
        for t in range(1, N):
            fac.append(fac[-1]*(1-Q**t))
            P.append((1-Q**t)**2*P[-1]+Q**t)
        R, H = mp.matrix(N), mp.matrix(N)
        for i in range(N):
            for j in range(d-i, N):
                k = i+j-d
                R[i, j] = (kappa*x**(-d+k)*Q**((d-j)*(d-i))*fac[i]*fac[j]
                           /(fac[k]*fac[d-j]*fac[d-i]))
                H[i, j] = x**i/N*R[i, j]*P[d-j]
                # This is the precise coupled finite entry estimate.
                assert abs(H[i, j]) <= (abs(R[i, j])
                        +4*N*abs(R[i, j])/abs(fac[j])**2)*(1+mp.mpf('1e-40'))
        Rhs = mp.sqrt(sum(abs(v)**2 for v in R))
        M = max(abs(fac[i])**2/abs(fac[k]) for i in range(N) for k in range(i+1))
        Hhs = mp.sqrt(sum(abs(v)**2 for v in H))
        assert Hhs <= (Rhs+4*M)*(1+mp.mpf('1e-40'))
        scale = max(abs(v) for v in H)
        A = np.array([[complex(H[i, j]/scale) for j in range(N)] for i in range(N)])
        largest = np.linalg.svd(A, compute_uv=False)[0]
        op_log = mp.log(scale)+mp.log(float(largest))
        return {'N': N, 'all_coupled_entry_bounds': N*(N+1)//2,
                'Hilbert_Schmidt_finite_inequality': True,
                'operator_2pi_lograte_diagnostic': float(2*mp.pi/N*op_log),
                'R_HS_2pi_lograte_diagnostic': float(2*mp.pi/N*mp.log(Rhs)),
                'M_2pi_lograte_diagnostic': float(2*mp.pi/N*mp.log(M))}


def quarter_density(N):
    with mp.workdps(N+65):
        Q = mp.exp(2*mp.j*mp.pi/N)
        t = N//4
        P = mp.mpc(1)
        for j in range(1, t+1):
            P = (1-Q**j)**2*P+Q**j
        reference = 1/(2-Q**t)
        error = abs(P-reference)
        # A nonzero macroscopic density, with an O(1/N) diagnostic.
        assert abs(P) >= mp.mpf('0.3')
        assert N*error < 3
        return {'N': N, 'physical_color': t, 'density_error': float(error),
                'N_times_density_error': float(N*error)}


if __name__ == '__main__':
    fields = [field_sandwich(N) for N in range(2, 10)]
    green = [complex_green(N) for N in range(2, 81)]
    operators = [finite_operator_bound(N) for N in (2, 3, 4, 5, 6, 8, 12, 24, 48, 96)]
    density = [quarter_density(N) for N in (24, 48, 96, 192, 384)]
    result = {'status': 'PASS', 'literal_original_full_matrix': fields,
              'source_endpoints_and_all_Green_colors': green,
              'coupled_finite_operator_bounds': operators,
              'nonzero_quarter_density': density,
              'scope': 'All-prefix terminal-with-inverse norm; no sharp knot-volume claim.'}
    Path(__file__).with_name('actual_terminal_green_capacity_bound_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 8 original full-Cartan packet matrices; 79 all-color source Green bounds; 10 coupled operator bounds; 5 nonzero quarter densities')
