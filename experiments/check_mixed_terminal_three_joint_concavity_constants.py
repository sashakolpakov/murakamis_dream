#!/usr/bin/env python3
"""Exact scalar inequalities for the reduced terminal type-three Hessian."""

import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path


def sine(x, degree):
    return sum(((-1)**j*x**(2*j+1)/factorial(2*j+1)
                for j in range((degree+1)//2)), F(0))


def cosine(x, degree):
    return sum(((-1)**j*x**(2*j)/factorial(2*j)
                for j in range(degree//2+1)), F(0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    # Use the classical rational enclosure 157/50 < pi < 22/7.
    # All sine/cosine arguments below lie in (0, pi/2), and their
    # alternating Taylor terms decrease. Degrees 7 and 6 give lower
    # bounds for sine and cosine; degrees 5 and 8 give upper bounds.
    pi_lo, pi_hi = F(157, 50), F(22, 7)
    check("Taylor argument range", 2*pi_hi/5 < pi_lo/2)
    x = 6*pi_hi/25
    cosh_upper = sum((x**(2*j)/factorial(2*j) for j in range(9)), F(0))
    cosh_upper += x**18/(factorial(18)*(1-x*x/(19*20)))
    check("cosh(6pi/25) < 13/10", cosh_upper < F(13, 10))

    check("sin(pi/5) > 29/50", sine(pi_lo/5, 7) > F(29, 50))
    check("sin(2pi/5) > 19/20", sine(2*pi_lo/5, 7) > F(19, 20))
    check("sin(pi/10) > 3/10", sine(pi_lo/10, 7) > F(3, 10))
    check("cos(pi/5) > 4/5", cosine(pi_hi/5, 6) > F(4, 5))
    check("cos(pi/5) < 81/100", cosine(pi_lo/5, 8) < F(81, 100))
    check("cos(2pi/5) > 3/10", cosine(2*pi_hi/5, 6) > F(3, 10))
    check("cos(2pi/5) < 31/100", cosine(2*pi_lo/5, 8) < F(31, 100))
    check("cos(pi/10) < 24/25", cosine(pi_lo/10, 8) < F(24, 25))

    # cot(pi*s) = tan(pi*(1/2-s)). The displayed quotient is an
    # upper bound: an upper sine polynomial over a positive lower
    # cosine polynomial, evaluated at the larger rational argument.
    for s, target in [(F(3, 10), F(3, 4)),
                      (F(7, 20), F(13, 25)),
                      (F(2, 5), F(1, 3)),
                      (F(21, 50), F(13, 50)),
                      (F(47, 100), F(1, 10))]:
        x = pi_hi*(F(1, 2)-s)
        denominator = cosine(x, 2)
        check(f"cot(pi*{s}) < {target}",
              denominator > 0 and sine(x, 5)/denominator < target)

    # Lower bounds for C(x)=sin(2pi*x)/(13/10-cos(2pi*x)).
    endpoint_bounds = {
        F(1, 10): (F(29, 50)/(F(13, 10)-F(4, 5)), F(19, 20)),
        F(1, 5): (F(19, 20)/(F(13, 10)-F(3, 10)), F(19, 20)),
        F(1, 4): (F(10, 13), F(3, 4)),
        F(3, 10): (F(19, 20)/(F(13, 10)+F(31, 100)), F(7, 12)),
        F(2, 5): (F(29, 50)/(F(13, 10)+F(81, 100)), F(1, 4)),
        F(9, 20): (F(3, 10)/(F(13, 10)+F(24, 25)), F(13, 100)),
    }
    for x, (derived, target) in endpoint_bounds.items():
        # Equality is permitted here because the trigonometric input
        # inequalities are already strict.
        check(f"C({x}) > {target}", derived >= target)
    check("C decreases on [1/5,9/20]", F(13, 10)*F(31, 100) < 1)

    margins = {
        "external low": F(7, 12)-2*F(13, 50),
        "external high": F(13, 100),
        "terminal [1/5,1/4]": 3*F(3, 4)-2*F(3, 4)-2*F(13, 50),
        "terminal [1/4,3/10]": 3*F(7, 12)-2*F(13, 25)-2*F(1, 10),
        "terminal [3/10,2/5]": 3*F(1, 4)-2*F(1, 3),
        "terminal [2/5,9/20]": 3*F(13, 100),
        "Newton [1/10,1/5]": 4*F(19, 20)-2*F(3, 4),
        "Newton [1/5,3/10]": 4*F(7, 12)-2*F(1, 3),
        "Newton [3/10,2/5]": F(1),
    }
    for name, margin in margins.items():
        check(f"Gershgorin margin: {name}", margin > F(3, 50))
    result = {
        "status": "passed",
        "exact_checks": len(checks),
        "checks": checks,
        "hessian_lower_bound_divided_by_pi": "3/50",
        "row_margins": {k: str(v) for k, v in margins.items()},
        "scope": "Exact rational scalar constants only. The phase, branch, "
                 "matrix and finite-source implications require their written "
                 "proofs. No root search, source evaluation or parameter cover.",
    }
    if args.output:
        assert not args.output.exists(), "saved records are immutable"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Checked {len(checks)} exact rational scalar inequalities.")


if __name__ == "__main__":
    main()
