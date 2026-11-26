#!/usr/bin/env python3
"""Saved-only audit of the centered product-boundary pass and witness cache.

Two explicitly pinned stdlib checker modules supply exact arithmetic helpers;
neither main function runs. No analytic/provider module is imported, and no
source, root, primitive, interval or optimization evaluation occurs.
"""
import argparse
import ast
from collections import Counter, defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "repro/results/research-mixed-third-selected-centered-product-boundary-attempt01.json.gz"
EXPECTED_SOURCE_SHA256 = "ef7c37a13f836d0e09a3ad45170e79946b16dd1436cb030816330f5270bed2ba"
EXPECTED_COUNTS = {
    "nodes": 2042, "pending": 166, "reference_cells": 2000,
    "cached_reference_uses": 11, "enclosed_reference_cells": 2000,
    "cached_trial_uses": 132, "centered_profile_interval_bounds": 24000,
    "provider_invocations": 1989, "new_target_proposals": 23868,
    "new_reference_proposals": 1989,
    "split": 1023, "excluded": 42, "accepted": 977,
    "unresolved": 0, "error": 0,
}
CACHE_SOURCE = "repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz"
CACHE_AUDIT = "repro/results/research-mixed-third-selected-product-boundary-saved-audit.json"
ANCHOR_SOURCE = "repro/results/research-mixed-third-selected-eight-center-diagnostic.json"
HELPERS = {
    "experiments/check_mixed_third_selected_product_boundary_record.py":
        "7ac82eedb454d2812a0c610b33a54cfb7a96a791cdb8e5844fce60e8c4235615",
    "experiments/check_mixed_third_selected_recentered_record.py":
        "47a09bb773e51ca1b9077f1d76ef002071b77f97801b4122bbb57742e57655ba",
}
MANDATORY_INPUTS = {
    "experiments/certify_mixed_third_selected_centered_product_boundary.py":
        "241bd8c5d8a56ca65d0fac4df73014a7ee76050c884f2c124c4db42b7fada4b4",
    "experiments/evaluate_mixed_third_selected_centered_tangent.py":
        "a0f06e9d6ffdff8468b6a4e403d6ba7105d03dafb6d8474e7f83bf021cc5e4f3",
    "experiments/mixed_third_selected_external_reference.py":
        "bfc1057caf82d14c34878f9e822570f087cd7c8d2f6632c39d88bd052eed9158",
    "notes/research_mixed_third_selected_centered_product_boundary_protocol.md":
        "46b3f5c76e5a05283f6b2f29cc6355cb6e5ee96fb81eb82a68f4986654fa1541",
    "notes/research_mixed_third_selected_centered_tangent_evaluation.md":
        "f5a7eace4e41e121f406799049af3537383c23f8a48fb873451ffb74cc67b2d6",
    CACHE_SOURCE: "e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e",
    CACHE_AUDIT: "9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647",
    ANCHOR_SOURCE: "69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a",
}
LIMITS = {
    "visited_cells": 4000, "reference_cells": 2000, "provider_invocations": 2000,
    "new_reference_proposals": 2000, "combined_binary_depth": 16,
    "newton_steps_per_proposal": 20, "target_iterations_per_proposal": 200,
    "precision_bits": 256, "new_target_proposals_per_label": 1,
}
CELL_FIELDS = ("case_index", "alpha", "beta", "sigma", "chart_a", "chart_c", "address",
               "interval_a", "interval_c", "abox", "cbox")
NAMES = ("a", "u", "z", "v", "b")
DELTA = F(1, 2000)


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2**20), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        assert isinstance(digest, str) and len(digest) == 64
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name


