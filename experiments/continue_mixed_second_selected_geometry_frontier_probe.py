#!/usr/bin/env python3
"""Resume the 349 unvisited leaves, with exact Cartesian disk filters.

At most 2000 new beta-specific nodes and depth 28. Preserve all prior
exclusions, including saved node 288. Stop at the first finite scalar
pair irrespective of signs; no source roots or finite quantum sums.
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
PRIOR = "repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json"
GEOMETRY = "repro/results/research-mixed-second-selected-saved-cell-geometric-exclusion.json"
PREVIOUS_DRIVER = "experiments/continue_mixed_second_selected_pending_scalar_probe.py"
SCALAR = "experiments/evaluate_mixed_second_selected_directional_budget.py"
PINNED = {
    PRIOR: "2f7640e7aefc655628b134ac50500e03b0971f2768b8f73c0df36a00b74b0f3c",
    GEOMETRY: "5326a8474727aba2516a9623c43a8bddc9ef167b07e356bc79c0e89a6bc7f400",
    PREVIOUS_DRIVER: "cc6eb2633994a430113839943d6948d90b69cfd27dfcb740a15631b4e724a2fc",
    SCALAR: "650a2a1319853df03430c267f28a5ffdc67b4bf7c7576e392cb3f22fbbe4c541",
    "notes/research_mixed_second_selected_geometry_frontier_probe.md": "3cbbd59f7ea7a4d7ac3ee8eda748951f02926b976163251d5b40106ed9798c6b",
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


class NecessaryGeometryExclusion(Exception):
    """A decoded full rectangle contradicts a necessary typed domain."""


def make_evaluator(classifier, shifted, old):
    Base = classifier.make_evaluator(shifted, old)

    class GeometryReference(Base):
        def rational_map(self, name):
            value = super().rational_map(name)
            if name not in ("E", "A", "U", "Z", "V", "B0", "C0", "B1", "C1"):
                raise RuntimeError("negative-shape sector applied to an unknown map")
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

        def disk_test(self, value, kind, label):
            a, b, radius = ((F(7, 20), F(-1, 100), F(83, 1000)) if kind == 3
                            else (F(3, 10), F(-13, 250), F(3, 50)))
            x_lo, x_hi = self.f.lower(value.real), self.f.upper(value.real)
            y_lo, y_hi = self.f.lower(value.imag), self.f.upper(value.imag)
            dx = max(F(0), x_lo-a, a-x_hi)
            dy = max(F(0), y_lo-b, b-y_hi)
            excess = dx**2+dy**2-radius**2
            self.details.setdefault("exact_cartesian_disk_tests", []).append({
                "label": label, "kind": kind, "full_decoded_coordinate": self.f.complex_record(value),
                "center_real_rational": str(a), "center_imag_rational": str(b),
                "radius_rational": str(radius), "horizontal_distance_rational": str(dx),
                "vertical_distance_rational": str(dy), "squared_excess_rational": str(excess),
                "strictly_excluded": excess > 0})
            self.counts["exact_cartesian_disk_tests"] += 1
            return excess > 0

        def finite(self, value, label):
            value = super().finite(value, label)
            suffix = " decoded coordinate"
            if not label.endswith(suffix):
                return value
            key = label[:-len(suffix)]
            if key == "e":
                return value
            if key in ("a", "u", "z", "v", "b"):
                kind = 3+self.current_beta if key in ("v", "b") else 4
                if self.disk_test(value, kind, key):
                    raise NecessaryGeometryExclusion(key+" exact Cartesian disk separation")
            elif key == "c":
                x_lo, y_lo, y_hi = (self.f.lower(value.real), self.f.lower(value.imag),
                                   self.f.upper(value.imag))
                typed = {}
                self.exact_external_types = []
                for kind, floor, ceiling in ((3, F(-9, 125), F(17, 250)),
                                             (4, F(-27, 250), F(-1, 1000))):
                    disk_excluded = self.disk_test(value, kind, "c type "+str(kind))
                    below, above = y_hi < floor, y_lo > ceiling
                    oblique_lower = x_lo-3*y_hi if kind == 3 else None
                    oblique = kind == 3 and oblique_lower > F(76, 125)
                    excluded = disk_excluded or below or above or oblique
                    typed[str(kind)] = {"disk_excluded": disk_excluded,
                        "height_lower_rational": str(y_lo), "height_upper_rational": str(y_hi),
                        "necessary_height_floor_rational": str(floor),
                        "necessary_height_ceiling_rational": str(ceiling),
                        "below_height_floor": below, "above_height_ceiling": above,
                        "oblique_lower_rational": None if oblique_lower is None else str(oblique_lower),
                        "oblique_ceiling_rational": "76/125" if kind == 3 else None,
                        "above_oblique_ceiling": oblique, "excluded": excluded}
                    if not excluded:
                        self.exact_external_types.append(kind)
                self.details["exact_external_geometry"] = typed
                self.details["exact_external_type_alternatives"] = self.exact_external_types
                if not self.exact_external_types:
                    raise NecessaryGeometryExclusion("both external types excluded by exact Cartesian geometry")
            else:
                raise RuntimeError("unexpected decoded coordinate label: "+label)
            return value

        def original_regularity(self, shapes):
            before = self.details["next_external_type_alternatives"]
            combined = [kind for kind in before if kind in self.exact_external_types]
            self.details["inherited_next_external_types_before_exact_intersection"] = before
            self.details["next_external_type_alternatives"] = combined
            if not combined:
                raise NecessaryGeometryExclusion("exact external types and typed internal sums have empty intersection")
            return super().original_regularity(shapes)

        def reference(self, box, beta, details):
            self.current_beta, self.exact_external_types = beta, None
            return super().reference(box, beta, details)

    return GeometryReference


def load_inputs():
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("frozen geometry-continuation input mismatch: "+name)
    previous, geometric = (json.loads((ROOT/name).read_text()) for name in (PRIOR, GEOMETRY))
    for source in (previous, geometric):
        for name, expected in source["input_sha256"].items():
            path = Path(name)
            relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
            if relative in bindings and bindings[relative] != expected:
                raise ValueError("conflicting inherited geometry binding: "+relative)
            bindings[relative] = expected
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("pre-import geometry dependency mismatch: "+name)
    prior_driver = importlib.import_module("continue_mixed_second_selected_pending_scalar_probe")
    classifier, shifted, old, four, exact, root_box, fixed, _, inherited = prior_driver.load_inputs()
    if tuple(map(F, previous["initial_auxiliary_rectangle"])) != root_box:
        raise ValueError("prior original rectangle mismatch")
    for name, expected in inherited.items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting first-pass binding: "+name)
        bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("final pre-evaluation dependency mismatch: "+name)
    if previous["stop_reason"] != "first fully evaluated scalar pair" or previous["fully_evaluated_pair_node_index"] != 288:
        raise ValueError("unexpected prior scalar stopping state")
    if previous["depth_limit_leaves"] or len(previous["new_nodes"]) != 289:
        raise ValueError("unexpected prior visit/depth inventory")
    if geometric["source_record_sha256"] != PINNED[PRIOR] or geometric["source_node_index"] != 288:
        raise ValueError("saved geometry does not bind the prior terminal scalar cell")
    scalar_node = previous["new_nodes"][288]
    if (geometric["source_node_canonical_sha256"] != canonical_hash(scalar_node)
            or not geometric["both_next_external_types_excluded"]
            or geometric["address"] != scalar_node["address"] or geometric["beta"] != 0):
        raise ValueError("saved geometric exclusion identity mismatch")
    for beta in (0, 1):
        if canonical_hash(fixed[beta]) != previous["fixed_prior_exclusion_canonical_sha256"][str(beta)]:
            raise ValueError("old fixed exclusions changed")
    prior_visited = {(node["beta"], node["address"]) for node in previous["new_nodes"]}
    if len(prior_visited) != 289:
        raise ValueError("prior visits are not unique")
    for leaf in previous["new_terminal_leaves"]:
        node = previous["new_nodes"][leaf["node_index"]]
        if (leaf["beta"], leaf["address"]) != (node["beta"], node["address"]):
            raise ValueError("prior terminal provenance mismatch")
        if leaf["status"] == "excluded":
            if node["reference"]["status"] != "excluded" or node["action"] != "excluded":
                raise ValueError("prior terminal exclusion mismatch")
            entry = {"address": leaf["address"], "source": "first scalar probe exclusion",
                     "reason": node["reference"]["reason"], "prior_node_sha256": canonical_hash(node)}
        elif leaf["status"] == "scalar pair evaluated" and leaf["node_index"] == 288:
            entry = {"address": leaf["address"], "source": "saved-cell geometric exclusion",
                     "saved_exclusion_sha256": PINNED[GEOMETRY], "prior_node_sha256": canonical_hash(node)}
        else:
            raise ValueError("unexpected old terminal leaf")
        fixed[leaf["beta"]].append(entry)
    source_frontier = previous["pending_frontier_stack_next_is_last"]
    if (len(source_frontier) != 349 or canonical_hash(source_frontier)
            != geometric["unchanged_pending_frontier_canonical_sha256"]):
        raise ValueError("saved 349-leaf frontier mismatch")
    def decode(address):
        box = root_box
        for depth, branch in enumerate(address):
            box = four.BASE.split(box, depth)[int(branch)]
        return box
    initial_frontier = []
    for item in source_frontier:
        if ((item["beta"], item["address"]) in prior_visited or tuple(map(F, item["box"])) != decode(item["address"])
                or len(item["address"]) > MAX_DEPTH):
            raise ValueError("initial frontier is visited or has wrong rectangle/depth")
        initial_frontier.append({**item, "continuation_seed_address": item["address"]})
    for beta, fixed_count, pending_count, pending_mass in ((0, 3335, 143, F(6605, 2097152)),
                                                          (1, 3217, 206, F(285, 65536))):
        selected = [leaf for leaf in initial_frontier if leaf["beta"] == beta]
        if (len(fixed[beta]) != fixed_count or len(selected) != pending_count
                or sum((F(1, 2**len(leaf["address"])) for leaf in selected), F(0)) != pending_mass):
            raise ValueError("initial geometry-frontier counts/mass mismatch")
        classifier.validate_partition([leaf["address"] for leaf in fixed[beta]]+[leaf["address"] for leaf in selected])
    return classifier, shifted, old, four, exact, root_box, fixed, initial_frontier, bindings, prior_visited


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    classifier, shifted, old, four, exact, root_box, fixed, initial_frontier, bindings, prior_visited = load_inputs()
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
    Provider = make_evaluator(classifier, shifted, old)
    Primitive = old.make_primitive_class(four)
    stack = [dict(item) for item in initial_frontier]
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
        if key in visited or key in prior_visited:
            raise RuntimeError("duplicate or previously visited reference replay")
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
            except (NecessaryShapeExclusion, NecessaryGeometryExclusion) as error:
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
                                 "box": list(map(str, box)), "seed_address": item["seed_address"],
                                 "continuation_seed_address": item["continuation_seed_address"]}
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
        if evaluator.counts["exact_cartesian_disk_tests"] > 7 or evaluator.counts["uniform_shape_sector_tests"] > 7:
            fatal, stop_reason = True, "necessary geometry operation cap exceeded"
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
        seed_key = (item["beta"], item["continuation_seed_address"])
        if (seed_key not in {(leaf["beta"], leaf["address"]) for leaf in initial_frontier}
                or not item["address"].startswith(item["continuation_seed_address"])):
            raise RuntimeError("new node is outside its initial pending leaf")
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
    result = {"status": "bounded geometry continuation stopped", "stop_reason": stop_reason,
        "scope": "saved 349-leaf frontier with exact disk exclusions, ending at one finite generic scalar pair or a bound",
        "alpha": 1, "beta_candidates": [0, 1],
        "prior_record": PRIOR, "prior_record_sha256": PINNED[PRIOR],
        "initial_auxiliary_rectangle": list(map(str, root_box)),
        "fixed_prior_exclusion_counts": {str(beta): len(fixed[beta]) for beta in (0, 1)},
        "fixed_prior_exclusion_canonical_sha256": fixed_hashes,
        "initial_unvisited_frontier_stack_next_is_last": initial_frontier,
        "initial_frontier_leaf_count": 349,
        "saved_geometry_exclusion_record": GEOMETRY, "saved_geometry_exclusion_sha256": PINNED[GEOMETRY],
        "new_nodes": nodes, "shared_transports_by_address": transports,
        "new_terminal_leaves": terminals, "depth_limit_leaves": depth_limited,
        "pending_frontier_stack_next_is_last": stack, "coverage_by_beta": coverage,
        "terminal_partition_verified": True, "fully_evaluated_pair_node_index": evaluated_pair_index,
        "maximum_new_visits": MAX_VISITS, "maximum_depth": MAX_DEPTH, "precision_bits": 160,
        "reference_call_counts": dict(reference_counts), "scalar_call_counts": dict(scalar_counts),
        "previously_visited_reference_replays": 0, "initial_frontier_presplits": 0, "old_inspect_calls": 0, "old_main_calls": 0,
        "source_root_evaluations": 0, "finite_source_evaluations": 0,
        "bound_sign_driven_subdivisions": 0, "automatic_retries": 0,
        "local_curvature_evaluator_used": False, "uniform_scalar_sign_claimed": False, "word_realization_claimed": False,
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
