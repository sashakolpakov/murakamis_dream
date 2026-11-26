#!/usr/bin/env python3
"""UNRUN: one reviewed, frozen, nonadaptive cap-343 radius cover.

Read the matching protocol. No pilots, retries, old-checker imports,
saved-root evaluations, adaptive refinement, or output replacement.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import traceback

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_cap_343_radius_coverage_protocol.md"
SCRIPT = "experiments/check_mixed_cap_343_radius_coverage.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-cap-343-radius-coverage.json"
OUTPUT = ROOT / "repro/results/research-mixed-cap-343-radius-coverage-attempt01.json"
PRECISION = 256
CELLS = 512
ITERATIONS = 24
POINT_RADIUS = "1/1073741824"
CELL_RADIUS = "1/256"
VARIABLES = ["e", "a", "u", "p", "y", "s", "z"]
INITIAL = [
    ["2/5", "1/100"], ["7/20", "-1/100"], ["23/100", "1/20"],
    ["3/10", "-13/250"], ["3/10", "-13/250"],
    ["7/20", "-1/100"], ["7/20", "-1/100"],
]
CIRCLES = [
    {"label": "P3", "center": ["7/20", "-1/100"],
     "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "P4", "center": ["3/10", "-13/250"],
     "radius": "3/50", "typed_radius": "8/125"},
]
PRIMARY = [
    (
        "repro/results/research-mixed-open-word-critical-localization.json",
        "repro/results/research-mixed-open-word-critical-localization-replay.json",
        "notes/research_mixed_open_word_critical_localization.md",
        "experiments/certify_mixed_open_word_critical_localization.py",
        "experiments/certify_mixed_open_word_critical_localization.py",
    ),
    (
        "repro/results/research-mixed-cyclic-block-localization.json",
        "repro/results/research-mixed-cyclic-block-localization-replay.json",
        "notes/research_mixed_cyclic_critical_localization.md",
        "experiments/certify_mixed_cyclic_block_localization.py",
        "experiments/replay_mixed_cyclic_block_localization.py",
    ),
    (
        "repro/results/research-mixed-open-word-hessian.json",
        "repro/results/research-mixed-open-word-hessian-replay.json",
        "notes/research_mixed_open_word_hessian.md",
        "experiments/check_mixed_open_word_hessian.py",
        "experiments/check_mixed_open_word_hessian.py",
    ),
]
DEPENDENCY_FIELDS = (
    "dependencies", "dependencies_sha256", "primary_records",
    "primary_records_sha256", "saved_replays", "saved_replays_sha256",
    "files_sha256",
)
REQUIRED = {
    PROTOCOL, SCRIPT,
    "notes/research_mixed_next_three_deep_radius_actual_coverage.md",
    "notes/research_mixed_alternating_cap_phase_entrance.md",
    "notes/research_mixed_arbitrary_prefix_pregram_curve.md",
    "notes/research_mixed_geometric_action_calibration.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_three_four_next_local_source.md",
    "notes/research_mixed_three_four_following_critical_curve.md",
    "notes/research_mixed_rational_critical_transport.md",
    "notes/research_mixed_cyclic_critical_height_bounds.md",
    "notes/research_mixed_open_local_factor_coverage.md",
    "notes/research_mixed_open_word_endpoint_rectangles.md",
    "notes/research_mixed_reduced_disk_conditional_packets.md",
    "notes/research_mixed_three_four_following_action_diagnostic_protocol.md",
    "notes/research_mixed_three_four_following_boundary_diagnostic_protocol.md",
    "notes/research_mixed_three_four_following_saved_response_protocol.md",
    "experiments/check_mixed_three_four_following_action_centers.py",
    "experiments/check_mixed_three_four_following_boundary_cover.py",
    "experiments/check_mixed_three_four_following_saved_response.py",
}
COUNTS = {
    "equation_calls": 0, "jacobian_calls": 0,
    "proposal_iterations_attempted": 0, "proposal_iterations_completed": 0,
    "proposal_inverse_calls": 0, "point_inverse_calls": 0,
    "point_inclusion_tests": 0, "parameter_inclusion_tests": 0,
    "response_evaluations": 0, "margin_evaluations": 0,
    "threshold_evaluations": 0,
    "action_evaluations": 0, "dilogarithm_evaluations": 0,
    "wide_interval_jacobian_inversions": 0, "saved_root_evaluations": 0,
    "adaptive_subdivisions": 0, "retries": 0,
}
PI = None
II = None


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def cp(pair):
    return acb(ar(pair[0]), ar(pair[1]))


def rational_midpoint(value):
    parts = [float(value.real.mid()), float(value.imag.mid())]
    if not all(math.isfinite(part) for part in parts):
        raise ValueError("nonfinite rational proposal")
    return [str(F(part)) for part in parts]


def exact_upper(value):
    return F(str(value.upper().fmpq()))


def exact_lower(value):
    return F(str(value.lower().fmpq()))


def identity(n):
    return acb_mat([[int(i == j) for j in range(n)] for i in range(n)])


def jp(value):
    return (2 * (PI * value).sin()).log()


def cot(value):
    return (PI * value).cot()


def equations(v, outside):
    COUNTS["equation_calls"] += 1
    e, a, u, p, y, s, z = v
    values = [
        -jp(e-u) + jp(e+a) + II*PI*(u-a),
        jp(e+a) + jp(a+p) - 2*jp(a) + II*PI*(p-e),
        2*(PI*u).cos().log() + (PI*(e-u)).sin().log()
        - 3*(PI*u).sin().log() + II*PI*e,
        jp(a+p) + jp(p+y) - 3*jp(p)
        + II*PI*(a-y+p-ar("1/2")),
        jp(p+y) + jp(y+s) - 3*jp(y)
        + II*PI*(s-p+y-ar("1/2")),
        jp(y+s) + jp(s+z) - 2*jp(s) + II*PI*(y-z),
        jp(s+z) + jp(z+outside) - 2*jp(z) + II*PI*(outside-s),
    ]
    return acb_mat([[value] for value in values])


def jacobian(v, outside):
    COUNTS["jacobian_calls"] += 1
    e, a, u, p, y, s, z = v
    eu, ea, ap, py, ys, sz, zb = [
        PI*cot(value) for value in
        (e-u, e+a, a+p, p+y, y+s, s+z, z+outside)
    ]
    du = PI*(2*(PI*u).tan() + 3*cot(u))
    return acb_mat([
        [-eu+ea, ea-II*PI, eu+II*PI, 0, 0, 0, 0],
        [ea-II*PI, ea+ap-2*PI*cot(a), 0, ap+II*PI, 0, 0, 0],
        [eu+II*PI, 0, -du-eu, 0, 0, 0, 0],
        [0, ap+II*PI, 0, ap+py-3*PI*cot(p)+II*PI, py-II*PI, 0, 0],
        [0, 0, 0, py-II*PI, py+ys-3*PI*cot(y)+II*PI, ys+II*PI, 0],
        [0, 0, 0, 0, ys+II*PI, ys+sz-2*PI*cot(s), sz-II*PI],
        [0, 0, 0, 0, 0, sz-II*PI, sz+zb-2*PI*cot(z)],
    ])


def real_ball(value):
    return {
        "ball": str(value),
        "lower": str(value.lower()), "upper": str(value.upper()),
    }


def complex_ball(value):
    return {"real": real_ball(value.real), "imag": real_ball(value.imag)}


def finite_complex(value):
    return value.real.is_finite() and value.imag.is_finite()


def require(cell, name, condition):
    passed = bool(condition)
    cell["checks"].append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)


def safe_relative(path):
    path = Path(path)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe dependency path")
    return ROOT / path


def hash_bindings(bindings):
    return {path: sha(safe_relative(path)) for path in sorted(bindings)}


def verify_inputs(manifest):
    expected = manifest["files_sha256"]
    required = set(REQUIRED)
    for row in PRIMARY:
        required.update(row)
    if not required <= expected.keys():
        raise AssertionError("missing mandatory source/provenance bindings")
    observed = hash_bindings(expected)
    if observed != expected:
        changed = [path for path in observed if observed[path] != expected[path]]
        raise AssertionError(("changed frozen inputs", changed))
    visited = set()
    dependency_edges = []

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
                if expected.get(child) != digest:
                    raise AssertionError(("unbound dependency", path, field, child))
                if observed.get(child) != digest:
                    raise AssertionError(("changed transitive dependency", child))
                dependency_edges.append({
                    "record": path, "field": field,
                    "dependency": child, "sha256": digest,
                })
                if child.startswith("repro/results/") and child.endswith(".json"):
                    inherit(child)

    primary_inventory = []
    for author_path, replay_path, proof_path, author_script, replay_script in PRIMARY:
        author = json.loads(safe_relative(author_path).read_text())
        replay = json.loads(safe_relative(replay_path).read_text())
        if author["status"] != "passed" or replay["status"] != "passed":
            raise AssertionError(("unpassed primary record", author_path, replay_path))
        if replay["input_sha256"] != expected[author_path]:
            raise AssertionError(("replay input mismatch", replay_path))
        ap = author.get("precision_bits", author.get("precision"))
        rp = replay.get("precision_bits", replay.get("precision"))
        if not isinstance(ap, int) or not isinstance(rp, int) or rp < ap:
            raise AssertionError(("primary precision mismatch", author_path, replay_path))
        if author["proof_sha256"] != expected[proof_path]:
            raise AssertionError(("author proof mismatch", author_path))
        if replay["proof_sha256"] != expected[proof_path]:
            raise AssertionError(("replay proof mismatch", replay_path))
        if author["script_sha256"] != expected[author_script]:
            raise AssertionError(("author script mismatch", author_path))
        if replay["script_sha256"] != expected[replay_script]:
            raise AssertionError(("replay script mismatch", replay_path))
        if author_path == PRIMARY[0][0]:
            if author["domains"] != replay["domains"]:
                raise AssertionError(("endpoint inventory changed", author_path))
            for key in ("domain_count", "one_vertex_count", "leaves", "excluded", "visits"):
                if author[key] != replay[key]:
                    raise AssertionError(("endpoint coverage changed", key))
            if [(row["epsilon"], row["witness"]) for row in author["one_vertex"]] != [
                (row["epsilon"], row["witness"]) for row in replay["one_vertex"]
            ]:
                raise AssertionError("one-vertex inventory changed")
        elif author_path == PRIMARY[1][0]:
            if len(author["cases"]) != len(replay["cases"]) or len(author["cases"]) != 6:
                raise AssertionError("ordinary case inventory changed")
            for original, checked in zip(author["cases"], replay["cases"]):
                if original["types"] != checked["types"]:
                    raise AssertionError("ordinary case type changed")
                if len(original["accepted"]) != checked["original_boxes"]:
                    raise AssertionError("ordinary original box count changed")
                if checked["replay_boxes"] != checked["original_boxes"]:
                    raise AssertionError("ordinary replay box count changed")
                if checked["refinements"] != 0:
                    raise AssertionError("ordinary replay refinement")
        elif author_path == PRIMARY[2][0]:
            for key in (
                "scalar_names", "exact_checks", "scalar_inequality_count",
                "exact_check_count", "domains", "endpoint_difference_lower_over_pi",
                "endpoint_u_lower_over_pi", "interior_pair_hessian_lower_over_pi",
                "inverse_norm_upper_times_pi", "open_word_hessian_lower_over_pi",
            ):
                if author[key] != replay[key]:
                    raise AssertionError(("Hessian inventory or constant changed", key))
            for key in (
                "critical_roots_computed", "parameter_cells", "cyclic_word_enumerations",
            ):
                if author[key] != 0 or replay[key] != 0:
                    raise AssertionError(("unexpected Hessian operation count", key))
        else:
            raise AssertionError(("unrecognized primary schema", author_path))
        inherit(author_path)
        inherit(replay_path)
        primary_inventory.append({
            "author": author_path, "replay": replay_path,
            "author_precision": ap, "replay_precision": rp,
            "status": "passed_metadata_verified",
        })
    expected_edges = manifest["transitive_dependency_edges"]
    edge_key = lambda item: (
        item["record"], item["field"], item["dependency"], item["sha256"]
    )
    if sorted(dependency_edges, key=edge_key) != sorted(expected_edges, key=edge_key):
        raise AssertionError("transitive dependency inventory mismatch")
    return observed, primary_inventory


def guarded_box(cell, tag, centers, radius, outside):
    box = [value + acb(arb(0, radius), arb(0, radius)) for value in centers]
    e, a, u, p, y, s, z = box
    require(cell, tag+": finite parameter/root box",
            finite_complex(outside) and all(finite_complex(value) for value in box))
    require(cell, tag+": private chamber",
            ar("33/100") < e.real < ar("47/100")
            and ar("-9/100") < e.imag < ar("2/25"))
    require(cell, tag+": auxiliary chamber",
            ar("21/100") < u.real < ar("1/4")
            and ar("1/100") < u.imag < ar("1/10"))
    for index in (1, 3, 4, 5, 6):
        value = box[index]
        require(cell, tag+": "+VARIABLES[index]+" common chamber",
                ar("23/100") < value.real < ar("9/20")
                and ar("-3/25") < value.imag < ar("3/25"))
    for index in (1, 5, 6):
        require(cell, tag+": "+VARIABLES[index]+" original type-three disk",
                abs(centers[index]-cp(["7/20", "-1/100"]))+radius < ar("9/100"))
    for index in (3, 4):
        require(cell, tag+": "+VARIABLES[index]+" original type-four disk",
                abs(centers[index]-cp(["3/10", "-13/250"]))+radius < ar("8/125"))
    arguments = [
        e, a, u, p, y, s, z, outside, ar("1/2")-u,
        e-u, e+a, a+p, p+y, y+s, s+z, z+outside,
    ]
    require(cell, tag+": all original primitive strips",
            all(0 < value.real < 1 for value in arguments))
    require(cell, tag+": original auxiliary branches",
            0 < u.real < ar("1/2") and 0 < (e-u).real < ar("1/2"))
    return box


def inclusion(cell, tag, centers, inverse, radius, outside):
    key = "point_inclusion_tests" if tag == "midpoint" else "parameter_inclusion_tests"
    COUNTS[key] += 1
    record = {"radius": real_ball(radius)}
    cell["inclusions"][tag] = record
    box = guarded_box(cell, tag, centers, radius, outside)
    record["coordinate_boxes"] = [complex_ball(value) for value in box]
    gradient = equations(centers, outside)
    residual = inverse*gradient
    jac = jacobian(box, outside)
    error = identity(7)-inverse*jac
    rows = [sum(abs(error[i, j]) for j in range(7)) for i in range(7)]
    record["original_center_gradient"] = [
        complex_ball(gradient[i, 0]) for i in range(7)
    ]
    record["rows"] = [
        {
            "residual": real_ball(abs(residual[i, 0])),
            "derivative_row": real_ball(rows[i]),
            "image_radius": real_ball(abs(residual[i, 0])+radius*rows[i]),
        } for i in range(7)
    ]
    for i in range(7):
        require(cell, tag+f" row {i}: contraction", rows[i] < 1)
        require(cell, tag+f" row {i}: strict disk inclusion",
                abs(residual[i, 0])+radius*rows[i] < radius)
    return box, rows


def classify(interval):
    if interval > 0:
        return "positive_shallow"
    if interval < 0:
        return "negative_deep"
    return "inconclusive"


def run_cell(circle, index, cell, threshold):
    theta_mid = PI*ar(F(2*index+1, CELLS))
    omega = PI/CELLS
    theta_cell = theta_mid+arb(0, omega.upper())
    circle_center = cp(circle["center"])
    rho = ar(circle["radius"])
    outside_mid = circle_center+rho*(II*theta_mid).exp()
    circle_exp = (II*theta_cell).exp()
    outside_cell = circle_center+rho*circle_exp
    b_theta = II*rho*circle_exp
    cell["external_midpoint"] = complex_ball(outside_mid)
    cell["external_cell"] = complex_ball(outside_cell)
    cell["theta_cell"] = real_ball(theta_cell)
    cell["theta_halfwidth"] = real_ball(omega)
    require(cell, "full parameter enclosure in larger original typed disk",
            abs(outside_cell-circle_center) < ar(circle["typed_radius"]))
    proposals = [list(pair) for pair in INITIAL]
    for iteration in range(ITERATIONS):
        COUNTS["proposal_iterations_attempted"] += 1
        v = list(map(cp, proposals))
        COUNTS["proposal_inverse_calls"] += 1
        step = jacobian(v, outside_mid).inv()*equations(v, outside_mid)
        proposals = [rational_midpoint(v[j]-step[j, 0]) for j in range(7)]
        COUNTS["proposal_iterations_completed"] += 1
        cell["proposal_history"].append({
            "iteration": iteration+1, "centers": proposals,
        })
    centers = list(map(cp, proposals))
    COUNTS["point_inverse_calls"] += 1
    inverse_mid = jacobian(centers, outside_mid).inv()
    inverse_exact = [
        [rational_midpoint(inverse_mid[i, j]) for j in range(7)] for i in range(7)
    ]
    inverse = acb_mat([[cp(pair) for pair in row] for row in inverse_exact])
    cell["final_center"] = proposals
    cell["rational_inverse"] = inverse_exact
    require(cell, "rational inverse nonsingular", abs(inverse.det()) > 0)
    point_box, _ = inclusion(
        cell, "midpoint", centers, inverse, ar(POINT_RADIUS), outside_mid
    )
    uniform_box, rows = inclusion(
        cell, "whole_cell", centers, inverse, ar(CELL_RADIUS), outside_cell
    )

    COUNTS["response_evaluations"] += 1
    k_rows = [exact_upper(value) for value in rows]
    k = max(k_rows)
    ma = max(exact_upper(abs(inverse[j, 6])) for j in range(7))
    require(cell, "Neumann maximum row bound below one", k < 1)
    denominator = 1-(-2*PI*II*(uniform_box[6]+outside_cell)).exp()
    require(cell, "original external derivative denominator nonzero",
            abs(denominator) > 0)
    gamma = 2*PI*II/denominator
    response_center = -gamma*inverse[4, 6]
    response_radius = abs(gamma)*ar(k_rows[4])*ar(ma)/(1-ar(k))
    angular_center = (response_center*b_theta).imag
    angular_error = rho*response_radius
    derivative = angular_center+arb(0, angular_error.upper())
    require(cell, "finite Neumann response and real angular derivative",
            finite_complex(response_center) and response_radius.is_finite()
            and derivative.is_finite())
    cell["response"] = {
        "k_rows_exact_upper": [str(value) for value in k_rows],
        "k_exact_upper": str(k), "column_max_exact_upper": str(ma),
        "inverse_entry_4_6": complex_ball(inverse[4, 6]),
        "external_mixed_derivative": complex_ball(gamma),
        "center": complex_ball(response_center),
        "error_radius": real_ball(response_radius),
        "parameter_angular_derivative": complex_ball(b_theta),
        "angular_center": real_ball(angular_center),
        "angular_error_radius": real_ball(angular_error),
        "margin_derivative": real_ball(derivative),
    }
    COUNTS["margin_evaluations"] += 1
    midpoint_margin = point_box[4].imag+threshold
    direct_margin = uniform_box[4].imag+threshold
    derivative_upper = exact_upper(abs(derivative))
    debit = omega*ar(derivative_upper)
    whole_margin = midpoint_margin+arb(0, debit.upper())
    require(cell, "finite midpoint/direct/transported margins",
            midpoint_margin.is_finite() and direct_margin.is_finite()
            and whole_margin.is_finite())
    cell["comparison"] = {
        "threshold": real_ball(threshold),
        "midpoint_margin": real_ball(midpoint_margin),
        "midpoint_verdict": classify(midpoint_margin),
        "direct_whole_cell_margin": real_ball(direct_margin),
        "derivative_absolute_exact_upper": str(derivative_upper),
        "transport_debit": real_ball(debit),
        "whole_cell_margin": real_ball(whole_margin),
        "whole_cell_margin_lower_exact": str(exact_lower(whole_margin)),
        "whole_cell_margin_upper_exact": str(exact_upper(whole_margin)),
        "verdict": classify(whole_margin),
    }
    cell["verdict"] = classify(whole_margin)
    cell["status"] = "completed"


def settings():
    return {
        "precision_bits": PRECISION,
        "variables": VARIABLES,
        "circle_inventory": CIRCLES,
        "cells_per_circle": CELLS,
        "proposal_iterations_per_cell": ITERATIONS,
        "initial_rational_proposal": INITIAL,
        "point_radius": POINT_RADIUS,
        "parameter_radius": CELL_RADIUS,
        "output": str(OUTPUT.relative_to(ROOT)),
        "threshold": "log(10/7)/(2*pi)",
        "margin": "Im(y)+log(10/7)/(2*pi)",
        "response_method": "row_4_Neumann_with_external_column_6",
    }


def disk_summary(result, circle):
    cells = [cell for cell in result["cells"] if cell["circle"] == circle["label"]]
    completed = [cell for cell in cells if cell["status"] == "completed"]
    signs = [cell["verdict"] for cell in completed]
    all_done = len(cells) == CELLS and len(completed) == CELLS
    if all_done and all(sign == "positive_shallow" for sign in signs):
        verdict = "whole_disk_strictly_shallow_deep_domain_excluded"
    elif all_done and all(sign == "negative_deep" for sign in signs):
        verdict = "whole_disk_strictly_deep_domain_covered"
    elif "positive_shallow" in signs and "negative_deep" in signs:
        verdict = "mixed_certified_boundary_signs_no_whole_disk_classification"
    else:
        verdict = "inconclusive_no_whole_disk_classification"
    summary = {
        "circle": circle["label"], "verdict": verdict,
        "attempted": len(cells), "completed": len(completed),
        "positive_shallow": signs.count("positive_shallow"),
        "negative_deep": signs.count("negative_deep"),
        "inconclusive": signs.count("inconclusive"),
        "failed": sum(cell["status"] == "failed" for cell in cells),
        "other_status": sum(cell["status"] not in ("completed", "failed")
                            for cell in cells),
        "unprocessed": CELLS-len(cells),
    }
    if all_done:
        lower = min(F(cell["comparison"]["whole_cell_margin_lower_exact"])
                    for cell in completed)
        upper = max(F(cell["comparison"]["whole_cell_margin_upper_exact"])
                    for cell in completed)
        summary["harmonic_whole_disk_margin_enclosure_exact"] = [str(lower), str(upper)]
    else:
        summary["harmonic_whole_disk_margin_enclosure_exact"] = None
    return summary


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    manifest_hash = sha(args.manifest)
    manifest = json.loads(args.manifest.read_text())
    if not (
        manifest.get("root_reviewed") is True
        and manifest.get("peer_reviewed") is True
        and manifest.get("execution_authorized") is True
    ):
        raise PermissionError("unreviewed or unauthorized frozen manifest; no evaluation")
    for key, value in settings().items():
        if manifest.get(key) != value:
            raise AssertionError(("changed fixed setting", key))
    inventory = [
        {
            "id": f'{circle["label"]}:{index:03d}',
            "circle": circle["label"], "index": index,
            "theta_start_pi": str(F(2*index, CELLS)),
            "theta_end_pi": str(F(2*(index+1), CELLS)),
            "theta_midpoint_pi": str(F(2*index+1, CELLS)),
        }
        for circle in CIRCLES for index in range(CELLS)
    ]
    result = {
        "status": "failed", "validity": "not_yet_verified",
        "verdict": "inconclusive", **settings(),
        "manifest_sha256": manifest_hash,
        "claimed_files_sha256": manifest.get("files_sha256", {}),
        "inventory": inventory, "cells": [],
        "unprocessed_inventory": [item["id"] for item in inventory],
        "operation_counts": COUNTS,
        "scope": (
            "Original cap-343 ordinary half-chain on full reduced external disks. "
            "Only single-sign complete-circle results classify a whole disk. "
            "Individual half-chain parameters do not identify actual knots."
        ),
    }
    bindings = None
    with OUTPUT.open("x") as output:
        try:
            bindings, primary_inventory = verify_inputs(manifest)
            result["files_sha256"] = bindings
            result["primary_provenance"] = primary_inventory
            result["validity"] = "initial_provenance_verified"
            ctx.prec = PRECISION
            PI, II = arb.pi(), acb(0, 1)
            COUNTS["threshold_evaluations"] += 1
            threshold = ar("10/7").log()/(2*PI)
            result["harmonic_threshold"] = real_ball(threshold)
            position = 0
            for circle in CIRCLES:
                for index in range(CELLS):
                    cell = {
                        **inventory[position],
                        "status": "failed", "verdict": "inconclusive",
                        "proposal_history": [], "checks": [], "inclusions": {},
                    }
                    result["cells"].append(cell)
                    try:
                        run_cell(circle, index, cell, threshold)
                    except Exception as error:
                        cell["error"] = {
                            "type": type(error).__name__, "message": str(error),
                            "traceback": traceback.format_exc(),
                        }
                    finally:
                        position += 1
                        result["unprocessed_inventory"] = [
                            item["id"] for item in inventory[position:]
                        ]
                    print(cell["id"], cell["status"], cell["verdict"], flush=True)
            result["status"] = "completed"
            result["disk_results"] = [disk_summary(result, circle) for circle in CIRCLES]
            result["verdict"] = "per_disk_results_recorded"
        except BaseException as error:
            result["error"] = {
                "type": type(error).__name__, "message": str(error),
                "traceback": traceback.format_exc(),
            }
        finally:
            try:
                final_hash = sha(args.manifest)
                result["final_manifest_sha256"] = final_hash
                if final_hash != manifest_hash:
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
                result["verdict"] = "no_mathematical_conclusion"
                result["final_validation_error"] = {
                    "type": type(error).__name__, "message": str(error),
                    "traceback": traceback.format_exc(),
                }
            if result["validity"] != "provenance_verified":
                result["verdict"] = "no_mathematical_conclusion"
            json.dump(result, output, indent=2, sort_keys=True)
            output.write("\n")
            output.flush()


if __name__ == "__main__":
    main()
