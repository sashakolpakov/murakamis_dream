#!/usr/bin/env python3
"""One bounded centered product-boundary pass with exact saved-witness reuse.

Old records and evaluators remain unchanged. Every new profile bound uses
the centered evaluator. Cached analytic counters are witnesses, never new
calls. A partial pass retains its entire untouched parameter frontier.
"""
import argparse
from collections import Counter, defaultdict
import copy
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

from flint import ctx

import mixed_second_selected_external_boundary as geometry
import mixed_third_selected_external_reference as provider
import evaluate_mixed_third_selected_centered_tangent as evaluator


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "repro/results/research-mixed-third-selected-centered-product-boundary-attempt01.json.gz"
PROTOCOL = "notes/research_mixed_third_selected_centered_product_boundary_protocol.md"
CACHE_SOURCE = "repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz"
CACHE_AUDIT = "repro/results/research-mixed-third-selected-product-boundary-saved-audit.json"
ANCHOR_FILE = "repro/results/research-mixed-third-selected-eight-center-diagnostic.json"
PINNED = {
    PROTOCOL: "46b3f5c76e5a05283f6b2f29cc6355cb6e5ee96fb81eb82a68f4986654fa1541",
    CACHE_SOURCE: "e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e",
    CACHE_AUDIT: "9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647",
    ANCHOR_FILE: "69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a",
    "experiments/check_mixed_third_selected_product_boundary_record.py":
        "7ac82eedb454d2812a0c610b33a54cfb7a96a791cdb8e5844fce60e8c4235615",
    "experiments/check_mixed_third_selected_eight_center_record.py":
        "347d1015bce33c1761609467ce9e96e331fb5f81107ba37dc62933230ee48998",
    "repro/results/research-mixed-third-selected-eight-center-saved-audit.json":
        "14e3f08a8113a501b3073298fff532c9f9c4c4b2552c84f6d8aaecc6d43b9d14",
    "notes/research_mixed_third_selected_recentered_defect.md":
        "7bb5864714f64eb55792096c12072d59207f37056cef16a4b0ba4ee11e4d4e1d",
    "repro/results/research-mixed-third-selected-recentered-diagnostic.json":
        "951944582a63523c90f6a493fb6665678075acb91fac45c888b9684bb455e713",
    "repro/results/research-mixed-third-selected-recentered-saved-audit.json":
        "1633d0de63f0672e77cd2da6fcd1c9aa237a60718dba66082bca670992915dac",
    "experiments/evaluate_mixed_third_selected_centered_tangent.py":
        "a0f06e9d6ffdff8468b6a4e403d6ba7105d03dafb6d8474e7f83bf021cc5e4f3",
}
LIMITS = {
    "visited_cells": 4000,
    "reference_cells": 2000,
    "provider_invocations": 2000,
    "new_reference_proposals": 2000,
    "combined_binary_depth": 16,
    "newton_steps_per_proposal": 20,
    "target_iterations_per_proposal": 200,
    "precision_bits": 256,
    "new_target_proposals_per_label": 1,
}
DELTA = F(1, 2000)
CELL_FIELDS = ("case_index", "alpha", "beta", "sigma", "chart_a", "chart_c", "address",
               "interval_a", "interval_c", "abox", "cbox")


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        if not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("unfinished input binding: " + name)
        path = Path(name)
        if sha(path if path.is_absolute() else ROOT/path) != digest:
            raise ValueError("changed input: " + name)


def bind(bindings, extra):
    for name, digest in extra.items():
        if name in bindings and bindings[name] != digest:
            raise ValueError("conflicting input binding: " + name)
        bindings[name] = digest


def cases():
    charts = geometry.chartlist()
    keys = sorted((beta, a.name, c.name)
                  for beta in (0, 1) for a in charts for c in charts)
    return [dict(case_index=i, beta=beta, alpha=int(a[1])-3, sigma=int(c[1])-3,
                 chart_a=a, chart_c=c) for i, (beta, a, c) in enumerate(keys)]


