#!/usr/bin/env python3
"""Four full-plateau first-cap currents, using saved endpoint root witnesses.

Author mode may subdivide the reference rectangles and propose rational
free-target trials. It never proposes a complex root. Saved replay validates
the same partition and trials without proposals or subdivision.
"""
import argparse
import cmath
from contextlib import contextmanager
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import time

from flint import acb, acb_mat, arb, ctx
import certify_mixed_open_word_critical_localization as old
import certify_mixed_endpoint_packet_extension as primitive

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_first_cap_plateau_certificate.md"
ROOT_AUTHOR = "repro/results/research-mixed-open-word-critical-localization.json"
ROOT_REPLAY = "repro/results/research-mixed-open-word-critical-localization-replay.json"
KAPPA, MU, GAP = F(1, 2500000), F(3, 200), F(1, 20000)
IY, IE = (F(".22"), F(".45")), (F(".27"), F(".49"))
FACES = [("cut", IE[0], F(0)), ("cut", IE[1], F(0)),
         ("alias", None, F("-.055")), ("alias", None, F(".04"))]
ar, cp = old.ar, old.cp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encoded_box(box):
    return [[str(lo), str(hi)] for lo, hi in box]


def decode_box(box):
    return [tuple(map(F, side)) for side in box]


def center_box(box):
    return [((lo+hi)/2, (lo+hi)/2) for lo, hi in box]


def original_root_proposals_forbidden(*args, **kwargs):
    raise AssertionError("complex-root proposals are forbidden")


def target_proposals_forbidden(*args, **kwargs):
    raise AssertionError("target proposals are forbidden during saved replay")


def g(z):
    return primitive.J(z)+II*PI*z*(1-z)/2


def gp(z):
    return old.jp(z)+II*PI*(ar("1/2")-z)


def gpp(z):
    return PI*old.cot(z)-II*PI


def phase_with_u(e, z, u, own):
    return (primitive.phase(e, u)+primitive.J(e+z)-primitive.J(z)
            -II*PI*e*z-own*g(e)-ar(F(own, 2))*g(z))


def phase(e, z, own):
    u, disc = primitive.critical(e)
    assert disc.real > 1 and u.is_finite()
    return phase_with_u(e, z, u, own)


def partials(e, z, own):
    u, disc = primitive.critical(e)
    assert disc.real > 1 and u.is_finite()
    pe = primitive.partials(e, u)[0]+old.jp(e+z)-II*PI*z-own*gp(e)
    pz = old.jp(e+z)-old.jp(z)-II*PI*e-ar(F(own, 2))*gp(z)
    return pe, pz


def reference_marginal(root, own):
    e, z, _ = root
    return old.jp(e+z)-old.jp(z)-II*PI*e-ar(F(own, 2))*gp(z)


def root_context(cell):
    box, neighbor, w = cell["box"], cell["neighbor"], cell["witness"]
    a = old.parameter(box, neighbor)
    own = cell["own"]
    assert old.test(w, a, own) is not None, "inherited original-root failure"
    z0 = list(map(cp, w["centers"]))
    Y = acb_mat([[cp(v) for v in row] for row in w["inverse"]])
    radius = ar(w["radius"])
    z = [v+acb(arb(0, radius), arb(0, radius)) for v in z0]
    E = old.ident(3)-Y*old.jacobian(z, a, own)
    q = max(sum((abs(E[i, j]) for j in range(3)), arb(0)).upper()
            for i in range(3))
    assert q < 1
    # Exact extraction bounds on the complete old witness squares.
    bounds = ([('.376', '.438', '-.019', '.037'),
               ('.278', '.391', '-.072', '.021'),
               ('.218', '.242', '.049', '.077')] if own == 0 else
              [('.333', '.363', '-.051', '-.019'),
               ('.246', '.350', '-.108', '-.020'),
               ('.217', '.234', '.027', '.045')])
    for value, (xl, xh, yl, yh) in zip(z, bounds):
        assert ar(xl) < value.real < ar(xh)
        assert ar(yl) < value.imag < ar(yh)
    return dict(z0=z0, Y=Y, radius=radius, z=z, q=q, own=own)


def intersection(z, w):
    return acb(z.real.intersection(w.real), z.imag.intersection(w.imag))


