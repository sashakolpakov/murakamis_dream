#!/usr/bin/env python3
"""Exact rational checks for adjacent-pair connector bounds.

The only transcendental enclosure needed here is the existing rational
interval calculation of the upper principal phase and its gradient at
(31/400,1/4). Strong concavity then bounds the exact stationary value.
All other decisions below are Fraction comparisons.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

import verify_adjacent_two_crossing_horizontal_maximum as horizontal


def run():
    hessian = horizontal.local_hessian_certificate()
    value, gx, gy = horizontal.value_and_gradient(*horizontal.REFERENCE)
    # The certified negative Hessian is at least 2I on the convex rectangle.
    # Taylor's upper bound, maximized over displacement, is f(p)+|grad f|^2/4.
    gradient_squared = (
        horizontal.interval_absolute_upper(gx) ** 2
        + horizontal.interval_absolute_upper(gy) ** 2
    )
    saddle_upper = F(value.hi, horizontal.SCALE) + gradient_squared / 4
    assert saddle_upper < F(17, 20)

    catalan_lower = F(1) - F(1, 9) + F(1, 25) - F(1, 49)
    assert catalan_lower > F(9, 10)
    exp6_lower = sum(F(6**j, factorial(j)) for j in range(14))
    assert exp6_lower > 400
    corner_lower = F(189, 220) - F(2, 1197)
    assert corner_lower > F(17, 20)

    top_upper = F(21, 40) + F(1783, 1200) * F(25, 157)
    diagonal_upper = (
        (F(71, 100) * F(484, 75) + F(5, 16)) * F(25, 157)
        - F(1, 32)
    )
    assert top_upper == F(28697, 37680)
    assert diagonal_upper == F(281887, 376800)
    assert top_upper < F(61, 80)
    assert diagonal_upper < F(3, 4)
    known_saddle_lower = F(1500409991957, 1956907128000)
    assert known_saddle_lower > F(23, 30) > F(61, 80)
    return {
        "scope": "Principal y-deformation ribbons and an obstruction to separate deep corner bounds; no full lattice transfer.",
        "arithmetic": "Outward fixed-scale rational intervals and exact Fraction comparisons.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "saddle_upper": str(saddle_upper),
        "saddle_upper_is_less_than": "17/20",
        "local_hessian_certificate": hessian,
        "catalan_lower": str(catalan_lower),
        "exp6_lower": str(exp6_lower),
        "deep_corner_lower": str(corner_lower),
        "gap_above_saddle_upper": str(corner_lower - saddle_upper),
        "top_ribbon_upper": str(top_upper),
        "diagonal_ribbon_upper": str(diagonal_upper),
        "known_saddle_lower": str(known_saddle_lower),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Saved rational connector checks to {args.output}.")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