def product_parameter(address):
    sides = [(-F(1), F(1)), (-F(1), F(1))]
    for digit in address:
        if digit not in "01":
            raise ValueError("invalid product address")
        axis = 0 if sides[0][1]-sides[0][0] >= sides[1][1]-sides[1][0] else 1
        sides[axis] = geometry.split(sides[axis])[int(digit)]
    return sides


def cell(case, address):
    aa, cc = product_parameter(address)
    return dict(case, address=address, interval_a=list(map(str, aa)), interval_c=list(map(str, cc)),
                abox=list(map(str, geometry.paramimage(case["chart_a"], aa))),
                cbox=list(map(str, geometry.paramimage(case["chart_c"], cc))))


def cell_identity(row):
    result = {name: row[name] for name in CELL_FIELDS}
    for name in ("interval_a", "interval_c", "abox", "cbox"):
        result[name] = [str(F(value)) for value in result[name]]
    return result


def cache_key(row):
    return canonical_hash(cell_identity(row))


def exclusion(row):
    for factor in ("a", "c"):
        witness = geometry.exactsourceexclusionwitness(row["chart_"+factor], row["interval_"+factor])
        if witness is not None:
            return {"factor": factor, "witness": witness}
    return None


def labels(beta):
    return tuple(itertools.product(("main", "left", "half"),
                                   ("main", "half") if beta == 0 else ("main",), (0, 1)))


