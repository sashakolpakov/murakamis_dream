#!/usr/bin/env python3
"""One fixed exact-rational quadratic comparison. UNRUN until approved."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import traceback

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_half_face_saved_quadratic_protocol.md"
PROTOCOL_SHA256 = "13b6d4cc3c9c76c0cd83fff00acbe430d32d89331af5879ffb175484e4f0f527"
SCRIPT = "experiments/check_mixed_half_face_saved_quadratic.py"
GUIDE = "notes/research_mixed_half_face_saved_quadratic_manifest_instructions.md"
MANIFEST = ROOT / "repro/protocols/research-mixed-half-face-saved-quadratic.json"
OUTPUT = ROOT / "repro/results/research-mixed-half-face-saved-quadratic-attempt01.json"
OLD_RESULT = "repro/results/research-mixed-half-face-saved-affine-attempt01.json"
OLD_MANIFEST = "repro/protocols/research-mixed-half-face-saved-affine.json"
OLD_PROTOCOL = "notes/research_mixed_half_face_saved_affine_protocol.md"
OLD_SCRIPT = "experiments/check_mixed_half_face_saved_affine.py"
OLD_VERDICT = "complete_inventory_recorded_affine_test_inconclusive"
PINNED = {
    PROTOCOL: PROTOCOL_SHA256,
    OLD_RESULT: "533f8dd9663b920b541c2f7e3252d12153fb6d16dfe726c615da9d63148092c2",
    OLD_MANIFEST: "a71b93551de6fb5a8137988cef3cad860cbf3894c5f369babd3ab978c6ba0b04",
    OLD_PROTOCOL: "4e69ba62e3e1346d25aca7a00e19bd4b5bdc5fcb88972851182a33a97031938d",
    OLD_SCRIPT: "0e21dcd63a282a441e643b40af90934957c43d60dc2e2407e340805f2b08f3e6",
    "notes/research_mixed_half_face_conditional_curvature.md":
        "a2900aa248151f3f521f7c1024d850e6a8f24bc7fd8e41310a0d93206ede335d",
    "notes/research_mixed_real_arc_conditional_absolute_decrease.md":
        "cd5f0883d0ed52e60aeb4998f5feeb2aff9904ec715b9546aef5ed9058d1a79a",
    "notes/research_mixed_real_arc_complete_conditional_packet.md":
        "3a4b5b12849457867e5e80d6b795af93ac94d4b526875ccf73fd447daa56a9b7",
    "notes/research_mixed_real_arc_complete_cap_upper.md":
        "192fdd7842c00301bd8c6eabfc33954e35e593cc376c5b1418294f5f8530ebb1",
    "notes/research_mixed_half_face_saved_affine_outcome.md":
        "02c723c6717c87bb768880ff92decc8f7fb9c0cf239063b16e70e3e1028b0a65",
}
REQUIRED = set(PINNED) | {
    SCRIPT, GUIDE,
    "notes/research_mixed_half_face_general_incoming_transport.md",
    "notes/research_mixed_half_face_global_phase_decrease.md",
    "notes/research_mixed_next_selected_first_wall_rows.md",
    "notes/research_mixed_next_far_half_conditional_aliases.md",
    "notes/research_mixed_three_four_next_local_source.md",
    "notes/research_mixed_next_coherent_cap_far_arc.md",
    "notes/research_mixed_next_wrapped_private_sector.md",
    "notes/research_mixed_cap_seam_source_bounds.md",
    "notes/research_mixed_three_four_continuous_far_half_cap.md",
    "notes/research_mixed_three_four_complementary_real_colors.md",
}
FORBIDDEN_BINDINGS = {"notes/research_finite_exceptions_progress.md"}
CIRCLES = [
    {"label": "c3", "center": ["7/20", "-1/100"], "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "c4", "center": ["3/10", "-13/250"], "radius": "3/50", "typed_radius": "8/125"},
]
OLD_TESTS = [
    {"label": "factorial_left", "alternative": "factorial", "x": "11/50"},
    {"label": "factorial_right", "alternative": "factorial", "x": "9/20"},
    {"label": "forcing_left", "alternative": "forcing", "x": "11/50"},
    {"label": "forcing_right", "alternative": "forcing", "x": "9/20"},
]
TESTS = [
    {"alternative": "factorial", "mu": "3575/3072",
     "left_label": "factorial_left", "right_label": "factorial_right"},
    {"alternative": "forcing", "mu": "25/24",
     "left_label": "forcing_left", "right_label": "forcing_right"},
]
CONSTANTS = {"delta_left": "-3/100", "delta_right": "1/5", "height_gain": "3/200"}
DEPENDENCY_FIELDS = (
    "dependencies", "dependencies_sha256", "primary_records",
    "primary_records_sha256", "saved_replays", "saved_replays_sha256", "files_sha256",
)
COUNTS = dict(
    saved_rational_certificates_parsed=0, quadratic_minima=0, sign_comparisons=0,
    decoded_real_intervals=0, response_enclosures=0, product_bounds=0,
    angular_derivative_enclosures=0, midpoint_proxies=0, disk_debits=0,
    new_roots=0, new_inclusions=0, new_hessians=0, new_matrix_inverses=0,
    new_actions=0, new_dilogarithms=0, source_replays=0, retries=0,
    refinements=0, subdivisions=0,
)
FORBIDDEN_COUNTS = tuple(k for k in COUNTS if k not in (
    "saved_rational_certificates_parsed", "quadratic_minima", "sign_comparisons"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path):
    """Reject duplicate JSON keys rather than silently replacing bindings."""
    def unique_pairs(pairs):
        data = {}
        for key, value in pairs:
            require(key not in data, f"duplicate JSON key in {path}: {key}")
            data[key] = value
        return data
    return json.loads(Path(path).read_text(), object_pairs_hook=unique_pairs)


def rational(text, label):
    require(isinstance(text, str) and text != "", f"{label}: missing rational string")
    pieces = text.split("/")
    require(len(pieces) in (1, 2), f"{label}: invalid rational format")
    numerator = pieces[0][1:] if pieces[0].startswith("-") else pieces[0]
    require(numerator != "" and all(c in "0123456789" for c in numerator),
            f"{label}: invalid integer numerator")
    if len(pieces) == 2:
        require(pieces[1] != "" and all(c in "0123456789" for c in pieces[1])
                and pieces[1].lstrip("0") != "", f"{label}: invalid positive denominator")
    value = F(text)
    require(str(value) == text, f"{label}: noncanonical exact rational")
    return value


def check(cell, name, condition):
    cell["checks"].append(dict(name=name, passed=bool(condition)))
    require(condition, f'{cell["id"]}: {name}')


def fixed_inventory():
    return [
        dict(id=f'{circle["label"]}:{index:03d}', circle=circle["label"], index=index,
             theta_start_pi=str(F(2 * index, 512)),
             theta_end_pi=str(F(2 * (index + 1), 512)),
             theta_midpoint_pi=str(F(2 * index + 1, 512)))
        for circle in CIRCLES for index in range(512)
    ]


def old_check_names():
    names = ["both saved inventories " + key for key in
             ("id", "circle", "index", "theta_start_pi", "theta_end_pi", "theta_midpoint_pi")]
    names.extend([
        "original failed status preserved", "only the original direct-inverse failure",
        "all original checks present and passed", "full original proposal inventory",
        "original failure did not yield comparison data", "original fixed operation inventory",
        "saved response completed with both old margins", "all saved-response checks present and passed",
        "both saved comparison inventories retained", "saved response operation inventory",
        "both complete original inclusions",
    ])
    for tag in ("midpoint", "whole_cell"):
        names.append(tag + ": fixed original radius")
        for index in range(5):
            names.extend([f"{tag} row {index}: decoded contraction",
                          f"{tag} row {index}: decoded strict inclusion"])
    names.extend([
        "all five saved response row bounds", "same five original decoded row bounds",
        "saved contraction maximum and final row agree", "complete exact rational inverse inventory",
        "same original exact inverse column", "saved rational column norm bound",
        "whole_cell: original derivative strips", "whole_cell: negative outgoing height",
        "midpoint: original derivative strips", "midpoint: negative outgoing height",
        "original external mixed strip", "saved finite final-row response",
        "finite penultimate-row response", "finite holomorphic product bound",
        "finite saved circle derivative and positive halfwidth",
        "11/50: finite signed deficit derivative", "9/20: finite signed deficit derivative",
        "finite original midpoint action and elementary lower halfweight",
    ])
    names.extend(test["label"] + ": finite conservative midpoint proxy" for test in OLD_TESTS)
    return names


def validate_manifest(manifest):
    require(manifest["schema"] == "fixed-saved-half-face-quadratic-v1", "manifest schema")
    require(manifest["protocol"] == PROTOCOL and manifest["checker"] == SCRIPT,
            "manifest protocol/checker paths")
    require(manifest["manifest_instructions"] == GUIDE, "manifest guide path")
    require(manifest["output"] == str(OUTPUT.relative_to(ROOT)), "manifest output path")
    require(manifest["old_result"] == OLD_RESULT and manifest["old_manifest"] == OLD_MANIFEST,
            "manifest old input paths")
    require(manifest["root_reviewed"] is True and manifest["peer_reviewed"] is True,
            "missing full static reviews")
    require(manifest["circle_inventory"] == CIRCLES, "manifest fixed circles")
    require(manifest["cells_per_circle"] == 512 and manifest["total_cells"] == 1024,
            "manifest cell counts")
    require(manifest["old_comparison_inventory"] == OLD_TESTS
            and manifest["saved_endpoint_count"] == 4096, "manifest old comparison inventory")
    require(manifest["comparison_inventory"] == TESTS and manifest["total_comparisons"] == 2048,
            "manifest new comparison inventory")
    require(manifest["constants"] == CONSTANTS, "manifest fixed rational constants")
    require(manifest["comparison_method"] == "exact_saved_endpoint_chord_clipped_quadratic",
            "manifest comparison method")
    require(manifest["arithmetic"] == "python_integer_and_fraction_only", "manifest arithmetic")
    require(manifest["pinned_inputs_sha256"] == PINNED, "manifest pinned inputs")
    expected = manifest["files_sha256"]
    reviews = manifest["review_records"]
    valid = [v for v in reviews if
             v.get("verdict") == "PASS" and v.get("protocol_sha256") == PROTOCOL_SHA256
             and v.get("checker_sha256") == expected[SCRIPT]
             and v.get("guide_sha256") == expected[GUIDE]
             and v.get("execution_performed") is False]
    require(any(v.get("reviewer") == "/root" for v in valid), "missing exact-hash root review")
    require(any(isinstance(v.get("reviewer"), str) and v["reviewer"] != ""
                and v["reviewer"] != "/root"
                for v in valid), "missing exact-hash independent review")


def verify_inputs(manifest, result):
    expected = manifest["files_sha256"]
    require(isinstance(expected, dict), "file bindings must be a dictionary")
    require(REQUIRED <= expected.keys(),
            f"missing mandatory bindings: {sorted(REQUIRED - expected.keys())}")
    require(str(OUTPUT.relative_to(ROOT)) not in expected
            and str(MANIFEST.relative_to(ROOT)) not in expected, "self/output binding forbidden")
    require(not FORBIDDEN_BINDINGS.intersection(expected), "mutable progress binding forbidden")
    for path, digest in PINNED.items():
        require(expected.get(path) == digest, f"incorrect pinned binding: {path}")
    for path, digest in expected.items():
        require(isinstance(path, str) and not Path(path).is_absolute()
                and ".." not in Path(path).parts, f"invalid relative binding path: {path}")
        require(isinstance(digest, str) and len(digest) == 64
                and all(c in "0123456789abcdef" for c in digest), f"invalid hash: {path}")
        require(sha(ROOT / path) == digest, f"changed frozen input: {path}")
    old_manifest = load_json(ROOT / OLD_MANIFEST)
    inherited = old_manifest["files_sha256"]
    require(len(inherited) == 379, "old manifest must retain all 379 bindings")
    for path, digest in inherited.items():
        require(expected.get(path) == digest, f"missing/changed inherited binding: {path}")
    require(old_manifest["root_reviewed"] is True and old_manifest["peer_reviewed"] is True,
            "old static review metadata")
    require(old_manifest["schema"] == "fixed-saved-half-face-affine-v1", "old manifest schema")
    visited, edges = set(), []
    audit = dict(files=len(expected), inherited_old_files=len(inherited),
                 records=[], edges=edges)
    result["provenance_audit"] = audit

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        audit["records"] = sorted(visited)
        data = load_json(ROOT / path)
        for field in DEPENDENCY_FIELDS:
            deps = data.get(field, {})
            if not isinstance(deps, dict):
                continue
            for child, digest in deps.items():
                require(expected.get(child) == digest,
                        f"unbound dependency: {path} / {field} / {child}")
                require(sha(ROOT / child) == digest, f"changed dependency: {child}")
                edges.append(dict(parent=path, field=field, child=child, sha256=digest))
                if child.startswith(("repro/results/", "repro/protocols/")) and child.endswith(".json"):
                    inherit(child)

    for path in sorted(expected):
        if path.startswith(("repro/results/", "repro/protocols/")) and path.endswith(".json"):
            inherit(path)
    return expected, old_manifest


def verify_old_result(old, old_manifest, result):
    inventory = fixed_inventory()
    ids = [v["id"] for v in inventory]
    require(old["status"] == "completed" and old["verdict"] == OLD_VERDICT,
            "old completed-inconclusive status/verdict")
    require(old["protocol"] == OLD_PROTOCOL and old["protocol_sha256"] == PINNED[OLD_PROTOCOL],
            "old protocol binding")
    require(old["manifest_sha256"] == PINNED[OLD_MANIFEST], "old manifest binding")
    require(old["files_sha256"] == old["claimed_files_sha256"] == old_manifest["files_sha256"],
            "old complete binding inventory")
    require(not any(old.get(key) for key in ("error", "traceback", "changed_inputs",
                                            "manifest_changed")), "old global failure")
    require(old["unprocessed_inventory"] == [] and old["unprocessed_comparisons"] == [],
            "old unprocessed inventory")
    require(old["retries"] == old["refinements"] == 0, "old retry/refinement metadata")
    require(old["precision_bits"] == 256 and old["circles"] == CIRCLES
            and old["cells_per_circle"] == 512, "old circle/precision metadata")
    require(old["inventory"] == inventory and len(old["cells"]) == 1024
            and [v["id"] for v in old["cells"]] == ids, "old full ordered cell inventory")
    require(old["comparison_inventory"] == OLD_TESTS, "old ordered comparisons")
    require(old["operation_counts"] == dict(
        decoded_real_intervals=63488, two_coordinate_response_enclosures=1024,
        product_bounds=1024, angular_derivative_enclosures=2048, midpoint_proxies=4096,
        final_comparisons=4096, new_roots=0, new_inclusions=0, new_hessians=0,
        new_matrix_inverses=0, new_actions=0, new_dilogarithms=0,
        source_replays=0, retries=0, subdivisions=0), "old complete operation inventory")
    require(old["original_boundary_status"] == "failed", "original interval-inverse failure status")
    original = load_json(ROOT / old["original_boundary"])
    require(sha(ROOT / old["original_boundary"]) == old["original_boundary_sha256"],
            "original failed bank hash")
    require(original["status"] == "failed" and original["verdict"] == "inconclusive",
            "original failure must not be promoted")
    require(len(original["cells"]) == 1024, "original failed bank full inventory")
    require([v["id"] for v in original["cells"]] == ids, "original failed bank cell order")
    require(all(v["status"] == "failed" and v["error"] == "ZeroDivisionError: matrix is singular"
                and v["comparisons"] == [] for v in original["cells"]),
            "original failures and empty comparisons preserved")
    result["original_failure_record"] = dict(
        path=old["original_boundary"], sha256=old["original_boundary_sha256"],
        status=original["status"], verdict=original["verdict"],
        summary=original["summary"], operation_counts=original["operation_counts"])
    require(len(old["circle_certificates"]) == 2
            and [v["circle"] for v in old["circle_certificates"]] == ["c3", "c4"],
            "old complete circle certificates")
    for circle, record in zip(CIRCLES, old["circle_certificates"]):
        require(record["status"] == "completed" and record["verdict"] == "insufficient"
                and record["blocking_cells"] == [] and record["radius"] == circle["radius"],
                f'old circle metadata: {circle["label"]}')
    result["old_status"] = old["status"]
    result["old_verdict"] = old["verdict"]
    result["old_summary"] = old["summary"]
    result["old_operation_counts"] = old["operation_counts"]
    result["old_circle_certificates"] = old["circle_certificates"]
    parsed = {}
    flat = []
    for item, cell in zip(inventory, old["cells"]):
        label = item["id"]
        require(all(cell.get(k) == v for k, v in item.items()), f"old inventory mismatch: {label}")
        require(cell["status"] == "completed" and cell["verdict"] == "insufficient"
                and not cell.get("error"), f"old cell status: {label}")
        require(cell["checks"] == [dict(name=name, passed=True) for name in old_check_names()],
                f"old complete 61-check inventory: {label}")
        require(len(cell["comparisons"]) == 4, f"old four comparisons: {label}")
        circle = old["circle_certificates"][0 if item["circle"] == "c3" else 1]
        for test, comp in zip(OLD_TESTS, cell["comparisons"]):
            comp_id = label + "/" + test["label"]
            require(all(comp.get(k) == v for k, v in test.items()) and comp["id"] == comp_id,
                    f"old comparison labels: {comp_id}")
            require(comp["status"] == "completed" and comp["verdict"] in ("positive", "insufficient"),
                    f"old comparison status: {comp_id}")
            require(comp["exact_disk_debit"] == circle["exact_disk_debit"],
                    f"old shared stored disk debit: {comp_id}")
            # This is the only saved mathematical field parsed by the new checker.
            parsed[comp_id] = rational(comp["exact_final_certificate_lower"], comp_id)
            COUNTS["saved_rational_certificates_parsed"] += 1
            flat.append(comp)
    summary = dict(
        attempted_cells=1024, completed_cells=1024, positive_cells=0,
        prepared_product_bounds=1024, completed_comparisons=4096,
        positive_comparisons=sum(v["verdict"] == "positive" for v in flat),
        insufficient_comparison_ids=[v["id"] for v in flat if v["verdict"] == "insufficient"],
        failed_cell_ids=[], blocked_comparison_ids=[])
    require(summary["positive_comparisons"] == 1498
            and len(summary["insufficient_comparison_ids"]) == 2598, "old verdict counts")
    require(old["summary"] == summary, "old complete summary metadata")
    require(len(parsed) == 4096 and COUNTS["saved_rational_certificates_parsed"] == 4096,
            "old exact rational certificate inventory")
    return parsed


def calculate_comparison(cell, comparison, old_cell, parsed):
    test = comparison
    by_label = {v["label"]: v for v in old_cell["comparisons"]}
    left = by_label[test["left_label"]]
    right = by_label[test["right_label"]]
    comparison["old_left"] = {key: left[key] for key in (
        "id", "label", "alternative", "x", "status", "verdict", "exact_final_certificate_lower")}
    comparison["old_right"] = {key: right[key] for key in (
        "id", "label", "alternative", "x", "status", "verdict", "exact_final_certificate_lower")}
    lower_left, lower_right = parsed[left["id"]], parsed[right["id"]]
    d_left, d_right = F(CONSTANTS["delta_left"]), F(CONSTANTS["delta_right"])
    mu, gain = F(test["mu"]), F(CONSTANTS["height_gain"])
    slope = (lower_right - lower_left) / (d_right - d_left)
    free_minimizer = -slope / (2 * mu)
    minimizer = max(d_left, min(d_right, free_minimizer))
    minimum = lower_left + slope * (minimizer - d_left) + mu * minimizer**2 + gain
    COUNTS["quadratic_minima"] += 1
    positive = minimum > 0
    COUNTS["sign_comparisons"] += 1
    location = ("left_endpoint" if free_minimizer <= d_left else
                "right_endpoint" if free_minimizer >= d_right else "interior")
    comparison.update(
        status="completed", verdict="positive" if positive else "insufficient",
        exact_slope=str(slope), exact_unclipped_minimizer=str(free_minimizer),
        exact_minimizer=str(minimizer), minimizer_location=location,
        exact_minimum=str(minimum), strict_positive=positive,
        delta_interval=[CONSTANTS["delta_left"], CONSTANTS["delta_right"]],
        height_gain=CONSTANTS["height_gain"],
        old_disk_debit_subtracted_again=False)


def main():
    if OUTPUT.exists():
        raise FileExistsError("the sole saved-quadratic attempt already exists; no overwrite")
    inventory = fixed_inventory()
    comparison_ids = [v["id"] + "/" + test["alternative"] for v in inventory for test in TESTS]
    result = dict(
        status="failed", verdict="inconclusive", arithmetic="python_integer_and_fraction_only",
        protocol=PROTOCOL, protocol_sha256=PROTOCOL_SHA256,
        old_result=OLD_RESULT, old_result_sha256=PINNED[OLD_RESULT],
        old_manifest=OLD_MANIFEST, old_manifest_sha256=PINNED[OLD_MANIFEST],
        circles=CIRCLES, cells_per_circle=512, constants=CONSTANTS,
        comparison_inventory=TESTS, inventory=inventory, cells=[],
        unprocessed_inventory=[v["id"] for v in inventory],
        unprocessed_comparisons=list(comparison_ids), operation_counts=COUNTS,
        changed_inputs=[], manifest_changed=False, retries=0, refinements=0,
        claimed_files_sha256={},
        scope="The improved selected real-arc comparison only; no vertical connector or knot-family conclusion.")
    claimed = {}
    manifest_hash = None
    try:
        manifest_hash = sha(MANIFEST)
        result["manifest_sha256"] = manifest_hash
        manifest = load_json(MANIFEST)
        claimed = manifest.get("files_sha256", {})
        result["claimed_files_sha256"] = claimed
        validate_manifest(manifest)
        frozen, old_manifest = verify_inputs(manifest, result)
        result["files_sha256"] = frozen
        old = load_json(ROOT / OLD_RESULT)
        parsed = verify_old_result(old, old_manifest, result)
        for item, old_cell in zip(inventory, old["cells"]):
            cell = dict(item, status="failed", verdict="inconclusive", checks=[],
                        old_checks=old_cell["checks"],
                        comparisons=[dict(test, id=item["id"] + "/" + test["alternative"],
                                          status="unprocessed", verdict="inconclusive") for test in TESTS])
            result["cells"].append(cell)
            for comparison in cell["comparisons"]:
                before = dict(COUNTS)
                try:
                    calculate_comparison(cell, comparison, old_cell, parsed)
                    result["unprocessed_comparisons"].remove(comparison["id"])
                except Exception as exc:
                    comparison["status"] = "failed"
                    comparison["error"] = f"{type(exc).__name__}: {exc}"
                    comparison["traceback"] = traceback.format_exc()
                finally:
                    comparison["operation_counts"] = {key: COUNTS[key] - before[key] for key in COUNTS}
            complete = all(v["status"] == "completed" for v in cell["comparisons"])
            cell["status"] = "completed" if complete else "failed"
            cell["verdict"] = ("both_quadratics_positive"
                               if complete and all(v["verdict"] == "positive" for v in cell["comparisons"])
                               else "insufficient" if complete else "inconclusive")
            check(cell, "both prescribed comparisons attempted",
                  [v["id"] for v in cell["comparisons"]] ==
                  [item["id"] + "/" + t["alternative"] for t in TESTS])
            result["unprocessed_inventory"].remove(cell["id"])
        comparisons = [v for cell in result["cells"] for v in cell["comparisons"]]
        require([v["id"] for v in comparisons] == comparison_ids, "new complete comparison order")
        result["circle_certificates"] = []
        for circle in CIRCLES:
            cells = [v for v in result["cells"] if v["circle"] == circle["label"]]
            complete = len(cells) == 512 and all(v["status"] == "completed" for v in cells)
            record = dict(
                circle=circle["label"], status="completed" if complete else "blocked",
                verdict=("all_quadratics_positive" if complete and all(
                    v["verdict"] == "both_quadratics_positive" for v in cells) else
                    "insufficient" if complete else "inconclusive"),
                failed_cell_ids=[v["id"] for v in cells if v["status"] != "completed"])
            result["circle_certificates"].append(record)
        result["summary"] = dict(
            attempted_cells=len(result["cells"]),
            completed_cells=sum(v["status"] == "completed" for v in result["cells"]),
            positive_cells=sum(v["verdict"] == "both_quadratics_positive" for v in result["cells"]),
            completed_comparisons=sum(v["status"] == "completed" for v in comparisons),
            positive_comparisons=sum(v["verdict"] == "positive" for v in comparisons),
            insufficient_comparison_ids=[v["id"] for v in comparisons if v["verdict"] == "insufficient"],
            failed_comparison_ids=[v["id"] for v in comparisons if v["status"] == "failed"],
            failed_cell_ids=[v["id"] for v in result["cells"] if v["status"] == "failed"])
        if all(v["status"] == "completed" for v in comparisons):
            require(COUNTS["saved_rational_certificates_parsed"] == 4096
                    and COUNTS["quadratic_minima"] == COUNTS["sign_comparisons"] == 2048,
                    "complete prescribed operation inventory")
            require(all(COUNTS[key] == 0 for key in FORBIDDEN_COUNTS), "forbidden operation count")
            require(not result["unprocessed_inventory"] and not result["unprocessed_comparisons"],
                    "unprocessed new inventory")
            result["status"] = "completed"
            result["verdict"] = (
                "both_full_disks_have_positive_quadratic_real_arc_certificates"
                if all(v["verdict"] == "positive" for v in comparisons)
                else "complete_inventory_recorded_quadratic_test_inconclusive")
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["traceback"] = traceback.format_exc()
    finally:
        def changed_or_missing(path, digest):
            try:
                return sha(path) != digest
            except (OSError, ValueError):
                return True
        if isinstance(claimed, dict):
            result["changed_inputs"] = [
                path for path, digest in claimed.items()
                if changed_or_missing(ROOT / path, digest)]
        if result["changed_inputs"]:
            result["status"], result["verdict"] = "failed", "inconclusive"
        if manifest_hash is not None and changed_or_missing(MANIFEST, manifest_hash):
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

