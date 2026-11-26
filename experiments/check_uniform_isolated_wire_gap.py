#!/usr/bin/env python3
"""Check the finite rational constants in the uniform wire-gap proof."""

import argparse
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    catalan_upper = sum(Q((-1)**j, (2*j+1)**2) for j in range(33))
    pi_lower = 16 * sum(
        Q((-1)**j, (2*j+1)*5**(2*j+1)) for j in range(4)
    ) - Q(4, 239)
    exp_lower = sum(Q(19, 5)**j / factorial(j) for j in range(10))
    comparisons = {
        "M_infinity_upper": (4*catalan_upper, Q(7, 6)*pi_lower),
        "exponential_partial_sum": (Q(128, 3), exp_lower),
        "degree_at_least_four": (Q(1, 6), Q(112, 99)-Q(44, 49)),
        "degree_two": (Q(1, 6), Q(112, 99)-Q(11, 14)),
        "degree_one": (Q(1, 6), Q(56, 99)),
        "sqrt_two_upper_squared": (Q(2), Q(10, 7)**2),
    }
    for name, (left, right) in comparisons.items():
        if not left < right:
            raise ArithmeticError((name, left, right))
    assert Q(5, 2)-Q(7, 3) == Q(1, 6)
    assert Q(1, 6)-Q(3, 20) == Q(1, 60)
    report = {
        "scope": "Finite rational constants; the analytic implications are proved in the accompanying note.",
        "strict_comparisons": {
            name: {"left": str(left), "right": str(right)}
            for name, (left, right) in comparisons.items()
        },
        "uniform_action_margin": "1/6",
        "wire_tail_upper": "3/20",
        "uniform_omitted_wire_gap": "1/60",
    }
    rendered = json.dumps(report, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print("All six rational comparisons and both margin identities hold.")


if __name__ == "__main__":
    main()
