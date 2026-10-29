#!/usr/bin/env python3
"""Original full-jet Gaussian filling, normal current and exact Weyl fold."""

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_twist_circle_fourier_kernel import matrix_power
from audit_actual_pretzel_complete_base_casimir_polynomial import rotate_box


def exact_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(N*N, dtype=np.int64)
    V = [2*I % prime, O]
    U = [I, O]
    for _ in range(2, N):
        V.append((O@V[-1]-V[-2]) % prime)
        U.append((O@U[-1]-U[-2]) % prime)
    kappa = pow(eta, d*d, prime)
    cup = np.array([N*pow(x, -b, prime) % prime if a+b == d else 0
                    for a in range(N) for b in range(N)], dtype=np.int64)
    cap = np.array([pow(x, a, prime)*pow(N, -1, prime) % prime if a+b == d else 0
                    for a in range(N) for b in range(N)], dtype=np.int64)
    cupcap = np.outer(cup, cap) % prime
    powers = (-3, -2, -1, 0, 1, 2, 3, N)
    rows = []
    for P in powers:
        # EXACT centered Gaussian at the original half-root nodes.
        h = [pow(eta, P*((2*k+1-N)**2-d*d), prime) for k in range(N)]
        derivative = [P*(2*k+1-N)*h[k] % prime for k in range(N)]
        for k in range(N):
            nu = pow(-1, k, prime)*pow(q, k*(k+1), prime) % prime
            assert h[k] == pow(nu, 2*P, prime)
        def HD(n):
            H = sum(h[k]*pow(q, -n*(2*k+1), prime) for k in range(N))*pow(N, -1, prime) % prime
            D = sum(derivative[k]*pow(q, -n*(2*k+1), prime) for k in range(N))*pow(N, -1, prime) % prime
            return H, D
        def a(n):
            H, D = HD(n)
            return (D+(N-n)*H)*pow(N, -1, prime) % prime
        aa = [a(n) for n in range(N)]
        actual = matrix_power(Rp if P >= 0 else Rm, 2*abs(P), prime)
        polynomial = aa[0]*I % prime
        for n in range(1, N):
            polynomial = (polynomial+aa[n]*V[n]) % prime
        assert np.array_equal(pow(kappa, 2*P, prime)*polynomial % prime, actual)
        # FULL physical endpoint Ward, including the unique wrap-normal jet.
        shifted = 2*aa[0]*I % prime
        for n in range(1, N):
            shifted = (shifted+aa[n]*(pow(Q, n, prime)+pow(Q, -n, prime))*V[n]) % prime
        if P == 0:
            gaussian_multiplier = 2*I % prime
        else:
            C0, C1 = 2*I % prime, O.copy()
            for _ in range(2, 2*abs(P)+1):
                C0, C1 = C1, (O@C1-C0) % prime
            gaussian_multiplier = C1
        endpoint = (shifted-pow(Q, P, prime)*gaussian_multiplier@polynomial) % prime
        expected_endpoint = 2*P*N*pow(-1, N, prime)*rho*cupcap % prime
        assert np.array_equal(endpoint, expected_endpoint)
        rotated_endpoint = rotate_box(Rm@endpoint % prime, N, x, prime)
        scalar_endpoint = 2*P*N*pow(-1, N, prime)*rho*pow(kappa, -1, prime) % prime
        assert np.array_equal(rotated_endpoint, scalar_endpoint*I % prime)
        extended = aa+[0, 0]
        beta = [pow(-1, j, prime)*(extended[j]-extended[j+2]) % prime for j in range(N)]
        original_filled = rotate_box(Rm@actual % prime, N, x, prime)
        filled = np.zeros_like(I)
        for j in range(N):
            circle_box = rotate_box(Rm@(pow(-1, j, prime)*U[j] % prime) % prime, N, x, prime)
            filled = (filled+pow(kappa, 2*P, prime)*beta[j]*circle_box) % prime
        assert np.array_equal(original_filled, filled)
        for n in range(-N, 2*N+1):
            assert (a(n-2*P)-pow(Q, n-P, prime)*a(n)
                    -2*P*pow(N, -1, prime)*pow(q, n-2*P, prime)) % prime == 0
        def folded(hdef):
            j = N-hdef
            return pow(-1, j-1, prime)*(a(j-1)-a(j+1)) % prime
        for hdef in range(N):
            assert folded(hdef) == folded(-hdef)
            expected = beta[N-hdef-1]*(2 if hdef == 0 else 1) % prime
            assert folded(hdef) == expected
        # Arbitrary spectator-valued EVEN core, with full physical halfweight.
        rng = np.random.default_rng(300*N+P)
        cores = [rng.integers(0, prime, size=(2, 2), dtype=np.int64) for _ in range(N)]
        left = sum((beta[N-hdef-1]*cores[hdef] for hdef in range(N)), np.zeros((2, 2), dtype=np.int64)) % prime
        right = sum((folded(hdef)*cores[abs(hdef)] for hdef in range(-N+1, N)),
                    np.zeros((2, 2), dtype=np.int64))*pow(2, -1, prime) % prime
        assert np.array_equal(left, right)
        rows.append({'P': P, 'full_physical_twist_and_odd_box': True,
                     'all_normal_jets_and_affine_chirp_Ward': True,
                     'full_pair_endpoint_Ward_and_scalar_turned_source': True,
                     'exact_physical_Weyl_halfweight_with_arbitrary_spectators': True})
    return {'N': N, 'full_original_physical_dimension': N*N, 'signed_chirps': rows}


