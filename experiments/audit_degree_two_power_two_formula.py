#!/usr/bin/env python3
"""Exact check of the two-crossing two-boundary factorial formula."""
import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ


def check_level(level):
    x = sp.Symbol("x")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(4 * level, x), x)
    field = QQ.alg_field_from_poly(cyclotomic, alias="x")
    root = field([1, 0])
    q, Q, imaginary = root**2, root**4, root**level
    D = level - 1
    kappa = root**(D * D)
    sine = [field.one]
    factorial = [field.one]
    for j in range(1, level):
        sine.append(sine[-1] * (q**j - q**(-j)) / imaginary)
        factorial.append(factorial[-1] * (1 - Q**j))
    factorial.extend([field.zero] * D)
    crossing = [
        [kappa * (-1)**i * q**(i * (j + 1)) * sine[i]
         / (sine[j] * sine[i - j]) if i >= j else field.zero
         for j in range(level)]
        for i in range(level)
    ]
    for i in range(level):
        for j in range(level):
            traced = sum(
                (crossing[D - i][a] * crossing[a][j]
                 for a in range(level)), field.zero
            )
            explicit = (
                field(level) * q**((i - j)**2) * factorial[i + j]
                / (factorial[i]**2 * factorial[j]**2)
            )
            assert traced == explicit, (level, i, j)
    return {"level": level, "exact_coefficient_checks": level**2}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_level < 2:
        parser.error("require max-level >= 2")
    records = [check_level(n) for n in range(2, args.max_level + 1)]
    result = {
        "arithmetic": "exact rational cyclotomic fields",
        "scope": "all coefficients of the two-boundary polynomial, including the quotient normal data",
        "checks": sum(r["exact_coefficient_checks"] for r in records),
        "records": records,
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()

