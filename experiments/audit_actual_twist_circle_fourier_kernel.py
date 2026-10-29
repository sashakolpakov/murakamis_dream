#!/usr/bin/env python3
"""Full original signed powers versus their Fourier-Hermite circle kernel."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct


def matrix_power(A, exponent, prime):
    result = np.eye(len(A), dtype=np.int64)
    while exponent:
        if exponent & 1:
            result = result@A % prime
        A = A@A % prime
        exponent >>= 1
    return result


def finite_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, rho = N-1, (q-pow(q, -1, prime)) % prime
    E2, F2, K2 = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki2 = np.diag([pow(int(z), -1, prime) for z in np.diag(K2)])
    Omega = (F2@E2+q*K2+pow(q, -1, prime)*Ki2) % prime
    I = np.eye(N*N, dtype=np.int64)
    # Full physical space, not just its degree-d multiplicity block.
    V = [2*I % prime, Omega]
    for _ in range(2, N+1):
        V.append((Omega@V[-1]-V[-2]) % prime)
    assert not np.any((V[N]+2*I) % prime)
    U = [I, Omega]
    for _ in range(2, N):
        U.append((Omega@U[-1]-U[-2]) % prime)
    w = [pow(q, 2*k+1, prime) for k in range(N)]
    nu = [pow(-1, k, prime)*pow(q, k*(k+1), prime) % prime for k in range(N)]
    kappa = int(Rp[0, 0])
    inverse_N = pow(N, -1, prime)
    signed_cases = []
    for ell in (-7, -4, -2, -1, 0, 1, 2, 3, 8):
        h = [pow(z, ell, prime) for z in nu]
        jet = [-ell*(d-2*k)*h[k]*pow(2, -1, prime) % prime for k in range(N)]
        H = [sum(h[k]*pow(w[k], -n, prime) for k in range(N))*inverse_N % prime
             for n in range(N)]
        D = [sum(jet[k]*pow(w[k], -n, prime) for k in range(N))*inverse_N % prime
             for n in range(N)]
        assert D[0] == 0
        a = [H[0]]+[(D[n]+(N-n)*H[n])*inverse_N % prime for n in range(1, N)]
        for n in range(1, N):
            assert (a[n]-a[N-n]) % prime == H[n]
            assert (n*a[n]+(N-n)*a[N-n]) % prime == D[n]
        polynomial = a[0]*I % prime
        for n in range(1, N):
            polynomial = (polynomial+a[n]*V[n]) % prime
        expected = matrix_power(Rp if ell >= 0 else Rm, abs(ell), prime)
        assert np.array_equal(pow(kappa, ell, prime)*polynomial % prime, expected)
        extended = a+[0, 0]
        beta = [pow(-1, j, prime)*(extended[j]-extended[j+2]) % prime for j in range(N)]
        reconstructed = np.zeros_like(I)
        for j in range(N):
            reconstructed = (reconstructed+beta[j]*pow(-1, j, prime)*U[j]) % prime
        assert np.array_equal(reconstructed, polynomial)
        if ell == 0:
            assert beta == [1]+[0]*(N-1)
        signed_cases.append(ell)
    return {'N': N, 'full_physical_dimension': N*N,
            'entire_Casimir_polynomial_including_normal_blocks': True,
            'literal_original_signed_powers': signed_cases,
            'Fourier_aliases_and_circle_basis_reconstruction': True}


def complex_case(N):
    with mp.workdps(90):
        d = N-1
        q = mp.exp(mp.pi*mp.j/N)
        w = [q**(2*k+1) for k in range(N)]
        nu = [(-1)**k*q**(k*(k+1)) for k in range(N)]
        ratios = []
        for ell in (-18, -3, -2, 0, 1, 2, 6, 16):
            h = [z**ell for z in nu]
            jet = [-mp.mpf(ell)/2*(d-2*k)*h[k] for k in range(N)]
            H = [mp.fsum(h[k]*w[k]**(-n) for k in range(N))/N for n in range(N)]
            D = [mp.fsum(jet[k]*w[k]**(-n) for k in range(N))/N for n in range(N)]
            a = [H[0]]+[(D[n]+(N-n)*H[n])/N for n in range(1, N)]
            assert abs(a[0]) <= 1+mp.mpf('1e-70')
            assert all(abs(z) <= 1+abs(ell)/2+mp.mpf('1e-70') for z in a[1:])
            for k in range(N):
                value = a[0]+mp.fsum(a[n]*(w[k]**n+w[k]**(-n)) for n in range(1, N))
                derivative = mp.fsum(n*a[n]*(w[k]**n-w[k]**(-n)) for n in range(1, N))
                assert abs(value-h[k])+abs(derivative-jet[k]) < mp.mpf('1e-65')
            extended = a+[0, 0]
            beta = [(-1)**j*(extended[j]-extended[j+2]) for j in range(N)]
            mass = mp.fsum(abs(z) for z in beta)
            bound = 2*N*(1+abs(ell)/2)
            assert mass <= bound+mp.mpf('1e-65')
            ratios.append(float(mass/bound))
        return {'N': N, 'Hermite_values_and_all_marked_logarithmic_derivatives': True,
                'eight_signed_coefficient_mass_checks': True, 'largest_mass_bound_ratio': max(ratios)}


if __name__ == '__main__':
    out = {'status': 'PASS', 'literal_full_physical_powers': [finite_case(N) for N in range(2, 11)],
           'complex_Fourier_kernel_and_mass': [complex_case(N) for N in (2, 3, 4, 6, 9, 12, 24, 48)],
           'scope': 'Exact original crossing-power kernel with polynomial coefficient mass; geometric filling survival remains unproved.'}
    Path(__file__).with_name('actual_twist_circle_fourier_kernel_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS 81 full original signed powers; 64 complex Hermite/circle coefficient bounds; all physical degree blocks retained')
