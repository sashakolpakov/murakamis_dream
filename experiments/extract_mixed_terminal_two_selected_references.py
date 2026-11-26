#!/usr/bin/env python3
"""Fixed saved-only projection of the two complete canonical reference banks.

No analytic, root, source, backward-shape or scalar-gain evaluator is imported.
The original audits supply analytic/exclusion validity. This program checks
payload associations and exact trees, then projects rational linear endpoints.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_two_selected_reference_bank_transfer.md"
BANKS = {
    0: "repro/results/research-mixed-second-selected-first-three-boundary-reference-bank.json.gz",
    1: "repro/results/research-mixed-second-selected-boundary-reference-bank.json",
}
AUDITS = {
    0: "repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json",
    1: "repro/results/research-mixed-second-selected-external-boundary-saved-audit.json",
}
EXTRACTORS = {
    0: "experiments/extract_mixed_second_selected_first_three_boundary_references.py",
    1: "experiments/extract_mixed_second_selected_boundary_references.py",
}
AUDITORS = {
    0: "experiments/check_mixed_second_selected_first_three_external_boundary_record.py",
    1: "experiments/check_mixed_second_selected_external_boundary_record.py",
}
PINNED = {
    PROOF: "eaf351d6f4bab35fbdec81b6642ba72b5777b582caafced26788d31908bf1223",
    BANKS[0]: "4b0bfa3cb2bfb68b622487c390879312b7d0832a056f03c3675a38cedeb8c323",
    BANKS[1]: "3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb",
    AUDITS[0]: "88d8f8177a439f4268980e7467fffc576b558776c22f2a6067361d0ab8b6a047",
    AUDITS[1]: "38971e851765e3a9df8be5aed447bf036110e7dc0a34e5c4885e5f59f3825f23",
    EXTRACTORS[0]: "0367c8d65f99b6ecd077928b03bc38aae3b432f21815ac18294c117cb015d643",
    EXTRACTORS[1]: "1264b86d37f34719ff8e8363abd86723f8355dfa122f1277778d20c897abc0e4",
    AUDITORS[0]: "9e53d3b6f9278289b7b2ba3ab3107b584d25f498d6a61dc5108ebb6c754315db",
    AUDITORS[1]: "984cf3e88275646106b5cb6da006771611459a23f6e7d25167cef80d5f4d026a",
    "notes/research_mixed_terminal_two_selected_reference_reconstruction.md":
        "2d81e3ee8e09c1cddf83a0b0579252d67f2b9a2ffd04f2e6b821dcf2b9d96f5a",
    "notes/research_mixed_prefix_residual_localization.md":
        "5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434",
    "notes/research_mixed_second_selected_external_boundary_charts.md":
        "afb4a56ad99c2100285e791e1a1fd8549b40bb40004cf4ddc1df1b5b7a5dacba",
}
MAPPING = {"r": "b", "b": "v", "s": "z", "a": "u"}
H = F(1, 100)
CHARTS = {
    "k3_circle_left", "k3_circle_right", "k3_lower_chord", "k3_upper_chord",
    "k3_oblique_chord", "k4_circle_left", "k4_circle_right",
    "k4_lower_chord", "k4_upper_chord",
}
EXPECTED = {
    0: {"all_accepted": 1419, "all_geometry": 1532, "all_excluded": 113,
        "selected_accepted": 637, "selected_excluded": 55, "k3": 310, "k4": 327},
    1: {"all_accepted": 1431, "all_geometry": 1545, "all_excluded": 114,
        "selected_accepted": 646, "selected_excluded": 56, "k3": 316, "k4": 330},
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2**20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def relative(name):
    p = Path(name)
    return str((p if p.is_absolute() else ROOT/p).resolve().relative_to(ROOT))


def merge(bindings, additions):
    for name, digest in additions.items():
        name = relative(name)
        require(name not in bindings or bindings[name] == digest,
                "conflicting inherited binding: "+name)
        bindings[name] = digest


def changes(bindings):
    bad = []
    for name, digest in bindings.items():
        path = ROOT/name
        if not path.exists() or sha(path) != digest:
            bad.append(name)
    return bad


def read_json(name):
    p = ROOT/name
    with (gzip.open(p, "rt") if p.suffix == ".gz" else p.open()) as stream:
        return json.load(stream)


def interval(record):
    require(record.get("finite") is True, "nonfinite saved coordinate")
    lo, hi = F(record["lower_rational"]), F(record["upper_rational"])
    require(lo <= hi, "reversed exact interval")
    return lo, hi


def address_interval(address):
    require(isinstance(address, str) and not set(address)-set("01"), "invalid address")
    lo, hi = F(-1), F(1)
    for bit in address:
        mid = (lo+hi)/2
        if bit == "0":
            hi = mid
        else:
            lo = mid
    return lo, hi


def witness(epsilon, row, theta=None):
    out = {key: row[key] for key in (
        "source_node_index", "chart", "address", "external_domain",
        "compact_payload_canonical_sha256")}
    out["epsilon"] = epsilon
    if theta is not None:
        out["theta_rational"] = str(theta)
    return out


def bound(items):
    require(bool(items), "empty projection family")
    low = min(items, key=lambda item: item[0][0])
    high = max(items, key=lambda item: item[0][1])
    return {"finite": True, "lower_rational": str(low[0][0]),
            "upper_rational": str(high[0][1]), "lower_witness": low[1],
            "upper_witness": high[1]}


def hull(records):
    low = min(records, key=lambda item: F(item["lower_rational"]))
    high = max(records, key=lambda item: F(item["upper_rational"]))
    return {"finite": True, "lower_rational": low["lower_rational"],
            "upper_rational": high["upper_rational"],
            "lower_witness": low["lower_witness"], "upper_witness": high["upper_witness"]}


def linear(row, coefficients, part, constant=F(0)):
    lo = hi = constant
    for name, coefficient in coefficients.items():
        left, right = interval(row["coordinates"][MAPPING[name]][part])
        lo += coefficient*(left if coefficient >= 0 else right)
        hi += coefficient*(right if coefficient >= 0 else left)
    return lo, hi


def project(epsilon, domain, rows):
    coordinates, sums, slabs = {}, {}, []
    for name in MAPPING:
        coordinates[name] = {
            part: bound([(linear(row, {name: F(1)}, part), witness(epsilon, row))
                         for row in rows]) for part in ("real", "imag")}
    for name, form in (("rb", {"r": F(1), "b": F(1)}),
                       ("sb", {"s": F(1), "b": F(1)}),
                       ("sa", {"s": F(1), "a": F(1)})):
        sums[name] = {part: bound([(linear(row, form, part), witness(epsilon, row))
                                  for row in rows]) for part in ("real", "imag")}
    for index in range(16):
        endpoints = (F(index, 16), F(index+1, 16))
        arguments = {}
        for key, neighbor, lifted in (
                ("b", None, "b"), ("rb", "r", "b"),
                ("sb", "s", "b"), ("sa", "s", "a")):
            real_form = {lifted: F(1)}
            if neighbor:
                real_form[neighbor] = F(1)
            real = bound([(linear(row, real_form, "real"), witness(epsilon, row))
                          for row in rows])
            imag_items = []
            for row in rows:
                for theta in endpoints:
                    imag_form = {lifted: 1-theta}
                    if neighbor:
                        imag_form[neighbor] = F(1)
                    imag_items.append((linear(row, imag_form, "imag", theta*H),
                                       witness(epsilon, row, theta)))
            arguments[key] = {"real": real, "imag": bound(imag_items)}
        slabs.append({"index": index, "theta_rational": list(map(str, endpoints)),
                      "arguments": arguments})
    return {"epsilon": epsilon, "external_domain": domain,
            "accepted_reference_count": len(rows), "coordinates": coordinates,
            "coordinate_sums": sums, "slabs": slabs}


def unite(epsilon, groups):
    result = {"epsilon": epsilon, "external_domains": ["k3", "k4"],
              "accepted_reference_count": sum(g["accepted_reference_count"] for g in groups)}
    for kind in ("coordinates", "coordinate_sums"):
        result[kind] = {
            name: {part: hull([g[kind][name][part] for g in groups])
                   for part in ("real", "imag")} for name in groups[0][kind]}
    result["slabs"] = []
    for index in range(16):
        slab = {"index": index, "theta_rational": groups[0]["slabs"][index]["theta_rational"],
                "arguments": {}}
        for key in ("b", "rb", "sb", "sa"):
            slab["arguments"][key] = {
                part: hull([g["slabs"][index]["arguments"][key][part] for g in groups])
                for part in ("real", "imag")}
        result["slabs"].append(slab)
    return result


def audit_bank(epsilon, bank, audit, result):
    expected = EXPECTED[epsilon]
    require(bank["status"] == "compact projection of the completed audited boundary references",
            "bank is not the completed projection")
    require(bank["alpha"] == epsilon and bank["beta_cases"] == [0, 1], "wrong bank flags")
    require(bank["precision_bits"] == 256, "wrong inherited precision")
    require(not bank["pending_frontier"] and not bank["unresolved_frontier"], "unfinished bank")
    require(bank["scope"]["individual_height_extrema_extend_harmonically_on_each_fixed_beta_K"]
            and not bank["scope"]["interior_joint_correlations_claimed"], "wrong bank scope")
    require(bank["saved_data_audit"] == AUDITS[epsilon]
            and bank["saved_data_audit_sha256"] == PINNED[AUDITS[epsilon]], "wrong saved audit")
    require(audit["status"] == ("exact saved-data check passed" if epsilon == 0
                               else "independent exact saved-data audit passed"), "failed old audit")
    require(audit["source"] == bank["source"] and audit["source_sha256"] == bank["source_sha256"],
            "old audit/source mismatch")
    require(audit["checker_sha256"] == PINNED[AUDITORS[epsilon]], "wrong old auditor")
    require(audit["complete_chart_cases"] == 18 and audit.get("certified_reference_exclusions", 0) == 0,
            "wrong original chart coverage or reference exclusions")
    require(audit["accepted_leaves"] == expected["all_accepted"]
            and audit["strict_geometry_exclusions"] == expected["all_excluded"], "old audit counts")
    require(bank["accepted_reference_count"] == len(bank["accepted_references"])
            == expected["all_accepted"], "bank accepted count")
    require(bank["terminal_geometry_count"] == len(bank["terminal_geometry"])
            == expected["all_geometry"], "bank terminal count")
    require(bank["strict_geometry_exclusions"] == expected["all_excluded"], "bank exclusion count")
    require(bank["input_sha256"].get(EXTRACTORS[epsilon]) == PINNED[EXTRACTORS[epsilon]],
            "wrong old extractor")
    require(bank["coverage"]["case_count"] == 18 and bank["coverage"]["chart_count"] == 9,
            "wrong bank coverage inventory")

    references = bank["accepted_references"]
    selected = [(index, row) for index, row in enumerate(references) if row["beta"] == 1]
    selected_ids = set()
    for index, row in selected:
        require(row["status"] == "accepted boundary estimate", "wrong reference status")
        require(row.get("alpha", epsilon) == epsilon, "wrong reference alpha")
        payload = dict(row)
        digest = payload.pop("compact_payload_canonical_sha256")
        require(canonical(payload) == digest, "changed compact reference payload")
        require(row["external_domain"] in ("k3", "k4")
                and row["chart"].startswith(row["external_domain"]+"_"), "wrong domain association")
        require(row["response"]["status"] == "enclosed"
                and row["response"]["height_conditions_verified"]
                and row["response"]["common_prefix_product_verified"], "missing original guards")
        require(row["source_node_index"] not in selected_ids, "duplicate selected source node")
        selected_ids.add(row["source_node_index"])
        for old_name in MAPPING.values():
            for part in ("real", "imag"):
                interval(row["coordinates"][old_name][part])
        result["reference_associations"].append({
            "epsilon": epsilon, "bank_accepted_index": index,
            **{key: row[key] for key in (
                "source_node_index", "source_node_canonical_sha256",
                "source_reference_certificate_canonical_sha256",
                "compact_payload_canonical_sha256", "external_domain", "chart",
                "address", "parameter_interval", "external_coordinate_box")}})

    by_chart, accepted_ids = defaultdict(list), set()
    exclusions = 0
    for leaf in bank["terminal_geometry"]:
        if leaf["beta"] != 1:
            continue
        require(leaf["chart"] in CHARTS, "unknown selected chart")
        require(tuple(map(F, leaf["parameter_interval"])) == address_interval(leaf["address"]),
                "address/parameter mismatch")
        by_chart[leaf["chart"]].append(leaf["address"])
        if leaf["status"] == "accepted boundary estimate":
            row = references[leaf["accepted_reference_index"]]
            for key in ("beta", "chart", "address", "external_domain", "parameter_interval",
                        "external_coordinate_box", "source_node_index", "source_node_canonical_sha256"):
                require(row[key] == leaf[key], "terminal/reference association: "+key)
            require(row["source_node_index"] not in accepted_ids, "repeated terminal reference")
            accepted_ids.add(row["source_node_index"])
        elif leaf["status"] == "excluded":
            ex = leaf["source_exclusion"]
            require(ex["criterion"] in ("outside_typed_disk", "below_lower_height",
                                        "above_upper_height", "above_oblique_halfplane"),
                    "not an inherited geometric exclusion")
            require(F(ex["strict_margin_rational"]) > 0, "non-strict old exclusion")
            require(ex["chart"] == leaf["chart"] and ex["parameter_interval"] == leaf["parameter_interval"]
                    and ex["coordinate_box"] == leaf["external_coordinate_box"], "exclusion association")
            exclusions += 1
        else:
            raise ValueError("reference exclusion or unresolved selected leaf")
        result["terminal_geometry"].append({"epsilon": epsilon, **leaf})
    require(accepted_ids == selected_ids and len(selected) == expected["selected_accepted"],
            "selected accepted inventory")
    require(exclusions == expected["selected_excluded"], "selected exclusion inventory")
    require(set(by_chart) == CHARTS, "missing selected chart")
    saved_coverage = {x["chart"]: x for x in bank["coverage"]["cases"] if x["beta"] == 1}
    require(set(saved_coverage) == CHARTS, "old selected coverage inventory")
    for chart, addresses in sorted(by_chart.items()):
        addresses.sort()
        require(len(addresses) == len(set(addresses)), "duplicate tree leaf")
        require(not any(b.startswith(a) for a, b in zip(addresses, addresses[1:])), "overlapping tree")
        require(sum((F(1, 2**len(a)) for a in addresses), F(0)) == 1, "incomplete tree")
        require(saved_coverage[chart]["leaf_count"] == len(addresses)
                and F(saved_coverage[chart]["normalized_mass_rational"]) == 1, "old tree summary")
        result["coverage"].append({"epsilon": epsilon, "chart": chart,
                                   "leaf_count": len(addresses), "normalized_mass_rational": "1",
                                   "addresses": addresses})
    groups = []
    for domain in ("k3", "k4"):
        rows = [row for _, row in selected if row["external_domain"] == domain]
        require(len(rows) == expected[domain], "selected domain count")
        group = project(epsilon, domain, rows)
        old = bank["height_extrema"]["by_beta_and_external_domain"]["1_"+domain]
        require(old["beta"] == 1 and old["external_domain"] == domain
                and old["accepted_reference_count"] == len(rows), "old height group association")
        for new_name, old_name in (("b", "h_v"), ("r", "h_b")):
            projected = group["coordinates"][new_name]["imag"]
            require(all(F(projected[key]) == F(old[old_name][key])
                        for key in ("lower_rational", "upper_rational")), "old height summary mismatch")
        blo, bhi = interval(group["coordinates"]["b"]["imag"])
        require(F(-77, 1250) < blo and bhi < F(-211, 5000), "proposed b-height guard failed")
        group["new_b_height_guard"] = {"lower_rational": "-77/1250", "upper_rational": "-211/5000",
                                      "strictly_verified": True}
        groups.append(group)
        result["domain_cases"].append(group)
    return unite(epsilon, groups)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings = dict(PINNED)
    result = {"status": "not completed", "proof_path": PROOF, "proof_sha256": PINNED.get(PROOF),
              "checker_path": str(Path(__file__).resolve().relative_to(ROOT)),
              "checker_sha256": sha(Path(__file__).resolve()), "height_rational": "1/100",
              "coordinate_mapping_new_to_old": MAPPING, "cases": [], "domain_cases": [],
              "coverage": [], "reference_associations": [], "terminal_geometry": [],
              "active_epsilon": None, "pending_epsilon": [0, 1],
              "input_sha256": bindings, "changed_inputs": []}
    try:
        required = {PROOF, *BANKS.values(), *AUDITS.values(), *EXTRACTORS.values(), *AUDITORS.values()}
        require(required <= set(PINNED) and all(PINNED.values()), "unfrozen projection pins")
        require(not changes(bindings), "changed direct projection input")
        banks = {epsilon: read_json(path) for epsilon, path in BANKS.items()}
        audits = {epsilon: read_json(path) for epsilon, path in AUDITS.items()}
        for bank in banks.values():
            require(bank["input_sha256"].get(bank["source"]) == bank["source_sha256"],
                    "bank/source binding mismatch")
            merge(bindings, bank["input_sha256"])
        bindings[result["checker_path"]] = result["checker_sha256"]
        require(not changes(bindings), "changed inherited input before projection")
        for epsilon in (0, 1):
            result["active_epsilon"] = epsilon
            result["cases"].append(audit_bank(epsilon, banks[epsilon], audits[epsilon], result))
            result["pending_epsilon"].remove(epsilon)
            result["active_epsilon"] = None
        require(len(result["coverage"]) == 18 and len(result["reference_associations"]) == 1283
                and len(result["terminal_geometry"]) == 1394, "wrong final projection inventory")
        require(sum(len(s["arguments"]) for c in result["cases"] for s in c["slabs"]) == 128,
                "wrong union argument inventory")
        result["case_canonical_sha256"] = {str(c["epsilon"]): canonical(c) for c in result["cases"]}
        result["status"] = "passed"
    except BaseException as exc:
        result["status"] = "failed"
        result["error"] = {"type": type(exc).__name__, "message": str(exc)}
    result["changed_inputs"] = changes(bindings)
    if result["changed_inputs"]:
        result["status"] = "failed"
        result["error"] = {"type": "InputChanged", "message": "saved projection bindings changed"}
    result["input_sha256"] = dict(sorted(bindings.items()))
    result["all_boundaries_complete"] = result["status"] == "passed"
    result["reference_counts"] = {str(c["epsilon"]): c["accepted_reference_count"]
                                  for c in result["cases"]}
    result["inherited_geometry_and_analytic_certificates_replayed"] = False
    result["exact_payload_tree_and_linear_projection_checks_completed"] = result["status"] == "passed"
    result["analytic_evaluations"] = 0
    result["root_evaluations"] = 0
    result["gain_evaluations"] = 0
    result["new_parameter_cells"] = 0
    result["new_source_or_budget_sign_claimed"] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, sort_keys=True, separators=(",", ":"))
        stream.write("\n")
    print(json.dumps({"status": result["status"], "input_bindings": len(bindings),
                      "completed_cases": len(result["cases"]), "output_sha256": sha(args.output)}))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
