#!/usr/bin/env python3
"""Check the definite rational-corridor normal form and its quantum scalar.

Affine maps and continued fractions are checked with exact integer/rational
arithmetic. Original quantum matrices are separate high-precision diagnostics,
not a replacement for the written operator proof.
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
    AFFINE_IDENTITY, TURN, compose, crossing, inverse, relative_rotation, word,
)
from check_twist_period_insertion import original_matrices


def ceiling_fraction(numerator, denominator):
    assert numerator > denominator > 0
    coefficients = []
    while True:
        coefficient = (numerator + denominator - 1) // denominator
        remainder = coefficient * denominator - numerator
        assert coefficient >= 2 and 0 <= remainder < denominator
        coefficients.append(coefficient)
        if remainder == 0:
            assert denominator == 1
            return coefficients
        numerator, denominator = denominator, remainder


def negative_word(coefficients, right_turn=True):
    affine = TURN
    for i, coefficient in enumerate(coefficients):
        affine = compose(affine, crossing(-coefficient))
        if i + 1 < len(coefficients) or right_turn:
            affine = compose(affine, TURN)
    return affine


def continuant(coefficients):
    previous, value = 0, 1
    for coefficient in coefficients:
        previous, value = value, coefficient * value - previous
        assert value > previous
    return value


def internal_normal_form(powers):
    original = word(powers, True)
    (a, b), (c, d) = original[0]
    if abs(c) < 2:
        return None
    sign = 1 if c > 0 else -1
    capacity = abs(c)
    left_residue, right_residue = sign * a % capacity, sign * d % capacity
    assert 1 <= left_residue < capacity and 1 <= right_residue < capacity
    left = (sign * a - left_residue) // capacity
    right = (sign * d - right_residue) // capacity
    coefficients = ceiling_fraction(capacity, left_residue)
    core = negative_word(coefficients)
    deck = (-1) ** len(coefficients)
    expected_core = (
        (left_residue, (left_residue * right_residue - 1) // capacity),
        (capacity, right_residue),
    )
    assert tuple(tuple(deck * x for x in row) for row in core[0]) == expected_core
    target = compose(crossing(left), compose(core, crossing(right)))
    rotation = relative_rotation(target, original)
    scalar_numerator = sum(powers) - left - right + sum(coefficients)
    assert scalar_numerator % 3 == 0
    assert continuant(coefficients) == capacity
    assert continuant(coefficients[1:]) == left_residue
    assert len(coefficients) <= left_residue
    return {
        "powers_from_inside": list(powers),
        "original_matrix": original[0],
        "negative_magnitudes_from_outside": coefficients,
        "left_power": left,
        "right_power": right,
        "rotation": rotation,
        "kappa_exponent": scalar_numerator // 3,
        "chain_determinant": capacity,
        "chain_tail_minor": left_residue,
    }


def pendant_normal_form(powers):
    original = word(powers, False)
    (a, b), (c, d) = original[0]
    if d == 0:
        return None
    slope = Fraction(b, d)
    if slope.denominator < 2:
        return None
    left = slope.numerator // slope.denominator
    fraction = slope - left
    coefficients = ceiling_fraction(fraction.denominator, fraction.numerator)
    target = compose(crossing(left), negative_word(coefficients, False))
    relative, translation = compose(inverse(target), original)
    (aa, bb), (cc, dd) = relative
    assert bb == 0 and aa == dd and aa in (-1, 1)
    h = aa * cc
    assert all((2 * t).denominator == 1 for t in translation)
    # The relative linear map is L_h = S A_{-h} S projectively.
    target_exponents = left - sum(coefficients)
    numerator = sum(powers) - target_exponents - 2 * h
    assert numerator % 3 == 0
    assert Fraction(target[0][0][1], target[0][1][1]) == slope
    return {
        "powers_from_inside": list(powers),
        "slope": str(slope),
        "negative_magnitudes_from_outside": coefficients,
        "left_power": left,
        "cap_stabilizer_h": h,
        "cap_kappa_exponent": numerator // 3,
    }


def quantum_word(matrix, reversal, powers, internal):
    value = mp.eye(matrix.rows)
    for power in powers:
        value = reversal * matrix**power * value
    return value * reversal if internal else value


def quantum_negative_word(matrix, reversal, coefficients, right_turn=True):
    value = reversal.copy()
    for i, coefficient in enumerate(coefficients):
        value = value * matrix**(-coefficient)
        if i + 1 < len(coefficients) or right_turn:
            value = value * reversal
    return value


def matrix_diagnostics(precision, max_level):
    mp.mp.dps = precision
    rows = []
    examples = ([2, -2], [3, 2], [-3, 2, 2], [-2, 3, -2, 2], [2] * 4)
    tolerance = mp.mpf(10) ** (-(precision - 30))
    for level in range(2, max_level + 1):
        matrix, _, _ = original_matrices(level)
        reversal = mp.matrix(level)
        for j in range(level):
            reversal[j, level - 1 - j] = 1
        kappa = mp.exp(1j * mp.pi * (level - 1)**2 / (2 * level))
        for powers in examples:
            normal = internal_normal_form(powers)
            left = quantum_word(matrix, reversal, powers, True)
            right = (
                kappa**normal["kappa_exponent"]
                * matrix**normal["left_power"]
                * quantum_negative_word(
                    matrix, reversal, normal["negative_magnitudes_from_outside"]
                )
                * matrix**normal["right_power"]
            )
            error = mp.norm(left - right) / max(1, mp.norm(left), mp.norm(right))
            assert error < tolerance
            rows.append({
                "N": level, "powers_from_inside": powers,
                "relative_matrix_error": mp.nstr(error, 20),
            })
            pendant = pendant_normal_form(powers)
            if pendant is None:
                continue
            cap = mp.matrix(level, 1)
            cap[0] = 1
            left_cap = quantum_word(matrix, reversal, powers, False) * cap
            right_cap = (
                kappa**pendant["cap_kappa_exponent"]
                * matrix**pendant["left_power"]
                * quantum_negative_word(
                    matrix, reversal, pendant["negative_magnitudes_from_outside"],
                    False,
                ) * cap
            )
            error = mp.norm(left_cap - right_cap) / max(
                1, mp.norm(left_cap), mp.norm(right_cap)
            )
            assert error < tolerance
            rows[-1]["relative_pendant_error"] = mp.nstr(error, 20)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=4)
    parser.add_argument("--max-power", type=int, default=3)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--max-level", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert args.max_length >= 1 and args.max_power >= 2 and args.precision >= 60
    counts = {"all_words": 0, "internal_forms": 0, "pendant_forms": 0}
    rotations = {}
    longest = 0
    for length in range(1, args.max_length + 1):
        for powers in product(range(-args.max_power, args.max_power + 1), repeat=length):
            counts["all_words"] += 1
            normal = internal_normal_form(powers)
            if normal:
                counts["internal_forms"] += 1
                rotation = normal["rotation"]
                rotations[rotation] = rotations.get(rotation, 0) + 1
                longest = max(longest, len(normal["negative_magnitudes_from_outside"]))
            if pendant_normal_form(powers):
                counts["pendant_forms"] += 1
    examples = []
    for powers in ([2, -2], [3, 2], [-3, 2, 2], [-2, 3, -2, 2], [2] * 4):
        examples.append({
            "internal": internal_normal_form(powers),
            "pendant": pendant_normal_form(powers),
        })
    here = Path(__file__).resolve()
    dependency_paths = [
        here,
        here.with_name("check_rational_corridor_compression.py"),
        here.with_name("check_twist_period_insertion.py"),
    ]
    result = {
        "scope": (
            "Exact continued-fraction, full affine, scalar-exponent and "
            "continuant checks. The original quantum-matrix checks are "
            "finite-precision diagnostics. No asymptotic or positivity claim."
        ),
        "sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in dependency_paths
        },
        "max_length": args.max_length,
        "max_absolute_power": args.max_power,
        "exact_counts": counts,
        "retained_rotations": rotations,
        "maximum_normal_form_length": longest,
        "decimal_precision": args.precision,
        "matrix_diagnostics": matrix_diagnostics(args.precision, args.max_level),
        "examples": examples,
        "status": "all asserted checks passed",
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
