#!/usr/bin/env python3
"""Exact algebra for the local retained-vertex composition.

This checks rational functions over Q(i,sqrt(3)), and determinant
identities modulo r^2-5r+1. It does not test contour asymptotics or infer
Gaussian branch choices from finite numerical values.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []

    def zero(name, expression):
        if isinstance(expression, sp.MatrixBase):
            reduced = expression.applyfunc(sp.simplify)
            assert reduced == sp.zeros(*reduced.shape), (name, reduced)
        else:
            reduced = sp.simplify(expression)
            assert reduced == 0, (name, reduced)
        checks.append(name)

    ii, rt = sp.I, sp.sqrt(3)
    X = (1 + ii * rt) / 4
    Y = sp.conjugate(X)
    es = (-1 + ii * rt) / 2
    index_q = (-1 - ii * rt) / 2
    index_q_sum = sp.simplify(index_q**2)
    zero("index stationary ratio", X * (1 - index_q_sum) / (1 - Y) - 1)
    zero("exponentiated wire critical equation", -es * (1 - Y) / (1 - X) - 1)
    hs = sp.Matrix([
        [2 * ii * (index_q_sum / (1 - index_q_sum) - Y / (1 - Y)),
         2 * ii * index_q_sum / (1 - index_q_sum)],
        [2 * ii * index_q_sum / (1 - index_q_sum),
         2 * ii * (index_q_sum / (1 - index_q_sum) - Y / (1 - Y))],
    ])
    mixed = 2 * ii / (1 - Y) * sp.eye(2)
    external = 2 * ii * (X / (1 - X) - Y / (1 - Y)) * sp.eye(2)
    zero("index Hessian divided by pi", hs + sp.Matrix([[rt + ii, 1 / rt + ii],
                                                        [1 / rt + ii, rt + ii]]))
    zero("mixed derivative block divided by pi", mixed - 2 * (1 / rt + ii) * sp.eye(2))
    zero("external derivative block divided by pi", external + 4 / rt * sp.eye(2))
    wire = sp.simplify(external - mixed.T * hs.inv() * mixed)
    core = sp.Matrix([[5, -2], [-2, 5]])
    k_over_pi = sp.Rational(4, 21) * (2 * rt - 3 * ii)
    a0_squared = 4 / (rt * (2 + ii * rt))
    zero("wire Schur complement", wire + k_over_pi * core)
    zero("pi a0 squared equals k0", a0_squared - k_over_pi)
    zero("real accretivity constant", sp.re(k_over_pi) - 8 * rt / 21)
    zero("two-incidence eigenvalues", core.charpoly().as_expr() -
         (sp.Symbol("lambda") - 3) * (sp.Symbol("lambda") - 7))

    r = sp.Symbol("r")
    modulus = sp.Poly(r**2 - 5 * r + 1, r, domain=sp.QQ)
    remainder_checks = []

    def remainder_zero(name, expression):
        numerator, denominator = sp.fraction(sp.together(expression))
        num = sp.Poly(numerator, r, domain=sp.QQ)
        den = sp.Poly(denominator, r, domain=sp.QQ)
        rem = num.rem(modulus)
        gcd = sp.gcd(den, modulus)
        assert rem.is_zero and gcd.degree() == 0, (name, rem, gcd)
        remainder_checks.append({"name": name, "remainder": "0",
                                 "denominator_gcd_degree": int(gcd.degree())})

    determinant_values = []
    previous, current = sp.Integer(0), sp.Integer(1)  # D_-1, D_0
    for m in range(1, 13):
        size = m - 1
        B = sp.zeros(size)
        for j in range(size):
            B[j, j] = 5
            if j + 1 < size:
                B[j, j + 1] = B[j + 1, j] = -1
        det_open = B.det()
        zero(f"open determinant recurrence m={m}", det_open - current)
        remainder_zero(f"open closed form m={m}",
                       current - (r**(-m) - r**m) / (r**-1 - r))

        # This automatically retains the loop at m=1 and the two
        # parallel incidences at m=2.
        P = sp.zeros(m)
        for j in range(m):
            P[j, (j + 1) % m] = 1
        C = 10 * sp.eye(m) - 2 * (P + P.T)
        cycle_half = 5 * sp.eye(m) - P - P.T
        zero(f"cycle nonnegative Laplacian m={m}",
             C - 6 * sp.eye(m) - 2 * (sp.eye(m) - P) * (sp.eye(m) - P).T)
        det_cycle = cycle_half.det()
        assert det_cycle > 0 and det_open > 0
        remainder_zero(f"cycle determinant product m={m}",
                       det_cycle - r**(-m) * (1 - r**m)**2)

        # The endpoint Schur complement is computed independently from
        # the sum of m original two-end blocks.
        full = sp.zeros(m + 1)
        for j in range(m):
            full[j, j] += 5
            full[j + 1, j + 1] += 5
            full[j, j + 1] -= 2
            full[j + 1, j] -= 2
        boundary = [0, m]
        endpoints = full.extract(boundary, boundary)
        if size:
            inside = list(range(1, m))
            coupling = full.extract(boundary, inside)
            endpoints -= coupling * full.extract(inside, inside).inv() * coupling.T
        claimed = sp.Matrix([[5 - 2 * previous / current, -2 / current],
                             [-2 / current, 5 - 2 * previous / current]])
        zero(f"effective endpoint Hessian m={m}", endpoints - claimed)
        determinant_values.append({"m": m, "open_D_m_minus_1": int(det_open),
                                   "cycle_determinant": int(det_cycle)})
        previous, current = current, 5 * current - previous

    zero("one-vertex loop determinant", determinant_values[0]["cycle_determinant"] - 3)
    zero("two-vertex parallel determinant", determinant_values[1]["cycle_determinant"] - 21)
    m = sp.Symbol("m", integer=True, positive=True)
    zero("cyclic N exponent", m - m / 2 - m / 2)
    zero("open N exponent", m - 1 - m / 2 - (m - 1) / 2 + sp.Rational(1, 2))

    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__).resolve(),
        root / "notes/research_three_vertex_local_composition.md",
        root / "notes/research_traced_three_vertex_endpoint.md",
        root / "notes/research_root_pochhammer_interpolation.md",
        root / "notes/research_positive_three_crossing_cycle.md",
        root / "notes/research_one_crossing_gaussian_window.md",
    ]
    result = {
        "status": "passed",
        "scope": (
            "Exact derivative, Schur-complement, scalar and determinant algebra. "
            "The continued logarithms, Gaussian square-root branch, local contour "
            "bounds, and global spectral theorem are written proof inputs; no "
            "numerical quantum asymptotic is inferred."
        ),
        "exact_identity_count": len(checks),
        "exact_identities": checks,
        "quadratic_remainder_count": len(remainder_checks),
        "quadratic_remainders": remainder_checks,
        "determinant_values": determinant_values,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in paths},
    }
    output = args.output or root / "repro/results/research-three-vertex-local-composition.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Passed {len(checks)} exact identities and {len(remainder_checks)} exact quadratic remainders.\n{output}")


if __name__ == "__main__":
    main()
