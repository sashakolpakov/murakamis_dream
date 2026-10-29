#!/usr/bin/env python3
"""Original full-R source and the uniform endpoint Gaussian normalization.

The asymptotic theorem is proved analytically in the note; no lower bound
is inferred from these finite tests or a fitted phase.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def original_source_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, kappa = N-1, q*q % p, int(Rp[0, 0])
    R3 = (Rp @ Rp % p) @ Rp % p
    cut = np.zeros((N, N), dtype=np.int64)
    for c in range(N):
        for a in range(N):
            cut[c, a] = sum(int(K[b, b])*int(R3[c*N+b, a*N+b])
                            for b in range(N)) % p
    fac, endpoint = 1, 1
    for j in range(1, N):
        fac = fac*(1-pow(Q, j, p)) % p
        endpoint = (endpoint+fac) % p
    original = -q*pow(kappa, -3, p)*cut % p
    assert np.array_equal(original, endpoint*np.eye(N, dtype=np.int64) % p)
    phi = 0
    for k in range(N):
        c = (pow(q, 2*k+1, p)+pow(q, -2*k-1, p)) % p
        A = (pow(q, 2*k+1, p)-pow(q, -2*k-1, p)) % p
        nu = pow(-1, k, p)*pow(q, k*(k+1), p) % p
        phi += pow(nu, 3, p)*(c-3*pow(2, -1, p)*(d-2*k)*A)
    folded = q*pow(2, -1, p)*phi % p
    assert folded == endpoint
    half = 0
    for k in range(N):
        if 2*k+1>=N:
            break
        c = (pow(q, 2*k+1, p)+pow(q, -2*k-1, p)) % p
        A = (pow(q, 2*k+1, p)-pow(q, -2*k-1, p)) % p
        nu = pow(-1, k, p)*pow(q, k*(k+1), p) % p
        half += pow(nu, 3, p)*(-c+3*pow(2, -1, p)*(d-2*k)*A)
    if N % 2:
        k = d//2
        nu = pow(-1, k, p)*pow(q, k*(k+1), p) % p
        half += pow(nu, 3, p)
    assert -q*half % p == endpoint
    # Full twisted pivotal partial trace coefficients, BOTH original signs.
    x = int(K[0, 0]); theta = pow(x, 1-N, p)
    Fplus, Fbar = [1], [1]
    for j in range(1, N):
        Fplus.append(Fplus[-1]*(1-pow(Q, j, p)) % p)
        Fbar.append(Fbar[-1]*(1-pow(Q, -j, p)) % p)
    D = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        for b in range(N):
            positive = (pow(Q, -b, p)*int(Rp[a*N+b, a*N+b])
                        *pow(kappa, -1, p)) % p
            negative = (theta*pow(Q, -b, p)*int(Rm[a*N+b, a*N+b])
                        *kappa*theta) % p
            expected_positive = (Fplus[a]**2*pow(Q, b*b, p)
                *pow(Fplus[a-b]*Fplus[b]**2 % p, -1, p) % p) if b<=a else 0
            r, A = d-b, d-a
            expected_negative = (Fbar[A]**2*pow(Q, -r*r, p)
                *pow(Fbar[A-r]*Fbar[r]**2 % p, -1, p) % p) if b>=a else 0
            assert positive == expected_positive
            assert negative == expected_negative
            D[a, b] = positive
    assert np.all(np.sum(D, axis=1) % p == 1)
    for a in range(2, N):
        shift = np.zeros(N, dtype=np.int64); shift[1:] = D[a-1, :-1]
        predicted = ((1+Q-2*pow(Q, a, p))*D[a-1]+pow(Q, 2*a-1, p)*shift
                     -Q*(1-pow(Q, a-1, p))**2*D[a-2]) % p
        assert np.array_equal(D[a], predicted)
    derivative = D @ np.arange(N, dtype=np.int64) % p
    P = [1]
    for j in range(1, N):
        P.append(((1-pow(Q, j, p))**2*P[-1]+pow(Q, j, p)) % p)
        assert (derivative[j]-derivative[j-1]) % p == pow(Q, j, p)*P[j-1] % p
    assert derivative[d] == (N-endpoint) % p
    return {'N': N, 'literal_full_R_cubed_K_pivotal_source': True,
            'all_original_kappa_and_q_source_phases': True,
            'complete_fold_and_odd_simple_node': True,
            'all_physical_signed_twisted_Markov_coefficients': N*N*2,
            'exact_closed_Ward_recurrence_and_normal_endpoint': True}


def gaussian_case(N):
    with mp.workdps(N+90):
        Q = mp.exp(2*mp.j*mp.pi/N)
        fac = [mp.mpc(1)]
        currents = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
            currents.append((1-Q**j)**2*currents[-1]+Q**j)
        endpoint = mp.fsum(fac)
        assert abs(endpoint-currents[-1])<mp.mpf('1e-55')*max(1, abs(endpoint))
        Sa, Sb = [], []
        for k in range(N):
            s = (mp.mpf(k)+mp.mpf('0.5'))/N
            phase = mp.exp(mp.j*mp.pi*N*(3*s*s+s))
            Sa.append((1-2*s)*mp.sin(2*mp.pi*s)*phase)
            Sb.append(mp.cos(2*mp.pi*s)*phase)
        exact = mp.exp(mp.j*mp.pi/(4*N))*(-mp.mpf(3)*N/2*mp.fsum(Sa)-mp.j*mp.fsum(Sb))
        assert abs(exact-endpoint)<mp.mpf('1e-50')*max(1, abs(endpoint))
        leading = N**mp.mpf('1.5')*mp.exp(mp.j*mp.pi*(mp.mpf('0.25')-
                                                       mp.mpf(N)/12+1/(mp.mpf(4)*N)))
        scaled_error = abs(endpoint-leading)/mp.sqrt(N)
        assert scaled_error<2  # Finite tested constant, not the proof of the O(sqrt N) bound.
        assert abs(endpoint)>N**mp.mpf('1.5')/2
        normal = [mp.mpc(0)]
        for a in range(1, N):
            normal.append(normal[-1]+Q**a*currents[a-1])
        assert abs(normal[-1]-(N-endpoint))<mp.mpf('1e-45')*max(1, abs(endpoint))
        Z = mp.fsum(abs(z)**2 for z in fac)
        assert max(abs(z) for z in normal)<=N*N+4*Z
        for a, value in enumerate(normal):
            assert abs(value)<=4*N**3*(1+abs(fac[a])**2)
            negative_value = N-1-mp.conj(normal[N-1-a])
            assert abs(negative_value)<=5*N**3*(1+abs(fac[N-1-a])**2)
        if N>=6:
            pindex = N-1-N//6
            assert max(abs(z) for z in normal)>=abs(currents[pindex])/2*(1-mp.mpf('1e-55'))
        tails = []
        if N>=12:
            for numerator, denominator in ((3, 4), (5, 6)):
                t = N*numerator//denominator
                reflected = mp.fsum(Q**(-k)*mp.conj(fac[k])**2
                                   for k in range(N-2-t+1))
                tail = mp.fsum(Q**r/fac[r]**2 for r in range(t+1, N))
                assert abs(N*N*tail-Q**(-1)*reflected)<mp.mpf('1e-50')
                assert mp.fsum(abs(fac[k])**2 for k in range(N-1-t))<2
                principal = fac[t]**2*endpoint/(N*N)
                assert abs(currents[t]/principal-1)<=2/abs(endpoint)
                tails.append({'fraction': f'{numerator}/{denominator}',
                              'relative_Green_density_error': float(abs(currents[t]/principal-1))})
        return {'N': N, 'exact_centered_quadratic_source_sum': True,
                'scaled_endpoint_error_over_sqrt_N': float(scaled_error),
                'endpoint_modulus_over_N_power_3_2': float(abs(endpoint)/N**mp.mpf('1.5')),
                'all_input_normal_current_and_factorial_energy_envelope': True,
                'reflected_original_Green_tail': tails}


def finite_integral_case(N):
    with mp.workdps(100):
        def J(ell):
            root = mp.sqrt(-3*mp.j*mp.pi*N)
            return (mp.exp(-mp.j*mp.pi*N*ell*ell/12)*mp.sqrt(mp.pi)/(2*root)*
                    (mp.erf(root*(1+ell/6))-mp.erf(root*ell/6)))

        def integral(m, typ):
            plus, minus = 1-2*m+mp.mpf(2)/N, 1-2*m-mp.mpf(2)/N
            jp, jm = J(plus), J(minus)
            if typ == 'a':
                return ((1+plus/3)*jp-(1+minus/3)*jm)/(2*mp.j)
            return (jp+jm)/2

        def direct(typ):
            total = []
            for k in range(N):
                s = (mp.mpf(k)+mp.mpf('0.5'))/N
                amp = (1-2*s)*mp.sin(2*mp.pi*s) if typ == 'a' else mp.cos(2*mp.pi*s)
                total.append(amp*mp.exp(mp.j*mp.pi*N*(3*s*s+s)))
            return mp.fsum(total)

        # The finite erf formula retains both endpoints, not an infinite Gaussian replacement.
        for m in (0, 1, 2, 3, 4):
            for typ in ('a', 'b'):
                f = (lambda s: (1-2*s)*mp.sin(2*mp.pi*s)) if typ == 'a' else (lambda s: mp.cos(2*mp.pi*s))
                numeric = mp.quad(lambda s: f(s)*mp.exp(mp.j*mp.pi*N*(3*s*s+(1-2*m)*s)),
                                  [0, mp.mpf(1)/6, mp.mpf(1)/2, mp.mpf(5)/6, 1])
                assert abs(numeric-integral(m, typ))<mp.mpf('1e-70')
        errors = []
        for M in (12, 24):
            for typ in ('a', 'b'):
                partial = N*mp.fsum((-1)**m*integral(m, typ) for m in range(-M, M+1))
                error = abs(partial-direct(typ))
                scale = N*M if typ == 'a' else M
                assert scale*error<10
                errors.append({'Poisson_cutoff': M, 'amplitude': typ,
                               'absolute_tail_error': float(error)})
        return {'N': N, 'finite_integral_endpoints_and_half_grid_sign': True,
                'truncated_Poisson_checks': errors}


if __name__ == '__main__':
    original = [original_source_case(N) for N in range(2, 11)]
    asymptotic = [gaussian_case(N) for N in (2, 3, 4, 5, 6, 7, 12, 24, 48, 96, 192, 384, 768)]
    integrals = [finite_integral_case(N) for N in (5, 6, 12)]
    result = {'status': 'PASS', 'original_full_signed_source_and_spectral_fold': original,
              'complete_endpoint_and_nonzero_Green_checks': asymptotic,
              'finite_Poisson_integrals_with_boundaries': integrals,
              'scope': 'Finite checks supplement the proved all-N Gaussian asymptotic; no phase fit or numerical-rate premise.'}
    Path(__file__).with_name('actual_normalization_endpoint_gaussian_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 9 full-R endpoint/signed all-input Ward sources; 13 quadratic-source/current levels; 3 finite-integral Poisson boundary checks')
