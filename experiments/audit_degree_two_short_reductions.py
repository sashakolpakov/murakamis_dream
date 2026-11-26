#!/usr/bin/env python3
"""Exact cyclotomic checks for the degree-two short-source reductions.

The all-level proof is in notes/research_degree_two_short_reductions.md.
No floating point arithmetic or evaluation only at distinct roots is used.
Requires SymPy.
"""

import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ


def check_level(level):
    variable = sp.Symbol("x")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(4 * level, variable), variable)
    field = QQ.alg_field_from_poly(cyclotomic, alias="x")
    x = field([1, 0])
    q, imaginary = x * x, x**level
    degree = level - 1
    kappa = x ** (degree * degree)
    sine = [field.one]
    for k in range(1, level):
        sine.append(sine[-1] * (q**k - q ** (-k)) / imaginary)
    assert all(sine)
    crossing = [
        [kappa * (-1)**i * q ** (i * (j + 1)) * sine[i]
         / (sine[j] * sine[i - j]) if j <= i else field.zero
         for j in range(level)]
        for i in range(level)
    ]
    inverse = [
        [kappa**-1 * (-1)**i * q ** (-i * (j + 1)) * sine[i]
         / (sine[j] * sine[i - j]) if j <= i else field.zero
         for j in range(level)]
        for i in range(level)
    ]
    for i in range(level):
        assert sine[i] * sine[degree - i] == field(level)
        for j in range(level):
            product = sum(
                (crossing[i][k] * inverse[k][j] for k in range(level)),
                field.zero,
            )
            assert product == (field.one if i == j else field.zero)
            reversed_product = kappa * sum(
                (inverse[i][k] * inverse[degree - k][j]
                 for k in range(level)), field.zero,
            )
            assert crossing[degree - i][degree - j] == reversed_product
            two_boundary = kappa * sum(
                (inverse[i][k] * inverse[j][k] for k in range(level)),
                field.zero,
            )
            assert crossing[degree - i][j] == two_boundary
    return {
        "level": level,
        "cyclotomic_order": 4 * level,
        "field_degree": cyclotomic.degree(),
        "matrix_entries_per_identity": level * level,
        "identities": [
            "M times inverse(M) = identity",
            "J M J = kappa inverse(M) J inverse(M)",
            "J M = kappa inverse(M) transpose(inverse(M))",
        ],
        "exact": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-level", type=int, default=2)
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 2 <= args.min_level <= args.max_level:
        parser.error("require 2 <= min-level <= max-level")
    records = [check_level(level)
               for level in range(args.min_level, args.max_level + 1)]
    result = {
        "arithmetic": "exact rational cyclotomic fields",
        "matrix_identity_entry_checks": sum(
            3 * record["matrix_entries_per_identity"] for record in records
        ),
        "records": records,
        "passed": True,
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
