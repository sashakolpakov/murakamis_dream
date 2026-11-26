#!/usr/bin/env python3
"""Twenty-one type-four terminal comparisons from saved endpoint witnesses.

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
PROOF = ROOT / "notes/research_mixed_terminal_four_source_certificate.md"
ROOT_AUTHOR = "repro/results/research-mixed-open-word-critical-localization.json"
ROOT_REPLAY = "repro/results/research-mixed-open-word-critical-localization-replay.json"
KAPPA, MU, GAP = F(1, 2500000), F(3, 100), F(1, 20000)
IA, IT = (F(".22"), F(".45")), (F(".15"), F(".50"))
IE, IU = (F(".27"), F(".49")), (F(".10"), F(".269"))
HEIGHT_T, HEIGHTS_E = F(3, 25), (F(-11, 200), F(1, 25))
MASK_NORMALIZED_MIN = F(-7, 8)
REFERENCE_SCOPE = {
    "external_three": "full original D3",
    "external_four": "original D4 intersect Im(a)>=-27/250",
    "external_four_normalized_imaginary_minimum": str(MASK_NORMALIZED_MIN),
}
# kind, fixed real t/e (None means free), fixed t/e heights,
# retain actual reference t/e height. Penalties use only fixed alias heights.
FACES = [("flat_t", c, None, F(0), F(0), 0, 1) for c in IT]
FACES += [("flat_e", None, c, F(0), F(0), 1, 0) for c in IE]
FACES += [("corner", t, e, F(0), F(0), 0, 0) for t in IT for e in IE]
FACES += [("t_alias", None, None, sign*HEIGHT_T, F(0), 0, retain)
          for sign in (-1, 1) for retain in (0, 1)]
FACES += [("e_alias", None, None, F(0), he, retain, 0)
          for he in HEIGHTS_E for retain in (0, 1)]
FACES += [("double_alias", None, None, sign*HEIGHT_T, he, 0, 0)
          for sign in (-1, 1) for he in HEIGHTS_E]
FACES += [("raw_half", F(1, 2), None, F(0), F(0), 0, 0)]
assert len(FACES) == 21
ar, cp = old.ar, old.cp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encoded_box(box):
    return [[str(lo), str(hi)] for lo, hi in box]


def decode_box(box):
    return [tuple(map(F, side)) for side in box]


def center_box(box):
    return [((lo+hi)/2, (lo+hi)/2) for lo, hi in box]


def physical_box(box, neighbor):
    """Exact mask intersection; a boundary contact is retained."""
    assert neighbor in (0, 1)
    result = list(box)
    if neighbor == 1:
        lo, hi = result[1]
        lo = max(lo, MASK_NORMALIZED_MIN)
        if lo > hi:
            return None
        result[1] = (lo, hi)
    return result


def physically_excluded(box, neighbor):
    clipped = physical_box(box, neighbor)
    return clipped is None or old.excluded(clipped)


def original_root_proposals_forbidden(*args, **kwargs):
    raise AssertionError("complex-root proposals are forbidden")


def target_proposals_forbidden(*args, **kwargs):
    raise AssertionError("target proposals are forbidden during saved replay")


def family_inventory():
    return [[v if isinstance(v, str) or v is None else str(v) for v in face]
            for face in FACES]


def g(z):
    return primitive.J(z)+II*PI*z*(1-z)/2


def gp(z):
    return old.jp(z)+II*PI*(ar("1/2")-z)


def gpp(z):
    return PI*old.cot(z)-II*PI


def full_phase(a, e, t, u):
    """The literal original own-four action, including all marked phases."""
    return (primitive.phase(e, u)+g(a+t)+g(e+t)-3*g(t)-g(e)-g(a)
            -II*PI*e*(1-e)/2+2*II*PI*a*t)


def full_partials(a, e, t, u):
    se, su = primitive.partials(e, u)
    return dict(a=gp(a+t)-gp(a)+2*II*PI*t,
                t=gp(a+t)+gp(e+t)-3*gp(t)+2*II*PI*a,
                e=se+gp(e+t)-gp(e)-II*PI*(ar("1/2")-e),
                u=su)


def target_phase(a, e, t, u):
    if u is None:
        u, disc = primitive.critical(e)
        assert disc.real > 1 and u.is_finite(), "canonical endpoint branch enclosure"
    return full_phase(a, e, t, u)


def target_partials(a, e, t, u):
    if u is None:
        u, disc = primitive.critical(e)
        assert disc.real > 1 and u.is_finite(), "canonical endpoint branch enclosure"
    return full_partials(a, e, t, u)


def root_context(cell):
    box, neighbor, w = cell["box"], cell["neighbor"], cell["witness"]
    a = old.parameter(box, neighbor)
    assert old.test(w, a, 1) is not None, "inherited original-root failure"
    z0 = list(map(cp, w["centers"]))
    Y = acb_mat([[cp(v) for v in row] for row in w["inverse"]])
    radius = ar(w["radius"])
    z = [v+acb(arb(0, radius), arb(0, radius)) for v in z0]
    E = old.ident(3)-Y*old.jacobian(z, a, 1)
    q = max(sum((abs(E[i, j]) for j in range(3)), arb(0)).upper()
            for i in range(3))
    assert q < 1
    # Complete accepted own-four image boxes, never midpoint samples.
    assert ar(".333") < z[0].real < ar(".363")
    assert ar("-.051") < z[0].imag < ar("-.019")
    assert ar(".246") < z[1].real < ar(".350")
    assert ar("-.108") < z[1].imag < ar("-.020")
    assert ar(".21") < z[2].real < ar(".25")
    assert ar(".01") < z[2].imag < ar(".10")
    return dict(z0=z0, Y=Y, radius=radius, z=z, q=q)


def intersection(z, w):
    return acb(z.real.intersection(w.real), z.imag.intersection(w.imag))


def enclosing_root(context, parameter, steps):
    """Contract an already proved enclosure; never propose a new root.

    The original self-map supplies existence. Each Taylor image below
    contains that root for every parameter in the same parameter box.
    Intersection can therefore tighten but cannot change the root branch.
    """
    Y, z0, q = context["Y"], context["z0"], context["q"]
    residual = Y*old.equation(z0, parameter, 1)
    b = max(abs(residual[i, 0]).upper() for i in range(3))
    radius = min(context["radius"], (b/(1-q)).upper())
    z = [v+acb(arb(0, radius), arb(0, radius)) for v in z0]
    for _ in range(steps):
        mid = [acb(v.real.mid(), v.imag.mid()) for v in z]
        E = old.ident(3)-Y*old.jacobian(z, parameter, 1)
        image = (acb_mat([[v] for v in mid])-Y*old.equation(mid, parameter, 1)
                 +E*acb_mat([[z[i]-mid[i]] for i in range(3)]))
        z = [intersection(z[i], image[i, 0]) for i in range(3)]
        assert all(v.is_finite() for v in z)
    return z


def responses(z, a, Y):
    E = old.ident(3)-Y*old.jacobian(z, a, 1)
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


def target_names(face):
    if face[0] == "raw_half":
        return ["a", "e", "u"]
    return ["a"]+(["t"] if face[1] is None else [])+(["e"] if face[2] is None else [])


def target_box(face):
    intervals = dict(a=IA, t=IT, e=IE, u=IU)
    return [intervals[name] for name in target_names(face)]


def validate_trial(targets, face):
    assert isinstance(targets, list)
    trial = list(map(F, targets))
    bounds = target_box(face)
    assert len(trial) == len(bounds)
    assert all(lo <= t <= hi for t, (lo, hi) in zip(trial, bounds))
    assert targets == [str(v) for v in trial]
    return trial


def target_arguments(a, root, face, trial):
    kind, ft, fe, ht, he, st, se = face
    coords = dict(zip(target_names(face), trial))
    target = acb(ar(coords["a"]), a.imag)
    t = acb(ar(coords["t"] if ft is None else ft), ar(ht)+st*root[1].imag)
    e = acb(ar(coords["e"] if fe is None else fe), ar(he)+se*root[0].imag)
    u = acb(ar(coords["u"])) if kind == "raw_half" else None
    return target, e, t, u, st, se


def alias_penalty(face):
    return 2*PI*ar(abs(face[3])+abs(face[4]))


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


def propose_targets(a0, root0, face):
    """Floating real-target ascent; canonical explicit u_c only, no root solve."""
    def cm(z):
        return complex(float(z.real.mid()), float(z.imag.mid()))
    aa, er, tr = cm(a0), cm(root0[0]), cm(root0[1])
    pi = math.pi

    def pg(z):
        return cmath.log(2*cmath.sin(pi*z))+1j*pi*(.5-z)

    def uc(e):
        return cmath.atan((1j+cmath.sqrt(1-2*cmath.exp(2j*pi*e)))/2)/pi

    pref = pg(aa+tr)-pg(aa)+2j*pi*tr
    bounds, names = target_box(face), target_names(face)
    x = [(float(lo)+float(hi))/2 for lo, hi in bounds]

    def gradient(values):
        kind, ft, fe, ht, he, st, se = face
        coords = dict(zip(names, values))
        a = complex(coords["a"], aa.imag)
        t = complex(coords["t"] if ft is None else float(ft), float(ht)+st*tr.imag)
        e = complex(coords["e"] if fe is None else float(fe), float(he)+se*er.imag)
        u = complex(coords["u"], 0) if kind == "raw_half" else uc(e)
        pe = (-cmath.log(2*cmath.sin(pi*(e-u)))+1j*pi*u
              +pg(e+t)-pg(e)-1j*pi*(.5-e))
        derivatives = dict(
            a=(pg(a+t)-pg(a)+2j*pi*t-pref).real
              +2*float(KAPPA)*(coords["a"]-aa.real),
            t=(pg(a+t)+pg(e+t)-3*pg(t)+2j*pi*a).real,
            e=pe.real,
            u=(2*cmath.log(cmath.cos(pi*u))+cmath.log(cmath.sin(pi*(e-u)))
               -3*cmath.log(cmath.sin(pi*u))+1j*pi*e).real)
        return [derivatives[name] for name in names]

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
    return [min(hi, max(lo, F(format(value, ".12f"))))
            for value, (lo, hi) in zip(x, bounds)]


def check_face(cell, context, box, face, saved_trial=None):
    neighbor = cell["neighbor"]
    box = physical_box(box, neighbor)
    assert box is not None and not old.excluded(box)
    a = old.parameter(box, neighbor)
    a0 = old.parameter(center_box(box), neighbor)
    root = enclosing_root(context, a, 5)
    point = enclosing_root(context, a0, 12)
    trial = (propose_targets(a0, point, face) if saved_trial is None
             else validate_trial(saved_trial, face))
    bounds = target_box(face)
    assert len(trial) == len(bounds)
    assert all(lo <= t <= hi for t, (lo, hi) in zip(trial, bounds))
    tar0, e0, t0, u0, _, _ = target_arguments(a0, point, face, trial)
    pref0 = full_partials(a0, point[0], point[1], point[2])["a"]
    d0 = ar(trial[0])-a0.real
    value = (target_phase(tar0, e0, t0, u0).real
             -full_phase(a0, point[0], point[1], point[2]).real
             -pref0.real*d0+ar(KAPPA)*d0*d0-alias_penalty(face))

    tar, e, t, u, st, se = target_arguments(a, root, face, trial)
    partial = target_partials(tar, e, t, u)
    pa, pt, pe = (partial[name] for name in ("a", "t", "e"))
    pref = full_partials(a, root[0], root[1], root[2])["a"]
    response = responses(root, a, context["Y"])
    ep, tp = response[0], response[1]
    psecond = gpp(a+root[1])*(1+tp)-gpp(a)+2*PI*II*tp
    d = ar(trial[0])-a.real
    # Flags retain actual heights only. All alias penalties are fixed.
    dA = -d*psecond.real-2*ar(KAPPA)*d-st*pt.imag*tp.imag-se*pe.imag*ep.imag
    dH = (pref-pa).imag+d*psecond.imag-st*pt.imag*tp.real-se*pe.imag*ep.real
    radii = [ar(old.DISKS[neighbor][2]*(hi-lo)/2) for lo, hi in box]
    contributions = [abs(dA)*radii[0], abs(dH)*radii[1]]
    mean = sum(contributions, arb(0))
    gradients = dict(partial)
    gradients["a"] = pa.real-pref.real+2*ar(KAPPA)*d
    for name in ("t", "e", "u"):
        gradients[name] = partial[name].real
    gains = [gain(gradients[name], v, interval)
             for name, v, interval in zip(target_names(face), trial, bounds)]
    upper = value+mean+sum(gains, arb(0))
    assert upper.is_finite(), "nonfinite validated source enclosure"
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
                if domain["epsilon"] == 1:
                    cells.append(dict(domain=domain_index, node=node_index,
                                      neighbor=domain["neighbor_epsilon"],
                                      box=box, witness=node[1]))
        assert not pending
        assert (leaves, excluded) == (domain["leaves"], domain["excluded"])
        total_leaves += leaves
        total_excluded += excluded
    assert (total_nodes, total_leaves, total_excluded) == (10978, 5258, 233)
    assert [sum(c["neighbor"] == n for c in cells) for n in (0, 1)] == [1002, 909]
    return cells


def frontier(box, tree, face, neighbor, replay_leaf=None):
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
            assert len(node) == 1 and physically_excluded(cell, neighbor)
            excluded += 1
        else:
            assert node[0] == "L" and len(node) == 2 and not physically_excluded(cell, neighbor)
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
    assert ar("3.14")/100-2*ar(KAPPA) > ar(MU)
    assert old.DISKS[1][1]+old.DISKS[1][2]*MASK_NORMALIZED_MIN == F(-27, 250)
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
    cap_author_name = "repro/results/research-mixed-endpoint-cap-rectangle.json"
    cap_replay_name = "repro/results/research-mixed-endpoint-cap-rectangle-replay.json"
    cap_author, cap_replay = inherit(cap_author_name), inherit(cap_replay_name)
    assert cap_author["status"] == cap_replay["status"] == "passed"
    assert cap_replay["input_sha256"] == dependencies[cap_author_name]
    for record in (cap_author, cap_replay):
        bind("notes/research_mixed_endpoint_cap_rectangle.md", record["proof_sha256"])
        bind("experiments/certify_mixed_endpoint_cap_rectangle.py", record["script_sha256"])
        assert record["accepted_cells"] == 151 and record["visited_cells"] == 300
        assert len(record["cases"]) == 2
    for ac, rc in zip(cap_author["cases"], cap_replay["cases"]):
        for field in ("initial_box", "nodes", "accepted_cells", "visited_cells", "remaining_boxes"):
            assert ac[field] == rc[field]
        assert ac["remaining_boxes"] == 0
    for name in [
        "notes/research_mixed_terminal_four_joint_source.md",
        "notes/research_mixed_terminal_four_reduced_currents.md",
        "notes/research_mixed_terminal_four_private_tails.md",
        "notes/research_mixed_terminal_four_left_strip.md",
        "notes/research_mixed_terminal_four_right_triangle.md",
        "notes/research_mixed_terminal_transform_tails.md",
        "notes/research_mixed_endpoint_polynomial_collar.md",
        "notes/research_mixed_reversed_cap_assembly.md",
        "notes/research_mixed_open_word_endpoint_rectangles.md",
        "notes/research_mixed_open_local_factor_coverage.md",
        "notes/research_mixed_cyclic_critical_height_bounds.md",
        "experiments/check_mixed_open_word_endpoint_rectangles.py",
        "experiments/certify_mixed_endpoint_packet_extension.py",
        "experiments/certify_mixed_terminal_three_aliases.py",
        "notes/research_mixed_terminal_three_alias_certificate.md",
        "notes/research_mixed_terminal_three_joint_zero_mode.md",
        "experiments/check_mixed_terminal_three_joint_concavity_constants.py",
        "repro/results/research-mixed-terminal-three-joint-concavity-constants.json",
        "experiments/check_mixed_terminal_three_extended_concavity_constants.py",
        "repro/results/research-mixed-terminal-three-extended-concavity-constants.json",
        "experiments/check_mixed_terminal_transform_tail_constants.py",
        "repro/results/research-mixed-terminal-transform-tail-constants.json",
    ]:
        bind(name)
    extraction = inherit("repro/results/research-mixed-open-word-endpoint-rectangles.json")
    assert extraction["status"] == "passed"
    assert extraction["proof_sha256"] == dependencies[
        "notes/research_mixed_open_word_endpoint_rectangles.md"]
    assert extraction["script_sha256"] == dependencies[
        "experiments/check_mixed_open_word_endpoint_rectangles.py"]
    cells = original_cells(roots)
    jobs = [(index, face) for index in range(len(cells)) for face in range(len(FACES))]
    assert len(jobs) == 40131
    source_path = args.input or args.resume
    source_hash = sha(source_path) if source_path else None
    saved = json.loads(source_path.read_text()) if source_path else None
    if saved:
        assert saved["proof_sha256"] == proof_hash and saved["script_sha256"] == script_hash
        assert saved["dependencies_sha256"] == dependencies
        assert saved["gap"] == str(GAP) and saved["target_curvature"] == str(MU)
        assert saved["job_count"] == len(jobs)
        assert saved["family_inventory"] == family_inventory()
        assert saved["reference_scope"] == REFERENCE_SCOPE
        assert saved["status"] == ("passed" if args.input else "incomplete")
    completed = saved["completed"] if saved else []
    active = saved["active"] if saved else None
    assert len(completed) <= len(jobs)
    for ji, tree in enumerate(completed):
        ci, face_index = jobs[ji]
        pending, _, _ = frontier(cells[ci]["box"], tree, FACES[face_index], cells[ci]["neighbor"])
        assert not pending
    if active:
        assert active["job"] == len(completed) < len(jobs)
        ci, fi = jobs[active["job"]]
        pending, _, _ = frontier(cells[ci]["box"], active["tree"], FACES[fi], cells[ci]["neighbor"])
        assert serialize_pending(pending) == active["pending"] and pending
    contexts = {}
    context_count = 0
    proposals = refinements = 0
    attempted = 0
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
                    original_own_four_cells=1911, face_families_per_cell=21,
                    reference_scope=REFERENCE_SCOPE,
                    family_inventory=family_inventory(),
                    job_count=len(jobs), completed=completed, active=active,
                    new_nodes=nodes, attempted_nodes=attempted,
                    revalidated_original_roots=context_count,
                    root_proposals=0, target_proposals=proposals,
                    refinements=refinements, fatal_error=fatal_error,
                    attempt_limits=None if args.input else dict(
                        additional_nodes=args.max_nodes, seconds=args.max_seconds,
                        additional_depth=args.max_depth),
                    replay_summaries=summaries, final_bindings_verified=True,
                    scope="Eight reduced constant-mode faces, twelve reduced aliases, "
                          "and the raw half-transform face for own type four, on full "
                          "D3 and D4 intersect Im(a)>=-.108. All real targets use strict "
                          "concavity. Only a complete author plus saved replay proves "
                          "the twenty-one comparisons and their cited source consequences.")


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

            pending, count, excluded = frontier(cells[ci]["box"], tree, FACES[fi],
                                                 cells[ci]["neighbor"], replay_leaf)
            assert not pending
            summaries.append(dict(job=ji, leaves=count, exclusions=excluded,
                                  maximum_upper=str(maximum) if maximum is not None else None))
            if ji % 128 == 0:
                print("REPLAY", ji, "/", len(jobs), "leaves", checked, flush=True)
        validate_bindings()
        write_atomic(args.output, result("passed", "all saved type-four families replayed", 0, summaries))
        print("PASS", len(jobs), "jobs;", checked, "leaves; no proposals/refinements", flush=True)
        return 0

    nodes = 0
    start = time.monotonic()
    checkpoint = start
    reason = "all type-four families verified"
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
            attempted += 1
            # The active box remains pending throughout all fallible arithmetic.
            if physically_excluded(box, cells[ci]["neighbor"]):
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

