#!/usr/bin/env python3
"""Numerically check the exact rational contour against the physical grid.

Includes partial grids and frequencies larger than N. Mathematical proofs
are in notes/research_exact_complete_trace_contour.md.
"""
import argparse
import json

import mpmath as mp


def check_case(level, power, degree, removed_pairs, height):
    eta = (-1)**(level-1)
    phase = mp.exp(mp.j*mp.pi*power*(level-1)**2/(4*level))
    quadratic = mp.mpf(power*level)/(4*mp.pi)
    boundary = mp.pi-2*mp.pi*removed_pairs/level

    def g(t):
        return mp.sin(t)*mp.cos(degree*t)*mp.exp(mp.j*quadratic*t*t)

    def derivative(t):
        return (
            mp.cos(t)*mp.cos(degree*t)
            - degree*mp.sin(t)*mp.sin(degree*t)
            + 2*mp.j*quadratic*t*mp.sin(t)*mp.cos(degree*t)
        )*mp.exp(mp.j*quadratic*t*t)

    nodes = [2*mp.pi*((mp.mpf(level)-1)/2-j)/level
             for j in range(removed_pairs, level-removed_pairs)]
    direct = eta*phase*sum(derivative(t) for t in nodes)

    def horizontal(x):
        t = x-mp.j*height
        r = mp.exp(-mp.j*level*t)
        return g(t)*r/(1-eta*r)**2

    horizontal_integral = mp.quad(horizontal, [-boundary, 0, boundary])
    endpoint_integral = mp.quad(
        lambda v: g(boundary+mp.j*v)/(4*mp.cosh(level*v/2)**2),
        [-height, 0, height])
    contour = (-level**2*phase/(mp.pi*mp.j)*horizontal_integral
               + eta*level**2*phase/mp.pi*endpoint_integral)
    return abs(contour-direct)/(1+abs(direct))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=60)
    parser.add_argument('--levels', type=int, nargs='+', default=[3, 4, 5, 8])
    parser.add_argument('--powers', type=int, nargs='+', default=[-3, 0, 1, 2, 3])
    parser.add_argument('--height', default='0.17')
    args = parser.parse_args()
    if args.digits < 40 or any(n < 3 for n in args.levels):
        parser.error('require at least 40 digits and all levels >= 3')
    mp.mp.dps = args.digits
    height = mp.mpf(args.height)
    if height <= 0:
        parser.error('height must be positive')
    worst = mp.mpf(0)
    worst_case = None
    count = 0
    for level in args.levels:
        for power in args.powers:
            for degree in (0, 2, level+2):
                for removed_pairs in (0, 1):
                    error = check_case(level, power, degree,
                                       removed_pairs, height)
                    count += 1
                    if error > worst:
                        worst, worst_case = error, [level, power, degree, removed_pairs]
    tolerance = mp.mpf(10)**(-3*args.digits//5)
    passed = worst < tolerance
    print(json.dumps({
        'cases': count,
        'decimal_digits': args.digits,
        'height': str(height),
        'maximum_relative_error': mp.nstr(worst, 14),
        'worst_case_N_n_degree_removed_pairs': worst_case,
        'relative_tolerance': mp.nstr(tolerance, 5),
        'passed': passed,
        'scope': 'numerical finite contour identity, including partial grids and normal derivatives',
    }, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
