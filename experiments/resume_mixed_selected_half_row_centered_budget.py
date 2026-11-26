#!/usr/bin/env python3
"""Continue nine pending half-row boxes using the reviewed centered primitive.

The original record/driver/dependencies are hash-bound. Only the saved pending
boxes and their descendants call the unchanged inspect(). Stop at the first
depth-limit failure or after 6000 additional visits; no automatic retry.
All 5996 old leaves retain their original direct-primitive provider.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/"repro/results/research-mixed-selected-half-row-budget-attempt02.json"
PREVIOUS_SHA256 = "8728c18541d17fd0a6533deb60bacfe8bbb8c728c50b90123ee3bc8fc6f5ba22"
DRIVER = REPO/"experiments/certify_mixed_selected_half_row_budget.py"
DRIVER_SHA256 = "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34"
CENTERED_PROOF = REPO/"notes/research_mixed_centered_primitive_enclosure.md"
CENTERED_PROOF_SHA256 = "ce2bebcca5ff53ca466948517f4324123b09bb7c92c6736409ff47ece9aac956"
DIAGNOSTIC = REPO/"repro/results/research-mixed-half-row-centered-primitive-diagnostic.json"
DIAGNOSTIC_SHA256 = "d27dd0d7a4d42147c92084a3c77b37b1b0091809e78ba3b096826109e110709d"


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
    parser.add_argument("--max-cells", type=int, default=6000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 6000:
        parser.error("the one continuation allows at most 6000 additional cells")
    if digest(PREVIOUS) != PREVIOUS_SHA256 or digest(DRIVER) != DRIVER_SHA256:
        raise ValueError("original record or driver hash mismatch")
    if (digest(CENTERED_PROOF) != CENTERED_PROOF_SHA256
            or digest(DIAGNOSTIC) != DIAGNOSTIC_SHA256):
        raise ValueError("centered proof or one-box diagnostic hash mismatch")
    original = json.loads(PREVIOUS.read_text())
    if (original["status"] != "unresolved" or original["precision_bits"] != 160
            or original["max_depth"] != 20 or original["visited_cells"] != 12000
            or original["unresolved_count"] != 9
            or original["terminal_counts"] != {"excluded": 2106, "accepted": 3890}
            or len(original["leaves"]) != 5996
            or original["gap"] != "1/2000"
            or original["height"] != "7/625"):
        raise ValueError("unexpected original scope or saved state")
    for name, expected in original["input_sha256"].items():
        if digest(REPO/name) != expected:
            raise ValueError("original dependency hash mismatch: "+name)
    diagnostic = json.loads(DIAGNOSTIC.read_text())
    if (diagnostic["precision_bits"] != 160 or diagnostic["tested_boxes"] != 1
            or diagnostic["inspect_calls"] != 2 or diagnostic["subdivisions"] != 0
            or diagnostic["status"] != "diagnostic complete"):
        raise ValueError("unexpected centered diagnostic scope")
    for name, expected in diagnostic["input_sha256"].items():
        if digest(REPO/name) != expected:
            raise ValueError("centered diagnostic dependency mismatch: "+name)
        if (name in original["input_sha256"]
                and original["input_sha256"][name] != expected):
            raise ValueError("inconsistent inherited dependency: "+name)
    verify_partition(original["leaves"], original["unresolved"])
    if Counter(item["status"] for item in original["leaves"]) != original["terminal_counts"]:
        raise ValueError("original terminal counts do not match leaves")
    if any(item["reason"] != "cell budget; box not inspected"
           or item["enclosures"] is not None for item in original["unresolved"]):
        raise ValueError("only previously unvisited pending boxes may continue")

    # No numerical driver is imported until every immutable input is checked.
    import certify_mixed_selected_half_row_budget as driver
    from flint import acb, ctx
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
    bindings.update(diagnostic["input_sha256"])
    bindings[str(PREVIOUS.relative_to(REPO))] = PREVIOUS_SHA256
    bindings[str(CENTERED_PROOF.relative_to(REPO))] = CENTERED_PROOF_SHA256
    bindings[str(DIAGNOSTIC.relative_to(REPO))] = DIAGNOSTIC_SHA256
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))
    old_leaf_hash = canonical_digest(original["leaves"])
    leaves = list(original["leaves"])
    unresolved, new_counts, visited = [], Counter(), 0
    depth_failure = False
    started = time.monotonic()
    class CenteredPrimitives(driver.OriginalPrimitives):
        def g(self, w):
            self.regular(w)
            center = acb(w.real.mid(), w.imag.mid())
            center_value = super().g(center)
            derivative = (1-(-2*self.pi*self.ii*w).exp()).log()
            if not derivative.is_finite():
                raise driver.Inconclusive("centered primitive derivative not finite")
            result = center_value+derivative*(w-center)
            if not result.is_finite():
                raise driver.Inconclusive("centered primitive enclosure not finite")
            return result

    primitive = CenteredPrimitives()
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
    if canonical_digest(leaves[:5996]) != old_leaf_hash:
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
        "previous_continuation_max_cells": original["continuation_max_cells"],
        "previous_continuation_elapsed_seconds": original["continuation_elapsed_seconds"],
        "original_leaves_preserved_count": 5996,
        "original_leaves_canonical_sha256": old_leaf_hash,
        "new_primitive_provider": "centered original g on a convex regular strip",
        "leaf_provider_ranges": [
            {"start": 0, "stop": 5996, "provider": "original direct primitive",
             "source_record_sha256": PREVIOUS_SHA256},
            {"start": 5996, "stop": len(leaves), "provider": "centered original primitive",
             "proof_sha256": CENTERED_PROOF_SHA256}],
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
    record.pop("max_cells", None)
    record.pop("elapsed_seconds", None)
    record["ancestor_initial_max_cells"] = record.pop("previous_max_cells")
    record["ancestor_initial_elapsed_seconds"] = record.pop("previous_elapsed_seconds")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({key: record[key] for key in (
        "status", "continuation_visited_cells", "continuation_terminal_counts",
        "continuation_stop_reason", "visited_cells", "terminal_counts",
        "unresolved_count", "unresolved_dyadic_fraction",
        "continuation_elapsed_seconds")}), flush=True)


if __name__ == "__main__":
    main()
