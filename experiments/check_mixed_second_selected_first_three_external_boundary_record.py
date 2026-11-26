"""Stdlib-only saved-data check of a complete first-three boundary record.

No provider is imported and no reference, root, primitive or interval
evaluation is performed. Source identity, counts and conservative bounds
are pinned to the separately completed boundary attempt.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import gzip
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "repro/results/research-mixed-second-selected-first-three-external-boundary-attempt01.json.gz"
EXPECTED_SOURCE_SHA256 = "9744bb69bd81745f856b0424f7df3448b39f5208eae929f709dc7a3d639af956"
EXPECTED_COUNTS = {
    "input_bindings": 57, "nodes": 3046, "leaves": 1532,
    "accepted": 1419, "geometry_excluded": 113, "reference_excluded": 0,
}
# Post-result bounds chosen for this source, not the first-type-four table.
# Each table row is (strict gamma lower, strict response upper).
CONSERVATIVE_TABLE = {
    (0, "k3"): (".02327", "1.637"),
    (0, "k4"): (".02142", "2.050"),
    (1, "k3"): (".01119", "1.363"),
    (1, "k4"): (".01616", "1.671"),
}
CHOSEN_COMMON_GAP = F(1, 200)
MANDATORY_INPUTS = {
    "experiments/certify_mixed_second_selected_first_three_external_boundary.py":
        "f5c346ba7bdc624953b2b808d8d07829d761cf3f382984a987bf856a29d62177",
    "experiments/mixed_second_selected_first_three_external_reference.py":
        "695ae91ad46581c74419e5ade992d7a233112761b88643199c9690a12b3df1d3",
    "experiments/mixed_second_selected_first_three_external_response.py":
        "476be0189ffb5b887316d230b0b8362108b5f5d97ec59c77d8232b3d9696a312",
    "notes/research_mixed_second_selected_first_three_extension.md":
        "d488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2",
    "notes/research_mixed_second_selected_first_three_external_boundary_evaluation.md":
        "27a46e35949c4fb31b8b01b2f68a6a6e4c4b0fd33887302c115127249525d8a8",
}
NAMES = ("e", "xi", "a", "u", "z", "v", "b")
DOMAINS = {
    3: (F(".35"), F("-.01"), F(".083"), F("-.072"), F(".068")),
    4: (F(".30"), F("-.052"), F(".060"), F("-.108"), F("-.001")),
}
CHARTS = (
    "k3_circle_right", "k3_circle_left", "k3_lower_chord",
    "k3_upper_chord", "k3_oblique_chord", "k4_circle_right",
    "k4_circle_left", "k4_lower_chord", "k4_upper_chord",
)


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2**20), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def interval(record):
    assert record.get("finite") is True
    low, high = F(record["lower_rational"]), F(record["upper_rational"])
    assert low <= high
    return low, high


def complex_box(record):
    return (*interval(record["real"]), *interval(record["imag"]))


def parameter_interval(address):
    assert set(address) <= set("01")
    low, high = F(-1), F(1)
    for digit in address:
        midpoint = (low + high)/2
        if digit == "0":
            high = midpoint
        else:
            low = midpoint
    return low, high


def line(chart):
    kind = int(chart[1])
    x, _, radius, bottom, top = DOMAINS[kind]
    if chart.endswith("lower_chord"):
        return x, bottom, radius, F(0)
    if chart.endswith("upper_chord"):
        return x, top, radius, F(0)
    assert chart == "k3_oblique_chord"
    return F(301, 500), F(-1, 500), F(21, 100), F(7, 100)


def image(chart, low, high):
    x, y, radius, _, _ = DOMAINS[int(chart[1])]
    if "circle" in chart:
        near = F(0) if low <= 0 <= high else min(abs(low), abs(high))
        far = max(abs(low), abs(high))
        real = ((1-far**2)/(1+far**2), (1-near**2)/(1+near**2))
        imag = (2*low/(1+low**2), 2*high/(1+high**2))
        sign = 1 if chart.endswith("right") else -1
        xx = [x+sign*radius*t for t in real]
        yy = [y+sign*radius*t for t in imag]
    else:
        a, b, dx, dy = line(chart)
        xx = [a+dx*low, a+dx*high]
        yy = [b+dy*low, b+dy*high]
    return min(xx), max(xx), min(yy), max(yy)


def check_geometry_exclusion(chart, low, high, box, witness):
    kind = int(chart[1])
    x, y, radius, bottom, top = DOMAINS[kind]
    xl, xh, yl, yh = box
    criterion = witness["criterion"]
    margin = F(witness["strict_margin_rational"])
    assert margin > 0 and witness["chart"] == chart
    assert witness["domain"] == "k"+str(kind)
    assert tuple(map(F, witness["parameter_interval"])) == (low, high)
    assert tuple(map(F, witness["coordinate_box"])) == box
    if criterion == "below_lower_height":
        assert margin == bottom-yh
    elif criterion == "above_upper_height":
        assert margin == yl-top
    elif criterion == "above_oblique_halfplane":
        assert kind == 3
        if "circle" in chart:
            bound = xl-3*yh
        else:
            a, b, dx, dy = line(chart)
            bound = min(a-3*b+(dx-3*dy)*low, a-3*b+(dx-3*dy)*high)
        assert margin == bound-F(76, 125)
    elif criterion == "outside_typed_disk":
        assert "circle" not in chart
        a, b, dx, dy = line(chart)
        a, b = a-x, b-y
        t = max(low, min(high, -(a*dx+b*dy)/(dx*dx+dy*dy)))
        assert margin == (a+dx*t)**2+(b+dy*t)**2-radius**2
    else:
        raise AssertionError(criterion)


def check_reference_metadata(node, box, low, high):
    beta = node["beta"]
    ref = node["reference"]
    details = ref["details"]
    assert ref["alpha"] == details["alpha"] == 0
    assert ref["beta"] == details["beta"] == beta
    assert details["precision_bits"] == 256
    assert ref["status"] == details["status"]
    assert tuple(map(F, details["cbox"])) == box
    midpoint = image(node["chart"], (low+high)/2, (low+high)/2)
    assert midpoint[0] == midpoint[1] and midpoint[2] == midpoint[3]
    assert tuple(map(F, details["cmid"])) == (midpoint[0], midpoint[2])
    assert details["seed_canonical_certification_required"] is False
    seed = [
        [F(".407"), F(".009")], [F(".230"), F(".063")],
        [F(".3345"), F("-.0255")], [F(".30"), F("-.052")],
        [F(".30"), F("-.052")],
    ]
    right = [F(".35"), F("-.01")] if beta == 0 else [F(".30"), F("-.052")]
    seed.extend([right, right])
    saved = [[F(x) for x in row] for row in details["seed_centers"]]
    assert saved == seed
    assert details["seed_centers_sha256"] == canonical_hash(
        [[str(x) for x in row] for row in seed])
    assert not details["suffix_realization_claimed"]
    assert not details["nonempty_parameter_intersection_claimed"]
    for key in ("alternative_seed_or_midpoint_calls", "proposal_retries",
                "finite_source_evaluations", "scalar_budget_evaluations"):
        assert details[key] == 0
    assert ref["counts"] == details["counts"]
    for key, limit in details["operation_limits"].items():
        assert 0 <= details["counts"].get(key, 0) <= limit
    return details


def check_reference_exclusion(details, box, beta):
    """Check saved strict contradiction; no residual or reference reevaluation."""
    assert details["status"] == "excluded"
    survivors = []
    for kind, (a, b, radius, floor, ceiling) in DOMAINS.items():
        dx = max(F(0), box[0]-a, a-box[1])
        dy = max(F(0), box[2]-b, b-box[3])
        excess = dx*dx+dy*dy-radius*radius
        excluded = (excess > 0 or box[3] < floor or box[2] > ceiling
                    or (kind == 3 and box[0]-3*box[3] > F(76, 125)))
        saved = details["external_typed_necessary_tests"][str(kind)]
        assert F(saved["squared_disk_distance_excess_rational"]) == excess
        assert saved["excluded"] == excluded
        assert tuple(map(F, saved["height_interval"])) == (floor, ceiling)
        if not excluded:
            survivors.append(kind)
    assert details["possible_external_types"] == survivors
    if not survivors:
        return
    # With a surviving external type, exclusion must follow a completed
    # localization and an empty necessary actual-coordinate intersection.
    assert details["residual_localization"]["no_clipped_value_used_in_Taylor_bound"]
    assert F(details["residual_localization"]["coordinate_error_modulus_upper_rational"]) >= 0
    ordinary = (".267", ".433", "-.065", ".068") if beta == 0 else (
        ".24", ".36", "-.102", "-.001")
    necessary = {
        "e": (".376", ".438", "-.019", ".037"),
        "xi": (".218", ".242", ".049", ".077"),
        "a": (".278", ".391", "-.072", ".021"),
        "u": (".24", ".36", "-.102", "-.001"),
        "z": (".24", ".36", "-.102", "-.001"), "v": ordinary, "b": ordinary,
    }
    external = {3: tuple(map(F, (".267", ".433", "-.072", ".068"))),
                4: tuple(map(F, (".24", ".36", "-.108", "-.001")))}
    necessary["c"] = (
        min(external[k][0] for k in survivors), max(external[k][1] for k in survivors),
        min(external[k][2] for k in survivors), max(external[k][3] for k in survivors))
    contradictions = []
    for name, saved in details["actual_reference_intersections"].items():
        raw = complex_box(saved["raw_coordinate"])
        bounds = tuple(map(F, necessary[name]))
        common = common_limits(name)
        clipped = (max(raw[0], bounds[0], common[0]),
                   min(raw[1], bounds[1], common[1]),
                   max(raw[2], bounds[2], common[2]),
                   min(raw[3], bounds[3], common[3]))
        assert tuple(map(F, saved["necessary_bounds"])) == bounds
        assert tuple(map(F, saved["common_bounds"])) == common
        assert tuple(map(F, saved["intersection_endpoints"])) == clipped
        contradictions.append(clipped[0] > clipped[1] or clipped[2] > clipped[3])
    assert any(contradictions)


def minimum(record):
    values = [F(x["upper_rational"]) for x in record["candidates"]]
    index = min(range(len(values)), key=values.__getitem__)
    assert record["selected_candidate_index"] == index
    assert F(record["upper_rational"]) == values[index]
    return values[index]


def check_scalar(result, coordinates, shapes, beta):
    assert result["alpha"] == 0 and result["alpha_provenance_supplied_by_driver"]
    assert result["beta"] == beta and result["fully_evaluated_pair"]
    assert result["frozen_helper_calls"] == 1 and result["status"] == "accepted"
    details = result["details"]
    old = details["frozen_result"]
    assert old["beta"] == beta and ("alpha" not in old or old["alpha"] == 0)
    for name in ("u", "z", "v"):
        assert details["input_enclosures"]["coordinates"][name] == coordinates[name]
    assert details["input_enclosures"]["negative_shapes"]["v"] == shapes["v"]
    assert result["additional_primitive_calls"] == 0
    assert result["additional_conjugate_calls"] == 0
    assert result["additional_reference_calls"] == 0
    components = details["component_bounds"]
    left, right, vertical = [minimum(components[x]) for x in ("left", "right", "vertical")]
    original = old["details"]
    pi_low, pi_high = interval(details["input_enclosures"]["pi"])
    assert F(157, 50) < pi_low <= pi_high < F(22, 7)
    assert interval(original["scalars"]["A"])[0] > 0
    assert interval(original["scalars"]["d"])[0] > 0
    assert set(details["branches"]) == set(original["branches"]) == {"forced", "factorial"}
    for label, nu in (("forced", 0), ("factorial", 1)):
        row, frozen = details["branches"][label], original["branches"][label]
        assert row["nu"] == frozen["nu"] == nu and row["selected_gain_keeps_its_sign"]
        selected, trial = minimum(row["selected_bound"]), minimum(row["trial_bound"])
        final = minimum(row["final_bound"])
        assert final == min(interval(frozen["budget"])[1], trial+left+right+selected)
        assert interval(row["budget"]) == (final, final)
        assert final < 0 and row["strictly_below_zero"]
        fourier = interval(original["scalars"]["g_zH_real"])[1] if nu == 0 else -pi_low/50
        assert F(row["trial_bound"]["candidates"][1]["upper_rational"]) == vertical+fourier
    upper = max(interval(details["branches"][label]["budget"])[1]
                for label in ("forced", "factorial"))
    width = max(interval(original["branches"][label]["budget"])[1]
                - interval(original["branches"][label]["budget"])[0]
                for label in ("forced", "factorial"))
    assert F(result["proved_margin_lower_rational"]) == -upper
    return upper, width


def common_limits(name):
    raw = (".33", ".47", "-.09", ".08") if name == "e" else (
        (".21", ".25", ".01", ".10") if name == "xi"
        else (".23", ".45", "-.12", ".12"))
    return tuple(map(F, raw))


def check_accepted(node, details):
    beta = node["beta"]
    assert details["status"] == "enclosed"
    coordinates, shapes = details["actual_coordinate_enclosures"], details["negative_shapes"]
    assert set(coordinates) == set(NAMES+("c",))
    assert set(shapes) == {"e", "a", "u", "z", "v", "b", "c"}
    response = node["response"]
    assert response["alpha"] == 0 and response["beta"] == beta
    assert response["status"] == "enclosed"
    assert response["height_conditions_verified"] and response["common_prefix_product_verified"]
    assert response["canonical_existence_certified_here"] is False
    assert response["qprime_certified_here"] is False
    assert response["coordinate_clipping_performed"] is False
    assert response["details"]["coordinates"] == coordinates
    assert response["details"]["qprime"] == details["response_verification"]["derivative_enclosures"]
    assert details["response_verification"]["neumann_passed"]
    assert F(details["response_verification"]["eta_upper_rational"]) < 1
    for name in NAMES:
        xlow, xhigh, ylow, yhigh = complex_box(coordinates[name])
        left, right, bottom, top = common_limits(name)
        assert left <= xlow <= xhigh <= right and bottom <= ylow <= yhigh <= top
    for name in ("a", "u", "v", "b"):
        low, high = interval(coordinates[name]["imag"])
        bounds = ("-.078", ".021") if name == "a" else (
            ("-.102", "-.001") if name == "u" or beta == 1 else ("-.065", ".068"))
        left, right = map(F, bounds)
        assert left < low <= high < right
    domain_reports = response["details"]["domain_checks"]
    assert domain_reports["common_prefix_product_contains_full_boxes"]
    assert domain_reports["boundary_extension_height_conditions_verified"]
    necessary = domain_reports["necessary_reference_domain_containments"]
    for name, bounds in {
            "e": (".376", ".438", "-.019", ".037"),
            "xi": (".218", ".242", ".049", ".077"),
            "a": (".278", ".391", "-.072", ".021")}.items():
        assert tuple(map(F, necessary[name]["rectangle"]["bounds"])) == tuple(map(F, bounds))
    assert necessary["a"]["disk"]["kind"] == 3
    assert necessary["u"]["disk"]["kind"] == necessary["z"]["disk"]["kind"] == 4
    assert necessary["v"]["disk"]["kind"] == necessary["b"]["disk"]["kind"] == 3+beta
    left = interval(response["details"]["left_product_modulus"])
    right = interval(response["details"]["right_product_modulus"])
    blow, bhigh = interval(response["B"])
    assert blow == max(0, left[0])+max(0, right[0])
    assert bhigh == left[1]+right[1] == F(response["B_upper_rational"])
    assert list(map(F, response["B_upper_components_rational"])) == [left[1], right[1]]
    upper, width = check_scalar(node["scalar"], coordinates, shapes, beta)
    gap = -upper
    assert gap == F(node["boundary_gap_lower_rational"])
    assert bhigh == F(node["boundary_response_upper_rational"])
    assert gap > 0 and (gap >= F(1, 200) or width <= gap/2)
    assert bhigh-blow <= max(F(1, 100), bhigh/4)
    resolution = node["resolution_test"]
    assert resolution["passed"] and resolution["phase_resolution_by_gap_or_width"]
    assert F(resolution["weakest_branch_upper_rational"]) == upper
    assert F(resolution["largest_frozen_budget_width_rational"]) == width
    assert F(resolution["response_width_rational"]) == bhigh-blow
    assert F(resolution["response_width_limit_rational"]) == max(F(1, 100), bhigh/4)
    return gap, bhigh


def main():
    if (EXPECTED_SOURCE_SHA256 is None or EXPECTED_COUNTS is None
            or any(value is None for value in MANDATORY_INPUTS.values())):
        raise RuntimeError("checker not frozen: final source identity and counts are pending")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    source = ROOT/SOURCE
    assert sha(source) == EXPECTED_SOURCE_SHA256
    with gzip.open(source, "rt", encoding="utf-8") as stream:
        data = json.load(stream)
    assert data["status"] == "complete boundary coverage"
    assert data["alpha"] == 0 and data["beta_cases"] == [0, 1]
    assert data["boundary_case_count"] == 18 and data["precision_bits"] == 256
    assert data["alpha_one_canonical_reference_data_used"] is False
    assert data["coverage_verified"] and data["complete_boundary_coverage"]
    assert data["uniform_central_gap_proved"]
    for key in ("pending_frontier_next_is_first", "unresolved_leaves",
                "changed_inputs", "stop_signals_received"):
        assert not data[key]
    for key in ("half_row_bound_claimed", "full_source_theorem_claimed",
                "global_filling_volume_theorem_claimed"):
        assert data[key] is False
    bindings = data["input_sha256"]
    assert len(bindings) == EXPECTED_COUNTS["input_bindings"]
    for name, digest in MANDATORY_INPUTS.items():
        assert bindings[name] == digest
    for name, digest in bindings.items():
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name
    nodes, leaves = data["nodes"], data["terminal_leaves"]
    assert len(nodes) == EXPECTED_COUNTS["nodes"]
    assert len(leaves) == EXPECTED_COUNTS["leaves"]
    assert len(nodes) == 2*len(leaves)-18
    index, buckets, accepted = {}, defaultdict(list), defaultdict(list)
    counts = Counter()
    for number, node in enumerate(nodes):
        assert node["alpha"] == 0
        key = (node["beta"], node["chart"], node["address"])
        assert key not in index and key[0] in (0, 1) and key[1] in CHARTS
        index[key] = number
        low, high = parameter_interval(key[2])
        box = image(key[1], low, high)
        assert tuple(map(F, node["parameter_interval"])) == (low, high)
        assert tuple(map(F, node["external_coordinate_box"])) == box
        assert len(key[2]) <= data["maximum_depth"] == 18
        action = node["action"]
        counts[action] += 1
        details = None
        if "reference" in node:
            details = check_reference_metadata(node, box, low, high)
        if "response" in node:
            assert node["response"]["alpha"] == 0 and node["response"]["beta"] == key[0]
        if "scalar" in node:
            assert node["scalar"]["alpha"] == 0
            assert node["scalar"]["alpha_provenance_supplied_by_driver"]
            assert node["scalar"]["beta"] == key[0]
        if action == "split":
            assert node["children"] == [key[2]+"0", key[2]+"1"]
        elif action == "excluded":
            check_geometry_exclusion(key[1], low, high, box, node["source_exclusion"])
        elif action == "excluded by certified reference domain":
            assert details is not None
            check_reference_exclusion(details, box, key[0])
        else:
            assert action == "accepted boundary estimate"
            assert details is not None
            accepted[(key[0], key[1][:2])].append(check_accepted(node, details))
    for key, number in index.items():
        node = nodes[number]
        if key[2]:
            parent = index[(key[0], key[1], key[2][:-1])]
            assert parent < number and nodes[parent]["action"] == "split"
        if node["action"] == "split":
            for child in node["children"]:
                assert (key[0], key[1], child) in index
    for leaf in leaves:
        assert leaf["alpha"] == 0
        key = (leaf["beta"], leaf["chart"], leaf["address"])
        number = leaf["node_index"]
        assert index[key] == number and nodes[number]["action"] == leaf["status"]
        assert leaf["status"] != "split"
        buckets[key[:2]].append(key[2])
    assert set(buckets) == {(beta, chart) for beta in (0, 1) for chart in CHARTS}
    coverage = []
    for (beta, chart), addresses in sorted(buckets.items()):
        ordered = sorted(addresses)
        assert len(ordered) == len(set(ordered))
        assert all(not y.startswith(x) for x, y in zip(ordered, ordered[1:]))
        assert sum((F(1, 2**len(x)) for x in ordered), F(0)) == 1
        coverage.append({
            "beta": beta, "chart": chart, "leaf_count": len(ordered),
            "normalized_mass_rational": "1", "full_tree_node_count": 2*len(ordered)-1,
            "maximum_depth": max(map(len, ordered)),
        })
    assert data["coverage"] == {
        "case_count": 18, "chart_count": 9, "cases": coverage,
        "total_frontier_leaves": len(leaves),
    }
    expected_actions = {
        "accepted boundary estimate": EXPECTED_COUNTS["accepted"],
        "excluded": EXPECTED_COUNTS["geometry_excluded"],
        "excluded by certified reference domain": EXPECTED_COUNTS["reference_excluded"],
        "split": len(leaves)-18,
    }
    assert counts == Counter(expected_actions)
    assert data["counts"]["accepted"] == EXPECTED_COUNTS["accepted"]
    assert data["counts"].get("geometry_exclusions", 0) == EXPECTED_COUNTS["geometry_excluded"]
    assert data["counts"].get("certified_reference_exclusions", 0) == EXPECTED_COUNTS["reference_excluded"]
    assert data["counts"]["reference_calls"] == sum("reference" in node for node in nodes)
    assert data["counts"]["response_calls"] == sum("response" in node for node in nodes)
    assert len(nodes) <= data["maximum_nodes"] == 12000
    assert data["counts"]["reference_calls"] <= data["maximum_references"] == 4000
    summaries, summary_keys = [], set()
    for row in data["domain_summaries"]:
        assert row["alpha"] == 0
        key = (row["beta"], row["domain"])
        assert key not in summary_keys
        summary_keys.add(key)
        values = accepted[key]
        gamma = min(x[0] for x in values)
        response = max(x[1] for x in values)
        radius = DOMAINS[int(key[1][1])][2]
        loss = radius**2/2
        deficit = gamma-loss*response
        assert row["accepted_cells"] == len(values)
        assert F(row["observed_boundary_gap_lower_rational"]) == gamma
        assert F(row["observed_response_upper_rational"]) == response
        assert F(row["disk_barrier_factor_rational"]) == loss
        assert F(row["compensated_gap_rational"]) == deficit
        assert row["valid_for_whole_domain"] and deficit > 0
        result = {
            "alpha": 0, "beta": key[0], "domain": key[1],
            "accepted_cells": len(values), "gamma_min_rational": str(gamma),
            "B_max_rational": str(response), "disk_barrier_factor_rational": str(loss),
            "corrected_gap_rational": str(deficit),
            "corrected_gap_decimal_display": float(deficit),
        }
        if CONSERVATIVE_TABLE is not None:
            lower, upper = map(F, CONSERVATIVE_TABLE[key])
            conservative = lower-loss*upper
            assert 0 < lower < gamma and response < upper and conservative > 0
            result.update({
                "conservative_gamma_lower_rational": str(lower),
                "conservative_B_upper_rational": str(upper),
                "conservative_corrected_gap_rational": str(conservative),
            })
        else:
            conservative = deficit
        if CHOSEN_COMMON_GAP is not None:
            assert 0 < F(CHOSEN_COMMON_GAP) < conservative
            result["strictly_above_chosen_common_gap"] = True
        summaries.append(result)
    assert summary_keys == {(beta, kind) for beta in (0, 1) for kind in ("k3", "k4")}
    if CONSERVATIVE_TABLE is not None:
        assert set(CONSERVATIVE_TABLE) == summary_keys
    # Check the same input bytes once more after the entire saved-data scan.
    for name, digest in bindings.items():
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name
    assert sha(source) == EXPECTED_SOURCE_SHA256
    output = {
        "status": "exact saved-data check passed", "alpha": 0,
        "source": SOURCE, "source_sha256": EXPECTED_SOURCE_SHA256,
        "checker_sha256": sha(Path(__file__)),
        "input_bindings_checked": len(bindings), "visited_nodes": len(nodes),
        "complete_chart_cases": 18, "terminal_leaves": len(leaves),
        "accepted_leaves": EXPECTED_COUNTS["accepted"],
        "strict_geometry_exclusions": EXPECTED_COUNTS["geometry_excluded"],
        "certified_reference_exclusions": EXPECTED_COUNTS["reference_excluded"],
        "all_address_images_reconstructed": True,
        "all_alpha_zero_metadata_checked": True,
        "all_accepted_reference_response_scalar_associations_checked": True,
        "all_common_product_and_strict_height_checks_recomputed": True,
        "all_candidate_minima_and_four_component_sums_checked": True,
        "all_global_gamma_B_extrema_recomputed_separately": True,
        "domain_summaries": summaries,
        "exact_minimum_corrected_gap_rational":
            str(min(F(row["corrected_gap_rational"]) for row in summaries)),
        "chosen_common_gap_rational":
            None if CHOSEN_COMMON_GAP is None else str(F(CHOSEN_COMMON_GAP)),
        "source_root_primitive_or_interval_evaluations": 0,
        "half_row_bound_claimed": False, "full_source_theorem_claimed": False,
        "global_filling_volume_theorem_claimed": False,
        "scope": "alpha0 central original comparison only; no half-row, full-source or filling theorem",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({
        "status": output["status"],
        "summaries": [(r["beta"], r["domain"], r["corrected_gap_decimal_display"])
                      for r in summaries],
        "output": str(args.output), "sha256": sha(args.output),
    }))


if __name__ == "__main__":
    main()
