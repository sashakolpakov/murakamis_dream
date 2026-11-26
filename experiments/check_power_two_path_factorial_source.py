#!/usr/bin/env python3
"""Compare the original Newton crossing matrices with the path factorial sum.

The matrix calculation keeps the complete quotient algebra, not just
values at its distinct roots. Results are numerical diagnostics.
"""

import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp


def crossing_matrix(n, signs=1):
    q = mp.exp(mp.pi * 1j / n)
    d = n - 1
    kappa = mp.exp(mp.pi * 1j * d * d / (2 * n))
    factorials = [mp.mpf(1)]
    for j in range(1, n):
        factorials.append(factorials[-1] * 2 * mp.sin(mp.pi * j / n))
    matrix = mp.matrix(n)
    for k in range(n):
        for j in range(k + 1):
            matrix[k, j] = (
                kappa * (-1)**k * q**(k * (j + 1))
                * factorials[k] / (factorials[j] * factorials[k - j]))
    if signs < 0:
        matrix = matrix.apply(mp.conj)
    return matrix, factorials


def original_path(n, edges):
    matrix, _ = crossing_matrix(n)
    squared = matrix * matrix
    vector = mp.matrix([1] + [0] * (n - 1))
    vector = squared * vector
    for _ in range(edges):
        vector = squared * mp.matrix(list(reversed(list(vector))))
    return vector[n - 1]


def factorial_path(n, edges):
    _, S = crossing_matrix(n)
    degrees = [int(j > 0) + int(j + 1 < edges) for j in range(edges)]
    vertex = [
        [mp.exp(1j * mp.pi * (mp.mpf(i * i) / n + (1 - mp.mpf(1) / n) * i))
         / S[i]**(degrees[j] + 2) for i in range(n)]
        for j in range(edges)
    ]
    edge = [
        [S[i + j] * mp.exp(-1j * mp.pi * i * j / n)
         if i + j < n else mp.mpc(0) for j in range(n)]
        for i in range(n)
    ]
    terms = []
    for indices in itertools.product(range(n), repeat=edges):
        if any(indices[j] + indices[j + 1] >= n for j in range(edges - 1)):
            continue
        term = mp.fprod(vertex[j][indices[j]] for j in range(edges))
        term *= mp.fprod(edge[indices[j]][indices[j + 1]]
                        for j in range(edges - 1))
        terms.append(term)
    return n**(edges + 1) * mp.fsum(terms)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-power-two-path-factorial-source.json")
    args = parser.parse_args()
    mp.mp.dps = args.dps
    tolerance = mp.mpf(10)**(15 - args.dps)
    cases = []
    for n in range(2, 10):
        for edges in range(1, 5):
            original = original_path(n, edges)
            factorial = factorial_path(n, edges)
            error = abs(original - factorial) / (1 + abs(original))
            assert error < tolerance, (n, edges, error)
            cases.append({
                "N": n, "path_edges": edges,
                "scaled_error": mp.nstr(error, 30),
            })
    result = {
        "status": "passed",
        "precision_decimal_digits": args.dps,
        "scope": (
            "Original full Newton multiplication matrices versus the "
            "zero-extended factorial path source, including its phases "
            "and N^(edges+1) factor. Numerical diagnostics, not a proof "
            "of any asymptotic or of a branching-source identity."),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Saved {len(cases)} original-matrix comparisons to {args.output}.")


if __name__ == "__main__":
    main()
