#!/usr/bin/env python3
"""Check full crossing multiplication and its Hermite Fourier reconstruction.

The finite algebra tests retain every Newton coefficient and first normal.
The off-grid records compare the canonical product with the analytic chirp
on actual bare-edge and terminal sources. Those records are diagnostics,
not proofs of the exponential bounds or of a volume limit.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_amplified_zero_block_composition import newton_values_and_derivatives, dot
from check_twist_period_insertion import encode


def original_crossings(level):
    """Original triangular Newton crossing; its inverse is its conjugate."""
    top = level - 1
    q = mp.exp(mp.pi * 1j / level)
    kappa = mp.exp(mp.pi * 1j * top**2 / (2 * level))
    factorial = [mp.mpf(1)]
    for k in range(1, level):
        factorial.append(factorial[-1] * 2 * mp.sin(mp.pi * k / level))
    matrix = mp.matrix(level)
    for j in range(level):
        for k in range(j, level):
            matrix[k, j] = (kappa * (-1)**k * q**(k * (j + 1))
                            * factorial[k] / (factorial[j] * factorial[k-j]))
    inverse = matrix.apply(mp.conj)
    return matrix, inverse


def multiply(crossings, power, coefficients):
    result = mp.matrix(coefficients)
    matrix = crossings[0 if power >= 0 else 1]
    for _ in range(abs(power)):
        result = matrix * result
    return result


def source(level, crossings, kind):
    if kind == 'edge':
        return mp.matrix(newton_values_and_derivatives(level, 0)[0])
    power = int(kind.split(':')[1])
    unit = mp.matrix([1] + [0] * (level - 1))
    return mp.matrix(list(reversed(list(multiply(crossings, power, unit)))))


def evaluate(level, coefficients, angle):
    values, derivatives = newton_values_and_derivatives(level, angle)
    return dot(coefficients, values), dot(coefficients, derivatives)


def chirp_jet(level, power, angle, jet):
    carrier = mp.exp(mp.pi * 1j * power * (level-1)**2 / (4*level))
    multiplier = carrier * mp.exp(1j * power * level * angle**2 / (4*mp.pi))
    return (multiplier * jet[0],
            multiplier * (jet[1] + 1j * power * level * angle * jet[0] / (2*mp.pi)))


def hermite_coefficients(level, values, derivatives, nodes):
    coefficients = [mp.fsum(values) / level]
    for m in range(1, level):
        value_transform = mp.fsum(v * mp.exp(-1j*m*t)
                                  for v, t in zip(values, nodes)) / level
        derivative_transform = mp.fsum(v * mp.exp(-1j*m*t)
                                       for v, t in zip(derivatives, nodes)) / (1j*level)
        coefficients.append(((level-m)*value_transform + derivative_transform)/level)
    return coefficients


def fourier_evaluate(coefficients, angle):
    value = coefficients[0] + 2 * mp.fsum(
        coefficients[m] * mp.cos(m*angle) for m in range(1, len(coefficients)))
    derivative = -2 * mp.fsum(
        m * coefficients[m] * mp.sin(m*angle) for m in range(1, len(coefficients)))
    return value, derivative


def relative_error(left, right):
    return abs(left-right)/max(1, abs(left), abs(right))


def exact_checks(precision):
    tolerance = mp.power(10, -precision//2)
    records = []
    angles = [mp.mpf(0), mp.mpc('.11', '.07'), mp.mpc('-.17', '.03')]
    for level in range(2, 13):
        crossings = original_crossings(level)
        inverse_error = mp.norm(crossings[0]*crossings[1]-mp.eye(level))
        if inverse_error > tolerance:
            raise ArithmeticError(('inverse crossing', level, inverse_error))
        nodes = [mp.pi * (level-1-2*j)/level for j in range(level)]
        for kind in ('edge', 'terminal:2', 'terminal:-3'):
            coefficients = source(level, crossings, kind)
            for power in (-3, -1, 1, 2):
                product = multiply(crossings, power, coefficients)
                jets = [chirp_jet(level, power, t, evaluate(level, coefficients, t))
                        for t in nodes]
                nodal_error = max(relative_error(actual, expected)
                                  for t, expected_jet in zip(nodes, jets)
                                  for actual, expected in zip(evaluate(level, product, t),
                                                              expected_jet))
                folded = hermite_coefficients(level, [j[0] for j in jets],
                                              [j[1] for j in jets], nodes)
                reconstruction_error = max(relative_error(actual, expected)
                                           for t in angles
                                           for actual, expected in zip(
                                               evaluate(level, product, t),
                                               fourier_evaluate(folded, t)))
                if max(nodal_error, reconstruction_error) > tolerance:
                    raise ArithmeticError((level, kind, power, nodal_error,
                                           reconstruction_error))
                records.append({'N': level, 'source': kind, 'power': power,
                                'physical_jet_relative_error': mp.nstr(nodal_error, 35),
                                'complex_reconstruction_relative_error':
                                    mp.nstr(reconstruction_error, 35)})
        print(f'Full original product and Fourier reconstruction checked at N={level}.',
              flush=True)
    return records


def off_grid_diagnostics():
    records = []
    real_angles = [-mp.pi + 2*mp.pi*j/47 for j in range(48)]
    complex_angles = [mp.mpc('.07', '.025'), mp.mpc('-.13', '.02')]
    for level in (16, 17, 32, 33, 64, 65):
        crossings = original_crossings(level)
        for kind, power in (('edge', -2), ('edge', 1),
                            ('terminal:-3', -1), ('terminal:3', 1)):
            coefficients = source(level, crossings, kind)
            product = multiply(crossings, power, coefficients)
            scale = abs(evaluate(level, coefficients, 0)[0])
            maximum = max(abs(evaluate(level, product, t)[0]
                              - chirp_jet(level, power, t,
                                          evaluate(level, coefficients, t))[0])
                          for t in real_angles)
            local = []
            for t in complex_angles:
                predicted = chirp_jet(level, power, t,
                                      evaluate(level, coefficients, t))[0]
                actual = evaluate(level, product, t)[0]
                local.append({'angle': encode(t),
                              'canonical_over_chirped_minus_one': encode(actual/predicted-1)})
            records.append({'N': level, 'source': kind, 'power': power,
                            'sampled_real_error_over_abs_source_at_zero':
                                mp.nstr(maximum/scale, 35),
                            'local_comparisons': local})
        print(f'Off-grid source diagnostics recorded at N={level}.', flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=120)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    result = {'scope': 'Finite original-algebra normalization and off-grid diagnostics; '
                       'the exponential theorem is proved in the accompanying note.',
              'decimal_precision': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'exact_checks': exact_checks(args.precision),
              'off_grid_diagnostics': off_grid_diagnostics()}
    content = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.')
    else:
        print(content)


if __name__ == '__main__':
    main()
