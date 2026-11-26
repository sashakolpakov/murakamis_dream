#!/usr/bin/env python3
"""Exact source checks for coherent deletion of highest conditional rows.

The all-level operator-norm estimate is analytic. No numerical norm
or finite-level asymptotic is used as its proof.
"""
import argparse
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-coherent-endpoint-deletion.json")
    args = parser.parse_args()
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda x: field.from_sympy(sp.sympify(x))
    checks = []

    def check(name, value):
        assert value == zero, (name, field.to_sympy(value))
        checks.append(name)

    @lru_cache(maxsize=None)
    def conjugate(value):
        return cv(sp.conjugate(field.to_sympy(value)))

    def product(values):
        result = one
        for value in values:
            result *= value
        return result

    def mul(A, B):
        n = len(A)
        return [[sum((A[i][k] * B[k][j] for k in range(n)), zero)
                 for j in range(n)] for i in range(n)]

    def transpose(A):
        return [list(row) for row in zip(*A)]

    def subtract(A, B):
        return [[a - b for a, b in zip(x, y)] for x, y in zip(A, B)]

    def assert_matrix(name, A, B):
        for i, row in enumerate(subtract(A, B)):
            for j, value in enumerate(row):
                check(f"{name} ({i},{j})", value)

    levels = [(2, sp.I), (3, (1 + sp.I * sp.sqrt(3)) / 2),
              (4, (1 + sp.I) / sp.sqrt(2)), (6, (sp.sqrt(3) + sp.I) / 2)]
    words = [(0, 1), (1, 0, 1), (0, 1, 0, 1)]
    for N, q_expression in levels:
        q, ii = cv(q_expression), cv(sp.I)
        r, Q, D = q ** -2, q ** 2, N - 1
        P = [product(one - r ** h for h in range(1, j + 1)) for j in range(N)]
        sine = [product((q ** h - q ** -h) / ii
                        for h in range(1, j + 1)) for j in range(N)]
        delta = [ii ** j * q ** (-j * (j + 1) // 2) for j in range(N)]
        S = [[q ** (j * ell) / (delta[j] * sine[ell] * sine[j - ell])
              if ell <= j else zero for ell in range(N)] for j in range(N)]
        ST = transpose(S)
        Gamma = [[Q ** (j * k) * P[j + k] / (P[j] ** 2 * P[k] ** 2)
                  if j + k < N else zero for k in range(N)] for j in range(N)]
        assert_matrix(f"N{N} original bilinear Gram", mul(S, ST), Gamma)
        u = [(-q ** -1) ** j for j in range(N)]
        for j in range(N):
            check(f"N{N} last-row phase j{j}", S[D][j] - u[j] / N)
            check(f"N{N} unit endpoint entry j{j}", u[j] * conjugate(u[j]) - one)
        check(f"N{N} exact endpoint norm squared",
              sum((v * conjugate(v) for v in u), zero) - N)
        for k in range(N // 2 + 1):
            for ell in range(D - k + 1):
                check(f"N{N} reflected high-row modulus k{k} ell{ell}",
                      S[D - k][ell] * conjugate(S[D - k][ell])
                      - sine[k + ell] ** 2 / (N * N * sine[ell] ** 2))

        # Literal original M/kappa. A_(3+eps)/kappa^(1+eps)
        # equals q^(D^2) times the reversed corresponding power.
        C = [product(one - Q ** h for h in range(1, j + 1)) for j in range(N)]
        M = [[(-1) ** j * q ** (j + ell * ell) * C[j] / (C[ell] * C[j - ell])
              if ell <= j else zero for ell in range(N)] for j in range(N)]
        M2 = mul(M, M)
        powers = [mul(M2, M), mul(M2, M2)]
        originals, blocks = {}, {}
        for eps in (0, 1):
            B = [[N ** eps * P[i + j] / (P[i] * P[j]) ** eps
                  if i + j < N else zero for j in range(N)] for i in range(N)]
            original = [[q ** (D * D) * powers[eps][D - i][j]
                         for j in range(N)] for i in range(N)]
            originals[eps] = original
            assert_matrix(f"N{N} original vertex scalar eps{eps}", mul(mul(ST, B), S), original)
            for k in range(N // 2 + 1):
                for b in range(k + 1):
                    check(f"N{N} boundary vertex modulus eps{eps} k{k} b{b}",
                          B[D - k][b] * conjugate(B[D - k][b])
                          - N * N * sine[k] ** (2 * eps)
                          / (sine[b] ** (2 * eps) * sine[k - b] ** 2))
            for L in range(N // 2 + 1):
                PB = [[value if i >= D - L else zero for value in row]
                      for i, row in enumerate(B)]
                endpoint = mul(mul(ST, PB), S)
                blocks[eps, L] = endpoint
                conditional = mul(Gamma, PB)
                assert_matrix(f"N{N} exact conditional deletion eps{eps} L{L}",
                              mul(S, endpoint), mul(conditional, S))
                for a in range(N):
                    for b in range(N):
                        if a > L or b > L:
                            check(f"N{N} both outer supports eps{eps} L{L} a{a} b{b}",
                                  conditional[a][b])
                if L == 0:
                    rank_one = [[u[i] if j == 0 else zero for j in range(N)] for i in range(N)]
                    assert_matrix(f"N{N} original endpoint rank one eps{eps}", endpoint, rank_one)

        # Noncommuting telescope, in the actual original coordinates.
        L = 1
        identity = [[one if i == j else zero for j in range(N)] for i in range(N)]
        for word in words:
            actual = identity
            retained = identity
            for eps in word:
                actual = mul(actual, originals[eps])
                retained = mul(retained, subtract(originals[eps], blocks[eps, L]))
            total = [[zero for _ in range(N)] for _ in range(N)]
            for v, eps in enumerate(word):
                term = identity
                for prior in word[:v]:
                    term = mul(term, subtract(originals[prior], blocks[prior, L]))
                term = mul(term, blocks[eps, L])
                for after in word[v + 1:]:
                    term = mul(term, originals[after])
                total = [[x + y for x, y in zip(a, b)] for a, b in zip(total, term)]
            assert_matrix(f"N{N} original word telescope {word}", subtract(actual, retained), total)

    x, y = sp.symbols("x y")
    combinatorial = []
    for k in range(9):
        expression = sum(sp.binomial(k, b) * x ** b * y ** (k - b)
                         for b in range(k + 1)) - (x + y) ** k
        assert sp.expand(expression) == 0
        combinatorial.append(f"exact binomial row sum k{k}")
    rational = [
        ("backward ratio bound", Fraction(1, 4)),
        ("geometric factor", 1 / (1 - Fraction(1, 4))),
        ("strict reserve below two", Fraction(2) - 1 / (1 - Fraction(1, 4))),
    ]
    assert rational[1][1] == Fraction(4, 3) and rational[2][1] > 0
    dependencies = [
        "notes/research_mixed_coherent_endpoint_deletion.md",
        "notes/research_mixed_wire_exact_contraction.md",
        "notes/research_mixed_complete_boundary_sum.md",
        "notes/research_mixed_conditional_leg_sum.md",
    ]
    record = {
        "status": "passed",
        "exact_source_identity_count": len(checks),
        "exact_source_identities": checks,
        "combinatorial_identity_count": len(combinatorial),
        "combinatorial_identities": combinatorial,
        "rational_comparisons": [{"name": name, "value": str(value)} for name, value in rational],
        "levels": [n for n, _ in levels],
        "arithmetic": "Exact Q(i,sqrt(2),sqrt(3)) and rational/combinatorial identities",
        "scope": (
            "Literal original vertex matrices, highest conditional blocks, both physical supports, "
            "rank-one endpoint normalization and noncommuting word telescopes. "
            "The analytic proof supplies the all-level operator norm; no observed-word gap is inferred."
        ),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {path: sha256((ROOT / path).read_bytes()).hexdigest()
                                for path in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in (
        "status", "exact_source_identity_count", "combinatorial_identity_count", "levels")}))


if __name__ == "__main__":
    main()
