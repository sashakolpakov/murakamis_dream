#!/usr/bin/env python3
"""One frozen two-center half-chain diagnostic. Read the protocol first.

No adaptive search, alternate proposal, retry, subdivision, or output
replacement is implemented. Newton proposals are never certificates.
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
PROTOCOL = "notes/research_mixed_three_four_following_action_diagnostic_protocol.md"
SCRIPT = "experiments/check_mixed_three_four_following_action_centers.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-three-four-following-action-centers.json"
OUTPUT = ROOT / "repro/results/research-mixed-three-four-following-action-centers-attempt01.json"
INITIAL = [
    ["2/5", "1/100"], ["7/20", "-1/100"], ["23/100", "1/20"],
    ["3/10", "-13/250"], ["3/10", "-13/250"],
]
CENTERS = [
    {"label": "c3", "external": ["7/20", "-1/100"]},
    {"label": "c4", "external": ["3/10", "-13/250"]},
]
RADIUS = "1/1073741824"
PRIMARY = [
    ("repro/results/research-mixed-open-word-critical-localization.json",
     "repro/results/research-mixed-open-word-critical-localization-replay.json",
     "notes/research_mixed_open_word_critical_localization.md",
     "experiments/certify_mixed_open_word_critical_localization.py",
     "experiments/certify_mixed_open_word_critical_localization.py"),
    ("repro/results/research-mixed-cyclic-block-localization.json",
     "repro/results/research-mixed-cyclic-block-localization-replay.json",
     "notes/research_mixed_cyclic_critical_localization.md",
     "experiments/certify_mixed_cyclic_block_localization.py",
     "experiments/replay_mixed_cyclic_block_localization.py"),
]
REQUIRED = {
    PROTOCOL, SCRIPT,
    "notes/research_mixed_alternating_cap_phase_entrance.md",
    "notes/research_mixed_actual_prefix_arbitrary_letter_phase_class.md",
    "notes/research_mixed_three_four_complete_transformed_prefix.md",
    "notes/research_mixed_three_four_next_conditional_attachment.md",
    "notes/research_mixed_three_four_following_action_direction.md",
    "notes/research_mixed_transformed_following_four_radial_majorant.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_open_word_hessian.md",
    "notes/research_mixed_cyclic_critical_height_bounds.md",
    "notes/research_mixed_three_four_half_face_witness_protocol.md",
    "experiments/check_mixed_three_four_half_face_witnesses.py",
}
COUNTS = dict(equation_calls=0, jacobian_calls=0, dilogarithm_calls=0,
              proposal_iterations=0, inclusion_tests=0,
              action_evaluations=0, comparison_evaluations=0)


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


def equations(v, outside):
    COUNTS["equation_calls"] += 1
    e, a, u, t, z = v
    values = [
        -jp(e-u)+jp(e+a)+II*PI*(u-a),
        jp(e+a)+jp(a+t)-2*jp(a)+II*PI*(t-e),
        2*(PI*u).cos().log()+(PI*(e-u)).sin().log()
        -3*(PI*u).sin().log()+II*PI*e,
        jp(a+t)+jp(t+z)-3*jp(t)+II*PI*(a-z+t-ar("1/2")),
        jp(t+z)+jp(z+outside)-3*jp(z)
        +II*PI*(outside-t+z-ar("1/2")),
    ]
    return acb_mat([[value] for value in values])


def jacobian(v, outside):
    COUNTS["jacobian_calls"] += 1
    e, a, u, t, z = v
    b, ea, at, tz, zc = [PI*cot(w) for w in
                         (e-u, e+a, a+t, t+z, z+outside)]
    d = PI*(2*(PI*u).tan()+3*cot(u))
    return acb_mat([
        [-b+ea, ea-II*PI, b+II*PI, 0, 0],
        [ea-II*PI, ea+at-2*PI*cot(a), 0, at+II*PI, 0],
        [b+II*PI, 0, -d-b, 0, 0],
        [0, at+II*PI, 0, at+tz-3*PI*cot(t)+II*PI, tz-II*PI],
        [0, 0, 0, tz-II*PI, tz+zc-3*PI*cot(z)+II*PI],
    ])


def J(z):
    COUNTS["dilogarithm_calls"] += 1
    z = acb(z)
    return (PI*PI/6-(2*PI*II*z).exp().polylog(2))/(2*PI*II) \
        + II*PI*z*(1-z)/2


def g(z):
    return J(z)+II*PI*z*(1-z)/2


def actions(v, outside):
    COUNTS["action_evaluations"] += 1
    e, a, u, t, z = v
    endpoint = -2*J(ar("1/2")-u)-3*J(u)-J(e-u) \
        + II*PI*e*u-II*PI*(e-e*e)/2
    bare = endpoint+g(e+a)+g(a+t)+g(t+z) \
        -2*g(a)-3*g(t)-g(z)+2*PI*II*a*t
    gram = g(z+outside)-2*g(z)-2*g(outside)+2*PI*II*z*outside
    return bare, bare+gram, gram


def real_ball(value):
    return dict(ball=str(value), lower=str(value.lower()), upper=str(value.upper()))


def complex_ball(value):
    return dict(real=real_ball(value.real), imag=real_ball(value.imag))


def verify_inputs(manifest):
    expected = manifest["files_sha256"]
    required = set(REQUIRED)
    for row in PRIMARY:
        required.update(row)
    assert required <= expected.keys(), "missing mandatory source binding"
    for path, digest in expected.items():
        assert sha(ROOT/path) == digest, ("changed frozen input", path)
    visited = set()

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        data = json.loads((ROOT/path).read_text())
        for field in ("dependencies", "dependencies_sha256", "primary_records",
                      "primary_records_sha256", "saved_replays", "saved_replays_sha256"):
            deps = data.get(field, {})
            if not isinstance(deps, dict):
                continue
            for child, digest in deps.items():
                assert expected.get(child) == digest, ("unbound dependency", child)
                assert sha(ROOT/child) == digest, ("changed dependency", child)
                if child.startswith("repro/results/") and child.endswith(".json"):
                    inherit(child)

    for author_path, replay_path, proof_path, author_script, replay_script in PRIMARY:
        author = json.loads((ROOT/author_path).read_text())
        replay = json.loads((ROOT/replay_path).read_text())
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == expected[author_path]
        ap = author.get("precision_bits", author.get("precision"))
        rp = replay.get("precision_bits", replay.get("precision"))
        assert isinstance(ap, int) and isinstance(rp, int) and rp >= ap
        assert author["proof_sha256"] == replay["proof_sha256"] == expected[proof_path]
        assert author["script_sha256"] == expected[author_script]
        assert replay["script_sha256"] == expected[replay_script]
        if "domains" in author:
            assert author["domains"] == replay["domains"]
            for key in ("domain_count", "one_vertex_count", "leaves", "excluded", "visits"):
                assert author[key] == replay[key], ("changed full coverage", key)
            assert [(v["epsilon"], v["witness"]) for v in author["one_vertex"]] == \
                [(v["epsilon"], v["witness"]) for v in replay["one_vertex"]]
        else:
            assert len(author["cases"]) == len(replay["cases"]) == 6
            for a_case, r_case in zip(author["cases"], replay["cases"]):
                assert a_case["types"] == r_case["types"]
                assert len(a_case["accepted"]) == r_case["original_boxes"]
                assert r_case["replay_boxes"] == r_case["original_boxes"]
                assert r_case["refinements"] == 0
        inherit(author_path)
        inherit(replay_path)
    return expected


def run_case(spec, case):
    outside = cp(spec["external"])
    centers = [list(value) for value in INITIAL]
    for index in range(24):
        v = list(map(cp, centers))
        step = jacobian(v, outside).inv()*equations(v, outside)
        centers = [rational_midpoint(v[j]-step[j, 0]) for j in range(5)]
        COUNTS["proposal_iterations"] += 1
        case["proposal_history"].append(dict(iteration=index+1, centers=centers))

    v0 = list(map(cp, centers))
    inverse = jacobian(v0, outside).inv()
    y_exact = [[rational_midpoint(inverse[i, j]) for j in range(5)]
               for i in range(5)]
    Y = acb_mat([[cp(value) for value in row] for row in y_exact])
    radius = ar(RADIUS)
    box = [v+acb(arb(0, radius), arb(0, radius)) for v in v0]
    case["final_center"] = centers
    case["rational_inverse"] = y_exact
    case["coordinate_boxes"] = [complex_ball(v) for v in box]

    def require(name, condition):
        case["checks"].append(dict(name=name, passed=bool(condition)))
        assert condition, name

    e, a, u, t, z = box
    require("original private chamber", ar("33/100") < e.real < ar("47/100")
            and ar("-9/100") < e.imag < ar("2/25"))
    require("original auxiliary chamber", ar("21/100") < u.real < ar("1/4")
            and ar("1/100") < u.imag < ar("1/10"))
    for label, w in (("a", a), ("t", t), ("z", z)):
        require(f"{label}: original Q chamber", ar("23/100") < w.real < ar("9/20")
                and ar("-3/25") < w.imag < ar("3/25"))
    require("original a typed disk", abs(v0[1]-cp(["7/20", "-1/100"]))+radius
            < ar("9/100"))
    for index, label in ((3, "t"), (4, "z")):
        require(f"{label}: original typed disk",
                abs(v0[index]-cp(["3/10", "-13/250"]))+radius < ar("8/125"))
        require(f"{label}: original reduced output disk",
                abs(v0[index]-cp(["3/10", "-13/250"]))+radius < ar("3/50"))
        require(f"{label}: original negative output height",
                ar("-51/500") < box[index].imag < ar("-1/1000"))
    arguments = [e, a, u, t, z, outside, ar("1/2")-u,
                 e-u, e+a, a+t, t+z, z+outside]
    require("all original primitive arguments regular",
            all(0 < w.real < 1 for w in arguments))
    require("original auxiliary sine and cosine branches", 0 < u.real < ar("1/2")
            and 0 < (e-u).real < ar("1/2"))

    COUNTS["inclusion_tests"] += 1
    require("rational inverse invertible", abs(Y.det()) > 0)
    center_gradient = equations(v0, outside)
    case["original_center_gradient"] = [complex_ball(center_gradient[i, 0])
                                        for i in range(5)]
    residual = Y*center_gradient
    error = identity(5)-Y*jacobian(box, outside)
    rows = [sum(abs(error[i, j]) for j in range(5)) for i in range(5)]
    case["inclusion"] = [dict(
        residual=real_ball(abs(residual[i, 0])),
        derivative_row=real_ball(rows[i]),
        image_radius=real_ball(abs(residual[i, 0])+radius*rows[i])) for i in range(5)]
    for i in range(5):
        require(f"row {i}: contraction", rows[i] < 1)
        require(f"row {i}: strict complex-disk inclusion",
                abs(residual[i, 0])+radius*rows[i] < radius)

    bare, whole, gram = actions(box, outside)
    require("finite original action values",
            all(v.real.is_finite() and v.imag.is_finite() for v in (bare, whole, gram)))
    case["bare_prefix_action"] = complex_ball(bare)
    case["whole_half_chain_action"] = complex_ball(whole)
    case["removed_gram_action"] = complex_ball(gram)
    outgoing_radius = (2*PI*z.imag).exp()
    require("outgoing radius in original range", ar("1/2") < outgoing_radius < 1)
    beta = (2/(1+outgoing_radius*outgoing_radius)).log()/2
    ceiling = ar("17539/9600")-ar("23/64000")-ar("6/25")*beta+beta*beta/20
    case["outgoing_radius"] = real_ball(outgoing_radius)
    case["radial_beta"] = real_ball(beta)
    for label, bound in (("real_initial", ar("7/4")), ("complete_complement", ceiling)):
        COUNTS["comparison_evaluations"] += 1
        difference = bare.real-bound
        require(f"{label}: finite comparison", bound.is_finite() and difference.is_finite())
        verdict = "positive" if difference > 0 else "negative" if difference < 0 else "inconclusive"
        case["comparisons"].append(dict(label=label, ceiling=real_ball(bound),
                                        margin=real_ball(difference), verdict=verdict))
    outcomes = [entry["verdict"] for entry in case["comparisons"]]
    case["verdict"] = ("both_margins_positive" if all(v == "positive" for v in outcomes)
                       else "a_sufficient_comparison_fails" if "negative" in outcomes
                       else "inconclusive")
    case["status"] = "completed"


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    if OUTPUT.exists():
        raise FileExistsError("the single-run output already exists; no overwrite")
    result = dict(status="failed", verdict="inconclusive", precision_bits=256,
                  initial_center=INITIAL, proposal_iterations_per_case=24, disk_radius=RADIUS,
                  center_inventory=CENTERS, cases=[], unprocessed_inventory=[v["label"] for v in CENTERS],
                  operation_counts=COUNTS, parameter_subdivisions=0, retries=0,
                  source_cover_evaluations=0,
                  scope="Two prescribed half-chain centers only; no cover, packet, or knot theorem.")
    frozen = None
    manifest_hash = None
    try:
        manifest_hash = sha(args.manifest)
        result["manifest_sha256"] = manifest_hash
        manifest = json.loads(args.manifest.read_text())
        result["claimed_files_sha256"] = manifest.get("files_sha256", {})
        assert manifest["root_reviewed"] is True and manifest["peer_reviewed"] is True
        assert manifest["precision_bits"] == 256
        assert manifest["proposal_iterations_per_case"] == 24
        assert manifest["disk_radius"] == RADIUS
        assert manifest["initial_center"] == INITIAL
        assert manifest["center_inventory"] == CENTERS
        assert manifest["output"] == str(OUTPUT.relative_to(ROOT))
        frozen = verify_inputs(manifest)
        result["files_sha256"] = frozen
        ctx.prec = 256
        PI, II = arb.pi(), acb(0, 1)
        for spec in CENTERS:
            case = dict(label=spec["label"], external=spec["external"], status="failed",
                        verdict="inconclusive", proposal_history=[], checks=[], comparisons=[])
            result["cases"].append(case)
            before = dict(COUNTS)
            try:
                run_case(spec, case)
            except Exception as exc:
                case["error"] = f"{type(exc).__name__}: {exc}"
                case["traceback"] = traceback.format_exc()
            finally:
                case["operation_counts"] = {key: COUNTS[key]-before[key] for key in COUNTS}
                result["unprocessed_inventory"].remove(spec["label"])
        if all(case["status"] == "completed" for case in result["cases"]):
            result["status"] = "completed"
            result["verdict"] = ("both_centers_have_positive_margins"
                                  if all(case["verdict"] == "both_margins_positive"
                                         for case in result["cases"])
                                  else "pointwise_comparisons_recorded_no_uniform_conclusion")
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
            result["manifest_changed"] = True
            result["status"] = "failed"
            result["verdict"] = "inconclusive"
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