def freeze_inputs(inventory):
    bindings = dict(PINNED)
    verify(bindings)
    with gzip.open(ROOT/CACHE_SOURCE, "rt", encoding="utf-8") as stream:
        source = json.load(stream)
    audit = json.loads((ROOT/CACHE_AUDIT).read_text())
    if (audit["status"] != "exact saved product-boundary audit passed"
            or audit["source_sha256"] != PINNED[CACHE_SOURCE]
            or audit["full_domain_proved"] is not False):
        raise ValueError("wrong saved reference audit")
    if (source["cases"] != inventory or source["precision_bits"] != 256
            or source["stop_reason"] != "first unresolved depth-limit cell"
            or not source["complete_partition"] or source["full_domain_proved"]):
        raise ValueError("wrong original bounded-pass scope")
    bind(bindings, source["input_sha256"])
    cached, cache_inventory = {}, []
    trial_count = 0
    for oldnode in source["nodes"]:
        if "reference" not in oldnode:
            continue
        oldref = oldnode["reference"]
        if oldref["status"] != "enclosed":
            raise ValueError("unexpected noncertified reference in fixed cache source")
        identity = cell_identity(oldnode)
        rebuilt = cell(inventory[oldnode["case_index"]], oldnode["address"])
        if identity != cell_identity(rebuilt):
            raise ValueError("old cached cell does not match original raw charts")
        if (oldref["alpha"] != oldnode["alpha"] or oldref["beta"] != oldnode["beta"]
                or list(map(F, oldref["diagnostics"]["input_abox"])) != list(map(F, oldnode["abox"]))
                or list(map(F, oldref["diagnostics"]["input_cbox"])) != list(map(F, oldnode["cbox"]))):
            raise ValueError("old reference/cell association mismatch")
        expected = labels(oldnode["beta"])
        if [(p["incoming_profile"], p["outgoing_profile"], p["nu"]) for p in oldnode["profiles"]] != list(expected):
            raise ValueError("old trial inventory mismatch")
        trials = {}
        trial_inventory = []
        for number, (oldprofile, label) in enumerate(zip(oldnode["profiles"], expected)):
            if len(oldprofile["trial"]) != 5 or "proposal" not in oldprofile:
                raise ValueError("old exact trial/proposal is missing")
            tuple(map(F, oldprofile["trial"]))
            trials[label] = oldprofile
            trial_inventory.append({"source_profile_index": number, "label": list(label),
                                    "source_profile_sha256": canonical_hash(oldprofile),
                                    "trial": oldprofile["trial"]})
        trial_count += len(trials)
        key = cache_key(oldnode)
        if key in cached:
            raise ValueError("duplicate saved reference cell")
        provenance = {
            "source": CACHE_SOURCE, "source_sha256": PINNED[CACHE_SOURCE],
            "source_node_index": oldnode["node_index"],
            "source_node_sha256": canonical_hash(oldnode),
            "source_reference_sha256": canonical_hash(oldref),
            "source_coordinate_sha256": canonical_hash(oldref["coordinates"]),
            "cell_identity": identity, "cell_identity_sha256": key,
            "old_reference_counts_are_witnesses_not_new_calls": True,
        }
        cached[key] = {"reference": oldref, "trials": trials, "provenance": provenance,
                       "trial_inventory": trial_inventory}
        cache_inventory.append(dict(provenance, trials=trial_inventory))
    if len(cached) != 20 or trial_count != 240:
        raise ValueError("fixed cache source must contain exactly twenty references and 240 trials")
    original = json.loads((ROOT/ANCHOR_FILE).read_text())
    bind(bindings, original["input_sha256"])
    anchors, anchor_inventory = {}, []
    for index, anchor in enumerate(original["references"]):
        key = (anchor["alpha"], anchor["beta"], anchor["external_right_type_flag"])
        if key in anchors or anchor["status"] != "fixed canonical reference certified":
            raise ValueError("duplicate or uncertified center anchor")
        anchors[key] = anchor
        anchor_inventory.append({"alpha": key[0], "beta": key[1], "sigma": key[2],
                                 "source_reference_index": index,
                                 "reference_canonical_sha256": canonical_hash(anchor),
                                 "coordinate_canonical_sha256": canonical_hash(anchor["reference_certificate"]["coordinates"])})
    if set(anchors) != set(itertools.product((0, 1), repeat=3)):
        raise ValueError("incomplete center-anchor inventory")
    pinfo, einfo = provider.initialize(), evaluator.initialize()
    bind(bindings, pinfo["bindings"])
    bind(bindings, einfo["bindings"])
    for path in (Path(__file__).resolve(), Path(geometry.__file__).resolve()):
        bind(bindings, {str(path.relative_to(ROOT)): sha(path)})
    verify(bindings)
    return bindings, cached, cache_inventory, anchors, anchor_inventory, pinfo, einfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("refusing to overwrite a completed or partial record")
    if not str(args.output).endswith(".json.gz"):
        raise ValueError("the complete archive must use .json.gz")
    ctx.prec = LIMITS["precision_bits"]
    inventory = cases()
    bindings, cache, cache_inventory, anchors, anchor_inventory, pinfo, einfo = freeze_inputs(inventory)
    pending = [cell(case, "") for case in reversed(inventory)]
    nodes, counts, new_provider_counts = [], Counter(), Counter()
    stop_reason, active = None, None
    started = time.monotonic()
    record = {
        "status": "bounded centered pass in progress", "stop_reason": None,
        "limits": dict(LIMITS), "precision_bits": ctx.prec, "delta": str(DELTA),
        "input_sha256": bindings, "cases": inventory, "nodes": nodes,
        "pending": [], "counts": {}, "complete_partition": False, "full_domain_proved": False,
        "anchor_source": ANCHOR_FILE, "anchor_inventory": anchor_inventory,
        "cache_source": CACHE_SOURCE, "cache_source_sha256": PINNED[CACHE_SOURCE],
        "cache_audit": CACHE_AUDIT, "cache_audit_sha256": PINNED[CACHE_AUDIT],
        "eligible_cached_references": 20, "eligible_cached_trials": 240,
        "cache_inventory": cache_inventory, "cache_inventory_sha256": canonical_hash(cache_inventory),
        "provider_initialization": pinfo, "evaluator_initialization": einfo,
        "scope": "third position, second position unselected; m>=5; full parameter comparison only if every chart is resolved",
        "parameter_clipping": "none before residual certification; strict whole-factor geometric exclusions only",
        "ordering": "lexicographic cases, depth first, longer normalized parameter side, a on ties",
        "reuse_policy": "complete exact cell identity; saved reference/trial witnesses do not count as new analytic calls",
        "old_source_frontier_modified": False, "whole_source_theorem_claimed": False,
    }
    try:
        while pending:
            if len(nodes) >= LIMITS["visited_cells"]:
                stop_reason = "visited-cell limit reached"
                break
            if counts["reference_cells"] >= LIMITS["reference_cells"]:
                stop_reason = "reference-cell limit reached"
                break
            active = pending.pop()
            active.update(node_index=len(nodes), profiles=[], status="unresolved")
            nodes.append(active)
            counts["visited_cells"] += 1
            witness = exclusion(active)
            if witness is not None:
                active.update(status="excluded", geometry_witness=witness)
            else:
                counts["reference_cells"] += 1
                saved = cache.get(cache_key(active))
                if saved is not None:
                    if cell_identity(active) != saved["provenance"]["cell_identity"]:
                        raise ValueError("saved reference cell-identity mismatch")
                    reference = copy.deepcopy(saved["reference"])
                    counts["cached_reference_uses"] += 1
                    active["reference_origin"] = "saved"
                    active["reference_cache_association"] = copy.deepcopy(saved["provenance"])
                else:
                    active["reference_origin"] = "new"
                    counts["provider_invocations"] += 1
                    reference = provider.evaluate(active["alpha"], active["beta"], active["abox"], active["cbox"])
                    new_provider_counts.update(reference.get("counts", {}))
                active["reference"] = reference
                reference_hash = canonical_hash(reference)
                active["reference_payload_sha256"] = reference_hash
                if saved is not None and reference_hash != saved["provenance"]["source_reference_sha256"]:
                    raise ValueError("cached reference witness changed")
                if reference["status"] == "error":
                    active.update(status="error", reason=reference.get("reason"))
                    stop_reason = "unexpected reference error"
                    break
                if reference["status"] == "enclosed":
                    counts["enclosed_reference_cells"] += 1
                    anchor = anchors[(active["alpha"], active["beta"], active["sigma"])]
                    active["anchor_reference_canonical_sha256"] = canonical_hash(anchor)
                    active["reference_coordinate_canonical_sha256"] = canonical_hash(reference["coordinates"])
                    for profile_index, (left, right, nu) in enumerate(labels(active["beta"])):
                        profile = dict(incoming_profile=left, outgoing_profile=right, nu=nu)
                        active["profiles"].append(profile)
                        if saved is not None:
                            oldprofile = saved["trials"][(left, right, nu)]
                            trial = tuple(map(F, oldprofile["trial"]))
                            proposal = copy.deepcopy(oldprofile["proposal"])
                            profile["proposal_origin"] = "saved"
                            profile["saved_trial_association"] = {
                                "source": CACHE_SOURCE, "source_sha256": PINNED[CACHE_SOURCE],
                                "source_node_index": saved["provenance"]["source_node_index"],
                                "source_profile_index": profile_index,
                                "source_profile_sha256": canonical_hash(oldprofile),
                                "source_reference_sha256": reference_hash,
                                "old_proposal_metadata_not_a_new_call": True,
                            }
                            counts["cached_trial_uses"] += 1
                        else:
                            profile["proposal_origin"] = "new"
                            counts["new_target_proposals"] += 1
                            try:
                                trial, proposal = evaluator.propose_trial(
                                    reference, active["alpha"], active["beta"], left, right, nu)
                            except evaluator.Inconclusive as error:
                                profile.update(status="inconclusive", reason=str(error), proposal_failed=True)
                                continue
                        profile.update(trial=list(map(str, trial)), proposal=proposal)
                        counts["centered_profile_interval_bounds"] += 1
                        evaluated = evaluator.evaluate(reference, anchor, active["alpha"], active["beta"],
                                                       left, right, nu, trial)
                        if "proposal_origin" in evaluated or "saved_trial_association" in evaluated:
                            raise ValueError("evaluator attempted to replace trial provenance")
                        profile.update(evaluated)
                        if profile.get("status") == "error":
                            active.update(status="error", reason=profile.get("reason"))
                            stop_reason = "unexpected centered target error"
                            break
                    if canonical_hash(reference) != reference_hash:
                        raise ValueError("evaluator modified its reference witness")
                    if stop_reason is not None:
                        break
                    bounds = [F(p["compensated_upper_rational"]) for p in active["profiles"]
                              if p.get("status") == "enclosed" and "compensated_upper_rational" in p]
                    if len(bounds) == len(labels(active["beta"])):
                        active["maximum_compensated_upper_rational"] = str(max(bounds))
                        if max(bounds) < -DELTA:
                            active["status"] = "accepted"
                elif reference["status"] != "inconclusive":
                    raise ValueError("unknown reference status")
                if active["status"] == "unresolved":
                    if len(active["address"]) >= LIMITS["combined_binary_depth"]:
                        stop_reason = "first unresolved depth-limit cell"
                        break
                    aa, cc = product_parameter(active["address"])
                    active.update(status="split", split_axis="a" if aa[1]-aa[0] >= cc[1]-cc[0] else "c")
                    case = inventory[active["case_index"]]
                    pending.append(cell(case, active["address"]+"1"))
                    pending.append(cell(case, active["address"]+"0"))
            if len(nodes) % 20 == 0:
                print(json.dumps({"visited": len(nodes), "pending": len(pending), "node_status": active["status"],
                                  "reference_cells": counts["reference_cells"],
                                  "cached_references": counts["cached_reference_uses"],
                                  "new_provider_invocations": counts["provider_invocations"],
                                  "centered_bounds": counts["centered_profile_interval_bounds"],
                                  "elapsed_seconds": round(time.monotonic()-started, 1)}), flush=True)
            active = None
    except KeyboardInterrupt:
        stop_reason = "interrupted; complete untouched frontier retained"
        if active is not None and active["status"] not in ("accepted", "excluded", "split"):
            active.update(status="unresolved", reason="interrupted during evaluation")
    except Exception as error:
        stop_reason = "unexpected driver or evaluator exception"
        record["unexpected_error"] = repr(error)
        if active is not None:
            active.update(status="error", reason=repr(error))

    record["pending"] = list(reversed(pending))
    counts["new_reference_proposals"] = new_provider_counts["proposal_calls"]
    for status, count in Counter(n["status"] for n in nodes).items():
        counts[status] = count
    counts["pending"] = len(pending)
    record["counts"] = dict(counts)
    record["new_provider_counts"] = dict(new_provider_counts)
    record["cached_provider_counts_included_in_new_counts"] = False
    record["elapsed_seconds"] = time.monotonic()-started
    record["stop_reason"] = stop_reason
    frontiers = defaultdict(list)
    for row in nodes:
        if row["status"] != "split":
            frontiers[row["case_index"]].append(row["address"])
    for row in pending:
        frontiers[row["case_index"]].append(row["address"])
    try:
        record["partition_summary"] = [dict(case_index=i, **geometry.validate_partition(frontiers[i]))
                                       for i in range(len(inventory))]
        leaf_count = sum(row["leaf_count"] for row in record["partition_summary"])
        if len(nodes)+len(pending) != 2*leaf_count-len(inventory):
            raise ValueError("visited/pending forest node identity failed")
        if counts["reference_cells"] != counts["cached_reference_uses"]+counts["provider_invocations"]:
            raise ValueError("new and saved reference-cell accounting mismatch")
        record["complete_partition"] = True
    except Exception as error:
        record["partition_error"] = repr(error)
    try:
        verify(bindings)
        record["input_bindings_unchanged"] = True
    except Exception as error:
        record["input_bindings_unchanged"] = False
        record["input_binding_error"] = repr(error)
    record["full_domain_proved"] = bool(
        record["complete_partition"] and record["input_bindings_unchanged"]
        and not pending and stop_reason is None and not counts["unresolved"] and not counts["error"]
        and counts["visited_cells"] <= LIMITS["visited_cells"]
        and counts["reference_cells"] <= LIMITS["reference_cells"]
        and counts["provider_invocations"] <= LIMITS["provider_invocations"]
        and counts["new_reference_proposals"] <= LIMITS["new_reference_proposals"])
    record["status"] = ("complete centered domain comparison" if record["full_domain_proved"]
                        else "bounded centered pass stopped without a full-domain conclusion")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("xb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0) as compressed:
            for chunk in json.JSONEncoder(sort_keys=True, separators=(",", ":")).iterencode(record):
                compressed.write(chunk.encode())
            compressed.write(b"\n")
    print(json.dumps({"status": record["status"], "stop_reason": stop_reason, "counts": record["counts"],
                      "complete_partition": record["complete_partition"], "output_sha256": sha(args.output)}), flush=True)


if __name__ == "__main__":
    main()
