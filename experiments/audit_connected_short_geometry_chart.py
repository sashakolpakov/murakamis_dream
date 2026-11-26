#!/usr/bin/env python3
"""Check the exact rational bounds for the 1/64 positive edge chart."""

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    r, h, e, z, b, a = F(1, 127), F(1, 16000), F(1, 15000), F(1, 175), F(1, 32000), F(3, 500)
    checks = []

    def less(name, value, bound):
        assert value < bound, (name, value, bound)
        checks.append({"name": name, "upper_expression": str(value),
                       "bound": str(bound), "strict": True})

    less("tan bound", F(128, 16383), r)
    less("inverse square root bound", F(1), (1+h)**2 * (1-2*r*r))
    less("E displacement", h/(1-F(5, 7)*h), e)
    less("Z displacement", (e+(F(10, 7)+e)*(1+h)*r)/2, z)
    less("equatorial R displacement", r*r/(2*(1-r*r)), b)
    less("A+ displacement", z, a)
    less("A- displacement", (z+F(5, 7)*e)/(1-e), a)
    denominator_plus = F(1, 2)-z-b
    denominator_minus = F(1, 2)-z-b-e/2-e*b
    less("positive B+ denominator", F(0), denominator_plus)
    less("positive B- denominator", F(0), denominator_minus)
    less("B+ displacement", (z/2+b+b*z)/denominator_plus, a)
    less("B- displacement", (z/2+b+F(5, 14)*e+b*z+F(5, 7)*e*b)/denominator_minus, a)
    delta = 4*a
    less("oriented shape displacement", (4*delta+2*delta*delta)/(1-delta)**2, F(1, 8))
    less("two-vertex minimal-degree saddle bound", F(7, 512), F(1, 64))
    result = {"arithmetic": "exact rational inequalities",
              "angular_bidisk_radius": "1/64",
              "oriented_shape_distance_from_i": "< 1/8",
              "checks": checks, "passed": True}
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