def enclosing_root(context, parameter, steps):
    """Contract an already proved enclosure; never propose a new root.

    The original self-map supplies existence. Each Taylor image below
    contains that root for every parameter in the same parameter box.
    Intersection can therefore tighten but cannot change the root branch.
    """
    Y, z0, q = context["Y"], context["z0"], context["q"]
    own = context["own"]
    residual = Y*old.equation(z0, parameter, own)
    b = max(abs(residual[i, 0]).upper() for i in range(3))
    radius = min(context["radius"], (b/(1-q)).upper())
    z = [v+acb(arb(0, radius), arb(0, radius)) for v in z0]
    for _ in range(steps):
        mid = [acb(v.real.mid(), v.imag.mid()) for v in z]
        E = old.ident(3)-Y*old.jacobian(z, parameter, own)
        image = (acb_mat([[v] for v in mid])-Y*old.equation(mid, parameter, own)
                 +E*acb_mat([[z[i]-mid[i]] for i in range(3)]))
        z = [intersection(z[i], image[i, 0]) for i in range(3)]
        assert all(v.is_finite() for v in z)
    return z


def responses(z, a, Y, own):
    E = old.ident(3)-Y*old.jacobian(z, a, own)
    q = max(sum((abs(E[i, j]) for j in range(3)), arb(0)).upper()
            for i in range(3))
    assert q < 1
    forcing = acb_mat([[0], [PI*old.cot(z[1]+a)+PI*II], [0]])
    term = -(Y*forcing)
    result = acb_mat(term)
    norm = max(abs(term[i, 0]).upper() for i in range(3))
    for _ in range(7):
        term = E*term
        result += term
    tail = (norm*q**8/(1-q)).upper()
    return [result[i, 0]+acb(arb(0, tail), arb(0, tail)) for i in range(3)]


def target_box(face):
    assert face in FACES
    return [IY] if face[0] == 'cut' else [IY, IE]


def family_metadata():
    return [dict(kind=kind, private_real=None if value is None else str(value),
                 private_height=str(height), penalty_over_pi=str(2*abs(height)))
            for kind, value, height in FACES]


def validate_trial(targets, face):
    assert isinstance(targets, list)
    trial = list(map(F, targets))
    bounds = target_box(face)
    assert len(trial) == len(bounds)
    assert all(lo <= t <= hi for t, (lo, hi) in zip(trial, bounds))
    # Canonical rational strings also make the replay equality literal.
    assert targets == [str(v) for v in trial]
    return trial


def target_arguments(root, face, trial):
    kind, real, height = face
    e = acb(ar(real if kind == 'cut' else trial[1]), ar(height))
    z = acb(ar(trial[0]), root[1].imag)
    return e, z


def penalty(face):
    return 2*PI*ar(abs(face[2]))


def one_sided_gain(slope, length):
    assert length >= 0
    if length == 0 or slope <= 0:
        return arb(0)
    beta = max(slope.upper(), arb(0))
    if beta >= ar(MU*length):
        return beta*ar(length)-ar(MU*length*length)/2
    # Also safe if the comparison at the clipped transition is uncertain.
    return beta*beta/(2*ar(MU))


def gain(gradient, trial, interval):
    lo, hi = interval
    return max(arb(0),
               one_sided_gain(gradient.upper(), hi-trial).upper(),
               one_sided_gain((-gradient).upper(), trial-lo).upper())


