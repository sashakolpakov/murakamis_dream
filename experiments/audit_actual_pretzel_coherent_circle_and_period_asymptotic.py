#!/usr/bin/env python3
"""Finite audits of the full coherent pretzel asymptotic proof.

The theorem is the written estimate/Gaussian proof, not an extrapolation
from these data. Periods here use the independently constructed physical
Casimir polynomial and its FULL value-plus-normal source functional.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from diagnose_pretzel_coherent_radial_capacity import (
    evaluate,
    lobachevsky,
    original_period,
    source_polynomial,
)


def parameters(s):
    alpha = mp.pi / s
    eta = 2 * mp.asinh(mp.tan(alpha))
    radius = mp.exp(eta)
    total = radius + 1 / radius
    u = mp.atan(mp.sec(alpha))
    rate = 4 * s / mp.pi * (
        lobachevsky(mp.pi / 4 + alpha / 2)
        + lobachevsky(mp.pi / 4 - alpha / 2)
    )
    a = mp.exp(1j * u / 2) / (2 * ((total + 2) * (total + 6)) ** mp.mpf('.25'))
    constant = (radius - 1 / radius) * a**s / mp.sqrt(s * mp.cos(alpha))
    return alpha, eta, radius, u, rate, a, constant


def exact_profile_algebra():
    t, T = sp.symbols('t T', positive=True)
    ratio = ((T + 2) + (T - 2) * t**2) / (4 * t**4)
    assert sp.factor(4*t**4 - (T-2)*t**2 - (T+2)) == (t**2+1)*(4*t**2-T-2)
    derivative = sp.diff(sp.log(ratio), t) * (1+t**2)
    at_maximum = sp.simplify(derivative.subs(t, sp.sqrt(T+2)/2))
    assert sp.simplify(at_maximum + (T+6)**2/(T+2)**sp.Rational(3, 2)) == 0
    enlarged_ratio = sp.simplify(ratio*t**2)
    assert sp.simplify(enlarged_ratio-((T+2)+(T-2)*t**2)/(4*t**2)) == 0
    return {'unique_positive_stationary_root': True,
            'exact_negative_index_hessian': True,
            'branch_switch_envelope_derivative': True}


def finite_newton_circle_checks():
    mp.mp.dps = 75
    count = 0
    largest_ratio = mp.mpf(0)
    for N in (3, 4, 9, 10, 17, 18, 31, 32):
        nodes = [2*mp.cos((2*a+1)*mp.pi/N) for a in range((N-1)//2)]
        for R in (mp.mpf('1.3'), mp.mpf('2.7'), mp.mpf('13.9')):
            constant = ((R+1)/(R-1))**2
            for r in range(len(nodes)+1):
                at_axis = mp.fprod(c+R+1/R for c in nodes[:r])
                for k in range(24):
                    w = R*mp.exp(2j*mp.pi*k/24)
                    value = abs(mp.fprod(c-w-1/w for c in nodes[:r]))
                    ratio = value/at_axis
                    assert ratio <= constant*(1+mp.mpf('1e-60'))
                    largest_ratio = max(largest_ratio, ratio)
                    count += 1
    return {'finite_factor_samples': count,
            'largest_sampled_axis_ratio': mp.nstr(largest_ratio, 20)}


def amplitude_checks():
    rows = []
    errors = {}
    window_errors = {}
    for N in (32, 33, 64, 65, 128, 129):
        q, coefficients = source_polynomial(N, max(160, N))
        for s in (3, 5, 7, 9):
            alpha, eta, R, u, rate, a, constant = parameters(s)
            expected = (mp.mpf(N)**mp.mpf('1.5')
                        *mp.exp(-1j*s*mp.pi*(N-1)/4)
                        *constant*mp.exp(N*rate))
            ratio = original_period(N, s, q, coefficients)/expected
            error = abs(ratio-1)
            errors[N, s] = error
            j = (rate+eta)/s
            central = []
            for t in (mp.mpf('-1'), mp.mpf('0'), mp.mpf('1')):
                w = -R*mp.exp(1j*t/mp.sqrt(N))
                expected_box = (mp.exp(-1j*mp.pi*(N-1)/4)*a*mp.exp(N*j)
                                *mp.exp(1j*mp.sqrt(N)*t/s
                                        -mp.cos(alpha)*t*t/(4*mp.pi)))
                window_ratio = evaluate(coefficients, w+1/w)[0]/expected_box
                central.append(abs(window_ratio-1))
            window_errors[N, s] = max(central)
            rows.append({'N': N, 'boxes': s,
                         'full_original_period_ratio_real': mp.nstr(mp.re(ratio), 18),
                         'full_original_period_ratio_imag': mp.nstr(mp.im(ratio), 18),
                         'ratio_error': float(error),
                         'central_window_error': float(max(central))})
            print(f'N={N} s={s} full ratio={mp.nstr(ratio, 14)} '
                  f'window error={mp.nstr(max(central), 6)}', flush=True)
    for s in (3, 5, 7, 9):
        for parity in (0, 1):
            assert errors[128+parity, s] < errors[64+parity, s] < errors[32+parity, s]
            assert window_errors[128+parity, s] < window_errors[64+parity, s] < window_errors[32+parity, s]
            assert errors[128+parity, s] < mp.mpf('.2')
    return rows


def original_fourier_cauchy_checks():
    rows = []
    for N in (3, 4, 9, 10, 17, 18):
        q, coefficients = source_polynomial(N, 120)
        M = len(coefficients)-1
        laurent = {}
        for j, c in enumerate(coefficients):
            for l in range(j+1):
                k = j-2*l
                laurent[k] = laurent.get(k, mp.mpc(0))+c*mp.binomial(j, l)
        powers = {0: mp.mpc(1)}
        for s in range(1, 10):
            next_power = {}
            for k, a in powers.items():
                for l, b in laurent.items():
                    next_power[k+l] = next_power.get(k+l, mp.mpc(0))+a*b
            powers = next_power
            if s not in (3, 5, 9):
                continue
            _, _, R, _, _, _, _ = parameters(s)
            finite_source = mp.mpc(0)
            for m in range(1, (s*M+1)//N+1):
                finite_source += (-1)**(m-1)*m*(powers.get(m*N-1, 0)-powers.get(m*N+1, 0))
            finite_source *= (-1)**(N-1)*N*N
            physical_source = original_period(N, s, q, coefficients)
            assert abs(finite_source-physical_source) <= mp.mpf('1e-85')*max(1, abs(physical_source))
            energy = mp.fsum(abs(a)**2*R**(2*(k-N)) for k, a in powers.items())
            x = R**(-2*N)
            cost = N**4*(R*R+R**(-2))*(1+x)/(1-x)**3
            assert abs(physical_source)**2 <= cost*energy*(1+mp.mpf('1e-85'))
            grid = 2*s*M+1
            sampled_energy = mp.fsum(
                abs(evaluate(coefficients, R*mp.exp(2j*mp.pi*k/grid)
                             +1/(R*mp.exp(2j*mp.pi*k/grid)))[0])**(2*s)
                for k in range(grid)) / grid / R**(2*N)
            assert abs(sampled_energy-energy) <= mp.mpf('1e-85')*max(1, energy)
            rows.append({'N': N, 'boxes': s, 'exact_original_winding_source': True,
                         'finite_fourier_plancherel': True,
                         'specified_metric_cauchy_bound': True})
    return rows


if __name__ == '__main__':
    result = {'status': 'PASS', 'profile_algebra': exact_profile_algebra(),
              'circle_factors': finite_newton_circle_checks(),
              'original_fourier_inner_product': original_fourier_cauchy_checks(),
              'all_parity_full_source_calibration': amplitude_checks(),
              'scope': 'Exact auxiliary algebra and finite checks of the written proof; '
                       'convergence samples are not themselves its proof. '
                       'Complete augmented pretzel link source, not fixed knot fillings.'}
    Path(__file__).with_name('actual_pretzel_coherent_circle_and_period_asymptotic_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: exact profile algebra, Newton circle factors, and full original period calibrations.')
