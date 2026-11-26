#!/usr/bin/env python3
"""Exact rational checks for the consequences of H < 23/20.

These checks do not certify the height premise itself. That is the separate
maximum-height support certificate. Every comparison here uses Fraction;
decimal values in the output are only for readability.
"""

import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-positive-path-energy-height-consequences.json",
    )
    args = parser.parse_args()
    checks = []

    def positive(name, margin):
        assert margin > 0, name
        checks.append(
            {"claim": name, "positive_rational_margin": str(margin),
             "decimal_margin": float(margin)}
        )

    x = Q(23, 20)
    positive("cosh tail ratios are below 1/60", Q(1, 60) - x * x / 90)
    cosh_upper = sum(x ** (2 * j) / math.factorial(2 * j) for j in range(4))
    cosh_upper += Q(60, 59) * x ** 8 / math.factorial(8)
    positive("cosh(23/20) < 7/4", Q(7, 4) - cosh_upper)
    positive("1/sqrt(2) > 7/10", Q(1, 2) - Q(7, 10) ** 2)
    product_upper = (Q(7, 4) + 1) / 2 * (Q(7, 4) - Q(7, 10)) / (
        Q(7, 4) + Q(7, 10)
    )
    assert product_upper == Q(33, 56)
    positive("the squared return modulus is below 5/8", Q(5, 8) - product_upper)
    positive("sqrt(2) < 7/4, hence cos(3*pi/8) > 1/4", Q(7, 4) ** 2 - 2)

    # Machin's identity pi = 16 atan(1/5) - 4 atan(1/239).
    # An odd number of alternating terms is an upper bound; an even
    # number is a lower bound. The identity also follows directly from
    # tangent addition and the range of these positive angles.
    def atan_partial(argument, number_of_terms):
        return sum(
            (-1) ** j * argument ** (2 * j + 1) / (2 * j + 1)
            for j in range(number_of_terms)
        )

    pi_upper = 16 * atan_partial(Q(1, 5), 11) - 4 * atan_partial(Q(1, 239), 4)
    positive("pi < 355/113", Q(355, 113) - pi_upper)
    catalan_lower = sum(
        Q((-1) ** j, (2 * j + 1) ** 2) for j in range(100)
    )
    assert Q(23, 20) * (1 + Q(8, 567)) == Q(2645, 2268)
    positive(
        "(23*pi/20)(1+8/567) < 4G",
        4 * catalan_lower - Q(2645, 2268) * Q(355, 113),
    )
    positive("the single-activation gap is positive", 4 * catalan_lower
             - Q(23, 20) * Q(355, 113))

    result = {
        "status": "passed",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact fractions",
        "height_premise": "H < 23/20, certified separately",
        "threshold": 562,
        "checks": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "checks"}
                     | {"checks_passed": len(checks)}, indent=2))


if __name__ == "__main__":
    main()
