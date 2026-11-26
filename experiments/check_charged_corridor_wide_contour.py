#!/usr/bin/env python3
"""Exact constants for the charged-corridor wide-contour proof.

These rational comparisons supplement, and do not replace, its source,
analytic continuation and contour arguments.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    pi_upper = F(22, 7)
    margins = {}

    def positive(name, value):
        assert value > 0, (name, value)
        margins[name] = str(value)

    positive("power2_height", F(3, 10) - pi_upper / 12)
    positive("power3_height", F(3, 10) - pi_upper / 11)
    positive("common_saddle_modulus", F(3, 5) - 2 * pi_upper / 11)
    positive("no_exit_imaginary", F(1, 3) - pi_upper / 11)
    positive("vertical_distance", F(3, 2) - 2 * pi_upper / 11 - F(9, 10))
    cosh_upper = 1 + F(9, 800) / (1 - F(3, 1600))
    positive("cosh_3_over20", F(81, 80) - cosh_upper)
    imaginary_argument = F(4, 35) + F(243, 800)
    positive("return_angle_below_half", F(23, 48) - imaginary_argument)
    positive("power2_lower_slope", F(53, 42) / pi_upper - F(1, 10) - F(3, 20))
    positive("power2_upper_slope", F(1, 2) / pi_upper - F(3, 20))
    positive("power3_lower_slope", F(169, 84) / pi_upper - F(1, 5) - F(3, 20))
    positive("power3_upper_slope", F(5, 4) / pi_upper - F(3, 20))
    positive("bottom_face_gap", F(81, 100) / (40 * pi_upper) - F(1, 200))
    positive("power2_activation_budget", F(1, 100) - pi_upper / 320)
    positive("power3_activation_budget", F(1, 40) - pi_upper / 130)
    assert F(21, 200) - F(1, 40) == F(2, 25)
    assert 1 - F(1, 5) == F(4, 5)

    parameter_checks = 0
    for lower_power, charge, angle_pi_coefficient, budget_pi_coefficient in (
        (2, F(1, 10), F(1, 6), F(1, 320)),
        (3, F(1, 5), F(2, 11), F(1, 130)),
    ):
        for power in range(lower_power, 31):
            for degree in (1, 2):
                denominator = power - F(2, 5) * degree
                assert denominator > 0
                assert 2 * charge / denominator <= angle_pi_coefficient
                assert charge * charge / (2 * denominator * degree) <= budget_pi_coefficient
                parameter_checks += 1
        # Both comparisons improve with increasing |n|, so the finite
        # sweep is diagnostic; the minimum-power inequalities suffice.
    for selected in range(1, 9):
        for outside_ends in (0, 1, 2):
            edges = selected - 1 + outside_ends
            exponent = 2 * selected - F(3, 2) * edges - F(1, 2) * selected
            assert exponent == F(3, 2) * (selected - edges)
            assert F(1, 2) ** selected == F(1, 2 ** selected)
    root = Path(__file__).resolve().parents[1]
    dependencies = [
        Path(__file__).resolve(),
        root / "notes/research_charged_corridor_wide_contour.md",
        root / "notes/research_dominant_saddle_transport.md",
        root / "notes/research_small_charge_path_source.md",
        root / "notes/research_positive_path_partial_charge_bounds.md",
        root / "notes/research_path_mixed_trace_currents.md",
        root / "notes/research_bare_kernel_thin_rectangle.md",
        root / "notes/research_exact_complete_trace_contour.md",
        root / "notes/research_network_whole_boundary_decay.md",
    ]
    result = {
        "status": "all exact constants passed",
        "scope": "Rational constants, charge/power degree bookkeeping, and source N/2 powers. No charge-one or top-relative-homology claim.",
        "strict_comparisons": len(margins),
        "parameter_comparisons": parameter_checks,
        "margins": margins,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
