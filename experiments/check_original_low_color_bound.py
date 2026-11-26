#!/usr/bin/env python3
"""Check the original divided differences and their uniform low-color bound.

This compares literal signed powers of the original crossing matrix with
distinct-node interpolation. The proof for all levels and all powers is in
notes/research_original_low_color_bound.md; finite tests do not replace it.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def relative(a, b):
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for level in range(2, 21):
        theta = mp.pi/level
        q = mp.exp(1j*theta)
        kappa = mp.exp(1j*theta*(level-1)**2/2)
        crossing, _, _ = original_matrices(level)
        first = mp.eye(level)[:, 0]
        s = [mp.mpf(0)]+[2*mp.sin(j*theta) for j in range(1, level)]
        factorial = [mp.mpf(1)]
        for sine in s[1:]:
            factorial.append(factorial[-1]*sine)
        nodes = [2*mp.cos((2*r+1)*theta) for r in range((level+1)//2)]
        powers = sorted({0, 1, -1, 2, -2, 3, -3, 4, -4, 7, -7,
                         level+1, -level-1, 2*level+1, -2*level-1})
        columns = {power: crossing**power*first for power in powers}
        maximum = mp.mpf(0)
        low_maximum = mp.mpf(0)
        checked = 0
        for j in range((level-1)//2+1):
            denominators = [mp.fprod(nodes[r]-nodes[h]
                                    for h in range(j+1) if h != r)
                            for r in range(j+1)]
            weights = [factorial[j]**2/abs(d) for d in denominators]
            if 2*j+1 < level:
                sequence = [factorial[j]**2/(factorial[j+r]*factorial[j-r])
                            for r in range(j+1)]+[mp.mpf(0)]
                for r in range(j+1):
                    exact_weight = (factorial[j]**2*s[2*r+1]
                                    /(factorial[j+r+1]*factorial[j-r]))
                    telescoping = ((sequence[r]-sequence[r+1])
                                   *mp.cos((r+mp.mpf(".5"))*theta)
                                   /mp.cos((j+mp.mpf(".5"))*theta))
                    maximum = max(maximum, relative(weights[r], exact_weight),
                                  relative(weights[r], telescoping))
                    assert sequence[r] >= sequence[r+1]-tolerance
                bound = mp.cos(theta/2)/mp.cos((j+mp.mpf(".5"))*theta)
                assert mp.fsum(weights) <= bound+tolerance
            else:
                assert level % 2 and j == (level-1)//2
                for r in range(j+1):
                    exact_weight = 1 if r == j else 2*mp.cos((j-r)*theta)
                    maximum = max(maximum, relative(weights[r], exact_weight))
                bound = 1/mp.sin(theta/2)
                maximum = max(maximum, relative(mp.fsum(weights), bound))
            for power, column in columns.items():
                values = [(kappa*(-1)**r*q**(r*(r+1)))**power
                          for r in range(j+1)]
                interpolated = (-1)**j*factorial[j]**2*mp.fsum(
                    values[r]/denominators[r] for r in range(j+1))
                maximum = max(maximum, relative(interpolated, column[j]))
                assert abs(column[j]) <= bound+tolerance
                if j <= (level-2)//4:
                    assert abs(column[j]) <= mp.sqrt(2)+tolerance
                    low_maximum = max(low_maximum, abs(column[j]))
                checked += 1
        assert maximum < tolerance, (level, maximum)
        records.append({
            "N": level, "signed_powers": powers,
            "original_coefficients_checked": checked,
            "last_distinct_index": (level-1)//2,
            "odd_simple_endpoint_checked": bool(level % 2),
            "maximum_relative_identity_error": mp.nstr(maximum, 25),
            "maximum_low_quarter_coefficient": mp.nstr(low_maximum, 25),
        })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = run(args.precision)
    source = Path(__file__).resolve()
    dependencies = ("check_twist_period_insertion.py",
                    "check_internal_vertex_asymptotic.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Finite original coefficient, interpolation-weight and bound "
                 "checks, including negative and level-dependent powers. "
                 "The uniform theorem is proved in the accompanying note.",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "dependency_sha256": {
            "experiments/"+name: hashlib.sha256(
                source.with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "levels": len(records),
        "coefficient_checks": sum(r["original_coefficients_checked"] for r in records),
        "maximum_relative_identity_error": max(
            (r["maximum_relative_identity_error"] for r in records), key=mp.mpf),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
