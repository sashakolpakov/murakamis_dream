#!/usr/bin/env python3
"""Resumable twelve-face half-row author; complete saved replay never proposes."""
import argparse
from contextlib import contextmanager
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time

PROGRAM_START = time.monotonic()
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"experiments"))
import continue_mixed_optimized_half_row_pilot as adaptive

prior, fixed, old, ar = adaptive.prior, adaptive.fixed, adaptive.old, adaptive.ar
GAP, CUT, KAPPA, CURVATURE = adaptive.GAP, adaptive.CUT, adaptive.KAPPA, adaptive.CURVATURE
FIXED_RULE, OPTIMIZED_RULE = prior.FIXED_RULE, prior.OPTIMIZED_RULE
PROOF = ROOT/"notes/research_mixed_resumable_half_row_support.md"
FIXED_PIN = prior.PIN
FIXED_SHA = prior.PIN_SHA
WEAK_PIN = "repro/diagnostics/2026-11-05-adaptive-half-row-continuation/result-partial.json"
WEAK_SHA = "4061218279b8792578c8f89959ba75a16c088f77ab1b67531e7d0835faf9014a"
SPECS = [(own, ta, tb, face) for own in (0, 1)
         for ta, tb in ((0, 0), (0, 1), (1, 1)) for face in (0, 1)]
WEAK_CASE = (0, 1, 1, 0)
MAX_NODES, MAX_SECONDS, MAX_DEPTH = 600000, 600, 45
CHECKPOINT_SECONDS = 30
SIGNALS = {signal.SIGALRM, signal.SIGINT, signal.SIGTERM}


class StopAttempt(Exception):
    def __init__(self, signum):
        self.signum = signum


@contextmanager
def atomic_section():
    """A signal cannot expose half of a tree/frontier commit or file publication."""
    mask = signal.pthread_sigmask(signal.SIG_BLOCK, SIGNALS)
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, mask)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024*1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(path):
    with Path(path).open() as handle:
        return json.load(handle)


def encode_frontier(frontier):
    return [[[[str(x) for x in pair] for pair in box], depth] for box, depth in frontier]


def decode_frontier(rows):
    return [([(Q(x), Q(y)) for x, y in box], depth) for box, depth in rows]


def inspect_tree(tree, cyclic_prefix=0):
    frontier, leaves, volume, depth = adaptive.reconstruct(tree, cyclic_prefix)
    return encode_frontier(frontier), leaves, volume, depth


def expected_kind(case):
    own, ta, tb, face = case
    if case == (0, 0, 0, 0):
        return "pinned_fixed", FIXED_RULE
    if ta == tb and face == 1:
        return "exact_swap", FIXED_RULE if case == (0, 0, 0, 1) else OPTIMIZED_RULE
    return "independent", OPTIMIZED_RULE


def make_domains(pinned, weak):
    domains = []
    for case in SPECS:
        kind, rule = expected_kind(case)
        domain = dict(case=list(case), kind=kind, acceptance_rule=rule)
        if kind == "pinned_fixed":
            domain.update(status="complete", leaves=pinned["leaves"],
                          tree_nodes=len(pinned["tree"]), maximum_depth=pinned["maximum_depth"],
                          tree_ref=FIXED_PIN, tree_sha256=FIXED_SHA)
        elif kind == "exact_swap":
            domain.update(status="waiting", source_case=list(case[:3]+(0,)), leaves=0, tree_nodes=0)
        else:
            if case == WEAK_CASE:
                tree = list(weak["tree"])
                frontier = weak["pending"]
                seed_nodes, cyclic_prefix = len(tree), 511
            else:
                tree, frontier, seed_nodes, cyclic_prefix = [], encode_frontier([(prior.ROOT_CUBE, 0)]), 0, 0
            derived, leaves, volume, depth = inspect_tree(tree, cyclic_prefix)
            assert derived == frontier
            domain.update(status="complete" if not frontier else "incomplete",
                          tree=tree, frontier=frontier, leaves=leaves,
                          tree_nodes=len(tree), resolved_volume=str(volume),
                          maximum_depth=depth, seed_nodes=seed_nodes,
                          cyclic_prefix=cyclic_prefix)
        domains.append(domain)
    refresh_swaps(domains)
    return domains


