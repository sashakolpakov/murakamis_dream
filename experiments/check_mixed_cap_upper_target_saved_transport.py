#!/usr/bin/env python3
"""Fixed exact extraction of old cap-current reserves; no analytic imports."""

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import re
import traceback

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json"
REPLAY = "repro/results/research-mixed-first-cap-coupled-plateau-replay.json"
ROOT_AUTHOR = "repro/results/research-mixed-open-word-critical-localization.json"
ROOT_REPLAY = "repro/results/research-mixed-open-word-critical-localization-replay.json"
PROTOCOL = "notes/research_mixed_cap_upper_target_saved_transport_protocol.md"
THEORY = "notes/research_mixed_cap_upper_target_current_transport.md"
OLD_PROOF = "notes/research_mixed_first_cap_coupled_plateau_certificate.md"
OLD_SCRIPT = "experiments/continue_mixed_first_cap_coupled_plateau.py"
PINNED = {
    AUTHOR: "1e7ecb710244d417de75d794688e8786153fa82355b3d73b6811621130e1c54c",
    REPLAY: "d1cc89d4ff8c249f2b4bc4b72e79842ca6151450518d99f00f28498d3edd912e",
    PROTOCOL: "dd680cdd7cc6191c22da11e82a48957b4213dbdb61f1f1bff1d0178513fdc7d3",
    THEORY: "9efc6fd503722791d6ddc67db2f13529f23750520c8fb52b1cb74bbf3ba52d60",
    OLD_PROOF: "cc56f9b28371f1829f9f1a54491d340d8364a1c680f43bee24d54da88d94267a",
    OLD_SCRIPT: "eb676b2736b953700d1542a40f944ec20a5427aab404935a5373d6b6a26cf8cb",
    "notes/research_mixed_first_cap_plateau_completion.md":
        "4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d",
    "notes/research_mixed_cap_upper_target_extension.md":
        "c705f72cbfaac8dc920ce48a4f6ea0402f15449f3ba4af202a04c5015cf2d46e",
    "notes/research_mixed_boundary_window_real_color_envelopes.md":
        "727aa6b7b477e3a984da4241d3ac9356858553e8aae74752bcf930a74abecd4b",
}
FAMILY_NAMES = ("left_cut", "right_cut", "lower_alias", "upper_alias")
COSTS = ((F(1, 25), F(0), F(1, 25), F(1, 20)),
         (F(0), F(0), F(0), F(11, 875)))
EXPECTED_FAMILIES = [
    {"kind": "cut", "private_real": "27/100", "private_height": "0",
     "penalty_over_pi": "0"},
    {"kind": "cut", "private_real": "49/100", "private_height": "0",
     "penalty_over_pi": "0"},
    {"kind": "alias", "private_real": None, "private_height": "-11/200",
     "penalty_over_pi": "11/100"},
    {"kind": "alias", "private_real": None, "private_height": "1/25",
     "penalty_over_pi": "2/25"},
]
RULES = ["original_full_disk_v1", "lower_height_v1", "typed_disk_v1",
         "adjacent_four_v1", "coupled_actual_v1"]
ALLOWED = (set("SXL"), set("SXHL"), set("SXHRUL"),
           set("SXHRUAL"), set("SXHRUAFL"))
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
BALL = re.compile(r"\[\s*(" + NUMBER + r")\s*\+/-\s*(" + NUMBER + r")\s*\]")
DECIMAL = re.compile(NUMBER)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def display_upper(value):
    """The displayed ball encloses the stored Arb maximum; never discard radius."""
    require(isinstance(value, str), "non-string Arb display")
    value = value.strip()
    match = BALL.fullmatch(value)
    if match:
        midpoint, radius = map(F, match.groups())
        require(radius >= 0, "negative displayed radius")
        return midpoint + radius, midpoint, radius
    require(DECIMAL.fullmatch(value) is not None, "unsupported Arb display: " + value)
    return F(value), F(value), F(0)


def split(box, axis):
    lo, hi = box[axis]
    midpoint = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis], right[axis] = (lo, midpoint), (midpoint, hi)
    return left, right


def prefix_tree(record, job):
    if job < len(record["completed"]):
        return record["completed"][job]
    active = record["active"]
    if active is not None and active["job"] == job:
        return active["tree"]
    return []


