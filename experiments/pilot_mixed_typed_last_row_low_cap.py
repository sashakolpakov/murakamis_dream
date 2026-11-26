#!/usr/bin/env python3
"""One low-height typed-envelope pilot: at most 511 nodes and 30 seconds.

Own epsilon is zero. The first external type-three input lies on the
slanted K3 chord, and the second type-four input fills the bottom K4 cap.
Both original conditional orientations, all four revived carriers, and
the complete target square are compulsory. This chord is outside O3 union
A3, so even a positive point would concern only this sufficient envelope.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import signal
import sys
import time

import numpy as np
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))
import pilot_mixed_attached_last_row_face as prior

old = prior.old
ar = old.ar
PROOF = ROOT / "notes/research_mixed_typed_last_row_support_design.md"
MAX_NODES = 511
MAX_SECONDS = 30
KAPPA = F(1, 2500000)
CURVATURE = F(1, 5)
LO, HI = F(11, 50), F(9, 20)
EXPECTED_ENVELOPES = 24


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interval(pair):
    return ar(pair[0]).union(ar(pair[1]))


def chart_constants():
    radical = ar(16906).sqrt()
    cminus = acb(ar("49/125"), -ar("9/125"))
    cplus = acb(ar("233/625")+3*radical/10000,
                -ar("49/625")+radical/10000)
    return cminus, cplus


def parameters(box):
    """Exact closed cap chart and its three real parameter derivatives."""
    t, u, v = map(interval, box)
    cminus, cplus = chart_constants()
    c = cminus+t*(cplus-cminus)
    h = -ar("27/250")+ar("3/500")*u
    radicand = ar("3/50")**2-(h+ar("13/250"))**2
    assert radicand > 0
    radius = radicand.sqrt()
    a = acb(ar("3/10")+(2*v-1)*radius, h)
    dp = [[cplus-cminus, acb(0), acb(0)],
          [acb(0), ar("3/500")*(II-(2*v-1)*(h+ar("13/250"))/radius),
           acb(2*radius)]]
    return [c, a], dp


def optimizer_enclosure(beta, trial):
    """Strongly decreasing target slope; includes clipped optimizers."""
    lower = (ar(trial)+min(arb(0), beta.lower())/ar(CURVATURE)).lower()
    upper = (ar(trial)+max(arb(0), beta.upper())/ar(CURVATURE)).upper()
    lower = max(ar(LO), lower)
    upper = min(ar(HI), upper)
    assert lower <= upper
    return lower.union(upper)


def check_deficits(box, pp, p0, dp, certificate):
    """Outward envelope mean values, with target gain only at midpoint.

    All derivatives are evaluated on an enclosure of the TRUE clipped
    optimizer, not at the fixed trial. This is the envelope theorem step.
    No derivative of a numerical target optimizer is used.
    """
    roots, points, response = (certificate[k] for k in ("root", "point", "response"))
    halfwidth = [ar((hi-lo)/2) for lo, hi in box]
    rows = []
    accepted = True
    positive = None
    for side in (0, 1):
        eta = side  # External order (type3 c, type4 a); own epsilon remains 0.
        a, s, b = pp[side], roots[side], roots[1-side]
        a0, s0, b0 = p0[side], points[side], points[1-side]
        P = prior.marginals(s, a, b, eta)
        P0 = prior.marginals(s0, a0, b0, eta)
        H = prior.hessian(s, a, b, eta)
        phase0 = prior.phase(s0, a0, b0, eta).real
        Zder = [dp[side],
                [sum((response[1-side][j]*dp[j][axis] for j in range(2)), acb(0))
                 for axis in range(3)]]
        trials = [LO, HI] if eta == 0 else [prior.trial_x(s0, a0, b0)]
        for trial in trials:
            assert LO <= trial <= HI
            at_trial = acb(ar(trial), a.imag)
            at_trial0 = acb(ar(trial), a0.imag)
            if eta:
                beta = (-old.gp(at_trial).real/2-P[0].real
                        +2*ar(KAPPA)*(ar(trial)-a.real))
                xenv = optimizer_enclosure(beta, trial)
                beta0 = (-old.gp(at_trial0).real/2-P0[0].real
                         +2*ar(KAPPA)*(ar(trial)-a0.real))
                midpoint_gain = prior.target_gain(beta0, trial)
            else:
                beta = beta0 = arb(0)
                xenv = ar(trial)
                midpoint_gain = arb(0)
            allocated0 = ar(eta)*old.g(at_trial0).real/2
            row_partial = -ar(eta)*old.gp(acb(xenv, a.imag))/2
            for z in (LO, HI):  # The second target is unweighted because own=0.
                delta = [xenv-a.real, ar(z)-b.real]
                delta0 = [ar(trial)-a0.real, ar(z)-b0.real]
                HD = [sum((H[i][j]*delta[j] for j in range(2)), acb(0))
                      for i in range(2)]
                DU = [-HD[i].real-2*ar(KAPPA)*delta[i] for i in range(2)]
                common0 = -allocated0-phase0
                common0 -= sum((P0[i].real*delta0[i] for i in range(2)), arb(0))
                common0 += ar(KAPPA)*sum((d*d for d in delta0), arb(0))
                for v in (0, 1):
                    for w in (0, 1):
                        midpoint = common0-2*PI*v*a0.imag+2*PI*w*b0.imag
                        Pc = [2*PI*II*v+row_partial, -2*PI*II*w]
                        DH = [(P[i]-Pc[i]+HD[i]).imag for i in range(2)]
                        derivatives = [
                            sum((DU[i]*Zder[i][axis].real+DH[i]*Zder[i][axis].imag
                                 for i in range(2)), arb(0))
                            for axis in range(3)]
                        error = sum((abs(derivatives[k])*halfwidth[k]
                                     for k in range(3)), arb(0))
                        bound = midpoint+midpoint_gain+error
                        assert all(value.is_finite() for value in
                                   [midpoint, midpoint_gain, error, bound]+derivatives)
                        record = dict(
                            side=side, eta=eta, own_epsilon=0,
                            carrier=[v, w], trial_target=[str(trial), str(z)],
                            optimizer_interval=[str(xenv.lower()), str(xenv.upper())],
                            whole_box_target_slope=str(beta),
                            midpoint_target_slope=str(beta0),
                            midpoint_trial_deficit=str(midpoint),
                            midpoint_target_gain=str(midpoint_gain),
                            envelope_parameter_derivatives=list(map(str, derivatives)),
                            envelope_meanvalue=str(error), upper=str(bound.upper()))
                        rows.append(record)
                        if not bound < 0:
                            accepted = False
                        # A positive fixed trial is enough; it is not inferred
                        # from the upper envelope or from a floating optimizer.
                        if midpoint > 0 and positive is None:
                            positive = record
    assert len(rows) == EXPECTED_ENVELOPES
    return accepted, rows, positive


def box_from_address(address):
    box = [(F(0), F(1))]*3
    for depth, bit in enumerate(address):
        box = old.split(box, depth % 3)[int(bit)]
    return box


def exact_frontier(nodes, pending, visits):
    """Verify every split has both children, and retain every unresolved box."""
    recorded = {}
    for node in nodes:
        address = node["address"]
        assert address not in recorded
        assert node["depth"] == len(address)
        assert node["box"] == [[str(v) for v in pair]
                               for pair in box_from_address(address)]
        if node["kind"] == "split":
            assert node["axis"] == len(address) % 3
        else:
            assert node["kind"] == "accepted"
        recorded[address] = node["kind"]
    frontier = {}
    for address, box, depth in pending:
        assert address not in recorded and address not in frontier
        assert depth == len(address)
        assert box == box_from_address(address)
        frontier[address] = depth
    all_addresses = set(recorded) | set(frontier)
    assert "" in all_addresses
    for address in all_addresses:
        if address:
            assert recorded.get(address[:-1]) == "split"
        if recorded.get(address) == "split":
            assert address+"0" in all_addresses and address+"1" in all_addresses
        else:
            assert address+"0" not in all_addresses and address+"1" not in all_addresses
    accepted_volume = sum((F(1, 2**len(a)) for a, kind in recorded.items()
                           if kind == "accepted"), F(0))
    pending_volume = sum((F(1, 2**d) for d in frontier.values()), F(0))
    assert accepted_volume+pending_volume == 1
    # One active box may have been popped when the deadline/positive stop fired.
    assert len(nodes) <= visits <= len(nodes)+1
    assert visits <= MAX_NODES
    return accepted_volume, pending_volume


def main():
    global PI, II
    start = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/diagnostics/2026-11-05-typed-last-row-low-cap/result.json")
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    PI, II = arb.pi(), acb(0, 1)
    prior.PI = old.PI = old.base.PI = PI
    prior.II = old.II = old.base.I = II
    assert prior.KAPPA == KAPPA and prior.CURVATURE == CURVATURE
    assert (prior.LO, prior.HI) == (LO, HI)
    assert F(9, 140)*F(157, 50)-2*KAPPA > CURVATURE
    # Exact chart identities: all points are in K3 x K4, including boundaries.
    assert F(3, 50)**2-F(7, 125)**2 == F(29, 62500)
    assert F(3, 50)**2-F(1, 20)**2 == F(11, 10000)
    assert F(49, 125)-3*(-F(9, 125)) == F(76, 125)
    assert (F(49, 125)-F(7, 20))**2+(-F(9, 125)+F(1, 100))**2 < F(83, 1000)**2
    cminus, cplus = chart_constants()
    assert -ar("9/125") < cplus.imag < -ar("13/200")
    assert cminus.real > ar("391/1000") and cplus.real > cminus.real
    # These rational identities give the upper endpoint's circle and line
    # equalities without an interval equality test on a square root.
    x0, x1 = F(233, 625)-F(7, 20), F(3, 10000)
    y0, y1 = -F(49, 625)+F(1, 100), F(1, 10000)
    assert x0*x0+y0*y0+16906*(x1*x1+y1*y1) == F(83, 1000)**2
    assert x0*x1+y0*y1 == 0
    assert F(233, 625)-3*(-F(49, 625)) == F(76, 125)
    assert x1 == 3*y1
    deps = {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        if name in deps:
            assert deps[name] == digest, name
        deps[name] = digest
        return digest

    def read(name):
        bind(name)
        obj = json.loads((ROOT/name).read_text())
        assert obj["status"] == "passed", name
        for path, digest in obj.get("dependencies_sha256", {}).items():
            bind(path, digest)
        return obj

    author_name = "repro/results/research-mixed-reduced-disk-conditional-packets.json"
    replay_name = "repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author, replay = read(author_name), read(replay_name)
    assert replay["input_sha256"] == deps[author_name]
    assert author["domain_count"] == replay["domain_count"] == 6
    assert len(author["domains"]) == len(replay["domains"]) == 6
    assert all(a["types"] == b["types"] and a["tree"] == b["tree"]
               and a["leaves"] == b["leaves"]
               for a, b in zip(author["domains"], replay["domains"]))
    for rec in (author, replay):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md", rec["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py", rec["script_sha256"])
    bind("experiments/pilot_mixed_attached_last_row_face.py")
    for name in (
        "research_mixed_attached_last_row_face_pilot",
        "research_mixed_typed_last_row_envelopes",
        "research_mixed_actual_last_row_reference_domains",
        "research_mixed_horizontal_revived_endpoint",
        "research_mixed_last_row_own_root_normal_form",
        "research_mixed_horizontal_tail_reference_boundary",
        "research_mixed_horizontal_zero_mode_support",
        "research_mixed_cyclic_critical_height_bounds",
        "research_mixed_open_local_factor_coverage",
        "research_mixed_open_word_endpoint_rectangles",
    ):
        bind("notes/"+name+".md")
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    todo = [("", [(F(0), F(1))]*3, 0)]
    nodes = []
    visits = accepted = 0
    active = None
    status, reason = "pilot_incomplete", "not started"
    positive = None
    failure_counts = dict(root=0, deficit=0)

    def expired(*_):
        raise prior.PilotDeadline()

    previous_handler = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, max(.000001, MAX_SECONDS-(time.monotonic()-start)))
    try:
        while todo:
            if visits >= MAX_NODES:
                reason = "511-node budget"
                break
            if time.monotonic()-start >= MAX_SECONDS:
                raise prior.PilotDeadline()
            with prior.atomic_bookkeeping():
                address, box, depth = todo.pop()
                active = dict(address=address, box=box, depth=depth)
                visits += 1
            pp, dp = parameters(box)
            p0, _ = parameters([((lo+hi)/2,)*2 for lo, hi in box])
            proposed = None
            detail = dict(reason="root enclosure")
            try:
                proposed = prior.propose(pp, p0)
                if proposed is not None:
                    witness, certificate = proposed
                    ok, rows, point = check_deficits(box, pp, p0, dp, certificate)
                    detail = dict(reason="deficit enclosure", rows=rows)
                    if point is not None:
                        positive = dict(
                            parameters=[str(z) for z in p0],
                            roots=[str(z) for z in certificate["point"]],
                            trial=point, witness=witness,
                            containing_address=address,
                            containing_box=[[str(v) for v in pair] for pair in box],
                            membership="Exact chart: K3 slanted chord times bottom K4 cap.",
                            actual_geometry="First input is outside O3 union A3.")
                        status = "positive_auxiliary_point"
                        reason = "outward positive fixed trial in the typed-envelope chart"
                        break
                    if ok:
                        with prior.atomic_bookkeeping():
                            nodes.append(dict(
                                address=address, depth=depth,
                                box=[[str(v) for v in pair] for pair in box],
                                kind="accepted", witness=witness, rows=rows))
                            accepted += 1
                            active = None
                        continue
            except (AssertionError, ValueError, ZeroDivisionError, OverflowError,
                    np.linalg.LinAlgError) as exc:
                detail = dict(reason="uncertain interval or proposal", exception=type(exc).__name__)
            failure_counts["root" if proposed is None else "deficit"] += 1
            axis = depth % 3
            left, right = old.split(box, axis)
            children = [(address+"0", left, depth+1), (address+"1", right, depth+1)]
            # LIFO: visit LOW t,u first and HIGH v first. Every visited box
            # lies in the low-height chart; the other child stays pending.
            if axis in (0, 1):
                children.reverse()
            with prior.atomic_bookkeeping():
                nodes.append(dict(address=address, depth=depth,
                                  box=[[str(v) for v in pair] for pair in box],
                                  kind="split", axis=axis, detail=detail))
                todo.extend(children)
                active = None
        else:
            status, reason = "pilot_subset_complete", "all boxes of this subset accepted"
    except prior.PilotDeadline:
        reason = "30-second budget including setup"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
    pending = list(todo)
    if active is not None:
        pending.append((active["address"], active["box"], active["depth"]))
    accepted_volume, pending_volume = exact_frontier(nodes, pending, visits)
    assert accepted == sum(node["kind"] == "accepted" for node in nodes)
    if status == "pilot_subset_complete":
        assert not pending and positive is None
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    result = dict(
        status=status, stop_reason=reason, precision_bits=args.precision,
        own_epsilon=0, external_types=[3, 4], boundary_slot=0,
        chart=dict(
            parameters=["t", "u", "v"], parameter_cube=["0", "1"],
            first="c=(1-t)*(49/125-9i/125)+t*(x_star+i*h_star)",
            h_star="-49/625+sqrt(16906)/10000",
            x_star="233/625+3*sqrt(16906)/10000",
            second="a=3/10+(2v-1)*sqrt((3/50)^2-(h+13/250)^2)+i*h",
            h="-27/250+(3/500)*u", radicand_lower="29/62500",
            membership="Entire chart lies in K3 x K4 by exact formulas.",
            exclusion="Entire first-input chord lies outside O3 union A3."),
        conditional_orientations=2, carrier_branches_per_orientation=4,
        target_interval=[str(LO), str(HI)], kappa=str(KAPPA),
        target_curvature=str(CURVATURE), target_envelopes_per_accepted_cell=EXPECTED_ENVELOPES,
        target_bound="Whole-box optimizer enclosures and midpoint-only target gains.",
        requested_deficit_upper="0", split_axes="depth modulo 3",
        child_priority=["low t", "low u", "high v"],
        max_nodes=MAX_NODES, max_seconds=MAX_SECONDS, visited_nodes=visits,
        accepted_cells=accepted, excluded_cells=0, failure_counts=failure_counts,
        nodes=nodes, pending=[dict(address=a, depth=d,
                                 box=[[str(v) for v in pair] for pair in box])
                                for a, box, d in pending],
        exact_accepted_parameter_volume=str(accepted_volume),
        exact_pending_parameter_volume=str(pending_volume),
        exact_terminal_and_pending_volume=str(accepted_volume+pending_volume),
        positive_point=positive, proof_sha256=proof_hash, script_sha256=script_hash,
        dependencies_sha256=deps, elapsed_seconds=time.monotonic()-start,
        scope="One bounded low-height auxiliary subset. No other face/type or actual-word "
              "realization is certified. A partial run proves no uniform sign; a positive "
              "point would refute only this sufficient typed-envelope comparison.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(status, reason, "nodes", visits, "accepted", accepted,
          "pending", len(pending), "bindings", len(deps),
          "seconds", round(result["elapsed_seconds"], 3), "output", args.output)
    return 0 if status == "pilot_subset_complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
