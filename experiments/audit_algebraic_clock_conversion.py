#!/usr/bin/env python3
"""Exact algebraic-clock conversion; not a knot or meridian operator."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import mpmath as mp


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def ipow(k):
    return [(1, 0), (0, 1), (-1, 0), (0, -1)][k % 4]


def middle_sum(H, r):
    out = (0, 0)
    for m in range(r, H-r):
        out = add(out, mul((comb(H, m), 0), ipow(m)))
    return out


def exact_case(r):
    H, n = 16*r, 14*r
    # Integer scaled matrices n*H*T_j; no floating point in the test.
    A, B, D = 1, (0, 0), (1, 0)
    for j in range(n):
        aa, dd = n*(r+j), n*(H-r-j)
        B = add(mul((aa, 0), B), mul((H, 0), D))
        A *= aa
        D = mul((0, dd), D)
    scale = (n*H)**n
    actual = F(B[0], scale), F(B[1], scale)
    C = F(factorial(H-r-1)*factorial(H-r),
          n*H**(n-1)*factorial(H))
    expected = mul((C, 0), mul(ipow(-r), middle_sum(H, r)))
    assert actual == expected
    u0, u1 = (F(0), F(0)), (F(1, n), F(0))
    for j in range(n-1):
        x, xp = F(r+j, H), F(r+j+1, H)
        u2 = add(mul((xp, 1-x), u1), mul((0, -x*(1-x)), u0))
        u0, u1 = u1, u2
    assert u1 == actual
    return {'r': r, 'steps': n, 'exact_product_and_companion': True}


def numerical_cases():
    mp.mp.dps = 80
    delta = mp.mpf(1)/16
    entropy = -delta*mp.log(delta)-(1-delta)*mp.log(1-delta)
    gap = (mp.log(2)/2-entropy)/(1-2*delta)
    I = -1+((1-delta)*mp.log(1-delta)-delta*mp.log(delta))/(1-2*delta)
    Gamma = I+gap
    assert gap > 0
    cases = []
    for r in [1, 4, 16, 64, 256]:
        H, n = 16*r, 14*r
        sr, si = middle_sum(H, r)
        logabs = mp.log(mp.hypot(mp.mpf(sr), mp.mpf(si)))
        logC = (mp.loggamma(H-r)+mp.loggamma(H-r+1)-mp.loggamma(H+1)
                -(n-1)*mp.log(H)-mp.log(n))
        rate = (logC+logabs)/n
        # Full sum is real and positive for H divisible by sixteen.
        full = 2**(H//2)
        tail_size = mp.hypot(mp.mpf(sr-full), mp.mpf(si))
        tail_bound = (2*r+1)*mp.exp(H*entropy)
        assert tail_size <= tail_bound
        assert abs(rate-Gamma) < 3*mp.log(n)/n
        cases.append({'r': r, 'rate': str(rate),
                      'proven_rate': str(Gamma),
                      'tail_bound_verified': True})
    return {'branch_action': str(I), 'conversion_rate': str(Gamma),
            'strict_gap': str(gap), 'samples': cases}


def main():
    data = {'status': 'PASS', 'exact': [exact_case(r) for r in [1, 2, 3, 4]],
            'asymptotic': numerical_cases(),
            'scope': 'Polynomial clock recurrence only; no knot or quantum-meridian operator asserted.'}
    Path(__file__).with_name('algebraic_clock_conversion_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