def original_cells(record):
    domains = record["domains"]
    require([(d["epsilon"], d["neighbor_epsilon"]) for d in domains]
            == [(0, 0), (0, 1), (1, 0), (1, 1)], "root domain order")
    cells, coverage = [], []
    for domain_index, domain in enumerate(domains):
        pending = [([(F(-1), F(1)), (F(-1), F(1))], 0, "")]
        leaves = excluded = 0
        mass = F(0)
        for node_index, node in enumerate(domain["tree"]):
            require(bool(pending), "root tree overrun")
            box, depth, address = pending.pop()
            require(isinstance(node, list) and node, "root node shape")
            if node[0] == "S":
                require(len(node) == 2 and node[1] == depth % 2, "root split axis")
                left, right = split(box, node[1])
                pending.extend([(left, depth + 1, address + "0"),
                                (right, depth + 1, address + "1")])
            else:
                mass += F(1, 2 ** depth)
                if node[0] == "X":
                    require(len(node) == 1, "root exclusion shape")
                    excluded += 1
                else:
                    require(node[0] == "L" and len(node) == 2, "root leaf shape")
                    leaves += 1
                    cells.append({"domain_index": domain_index, "node_index": node_index,
                                  "address": address, "box": box, "own": domain["epsilon"],
                                  "neighbor": domain["neighbor_epsilon"]})
        require(not pending and mass == 1, "incomplete root partition")
        require((leaves, excluded) == (domain["leaves"], domain["excluded"]),
                "root leaf/exclusion counts")
        coverage.append({"domain_index": domain_index, "own": domain["epsilon"],
                         "neighbor": domain["neighbor_epsilon"], "leaves": leaves,
                         "excluded": excluded, "partition_mass": str(mass)})
    require(len(cells) == 5258, "original reference-cell count")
    return cells, coverage


