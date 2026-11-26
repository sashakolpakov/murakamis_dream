#!/usr/bin/env python3
"""Exact original-source torus composition, including its wrapped Fourier term.

All assertions use algebraic-number arithmetic.  The note proves the identities
for every level; these finite checks guard scalars, support, and alias signs.
"""
import argparse
import json
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-mixed-conditional-torus-composition.json",
    )
    args = parser.parse_args()
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda value: field.from_sympy(sp.sympify(value))
    identities = []

    def check(label, value):
        assert value == zero, (label, field.to_sympy(value))
        identities.append(label)

    @lru_cache(maxsize=None)
    def conjugate(value):
        return cv(sp.conjugate(field.to_sympy(value)))

    def product(values):
        result = one
        for value in values:
            result *= value
        return result

    def poly_product(left, right):
        result = [zero] * (len(left) + len(right) - 1)
        for a, x in enumerate(left):
            for b, y in enumerate(right):
                result[a + b] += x * y
        return result

    def evaluate(coefficients, value):
        result = zero
        for coefficient in reversed(coefficients):
            result = result * value + coefficient
        return result

    def multiply(left, right):
        size = len(left)
        return [
            [
                sum((left[a][j] * right[j][b] for j in range(size)), zero)
                for b in range(size)
            ]
            for a in range(size)
        ]

    def word_trace(matrices, word):
        result = matrices[word[0]]
        for letter in word[1:]:
            result = multiply(result, matrices[letter])
        return sum((result[a][a] for a in range(len(result))), zero)

    def row_times(row, matrix):
        return [
            sum((row[a] * matrix[a][b] for a in range(len(row))), zero)
            for b in range(len(row))
        ]

    levels = [
        (2, sp.I),
        (3, (1 + sp.I * sp.sqrt(3)) / 2),
        (4, (1 + sp.I) / sp.sqrt(2)),
        (6, (sp.sqrt(3) + sp.I) / 2),
    ]
    words = [(3,), (4,), (3, 4), (4, 3, 4), (3, 3, 4), (3, 4, 3, 4)]
    for N, q_expression in levels:
        q = cv(q_expression)
        r, Q, D = q ** -2, q * q, N - 1
        P = [product(one - r ** h for h in range(1, j + 1)) for j in range(N)]
        polynomials = []
        for j in range(N):
            coefficients = [one]
            for h in range(1, j + 1):
                coefficients = poly_product(coefficients, [one, -r ** h])
            polynomials.append(coefficients)
        nodes = [q ** a for a in range(2 * N)]
        # Rows j, columns a: exact p_j at all 2N quadrature nodes.
        values = [[evaluate(p, x) for x in nodes] for p in polynomials]
        for j in range(N):
            tau = (-1) ** j * r ** (j * (j + 1) // 2)
            for a, x in enumerate(nodes):
                check(f"N{N} reciprocal polynomial j{j} node{a}",
                      x ** -j * values[j][a] - tau * conjugate(values[j][a]))
            for a in range(N):
                actual = evaluate(polynomials[j], r ** a)
                expected = P[a + j] / P[a] if a + j < N else zero
                check(f"N{N} original support j{j} a{a}", actual - expected)

        moments = [
            sum((r ** (a * k) / P[a] for a in range(N)), zero)
            for k in range(N)
        ]
        d = [moments[(-k) % N] / N for k in range(N)]
        for a in range(N):
            check(f"N{N} polynomial interpolation a{a}",
                  evaluate(d, r ** a) - one / P[a])
        check(f"N{N} highest coefficient", d[-1] - one / (N * N))
        # Finite geometric representation of the removable Cauchy formula.
        for k in range(N):
            coefficient = sum((r ** (-a * k) / P[a] for a in range(N)), zero) / N
            check(f"N{N} removable Cauchy coefficient k{k}", coefficient - d[k])
        for k in range(N + 1):
            left = (d[k] * (r ** k - one) if k < N else zero)
            if k:
                left -= d[k - 1] * r ** k
            right = -r ** k / (N * N) if k else zero
            check(f"N{N} forward forced transport k{k}", left - right)
            reverse = (d[k] * (r ** -k - one) if k < N else zero)
            if k:
                reverse += d[k - 1]
            check(f"N{N} reverse forced transport k{k}",
                  reverse - (one / (N * N) if k else zero))

        # All monomial bands occurring in the torus theorem, including m=1.
        for power in range(-N + 1, N):
            for eps in (0, 1):
                physical = sum(
                    (r ** (a * power) / P[a] ** eps for a in range(N)), zero
                ) / N
                if eps:
                    coefficient = sum(
                        (d[k] for k in (-power, N - power) if 0 <= k < N), zero
                    )
                else:
                    coefficient = one if power == 0 else zero
                check(f"N{N} root/torus monomial eps{eps} power{power}",
                      physical - coefficient)

        E = [[d[N + a - b] if b > a else zero for b in range(N)] for a in range(N)]
        for a in range(N):
            for b in range(N):
                toeplitz = d[a - b] if a >= b else zero
                check(f"N{N} wrapped matrix a{a} b{b}",
                      toeplitz + E[a][b] - moments[(b - a) % N] / N)
        Epower = E
        for _ in range(1, N - 1):
            Epower = multiply(Epower, E)
        check(f"N{N} nilpotent top coefficient",
              Epower[0][-1] - one / N ** (2 * (N - 1)))
        EN = multiply(Epower, E)
        for a in range(N):
            for b in range(N):
                check(f"N{N} nilpotent order a{a} b{b}", EN[a][b])
        # The rows 0..N-2 and columns 1..N-1 form an upper triangular minor.
        check(f"N{N} rank N-1 minor",
              product(E[a][a + 1] for a in range(N - 1))
              - one / N ** (2 * (N - 1)))

        kernels = {}
        transfers = {}
        torus_matrices = {}
        for eps in (0, 1):
            kernel = [
                [
                    sum(
                        (nodes[a] ** -j * values[j][a] * values[j][b]
                         / P[j] ** (2 + eps) for j in range(N)), zero
                    )
                    for b in range(2 * N)
                ]
                for a in range(2 * N)
            ]
            kernels[eps] = kernel
            transfer = [[zero for _ in range(N)] for _ in range(N)]
            for a in range(N):
                for b in range(N):
                    # The direct physical source, without using its polynomial form.
                    L = sum(
                        (r ** (-a * j) * P[j + a] * P[j + b] / P[j] ** (2 + eps)
                         for j in range(N - max(a, b))), zero
                    )
                    C = kernel[(-2 * a) % (2 * N)][(-2 * b) % (2 * N)]
                    check(f"N{N} original L gauge eps{eps} a{a} b{b}",
                          L - P[a] * P[b] * C)
                    transfer[a][b] = L / (P[a] ** 2 * P[b] ** eps)
                    check(f"N{N} transfer gauge eps{eps} a{a} b{b}",
                          transfer[a][b] - P[b] ** (1 - eps) * C / P[a])
            transfers[3 + eps] = transfer
            torus_matrices[3 + eps] = [
                [
                    kernel[a][b] * (
                        evaluate(d, nodes[b]) * (one + nodes[b] ** -N)
                    ) ** eps
                    for b in range(2 * N)
                ]
                for a in range(2 * N)
            ]
            for a in range(2 * N):
                for b in range(2 * N):
                    weighted_gram = sum(
                        (conjugate(values[j][a]) * values[j][b]
                         / (P[j] * conjugate(P[j]) * P[j] ** eps)
                         for j in range(N)), zero
                    )
                    check(f"N{N} circle Gram eps{eps} a{a} b{b}",
                          kernel[a][b] - weighted_gram)

        # Literal crossing matrix M/kappa, including its full confluent source.
        original_factorials = [
            product(one - Q ** h for h in range(1, a + 1)) for a in range(N)
        ]
        M = [
            [
                (-1) ** a * q ** (a + b * b) * original_factorials[a]
                / (original_factorials[b] * original_factorials[a - b])
                if b <= a else zero
                for b in range(N)
            ]
            for a in range(N)
        ]
        M2 = multiply(M, M)
        M3, M4 = multiply(M2, M), multiply(M2, M2)
        original = {
            3: [[q ** (D * D) * M3[D - a][b] for b in range(N)] for a in range(N)],
            4: [[q ** (D * D) * M4[D - a][b] / N for b in range(N)] for a in range(N)],
        }
        for word in words:
            literal = word_trace(original, word)
            check(f"N{N} original conditional word {word}",
                  literal - word_trace(transfers, word))
            # Every torus variable has band [-2N+1,2N-2], so 2N-root
            # averaging is its exact constant term, for every word length.
            check(f"N{N} original full torus word {word}",
                  literal - word_trace(torus_matrices, word) / 2 ** len(word))

        # Original ordinary boundary derivatives, without division by Newton
        # values. This retains the odd zero and its nonzero first normal.
        ii = cv(sp.I)
        signed_jets = [[one, zero, zero]]
        for ell in range(1, N):
            sine = (q ** ell - q ** -ell) / ii
            node_plus_two = q ** (2 * ell - 1) + q ** (-2 * ell + 1) + 2
            previous = signed_jets[-1]
            signed_jets.append([
                (node_plus_two * previous[a] + (a * previous[a - 1] if a else zero))
                / sine ** 2
                for a in range(3)
            ])
        H = [[zero] * N for _ in range(3)]
        basis = [one]
        for ell in range(N):
            for a in range(3):
                coefficient = (-q) ** -ell * signed_jets[ell][a] / P[ell]
                for degree, value in enumerate(basis):
                    H[a][degree] += coefficient * value
            basis = poly_product(basis, [one, -r ** ell])
        Hvalues = [
            [evaluate(H[a], x ** -1) for x in nodes]
            for a in range(3)
        ]
        U = {}
        for a in range(3):
            for j in range(N):
                original_boundary = (-q) ** -j / P[j] * sum(
                    (M[j][ell] * (-1) ** a * signed_jets[ell][a]
                     for ell in range(N)), zero
                )
                check(f"N{N} original boundary polynomial jet{a} j{j}",
                      original_boundary - (-1) ** a
                      * evaluate(H[a], r ** -j) / P[j])
            for eps in (0, 1):
                coefficients = [zero] * N
                for i in range(N):
                    weight = evaluate(H[a], r ** -i) / P[i] ** (1 + eps)
                    for degree, value in enumerate(polynomials[i]):
                        coefficients[degree] += weight * value
                U[eps, a] = coefficients
                for j in range(N):
                    left = sum(
                        ((-1) ** a * evaluate(H[a], r ** -i) / P[i]
                         * P[i + j] / (P[i] * P[j]) ** eps
                         for i in range(N - j)), zero
                    )
                    check(f"N{N} full first vertex jet{a} eps{eps} j{j}",
                          left - (-1) ** a * P[j] ** (1 - eps)
                          * evaluate(coefficients, r ** j))

        physical_kernels = {
            3 + eps: [
                [
                    kernels[eps][(-2 * a) % (2 * N)][(-2 * b) % (2 * N)]
                    / P[b] ** eps
                    for b in range(N)
                ]
                for a in range(N)
            ]
            for eps in (0, 1)
        }
        for word in words:
            original_product = original[word[0]]
            for letter in word[1:]:
                original_product = multiply(original_product, original[letter])
            eps_first = word[0] - 3
            for a in range(3):
                original_left = [(-1) ** a * signed_jets[j][a] for j in range(N)]
                original_row = row_times(original_left, original_product)
                physical_row = [
                    evaluate(U[eps_first, a], r ** j) / P[j] ** eps_first
                    for j in range(N)
                ]
                torus_row = [
                    evaluate(U[eps_first, a], x) * (
                        evaluate(d, x) * (one + x ** -N)
                    ) ** eps_first
                    for x in nodes
                ]
                for letter in word[1:]:
                    physical_row = row_times(physical_row, physical_kernels[letter])
                    torus_row = row_times(torus_row, torus_matrices[letter])
                for b in range(3):
                    literal = sum(
                        (original_row[j] * (-1) ** b * signed_jets[j][b]
                         for j in range(N)), zero
                    )
                    physical = (-1) ** (a + b) * sum(
                        (physical_row[j] * evaluate(H[b], r ** -j)
                         for j in range(N)), zero
                    )
                    torus = cv((-1) ** (a + b)) / cv(2 ** len(word)) * sum(
                        (torus_row[j] * Hvalues[b][j] for j in range(2 * N)), zero
                    )
                    check(f"N{N} original open root sum word{word} jets{a},{b}",
                          literal - physical)
                    check(f"N{N} original open torus word{word} jets{a},{b}",
                          literal - torus)

    dependencies = [
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_mixed_conditional_leg_sum.md",
        "notes/research_mixed_wire_exact_contraction.md",
        "notes/research_mixed_four_conditional_complex_neighbors.md",
        "notes/research_mixed_fourier_weight_continuation.md",
        "notes/research_mixed_three_four_operator_obstruction.md",
        "notes/research_complete_boundary_complex_index.md",
        "notes/research_mixed_complete_boundary_sum.md",
    ]
    result = {
        "status": "passed",
        "exact_identity_count": len(identities),
        "exact_identities": identities,
        "levels": [N for N, _ in levels],
        "words": words,
        "arithmetic": "Exact Q(i,sqrt(2),sqrt(3)); polynomial and original matrix identities",
        "scope": (
            "Original cyclic source, diagonal gauge, all outer aliases, forced "
            "interpolating weight, wrapped operator, and full constant-term scalars. "
            "Open original words include both complete ordinary boundary jets "
            "of orders 0,1,2. No asymptotic estimate or free-color packet."
        ),
        "reproduction_command": "python3 experiments/check_mixed_conditional_torus_composition.py",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in dependencies
        },
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "exact_identity_count", "levels")}))


if __name__ == "__main__":
    main()
