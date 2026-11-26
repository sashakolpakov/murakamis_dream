#!/usr/bin/env python3
"""Saved-only coverage and assembly audit of the uniform ordinary labels.

No analytic libraries or evaluator imports. The saved midpoint and pi
enclosures remain inputs; their endpoint recombinations are exact Fractions.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "repro/results/research-mixed-terminal-upper-input-left-cut.json"
LAST = "repro/results/research-mixed-selected-outgoing-four-last-row-domination.json"
LEFT = "repro/results/research-mixed-second-selected-left-cut-domination.json"
HALF = "repro/results/research-mixed-second-selected-left-half-row-domination.json"
PROOF = "notes/research_mixed_terminal_ordinary_label_completion.md"
PROTOCOL = "notes/research_mixed_terminal_upper_input_left_cut_protocol.md"
DRIVER = "experiments/check_mixed_terminal_upper_input_left_cut.py"
PINNED = {
    SOURCE: "f55e7101f558c44f11f59798e54dbf6f5250617831a7f899fd1a5513ef6342d2",
    LAST: "23f975f20c70e2f22a197c705d7225c37a30f175c13e92e59353410543d64eeb",
    LEFT: "1404479b59692fb21ab22663c42bc1841a819a73af9ad8d15d23c6a46efecaf7",
    HALF: "2950716a5606c9eba7155a3cb7b97588916782d09b0b4f2c913edebe1a429701",
    PROOF: "592b37d691db0359d4440d6ebffb35591ca14f00f71f3f2bffcc27b72beeec3a",
    PROTOCOL: "1f2fd095cfcf9a0a3a847d6db9d811f6236bb5f6cec940206b20420dbe445fc8",
    DRIVER: "066052c0ae8301c1ce1afa41343289dbbe31e4181fd0e5434b6765d2121c5e0e",
    "notes/research_mixed_terminal_ordinary_label_height_extension.md":
        "1b3b37f6166aed8b5b4e21170d2e6ad9056a73235ce63005c4ba021da341ab7d",
    "notes/research_mixed_typed_last_row_envelopes.md":
        "5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d",
    "notes/research_mixed_terminal_concave_profile_envelope.md":
        "6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd",
}
HEIGHTS = (F(-51, 500), F(-1, 1000))
CORNERS = tuple(itertools.product((F(11, 50), F(9, 20)), repeat=2))


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def interval(value):
    assert value["finite"] is True
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    assert lo <= hi
    return lo, hi


def expected_cells(corners):
    step = (HEIGHTS[1]-HEIGHTS[0])/32
    cells = []
    for j in range(32):
        lo, hi = HEIGHTS[0]+j*step, HEIGHTS[0]+(j+1)*step
        for corner in corners:
            cells.append((j, lo, hi, (lo+hi)/2, corner))
    assert cells[0][1] == HEIGHTS[0] and cells[-1][2] == HEIGHTS[1]
    return cells


def check_cell(row, expected, row_has_corner=True):
    j, lo, hi, mid, corner = expected
    assert row["index"] == j
    assert tuple(map(F, row["height_interval"])) == (lo, hi)
    assert F(row["height_midpoint"]) == mid
    if row_has_corner:
        assert tuple(map(F, row["real_targets"])) == corner
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for path, digest in inputs.items():
        assert sha(ROOT/path) == digest, path
    records = {path: json.loads((ROOT/path).read_text())
               for path in (SOURCE, LAST, LEFT, HALF)}
    for record in records.values():
        assert record.get("changed_inputs", []) == []
        for path, digest in record["input_sha256"].items():
            assert path not in inputs or inputs[path] == digest, path
            inputs[path] = digest
    for path, digest in inputs.items():
        assert sha(ROOT/path) == digest, path

    source = records[SOURCE]
    assert source["status"] == "passed"
    assert source["proof_path"] == PROTOCOL and source["proof_sha256"] == inputs[PROTOCOL]
    assert source["checker_sha256"] == inputs[DRIVER]
    assert source["precision_bits"] == 160
    assert tuple(map(F, source["height_interval"])) == HEIGHTS
    assert source["partition_count"] == 32
    assert F(source["incoming_height"]) == F(17, 250)
    assert F(source["selected_height"]) == F(1, 100)
    assert F(source["trial_real_part"]) == F(1, 4)
    assert F(source["left_cut"]) == F(1, 8)
    assert tuple(map(F, source["incoming_strip_covered_if_passed"])) == (F(3, 100), F(17, 250))
    assert tuple(map(F, source["target_real_interval"])) == (F(11, 50), F(9, 20))
    assert F(source["lipschitz_coefficient_times_pi"]) == F(3, 4)
    assert source["planned_checks"] == source["completed_checks"] == 128
    assert source["arithmetic_complete"] is True
    assert source["pending_planned_checks"] == [] and source["error"] is None
    assert source["strictly_positive_checks"] == 128
    assert source["uniform_left_cut_comparison_proved"] is True
    assert source["primitive_evaluations"] == 768 == 6*128
    for field in ("root_evaluations", "finite_source_evaluations",
                  "adaptive_subdivisions", "target_optimizations", "automatic_retries"):
        assert source[field] == 0
    assert source["new_terminal_profile_sign_claimed"] is False
    assert source["whole_word_or_global_knot_theorem_claimed"] is False

    expected = expected_cells(CORNERS)
    assert len(source["checks"]) == len(expected) == 128
    new_bounds, per_corner, loss_intervals = [], {}, set()
    for row, cell in zip(source["checks"], expected):
        lo, hi = check_cell(row, cell)
        midpoint, loss = interval(row["midpoint_difference"]), interval(row["height_loss"])
        assert 0 < loss[0] <= loss[1]
        coefficient = F(3, 4)*(hi-lo)/2
        # Rational sanity range only; the author enclosure certifies pi.
        assert coefficient*F(157, 50) < loss[0] <= loss[1] < coefficient*F(22, 7)
        lower, upper = midpoint[0]-loss[1], midpoint[1]+loss[1]
        assert lower == F(row["whole_interval_lower_rational"])
        assert upper == F(row["whole_interval_upper_rational"])
        assert row["strictly_positive"] is True and lower > F(1, 300)
        loss_intervals.add(loss)
        corner = cell[-1]
        per_corner[corner] = min(per_corner.get(corner, lower), lower)
        new_bounds.append(lower)
    assert len(loss_intervals) == 1  # All 32 intervals have exactly equal width.
    new_min = min(new_bounds)
    assert new_min == F(source["minimum_whole_interval_lower_rational"])
    assert new_min == F(321523598565176372593575865896782689064112233199,
                       93536104789177786765035829293842113257979682750464)

    old_specs = ((LAST, CORNERS, F(49, 2000)),
                 (LEFT, CORNERS, F(163, 10000)),
                 (HALF, ((F(11, 50), F(11, 50)),), F(23, 625)))
    old_summaries = []
    for path, corners, threshold in old_specs:
        record = records[path]
        assert record["status"] == "complete" and record["precision_bits"] == 160
        assert record["partition_count"] == 32
        assert tuple(map(F, record["height_interval"])) == HEIGHTS
        assert record["lipschitz_constant"] == "9*pi/10"
        assert record["source_root_evaluations"] == record["finite_sum_evaluations"] == 0
        if path != HALF:
            assert record["corner_count"] == 4
        else:
            assert tuple(map(F, record["real_targets"])) == corners[0]
        if path in (LEFT, HALF):
            assert F(record["outgoing_height"]) == F(1, 100)
            assert F(record["trial_real_part"]) == F(3, 10)
            assert record["adaptive_subdivisions"] == 0
        if path == LEFT:
            assert F(record["incoming_height"]) == F(21, 1000)
            assert F(record["left_cut"]) == F(1, 8)
        if path == HALF:
            assert F(record["incoming_height"]) == -F(39, 500)
            assert F(record["half_row"]) == F(1, 2)
            assert F(record["real_target_loss"]) == F(3, 800)
        cells = expected_cells(corners)
        assert len(record["checks"]) == len(cells)
        bounds = []
        for row, cell in zip(record["checks"], cells):
            check_cell(row, cell, row_has_corner=path != HALF)
            lower, upper = F(row["lower_rational"]), F(row["upper_rational"])
            assert threshold < lower <= upper and row["pass"] is True
            bounds.append(lower)
        minimum = min(bounds)
        assert minimum == F(record["worst_lower_rational"])
        old_summaries.append({"path": path, "sha256": inputs[path],
                              "whole_height_checks": len(cells),
                              "minimum_saved_lower_rational": str(minimum),
                              "strict_verified_threshold_rational": str(threshold)})
    assert [r["whole_height_checks"] for r in old_summaries] == [128, 128, 32]

    # The exact transport margins from the independently proved height lemma.
    half_gap = F(23, 625)-F(19, 500)*F(127, 140)
    left_low_gap = F(163, 10000)-F(9, 1000)*F(11, 7)
    last_gap = F(49, 2000)-F(7, 2000)*F(44, 7)
    assert half_gap == F(163, 70000) > F(1, 500)
    assert left_low_gap == F(151, 70000) > F(1, 500)
    assert last_gap == F(1, 400) > F(1, 500)
    assert new_min > F(1, 300) > F(1, 500)
    low_left = (F(-29, 250), F(3, 100))
    high_left = (F(3, 100), F(17, 250))
    half_domain = (F(-29, 250), F(2, 25))
    last_domain = (F(-223, 2000), F(2, 25))
    common_domain = (F(-223, 2000), F(17, 250))
    assert low_left[1] == high_left[0]
    assert low_left[0] <= common_domain[0] < high_left[1] == common_domain[1]
    for domain in (half_domain, last_domain):
        assert domain[0] <= common_domain[0] <= common_domain[1] <= domain[1]
    typed_heights = {"K3": (F(-9, 125), F(17, 250)),
                     "K4": (F(-27, 250), F(-1, 1000))}
    assert all(common_domain[0] <= lo <= hi <= common_domain[1]
               for lo, hi in typed_heights.values())
    changed = [path for path, digest in inputs.items() if sha(ROOT/path) != digest]
    result = {
        "status": "passed" if not changed else "input failure",
        "source_path": SOURCE, "source_sha256": inputs[SOURCE],
        "proof_path": PROOF, "proof_sha256": inputs[PROOF],
        "checker_sha256": inputs[own], "input_sha256": inputs, "changed_inputs": changed,
        "new_closed_height_cells": 32, "new_corner_count": 4,
        "new_exact_endpoint_recombinations": 128,
        "author_primitive_call_count_verified": 768,
        "minimum_new_lower_rational": str(new_min),
        "new_corner_minima": [{"corner": list(map(str, corner)), "lower_rational": str(value)}
                              for corner, value in per_corner.items()],
        "old_record_checks": old_summaries,
        "transport_gap_lower_bounds_rational": {
            "half_row": str(half_gap), "left_cut_lower_strip": str(left_low_gap),
            "last_row": str(last_gap), "left_cut_upper_strip": str(new_min)},
        "incoming_height_interval_rational": list(map(str, common_domain)),
        "index_height_interval_rational": list(map(str, HEIGHTS)),
        "typed_height_intervals_rational": {k: list(map(str, v)) for k, v in typed_heights.items()},
        "target_real_interval_rational": ["11/50", "9/20"],
        "selected_height_rational": "1/100",
        "common_ordinary_profile_gap_rational": "1/500",
        "nonmain_labels_dominated": 6, "periodic_last_row_carriers": 4,
        "profile_count_before": 378, "profile_count_after": 54,
        "independent_real_target_domain_preserved": True,
        "original_finite_envelope_hypotheses_retained": True,
        "analytic_evaluations": 0, "source_or_root_replays": 0,
        "new_terminal_profile_sign_claimed": False,
        "uniform_complete_terminal_source_gap_claimed": False,
        "whole_word_or_global_knot_theorem_claimed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    assert not changed, changed
    print(json.dumps({"status": result["status"], "bindings": len(inputs),
                      "new_checks": 128, "old_checks": [128, 128, 32],
                      "new_minimum": float(new_min), "common_gap": "1/500",
                      "output_sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
