#!/usr/bin/env python3
"""One fixed saved-bound comparison; standard library only, no analytic replay.

The protocol fixes every input, family, cost and output.  This program decodes
printed finite bounds as exact fractions and validates saved tree associations.
It never imports an old checker or evaluates a phase, root or source.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import traceback

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "repro/results/research-mixed-terminal-four-source-stage4-attempt01.json"
REPLAY = "repro/results/research-mixed-terminal-four-source-replay.json"
ROOT_AUTHOR = "repro/results/research-mixed-open-word-critical-localization.json"
ROOT_REPLAY = "repro/results/research-mixed-open-word-critical-localization-replay.json"
PROTOCOL = "notes/research_mixed_three_four_right_strip_saved_faces_protocol.md"
THEORY = "notes/research_mixed_three_four_private_left_right_extension.md"
OLD_PROOF = "notes/research_mixed_terminal_four_coupled_source_continuation.md"
OLD_SCRIPT = "experiments/continue_mixed_terminal_four_source_coupled.py"
OUTPUT = "repro/results/research-mixed-three-four-right-strip-saved-faces.json"
ANCESTORS = (
    "repro/results/research-mixed-terminal-four-source-attempt01.json",
    "repro/results/research-mixed-terminal-four-source-stage2-attempt01.json",
    "repro/results/research-mixed-terminal-four-source-stage3-attempt01.json",
)
PINNED = {
    AUTHOR: "e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3",
    REPLAY: "3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79",
    ROOT_AUTHOR: "ac2991d4cd5b7a78d202a237efebf98a9ad7ab77b6bacc4ab82568b8aa3cdad5",
    ROOT_REPLAY: "2b5d91f8fbfa860d978f7b2076270b33bbe40d7410d39e91c9733e41b03ec247",
    PROTOCOL: "613fab372915864925959d52de088d5cf673d4aa4eb46dc6351cc8ac1e4440b6",
    THEORY: "4c263a6302e331d0b34e8d2c260c8321a4fe37eb0bda0afac5a4ecc45b6017cc",
    OLD_PROOF: "ee52ddb19be76ed0147a2e23309f2feafd812b4f8758eecabdd3096b8f0b0830",
    OLD_SCRIPT: "08b6f5b2eab5abc5ad2a4ab424034256f55c0211b08c04f2f1eda4fe4cc5de9d",
    ANCESTORS[0]: "8bd75d7cfc1a5dad99579cb48e69aef5ced000ce505687aae805ec24183b041e",
    ANCESTORS[1]: "ac3053b04d24b46dda525f4746ba1e7c1b3fc937b51eef763adeb8e878d15a03",
    ANCESTORS[2]: "151200a014e548445543a2aba66210c38714d0904305cdb3a73d665f60429738",
}
COSTS = (F(7, 400), F(0), F(0), F(103, 2000),
         F(7, 400), F(7, 400), F(0), F(0))
TIERS = ("first_stage", "second_stage", "third_stage", "new")
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
DECIMAL = re.compile(NUMBER)
BALL = re.compile(r"\[\s*(" + NUMBER + r")\s*\+/-\s*(" + NUMBER + r")\s*\]")
SELECTED_JOBS = tuple(21 * cell + family for cell in range(1911) for family in range(8))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def inventory():
    ts, es = ("3/20", "1/2"), ("27/100", "49/100")
    rows = [["flat_t", t, None, "0", "0", "0", "1"] for t in ts]
    rows += [["flat_e", None, e, "0", "0", "1", "0"] for e in es]
    rows += [["corner", t, e, "0", "0", "0", "0"] for t in ts for e in es]
    rows += [["t_alias", None, None, h, "0", "0", keep]
             for h in ("-3/25", "3/25") for keep in ("0", "1")]
    rows += [["e_alias", None, None, "0", h, keep, "0"]
             for h in ("-11/200", "1/25") for keep in ("0", "1")]
    rows += [["double_alias", None, None, t, e, "0", "0"]
             for t in ("-3/25", "3/25") for e in ("-11/200", "1/25")]
    return rows + [["raw_half", "1/2", None, "0", "0", "0", "0"]]


def displayed_upper(value):
    require(isinstance(value, str), "non-string saved bound")
    text = value.strip()
    match = BALL.fullmatch(text)
    if match:
        midpoint, radius = map(F, match.groups())
        require(radius >= 0, "negative saved radius")
        return midpoint + radius, midpoint, radius
    require(DECIMAL.fullmatch(text) is not None, "unsupported or nonfinite saved bound")
    return F(text), F(text), F(0)


def original_cells(author, replay):
    """Only parse the saved partition; do not reevaluate an exclusion or root."""
    require(author["status"] == replay["status"] == "passed", "root record status")
    require(author["domain_count"] == replay["domain_count"] == 4, "root domain count")
    require(author["domains"] == replay["domains"], "root author/replay tree equality")
    require(replay["input_sha256"] == PINNED[ROOT_AUTHOR], "root replay input")
    require([(d["epsilon"], d["neighbor_epsilon"]) for d in author["domains"]]
            == [(0, 0), (0, 1), (1, 0), (1, 1)], "root domain ordering")
    cells, partitions = [], []
    total_nodes = 0
    for domain_index, domain in enumerate(author["domains"]):
        pending = [(0, "")]
        leaves = excluded = 0
        mass = F(0)
        for node_index, node in enumerate(domain["tree"]):
            require(bool(pending), "root partition overrun")
            depth, address = pending.pop()
            total_nodes += 1
            require(isinstance(node, list) and node, "root node shape")
            if node[0] == "S":
                require(len(node) == 2 and type(node[1]) is int
                        and node[1] == depth % 2, "root split axis")
                pending.extend([(depth + 1, address + "0"), (depth + 1, address + "1")])
                continue
            mass += F(1, 2 ** depth)
            if node[0] == "X":
                require(len(node) == 1, "root exclusion shape")
                excluded += 1
            else:
                require(node[0] == "L" and len(node) == 2, "root source shape")
                leaves += 1
                if domain["epsilon"] == 1:
                    cells.append({"cell": len(cells), "domain": domain_index,
                                  "node": node_index, "neighbor": domain["neighbor_epsilon"],
                                  "address": address, "depth": depth,
                                  "original_node_sha256": canonical_sha(node)})
        require(not pending and mass == 1, "root partition incomplete")
        require((leaves, excluded) == (domain["leaves"], domain["excluded"]),
                "root partition counts")
        partitions.append({"domain": domain_index, "leaves": leaves,
                           "excluded": excluded, "partition_mass": str(mass)})
    require([p["leaves"] for p in partitions] == [1645, 1702, 1002, 909], "root leaf inventory")
    require((total_nodes, sum(p["leaves"] for p in partitions),
             sum(p["excluded"] for p in partitions)) == (10978, 5258, 233), "root totals")
    require(len(cells) == 1911 and [sum(c["neighbor"] == n for c in cells)
                                  for n in (0, 1)] == [1002, 909], "own-four cell inventory")
    return cells, partitions


def prefix_tree(record, job):
    if job < len(record["completed"]):
        return record["completed"][job]
    active = record["active"]
    return active["tree"] if active is not None and active["job"] == job else []


def target_intervals(family):
    a, t, e = (F(11, 50), F(9, 20)), (F(3, 20), F(1, 2)), (F(27, 100), F(49, 100))
    if family < 2:
        return (a, e)
    if family < 4:
        return (a, t)
    if family < 8:
        return (a,)
    return (a, e, (F(1, 10), F(269, 1000))) if family == 20 else (a, t, e)


def saved_tree(tree, summary, job, cell, ancestors):
    prefixes = [prefix_tree(record, job) for record in ancestors]
    for before, after in zip(prefixes, prefixes[1:] + [tree]):
        require(after[:len(before)] == before, "inherited source prefix changed")
    counts = {tier + suffix: 0 for tier in TIERS for suffix in ("_leaves", "_exclusions")}
    counts.update(inverse_exclusions=0, nodes=len(tree))
    pending, mass = [0], F(0)
    splits = 0
    for node_index, node in enumerate(tree):
        require(bool(pending), "source tree overrun")
        depth = pending.pop()
        require(isinstance(node, list) and node, "source node shape")
        tier_index = next((i for i, prior in enumerate(prefixes) if node_index < len(prior)), 3)
        tier = TIERS[tier_index]
        kind = node[0]
        if kind == "S":
            require(len(node) == 2 and type(node[1]) is int and node[1] in (0, 1), "source split")
            pending.extend([depth + 1, depth + 1])
            splits += 1
            continue
        mass += F(1, 2 ** depth)
        if kind == "L":
            require(len(node) == 2 and isinstance(node[1], list), "source leaf shape")
            bounds = target_intervals(job % 21)
            require(len(node[1]) == len(bounds), "target dimension")
            for value, (lo, hi) in zip(node[1], bounds):
                require(isinstance(value, str) and lo <= F(value) <= hi, "target outside original range")
            counts[tier + "_leaves"] += 1
        elif kind == "X":
            require(len(node) == 1, "saved exclusion shape")
            counts[tier + "_exclusions"] += 1
        elif kind == "F":
            require(tier_index == 3 and cell["neighbor"] == 1, "coupled exclusion scope")
            require(len(node) == 2 and isinstance(node[1], dict)
                    and set(node[1]) == {"m2", "m3"}, "both coupled length cases required")
            require(node[1]["m2"] in {"attached_real_floor", "attached_fixed_point"}, "m2 exclusion reason")
            require(node[1]["m3"] in {"opposite_half_plane", "external_half_plane",
                    "opposite_outside_P4", "external_outside_both_P"}, "m3 exclusion reason")
            counts["inverse_exclusions"] += 1
        else:
            raise AssertionError("unknown source node kind")
    require(not pending and mass == 1, "source partition incomplete")
    require(summary["job"] == job and all(summary[k] == v for k, v in counts.items()),
            "saved summary/source-tree association")
    leaves = sum(counts[t + "_leaves"] for t in TIERS)
    excluded = sum(counts[t + "_exclusions"] for t in TIERS) + counts["inverse_exclusions"]
    require(leaves + excluded == splits + 1, "source binary-tree counts")
    require((summary["maximum_upper"] is None) == (leaves == 0), "null/source maximum mismatch")
    require(leaves > 0 or excluded > 0, "empty source job")
    decoded = displayed_upper(summary["maximum_upper"]) if leaves else None
    return counts, leaves, excluded, decoded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / OUTPUT)
    args = parser.parse_args()
    require(args.output.resolve() == (ROOT / OUTPUT).resolve(), "protocol fixes the output path")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Reserve the one permitted output before reading/comparing inputs.  Never overwrite or retry.
    with args.output.open("x", encoding="utf-8") as output:
        bindings = dict(PINNED)
        rows, family_summaries, partitions, cells = [], [], [], []
        errors, changed = [], []
        active_job = None
        checked_jobs = 0
        inventory_counts = [0] * 21
        source_totals = {tier + suffix: 0 for tier in TIERS for suffix in ("_leaves", "_exclusions")}
        source_totals.update(inverse_exclusions=0, nodes=0)
        maxima = [None] * 8
        maximal_jobs = [None] * 8
        failed_jobs = [[] for _ in range(8)]
        source_jobs = [0] * 8
        excluded_jobs = [0] * 8
        selected_counts = [0] * 8
        selected_leaf_totals = [dict(source_totals) for _ in range(8)]
        inputs_verified = False
        complete_inventory = False
        final_bindings_verified = False
        try:
            own = Path(__file__).resolve().relative_to(ROOT).as_posix()
            bindings[own] = sha(ROOT / own)
            verified = {}

            def bind(name, digest):
                require(isinstance(name, str) and not Path(name).is_absolute()
                        and ".." not in Path(name).parts, "unsafe dependency path")
                require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest), "hash format")
                require(name not in bindings or bindings[name] == digest, "conflicting dependency binding: " + name)
                bindings[name] = digest
                if name not in verified:
                    require(sha(ROOT / name) == digest, "changed input: " + name)
                    verified[name] = digest

            for name, digest in list(bindings.items()):
                bind(name, digest)
            author, replay = [json.loads((ROOT / p).read_text()) for p in (AUTHOR, REPLAY)]
            for record in (author, replay):
                require(record["status"] == "passed" and record["active"] is None
                        and record["fatal_error"] is None and record["final_bindings_verified"] is True,
                        "incomplete source record")
                require(record["format_version"] == 4 and record["original_own_four_cells"] == 1911
                        and record["face_families_per_cell"] == 21 and record["job_count"] == 40131,
                        "source coverage inventory")
                require(record["family_inventory"] == inventory(), "complete family order")
                for name, digest in record["dependencies_sha256"].items():
                    bind(name, digest)
                bind(OLD_PROOF, record["proof_sha256"])
                bind(OLD_SCRIPT, record["script_sha256"])
                for key, path in zip(("first_stage_sha256", "second_stage_sha256", "seed_sha256"), ANCESTORS):
                    require(record[key] == PINNED[path], "inherited stage binding")
            require(author["precision_bits"] == 256 and replay["precision_bits"] == 320, "saved precisions")
            require(replay["input_sha256"] == PINNED[AUTHOR], "replay author binding")
            require(author["completed"] == replay["completed"], "full author/replay tree equality")
            require(len(replay["completed"]) == len(replay["replay_summaries"]) == 40131, "completed job count")
            for key in ("acceptance_rules", "reference_scope", "gap", "target_curvature", "scope"):
                require(author[key] == replay[key], "saved source semantics: " + key)
            require(all(replay[k] == 0 for k in ("additional_nodes", "attempted_nodes",
                    "root_proposals", "target_proposals", "refinements")), "replay changed inventory")
            roots, roots_replay = [json.loads((ROOT / p).read_text()) for p in (ROOT_AUTHOR, ROOT_REPLAY)]
            cells, partitions = original_cells(roots, roots_replay)
            ancestors = [json.loads((ROOT / p).read_text()) for p in ANCESTORS]
            inputs_verified = True
            for job, (tree, summary) in enumerate(zip(replay["completed"], replay["replay_summaries"])):
                active_job = job
                family, cell = job % 21, cells[job // 21]
                counts, leaves, excluded, decoded = saved_tree(tree, summary, job, cell, ancestors)
                inventory_counts[family] += 1
                for key, value in counts.items():
                    source_totals[key] += value
                if family < 8:
                    row = {"job": job, "cell": cell["cell"], "family": family,
                           "root_domain": cell["domain"], "root_node": cell["node"],
                           "neighbor": cell["neighbor"], "tree_sha256": canonical_sha(tree),
                           "counts": counts, "source_leaves": leaves, "excluded_leaves": excluded,
                           "original_upper_display": summary["maximum_upper"],
                           "cost_rational": str(COSTS[family]), "original_upper_rational": None,
                           "midpoint_rational": None, "radius_rational": None,
                           "adjusted_upper_rational": None, "strictly_negative": None}
                    if decoded is None:
                        row["status"] = "original exclusions only; no source estimate"
                        excluded_jobs[family] += 1
                    else:
                        upper, midpoint, radius = decoded
                        adjusted = upper + COSTS[family]
                        row.update(original_upper_rational=str(upper), midpoint_rational=str(midpoint),
                                   radius_rational=str(radius), adjusted_upper_rational=str(adjusted),
                                   strictly_negative=adjusted < 0,
                                   status="strict saved reserve" if adjusted < 0 else "insufficient saved reserve")
                        source_jobs[family] += 1
                        if maxima[family] is None or adjusted > maxima[family]:
                            maxima[family], maximal_jobs[family] = adjusted, job
                        if adjusted >= 0:
                            failed_jobs[family].append(job)
                    rows.append(row)
                    selected_counts[family] += 1
                    for key, value in counts.items():
                        selected_leaf_totals[family][key] += value
                checked_jobs += 1
            active_job = None
            require(inventory_counts == [1911] * 21 and selected_counts == [1911] * 8,
                    "final family coverage")
            require(tuple(row["job"] for row in rows) == SELECTED_JOBS, "selected job ordering")
            complete_inventory = True
        except (Exception, KeyboardInterrupt) as exc:
            errors.append({"active_original_job": active_job, "type": type(exc).__name__,
                           "message": str(exc), "traceback": traceback.format_exc()})
        # Always perform a final binding audit; a failed or partial audit proves no family.
        for name, digest in bindings.items():
            try:
                if sha(ROOT / name) != digest:
                    changed.append(name)
            except (Exception, KeyboardInterrupt) as exc:
                changed.append(name)
                errors.append({"binding": name, "type": type(exc).__name__, "message": str(exc)})
        final_bindings_verified = inputs_verified and not changed
        certified = complete_inventory and final_bindings_verified and not errors
        for family in range(8):
            success = certified and source_jobs[family] > 0 and not failed_jobs[family]
            family_summaries.append({"family": family, "inventory": inventory()[family],
                "cost_rational": str(COSTS[family]), "jobs": selected_counts[family],
                "source_bearing_jobs": source_jobs[family], "excluded_only_jobs": excluded_jobs[family],
                "counts": selected_leaf_totals[family], "coverage_verified": certified,
                "maximum_adjusted_upper_rational": None if maxima[family] is None else str(maxima[family]),
                "maximum_original_upper_rational": None if maxima[family] is None else str(maxima[family] - COSTS[family]),
                "witness_job": maximal_jobs[family], "insufficient_jobs": failed_jobs[family],
                "successful": success,
                "status": "proved by fixed saved comparison" if success else
                    "incomplete or invalid coverage" if not certified else
                    "entirely excluded; no source estimate" if not source_jobs[family] else
                    "inconclusive saved reserve"})
        processed = {row["job"] for row in rows}
        result = {"status": "completed fixed saved-only comparison" if certified else "incomplete or invalid fixed comparison",
                  "all_families_successful": all(f["successful"] for f in family_summaries),
                  "arithmetic": "exact rational outward saved-display decoding and fixed rational addition",
                  "protocol_sha256": bindings[PROTOCOL], "theory_sha256": bindings[THEORY],
                  "dependencies_sha256": bindings, "changed_inputs": changed,
                  "final_bindings_verified": final_bindings_verified,
                  "original_jobs_checked": checked_jobs, "original_family_counts": inventory_counts,
                  "original_source_counts": source_totals, "root_partition_counts": partitions,
                  "original_reference_cells": cells, "selected_jobs_expected": 15288,
                  "selected_jobs_processed": len(rows), "selected_family_counts": selected_counts,
                  "families": family_summaries, "jobs": rows,
                  "insufficient_jobs": [j for group in failed_jobs for j in group],
                  "unprocessed_selected_jobs": [j for j in SELECTED_JOBS if j not in processed],
                  "unprocessed_original_job_range": [checked_jobs, 40131],
                  "errors": errors, "phase_evaluations": 0, "root_evaluations": 0,
                  "primitive_evaluations": 0, "source_evaluations": 0, "derivative_evaluations": 0,
                  "optimizer_calls": 0, "new_cells": 0, "new_exclusions": 0,
                  "refinements": 0, "source_replays": 0,
                  "scope": "Saved reserves on every original cell; analytic transport only for actual ordinary (3,4). "
                           "Insufficient sums do not decide the actual source sign; no whole-circle or filling theorem."}
        json.dump(result, output, indent=2, sort_keys=True)
        output.write("\n")
        output.flush()
    print(result["status"], "; selected jobs", len(rows), "; successful families",
          sum(f["successful"] for f in family_summaries), "/ 8")
    return 0 if certified else 1


if __name__ == "__main__":
    raise SystemExit(main())
