#!/usr/bin/env python3
"""Resumable 72-chart typed last-row certificate; no run is implied by this file."""
import argparse
from contextlib import contextmanager
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time

PROGRAM_START = time.monotonic()
import numpy as np
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))
import pilot_mixed_attached_last_row_face as helper
import pilot_mixed_typed_last_row_low_cap as pinned_lowcap

old, ar = helper.old, helper.old.ar
PROOF = ROOT / "notes/research_mixed_typed_last_row_support_certificate.md"
DESIGN = "notes/research_mixed_typed_last_row_height_charts.md"
IMPORTED = "repro/diagnostics/2026-11-05-typed-last-row-low-cap/continuation.json"
IMPORTED_REPLAY = "repro/diagnostics/2026-11-05-typed-last-row-low-cap/continuation-replay.json"
PINS = {
    DESIGN: "438eeebdf30540ddaabaf18e04f67756071a66f83330f1bf85413f3aeec7b821",
    IMPORTED: "00b83fd73691bc24f1bf6e41db8481263eea39978912311c0b724a7b72b2cf69",
    IMPORTED_REPLAY: "9c532b9c0aea845f2e7ac4913d848e0f45078f3e500e567f734ac267c004697a",
}
KAPPA, CURVATURE = F(1, 2500000), F(1, 5)
LO, HI = F(11, 50), F(9, 20)
MAX_NODES, MAX_SECONDS, MAX_DEPTH = 200000, 300, 60
CHECKPOINT_SECONDS = 20
SIGNALS = {signal.SIGALRM, signal.SIGINT, signal.SIGTERM}
CUBE = [(F(0), F(1))] * 3
BOUNDARIES = {3: ("L3", "R3", "H3-", "H3+", "S3"),
              4: ("L4", "R4", "H4-", "H4+")}


class StopAttempt(Exception):
    def __init__(self, signum):
        self.signum = signum


@contextmanager
def atomic_section():
    previous = signal.pthread_sigmask(signal.SIG_BLOCK, SIGNALS)
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, previous)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for part in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(part)
    return digest.hexdigest()


def load(path):
    with Path(path).open() as handle:
        return json.load(handle)


