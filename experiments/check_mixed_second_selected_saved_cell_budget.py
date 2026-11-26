#!/usr/bin/env python3
"""UNEXECUTED SUPERSEDED DRAFT: node 288 is geometrically excluded.

The proposed sharper scalar recombination below was never executed.
The saved-coordinate disk exclusion supersedes this diagnostic; these
formulas cannot provide evidence from an admissible reference cell.

No repository imports, flint, reference evaluation, primitive evaluation,
optimization, source root, subdivision, or replacement-cell selection.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = "repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json"
PINNED = {
    DATA: "2f7640e7aefc655628b134ac50500e03b0971f2768b8f73c0df36a00b74b0f3c",
    "notes/research_mixed_second_selected_directional_budget.md": "f74ddbea9c59685e7c6d343c7b41490c1c81520d09016664f274ff003331efd2",
    "notes/research_mixed_second_selected_central_budget.md": "c839f134024ccd2ad0a95ce81ed8cd16fb0bcefb9d508a347c9278c84bd3f21d",
}
NODE_INDEX = 288
ADDRESS = "0011111110111111100101"
BOX = ["115439/512000", "461773/2048000", "36243/1024000", "9063/256000"]
GAP = F(1, 2000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoints(record):
    require(record.get("finite") is True, "saved scalar is not finite")
    lo, hi = F(record["lower_rational"]), F(record["upper_rational"])
    require(lo <= hi, "reversed saved scalar endpoints")
    return lo, hi


def main():
    raise RuntimeError("superseded unexecuted draft: saved node 288 is geometrically excluded")
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
        require(relative not in bindings or bindings[relative] == expected,
                "conflicting inherited binding: "+relative)
        bindings[relative] = expected
    script = str(Path(__file__).resolve().relative_to(ROOT))
    bindings[script] = sha(Path(__file__))
    for name, expected in bindings.items():
        require(sha(ROOT/name) == expected, "frozen dependency mismatch: "+name)

    require(data["stop_reason"] == "first fully evaluated scalar pair", "unexpected source stopping rule")
    require(data["fully_evaluated_pair_node_index"] == NODE_INDEX, "unexpected saved node")
    require(len(data["new_nodes"]) == NODE_INDEX+1, "saved scalar pair was not final")
    node = data["new_nodes"][NODE_INDEX]
    require(node["beta"] == 0 and node["address"] == ADDRESS and node["box"] == BOX,
            "prescribed beta/address/box mismatch")
    require(node["action"] == "stop at fully evaluated scalar pair", "unexpected saved node action")
    require(node["reference"]["status"] == "retained", "saved reference not retained")
    reference = node["reference"]["details"]
    require(reference["all_original_regularity_checks_passed"] is True, "original regularity not certified")
    require(reference["next_external_type_alternatives"] == [3], "unexpected next-type alternatives")
    coordinates = reference["reference_coordinates_after_necessary_intersection"]
    scalar = node["scalar"]["details"]
    branches = scalar["branches"]
    require(set(branches) == {"forced", "factorial"}, "missing finite branch")
    require(branches["forced"]["nu"] == 0 and branches["factorial"]["nu"] == 1,
            "Fourier branch mismatch")
    require(branches["forced"]["selected_gain"]["target_interval"] == ["2/5", "9/20"],
            "wrong forced selected domain")
    require(branches["factorial"]["selected_gain"]["target_interval"] == ["11/50", "9/20"],
            "wrong factorial selected domain")
    for branch in branches.values():
        endpoints(branch["budget"])
        require(branch["selected_gain_keeps_its_sign"] is True, "selected signed gain was discarded")

    conditions = []
    def condition(label, lhs, relation, rhs):
        lhs, rhs = F(lhs), F(rhs)
        passed = {"<=": lhs <= rhs, "<": lhs < rhs, ">": lhs > rhs, ">=": lhs >= rhs}[relation]
        conditions.append({"label": label, "left_rational": str(lhs), "relation": relation,
                           "right_rational": str(rhs), "passed": passed})
        require(passed, "sharper-bound hypothesis failed: "+label)

    u_lo, u_hi = endpoints(coordinates["u"]["real"])
    hu_lo, hu_hi = endpoints(coordinates["u"]["imag"])
    v_lo, v_hi = endpoints(coordinates["v"]["real"])
    hv_lo, hv_hi = endpoints(coordinates["v"]["imag"])
    z_lo, z_hi = endpoints(coordinates["z"]["real"])
    c_lo, c_hi = endpoints(coordinates["z"]["imag"])
    A_lo, A_hi = endpoints(scalar["scalars"]["A"])
    d_lo, d_hi = endpoints(scalar["scalars"]["d"])
    D_lo, D_hi = endpoints(branches["factorial"]["D_nu"])
    _, g_zH_hi = endpoints(scalar["scalars"]["g_zH_real"])
    _, forced_selected_hi = endpoints(branches["forced"]["selected_gain"]["value"])
    condition("left index lower real", u_lo, ">=", F(5, 16))
    condition("left index upper real", u_hi, "<=", F(63, 200))
    condition("left index absolute height", max(abs(hu_lo), abs(hu_hi)), "<=", F(9, 200))
    condition("positive left force", A_lo, ">", 0)
    condition("left force upper", A_hi, "<=", F(33, 200))
    condition("right index lower real", v_lo, ">=", F(1, 3))
    condition("right index upper real", v_hi, "<=", F(3, 8))
    condition("right index absolute height", max(abs(hv_lo), abs(hv_hi)), "<=", F(1, 50))
    condition("positive downward right force", d_lo, ">", 0)
    condition("selected reference lower real", z_lo, ">=", F(11, 50))
    condition("selected reference upper real", z_hi, "<=", F(7, 25))
    condition("negative original selected height", c_hi, "<", 0)
    condition("negative factorial selected force", D_hi, "<", 0)

    # These constants and their domains are proved in the pinned elementary note.
    delta_hi = F(1, 100)-c_lo
    vertical_hi = F(33, 5)*delta_hi**2
    left_hi = F(2691, 204800)
    right_mu_lo = F(471, 265)
    right_hi = d_hi**2/(2*right_mu_lo)
    factorial_selected_hi = D_lo**2/10
    factorial_T_hi = vertical_hi-F(157, 2500)
    forced_T_hi = vertical_hi+g_zH_hi
    new_budgets = {
        "factorial": factorial_T_hi+left_hi+right_hi+factorial_selected_hi,
        "forced": forced_T_hi+left_hi+right_hi+forced_selected_hi,
    }
    results = {}
    for label, upper in new_budgets.items():
        condition(label+" sharper main/main upper", upper, "<", -GAP)
        results[label] = {
            "upper_rational": str(upper), "strictly_below_minus_one_over_2000": True,
            "margin_beyond_one_over_2000_rational": str(-GAP-upper),
            "original_saved_budget_unchanged": branches[label]["budget"],
            "original_saved_strict_negativity_flag_unchanged": branches[label]["strictly_below_zero"],
        }

    for name, expected in bindings.items():
        require(sha(ROOT/name) == expected, "input changed during saved-data check: "+name)
    record = {
        "status": "both one-cell main/main budgets strictly below -1/2000",
        "source_record": DATA, "source_record_sha256": PINNED[DATA],
        "source_node_index": NODE_INDEX, "source_node_canonical_sha256": canonical_hash(node),
        "alpha": 1, "beta": 0, "address": ADDRESS, "box": BOX,
        "scope": "main/main central phases on this saved necessary-reference cell only",
        "verified_hypotheses": conditions,
        "recombination": {
            "height_increment_upper_rational": str(delta_hi),
            "vertical_coefficient_upper_rational": "33/5",
            "vertical_upper_rational": str(vertical_hi),
            "factorial_fourier_credit_lower_rational": "157/2500",
            "forced_g_zH_upper_rational": str(g_zH_hi),
            "factorial_T_upper_rational": str(factorial_T_hi),
            "forced_T_upper_rational": str(forced_T_hi),
            "left_gain_upper_rational": str(left_hi),
            "right_curvature_lower_rational": str(right_mu_lo),
            "right_force_upper_rational": str(d_hi),
            "right_gain_upper_rational": str(right_hi),
            "factorial_selected_force_lower_rational": str(D_lo),
            "factorial_selected_gain_upper_rational": str(factorial_selected_hi),
            "forced_selected_gain_saved_upper_rational": str(forced_selected_hi),
        },
        "branch_results": results, "candidate_gap_rational": str(GAP),
        "saved_coordinates_unchanged": coordinates,
        "saved_scalar_components_unchanged": scalar,
        "original_records_modified": False, "whole_frontier_discharged": False,
        "half_row_bound_claimed": False, "actual_word_realization_claimed": False,
        "reference_evaluations": 0, "primitive_evaluations": 0,
        "conjugate_evaluations": 0, "root_evaluations": 0,
        "finite_source_evaluations": 0, "subdivisions": 0,
        "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "result_sha256": sha(args.output),
        "bindings": len(bindings), "branch_upper_rationals": {
            label: row["upper_rational"] for label, row in results.items()}}))


if __name__ == "__main__":
    main()
