#!/usr/bin/env python3
"""Exactly one clipped attached face; hard limits 511 nodes and 30 seconds.

No source-domain or global last-row conclusion follows from a partial run.
Floating operations only propose original-log affine witnesses and targets.
"""
import argparse
from contextlib import contextmanager
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
import certify_mixed_reduced_disk_conditional_packets as old

PROOF = ROOT / "notes/research_mixed_attached_last_row_face_pilot.md"
MAX_NODES = 511
MAX_SECONDS = 30
KAPPA = F(1, 2500000)
CURVATURE = F(1, 5)
LO, HI = F(11, 50), F(9, 20)
CLIP = (F(123, 500), F(7, 20), -F(27, 250), -F(1, 50))
ar = old.ar


class PilotDeadline(Exception):
    pass


@contextmanager
def atomic_bookkeeping():
    """Let a pending deadline fire only after a box has one recorded fate."""
    mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGALRM})
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, mask)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def iv(pair):
    return ar(pair[0]).union(ar(pair[1]))


def parameters(box):
    t, rho, theta = map(iv, box)
    c = acb(ar("391/1000"), -ar("9/125")+ar("93/1000")*t)
    radial = ar("3/50")*(2*PI*II*theta).exp()
    a = acb(ar("3/10"), -ar("13/250"))+rho*radial
    derivative = [[II*ar("93/1000"), acb(0), acb(0)],
                  [acb(0), radial, 2*PI*II*rho*radial]]
    return [c, a], derivative


def outside_clip(a):
    xl, xu, yl, yu = map(ar, CLIP)
    return a.real < xl or a.real > xu or a.imag < yl or a.imag > yu


def inside_clip(a):
    xl, xu, yl, yu = map(ar, CLIP)
    return xl <= a.real <= xu and yl <= a.imag <= yu


def propose(pp, p0):
    fp = [complex(float(z.real.mid()), float(z.imag.mid())) for z in p0]
    roots, derivative, residual = old.base.block(
        [fp[0].real, fp[0].imag, fp[1].real, fp[1].imag], 0)
    if residual > 1e-9:
        return None
    centers = [old.encode(z) for z in roots]
    _, J0 = old.base.evalf(list(map(old.cp, centers)), *p0, 2)
    floating = np.array([[complex(float(z.real.mid()), float(z.imag.mid()))
                          for z in row] for row in J0])
    inverse = np.linalg.inv(floating)
    witness = dict(centers=centers,
                   inverse=[[old.encode(z) for z in row] for row in inverse],
                   affine=[[old.encode(z) for z in row] for row in derivative])
    *_, radii0 = old.components(witness, pp, p0, 0)
    if any(not r.is_finite() for r in radii0):
        return None
    for factor in (F(5, 4), F(3, 2), F(2)):
        witness["radii"] = [str(F(max(1, int(np.ceil(float(r.upper())
                                         *float(factor)*2**40))), 2**40))
                            for r in radii0]
        certificate = old.root_box(witness, pp, p0, 0)
        if certificate is not None:
            return witness, certificate
    return None


def g2(z):
    q = (-2*PI*II*z).exp()
    return 2*PI*II*q/(1-q)


def phase(s, a, b, eta):
    return old.phase(s, a, b, 0)-(1+ar(eta)/2)*old.g(a)-old.g(b)


def marginals(s, a, b, eta):
    return [old.gp(s+a)-(1+ar(eta)/2)*old.gp(a)+2*PI*II*s,
            old.gp(s+b)-old.gp(b)]


def hessian(s, a, b, eta):
    ss = g2(s+a)+g2(s+b)-2*g2(s)
    assert abs(ss) > 0
    off = [g2(s+a)+2*PI*II, g2(s+b)]
    diagonal = [g2(s+a)-(1+ar(eta)/2)*g2(a), g2(s+b)-g2(b)]
    return [[(diagonal[i] if i == j else acb(0))-off[i]*off[j]/ss
             for j in range(2)] for i in range(2)]


def trial_x(s, a, b):
    sf, af, bf = [complex(float(z.real.mid()), float(z.imag.mid())) for z in (s, a, b)]
    gp = lambda z: np.log(1-np.exp(-2j*np.pi*z))
    pa = (gp(sf+af)-1.5*gp(af)+2j*np.pi*sf).real
    radius = np.exp(2*np.pi*af.imag)
    target = np.exp(-4*pa)
    distance = lambda x: 1+radius*radius-2*radius*np.cos(2*np.pi*x)
    if target <= distance(float(LO)):
        x = LO
    elif target >= distance(float(HI)):
        x = HI
    else:
        xf = np.arccos((1+radius*radius-target)/(2*radius))/(2*np.pi)
        x = F(round(float(xf)*10**12), 10**12)
    assert LO <= x <= HI
    return x


