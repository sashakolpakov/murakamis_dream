#!/usr/bin/env python3
"""One bounded full-domain attempt for the two cap-left/main scalar bounds.

Uses exactly the frozen one-box diagnostic inspect() and CenteredPrimitives.
Stops at the first depth-limit failure or after at most 8000 visits.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
DIAGNOSTIC = REPO/"repro/results/research-mixed-cap-left-main-budget-diagnostic.json"
DIAGNOSTIC_SHA = "0473506e898bff5113edc4f4e721cdbe9489db8e0071be633788edc12dc89c56"
EVALUATOR = REPO/"experiments/diagnose_mixed_cap_left_main_budget.py"
EVALUATOR_SHA = "c044109d836617e32bfeb938aef3e9945de974bdd8c67da04e189eb99800a5b6"
PROOF = REPO/"notes/research_mixed_selected_cap_left_main_scalar_certificate.md"
PROOF_SHA = "1784b360197ec831113916b1cc6c2c51739004a296bf13dfd936793d0d30a4c1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-cells", type=int, default=8000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 8000:
        parser.error("one bounded attempt permits at most8000 visits")
    for path, expected in ((DIAGNOSTIC, DIAGNOSTIC_SHA),
                           (EVALUATOR, EVALUATOR_SHA), (PROOF, PROOF_SHA)):
        if digest(path) != expected:
            raise ValueError("frozen input hash mismatch: "+str(path))
    diagnostic = json.loads(DIAGNOSTIC.read_text())
    if diagnostic["precision_bits"] != 160 or diagnostic["candidate_gap"] != "1/2000":
        raise ValueError("unexpected diagnostic precision or target")
    bindings = dict(diagnostic["input_sha256"])
    for path in (DIAGNOSTIC, PROOF, Path(__file__).resolve()):
        bindings[str(path.relative_to(REPO))] = digest(path)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)

    # The exact reviewed evaluator is imported only after validating its
    # bytes and dependencies. Its old one-box main() is never called.
    import diagnose_mixed_cap_left_main_budget as scalar
    from flint import ctx
    if Path(scalar.__file__).resolve() != EVALUATOR:
        raise ValueError("unexpected diagnostic module path")
    if scalar.GAP != F(1, 2000):
        raise ValueError("unexpected evaluator target gap")
    ctx.prec = 160
    primitive = scalar.CenteredPrimitives()
    base, keys = scalar.frozen.base, scalar.KEYS
    started = time.monotonic()
    stack = [("", base.ROOT)]
    leaves, unresolved, counts, visited = [], [], Counter(), 0
    depth_failure = False
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, details = scalar.inspect(box, primitive)
        visited += 1
        if kind in ("accepted", "excluded"):
            counts[kind] += 1
            item = {"address": address, "status": kind, "reason": reason}
            if kind == "accepted":
                for key in keys:
                    bound = F(details["majorants"][key]["value"]["upper_rational"])
                    if not bound < -scalar.GAP:
                        raise RuntimeError("accepted rational endpoint is not strict")
                item["certificate"] = details
            leaves.append(item)
        elif kind == "split" and len(address) >= 20:
            unresolved.append({"address": address, "box": list(map(str, box)),
                               "reason": reason, "enclosures": details})
            depth_failure = True
            break
        elif kind == "split":
            children = base.split(box, len(address))
            stack.extend([(address+"1", children[1]), (address+"0", children[0])])
        else:
            raise RuntimeError("unexpected evaluator state: "+str(kind))
        if visited % 500 == 0:
            print(json.dumps({"visited": visited, "terminal_counts": dict(counts),
                              "pending": len(stack)}), flush=True)

    stop_reason = ("first depth-limit failure" if depth_failure else
                   "cell budget" if stack else "complete root partition")
    unresolved.extend({"address": address, "box": list(map(str, box)),
                       "reason": stop_reason+"; box not inspected",
                       "enclosures": None} for address, box in stack)
    scalar.frozen.verify_partition(leaves, unresolved)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during attempt: "+name)
    maxima = {}
    for key in keys:
        values = [F(item["certificate"]["majorants"][key]["value"]["upper_rational"])
                  for item in leaves if item["status"] == "accepted"]
        maxima[key] = str(max(values)) if values else None
    record = {
        "status": "proved" if not unresolved else "unresolved",
        "scope": "Two corrected cap-left/ordinary-main scalar majorants only",
        "precision_bits": 160, "height": str(scalar.frozen.H),
        "gap": str(scalar.GAP), "independent_tests": list(keys),
        "initial_auxiliary_rectangle": list(map(str, base.ROOT)),
        "necessary_reference_ranges": base.RANGES,
        "reference_filters": "unchanged frozen half-row reference()",
        "primitive": "unchanged reviewed diagnostic CenteredPrimitives",
        "index_curvature": "exact rational lower2*pi*min(Re cot(pi*s*),15/53)",
        "incoming_curvature": "exact rational lower(23+18*nu)*pi/120",
        "one_sided_index_gain": True, "outgoing_gradient_exact": "0",
        "visited_cells": visited, "inspect_calls": visited,
        "frozen_half_row_inspect_calls": 0,
        "terminal_counts": dict(counts), "unresolved_count": len(unresolved),
        "unresolved_dyadic_fraction": str(sum(
            (F(1, 2**len(item["address"])) for item in unresolved), F(0))),
        "stop_reason": stop_reason, "first_depth_failure_stops": True,
        "max_cells": args.max_cells, "max_depth": 20,
        "split_rule": "alternate real/imaginary dyadic subdivision, real first",
        "terminal_partition_verified": True,
        "accepted_maximum_upper_rational": maxima,
        "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings, "leaves": leaves, "unresolved": unresolved,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({key: record[key] for key in
                     ("status", "visited_cells", "terminal_counts", "unresolved_count",
                      "unresolved_dyadic_fraction", "stop_reason", "elapsed_seconds")}),
          flush=True)


if __name__ == "__main__":
    main()
