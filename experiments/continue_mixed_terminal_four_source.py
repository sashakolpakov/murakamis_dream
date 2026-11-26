#!/usr/bin/env python3
"""Continue the pinned type-four source certificate on the actual K4 domain.

No prior accepted search is repeated. Final saved replay validates every
legacy leaf with its original arithmetic and every appended leaf on K4.
"""
import argparse
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import signal
import time

from flint import acb, arb, ctx
import certify_mixed_terminal_four_source as base

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_terminal_four_source_continuation.md"
SEED_NAME = "repro/results/research-mixed-terminal-four-source-attempt01.json"
SEED_SHA = "8bd75d7cfc1a5dad99579cb48e69aef5ced000ce505687aae805ec24183b041e"
BASE_NAME = "experiments/certify_mixed_terminal_four_source.py"
BASE_SHA = "ded3dc6dfca6ed6206251b32139a7e0d7051b85a1e53306b297671f00b706ccf"
BASE_PROOF = "notes/research_mixed_terminal_four_source_certificate.md"
BASE_PROOF_SHA = "3166c5343b4a079f07e80beb80bc3e25f3107343fe079cab07a5ff682029ebe3"
RADIUS = F(15, 16)
HEIGHTS = (F(-7, 8), F(51, 64))
SCOPE = {
    "external_three": "full original D3",
    "external_four": "D4-prime intersect -27/250<=Im(a)<=-1/1000",
    "external_four_normalized_disk_radius": str(RADIUS),
    "external_four_normalized_height_interval": list(map(str, HEIGHTS)),
}
RULES = {
    "pinned_prefix": "original_mask_fixed_trial_v1",
    "appended_nodes": "actual_k4_fixed_trial_v1",
}


def clipped_box(box, neighbor):
    if neighbor == 0:
        return list(box)
    assert neighbor == 1
    result = []
    for (lo, hi), (left, right) in zip(
            box, [(-RADIUS, RADIUS), HEIGHTS]):
        lo, hi = max(lo, left), min(hi, right)
        if lo > hi:
            return None
        result.append((lo, hi))
    return result


def excluded(box, neighbor):
    box = clipped_box(box, neighbor)
    if box is None:
        return True
    if neighbor == 0:
        return base.old.excluded(box)
    distance = sum((0 if lo <= 0 <= hi else min(lo*lo, hi*hi))
                   for lo, hi in box)
    return distance > RADIUS*RADIUS  # equality is retained


def check_new(cell, context, box, face, saved_trial=None):
    clipped = clipped_box(box, cell["neighbor"])
    assert clipped is not None and not excluded(box, cell["neighbor"])
    # The old helper clips only the weaker lower height. Hence it leaves
    # this already-clipped rectangle unchanged, preserving all arithmetic.
    assert base.physical_box(clipped, cell["neighbor"]) == clipped
    return base.check_face(cell, context, clipped, face, saved_trial)


def prefix_tree(record, job):
    if job < len(record["completed"]):
        return record["completed"][job]
    active = record["active"]
    if active is not None and job == active["job"]:
        return active["tree"]
    return []


def assert_extends(record, previous):
    assert len(record["completed"]) >= len(previous["completed"])
    for j, tree in enumerate(previous["completed"]):
        assert record["completed"][j] == tree
    if previous["active"] is not None:
        j = previous["active"]["job"]
        before = previous["active"]["tree"]
        after = prefix_tree(record, j)
        assert after[:len(before)] == before
        assert j < len(record["completed"]) or record["active"] is not None


