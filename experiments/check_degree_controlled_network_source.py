#!/usr/bin/env python3
"""Exact constants for the degree-controlled original network source.

The written proof establishes the graph-independent source decomposition
and the marked geometry. These checks cover only its scalar budgets.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_degree_controlled_network_source.md"
DEPENDENCIES = [
    "notes/research_positive_path_partial_charge_bounds.md",
    "notes/research_bare_kernel_thin_rectangle.md",
    "notes/research_path_mixed_trace_currents.md",
    "notes/research_uniform_path_trace_assembly.md",
    "notes/research_positive_point_marked_completion.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    pi_upper, pi_lower = F(22, 7), F(157, 50)
    margins = {
        "real_box_with_complex_charge_reserve": 1-pi_upper/4-F(7,40)-pi_upper/400,
        "imaginary_box_with_complex_charge_reserve": F(1,3)-F(123,400)-pi_upper/400,
        "return_map_contraction_below_half": F(1,2)-F(43,90),
        "critical_modulus_below_9_over_10": F(9,10)-5*pi_upper/18,
        "critical_height_below_3_over_10": F(3,10)-35*pi_upper/373,
        "action_cost_per_incidence_below_3_over_40": F(3,40)-35*pi_upper/1492,
        "degree_one_height_below_degree_two_maximum": F(35,373)-F(70,1493),
        "height_corner_monotonicity": 4-F(9,5),
        "midpoint_interval_nonempty": pi_lower/2-F(3,2),
        "negative_height_slope_degree_at_least_two": F(242,42)/pi_upper-F(9,5),
        "negative_height_slope_degree_one": F(247,42)/pi_upper-F(9,5),
        "positive_height_slope_below_minus_one": 3/pi_upper-F(1,2),
        "bottom_current_loss_per_incidence": F(9,1000)/pi_upper-F(1,400),
        "removed_row_surplus_per_incidence": F(21,200)-F(3,40),
        "wide_current_real_coordinate_margin": F(3,2)-F(9,10),
    }
    assert all(value > 0 for value in margins.values()), margins
    identities = {
        "degree_scaled_height_denominator": (4-F(2,5))**2+F(7,5)**2 == F(373,25),
        "degree_one_height_denominator": (8-F(2,5))**2+F(7,5)**2 == F(1493,25),
        "degree_two_height_denominator": (8-F(4,5))**2+F(14,5)**2 == F(1492,25),
        "removed_row_loss": F(21,200)-F(3,40) == F(3,100),
        "minimum_current_displacement": F(3,2)-F(9,10) == F(3,5),
    }
    assert all(identities.values())
    record = {
        "status": "passed",
        "strict_comparisons": len(margins),
        "exact_identities": len(identities),
        "arithmetic": "exact fractions",
        "scope": "Scalar contraction, height, current and removed-row budgets; not numerical evidence for graph geometry.",
        "margins": {k:{"exact":str(v),"approximate":float(v)} for k,v in margins.items()},
        "identities": identities,
        "script_sha256": sha(Path(__file__).resolve()),
        "proof_sha256": sha(PROOF),
        "dependency_sha256": {name:sha(ROOT/name) for name in DEPENDENCIES},
    }
    out = ROOT / "repro/results/research-degree-controlled-network-source.json"
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(margins)} strict comparisons and {len(identities)} identities: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
