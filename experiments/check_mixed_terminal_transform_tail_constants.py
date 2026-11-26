#!/usr/bin/env python3
"""Exact rational constants for terminal-transform tails; no roots or source cover."""
import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path


def taylor(x, degree):
    return sum((x**j / factorial(j) for j in range(degree + 1)), F(0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    values = {}
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    pi_lower, pi_upper = F(157, 50), F(22, 7)
    check("log2 upper via positive exp Taylor", taylor(F(7, 10), 4) > 2)
    check("log3 lower via artanh terms", 2*(F(1, 2)+F(1, 2)**3/3) == F(13, 12))
    check("sine at .45 lower", 2*(1-(pi_upper/20)**2/2) > F(19, 10))
    check("log1.9 lower", F(18, 29) > F(3, 5))
    check("pi over5 below2over3", pi_upper/5 < F(2, 3))
    low_corner = F(17, 72)-F(7, 250)
    high_corner_floor = F(7, 50)+2*F(3, 100)
    mixed_corner = F(1, 12)+F(17, 144)+F(3, 100)
    check("lower corner strict floor", low_corner > F(1, 5))
    # Both input inequalities at the upper corner are strict.
    check("upper corner floor", high_corner_floor == F(1, 5))
    check("mixed corner strict floor", mixed_corner > F(1, 5))
    vertical_cost = F(391, 1000)*F(2, 25)+F(9, 20)*F(21, 1000)
    check("vertical cost allocation", vertical_cost == F(4073, 100000))
    wire_floor = F(1, 5)-pi_upper*vertical_cost
    check("wire floor", wire_floor > F(7, 100))

    x = F(44, 125)*pi_lower
    cosine_upper = sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(5)), F(0))
    check("cosine alternating magnitudes", x*x < 2)
    check("summed-angle cosine", cosine_upper < F(9, 20))
    check("external-angle cosine", pi_upper/50 < F(63, 1000))
    x = F(54, 125)*pi_upper
    exp_upper = taylor(x, 20)+x**21/(factorial(21)*(1-x/22))
    check("positive geometric remainder denominator", 0 < x < 22)
    check("height exponential upper", exp_upper < F(389, 100))
    check("height exponential linear lower", 1-F(21, 500)*pi_upper == F(217, 250))
    ratio_upper = F(4890, 937)
    ratio_lower = F(11, 40)*F(217, 250)**2
    check("positive derivative upper", taylor(F(42, 25), 16) > ratio_upper)
    check("negative derivative lower", ratio_lower*taylor(F(8, 5), 16) > 1)

    kappa = F(1, 2500000)
    dmax = F(213, 1000)
    plane = F(107, 100)-F(21, 25)*dmax-kappa*dmax*dmax
    check("exact reference plane", plane == F(2227699954631, 2500000000000))
    check("full plateau plane", plane > F(89, 100))
    check("last-row height cost", F(6, 25)*pi_upper == F(132, 175))
    tail_rate = F(433, 500)+F(1, 500)
    check("low tail budget", tail_rate == F(217, 250))
    check("high tail budget", F(132, 175)+F(1, 500) < tail_rate)
    check("remaining strict rate reserve", F(89, 100)-tail_rate == F(11, 500))
    check("finite tail loss", F(11, 500) > F(1, 50))
    values.update(wire_floor=str(wire_floor), cosine_upper=str(cosine_upper),
                  exp_upper=str(exp_upper), ratio_lower=str(ratio_lower),
                  ratio_upper=str(ratio_upper), reference_plane=str(plane),
                  tail_rate=str(tail_rate), finite_loss=str(F(1, 50)))
    result = dict(status="passed", exact_checks=len(checks), checks=checks,
                  rational_values=values,
                  scope="Rational scalar constants only; analytic source, phase and contour "
                        "arguments remain those in research_mixed_terminal_transform_tails.md. "
                        "No root solve, source evaluation or parameter cover.")
    if args.output:
        assert not args.output.exists(), "do not overwrite a saved check"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact rational checks; no root or source computation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

