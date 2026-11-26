#!/usr/bin/env python3
"""Check Newton saddle normalizations against the complete finite trace.

The three-edge star has leading coefficient 1/16. The adjacent pair of
trivalent vertices has four boundary edges and coefficient 2**(-29/4).
For both, this script checks the Hessian, density, and leading constant,
then evaluates every Newton index at every original derivative-trace
node. No retained-index window or asymptotic kernel is used in the
finite calculation.

The finite-level ratios are numerical diagnostics, not a proof of the
asymptotic theorem or of a hyperbolic-volume identification.

Run from the research workspace:
  python3 experiments/check_zero_subtree_newton_normalization.py \
    --output repro/results/research-zero-subtree-newton-normalization.json

Requires mpmath, as does check_internal_vertex_asymptotic.py.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_internal_vertex_asymptotic import (
    complete_trace,
    full_edge_at_trace_nodes,
)


STAR_MATRIX = [
    [Fraction(-25, 2), Fraction(-25, 4), Fraction(25, 4)],
    [Fraction(-25, 4), Fraction(-25, 2), Fraction(25, 4)],
    [Fraction(25, 4), Fraction(25, 4), Fraction(-25, 2)],
]
PAIR_MATRIX = [
    [Fraction(-27, 4), Fraction(-9, 4), 0, 0, 3],
    [Fraction(-9, 4), Fraction(-27, 4), 0, 0, 3],
    [0, 0, Fraction(-27, 4), Fraction(-9, 4), 3],
    [0, 0, Fraction(-9, 4), Fraction(-27, 4), 3],
    [3, 3, 3, 3, -8],
]


def rational_determinant(matrix):
    """Fraction-only elimination, separate from the numerical Hessian."""
    rows = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for col in range(len(rows)):
        pivot = next((r for r in range(col, len(rows)) if rows[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            result = -result
        value = rows[col][col]
        result *= value
        for row in range(col + 1, len(rows)):
            factor = rows[row][col] / value
            for j in range(col + 1, len(rows)):
                rows[row][j] -= factor * rows[col][j]
            rows[row][col] = Fraction(0)
    return result


def as_mp(value):
    value = Fraction(value)
    return mp.mpf(value.numerator) / value.denominator


def affine(size, coordinate=None, constant=0):
    result = [Fraction(constant)] + [Fraction(0)] * size
    if coordinate is not None:
        result[coordinate + 1] = Fraction(1)
    return result


def add(left, right, scale=1):
    return [a + scale * b for a, b in zip(left, right)]


def evaluate(form, coordinates):
    return as_mp(form[0]) + mp.fsum(
        as_mp(coefficient) * coordinate
        for coefficient, coordinate in zip(form[1:], coordinates)
    )


def leaf_terms(form):
    return [(1, [2 * x for x in form]), (-4, form)]


def gate_terms(x, y, z):
    return [
        (1, add(x, y)), (1, z), (-1, x), (-1, y),
        (-1, add(z, x, -1)), (-1, add(z, y, -1)),
        (-1, add(add(x, y), z, -1)),
    ]


def j_integral(value):
    # This is the real continuous primitive, with J(0)=J(1/2)=0.
    return -mp.im(mp.polylog(2, mp.exp(2j * mp.pi * value))) / (2 * mp.pi)


def gate_density(x, y, z):
    numerator = (2 * mp.sin(mp.pi * (x + y))) * (2 * mp.sin(mp.pi * z))
    denominator = mp.fprod(
        2 * mp.sin(mp.pi * t)
        for t in (x, y, z - x, z - y, x + y - z)
    )
    return mp.sqrt(numerator / denominator)


def check_saddle(kind):
    """Differentiate the J-linear action, then compare with exact matrices."""
    if kind == 'three_edge_star':
        size = 3
        x, y, z = [affine(size, j) for j in range(size)]
        leaves = [x, y, add(affine(size, constant=1), z, -1)]
        gates = [(x, y, z)]
        a = mp.atan(2) / mp.pi
        point = [a, a, 1 - a]
        reference = STAR_MATRIX
        matrix_scale = mp.pi
        expected_determinant = Fraction(15625, 16)
        expected_density = 125 * mp.sqrt(2) / 256
        exact_density_squared = Fraction(125 ** 2 * 2, 256 ** 2)
        expected_amplitude = mp.mpf(1) / 16
        # The third leaf has label D-r_z=N(1-z)-1.
        offset = mp.exp(-2 * mp.log(1 / mp.tan(mp.pi * a)))
        expected_offset = mp.mpf(4)
        rate_power = -3
    elif kind == 'adjacent_trivalent_pair':
        size = 5
        wires = [affine(size, j) for j in range(size)]
        leaves = wires[:4]
        gates = [(wires[0], wires[1], wires[4]),
                 (wires[2], wires[3], wires[4])]
        a = mp.atan(mp.sqrt(2)) / mp.pi
        point = [a, a, a, a, mp.mpf(1) / 2]
        reference = PAIR_MATRIX
        matrix_scale = mp.pi * mp.sqrt(2)
        expected_determinant = Fraction(6561)
        expected_density = 81 * mp.sqrt(2) / 512
        exact_density_squared = Fraction(81 ** 2 * 2, 512 ** 2)
        expected_amplitude = mp.power(2, -mp.mpf(29) / 4)
        # Both closing product coefficients use the same integer r.
        offset = expected_offset = mp.mpf(1)
        rate_power = -mp.mpf(9) / 2
    else:
        raise ValueError(kind)

    terms = [term for leaf in leaves for term in leaf_terms(leaf)]
    terms += [term for gate in gates for term in gate_terms(*gate)]
    action = mp.mpf(0)
    gradient = [mp.mpf(0)] * size
    hessian = mp.matrix(size)
    for sign, form in terms:
        value = evaluate(form, point)
        if not 0 < value < 1:
            raise AssertionError('A retained factorial argument is not strict')
        action += sign * j_integral(value)
        first = mp.log(2 * mp.sin(mp.pi * value))
        second = mp.pi / mp.tan(mp.pi * value)
        for i, ai in enumerate(form[1:]):
            gradient[i] += sign * as_mp(ai) * first
            for j, aj in enumerate(form[1:]):
                hessian[i, j] += sign * as_mp(ai) * as_mp(aj) * second

    negative_reference = [[-Fraction(x) for x in row] for row in reference]
    exact_determinant = rational_determinant(negative_reference)
    if exact_determinant != expected_determinant:
        raise AssertionError('The rational Hessian determinant is incorrect')
    # Sylvester's criterion is checked in exact arithmetic as well.
    principal_minors = [
        rational_determinant([row[:j] for row in negative_reference[:j]])
        for j in range(1, size + 1)
    ]
    if any(value <= 0 for value in principal_minors):
        raise AssertionError('The proposed negative Hessian is not positive definite')
    if kind == 'three_edge_star':
        exact_amplitude_power = 2
        exact_amplitude_value = 2 ** size * exact_density_squared / exact_determinant
        if exact_amplitude_value != Fraction(1, 256):
            raise AssertionError('The exact star Gaussian normalization is incorrect')
    else:
        exact_amplitude_power = 4
        exact_amplitude_value = (2 ** size * exact_density_squared ** 2
                                 / exact_determinant ** 2)
        if exact_amplitude_value != Fraction(1, 2 ** 29):
            raise AssertionError('The exact pair Gaussian normalization is incorrect')

    density = offset * mp.fprod(
        1 / (2 * mp.sin(mp.pi * evaluate(leaf, point))) for leaf in leaves
    )
    density *= mp.fprod(
        gate_density(*(evaluate(form, point) for form in gate)) for gate in gates
    )
    amplitude = (2 * mp.pi) ** (mp.mpf(size) / 2) * density / mp.sqrt(mp.det(-hessian))
    residuals = {
        'stationary_gradient': max(map(abs, gradient)),
        'scaled_hessian': max(
            abs(hessian[i, j] / matrix_scale - as_mp(reference[i][j]))
            for i in range(size) for j in range(size)
        ),
        'density_relative_error': abs(density / expected_density - 1),
        'amplitude_relative_error': abs(amplitude / expected_amplitude - 1),
        'offset_relative_error': abs(offset / expected_offset - 1),
    }
    threshold = mp.power(10, -mp.mp.dps // 2)
    if max(residuals.values()) > threshold:
        raise AssertionError(f'{kind}: a stationary normalization identity failed')
    return {
        'kind': kind, 'boundary_edges': len(leaves), 'primitive_dimension': size,
        'leaf_coordinate': a, 'action': action, 'density': density,
        'amplitude': amplitude, 'level_power': rate_power,
        'offset_factor': offset,
        'exact_negative_scaled_hessian_determinant': str(exact_determinant),
        'exact_density_squared': str(exact_density_squared),
        'exact_amplitude_power': exact_amplitude_power,
        'exact_amplitude_power_value': str(exact_amplitude_value),
        'exact_principal_minors': [str(value) for value in principal_minors],
        'normalization_residuals': residuals,
    }


def full_pair_and_star(level, edge_data):
    """Use all c_i=phi(e_i K(t,0)^2), including high i and trace normals."""
    top = level - 1
    nodes = [2 * mp.cos((2 * k + 1) * mp.pi / level) for k in range(top)]
    scales = [(2 * mp.sin((k + 1) * mp.pi / level)) ** 2 for k in range(top)]
    trace_coefficients = [mp.mpf(0)] * level
    eta = (-1) ** top
    for angle, kernel, kernel_derivative in edge_data:
        sine, cosine = mp.sin(angle), mp.cos(angle)
        spectral, spectral_derivative = -2 * cosine, 2 * sine
        square, square_derivative = kernel ** 2, 2 * kernel * kernel_derivative
        value, derivative = mp.mpf(1), mp.mpf(0)
        for index in range(level):
            trace_coefficients[index] += eta * (
                cosine * value * square
                + sine * (derivative * square + value * square_derivative)
            )
            if index < top:
                factor = (nodes[index] - spectral) / scales[index]
                derivative, value = (
                    derivative * factor - value * spectral_derivative / scales[index],
                    value * factor,
                )
    complete_values = [mp.mpf(1)]
    for node, scale in zip(nodes, scales):
        complete_values.append(complete_values[-1] * (node + 2) / scale)
    star_from_pairing = mp.fsum(
        coefficient * boundary for coefficient, boundary
        in zip(trace_coefficients, complete_values)
    )
    # The contraction is sum c_i^2, not sum |c_i|^2. All c_i are real.
    pair = mp.fsum(coefficient ** 2 for coefficient in trace_coefficients)
    return pair, star_from_pairing, min(trace_coefficients), max(trace_coefficients)


def finite_values(level):
    edge_data = full_edge_at_trace_nodes(level)
    star, unit = complete_trace(level, 3, 0, edge_data)
    if unit != 1:
        raise AssertionError('Unexpected phase at zero crossing power')
    pair, pairing_star, minimum, maximum = full_pair_and_star(level, edge_data)
    error = abs(pairing_star / star - 1)
    threshold = mp.power(10, -mp.mp.dps // 3)
    if error > threshold:
        raise AssertionError('Independent star contractions disagree')
    if minimum < -threshold * maximum:
        raise AssertionError('A trace coefficient violates positivity beyond precision error')
    return {
        'three_edge_star': mp.re(star),
        'adjacent_trivalent_pair': pair,
        'star_pairing_relative_error': error,
        'minimum_trace_coefficient': minimum,
    }


def encode(value):
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    return mp.nstr(value, 35)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--levels', default='24,25,48,49,96,97')
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--precision-increment', type=int, default=30)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.precision < 60 or args.precision_increment < 20:
        parser.error('Use at least 60 decimal digits and a precision increment of 20')
    levels = [int(value) for value in args.levels.split(',')]
    if not levels or any(level < 3 for level in levels):
        parser.error('All levels must be at least three')
    if args.output and args.output.exists():
        args.output.unlink()  # A failed run must not leave an earlier success record.

    mp.mp.dps = args.precision
    saddles = {kind: check_saddle(kind) for kind in
               ('three_edge_star', 'adjacent_trivalent_pair')}
    rows = []
    for level in levels:
        mp.mp.dps = args.precision
        baseline = finite_values(level)
        with mp.workdps(args.precision + args.precision_increment):
            higher = finite_values(level)
            changes = {
                kind: abs(higher[kind] / baseline[kind] - 1) for kind in saddles
            }
            if max(changes.values()) > mp.power(10, -args.precision // 3):
                raise AssertionError(f'Precision stability failed at level {level}')
            for kind, saddle in saddles.items():
                leading = (mp.power(level, saddle['level_power']) * saddle['amplitude']
                           * mp.exp(level * saddle['action']))
                ratio = higher[kind] / leading
                rows.append({
                    'level': level, 'case': kind, 'finite_value': higher[kind],
                    'finite_over_leading': ratio,
                    'level_times_relative_error': level * (ratio - 1),
                    'precision_relative_change': changes[kind],
                    'star_pairing_relative_error': higher['star_pairing_relative_error'],
                })
        print(f'Computed both complete sources at level {level}', flush=True)

    source_paths = [Path(__file__).resolve(),
                    Path(__file__).resolve().with_name('check_internal_vertex_asymptotic.py')]
    result = {
        'scope': 'Finite normalization diagnostic; not an asymptotic or volume proof',
        'status': 'completed',
        'decimal_precision': args.precision,
        'independent_recalculation_precision': args.precision + args.precision_increment,
        'finite_method': ('All original derivative-trace nodes and all N Newton indices; '
                          'pair source=sum_i phi(e_i K(t,0)^2)^2'),
        'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in source_paths},
        'stationary_normalizations': list(saddles.values()),
        'comparisons': rows,
    }
    output = json.dumps(encode(result), indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(f'Wrote {args.output}', flush=True)
    else:
        print(output)


if __name__ == '__main__':
    main()
