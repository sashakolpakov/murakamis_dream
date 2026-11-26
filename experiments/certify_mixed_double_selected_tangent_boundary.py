#!/usr/bin/env python3
"""Evaluate prescribed double-selection tangent bounds on saved references.

Use --diagnostic for the eight previously prescribed reference boxes.
Without it, visit the entire saved boundary bank once. No source roots,
parameter subdivisions, or automatic retries are performed.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize
from flint import ctx

import diagnose_mixed_double_selected_profiles as proposal
import evaluate_mixed_double_selected_tangent as evaluator

ROOT = Path(__file__).resolve().parents[1]
BANK = "repro/results/research-mixed-second-selected-boundary-reference-bank.json"
PROPOSALS = "repro/diagnostics/research-mixed-double-selected-profiles-attempt01.json"
EXPECTED_BANK = "3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb"


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def check_partition(bank):
    trees = defaultdict(list)
    for row in bank["terminal_geometry"]:
        trees[(row["beta"], row["chart"])].append(row["address"])
    if len(trees) != 18:
        raise ValueError("missing boundary charts")
    for addresses in trees.values():
        ordered = sorted(addresses)
        if any(set(a)-set("01") for a in ordered):
            raise ValueError("invalid boundary address")
        if any(b.startswith(a) for a, b in zip(ordered, ordered[1:])):
            raise ValueError("overlapping boundary leaves")
        if sum((F(1, 2**len(a)) for a in ordered), F(0)) != 1:
            raise ValueError("incomplete boundary partition")
    if len(bank["accepted_references"]) != 1431 or len(bank["terminal_geometry"]) != 1545:
        raise ValueError("unexpected saved bank inventory")
    return {str(k): len(v) for k, v in trees.items()}


def propose(row, cap_kind, right_kind, nu1, nu2):
    r = np.array([proposal.coordinate(row["coordinates"][name]) for name in evaluator.NAMES])
    box = evaluator.target_box(row["beta"], cap_kind, right_kind)
    float_box = [(float(lo), float(hi)) for lo, hi in box]
    x0 = np.clip(r.real, [lo for lo, hi in float_box], [hi for lo, hi in float_box])
    opt = minimize(proposal.objective, x0,
                   args=(r, row["beta"], cap_kind, right_kind, nu1, nu2),
                   jac=True, bounds=float_box, method="L-BFGS-B",
                   options={"ftol": 1e-13, "gtol": 1e-9, "maxiter": 100, "maxls": 40})
    if not np.isfinite(opt.x).all():
        raise ValueError("nonfinite trial proposal")
    # Exact clipping only ensures that the arbitrary rational trial is legal.
    trial = [str(min(hi, max(lo, F(format(float(x), ".12f")))))
             for x, (lo, hi) in zip(opt.x, box)]
    metadata = {"success": bool(opt.success), "message": str(opt.message),
                "iterations": int(opt.nit), "evaluations": int(opt.nfev),
                "candidate_value_display_only": float(-opt.fun)}
    return trial, metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostic", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if sha(ROOT/BANK) != EXPECTED_BANK:
        raise ValueError("changed reference bank")
    bank = json.loads((ROOT/BANK).read_text())
    partition = check_partition(bank)
    paths = [
        BANK, "experiments/diagnose_mixed_double_selected_profiles.py",
        "experiments/evaluate_mixed_double_selected_tangent.py",
        str(Path(__file__).resolve().relative_to(ROOT)),
        "notes/research_mixed_double_selected_last_rows.md",
        "notes/research_mixed_first_cap_plateau_phase.md",
        "notes/research_mixed_second_selected_horizontal_concavity.md",
        "notes/research_mixed_stationary_reference_boundary_extension.md",
        "notes/research_mixed_double_selected_concave_profile_budget.md",
        "notes/research_mixed_double_selected_boundary_extension.md",
    ]
    inputs = dict(bank["input_sha256"])
    for path, digest in inputs.items():
        if sha(ROOT/path) != digest:
            raise ValueError("changed inherited reference dependency: "+path)
    for path in paths:
        digest = sha(ROOT/path)
        if path in inputs and inputs[path] != digest:
            raise ValueError("conflicting reference dependency: "+path)
        inputs[path] = digest
    rows = bank["accepted_references"]
    diagnostic_trials = {}
    if args.diagnostic:
        prior = json.loads((ROOT/PROPOSALS).read_text())
        inputs[PROPOSALS] = sha(ROOT/PROPOSALS)
        wanted = [r["source_node_index"] for r in prior["references"]]
        lookup = {r["source_node_index"]: r for r in rows}
        rows = [lookup[i] for i in wanted]
        for r in prior["references"]:
            for p in r["profiles"]:
                key = (r["source_node_index"], p["cap"], p["right"], p["nu1"], p["nu2"])
                diagnostic_trials[key] = [format(float(x), ".12f") for x in p["candidate_targets"]]
    ctx.prec = 192
    start = time.monotonic()
    results, unresolved = [], []
    counts = Counter()
    for index, row in enumerate(rows):
        result = {
            "source_node_index": row["source_node_index"], "beta": row["beta"],
            "external_domain": row["external_domain"], "chart": row["chart"], "address": row["address"],
            "source_payload_sha256": row["compact_payload_canonical_sha256"],
            "right_response": row["response"]["details"]["right_product_modulus"],
            "profiles": [],
        }
        for cap_kind, right_kind, nu1, nu2 in itertools.product(
                ("main", "left"), ("main", "half") if row["beta"] == 0 else ("main",), (0, 1), (0, 1)):
            key = (row["source_node_index"], cap_kind, right_kind, nu1, nu2)
            try:
                if args.diagnostic:
                    trial, metadata = diagnostic_trials[key], {"mode": "prescribed saved trial"}
                else:
                    trial, metadata = propose(row, cap_kind, right_kind, nu1, nu2)
                    counts["optimizer_not_successful"] += int(not metadata["success"])
                value = evaluator.evaluate(row, cap_kind, right_kind, nu1, nu2, trial)
                value["proposal"] = metadata
                result["profiles"].append(value)
                counts["finite_bounds"] += 1
                counts["strict_negative_bounds"] += int(F(value["upper_rational"]) < 0)
                counts.update(value["primitive_calls"])
            except Exception as error:
                item = {"profile_key": list(key), "error_type": type(error).__name__, "error": str(error)}
                unresolved.append(item)
                result["profiles"].append({"status": "unresolved", **item})
        results.append(result)
        if (index+1) % 100 == 0:
            print(json.dumps({"references_done": index+1, "total": len(rows),
                              "finite_bounds": counts["finite_bounds"], "unresolved": len(unresolved),
                              "elapsed_seconds": time.monotonic()-start}), flush=True)
    summaries = []
    for beta, domain in itertools.product((0, 1), ("k3", "k4")):
        group = [r for r in results if (r["beta"], r["external_domain"]) == (beta, domain)]
        uppers = [F(p["upper_rational"]) for r in group for p in r["profiles"] if "upper_rational" in p]
        response = max(F(r["right_response"]["upper_rational"]) for r in group)
        factor = F(6889, 2000000) if domain == "k3" else F(9, 5000)
        maximum = max(uppers) if uppers else None
        summaries.append({
            "beta": beta, "domain": domain, "reference_count": len(group),
            "boundary_upper_rational": str(maximum) if maximum is not None else None,
            "response_upper_rational": str(response), "barrier_factor_rational": str(factor),
            "corrected_upper_rational": str(maximum+factor*response) if maximum is not None else None,
            "corrected_upper_decimal_display": float(maximum+factor*response) if maximum is not None else None,
        })
    changed = [path for path, digest in inputs.items() if sha(ROOT/path) != digest]
    strict = not unresolved and not changed and all(F(s["corrected_upper_rational"]) < 0 for s in summaries)
    result = {
        "status": ("diagnostic subset only" if args.diagnostic else "complete saved-boundary evaluation"),
        "diagnostic": args.diagnostic, "precision_bits": 192, "input_sha256": inputs,
        "reference_count": len(rows), "full_bank_partition": partition,
        "strict_corrected_bounds_on_evaluated_references": strict,
        "new_source_roots": 0, "parameter_subdivisions": 0, "finite_quantum_sums": 0,
        "counts": dict(counts), "unresolved": unresolved, "changed_inputs": changed,
        "summaries": summaries, "references": results, "elapsed_seconds": time.monotonic()-start,
        "scope": "Concavity and boundary extension are separate written premises; trials require no optimizer proof.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    opener = gzip.open if args.output.suffix == ".gz" else open
    with opener(args.output, "wt") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "strict": strict, "changed": changed,
                      "counts": dict(counts), "summaries": summaries}), flush=True)


if __name__ == "__main__":
    main()
