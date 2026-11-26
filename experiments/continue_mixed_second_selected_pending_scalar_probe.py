#!/usr/bin/env python3
"""Pending-only reference DFS, stopping at the first finite scalar pair.

At most 2000 new beta-specific nodes and depth 28. Saved inconclusive
seeds are split without replay. No refinement after a finite pair,
irrespective of signs; no source roots or finite quantum sums.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import time
from types import SimpleNamespace

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
PRIOR = "repro/results/research-mixed-second-selected-reference-partition-attempt01.json"
CLASSIFIER = "experiments/classify_mixed_second_selected_reference_partition.py"
SCALAR = "experiments/evaluate_mixed_second_selected_directional_budget.py"
PINNED = {
    PRIOR: "b1ae0e2e5584fba31cc510a35f993fd6132a6e16ccf06011c03dcbd329f98293",
    CLASSIFIER: "2964a89859c7626b83f7e00dac9868a76697d6c78199de1d2eace884be50a5c7",
    SCALAR: "650a2a1319853df03430c267f28a5ffdc67b4bf7c7576e392cb3f22fbbe4c541",
    "notes/research_mixed_second_selected_directional_budget.md": "f74ddbea9c59685e7c6d343c7b41490c1c81520d09016664f274ff003331efd2",
    "notes/research_mixed_second_selected_directional_evaluation.md": "b92c388a7412d9309851f6c1db9c3b1ecbf0832b01a85c756e0e25c0970e45f7",
    "notes/research_mixed_second_selected_pending_scalar_probe.md": "c6e03f420a87867beabe207337540d8d318a793729c1afaae2c79d3fcc91682b",
    "notes/research_mixed_reference_shape_half_plane.md": "28c1d35c39ac2290733d6cada8e4ae1d1e6fd58ebf641c0aef9168f962e7a143",
}
MAX_VISITS, MAX_DEPTH = 2000, 28
GAP = F(1, 2000)


class NecessaryShapeExclusion(Exception):
    """A full-box shape contradicts the proved necessary negative sector."""


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fully_evaluated_pair(result):
    """Only arithmetic completeness matters; never inspect the budget signs."""
    branches = result.get("details", {}).get("branches", {})
    for label in ("forced", "factorial"):
        budget = branches.get(label, {}).get("budget", {})
        if budget.get("finite") is not True:
            return False
        try:
            lo, hi = F(budget["lower_rational"]), F(budget["upper_rational"])
        except (KeyError, ValueError, ZeroDivisionError):
            return False
        if lo > hi:
            return False
    return True


def load_inputs():
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("frozen continuation input mismatch: "+name)
    prior = json.loads((ROOT/PRIOR).read_text())
    if prior["status"] != "reference partition pass complete":
        raise ValueError("prior reference partition is incomplete")
    for name, expected in prior["input_sha256"].items():
        path = Path(name)
        relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
        if relative in bindings and bindings[relative] != expected:
            raise ValueError("conflicting prior binding: "+relative)
        bindings[relative] = expected
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("pre-import continuation dependency mismatch: "+name)
    classifier = importlib.import_module("classify_mixed_second_selected_reference_partition")
    shifted, old, exact, previous, old_excluded, old_candidates, inherited = classifier.inputs()
    for name, expected in inherited.items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting inherited binding: "+name)
        bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("final pre-import dependency mismatch: "+name)
    four = importlib.import_module("diagnose_mixed_four_four_half_row_budget")
    root_box = tuple(map(F, prior["initial_auxiliary_rectangle"]))
    if root_box != four.BASE.ROOT:
        raise ValueError("original root rectangle mismatch")
    def decode(address):
        box = root_box
        for depth, branch in enumerate(address):
            box = four.BASE.split(box, depth)[int(branch)]
        return box
    if prior["inherited_excluded_leaves"] != old_excluded:
        raise ValueError("prior inherited exclusions changed")
    cells = prior["candidate_cells"]
    if len(cells) != 678 or [cell["address"] for cell in cells] != [leaf["address"] for leaf in old_candidates]:
        raise ValueError("prior candidate inventory changed")
    fixed = {beta: [{"address": leaf["address"], "source": "inherited exclusion", "reason": leaf["reason"]}
                    for leaf in old_excluded] for beta in (0, 1)}
    seeds = []
    for cell, old_leaf in zip(cells, old_candidates):
        if tuple(map(F, cell["box"])) != decode(cell["address"]):
            raise ValueError("prior candidate box mismatch")
        if cell["original_leaf_sha256"] != canonical_hash(old_leaf):
            raise ValueError("prior original-leaf binding mismatch")
        for beta in (0, 1):
            case = cell["cases"][str(beta)]
            if case["status"] == "excluded":
                fixed[beta].append({"address": cell["address"], "source": "first-pass exclusion",
                                    "reason": case["reason"], "prior_case_sha256": canonical_hash(case)})
            elif case["status"] == "inconclusive":
                seeds.append({"beta": beta, "address": cell["address"], "box": cell["box"],
                              "prior_case_sha256": canonical_hash(case), "prior_reason": case["reason"]})
            else:
                raise ValueError("unexpected prior reference status")
    seeds.sort(key=lambda row: (row["address"], row["beta"]))
    for beta, expected_count, expected_mass in ((0, 88, F(223, 65536)), (1, 121, F(607, 131072))):
        selected = [seed for seed in seeds if seed["beta"] == beta]
        if len(selected) != expected_count or sum((F(1, 2**len(seed["address"])) for seed in selected), F(0)) != expected_mass:
            raise ValueError("prior pending frontier mismatch")
        classifier.validate_partition([leaf["address"] for leaf in fixed[beta]]+[seed["address"] for seed in selected])
    return classifier, shifted, old, four, exact, root_box, fixed, seeds, bindings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    classifier, shifted, old, four, exact, root_box, fixed, seeds, bindings = load_inputs()
    directional = importlib.import_module("evaluate_mixed_second_selected_directional_budget")
    def forbidden(*args, **kwargs):
        raise RuntimeError("old inspect/main/reference callback forbidden")
    for provider in (classifier, shifted, old, four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = forbidden
    four.reference_four = four.frozen.reference = forbidden
    # Original centered g and old.Evaluator.conjugate are deliberately permitted.
    ctx.prec = 160
    reference_primitive = SimpleNamespace(pi=arb.pi(), ii=acb(0, 1))
    BaseProvider = classifier.make_evaluator(shifted, old)

    class Provider(BaseProvider):
        def rational_map(self, name):
            value = super().rational_map(name)
            if name not in ("E", "A", "U", "Z", "V", "B0", "C0", "B1", "C1"):
                raise RuntimeError("uniform shape sector applied to an unknown map")
            lo = self.f.lower(value.imag)
            excluded = lo > F(-3, 20)
            self.details.setdefault("uniform_shape_sector_tests", []).append({
                "map": name, "shape": self.f.complex_record(value),
                "imaginary_lower_rational": str(lo), "strict_necessary_threshold": "-3/20",
                "excluded": excluded})
            self.counts["uniform_shape_sector_tests"] += 1
            if excluded:
                raise NecessaryShapeExclusion(name+" imaginary lower endpoint exceeds -3/20")
            return value

    Primitive = old.make_primitive_class(four)
    initial_children, initial_splits = [], []
    for seed in seeds:
        if len(seed["address"]) >= MAX_DEPTH:
            raise ValueError("saved seed has no permitted initial split")
        children = four.BASE.split(tuple(map(F, seed["box"])), len(seed["address"]))
        addresses = []
        for branch, box in enumerate(children):
            address = seed["address"]+str(branch)
            addresses.append(address)
            initial_children.append({"beta": seed["beta"], "address": address,
                                     "box": list(map(str, box)), "seed_address": seed["address"]})
        initial_splits.append({"beta": seed["beta"], "address": seed["address"], "children": addresses})
    stack = list(reversed(initial_children))
    nodes, terminals, depth_limited, transports = [], [], [], {}
    visited = set()
    reference_counts, scalar_counts = Counter(), Counter()
    stop_reason, evaluated_pair_index = "visit cap", None
    fixed_hashes = {str(beta): canonical_hash(fixed[beta]) for beta in (0, 1)}
    started = time.monotonic()

    def merge_transport(address, shared):
        if address not in transports:
            transports[address] = shared
            return address
        current = transports[address]
        compatible = True
        for key, value in shared.items():
            if key in ("maps", "polynomials"):
                for name, item in value.items():
                    if name in current.get(key, {}) and current[key][name] != item:
                        compatible = False
            elif key in current and current[key] != value:
                compatible = False
        if not compatible:
            identifier = address+"@"+canonical_hash(shared)
            transports[identifier] = shared
            return identifier
        for key, value in shared.items():
            if key in ("maps", "polynomials"):
                current.setdefault(key, {}).update(value)
            else:
                current[key] = value
        return address

    while stack and len(nodes) < MAX_VISITS:
        item = stack.pop()
        key = (item["beta"], item["address"])
        if key in visited or any(key == (seed["beta"], seed["address"]) for seed in seeds):
            raise RuntimeError("duplicate or saved-seed reference replay")
        visited.add(key)
        node = {**item, "transport_address": item["address"]}
        index = len(nodes)
        nodes.append(node)
        evaluator = Provider(four, reference_primitive, exact)
        details = {}
        fatal = False
        try:
            try:
                state, reason, reference = evaluator.reference(tuple(map(F, item["box"])), item["beta"], details)
            except NecessaryShapeExclusion as error:
                state, reason, reference = "excluded", str(error), None
            except four.frozen.Inconclusive as error:
                state, reason, reference = "inconclusive", str(error), None
            node["reference"] = {"status": state, "reason": reason, "details": details}
            split_reason = "reference arithmetic inconclusive"
            if state == "retained":
                shapes, coordinates = reference
                primitive = Primitive()
                scalar_evaluator = old.Evaluator(four, primitive)
                try:
                    node["scalar"] = directional.evaluate_reference(scalar_evaluator, shapes, coordinates, item["beta"], GAP)
                finally:
                    counts = scalar_evaluator.counts+primitive.counts
                    node["scalar_call_counts"] = dict(counts)
                    scalar_counts.update(counts)
                if (counts["directional_reference_attempts"] != 1 or counts["directional_branch_attempts"] > 2
                        or counts["node_conjugates"] > 3 or counts["edge_conjugates"] != 0
                        or counts["centered_primitive_calls"] > 12):
                    raise RuntimeError("frozen scalar callback count exceeded")
                if fully_evaluated_pair(node["scalar"]):
                    node["action"] = "stop at fully evaluated scalar pair"
                    evaluated_pair_index, stop_reason = index, "first fully evaluated scalar pair"
                    terminals.append({"beta": item["beta"], "address": item["address"],
                                      "status": "scalar pair evaluated", "node_index": index})
                else:
                    split_reason = "scalar arithmetic inconclusive before both finite branches"
            if evaluated_pair_index is None:
                if state == "excluded":
                    node["action"] = "excluded"
                    terminals.append({"beta": item["beta"], "address": item["address"],
                                      "status": "excluded", "node_index": index})
                elif len(item["address"]) < MAX_DEPTH:
                    boxes = four.BASE.split(tuple(map(F, item["box"])), len(item["address"]))
                    children = [{"beta": item["beta"], "address": item["address"]+str(branch),
                                 "box": list(map(str, box)), "seed_address": item["seed_address"]}
                                for branch, box in enumerate(boxes)]
                    stack.extend(reversed(children))
                    node.update({"action": "split", "split_reason": split_reason,
                                 "children": [child["address"] for child in children]})
                else:
                    node.update({"action": "depth limit", "unresolved_reason": split_reason})
                    depth_limited.append({**item, "node_index": index, "status": "unresolved depth limit"})
        except Exception as error:
            node.update({"action": "unexpected error", "error": repr(error)})
            node.setdefault("reference", {"status": "inconclusive", "reason": "unexpected error", "details": details})
            terminals.append({"beta": item["beta"], "address": item["address"],
                              "status": "unresolved unexpected error", "node_index": index})
            fatal, stop_reason = True, "unexpected error"
        node["reference_call_counts"] = dict(evaluator.counts)
        reference_counts.update(evaluator.counts)
        for name, limit in classifier.CELL_LIMITS.items():
            if evaluator.counts[name] > (1 if name == "reference_calls" else limit):
                fatal, stop_reason = True, "reference operation cap exceeded: "+name
        node["transport_address"] = merge_transport(item["address"], evaluator.shared)
        if len(nodes) % 20 == 0 or fatal or evaluated_pair_index is not None:
            print(json.dumps({"new_visits": len(nodes), "maximum_visits": MAX_VISITS,
                "pending_frontier": len(stack), "depth_limit_leaves": len(depth_limited),
                "reference_statuses": dict(Counter(n["reference"]["status"] for n in nodes)),
                "scalar_attempts": scalar_counts["directional_reference_attempts"],
                "fully_evaluated_pair": evaluated_pair_index is not None,
                "elapsed_seconds": time.monotonic()-started}), flush=True)
        if fatal or evaluated_pair_index is not None:
            break
    if not stack and evaluated_pair_index is None and stop_reason == "visit cap":
        stop_reason = "frontier exhausted with depth-limit cases" if depth_limited else "frontier exhausted"
    if {str(beta): canonical_hash(fixed[beta]) for beta in (0, 1)} != fixed_hashes:
        raise RuntimeError("fixed prior exclusions changed")
    def decode(address):
        box = root_box
        for depth, branch in enumerate(address):
            box = four.BASE.split(box, depth)[int(branch)]
        return box
    for item in nodes+stack+depth_limited:
        if tuple(map(F, item["box"])) != decode(item["address"]) or len(item["address"]) > MAX_DEPTH:
            raise RuntimeError("new descendant rectangle/depth mismatch")
    coverage = {}
    for beta in (0, 1):
        leaves = [{"address": leaf["address"], "status": "fixed prior exclusion"} for leaf in fixed[beta]]
        leaves += [leaf for leaf in terminals+depth_limited if leaf["beta"] == beta]
        leaves += [{"address": leaf["address"], "status": "unvisited pending"} for leaf in stack if leaf["beta"] == beta]
        classifier.validate_partition([leaf["address"] for leaf in leaves])
        counts, masses = Counter(), {}
        for leaf in leaves:
            status = leaf["status"]
            counts[status] += 1
            masses[status] = masses.get(status, F(0))+F(1, 2**len(leaf["address"]))
        coverage[str(beta)] = {"counts": dict(counts), "dyadic_masses": {name: str(value) for name, value in masses.items()}}
    if len(nodes) > MAX_VISITS or reference_counts["reference_calls"] != len(nodes):
        raise RuntimeError("visit/reference call bound mismatch")
    for node in nodes:
        if "scalar" in node and fully_evaluated_pair(node["scalar"]) and node["action"] != "stop at fully evaluated scalar pair":
            raise RuntimeError("finite scalar pair was refined or bypassed")
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise RuntimeError("input changed during continuation: "+name)
    result = {"status": "bounded continuation stopped", "stop_reason": stop_reason,
        "scope": "pending-only reference arithmetic, ending at one finite directional scalar pair or a bound",
        "prior_record": PRIOR, "prior_record_sha256": PINNED[PRIOR],
        "initial_auxiliary_rectangle": list(map(str, root_box)),
        "fixed_prior_exclusion_counts": {str(beta): len(fixed[beta]) for beta in (0, 1)},
        "fixed_prior_exclusion_canonical_sha256": fixed_hashes,
        "initial_seeds": seeds, "initial_splits_without_replay": initial_splits,
        "new_nodes": nodes, "shared_transports_by_address": transports,
        "new_terminal_leaves": terminals, "depth_limit_leaves": depth_limited,
        "pending_frontier_stack_next_is_last": stack, "coverage_by_beta": coverage,
        "terminal_partition_verified": True, "fully_evaluated_pair_node_index": evaluated_pair_index,
        "maximum_new_visits": MAX_VISITS, "maximum_depth": MAX_DEPTH, "precision_bits": 160,
        "reference_call_counts": dict(reference_counts), "scalar_call_counts": dict(scalar_counts),
        "saved_seed_reference_replays": 0, "old_inspect_calls": 0, "old_main_calls": 0,
        "source_root_evaluations": 0, "finite_source_evaluations": 0,
        "bound_sign_driven_subdivisions": 0, "automatic_retries": 0,
        "uniform_scalar_sign_claimed": False, "word_realization_claimed": False,
        "elapsed_seconds": time.monotonic()-started, "input_sha256": bindings}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, separators=(",", ":"))+"\n")
    print(json.dumps({"status": result["status"], "stop_reason": stop_reason,
        "new_visits": len(nodes), "scalar_attempts": scalar_counts["directional_reference_attempts"],
        "fully_evaluated_pair_node_index": evaluated_pair_index, "coverage_by_beta": coverage,
        "elapsed_seconds": result["elapsed_seconds"], "result_sha256": sha(args.output)}), flush=True)


if __name__ == "__main__":
    main()