def propose_targets(root0, own, face):
    """Only a floating real-target trial; never a complex-root solve."""
    def cm(z):
        return complex(float(z.real.mid()), float(z.imag.mid()))
    er, zr = cm(root0[0]), cm(root0[1])
    pi = math.pi
    def jp(z):
        return cmath.log(2*cmath.sin(pi*z))
    def gprime(z):
        return jp(z)+1j*pi*(.5-z)
    pref = jp(er+zr)-jp(zr)-1j*pi*er-own*gprime(zr)/2
    bounds = target_box(face)
    x = [(float(lo)+float(hi))/2 for lo, hi in bounds]
    def gradient(values):
        z = complex(values[0], zr.imag)
        e = complex(float(face[1]) if face[0] == 'cut' else values[1], float(face[2]))
        pz = jp(e+z)-jp(z)-1j*pi*e-own*gprime(z)/2
        result = [(pz-pref).real+2*float(KAPPA)*(values[0]-zr.real)]
        if face[0] == 'alias':
            uc = cmath.atan((1j+cmath.sqrt(1-2*cmath.exp(2j*pi*e)))/2)/pi
            pe = -jp(e-uc)+1j*pi*uc+jp(e+z)-1j*pi*z-own*gprime(e)
            result.append(pe.real)
        return result
    for _ in range(16):
        previous = list(x)
        for j, (lo, hi) in enumerate(bounds):
            left, right = float(lo), float(hi)
            x[j] = left
            gl = gradient(x)[j]
            x[j] = right
            gr = gradient(x)[j]
            if gl <= 0:
                x[j] = left
            elif gr >= 0:
                x[j] = right
            else:
                for _ in range(36):
                    x[j] = (left+right)/2
                    if gradient(x)[j] > 0:
                        left = x[j]
                    else:
                        right = x[j]
                x[j] = (left+right)/2
        if max(abs(a-b) for a, b in zip(x, previous)) < 1e-11:
            break
    return [min(hi, max(lo, F(format(value, '.12f'))))
            for value, (lo, hi) in zip(x, bounds)]


def check_face(cell, context, box, face, saved_trial=None):
    neighbor, own = cell['neighbor'], cell['own']
    b = old.parameter(box, neighbor)
    b0 = old.parameter(center_box(box), neighbor)
    root = enclosing_root(context, b, 5)
    point = enclosing_root(context, b0, 12)
    trial = (propose_targets(point, own, face) if saved_trial is None
             else validate_trial(saved_trial, face))
    bounds = target_box(face)
    assert len(trial) == len(bounds)
    assert all(lo <= t <= hi for t, (lo, hi) in zip(trial, bounds))
    e0, z0 = target_arguments(point, face, trial)
    p0 = reference_marginal(point, own)
    d0 = ar(trial[0])-point[1].real
    value = (phase(e0, z0, own).real
             -phase_with_u(point[0], point[1], point[2], own).real
             -p0.real*d0+ar(KAPPA)*d0*d0-penalty(face))

    e, z = target_arguments(root, face, trial)
    pe, pz = partials(e, z, own)
    pref = reference_marginal(root, own)
    response = responses(root, b, context['Y'], own)
    ep, tp = response[0], response[1]
    pb = (PI*old.cot(root[0]+root[1])*(ep+tp)
          -PI*old.cot(root[1])*tp-II*PI*ep
          -ar(F(own, 2))*gpp(root[1])*tp)
    d = ar(trial[0])-root[1].real
    # Differentiate in the original external input b, not outgoing t(b).
    # This avoids division by t'(b), and the critical reference forces cancel.
    dA = (pref-pz).imag*tp.imag-d*pb.real-2*ar(KAPPA)*d*tp.real
    dH = (pref-pz).imag*tp.real+d*pb.imag+2*ar(KAPPA)*d*tp.imag
    radii = [ar(old.DISKS[neighbor][2]*(hi-lo)/2) for lo, hi in box]
    contributions = [abs(dA)*radii[0], abs(dH)*radii[1]]
    mean = sum(contributions, arb(0))
    gradients = [pz.real-pref.real+2*ar(KAPPA)*d]
    if face[0] == 'alias':
        gradients.append(pe.real)
    gains = [gain(v, t, interval) for v, t, interval in zip(gradients, trial, bounds)]
    upper = value+mean+sum(gains, arb(0))
    assert upper.is_finite(), 'nonfinite validated source enclosure'
    summary = dict(point=str(value), variation=str(mean),
                   gains=[str(v) for v in gains], upper=str(upper.upper()))
    split_axis = max(range(2), key=lambda j: float(contributions[j].upper()))
    return upper < -ar(GAP), [str(v) for v in trial], summary, split_axis


