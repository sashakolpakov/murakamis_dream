#!/usr/bin/env python3
"""UNRUN: two fixed harmonic comparisons from the frozen cap-343 cover.

No Newton steps, root solves, gradients, inverses, old-checker imports,
adaptive alternatives, retries, or output replacement.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import traceback

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_cap_343_saved_height_protocol.md"
SCRIPT = "experiments/check_mixed_cap_343_saved_height_comparisons.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-cap-343-saved-height-comparisons.json"
OUTPUT = ROOT / "repro/results/research-mixed-cap-343-saved-height-comparisons-attempt01.json"
OLD_RESULT = "repro/results/research-mixed-cap-343-radius-coverage-attempt01.json"
OLD_MANIFEST = "repro/protocols/research-mixed-cap-343-radius-coverage.json"
OLD_PROTOCOL = "notes/research_mixed_cap_343_radius_coverage_protocol.md"
OLD_SCRIPT = "experiments/check_mixed_cap_343_radius_coverage.py"
PINNED = {
    OLD_RESULT: "1edec732c28ac64dd11ca63026722e8062a0598aa49b15ea2f2887a7dcbdb3d5",
    OLD_MANIFEST: "45091a7e3284acbcf4d8adf03267ef505f378d8a019f3a867aba7ca77255fb25",
    OLD_PROTOCOL: "971fb50a335c9ad3588ef431e09ee0ccd204e6ef95c4b14b23695b96dbe070ae",
    OLD_SCRIPT: "ce4942685353371270917272a5d069e230df2597df5207ae5d52c11117c27084",
    "notes/research_mixed_next_three_correlated_last_row_transport.md":
        "565922d4a5594c3d603882b98fe477c676377ca6dd334cfb99130de229b02872",
}
REQUIRED = {
    PROTOCOL, SCRIPT, *PINNED,
    "notes/research_mixed_cap_343_radius_exclusion.md",
    "notes/research_mixed_next_three_deep_radius_actual_coverage.md",
    "notes/research_mixed_alternating_cap_phase_entrance.md",
    "notes/research_mixed_arbitrary_prefix_pregram_curve.md",
    "notes/research_mixed_three_four_next_local_source.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_cyclic_critical_localization.md",
    "notes/research_mixed_open_word_hessian.md",
}
FORBIDDEN_BINDING = "notes/research_finite_exceptions_progress.md"
DEPENDENCY_FIELDS = (
    "dependencies", "dependencies_sha256", "primary_records",
    "primary_records_sha256", "saved_replays", "saved_replays_sha256",
    "files_sha256",
)
PRECISION = 256
CELLS = 512
POINT_RADIUS = "1/1073741824"
CELL_RADIUS = "1/256"
VARIABLES = ["e", "a", "u", "p", "y", "s", "z"]
COMPARISONS = ["f1", "f2"]
THRESHOLDS = {"f1": "log(41/50)/(2*pi)", "f2": "log(4/5)/(2*pi)"}
FORMULAS = {
    "f1": "log(41/50)/(2*pi)-Im(y)",
    "f2": "Im(p)-Im(y)-log(4/5)/(2*pi)",
}
CIRCLES = [
    {"label": "P3", "center": ["7/20", "-1/100"],
     "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "P4", "center": ["3/10", "-13/250"],
     "radius": "3/50", "typed_radius": "8/125"},
]
OLD_INITIAL = [
    ["2/5", "1/100"], ["7/20", "-1/100"], ["23/100", "1/20"],
    ["3/10", "-13/250"], ["3/10", "-13/250"],
    ["7/20", "-1/100"], ["7/20", "-1/100"],
]
OLD_COUNTS = {
    "action_evaluations": 0, "adaptive_subdivisions": 0,
    "dilogarithm_evaluations": 0, "equation_calls": 26624,
    "jacobian_calls": 27648, "margin_evaluations": 1024,
    "parameter_inclusion_tests": 1024, "point_inclusion_tests": 1024,
    "point_inverse_calls": 1024, "proposal_inverse_calls": 24576,
    "proposal_iterations_attempted": 24576,
    "proposal_iterations_completed": 24576,
    "response_evaluations": 1024, "retries": 0,
    "saved_root_evaluations": 0, "threshold_evaluations": 1,
    "wide_interval_jacobian_inversions": 0,
}
COUNTS = {
    "saved_response_cells_attempted": 0, "saved_center_decodes": 0,
    "saved_inverse_decodes": 0, "uniform_guard_tests": 0,
    "jacobian_calls": 0, "response_evaluations": 0,
    "threshold_evaluations": 0, "comparisons_attempted": 0,
    "comparisons_completed": 0,
    "new_root_solves": 0, "newton_steps": 0, "proposal_iterations": 0,
    "equation_calls": 0, "new_root_inclusion_tests": 0,
    "point_matrix_inversions": 0, "wide_interval_matrix_inversions": 0,
    "action_evaluations": 0, "dilogarithm_evaluations": 0,
    "adaptive_subdivisions": 0, "retries": 0,
}
PI = None
II = None


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_relative(path):
    value = Path(path)
    if value.is_absolute() or ".." in value.parts:
        raise ValueError(("unsafe dependency path", path))
    if path == FORBIDDEN_BINDING:
        raise ValueError(("mutable progress binding forbidden", path))
    return ROOT / value


def hash_bindings(bindings):
    return {path: sha(safe_relative(path)) for path in sorted(bindings)}


def settings():
    return {
        "precision_bits": PRECISION, "variables": VARIABLES,
        "circle_inventory": CIRCLES, "cells_per_circle": CELLS,
        "comparison_inventory": COMPARISONS,
        "comparison_formulas": FORMULAS, "thresholds": THRESHOLDS,
        "point_radius": POINT_RADIUS, "parameter_radius": CELL_RADIUS,
        "saved_result": OLD_RESULT, "saved_manifest": OLD_MANIFEST,
        "response_method": "Neumann_row4_and_correlated_row3_minus_row4",
        "output": str(OUTPUT.relative_to(ROOT)),
        "newton_steps": 0, "matrix_inversions": 0,
    }


def inventory():
    return [
        {
            "id": f'{circle["label"]}:{index:03d}',
            "circle": circle["label"], "index": index,
            "theta_start_pi": str(F(2*index, CELLS)),
            "theta_end_pi": str(F(2*(index+1), CELLS)),
            "theta_midpoint_pi": str(F(2*index+1, CELLS)),
        }
        for circle in CIRCLES for index in range(CELLS)
    ]


def old_check_names():
    names = [
        "full parameter enclosure in larger original typed disk",
        "rational inverse nonsingular",
    ]
    for tag in ("midpoint", "whole_cell"):
        names.extend([
            tag+": finite parameter/root box", tag+": private chamber",
            tag+": auxiliary chamber",
        ])
        names.extend(tag+": "+v+" common chamber" for v in ("a", "p", "y", "s", "z"))
        names.extend(tag+": "+v+" original type-three disk" for v in ("a", "s", "z"))
        names.extend(tag+": "+v+" original type-four disk" for v in ("p", "y"))
        names.extend([tag+": all original primitive strips", tag+": original auxiliary branches"])
        for i in range(7):
            names.extend([
                tag+f" row {i}: contraction", tag+f" row {i}: strict disk inclusion",
            ])
    names.extend([
        "Neumann maximum row bound below one",
        "original external derivative denominator nonzero",
        "finite Neumann response and real angular derivative",
        "finite midpoint/direct/transported margins",
    ])
    return names


def verify_saved_metadata(old, old_manifest, frozen_inventory):
    if old["status"] != "completed" or old["validity"] != "provenance_verified":
        raise AssertionError("old radius attempt not completed and validated")
    if old["manifest_sha256"] != PINNED[OLD_MANIFEST] or old["final_manifest_sha256"] != PINNED[OLD_MANIFEST]:
        raise AssertionError("old manifest hash mismatch")
    inherited = old_manifest["files_sha256"]
    for key in ("claimed_files_sha256", "files_sha256", "final_files_sha256"):
        if old[key] != inherited:
            raise AssertionError(("old binding map mismatch", key))
    for key in ("root_reviewed", "peer_reviewed", "execution_authorized"):
        if old_manifest.get(key) is not True:
            raise AssertionError(("missing old approval", key))
    if old_manifest.get("execution_authorized_by") != "/root":
        raise AssertionError("old execution not root-authorized")
    reviews = old_manifest["review_records"]
    if {r["reviewer"] for r in reviews} != {"/root", "/root/terminal_scope_review"}:
        raise AssertionError("old review inventory mismatch")
    for review in reviews:
        if not (review["verdict"] == "PASS"
                and review["protocol_sha256"] == PINNED[OLD_PROTOCOL]
                and review["checker_sha256"] == PINNED[OLD_SCRIPT]
                and review["execution_performed"] is False):
            raise AssertionError("old exact-byte static approval mismatch")
    fixed = {
        "precision_bits": PRECISION, "variables": VARIABLES,
        "circle_inventory": CIRCLES, "cells_per_circle": CELLS,
        "proposal_iterations_per_cell": 24,
        "initial_rational_proposal": OLD_INITIAL,
        "point_radius": POINT_RADIUS, "parameter_radius": CELL_RADIUS,
        "output": OLD_RESULT, "threshold": "log(10/7)/(2*pi)",
        "margin": "Im(y)+log(10/7)/(2*pi)",
        "response_method": "row_4_Neumann_with_external_column_6",
    }
    for key, value in fixed.items():
        if old[key] != value or old_manifest[key] != value:
            raise AssertionError(("old setting mismatch", key))
    if old["inventory"] != frozen_inventory or old["unprocessed_inventory"] != []:
        raise AssertionError("old inventory incomplete or changed")
    if old["operation_counts"] != OLD_COUNTS or len(old["cells"]) != 1024:
        raise AssertionError("old operations or cell count changed")
    expected_checks = [{"name": name, "passed": True} for name in old_check_names()]
    for expected, cell in zip(frozen_inventory, old["cells"]):
        if any(cell[key] != value for key, value in expected.items()):
            raise AssertionError(("old cell label mismatch", expected["id"]))
        if cell["status"] != "completed" or cell["verdict"] != "positive_shallow" or "error" in cell:
            raise AssertionError(("old cell not passed", cell["id"]))
        if cell["checks"] != expected_checks:
            raise AssertionError(("old full check inventory mismatch", cell["id"]))
        history = cell["proposal_history"]
        if [step["iteration"] for step in history] != list(range(1, 25)):
            raise AssertionError(("old proposal history incomplete", cell["id"]))
        if cell["final_center"] != history[-1]["centers"]:
            raise AssertionError(("old final center changed", cell["id"]))
        if any(len(step["centers"]) != 7 for step in history):
            raise AssertionError(("old proposal shape", cell["id"]))
        inverse = cell["rational_inverse"]
        if len(inverse) != 7 or any(len(row) != 7 for row in inverse):
            raise AssertionError(("old inverse shape", cell["id"]))
        if set(cell["inclusions"]) != {"midpoint", "whole_cell"}:
            raise AssertionError(("old inclusions missing", cell["id"]))
        for tag in ("midpoint", "whole_cell"):
            inclusion = cell["inclusions"][tag]
            if any(len(inclusion[key]) != 7 for key in
                   ("rows", "coordinate_boxes", "original_center_gradient")):
                raise AssertionError(("old inclusion inventory incomplete", cell["id"], tag))
        if (cell["comparison"]["verdict"] != "positive_shallow"
                or cell["comparison"]["threshold"] != old["harmonic_threshold"]):
            raise AssertionError(("old stored comparison changed", cell["id"]))
    if len(old["disk_results"]) != 2:
        raise AssertionError("old disk inventory mismatch")
    for result, circle in zip(old["disk_results"], CIRCLES):
        if result["circle"] != circle["label"] or result["verdict"] != "whole_disk_strictly_shallow_deep_domain_excluded":
            raise AssertionError("old disk verdict mismatch")
        for key in ("attempted", "completed", "positive_shallow"):
            if result[key] != 512:
                raise AssertionError(("old disk completion count", key))
        for key in ("failed", "inconclusive", "negative_deep", "other_status", "unprocessed"):
            if result[key] != 0:
                raise AssertionError(("old disk nonpass count", key))
    return inherited


def verify_inputs(manifest, frozen_inventory):
    expected = manifest["files_sha256"]
    if FORBIDDEN_BINDING in expected or not REQUIRED <= expected.keys():
        raise AssertionError("missing mandatory or forbidden mutable binding")
    if manifest.get("execution_authorized_by") != "/root":
        raise AssertionError("new execution not root-authorized")
    reviews = manifest["review_records"]
    if (len(reviews) != 2 or {r["reviewer"] for r in reviews}
            != {"/root", "/root/endpoint_majorant_review"}):
        raise AssertionError("new static review inventory mismatch")
    for review in reviews:
        if not (review["verdict"] == "PASS"
                and review["protocol_sha256"] == expected[PROTOCOL]
                and review["checker_sha256"] == expected[SCRIPT]
                and review["execution_performed"] is False):
            raise AssertionError("new exact-byte static approval mismatch")
    for path, digest in PINNED.items():
        if expected.get(path) != digest:
            raise AssertionError(("incorrect pinned source", path))
    observed = hash_bindings(expected)
    if observed != expected:
        raise AssertionError(("changed frozen input",
                              [p for p in observed if observed[p] != expected[p]]))
    old = json.loads(safe_relative(OLD_RESULT).read_text())
    old_manifest = json.loads(safe_relative(OLD_MANIFEST).read_text())
    inherited = verify_saved_metadata(old, old_manifest, frozen_inventory)
    for path, digest in inherited.items():
        if expected.get(path) != digest:
            raise AssertionError(("inherited binding omitted or changed", path))
    for source in old["primary_provenance"]:
        author = json.loads(safe_relative(source["author"]).read_text())
        replay = json.loads(safe_relative(source["replay"]).read_text())
        if source["status"] != "passed_metadata_verified" or author["status"] != "passed" or replay["status"] != "passed":
            raise AssertionError(("unpassed inherited primary record", source))
        if replay["input_sha256"] != expected[source["author"]]:
            raise AssertionError(("inherited replay input mismatch", source["replay"]))
    visited, edges = set(), []

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        data = json.loads(safe_relative(path).read_text())
        for field in DEPENDENCY_FIELDS:
            dependencies = data.get(field, {})
            if not isinstance(dependencies, dict):
                continue
            for child, digest in dependencies.items():
                if not isinstance(digest, str) or len(digest) != 64:
                    raise AssertionError(("unsupported dependency entry", path, field, child))
                if expected.get(child) != digest or observed.get(child) != digest:
                    raise AssertionError(("unbound or changed dependency", path, field, child))
                edges.append({"record": path, "field": field,
                              "dependency": child, "sha256": digest})
                if child.startswith("repro/results/") and child.endswith(".json"):
                    inherit(child)
    inherit(OLD_RESULT)
    inherit(OLD_MANIFEST)
    edge_key = lambda item: (item["record"], item["field"], item["dependency"], item["sha256"])
    if sorted(edges, key=edge_key) != sorted(manifest["transitive_dependency_edges"], key=edge_key):
        raise AssertionError("transitive dependency edge inventory mismatch")
    return observed, old, {
        "old_result": OLD_RESULT, "old_manifest": OLD_MANIFEST,
        "saved_cells_verified": 1024, "saved_checks_per_cell": 64,
        "inherited_files": len(inherited), "transitive_records": sorted(visited),
        "transitive_edge_count": len(edges),
        "old_primary_provenance": old["primary_provenance"],
    }


def ar(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def saved_cp(pair):
    if len(pair) != 2 or any(not isinstance(part, str) for part in pair):
        raise ValueError("malformed saved rational complex number")
    if any(str(F(part)) != part for part in pair):
        raise ValueError("noncanonical saved rational")
    return acb(ar(pair[0]), ar(pair[1]))


def cp(pair):
    return acb(ar(pair[0]), ar(pair[1]))


def real_ball(value):
    return {"ball": str(value), "lower": str(value.lower()), "upper": str(value.upper())}


def complex_ball(value):
    return {"real": real_ball(value.real), "imag": real_ball(value.imag)}


def upper(value):
    return F(str(value.upper().fmpq()))


def lower(value):
    return F(str(value.lower().fmpq()))


def finite(value):
    return value.real.is_finite() and value.imag.is_finite()


def require(record, name, condition):
    passed = bool(condition)
    record["checks"].append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)


def root_box(centers, radius):
    return [value+acb(arb(0, radius), arb(0, radius)) for value in centers]


def uniform_guards(cell, centers, box, radius, outside, circle):
    COUNTS["uniform_guard_tests"] += 1
    e, a, u, p, y, s, z = box
    require(cell, "finite parameter and uniform root box",
            finite(outside) and all(finite(value) for value in box))
    require(cell, "full parameter enclosure in larger original typed disk",
            abs(outside-cp(circle["center"])) < ar(circle["typed_radius"]))
    require(cell, "private chamber", ar("33/100") < e.real < ar("47/100")
            and ar("-9/100") < e.imag < ar("2/25"))
    require(cell, "auxiliary chamber", ar("21/100") < u.real < ar("1/4")
            and ar("1/100") < u.imag < ar("1/10"))
    for i in (1, 3, 4, 5, 6):
        require(cell, VARIABLES[i]+": common chamber",
                ar("23/100") < box[i].real < ar("9/20")
                and ar("-3/25") < box[i].imag < ar("3/25"))
    for i in (1, 5, 6):
        require(cell, VARIABLES[i]+": original type-three disk",
                abs(centers[i]-cp(["7/20", "-1/100"]))+radius < ar("9/100"))
    for i in (3, 4):
        require(cell, VARIABLES[i]+": original type-four disk",
                abs(centers[i]-cp(["3/10", "-13/250"]))+radius < ar("8/125"))
    arguments = [e, a, u, p, y, s, z, outside, ar("1/2")-u,
                 e-u, e+a, a+p, p+y, y+s, s+z, z+outside]
    require(cell, "all original primitive strips",
            all(0 < value.real < 1 for value in arguments))
    require(cell, "original auxiliary branches",
            0 < u.real < ar("1/2") and 0 < (e-u).real < ar("1/2"))


def jacobian(v, outside):
    COUNTS["jacobian_calls"] += 1
    e, a, u, p, y, s, z = v
    cot = lambda value: (PI*value).cot()
    eu, ea, ap, py, ys, sz, zb = [
        PI*cot(value) for value in (e-u, e+a, a+p, p+y, y+s, s+z, z+outside)
    ]
    du = PI*(2*(PI*u).tan()+3*cot(u))
    return acb_mat([
        [-eu+ea, ea-II*PI, eu+II*PI, 0, 0, 0, 0],
        [ea-II*PI, ea+ap-2*PI*cot(a), 0, ap+II*PI, 0, 0, 0],
        [eu+II*PI, 0, -du-eu, 0, 0, 0, 0],
        [0, ap+II*PI, 0, ap+py-3*PI*cot(p)+II*PI, py-II*PI, 0, 0],
        [0, 0, 0, py-II*PI, py+ys-3*PI*cot(y)+II*PI, ys+II*PI, 0],
        [0, 0, 0, 0, ys+II*PI, ys+sz-2*PI*cot(s), sz-II*PI],
        [0, 0, 0, 0, 0, sz-II*PI, sz+zb-2*PI*cot(z)],
    ])


def classify(value):
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "inconclusive"


def reconstruct_response(circle, old_cell, cell):
    COUNTS["saved_response_cells_attempted"] += 1
    centers_raw, inverse_raw = old_cell["final_center"], old_cell["rational_inverse"]
    cell["saved_rational_center"] = centers_raw
    cell["saved_rational_preconditioner"] = inverse_raw
    COUNTS["saved_center_decodes"] += 1
    centers = [saved_cp(pair) for pair in centers_raw]
    COUNTS["saved_inverse_decodes"] += 1
    matrix = acb_mat([[saved_cp(pair) for pair in row] for row in inverse_raw])
    omega = PI/CELLS
    theta_mid = PI*ar(F(2*cell["index"]+1, CELLS))
    theta_cell = theta_mid+arb(0, omega.upper())
    rho, circle_center = ar(circle["radius"]), cp(circle["center"])
    exponential = (II*theta_cell).exp()
    outside = circle_center+rho*exponential
    b_theta = II*rho*exponential
    point = root_box(centers, ar(POINT_RADIUS))
    uniform = root_box(centers, ar(CELL_RADIUS))
    cell["theta_cell"] = real_ball(theta_cell)
    cell["external_cell"] = complex_ball(outside)
    cell["parameter_angular_derivative"] = complex_ball(b_theta)
    cell["reconstructed_midpoint_box"] = [complex_ball(value) for value in point]
    cell["reconstructed_uniform_box"] = [complex_ball(value) for value in uniform]
    uniform_guards(cell, centers, uniform, ar(CELL_RADIUS), outside, circle)
    identity = acb_mat([[int(i == j) for j in range(7)] for i in range(7)])
    error = identity-matrix*jacobian(uniform, outside)
    rows = [sum(abs(error[i, j]) for j in range(7)) for i in range(7)]
    row_difference = sum(abs(error[3, j]-error[4, j]) for j in range(7))
    k_rows = [upper(value) for value in rows]
    k, k34 = max(k_rows), upper(row_difference)
    ma = max(upper(abs(matrix[j, 6])) for j in range(7))
    cell["jacobian_error"] = [
        [complex_ball(error[i, j]) for j in range(7)] for i in range(7)
    ]
    cell["neumann_bounds"] = {
        "row_norms": [real_ball(value) for value in rows],
        "row_upper_exact": [str(value) for value in k_rows],
        "maximum_row_upper_exact": str(k),
        "row3_minus_row4_norm": real_ball(row_difference),
        "row3_minus_row4_upper_exact": str(k34),
        "column6_maximum_upper_exact": str(ma),
    }
    require(cell, "uniform Neumann maximum row bound below one", k < 1)
    denominator = 1-(-2*PI*II*(uniform[6]+outside)).exp()
    require(cell, "original external derivative denominator nonzero",
            abs(denominator) > 0)
    gamma = 2*PI*II/denominator
    COUNTS["response_evaluations"] += 1
    common_radius = abs(gamma)*ar(ma)/(1-ar(k))
    responses = {
        "f1": (gamma*matrix[4, 6], common_radius*ar(k_rows[4])),
        "f2": (-gamma*(matrix[3, 6]-matrix[4, 6]), common_radius*ar(k34)),
    }
    cell["external_mixed_derivative"] = complex_ball(gamma)
    for name, (center, radius) in responses.items():
        require(cell, name+": finite response", finite(center) and radius.is_finite())
    return point, uniform, responses, b_theta, rho, omega


def compare(name, record, data, threshold):
    COUNTS["comparisons_attempted"] += 1
    point, uniform, responses, b_theta, rho, omega = data
    center, radius = responses[name]
    angular_center = (center*b_theta).imag
    angular_error = rho*radius
    derivative = angular_center+arb(0, angular_error.upper())
    if name == "f1":
        midpoint = threshold-point[4].imag
        direct = threshold-uniform[4].imag
    elif name == "f2":
        midpoint = point[3].imag-point[4].imag-threshold
        direct = uniform[3].imag-uniform[4].imag-threshold
    else:
        raise AssertionError("unrecognized fixed comparison")
    require(record, "finite derivative and midpoint/direct margins",
            derivative.is_finite() and midpoint.is_finite() and direct.is_finite())
    derivative_upper = upper(abs(derivative))
    debit = omega*ar(derivative_upper)
    whole = midpoint+arb(0, debit.upper())
    require(record, "finite transported whole-cell margin", whole.is_finite())
    record.update({
        "threshold": real_ball(threshold),
        "response_center": complex_ball(center), "response_error_radius": real_ball(radius),
        "angular_center": real_ball(angular_center), "angular_error_radius": real_ball(angular_error),
        "angular_derivative": real_ball(derivative),
        "derivative_absolute_upper_exact": str(derivative_upper),
        "midpoint_margin": real_ball(midpoint), "midpoint_verdict": classify(midpoint),
        "direct_whole_cell_margin": real_ball(direct),
        "transport_debit": real_ball(debit), "whole_cell_margin": real_ball(whole),
        "whole_cell_margin_lower_exact": str(lower(whole)),
        "whole_cell_margin_upper_exact": str(upper(whole)),
        "status": "completed", "verdict": classify(whole),
    })
    COUNTS["comparisons_completed"] += 1


def disk_summary(result, circle, name):
    records = [cell["comparisons"][name] for cell in result["cells"]
               if cell["circle"] == circle["label"]]
    completed = [record for record in records if record["status"] == "completed"]
    signs = [record["verdict"] for record in completed]
    all_done = len(records) == CELLS and len(completed) == CELLS
    verdict = "inconclusive_no_whole_disk_sign"
    if all_done and all(sign == "positive" for sign in signs):
        verdict = "whole_disk_strictly_positive"
    elif all_done and all(sign == "negative" for sign in signs):
        verdict = "whole_disk_strictly_negative"
    elif "positive" in signs and "negative" in signs:
        verdict = "mixed_certified_boundary_signs_no_whole_disk_sign"
    summary = {
        "circle": circle["label"], "comparison": name, "verdict": verdict,
        "present": len(records), "completed": len(completed),
        "positive": signs.count("positive"), "negative": signs.count("negative"),
        "inconclusive": signs.count("inconclusive"),
        "failed_ids": [r["id"] for r in records if r["status"] == "failed"],
        "blocked_ids": [r["id"] for r in records if r["status"] == "blocked"],
        "unprocessed_ids": [r["id"] for r in records if r["status"] == "unprocessed"],
        "absent_cell_count": CELLS-len(records),
        "harmonic_whole_disk_enclosure_exact": None,
    }
    if all_done:
        lo = min(F(r["whole_cell_margin_lower_exact"]) for r in completed)
        hi = max(F(r["whole_cell_margin_upper_exact"]) for r in completed)
        summary["harmonic_whole_disk_enclosure_exact"] = [str(lo), str(hi)]
    return summary


def error_record(error):
    return {"type": type(error).__name__, "message": str(error),
            "traceback": traceback.format_exc()}


def update_pending(result):
    cells = {cell["id"]: cell for cell in result["cells"]}
    result["unprocessed_cells"] = [
        item["id"] for item in result["inventory"]
        if item["id"] not in cells or cells[item["id"]]["status"] == "unprocessed"
    ]
    result["unprocessed_comparisons"] = [
        item["id"]+":"+name for item in result["inventory"] for name in COMPARISONS
        if item["id"] not in cells
        or cells[item["id"]]["comparisons"][name]["status"] == "unprocessed"
    ]
    result["failed_cell_ids"] = [
        cell["id"] for cell in result["cells"]
        if cell["status"] in ("failed", "partial_failure")
    ]
    result["failed_comparison_ids"] = [
        record["id"] for cell in result["cells"] for record in cell["comparisons"].values()
        if record["status"] == "failed"
    ]
    result["blocked_comparison_ids"] = [
        record["id"] for cell in result["cells"] for record in cell["comparisons"].values()
        if record["status"] == "blocked"
    ]


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    manifest_hash = sha(args.manifest)
    manifest = json.loads(args.manifest.read_text())
    if not all(manifest.get(key) is True for key in
               ("root_reviewed", "peer_reviewed", "execution_authorized")):
        raise PermissionError("unreviewed or unauthorized frozen manifest; no evaluation")
    for key, value in settings().items():
        if manifest.get(key) != value:
            raise AssertionError(("changed fixed setting", key))
    frozen_inventory = inventory()
    result = {
        "status": "failed", "validity": "not_yet_verified",
        "verdict": "no_mathematical_conclusion", **settings(),
        "manifest_sha256": manifest_hash,
        "claimed_files_sha256": manifest.get("files_sha256", {}),
        "inventory": frozen_inventory, "cells": [], "operation_counts": COUNTS,
        "scope": "Two harmonic comparisons on the original ordinary cap343 half-chain; no finite-source conclusion.",
    }
    update_pending(result)
    bindings = None
    with OUTPUT.open("x") as output:
        try:
            bindings, old, audit = verify_inputs(manifest, frozen_inventory)
            result["files_sha256"] = bindings
            result["saved_metadata_audit"] = audit
            result["validity"] = "initial_provenance_verified"
            ctx.prec = PRECISION
            PI, II = arb.pi(), acb(0, 1)
            COUNTS["threshold_evaluations"] += 2
            thresholds = {
                "f1": ar("41/50").log()/(2*PI),
                "f2": ar("4/5").log()/(2*PI),
            }
            result["threshold_balls"] = {name: real_ball(value) for name, value in thresholds.items()}
            circles = {circle["label"]: circle for circle in CIRCLES}
            for item, old_cell in zip(frozen_inventory, old["cells"]):
                cell = {
                    **item, "status": "unprocessed", "checks": [],
                    "comparisons": {
                        name: {"id": item["id"]+":"+name, "comparison": name,
                               "status": "unprocessed", "verdict": "inconclusive",
                               "checks": []}
                        for name in COMPARISONS
                    },
                }
                result["cells"].append(cell)
                try:
                    data = reconstruct_response(circles[item["circle"]], old_cell, cell)
                except Exception as error:
                    cell["status"] = "failed"
                    cell["shared_error"] = error_record(error)
                    for record in cell["comparisons"].values():
                        record["status"] = "blocked"
                        record["blocked_by"] = "shared reconstruction/response failure"
                else:
                    for name in COMPARISONS:
                        record = cell["comparisons"][name]
                        try:
                            compare(name, record, data, thresholds[name])
                        except Exception as error:
                            record["status"] = "failed"
                            record["error"] = error_record(error)
                    cell["status"] = (
                        "completed" if all(r["status"] == "completed"
                                           for r in cell["comparisons"].values())
                        else "partial_failure"
                    )
                finally:
                    update_pending(result)
                print(cell["id"], cell["status"],
                      *(cell["comparisons"][name]["verdict"] for name in COMPARISONS),
                      flush=True)
            result["disk_results"] = [
                disk_summary(result, circle, name)
                for circle in CIRCLES for name in COMPARISONS
            ]
            result["status"] = "completed"
            result["verdict"] = "per_disk_comparison_results_recorded"
        except BaseException as error:
            result["error"] = error_record(error)
        finally:
            update_pending(result)
            try:
                final_manifest = sha(args.manifest)
                result["final_manifest_sha256"] = final_manifest
                if final_manifest != manifest_hash:
                    raise AssertionError("manifest changed during attempt")
                if bindings is not None:
                    final_bindings = hash_bindings(bindings)
                    result["final_files_sha256"] = final_bindings
                    if final_bindings != bindings:
                        raise AssertionError("frozen inputs changed during attempt")
                    result["validity"] = "provenance_verified"
                else:
                    result["validity"] = "invalid_provenance"
            except BaseException as error:
                result["status"] = "invalidated"
                result["validity"] = "invalid_provenance"
                result["final_validation_error"] = error_record(error)
            if result["validity"] != "provenance_verified":
                result["verdict"] = "no_mathematical_conclusion"
                for summary in result.get("disk_results", []):
                    summary["provisional_verdict"] = summary["verdict"]
                    summary["verdict"] = "invalidated_no_mathematical_conclusion"
                    summary["harmonic_whole_disk_enclosure_exact"] = None
            json.dump(result, output, indent=2, sort_keys=True)
            output.write("\n")
            output.flush()


if __name__ == "__main__":
    main()
