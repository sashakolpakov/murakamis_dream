#!/usr/bin/env python3
"""Exact rational check of the boundary example in the -2 period note."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path


@dataclass(frozen=True)
class Gaussian:
    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other):
        if not isinstance(other, Gaussian):
            other = Gaussian(Q(other))
        return Gaussian(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Gaussian):
            other = Gaussian(Q(other))
        return Gaussian(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Gaussian):
            other = Gaussian(Q(other))
        norm = other.re**2 + other.im**2
        assert norm > 0
        return self * Gaussian(other.re / norm, -other.im / norm)

    def json(self):
        return [str(self.re), str(self.im)]


SCALE = 10**30
ONE = Gaussian(Q(1))
I = Gaussian(Q(0), Q(1))


def square_root_interval(value: Q):
    assert value >= 0
    k = isqrt(value.numerator * SCALE**2 // value.denominator)
    assert k**2 * value.denominator <= value.numerator * SCALE**2
    assert value.numerator * SCALE**2 < (k + 1)**2 * value.denominator
    return Q(k, SCALE), Q(k + 1, SCALE)


def squared_real_part_of_root(value: Gaussian):
    """Both square roots have the same squared real part."""
    lo, hi = square_root_interval(value.re**2 + value.im**2)
    return (lo + value.re) / 2, (hi + value.re) / 2


def verify():
    lam = Gaussian(Q(43, 50), Q(9, 200))
    cosines = [ONE, lam - I]
    for _ in range(3):
        cosines.append(2 * lam * cosines[-1] - cosines[-2])
    assert all(c.re > 0 and c.im < 0 for c in cosines[1:])
    tangent_squares = [ONE / (c * c) - ONE for c in cosines]
    assert tangent_squares[0] == Gaussian()
    assert all(a.im > 0 for a in tangent_squares[1:])
    rows = []
    lower_targets = [Q(19, 100), Q(1, 40), Q(1, 250)]
    for j in range(4):
        left, right = cosines[j : j + 2]
        q = I * (ONE - lam / (left * right))
        assert q * q == ONE + tangent_squares[j] + tangent_squares[j + 1]
        assert lam * lam - 2 * lam * left * right + left * left + right * right == Gaussian()
        assert q.re > 0 and (q * left).re > 0 and (q * right).re > 0
        a_lo, a_hi = squared_real_part_of_root(tangent_squares[j])
        b_lo, b_hi = squared_real_part_of_root(tangent_squares[j + 1])
        lo, hi = q.re**2 - a_hi - b_hi, q.re**2 - a_lo - b_lo
        if j < 3:
            assert lo > lower_targets[j]
        else:
            assert hi < -Q(1, 12500)
        rows.append({
            "edge": [j, j + 1],
            "q": q.json(),
            "real_q_times_left": str((q * left).re),
            "real_q_times_right": str((q * right).re),
            "positivity_margin": [str(lo), str(hi)],
        })
    return {
        "scope": "Three -2 vertices, one complete and one fixed complex outside boundary; not a complete-end counterexample.",
        "lambda": lam.json(),
        "cosines": [c.json() for c in cosines],
        "edges": rows,
        "square_root_scale": str(SCALE),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("Verified four exact edge identities and three positive / one negative cell margins.")
    print("The final outside boundary is complex; complete-end positivity remains unresolved.")
