#!/usr/bin/env python3
"""Check repeated zero-block gluing in the complete original finite algebra.

Each block is a trivalent zero-filled vertex with two independent complex
outside angles. The matrix route contracts it in the full Newton quotient.
The other route uses every physical derivative-trace node at both the
block vertices and the common signed-power center. No normal or wire
index is discarded. These are finite normalization checks, not numerical
evidence for the large-multiplicity threshold or a volume limit.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_corner_newton_source_transport import basis_matrices
from check_twist_period_insertion import original_matrices, encode


def newton_values_and_derivatives(N, angle):
    spectral = -2 * mp.cos(angle)
    spectral_prime = 2 * mp.sin(angle)
    values = [mp.mpf(1)]
    derivatives = [mp.mpf(0)]
    for k in range(N - 1):
        node = 2 * mp.cos((2 * k + 1) * mp.pi / N)
        scale = 4 * mp.sin((k + 1) * mp.pi / N) ** 2
        factor = (node - spectral) / scale
        derivatives.append(derivatives[-1] * factor
                           - values[-1] * spectral_prime / scale)
        values.append(values[-1] * factor)
    return values, derivatives


def dot(left, right):
    return mp.fsum(a * b for a, b in zip(left, right))


def polynomial_matrix(values, basis):
    result = mp.matrix(len(values))
    for a, E in zip(values, basis):
        result += a * E
    return result


def block_matrix(N, boundary, basis):
    left = newton_values_and_derivatives(N, boundary[0])[0]
    right = newton_values_and_derivatives(N, boundary[1])[0]
    product = polynomial_matrix(left, basis) * polynomial_matrix(right, basis)
    coefficients = [(E * product)[N - 1, 0] for E in basis]
    return polynomial_matrix(coefficients, basis)


def block_at_node(N, center_data, boundary, node_data):
    center_values, center_derivatives = center_data
    left = newton_values_and_derivatives(N, boundary[0])[0]
    right = newton_values_and_derivatives(N, boundary[1])[0]
    value_terms, derivative_terms = [], []
    for angle, values, derivatives in node_data:
        Kt, Ks_t = dot(values, center_values), dot(derivatives, center_values)
        Kt_prime = dot(values, center_derivatives)
        Ks_t_prime = dot(derivatives, center_derivatives)
        Ku, Kv = dot(values, left), dot(values, right)
        Ksu, Ksv = dot(derivatives, left), dot(derivatives, right)
        outer = Ku * Kv
        outer_prime = Ksu * Kv + Ku * Ksv
        value_terms.append(mp.cos(angle) * Kt * outer
                           + mp.sin(angle) * (Ks_t * outer + Kt * outer_prime))
        derivative_terms.append(mp.cos(angle) * Kt_prime * outer
                                + mp.sin(angle) * (Ks_t_prime * outer
                                                  + Kt_prime * outer_prime))
    eta = (-1) ** (N - 1)
    return eta * mp.fsum(value_terms), eta * mp.fsum(derivative_terms)


def center_trace(N, power, blocks, node_data):
    terms = []
    for angle, values, derivatives in node_data:
        jets = [block_at_node(N, (values, derivatives), pair, node_data)
                for pair in blocks]
        product = mp.fprod(value for value, _ in jets)
        # Product rule without division, including exact or accidental zeros.
        derivative = mp.fsum(
            jet[1] * mp.fprod(jets[k][0] for k in range(len(jets)) if k != j)
            for j, jet in enumerate(jets))
        chirp = mp.exp(1j * power * N * angle ** 2 / (4 * mp.pi))
        terms.append(chirp * (mp.cos(angle) * product
                              + mp.sin(angle) * derivative
                              + 1j * power * N * angle / (2 * mp.pi)
                              * mp.sin(angle) * product))
    carrier = mp.exp(1j * mp.pi * power * (N - 1) ** 2 / (4 * N))
    return (-1) ** (N - 1) * carrier * mp.fsum(terms)


def run(precision):
    mp.mp.dps = precision
    rows = []
    for N in (3, 4, 5, 6):
        basis = basis_matrices(N)
        crossing, _, _ = original_matrices(N)
        node_data = []
        for j in range(N):
            angle = mp.pi * (N - 1 - 2 * j) / N
            values, derivatives = newton_values_and_derivatives(N, angle)
            node_data.append((angle, values, derivatives))
        for multiplicity in (3, 4):
            boundaries = [
                (mp.mpc(mp.mpf(j + 1) / 40, mp.mpf(j + 2) / 200),
                 mp.mpc(-mp.mpf(j + 2) / 50, mp.mpf(j + 1) / 250))
                for j in range(multiplicity)]
            product = mp.eye(N)
            for pair in boundaries:
                product *= block_matrix(N, pair, basis)
            for power in (-2, 0, 1, 3):
                matrix_value = (crossing ** power * product)[N - 1, 0]
                nodal_value = center_trace(N, power, boundaries, node_data)
                error = abs(matrix_value - nodal_value) / max(
                    1, abs(matrix_value), abs(nodal_value))
                if error > mp.mpf('1e-50'):
                    raise ArithmeticError('The full repeated-block traces disagree')
                rows.append({
                    'N': N, 'copies': multiplicity, 'central_power': power,
                    'outside_angles': [[encode(u), encode(v)] for u, v in boundaries],
                    'matrix_value': encode(matrix_value),
                    'nested_physical_trace': encode(nodal_value),
                    'relative_difference': mp.nstr(error, 35)})
        print(f'Checked eight signed central fillings at N={N}.', flush=True)
    return {
        'scope': ('Finite original-quotient versus nested full derivative-trace '
                  'normalization checks. No asymptotic threshold is tested.'),
        'decimal_precision': precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
        print(f'Saved {args.output}.')
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

