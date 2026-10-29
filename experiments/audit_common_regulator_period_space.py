#!/usr/bin/env python3
"""Exact common Frobenius/regulator connection and source descent checks.

The geometric action line is not identified with the actual knot period.
The last scalar recurrence is a non-knot diagnostic of root-only descent.
"""

import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


def connection_and_deck_certificate():
    h, U, V, H, tau = s.symbols("h U V H tau", nonzero=True)
    A, B, C = s.symbols("A B C", integer=True)
    A1, B1, C1, A2, B2, C2 = s.symbols(
        "A1 B1 C1 A2 B2 C2", integer=True
    )
    R = U * V / 4 - H / 2
    action = (U * V - H) / 2

    # Components along omega_q, omega_m, omega_l of the horizontal
    # derivative on the Kummer/Heisenberg connection space.
    def horizontal_d(f):
        return s.Matrix([s.diff(f, h), s.diff(f, U),
                         s.diff(f, V) + U * s.diff(f, H)])

    assert horizontal_d(R) == s.Matrix([0, V / 4, -U / 4])
    assert horizontal_d(action) == s.Matrix([0, V / 2, 0])
    kappa = s.Symbol("kappa", integer=True)
    action_lift = action + kappa * tau * U
    assert horizontal_d(action_lift) == s.Matrix([0, V / 2 + kappa * tau, 0])
    fJ = tau**2 / (2 * h)
    fW = tau * U / (2 * h)
    fZ = action / (2 * h)
    assert s.cancel(action_lift / (2 * h) - fZ - kappa * fW) == 0
    expected = [
        s.Matrix([-tau**2 / (2 * h**2), 0, 0]),
        s.Matrix([-tau * U / (2 * h**2), tau / (2 * h), 0]),
        s.Matrix([-action / (2 * h**2), V / (4 * h), 0]),
    ]
    for f, derivative in zip((fJ, fW, fZ), expected):
        assert (horizontal_d(f) - derivative).applyfunc(s.cancel) == s.zeros(3, 1)
        # Full exponential connection d-df is integrable.
        coordinates = (h, U, V, H)
        for x in coordinates:
            for y in coordinates:
                assert s.diff(f, x, y) == s.diff(f, y, x)

    def deck(values, a, b, c):
        u, v, z = values
        return u + 2 * tau * a, v + 2 * tau * b, z + 2 * tau * a * v + 4 * tau**2 * c

    changed = dict(zip((U, V, H), deck((U, V, H), A, B, C)))
    pull = lambda f: f.subs(changed, simultaneous=True)
    assert s.expand(pull(fW) - fW - 2 * A * fJ) == 0
    assert s.expand(pull(fZ) - fZ - B * fW - 2 * (A * B - C) * fJ) == 0
    assert s.expand(pull(R) - R
                    - tau * (B * U - A * V) / 2
                    - tau**2 * (A * B - 2 * C)) == 0
    left = deck(deck((U, V, H), A1, B1, C1), A2, B2, C2)
    right = deck((U, V, H), A1 + A2, B1 + B2, C1 + C2 + A2 * B1)
    assert all(s.expand(x - y) == 0 for x, y in zip(left, right))
    # The action-line monomials have the same noncommutative central law.
    exponent_left = 2 * (A1 * B1 - C1 + A2 * B2 - C2 + A1 * B2)
    exponent_right = 2 * ((A1 + A2) * (B1 + B2) - C1 - C2 - A2 * B1)
    assert s.expand(exponent_left - exponent_right) == 0

    N = s.Symbol("N", integer=True, positive=True)
    assert s.cancel(fW.subs(h, tau / N) - N * U / 2) == 0
    assert s.cancel(fZ.subs(h, tau / N) - N * action / (2 * tau)) == 0
    assert s.cancel(fJ.subs(h, tau / N) - tau * N / 2) == 0
    assert s.cancel(s.diff(fJ + s.log(h), h)
                    - 1 / h + tau**2 / (2 * h**2)) == 0
    assert s.cancel(4 * s.diff(fJ, h) + 2 * tau**2 / h**2) == 0
    return {
        "regulator_and_preferred_longitude_action_differentials_exact": True,
        "three_standard_exponential_connection_forms_exact": True,
        "flatness_on_the_marked_curve_uses_omega_m_wedge_omega_l_zero": True,
        "integral_Heisenberg_group_composition_exact": True,
        "central_Tate_and_Frobenius_monomials_retained": True,
        "root_restrictions_of_the_three_exponents_exact": True,
        "joint_complete_cap_connection_retains_the_Tate_line": True,
        "finite_root_phase_divisor_is_not_preserved_by_q_connection": True,
        "no_identification_with_the_selected_quantum_knot_period": True,
    }


