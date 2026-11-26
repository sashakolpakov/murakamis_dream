#!/usr/bin/env python3
"""Exact original-source checks for arbitrary-twist conditional endpoint blocks.

The twist-uniform norm inequality is proved analytically in the cited note.
These checks retain negative powers, the original carrier, and both physical
support constraints; they do not infer an all-level bound from finite norms.
"""
import argparse
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-arbitrary-twist-conditional-endpoints.json")
    args = parser.parse_args()
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda value: field.from_sympy(sp.sympify(value))
    checks = []

    @lru_cache(maxsize=None)
    def conjugate(value):
        return cv(sp.conjugate(field.to_sympy(value)))

    def identity(n):
        return [[one if j == k else zero for k in range(n)] for j in range(n)]

    def multiply(a, b):
        return [[sum((x * y for x, y in zip(row, col)), zero)
                 for col in zip(*b)] for row in a]

    def transpose(a):
        return [list(row) for row in zip(*a)]

    def inverse_lower(a):
        n = len(a)
        result = identity(n)
        for k in range(n):
            for j in range(n):
                result[j][k] = ((one if j == k else zero) -
                                sum((a[j][ell] * result[ell][k]
                                     for ell in range(j)), zero)) / a[j][j]
        return result

    def check(name, value):
        assert value == zero, (name, field.to_sympy(value))
        checks.append(name)

    def matrix_check(name, a, b):
        for j, (arow, brow) in enumerate(zip(a, b)):
            for k, (av, bv) in enumerate(zip(arow, brow)):
                check(f"{name} ({j},{k})", av - bv)

    levels = [(2, sp.I), (3, (1 + sp.I * sp.sqrt(3)) / 2),
              (4, (1 + sp.I) / sp.sqrt(2)), (6, (sp.sqrt(3) + sp.I) / 2)]
    twists = list(range(-3, 9))
    for n_level, q_expression in levels:
        q, ii = cv(q_expression), cv(sp.I)
        r, degree = q ** -2, n_level - 1
        pochhammer, sine = [one], [one]
        for j in range(1, n_level):
            pochhammer.append(pochhammer[-1] * (one - r ** j))
            sine.append(sine[-1] * (q ** j - q ** -j) / ii)
        basis = [[q ** (j * ell) /
                  (ii ** j * q ** (-j * (j + 1) // 2) *
                   sine[ell] * sine[j - ell])
                  if ell <= j else zero for ell in range(n_level)]
                 for j in range(n_level)]
        basis_inverse = inverse_lower(basis)
        basis_transpose = transpose(basis)
        matrix_check(f"N{n_level} original basis inverse",
                     multiply(basis, basis_inverse), identity(n_level))

        # This is the literal original M/kappa, in the sine convention.
        # Since |kappa|=1, M^{-1}=bar(M) is equivalent to this exact check.
        crossing = [[(-1) ** j * q ** (j * (ell + 1)) *
                     sine[j] / (sine[ell] * sine[j - ell])
                     if ell <= j else zero for ell in range(n_level)]
                    for j in range(n_level)]
        crossing_inverse = [[conjugate(value) for value in row]
                            for row in crossing]
        matrix_check(f"N{n_level} original negative inverse",
                     multiply(crossing, crossing_inverse), identity(n_level))
        physical_color = q + q ** -1
        newton_numerator = one
        physical_vector = []
        for j in range(n_level):
            if j:
                node = q ** (2 * j - 1) + q ** (-2 * j + 1)
                newton_numerator *= node - physical_color
            physical_vector.append(newton_numerator / sine[j] ** 2)
            check(f"N{n_level} actual opposite-color evaluation {j}",
                  physical_vector[-1] - (one if j == 0 else zero))
            check(f"N{n_level} exact inverse-crossing endpoint {j}",
                  sum((crossing_inverse[j][k] * physical_vector[k]
                       for k in range(j + 1)), zero) - (-q ** -1) ** j)
        casimir = [[q ** (2 * j + 1) + q ** (-2 * j - 1)
                    if j == ell else
                    -(q ** j - q ** -j) ** 2 / ii ** 2
                    if j == ell + 1 else zero
                    for ell in range(n_level)] for j in range(n_level)]
        matrix_check(f"N{n_level} original Casimir commutation",
                     multiply(casimir, crossing), multiply(crossing, casimir))

        powers = {0: identity(n_level)}
        for power in range(1, 9):
            powers[power] = multiply(powers[power - 1], crossing)
            powers[-power] = multiply(powers[-power + 1], crossing_inverse)
        b_three = [[pochhammer[j + k] if j + k < n_level else zero
                    for k in range(n_level)] for j in range(n_level)]
        gram = multiply(basis, basis_transpose)
        for twist in twists:
            relative_power = twist - 3
            transported = multiply(
                b_three, multiply(basis, multiply(powers[relative_power], basis_inverse)))
            # A_n/kappa^(n-2) = kappa^2 J (M/kappa)^n.
            # kappa^2=q^(D^2), retaining the original carrier for ALL n.
            original = [[q ** (degree * degree) * powers[twist][degree - j][k]
                         for k in range(n_level)] for j in range(n_level)]
            matrix_check(f"N{n_level} twist{twist} original carrier",
                         multiply(basis_transpose, multiply(transported, basis)),
                         original)
            for j in range(n_level):
                check(f"N{n_level} twist{twist} unit diagonal {j}",
                      powers[relative_power][j][j] *
                      conjugate(powers[relative_power][j][j]) - one)
                for k in range(n_level):
                    if j + k >= n_level:
                        check(f"N{n_level} twist{twist} antitriangle {j},{k}",
                              transported[j][k])
            for cutoff in range(n_level // 2 + 1):
                projected = [[value if j >= degree - cutoff else zero
                              for value in row] for j, row in enumerate(transported)]
                projected_three = [[value if j >= degree - cutoff else zero
                                    for value in row] for j, row in enumerate(b_three)]
                endpoint = multiply(basis_transpose, multiply(projected, basis))
                expected = multiply(
                    multiply(basis_transpose, multiply(projected_three, basis)),
                    powers[relative_power])
                matrix_check(f"N{n_level} twist{twist} cutoff{cutoff} transport",
                             endpoint, expected)
                conditional = multiply(gram, projected)
                for j in range(n_level):
                    for k in range(n_level):
                        if max(j, k) > cutoff:
                            check(f"N{n_level} twist{twist} cutoff{cutoff} outer {j},{k}",
                                  conditional[j][k])
                if cutoff == 0:
                    rank_one = [[(-q ** -1) ** j if k == 0 else zero
                                 for k in range(n_level)] for j in range(n_level)]
                    matrix_check(f"N{n_level} twist{twist} exact rank one",
                                 endpoint, rank_one)
                    observed = multiply(original, endpoint)
                    trace = sum((observed[j][j] for j in range(n_level)), zero)
                    inverse_boundary = multiply(original, crossing_inverse)
                    right = sum((physical_vector[j] * inverse_boundary[j][k] *
                                 physical_vector[k] for j in range(n_level)
                                 for k in range(n_level)), zero)
                    check(f"N{n_level} twist{twist} actual opposite-color trace",
                          trace - right)
        print(f"Exact original level {n_level}: passed", flush=True)

    # Divide the binomial commutator identity by binom(j,ell).
    # The two standard adjacent-binomial ratios give this polynomial identity.
    j, ell, z = sp.symbols("j ell z")
    symbolic = []
    induction = (j * (j - ell) + (ell + 1) * (j - ell)
                 - (j - ell) * (j + ell + 1))
    assert sp.expand(induction) == 0
    symbolic.append("binomial commutator induction after exact adjacent ratios")
    for degree in range(9):
        for lower in range(degree + 1):
            left = (degree ** 2 * sp.binomial(degree - 1, lower)
                    if degree else 0)
            left += (lower + 1) ** 2 * sp.binomial(degree, lower + 1)
            right = ((degree - lower) * (degree + lower + 1) *
                     sp.binomial(degree, lower))
            assert left == right
    symbolic.append("binomial induction endpoint conventions through degree eight")
    for degree in range(9):
        assert sp.expand(sum(sp.binomial(degree, lower) * (1 + z) ** lower
                             for lower in range(degree + 1)) - (2 + z) ** degree) == 0
    symbolic.append("transported row binomial sum")

    dependencies = [
        "notes/research_arbitrary_twist_conditional_endpoints.md",
        "notes/research_mixed_coherent_endpoint_deletion.md",
        "notes/research_mixed_wire_exact_contraction.md",
        "notes/research_positive_three_crossing_cycle.md",
        "notes/research_newton_interpolation_finite_fourier_band.md",
    ]
    record = {
        "status": "passed",
        "exact_source_identity_count": len(checks),
        "exact_source_identities": checks,
        "symbolic_identity_count": len(symbolic),
        "symbolic_identities": symbolic,
        "levels": [level for level, _ in levels],
        "twists": twists,
        "arithmetic": "Exact Q(i,sqrt(2),sqrt(3)); symbolic binomial identities",
        "normalization": (
            "Original M/kappa; A_n/kappa^(n-2)=q^((N-1)^2) J (M/kappa)^n. "
            "Negative powers use the exactly verified conjugate inverse."
        ),
        "scope": (
            "Original arbitrary integer-twist endpoint transport, anti-triangle and "
            "both physical supports, rank-one carrier, Casimir commutation and "
            "binomial induction. Uniform operator-norm inequalities are analytic "
            "and are not inferred from sampled matrix powers."
        ),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {path: sha256((ROOT / path).read_bytes()).hexdigest()
                                for path in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in (
        "status", "exact_source_identity_count", "symbolic_identity_count", "levels", "twists")}))


if __name__ == "__main__":
    main()
