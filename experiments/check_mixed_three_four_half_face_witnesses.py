#!/usr/bin/env python3
"""One frozen diagnostic for the mandatory real cuts of the half-face bound.

Read the protocol before running. No adaptive retry, subdivision, or output
replacement is implemented. Numerical proposals are not accepted as proofs.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path
import traceback

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_three_four_half_face_witness_protocol.md"
SCRIPT = "experiments/check_mixed_three_four_half_face_witnesses.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-three-four-half-face-witnesses.json"
OUTPUT = ROOT / "repro/results/research-mixed-three-four-half-face-witnesses-attempt01.json"
INITIAL = [
    ["2/5", "1/100"], ["7/20", "-1/100"], ["23/100", "1/20"],
    ["7/20", "-7/200"], ["3/10", "-13/250"], ["23/100", "1/20"],
]
SPECS = [(e, t) for e in ("27/100", "49/100")
         for t in ("1/5", "1/4", "3/10")]
PRIMARY = [
    ("repro/results/research-mixed-open-word-critical-localization.json",
     "repro/results/research-mixed-open-word-critical-localization-replay.json",
     "notes/research_mixed_open_word_critical_localization.md",
     "experiments/certify_mixed_open_word_critical_localization.py"),
    ("repro/results/research-mixed-endpoint-cap-rectangle.json",
     "repro/results/research-mixed-endpoint-cap-rectangle-replay.json",
     "notes/research_mixed_endpoint_cap_rectangle.md",
     "experiments/certify_mixed_endpoint_cap_rectangle.py"),
]
COUNTS = dict(equation_calls=0, jacobian_calls=0, dilogarithm_calls=0,
              proposal_iterations=0, inclusion_tests=0,
              explicit_private_criticals=0, action_evaluations=0,
              witness_evaluations=0)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def cp(pair):
    return acb(ar(pair[0]), ar(pair[1]))


def rational_midpoint(z):
    parts = [float(z.real.mid()), float(z.imag.mid())]
    if not all(math.isfinite(v) for v in parts):
        raise ValueError("nonfinite midpoint proposal")
    return [str(F(v)) for v in parts]


def identity(n):
    return acb_mat([[int(i == j) for j in range(n)] for i in range(n)])


def jp(z):
    return (2 * (PI * z).sin()).log()


def cot(z):
    return (PI * z).cot()


def node_equations(z, outside, eps):
    e, t, u = z
    fe = -jp(e-u)+jp(e+t)-eps*jp(e)+II*PI*(u-t+eps*(e-ar("1/2")))
    ft = jp(e+t)+jp(t+outside)-(2+eps)*jp(t) + \
        II*PI*(outside-e+eps*(t-ar("1/2")))
    fu = 2*(PI*u).cos().log()+(PI*(e-u)).sin().log() - \
        3*(PI*u).sin().log()+II*PI*e
    return [fe, ft, fu]


def equations(z):
    COUNTS["equation_calls"] += 1
    values = node_equations(z[:3], z[4], 0) + \
        node_equations(z[3:], z[1], 1)
    return acb_mat([[v] for v in values])


def node_jacobian(z, outside, eps):
    e, t, u = z
    b = PI*cot(e-u)
    c = PI*cot(e+t)
    d = PI*(2*(PI*u).tan()+3*cot(u))
    return [
        [-b+c-eps*PI*cot(e)+II*PI*eps, c-II*PI, b+II*PI],
        [c-II*PI, c+PI*cot(t+outside)-(2+eps)*PI*cot(t)+II*PI*eps, 0],
        [b+II*PI, 0, -d-b],
    ]


def jacobian(z):
    COUNTS["jacobian_calls"] += 1
    entries = [[acb(0) for _ in range(6)] for _ in range(6)]
    for offset, outside, eps in ((0, z[4], 0), (3, z[1], 1)):
        block = node_jacobian(z[offset:offset+3], outside, eps)
        for i in range(3):
            for j in range(3):
                entries[offset+i][offset+j] = block[i][j]
    entries[1][4] = entries[4][1] = PI*cot(z[1]+z[4])+II*PI
    return acb_mat(entries)


def J(z):
    COUNTS["dilogarithm_calls"] += 1
    z = acb(z)
    return (PI*PI/6-(2*PI*II*z).exp().polylog(2))/(2*PI*II) + \
        II*PI*z*(1-z)/2


def g(z):
    return J(z)+II*PI*z*(1-z)/2


def F_endpoint(e, u):
    return -2*J(ar("1/2")-u)-3*J(u)-J(e-u)+II*PI*e*u


def P_node(e, t, u, eps):
    return F_endpoint(e, u)+J(e+t)-J(t)-II*PI*e*t-eps*g(e)


def action(z):
    COUNTS["action_evaluations"] += 1
    e, a, u, f, b, v = z
    shared = J(a+b)-J(a)-J(b)+II*PI*a*b
    return P_node(e, a, u, 0)+P_node(f, b, v, 1)+shared-g(b)


def real_ball(value):
    return dict(ball=str(value), lower=str(value.lower()),
                upper=str(value.upper()))


def complex_ball(value):
    return dict(real=real_ball(value.real), imag=real_ball(value.imag))


def verify_inputs(manifest):
    expected = manifest["files_sha256"]
    required = {PROTOCOL, SCRIPT,
                "notes/research_mixed_three_four_physical_middle_reduction.md",
                "notes/research_mixed_three_four_ordinary_pair_target.md",
                "notes/research_mixed_two_vertex_first_collar.md",
                "notes/research_mixed_cap_real_cut_gaps.md",
                "notes/research_mixed_open_word_hessian.md",
                "notes/research_mixed_endpoint_cap_rectangle.md",
                "notes/research_mixed_three_four_physical_far_half.md",
                "notes/research_complete_boundary_full_index_interval.md"}
    for row in PRIMARY:
        required.update(row)
    assert required <= expected.keys(), "missing mandatory source bindings"
    for path, digest in expected.items():
        assert sha(ROOT/path) == digest, ("changed frozen input", path)
    visited = set()

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        data = json.loads((ROOT/path).read_text())
        for field in ("dependencies", "dependencies_sha256",
                      "primary_records", "primary_records_sha256"):
            deps = data.get(field, {})
            if not isinstance(deps, dict):
                continue
            for child, digest in deps.items():
                assert expected.get(child) == digest, ("unbound dependency", child)
                assert sha(ROOT/child) == digest, ("changed dependency", child)
                if child.startswith("repro/results/") and child.endswith(".json"):
                    inherit(child)

    for author_path, replay_path, proof_path, script_path in PRIMARY:
        author = json.loads((ROOT/author_path).read_text())
        replay = json.loads((ROOT/replay_path).read_text())
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == expected[author_path]
        assert replay["precision_bits"] >= author["precision_bits"]
        assert author["proof_sha256"] == replay["proof_sha256"] == expected[proof_path]
        assert author["script_sha256"] == replay["script_sha256"] == expected[script_path]
        if "domains" in author:
            assert author["domains"] == replay["domains"]
            # The replay recomputes enclosure strings at higher precision.
            # Its exact rational witnesses and case inventory must agree.
            for key in ("domain_count", "one_vertex_count", "leaves", "excluded", "visits"):
                assert author[key] == replay[key], ("changed coverage", key)
            author_single = [(row["epsilon"], row["witness"])
                             for row in author["one_vertex"]]
            replay_single = [(row["epsilon"], row["witness"])
                             for row in replay["one_vertex"]]
            assert author_single == replay_single
        inherit(author_path)
        inherit(replay_path)
    return expected


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    if OUTPUT.exists():
        raise FileExistsError("the single-run output already exists; no overwrite")
    result = dict(
        status="failed", verdict="inconclusive", precision_bits=256,
        initial_center=INITIAL, proposal_iteration_limit=24, disk_radius="1/1073741824",
        witness_inventory=SPECS, proposal_history=[], witnesses=[],
        unprocessed_inventory=list(SPECS), operation_counts=COUNTS,
        parameter_subdivisions=0, retries=0, source_cover_evaluations=0,
        scope="Necessary lower-witness diagnostic only; no upper envelope or knot theorem.",
    )
    frozen = None
    manifest_hash = None
    try:
        manifest_hash = sha(args.manifest)
        result["manifest_sha256"] = manifest_hash
        manifest = json.loads(args.manifest.read_text())
        result["claimed_files_sha256"] = manifest.get("files_sha256", {})
        assert manifest["root_reviewed"] is True and manifest["peer_reviewed"] is True
        assert manifest["precision_bits"] == 256 and manifest["proposal_iterations"] == 24
        assert manifest["disk_radius"] == "1/1073741824"
        assert manifest["initial_center"] == INITIAL
        assert manifest["witness_inventory"] == [list(p) for p in SPECS]
        assert manifest["output"] == str(OUTPUT.relative_to(ROOT))
        frozen = verify_inputs(manifest)
        result["files_sha256"] = frozen
        ctx.prec = 256
        PI, II = arb.pi(), acb(0, 1)
        centers = INITIAL
        for index in range(24):
            z = list(map(cp, centers))
            step = jacobian(z).inv()*equations(z)
            centers = [rational_midpoint(z[j]-step[j, 0]) for j in range(6)]
            COUNTS["proposal_iterations"] += 1
            result["proposal_history"].append(dict(iteration=index+1, centers=centers))

        z0 = list(map(cp, centers))
        inverse = jacobian(z0).inv()
        y_exact = [[rational_midpoint(inverse[i, j]) for j in range(6)]
                   for i in range(6)]
        Y = acb_mat([[cp(value) for value in row] for row in y_exact])
        radius = ar("1/1073741824")
        box = [z+acb(arb(0, radius), arb(0, radius)) for z in z0]
        result["final_center"] = centers
        result["rational_inverse"] = y_exact
        result["coordinate_boxes"] = [complex_ball(z) for z in box]

        def require(name, condition):
            result.setdefault("checks", []).append(dict(name=name, passed=bool(condition)))
            assert condition, name

        for side in (0, 3):
            e, t, u = box[side:side+3]
            require(f"node {side}: private chamber",
                    ar("33/100") < e.real < ar("47/100") and
                    ar("-9/100") < e.imag < ar("2/25"))
            require(f"node {side}: auxiliary chamber",
                    ar("21/100") < u.real < ar("1/4") and
                    ar("1/100") < u.imag < ar("1/10"))
            require(f"node {side}: attached rectangle",
                    ar("23/100") < t.real < ar("9/20") and
                    ar("-3/25") < t.imag < ar("3/25"))
            require(f"node {side}: regular primitive arguments",
                    all(0 < z.real < 1 for z in
                        [e, t, u, e-u, e+t, ar("1/2")-u]) and
                    0 < u.real < ar("1/2"))
        require("shared primitive argument", 0 < (box[1]+box[4]).real < 1)
        require("left original attached disk",
                abs(z0[1]-cp(["7/20", "-1/100"]))+radius < ar("9/100"))
        require("right original attached disk",
                abs(z0[4]-cp(["3/10", "-13/250"]))+radius < ar("8/125"))
        COUNTS["inclusion_tests"] += 1
        require("rational inverse is invertible", abs(Y.det()) > 0)
        residual = Y*equations(z0)
        error = identity(6)-Y*jacobian(box)
        rows = [sum(abs(error[i, j]) for j in range(6)) for i in range(6)]
        result["inclusion"] = [
            dict(residual=real_ball(abs(residual[i, 0])),
                 derivative_row=real_ball(rows[i]),
                 image_radius=real_ball(abs(residual[i, 0])+radius*rows[i]))
            for i in range(6)]
        for i in range(6):
            require(f"row {i}: contraction", rows[i] < 1)
            require(f"row {i}: strict disk inclusion",
                    abs(residual[i, 0])+radius*rows[i] < radius)

        M = action(box).real
        require("finite original action", M.is_finite())
        result["original_action"] = real_ball(M)
        lambdas = {}
        result["private_criticals"] = {}
        for es in ("27/100", "49/100"):
            e = acb(ar(es))
            disc = 1-2*(2*PI*II*e).exp()
            root = disc.sqrt()
            u = ((II+root)/2).atan()/PI
            COUNTS["explicit_private_criticals"] += 1
            require(f"private {es}: principal root", root.real > 0)
            require(f"private {es}: regular branch",
                    0 < u.real < e.real and u.imag > 0 and
                    0 < (e-u).real < ar("1/2") and u.real < ar("1/2"))
            lift = 2*(PI*u).cos().log()+(PI*(e-u)).sin().log() - \
                3*(PI*u).sin().log()+II*PI*e
            require(f"private {es}: original logarithmic lift", abs(lift) < PI)
            lambdas[es] = F_endpoint(e, u).real
            result["private_criticals"][es] = dict(
                point=complex_ball(u), lift=complex_ball(lift),
                lambda_value=real_ball(lambdas[es]))

        q_trial = (-7*J(ar("1/4"))).real
        result["first_cap_trial"] = real_ball(q_trial)
        for es, ts in SPECS:
            e, t = ar(es), ar(ts)
            B = q_trial+lambdas[es] + \
                (J(e+t)-J(e)-J(ar("1/2")-t)-3*J(t)).real
            diff = B-M
            require(f"witness {es},{ts}: finite", B.is_finite() and diff.is_finite())
            positive = bool(diff > 0)
            result["witnesses"].append(dict(
                private_cut=es, transform=ts, lower_witness=real_ball(B),
                difference_from_action=real_ball(diff),
                proves_criterion_impossible=positive))
            COUNTS["witness_evaluations"] += 1
            result["unprocessed_inventory"].remove((es, ts))
        result["verdict"] = ("half_face_criterion_refuted_for_all_main_heights"
                             if any(w["proves_criterion_impossible"]
                                    for w in result["witnesses"])
                             else "inconclusive")
        result["status"] = "completed"
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["traceback"] = traceback.format_exc()
    finally:
        def changed_or_missing(path, digest):
            try:
                return sha(path) != digest
            except OSError:
                return True

        if frozen is not None:
            changed = [p for p, h in frozen.items() if changed_or_missing(ROOT/p, h)]
            if changed:
                result["changed_inputs"] = changed
                result["status"] = "failed"
                result["verdict"] = "inconclusive"
        if manifest_hash is not None and changed_or_missing(args.manifest, manifest_hash):
            result["status"] = "failed"
            result["verdict"] = "inconclusive"
            result["manifest_changed"] = True
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        with OUTPUT.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    print(json.dumps(dict(status=result["status"], verdict=result["verdict"],
                          counts=COUNTS, output=str(OUTPUT))))
    if result["status"] != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