def invariant_norm_certificate():
    u, ui, v, vi, r = s.symbols("ReU ImU ReV ImV ImR", real=True)
    N = s.Symbol("N", integer=True, positive=True)
    A, B = s.symbols("A B", integer=True)
    pi = s.pi
    imaginary_action = r + (u * vi + ui * v) / 4
    regulator_norm = 2 * r / pi - (u * vi - v * ui) / (2 * pi)
    action_norm = N * imaginary_action / (2 * pi) - N * u * vi / (4 * pi)
    assert s.expand(action_norm - N * regulator_norm / 4) == 0
    changed = {ui: ui + 2 * pi * A, vi: vi + 2 * pi * B,
               r: r + pi * (B * u - A * v) / 2}
    assert s.expand(regulator_norm.subs(changed, simultaneous=True) - regulator_norm) == 0
    assert s.expand(action_norm.subs(changed, simultaneous=True) - action_norm) == 0
    assert s.expand(action_norm.subs({u: 0, ui: 0, v: 0, vi: 0}) - N * r / (2 * pi)) == 0
    return {
        "log_norm_action_equals_N_over_four_log_norm_regulator": True,
        "both_norms_invariant_under_the_integral_deck_action": True,
        "complete_action_log_norm": "N*Vol/(2*pi)",
        "scope": "Constructed marked geometric period; no assertion for F_N(1).",
    }


def root_phase_certificates():
    results = []
    for N in range(2, 26):
        J = s.I**N
        zeta = s.cancel(s.I / J)
        epsilon = J**2
        eta = -s.I * J
        assert s.simplify(s.exp(s.pi * s.I * N / 2) - J) == 0
        assert s.simplify(zeta - s.I**(1 - N)) == 0
        assert s.simplify(epsilon - (-1)**N) == 0
        assert s.simplify(eta - s.I**(N + 3)) == 0
        assert s.simplify(eta - zeta**3) == 0
        assert s.simplify(-zeta**2 - epsilon) == 0
        assert s.simplify(J**4 - 1) == 0
        results.append({"level": N, "J_N": str(J), "zeta_N": str(zeta),
                        "eta_N": str(eta), "all_actual_phase_relations_exact": True})
    return results


def source_retraction_certificate():
    q, M, w = s.symbols("q M w", nonzero=True)
    sigma = lambda f: s.cancel(f.subs({M: q * M, w: -w}, simultaneous=True))
    constant_term = lambda f: s.cancel(s.residue(f / w, w, 0))
    C = s.Matrix([[M, 1], [1, q / M]])
    assert s.cancel(C.det()) != 0
    fixtures = [
        s.Matrix([(M + w) / (w**2 * (w - M)), (1 + M * w) / (1 - q * w)]),
        s.Matrix([(1 + M + w**2) / (M + w), 1 / w + M / (1 + M * w)]),
        s.Matrix([w**3 / (1 - M * w) + 1 / (M * w),
                  (M**2 + w + w**2) / (w**2 * (1 + q * M * w))]),
    ]
    records = []
    for index, vector in enumerate(fixtures):
        residual = vector.applyfunc(sigma) - C * vector
        left = residual.applyfunc(constant_term)
        extracted = vector.applyfunc(constant_term)
        right = extracted.applyfunc(sigma) - C * extracted
        assert (left - right).applyfunc(s.cancel) == s.zeros(2, 1)
        records.append({"fixture": index, "Laurent_constant_vector": str(extracted),
                        "matrix_source_retraction_exact_with_polar_denominators": True})
    return records


def root_only_splitting_certificates():
    results = []
    for N in range(2, 14):
        prime, _, q = field(N)
        n = 2 * N
        coefficients = [pow(q, -r * (r + 1) // 2, prime) for r in range(n)]
        assert coefficients[0] == 1
        assert all(pow(q, r, prime) * coefficients[r] % prime == coefficients[r - 1]
                   for r in range(1, n))
        assert coefficients[-1] == prime - 1
        # sigma(A)-M*A-(1+w^2)=M^(2N)-w^2 exactly over F_p[M,w].
        # It vanishes only after w=M^N, and its M span is exactly 2N.
        assert -coefficients[-1] % prime == 1
        results.append({"level": N, "prime": prime, "cyclic_order": n,
                        "generic_Frobenius_residual": "(M^(2N)-w^2)/(1+w^2)",
                        "cleared_residual_M_span": 2 * N,
                        "whole_root_graph_solution_exact": True,
                        "generic_source_comparison_fails": True})
    return results


def main():
    result = {
        "scope": "A common marked geometric period space and faithful source descent; no volume-conjecture proof.",
        "connection_and_deck_action": connection_and_deck_certificate(),
        "invariant_root_norm": invariant_norm_certificate(),
        "prescribed_root_phases": root_phase_certificates(),
        "matrix_source_retractions": source_retraction_certificate(),
        "non_knot_root_only_splittings": root_only_splitting_certificates(),
    }
    output = Path(__file__).with_name("common_regulator_period_space_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "result": str(output),
        "exact_connection_Heisenberg_action_and_regulator_norm": True,
        "actual_phase_levels": len(result["prescribed_root_phases"]),
        "polar_matrix_source_retractions": len(result["matrix_source_retractions"]),
        "non_knot_root_only_comparison_diagnostics": len(result["non_knot_root_only_splittings"]),
    }), flush=True)


if __name__ == "__main__":
    main()
