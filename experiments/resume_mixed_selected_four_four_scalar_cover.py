#!/usr/bin/env python3
"""One pending-only continuation of the frozen ten-test next-four cover.

Preserve all3997 terminal leaves and inspect only descendants of the exact
seven pending boxes. No fresh start or old terminal-leaf evaluation exists.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import signal
import time


REPO = Path(__file__).resolve().parents[1]
PARENT = "repro/results/research-mixed-selected-four-four-scalar-cover-attempt01.json"
PARENT_SHA = "07ed9c2f056f1e5ddc133212c5639a49fe63e1bd43a65773a4b9b28715ef5f4a"
PROOF = "notes/research_mixed_selected_four_four_scalar_continuation.md"
PROOF_SHA = "2fbac323112a925093103e03dc1c7039a1daea7f79fd7d9693e993e303a431dd"
ORIGINAL = "experiments/certify_mixed_selected_four_four_scalar_cover.py"
ORIGINAL_SHA = "eda358d412eab159b8bcbdc447338e3d4cc11abcb6054b441a8e7985467d3bd0"
FRONTIER = ("11", "101", "10011", "1001011", "10010101111",
            "100101011101", "10010101110011")
PREFIX_COUNT = 3997


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def load_inputs(input_path):
    if input_path.resolve() != REPO/PARENT or digest(input_path) != PARENT_SHA:
        raise ValueError("only the exact pinned attempt01 may be continued")
    previous = json.loads(input_path.read_text())
    if (previous["status"] != "unresolved" or previous["stop_reason"] != "cell budget"
            or previous["precision_bits"] != 160 or previous["height"] != "1/100"
            or previous["upper_gap"] != "1/2000" or previous["corner_threshold"] != "0"
            or previous["max_depth"] != 20 or previous["visited_cells"] != 8000):
        raise ValueError("unexpected pinned parent scope")
    if (len(previous["leaves"]) != PREFIX_COUNT
            or previous["terminal_counts"] != {"accepted": 1454, "excluded": 2543}
            or tuple(item["address"] for item in previous["unresolved"]) != FRONTIER
            or any(item["inspected"] or item["enclosures"] is not None
                   for item in previous["unresolved"])):
        raise ValueError("unexpected immutable prefix or pending order")
    bindings = dict(previous["input_sha256"])
    additions = {PARENT: PARENT_SHA, PROOF: PROOF_SHA, ORIGINAL: ORIGINAL_SHA,
                 str(Path(__file__).resolve().relative_to(REPO)): digest(Path(__file__))}
    for name, expected in additions.items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting inherited binding: "+name)
        bindings[name] = expected
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)
    return previous, bindings


def check_descendant(address):
    if sum(address.startswith(root) for root in FRONTIER) != 1:
        raise ValueError("new address is outside the seven pending roots")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=REPO/PARENT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-cells", type=int, default=8000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 8000:
        parser.error("this continuation permits at most8000 additional visits")
    previous, bindings = load_inputs(args.input)
    prefix_hash = canonical_digest(previous["leaves"])

    # Only the control helper is imported first. All arithmetic bytes and
    # their complete dependency graph have already been validated above.
    import certify_mixed_selected_four_four_scalar_cover as original
    if Path(original.__file__).resolve() != REPO/ORIGINAL:
        raise ValueError("unexpected original combined-wrapper module")
    original.verify_partition(previous["leaves"], previous["unresolved"])
    if list(map(str, original.ROOT)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original root rectangle changed")
    if tuple(previous["upper_tests"]) != original.UPPER_KEYS or tuple(
            previous["lower_tests"]) != original.LOWER_KEYS:
        raise ValueError("original ten-test inventory changed")

    import diagnose_mixed_four_four_half_row_budget as half
    import diagnose_mixed_four_four_left_main_budget as left
    import diagnose_mixed_four_left_row_corners as corners
    from flint import ctx
    for module, name in ((half, original.HALF), (left, original.LEFT),
                         (corners, original.CORNERS)):
        if Path(module.__file__).resolve() != REPO/name:
            raise ValueError("unexpected scalar provider module: "+name)
    if (half.H != original.H or left.H != original.H
            or half.GAP != original.GAP or left.GAP != original.GAP
            or half.BASE.ROOT != original.ROOT):
        raise ValueError("original scalar scope changed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("old scalar inspections are forbidden")

    half.frozen.inspect = half.maps_four.inspect = half.BASE.inspect = forbidden
    # Preserve the serialized stack order, bottom to top. Never seed ROOT.
    stack = [(item["address"], tuple(map(F, item["box"])))
             for item in previous["unresolved"]]
    initial_pending = [{"address": address, "box": list(map(str, box))}
                       for address, box in stack]
    for address, box in stack:
        check_descendant(address)
        if box != original.address_box(address):
            raise ValueError("saved frontier box does not match its address")
    if sum((F(1, 2**len(address)) for address, _ in stack), F(0)) != F(6797, 16384):
        raise ValueError("saved frontier mass changed")

    requested_stop = []

    def request_stop(signum, frame):
        requested_stop.append(signum)

    previous_handlers = {sig: signal.signal(sig, request_stop)
                         for sig in (signal.SIGINT, signal.SIGTERM)}
    ctx.prec = 160
    started = time.monotonic()
    leaves = list(previous["leaves"])
    counts = Counter(previous["terminal_counts"])
    new_counts, callback_counts = Counter(), Counter()
    new_visits, new_refinements = 0, 0
    stop_reason, active_failure = None, None
    try:
        try:
            primitive = half.CenteredPrimitives()
        except Exception as error:
            stop_reason = "primitive initialization failed"
            active_failure = (stack[-1][0], type(error).__name__+": "+str(error), {})
        while stack and new_visits < args.max_cells and stop_reason is None:
            if requested_stop:
                stop_reason = "interruption requested"
                break
            address, box = stack[-1]
            check_descendant(address)
            new_visits += 1
            state, reason, details = original.inspect_combined(
                box, primitive, half, left, corners, callback_counts)
            if state in ("accepted", "excluded"):
                item = {"address": address, "box": list(map(str, box)),
                        "status": state, "reason": reason, "certificate": details}
                stack.pop()
                leaves.append(item)
                counts[state] += 1
                new_counts[state] += 1
            elif state == "error":
                active_failure = (address, reason, details)
                stop_reason = "arithmetic or callback error"
                break
            elif len(address) >= 20:
                active_failure = (address, reason, details)
                stop_reason = "first depth-limit failure"
                break
            else:
                children = original.split(box, len(address))
                stack.pop()
                stack.extend(((address+"1", children[1]), (address+"0", children[0])))
                new_refinements += 1
            if new_visits % 500 == 0:
                print(json.dumps({"new_visits": new_visits,
                                  "new_terminal_counts": dict(new_counts),
                                  "pending": len(stack)}), flush=True)
        if stop_reason is None:
            stop_reason = "cell budget" if stack else "complete pending partition"
        unresolved = []
        for address, box in stack:
            check_descendant(address)
            inspected = active_failure is not None and active_failure[0] == address
            unresolved.append({
                "address": address, "box": list(map(str, box)),
                "reason": active_failure[1] if inspected else stop_reason+"; box uninspected",
                "inspected": inspected,
                "enclosures": active_failure[2] if inspected else None,
            })
        if (leaves[:PREFIX_COUNT] != previous["leaves"]
                or canonical_digest(leaves[:PREFIX_COUNT]) != prefix_hash):
            raise ValueError("immutable terminal prefix changed")
        for item in leaves[PREFIX_COUNT:]:
            check_descendant(item["address"])
        original.verify_partition(leaves, unresolved)
        original.verify_bindings(bindings)
        accepted = [leaf for leaf in leaves if leaf["status"] == "accepted"]
        worst_upper = {key: str(max(F(leaf["certificate"]["tests"][key]["endpoint_rational"])
                                    for leaf in accepted)) if accepted else None
                       for key in original.UPPER_KEYS}
        worst_lower = {key: str(min(F(leaf["certificate"]["tests"][key]["endpoint_rational"])
                                    for leaf in accepted)) if accepted else None
                       for key in original.LOWER_KEYS}
        masses = {state: str(sum((F(1, 2**len(leaf["address"])) for leaf in leaves
                                  if leaf["status"] == state), F(0)))
                  for state in ("accepted", "excluded")}
        masses["unresolved"] = str(sum((F(1, 2**len(item["address"]))
                                        for item in unresolved), F(0)))
        total_callbacks = Counter(previous["callback_inspect_calls"])+callback_counts
        record = {
            "status": "proved" if not unresolved else "unresolved",
            "scope": previous["scope"], "precision_bits": 160,
            "height": str(original.H), "upper_gap": str(original.GAP),
            "corner_threshold": "0", "upper_tests": list(original.UPPER_KEYS),
            "lower_tests": list(original.LOWER_KEYS),
            "initial_auxiliary_rectangle": list(map(str, original.ROOT)),
            "necessary_reference_ranges": previous["necessary_reference_ranges"],
            "reference": previous["reference"], "primitive": previous["primitive"],
            "visited_cells": previous["visited_cells"]+new_visits,
            "combined_inspect_calls": previous["combined_inspect_calls"]+new_visits,
            "callback_inspect_calls": dict(total_callbacks),
            "refinements": previous["refinements"]+new_refinements,
            "terminal_counts": dict(counts), "unresolved_count": len(unresolved),
            "dyadic_fractions": masses, "stop_reason": stop_reason,
            "requested_signals": requested_stop, "first_depth_failure_stops": True,
            "max_depth": 20, "split_rule": previous["split_rule"],
            "terminal_partition_verified": True,
            "accepted_maximum_upper_rational": worst_upper,
            "accepted_minimum_lower_rational": worst_lower,
            "previous_record": PARENT, "previous_record_sha256": PARENT_SHA,
            "previous_terminal_count": PREFIX_COUNT,
            "original_leaves_canonical_sha256": prefix_hash,
            "original_leaves_preserved_count": PREFIX_COUNT,
            "continuation_initial_pending": initial_pending,
            "continuation_initial_pending_dyadic_fraction": "6797/16384",
            "continuation_max_cells": args.max_cells,
            "continuation_visited_cells": new_visits,
            "continuation_terminal_counts": dict(new_counts),
            "continuation_callback_inspect_calls": dict(callback_counts),
            "continuation_refinements": new_refinements,
            "old_terminal_leaf_inspect_calls": 0,
            "old_scalar_inspect_calls": 0, "root_proposals": 0,
            "finite_source_evaluations": 0, "automatic_retries": 0,
            "continuation_elapsed_seconds": time.monotonic()-started,
            "input_sha256": bindings, "leaves": leaves, "unresolved": unresolved,
        }
        original.atomic_new_record(args.output, record)
        print(json.dumps({key: record[key] for key in (
            "status", "continuation_visited_cells", "continuation_terminal_counts",
            "terminal_counts", "unresolved_count", "dyadic_fractions", "stop_reason",
            "continuation_elapsed_seconds")}), flush=True)
    finally:
        for sig, previous_handler in previous_handlers.items():
            signal.signal(sig, previous_handler)


if __name__ == "__main__":
    main()
