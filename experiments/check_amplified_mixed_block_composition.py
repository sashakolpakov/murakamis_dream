#!/usr/bin/env python3
"""Check mixed zero, terminal and bare-edge gluing in the original source.

The two calculations are original Newton multiplication/crossing matrices
and nested complete derivative traces. Terminal values are not substituted
for their first normals. Finite identities do not test the asymptotic
multiplicity threshold.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_amplified_zero_block_composition import (
    newton_values_and_derivatives, polynomial_matrix, block_matrix,
    block_at_node, dot,
)
from check_corner_newton_source_transport import basis_matrices
from check_twist_period_insertion import original_matrices, encode


def original_block_matrix(N, block, basis, crossing):
    kind, data = block
    if kind == 'zero':
        return block_matrix(N, data, basis)
    if kind == 'edge':
        return polynomial_matrix(
            newton_values_and_derivatives(N, data)[0], basis)
    power = data
    Mn = crossing ** power
    return polynomial_matrix([(Mn * E)[N - 1, 0] for E in basis], basis)


def original_block_jet(N, block, center, nodes):
    kind, data = block
    if kind == 'zero':
        return block_at_node(N, center, data, nodes)
    if kind == 'edge':
        outside = newton_values_and_derivatives(N, data)[0]
        return dot(center[0], outside), dot(center[1], outside)
    power = data
    values, derivatives = [], []
    for angle, basis, basis_prime in nodes:
        chirp = mp.exp(1j * power * N * angle ** 2 / (4 * mp.pi))
        linear = mp.cos(angle) + 1j * power * N * angle / (2 * mp.pi) * mp.sin(angle)
        values.append(chirp * (linear * dot(basis, center[0])
                               + mp.sin(angle) * dot(basis_prime, center[0])))
        derivatives.append(chirp * (linear * dot(basis, center[1])
                                    + mp.sin(angle) * dot(basis_prime, center[1])))
    unit = (-1) ** (N - 1) * mp.exp(1j * mp.pi * power * (N - 1) ** 2 / (4 * N))
    return unit * mp.fsum(values), unit * mp.fsum(derivatives)


def complete_mixed_trace(N, power, blocks, nodes):
    terms = []
    for angle, basis, basis_prime in nodes:
        jets = [original_block_jet(N, block, (basis, basis_prime), nodes)
                for block in blocks]
        product = mp.fprod(value for value, _ in jets)
        derivative = mp.fsum(
            jet[1] * mp.fprod(jets[k][0] for k in range(len(jets)) if k != j)
            for j, jet in enumerate(jets))
        linear = mp.cos(angle) + 1j * power * N * angle / (2 * mp.pi) * mp.sin(angle)
        terms.append(mp.exp(1j * power * N * angle ** 2 / (4 * mp.pi))
                     * (linear * product + mp.sin(angle) * derivative))
    unit = (-1) ** (N - 1) * mp.exp(1j * mp.pi * power * (N - 1) ** 2 / (4 * N))
    return unit * mp.fsum(terms)


def run(precision):
    mp.mp.dps = precision
    cases = [
        [('terminal', 2), ('terminal', -3), ('terminal', 64)],
        [('terminal', -2), ('terminal', 7), ('terminal', -65), ('terminal', 3)],
        [('zero', (mp.mpc('.07', '.012'), mp.mpc('-.09', '.017'))),
         ('terminal', -2), ('edge', mp.mpc('.05', '-.013')), ('terminal', 5)],
    ]
    rows = []
    for N in (3, 4, 5, 6):
        E = basis_matrices(N)
        M, _, _ = original_matrices(N)
        nodes = []
        for j in range(N):
            angle = mp.pi * (N - 1 - 2 * j) / N
            value, derivative = newton_values_and_derivatives(N, angle)
            nodes.append((angle, value, derivative))
        for case, blocks in enumerate(cases):
            product = mp.eye(N)
            for block in blocks:
                product *= original_block_matrix(N, block, E, M)
            for power in (-2, 0, 1, 3):
                matrix_value = (M ** power * product)[N - 1, 0]
                nodal_value = complete_mixed_trace(N, power, blocks, nodes)
                error = abs(matrix_value - nodal_value) / max(
                    1, abs(matrix_value), abs(nodal_value))
                if error > mp.mpf('1e-50'):
                    raise ArithmeticError('Mixed original source representations disagree')
                rows.append({
                    'N': N, 'case': case, 'central_power': power,
                    'matrix_value': encode(matrix_value),
                    'nested_full_trace': encode(nodal_value),
                    'relative_difference': mp.nstr(error, 35)})
        print(f'Checked twelve mixed original fillings at N={N}.', flush=True)
    return {
        'scope': ('Original matrix versus nested complete-node normalization. '
                  'No asymptotic threshold or uniform convergence is tested.'),
        'decimal_precision': precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'cases': [
            {'blocks': ['terminal 2', 'terminal -3', 'terminal 64']},
            {'blocks': ['terminal -2', 'terminal 7', 'terminal -65', 'terminal 3']},
            {'blocks': ['trivalent zero vertex with two complex free angles',
                        'terminal -2', 'bare edge with a complex free angle', 'terminal 5']},
        ],
        'checks': rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--precision', type=int, default=100)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    result = run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
        print(f'Saved {args.output}.')
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