def data(N, P):
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2j*mp.pi/N)
    kappa = mp.exp(mp.pi*1j*(N-1)**2/(2*N))
    x = [mp.pi*1j*(2*k+1)/N for k in range(N)]
    h = [kappa**(-P)*mp.exp(P*(z-mp.pi*1j)**2/(2j*mp.pi/N)) for z in x]
    d = [P*(2*k+1-N)*h[k] for k in range(N)]
    def HD(n):
        return (mp.fsum(h[k]*mp.exp(-n*x[k]) for k in range(N))/N,
                mp.fsum(d[k]*mp.exp(-n*x[k]) for k in range(N))/N)
    def a(n):
        H, D = HD(n)
        return (D+(N-n)*H)/N
    def K(hdef):
        j = N-hdef
        return mp.exp(mp.pi*1j*(j-1))*(a(j-1)-a(j+1))
    return q, Q, kappa, x, h, d, HD, a, K


def gauss_case(N, P):
    mp.mp.dps = 85
    q, Q, kappa, x, h, d, HD, a, K = data(N, P)
    H = [HD(n)[0] for n in range(N)]
    D = [HD(n)[1] for n in range(N)]
    for n in range(N):
        expected = -1j*P*mp.fsum(H[m]/mp.sin(mp.pi*(m-n)/N) for m in range(N) if m != n)
        assert abs(D[n]-expected) < mp.mpf('1e-65')
        if P == 0:
            assert abs(H[n]-(1 if n == 0 else 0)) < mp.mpf('1e-65')
        else:
            g, L = math.gcd(abs(P), N), N//math.gcd(abs(P), N)
            allowed = n % g == 0
            if allowed and L % 2 == 0:
                allowed = ((P-n)//g-(P//g)*(L//2)) % 2 == 0
            expected_modulus = (mp.sqrt(mp.mpf(2)/L) if L % 2 == 0 else 1/mp.sqrt(L)) if allowed else 0
            assert abs(abs(H[n])-expected_modulus) < mp.mpf('1e-65')
    for n in (mp.mpc('1.3', '.1'), mp.mpc(N-2, '-.2')):
        current = ((mp.exp(-2j*mp.pi*n)-1)*mp.exp(mp.pi*1j*(n-2*P)/N)
                   *(N-n+P*(N+1))/N**2)
        actual = a(n-2*P)-mp.exp(2j*mp.pi*(n-P)/N)*a(n)-mp.mpf(2)*P/N*mp.exp(mp.pi*1j*(n-2*P)/N)
        assert abs(actual-current) < mp.mpf('1e-60')
    for hdef in (mp.mpc('.3', '.2'), mp.mpc('1.2', '-.1')):
        assert abs(K(hdef)-K(-hdef)) < mp.mpf('1e-60')
        hbar = 2j*mp.pi/N
        finite = (mp.mpf(2)*(-1)**(N-1)/N**2*mp.fsum(h[k]*mp.exp(hdef*(x[k]-mp.pi*1j))
                  *((hdef+2*P*(x[k]-mp.pi*1j)/hbar)*mp.sinh(x[k]-mp.pi*1j)
                    +mp.cosh(x[k]-mp.pi*1j)) for k in range(N)))
        assert abs(K(hdef)-finite) < mp.mpf('1e-60')
    return {'N': N, 'P': P, 'all_gcd_and_parity_value_selection': True,
            'entire_normal_current_and_even_extension': True,
            'complete_finite_Hilbert_normal_kernel': True}


def fresnel(P, N, b):
    if P == 0:
        return -mp.expm1(-2j*mp.pi*b)/(2j*mp.pi*b) if abs(b) > mp.mpf('1e-80') else mp.mpf(1)
    z = mp.sqrt(-2j*mp.pi*P*N)
    primitive = lambda t: mp.sqrt(mp.pi)/(2*z)*mp.erf(z*t)
    return (mp.exp(-mp.pi*1j*b-mp.pi*1j*b*b/(2*P*N))
            *(primitive(mp.mpf('.5')-b/(2*P*N))
              -primitive(-mp.mpf('.5')-b/(2*P*N))))


def poisson_case(N, P, n):
    mp.mp.dps = 100
    q, Q, kappa, x, h, d, HD, a, K = data(N, P)
    n = mp.mpc(n)
    J = mp.exp(mp.pi*1j*P*N/2)*(-mp.expm1(-2j*mp.pi*n))/(2j*mp.pi*N)
    errors = []
    for cutoff in (16, 32, 64):
        value = kappa**(-P)*mp.fsum((-1)**ell*((ell+1)*fresnel(P, N, n+N*ell)-J)
                                  for ell in range(-cutoff, cutoff+1))
        errors.append(abs(value-a(n)))
    assert errors[2] < errors[1] < errors[0]
    assert errors[2] < mp.mpf('.002')
    if abs(mp.im(n)) > 0:
        assert abs(J) > mp.mpf('1e-5')
        # Omission would retain the nonzero oscillating endpoint piece.
        assert abs((value+kappa**(-P)*J)-a(n)) > errors[2]
    # J cancels EXACTLY in the actual circle difference, even off lattice.
    hdef = mp.mpc('.4', '.1')
    j = N-hdef
    cutoff = 96
    value = (mp.exp(mp.pi*1j*(j-1))*kappa**(-P)
             *mp.fsum((-1)**ell*(ell+1)*(fresnel(P, N, j+N*ell-1)
                                            -fresnel(P, N, j+N*ell+1))
                      for ell in range(-cutoff, cutoff+1)))
    assert abs(value-K(hdef)) < mp.mpf('.002')
    for c in (-3, -1, 1, 2, 3):
        def channel(hh, cc):
            ell, b = cc-1, N*cc-hh
            return (mp.exp(mp.pi*1j*(N-hh-1))*kappa**(-P)*(-1)**ell*cc
                    *(fresnel(P, N, b-1)-fresnel(P, N, b+1)))
        assert abs(channel(hdef, c)-channel(-hdef, -c)) < mp.mpf('1e-65')
    return {'N': N, 'P': P, 'complex_n': str(n), 'paired_cutoff_errors': [float(e) for e in errors],
            'retained_endpoint_current_and_its_exact_beta_cancellation': True,
            'exact_charge_reflection': True}


def stationary_case(P, N, deficit, charge):
    mp.mp.dps = 90
    hdef = mp.mpf(deficit)
    b = N*charge-hdef
    j, ell = N-hdef, charge-1
    exact = (mp.exp(mp.pi*1j*(j-1))*(-1)**ell*charge
             *(fresnel(P, N, b-1)-fresnel(P, N, b+1)))
    leading = (2j*mp.exp(mp.pi*1j*mp.sign(P)/4)/mp.sqrt(2*abs(P)*N)
               *(-1)**((N+1)*ell)*charge*mp.sin(mp.pi*b/(P*N))
               *mp.exp(-mp.pi*1j*(b*b+1)/(2*P*N)))
    assert abs(leading) > 0
    assert abs(exact-leading)*N < 20*(1+abs(P))
    return {'P': P, 'N': N, 'color_deficit': float(hdef), 'charge': charge,
            'nonzero_sine_Gaussian_amplitude': float(abs(leading)),
            'N_times_endpoint_error': float(N*abs(exact-leading))}


if __name__ == '__main__':
    exact = [exact_case(N) for N in range(2, 10)]
    arithmetic = [gauss_case(N, P) for N in (2, 3, 4, 5, 6, 8, 9, 12, 16, 24)
                  for P in (-3, -2, -1, 0, 1, 2, 3, 6)]
    poisson = [poisson_case(N, P, n) for N, P, n in
               ((4, 1, 3), (5, 2, 4), (6, -2, 5),
                (7, 3, mp.mpc('5.3', '.1')), (5, 0, mp.mpc('3.2', '.1')))]
    stationary = [stationary_case(P, N, h, c) for P in (-3, 2, 5)
                  for N in (32, 64, 128) for h in (0, N/10) for c in (-1, 1)]
    result = {'status': 'PASS', 'full_physical_Gaussian_twists_odd_boxes_and_Weyl_folds': exact,
              'all_normal_arithmetic_and_entire_source_checks': arithmetic,
              'current_inclusive_Poisson_Fresnel_checks': poisson,
              'actual_nonzero_local_charge_asymptotics': stationary,
              'scope': 'Exact original chirp, normal current and core Weyl folding; no filled-knot exterior survival or endpoint remainder deletion.'}
    Path(__file__).with_name('actual_coherent_filling_gaussian_chirp_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(exact)} full physical chirp/fold levels; {len(arithmetic)} normal/arithmetic families; {len(poisson)} Poisson/current families; {len(stationary)} local charge amplitudes')
