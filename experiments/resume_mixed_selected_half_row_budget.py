#!/usr/bin/env python3
"""Continue the nine unvisited half-row boxes once, preserving all old leaves.

The original record/driver/dependencies are hash-bound. Only the saved pending
boxes and their descendants call the unchanged inspect(). Stop at the first
depth-limit failure or after8000 additional visits; no automatic retry.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/"repro/results/research-mixed-selected-half-row-budget-attempt01.json"
PREVIOUS_SHA256 = "face0d1cfe67cd2134f3ff8c661c9589089c0aaec95ec7fb96f5ad0012db55c4"
DRIVER = REPO/"experiments/certify_mixed_selected_half_row_budget.py"
DRIVER_SHA256 = "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify_partition(leaves, pending):
    addresses = [item["address"] for item in leaves+pending]
    if any(set(address)-set("01") for address in addresses):
        raise ValueError("nonbinary terminal address")
    ordered = sorted(addresses)
    if len(set(addresses)) != len(addresses):
        raise ValueError("duplicate terminal address")
    if any(right.startswith(left) for left, right in zip(ordered, ordered[1:])):
        raise ValueError("terminal addresses are not prefix-free")
    if sum((F(1, 2**len(address)) for address in addresses), F()) != 1:
        raise ValueError("terminal dyadic masses do not sum to one")
    if any(item["status"] not in ("accepted", "excluded") for item in leaves):
        raise ValueError("nonterminal entry in old leaves")


def decode_box(address, base):
    box = base.ROOT
    for depth, branch in enumerate(address):
        box = base.split(box, depth)[int(branch)]
    return box


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-cells", type=int, default=8000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 8000:
        parser.error("the one continuation allows at most8000 additional cells")
    if digest(PREVIOUS) != PREVIOUS_SHA256 or digest(DRIVER) != DRIVER_SHA256:
        raise ValueError("original record or driver hash mismatch")
    original = json.loads(PREVIOUS.read_text())
    if (original["status"] != "unresolved" or original["precision_bits"] != 160
            or original["max_depth"] != 20 or original["visited_cells"] != 4000
            or original["unresolved_count"] != 9
            or original["terminal_counts"] != {"excluded": 1653, "accepted": 343}
            or len(original["leaves"]) != 1996
            or original["gap"] != "1/2000"
            or original["height"] != "7/625"):
        raise ValueError("unexpected original scope or saved state")
    for name, expected in original["input_sha256"].items():
        if digest(REPO/name) != expected:
            raise ValueError("original dependency hash mismatch: "+name)
    verify_partition(original["leaves"], original["unresolved"])
    if Counter(item["status"] for item in original["leaves"]) != original["terminal_counts"]:
        raise ValueError("original terminal counts do not match leaves")
    if any(item["reason"] != "cell budget; box not inspected"
           or item["enclosures"] is not None for item in original["unresolved"]):
        raise ValueError("only previously unvisited pending boxes may continue")

    # No numerical driver is imported until every immutable input is checked.
    import certify_mixed_selected_half_row_budget as driver
    from flint import ctx
    ctx.prec = original["precision_bits"]
    if list(map(str, driver.base.ROOT)) != original["initial_auxiliary_rectangle"]:
        raise ValueError("initial reference rectangle mismatch")
    stack = []
    for item in original["unresolved"]:
        address = item["address"]
        box = tuple(map(F, item["box"]))
        if box != decode_box(address, driver.base) or len(address) > 20:
            raise ValueError("pending address-to-box mismatch")
        stack.append((address, box))

    bindings = dict(original["input_sha256"])
    bindings[str(PREVIOUS.relative_to(REPO))] = PREVIOUS_SHA256
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    old_leaf_hash = canonical_digest(original["leaves"])
    leaves = list(original["leaves"])
    unresolved, new_counts, visited = [], Counter(), 0
    depth_failure = False
    started = time.monotonic()
    primitive = driver.OriginalPrimitives()
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, details = driver.inspect(box, primitive)
        visited += 1
        if kind in ("accepted", "excluded"):
            new_counts[kind] += 1
            item = {"address": address, "status": kind, "reason": reason}
            if kind == "accepted":
                item["certificate"] = details
            leaves.append(item)
        elif len(address) >= original["max_depth"]:
            unresolved.append({"address": address, "box": list(map(str, box)),
                               "reason": reason, "enclosures": details})
            depth_failure = True
            break
        else:
            children = driver.base.split(box, len(address))
            stack.extend([(address+"1", children[1]), (address+"0", children[0])])
        if visited % 250 == 0:
            print(json.dumps({"additional_visits": visited,
                              "new_terminal_counts": dict(new_counts),
                              "pending": len(stack)}), flush=True)
    stop_reason = ("first depth-limit failure" if depth_failure else
                   "cell budget" if stack else "pending partition completed")
    unresolved.extend({"address": address, "box": list(map(str, box)),
                       "reason": stop_reason+"; box not inspected", "enclosures": None}
                      for address, box in stack)
    verify_partition(leaves, unresolved)
    if canonical_digest(leaves[:1996]) != old_leaf_hash:
        raise ValueError("original terminal leaves changed")
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during continuation: "+name)
    maxima = {}
    for key in driver.KEYS:
        values = [F(item["certificate"]["majorants"][key]["value"]["upper_rational"])
                  for item in leaves if item["status"] == "accepted"]
        maxima[key] = str(max(values)) if values else None
    record = dict(original)
    record.update({
        "status": "unresolved" if unresolved else "proved",
        "previous_record": str(PREVIOUS.relative_to(REPO)),
        "previous_record_sha256": PREVIOUS_SHA256,
        "previous_visited_cells": original["visited_cells"],
        "previous_terminal_counts": original["terminal_counts"],
        "original_leaves_preserved_count": 1996,
        "original_leaves_canonical_sha256": old_leaf_hash,
        "continuation_initial_pending_addresses":
            [item["address"] for item in original["unresolved"]],
        "continuation_max_cells": args.max_cells,
        "continuation_visited_cells": visited,
        "continuation_terminal_counts": dict(new_counts),
        "continuation_stop_reason": stop_reason,
        "continuation_elapsed_seconds": time.monotonic()-started,
        "visited_cells": original["visited_cells"]+visited,
        "terminal_counts": dict(Counter(item["status"] for item in leaves)),
        "unresolved_count": len(unresolved),
        "unresolved_dyadic_fraction": str(sum(
            (F(1, 2**len(item["address"])) for item in unresolved), F())),
        "terminal_partition_verified": True,
        "accepted_maximum_upper_rational": maxima,
        "input_sha256": bindings, "leaves": leaves, "unresolved": unresolved,
    })
    record["previous_max_cells"] = record.pop("max_cells")
    record["previous_elapsed_seconds"] = record.pop("elapsed_seconds")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({key: record[key] for key in (
        "status", "continuation_visited_cells", "continuation_terminal_counts",
        "continuation_stop_reason", "visited_cells", "terminal_counts",
        "unresolved_count", "unresolved_dyadic_fraction",
        "continuation_elapsed_seconds")}), flush=True)


if __name__ == "__main__":
    main()
