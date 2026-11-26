#!/usr/bin/env python3
"""UNRUN: harmonic attachment excess from the frozen cap-343 cover.

No new seven-root or M3 solves, Newton steps, inverses, old-checker
imports, adaptive alternatives, retries, or output replacement.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import traceback

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_cap_343_harmonic_excess_protocol.md"
SCRIPT = "experiments/check_mixed_cap_343_harmonic_excess.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-cap-343-harmonic-excess.json"
OUTPUT = ROOT / "repro/results/research-mixed-cap-343-harmonic-excess-attempt01.json"
OLD_RESULT = "repro/results/research-mixed-cap-343-radius-coverage-attempt01.json"
OLD_MANIFEST = "repro/protocols/research-mixed-cap-343-radius-coverage.json"
OLD_PROTOCOL = "notes/research_mixed_cap_343_radius_coverage_protocol.md"
OLD_SCRIPT = "experiments/check_mixed_cap_343_radius_coverage.py"
M3_RESULT = "repro/results/research-internal-degree-two-contours.json"
M3_SCRIPT = "experiments/certify_internal_degree_two_contours.py"
M3_ENGINE = "experiments/certify_terminal_three_central_phase.py"
M3_INTERVAL = "[1.870362816119209077476382263 +/- 4.06e-28]"
PINNED = {
    OLD_RESULT: "1edec732c28ac64dd11ca63026722e8062a0598aa49b15ea2f2887a7dcbdb3d5",
    OLD_MANIFEST: "45091a7e3284acbcf4d8adf03267ef505f378d8a019f3a867aba7ca77255fb25",
    OLD_PROTOCOL: "971fb50a335c9ad3588ef431e09ee0ccd204e6ef95c4b14b23695b96dbe070ae",
    OLD_SCRIPT: "ce4942685353371270917272a5d069e230df2597df5207ae5d52c11117c27084",
    M3_RESULT: "22a4af3e274339b54fd2f4eaf475c22edf84858b9368b930bb1df615a5bafe11",
    M3_SCRIPT: "5f9d19c803f0763b448063055ec33852dfb29559031a620b45d97bc720fb30c1",
    M3_ENGINE: "a89cf8c782c1c782a644cfb59e6586a9a07db36c82653e65363d6b74cea0bef0",
    "notes/research_mixed_next_attachment_excess_harmonic_disks.md":
        "623ebfda0574d46a7e10e851d27a9fd48a8910543691a58a8d819a882878be47",
    "notes/research_internal_degree_two_contour_certificates.md":
        "954ff66b16b74aaa24a107cd2184a774ec7a0f97acf7d58d8f8aabd1a58288ec",
    "notes/research_all_nonzero_degree_two_fillings.md":
        "7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c",
    "notes/research_terminal_three_central_phase.md":
        "2dc766a10884bd60c477610cc596bfeefcb6e3742fc87203f0c241d62870da47",
    "notes/research_mixed_cap_343_saved_height_protocol.md":
        "fd2117a883a3c8dfc54e1141bc3ca866b85351d0326a24308165eccd8c7653d0",
    "experiments/check_mixed_cap_343_saved_height_comparisons.py":
        "521095d1d3b428c61777627f58b386c2a895b72ff37dc725b8e344821b67dfb8",
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
    "notes/research_mixed_global_cotangent_roots.md",
    "notes/research_mixed_next_outer_selected_outgoing_sheet.md",
    "notes/research_mixed_next_outgoing_absolute_anchor.md",
    "notes/research_mixed_next_outgoing_action_terminal_normalization.md",
    "notes/research_mixed_cap_343_correlated_height_bounds.md",
    "notes/research_mixed_geometric_action_calibration.md",
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
COMPARISONS = ["excess"]
FORMULAS = {"excess": "M3+Re(S_half(z)-Pi(e,a,u,p,y,s,z))"}
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
    "M3_saved_interval_decodes": 0, "comparisons_attempted": 0,
    "comparisons_completed": 0,
    "new_seven_root_solves": 0, "new_M3_root_solves": 0,
    "explicit_half_root_evaluations": 0,
    "newton_steps": 0, "proposal_iterations": 0,
    "equation_calls": 0, "new_root_inclusion_tests": 0,
    "point_matrix_inversions": 0, "wide_interval_matrix_inversions": 0,
    "action_evaluations": 0, "dilogarithm_evaluations": 0,
    "primitive_evaluations": 0, "primitive_derivative_evaluations": 0,
    "M3_action_evaluations": 0,
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
        "comparison_formulas": FORMULAS, "sign_threshold": "0",
        "point_radius": POINT_RADIUS, "parameter_radius": CELL_RADIUS,
        "saved_result": OLD_RESULT, "saved_manifest": OLD_MANIFEST,
        "response_method": "Neumann_row6_times_exact_Delta_z",
        "M3_record": M3_RESULT, "M3_degree": 2, "M3_power": 3,
        "M3_saved_selected_rate": M3_INTERVAL,
        "M3_method": "literal_saved_decimal_midpoint_radius_interval",
        "half_root_method": "principal_sqrt_right_cotangent_then_upper_T_log",
        "comparison_method": "midpoint_plus_fixed_angular_response_debit",
        "direct_whole_cell_action": "audit_only_no_intersection",
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


def verify_m3_metadata(document):
    fixed = {
        "scope": "Certified scaled limiting-phase inequalities; finite-source assembly is separate.",
        "precision_bits": 180, "degree": 2,
        "script_sha256": PINNED[M3_SCRIPT],
        "engine_sha256": PINNED[M3_ENGINE],
        "wire_interval": ["1/32", "15/32"],
        "angular_interval_over_2pi": ["-1/3", "1/3"],
        "lower_wire_penalty_multiplier": 2,
    }
    for key, value in fixed.items():
        if document.get(key) != value:
            raise AssertionError(("M3 source metadata mismatch", key))
    powers = document["powers"]
    if [entry["power"] for entry in powers] != list(range(3, 32)):
        raise AssertionError("M3 complete power inventory mismatch")
    surfaces = [("central", None), ("negative", None), ("lower", None)]
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            surfaces.append((prefix+sign, None))
    for endpoint in ("1/32", "15/32"):
        for side in ("upper", "lower"):
            surfaces.append(("bottom_endpoint_"+side, endpoint))
            for sign in ("positive", "negative"):
                surfaces.append(("nested_"+side+"_"+sign, endpoint))
    for entry in powers:
        root = entry["root"]
        if (entry["degree"] != 2 or root["variable"] != "r=exp(i*t/4)"
                or root["Rouche_disk_radius"] != "2^-100"
                or len(root["logarithmic_gradient_enclosures"]) != 2
                or [(s["surface"], s["endpoint"]) for s in entry["surfaces"]] != surfaces):
            raise AssertionError(("M3 certificate inventory mismatch", entry["power"]))
    selected = powers[0]
    if selected["selected_rate"] != M3_INTERVAL:
        raise AssertionError("M3 literal interval changed")
    if selected["root"]["polynomial_coefficients"] != [
            "-1", "0", "0", "-2", "-1", "0", "-1", "2", "0", "0", "-1"]:
        raise AssertionError("M3 selected polynomial convention mismatch")
    return {
        "record": M3_RESULT, "degree": 2, "power": 3,
        "selected_rate_literal": M3_INTERVAL,
        "complete_power_inventory_verified": list(range(3, 32)),
        "surface_inventory_per_power_verified": 19,
        "root_or_rate_recomputed": False,
    }


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
    m3_document = json.loads(safe_relative(M3_RESULT).read_text())
    m3_audit = verify_m3_metadata(m3_document)
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
        if path == M3_RESULT:
            for field, child in (("script_sha256", M3_SCRIPT),
                                 ("engine_sha256", M3_ENGINE)):
                digest = data[field]
                if expected.get(child) != digest or observed.get(child) != digest:
                    raise AssertionError(("unbound M3 scalar dependency", field, child))
                edges.append({"record": path, "field": field,
                              "dependency": child, "sha256": digest})
    inherit(OLD_RESULT)
    inherit(OLD_MANIFEST)
    inherit(M3_RESULT)
    edge_key = lambda item: (item["record"], item["field"], item["dependency"], item["sha256"])
    if sorted(edges, key=edge_key) != sorted(manifest["transitive_dependency_edges"], key=edge_key):
        raise AssertionError("transitive dependency edge inventory mismatch")
    return observed, old, {
        "old_result": OLD_RESULT, "old_manifest": OLD_MANIFEST,
        "saved_cells_verified": 1024, "saved_checks_per_cell": 64,
        "inherited_files": len(inherited), "transitive_records": sorted(visited),
        "transitive_edge_count": len(edges),
        "old_primary_provenance": old["primary_provenance"],
        "M3_metadata_audit": m3_audit,
    }


def ar(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def decode_m3_interval():
    COUNTS["M3_saved_interval_decodes"] += 1
    pattern = r"\[([+-]?[0-9]+(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?) \+/- ([0-9]+(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?)\]"
    match = re.fullmatch(pattern, M3_INTERVAL)
    if match is None:
        raise AssertionError("unsupported frozen M3 interval syntax")
    midpoint, radius = F(match.group(1)), F(match.group(2))
    if radius <= 0:
        raise AssertionError("nonpositive saved M3 radius")
    value = ar(midpoint)+arb(0, ar(radius).upper())
    if not value.is_finite():
        raise AssertionError("nonfinite decoded M3 interval")
    return value, {
        "literal": M3_INTERVAL, "midpoint_exact": str(midpoint),
        "radius_exact": str(radius), "outward_ball": real_ball(value),
        "original_lower_exact": str(midpoint-radius),
        "original_upper_exact": str(midpoint+radius),
    }


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


def off_log_cut(value):
    return value.real > 0 or value.imag > 0 or value.imag < 0


def g(value, record, label):
    COUNTS["primitive_evaluations"] += 1
    value = acb(value)
    require(record, label+": original primitive strip", 0 < value.real < 1)
    argument = (-2*PI*II*value).exp()
    require(record, label+": principal dilogarithm cut avoided",
            argument.real < 1 or argument.imag > 0 or argument.imag < 0)
    COUNTS["dilogarithm_evaluations"] += 1
    answer = (argument.polylog(2)-PI**2/6)/(2*PI*II)
    require(record, label+": finite original primitive", finite(answer))
    return answer


def gp(value, record, label):
    COUNTS["primitive_derivative_evaluations"] += 1
    value = acb(value)
    require(record, label+": derivative primitive strip", 0 < value.real < 1)
    argument = 1-(-2*PI*II*value).exp()
    require(record, label+": principal derivative log cut avoided", off_log_cut(argument))
    answer = argument.log()
    require(record, label+": finite original primitive derivative", finite(answer))
    return answer


def J(value, record, label):
    return g(value, record, label)-II*PI*(value-value**2)/2


def vertex(beta, left, right, record, label):
    answer = g(left+right, record, label+": sum")
    if beta == 1:
        answer -= g(left, record, label+": left")+g(right, record, label+": right")
    elif beta != 0:
        raise AssertionError("unsupported fixed vertex type")
    return answer


def gram(left, right, record, label):
    return (g(left+right, record, label+": sum")
            -2*g(left, record, label+": left")
            -2*g(right, record, label+": right")+2*PI*II*left*right)


def half_root(z, record, label):
    COUNTS["explicit_half_root_evaluations"] += 1
    saved = {"output": complex_ball(z)}
    record.setdefault("half_roots", {})[label] = saved
    require(record, label+": half-input output strip", finite(z) and 0 < z.real < ar("1/2"))
    cotangent = (PI*z).cot()
    saved["Q"] = complex_ball(cotangent)
    require(record, label+": right cotangent half-plane",
            finite(cotangent) and cotangent.real > 0)
    discriminant = cotangent**2+4-4*II*cotangent
    saved["discriminant"] = complex_ball(discriminant)
    require(record, label+": principal square-root cut avoided",
            finite(discriminant) and off_log_cut(discriminant))
    radical = discriminant.sqrt()
    selected = (-cotangent+radical)/2
    saved["principal_square_root"] = complex_ball(radical)
    saved["S"] = complex_ball(selected)
    require(record, label+": selected right half-root",
            finite(radical) and finite(selected) and selected.real > 0)
    require(record, label+": reciprocal denominator nonzero", abs(selected-II) > 0)
    reciprocal = (selected+II)/(selected-II)
    saved["T"] = complex_ball(reciprocal)
    require(record, label+": selected reciprocal upper half-plane",
            finite(reciprocal) and reciprocal.imag > 0)
    index = reciprocal.log()/(2*PI*II)
    saved["index"] = complex_ball(index)
    require(record, label+": selected index in original half strip",
            finite(index) and 0 < index.real < ar("1/2"))
    require(record, label+": all half-action primitive strips",
            all(0 < value.real < 1 for value in (index, ar("1/2")+index, z, z+index)))
    return index


def actions(box, index, record, label):
    e, a, u, p, y, s, z = box
    COUNTS["action_evaluations"] += 2
    cap = (-2*J(ar("1/2")-u, record, label+": cap half-u")
           -3*J(u, record, label+": cap u")-J(e-u, record, label+": cap e-u")
           +II*PI*e*u-II*PI*(e-e**2)/2)
    prefix = (cap+vertex(0, e, a, record, label+": vertex e,a")
              +gram(a, p, record, label+": Gram a,p")
              +vertex(1, p, y, record, label+": vertex p,y")
              +gram(y, s, record, label+": Gram y,s")
              +vertex(0, s, z, record, label+": vertex s,z")
              -g(z, record, label+": final normalization"))
    half = (g(ar("1/2")+index, record, label+": half incoming")
            +g(z+index, record, label+": half outgoing")
            -2*g(index, record, label+": half own")
            -g(ar("1/2"), record, label+": half input constant")
            -g(z, record, label+": half output constant")+PI*II*index)
    difference = half-prefix
    require(record, label+": finite original actions",
            finite(cap) and finite(prefix) and finite(half) and finite(difference))
    record.setdefault("actions", {})[label] = {
        "cap": complex_ball(cap), "Pi": complex_ball(prefix),
        "S_half": complex_ball(half), "Delta": complex_ball(difference),
    }
    return difference


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
    k_rows = [upper(value) for value in rows]
    k = max(k_rows)
    ma = max(upper(abs(matrix[j, 6])) for j in range(7))
    cell["jacobian_error"] = [
        [complex_ball(error[i, j]) for j in range(7)] for i in range(7)
    ]
    cell["neumann_bounds"] = {
        "row_norms": [real_ball(value) for value in rows],
        "row_upper_exact": [str(value) for value in k_rows],
        "maximum_row_upper_exact": str(k),
        "column6_maximum_upper_exact": str(ma),
    }
    require(cell, "uniform Neumann maximum row bound below one", k < 1)
    denominator = 1-(-2*PI*II*(uniform[6]+outside)).exp()
    require(cell, "original external derivative denominator nonzero",
            abs(denominator) > 0)
    gamma = 2*PI*II/denominator
    COUNTS["response_evaluations"] += 1
    common_radius = abs(gamma)*ar(ma)/(1-ar(k))
    center = -gamma*matrix[6, 6]
    radius = common_radius*ar(k_rows[6])
    cell["external_mixed_derivative"] = complex_ball(gamma)
    require(cell, "finite row-six response", finite(center) and radius.is_finite())
    return point, uniform, center, radius, b_theta, rho, omega


def compare(name, record, data, m3):
    COUNTS["comparisons_attempted"] += 1
    if name != "excess":
        raise AssertionError("unrecognized fixed comparison")
    point, uniform, center, radius, b_theta, rho, omega = data
    point_index = half_root(point[6], record, "midpoint")
    uniform_index = half_root(uniform[6], record, "whole_cell")
    midpoint = m3+actions(point, point_index, record, "midpoint").real
    direct = m3+actions(uniform, uniform_index, record, "whole_cell").real
    delta_z = (gp(uniform[6]+uniform_index, record, "Delta derivative half outgoing")
               -gp(uniform[6]+uniform[5], record, "Delta derivative prefix outgoing"))
    angular_center = (delta_z*center*b_theta).real
    angular_error = rho*abs(delta_z)*radius
    derivative = angular_center+arb(0, angular_error.upper())
    require(record, "finite derivative and midpoint/direct margins",
            derivative.is_finite() and midpoint.is_finite() and direct.is_finite())
    derivative_upper = upper(abs(derivative))
    debit = omega*ar(derivative_upper)
    whole = midpoint+arb(0, debit.upper())
    require(record, "finite transported whole-cell margin", whole.is_finite())
    record.update({
        "saved_M3_interval": real_ball(m3), "Delta_z": complex_ball(delta_z),
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
        "scope": "Harmonic attachment excess on both full ordinary cap343 disks; no finite-source or cancellation conclusion.",
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
            m3, m3_record = decode_m3_interval()
            result["saved_M3_interval"] = m3_record
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
                            compare(name, record, data, m3)
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
