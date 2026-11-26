#!/usr/bin/env python3
"""Two fixed scalar budgets from already certified canonical coordinates.

The external coordinate is exactly 1/3 and beta is exactly 0, then 1.
No root, residual, rational transport, alternate input or refinement.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "repro/results/research-mixed-second-selected-canonical-reference.json"
OLD = "experiments/diagnose_mixed_second_selected_central_budget.py"
IMPROVED = "experiments/evaluate_mixed_second_selected_curvature_budget.py"
PINNED = {
    CANONICAL: "5c9fe5c7cddc01fce993818ccde45005e10b768dae20dab8f37ce03ab3781ff8",
    OLD: "fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce",
    IMPROVED: "9adc88e0c1cdf912574c6dc767d4b31f5bd88ba398446f77a7510cc90982e228",
    "notes/research_mixed_second_selected_curvature_evaluation.md": "db6931fee465f99623b9f75838c3e0b7ea6dbb684544de8f3e821a2ef33cbe2e",
    "notes/research_mixed_second_selected_canonical_budget_evaluation.md": "5a8d9c9293a16d487688c6718395e0224027e9867a4577a84b5f807b5f0034c1",
}
NAMES = ("e", "xi", "a", "u", "z", "v", "b", "c")
NEGATIVE_NAMES = ("e", "a", "u", "z", "v", "b", "c")
GAP = F(1, 2000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def merge(bindings, source):
    for name, expected in source.items():
        path = Path(name)
        relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
        if relative in bindings and bindings[relative] != expected:
            raise ValueError("conflicting input binding: "+relative)
        bindings[relative] = expected


def verify(bindings):
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("frozen canonical-budget input mismatch: "+name)


def literal_pins(name):
    """Read only literal constant names and PINNED; do not import the file."""
    constants = {}
    for node in ast.parse((ROOT/name).read_text()).body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        key = node.targets[0].id
        if isinstance(node.value, ast.Constant):
            constants[key] = node.value.value
        if key == "PINNED":
            if not isinstance(node.value, ast.Dict):
                raise ValueError("provider pins are not a static dictionary")
            return {(constants[k.id] if isinstance(k, ast.Name) else ast.literal_eval(k)): ast.literal_eval(v)
                    for k, v in zip(node.value.keys, node.value.values)}
    raise ValueError("missing provider pins: "+name)


def load_inputs():
    bindings = dict(PINNED)
    verify(bindings)
    data = json.loads((ROOT/CANONICAL).read_text())
    if (data["status"] != "both prescribed canonical prefixes localized"
            or data["outside_coordinate"] != ["1/3", "0"]
            or data["precision_bits"] != 256 or len(data["input_sha256"]) != 29
            or [row["beta"] for row in data["cases"]] != [0, 1]):
        raise ValueError("canonical record inventory/status mismatch")
    merge(bindings, data["input_sha256"])
    merge(bindings, literal_pins(OLD))
    merge(bindings, literal_pins(IMPROVED))
    verify(bindings)
    # This frozen module imports no repository provider on import. Its
    # metadata-only verifier checks the full primitive/helper dependency tree.
    old = importlib.import_module("diagnose_mixed_second_selected_central_budget")
    if Path(old.__file__).resolve() != (ROOT/OLD).resolve():
        raise ValueError("unexpected original-evaluator module location")
    inherited, _ = old.verified_inputs()
    merge(bindings, inherited)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)
    four = importlib.import_module("diagnose_mixed_four_four_half_row_budget")
    improved = importlib.import_module("evaluate_mixed_second_selected_curvature_budget")
    if Path(improved.__file__).resolve() != (ROOT/IMPROVED).resolve():
        raise ValueError("unexpected curvature-wrapper module location")
    for row in data["cases"]:
        if row["alpha"] != 1 or row["status"] != "canonical prefix localized" or row["strict_residual_test"] is not True:
            raise ValueError("canonical localization certificate missing")
        coords = row["coordinate_enclosures"]
        if set(coords) != set(NAMES):
            raise ValueError("wrong canonical coordinate names")
        for axis, expected in (("real", F(1, 3)), ("imag", F(0))):
            if {F(coords["c"][axis][side+"_rational"]) for side in ("lower", "upper")} != {expected}:
                raise ValueError("external canonical input changed")
    return data, old, four, improved, bindings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    data, old, four, improved, bindings = load_inputs()
    def forbidden(*args, **kwargs):
        raise RuntimeError("old source/reference/transport/inspection callback forbidden")
    for provider in (old, four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = provider.reference = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = old.Evaluator.transfer = forbidden
    four.reference_four = four.BASE.rational_enclosure = four.BASE.split = forbidden
    # Do not import the canonical certifier or any rational-transport driver.
    ctx.prec = 256
    Primitive = old.make_primitive_class(four)
    totals = Counter()
    cases = []
    started = time.monotonic()
    for beta in (0, 1):
        source = data["cases"][beta]
        case = {"alpha": 1, "beta": beta, "source_case_canonical_sha256": canonical_hash(source),
                "source_coordinate_enclosures_unchanged": source["coordinate_enclosures"],
                "canonical_prefix_existence_supplied_by_input": True,
                "suffix_realization_claimed": False,
                "input_coordinates": {}, "input_negative_shapes": {}, "outward_reconstruction_checks": []}
        primitive = Primitive()
        evaluator = old.Evaluator(four, primitive)
        counts = Counter()
        coordinates, shapes = {}, {}
        try:
            for name in NAMES:
                values = {}
                for axis in ("real", "imag"):
                    saved = source["coordinate_enclosures"][name][axis]
                    lo, hi = F(saved["lower_rational"]), F(saved["upper_rational"])
                    if lo > hi:
                        raise ValueError("reversed canonical input interval")
                    value = four.frozen.interval(lo, hi)
                    counts["coordinate_interval_reconstructions"] += 1
                    if not value.is_finite() or four.frozen.lower(value) > lo or four.frozen.upper(value) < hi:
                        raise ValueError("outward canonical interval reconstruction failed")
                    values[axis] = value
                    case["outward_reconstruction_checks"].append({"coordinate": name, "axis": axis,
                        "saved_lower_rational": str(lo), "saved_upper_rational": str(hi),
                        "reconstructed_interval": four.frozen.real_record(value), "contains_saved_interval": True})
                coordinates[name] = acb(values["real"], values["imag"])
                case["input_coordinates"][name] = four.frozen.complex_record(coordinates[name])
            for name in NEGATIVE_NAMES:
                counts["negative_shape_exponentials"] += 1
                shape = (-2*primitive.pi*primitive.ii*coordinates[name]).exp()
                if not shape.is_finite():
                    raise four.frozen.Inconclusive("nonfinite canonical negative shape: "+name)
                shapes[name] = shape
                case["input_negative_shapes"][name] = four.frozen.complex_record(shape)
            counts["improved_wrapper_calls"] += 1
            result = improved.evaluate_reference(evaluator, shapes, coordinates, beta, GAP)
            case["improved_result"] = result
            case["original_result"] = result["details"]["frozen_result"]
            case["status"] = result["status"]
            if result.get("frozen_helper_calls") != 1:
                raise RuntimeError("wrapper did not make exactly one frozen-helper call")
        except Exception as error:
            case["status"] = "arithmetic or callback failure"
            case["error"] = repr(error)
        finally:
            combined = counts+evaluator.counts+primitive.counts
            case["call_counts"] = dict(combined)
            totals.update(combined)
        if (combined["improved_wrapper_calls"] > 1 or combined["directional_reference_attempts"] > 1
                or combined["directional_branch_attempts"] > 2 or combined["node_conjugates"] > 3
                or combined["edge_conjugates"] != 0 or combined["centered_primitive_calls"] > 12
                or combined["coordinate_interval_reconstructions"] > 16
                or combined["negative_shape_exponentials"] > 7):
            case["status"] = "callback count violation"
        cases.append(case)
        print(json.dumps({"beta": beta, "status": case["status"], "call_counts": case["call_counts"],
            "fully_evaluated_pair": case.get("improved_result", {}).get("fully_evaluated_pair", False)}), flush=True)
    verify(bindings)
    result = {"status": "both prescribed canonical budget cases processed", "alpha": 1,
        "beta_candidates": [0, 1], "external_coordinate_exact": ["1/3", "0"],
        "canonical_record": CANONICAL, "canonical_record_sha256": PINNED[CANONICAL],
        "precision_bits": 256, "candidate_gap_rational": str(GAP), "cases": cases,
        "call_counts": dict(totals), "canonical_prefix_existence_supplied_by_input": True,
        "reference_or_residual_reevaluations": 0, "rational_transport_evaluations": 0,
        "source_root_evaluations": 0, "finite_source_evaluations": 0,
        "alternate_external_inputs": 0, "parameter_subdivisions": 0, "automatic_retries": 0,
        "old_inspect_calls": 0, "old_main_calls": 0,
        "suffix_realization_claimed": False, "uniform_parameter_bound_claimed": False,
        "half_row_bound_claimed": False, "finite_source_theorem_claimed": False,
        "global_filling_volume_theorem_claimed": False,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "result_sha256": sha(args.output),
        "case_statuses": {str(row["beta"]): row["status"] for row in cases},
        "call_counts": dict(totals), "bindings": len(bindings)}))


if __name__ == "__main__":
    main()
