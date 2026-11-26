#!/usr/bin/env python3
"""One 511-additional-node adaptive continuation of the pinned weak-face pilot."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

PROGRAM_START = time.monotonic()
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"experiments"))
import certify_mixed_optimized_half_row_support as prior

fixed, old, ar = prior.fixed, prior.old, prior.ar
CUT, GAP, KAPPA, CURVATURE = prior.CUT, prior.GAP, prior.KAPPA, prior.CURVATURE
LO, HI = prior.LO, prior.HI
optimizer_interval, midpoint_gain = prior.optimizer_interval, prior.midpoint_gain
SOURCE = "repro/diagnostics/2026-11-05-optimized-half-row-support-pilot/result-partial.json"
SOURCE_SHA = "16e0ffe2e8b2ad6d33ecefbf34f1c6f01523d49102072d06ecf145ac20cec145"
PROOF = ROOT/"notes/research_mixed_half_row_adaptive_continuation.md"
MAX_NODES, MAX_SECONDS, MAX_DEPTH = 511, 60, 45
CASE = [0, 1, 1, 0]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024*1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def children(box, depth, axis):
    assert axis in (0, 1, 2)
    lo, hi = box[axis]
    mid = (lo+hi)/2
    left, right = list(box), list(box)
    left[axis], right[axis] = (lo, mid), (mid, hi)
    return (left, depth+1), (right, depth+1)


def reconstruct(tree, cyclic_prefix):
    """Arbitrary stored axes after the immutable old cyclic prefix."""
    todo = [([(Q(0), Q(1))]*3, 0)]
    leaves, volume, maximum_depth = 0, Q(0), 0
    for index, node in enumerate(tree):
        assert todo
        box, depth = todo.pop()
        maximum_depth = max(maximum_depth, depth)
        if node[0] == "S":
            assert len(node) == 2 and type(node[1]) is int and node[1] in (0, 1, 2)
            if index < cyclic_prefix:
                assert node[1] == depth % 3
            todo.extend(children(box, depth, node[1]))
        else:
            assert node[0] == "L" and len(node) == 2
            assert set(node[1]) == {"witness", "targets"}
            leaves += 1
            volume += Q(1, 2**depth)
    assert volume+sum((Q(1, 2**d) for _, d in todo), Q(0)) == 1
    return todo, leaves, volume, maximum_depth


# The optimized formulas below are copied from the frozen implementation.
# Only the interval-failure return is deferred until both orientations have
# been evaluated, and their parameter contributions are returned as scores.

def check_cell(box, pp, p0, dp, certificate, types, own, targets=None):
    roots, points, response = (certificate[k] for k in ("root", "point", "response"))
    halfwidth = [ar((hi-lo)/2) for lo, hi in box]
    rows = []
    axis_costs = []
    cut = acb(ar(CUT))
    for side in (0, 1):
        eta = types[side]
        a, s, b = pp[side], roots[side], roots[1-side]
        a0, s0, b0 = p0[side], points[side], points[1-side]
        trial = (fixed.trial_targets(s0, a0, b0, eta, own) if targets is None
                 else list(map(Q, targets[side])))
        assert len(trial) == 2 and all(LO <= x <= HI for x in trial)
        P = fixed.marginals(s, a, b, eta, own)
        P0 = fixed.marginals(s0, a0, b0, eta, own)
        H = fixed.hessian(s, a, b, eta, own)
        trial_z = [acb(ar(trial[0]), a.imag), acb(ar(trial[1]), b.imag)]
        trial_z0 = [acb(ar(trial[0]), a0.imag), acb(ar(trial[1]), b0.imag)]
        delta_hat = [ar(trial[0])-a.real, ar(trial[1])-b.real]
        delta0 = [ar(trial[0])-a0.real, ar(trial[1])-b0.real]
        Pc_hat = fixed.marginals(cut, *trial_z, eta, own)
        Pc0 = fixed.marginals(cut, *trial_z0, eta, own)
        beta = [Pc_hat[i].real-P[i].real+2*ar(KAPPA)*delta_hat[i] for i in range(2)]
        beta0 = [Pc0[i].real-P0[i].real+2*ar(KAPPA)*delta0[i] for i in range(2)]
        optimizers = [optimizer_interval(beta[i], trial[i]) for i in range(2)]
        gains0 = [midpoint_gain(beta0[i], trial[i]) for i in range(2)]
        midpoint = (fixed.phase(cut, *trial_z0, eta, own)
                    - fixed.phase(s0, a0, b0, eta, own)).real
        midpoint -= sum((P0[i].real*delta0[i] for i in range(2)), arb(0))
        midpoint += ar(KAPPA)*sum((d*d for d in delta0), arb(0))
        midpoint_maximum = midpoint+sum(gains0, arb(0))

        # Differentiate V at its unknown optimizer, enclosed by optimizers.
        optimal_z = [acb(optimizers[0], a.imag), acb(optimizers[1], b.imag)]
        delta = [optimizers[0]-a.real, optimizers[1]-b.real]
        Pc = fixed.marginals(cut, *optimal_z, eta, own)
        Hd = [sum((H[i][j]*delta[j] for j in range(2)), acb(0)) for i in range(2)]
        DU = [-Hd[i].real-2*ar(KAPPA)*delta[i] for i in range(2)]
        DH = [(P[i]-Pc[i]+Hd[i]).imag for i in range(2)]
        Zder = [dp[side],
                [sum((response[1-side][j]*dp[j][axis] for j in range(2)), acb(0))
                 for axis in range(3)]]
        gradient = [sum((DU[i]*Zder[i][axis].real+DH[i]*Zder[i][axis].imag
                         for i in range(2)), arb(0)) for axis in range(3)]
        meanvalue = sum((abs(gradient[j])*halfwidth[j] for j in range(3)), arb(0))
        bound = midpoint_maximum+meanvalue
        assert bound.is_finite()
        axis_costs.append([abs(gradient[j])*halfwidth[j] for j in range(3)])
        rows.append(dict(side=side, passed=bound < -ar(GAP), trial=[str(x) for x in trial],
                         midpoint=str(midpoint), midpoint_gains=[str(x) for x in gains0],
                         midpoint_maximum=str(midpoint_maximum),
                         optimizer_intervals=[str(x) for x in optimizers],
                         meanvalue=str(meanvalue), upper_bound=bound.upper().str(70)))
        if midpoint > -ar(GAP):
            return None, dict(reason="point exceeds requested gap", rows=rows)
    failed = [i for i, row in enumerate(rows) if not row["passed"]]
    if failed:
        scores = [max(axis_costs[i][j].upper() for i in failed) for j in range(3)]
        return None, dict(reason="interval bound", rows=rows, scores=scores)
    return rows, dict(reason="passed", rows=rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--output", type=Path,
                    default=ROOT/"repro/diagnostics/2026-11-05-adaptive-half-row-continuation/result.json")
    args = ap.parse_args()
    assert args.precision >= 192
    start = PROGRAM_START
    ctx.prec = args.precision
    fixed.PI = old.PI = old.base.PI = arb.pi()
    fixed.II = old.II = old.base.I = acb(0, 1)
    assert Q(720, 781)*Q(157, 50) > Q(14, 5)
    deps = {}
    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        if name in deps:
            assert deps[name] == digest, name
        deps[name] = digest
        return digest
    bind(SOURCE, SOURCE_SHA)
    with (ROOT/SOURCE).open() as handle:
        source = json.load(handle)
    assert source["status"] == "incomplete" and source["pilot"]
    assert source["domain_count"] == 0 and source["domains"] == []
    assert source["strict_gap"] == str(GAP)
    assert source["optimized_target_curvature"] == str(CURVATURE)
    for name, digest in source["dependencies_sha256"].items():
        bind(name, digest)
    bind("notes/research_mixed_optimized_half_row_support.md", source["proof_sha256"])
    bind("experiments/certify_mixed_optimized_half_row_support.py", source["script_sha256"])
    active_source = source["incomplete_domain"]
    assert active_source["case"] == CASE
    assert active_source["acceptance_rule"] == prior.OPTIMIZED_RULE
    assert active_source["origin"] == "search"
    initial_tree = active_source["tree"]
    initial_nodes = len(initial_tree)
    assert initial_nodes == source["visited_nodes"] == 511
    todo, initial_leaves, initial_volume, _ = reconstruct(initial_tree, initial_nodes)
    assert initial_leaves == source["accepted_cells"] == active_source["leaves"] == 249
    assert initial_volume == Q(535, 262144)
    saved_pending = [([(Q(x), Q(y)) for x, y in box], depth)
                     for box, depth in active_source["pending"]]
    assert todo == saved_pending and len(todo) == 14
    # No old numerical root/source test or proposal is repeated.
    tree = list(initial_tree)
    ph, sh = sha(PROOF), sha(__file__)
    additional = accepted = proposals = 0
    failures = dict(root=0, source=0)
    policies = dict(adaptive_source=0, cyclic_root=0, cyclic_nonfinite=0)
    decisions = []
    maximum = None
    stopped_box = None
    status, reason = "incomplete", "not started"
    last_log = time.monotonic()
    while todo:
        if additional >= MAX_NODES:
            reason = "511-additional-node budget"
            break
        if time.monotonic()-start >= MAX_SECONDS:
            reason = "60-second budget including setup"
            break
        box, depth = todo.pop()
        additional += 1
        pp, dp = fixed.parameters(box, (1, 1), 0)
        p0, _ = fixed.parameters([((lo+hi)/2,)*2 for lo, hi in box], (1, 1), 0)
        proposals += 1
        try:
            proposed = fixed.propose(pp, p0, 0)
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
                rows, detail = check_cell(box, pp, p0, dp, certificate, (1, 1), 0)
            except (AssertionError, ValueError, ZeroDivisionError, OverflowError) as exc:
                detail = dict(reason="nonfinite interval or uncertain division",
                              exception=type(exc).__name__)
        if rows is not None:
            tree.append(["L", dict(witness=witness, targets=[r["trial"] for r in rows])])
            accepted += 1
            for row in rows:
                value = arb(row["upper_bound"]).upper()
                maximum = value if maximum is None else max(maximum, value)
        else:
            if depth >= MAX_DEPTH or detail["reason"] == "point exceeds requested gap":
                # The attempted but uncommitted box remains on the exact frontier.
                todo.append((box, depth))
                printable = {k: v for k, v in detail.items() if k != "scores"}
                if "scores" in detail:
                    printable["scores"] = [str(x) for x in detail["scores"]]
                stopped_box = dict(box=[[str(v) for v in pair] for pair in box],
                                   depth=depth, witness=witness, detail=printable)
                reason = "depth cap" if depth >= MAX_DEPTH else detail["reason"]
                break
            failures[kind] += 1
            axis = depth % 3
            scores = detail.get("scores")
            if kind == "root":
                policy = "cyclic_root"
            elif scores is None or not all(x.is_finite() for x in scores):
                policy = "cyclic_nonfinite"
            else:
                assert len(scores) == 3
                policy = "adaptive_source"
                axis = 0
                for j in (1, 2):
                    if scores[j] > scores[axis]:
                        axis = j
            decision = dict(node_index=len(tree), depth=depth, axis=axis, policy=policy)
            if policy == "adaptive_source":
                decision["scores"] = [x.str(70) for x in scores]
                decision["failed_orientations"] = [r["side"] for r in detail["rows"] if not r["passed"]]
            decisions.append(decision)
            policies[policy] += 1
            tree.append(["S", axis])
            todo.extend(children(box, depth, axis))
        now = time.monotonic()
        if now-last_log >= 10:
            print("progress", additional, accepted, len(todo), round(now-start, 2), flush=True)
            last_log = now
    else:
        status, reason = "pilot_face_complete", "entire weak face resolved"

    reconstructed, total_leaves, volume, max_depth = reconstruct(tree, initial_nodes)
    assert reconstructed == todo
    assert tree[:initial_nodes] == initial_tree
    assert total_leaves == initial_leaves+accepted
    recorded = len(tree)-initial_nodes
    assert recorded+(stopped_box is not None) == additional == proposals
    assert additional <= MAX_NODES and max_depth <= MAX_DEPTH
    assert len(decisions) == sum(policies.values())
    assert all(tree[d["node_index"]] == ["S", d["axis"]] for d in decisions)
    assert sum(failures.values()) == len(decisions)
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/name) == digest for name, digest in deps.items())
    pending_volume = sum((Q(1, 2**d) for _, d in todo), Q(0))
    assert volume+pending_volume == 1
    result = dict(
        status=status, stop_reason=reason, precision_bits=args.precision,
        case=CASE, acceptance_rule=prior.OPTIMIZED_RULE,
        split_policy="recorded adaptive source cost; cyclic root/nonfinite fallback",
        strict_gap=str(GAP), optimized_target_curvature=str(CURVATURE),
        source_record=SOURCE, source_sha256=SOURCE_SHA,
        initial_nodes=initial_nodes, initial_accepted_cells=initial_leaves,
        initial_resolved_volume=str(initial_volume),
        additional_attempted_nodes=additional, additional_recorded_nodes=recorded,
        additional_accepted_cells=accepted, root_proposals=proposals,
        visited_nodes=len(tree), accepted_cells=total_leaves,
        maximum_depth=max_depth, new_maximum_upper=str(maximum),
        resolved_volume=str(volume), pending_volume=str(pending_volume),
        failure_counts=failures, split_policy_counts=policies,
        max_additional_nodes=MAX_NODES, max_seconds=MAX_SECONDS, max_depth=MAX_DEPTH,
        tree=tree, split_decisions=decisions,
        pending=[[[[str(v) for v in pair] for pair in box], depth] for box, depth in todo],
        stopped_box=stopped_box, elapsed_seconds=time.monotonic()-start,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="A single bounded continuation of one ordinary face. Imported accepted "
              "nodes are unchanged; no twelve-face or full-source theorem follows.")
    path = args.output if status == "pilot_face_complete" else args.output.with_name(args.output.stem+"-partial.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(status, reason, "additional", additional, "new leaves", accepted,
          "resolved", volume, "pending", pending_volume, "bindings", len(deps),
          "seconds", round(result["elapsed_seconds"], 3), "output", path, flush=True)
    return 0 if status == "pilot_face_complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