def one_sided_gain(slope, length):
    assert length >= 0
    if length == 0 or slope <= 0:
        return arb(0)
    beta = max(arb(0), slope.upper())
    if beta >= ar(CURVATURE*length):
        return beta*ar(length)-ar(CURVATURE*length*length)/2
    return beta*beta/(2*ar(CURVATURE))


def target_gain(beta, trial):
    return max(arb(0),
               one_sided_gain(beta.upper(), HI-trial).upper(),
               one_sided_gain((-beta).upper(), trial-LO).upper())


def check_deficits(box, pp, p0, dp, certificate):
    roots, points, response = (certificate[k] for k in ("root", "point", "response"))
    halfwidth = [ar((hi-lo)/2) for lo, hi in box]
    rows = []
    accepted = True
    positive = None
    for side in (0, 1):
        eta = side  # Input order is type3 c, type4 a; own epsilon stays zero.
        a, s, b = pp[side], roots[side], roots[1-side]
        a0, s0, b0 = p0[side], points[side], points[1-side]
        P, P0 = marginals(s, a, b, eta), marginals(s0, a0, b0, eta)
        H = hessian(s, a, b, eta)
        Zder = [dp[side],
                [sum((response[1-side][j]*dp[j][axis] for j in range(2)), acb(0))
                 for axis in range(3)]]
        xvalues = [LO, HI] if eta == 0 else [trial_x(s0, a0, b0)]
        for x in xvalues:
            for z in (LO, HI):
                aa = acb(ar(x), a.imag)
                aa0 = acb(ar(x), a0.imag)
                delta = [ar(x)-a.real, ar(z)-b.real]
                delta0 = [ar(x)-a0.real, ar(z)-b0.real]
                HD = [sum((H[i][j]*delta[j] for j in range(2)), acb(0))
                      for i in range(2)]
                DU = [-HD[i].real-2*ar(KAPPA)*delta[i] for i in range(2)]
                for v in (0, 1):
                    for w in (0, 1):
                        row0 = -2*PI*v*a0.imag+2*PI*w*b0.imag-ar(eta)*old.g(aa0).real/2
                        midpoint = row0-phase(s0, a0, b0, eta).real
                        midpoint -= sum((P0[i].real*delta0[i] for i in range(2)), arb(0))
                        midpoint += ar(KAPPA)*sum((d*d for d in delta0), arb(0))
                        Pc = [2*PI*II*v-ar(eta)*old.gp(aa)/2, -2*PI*II*w]
                        DH = [(P[i]-Pc[i]+HD[i]).imag for i in range(2)]
                        derivatives = [sum((DU[i]*Zder[i][axis].real
                                            +DH[i]*Zder[i][axis].imag
                                            for i in range(2)), arb(0)) for axis in range(3)]
                        error = sum((abs(derivatives[k])*halfwidth[k] for k in range(3)), arb(0))
                        beta = Pc[0].real-P[0].real+2*ar(KAPPA)*delta[0]
                        gain = target_gain(beta, x) if eta else arb(0)
                        bound = midpoint+error+gain
                        assert bound.is_finite()
                        record = dict(side=side, eta=eta, own_epsilon=0,
                                      carrier=[v, w], target=[str(x), str(z)],
                                      midpoint=str(midpoint), meanvalue=str(error),
                                      target_gain=str(gain), upper=str(bound.upper()))
                        rows.append(record)
                        if not bound < 0:
                            accepted = False
                        if midpoint > 0 and inside_clip(p0[1]):
                            positive = record
    assert len(rows) == 24
    return accepted, rows, positive


