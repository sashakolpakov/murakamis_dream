#!/usr/bin/env python3
"""Exact rational bounds for the internal power-three pair's energy trial.

This verifies scalar inequalities in the written geometric proof. The
variational principle, matching formula, and analytic source estimates
are separate arguments in the research notes.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=
                        "repro/results/research-three-pair-radical-energy-gap.json")
    args = parser.parse_args()
    pi_upper = F(22, 7)
    secants = {F(1, 16): F(51, 50), F(1, 8): F(13, 12),
               F(1, 4): F(10, 7), F(3, 16): F(121, 100),
               F(3, 8): F(21, 8)}
    margins = {}

    def positive(label, value):
        assert value > 0, (label, value)
        margins[label] = str(value)

    for angle, secant in secants.items():
        x = angle * pi_upper
        cosine_lower = sum(((-1) ** j * x ** (2*j) / factorial(2*j)
                            for j in range(4)), F(0))
        positive(f"secant_at_{angle}_pi", cosine_lower - 1/secant)

    energy_upper = sum(
        (F(weight) * (k*pi_upper/16)**2
         * (5 + 6*secants[F(k, 16)] + secants[F(k, 8)]) / 24
         for k, weight in [(1, 24), (2, 16), (3, 8)]), F(0))
    assert energy_upper == F(9283241, 2634240)
    positive("energy_below_18_over_5", F(18, 5) - energy_upper)
    catalan_lower = 1 - F(1, 9) + F(1, 25) - F(1, 49)
    positive("action_gap_above_1_over_100",
             (4*catalan_lower - F(18, 5))/pi_upper - F(1, 100))
    record = {
        "status": "passed",
        "arithmetic": "exact fractions",
        "scope": "scalar inequalities for the feasible-angle trial",
        "energy_upper": str(energy_upper),
        "catalan_lower": str(catalan_lower),
        "inequality_count": len(margins),
        "positive_margins": margins,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"passed {len(margins)} exact inequalities; {output}")


if __name__ == "__main__":
    main()
