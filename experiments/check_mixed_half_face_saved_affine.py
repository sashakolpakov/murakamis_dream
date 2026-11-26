#!/usr/bin/env python3
"""One fixed saved-only affine comparison. UNRUN until independently approved."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import traceback

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_half_face_saved_affine_protocol.md"
PROTOCOL_SHA256 = "4e69ba62e3e1346d25aca7a00e19bd4b5bdc5fcb88972851182a33a97031938d"
SCRIPT = "experiments/check_mixed_half_face_saved_affine.py"
GUIDE = "notes/research_mixed_half_face_saved_affine_manifest_instructions.md"
MANIFEST = ROOT / "repro/protocols/research-mixed-half-face-saved-affine.json"
OUTPUT = ROOT / "repro/results/research-mixed-half-face-saved-affine-attempt01.json"
BOUNDARY = "repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json"
BOUNDARY_MANIFEST = "repro/protocols/research-mixed-three-four-following-boundary-cover.json"
RESPONSE = "repro/results/research-mixed-three-four-following-saved-response-attempt01.json"
RESPONSE_MANIFEST = "repro/protocols/research-mixed-three-four-following-saved-response.json"
PINNED = {
    PROTOCOL: PROTOCOL_SHA256,
    BOUNDARY: "e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b",
    BOUNDARY_MANIFEST: "d7e9e6a096e4ce5dc77858691a90b257f842a42910603f74f3d15a6e20a46405",
    RESPONSE: "5bc3e5ff76ab5371e76bddb8d8fc32512ef16d9571d1991fb0c5f57dd39867c3",
    RESPONSE_MANIFEST: "84fe02e65cb17575f5016e8d70e67c261b93ea4a65d9992c99f9ccd9cfb92859",
    "notes/research_mixed_half_face_cap_action_upper.md": "c0cd423c0119e3086f8897836aac37c9e018e427aa4d5eacb320d6bef438060f",
    "notes/research_mixed_half_face_scalar_envelope_obstruction.md": "ca50dcc82834d760ae60ded4e7db070f6020d574ce6d7f8afec0c65a2011218f",
    "notes/research_mixed_half_face_joint_source_packet.md": "16ee5063f5ca6c745ecb5fdd9aef4409ee7d83c8745f372461bdbef125e7083b",
    "notes/research_mixed_half_face_complete_cap_packet.md": "d9d893da266c8aea4451559eb12cb791e3fda8295e721f9a4393d2fe79d6b054",
    "notes/research_mixed_half_face_complete_conditional_packet.md": "e0e5a1d9ad747075d63f9e7d367dc5755f75b943137ed7dea3b3143ecaa03747",
    "repro/results/research-mixed-cap-seam-source-bounds-replay.json": "8d907c890073955f7e1122abc78f1334ab00a885959d839316d3852e2a64f3f8",
}
CIRCLES = [
    {"label": "c3", "center": ["7/20", "-1/100"], "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "c4", "center": ["3/10", "-13/250"], "radius": "3/50", "typed_radius": "8/125"},
]
CELLS_PER_CIRCLE = 512
POINT_RADIUS = "1/1073741824"
CELL_RADIUS = "1/256"
TESTS = [
    {"label": "factorial_left", "alternative": "factorial", "x": "11/50"},
    {"label": "factorial_right", "alternative": "factorial", "x": "9/20"},
    {"label": "forcing_left", "alternative": "forcing", "x": "11/50"},
    {"label": "forcing_right", "alternative": "forcing", "x": "9/20"},
]
REQUIRED = {
    PROTOCOL, SCRIPT, GUIDE, BOUNDARY, BOUNDARY_MANIFEST, RESPONSE, RESPONSE_MANIFEST,
    "notes/research_mixed_half_face_scalar_envelope_obstruction.md",
    "notes/research_mixed_half_face_cap_action_upper.md",
    "notes/research_mixed_half_face_complete_cap_packet.md",
    "notes/research_mixed_half_face_complete_conditional_packet.md",
    "notes/research_mixed_half_face_joint_source_packet.md",
    "notes/research_mixed_endpoint_seam_majorants.md",
    "notes/research_mixed_next_allocated_action_floor.md",
    "notes/research_mixed_next_filtered_selected_plateau.md",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_three_four_following_critical_curve.md",
    "notes/research_mixed_three_four_following_remainder_gaps.md",
    "notes/research_mixed_three_four_following_boundary_diagnostic_protocol.md",
    "experiments/check_mixed_three_four_following_boundary_cover.py",
    "notes/research_mixed_three_four_following_saved_response_protocol.md",
    "experiments/check_mixed_three_four_following_saved_response.py",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_alternating_cap_phase_entrance.md",
    "notes/research_mixed_open_word_hessian.md",
    "repro/results/research-mixed-cap-seam-source-bounds-replay.json",
}
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
DEPENDENCY_FIELDS = (
    "dependencies", "dependencies_sha256", "primary_records",
    "primary_records_sha256", "saved_replays", "saved_replays_sha256", "files_sha256",
)
COUNTS = dict(
    decoded_real_intervals=0, two_coordinate_response_enclosures=0,
    product_bounds=0, angular_derivative_enclosures=0, midpoint_proxies=0,
    final_comparisons=0, new_roots=0, new_inclusions=0, new_hessians=0,
    new_matrix_inverses=0, new_actions=0, new_dilogarithms=0,
    source_replays=0, retries=0, subdivisions=0,
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def cp(pair):
    return acb(ar(pair[0]), ar(pair[1]))


def real_ball(value):
    return dict(ball=str(value), lower=str(value.lower()), upper=str(value.upper()))


def complex_ball(value):
    return dict(real=real_ball(value.real), imag=real_ball(value.imag))


def decode_real(record):
    """Union of full outward endpoint displays, including printed radii."""
    COUNTS["decoded_real_intervals"] += 1
    assert isinstance(record["lower"], str) and isinstance(record["upper"], str)
    left, right = arb(record["lower"]), arb(record["upper"])
    assert left.is_finite() and right.is_finite(), "nonfinite saved endpoint"
    assert left.lower() <= right.upper(), "reversed saved endpoints"
    return left.union(right)


def decode_complex(record):
    return acb(decode_real(record["real"]), decode_real(record["imag"]))


def exact_upper(value):
    assert value.is_finite(), "nonfinite upper endpoint"
    return F(str(value.upper().fmpq()))


def exact_lower(value):
    assert value.is_finite(), "nonfinite lower endpoint"
    return F(str(value.lower().fmpq()))


def finite_complex(value):
    return value.real.is_finite() and value.imag.is_finite()


def check(cell, name, condition):
    cell["checks"].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def fixed_inventory():
    return [
        dict(id=f'{circle["label"]}:{index:03d}', circle=circle["label"], index=index,
             theta_start_pi=str(F(2 * index, CELLS_PER_CIRCLE)),
             theta_end_pi=str(F(2 * (index + 1), CELLS_PER_CIRCLE)),
             theta_midpoint_pi=str(F(2 * index + 1, CELLS_PER_CIRCLE)))
        for circle in CIRCLES for index in range(CELLS_PER_CIRCLE)
    ]


def verify_inputs(manifest):
    expected = manifest["files_sha256"]
    required = set(REQUIRED)
    for row in PRIMARY:
        required.update(row)
    assert required <= expected.keys(), ("missing mandatory source bindings", sorted(required - expected.keys()))
    for path, digest in PINNED.items():
        assert expected.get(path) == digest, ("incorrect pinned input", path)
    for path, digest in expected.items():
        assert sha(ROOT / path) == digest, ("changed frozen input", path)
    visited, edges = set(), []

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        data = json.loads((ROOT / path).read_text())
        for field in DEPENDENCY_FIELDS:
            deps = data.get(field, {})
            if not isinstance(deps, dict):
                continue
            for child, digest in deps.items():
                assert expected.get(child) == digest, ("unbound dependency", path, child)
                assert sha(ROOT / child) == digest, ("changed dependency", child)
                edges.append(dict(parent=path, field=field, child=child, sha256=digest))
                if child.startswith(("repro/results/", "repro/protocols/")) and child.endswith(".json"):
                    inherit(child)

    for author_path, replay_path, proof_path, author_script, replay_script in PRIMARY:
        author = json.loads((ROOT / author_path).read_text())
        replay = json.loads((ROOT / replay_path).read_text())
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
            assert [(v["epsilon"], v["witness"]) for v in author["one_vertex"]] == [
                (v["epsilon"], v["witness"]) for v in replay["one_vertex"]]
        else:
            assert len(author["cases"]) == len(replay["cases"]) == 6
            for a_case, r_case in zip(author["cases"], replay["cases"]):
                assert a_case["types"] == r_case["types"]
                assert len(a_case["accepted"]) == r_case["original_boxes"]
                assert r_case["replay_boxes"] == r_case["original_boxes"]
                assert r_case["refinements"] == 0
        inherit(author_path)
        inherit(replay_path)
    for path in sorted(expected):
        if path.startswith(("repro/results/", "repro/protocols/")) and path.endswith(".json"):
            inherit(path)
    return expected, dict(files=len(expected), records=sorted(visited), edges=edges)


def boundary_check_names():
    names = ["full parameter enclosure in original typed disk", "rational inverse invertible"]
    for tag in ("midpoint", "whole_cell"):
        guards = ["original private chamber", "original auxiliary chamber"]
        guards.extend(label + ": original Q chamber" for label in ("a", "t", "z"))
        guards.append("original a typed disk")
        for label in ("t", "z"):
            guards.extend(label + ": " + suffix for suffix in
                          ("original typed disk", "original reduced output disk", "original negative output height"))
        guards.extend(["all original primitive arguments regular",
                       "original auxiliary sine and cosine branches", "outgoing radius in original range"])
        names.extend(tag + ": " + name for name in guards)
        for index in range(5):
            names.extend([f"{tag} row {index}: contraction",
                          f"{tag} row {index}: strict complex-disk inclusion"])
    names.append("finite original midpoint action values")
    return names


def response_check_names():
    names = ["saved inventory " + key for key in
             ("id", "circle", "index", "theta_start_pi", "theta_end_pi", "theta_midpoint_pi")]
    names.extend([
        "original failed status preserved", "only the prescribed interval-inverse failure",
        "all original checks present and passed", "original proposal inventory retained",
        "no old comparison or derivative enclosure promoted",
        "both complete original inclusion inventories", "original operation counts",
    ])
    for tag in ("midpoint", "whole_cell"):
        names.append(tag + ": original fixed radius")
        for index in range(5):
            names.extend([f"{tag} row {index}: decoded contraction",
                          f"{tag} row {index}: decoded strict inclusion"])
    names.extend([
        "decoded original derivative logarithm strips", "decoded original mixed derivative strip",
        "complete exact rational inverse", "positive finite saved inverse column bound",
        "positive decoded angular halfwidth", "original mixed derivative denominator nonzero",
        "decoded uniform outgoing radius", "finite saved-response enclosure",
        "decoded midpoint radius and beta domain",
        "real_initial: finite transported margin", "complete_complement: finite transported margin",
    ])
    return names


def verify_banks():
    boundary = json.loads((ROOT / BOUNDARY).read_text())
    response = json.loads((ROOT / RESPONSE).read_text())
    ids = [v["id"] for v in fixed_inventory()]
    for bank, manifest_path in ((boundary, BOUNDARY_MANIFEST), (response, RESPONSE_MANIFEST)):
        inherited = json.loads((ROOT / manifest_path).read_text())
        assert inherited["root_reviewed"] is True and inherited["peer_reviewed"] is True
        assert bank["manifest_sha256"] == PINNED[manifest_path]
        assert bank["files_sha256"] == bank["claimed_files_sha256"] == inherited["files_sha256"]
        assert not any(bank.get(key) for key in ("error", "changed_inputs", "manifest_changed"))
        assert bank["precision_bits"] == 256 and bank["circles"] == CIRCLES
        assert bank["cells_per_circle"] == CELLS_PER_CIRCLE
        assert bank["inventory"] == fixed_inventory() and len(bank["cells"]) == 1024
        assert [v["id"] for v in bank["cells"]] == ids and bank["unprocessed_inventory"] == []
        assert bank["retries"] == 0
    assert boundary["status"] == "failed" and boundary["verdict"] == "inconclusive"
    assert boundary["proposal_iterations_per_cell"] == 24
    assert boundary["point_radius"] == POINT_RADIUS and boundary["parameter_radius"] == CELL_RADIUS
    assert boundary["adaptive_subdivisions"] == 0
    assert boundary["operation_counts"] == dict(
        equation_calls=26624, jacobian_calls=27648, dilogarithm_calls=12288,
        proposal_iterations=24576, point_inclusion_tests=1024, parameter_inclusion_tests=1024,
        action_evaluations=1024, comparison_evaluations=0, derivative_evaluations=1024)
    assert boundary["summary"] == dict(
        attempted_cells=1024, completed_cells=0, positive_cells=0,
        failed_cell_ids=ids, nonpositive_cell_ids=ids)
    assert response["status"] == "completed" and response["verdict"] == "both_full_disks_have_positive_margins"
    assert response["original_result"] == BOUNDARY
    assert response["original_result_sha256"] == PINNED[BOUNDARY]
    assert response["original_result_status"] == "failed" and response["refinements"] == 0
    assert response["summary"] == dict(
        attempted_cells=1024, completed_cells=1024, positive_cells=1024,
        failed_cell_ids=[], nonpositive_cell_ids=[])
    assert response["operation_counts"] == dict(
        decoded_real_intervals=48128, response_enclosures=1024, margin_comparisons=2048,
        new_roots=0, new_inclusions=0, new_hessians=0, new_matrix_inverses=0,
        new_actions=0, new_dilogarithms=0)
    return boundary, response


def verify_cell_sources(original, saved, cell):
    for key in ("id", "circle", "index", "theta_start_pi", "theta_end_pi", "theta_midpoint_pi"):
        check(cell, "both saved inventories " + key, original[key] == saved[key] == cell[key])
    check(cell, "original failed status preserved",
          original["status"] == "failed" and original["verdict"] == "inconclusive")
    check(cell, "only the original direct-inverse failure",
          original["error"] == "ZeroDivisionError: matrix is singular"
          and "inverse_cell = cell_jac.inv()" in original["traceback"])
    check(cell, "all original checks present and passed",
          [v["name"] for v in original["checks"]] == boundary_check_names()
          and all(v["passed"] is True for v in original["checks"]))
    check(cell, "full original proposal inventory",
          len(original["proposal_history"]) == 24
          and [v["iteration"] for v in original["proposal_history"]] == list(range(1, 25))
          and original["final_center"] == original["proposal_history"][-1]["centers"])
    check(cell, "original failure did not yield comparison data",
          original["comparisons"] == [] and "derivative_enclosures" not in original)
    check(cell, "original fixed operation inventory", original["operation_counts"] == dict(
        equation_calls=26, jacobian_calls=27, dilogarithm_calls=12, proposal_iterations=24,
        point_inclusion_tests=1, parameter_inclusion_tests=1, action_evaluations=1,
        comparison_evaluations=0, derivative_evaluations=1))
    check(cell, "saved response completed with both old margins",
          saved["status"] == "completed" and saved["verdict"] == "both_cell_margins_positive")
    check(cell, "all saved-response checks present and passed",
          [v["name"] for v in saved["checks"]] == response_check_names()
          and all(v["passed"] is True for v in saved["checks"]))
    check(cell, "both saved comparison inventories retained",
          [v["label"] for v in saved["comparisons"]] == ["real_initial", "complete_complement"]
          and all(v["verdict"] == v["midpoint_verdict"] == "positive" for v in saved["comparisons"]))
    check(cell, "saved response operation inventory", saved["operation_counts"] == dict(
        decoded_real_intervals=47, response_enclosures=1, margin_comparisons=2,
        new_roots=0, new_inclusions=0, new_hessians=0, new_matrix_inverses=0,
        new_actions=0, new_dilogarithms=0))
    check(cell, "both complete original inclusions",
          set(original["inclusions"]) == {"midpoint", "whole_cell"}
          and all(len(original["inclusions"][tag]["rows"]) == 5
                  and len(original["inclusions"][tag]["coordinate_boxes"]) == 5
                  for tag in ("midpoint", "whole_cell")))


def gp(value):
    """Original strip g-prime; no primitive or dilogarithm."""
    return (2 * (PI * value).sin()).log() + II * PI * (1 - 2 * value) / 2


def gpp(value):
    return PI * ((PI * value).cot() - II)


def scalar_cost(alternative, x):
    cap = ar("203/200") - ar("1303/7680000")
    catalan_upper = ar("73/500")
    if alternative == "factorial":
        return cap + ar("11/2") * catalan_upper + LOG2 * (x-ar("1/4")) / 4 + PI/400 + ar("7/250")
    assert alternative == "forcing"
    return cap + 5*catalan_upper + LOG2 * (x-ar("1/4")) / 2 + PI/100 + ar("7/250")


def prepare_cell(original, saved, cell):
    verify_cell_sources(original, saved, cell)
    cell["decoded_inclusions"] = {}
    decoded_rows = {}
    for tag, radius in (("midpoint", POINT_RADIUS), ("whole_cell", CELL_RADIUS)):
        inclusion = original["inclusions"][tag]
        check(cell, tag + ": fixed original radius", F(inclusion["radius"]) == F(radius))
        records, row_bounds = [], []
        for index, row in enumerate(inclusion["rows"]):
            derivative = decode_real(row["derivative_row"])
            image = decode_real(row["image_radius"])
            residual = decode_real(row["residual"])
            upper = exact_upper(derivative)
            check(cell, f"{tag} row {index}: decoded contraction", 0 <= upper < 1)
            check(cell, f"{tag} row {index}: decoded strict inclusion", exact_upper(image) < F(radius))
            row_bounds.append(upper)
            records.append(dict(derivative_row=real_ball(derivative), image_radius=real_ball(image),
                                residual=real_ball(residual), exact_row_upper=str(upper)))
        decoded_rows[tag] = row_bounds
        cell["decoded_inclusions"][tag] = records

    response = saved["response"]
    k_rows = list(map(F, response["row_upper_bounds"]))
    check(cell, "all five saved response row bounds",
          len(k_rows) == 5 and all(0 <= value < 1 for value in k_rows))
    check(cell, "same five original decoded row bounds",
          k_rows == decoded_rows["whole_cell"]
          and [str(v) for v in k_rows] == [
              v["exact_row_upper"] for v in saved["decoded_inclusions"]["whole_cell"]])
    k, m = F(response["k"]), F(response["m"])
    check(cell, "saved contraction maximum and final row agree",
          k == max(k_rows) and F(response["k_last"]) == k_rows[4])
    matrix = original["rational_inverse"]
    check(cell, "complete exact rational inverse inventory",
          len(matrix) == 5 and all(len(row) == 5 and all(len(v) == 2 for v in row) for row in matrix))
    column = [matrix[index][4] for index in range(5)]
    check(cell, "same original exact inverse column",
          column == response["exact_last_inverse_column"]
          and column[4] == response["exact_last_inverse_entry"])
    check(cell, "saved rational column norm bound",
          m > 0 and all(F(v[0])**2 + F(v[1])**2 <= m*m for v in column))

    boxes = [decode_complex(v) for v in original["inclusions"]["whole_cell"]["coordinate_boxes"]]
    point = [decode_complex(v) for v in original["inclusions"]["midpoint"]["coordinate_boxes"]]
    outside = decode_complex(original["external_cell"])
    s, q = boxes[3], boxes[4]
    sp, qp = point[3], point[4]
    for tag, sv, qv in (("whole_cell", s, q), ("midpoint", sp, qp)):
        check(cell, tag + ": original derivative strips",
              0 < sv.real < 1 and 0 < qv.real < ar("1/2") and 0 < (sv+qv).real < 1)
        check(cell, tag + ": negative outgoing height", qv.imag < 0)
    check(cell, "original external mixed strip", 0 < (q+outside).real < 1)
    gamma = decode_complex(response["gamma"])
    q0 = decode_complex(response["center"])
    rq_display = decode_real(response["error_radius"])
    rq = exact_upper(rq_display)
    check(cell, "saved finite final-row response",
          finite_complex(gamma) and finite_complex(q0) and rq >= 0)
    s0 = -gamma * cp(column[3])
    rs_ball = abs(gamma) * ar(k_rows[3]) * ar(m) / (1-ar(k))
    rs = exact_upper(rs_ball)
    check(cell, "finite penultimate-row response", finite_complex(s0) and rs >= 0)
    COUNTS["two_coordinate_response_enclosures"] += 1

    h = gp(s+q) - ar("3/2")*gp(q)
    g1 = gpp(s+q)
    g2 = g1-ar("3/2")*gpp(q)
    h0prime = g1*s0+g2*q0
    rh_ball = abs(g1)*ar(rs)+abs(g2)*ar(rq)
    rh = exact_upper(rh_ball)
    product = abs(h0prime*q0)+abs(h0prime)*ar(rq)+abs(q0)*ar(rh)+ar(rh)*ar(rq)
    product_upper = exact_upper(product)
    check(cell, "finite holomorphic product bound",
          all(finite_complex(v) for v in (h, g1, g2, h0prime))
          and rh >= 0 and product_upper >= 0)
    COUNTS["product_bounds"] += 1
    ctheta = decode_complex(response["parameter_angular_derivative"])
    halfwidth = decode_real(original["theta_halfwidth"])
    omega = exact_upper(halfwidth)
    check(cell, "finite saved circle derivative and positive halfwidth",
          finite_complex(ctheta) and halfwidth > 0 and omega > 0)
    cell["decoded_whole_box"] = [complex_ball(v) for v in boxes]
    cell["decoded_midpoint_box"] = [complex_ball(v) for v in point]
    cell["decoded_external_cell"] = complex_ball(outside)
    cell["responses"] = dict(
        row_upper_bounds=[str(v) for v in k_rows], k=str(k), m=str(m),
        exact_last_inverse_column=column, gamma=complex_ball(gamma),
        q_center=complex_ball(q0), q_error=real_ball(rq_display), q_error_upper=str(rq),
        s_center=complex_ball(s0), s_error=real_ball(rs_ball), s_error_upper=str(rs),
        h=complex_ball(h), G1=complex_ball(g1), G2=complex_ball(g2),
        hprime_center=complex_ball(h0prime), hprime_error=real_ball(rh_ball),
        hprime_error_upper=str(rh), angular_derivative=complex_ball(ctheta),
        halfwidth=real_ball(halfwidth), exact_halfwidth_upper=str(omega))
    cell["product_bound"] = dict(enclosure=real_ball(product), exact_upper=str(product_upper))

    angular = {}
    for x_text in ("11/50", "9/20"):
        x = ar(x_text)
        cq = -II*h.imag-(x-q.real)*g2
        cs = -(x-q.real)*g1
        central = ((cq*q0+cs*s0)*ctheta).real
        error_ball = abs(ctheta)*(abs(cq)*ar(rq)+abs(cs)*ar(rs))
        error_upper = exact_upper(error_ball)
        derivative = central+arb(0, ar(error_upper).upper())
        derivative_upper = exact_upper(abs(derivative))
        debit = omega*derivative_upper
        check(cell, x_text + ": finite signed deficit derivative",
              central.is_finite() and derivative.is_finite()
              and error_upper >= 0 and derivative_upper >= 0)
        COUNTS["angular_derivative_enclosures"] += 1
        angular[x_text] = dict(
            Cq=complex_ball(cq), Cs=complex_ball(cs),
            central_real_derivative=real_ball(central), disk_error=real_ball(error_ball),
            exact_disk_error_upper=str(error_upper), derivative=real_ball(derivative),
            exact_absolute_upper=str(derivative_upper), exact_transport_debit=str(debit))
    cell["angular_transport"] = angular

    bare = decode_complex(original["bare_prefix_action_midpoint"])
    hm = gp(sp+qp)-ar("3/2")*gp(qp)
    radius = (2*PI*qp.imag).exp()
    nu_lower = (2*PI*qp.real).sin()*(1+radius).log()/(4*PI)
    check(cell, "finite original midpoint action and elementary lower halfweight",
          finite_complex(bare) and finite_complex(hm)
          and 0 < radius < 1 and nu_lower > 0)
    cell["midpoint"] = dict(
        saved_bare_action=complex_ball(bare), h=complex_ball(hm),
        outgoing_radius=real_ball(radius), elementary_nu_half_lower=real_ball(nu_lower))
    for comparison in cell["comparisons"]:
        x = ar(comparison["x"])
        cost = scalar_cost(comparison["alternative"], x)
        proxy = bare.real+nu_lower+hm.real*(x-qp.real)-cost
        check(cell, comparison["label"] + ": finite conservative midpoint proxy", proxy.is_finite())
        lower = exact_lower(proxy)
        debit = F(angular[comparison["x"]]["exact_transport_debit"])
        COUNTS["midpoint_proxies"] += 1
        comparison.update(
            status="boundary_prepared", cost=real_ball(cost), midpoint_proxy=real_ball(proxy),
            exact_midpoint_proxy_lower=str(lower), exact_transport_debit=str(debit),
            exact_boundary_margin_lower=str(lower-debit))
    cell["status"] = "boundary_prepared"


def finish_circles(result):
    result["circle_certificates"] = []
    for circle in CIRCLES:
        cells = [v for v in result["cells"] if v["circle"] == circle["label"]]
        complete = len(cells) == 512 and all(v["status"] == "boundary_prepared" for v in cells)
        record = dict(circle=circle["label"], status="blocked", verdict="inconclusive",
                      blocking_cells=[v["id"] for v in cells if v["status"] != "boundary_prepared"])
        result["circle_certificates"].append(record)
        if not complete:
            for cell in cells:
                for comparison in cell["comparisons"]:
                    comparison["status"] = "blocked"
                    comparison["reason"] = "The full circle product bound is unavailable; no cell is omitted."
            continue
        witness = max(cells, key=lambda v: F(v["product_bound"]["exact_upper"]))
        bound = F(witness["product_bound"]["exact_upper"])
        radius = F(circle["radius"])
        disk_debit = radius*radius*bound/2
        record.update(status="completed", exact_B_upper=str(bound), witness=witness["id"],
                      exact_disk_debit=str(disk_debit), radius=circle["radius"])
        for cell in cells:
            for comparison in cell["comparisons"]:
                boundary_lower = F(comparison["exact_boundary_margin_lower"])
                certificate = boundary_lower-disk_debit
                comparison.update(
                    status="completed", exact_disk_debit=str(disk_debit),
                    exact_final_certificate_lower=str(certificate),
                    lower_certificate_display=real_ball(ar(certificate)),
                    verdict="positive" if certificate > 0 else "insufficient")
                COUNTS["final_comparisons"] += 1
                result["unprocessed_comparisons"].remove(comparison["id"])
            cell["status"] = "completed"
            cell["verdict"] = ("all_four_certificates_positive"
                               if all(v["verdict"] == "positive" for v in cell["comparisons"])
                               else "insufficient")
        record["verdict"] = ("all_circle_certificates_positive"
                             if all(v["verdict"] == "all_four_certificates_positive" for v in cells)
                             else "insufficient")


def validate_new_manifest(manifest):
    assert manifest["schema"] == "fixed-saved-half-face-affine-v1"
    assert manifest["root_reviewed"] is True and manifest["peer_reviewed"] is True
    assert manifest["protocol"] == PROTOCOL and manifest["checker"] == SCRIPT
    assert manifest["manifest_instructions"] == GUIDE
    assert manifest["output"] == str(OUTPUT.relative_to(ROOT))
    assert manifest["precision_bits"] == 256 and manifest["circle_inventory"] == CIRCLES
    assert manifest["cells_per_circle"] == 512 and manifest["total_cells"] == 1024
    assert manifest["comparison_inventory"] == TESTS and manifest["total_comparisons"] == 4096
    assert manifest["comparison_method"] == "two_response_affine_disk_barrier"
    assert manifest["nu_method"] == "original_elementary_log_lower_bound"
    assert manifest["catalan_upper"] == "73/500"
    assert manifest["cap_upper"] == {"base": "203/200", "subtract": "1303/7680000"}
    assert manifest["point_radius"] == POINT_RADIUS and manifest["parameter_radius"] == CELL_RADIUS
    assert manifest["pinned_inputs_sha256"] == PINNED
    reviews = manifest["review_records"]
    valid = [v for v in reviews if
             v.get("verdict") == "PASS"
             and v.get("protocol_sha256") == PROTOCOL_SHA256
             and v.get("checker_sha256") == manifest["files_sha256"][SCRIPT]
             and v.get("execution_performed") is False]
    assert any(v["reviewer"] == "/root" for v in valid), "missing exact-hash root review"
    assert any(v["reviewer"] != "/root" for v in valid), "missing exact-hash independent review"


def main():
    global PI, II, LOG2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    if OUTPUT.exists():
        raise FileExistsError("the sole saved-affine attempt already exists; no overwrite")
    inventory = fixed_inventory()
    comparison_ids = [v["id"]+"/"+test["label"] for v in inventory for test in TESTS]
    result = dict(
        status="failed", verdict="inconclusive", precision_bits=256,
        protocol=PROTOCOL, protocol_sha256=PROTOCOL_SHA256,
        original_boundary=BOUNDARY, original_boundary_sha256=PINNED[BOUNDARY],
        original_boundary_status="failed", saved_response=RESPONSE,
        saved_response_sha256=PINNED[RESPONSE], circles=CIRCLES, cells_per_circle=512,
        comparison_inventory=TESTS, inventory=inventory, cells=[],
        unprocessed_inventory=[v["id"] for v in inventory],
        unprocessed_comparisons=list(comparison_ids), operation_counts=COUNTS,
        changed_inputs=[], manifest_changed=False, retries=0, refinements=0,
        scope="Conservative full-disk half-face affine certificates only; no macroscopic arc, vertical join, or knot-family conclusion.")
    frozen = None
    claimed = {}
    manifest_hash = None
    try:
        manifest_hash = sha(args.manifest)
        result["manifest_sha256"] = manifest_hash
        manifest = json.loads(args.manifest.read_text())
        claimed = manifest.get("files_sha256", {})
        result["claimed_files_sha256"] = claimed
        validate_new_manifest(manifest)
        frozen, audit = verify_inputs(manifest)
        result["files_sha256"] = frozen
        result["provenance_audit"] = audit
        boundary, response = verify_banks()
        ctx.prec = 256
        PI, II = arb.pi(), acb(0, 1)
        LOG2 = arb(2).log()
        for position, item in enumerate(inventory):
            cell = dict(item, status="failed", verdict="inconclusive", checks=[],
                        comparisons=[dict(test, id=item["id"]+"/"+test["label"],
                                          status="unprocessed", verdict="inconclusive")
                                     for test in TESTS])
            result["cells"].append(cell)
            before = dict(COUNTS)
            try:
                prepare_cell(boundary["cells"][position], response["cells"][position], cell)
            except Exception as exc:
                cell["error"] = f"{type(exc).__name__}: {exc}"
                cell["traceback"] = traceback.format_exc()
            finally:
                cell["preparation_operation_counts"] = {key: COUNTS[key]-before[key] for key in COUNTS}
                result["unprocessed_inventory"].remove(cell["id"])
        assert [v["id"] for v in result["cells"]] == [v["id"] for v in inventory]
        finish_circles(result)
        comparisons = [v for cell in result["cells"] for v in cell["comparisons"]]
        assert [v["id"] for v in comparisons] == comparison_ids
        result["summary"] = dict(
            attempted_cells=len(result["cells"]),
            completed_cells=sum(v["status"] == "completed" for v in result["cells"]),
            positive_cells=sum(v["verdict"] == "all_four_certificates_positive" for v in result["cells"]),
            prepared_product_bounds=sum("product_bound" in v for v in result["cells"]),
            completed_comparisons=sum(v["status"] == "completed" for v in comparisons),
            positive_comparisons=sum(v["verdict"] == "positive" for v in comparisons),
            insufficient_comparison_ids=[v["id"] for v in comparisons if v["verdict"] == "insufficient"],
            failed_cell_ids=[v["id"] for v in result["cells"] if "error" in v],
            blocked_comparison_ids=[v["id"] for v in comparisons if v["status"] == "blocked"])
        if all(v["status"] == "completed" for v in comparisons):
            assert COUNTS["two_coordinate_response_enclosures"] == COUNTS["product_bounds"] == 1024
            assert COUNTS["angular_derivative_enclosures"] == 2048
            assert COUNTS["midpoint_proxies"] == COUNTS["final_comparisons"] == 4096
            assert not result["unprocessed_comparisons"]
            assert all(COUNTS[key] == 0 for key in (
                "new_roots", "new_inclusions", "new_hessians", "new_matrix_inverses",
                "new_actions", "new_dilogarithms", "source_replays", "retries", "subdivisions"))
            result["status"] = "completed"
            result["verdict"] = ("both_full_disks_have_positive_half_face_affine_certificates"
                                 if all(v["verdict"] == "positive" for v in comparisons)
                                 else "complete_inventory_recorded_affine_test_inconclusive")
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["traceback"] = traceback.format_exc()
    finally:
        def changed_or_missing(path, digest):
            try:
                return sha(path) != digest
            except OSError:
                return True
        result["changed_inputs"] = [
            path for path, digest in claimed.items() if changed_or_missing(ROOT/path, digest)]
        if result["changed_inputs"]:
            result["status"], result["verdict"] = "failed", "inconclusive"
        if manifest_hash is not None and changed_or_missing(args.manifest, manifest_hash):
            result["manifest_changed"] = True
            result["status"], result["verdict"] = "failed", "inconclusive"
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        with OUTPUT.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    print(json.dumps(dict(status=result["status"], verdict=result["verdict"],
                         summary=result.get("summary"), counts=COUNTS, output=str(OUTPUT))))
    if result["status"] != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
