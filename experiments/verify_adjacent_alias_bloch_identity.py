#!/usr/bin/env python3
"""Verify the four exact pentagon substitutions over Q(sqrt(-7)).

This checks algebraic arguments and Bloch--Wigner symmetry reductions.
It performs no numerical dilogarithm evaluation and proves no contour estimate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class Quadratic:
    a: F
    b: F = F(0)

    def __add__(self, other):
        other = scalar(other)
        return Quadratic(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-scalar(other))

    def __rsub__(self, other):
        return scalar(other) + (-self)

    def __mul__(self, other):
        other = scalar(other)
        return Quadratic(self.a * other.a - 7 * self.b * other.b,
                         self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a * self.a + 7 * self.b * self.b
        return Quadratic(self.a / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * scalar(other).inverse()

    def __rtruediv__(self, other):
        return scalar(other) * self.inverse()

    def conjugate(self):
        return Quadratic(self.a, -self.b)


def scalar(value):
    return value if isinstance(value, Quadratic) else Quadratic(F(value))


def canonical(value):
    """Return the sixfold symmetry class and sign of D(value)."""
    if not value.b:
        return None, 0
    sign = 1 if value.b > 0 else -1
    value = value if sign == 1 else value.conjugate()
    conjugate = value.conjugate()
    orbit = (value, 1 / (1 - value), (value - 1) / value,
             1 - conjugate, 1 / conjugate, conjugate / (conjugate - 1))
    return min(orbit, key=lambda z: (z.a, z.b)), sign


def formal_sum(terms):
    result = {}
    for value, coefficient in terms:
        representative, sign = canonical(value)
        if sign:
            result[representative] = (
                result.get(representative, 0) + coefficient * sign)
    return {key: value for key, value in result.items() if value}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-adjacent-alias-bloch-identity.json")
    args = parser.parse_args()

    delta = Quadratic(F(0), F(1))
    z, X, Y = (1 + delta) / 4, (5 + delta) / 16, delta / 7
    E, G, H = (-1 + delta) / 2, (-3 + delta) / 4, (-5 + delta) / 2
    pairs = (
        ((7 + delta) / 8, (5 - delta) / 4),
        ((7 + delta) / 8, scalar(2)),
        (X.conjugate(), X.conjugate()),
        (X.conjugate(), 2 * z),
    )
    expected = (
        [(Y, 1), (E, -2), (H, 1), (G, 1)],
        [(Y, 2), (G, -1), (z, -1)],
        [(X, -2), (X * Y, 1), (H, 2)],
        [(X, -1), (z, 2), (E, -2)],
    )
    relations = []
    for (r, s), expected_terms in zip(pairs, expected):
        product = r * s
        first = r * (1 - s) / (1 - product)
        second = s * (1 - r) / (1 - product)
        actual = formal_sum([(r, 1), (s, 1), (product, -1),
                             (first, -1), (second, -1)])
        assert actual == formal_sum(expected_terms)
        relations.append(actual)

    assert 2 * z * z - z + 1 == scalar(0)
    assert X == -(z * z * z)
    assert Y == z / (2 - z)
    assert 1 / (z * z).conjugate() == (X - 1) / X
    assert canonical(z * z) == canonical(X)

    # The target is twice row 1 plus twice row 2 minus row 3 minus twice row 4.
    combination = {}
    for weight, relation in zip((2, 2, -1, -2), relations):
        for key, coefficient in relation.items():
            combination[key] = combination.get(key, 0) + weight * coefficient
    combination = {key: value for key, value in combination.items() if value}
    target = formal_sum([(X, 3), (Y, 6), (X * Y, -1),
                         (z, -6), (z * z, 1)])
    assert combination == target

    result = {
        "status": "passed",
        "arithmetic": "exact fractions in Q(sqrt(-7))",
        "pentagon_relations": len(relations),
        "combination_coefficients": [2, 2, -1, -2],
        "conclusion": (
            "3D(X)+6D(Y)-D(XY)=6D(z)-D(z^2); "
            "the finite saddle and boundary alias have equal real actions"),
        "scope": (
            "Checks the exact algebraic witness. Does not determine "
            "complex phase constants, contour coefficients, or cancellation."),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
