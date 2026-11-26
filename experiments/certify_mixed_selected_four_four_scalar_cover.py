#!/usr/bin/env python3
"""One bounded ten-test cover of the selected next-four reference domain.

The three reviewed scalar callbacks are unchanged. There are at most8000
visits at160bits/depth20, stopping on the first depth failure. Every stop
retains the exact pending partition; no prior cover is replayed.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import signal
import tempfile
import time


REPO = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_selected_four_four_scalar_cover.md"
HALF = "experiments/diagnose_mixed_four_four_half_row_budget.py"
LEFT = "experiments/diagnose_mixed_four_four_left_main_budget.py"
CORNERS = "experiments/diagnose_mixed_four_left_row_corners.py"
HALF_RECORD = "repro/results/research-mixed-four-four-half-row-budget-diagnostic.json"
LEFT_RECORD = "repro/results/research-mixed-four-four-left-main-budget-diagnostic.json"
CORNER_RECORD = "repro/results/research-mixed-four-left-row-corners-diagnostic.json"
H, GAP = F(1, 100), F(1, 2000)
ROOT = tuple(map(F, ("217/1000", "117/500", "27/1000", "9/200")))
UPPER_KEYS = ("halfrow.main_factorial", "halfrow.main_forced",
              "halfrow.left_factorial", "halfrow.left_forced",
              "leftmain.factorial", "leftmain.forced")
LOWER_KEYS = ("corners.22_22", "corners.22_45", "corners.45_22", "corners.45_45")
PINNED = {
    PROOF: "baccd427a5d41553cff0d41855ed26ecc8aea729fe5339ff41531b7776a4310c",
    HALF: "cc1d86c233ef74f343796b6ad64967ca8a86c8dd315546b1de7c440cd9f9f82f",
    LEFT: "17762b2054283e0be8f2443cb66ee55a333eca70a42c9a2e7169c4f57d3a1a66",
    CORNERS: "f23330e8f1f499258428b9d3fe65deede1d46faf7f01ac0b36a6a773c1b987d4",
    HALF_RECORD: "9fc41c47559efdf8466b15fd3950fd952a39169d536928faf53cf0b3a2bf54b6",
    LEFT_RECORD: "1b885b2f5b9b1928758ce19df3c702b6459fedd5f6721f985d5c728661422401",
    CORNER_RECORD: "1ab751f6e88c713ed07104f5a5b82bca53e35ad112e139f92eefc8f4634084ee",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bindings_before_import():
    """All helper/diagnostic bytes are checked before loading arithmetic."""
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if len(expected) != 64 or digest(REPO/name) != expected:
            raise ValueError("unready or changed pinned input: "+name)
    for record_name in (HALF_RECORD, LEFT_RECORD, CORNER_RECORD):
        record = json.loads((REPO/record_name).read_text())
        if record["precision_bits"] != 160 or F(record["height"]) != H:
            raise ValueError("diagnostic precision/height mismatch: "+record_name)
        if record["tested_boxes"] != 1 or record["subdivisions"] != 0:
            raise ValueError("unexpected diagnostic scope: "+record_name)
        for name, expected in record["input_sha256"].items():
            path = Path(name)
            relative = str((path if path.is_absolute() else REPO/path).relative_to(REPO))
            if relative in bindings and bindings[relative] != expected:
                raise ValueError("conflicting inherited binding: "+relative)
            bindings[relative] = expected
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    verify_bindings(bindings)
    return bindings


def verify_bindings(bindings):
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)


def split(box, depth):
    axis = 2*(depth % 2)
    midpoint = (box[axis]+box[axis+1])/2
    left, right = list(box), list(box)
    left[axis+1], right[axis] = midpoint, midpoint
    return tuple(left), tuple(right)


def address_box(address):
    box = ROOT
    for depth, branch in enumerate(address):
        if branch not in "01":
            raise ValueError("nonbinary partition address")
        box = split(box, depth)[int(branch)]
    return box


def verify_partition(leaves, unresolved):
    entries = leaves+unresolved
    addresses = sorted(item["address"] for item in entries)
    if len(set(addresses)) != len(addresses):
        raise ValueError("duplicate partition address")
    if any(b.startswith(a) for a, b in zip(addresses, addresses[1:])):
        raise ValueError("overlapping partition addresses")
    if sum((F(1, 2**len(a)) for a in addresses), F(0)) != 1:
        raise ValueError("incomplete dyadic partition")
    for item in entries:
        if list(map(str, address_box(item["address"]))) != item["box"]:
            raise ValueError("address/box mismatch")


def inspect_combined(box, primitive, half, left, corners, callback_counts):
    """Keep all frozen formulas; acceptance depends on exact endpoints."""
    groups, tests = {}, {}
    callbacks = (
        ("halfrow", lambda: half.inspect(box, primitive), "majorants",
         ("main_factorial", "main_forced", "left_factorial", "left_forced")),
        ("leftmain", lambda: left.inspect(box, primitive, half), "majorants",
         ("factorial", "forced")),
        ("corners", lambda: corners.inspect(box, primitive), "corners",
         ("22_22", "22_45", "45_22", "45_45")),
    )
    all_accepted = True
    for group, callback, field, keys in callbacks:
        try:
            callback_counts[group] += 1
            state, reason, details = callback()
            groups[group] = {"status": state, "reason": reason, "details": details}
            if state == "excluded":
                return "excluded", group+": "+reason, {"groups": groups}
            if state not in ("accepted", "split", "inconclusive"):
                raise ValueError("unexpected callback state: "+str(state))
            all_accepted = all_accepted and state == "accepted"
            values = details.get(field, {})
            for key in keys:
                value = values.get(key, {}).get("value")
                if value is None or not value.get("finite", False):
                    continue
                endpoint_name = "lower_rational" if group == "corners" else "upper_rational"
                endpoint = F(value[endpoint_name])
                passed = endpoint > 0 if group == "corners" else endpoint < -GAP
                tests[group+"."+key] = {
                    "direction": "lower>0" if group == "corners" else "upper<-1/2000",
                    "endpoint_rational": str(endpoint), "passed": passed,
                }
        except Exception as error:
            return "error", group+": "+type(error).__name__+": "+str(error), {
                "groups": groups, "tests": tests}
    expected = set(UPPER_KEYS+LOWER_KEYS)
    passed = set(tests) == expected and all(test["passed"] for test in tests.values())
    if all_accepted and not passed:
        return "error", "callback acceptance contradicts exact endpoint check", {
            "groups": groups, "tests": tests}
    details = {"groups": groups, "tests": tests}
    if all_accepted and passed:
        return "accepted", "all six upper and four lower strict tests", details
    return "inconclusive", "ten-test comparison not certified on this box", details


def atomic_new_record(path, record):
    """Install a complete new record atomically, with no overwrite."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix="."+path.name+".", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w") as output:
            json.dump(record, output, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.link(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-cells", type=int, default=8000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 8000:
        parser.error("one bounded attempt permits at most8000 visits")
    bindings = bindings_before_import()

    import diagnose_mixed_four_four_half_row_budget as half
    import diagnose_mixed_four_four_left_main_budget as left
    import diagnose_mixed_four_left_row_corners as corners
    from flint import ctx
    for module, name in ((half, HALF), (left, LEFT), (corners, CORNERS)):
        if Path(module.__file__).resolve() != REPO/name:
            raise ValueError("unexpected module path: "+name)
    if half.H != H or left.H != H or half.GAP != GAP or left.GAP != GAP:
        raise ValueError("reviewed height or upper gap changed")
    if half.BASE.ROOT != ROOT:
        raise ValueError("reviewed root rectangle changed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("old scalar inspections are forbidden")

    half.frozen.inspect = half.maps_four.inspect = half.BASE.inspect = forbidden
    requested_stop = []

    def request_stop(signum, frame):
        requested_stop.append(signum)

    previous_handlers = {sig: signal.signal(sig, request_stop)
                         for sig in (signal.SIGINT, signal.SIGTERM)}
    ctx.prec = 160
    started = time.monotonic()
    stack = [("", ROOT)]
    leaves, counts, callback_counts = [], Counter(), Counter()
    visited, refinements = 0, 0
    active_failure = None
    stop_reason = None
    try:
        try:
            primitive = half.CenteredPrimitives()
        except Exception as error:
            stop_reason = "primitive initialization failed"
            active_failure = ("", type(error).__name__+": "+str(error), {})
        while stack and visited < args.max_cells and stop_reason is None:
            if requested_stop:
                stop_reason = "interruption requested"
                break
            # Peek, do not pop: a failed or interrupted evaluation remains
            # an exact unresolved part of the pending partition.
            address, box = stack[-1]
            visited += 1
            state, reason, details = inspect_combined(
                box, primitive, half, left, corners, callback_counts)
            if state in ("accepted", "excluded"):
                item = {"address": address, "box": list(map(str, box)),
                        "status": state, "reason": reason, "certificate": details}
                stack.pop()
                leaves.append(item)
                counts[state] += 1
            elif state == "error":
                active_failure = (address, reason, details)
                stop_reason = "arithmetic or callback error"
                break
            elif len(address) >= 20:
                active_failure = (address, reason, details)
                stop_reason = "first depth-limit failure"
                break
            else:
                children = split(box, len(address))
                stack.pop()
                stack.extend(((address+"1", children[1]), (address+"0", children[0])))
                refinements += 1
            if visited % 500 == 0:
                print(json.dumps({"visited": visited, "terminal_counts": dict(counts),
                                  "pending": len(stack)}), flush=True)
        if stop_reason is None:
            stop_reason = "cell budget" if stack else "complete root partition"
        unresolved = []
        for address, box in stack:
            inspected = active_failure is not None and active_failure[0] == address
            unresolved.append({
                "address": address, "box": list(map(str, box)),
                "reason": active_failure[1] if inspected else stop_reason+"; box uninspected",
                "inspected": inspected,
                "enclosures": active_failure[2] if inspected else None,
            })
        verify_partition(leaves, unresolved)
        verify_bindings(bindings)
        accepted = [leaf for leaf in leaves if leaf["status"] == "accepted"]
        worst_upper = {key: str(max(F(leaf["certificate"]["tests"][key]["endpoint_rational"])
                                    for leaf in accepted)) if accepted else None
                       for key in UPPER_KEYS}
        worst_lower = {key: str(min(F(leaf["certificate"]["tests"][key]["endpoint_rational"])
                                    for leaf in accepted)) if accepted else None
                       for key in LOWER_KEYS}
        masses = {state: str(sum((F(1, 2**len(leaf["address"])) for leaf in leaves
                                  if leaf["status"] == state), F(0)))
                  for state in ("accepted", "excluded")}
        masses["unresolved"] = str(sum((F(1, 2**len(item["address"]))
                                        for item in unresolved), F(0)))
        record = {
            "status": "proved" if not unresolved else "unresolved",
            "scope": "Ten next-four scalar comparisons on the necessary actual-reference superset",
            "precision_bits": 160, "height": str(H), "upper_gap": str(GAP),
            "corner_threshold": "0", "upper_tests": list(UPPER_KEYS),
            "lower_tests": list(LOWER_KEYS),
            "initial_auxiliary_rectangle": list(map(str, ROOT)),
            "necessary_reference_ranges": half.maps_four.RANGES,
            "reference": "unchanged reference_four in every frozen callback",
            "primitive": "unchanged CenteredPrimitives, explicit Q4 and outgoing halfweight",
            "visited_cells": visited, "combined_inspect_calls": visited,
            "callback_inspect_calls": dict(callback_counts), "refinements": refinements,
            "terminal_counts": dict(counts), "unresolved_count": len(unresolved),
            "dyadic_fractions": masses, "stop_reason": stop_reason,
            "requested_signals": requested_stop, "first_depth_failure_stops": True,
            "max_cells": args.max_cells, "max_depth": 20,
            "split_rule": "alternate real/imaginary dyadic subdivision, real first, lower child first",
            "terminal_partition_verified": True,
            "accepted_maximum_upper_rational": worst_upper,
            "accepted_minimum_lower_rational": worst_lower,
            "old_scalar_inspect_calls": 0, "root_proposals": 0,
            "finite_source_evaluations": 0, "automatic_retries": 0,
            "elapsed_seconds": time.monotonic()-started,
            "input_sha256": bindings, "leaves": leaves, "unresolved": unresolved,
        }
        atomic_new_record(args.output, record)
        print(json.dumps({key: record[key] for key in (
            "status", "visited_cells", "terminal_counts", "unresolved_count",
            "dyadic_fractions", "stop_reason", "elapsed_seconds")}), flush=True)
    finally:
        for sig, previous in previous_handlers.items():
            signal.signal(sig, previous)


if __name__ == "__main__":
    main()