def source_tree(tree, cell, family, job, ancestors, summary):
    prefixes = [prefix_tree(record, job) for record in ancestors]
    for before, after in zip(prefixes, prefixes[1:] + [tree]):
        require(after[:len(before)] == before, "changed inherited source prefix")
    pending = [(cell["box"], 0, "")]
    leaves = [0] * 5
    excluded = {name: 0 for name in "XHRUAF"}
    mass = F(0)
    max_depth = 0
    for index, node in enumerate(tree):
        require(bool(pending), "source tree overrun")
        box, depth, address = pending.pop()
        max_depth = max(max_depth, depth)
        tier = next((j for j, prior in enumerate(prefixes) if index < len(prior)), 4)
        require(isinstance(node, list) and node and node[0] in ALLOWED[tier],
                "source node/tier mismatch")
        kind = node[0]
        if kind == "S":
            require(len(node) == 2 and node[1] in (0, 1), "source split")
            left, right = split(box, node[1])
            pending.extend([(left, depth + 1, address + "0"),
                            (right, depth + 1, address + "1")])
            continue
        mass += F(1, 2 ** depth)
        if kind == "L":
            require(len(node) == 2 and isinstance(node[1], list), "source leaf")
            trial = node[1]
            require(len(trial) == (1 if family < 2 else 2), "target dimension")
            for value, (lo, hi) in zip(trial, [(F(22, 100), F(45, 100)),
                                              (F(27, 100), F(49, 100))]):
                require(isinstance(value, str) and str(F(value)) == value,
                        "noncanonical saved target")
                require(lo <= F(value) <= hi, "target outside original interval")
            leaves[tier] += 1
        elif kind == "F":
            require(tier == 4 and (cell["own"], cell["neighbor"]) == (1, 1),
                    "coupled exclusion scope")
            require(len(node) == 2 and set(node[1]) == {"m2", "m3"},
                    "coupled length-case witnesses")
            require(node[1]["m2"] in {"attached_real_floor", "attached_fixed_point"}
                    and node[1]["m3"] in {"opposite_half_plane", "external_half_plane",
                                         "opposite_outside_P4", "external_outside_both_P"},
                    "coupled exclusion reason")
            excluded[kind] += 1
        else:
            require(len(node) == 1, "geometric exclusion shape")
            excluded[kind] += 1
    require(not pending and mass == 1, "incomplete source partition")
    require(summary["job"] == job and summary["nodes"] == len(tree)
            and summary["leaves_by_tier"] == leaves
            and summary["exclusions"] == excluded, "saved replay count association")
    require((summary["maximum_upper"] is None) == (sum(leaves) == 0),
            "source maximum/null coverage")
    return {"nodes": len(tree), "leaves_by_tier": leaves, "exclusions": excluded,
            "maximum_depth": max_depth, "partition_mass": str(mass)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), "output must be fresh")
    require(args.output.resolve() not in {(ROOT / p).resolve() for p in PINNED},
            "output equals input")
    bindings = dict(PINNED)
    self_path = Path(__file__).resolve()
    bindings[str(self_path.relative_to(ROOT))] = sha(self_path)
    cache = {}
    rows = []
    active_job = None
    output = {
        "schema": "mixed-cap-upper-target-saved-transport-v1",
        "status": "running", "complete_coverage": False, "all_current_signs_proved": False,
        "job_count_expected": 21032, "jobs": rows, "family_results": [],
        "counts": {"analytic_calls": 0, "root_calls": 0, "optimizer_calls": 0,
                   "new_gain_calls": 0, "source_replays": 0, "new_parameter_cells": 0,
                   "refinements": 0, "retries": 0},
        "scope": "Original fixed-height cap cuts/aliases through y=1/2 only; "
                 "no extreme-row, height-taper, full boundary-source or knot conclusion.",
    }

    def verify():
        for name, digest in bindings.items():
            require(sha(ROOT / name) == digest, "changed binding: " + name)

    def load(name):
        require(name in bindings, "unbound record: " + name)
        if name not in cache:
            cache[name] = json.loads((ROOT / name).read_text())
        return cache[name]

    try:
        verify()
        author, replay = load(AUTHOR), load(REPLAY)
        for record in (author, replay):
            require(record["status"] == "passed" and record["fatal_error"] is None
                    and record["final_bindings_verified"], "original completion status")
            require(record["format_version"] == 5 and record["job_count"] == 21032
                    and record["original_endpoint_cells"] == 5258
                    and record["face_families_per_cell"] == 4, "original inventory")
            require(record["proof_sha256"] == PINNED[OLD_PROOF]
                    and record["script_sha256"] == PINNED[OLD_SCRIPT], "original code/proof")
            require(record["families"] == EXPECTED_FAMILIES
                    and record["acceptance_rules"] == RULES, "family/rule order")
            require(record["active"] is None and len(record["completed"]) == 21032,
                    "original unfinished frontier")
            for name, digest in record["dependencies_sha256"].items():
                require(name not in bindings or bindings[name] == digest, "binding conflict")
                bindings[name] = digest
        require(author["dependencies_sha256"] == replay["dependencies_sha256"],
                "original binding manifests differ")
        verify()
        require(replay["input_sha256"] == PINNED[AUTHOR]
                and replay["completed"] == author["completed"]
                and replay["reference_domains"] == author["reference_domains"]
                and replay["stage_provenance"] == author["stage_provenance"],
                "source/replay association")
        require(replay["precision_bits"] == 320 and replay["target_proposals"] == 0
                and replay["root_proposals"] == 0 and replay["refinements"] == 0,
                "original replay policy")
        require(F(author["gap"]) == F(1, 200000)
                and F(replay["gap"]) == F(1, 200000)
                and F(replay["target_curvature"]) == F(3, 200), "original criterion")
        roots, root_replay = load(ROOT_AUTHOR), load(ROOT_REPLAY)
        require(roots["status"] == root_replay["status"] == "passed"
                and roots["domains"] == root_replay["domains"]
                and root_replay["input_sha256"] == bindings[ROOT_AUTHOR],
                "original endpoint existence/coverage audit")
        cells, root_coverage = original_cells(roots)
        output["original_reference_coverage"] = root_coverage
        ancestors = []
        require(len(author["stage_provenance"]) == 4, "source tier inventory")
        for meta in author["stage_provenance"]:
            require(bindings[meta["record"]] == meta["record_sha256"],
                    "source tier record association")
            record = load(meta["record"])
            require(record["proof_sha256"] == meta["proof_sha256"]
                    and record["script_sha256"] == meta["script_sha256"],
                    "source tier proof/code")
            ancestors.append(record)
        summaries = replay["replay_summaries"]
        require(len(summaries) == 21032, "one maximum per original job")
        maxima = {(own, fi): None for own in (0, 1) for fi in range(4)}
        totals = {"source_leaves": 0, "geometric_exclusions": 0, "nodes": 0,
                  "nonempty_jobs": 0, "all_excluded_jobs": 0, "maximum_depth": 0}
        for job, tree in enumerate(replay["completed"]):
            active_job = job
            ci, fi = divmod(job, 4)
            cell, summary = cells[ci], summaries[job]
            coverage = source_tree(tree, cell, fi, job, ancestors, summary)
            totals["source_leaves"] += sum(coverage["leaves_by_tier"])
            totals["geometric_exclusions"] += sum(coverage["exclusions"].values())
            totals["nodes"] += coverage["nodes"]
            totals["maximum_depth"] = max(totals["maximum_depth"], coverage["maximum_depth"])
            row = {"job": job, "reference_cell": ci, "reference_domain": cell["domain_index"],
                   "reference_tree_node": cell["node_index"], "reference_address": cell["address"],
                   "own": cell["own"], "neighbor": cell["neighbor"], "family_index": fi,
                   "family": FAMILY_NAMES[fi], "coverage": coverage,
                   "source_tree_canonical_sha256": canonical_hash(tree),
                   "replay_summary_canonical_sha256": canonical_hash(summary),
                   "transport_cost_rational": str(COSTS[cell["own"]][fi]),
                   "original_display": summary["maximum_upper"]}
            if summary["maximum_upper"] is None:
                row["status"] = "inherited_all_excluded"
                row["strict_negative"] = None
                totals["all_excluded_jobs"] += 1
            else:
                upper, midpoint, radius = display_upper(summary["maximum_upper"])
                require(upper < 0, "outward original maximum not negative")
                corrected = upper + COSTS[cell["own"]][fi]
                row.update(status="compared", original_upper_rational=str(upper),
                           display_midpoint_rational=str(midpoint),
                           display_radius_rational=str(radius),
                           transported_upper_rational=str(corrected),
                           strict_negative=corrected < 0)
                key = (cell["own"], fi)
                if maxima[key] is None or corrected > maxima[key][0]:
                    maxima[key] = (corrected, job)
                totals["nonempty_jobs"] += 1
            rows.append(row)
        family_results = []
        for (own, fi), worst in sorted(maxima.items()):
            require(worst is not None, "entire own/family has no source witness")
            upper, job = worst
            family_results.append({"own": own, "family": FAMILY_NAMES[fi],
                                   "transport_cost_rational": str(COSTS[own][fi]),
                                   "maximum_upper_rational": str(upper), "maximum_job": job,
                                   "strict_negative": upper < 0,
                                   "unconditional_monotonicity_family": COSTS[own][fi] == 0})
        all_paid = all(row["strict_negative"] for row in family_results)
        output.update(status="completed_fixed_saved_data", complete_coverage=True,
                      all_current_signs_proved=all_paid, family_results=family_results,
                      remaining_family_count=sum(not row["strict_negative"] for row in family_results),
                      common_margin_rational=(str(-max(x[0] for x in maxima.values()))
                                              if all_paid else None),
                      charged_failed_jobs=[row["job"] for row in rows
                                           if row["status"] == "compared"
                                           and not row["strict_negative"]])
        output["counts"].update(totals)
        output["counts"]["jobs"] = len(rows)
        verify()
        output["input_sha256"] = bindings
        output["input_binding_count"] = len(bindings)
        output["changed_inputs"] = []
        output["final_bindings_verified"] = True
        with args.output.open("x") as stream:
            json.dump(output, stream, indent=2, sort_keys=True)
            stream.write("\n")
        print(json.dumps({"status": output["status"], "jobs": len(rows),
                          "all_current_signs_proved": all_paid,
                          "remaining_family_count": output["remaining_family_count"],
                          "input_binding_count": len(bindings)}), flush=True)
        return 0
    except Exception as exc:
        output.update(status="error", active_job=active_job,
                      error={"type": type(exc).__name__, "message": str(exc),
                             "traceback": traceback.format_exc()},
                      pending_jobs=list(range(len(rows), 21032)), input_sha256=bindings,
                      input_binding_count=len(bindings))
        output["changed_inputs"] = [name for name, digest in bindings.items()
                                    if not (ROOT / name).exists() or sha(ROOT / name) != digest]
        with args.output.open("x") as stream:
            json.dump(output, stream, indent=2, sort_keys=True)
            stream.write("\n")
        print(json.dumps({"status": "error", "active_job": active_job,
                          "message": str(exc)}), flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