def main():
    global PI, II
    start = time.monotonic()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--output", type=Path,
                    default=Path("/tmp/research-mixed-attached-last-row-face-pilot.json"))
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    PI = arb.pi(); II = acb(0, 1)
    old.PI = PI; old.II = II; old.base.PI = PI; old.base.I = II
    assert F(41, 1000)**2+F(62, 1000)**2 < F(83, 1000)**2
    assert F(9, 140)*F(157, 50)-2*KAPPA > CURVATURE
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
    an = "repro/results/research-mixed-reduced-disk-conditional-packets.json"
    rn = "repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author, replay = read(an), read(rn)
    assert replay["input_sha256"] == deps[an]
    assert author["domain_count"] == replay["domain_count"] == 6
    assert len(author["domains"]) == len(replay["domains"]) == 6
    assert all(a["types"] == b["types"] and a["tree"] == b["tree"]
               and a["leaves"] == b["leaves"]
               for a, b in zip(author["domains"], replay["domains"]))
    for rec in (author, replay):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md", rec["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py", rec["script_sha256"])
    for name in (
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
    ph, sh = sha(PROOF), sha(__file__)
    todo = [("", [(F(0), F(1))]*3, 0)]
    nodes = []
    terminals = []
    visits = accepted = excluded = 0
    active = None
    status, reason = "pilot_incomplete", "not started"
    positive = None
    failure_counts = dict(root=0, deficit=0)
    def expired(*_):
        raise PilotDeadline()
    previous_handler = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, max(.000001, MAX_SECONDS-(time.monotonic()-start)))
    try:
        while todo:
            if visits >= MAX_NODES:
                reason = "511-node budget"
                break
            if time.monotonic()-start >= MAX_SECONDS:
                raise PilotDeadline()
            with atomic_bookkeeping():
                address, box, depth = todo.pop()
                active = dict(address=address, box=box, depth=depth)
                visits += 1
            pp, dp = parameters(box)
            p0, _ = parameters([((lo+hi)/2,)*2 for lo, hi in box])
            if outside_clip(pp[1]):
                with atomic_bookkeeping():
                    nodes.append(dict(address=address, kind="excluded"))
                    terminals.append((address, depth)); excluded += 1; active = None
                continue
            proposed = None
            detail = dict(reason="root enclosure")
            try:
                proposed = propose(pp, p0)
                if proposed is not None:
                    witness, certificate = proposed
                    ok, rows, point = check_deficits(box, pp, p0, dp, certificate)
                    detail = dict(reason="deficit enclosure", rows=rows)
                    if point is not None:
                        positive = dict(parameters=[str(z) for z in p0],
                                        roots=[str(z) for z in certificate["point"]],
                                        trial=point, witness=witness,
                                        box=[[str(v) for v in row] for row in box])
                        reason = "outward positive point inside the clipped face"
                        break
                    if ok:
                        with atomic_bookkeeping():
                            nodes.append(dict(address=address, kind="accepted",
                                              witness=witness, rows=rows))
                            terminals.append((address, depth)); accepted += 1; active = None
                        continue
            except (AssertionError, ValueError, ZeroDivisionError, OverflowError,
                    np.linalg.LinAlgError) as exc:
                detail = dict(reason="uncertain interval or proposal", exception=type(exc).__name__)
            failure_counts["root" if proposed is None else "deficit"] += 1
            axis = depth % 3
            left, right = old.split(box, axis)
            with atomic_bookkeeping():
                nodes.append(dict(address=address, kind="split", axis=axis, detail=detail))
                todo.extend([(address+"0", left, depth+1), (address+"1", right, depth+1)])
                active = None
        else:
            status, reason = "pilot_face_complete", "all boxes accepted or rigorously excluded"
    except PilotDeadline:
        reason = "30-second budget including setup"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
    pending = list(todo)
    if active is not None:
        pending.append((active["address"], active["box"], active["depth"]))
    coverage = sum((F(1, 2**depth) for _, depth in terminals), F(0))
    coverage += sum((F(1, 2**depth) for _, _, depth in pending), F(0))
    assert coverage == 1
    assert visits <= MAX_NODES
    if status == "pilot_face_complete":
        assert not pending and positive is None
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    result = dict(
        status=status, stop_reason=reason, precision_bits=args.precision,
        own_epsilon=0, external_types=[3, 4], roles=["attached", "attached"],
        face="Re c=391/1000; Im c in [-9/125,21/1000]; a in clipped A4",
        conditional_orientations=2, carrier_branches_per_orientation=4,
        target_interval=[str(LO), str(HI)], kappa=str(KAPPA), target_curvature=str(CURVATURE),
        target_trials_per_accepted_cell=24, requested_deficit_upper="0",
        max_nodes=MAX_NODES, max_seconds=MAX_SECONDS, visited_nodes=visits,
        accepted_cells=accepted, excluded_cells=excluded, failure_counts=failure_counts,
        nodes=nodes, pending=[dict(address=address, depth=depth,
                                 box=[[str(v) for v in row] for row in box])
                                for address, box, depth in pending],
        exact_terminal_and_pending_volume=str(coverage), positive_point=positive,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        elapsed_seconds=time.monotonic()-start,
        scope="One bounded face pilot only. No other face/type/role or actual-word realization "
              "is certified; an incomplete run carries no uniform sign claim.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(status, reason, "nodes", visits, "accepted", accepted, "excluded", excluded,
          "bindings", len(deps), "seconds", round(result["elapsed_seconds"], 3),
          "output", args.output)
    return 0 if status == "pilot_face_complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
