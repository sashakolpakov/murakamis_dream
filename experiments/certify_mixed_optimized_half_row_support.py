#!/usr/bin/env python3
"""Half-row envelope certificate; old leaves and exact swaps are replayed, never searched."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))
import certify_mixed_half_row_support as fixed

old = fixed.old
ar = fixed.ar
PROOF = ROOT / "notes/research_mixed_optimized_half_row_support.md"
METHOD = "notes/research_mixed_half_row_optimized_envelope.md"
STEM = "research-mixed-optimized-half-row-support"
PIN = "repro/results/research-mixed-half-row-support-partial.json"
PIN_SHA = "f326bde32741e73dee5b9f8475d31b897d16569cdc002d970f4cfa49219f0686"
FIXED_RULE = "fixed_trial_v1"
OPTIMIZED_RULE = "optimized_envelope_v1"
GAP, CUT, KAPPA = fixed.GAP, fixed.CUT, fixed.KAPPA
CURVATURE = Q(14, 5) - 2*KAPPA
LO, HI = Q(11, 50), Q(9, 20)
ROOT_CUBE = [(Q(0), Q(1))]*3


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024*1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split(box, depth):
    axis = depth % 3
    lo, hi = box[axis]
    middle = (lo+hi)/2
    left, right = list(box), list(box)
    left[axis], right[axis] = (lo, middle), (middle, hi)
    return axis, left, right


def complete_tree(tree, expected_leaves):
    """Reconstruct every dyadic box; counts alone do not establish coverage."""
    todo = [(ROOT_CUBE, 0)]
    leaves = 0
    for node in tree:
        assert todo
        box, depth = todo.pop()
        if node[0] == "S":
            assert len(node) == 2 and node[1] == depth % 3
            _, left, right = split(box, depth)
            todo.extend([(left, depth+1), (right, depth+1)])
        else:
            assert node[0] == "L" and len(node) == 2
            assert set(node[1]) == {"witness", "targets"}
            leaves += 1
    assert not todo and leaves == expected_leaves
    assert len(tree) == 2*leaves-1


def swap_node(node):
    """Exact S exchange of roots AND exterior coordinates; target orientations swap."""
    if node[0] == "S":
        return node
    assert node[0] == "L"
    data = node[1]
    w = data["witness"]
    assert set(w) == {"centers", "inverse", "affine", "radii"}
    swapped = dict(
        centers=list(reversed(w["centers"])),
        radii=list(reversed(w["radii"])),
        inverse=[[w["inverse"][1-i][1-j] for j in range(2)] for i in range(2)],
        affine=[[w["affine"][1-i][1-j] for j in range(2)] for i in range(2)])
    return ["L", dict(witness=swapped, targets=list(reversed(data["targets"])))]


def positive_upper(value):
    return arb(0) if value <= 0 else value.upper()


def one_sided_gain(slope, length):
    assert length >= 0
    if length == 0 or slope <= 0:
        return arb(0)
    beta = positive_upper(slope)
    if beta >= ar(CURVATURE*length):
        return beta*ar(length)-ar(CURVATURE*length*length)/2
    return beta*beta/(2*ar(CURVATURE))


def midpoint_gain(beta, trial):
    return max(arb(0),
               one_sided_gain(beta.upper(), HI-trial).upper(),
               one_sided_gain((-beta).upper(), trial-LO).upper())


def optimizer_interval(beta, trial):
    """All clipping and all sign decisions use exact rationals/outward intervals."""
    lower = ar(trial)-positive_upper(-beta)/ar(CURVATURE)
    upper = ar(trial)+positive_upper(beta)/ar(CURVATURE)
    result = lower.lower().union(upper.upper()).intersection(ar(LO).union(ar(HI)))
    assert result.is_finite()
    return result


def check_optimized(box, pp, p0, dp, certificate, types, own, targets=None):
    roots, points, response = (certificate[k] for k in ("root", "point", "response"))
    halfwidth = [ar((hi-lo)/2) for lo, hi in box]
    rows = []
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
        rows.append(dict(side=side, trial=[str(x) for x in trial],
                         midpoint=str(midpoint), midpoint_gains=[str(x) for x in gains0],
                         midpoint_maximum=str(midpoint_maximum),
                         optimizer_intervals=[str(x) for x in optimizers],
                         meanvalue=str(meanvalue), upper_bound=bound.upper().str(70)))
        if midpoint > -ar(GAP):
            return None, dict(reason="point exceeds requested gap", rows=rows)
        if not bound < -ar(GAP):
            return None, dict(reason="interval bound", rows=rows)
    return rows, dict(reason="passed", rows=rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--max-nodes", type=int, default=600000)
    ap.add_argument("--max-seconds", type=float, default=600)
    ap.add_argument("--max-depth", type=int, default=45)
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT/"repro/results"/(STEM+".json"))
    args = ap.parse_args()
    assert args.precision >= 192
    assert 0 < args.max_nodes <= 600000 and 0 < args.max_seconds <= 600
    assert 0 < args.max_depth <= 45
    if args.pilot:
        assert args.input is None
        args.max_nodes = min(args.max_nodes, 511)
        args.max_seconds = min(args.max_seconds, 60)
    start = time.monotonic()
    ctx.prec = args.precision
    fixed.PI = old.PI = old.base.PI = arb.pi()
    fixed.II = old.II = old.base.I = acb(0, 1)
    assert Q(720, 781)*Q(157, 50) > Q(14, 5)
    assert CURVATURE > 0 and Q(1, 1000) > GAP
    deps = {}
    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        if name in deps:
            assert deps[name] == digest, name
        deps[name] = digest
        return digest
    bind(PIN, PIN_SHA)
    with (ROOT/PIN).open() as handle:
        partial = json.load(handle)
    assert partial["status"] == "incomplete" and not partial["pilot"]
    assert partial["strict_gap"] == str(GAP)
    assert len(partial["domains"]) == partial["domain_count"] == 1
    pinned = partial["domains"][0]
    assert pinned["case"] == [0, 0, 0, 0] and pinned["leaves"] == 96199
    complete_tree(pinned["tree"], pinned["leaves"])
    for name, digest in partial["dependencies_sha256"].items():
        bind(name, digest)
    bind("notes/research_mixed_half_row_support.md", partial["proof_sha256"])
    bind("experiments/certify_mixed_half_row_support.py", partial["script_sha256"])
    del partial
    bind(METHOD, "48fcba6cfd5237e43efb5ec908b87671c0fb90cb0b08c0b7f859c0bbead11ac5")
    # Recheck the original complete author/replay relationship as well as their hashes.
    source_name = "repro/results/research-mixed-reduced-disk-conditional-packets.json"
    replay_name = "repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    with (ROOT/source_name).open() as handle:
        author = json.load(handle)
    with (ROOT/replay_name).open() as handle:
        previous = json.load(handle)
    assert author["status"] == previous["status"] == "passed"
    assert previous["input_sha256"] == deps[source_name]
    assert author["domain_count"] == previous["domain_count"] == 6
    assert len(author["domains"]) == len(previous["domains"]) == 6
    assert all(a["types"] == b["types"] and a["tree"] == b["tree"]
               and a["leaves"] == b["leaves"]
               for a, b in zip(author["domains"], previous["domains"]))
    ph, sh = sha(PROOF), sha(__file__)
    source_input = None
    ih = None
    if args.input:
        ih = sha(args.input)
        with args.input.open() as handle:
            source_input = json.load(handle)
        assert source_input["status"] == "passed" and not source_input["pilot"]
        assert source_input["proof_sha256"] == ph and source_input["script_sha256"] == sh
        assert source_input["dependencies_sha256"] == deps
        assert source_input["strict_gap"] == str(GAP)
        assert source_input["optimized_target_curvature"] == str(CURVATURE)
    specs = [(own, ta, tb, face) for own in (0, 1)
             for ta, tb in ((0, 0), (0, 1), (1, 1)) for face in (0, 1)]
    if args.pilot:
        specs = [(0, 1, 1, 0)]
    if source_input:
        assert [tuple(d["case"]) for d in source_input["domains"]] == specs
    domains = []
    by_case = {}
    visits = leaves = proposals = 0
    failures = dict(root=0, source=0)
    last_log = time.monotonic()

    def snapshot(status, active=None, reason=None):
        assert sha(PROOF) == ph and sha(__file__) == sh
        assert all(sha(ROOT/name) == digest for name, digest in deps.items())
        if args.input:
            assert sha(args.input) == ih
        result = dict(status=status, pilot=args.pilot, precision_bits=args.precision,
                      strict_gap=str(GAP), half_cut=str(CUT), kappa=str(KAPPA),
                      optimized_target_curvature=str(CURVATURE),
                      fixed_target_curvature=str(fixed.TARGET_CURVATURE),
                      domains=domains, domain_count=len(domains),
                      conditional_orientations=2, visited_nodes=visits,
                      accepted_cells=leaves, root_proposals=proposals,
                      failure_counts=failures, max_nodes=args.max_nodes,
                      max_seconds=args.max_seconds, max_depth=args.max_depth,
                      elapsed_seconds=time.monotonic()-start,
                      proof_sha256=ph, script_sha256=sh,
                      dependencies_sha256=deps, input_sha256=ih,
                      pinned_partial_sha256=PIN_SHA,
                      scope="Only a complete non-pilot twelve-face record proves a uniform "
                            "ordinary-reference half-row bound. Both allocations and original "
                            "lifts remain; physical height restrictions are separate.")
        if active is not None:
            result["incomplete_domain"] = active
        if reason is not None:
            result["stop_reason"] = reason
        path = args.output if status == "passed" else args.output.with_name(args.output.stem+"-partial.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as handle:
            json.dump(result, handle, indent=2)
            handle.write("\n")
        return path

    for case_index, case in enumerate(specs):
        own, ta, tb, face = case
        types = (ta, tb)
        if case == (0, 0, 0, 0):
            origin, rule, source_case = "pinned_partial", FIXED_RULE, None
            saved_tree = pinned["tree"]
        elif ta == tb and face == 1:
            origin, source_case = "equal_type_swap", (own, ta, tb, 0)
            source_domain = by_case[source_case]
            rule = source_domain["acceptance_rule"]
            saved_tree = source_domain["tree"]
        else:
            origin, rule, source_case = "search", OPTIMIZED_RULE, None
            saved_tree = None
        replay_domain = source_input["domains"][case_index] if source_input else None
        if replay_domain:
            assert replay_domain["origin"] == origin and replay_domain["acceptance_rule"] == rule
            if source_case is not None:
                assert replay_domain["source_case"] == list(source_case)
                assert "tree" not in replay_domain
            else:
                if saved_tree is not None:
                    assert replay_domain["tree"] == saved_tree
                saved_tree = replay_domain["tree"]
        todo = [(ROOT_CUBE, 0)]
        tree = []
        cursor = local_leaves = maximum_depth = 0
        maximum = None
        while todo:
            if visits >= args.max_nodes or time.monotonic()-start >= args.max_seconds:
                active = dict(case=list(case), origin=origin, acceptance_rule=rule,
                              source_case=list(source_case) if source_case else None,
                              tree=tree, leaves=local_leaves, source_cursor=cursor,
                              pending=[[[[str(v) for v in pair] for pair in box], depth]
                                       for box, depth in todo])
                path = snapshot("incomplete", active, "explicit node or time budget")
                print("INCOMPLETE", visits, leaves, path, flush=True)
                return 2
            box, depth = todo.pop()
            visits += 1
            pp, dp = fixed.parameters(box, types, face)
            p0, _ = fixed.parameters([((lo+hi)/2,)*2 for lo, hi in box], types, face)
            if saved_tree is not None:
                assert cursor < len(saved_tree)
                node = saved_tree[cursor]
                cursor += 1
                if origin == "equal_type_swap":
                    node = swap_node(node)
                if node[0] == "S":
                    assert len(node) == 2 and node[1] == depth % 3
                    _, left, right = split(box, depth)
                    todo.extend([(left, depth+1), (right, depth+1)])
                    tree.append(node)
                    continue
                assert node[0] == "L" and len(node) == 2
                witness, targets = node[1]["witness"], node[1]["targets"]
                assert len(targets) == 2
                certificate = old.root_box(witness, pp, p0, own)
                assert certificate is not None, ("saved root", case, cursor)
                checker = fixed.check_source if rule == FIXED_RULE else check_optimized
                rows, detail = checker(box, pp, p0, dp, certificate, types, own, targets)
                assert rows is not None, ("saved acceptance", case, cursor, detail)
            else:
                assert rule == OPTIMIZED_RULE and args.input is None
                proposals += 1
                proposed = fixed.propose(pp, p0, own)
                rows = None
                witness = None
                if proposed is None:
                    reason, detail = "root", dict(reason="root")
                else:
                    witness, certificate = proposed
                    reason = "source"
                    try:
                        rows, detail = check_optimized(box, pp, p0, dp, certificate, types, own)
                    except (AssertionError, ValueError, ZeroDivisionError) as exc:
                        detail = dict(reason="uncertain interval or division", exception=type(exc).__name__)
                if rows is None:
                    if depth >= args.max_depth or detail["reason"] == "point exceeds requested gap":
                        active = dict(case=list(case), origin=origin, acceptance_rule=rule,
                                      tree=tree, leaves=local_leaves, failing_depth=depth,
                                      failing_box=[[str(v) for v in pair] for pair in box],
                                      witness=witness, detail=detail,
                                      pending=[[[[str(v) for v in pair] for pair in box], dd]
                                               for box, dd in todo])
                        path = snapshot("incomplete", active, detail["reason"])
                        print("INCOMPLETE", case, visits, leaves, detail, path, flush=True)
                        return 2
                    failures[reason] += 1
                    axis, left, right = split(box, depth)
                    todo.extend([(left, depth+1), (right, depth+1)])
                    tree.append(["S", axis])
                    continue
                node = ["L", dict(witness=witness, targets=[row["trial"] for row in rows])]
            tree.append(node)
            leaves += 1
            local_leaves += 1
            maximum_depth = max(maximum_depth, depth)
            for row in rows:
                bound = arb(row["upper_bound"]).upper()
                maximum = bound if maximum is None else max(maximum, bound)
            now = time.monotonic()
            if now-last_log >= 10:
                print("progress", case, visits, leaves, len(todo), round(now-start, 2), flush=True)
                last_log = now
        complete_tree(tree, local_leaves)
        if saved_tree is not None:
            assert cursor == len(saved_tree)
            if origin != "equal_type_swap":
                assert tree == saved_tree
        if replay_domain:
            assert local_leaves == replay_domain["leaves"]
        domain = dict(case=list(case), acceptance_rule=rule, origin=origin,
                      leaves=local_leaves, maximum_depth=maximum_depth,
                      maximum_upper=str(maximum))
        if source_case is None:
            domain["tree"] = tree
        else:
            domain["source_case"] = list(source_case)
        domains.append(domain)
        by_case[case] = domain
        print("PASS face", case, rule, local_leaves, maximum, round(time.monotonic()-start, 2), flush=True)
    assert len(domains) == len(specs) and visits == 2*leaves-len(specs)
    if args.input:
        assert proposals == 0
    path = snapshot("pilot_complete" if args.pilot else "passed")
    print("PILOT" if args.pilot else "PASS", len(specs), leaves, visits, len(deps), path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