def refresh_swaps(domains):
    seen = {}
    for domain in domains:
        case = tuple(domain["case"])
        if domain["kind"] == "exact_swap":
            base = seen[tuple(domain["source_case"])]
            assert base["kind"] in ("pinned_fixed", "independent")
            assert base["acceptance_rule"] == domain["acceptance_rule"]
            ready = base["status"] == "complete"
            domain["status"] = "complete" if ready else "waiting"
            domain["leaves"] = base["leaves"] if ready else 0
            domain["tree_nodes"] = base["tree_nodes"] if ready else 0
        seen[case] = domain


def validate_domains(domains, pinned, weak, complete=False):
    assert [tuple(d["case"]) for d in domains] == SPECS
    seen = {}
    for domain in domains:
        case = tuple(domain["case"])
        kind, rule = expected_kind(case)
        assert domain["kind"] == kind and domain["acceptance_rule"] == rule
        if kind == "pinned_fixed":
            assert "tree" not in domain and "frontier" not in domain
            assert domain["tree_ref"] == FIXED_PIN and domain["tree_sha256"] == FIXED_SHA
            assert domain["status"] == "complete"
            assert domain["leaves"] == pinned["leaves"]
            assert domain["tree_nodes"] == len(pinned["tree"])
        elif kind == "exact_swap":
            assert "tree" not in domain and "frontier" not in domain
            assert domain["source_case"] == list(case[:3]+(0,))
            base = seen[tuple(domain["source_case"])]
            assert base["kind"] in ("pinned_fixed", "independent")
            ready = base["status"] == "complete"
            assert domain["status"] == ("complete" if ready else "waiting")
            assert domain["leaves"] == (base["leaves"] if ready else 0)
            assert domain["tree_nodes"] == (base["tree_nodes"] if ready else 0)
        else:
            seed = weak["tree"] if case == WEAK_CASE else []
            assert domain["seed_nodes"] == len(seed)
            assert domain["cyclic_prefix"] == (511 if case == WEAK_CASE else 0)
            assert domain["tree"][:len(seed)] == seed
            frontier, leaves, volume, depth = inspect_tree(domain["tree"], domain["cyclic_prefix"])
            assert frontier == domain["frontier"]
            assert leaves == domain["leaves"] and str(volume) == domain["resolved_volume"]
            assert depth == domain["maximum_depth"] <= MAX_DEPTH
            assert len(domain["tree"]) == domain["tree_nodes"]
            assert domain["status"] == ("complete" if not frontier else "incomplete")
        if complete:
            assert domain["status"] == "complete"
        seen[case] = domain


