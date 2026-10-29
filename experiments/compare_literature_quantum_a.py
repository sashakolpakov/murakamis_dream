#!/usr/bin/env python3
"""Exact generic-variable checks against Andersen--Malusa arXiv v3.

The published/preprint operators are inputs to be audited. This script does
not assume that they annihilate the stated integral or have minimal degree.
Normal order is sum_j a_j(Q) E^j, with E Q = q Q E.
"""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    q, Q = sp.symbols("q Q")
    F = Q**4 - Q**3 - 2 * Q**2 - Q + 1
    R = q**4 * Q**4 - q**3 * Q**3 - q * (q**2 + 1) * Q**2 - q * Q + 1

    # Custom left-ordered classical factor, multiplied on the left by Q^2.
    custom = [Q**2, -F, Q**2]

    # The explicit candidate q P'_q obtained from equation (13) by E_2=1,
    # E_1=q^(-1)E, as in the proof of Theorem 19 of arXiv:1711.11522v3.
    candidate = [
        q**2 * Q**2 * (q**3 * Q**2 - 1),
        -(q**2 * Q**2 - 1) * R,
        q**2 * Q**2 * (q * Q**2 - 1),
    ]
    for a, b in zip(custom, candidate):
        assert sp.expand(b.subs(q, 1) - (Q**2 - 1) * a) == 0

    def invariant(coefficients):
        a0, a1, a2 = coefficients
        return sp.factor(a0.subs(Q, q * Q) * a2 / (a1.subs(Q, q * Q) * a1))

    custom_I = invariant(custom)
    candidate_I = invariant(candidate)
    assert sp.cancel(custom_I - candidate_I) != 0
    assert sp.cancel(custom_I.subs(q, 1) - candidate_I.subs(q, 1)) == 0

    # Endpoint data for the rational matrix-gauge obstruction proved in the
    # companion note. A determinant discrepancy alone would not suffice:
    # the literature determinant is itself a q-coboundary.
    custom_trace = F / Q**2
    literature_trace = -candidate[1] / candidate[2]
    literature_det = candidate[0] / candidate[2]
    determinant_factor = q * Q**2 - 1
    assert sp.cancel(
        literature_det - determinant_factor.subs(Q, q * Q) / determinant_factor
    ) == 0
    assert sp.limit(literature_trace / Q**2, Q, sp.oo) == q**3
    assert sp.limit(literature_trace * Q**2, Q, 0) == q**(-2)
    assert sp.limit(literature_det, Q, sp.oo) == q**2
    assert sp.limit(literature_det, Q, 0) == 1
    assert sp.limit(custom_trace / Q**2, Q, sp.oo) == 1
    assert sp.limit(custom_trace * Q**2, Q, 0) == 1
    A, B, c = sp.symbols("A B c")
    final_gauge_residual = sp.Poly(
        sp.expand((A + B * q * Q) * (A + B * Q) - c * determinant_factor), Q
    )
    assert sp.factor(final_gauge_residual.coeff_monomial(Q)) == A * B * (q + 1)
    assert final_gauge_residual.coeff_monomial(1) == A**2 + c
    assert sp.expand(final_gauge_residual.coeff_monomial(Q**2) - q * (B**2 - c)) == 0

    # Scalar equation multipliers and scalar state gauges cancel from I.
    a0q, a1q, a2, a1 = sp.symbols("a0q a1q a2 a1", nonzero=True)
    r0, r1, g0, g1, g2 = sp.symbols("r0 r1 g0 g1 g2", nonzero=True)
    transformed = (r1 * a0q) * (r0 * a2 * g2 / g0) / (
        (r1 * a1q * g2 / g1) * (r0 * a1 * g1 / g0)
    )
    assert sp.cancel(transformed - a0q * a2 / (a1q * a1)) == 0

    # Right multiplication by Q-1 must be done before ideal specialization.
    candidate_times_right_factor = [
        sp.expand(coefficient * (q**j * Q - 1))
        for j, coefficient in enumerate(candidate)
    ]

    # Equation (5) transcribed literally from the v3 TeX source (lines 593-595).
    printed_eq5 = [
        q**2 * Q**2 * (Q - 1) * (q**3 * Q**2 - 1),
        -(q * Q - 1) * (q * Q + 1) * R,
        q**2 * Q**2 * (q**2 * Q - 1) * (q * Q**2 - 1),
    ]
    discrepancy = [
        sp.factor(left - right)
        for left, right in zip(candidate_times_right_factor, printed_eq5)
    ]
    assert discrepancy[0] == discrepancy[2] == 0
    assert discrepancy[1] != 0
    repaired_eq5 = printed_eq5.copy()
    repaired_eq5[1] *= q * Q - 1
    assert all(
        sp.expand(left - right) == 0
        for left, right in zip(candidate_times_right_factor, repaired_eq5)
    )

    result = {
        "source_version": "arXiv:1711.11522v3; equations (5), (13), proof of Theorem 19",
        "scope": "algebraic comparison only; no assumed integral identity or minimality theorem",
        "normal_order": "sum a_j(Q) E^j; E Q=q Q E",
        "custom_scalar_gauge_invariant": str(custom_I),
        "eq13_candidate_scalar_gauge_invariant": str(candidate_I),
        "same_classical_invariant": True,
        "same_generic_quantum_invariant": False,
        "allowed_scalar_gauge_and_equation_multiplier_invariance_checked": True,
        "scalar_equivalence_conclusion": "No scalar gauge in fixed peripheral coordinates relates these two explicit operators.",
        "rational_matrix_gauge_data": {
            "determinant_q_coboundary_factor": str(determinant_factor),
            "literature_trace_leading_infinity": "q^3 Q^2",
            "literature_trace_leading_zero": "q^(-2) Q^(-2)",
            "literature_determinant_infinity": "q^2",
            "literature_determinant_zero": "1",
            "required_formal_gauge_degrees_infinity": [3, -1],
            "required_formal_gauge_orders_zero": [-2, 2],
            "final_determinant_residual": str(final_gauge_residual.as_expr()),
            "proof_location": "notes/custom_literature_equivalence.md, Proposition 3.1",
            "conclusion": "The pole and formal endpoint argument rules out an invertible rational 2x2 gauge in these fixed coordinates. Polarization changes and nonrational gauges remain outside this test.",
        },
        "v3_printed_right_factor_identity_residual_by_E_degree": [str(value) for value in discrepancy],
        "v3_possible_typo_repair": "An additional factor (q Q-1) in the E coefficient of printed equation (5) makes this right-factor identity exact.",
        "ideal_point_caution": "Q-1 is not an analytic unit at Q=1; generic Ore localization and ideal-point specialization are different operations.",
        "bare_two_three_factor_caution": "The factor 8 alone does not test invariance modulo permitted peripheral or boundary factors.",
    }
    destination = Path(__file__).with_name("literature_comparison_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
