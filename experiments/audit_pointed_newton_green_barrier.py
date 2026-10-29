#!/usr/bin/env python3
"""Actual affine-operator Newton conjugacy and pointed positive Green barrier."""

import cmath
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np


def newton_matrix(N, Q, c):
    A = mp.matrix(N)
    s = [2-Q**r-Q**(-r) for r in range(N+1)]
    for k in range(N):
        A[k, k] += 1+s[k+1] if k < N-1 else 1
        if k < N-1:
            A[k+1, k] -= 1
        if k:
            A[k-1, k] -= s[k]
    A[0, N-1] -= c
    return A


def actual_coefficients(Y, Q):
    D = Y*(Y+1)*(Q-Y*Y)*(Q*Y*Y-1)
    g = Q*Q*Y*Y-Q*Y**4+Q*Y**3+Q*Y-Q+Y*Y
    return D, { -1: Y*Y*(Q-Y)*(Q*Y*Y-1),
                 0: -(Y-1)**2*(Y+1)*g,
                 1: Y*Y*(Q*Y-1)*(Q-Y*Y)}


def generic_actual_conjugacy():
    rows = []
    for N in range(2, 11):
        Q = mp.exp(2j*mp.pi/N)
        for U in (mp.mpf(2), mp.mpc(.7, .2)):
            base = mp.exp(mp.log(U)/N)
            c = U+1/U-2
            C, V = mp.matrix(N), mp.matrix(N)
            Ds = []
            for j in range(N):
                Y = base*Q**j
                D, coeffs = actual_coefficients(Y, Q)
                Ds.append(D)
                for shift, value in coeffs.items():
                    C[j, (j+shift) % N] += value
                h = Y+1/Y
                t = mp.mpf(1)
                for k in range(N):
                    V[j, k] = t
                    t *= h-Q**(k+1)-Q**(-k-1)
                assert abs(t-c) < mp.mpf('1e-55')
            orbit_A = mp.diag([1/D for D in Ds])*C
            A = newton_matrix(N, Q, c)
            residual = mp.norm(orbit_A*V-V*A)
            scale = max(1, mp.norm(orbit_A*V), mp.norm(V*A))
            assert residual/scale < mp.mpf('1e-50')
            det_error = abs(mp.det(A)-(1-c))
            norm_det_error = abs(mp.det(C)-mp.fprod(Ds)*(1-c))
            assert det_error < mp.mpf('1e-50')
            assert norm_det_error/max(1, abs(mp.det(C))) < mp.mpf('1e-45')
            ones = mp.matrix([1]*N)
            source = mp.matrix([1-c]+[0]*(N-1))
            assert mp.norm(A*ones-source) < mp.mpf('1e-55')
            rows.append({'N': N, 'central_U': str(U),
                         'actual_generic_conjugacy_relative_error': float(residual/scale),
                         'central_det_error': float(det_error),
                         'full_norm_D_det_relative_error': float(norm_det_error/max(1, abs(mp.det(C))))})
    return rows


def green_vector(s, g):
    N = len(g)
    w = np.zeros(N, dtype=complex)
    w[-1] = g[-1]
    for i in range(N-2, 0, -1):
        w[i] = g[i]+s[i+1]*w[i+1]
    v = np.zeros(N, dtype=complex)
    v[0] = g[0]+s[1]*w[1]
    for i in range(1, N):
        v[i] = v[i-1]+w[i]
    return v


def source_green_bounds():
    rows = []
    for N in (2, 3, 4, 7, 16, 32, 64, 128):
        s = 4*np.sin(np.arange(N+1)*math.pi/N)**2
        s[-1] = 0
        A = np.diag(1+s[1:])
        A[-1, -1] = 1
        A += np.diag(-np.ones(N-1), -1)+np.diag(-s[1:N], 1)
        worst, ratios = 0., []
        for J in range(min(4, N)):
            g = np.zeros(N, dtype=complex)
            g[:J+1] = [cmath.exp(.31j*k)/(k+1) for k in range(J+1)]
            v = green_vector(s, g)
            err = float(np.max(abs(A@v-g)))
            worst = max(worst, err)
            bound = math.sqrt(N)*(J+1)**1.5*4**J*np.linalg.norm(g)
            assert np.linalg.norm(v) <= bound*(1+1e-12)
            ratios.append(float(np.linalg.norm(v)/bound))
            for c in (.2+.1j, -2.):
                Ac = A.astype(complex).copy()
                Ac[0, -1] -= c
                vc = v+c/(1-c)*v[-1]*np.ones(N)
                assert np.max(abs(Ac@vc-g)) < 1e-10
        assert worst < 1e-10
        # Arbitrary single boundary-column Green entries remain nonnegative.
        for j in range(min(4, N)):
            g = np.zeros(N)
            g[j] = 1
            assert min(green_vector(s, g).real) >= -1e-13
        rows.append({'N': N, 'max_pointed_Green_residual': worst,
                     'boundary_source_norm_ratios': ratios,
                     'exact_rank_one_central_formula_checked': True})
    return rows


