#!/usr/bin/env python3
"""Check the finite identities used in the degree-three zero-power proof.

The reference trace is computed by division by the complete Chebyshev
polynomial. It therefore retains root multiplicities. The Fourier and
positive multiplication formulas are computed separately. These finite
checks support the normalization; the uniform gap has a written proof.
"""

import argparse
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ


def multiply(left, right, zero):
    result = [zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def trace(coefficients, modulus, level, field):
    remainder = coefficients[:]
    for degree in range(len(remainder) - 1, level - 1, -1):
        leading = remainder[degree]
        if leading:
            offset = degree - level
            for index, value in enumerate(modulus):
                remainder[offset + index] -= leading * value
    coefficient = remainder[level - 1] if len(remainder) >= level else field.zero
    return (-1) ** (level - 1) * level**2 * coefficient


def check_level(level):
    symbol = sp.Symbol("x")
    field = QQ.alg_field_from_poly(
        sp.Poly(sp.cyclotomic_poly(4 * level, symbol), symbol), alias="x"
    )
    root = field([1, 0])
    q, imaginary = root**2, root**level
    sine = [field.one]
    for index in range(1, level):
        sine.append(sine[-1] * (q**index - q**(-index)) / imaginary)
    modulus_expression = sp.Poly(2 * sp.chebyshevt(level, symbol / 2) + 2, symbol)
    modulus = [field(int(modulus_expression.nth(i))) for i in range(level + 1)]
    polynomials = [[field.one]]
    laurent = [[field.one]]
    for index in range(1, level):
        node = q ** (2 * index - 1) + q ** (-(2 * index - 1))
        scale = (sine[index] / sine[index - 1]) ** 2
        polynomials.append([
            value / scale
            for value in multiply(polynomials[-1], [node, -field.one], field.zero)
        ])
        # The array has exponents -index,...,index after multiplication.
        laurent.append([
            value / scale
            for value in multiply(laurent[-1], [field.one, node, field.one], field.zero)
        ])

    pairings = 0
    for i in range(level):
        for j in range(level):
            actual = trace(multiply(polynomials[i], polynomials[j], field.zero),
                           modulus, level, field)
            assert actual == field(int(i + j == level - 1)), (level, i, j, "pairing")
            pairings += 1

    triple_checks = fourier_checks = high_checks = double_high_checks = 0
    for indices in combinations_with_replacement(range(level), 3):
        i, j, k = indices
        product = multiply(multiply(polynomials[i], polynomials[j], field.zero),
                           polynomials[k], field.zero)
        actual = trace(product, modulus, level, field)
        r = level - 1 - k
        if i + j < level and max(i, j) <= r <= i + j:
            coefficient = (
                sine[i + j] * sine[r]
                / (sine[i] * sine[j] * sine[r - i] * sine[r - j] * sine[i + j - r])
            )
        else:
            coefficient = field.zero
        assert actual == coefficient, (level, indices, "multiplication")
        triple_checks += 1
        high_count = sum(2 * index >= level for index in indices)
        if high_count >= 2:
            assert actual == field.zero, (level, indices, "two high indices")
            double_high_checks += 1
        elif high_count == 1:
            high_checks += 1
        else:
            fourier = multiply(multiply(laurent[i], laurent[j], field.zero),
                               laurent[k], field.zero)
            degree = i + j + k

            def at(frequency):
                position = frequency + degree
                return fourier[position] if 0 <= position < len(fourier) else field.zero

            expected = level**2 * (at(level - 1) - at(level + 1))
            assert actual == expected, (level, indices, "Fourier trace")
            fourier_checks += 1

    return {
        "level": level,
        "pairings": pairings,
        "triple_product_coefficients": triple_checks,
        "low_triple_fourier_identities": fourier_checks,
        "single_high_triples": high_checks,
        "vanishing_multiple_high_triples": double_high_checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=9)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_level < 3:
        parser.error("require max-level >= 3")
    records = []
    for level in range(3, args.max_level + 1):
        records.append(check_level(level))
        print(f"Checked level {level}", flush=True)
    result = {
        "arithmetic": "exact rational cyclotomic fields",
        "reference": "polynomial division by 2 T_N(z/2)+2, including root multiplicities",
        "scope": "finite trace identities; the uniform tail gap is proved in the research note",
        "records": records,
        "totals": {key: sum(record[key] for record in records)
                   for key in records[0] if key != "level"},
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(f"Wrote {args.output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
