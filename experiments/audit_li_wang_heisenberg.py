#!/usr/bin/env python3
"""Exact calculations for the Li--Wang terminology and branch audit.

The counterexample is a torsion-zero algebraic curve, not a knot claim.
No colored-Jones asymptotics or knot K2 torsion theorem is tested here.
"""

import json
from pathlib import Path

import sympy as s


def universal_line():
    t = 2 * s.pi * s.I
    F, G, dF, dG = s.symbols("F G dF dG")
    a, b, c, d = s.symbols("a b c d", integer=True)
    connection = F * dG / t
    shifted = connection.subs(F, F + t * a)
    assert s.expand(shifted - connection - a * dG) == 0
    cocycle_error = a * G + c * (G + t * b) - (a + c) * G
    assert s.expand(cocycle_error - t * b * c) == 0
    assert s.simplify(s.exp(cocycle_error)) == 1

    F0, G0 = s.symbols("F0 G0")
    # Antisymmetry: the boundary term of integral d(FG) is explicit.
    skew_sum = ((F0 + t * a) * (G0 + t * b) - F0 * G0
                - G0 * t * a - F0 * t * b)
    assert s.expand(skew_sum - t**2 * a * b) == 0
    assert s.simplify(s.exp(skew_sum / t)) == 1
    # Logarithm changes alter the exponent by an integral multiple of t.
    r, k = s.symbols("r k", integer=True)
    branch_error = t * r * (t * b) - t * k * (t * a)
    assert s.simplify(s.exp(branch_error / t)) == 1

    # The Heisenberg horizontal form dH-F dG is invariant.
    H, dH = s.symbols("H dH")
    assert s.expand((dH + t * a * dG)
                    - (F + t * a) * dG - (dH - F * dG)) == 0
    # Curvature of the declared connection nabla=d-A, in dF wedge dG units.
    curvature = -s.diff(F / t, F)
    assert s.simplify(curvature + 1 / t) == 0
    # The real two-torus integral of dF wedge dG is t^2.
    assert s.simplify(curvature * t**2 / t) == -1
    return {
        "deck_cocycle_exact_mod_2pi_i": True,
        "connection_automorphy_exact": True,
        "antisymmetry_exact": True,
        "log_branch_independence_with_continued_logs": True,
        "Heisenberg_horizontal_form_invariant": True,
        "curvature_for_nabla_equals_d_minus_A": "-dF wedge dG/(2*pi*i)",
        "curvature_integral_over_real_torus_divided_by_2pi_i": -1,
    }


def local_secondary_form():
    x, u, y, v = s.symbols("x u y v", real=True)
    a = s.Symbol("a", integer=True)
    coordinates = (x, u, y, v)
    F, G = x + s.I * u, y + s.I * v
    rho = s.Matrix([-y, -s.I * y, 0, -u + s.I * x])
    rhs = s.Matrix([F * s.diff(G, z) - s.diff(y * F, z)
                    for z in coordinates])
    assert (rho - rhs).applyfunc(s.expand) == s.zeros(4, 1)
    for j in range(4):
        for k in range(j + 1, 4):
            exterior = s.diff(rho[k], coordinates[j]) - s.diff(rho[j], coordinates[k])
            expected = (s.diff(F, coordinates[j]) * s.diff(G, coordinates[k])
                        - s.diff(F, coordinates[k]) * s.diff(G, coordinates[j]))
            assert s.expand(exterior - expected) == 0
    shift = rho.subs(u, u + 2 * s.pi * a) - rho
    assert shift == s.Matrix([0, 0, 0, -2 * s.pi * a])
    return {
        "rho_equals_F_dG_minus_d_ReG_F": True,
        "d_rho_equals_dF_wedge_dG": True,
        "rho_is_local_with_change_minus_2pi_a_d_arg_g": True,
        "imaginary_part_eta_is_globally_branch_invariant": True,
    }


def common_coordinate_comparison():
    t = 2 * s.pi * s.I
    U, V, dU, dV = s.symbols("U V dU dV")
    a, b = s.symbols("a b", integer=True)
    regulator = V * dU / t  # f=l, g=m
    gauge = -U * V / (2 * t)
    symmetric = regulator + s.diff(gauge, U) * dU + s.diff(gauge, V) * dV
    repository = -(U * dV - V * dU) / t
    assert s.expand(2 * symmetric - repository) == 0
    shifted_gauge = gauge.subs({U: U + t * a, V: V + t * b}, simultaneous=True)
    multiplier_log = shifted_gauge - gauge + b * U
    expected = (b * U - a * V) / 2 - t * a * b / 2
    assert s.expand(multiplier_log - expected) == 0
    assert s.simplify(s.exp(2 * multiplier_log - (b * U - a * V))) == 1
    return {
        "same_torus_coordinates_only": True,
        "repository_boundary_line_is_square_of_symmetric_regulator_line": True,
        "unsquared_symmetric_multiplier_retains_minus_one_to_ab": True,
        "coordinate_squares_and_complete_point_shifts_require_separate_transport": True,
    }


def branch_counterexamples():
    theta = s.Symbol("theta", real=True)
    t = 2 * s.pi * s.I
    # Curve l=-z, m=z, with {l,m}=0 by {x,-x}=0.
    # At z=1, log(m)=0 and the starting arg(l) is pi.
    continued_integral = s.integrate(s.pi + theta, (theta, 0, 2 * s.pi))
    fixed_cut_integral = (s.integrate(s.pi + theta, (theta, 0, s.pi))
                          + s.integrate(theta - s.pi, (theta, s.pi, 2 * s.pi)))
    assert continued_integral == 4 * s.pi**2
    assert fixed_cut_integral == 2 * s.pi**2
    assert s.simplify(s.exp(-continued_integral / t)) == 1
    assert s.simplify(s.exp(-fixed_cut_integral / t)) == -1

    # Even with continued logs, the integral called U is a path-cover
    # coordinate. Inserting a loop changes the endpoint frame.
    action = -(s.pi * theta + theta**2 / 2)
    endpoint_difference = s.expand(action.subs(theta, theta + 2 * s.pi) - action)
    assert s.expand(endpoint_difference + 4 * s.pi**2 + 2 * s.pi * theta) == 0
    normalized_example = s.simplify(endpoint_difference.subs(theta, s.pi / 2)
                                    / (4 * s.pi**2))
    assert normalized_example == -s.Rational(5, 4)
    assert normalized_example.is_integer is False
    return {
        "curve": "l=-z,m=z on C*, with K2 symbol zero (q=1)",
        "continued_unit_loop_regulator": 1,
        "literal_fixed_cut_unit_loop_regulator": -1,
        "continued_quantization_integral_divided_by_4pi_squared": "1",
        "fixed_cut_quantization_integral_divided_by_4pi_squared": "1/2",
        "continued_open_path_U_difference_at_theta_pi_over_2_divided_by_4pi_squared": "-5/4",
        "domain_of_open_path_obstruction": "endpoint-only scalar reading; path-cover or bundle-section reading survives",
        "counterexample_is_not_claimed_to_be_a_knot_A_curve": True,
    }


def main():
    result = {
        "scope": "Independent logarithmic line and branch audit; no knot asymptotic theorem.",
        "universal_line": universal_line(),
        "secondary_form": local_secondary_form(),
        "boundary_line_comparison": common_coordinate_comparison(),
        "branch_diagnostics": branch_counterexamples(),
        "knot_K2_torsion_input_reproved": False,
        "root_of_unity_quantum_norm_torsor_identification_proved": False,
    }
    destination = Path(__file__).with_name("li_wang_heisenberg_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
