#!/usr/bin/env python3
"""Reproduce the finite checks in research_terminal_powers_qbinomial.md.

The mathematical proofs are in the note. These numerical checks compare
independent finite formulas and detect scalar/index errors; they are not
proofs of asymptotic estimates.
"""
import argparse
import json

import mpmath as mp


def finite_data(level):
    q = mp.exp(mp.j * mp.pi / level)
    Q = q * q
    sine, factorial = [mp.mpf(1)], [mp.mpc(1)]
    for k in range(1, level):
        sine.append(sine[-1] * 2 * mp.sin(mp.pi * k / level))
        factorial.append(factorial[-1] * (1 - Q**k))
    kappa = mp.exp(mp.j * mp.pi * (level - 1)**2 / (2 * level))
    crossing, transform, paired = [], [], []
    for k in range(level):
        crossing.append([
            kappa * (-1)**k * q**(k*(j+1)) * sine[k]
            / (sine[j] * sine[k-j]) for j in range(k+1)
        ])
        transform.append([
            (-1)**j * Q**(j*(j+1)//2) / factorial[k-j]
            for j in range(k+1)
        ])
        paired.append([
            Q**(j*(j+1)) * factorial[k]
            / (factorial[j] * factorial[k-j]) for j in range(k+1)
        ])
    diagonal = [(-q)**k * factorial[k] for k in range(level)]
    return q, Q, sine, factorial, kappa, crossing, transform, paired, diagonal


def multiply(matrix, vector):
    return [sum(value * vector[j] for j, value in enumerate(row))
            for row in matrix]


def paired_power(power, data):
    q, _, _, factorial, kappa, _, transform, paired, diagonal = data
    level = len(factorial)
    if power == 1:
        return [kappa * (-q)**k for k in range(level)][::-1]
    vector = [mp.mpc(1)] * level
    for _ in range(power//2 - 1):
        vector = multiply(paired, vector)
    if power % 2:
        vector = multiply(transform, vector)
    return [(kappa**power) * diagonal[k] * vector[k]
            for k in range(level)][::-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-level', type=int, default=18)
    parser.add_argument('--max-power', type=int, default=8)
    parser.add_argument('--digits', type=int, default=90)
    args = parser.parse_args()
    if args.max_level < 3 or args.max_power < 2 or args.digits < 40:
        parser.error('require max-level >= 3, max-power >= 2, digits >= 40')
    mp.mp.dps = args.digits
    errors = {name: mp.mpf(0) for name in
              ('similarity', 'square', 'paired_powers', 'durfee_transport')}
    entries = 0
    comparisons = 0
    tolerance = mp.mpf(10)**(-args.digits//2)
    for level in range(3, args.max_level+1):
        data = finite_data(level)
        q, Q, sine, factorial, kappa, crossing, transform, paired, diagonal = data
        for k in range(level):
            for j in range(k+1):
                lhs = crossing[k][j] * diagonal[j]
                rhs = kappa * diagonal[k] * transform[k][j]
                errors['similarity'] = max(errors['similarity'], abs(lhs-rhs))
                lhs = sum(transform[k][h] * transform[h][j]
                          for h in range(j, k+1))
                errors['square'] = max(errors['square'], abs(lhs-paired[k][j]))
                entries += 1
        vector = [mp.mpc(int(k == 0)) for k in range(level)]
        for power in range(1, args.max_power+1):
            vector = multiply(crossing, vector)
            alternative = paired_power(power, data)
            errors['paired_powers'] = max(
                errors['paired_powers'],
                max(abs(x-y) for x, y in zip(vector[::-1], alternative)))
            comparisons += 1
        h2 = [level * q**(k*k)/factorial[k] for k in range(level)]
        transported = multiply(crossing, h2)
        errors['durfee_transport'] = max(
            errors['durfee_transport'],
            max(abs(transported[k]-kappa*mp.conj(h2[k]))
                for k in range(level)))
    passed = all(error < tolerance for error in errors.values())
    print(json.dumps({
        'levels': [3, args.max_level],
        'positive_powers': [1, args.max_power],
        'decimal_digits': args.digits,
        'matrix_entries': entries,
        'power_comparisons': comparisons,
        'max_absolute_errors': {key: mp.nstr(value, 12)
                                for key, value in errors.items()},
        'absolute_tolerance': mp.nstr(tolerance, 4),
        'passed': passed,
        'scope': 'finite numerical checks; analytic proofs are in the research note',
    }, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