def original_cells(record):
    assert [(d["epsilon"], d["neighbor_epsilon"]) for d in record["domains"]] == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    cells = []
    total_nodes = total_leaves = total_excluded = 0
    for domain_index, domain in enumerate(record["domains"]):
        pending = [([(F(-1), F(1)), (F(-1), F(1))], 0)]
        leaves = excluded = 0
        for node_index, node in enumerate(domain["tree"]):
            assert pending
            box, depth = pending.pop()
            total_nodes += 1
            if node[0] == "S":
                assert len(node) == 2 and node[1] == depth % 2
                left, right = old.split(box, node[1])
                pending.extend([(left, depth+1), (right, depth+1)])
            elif node[0] == "X":
                assert len(node) == 1 and old.excluded(box)
                excluded += 1
            else:
                assert node[0] == "L" and len(node) == 2 and not old.excluded(box)
                leaves += 1
                cells.append(dict(domain=domain_index, node=node_index,
                                  own=domain["epsilon"], neighbor=domain["neighbor_epsilon"],
                                  box=box, witness=node[1]))
        assert not pending
        assert (leaves, excluded) == (domain["leaves"], domain["excluded"])
        total_leaves += leaves
        total_excluded += excluded
    assert (total_nodes, total_leaves, total_excluded) == (10978, 5258, 233)
    assert [sum(c["domain"] == n for c in cells) for n in range(4)] == [1645, 1702, 1002, 909]
    return cells


def frontier(box, tree, face, replay_leaf=None):
    pending = [(box, 0)]
    leaves = excluded = 0
    for node in tree:
        assert pending
        cell, depth = pending.pop()
        if node[0] == "S":
            assert len(node) == 2 and node[1] in (0, 1)
            left, right = old.split(cell, node[1])
            pending.extend([(left, depth+1), (right, depth+1)])
        elif node[0] == "X":
            assert len(node) == 1 and old.excluded(cell)
            excluded += 1
        else:
            assert node[0] == "L" and len(node) == 2 and not old.excluded(cell)
            validate_trial(node[1], face)
            if replay_leaf is not None:
                replay_leaf(cell, node[1])
            leaves += 1
    return pending, leaves, excluded


def serialize_pending(pending):
    return [[encoded_box(box), depth] for box, depth in pending]


class BudgetStop(Exception):
    pass


def alarm_handler(signum, frame):
    raise BudgetStop("author time cap")


@contextmanager
def atomic_state():
    previous = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGALRM})
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, previous)


