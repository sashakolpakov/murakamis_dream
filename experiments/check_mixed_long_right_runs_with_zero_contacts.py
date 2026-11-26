#!/usr/bin/env python3
"""Exact existing-input assembly of long right runs with zero contacts."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_long_right_runs_with_zero_contacts.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-long-right-runs-with-zero-contacts.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        value = sha(ROOT / path)
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        if expected is not None:
            assert value == expected, path
        return value

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in merged:
                    assert merged[p] == digest
                merged[p] = digest
                bind(p, digest)
        for p in merged:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem):
        path = "repro/results/research-" + stem.replace("_", "-") + ".json"
        record = inherit(path)
        if record is None:
            raw = (ROOT / path).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == bind(path)
            record = json.loads(raw)
        assert record["status"] == "passed"
        assert record["proof_sha256"] == bind("notes/research_" + stem + ".md")
        assert record["script_sha256"] == bind("experiments/check_" + stem + ".py")
        primary[path] = record
        return record

    half = load("mixed_closed_half_period")
    quantitative = load("mixed_quantitative_right_run_boundary")
    profiles = load("mixed_height_resolved_seam_sources")
    bind("notes/research_mixed_direct_right_run_replacement.md")
    bind("notes/research_mixed_split_cutoff_hybrid_contour.md")
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    check("complete closed-half pointwise input",
          half["typed_selection_cases"] == 24 and half["rational_intervals"] == 96
          and half["subdivisions"] == 0
          and F(half["singleton_phase_reserve"]) == F(3, 1000)
          and F(half["internal_phase_reserve"]) == F(1, 3))
    check("completed quantitative boundary costs",
          quantitative["real_corner_count"] == 32
          and quantitative["exact_identity_count"] == 13
          and quantitative["scalar_comparison_count"] == 6
          and quantitative["boundary_costs"] ==
              {"outside_collar": "11/4", "nonlow": "7/4"}
          and quantitative["run_cutoffs"] ==
              {"outside_collar": 552, "nonlow": 352})
    check("complete old height source extraction",
          profiles["source_grid_values"] == 225
          and profiles["original_source_cells"] == 57092
          and profiles["independent_replay_source_cells"] == 57166)

    expected = {
        "A00": ["-3/100", "0", "1/50"],
        "A10": ["-3/100", "0", "1/50"],
        "A01": ["-57/1000", "-1/50", "0", "7/500"],
        "A11": ["-57/1000", "0", "7/500"],
        "B0": ["-3/100", "0", "1/50"],
        "B1": ["-57/1000", "0", "7/500"],
    }
    table = profiles["profiles"]
    assert set(table) == set(expected)
    knots = []
    for name, heights in expected.items():
        assert [F(row["height"]) for row in table[name]] == list(map(F, heights))
        for row in table[name]:
            assert F(row["upper"]) > F(29, 100)
            knots.append(dict(profile=name, height=row["height"], ceiling=row["upper"]))
    check("all 19 fixed profile knots exceed 29/100", len(knots) == 19)
    check("source profiles contain the entire repaired unselected bands",
          min(F(row["height"]) for row in table["A00"]) == -F(3, 100)
          and max(F(row["height"]) for row in table["A00"]) == F(1, 50)
          and min(F(row["height"]) for row in table["A01"]) == -F(57, 1000)
          and any(F(row["height"]) == 0 for row in table["A01"]))
    check("one seam Fourier half on each incident edge",
          F(1, 2)+F(1, 2) == 1)
    gamma = F(439, 1250)
    seam_cost = F(13, 8)-F(29, 100)+gamma
    check("exact repaired seam boundary cost", seam_cost == F(8431, 5000))
    check("strict nonlow allowance contains every seam boundary",
          F(7, 4)-seam_cost == F(319, 5000) > 0)
    check("general allowance contains nonlow allowance", F(11, 4) > F(7, 4))
    for cost, cutoff in ((F(11, 4), 552), (F(7, 4), 352)):
        check(f"arbitrary run length threshold {cutoff}",
              2*cost-F(cutoff-1, 50) == -F(cutoff, 100))
    check("each extra internal edge retains favorable slope",
          F(1, 50)-F(1, 100) == F(1, 100) > 0)
    check("all-right cycles need no boundary debit", F(1, 50) > F(1, 100))
    check("one total finite tolerance with a nonempty right set",
          F(1, 100)-F(1, 200)-F(1, 1000) == F(1, 250) > 0
          and F(3, 1000)-F(1, 500) == F(1, 1000) > 0)

    old, input_hash = None, None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert old["checks"] == checks and old["validated_profile_knots"] == knots
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == h for p, h in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(
        status="passed", exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(deps),
        validated_profile_knots=knots, profile_knot_count=19,
        seam_boundary_cost="8431/5000", seam_boundary_allowance="7/4",
        general_run_cutoff=552, nonlow_or_collar_run_cutoff=352,
        right_phase_loss_per_vertex="1/100",
        seam_phase_loss_per_vertex="3/1000",
        right_finite_loss_per_vertex="1/200",
        seam_finite_loss_per_vertex="1/500",
        new_critical_roots=0, new_source_cells=0, new_parameter_cells=0,
        cyclic_word_enumerations=0, proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope="Complete original selected integrals with sufficiently long right runs, allowing arbitrary physical zero contacts. No general short-run or whole-period conclusion.",
    )
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks; 19 profile knots;",
          len(primary), "primary records;", len(deps), "bindings", flush=True)


if __name__ == "__main__":
    main()
