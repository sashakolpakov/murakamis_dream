#!/usr/bin/env python3
"""Exact algebra and rational budgets for internal-index deletion.

This replays the noncommutative telescope and its two adjacent small
factors. It does not infer asymptotic matrix estimates from finite data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import factorial
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    identities, margins = [], []

    def zero(name, expression):
        if isinstance(expression, sp.MatrixBase):
            reduced = expression.applyfunc(sp.simplify)
            assert reduced == sp.zeros(*reduced.shape), (name, reduced)
        else:
            reduced = sp.expand(expression)
            assert reduced == 0, (name, reduced)
        identities.append(name)

    def positive(name, expression):
        assert expression.is_Rational and expression > 0, (name, expression)
        margins.append({"name": name, "positive_margin": str(expression)})

    # Arbitrary noncommuting factors: no symmetry or positivity is used.
    b, p = sp.symbols("b p", commutative=False)
    for m in range(2, 11):
        left = b**m-b*(p*b)**(m-1)
        right = sum(b*(p*b)**(j-1)*(1-p)*b**(m-j) for j in range(1, m))
        zero(f"noncommutative telescope m={m}", left-right)

    B = sp.Matrix([[2, 1, -2], [3, -1, 4], [1, 2, 3]])
    P = sp.diag(0, 1, 0)
    Q = sp.eye(3)-P
    M = sp.Matrix([[1, 0, 0], [1, 2, 0], [2, -1, 3]])
    inverse = M.inv()
    kappa = sp.I
    A = (kappa*inverse*B*M).applyfunc(sp.simplify)
    Pi = inverse*P*M
    zero("endpoint projector idempotence", Q**2-Q)
    zero("literal internal projector idempotence", Pi**2-Pi)
    assert Pi != Pi.conjugate().T  # The replay must not assume orthogonality.
    for m in range(2, 8):
        literal = A
        for _ in range(m-1):
            literal = literal*Pi*A
        zero(f"literal similarity-source normalization m={m}",
             literal-kappa**m*inverse*B*(P*B)**(m-1)*M)
        for j in range(1, m):
            original = B*(P*B)**(j-1)*Q*B**(m-j)
            if j == 1:
                factored = (B*Q)*(Q*B)*B**(m-2)
            else:
                factored = B*(P*B)**(j-2)*P*(B*Q)*(Q*B)*B**(m-j-1)
            zero(f"two adjacent small factors m={m}, j={j}", original-factored)

    r = sp.Rational
    sine_margin = r(25, 8)*(1-r(22, 7)**2/(6*50**2))-3
    zero("displayed sine lower-bound margin", sine_margin-r(7229, 58800))
    positive("sin(pi x)>=3x on endpoint range", sine_margin)
    exponential_margin = sum(r(3)**j/factorial(j) for j in range(6))-r(50, 3)
    zero("displayed exponential-series margin", exponential_margin-r(26, 15))
    positive("exp(3)>50/3", exponential_margin)
    zero("endpoint entropy budget", (1+3)*r(1, 50)-r(2, 25))
    c, m = sp.symbols("c m")
    zero("operator error exponent", 2*(m-2)*c+2*(c+r(2, 25))-((2*m-2)*c+r(4, 25)))
    zero("source error exponent", (2*m-2)*c+r(4, 25)+c-((2*m-1)*c+r(4, 25)))
    zero("exact geometric margin", r(3, 25)+r(1, 15)-r(4, 25)-r(2, 75))
    positive("geometric gap", r(2, 75))
    positive("corner exponent below internal-column budget using c>8/25",
             r(8, 25)+r(2, 25)-r(3, 25))

    root = Path(__file__).resolve().parents[1]
    dependencies = [Path(__file__).resolve(),
                    root/"notes/research_homogeneous_chain_internal_projection.md",
                    root/"notes/research_traced_three_vertex_endpoint.md",
                    root/"notes/research_positive_three_crossing_cycle.md"]
    record = {
        "status": "passed",
        "scope": "Exact noncommutative telescope, source similarity, two-small-factor decomposition and rational scalar budgets. Analytic original-source norm bounds and the geometric lower action are written proof inputs.",
        "exact_identity_count": len(identities), "exact_identities": identities,
        "rational_comparison_count": len(margins), "rational_comparisons": margins,
        "sha256": {str(f.relative_to(root)): hashlib.sha256(f.read_bytes()).hexdigest()
                   for f in dependencies},
    }
    output = args.output or root/"repro/results/research-homogeneous-chain-internal-projection.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(identities)} exact identities and {len(margins)} rational comparisons.\n{output}")


if __name__ == "__main__":
    main()
