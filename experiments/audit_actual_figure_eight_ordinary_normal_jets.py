#!/usr/bin/env python3
"""Actual figure-eight ordinary q-jets, activated root products and sharp top jet."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def source_jets(N, color, order):
    q = mp.exp(mp.pi*1j/N)
    product = [mp.mpc(1)]+[mp.mpc(0)]*order
    total = product.copy()
    for r in range(1, color):
        factor = []
        for t in range(order+1):
            if t == 0:
                value = (mp.mpf(0) if color+r == N else
                         -4*mp.sin(mp.pi*(color+r)/N)*mp.sin(mp.pi*(color-r)/N))
            else:
                value = (mp.binomial(2*color, t)*q**(2*color)
                         +mp.binomial(-2*color, t)*q**(-2*color)
                         -mp.binomial(2*r, t)*q**(2*r)
                         -mp.binomial(-2*r, t)*q**(-2*r))
            factor.append(value)
        product = [mp.fsum(product[a]*factor[t-a] for a in range(t+1))
                   for t in range(order+1)]
        total = [a+b for a, b in zip(total, product)]
    return total


def factorials(N):
    Q = mp.exp(2j*mp.pi/N)
    fac = [mp.mpf(1)]
    for k in range(1, N):
        fac.append(fac[-1]*abs(1-Q**k))
    return Q, fac


def exact_small_polynomials():
    q, t = sp.symbols('q t')
    rows = []
    for color in range(1, 7):
        product = sp.Integer(1)
        polynomial = product
        for r in range(1, color):
            product *= q**(2*color)+q**(-2*color)-q**(2*r)-q**(-2*r)
            polynomial += product
        derivatives = [sp.lambdify(q, sp.diff(polynomial, q, order)/sp.factorial(order), 'mpmath')
                       for order in range(3)]
        N = color+3
        root = mp.exp(mp.pi*1j/N)
        actual = source_jets(N, color, 2)
        for order in range(3):
            expected = root**order*derivatives[order](root)
            assert abs(actual[order]-expected) < mp.mpf('1e-70')*max(1, abs(expected))
        rows.append({'color': color, 'N': N, 'exact_Laurent_Taylor_orders': [0, 1, 2]})
    return rows


def product_checks():
    count = 0
    for N in range(3, 25):
        Q, fac = factorials(N)
        for j in range(1, N):
            product = mp.mpf(1)
            for k in range(0, j):
                if k:
                    if j+k != N:
                        product *= abs(-4*mp.sin(mp.pi*(j+k)/N)*mp.sin(mp.pi*(j-k)/N))
                    # The one root-zero is REMOVED, not multiplied in.
                if k < min(j, N-j):
                    expected = fac[j+k]/(abs(1-Q**j)*fac[j-k-1])
                else:
                    m = N-j
                    expected = fac[k+m]*fac[k-m]/(abs(1-Q**m)*abs(1-Q**(2*m)))
                assert abs(product-expected) < mp.mpf('1e-70')*max(1, abs(expected))
                count += 1
    return {'all_color_nonzero_product_certificates': count}


def endpoint_checks():
    Delta = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))/mp.pi
    rows = []
    for N in [8, 16, 32, 64, 128, 256, 512]:
        mp.mp.dps = max(100, N//2+80)
        Q, fac = factorials(N)
        positive = mp.fsum(fac[k-1]*fac[k+1]/fac[2] for k in range(1, N-1))
        exact = -2*N*(Q-Q**-1)*positive
        actual = source_jets(N, N-1, 1)[1]
        error = abs(actual-exact)/max(1, abs(exact))
        assert error < mp.mpf('1e-70')
        leading = -1j*N**mp.mpf('3.5')/(mp.pi*3**mp.mpf('.25'))*mp.exp(N*Delta)
        ratio = actual/leading
        assert abs(ratio-1) < mp.mpf(10)/N
        rows.append({'N': N, 'exact_positive_first_jet_relative_error': float(error),
                     'ratio_to_proved_leading_asymptotic': [float(mp.re(ratio)), float(mp.im(ratio))],
                     'first_jet_log_modulus_over_N': float(mp.log(abs(actual))/N)})
    return rows


def all_jet_and_midpoint_checks():
    rows = []
    Delta = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))/mp.pi
    for N in [12, 24, 40, 64]:
        mp.mp.dps = 120
        maximum = [mp.mpf(0)]*4
        for j in range(1, N):
            jets = source_jets(N, j, 3)
            for r, value in enumerate(jets):
                maximum[r] = max(maximum[r], abs(value))
                assert abs(value) <= N**(8+4*r)*mp.exp(N*Delta)
        mid = source_jets(N, (N+1)//2, 3)
        rows.append({'N': N, 'all_ordinary_max_jet_log_rates': [float(mp.log(max(1, a))/N) for a in maximum],
                     'midpoint_fixed_jets': [[float(mp.re(a)), float(mp.im(a))] for a in mid]})
    for N in [128, 256, 512]:
        mp.mp.dps = max(120, N//3+60)
        value = source_jets(N, N//2, 1)[1]
        rows.append({'N': N, 'midpoint_first_jet_log_rate_diagnostic': float(mp.log(abs(value))/N)})
    return rows


def main():
    mp.mp.dps = 100
    data = {'status': 'PASS', 'actual_small_Laurent_polynomials': exact_small_polynomials(),
            'uniform_root_product_identities': product_checks(),
            'sharp_endpoint_normal_jet': endpoint_checks(),
            'all_fixed_jets_and_midpoint': all_jet_and_midpoint_checks(),
            'scope': 'Actual figure-eight q-jets and all-level product proofs. The broad polynomial k-plat window is separately proved/audited in ordinary_color_macroscopic_normal_jet_window; no broad sharp volume conclusion is inferred.'}
    Path(__file__).with_name('actual_figure_eight_ordinary_normal_jets_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS exact actual Laurent jets, all-color nonzero products, 7 sharp endpoint levels, '
          'uniform fixed-order jets and midpoint diagnostics')


if __name__ == '__main__':
    main()
