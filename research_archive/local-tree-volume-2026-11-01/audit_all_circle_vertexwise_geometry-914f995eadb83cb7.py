#!/usr/bin/env python3
"""Exact rational enclosures used in the vertexwise geometric proof.

These finite comparisons check its constants, not the global topology,
holomorphic fixed-point theorem, or primitive metric completion.
"""
from fractions import Fraction as F
import argparse
import json
import hashlib
from pathlib import Path


def main():
    radius = F(1, 100)
    half_radius = radius / 2
    a, b, delta = F(1, 79000), F(1, 199), F(1, 39000)
    omega = b ** 4
    checks = [
        ("sinh bound", half_radius / (1-half_radius**2/6), b),
        ("cosh minus one bound",
         half_radius**2/(2*(1-half_radius**2/12)), a),
        ("first error derivative",
         (2*a/(1-a)+omega)/(1-omega), delta),
        ("second error derivative", b*b/(1-omega), delta),
        ("invariant disk using pi < 22/7",
         2*F(22,7)/630+delta*radius, radius),
        ("maximum norm contraction", 2*delta, F(1)),
        ("positive denominator fraction", delta, F(1)),
        ("global old condition implies local condition",
         F(630**2), F(2**25)),
    ]
    result = []
    for name, lower, upper in checks:
        if not lower < upper:
            raise AssertionError((name, lower, upper))
        result.append({"name": name, "lower": str(lower),
                       "upper": str(upper), "strict_margin": str(upper-lower)})
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name('all_circle_vertexwise_geometry_results.json'))
    args = parser.parse_args()
    record = {"script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Exact rational constants only; geometric and analytic proofs remain separate.",
              "checks": result, "check_count": len(result)}
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"checks": len(result), "output": str(args.output)}))


if __name__ == "__main__":
    main()