def frontier(box, tree, face, neighbor, job, seed, replay_leaf=None):
    pinned = prefix_tree(seed, job)
    assert tree[:len(pinned)] == pinned
    pending = [(box, 0)]
    counts = dict(legacy_leaves=0, new_leaves=0, legacy_exclusions=0,
                  new_exclusions=0, nodes=len(tree))
    for index, node in enumerate(tree):
        assert pending
        cell, depth = pending.pop()
        legacy = index < len(pinned)
        is_excluded = (base.physically_excluded(cell, neighbor) if legacy
                       else excluded(cell, neighbor))
        if node[0] == "S":
            assert len(node) == 2 and node[1] in (0, 1)
            left, right = base.old.split(cell, node[1])
            pending.extend([(left, depth+1), (right, depth+1)])
        elif node[0] == "X":
            assert len(node) == 1 and is_excluded
            counts["legacy_exclusions" if legacy else "new_exclusions"] += 1
        else:
            assert node[0] == "L" and len(node) == 2 and not is_excluded
            base.validate_trial(node[1], face)
            if replay_leaf is not None:
                replay_leaf(cell, node[1], legacy)
            counts["legacy_leaves" if legacy else "new_leaves"] += 1
    return pending, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-nodes", type=int, default=600000)
    parser.add_argument("--max-seconds", type=float, default=600)
    parser.add_argument("--max-depth", type=int, default=20)
    args = parser.parse_args()
    assert args.precision >= 192 and not (args.input and args.resume)
    assert not args.output.exists(), "use a new immutable output path"
    assert 0 < args.max_nodes <= 600000 and 0 < args.max_seconds <= 600
    assert 0 <= args.max_depth <= 45
    source_path = args.input or args.resume
    assert all(args.output.resolve() != p.resolve()
               for p in [ROOT/SEED_NAME]+([source_path] if source_path else []))
    ctx.prec = args.precision
    base.PI, base.II = arb.pi(), acb(0, 1)
    base.primitive.PI, base.primitive.II = base.PI, base.II
    base.old.propose = base.original_root_proposals_forbidden
    if args.input:
        base.propose_targets = base.target_proposals_forbidden
    assert base.ar("3.14")/100-2*base.ar(base.KAPPA) > base.ar(base.MU)
    assert base.old.DISKS[1][2]*RADIUS == F(3, 50)
    assert [base.old.DISKS[1][1]+base.old.DISKS[1][2]*h for h in HEIGHTS] == [
        F(-27, 250), F(-1, 1000)]
    proof_hash, script_hash = base.sha(PROOF), base.sha(__file__)
    dependencies = {}

    def bind(name, expected=None):
        digest = base.sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    bind(BASE_NAME, BASE_SHA)
    bind(BASE_PROOF, BASE_PROOF_SHA)
    bind(SEED_NAME, SEED_SHA)
    seed = json.loads((ROOT/SEED_NAME).read_text())
    assert seed["status"] == "incomplete" and seed["fatal_error"] is None
    assert seed["proof_sha256"] == BASE_PROOF_SHA
    assert seed["script_sha256"] == BASE_SHA
    assert seed["reference_scope"] == base.REFERENCE_SCOPE
    assert seed["gap"] == str(base.GAP) and seed["target_curvature"] == str(base.MU)
    assert seed["family_inventory"] == base.family_inventory()
    assert len(seed["completed"]) == 36752 and seed["job_count"] == 40131
    assert seed["active"]["job"] == 36752 and len(seed["active"]["tree"]) == 2566
    assert len(seed["active"]["pending"]) == 5
    assert sum(map(len, seed["completed"]))+len(seed["active"]["tree"]) == 93994
    for name, digest in seed["dependencies_sha256"].items():
        bind(name, digest)
    # New compact-domain provenance, not just the weaker original height mask.
    for name in [
        "notes/research_mixed_open_local_factor_coverage.md",
        "experiments/check_mixed_open_local_factor_coverage.py",
        "repro/results/research-mixed-open-local-factor-coverage.json",
        "repro/results/research-mixed-open-local-factor-coverage-replay.json",
    ]:
        bind(name)
    extraction_name = "repro/results/research-mixed-open-local-factor-coverage.json"
    extraction_replay_name = "repro/results/research-mixed-open-local-factor-coverage-replay.json"
    extraction = json.loads((ROOT/extraction_name).read_text())
    extraction_replay = json.loads((ROOT/extraction_replay_name).read_text())
    assert extraction["status"] == extraction_replay["status"] == "passed"
    assert extraction_replay["input_sha256"] == dependencies[extraction_name]
    for record in (extraction, extraction_replay):
        for name, digest in record.get("dependencies_sha256", {}).items():
            bind(name, digest)
        for name, digest in record.get("dependencies", {}).items():
            bind(name, digest)
        bind("notes/research_mixed_open_local_factor_coverage.md", record["proof_sha256"])
        bind("experiments/check_mixed_open_local_factor_coverage.py", record["script_sha256"])
    roots = json.loads((ROOT/base.ROOT_AUTHOR).read_text())
    roots_replay = json.loads((ROOT/base.ROOT_REPLAY).read_text())
    assert roots["status"] == roots_replay["status"] == "passed"
    assert roots_replay["input_sha256"] == dependencies[base.ROOT_AUTHOR]
    assert roots["domains"] == roots_replay["domains"]
    cells = base.original_cells(roots)
    jobs = [(index, face) for index in range(len(cells)) for face in range(len(base.FACES))]
    assert len(jobs) == 40131

    source_hash = base.sha(source_path) if source_path else None
    saved = json.loads(source_path.read_text()) if source_path else None
    if saved:
        assert saved["format_version"] == 2
        assert saved["proof_sha256"] == proof_hash and saved["script_sha256"] == script_hash
        assert saved["dependencies_sha256"] == dependencies
        assert saved["seed_sha256"] == SEED_SHA and saved["acceptance_rules"] == RULES
        assert saved["reference_scope"] == SCOPE
        assert saved["family_inventory"] == base.family_inventory()
        assert saved["gap"] == str(base.GAP) and saved["target_curvature"] == str(base.MU)
        assert saved["job_count"] == len(jobs)
        assert saved["status"] == ("passed" if args.input else "incomplete")
        assert_extends(saved, seed)
    initial = saved or seed
    completed = copy.deepcopy(initial["completed"])
    active = copy.deepcopy(initial["active"])
    # The previous failed uncommitted trial is diagnostic, not acceptance.
    if active is not None:
        active.pop("failure", None)

    def validate_partition():
        assert len(completed) <= len(jobs)
        for ji, tree in enumerate(completed):
            ci, fi = jobs[ji]
            pending, _ = frontier(cells[ci]["box"], tree, base.FACES[fi],
                                  cells[ci]["neighbor"], ji, seed)
            assert not pending
        if active is not None:
            assert active["job"] == len(completed) < len(jobs)
            ci, fi = jobs[active["job"]]
            pending, _ = frontier(cells[ci]["box"], active["tree"], base.FACES[fi],
                                  cells[ci]["neighbor"], active["job"], seed)
            assert pending and base.serialize_pending(pending) == active["pending"]
        assert_extends(dict(completed=completed, active=active), initial)

    validate_partition()
    contexts = {}
    context_count = proposals = refinements = attempted = nodes = 0
    fatal_error = None

    def context(ci):
        nonlocal context_count
        if ci not in contexts:
            contexts[ci] = base.root_context(cells[ci])
            context_count += 1
        return contexts[ci]

    def validate_bindings():
        assert base.sha(PROOF) == proof_hash and base.sha(__file__) == script_hash
        assert all(base.sha(ROOT/name) == digest for name, digest in dependencies.items())
        if source_path:
            assert base.sha(source_path) == source_hash

    def result(status, reason, summaries):
        return dict(format_version=2, status=status, stop_reason=reason,
                    precision_bits=args.precision, proof_sha256=proof_hash,
                    script_sha256=script_hash, dependencies_sha256=dependencies,
                    seed_sha256=SEED_SHA, acceptance_rules=RULES,
                    input_sha256=source_hash if args.input else None,
                    resume_sha256=source_hash if args.resume else None,
                    reference_scope=SCOPE, gap=str(base.GAP), target_curvature=str(base.MU),
                    original_own_four_cells=1911, face_families_per_cell=21,
                    family_inventory=base.family_inventory(), job_count=len(jobs),
                    completed=completed, active=active, additional_nodes=nodes,
                    attempted_nodes=attempted, target_proposals=proposals,
                    root_proposals=0, refinements=refinements,
                    revalidated_original_roots=context_count, fatal_error=fatal_error,
                    attempt_limits=None if args.input else dict(additional_nodes=args.max_nodes,
                        seconds=args.max_seconds, depth_from_inherited_cell=args.max_depth),
                    replay_summaries=summaries, final_bindings_verified=True,
                    scope="All 21 original bare comparisons on full D3 and actual K4. "
                          "Legacy leaves retain original-mask arithmetic, including outside K4; "
                          "new leaves use exact K4 clipping. Complete author and saved replay required.")

    if args.input:
        assert active is None and len(completed) == len(jobs)
        summaries = []
        checked = legacy_checked = 0
        for ji, tree in enumerate(completed):
            ci, fi = jobs[ji]
            maximum = None

            def replay_leaf(box, targets, legacy):
                nonlocal checked, legacy_checked, maximum
                rule = base.check_face if legacy else check_new
                passed, trial, info, _ = rule(cells[ci], context(ci), box, base.FACES[fi], targets)
                assert passed and trial == targets, (ji, legacy, box, info)
                checked += 1
                legacy_checked += int(legacy)
                value = arb(info["upper"]).upper()
                maximum = value if maximum is None else max(maximum, value)

            pending, counts = frontier(cells[ci]["box"], tree, base.FACES[fi],
                                        cells[ci]["neighbor"], ji, seed, replay_leaf)
            assert not pending
            summaries.append(dict(job=ji, **counts,
                                  maximum_upper=None if maximum is None else str(maximum)))
            if ji % 128 == 0:
                print("REPLAY", ji, "/", len(jobs), "leaves", checked, flush=True)
        assert proposals == refinements == nodes == attempted == 0
        validate_bindings()
        validate_partition()
        base.write_atomic(args.output, result("passed", "all saved original and K4 leaves replayed", summaries))
        print("PASS", len(jobs), "jobs", checked, "leaves", legacy_checked,
              "legacy; no proposals/refinements", flush=True)
        return 0

    start = checkpoint = time.monotonic()
    reason = "all K4 continuation families verified"
    signal.signal(signal.SIGALRM, base.alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, args.max_seconds)
    try:
        while len(completed) < len(jobs):
            if nodes >= args.max_nodes or time.monotonic()-start >= args.max_seconds:
                raise base.BudgetStop("author additional-node/time cap")
            ji = len(completed)
            ci, fi = jobs[ji]
            if active is None:
                with base.atomic_state():
                    active = dict(job=ji, tree=[], pending=base.serialize_pending([(cells[ci]["box"], 0)]))
            box_strings, depth = active["pending"][-1]
            box = base.decode_box(box_strings)
            attempted += 1
            if excluded(box, cells[ci]["neighbor"]):
                new_node, replacement = ["X"], []
            else:
                passed, trial, info, axis = check_new(cells[ci], context(ci), box, base.FACES[fi])
                proposals += 1
                if passed:
                    new_node, replacement = ["L", trial], []
                else:
                    if depth >= args.max_depth:
                        reason = "maximum depth; unresolved K4 face"
                        active["failure"] = dict(box=box_strings, targets=trial, bounds=info)
                        break
                    left, right = base.old.split(box, axis)
                    new_node = ["S", axis]
                    replacement = base.serialize_pending([(left, depth+1), (right, depth+1)])
            with base.atomic_state():
                active["pending"].pop()
                active["tree"].append(new_node)
                active["pending"].extend(replacement)
                nodes += 1
                refinements += int(new_node[0] == "S")
                if not active["pending"]:
                    completed.append(active["tree"])
                    active = None
            if time.monotonic()-checkpoint >= 10:
                validate_bindings()
                validate_partition()
                base.write_atomic(args.output, result("incomplete", "atomic checkpoint", []))
                print("CHECKPOINT", len(completed), "/", len(jobs), "additional nodes", nodes, flush=True)
                checkpoint = time.monotonic()
    except base.BudgetStop as exc:
        reason = str(exc)
    except Exception as exc:
        fatal_error = dict(type=type(exc).__name__, message=str(exc))
        reason = "unresolved arithmetic/inherited-input failure"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    validate_bindings()
    validate_partition()
    status = "passed" if len(completed) == len(jobs) and active is None else "incomplete"
    base.write_atomic(args.output, result(status, reason, []))
    print(status.upper(), len(completed), "/", len(jobs), "additional nodes", nodes,
          "seconds", time.monotonic()-start, flush=True)
    return 0 if status == "passed" else 3 if fatal_error else 2


if __name__ == "__main__":
    raise SystemExit(main())