def atomic_json(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with atomic_section():
        try:
            with temporary.open("w") as handle:
                json.dump(result, handle, separators=(",", ":"))
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
            descriptor = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
        finally:
            if temporary.exists():
                temporary.unlink()


def tree_for(domain, seen, pinned):
    if domain["kind"] == "pinned_fixed":
        return pinned["tree"], False
    if domain["kind"] == "independent":
        return domain["tree"], False
    base = seen[tuple(domain["source_case"])]
    assert base["status"] == "complete" and base["kind"] != "exact_swap"
    return (pinned["tree"] if base["kind"] == "pinned_fixed" else base["tree"]), True


def replay_all(domains, pinned, progress):
    """All twelve complete faces; only saved witnesses, axes and target trials."""
    proposal, trial, block = fixed.propose, fixed.trial_targets, old.base.block
    def forbidden(*_, **__):
        raise RuntimeError("saved replay cannot propose roots or targets")
    fixed.propose = fixed.trial_targets = old.base.block = forbidden
    summaries, seen = [], {}
    try:
        for case_index, domain in enumerate(domains):
            own, ta, tb, face = domain["case"]
            tree, swapped = tree_for(domain, seen, pinned)
            todo = [(prior.ROOT_CUBE, 0)]
            leaves, maximum = 0, None
            for cursor, original in enumerate(tree):
                progress.update(case_index=case_index, node_cursor=cursor, checked_leaves=leaves)
                box, depth = todo[-1]
                node = prior.swap_node(original) if swapped else original
                if node[0] == "S":
                    axis = node[1]
                    assert type(axis) is int and axis in (0, 1, 2)
                    todo.pop()
                    todo.extend(adaptive.children(box, depth, axis))
                    continue
                assert node[0] == "L" and len(node) == 2
                witness, targets = node[1]["witness"], node[1]["targets"]
                assert len(targets) == 2
                pp, dp = fixed.parameters(box, (ta, tb), face)
                p0, _ = fixed.parameters([((lo+hi)/2,)*2 for lo, hi in box], (ta, tb), face)
                certificate = old.root_box(witness, pp, p0, own)
                assert certificate is not None, ("saved root", domain["case"], cursor)
                checker = fixed.check_source if domain["acceptance_rule"] == FIXED_RULE else adaptive.check_cell
                rows, detail = checker(box, pp, p0, dp, certificate, (ta, tb), own, targets)
                assert rows is not None, ("saved source", domain["case"], cursor, detail)
                assert [r["trial"] for r in rows] == targets
                for row in rows:
                    value = arb(row["upper_bound"]).upper()
                    maximum = value if maximum is None else max(maximum, value)
                todo.pop()
                leaves += 1
            assert not todo and leaves == domain["leaves"]
            summaries.append(dict(case=domain["case"], leaves=leaves,
                                  acceptance_rule=domain["acceptance_rule"],
                                  maximum_upper=str(maximum)))
            seen[tuple(domain["case"])] = domain
            print("REPLAY face", domain["case"], leaves, maximum, flush=True)
    finally:
        fixed.propose, fixed.trial_targets, old.base.block = proposal, trial, block
    return summaries


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    modes = ap.add_mutually_exclusive_group()
    modes.add_argument("--resume", type=Path, help="frozen incomplete author checkpoint")
    modes.add_argument("--input", type=Path, help="complete author record for saved replay")
    ap.add_argument("--output", type=Path,
                    default=ROOT/"repro/results/research-mixed-resumable-half-row-support.json")
    ap.add_argument("--max-nodes", type=int, default=MAX_NODES)
    ap.add_argument("--max-seconds", type=float, default=MAX_SECONDS)
    args = ap.parse_args()
    assert args.precision >= (320 if args.input else 192)
    assert 0 < args.max_nodes <= MAX_NODES and 0 < args.max_seconds <= MAX_SECONDS
    output = args.output.resolve()
    assert not output.exists(), "use a distinct new output; old records remain immutable"
    incoming_path = args.input or args.resume
    if incoming_path:
        assert output != incoming_path.resolve()
    ctx.prec = args.precision
    fixed.PI = old.PI = old.base.PI = arb.pi()
    fixed.II = old.II = old.base.I = acb(0, 1)
    assert CURVATURE == Q(14, 5)-2*KAPPA
    assert Q(720, 781)*Q(157, 50) > Q(14, 5)
    deps = {}
    def key(path):
        resolved = Path(path).resolve()
        try:
            return str(resolved.relative_to(ROOT))
        except ValueError:
            return str(resolved)
    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        if name in deps:
            assert deps[name] == digest, name
        deps[name] = digest
        return digest
    bind(WEAK_PIN, WEAK_SHA)
    weak = load(ROOT/WEAK_PIN)
    assert weak["status"] == "incomplete" and weak["case"] == list(WEAK_CASE)
    assert weak["acceptance_rule"] == OPTIMIZED_RULE
    assert weak["accepted_cells"] == 505 and weak["visited_nodes"] == len(weak["tree"]) == 1022
    assert weak["resolved_volume"] == "37/8192"
    assert weak["stopped_box"] is None
    for name, digest in weak["dependencies_sha256"].items():
        bind(name, digest)
    bind("notes/research_mixed_half_row_adaptive_continuation.md", weak["proof_sha256"])
    bind("experiments/continue_mixed_optimized_half_row_pilot.py", weak["script_sha256"])
    bind(FIXED_PIN, FIXED_SHA)
    fixed_source = load(ROOT/FIXED_PIN)
    assert fixed_source["status"] == "incomplete" and not fixed_source["pilot"]
    assert len(fixed_source["domains"]) == fixed_source["domain_count"] == 1
    pinned = fixed_source["domains"][0]
    assert pinned["case"] == [0, 0, 0, 0] and pinned["leaves"] == 96199
    frontier, count, volume, depth = inspect_tree(pinned["tree"], len(pinned["tree"]))
    assert not frontier and count == pinned["leaves"] and volume == 1
    assert depth == pinned["maximum_depth"]
    bind("notes/research_mixed_half_row_support.md", fixed_source["proof_sha256"])
    bind("experiments/certify_mixed_half_row_support.py", fixed_source["script_sha256"])
    del fixed_source
    weak_frontier, count, volume, depth = inspect_tree(weak["tree"], 511)
    assert weak_frontier == weak["pending"] and count == 505
    assert volume == Q(37, 8192) and depth == 18
    ph, sh = sha(PROOF), sha(__file__)
    incoming = None
    incoming_hash = None
    if incoming_path:
        incoming_hash = sha(incoming_path)
        incoming = load(incoming_path)
        assert incoming["format_version"] == 1 and incoming["mode"] == "author"
        assert incoming["proof_sha256"] == ph and incoming["script_sha256"] == sh
        assert incoming["strict_gap"] == str(GAP)
        assert incoming["half_cut"] == str(CUT) and incoming["kappa"] == str(KAPPA)
        assert incoming["optimized_target_curvature"] == str(CURVATURE)
        assert incoming["fixed_target_curvature"] == str(fixed.TARGET_CURVATURE)
        assert all(incoming["dependencies_sha256"].get(name) == digest
                   for name, digest in deps.items())
        for name, digest in incoming["dependencies_sha256"].items():
            bind(name, digest)
        bind(key(incoming_path), incoming_hash)
        assert incoming["status"] == ("passed" if args.input else "incomplete")
        domains = incoming["domains"]
        validate_domains(domains, pinned, weak, complete=bool(args.input))
        history = list(incoming["attempt_history"])
    else:
        domains = make_domains(pinned, weak)
        validate_domains(domains, pinned, weak)
        history = []
    initial_lengths = {tuple(d["case"]): len(d["tree"])
                       for d in domains if d["kind"] == "independent"}
    attempt = dict(number=len(history)+1, precision_bits=args.precision,
                   max_additional_nodes=args.max_nodes, max_seconds=args.max_seconds,
                   attempted_nodes=0, committed_nodes=0, accepted_cells=0,
                   root_proposals=0, failure_counts=dict(root=0, source=0),
                   split_policies=dict(adaptive_source=0, cyclic_root=0, cyclic_nonfinite=0),
                   split_axes=[0, 0, 0], worst_new_upper=None)
    last_attempt = None
    replay_progress = {}
    replay_summaries = None

    def record(status, reason, final_verified):
        refresh_swaps(domains)
        attempt.update(elapsed_seconds=time.monotonic()-PROGRAM_START,
                       status=status, stop_reason=reason)
        result = dict(
            format_version=1, mode="saved_replay" if args.input else "author",
            status=status, stop_reason=reason, precision_bits=args.precision,
            strict_gap=str(GAP), half_cut=str(CUT), kappa=str(KAPPA),
            optimized_target_curvature=str(CURVATURE),
            fixed_target_curvature=str(fixed.TARGET_CURVATURE),
            domains=domains, domain_count=12,
            completed_faces=sum(d["status"] == "complete" for d in domains),
            attempt_history=history if args.input else history+[dict(attempt)],
            proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
            resume_sha256=incoming_hash if args.resume else None,
            input_sha256=incoming_hash if args.input else None,
            final_bindings_verified=final_verified,
            scope="Twelve ordinary reference faces, both own flags and both conditional "
                  "orientations. Only a complete author and saved replay establish the "
                  "uniform half-row assertion; physical height restrictions remain.")
        if last_attempt is not None:
            result["uncommitted_attempt"] = last_attempt
        if args.input:
            result.update(replay_progress=dict(replay_progress),
                          replay_summaries=replay_summaries,
                          proposals=0, refinements=0)
        return result

    def publish(status, reason, final_verified=False):
        # Local commits preserve the partition. Full reconstruction and all
        # bindings are checked initially and before the final publication.
        assert sha(PROOF) == ph and sha(__file__) == sh
        atomic_json(output, record(status, reason, final_verified))

    def verify_final():
        refresh_swaps(domains)
        validate_domains(domains, pinned, weak)
        assert all(sha(ROOT/name) == digest for name, digest in deps.items())
        assert sha(PROOF) == ph and sha(__file__) == sh
        # Compare against newly read immutable inputs, not aliased Python lists.
        fresh_weak = load(ROOT/WEAK_PIN)
        weak_domain = domains[SPECS.index(WEAK_CASE)]
        assert weak_domain["tree"][:1022] == fresh_weak["tree"]
        if args.resume:
            assert sha(args.resume) == incoming_hash
            frozen = load(args.resume)
            for previous, current in zip(frozen["domains"], domains):
                assert previous["case"] == current["case"]
                assert previous["kind"] == current["kind"]
                assert previous["acceptance_rule"] == current["acceptance_rule"]
                if previous["kind"] == "independent":
                    assert current["tree"][:len(previous["tree"])] == previous["tree"]
                    if previous["status"] == "complete":
                        assert current["tree"] == previous["tree"]
        if args.input:
            assert sha(args.input) == incoming_hash
            assert domains == load(args.input)["domains"]
        if not args.input:
            appended = sum(len(d["tree"])-initial_lengths[tuple(d["case"])]
                           for d in domains if d["kind"] == "independent")
            assert appended == attempt["committed_nodes"]
            assert attempt["attempted_nodes"]-attempt["committed_nodes"] in (0, 1)
            assert attempt["accepted_cells"] <= attempt["committed_nodes"]

    handlers = {}
    def stop(signum, _frame):
        raise StopAttempt(signum)
    for signum in SIGNALS:
        handlers[signum] = signal.signal(signum, stop)
    status, reason = "incomplete", "initial checkpoint"
    last_checkpoint = time.monotonic()
    try:
        if args.input:
            publish("replay_incomplete", "saved replay in progress")
            replay_summaries = replay_all(domains, pinned, replay_progress)
            status, reason = "passed", "all twelve saved faces replayed"
        else:
            signal.setitimer(signal.ITIMER_REAL,
                             max(.001, args.max_seconds-(time.monotonic()-PROGRAM_START)))
            publish("incomplete", "initial checkpoint")
            while True:
                refresh_swaps(domains)
                if all(d["status"] == "complete" for d in domains):
                    status, reason = "passed", "all twelve faces complete"
                    break
                if attempt["attempted_nodes"] >= args.max_nodes:
                    reason = "additional-node budget"
                    break
                if time.monotonic()-PROGRAM_START >= args.max_seconds:
                    reason = "time budget including setup"
                    break
                domain = next(d for d in domains
                              if d["kind"] == "independent" and d["status"] == "incomplete")
                own, ta, tb, face = domain["case"]
                # The active box remains on the frontier until an atomic commit.
                box, depth = decode_frontier([domain["frontier"][-1]])[0]
                with atomic_section():
                    attempt["attempted_nodes"] += 1
                    last_attempt = dict(case=domain["case"], tree_cursor=len(domain["tree"]),
                                        box=[[str(v) for v in pair] for pair in box], depth=depth)
                pp, dp = fixed.parameters(box, (ta, tb), face)
                p0, _ = fixed.parameters([((lo+hi)/2,)*2 for lo, hi in box], (ta, tb), face)
                attempt["root_proposals"] += 1
                try:
                    proposed = fixed.propose(pp, p0, own)
                except (AssertionError, ValueError, ZeroDivisionError, OverflowError,
                        fixed.np.linalg.LinAlgError):
                    proposed = None
                rows, witness = None, None
                if proposed is None:
                    kind, detail = "root", dict(reason="root enclosure")
                else:
                    witness, certificate = proposed
                    kind = "source"
                    try:
                        rows, detail = adaptive.check_cell(box, pp, p0, dp, certificate,
                                                           (ta, tb), own)
                    except (AssertionError, ValueError, ZeroDivisionError, OverflowError) as exc:
                        detail = dict(reason="nonfinite interval or uncertain division",
                                      exception=type(exc).__name__)
                if rows is None and (depth >= MAX_DEPTH or detail["reason"] == "point exceeds requested gap"):
                    last_attempt.update(witness=witness,
                                        detail={k: v for k, v in detail.items() if k != "scores"})
                    status = "depth_limit" if depth >= MAX_DEPTH else "point_obstruction"
                    reason = detail["reason"]
                    break
                if rows is not None:
                    node = ["L", dict(witness=witness, targets=[r["trial"] for r in rows])]
                    worst = max(arb(r["upper_bound"]).upper() for r in rows)
                    with atomic_section():
                        domain["frontier"].pop()
                        domain["tree"].append(node)
                        domain["leaves"] += 1
                        domain["resolved_volume"] = str(Q(domain["resolved_volume"])+Q(1, 2**depth))
                        attempt["accepted_cells"] += 1
                        previous = attempt["worst_new_upper"]
                        attempt["worst_new_upper"] = str(worst if previous is None else max(worst, arb(previous).upper()))
                        attempt["committed_nodes"] += 1
                        domain["tree_nodes"] = len(domain["tree"])
                        domain["maximum_depth"] = max(domain["maximum_depth"], depth)
                        domain["status"] = "complete" if not domain["frontier"] else "incomplete"
                        last_attempt = None
                else:
                    axis = depth % 3
                    scores = detail.get("scores")
                    if kind == "root":
                        policy = "cyclic_root"
                    elif scores is None or not all(x.is_finite() for x in scores):
                        policy = "cyclic_nonfinite"
                    else:
                        assert len(scores) == 3
                        policy, axis = "adaptive_source", 0
                        for j in (1, 2):
                            if scores[j] > scores[axis]:
                                axis = j
                    children = encode_frontier(adaptive.children(box, depth, axis))
                    with atomic_section():
                        domain["frontier"].pop()
                        domain["tree"].append(["S", axis])
                        domain["frontier"].extend(children)
                        domain["tree_nodes"] = len(domain["tree"])
                        domain["maximum_depth"] = max(domain["maximum_depth"], depth)
                        attempt["failure_counts"][kind] += 1
                        attempt["split_policies"][policy] += 1
                        attempt["split_axes"][axis] += 1
                        attempt["committed_nodes"] += 1
                        last_attempt = None
                now = time.monotonic()
                if now-last_checkpoint >= CHECKPOINT_SECONDS:
                    publish("incomplete", "periodic checkpoint")
                    last_checkpoint = time.monotonic()
                    print("CHECKPOINT", attempt["attempted_nodes"], attempt["accepted_cells"],
                          "complete faces", sum(d["status"] == "complete" for d in domains),
                          "seconds", round(time.monotonic()-PROGRAM_START, 2), flush=True)
    except StopAttempt as exc:
        if args.input:
            status, reason = "replay_incomplete", "saved replay interrupted"
        else:
            status = "incomplete"
            reason = "time budget including setup" if exc.signum == signal.SIGALRM else "interrupted with frontier preserved"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        for signum, handler in handlers.items():
            signal.signal(signum, handler)

    with atomic_section():
        verify_final()
        if status == "passed":
            validate_domains(domains, pinned, weak, complete=True)
        publish(status, reason, final_verified=True)
    print(status, reason, "complete faces", sum(d["status"] == "complete" for d in domains),
          "additional", attempt["attempted_nodes"] if not args.input else 0,
          "new leaves", attempt["accepted_cells"] if not args.input else 0,
          "bindings", len(deps), "output", output, flush=True)
    return 0 if status == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
