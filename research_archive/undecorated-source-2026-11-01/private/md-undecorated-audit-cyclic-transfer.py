#!/usr/bin/env python3
"""Exact combinatorial test of the bipyramid two-pending-degree transfer.

Uses generic signed homogeneous polynomial factors, not quantum samples.
It tests the finite coefficient/trace identity only, not an invariant
identification, spectral bound, or hyperbolic-volume asymptotic.
"""
from collections import defaultdict
from pathlib import Path
import hashlib
import json


def local_terms(j, d):
    result = {}
    for a in range(d + 1):
        for b in range(d + 1 - a):
            for c in range(d + 1 - a - b):
                p = d - a - b - c
                if j % 2 and p:
                    continue
                coefficient = (-1) ** (j + a + c) * (
                    1 + (j + 1) * (a + 1) + 2 * b + 3 * c + 5 * p
                )
                result[a, b, c, p] = coefficient
    return result


def direct(m, d, factors):
    # Coordinates are S,z_0,...,z_(m-1). The protected z_0 target is zero.
    target = (d, 0) + (d,) * (m - 1)
    product = {(0,) * (m + 1): 1}
    for j, terms in enumerate(factors):
        new = defaultdict(int)
        for powers, value in product.items():
            for (a, b, c, p), coefficient in terms.items():
                exponents = list(powers)
                exponents[0] += p
                exponents[1 + (j - 1) % m] += a
                exponents[1 + j] += b
                exponents[1 + (j + 1) % m] += c
                if all(x <= y for x, y in zip(exponents, target)):
                    new[tuple(exponents)] += value * coefficient
        product = dict(new)
    return product.get(target, 0)


def transfer(m, d, factors):
    states = [(u, v) for u in range(d + 1) for v in range(d + 1)]
    number = len(states)
    product = [[int(i == j) for j in range(number)] for i in range(number)]
    for j, terms in enumerate(factors):
        target_previous = 0 if (j - 1) % m == 0 else d
        matrix = [[0] * number for _ in states]
        for i, (u, v) in enumerate(states):
            for k, (up, vp) in enumerate(states):
                a, b, c = target_previous - u, up - v, vp
                p = d - a - b - c
                matrix[i][k] = terms.get((a, b, c, p), 0)
                if matrix[i][k]:
                    if j == 1:
                        assert u == 0 and up + vp == d + u + v
                    else:
                        assert up + vp == u + v - p
        product = [
            [sum(product[i][k] * matrix[k][j] for k in range(number))
             for j in range(number)]
            for i in range(number)
        ]
    return sum(product[i][i] for i in range(number))


def main():
    cases = []
    for m, d in [(6, 1), (6, 2), (6, 3), (8, 1), (8, 2), (10, 1)]:
        factors = [local_terms(j, d) for j in range(m)]
        left = direct(m, d, factors)
        right = transfer(m, d, factors)
        assert left == right, (m, d, left, right)
        cases.append({"m": m, "degree": d, "coefficient": str(left),
                      "matrix_size": (d + 1) ** 2})
    result = {
        "status": "passed",
        "arithmetic": "exact signed integers",
        "scope": "generic homogeneous coefficient versus cyclic transfer identity",
        "not_checked": ["physical coupon dictionary", "quantum norms",
                        "circle packing", "asymptotic volume"],
        "cases": cases,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_name("md-undecorated-cyclic-transfer-results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "passed", "cases": len(cases), "output": str(output)}))


if __name__ == "__main__":
    main()