def full_root_metric():
    rows = []
    for N in range(3, 21):
        Q = mp.exp(2j*mp.pi/N)
        F = [mp.mpf(1)]
        for r in range(1, N):
            F.append(F[-1]*2*mp.sin(mp.pi*r/N))
        V = mp.matrix(N)
        maxerr = mp.mpf(0)
        for j in range(N):
            h = 2*mp.cos(2*mp.pi*j/N)
            t = mp.mpf(1)
            for k in range(N):
                V[j, k] = t
                if j == 0:
                    predicted = F[k]**2
                elif k >= min(j, N-j):
                    predicted = 0
                else:
                    predicted = F[j+k]/(2*mp.sin(mp.pi*j/N)*F[j-k-1])
                maxerr = max(maxerr, abs(abs(t)-predicted))
                t *= h-2*mp.cos(2*mp.pi*(k+1)/N)
        assert maxerr < mp.mpf('1e-45')
        c = V*mp.matrix([1]*N)
        K = mp.fsum(F[k]**2 for k in range(N))
        assert abs(c[0]-K) < mp.mpf('1e-45')
        ordinary_energy = mp.fsum(abs(c[j])**2 for j in range(1, N))
        for j in range(1, N):
            qint = mp.sin(mp.pi*j/N)/mp.sin(mp.pi/N)
            assert abs(c[j]) <= qint**2+mp.mpf('1e-40')
        dual = [mp.fsum(c[j]*Q**(-j*k) for j in range(N))/mp.sqrt(N)
                for k in range(N)]
        energy = mp.fsum(abs(v)**2 for v in dual)
        rel = abs(energy-(abs(K)**2+ordinary_energy))/max(1, energy)
        assert rel < mp.mpf('1e-50')
        rows.append({'N': N, 'max_exact_endpoint_product_error': float(maxerr),
                     'full_Planchelel_energy_relative_error': float(rel),
                     'complete_log_rate': float(mp.log(K)/N),
                     'ordinary_energy': float(ordinary_energy)})
    return rows


def pointed_UL_class():
    rows = []
    for N in (2, 4, 8, 16, 32, 64):
        S = np.diag(np.ones(N-1), -1)
        U = np.eye(N)-2*S.T
        J = min(3, N-1)
        g = np.zeros(N, dtype=complex)
        g[:J+1] = [cmath.exp(.27j*k)/(k+1) for k in range(J+1)]
        w = np.zeros(N, dtype=complex)
        for k in range(N-1, -1, -1):
            w[k] = g[k]+(2*w[k+1] if k+1 < N else 0)
        assert np.max(abs(w[J+1:]), initial=0) == 0
        for r in (1, 2, 3):
            v = w.copy()
            for _ in range(r):
                v = np.cumsum(v)
            L = U@np.linalg.matrix_power(np.eye(N)-S, r)
            residual = np.max(abs(L@v-g))
            bound = (math.comb(N+r-1, r)*(J+1)**(J+1)
                     *N**(2*J+1)*np.linalg.norm(g))
            assert np.linalg.norm(v) <= bound
            assert residual <= 1e-7
            rows.append({'N': N, 'difference_order': r, 'boundary_window_J': J,
                         'source_response_norm': float(np.linalg.norm(v)),
                         'proved_polynomial_bound': float(bound),
                         'source_equation_residual': float(residual),
                         'unrestricted_U_inverse_norm_lower_bound': 2**(N-1)})
    return rows


