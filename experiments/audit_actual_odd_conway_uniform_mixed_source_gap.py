#!/usr/bin/env python3
"""Certificates for the supporting-plane alias bound.

The general source estimate is proved in the note. The exact algebra
below verifies its port normalization, universal positive margin and
Legendre derivative. Numerical samples are diagnostics only.
"""
from fractions import Fraction
from pathlib import Path
import json
import math

import mpmath as mp
import sympy as sp


def exact_certificates():
    X, z, a = sp.symbols('X z a', positive=True)
    Y = 1/(4*X*X-1)
    assert sp.cancel(1-Y-2*(2*X*X-1)/(4*X*X-1)) == 0
    # The elementary positive-integral certificate for pi<22/7.
    integral = sp.integrate(z**4*(1-z)**4/(1+z*z), (z, 0, 1))
    assert sp.simplify(integral-(sp.Rational(22, 7)-sp.pi)) == 0
    # exp(7/10)>2 from a strict finite positive partial sum.
    exponential_lower = sum(Fraction(7, 10)**k/math.factorial(k) for k in range(5))
    assert exponential_lower > 2
    margin = Fraction(56, 99)-Fraction(21, 40)
    assert margin == Fraction(161, 3960) and margin > 0
    # Envelope differentiation with the actual critical identities.
    u, s, second, velocity = sp.symbols('u s second velocity')
    g, k = sp.Function('g'), sp.Function('k')
    I = g(a)+s*(u-a)-k(u)
    derivative = sp.diff(I, a)+second*sp.diff(I, s)+velocity*sp.diff(I, u)
    reduced = sp.simplify(derivative.subs({sp.diff(g(a), a): s,
                                         sp.diff(k(u), u): s}))
    assert sp.simplify(reduced-second*(u-a)) == 0
    return {'proper_seed_Y_less_than_one_equivalence': 'X>1/sqrt(2), using X>1/2',
            'pi_upper_bound_positive_integral': str(integral),
            'exp_7_over_10_strict_lower_partial_sum': str(exponential_lower),
            'universal_margin_strict_lower_bound': str(margin),
            'Legendre_gap_derivative': 'g_second(a)*(u(a)-a)'}


def profile_diagnostics():
    with mp.workdps(50):
        J = lambda t: -mp.im(mp.polylog(2, mp.exp(2j*mp.pi*t)))/(2*mp.pi)
        g = lambda t: J(2*t)-4*J(t)
        a0 = mp.atan(mp.sqrt(2))/mp.pi
        c0 = 2*mp.catalan/mp.pi-mp.mpf(3)/4*mp.log(2)
        smallest = mp.inf
        count = 0
        for index in range(21):
            a = mp.mpf(1)/4+(a0-mp.mpf(1)/4)*index/20
            slope = 2*mp.log(mp.cot(mp.pi*a))
            maximizer = 2/mp.pi*mp.asin(min(mp.mpf(1), mp.exp(-slope)/2))
            gap = g(a)+slope*(maximizer-a)+2*J(maximizer/2)
            assert gap > c0
            for j in range(41):
                u = mp.mpf(j)/40
                slack = g(a)+slope*(u-a)+2*J(u/2)
                assert slack >= c0
                smallest = min(smallest, slack)
                count += 1
        return {'tangent_samples': count, 'minimum_sampled_gap': mp.nstr(smallest, 25),
                'proved_uniform_margin_c0': mp.nstr(c0, 25),
                'scope': 'diagnostic; uniform strict inequality is proved analytically'}


if __name__ == '__main__':
    result = {'status': 'PASS', 'exact_certificates': exact_certificates(),
              'profile_diagnostics': profile_diagnostics(),
              'scope': 'Supporting-plane source certificate for C(FG); C(A) excluded. Full all-color core recurrence is an explicit independent premise. No odd-coupon long-filling theorem.'}
    Path(__file__).with_name('actual_odd_conway_uniform_mixed_source_gap_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS exact port/Legendre/positive-margin certificates; 861 profile diagnostics')
