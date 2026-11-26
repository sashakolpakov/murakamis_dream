#!/usr/bin/env python3
"""Exact scalar checks for the uniform pair-kernel library proof.

This checks seven rational sufficient inequalities. The source contour,
Schur-complement, and marked zero-join claims have written proofs; no
finite-level numerical experiment is offered as a proof of them.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_internal_pair_three_kernel_compositions.md"
DEPENDENCIES = [
    "notes/research_high_degree_short_internal_vertex.md",
    "notes/research_uniform_terminal_family_and_star_fillings.md",
    "notes/research_finite_two_boundary_kernel_closure.md",
    "notes/research_all_nonzero_degree_two_fillings.md",
    "notes/research_marked_degree_two_tangle_moves.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    pi_upper, pi_lower = F(22, 7), F(25, 8)
    cutoff = F(6, 25)
    margins = {
        "critical_contraction_maps_radius_7_strictly_inside":
            7 - 2 * pi_upper - F(4, 5) * pi_upper * F(7, 64),
        "critical_contraction_derivative_less_than_1_over_25":
            F(1, 25) - F(4, 5) * pi_upper / 64,
        "horizontal_endpoint_separation": cutoff - F(7, 64),
        "discarded_wire_gap": pi_lower / 100 - F(7, 4100),
        "outer_original_row_gap": cutoff**2 / (2 * pi_upper) - F(7, 4100),
        "central_trace_rectangle_inside_radius_1_over_4":
            F(1, 16) - cutoff**2 - F(7, 128)**2,
        "rescaled_amplitude_denominator_nonzero":
            1 / (2 * pi_upper) - F(2, 5 * 64),
    }
    assert len(margins) == 7
    assert all(margin > 0 for margin in margins.values()), margins
    record = {
        "status": "passed",
        "check_count": len(margins),
        "arithmetic": "exact fractions",
        "scope": "Scalar sufficient inequalities only; no threshold value or asymptotic sample.",
        "margins": {
            name: {"exact": str(margin), "approximate": float(margin)}
            for name, margin in margins.items()
        },
        "script_sha256": sha(Path(__file__).resolve()),
        "proof_sha256": sha(PROOF),
        "dependency_sha256": {name: sha(ROOT / name) for name in DEPENDENCIES},
    }
    output = ROOT / "repro/results/research-uniform-pair-kernel-library.json"
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Passed {len(margins)} exact scalar comparisons: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
