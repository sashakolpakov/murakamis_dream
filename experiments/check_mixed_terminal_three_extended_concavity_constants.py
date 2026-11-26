#!/usr/bin/env python3
"""Additional exact constants for the terminal rectangle 3/20 <= Re(t) <= 1/2."""

import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path

from check_mixed_terminal_three_joint_concavity_constants import sine, cosine


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    pi_lo, pi_hi = F(157, 50), F(22, 7)
    for factor, upper in [(F(11, 50), F(121, 100)),
                          (F(3, 20), F(197, 100))]:
        x = factor*pi_lo
        check(f"cot(pi*{factor}) < {upper}",
              sine(x, 7) > 0 and cosine(x, 8)/sine(x, 7) < upper)
    r, c = F(121, 100), F(197, 100)
    polynomial = 13*r*r-13*c*r-3*c*r**3+23
    denominator = (3*r*r+23)*(r+c)
    check("left external-row polynomial positive", polynomial > 0)
    check("polynomial decreasing in r", F(169, 9)/c-13*c < 0)
    check("left external-row margin", 2*polynomial/denominator > F(1, 100))

    x_lo, x_hi = 7*pi_lo/20, 7*pi_hi/20
    check("sin(7pi/20) > 22/25", sine(x_lo, 7) > F(22, 25))
    check("cos(7pi/20) > 11/25", cosine(x_hi, 6) > F(11, 25))
    check("C(7/40) > 1", F(22, 25)/(F(13, 10)-F(11, 25)) > 1)
    for factor, upper in [(F(37, 100), F(11, 25)),
                          (F(11, 40), F(9, 10)),
                          (F(79, 200), F(2, 5)),
                          (F(9, 20), F(17, 100))]:
        x = (F(1, 2)-factor)*pi_hi
        check(f"cot(pi*{factor}) < {upper}",
              cosine(x, 2) > 0 and sine(x, 5)/cosine(x, 2) < upper)
    margins = [3-2-2*F(11, 25),
               3*F(19, 20)-2*F(9, 10)-2*F(2, 5),
               4*F(19, 20)-2,
               4*F(7, 12)-2*F(13, 25),
               1-2*F(17, 100)]
    check("all remaining left-strip row margins", min(margins) > F(1, 100))

    x = 12*pi_hi/25
    cosh_upper = sum((x**(2*j)/factorial(2*j) for j in range(9)), F(0))
    cosh_upper += x**18/(factorial(18)*(1-x*x/(19*20)))
    check("cosh(12pi/25) < 12/5", cosh_upper < F(12, 5))
    check("cos(pi/10) > 19/20", cosine(pi_hi/10, 6) > F(19, 20))
    check("sin(pi/5) < 3/5", sine(pi_hi/5, 5) < F(3, 5))
    check("right shifted-cotangent first endpoint",
          F(3, 10)/(F(12, 5)-F(19, 20)) > F(1, 5))
    check("right shifted-cotangent last endpoint",
          F(4, 5)/(F(12, 5)+F(3, 5)) > F(1, 5))
    check("right 2x2 block minus 1/100 is positive",
          (F(13, 100)+F(1, 5)-F(1, 100))
          *(F(1, 5)-F(1, 100))-F(1, 5)**2 == F(13, 625))
    check("free-target curvature after allocation",
          pi_lo/100-2*F(1, 2500000) > F(3, 100))
    result = dict(status="passed", exact_checks=len(checks), checks=checks,
                  hessian_lower_bound_divided_by_pi="1/100",
                  free_target_curvature="3/100",
                  scope="Additional rational scalar inequalities only. The earlier "
                        "joint-Hessian constants are reused without rerunning them. "
                        "No root search, source evaluation or parameter subdivision.")
    if args.output:
        assert not args.output.exists(), "saved records are immutable"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Checked {len(checks)} additional exact scalar inequalities.")


if __name__ == "__main__":
    main()
