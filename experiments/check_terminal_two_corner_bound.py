#!/usr/bin/env python3
"""Check the rational bounds excluding a terminal-two / neighbor-six corner.

The written argument is Proposition 7 in
notes/research_negative_two_chain_original_periods.md.  This program checks
its rational constants only.  It does not replace the analytic monotonicity,
corner optimality, or marked metric-completion proofs.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


Q = Fraction


def sinh_majorant(x):
    """Written proof: sinh(x) <= this polynomial for 0 < x <= 1."""
    return x + x**3 / 6 + x**5 / 120 + x**7 / 4970


def run():
    checks = []

    def less(name, left, right, meaning):
        left, right = Q(left), Q(right)
        assert left < right, (name, left, right)
        checks.append({
            "name": name,
            "left": str(left),
            "right": str(right),
            "positive_gap": str(right - left),
            "meaning": meaning,
        })

    # sin(7*pi/26) <= (1+pi/52)/sqrt(2), and pi < 22/7.
    sine_numerator = 1 + Q(22, 7) / 52
    assert sine_numerator == Q(193, 182)
    less(
        "sine_comparison_squared",
        sine_numerator**2,
        2 * Q(3, 4)**2,
        "The tangent-line upper bound is smaller than 3/4.",
    )

    # At the comparison point sin(delta)=3/4, X=asinh(9/8)/2.
    x = Q(121, 125)
    sinh_lower = x + x**3 / 6 + x**5 / 120
    less(
        "X_upper_bound",
        Q(9, 8),
        sinh_lower,
        "The positive sinh series proves X < 121/250.",
    )

    # H=asinh(1/12)/2.  The lower estimate is 1/(2*sqrt(145)).
    less(
        "H_lower_bound_squared",
        4 * 145,
        25**2,
        "The integral lower bound for asinh gives H > 1/25.",
    )
    # H < 1/24 follows directly from asinh(t)<t.
    x_upper, h_lower, h_upper = Q(121, 250), Q(1, 25), Q(1, 24)
    u_upper = (11 * x_upper - 4 * h_lower) / 13
    v_upper = (12 * x_upper + 11 * h_upper) / 13
    less(
        "corner_U_bound",
        u_upper,
        Q(2, 5),
        "The real equations and monotonicity give U < 2/5.",
    )
    less(
        "corner_V_bound",
        v_upper,
        Q(483, 1000),
        "The real equations and monotonicity give V < 483/1000.",
    )

    # The omitted sinh tail begins at x^7/7! and has ratio <= 1/72.
    assert Q(5040) * (1 - Q(1, 72)) == 4970
    first_argument, second_argument = Q(4, 5), Q(483, 500)
    assert 0 < first_argument <= 1 and 0 < second_argument <= 1
    product = sinh_majorant(first_argument) * sinh_majorant(second_argument)
    less(
        "corner_product_below_one",
        product,
        Q(499, 500),
        "The two sinh factors have product <499/500<1.",
    )
    return {
        "scope": (
            "Exact rational diagnostic for equations (61), (63)-(65) of "
            "Proposition 7. The written proof supplies the analytic, "
            "geometric, branch and peripheral arguments."
        ),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "fractions.Fraction; no floating-point decisions",
        "checked_inequalities": checks,
        "sinh_product_upper_bound": str(product),
        "gap_below_one": str(1 - product),
        "conclusion_of_written_proof": (
            "A terminal magnitude-two corner has neighboring magnitude at "
            "most five. This is a geometric criterion, not a quantum "
            "asymptotic or a general theorem for internal runs of twos."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Verified {len(result['checked_inequalities'])} exact rational bounds.")
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
