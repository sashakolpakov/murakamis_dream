#!/usr/bin/env python3
"""Exclude saved node 288 by exact rectangle-to-disk distance only."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = "repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json"
PINNED = {
    DATA: "2f7640e7aefc655628b134ac50500e03b0971f2768b8f73c0df36a00b74b0f3c",
    "notes/research_mixed_second_selected_saved_cell_geometric_exclusion.md": "7cab40fc02773ffe6bc11550685a93d03ccad477eb33217066b7619f6155393c",
    "notes/research_mixed_second_selected_reference_curve.md": "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
}
NODE_INDEX = 288
ADDRESS = "0011111110111111100101"
BOX = ["115439/512000", "461773/2048000", "36243/1024000", "9063/256000"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoints(record):
    require(record.get("finite") is True, "nonfinite saved interval")
    lo, hi = F(record["lower_rational"]), F(record["upper_rational"])
    require(lo <= hi, "reversed saved endpoints")
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        require(sha(ROOT/name) == expected, "frozen input mismatch: "+name)
    data = json.loads((ROOT/DATA).read_text())
    for name, expected in data["input_sha256"].items():
        path = Path(name)
        relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
        require(relative not in bindings or bindings[relative] == expected, "conflicting binding: "+relative)
        bindings[relative] = expected
    script = str(Path(__file__).resolve().relative_to(ROOT))
    bindings[script] = sha(Path(__file__))
    for name, expected in bindings.items():
        require(sha(ROOT/name) == expected, "frozen dependency mismatch: "+name)

    require(data["stop_reason"] == "first fully evaluated scalar pair", "unexpected probe stopping rule")
    require(data["fully_evaluated_pair_node_index"] == NODE_INDEX, "wrong prescribed node")
    require(len(data["new_nodes"]) == NODE_INDEX+1, "unexpected probe length")
    node = data["new_nodes"][NODE_INDEX]
    require(node["beta"] == 0 and node["address"] == ADDRESS and node["box"] == BOX,
            "prescribed beta/address/box mismatch")
    require(node["action"] == "stop at fully evaluated scalar pair", "unexpected original action")
    require(node["reference"]["status"] == "retained", "unexpected original reference status")
    details = node["reference"]["details"]
    require(details["all_original_regularity_checks_passed"] is True, "missing original regularity")
    require(details["next_external_type_alternatives"] == [3], "unexpected old type alternatives")
    coordinate = details["reference_coordinates_before_intersection"]["c"]
    x_lo, x_hi = endpoints(coordinate["real"])
    y_lo, y_hi = endpoints(coordinate["imag"])
    expected = (F(1050214639, 4294967296), F(1331525037, 4294967296),
                F(555453115, 8589934592), F(1092931997, 8589934592))
    require((x_lo, x_hi, y_lo, y_hi) == expected, "saved full c rectangle mismatch")
    center_x, center_y, radius = F(7, 20), F(-1, 100), F(83, 1000)
    dx = max(F(0), x_lo-center_x, center_x-x_hi)
    dy = max(F(0), y_lo-center_y, center_y-y_hi)
    disk_excess = dx**2+dy**2-radius**2
    require(dx == F(858567583, 21474836480), "unexpected horizontal disk distance")
    require(dy == F(16033811523, 214748364800), "unexpected vertical disk distance")
    require(disk_excess == F(327447290086775393061, 1152921504606846976000000),
            "unexpected squared-distance witness")
    require(disk_excess > 0, "K3 disk not excluded")
    k4_ceiling = F(-1, 1000)
    k4_excess = y_lo-k4_ceiling
    require(k4_excess > 0, "K4 height not excluded")

    branches = node["scalar"]["details"]["branches"]
    require(set(branches) == {"forced", "factorial"}, "missing original scalar branch")
    original_budgets = {}
    for label, branch in branches.items():
        lo, hi = endpoints(branch["budget"])
        require(lo < 0 < hi, "unexpected original scalar enclosure")
        original_budgets[label] = branch["budget"]
    frontier = data["pending_frontier_stack_next_is_last"]
    require(len(frontier) == 349 and not data["depth_limit_leaves"], "unexpected remaining frontier")
    require(not any(item["beta"] == 0 and item["address"] == ADDRESS for item in frontier),
            "prescribed scalar leaf was pending")
    require(sum(leaf["beta"] == 0 and leaf["address"] == ADDRESS
                and leaf["status"] == "scalar pair evaluated" for leaf in data["new_terminal_leaves"]) == 1,
            "missing original terminal leaf")
    for name, expected_hash in bindings.items():
        require(sha(ROOT/name) == expected_hash, "input changed during saved-data check: "+name)
    record = {
        "status": "prescribed saved scalar cell excluded by necessary external geometry",
        "source_record": DATA, "source_record_sha256": PINNED[DATA],
        "source_node_index": NODE_INDEX, "source_node_canonical_sha256": canonical_hash(node),
        "alpha": 1, "beta": 0, "address": ADDRESS, "box": BOX,
        "saved_full_external_coordinate_unchanged": coordinate,
        "type_three_disk": {"center_real_rational": str(center_x), "center_imag_rational": str(center_y),
            "radius_rational": str(radius), "rectangle_horizontal_distance_rational": str(dx),
            "rectangle_vertical_distance_rational": str(dy),
            "squared_distance_minus_radius_squared_rational": str(disk_excess), "strictly_excluded": True},
        "type_four_height": {"necessary_upper_rational": str(k4_ceiling),
            "saved_lower_rational": str(y_lo), "strict_positive_excess_rational": str(k4_excess),
            "strictly_excluded": True},
        "both_next_external_types_excluded": True,
        "original_reference_status_unchanged": node["reference"]["status"],
        "original_scalar_status_unchanged": node["scalar"]["status"],
        "original_scalar_budgets_unchanged": original_budgets,
        "new_necessary_exclusion": {"beta": 0, "address": ADDRESS, "dyadic_mass": str(F(1, 2**len(ADDRESS)))},
        "unchanged_pending_frontier_count": len(frontier),
        "unchanged_pending_frontier_canonical_sha256": canonical_hash(frontier),
        "original_records_modified": False, "replacement_cell_selected": False,
        "main_main_gap_claimed": False, "half_row_bound_claimed": False,
        "actual_word_realization_claimed": False, "global_theorem_claimed": False,
        "reference_evaluations": 0, "polynomial_evaluations": 0, "logarithm_evaluations": 0,
        "primitive_evaluations": 0, "conjugate_evaluations": 0, "root_evaluations": 0,
        "finite_source_evaluations": 0, "subdivisions": 0, "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "result_sha256": sha(args.output),
        "bindings": len(bindings), "disk_squared_excess_rational": str(disk_excess),
        "type_four_height_excess_rational": str(k4_excess)}))


if __name__ == "__main__":
    main()
