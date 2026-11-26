#!/usr/bin/env python3
"""Check the binary negative-chain replacement and its exact scalar exponents.

The affine and continued-fraction checks use rational arithmetic.
Original quantum matrices provide separate finite-precision diagnostics;
the written modular-group proof establishes their all-level identity.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path

import mpmath as mp

from check_rational_corridor_compression import (
    AFFINE_IDENTITY, TURN, compose, crossing, inverse, relative_rotation,
)
from check_twist_period_insertion import original_matrices


def complement(magnitudes):
    assert magnitudes and magnitudes[0] == magnitudes[-1] == 2
    assert all(b in (2, 3) for b in magnitudes)
    runs = [0]
    for b in magnitudes:
        if b == 2:
            runs[-1] += 1
        else:
            runs.append(0)
    k = len(runs) - 1
    if not k:
        return [len(magnitudes) + 1]
    return [runs[0] + 2] + [r + 3 for r in runs[1:-1]] + [runs[-1] + 2]


def continued_fraction(coefficients):
    value = Fraction(coefficients[-1])
    for c in reversed(coefficients[:-1]):
        value = c - 1 / value
    return value


def affine_word(coefficients, sign, internal):
    value = AFFINE_IDENTITY
    for b in coefficients:
        value = compose(value, compose(TURN, crossing(sign * b)))
    return compose(value, TURN) if internal else value


def exact_case(coefficients):
    m, k = len(coefficients), coefficients.count(3)
    positive = complement(coefficients)
    alpha = continued_fraction(coefficients)
    assert continued_fraction(positive) == alpha / (alpha - 1)
    assert len(positive) == k + 1
    assert sum(coefficients) == 2 * m + k
    assert sum(positive) == m + 2 * k + 1
    assert min(positive) >= 3 or coefficients == [2]

    original = affine_word(coefficients, -1, True)
    target = compose(crossing(1), compose(affine_word(positive, 1, True), crossing(1)))
    rotation = relative_rotation(target, original)

    old_cap = affine_word(coefficients, -1, False)
    new_cap = compose(crossing(1), affine_word(positive, 1, False))
    matrix, translation = compose(inverse(new_cap), old_cap)
    deck = matrix[0][0]
    assert deck in (-1, 1)
    assert matrix == ((deck, 0), (-deck, deck))
    assert all((2 * t).denominator == 1 for t in translation)
    stabilizer = compose(TURN, compose(crossing(1), inverse(TURN)))
    cap_rotation = relative_rotation(compose(new_cap, stabilizer), old_cap)
    return {
        "negative_magnitudes": coefficients,
        "positive_magnitudes": positive,
        "retained_rotation": rotation,
        "cap_rotation": cap_rotation,
        "two_boundary_kappa_exponent": -(m + k + 1),
        "pendant_kappa_exponent": -(m + k),
    }


def quantum_word(matrix, reversal, coefficients, sign):
    value = mp.eye(matrix.rows)
    for b in coefficients:
        value = value * reversal * matrix**(sign * b)
    return value


def quantum_diagnostics(precision, maximum_level):
    mp.mp.dps = precision
    examples = [[2], [2, 2], [2, 3, 2], [2, 3, 3, 2],
                [2, 2, 3, 2, 2], [2, 3, 2, 2, 3, 2], [2] * 8]
    rows = []
    for n in range(2, maximum_level + 1):
        matrix, _, _ = original_matrices(n)
        reversal = mp.matrix(n)
        for j in range(n):
            reversal[j, n - 1 - j] = 1
        cap = mp.matrix(n, 1)
        cap[0] = 1
        kappa = mp.exp(1j * mp.pi * (n - 1)**2 / (2 * n))
        for coefficients in examples:
            case = exact_case(coefficients)
            left = quantum_word(matrix, reversal, coefficients, -1)
            plus = quantum_word(matrix, reversal, case["positive_magnitudes"], 1)
            right = kappa**case["two_boundary_kappa_exponent"] * matrix * plus * matrix.T
            tensor_error = mp.norm(left - right) / max(1, mp.norm(left), mp.norm(right))
            old_column = left * cap
            new_column = kappa**case["pendant_kappa_exponent"] * matrix * plus * cap
            cap_error = mp.norm(old_column - new_column) / max(
                1, mp.norm(old_column), mp.norm(new_column)
            )
            assert tensor_error < mp.power(10, -(precision - 30))
            assert cap_error < mp.power(10, -(precision - 30))
            rows.append({
                "N": n, "negative_magnitudes": coefficients,
                "tensor_relative_error": mp.nstr(tensor_error, 20),
                "pendant_relative_error": mp.nstr(cap_error, 20),
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--max-level", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert args.max_length >= 1 and args.precision >= 60 and args.max_level >= 2
    count, rotations = 0, {}
    examples = []
    for length in range(1, args.max_length + 1):
        words = [[2]] if length == 1 else (
            [2, *middle, 2] for middle in product((2, 3), repeat=length - 2)
        )
        for coefficients in words:
            case = exact_case(coefficients)
            count += 1
            name = case["retained_rotation"]
            rotations[name] = rotations.get(name, 0) + 1
            if coefficients in ([2], [2, 2], [2, 3, 2], [2, 3, 3, 2],
                                [2, 2, 3, 2, 2], [2, 3, 2, 2, 3, 2]):
                examples.append(case)
    here = Path(__file__).resolve()
    dependencies = [
        here,
        here.with_name("check_rational_corridor_compression.py"),
        here.with_name("check_twist_period_insertion.py"),
        here.with_name("check_internal_vertex_asymptotic.py"),
    ]
    diagnostics = quantum_diagnostics(args.precision, args.max_level)
    result = {
        "scope": "Exact full affine, cap-stabilizer, continued-fraction and scalar-exponent checks. Quantum matrices are finite-precision diagnostics. No source asymptotic or stationary-cycle comparison.",
        "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "maximum_length": args.max_length,
        "exact_words": count,
        "retained_rotations": rotations,
        "examples": examples,
        "decimal_precision": args.precision,
        "quantum_diagnostics": diagnostics,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "exact_words": count,
        "retained_rotations": rotations,
        "quantum_matrix_pairs": len(diagnostics),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()