def write_atomic(path, result):
    temporary = path.with_name(path.name+".tmp-"+str(os.getpid()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with atomic_state():
        temporary.write_text(json.dumps(result, separators=(",", ":"))+"\n")
        os.replace(temporary, path)


def main():
    global PI, II, propose_targets
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
    assert not args.output.exists(), "output must be a new immutable record path"
    assert all(args.output.resolve() != p.resolve() for p in (args.input, args.resume) if p)
    assert 0 < args.max_nodes <= 600000 and 0 < args.max_seconds <= 600
    assert 0 <= args.max_depth <= 45
    ctx.prec = args.precision
    PI, II = arb.pi(), acb(0, 1)
    primitive.PI, primitive.II = PI, II
    old.propose = original_root_proposals_forbidden
    if args.input:
        propose_targets = target_proposals_forbidden
    assert ar("3.14")/200-2*ar(KAPPA) > ar(MU)
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    dependencies, records = {}, {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    def inherit(name):
        bind(name)
        if name in records:
            return records[name]
        record = json.loads((ROOT/name).read_text())
        records[name] = record
        for key in ("dependencies_sha256", "dependencies"):
            for path, digest in record.get(key, {}).items():
                bind(path, digest)
                if path.startswith("repro/results/") and path.endswith(".json"):
                    inherit(path)
        return record

    roots, replay = inherit(ROOT_AUTHOR), inherit(ROOT_REPLAY)
    assert roots["status"] == replay["status"] == "passed"
    assert replay["input_sha256"] == dependencies[ROOT_AUTHOR]
    assert roots["domains"] == replay["domains"]
    for record in (roots, replay):
        bind("notes/research_mixed_open_word_critical_localization.md", record["proof_sha256"])
        bind("experiments/certify_mixed_open_word_critical_localization.py", record["script_sha256"])
    pairs = [
        ('mixed-complete-first-cap-packet', 'mixed_complete_first_cap_packet',
         'check_mixed_complete_first_cap_packet'),
        ('mixed-endpoint-cap-rectangle', 'mixed_endpoint_cap_rectangle',
         'certify_mixed_endpoint_cap_rectangle'),
        ('mixed-cap-real-cut-gaps', 'mixed_cap_real_cut_gaps',
         'check_mixed_cap_real_cut_gaps'),
        ('mixed-outer-cap-real-tails', 'mixed_outer_cap_real_tails',
         'check_mixed_outer_cap_real_tails'),
    ]
    for stem, proof, script in pairs:
        author_name = f'repro/results/research-{stem}.json'
        replay_name = f'repro/results/research-{stem}-replay.json'
        previous, checked = inherit(author_name), inherit(replay_name)
        assert previous['status'] == checked['status'] == 'passed'
        assert checked['input_sha256'] == dependencies[author_name]
        for record in (previous, checked):
            bind(f'notes/research_{proof}.md', record['proof_sha256'])
            bind(f'experiments/{script}.py', record['script_sha256'])
    for name in [
        'notes/research_mixed_first_cap_plateau_phase.md',
        'notes/research_mixed_open_word_hessian.md',
        'notes/research_terminal_supporting_plane.md',
        'notes/research_mixed_cap_outer_contour_reduction.md',
        'notes/research_mixed_open_word_endpoint_rectangles.md',
        'experiments/check_mixed_open_word_endpoint_rectangles.py',
        'experiments/certify_mixed_endpoint_packet_extension.py',
    ]:
        bind(name)
    extraction = inherit('repro/results/research-mixed-open-word-endpoint-rectangles.json')
    assert extraction['status'] == 'passed'
    assert extraction['proof_sha256'] == dependencies[
        'notes/research_mixed_open_word_endpoint_rectangles.md']
    assert extraction['script_sha256'] == dependencies[
        'experiments/check_mixed_open_word_endpoint_rectangles.py']
    cells = original_cells(roots)
    jobs = [(index, face) for index in range(len(cells)) for face in range(len(FACES))]
    assert len(cells) == 5258 and len(jobs) == 21032
    source_path = args.input or args.resume
    source_hash = sha(source_path) if source_path else None
    saved = json.loads(source_path.read_text()) if source_path else None
    if saved:
        assert saved["proof_sha256"] == proof_hash and saved["script_sha256"] == script_hash
        assert saved["dependencies_sha256"] == dependencies
        assert saved["gap"] == str(GAP) and saved["target_curvature"] == str(MU)
        assert saved["job_count"] == len(jobs)
        assert saved["families"] == family_metadata()
        assert saved["original_endpoint_cells"] == 5258
        assert saved["face_families_per_cell"] == 4
        assert saved["own_types"] == [0, 1] and saved["one_vertex_included"] is False
        assert saved["status"] == ("passed" if args.input else "incomplete")
    completed = saved["completed"] if saved else []
    active = saved["active"] if saved else None
    assert len(completed) <= len(jobs)
    for ji, tree in enumerate(completed):
        ci, face_index = jobs[ji]
        pending, _, _ = frontier(cells[ci]["box"], tree, FACES[face_index])
        assert not pending
    if active:
        assert active["job"] == len(completed) < len(jobs)
        ci, fi = jobs[active["job"]]
        pending, _, _ = frontier(cells[ci]["box"], active["tree"], FACES[fi])
        assert serialize_pending(pending) == active["pending"] and pending
    contexts = {}
    context_count = 0
    proposals = refinements = 0
    fatal_error = None

    def context(ci):
        nonlocal context_count
        if ci not in contexts:
            contexts[ci] = root_context(cells[ci])
            context_count += 1
        return contexts[ci]

    def validate_bindings():
        assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
        assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
        if source_path:
            assert sha(source_path) == source_hash

    def result(status, reason, nodes, summaries):
        return dict(format_version=1, status=status, stop_reason=reason,
                    precision_bits=args.precision, gap=str(GAP), target_curvature=str(MU),
                    proof_sha256=proof_hash, script_sha256=script_hash,
                    dependencies_sha256=dependencies,
                    input_sha256=source_hash if args.input else None,
                    resume_sha256=source_hash if args.resume else None,
                    original_endpoint_cells=5258, face_families_per_cell=4,
                    families=family_metadata(), own_types=[0, 1], one_vertex_included=False,
                    job_count=len(jobs), completed=completed, active=active,
                    new_nodes=nodes, revalidated_original_roots=context_count,
                    root_proposals=0, target_proposals=proposals,
                    refinements=refinements, fatal_error=fatal_error,
                    attempt_limits=None if args.input else dict(
                        additional_nodes=args.max_nodes, seconds=args.max_seconds,
                        additional_depth=args.max_depth),
                    replay_summaries=summaries, final_bindings_verified=True,
                    scope="All four first-cap cut/alias families over both own types "
                          "and both complete original external disks, outgoing targets "
                          "on full P at the actual attached height. No one-vertex case. "
                          "Only complete author and saved replay prove the signs.")

    if args.input:
        assert active is None and len(completed) == len(jobs)
        summaries = []
        checked = 0
        for ji, tree in enumerate(completed):
            ci, fi = jobs[ji]
            maximum = None

            def replay_leaf(box, targets):
                nonlocal maximum, checked
                passed, trial, info, _ = check_face(cells[ci], context(ci), box, FACES[fi], targets)
                assert passed and trial == targets, (ji, box, info)
                checked += 1
                value = arb(info["upper"])
                maximum = value.upper() if maximum is None else max(maximum, value.upper())

            pending, count, excluded = frontier(cells[ci]["box"], tree, FACES[fi], replay_leaf)
            assert not pending
            summaries.append(dict(job=ji, leaves=count, exclusions=excluded,
                                  maximum_upper=str(maximum) if maximum is not None else None))
            if ji % 128 == 0:
                print("REPLAY", ji, "/", len(jobs), "leaves", checked, flush=True)
        validate_bindings()
        write_atomic(args.output, result("passed", "all saved first-cap plateau currents replayed", 0, summaries))
        print("PASS", len(jobs), "jobs;", checked, "leaves; no proposals/refinements", flush=True)
        return 0

    nodes = 0
    start = time.monotonic()
    checkpoint = start
    reason = "all first-cap plateau currents verified"
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, args.max_seconds)
    try:
        while len(completed) < len(jobs):
            if nodes >= args.max_nodes or time.monotonic()-start >= args.max_seconds:
                raise BudgetStop("author additional-node/time cap")
            ji = len(completed)
            ci, fi = jobs[ji]
            if active is None:
                with atomic_state():
                    active = dict(job=ji, tree=[], pending=serialize_pending([(cells[ci]["box"], 0)]))
            box_strings, depth = active["pending"][-1]
            box = decode_box(box_strings)
            # The active box remains pending throughout all fallible arithmetic.
            if old.excluded(box):
                new_node = ["X"]
                replacement = []
            else:
                passed, trial, info, axis = check_face(cells[ci], context(ci), box, FACES[fi])
                proposals += 1
                if passed:
                    new_node = ["L", trial]
                    replacement = []
                else:
                    if depth >= args.max_depth:
                        reason = "maximum added depth; unresolved face"
                        active["failure"] = dict(box=box_strings, targets=trial, bounds=info)
                        break
                    left, right = old.split(box, axis)
                    new_node = ["S", axis]
                    replacement = serialize_pending([(left, depth+1), (right, depth+1)])
            with atomic_state():
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
                write_atomic(args.output, result("incomplete", "atomic checkpoint", nodes, []))
                print("CHECKPOINT", len(completed), "/", len(jobs), "new nodes", nodes, flush=True)
                checkpoint = time.monotonic()
    except BudgetStop as exc:
        reason = str(exc)
    except Exception as exc:
        # The uncommitted active box is still pending. Preserve that exact
        # frontier and stop; an inherited-root or arithmetic failure never
        # becomes an accepted leaf or a silent refinement.
        fatal_error = dict(type=type(exc).__name__, message=str(exc))
        reason = "unresolved arithmetic/inherited-input failure"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    validate_bindings()
    status = "passed" if len(completed) == len(jobs) and active is None else "incomplete"
    write_atomic(args.output, result(status, reason, nodes, []))
    print(status.upper(), len(completed), "/", len(jobs), "new nodes", nodes,
          "seconds", time.monotonic()-start, flush=True)
    return 0 if status == "passed" else 3 if fatal_error else 2


if __name__ == "__main__":
    raise SystemExit(main())

