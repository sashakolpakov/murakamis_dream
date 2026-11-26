#!/usr/bin/env python3
"""Exact saved-endpoint exclusion; no numerical/reference reevaluation."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = "repro/results/research-mixed-second-selected-shifted-reference-diagnostic.json"
EXACT = "repro/results/research-mixed-second-selected-rational-transport-exact.json"
PINNED = {
    DATA: "4030c1155214b98b9a7129204d99fbefae13fce6bf0313a3f45833f68f99d4d5",
    EXACT: "7db105fdc67e0331bebc69d29d33c11cfaff6432f0366344932c96966887bc43",
    "notes/research_mixed_second_selected_saved_reference_exclusion.md": "6cdbff9cfc3459811c462e76c02d381f87eb07da8eb56f51709f0d7629c89292",
    "notes/research_mixed_second_selected_reference_curve.md": "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoints(record):
    assert record["finite"]
    lo, hi = F(record["lower_rational"]), F(record["upper_rational"])
    assert lo <= hi
    return lo, hi


def coordinate_distance(record):
    lo, hi = endpoints(record)
    return max(F(0), lo, -hi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        assert sha(ROOT/name) == expected, name
    data = json.loads((ROOT/DATA).read_text())
    exact = json.loads((ROOT/EXACT).read_text())
    assert data["alpha"] == 1 and data["beta_candidates"] == [0, 1]
    assert data["tested_address"] == "001111101111010111"
    assert data["tested_box"] == ["115337/512000", "57677/256000", "8919/256000", "279/8000"]
    assert data["tested_boxes"] == 1 and data["primitive_evaluations"] == 0
    assert data["scalar_budget_evaluations"] == 0
    for source in (data, exact):
        for name, expected in source["input_sha256"].items():
            path = Path(name)
            relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
            assert relative not in bindings or bindings[relative] == expected
            bindings[relative] = expected
    script = str(Path(__file__).resolve().relative_to(ROOT))
    bindings[script] = sha(Path(__file__))
    for name, expected in bindings.items():
        assert sha(ROOT/name) == expected, name

    results = {}
    expected_product_bounds = {
        "0": F(31265543203252460797129721291185489, 18014398509481984),
        "1": F(400032683734846533672225797599641489, 4294967296),
    }
    for beta in ("0", "1"):
        shape = data["shared_transport"]["maps"]["B"+beta]
        assert shape["status"] == "enclosed"
        imag_lo, imag_hi = endpoints(shape["full_value"]["imag"])
        assert imag_lo > 0
        original = data["results_by_beta"][beta]
        assert original["status"] == "inconclusive"
        label = "C"+beta+" derivative denominator product"
        assert original["reason"] == "zero not excluded: "+label
        checks = original["details"]["regularity_checks"]
        failed = [check for check in checks if check["label"] == label]
        assert len(failed) == 1 and not failed[0]["strictly_separated"]
        coordinate_lower = max(coordinate_distance(failed[0]["value"][axis]) for axis in ("real", "imag"))
        assert coordinate_lower > 0
        derivative_denominator = exact["maps"]["C"+beta]["derivative"]["denominator"]
        product_lower = F(abs(derivative_denominator["content"]))
        factor_bounds = []
        for factor in derivative_denominator["factors"]:
            name = hashlib.sha256(json.dumps(factor["coefficients_descending"], separators=(",", ":")).encode()).hexdigest()
            factor_label = "C"+beta+" derivative denominator factor "+name
            hits = [check for check in checks if check["label"] == factor_label]
            assert len(hits) == 1 and hits[0]["strictly_separated"]
            lower, _ = endpoints(hits[0]["modulus"])
            assert lower > 0
            product_lower *= lower**factor["power"]
            factor_bounds.append({"polynomial_id": name, "degree": factor["degree"],
                                  "power": factor["power"], "modulus_lower_rational": str(lower)})
        assert product_lower == expected_product_bounds[beta]
        results[beta] = {
            "status": "excluded by saved B imaginary sign",
            "shape_imaginary_lower_rational": str(imag_lo),
            "shape_imaginary_upper_rational": str(imag_hi),
            "necessary_actual_sign": "strictly negative",
            "original_diagnostic_status_unchanged": original["status"],
            "original_diagnostic_reason_unchanged": original["reason"],
            "failed_radial_guard_rectangle_modulus_lower_rational": str(coordinate_lower),
            "failed_radial_guard_factor_product_modulus_lower_rational": str(product_lower),
            "denominator_factors": factor_bounds,
            "guard_failure_is_not_a_zero_or_rectangle_zero": True,
        }
    for name, expected in bindings.items():
        assert sha(ROOT/name) == expected, name
    record = {
        "status": "both inherited-box prefix alternatives excluded",
        "alpha": 1, "beta_candidates": [0, 1], "tested_address": data["tested_address"],
        "tested_box": data["tested_box"], "results_by_beta": results,
        "method": "exact rational comparisons and products of existing serialized endpoints",
        "original_diagnostic_statuses_modified": False, "replacement_box_selected": False,
        "reference_reevaluations": 0, "polynomial_reevaluations": 0,
        "primitive_evaluations": 0, "source_root_evaluations": 0,
        "scalar_budget_evaluations": 0, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "result_sha256": sha(args.output),
                     "bindings": len(bindings), "positive_B_imaginary_lower_endpoints": {
                         beta: row["shape_imaginary_lower_rational"] for beta, row in results.items()}}))


if __name__ == "__main__":
    main()
