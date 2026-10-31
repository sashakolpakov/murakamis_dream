"""Exact one-level obstruction to a scalar orthogonal identification."""

import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ


def verify():
    field = QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3))
    N = 12
    d = N - 1
    M = N // 2 - 1
    theta = sp.pi / N
    assert 3 <= M
    s = [field.from_sympy(sp.simplify(2 * sp.sin(r * theta))) for r in range(N)]
    a = [field.from_sympy(sp.simplify(2 + 2 * sp.cos((2 * r + 1) * theta))) for r in range(N)]
    rows = [[field.one]]
    for r in range(1, N):
        row = [field.zero] * (r + 1)
        for j, value in enumerate(rows[-1]):
            row[j] += s[r] ** 2 * value
            row[j + 1] += s[r] ** 2 * value
        if r >= 2:
            for j, value in enumerate(rows[-2]):
                row[j + 1] += s[r] * s[r - 1] * a[r - 1] * value
        rows.append(row)
    tail = [field.one] * N
    for r in range(d - 1, -1, -1):
        tail[r] = tail[r + 1] * a[r + 1]
    slices = []
    for n in range(4):
        assert max(0, n - M) == 0 and min(M, n) == n
        row = [(-1) ** j * rows[d - n + j][j] * tail[d - n + j] for j in range(n + 1)]
        assert row[0] != field.zero
        slices.append([value / row[0] for value in row])
    expected = [
        [1],
        [1, -2],
        [1, -2 - sp.sqrt(3) - sp.sqrt(2) - sp.sqrt(6) / 2,
         (7 + sp.sqrt(2) + sp.sqrt(3) + sp.sqrt(6)) / 2],
        [1, -8 - 5 * sp.sqrt(2),
         15 + 10 * sp.sqrt(2) + 3 * sp.sqrt(3) + 2 * sp.sqrt(6),
         -14 - 8 * sp.sqrt(2)],
    ]
    for got, wanted in zip(slices, expected):
        assert got == [field.from_sympy(sp.sympify(value)) for value in wanted]
    remainder = [field.zero] + slices[2]
    expansion = {}
    for r in range(3, -1, -1):
        coefficient = remainder[r] / slices[r][r]
        expansion[r] = coefficient
        for j in range(r + 1):
            remainder[j] -= coefficient * slices[r][j]
    assert all(value == field.zero for value in remainder)
    target = (5341 - 5789 * sp.sqrt(2) + 1110 * sp.sqrt(3) + 665 * sp.sqrt(6)) / 13906
    assert expansion[0] == field.from_sympy(target)
    assert expansion[0] != field.zero
    return {
        "status": "PASS",
        "N": N,
        "original_cutoff_M": M,
        "field": "Q(sqrt(2),sqrt(3))",
        "exact_polynomial_coefficients": sum(map(len, slices)),
        "normalized_slices": [[str(sp.expand(field.to_sympy(v))) for v in row] for row in slices],
        "constant_basis_coefficient": str(sp.expand(target)),
        "constant_basis_coefficient_nonzero": True,
        "full_expansion_remainder_zero": True,
        "scope": "No positive scalar orthogonal identification of H0..H3; original convolution bound remains open.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("research_cap_demand_scalar_orthogonality_results.json"))
    args = parser.parse_args()
    result = verify()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "N": result["N"], "exact_coefficients": result["exact_polynomial_coefficients"]}))


if __name__ == "__main__":
    main()