def publish(path, record):
    """Atomic durable replacement of this attempt's distinct output only."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with atomic_section():
        try:
            with temporary.open("w") as handle:
                json.dump(record, handle, separators=(",", ":"))
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


def specifications():
    result = []
    for own in (0, 1):
        for types in ((3, 3), (3, 4), (4, 4)):
            for slot in ((0,) if types[0] == types[1] else (0, 1)):
                for curve in BOUNDARIES[types[slot]]:
                    for piece in ("lower", "upper"):
                        result.append(dict(own=own, types=list(types), slot=slot,
                                           curve=curve, piece=piece))
    assert len(result) == 72
    return result


SPECS = specifications()
IMPORT_SPEC = dict(own=0, types=[3, 4], slot=0, curve="S3", piece="lower")
IMPORT_INDEX = SPECS.index(IMPORT_SPEC)


def interval(pair):
    return ar(pair[0]).union(ar(pair[1]))


def hstar():
    return -ar("49/625") + ar(16906).sqrt() / 10000


def constants(n):
    if n == 3:
        return (ar("7/20"), -ar("1/100"), ar("83/1000"),
                -ar("9/125"), ar("17/250"))
    assert n == 4
    return (ar("3/10"), -ar("13/250"), ar("3/50"),
            -ar("27/250"), -ar("1/1000"))


def radius(n, h):
    _, center_h, r, _, _ = constants(n)
    square = r*r - (h-center_h)**2
    assert square > 0
    value = square.sqrt()
    return value, -(h-center_h)/value


def height_limits(n, piece):
    _, _, _, lower, upper = constants(n)
    cut = hstar() if n == 3 else -ar("51/500")
    assert piece in ("lower", "upper")
    return (lower, cut) if piece == "lower" else (cut, upper)


def endpoints(n, h, slanted=False):
    center, _, _, _, _ = constants(n)
    r, rp = radius(n, h)
    left, left_p = center-r, -rp
    if slanted:
        assert n == 3
        return left, ar("76/125")+3*h, left_p, ar(3)
    return left, center+r, left_p, rp


def disk_chart(n, piece, u, v):
    lower, upper = height_limits(n, piece)
    dh = upper-lower
    h = lower+dh*u
    if n != 3 or piece != "lower":
        # Keep the shared radius correlated. The algebraically equal
        # left+v*(right-left) expression unnecessarily enlarges intervals.
        center, _, _, _, _ = constants(n)
        r, rp = radius(n, h)
        return acb(center+(2*v-1)*r, h), dh*acb((2*v-1)*rp, 1), acb(2*r)
    left, right, lp, rp = endpoints(n, h, n == 3 and piece == "lower")
    width = right-left
    assert width > 0
    value = acb(left+v*width, h)
    du = dh*acb(lp+v*(rp-lp), 1)
    dv = acb(width)
    return value, du, dv


def boundary_chart(n, curve, t):
    center, _, _, lower, upper = constants(n)
    if curve == "S3":
        assert n == 3
        dh = hstar()-lower
        h = lower+dh*t
        return acb(ar("76/125")+3*h, h), dh*acb(3, 1)
    if curve in ("H3-", "H3+", "H4-", "H4+"):
        assert curve[1] == str(n)
        h = lower if curve.endswith("-") else upper
        left, right, _, _ = endpoints(n, h, n == 3 and curve.endswith("-"))
        width = right-left
        assert width > 0
        return acb(left+t*width, h), acb(width)
    assert curve in ("L"+str(n), "R"+str(n))
    if curve == "R3":
        lower = hstar()
    dh = upper-lower
    h = lower+dh*t
    r, rp = radius(n, h)
    sign = -1 if curve.startswith("L") else 1
    return acb(center+sign*r, h), dh*acb(sign*rp, 1)


def parameters(box, spec):
    if spec == IMPORT_SPEC:
        # Preserve not just the exact map but every interval expression and
        # derivative used for the 402 saved witnesses, including the slant.
        return pinned_lowcap.parameters(box)
    t, u, v = map(interval, box)
    slot, types = spec["slot"], spec["types"]
    boundary, dt = boundary_chart(types[slot], spec["curve"], t)
    interior, du, dv = disk_chart(types[1-slot], spec["piece"], u, v)
    pp, dp = [None, None], [None, None]
    pp[slot], pp[1-slot] = boundary, interior
    dp[slot], dp[1-slot] = [dt, acb(0), acb(0)], [acb(0), du, dv]
    return pp, dp


def propose_root(pp, p0, own):
    floating = [complex(float(z.real.mid()), float(z.imag.mid())) for z in p0]
    roots, derivative, error = old.base.block(
        [floating[0].real, floating[0].imag, floating[1].real, floating[1].imag], own)
    if error > 1e-9:
        return None
    centers = [old.encode(z) for z in roots]
    _, J0 = old.base.evalf(list(map(old.cp, centers)), *p0, 2+own)
    J = np.array([[complex(float(z.real.mid()), float(z.imag.mid())) for z in row]
                  for row in J0])
    inverse = np.linalg.inv(J)
    witness = dict(centers=centers,
                   inverse=[[old.encode(z) for z in row] for row in inverse],
                   affine=[[old.encode(z) for z in row] for row in derivative])
    *_, bb = old.components(witness, pp, p0, own)
    if any(not b.is_finite() for b in bb):
        return None
    for factor in (F(5, 4), F(3, 2), F(2)):
        witness["radii"] = [
            str(F(max(1, int(np.ceil(float(b.upper())*float(factor)*2**40))), 2**40))
            for b in bb]
        certificate = old.root_box(witness, pp, p0, own)
        if certificate is not None:
            return witness, certificate
    return None


def phase(s, a, b, eta, own):
    return old.phase(s, a, b, own) - (1+ar(eta)/2)*old.g(a) - (1+ar(own)/2)*old.g(b)


def marginals(s, a, b, eta, own):
    return [old.gp(s+a)-(1+ar(eta)/2)*old.gp(a)+2*PI*II*s,
            old.gp(s+b)-(1+ar(own)/2)*old.gp(b)]


def hessian(s, a, b, eta, own):
    g2 = helper.g2
    sigma = g2(s+a)+g2(s+b)-(2+own)*g2(s)
    assert abs(sigma) > 0
    omega = [g2(s+a)+2*PI*II, g2(s+b)]
    diagonal = [g2(s+a)-(1+ar(eta)/2)*g2(a),
                g2(s+b)-(1+ar(own)/2)*g2(b)]
    return [[(diagonal[i] if i == j else acb(0))-omega[i]*omega[j]/sigma
             for j in range(2)] for i in range(2)]


def flags(spec, side):
    return (spec["types"][side]-3, spec["own"])


def validate_trials(trials, spec):
    assert len(trials) == 2
    for side in (0, 1):
        assert len(trials[side]) == 2
        for i, flag in enumerate(flags(spec, side)):
            if flag:
                assert isinstance(trials[side][i], str)
                assert LO <= F(trials[side][i]) <= HI
            else:
                assert trials[side][i] is None


def propose_targets(p0, points, spec):
    """Floating numbers propose rational trials, never acceptance bounds."""
    trials = []
    for side in (0, 1):
        tau = flags(spec, side)
        a, s, b = p0[side], points[side], points[1-side]
        P0 = marginals(s, a, b, *tau)
        row = []
        for i, z in enumerate((a, b)):
            if not tau[i]:
                row.append(None)
                continue
            p, h = float(P0[i].real.mid()), float(z.imag.mid())
            r = np.exp(2*np.pi*h)
            goal = np.exp(-4*p)
            distance = lambda x: 1+r*r-2*r*np.cos(2*np.pi*x)
            if goal <= distance(float(LO)):
                x = LO
            elif goal >= distance(float(HI)):
                x = HI
            else:
                cosine = (1+r*r-goal)/(2*r)
                x = F(round(float(np.arccos(np.clip(cosine, -1, 1))/(2*np.pi))*10**12),
                      10**12)
                x = max(LO, min(HI, x))
            row.append(str(x))
        trials.append(row)
    validate_trials(trials, spec)
    return trials


def optimizer_interval(beta, trial):
    lower = (ar(trial)+min(arb(0), beta.lower())/ar(CURVATURE)).lower()
    upper = (ar(trial)+max(arb(0), beta.upper())/ar(CURVATURE)).upper()
    lower, upper = max(ar(LO), lower), min(ar(HI), upper)
    assert lower <= upper
    return lower.union(upper)


def envelope_count(spec):
    return sum(4*2**sum(t == 0 for t in flags(spec, side)) for side in (0, 1))


def check_cell(box, pp, p0, dp, certificate, spec, trials):
    validate_trials(trials, spec)
    roots, points, response = (certificate[k] for k in ("root", "point", "response"))
    halfwidth = [ar((hi-lo)/2) for lo, hi in box]
    maximum, count, positive = None, 0, None
    for side in (0, 1):
        tau = flags(spec, side)
        a, s, b = pp[side], roots[side], roots[1-side]
        a0, s0, b0 = p0[side], points[side], points[1-side]
        Z, Z0 = [a, b], [a0, b0]
        P = marginals(s, a, b, *tau)
        P0 = marginals(s0, a0, b0, *tau)
        H = hessian(s, a, b, *tau)
        phase0 = phase(s0, a0, b0, *tau).real
        Zder = [dp[side],
                [sum((response[1-side][j]*dp[j][axis] for j in range(2)), acb(0))
                 for axis in range(3)]]
        weighted = {}
        for i in (0, 1):
            if not tau[i]:
                continue
            q = F(trials[side][i])
            beta = (-old.gp(acb(ar(q), Z[i].imag)).real/2-P[i].real
                    +2*ar(KAPPA)*(ar(q)-Z[i].real))
            beta0 = (-old.gp(acb(ar(q), Z0[i].imag)).real/2-P0[i].real
                     +2*ar(KAPPA)*(ar(q)-Z0[i].real))
            weighted[i] = (optimizer_interval(beta, q), helper.target_gain(beta0, q))
        choices = [(F(trials[side][i]),) if tau[i] else (LO, HI) for i in (0, 1)]
        for target in itertools.product(*choices):
            X = [weighted[i][0] if tau[i] else ar(target[i]) for i in (0, 1)]
            delta = [X[i]-Z[i].real for i in (0, 1)]
            delta0 = [ar(target[i])-Z0[i].real for i in (0, 1)]
            HD = [sum((H[i][j]*delta[j] for j in (0, 1)), acb(0)) for i in (0, 1)]
            DU = [-HD[i].real-2*ar(KAPPA)*delta[i] for i in (0, 1)]
            base0 = -phase0-sum((P0[i].real*delta0[i] for i in (0, 1)), arb(0))
            base0 += ar(KAPPA)*sum((d*d for d in delta0), arb(0))
            rowpartial = [acb(0), acb(0)]
            gain = arb(0)
            for i in (0, 1):
                if tau[i]:
                    base0 -= old.g(acb(ar(target[i]), Z0[i].imag)).real/2
                    rowpartial[i] = -old.gp(acb(X[i], Z[i].imag))/2
                    gain += weighted[i][1]
            for v, w in itertools.product((0, 1), repeat=2):
                midpoint = base0-2*PI*v*a0.imag+2*PI*w*b0.imag
                Pc = [2*PI*II*v+rowpartial[0], -2*PI*II*w+rowpartial[1]]
                DH = [(P[i]-Pc[i]+HD[i]).imag for i in (0, 1)]
                derivatives = [sum((DU[i]*Zder[i][axis].real+DH[i]*Zder[i][axis].imag
                                    for i in (0, 1)), arb(0)) for axis in range(3)]
                error = sum((abs(derivatives[k])*halfwidth[k] for k in range(3)), arb(0))
                bound = midpoint+gain+error
                assert all(x.is_finite() for x in [midpoint, gain, error, bound]+derivatives)
                upper = bound.upper()
                maximum = upper if maximum is None else max(maximum, upper)
                count += 1
                if midpoint > 0 and positive is None:
                    positive = dict(side=side, flags=list(tau), carrier=[v, w],
                                    target=list(map(str, target)), lower=str(midpoint.lower()))
    assert count == envelope_count(spec)
    return maximum < 0, dict(max_upper=str(maximum), envelope_count=count), positive


def imported_targets(node):
    rows = node["rows"]
    assert len(rows) == 24
    targets = {F(r["trial_target"][0]) for r in rows if r["side"] == 1}
    assert len(targets) == 1
    q = targets.pop()
    result = [[None, None], [str(q), None]]
    validate_trials(result, IMPORT_SPEC)
    expected = {(side, x, z, v, w) for side in (0, 1)
                for x in ((LO, HI) if side == 0 else (q,))
                for z in (LO, HI) for v in (0, 1) for w in (0, 1)}
    actual = set()
    for row in rows:
        side = row["side"]
        assert row["eta"] == side and row["own_epsilon"] == 0
        x, z = map(F, row["trial_target"])
        key = (side, x, z, *row["carrier"])
        assert key not in actual
        actual.add(key)
    assert actual == expected
    return result


def validate_import(imported, replay):
    assert imported["status"] == "subset_complete" and replay["status"] == "passed"
    assert imported["own_epsilon"] == replay["own_epsilon"] == 0
    assert imported["external_types"] == replay["external_types"] == [3, 4]
    assert imported["boundary_slot"] == replay["boundary_slot"] == 0
    assert imported["accepted_cells_total"] == replay["accepted_cells_total"] == 402
    assert imported["visited_nodes_total"] == replay["visited_nodes_total"] == 803
    assert not imported["pending"] and not replay["pending"]
    assert imported["exact_accepted_parameter_volume"] == replay["exact_accepted_parameter_volume"] == "1"
    assert imported["positive_point"] is replay["positive_point"] is None
    assert replay["proposals"] == replay["refinements"] == 0
    assert len(imported["nodes"]) == len(replay["nodes"]) == 803
    pending, leaves, volume = [("", list(CUBE), 0)], 0, F(0)
    for a, b in zip(imported["nodes"], replay["nodes"]):
        assert pending
        address, box, depth = pending.pop()
        assert a["address"] == address and a["depth"] == depth
        assert a["box"] == [[str(x) for x in pair] for pair in box]
        assert (a["address"], a["box"], a["kind"]) == (b["address"], b["box"], b["kind"])
        if a["kind"] == "accepted":
            assert a["witness"] == b["witness"]
            assert imported_targets(a) == imported_targets(b)
            leaves += 1
            volume += F(1, 2**depth)
        else:
            assert a["kind"] == "split" and a["axis"] == b["axis"]
            pending.extend(split_children(address, box, depth, a["axis"]))
    assert not pending and leaves == 402 and volume == 1


def split_children(address, box, depth, axis):
    assert axis == depth % 3
    left, right = old.split(box, axis)
    result = [(address+"0", left, depth+1), (address+"1", right, depth+1)]
    if axis in (0, 1):
        result.reverse()  # LIFO: low boundary/height; high width.
    return result


def encode_frontier(frontier):
    return [[address, [[str(x) for x in pair] for pair in box], depth]
            for address, box, depth in frontier]


def decode_frontier(rows):
    return [(address, [tuple(map(F, pair)) for pair in box], depth)
            for address, box, depth in rows]


def reconstruct(tree, spec):
    frontier = [("", list(CUBE), 0)]
    leaves, volume, maxdepth = 0, F(0), 0
    for node in tree:
        assert frontier
        address, box, depth = frontier[-1]
        maxdepth = max(maxdepth, depth)
        assert depth <= MAX_DEPTH
        assert len(node) == 2
        if node[0] == "S":
            axis = node[1]
            assert type(axis) is int and axis == depth % 3
            assert depth < MAX_DEPTH
            frontier.pop()
            frontier.extend(split_children(address, box, depth, axis))
        else:
            assert node[0] == "L" and isinstance(node[1], dict)
            data = node[1]
            validate_trials(data["targets"], spec)
            assert data["envelope_count"] == envelope_count(spec)
            assert arb(data["max_upper"]) < 0
            assert isinstance(data["witness"], dict)
            frontier.pop()
            leaves += 1
            volume += F(1, 2**depth)
    for address, box, depth in frontier:
        assert len(address) == depth
        assert depth <= MAX_DEPTH
        assert all(F(0) <= lo < hi <= F(1) for lo, hi in box)
    pending_volume = sum((F(1, 2**depth) for _, _, depth in frontier), F(0))
    assert volume+pending_volume == 1
    return frontier, leaves, volume, maxdepth


def initial_domains():
    domains = []
    for index, spec in enumerate(SPECS):
        domain = dict(spec=spec)
        if index == IMPORT_INDEX:
            domain.update(kind="imported", status="complete", leaves=402, tree_nodes=803,
                          resolved_volume="1", record=IMPORTED, record_sha256=PINS[IMPORTED],
                          replay=IMPORTED_REPLAY, replay_sha256=PINS[IMPORTED_REPLAY])
        else:
            domain.update(kind="computed", status="incomplete", tree=[],
                          frontier=encode_frontier([("", list(CUBE), 0)]),
                          leaves=0, tree_nodes=0, resolved_volume="0", maximum_depth=0)
        domains.append(domain)
    return domains


def refresh(domain):
    assert domain["kind"] == "computed"
    pending, leaves, volume, depth = reconstruct(domain["tree"], domain["spec"])
    domain.update(frontier=encode_frontier(pending), leaves=leaves,
                  tree_nodes=len(domain["tree"]), resolved_volume=str(volume),
                  maximum_depth=depth, status="complete" if not pending else "incomplete")


def validate_domains(domains, complete=False):
    assert len(domains) == len(SPECS) == 72
    for index, (domain, spec) in enumerate(zip(domains, SPECS)):
        assert domain["spec"] == spec
        if index == IMPORT_INDEX:
            assert domain == initial_domains()[IMPORT_INDEX]
        else:
            assert domain["kind"] == "computed"
            pending, leaves, volume, depth = reconstruct(domain["tree"], spec)
            assert encode_frontier(pending) == domain["frontier"]
            assert leaves == domain["leaves"] and str(volume) == domain["resolved_volume"]
            assert len(domain["tree"]) == domain["tree_nodes"]
            assert depth == domain["maximum_depth"]
            assert domain["status"] == ("complete" if not pending else "incomplete")
        if complete:
            assert domain["status"] == "complete"


def replay_all(domains, imported):
    """Every chart, including imported cells; only saved witnesses/trials."""
    global propose_root, propose_targets
    saved_root, saved_targets, saved_block = propose_root, propose_targets, old.base.block

    def forbidden(*_, **__):
        raise RuntimeError("saved replay cannot propose roots or target trials")

    propose_root = propose_targets = old.base.block = forbidden
    summaries = []
    try:
        for index, domain in enumerate(domains):
            spec = domain["spec"]
            maximum, leaves, envelopes = None, 0, 0
            if index == IMPORT_INDEX:
                iterable = (([tuple(map(F, pair)) for pair in node["box"]],
                             node["witness"], imported_targets(node))
                            for node in imported["nodes"] if node["kind"] == "accepted")
                # Materialize only the small imported accepted collection.
                cells = [(list(box), witness, trials) for box, witness, trials in iterable]
            else:
                pending = [("", list(CUBE), 0)]
                cells = []
                # The saved split axes are only used to reconstruct exact boxes.
                # Nothing is refined during replay.
                for node in domain["tree"]:
                    address, box, depth = pending.pop()
                    if node[0] == "S":
                        pending.extend(split_children(address, box, depth, node[1]))
                    else:
                        assert node[0] == "L"
                        cells.append((box, node[1]["witness"], node[1]["targets"]))
                assert not pending
            for box, witness, trials in cells:
                pp, dp = parameters(box, spec)
                p0, _ = parameters([((lo+hi)/2,)*2 for lo, hi in box], spec)
                certificate = old.root_box(witness, pp, p0, spec["own"])
                assert certificate is not None, ("saved root", index, leaves)
                passed, bound, positive = check_cell(box, pp, p0, dp, certificate, spec, trials)
                assert passed and positive is None, ("saved deficit", index, leaves, bound)
                value = arb(bound["max_upper"]).upper()
                maximum = value if maximum is None else max(maximum, value)
                envelopes += bound["envelope_count"]
                leaves += 1
            assert leaves == domain["leaves"]
            assert envelopes == leaves*envelope_count(spec)
            summaries.append(dict(index=index, spec=spec, leaves=leaves,
                                  envelope_bounds=envelopes, maximum_upper=str(maximum)))
            print("REPLAY", index, spec, "leaves", leaves, "upper", maximum, flush=True)
    finally:
        propose_root, propose_targets, old.base.block = saved_root, saved_targets, saved_block
    return summaries


def author_attempt(domains, save, counters):
    """A box remains on the frontier until an atomic accepted/split commit."""
    reason, positive = "not started", None
    handlers = {}

    def stop(signum, *_):
        raise StopAttempt(signum)

    for signum in SIGNALS:
        handlers[signum] = signal.signal(signum, stop)
    signal.setitimer(signal.ITIMER_REAL, max(.000001, MAX_SECONDS-(time.monotonic()-PROGRAM_START)))
    last_checkpoint = time.monotonic()
    try:
        save("partial", "attempt started", None)
        for index, domain in enumerate(domains):
            if domain["status"] == "complete":
                continue
            frontier = decode_frontier(domain["frontier"])
            spec = domain["spec"]
            while frontier:
                if counters["visited"] >= MAX_NODES:
                    reason = "200000 additional-node budget"
                    return "partial", reason, positive
                if time.monotonic()-PROGRAM_START >= MAX_SECONDS:
                    raise StopAttempt(signal.SIGALRM)
                address, box, depth = frontier[-1]
                if depth >= MAX_DEPTH:
                    reason = "depth guard; unresolved box retained"
                    return "partial", reason, positive
                counters["visited"] += 1
                pp, dp = parameters(box, spec)
                p0, _ = parameters([((lo+hi)/2,)*2 for lo, hi in box], spec)
                proposed, accepted = None, None
                try:
                    proposed = propose_root(pp, p0, spec["own"])
                    if proposed is not None:
                        witness, certificate = proposed
                        trials = propose_targets(p0, certificate["point"], spec)
                        ok, bound, point = check_cell(box, pp, p0, dp, certificate, spec, trials)
                        if point is not None:
                            positive = dict(
                                chart_index=index, spec=spec, address=address, depth=depth,
                                box=[[str(x) for x in pair] for pair in box],
                                witness=witness, targets=trials, trial=point,
                                midpoint_parameters=list(map(str, p0)),
                                midpoint_roots=list(map(str, certificate["point"])),
                                scope="Sufficient typed reference family only; actual-word realization not asserted.")
                            reason = "certified positive fixed trial; no further cells attempted"
                            return "positive_auxiliary_point", reason, positive
                        if ok:
                            accepted = dict(witness=witness, targets=trials, **bound)
                except (AssertionError, ValueError, ZeroDivisionError, OverflowError,
                        np.linalg.LinAlgError):
                    counters["uncertain"] += 1
                with atomic_section():
                    assert frontier[-1] == (address, box, depth)
                    frontier.pop()
                    if accepted is not None:
                        domain["tree"].append(["L", accepted])
                        counters["accepted"] += 1
                    else:
                        axis = depth % 3
                        domain["tree"].append(["S", axis])
                        frontier.extend(split_children(address, box, depth, axis))
                        counters["root_failures" if proposed is None else "deficit_failures"] += 1
                    domain["frontier"] = encode_frontier(frontier)
                if time.monotonic()-last_checkpoint >= CHECKPOINT_SECONDS:
                    refresh(domain)
                    save("partial", "periodic checkpoint", None)
                    last_checkpoint = time.monotonic()
            refresh(domain)
            assert domain["status"] == "complete"
            save("partial", "completed chart "+str(index), None)
            last_checkpoint = time.monotonic()
            print("AUTHOR", index, spec, "leaves", domain["leaves"], flush=True)
        reason = "all72 charts complete"
        return "passed", reason, None
    except StopAttempt as exc:
        reason = "working deadline" if exc.signum == signal.SIGALRM else "external stop signal"
        return "partial", reason, positive
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        for signum, handler in handlers.items():
            signal.signal(signum, handler)
        # The active box was never removed before a complete commit.
        for domain in domains:
            if domain["kind"] == "computed":
                refresh(domain)


def tree_digest(tree):
    digest = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"))
    for chunk in encoder.iterencode(tree):
        digest.update(chunk.encode())
    return digest.hexdigest()


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--resume", type=Path, help="immutable partial author checkpoint")
    modes.add_argument("--input", type=Path, help="complete author record for saved replay")
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-typed-last-row-support.json")
    args = parser.parse_args()
    assert args.precision >= 320 if args.input else args.precision == 256
    input_path = args.input or args.resume
    assert not args.output.exists(), "each attempt/replay uses a distinct new output"
    if input_path:
        assert args.output.resolve() != input_path.resolve()
    ctx.prec = args.precision
    PI, II = arb.pi(), acb(0, 1)
    helper.PI = old.PI = old.base.PI = PI
    helper.II = old.II = old.base.I = II
    pinned_lowcap.PI, pinned_lowcap.II = PI, II
    assert helper.KAPPA == KAPPA and helper.CURVATURE == CURVATURE
    assert (helper.LO, helper.HI) == (LO, HI)
    assert F(9, 140)*F(157, 50)-2*KAPPA > CURVATURE
    assert F(83, 1000)**2-F(78, 1000)**2 == F(805, 1000000) > F(1, 40)**2
    assert F(3, 50)**2-F(56, 1000)**2 == F(29, 62500) > F(1, 50)**2
    assert F(78, 1000)**2 < 9*F(805, 1000000)
    assert F(56, 1000)**2 < 9*F(29, 62500)
    assert F(129, 500)-3*F(9, 125)+F(1, 40) == F(67, 1000)
    for own, expected in ((0, (32, 24, 16)), (1, (16, 12, 8))):
        for types, count in zip(([3, 3], [3, 4], [4, 4]), expected):
            assert envelope_count(dict(own=own, types=types)) == count
    deps = {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in deps or deps[name] == digest, name
        deps[name] = digest
        return digest

    for name, digest in PINS.items():
        bind(name, digest)
    imported, imported_replay = load(ROOT/IMPORTED), load(ROOT/IMPORTED_REPLAY)
    assert imported_replay["input_sha256"] == PINS[IMPORTED]
    for record in (imported, imported_replay):
        for name, digest in record["dependencies_sha256"].items():
            bind(name, digest)
        bind("repro/diagnostics/2026-11-05-typed-last-row-low-cap/continue_subset.py",
             record["script_sha256"])
        bind("experiments/pilot_mixed_typed_last_row_low_cap.py",
             record["original_driver_sha256"])
        bind("notes/research_mixed_typed_last_row_support_design.md", record["proof_sha256"])
    validate_import(imported, imported_replay)
    for name in (
        "notes/research_mixed_typed_last_row_envelopes.md",
        "notes/research_mixed_actual_last_row_reference_domains.md",
        "notes/research_mixed_horizontal_tail_reference_boundary.md",
        "notes/research_mixed_horizontal_zero_mode_support.md",
        "notes/research_mixed_horizontal_revived_endpoint.md",
        "notes/research_mixed_last_row_own_root_normal_form.md",
        "experiments/pilot_mixed_attached_last_row_face.py",
    ):
        bind(name)
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    assert args.output.resolve() not in {(ROOT/name).resolve() for name in deps}
    assert args.output.resolve() not in {PROOF.resolve(), Path(__file__).resolve()}
    source, input_hash = None, None
    if input_path:
        input_hash = sha(input_path)
        source = load(input_path)
        assert source["schema"] == "typed-last-row-height-charts-v1"
        assert source["mode"] == "author"
        assert source["proof_sha256"] == proof_hash and source["script_sha256"] == script_hash
        assert source["dependencies_sha256"] == deps
        assert source["chart_count"] == 72 and source["imported_chart_index"] == IMPORT_INDEX
        assert source["max_nodes_per_attempt"] == MAX_NODES
        assert source["max_seconds_per_attempt"] == MAX_SECONDS
        assert source["maximum_depth_guard"] == MAX_DEPTH
        assert source["precision_bits"] == 256
        assert source["positive_point"] is None
        validate_domains(source["domains"], complete=bool(args.input))
        for history in source["attempt_history"]:
            assert 0 <= history["visited"] <= MAX_NODES
        if args.input:
            assert source["status"] == "passed"
        else:
            assert source["status"] == "partial"
    domains = source["domains"] if source else initial_domains()
    validate_domains(domains, complete=bool(args.input))
    common = dict(
        schema="typed-last-row-height-charts-v1", chart_count=72,
        imported_chart_index=IMPORT_INDEX, proof_sha256=proof_hash,
        script_sha256=script_hash, dependencies_sha256=deps,
        precision_bits=args.precision, max_nodes_per_attempt=MAX_NODES,
        max_seconds_per_attempt=MAX_SECONDS, maximum_depth_guard=MAX_DEPTH,
        target_interval=[str(LO), str(HI)], target_curvature=str(CURVATURE),
        kappa=str(KAPPA), requested_deficit_upper="0",
        source_scope="Original coupled references on K3/K4, both own types and orientations, "
                     "all revived carriers and all horizontal targets. No masks or independent legs.",
        conclusion_scope="A complete record concerns only the typed last-row supporting-plane "
                         "comparison, not a complete open finite-source noncancellation theorem.")

    def frozen_inputs():
        assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
        assert all(sha(ROOT/name) == digest for name, digest in deps.items())
        if input_path:
            assert sha(input_path) == input_hash

    if args.input:
        summaries = replay_all(domains, imported)
        frozen_inputs()
        validate_domains(domains, complete=True)
        result = dict(
            common, mode="saved_replay", status="passed", stop_reason="all72 saved charts replayed",
            input_sha256=input_hash, domains=domains, replay_summaries=summaries,
            replayed_cells=sum(row["leaves"] for row in summaries),
            replayed_envelope_bounds=sum(row["envelope_bounds"] for row in summaries),
            proposals=0, refinements=0, positive_point=None,
            elapsed_seconds=time.monotonic()-PROGRAM_START)
        publish(args.output, result)
        print("REPLAY PASS", result["replayed_cells"], "cells",
              result["replayed_envelope_bounds"], "bounds", len(deps), "bindings", flush=True)
        return 0

    # Hash each immutable accepted/split prefix before resuming. Every mutation
    # below is an append to a previously pending box; a final check binds that.
    prefixes = [(len(d.get("tree", [])), tree_digest(d.get("tree", []))) for d in domains]
    history = list(source["attempt_history"]) if source else []
    counters = dict(visited=0, accepted=0, root_failures=0, deficit_failures=0, uncertain=0)
    attempt = dict(resume_input_sha256=input_hash, prior_tree_nodes=sum(d["tree_nodes"] for d in domains))
    source_note = str(input_path) if input_path else None

    def prefix_check():
        for domain, (length, digest) in zip(domains, prefixes):
            assert tree_digest(domain.get("tree", [])[:length]) == digest

    def snapshot(status, reason, positive):
        for domain in domains:
            if domain["kind"] == "computed":
                refresh(domain)
        validate_domains(domains, complete=status == "passed")
        frozen_inputs()
        prefix_check()
        current = dict(
            attempt, **counters, stop_reason=reason,
            elapsed_seconds=time.monotonic()-PROGRAM_START,
            complete_charts=sum(d["status"] == "complete" for d in domains))
        result = dict(
            common, mode="author", status=status, stop_reason=reason,
            resume_input_path=source_note, resume_input_sha256=input_hash,
            domains=domains, positive_point=positive, attempt_history=history+[current],
            complete_charts=current["complete_charts"],
            accepted_cells_total=sum(d["leaves"] for d in domains),
            tree_nodes_total=sum(d["tree_nodes"] for d in domains),
            pending_boxes_total=sum(len(d.get("frontier", [])) for d in domains),
            elapsed_seconds=current["elapsed_seconds"])
        publish(args.output, result)
        return result

    try:
        status, reason, positive = author_attempt(domains, snapshot, counters)
    except Exception as exc:
        # No failed/in-flight cell was committed. Preserve exact pending work,
        # then report the unexpected error without claiming a successful run.
        snapshot("partial", "unexpected error: "+type(exc).__name__, None)
        raise
    result = snapshot(status, reason, positive)
    assert counters["visited"] <= MAX_NODES
    print(status, "complete charts", result["complete_charts"], "/72",
          "new visits", counters["visited"], "accepted", result["accepted_cells_total"],
          "pending", result["pending_boxes_total"], "bindings", len(deps),
          "seconds", round(result["elapsed_seconds"], 3), "output", args.output, flush=True)
    return 0 if status == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())