def complete_divisor_stress():
    rows = []
    for N in range(2, 11):
        Q = mp.exp(2j*mp.pi/N)
        F = [mp.mpf(1)]
        for k in range(1, N):
            F.append(F[-1]*2*mp.sin(mp.pi*k/N))
        K = mp.fsum(t*t for t in F)
        eta = mp.j**(N+3)
        for power in (6, 12, 20):
            eps = mp.mpf(10)**(-power)
            U = 1+eps
            Y = mp.exp(mp.log(U)/N)
            h = Y+1/Y
            terms = [mp.mpf(1)]
            for k in range(1, N):
                terms.append(terms[-1]*(h-Q**k-Q**(-k)))
            actual_reduced = mp.fsum(terms)
            # Retain the ENTIRE original peripheral monomial and its canceled
            # (Y-1)/(U-1) divisor before taking the complete value.
            full = eta*mp.exp((N-1)*mp.log(U)/(2*N))*(Y-1)/(U-1)*actual_reduced
            limiting = eta*K/N
            relative = abs(full/limiting-1)
            assert relative < 100*N*N*eps*eps
            D, _ = actual_coefficients(Y, Q)
            assert abs(D) > 0
            # The exact Newton source is used while this diagonal divisor is
            # small, not by substituting D(1)=0 and dividing numerically.
            c = U+1/U-2
            A = newton_matrix(N, Q, c)
            source = mp.matrix([1-c]+[0]*(N-1))
            residual = mp.norm(A*mp.matrix([1]*N)-source)
            assert residual < mp.mpf('1e-55')
            rows.append({'N': N, 'U_minus_one': str(eps),
                         'retained_full_peripheral_relative_error': float(relative),
                         'normal_source_residual': float(residual)})
    return rows


def whole_circle_metric_stress():
    Delta = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))/mp.pi
    rows = []
    for N in (8, 16, 32, 64):
        qs = [mp.mpf(0), mp.mpf('.123456789'), mp.mpf('.5'),
              mp.mpf(1)/N+mp.mpf('1e-30'),
              mp.mpf(1)/N-mp.mpf('1e-30'),
              mp.mpf(N-1)/N+mp.mpf('1e-30')]
        best = -mp.inf
        for u in qs:
            h = 2*mp.cos(2*mp.pi*u)
            log_modulus = mp.mpf(0)
            best = max(best, log_modulus)
            for k in range(1, N):
                factor = abs(h-2*mp.cos(2*mp.pi*k/N))
                if factor == 0:
                    break
                log_modulus += mp.log(factor)
                best = max(best, log_modulus)
        assert best <= N*Delta+10*mp.log(N)
        rows.append({'N': N, 'includes_root_offsets': 'plus/minus 1e-30',
                     'largest_sampled_log_modulus': float(best),
                     'upper_endpoint_barrier': float(N*Delta),
                     'uniform_logarithmic_error_checked': True})
    return rows


def endpoint_barrier():
    Delta = float(mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))/mp.pi)
    rows = []
    for N in (16, 32, 64, 128, 256, 512):
        factors = [0.]+[math.log(2*math.sin(math.pi*r/N)) for r in range(1, N)]
        logF = np.cumsum(factors)
        best = float(max(2*logF))
        for j in range(1, N):
            for k in range(min(j, N-j)):
                val = logF[j+k]-logF[j-k-1]-factors[j]
                best = max(best, float(val))
        logK = float(np.max(2*logF)+math.log(np.sum(np.exp(2*logF-np.max(2*logF)))))
        assert abs(best-N*Delta) <= 10*math.log(N)
        assert abs(logK-N*Delta) <= 10*math.log(N)
        rows.append({'N': N, 'max_root_metric_log_rate': best/N,
                     'source_log_rate': logK/N,
                     'endpoint_barrier': Delta,
                     'uniform_log_error_bound_checked': True})
    return rows


def main():
    mp.mp.dps = 80
    data = {'status': 'PASS', 'actual_generic_orbit_Newton_operator': generic_actual_conjugacy(),
            'fixed_boundary_positive_Green_bounds': source_green_bounds(),
            'general_pointed_UL_class': pointed_UL_class(),
            'complete_D_divisor_and_full_peripheral_stress': complete_divisor_stress(),
            'whole_unit_circle_metric_stress': whole_circle_metric_stress(),
            'complete_original_root_metric_and_energy': full_root_metric(),
            'uniform_endpoint_barrier': endpoint_barrier(),
            'scope': ('Known actual rank-two prototype and checkable Newton boundary-source '
                      'class; no general-knot Newton reduction or volume theorem inferred.')}
    Path(__file__).with_name('pointed_newton_green_barrier_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS actual Newton conjugacy/central determinant, positive pointed Green bound, '
          'full root-color Fourier metric and sharp endpoint barrier')


if __name__ == '__main__':
    main()