def load_checker(name, digest, module_name):
    path = ROOT/name
    assert sha(path) == digest
    tree = ast.parse(path.read_text())
    allowed = {"argparse", "collections", "fractions", "gzip", "hashlib", "itertools", "json", "pathlib"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert all(item.name in allowed for item in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert node.level == 0 and node.module in allowed
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def identity(row):
    result = {key: row[key] for key in CELL_FIELDS}
    for key in ("interval_a", "interval_c", "abox", "cbox"):
        result[key] = [str(F(value)) for value in result[key]]
    return result


def read_cache(data, cache_source, product):
    assert data["cache_source"] == CACHE_SOURCE
    assert data["cache_source_sha256"] == MANDATORY_INPUTS[CACHE_SOURCE]
    assert data["cache_audit"] == CACHE_AUDIT
    assert data["cache_audit_sha256"] == MANDATORY_INPUTS[CACHE_AUDIT]
    assert data["eligible_cached_references"] == 20 and data["eligible_cached_trials"] == 240
    assert cache_source["cases"] == data["cases"]
    registry, inventory = {}, []
    trial_count = 0
    for node in cache_source["nodes"]:
        if "reference" not in node:
            continue
        reference = node["reference"]
        assert reference["status"] == "enclosed"
        product.check_cell_geometry(node, data["cases"])
        key = canonical_hash(identity(node))
        assert key not in registry
        labels = product.profile_inventory(node["beta"])
        assert [(p["incoming_profile"], p["outgoing_profile"], p["nu"]) for p in node["profiles"]] == labels
        trials = [{"source_profile_index": i, "label": list(label),
                   "source_profile_sha256": canonical_hash(row), "trial": row["trial"]}
                  for i, (row, label) in enumerate(zip(node["profiles"], labels))]
        trial_count += len(trials)
        provenance = {
            "source": CACHE_SOURCE, "source_sha256": MANDATORY_INPUTS[CACHE_SOURCE],
            "source_node_index": node["node_index"], "source_node_sha256": canonical_hash(node),
            "source_reference_sha256": canonical_hash(reference),
            "source_coordinate_sha256": canonical_hash(reference["coordinates"]),
            "cell_identity": identity(node), "cell_identity_sha256": key,
            "old_reference_counts_are_witnesses_not_new_calls": True,
        }
        registry[key] = (node, provenance)
        inventory.append(dict(provenance, trials=trials))
    assert len(registry) == 20 and trial_count == 240
    assert data["cache_inventory"] == inventory
    assert data["cache_inventory_sha256"] == canonical_hash(inventory)
    return registry


def check_centered_profile(row, reference, anchor, product, centered):
    alpha, beta, left, right, nu = (row[key] for key in ("alpha", "beta", "left", "right", "nu"))
    assert alpha in (0, 1) and beta in (0, 1) and nu in (0, 1)
    assert row["precision_bits"] == 256
    assert row["trial_enclosure_method"] == "centered original difference of actions"
    assert row["primitive_calls"] == {"g": 27, "gp": 56}
    assert row["enclosure_calls"] == {
        "midpoint_defect_evaluations": 1, "full_box_gradient_evaluations": 2,
        "cotangent_evaluations": 4, "reference_proposals": 0,
        "target_optimizations": 0, "parameter_subdivisions": 0,
    }
    coordinates = reference["coordinates"]
    assert row["reference_coordinate_endpoints"] == coordinates
    assert row["anchor_coordinate_endpoints"] == anchor["reference_certificate"]["coordinates"]
    midpoint, displacements = {}, {}
    for name in NAMES:
        midpoint[name], displacements[name] = {}, {}
        for part in ("real", "imag"):
            lo, hi = product.interval(coordinates[name][part])
            middle = (lo+hi)/2
            midpoint[name][part] = str(middle)
            displacements[name][part] = [str(lo-middle), str(hi-middle)]
    assert row["exact_midpoint"] == midpoint
    assert row["reference_displacements"] == displacements
    trial = list(map(F, row["trial"]))
    centered.check_images(row, coordinates, midpoint, trial, left, right)
    centered.check_derivatives(row, trial, left, right)
    lower, upper = product.interval(row["midpoint_defect"])
    for term in row["mean_value_terms"]:
        dl, dh = map(F, displacements[term["name"]][term["part"]])
        assert list(map(F, term["displacement"])) == [dl, dh]
        gl, gh = product.interval(term["derivative"])
        products = [gl*dl, gl*dh, gh*dl, gh*dh]
        assert list(map(F, term["corner_products"])) == products
        assert F(term["lower_rational"]) == min(products)
        assert F(term["upper_rational"]) == max(products)
        lower += min(products)
        upper += max(products)
    assert product.interval(row["centered_trial_defect"]) == (lower, upper)
    assert row["trial_defect"] == row["centered_trial_defect"]
    assert row["incoming_marginal"] == row["reference_gradient"]["a"]
    assert row["outgoing_marginal"] == row["reference_gradient"]["b"]
    for j, name in enumerate(NAMES):
        slope = product.interval(row["target_gradient"][name]["real"])
        if name in ("a", "b"):
            slope = product.interval_difference(slope, product.interval(row["reference_gradient"][name]["real"]))
        elif name == "z" and nu == 0:
            slope = product.interval_sum(slope, product.interval(row["target_selected_logarithm"]["real"]))
        assert product.interval_contains(product.interval(row["support_terms"][j]["gradient"]), slope)
    supported = product.support_upper(row, beta)
    assert F(row["support_correction_rational"]) == supported-upper
    return product.check_compensation(row, reference, anchor)


def coverage_summaries(cases, nodes, pending):
    """Exact parameter mass and compressed proved prefixes, not physical area."""
    leaves = defaultdict(list)
    for node in nodes:
        if node["status"] != "split":
            leaves[node["case_index"]].append((node["address"], node["status"]))
    for node in pending:
        leaves[node["case_index"]].append((node["address"], "pending"))
    summaries = []
    for i, case in enumerate(cases):
        counts, masses = Counter(), defaultdict(F)
        proved = set()
        for address, status in leaves[i]:
            counts[status] += 1
            masses[status] += F(1, 2**len(address))
            if status in ("accepted", "excluded"):
                proved.add(address)
        assert sum(masses.values()) == 1
        for depth in range(16, 0, -1):
            for address in sorted(a for a in proved if len(a) == depth and a.endswith("0")):
                if address[:-1]+"1" in proved:
                    proved.remove(address)
                    proved.remove(address[:-1]+"1")
                    proved.add(address[:-1])
        assert sum(F(1, 2**len(a)) for a in proved) == masses["accepted"]+masses["excluded"]
        summaries.append(dict(case, case_index=i, terminal_counts=dict(counts),
                              normalized_parameter_mass={key: str(value) for key, value in masses.items()},
                              complete_comparison=(proved == {""}),
                              proved_prefixes=sorted(proved),
                              pending_prefixes=sorted(a for a, status in leaves[i] if status == "pending"),
                              maximum_depth=max(len(a) for a, _ in leaves[i])))
    return summaries


def main():
    if EXPECTED_SOURCE_SHA256 is None or EXPECTED_COUNTS is None:
        raise RuntimeError("checker guarded: terminal source hash and counts are pending")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    verify(HELPERS)
    verify(MANDATORY_INPUTS)
    assert sha(ROOT/SOURCE) == EXPECTED_SOURCE_SHA256
    product, centered = [load_checker(name, digest, "_saved_centered_checker_"+str(i))
                         for i, (name, digest) in enumerate(HELPERS.items())]
    with gzip.open(ROOT/SOURCE, "rt", encoding="utf-8") as stream:
        data = json.load(stream)
    bindings = data["input_sha256"]
    assert all(bindings[name] == digest for name, digest in MANDATORY_INPUTS.items())
    verify(bindings)
    assert data["limits"] == LIMITS and data["precision_bits"] == 256
    assert F(data["delta"]) == DELTA and data["input_bindings_unchanged"] is True
    assert data["old_source_frontier_modified"] is False
    assert data["whole_source_theorem_claimed"] is False
    assert data["cached_provider_counts_included_in_new_counts"] is False
    for key in ("provider_initialization", "evaluator_initialization"):
        assert data[key]["precision_bits"] == 256
        assert all(bindings[name] == digest for name, digest in data[key]["bindings"].items())
    assert data["evaluator_initialization"]["complete_evaluation_counts"] == {"g": 27, "gp": 56, "cotangent": 4}
    with gzip.open(ROOT/CACHE_SOURCE, "rt", encoding="utf-8") as stream:
        cache_source = json.load(stream)
    assert all(bindings[name] == digest for name, digest in cache_source["input_sha256"].items())
    cache_audit = json.loads((ROOT/CACHE_AUDIT).read_text())
    assert cache_audit["status"] == "exact saved product-boundary audit passed"
    assert cache_audit["source_sha256"] == MANDATORY_INPUTS[CACHE_SOURCE]
    assert cache_audit["full_domain_proved"] is False
    cache = read_cache(data, cache_source, product)
    anchors = json.loads((ROOT/ANCHOR_SOURCE).read_text())
    anchor_index = product.check_anchor_inventory(data, anchors)
    cases, frontier, status_counts = product.check_geometry_forest(data)
    assert data["complete_partition"] is True
    expected_partition = [{"case_index": row["case_index"], "leaf_count": row["leaves"],
                           "normalized_mass_rational": "1", "full_tree_node_count": row["full_tree_nodes"],
                           "maximum_depth": row["maximum_depth"]} for row in frontier]
    assert data["partition_summary"] == expected_partition
    assert max(row["maximum_depth"] for row in frontier) <= 16
    nodes, pending = data["nodes"], data["pending"]
    tally, provider_counts, primitive_counts, enclosure_counts = Counter(), Counter(), Counter(), Counter()
    accepted_bounds, finite_bounds = defaultdict(list), []
    profile_status_counts, worst_profiles = Counter(), {}
    weakest_accepted = None
    for node in nodes:
        case = cases[node["case_index"]]
        if node["status"] == "excluded":
            assert "reference" not in node and not node["profiles"]
            continue
        tally["reference_cells"] += 1
        saved = cache.get(canonical_hash(identity(node)))
        if saved is not None:
            oldnode, provenance = saved
            assert node["reference_origin"] == "saved"
            assert node["reference_cache_association"] == provenance
            assert node["reference"] == oldnode["reference"]
            tally["cached_reference_uses"] += 1
        else:
            assert node["reference_origin"] == "new"
            assert "reference_cache_association" not in node
            tally["provider_invocations"] += 1
        if "reference" not in node:
            assert node["status"] == "error" and data.get("unexpected_error")
            continue
        reference = node["reference"]
        assert node["reference_payload_sha256"] == canonical_hash(reference)
        if saved is None:
            provider_counts.update(reference["counts"])
        product.check_reference(reference, case, tuple(map(F, node["abox"])), tuple(map(F, node["cbox"])))
        if reference["status"] != "enclosed":
            assert node["status"] != "accepted" and not node["profiles"]
            continue
        tally["enclosed_reference_cells"] += 1
        anchor = anchor_index[(node["alpha"], node["beta"], node["sigma"])]
        assert node["anchor_reference_canonical_sha256"] == canonical_hash(anchor)
        assert node["reference_coordinate_canonical_sha256"] == canonical_hash(reference["coordinates"])
        labels = product.profile_inventory(node["beta"])
        assert len(node["profiles"]) <= len(labels)
        if node["status"] != "error" and node.get("reason") != "interrupted during evaluation":
            assert len(node["profiles"]) == len(labels)
        node_bounds = []
        for i, (row, label) in enumerate(zip(node["profiles"], labels)):
            left, right, nu = label
            assert (row["incoming_profile"], row["outgoing_profile"], row["nu"]) == label
            profile_status_counts[row["status"]] += 1
            if saved is not None:
                oldrow = oldnode["profiles"][i]
                assert row["proposal_origin"] == "saved"
                assert row["trial"] == oldrow["trial"] and row["proposal"] == oldrow["proposal"]
                assert row["saved_trial_association"] == {
                    "source": CACHE_SOURCE, "source_sha256": MANDATORY_INPUTS[CACHE_SOURCE],
                    "source_node_index": oldnode["node_index"], "source_profile_index": i,
                    "source_profile_sha256": canonical_hash(oldrow),
                    "source_reference_sha256": canonical_hash(reference),
                    "old_proposal_metadata_not_a_new_call": True,
                }
                tally["cached_trial_uses"] += 1
            else:
                assert row["proposal_origin"] == "new" and "saved_trial_association" not in row
                tally["new_target_proposals"] += 1
            if row.get("proposal_failed"):
                assert saved is None and row["status"] == "inconclusive"
                continue
            assert row["proposal"]["maximum_iterations"] == 200
            assert row["proposal"]["proposal_calls"] == 1
            assert 0 <= row["proposal"]["iterations"] <= 200
            tally["centered_profile_interval_bounds"] += 1
            primitive_counts.update(row.get("primitive_calls", {}))
            enclosure_counts.update(row.get("enclosure_calls", {}))
            if row["status"] != "enclosed":
                assert row["status"] in ("inconclusive", "error")
                continue
            assert (row["alpha"], row["beta"], row["left"], row["right"], row["nu"]) == (
                node["alpha"], node["beta"], left, right, nu)
            upper = check_centered_profile(row, reference, anchor, product, centered)
            node_bounds.append(upper)
            finite_bounds.append(upper)
            key = (node["alpha"], node["beta"], node["sigma"], left, right, nu)
            details = {"node_index": node["node_index"], "case_index": node["case_index"],
                       "address": node["address"], "node_status": node["status"],
                       "alpha": node["alpha"], "beta": node["beta"], "sigma": node["sigma"],
                       "incoming_profile": left, "outgoing_profile": right, "nu": nu,
                       "compensated_upper_rational": str(upper)}
            if key not in worst_profiles or upper > F(worst_profiles[key]["compensated_upper_rational"]):
                worst_profiles[key] = details
            if node["status"] == "accepted" and (weakest_accepted is None
                    or upper > F(weakest_accepted["compensated_upper_rational"])):
                weakest_accepted = details
        if len(node_bounds) == len(labels) and node["status"] != "error":
            maximum = max(node_bounds)
            assert F(node["maximum_compensated_upper_rational"]) == maximum
            assert (node["status"] == "accepted") == (maximum < -DELTA)
            if node["status"] == "accepted":
                accepted_bounds[(node["alpha"], node["beta"], node["sigma"])].append(maximum)
        else:
            assert node["status"] != "accepted"
    counts = data["counts"]
    assert len(nodes) == counts["visited_cells"] == EXPECTED_COUNTS["nodes"] <= 4000
    assert len(pending) == counts["pending"] == EXPECTED_COUNTS["pending"]
    for key, value in tally.items():
        assert counts.get(key, 0) == value
    for key in ("reference_cells", "cached_reference_uses", "provider_invocations", "enclosed_reference_cells",
                "cached_trial_uses", "new_target_proposals", "centered_profile_interval_bounds"):
        assert counts.get(key, 0) == tally[key] == EXPECTED_COUNTS[key]
    assert counts["reference_cells"] == counts.get("cached_reference_uses", 0)+counts.get("provider_invocations", 0) <= 2000
    assert data["new_provider_counts"] == dict(provider_counts)
    assert counts["new_reference_proposals"] == provider_counts["proposal_calls"] == EXPECTED_COUNTS["new_reference_proposals"]
    assert counts["new_reference_proposals"] <= counts.get("provider_invocations", 0)
    for key in ("accepted", "excluded", "split", "unresolved", "error"):
        assert counts.get(key, 0) == status_counts[key] == EXPECTED_COUNTS.get(key, 0)
    complete = (not pending and not status_counts["unresolved"] and not status_counts["error"]
                and data["stop_reason"] is None)
    assert data["full_domain_proved"] is complete
    assert data["status"] == ("complete centered domain comparison" if complete
                              else "bounded centered pass stopped without a full-domain conclusion")
    if complete:
        assert set(accepted_bounds) == set(itertools.product((0, 1), repeat=3))
    verify(bindings)
    verify(HELPERS)
    assert sha(ROOT/SOURCE) == EXPECTED_SOURCE_SHA256
    summaries = [{"alpha": k[0], "beta": k[1], "sigma": k[2], "accepted_cells": len(v),
                  "maximum_compensated_upper_rational": str(max(v)), "strict_gap_lower_rational": str(-max(v))}
                 for k, v in sorted(accepted_bounds.items())]
    coverage = coverage_summaries(cases, nodes, pending)
    output = {
        "status": "exact saved centered product-boundary audit passed",
        "source": SOURCE, "source_sha256": EXPECTED_SOURCE_SHA256,
        "checker_sha256": sha(Path(__file__)), "stdlib_helper_sha256": HELPERS,
        "input_bindings_checked": len(bindings), "cases_checked": 162,
        "visited_nodes": len(nodes), "pending_cells": len(pending),
        "frontier_leaves": sum(row["leaves"] for row in frontier),
        "accepted_cells": status_counts["accepted"], "strict_geometry_exclusions": status_counts["excluded"],
        "eligible_cached_references_checked": 20, "eligible_cached_trials_checked": 240,
        "cached_reference_uses_checked": tally["cached_reference_uses"],
        "cached_trial_uses_checked": tally["cached_trial_uses"],
        "new_provider_invocations_checked": tally["provider_invocations"],
        "new_reference_proposals_checked": provider_counts["proposal_calls"],
        "new_target_proposals_checked": tally["new_target_proposals"],
        "enclosed_references_checked": tally["enclosed_reference_cells"],
        "finite_profile_bounds_checked": len(finite_bounds), "mean_value_terms_checked": 10*len(finite_bounds),
        "support_terms_checked": 5*len(finite_bounds), "saved_primitive_call_totals": dict(primitive_counts),
        "saved_enclosure_call_totals": dict(enclosure_counts),
        "full_domain_proved": complete, "delta_rational": str(DELTA),
        "accepted_domain_summaries": summaries,
        "stop_reason": data["stop_reason"],
        "maximum_frontier_depth": max(row["maximum_depth"] for row in coverage),
        "profile_status_counts": dict(profile_status_counts),
        "weakest_accepted_profile": weakest_accepted,
        "worst_evaluated_profile_families": [worst_profiles[key] for key in sorted(worst_profiles)],
        "completed_chart_cases": [row["case_index"] for row in coverage if row["complete_comparison"]],
        "chart_case_coverage": coverage,
        "maximum_evaluated_compensated_upper_rational": str(max(finite_bounds)) if finite_bounds else None,
        "old_source_frontier_modified": False, "whole_source_or_knot_asymptotic_claimed": False,
        "new_root_primitive_interval_or_target_evaluations": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": output["status"], "full_domain_proved": complete,
                      "visited": len(nodes), "pending": len(pending), "finite_bounds": len(finite_bounds),
                      "sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
