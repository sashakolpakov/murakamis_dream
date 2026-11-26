#!/usr/bin/env python3
"""Compare recursive original tree contractions with full physical traces.

One calculation uses multiplication in the original Newton quotient.
The other recursively retains every physical trace node and its first
angular derivative. The small trees check normalization and boundary
dependence; they do not meet or test an asymptotic branching threshold.
"""

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_amplified_zero_block_composition import (
    dot, newton_values_and_derivatives, polynomial_matrix,
)
from check_corner_newton_source_transport import basis_matrices
from check_twist_period_insertion import original_matrices, encode


def leaf(power):
    return power, ()


def tree_size(tree):
    return 1 + sum(tree_size(child) for child in tree[1])


def tree_depth(tree):
    return 1 + max((tree_depth(child) for child in tree[1]), default=0)


def product_jet(jets):
    value = mp.fprod(v for v, _ in jets)
    derivative = mp.fsum(
        derivative * mp.fprod(jets[k][0] for k in range(len(jets)) if k != j)
        for j, (_, derivative) in enumerate(jets))
    return value, derivative


def check_level(level, trees, tolerance):
    basis = basis_matrices(level)
    crossing, _, _ = original_matrices(level)
    nodes = [mp.pi * (level - 1 - 2*j) / level for j in range(level)]
    node_basis = [newton_values_and_derivatives(level, t) for t in nodes]

    @lru_cache(None)
    def inner_matrix(tree):
        result = crossing ** tree[0]
        for child in tree[1]:
            result *= polynomial_matrix(matrix_coefficients(child), basis)
        return result

    @lru_cache(None)
    def matrix_coefficients(tree):
        matrix = inner_matrix(tree)
        return tuple((matrix * entry)[level-1, 0] for entry in basis)

    def trace(power, jets):
        terms = []
        for t, (value, derivative) in zip(nodes, jets):
            chirp = mp.exp(1j * power * level * t*t / (4*mp.pi))
            linear = mp.cos(t) + 1j * power * level * t * mp.sin(t)/(2*mp.pi)
            terms.append(chirp * (linear*value + mp.sin(t)*derivative))
        carrier = (-1)**(level-1) * mp.exp(
            1j * mp.pi * power * (level-1)**2 / (4*level))
        return carrier * mp.fsum(terms)

    @lru_cache(None)
    def child_products(tree):
        child_data = [physical_jets(child) for child in tree[1]]
        return tuple(product_jet([data[j] for data in child_data])
                     for j in range(level))

    def open_physical_jet(tree, angle):
        outside, outside_prime = newton_values_and_derivatives(level, angle)
        value_jets, derivative_jets = [], []
        for (values, primes), (product, product_prime) in zip(
                node_basis, child_products(tree)):
            kernel, kernel_t = dot(values, outside), dot(primes, outside)
            kernel_u, kernel_tu = dot(values, outside_prime), dot(primes, outside_prime)
            value_jets.append((kernel*product, kernel_t*product + kernel*product_prime))
            derivative_jets.append((kernel_u*product,
                                    kernel_tu*product + kernel_u*product_prime))
        return trace(tree[0], value_jets), trace(tree[0], derivative_jets)

    @lru_cache(None)
    def physical_jets(tree):
        return tuple(open_physical_jet(tree, t) for t in nodes)

    angles = [mp.mpf(0), mp.mpc('.031', '.019'), mp.mpc('-.08', '.02')]
    checks = []
    for index, tree in enumerate(trees):
        coeff = matrix_coefficients(tree)
        errors = []
        for angle in angles:
            vals, ders = newton_values_and_derivatives(level, angle)
            expected = dot(coeff, vals), dot(coeff, ders)
            actual = open_physical_jet(tree, angle)
            error = max(abs(a-b)/max(1, abs(a), abs(b)) for a, b in zip(actual, expected))
            if error > tolerance:
                raise ArithmeticError(('open boundary or derivative', level, index, error))
            errors.append({'angle': encode(angle), 'relative_error': mp.nstr(error, 35)})
        closed_matrix = inner_matrix(tree)[level-1, 0]
        closed_physical = trace(tree[0], child_products(tree))
        closed_error = abs(closed_matrix-closed_physical)/max(
            1, abs(closed_matrix), abs(closed_physical))
        if closed_error > tolerance:
            raise ArithmeticError(('closed root', level, index, closed_error))
        checks.append({'N': level, 'tree': index, 'vertices': tree_size(tree),
                       'depth': tree_depth(tree), 'open_boundary_checks': errors,
                       'closed_root_relative_error': mp.nstr(closed_error, 35)})
    print(f'Checked four recursive trees and their full boundary derivatives at N={level}.',
          flush=True)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=120)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    trees = [
        (0, (leaf(2), leaf(-3), leaf(4))),
        (-2, ((2, (leaf(3), leaf(-2))), (0, (leaf(2), leaf(-3), leaf(4))))),
        (3, ((-1, ((0, (leaf(-2), leaf(5))), leaf(3))), leaf(-4))),
        (0, ((1, ((-2, ((3, (leaf(2),)), leaf(-3))),)), leaf(2))),
    ]
    rows = []
    for level in range(2, 8):
        rows.extend(check_level(level, trees, mp.power(10, -args.precision//2)))
    result = {
        'scope': ('Finite original matrix versus recursive full-node traces, including '
                  'free complex boundary values and their first derivatives. '
                  'No large-branching threshold or volume asymptotic is tested.'),
        'decimal_precision': args.precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'trees': trees, 'checks': rows,
    }
    content = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.')
    else:
        print(content)


if __name__ == '__main__':
    main()
