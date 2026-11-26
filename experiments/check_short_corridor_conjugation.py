#!/usr/bin/env python3
"""Exact checks for the threshold and modular-conjugacy presentation criteria.

All arithmetic is integer/rational. This checks no quantum asymptotic and
asserts no faithfulness of the finite-level quantum representation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


IDENTITY = (1, 0, 0, 1)
S = (0, -1, 1, 0)
U = (0, -1, 1, 1)


def multiply(a, b):
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def projective(a):
    first = next(x for x in a if x)
    return a if first > 0 else tuple(-x for x in a)


def reduce_word(word):
    stack = []
    for factor, exponent in word:
        if stack and stack[-1][0] == factor:
            exponent = (stack.pop()[1] + exponent) % (2 if factor == "S" else 3)
            if exponent:
                stack.append((factor, exponent))
        else:
            stack.append((factor, exponent))
    return stack


def inverse_word(word):
    return [(g, (-e) % (2 if g == "S" else 3)) for g, e in reversed(word)]


def cyclic_word(word):
    word = reduce_word(word)
    while len(word) > 1 and word[0][0] == word[-1][0]:
        word = reduce_word(word[1:] + word[:1])
    return word


def signature(word):
    word = cyclic_word(word)
    assert len(word) > 1 and len(word) % 2 == 0
    exponents = tuple(e for g, e in word if g == "U")
    return min(exponents[i:] + exponents[:i] for i in range(len(exponents)))


def crossing_block(n):
    return [("S", 1)] + (
        [("S", 1), ("U", 1)] * n
        if n > 0 else [("U", 2), ("S", 1)] * (-n)
    )


def original_matrix(powers):
    value = IDENTITY
    for n in powers:
        value = multiply(value, multiply(S, (1, n, 0, 1)))
    return projective(value)


def word_matrix(word):
    value = IDENTITY
    for g, e in word:
        matrix = S if g == "S" else U if e == 1 else multiply(U, U)
        value = multiply(value, matrix)
    return projective(value)


def maximal_run(sequence):
    assert len(set(sequence)) == 2
    return max(
        next(k for k in range(1, len(sequence)) if sequence[(i + k) % len(sequence)] != sequence[i])
        for i in range(len(sequence))
    )


def negative_fraction(coefficients):
    value = Fraction(coefficients[-1])
    for a in reversed(coefficients[:-1]):
        value = a - 1 / value
    return value


def ceiling_expansion(value):
    result = []
    while True:
        a = -(-value.numerator // value.denominator)
        result.append(a)
        remainder = a - value
        if not remainder:
            return tuple(result)
        value = 1 / remainder


def threshold_criterion(coefficients, threshold):
    if min(coefficients) >= threshold:
        return True
    if set(coefficients) == {2}:
        return len(coefficients) >= threshold - 1
    if not set(coefficients) <= {2, 3}:
        return False
    runs = [0]
    for a in coefficients:
        if a == 2:
            runs[-1] += 1
        else:
            runs.append(0)
    return (
        runs[0] >= threshold - 2
        and runs[-1] >= threshold - 2
        and all(r >= threshold - 3 for r in runs[1:-1])
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    counts = {"threshold_comparisons": 0, "signed_seams_and_matrices": 0,
              "conjugacy_signatures": 0, "positive_exact_sequences": 0}
    for length in range(1, 5):
        for coefficients in product(range(2, 10), repeat=length):
            value = negative_fraction(coefficients)
            dual = ceiling_expansion(value / (value - 1))
            assert negative_fraction(dual) == value / (value - 1)
            for threshold in range(3, 10):
                observed = min(coefficients) >= threshold or min(dual) >= threshold
                assert observed == threshold_criterion(coefficients, threshold)
                counts["threshold_comparisons"] += 1
        for powers in product((-9, -8, -4, -3, 3, 4, 8, 9), repeat=length):
            word = sum((crossing_block(n) for n in powers), [])
            assert original_matrix(powers) == word_matrix(reduce_word(word))
            exponents = signature(word)
            assert maximal_run(exponents) >= max(abs(n) for n in powers) - 2
            counts["signed_seams_and_matrices"] += 1
            if min(powers) > 0:
                predicted = sum(([2] + [1] * (n - 2) for n in powers), [])
                canonical = min(tuple(predicted[i:] + predicted[:i]) for i in range(len(predicted)))
                assert exponents == canonical
                counts["positive_exact_sequences"] += 1
    generators = (("S", 1), ("U", 1), ("U", 2))
    for r in range(1, 7):
        core = crossing_block(3) * r
        expected = signature(core)
        assert maximal_run(expected) == 1
        for length in range(6):
            for conjugator in product(generators, repeat=length):
                conjugate = list(conjugator) + core + inverse_word(conjugator)
                assert signature(conjugate) == expected
                counts["conjugacy_signatures"] += 1
    root = Path(__file__).resolve().parents[1]
    dependencies = [
        Path(__file__).resolve(),
        root / "notes/research_affine_reduction_fibers_and_core_obligation.md",
        root / "notes/research_definite_rational_corridor_normal_form.md",
        root / "notes/research_binary_negative_corridor_positive_reexpression.md",
        root / "notes/research_uniform_path_trace_assembly.md",
        root / "notes/research_network_whole_boundary_decay.md",
        root / "notes/research_boundary_crossing_packet_preservation.md",
    ]
    result = {
        "status": "all exact checks passed",
        "scope": "Presentation algebra only; no asymptotic or finite-level faithfulness claim.",
        "counts": counts,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)


if __name__ == "__main__":
    main()
