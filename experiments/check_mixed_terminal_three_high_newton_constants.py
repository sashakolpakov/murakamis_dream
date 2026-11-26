#!/usr/bin/env python3
"""Exact scalar constants for the upper Newton half; no roots or source sweep."""
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
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    catalan_upper = sum(((-1)**j * F(1, (2*j+1)**2) for j in range(101)), F(0))
    check("alternating Catalan upper partial sum", catalan_upper < F(229, 250))
    log2_lower = 2*sum((F(1, 3)**(2*j+1)/(2*j+1) for j in range(4)), F(0))
    check("positive log2 lower partial sum", log2_lower > F(693, 1000))
    check("sqrt3 rational lower", F(433, 250)**2 < 3)
    x = F(6, 25)*F(22, 7)
    check("upper exponential parameter", x == F(132, 175) and x < 22)
    exp_upper = taylor(x, 20)+x**21/(factorial(21)*(1-x/22))
    check("log1plusexp upper", 1+exp_upper < taylor(F(57, 50), 20))
    ceiling = (2*F(229, 250)/F(157, 50)+F(57, 200)
               +(F(57, 50)-F(693, 1000))**2/(4*F(157, 50)*F(433, 250)))
    check("exact scalar ceiling", ceiling == F(95458861, 108769600))
    check("scalar ceiling below .878", ceiling < F(439, 500))
    check("finite source tolerance", F(439, 500)+F(1, 1000) == F(879, 1000))
    check("calibrated reserve", F(89, 100)-F(879, 1000) == F(11, 1000))
    check("strict loss .01", F(11, 1000) > F(1, 100))
    result = dict(status="passed", exact_checks=len(checks), checks=checks,
                  scalar_ceiling=str(ceiling), finite_rate=str(F(879, 1000)),
                  calibrated_loss=str(F(1, 100)),
                  scope="Exact rational constants only. The finite-source and geometric "
                        "implications are proved in research_mixed_terminal_three_high_newton.md. "
                        "No root search, source evaluation or parameter subdivision.")
    if args.output:
        assert not args.output.exists(), "saved records are immutable"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact rational scalar checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
