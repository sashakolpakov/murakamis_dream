#!/usr/bin/env python3
"""Exact saved-data audit of the complete double-selection tangent pass.

No source, root, optimizer, primitive, or interval provider is imported.
The certified bank supplies reference validity; this checks all recorded
rational support calculations and their separate global aggregation.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "repro/results/research-mixed-double-selected-tangent-boundary-attempt01.json.gz"
BANK = "repro/results/research-mixed-second-selected-boundary-reference-bank.json"
PINNED = {
    SOURCE: "7558c95df3e34d43f8f3e2177ac3768617a50d63864b9a98c329c65639dce61e",
    BANK: "3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb",
}
NAMES = ("e", "a", "u", "z", "v", "b")
P = (F(11, 50), F(9, 20))
DOMAINS = {
    "k3": (F(7, 20), -F(1, 100), F(83, 1000), -F(9, 125), F(17, 250)),
    "k4": (F(3, 10), -F(13, 250), F(3, 50), -F(27, 250), -F(1, 1000)),
}
CHARTS = {
    "k3_circle_left": ("k3", -1), "k3_circle_right": ("k3", 1),
    "k4_circle_left": ("k4", -1), "k4_circle_right": ("k4", 1),
    "k3_lower_chord": ("k3", F(7, 20), -F(9, 125), F(83, 1000), F(0)),
    "k3_upper_chord": ("k3", F(7, 20), F(17, 250), F(83, 1000), F(0)),
    "k3_oblique_chord": ("k3", F(301, 500), -F(1, 500), F(21, 100), F(7, 100)),
    "k4_lower_chord": ("k4", F(3, 10), -F(27, 250), F(3, 50), F(0)),
    "k4_upper_chord": ("k4", F(3, 10), -F(1, 1000), F(3, 50), F(0)),
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        if not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("unfinished binding: " + name)
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name


def interval(row):
    assert row.get("finite") is True
    lo, hi = F(row["lower_rational"]), F(row["upper_rational"])
    assert lo <= hi
    return lo, hi


def contained(row, bounds):
    lo, hi = interval(row)
    assert bounds[0] <= lo <= hi <= bounds[1]
    return lo, hi


def parameter(address):
    assert set(address) <= {"0", "1"}
    lo, hi = F(-1), F(1)
    for digit in address:
        mid = (lo+hi)/2
        lo, hi = (lo, mid) if digit == "0" else (mid, hi)
    return lo, hi


def affine(center, slope, lo, hi):
    values = (center+slope*lo, center+slope*hi)
    return min(values), max(values)


def image(chart, param):
    data = CHARTS[chart]
    domain = DOMAINS[data[0]]
    lo, hi = param
    if len(data) == 5:
        _, x, y, dx, dy = data
        return (*affine(x, dx, lo, hi), *affine(y, dy, lo, hi))
    near = F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))
    far = max(abs(lo), abs(hi))
    real = ((1-far*far)/(1+far*far), (1-near*near)/(1+near*near))
    imag = (2*lo/(1+lo*lo), 2*hi/(1+hi*hi))
    scale = data[1]*domain[2]
    return (*affine(domain[0], scale, *real), *affine(domain[1], scale, *imag))


def exclusion(row, param, box):
    witness = row["source_exclusion"]
    chart = CHARTS[row["chart"]]
    cx, cy, radius, hlo, hhi = DOMAINS[chart[0]]
    xlo, xhi, ylo, yhi = box
    assert witness["chart"] == row["chart"] and witness["domain"] == chart[0]
    assert tuple(map(F, witness["parameter_interval"])) == param
    assert tuple(map(F, witness["coordinate_box"])) == box
    criterion = witness["criterion"]
    if criterion == "below_lower_height":
        margin = hlo-yhi
    elif criterion == "above_upper_height":
        margin = ylo-hhi
    elif criterion == "above_oblique_halfplane":
        assert chart[0] == "k3"
        lower = (affine(chart[1]-3*chart[2], chart[3]-3*chart[4], *param)[0]
                 if len(chart) == 5 else xlo-3*yhi)
        margin = lower-F(76, 125)
    elif criterion == "outside_typed_disk":
        assert len(chart) == 5
        _, x, y, dx, dy = chart
        x, y = x-cx, y-cy
        a, b = dx*dx+dy*dy, 2*(x*dx+y*dy)
        t = param[0] if a == 0 else min(param[1], max(param[0], -b/(2*a)))
        distance = (x+dx*t)**2+(y+dy*t)**2
        margin = distance-radius*radius
        assert F(witness["details"]["minimizing_parameter"]) == t
        assert F(witness["details"]["squared_distance_minimum"]) == distance
        assert F(witness["details"]["radius_squared"]) == radius*radius
    else:
        raise AssertionError("unknown geometric exclusion")
    assert margin > 0 and F(witness["strict_margin_rational"]) == margin


def target_box(beta, cap, right):
    result = [(F(27, 100), F(49, 100)), P, (F(1, 8), F(1, 2)), P,
              (F(3, 20) if beta == 0 else F(1, 8), F(1, 2)), P]
    if cap == "left":
        result[0] = (F(27, 100), F(27, 100))
    if right == "half":
        result[4] = (F(1, 2), F(1, 2))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    verify(PINNED)
    with gzip.open(ROOT/SOURCE, "rt") as stream:
        source = json.load(stream)
    bank = json.loads((ROOT/BANK).read_text())
    verify(bank["input_sha256"])
    verify(source["input_sha256"])
    assert all(source["input_sha256"].get(k) == v for k, v in bank["input_sha256"].items())
    assert source["input_sha256"][BANK] == PINNED[BANK]
    assert source["status"] == "complete saved-boundary evaluation" and source["diagnostic"] is False
    assert source["precision_bits"] == 192 and source["reference_count"] == 1431
    assert not source["unresolved"] and not source["changed_inputs"]
    for name in ("new_source_roots", "parameter_subdivisions", "finite_quantum_sums"):
        assert source[name] == 0
    assert bank["alpha"] == 1 and bank["beta_cases"] == [0, 1]
    assert not bank["pending_frontier"] and not bank["unresolved_frontier"]
    refs = bank["accepted_references"]
    geometry = bank["terminal_geometry"]
    assert len(refs) == 1431 and len(geometry) == 1545
    lookup = {r["source_node_index"]: r for r in refs}
    assert len(lookup) == len(refs)
    height_groups = defaultdict(list)
    strongest_private_height = True
    for r in refs:
        payload = dict(r)
        assert canonical_sha({k: v for k, v in payload.items() if k != "compact_payload_canonical_sha256"}) == r["compact_payload_canonical_sha256"]
        response = r["response"]
        assert response["status"] == "enclosed"
        assert response["height_conditions_verified"] and response["common_prefix_product_verified"]
        assert interval(response["details"]["right_product_modulus"])[0] >= 0
        coordinates = r["coordinates"]
        er = contained(coordinates["e"]["real"], (F(27, 100), F(49, 100)))
        eh = contained(coordinates["e"]["imag"], (-F(11, 200), F(1, 25)))
        strongest_private_height &= -F(51, 1000) <= eh[0] <= eh[1] <= -F(19, 1000)
        contained(coordinates["u"]["real"], (F(1, 8), F(1, 2)))
        contained(coordinates["u"]["imag"], (-F(51, 500), -F(1, 1000)))
        for name in ("a", "z", "b"):
            contained(coordinates[name]["real"], P)
        contained(coordinates["v"]["real"], (F(3, 20) if r["beta"] == 0 else F(1, 8), F(1, 2)))
        typed_height = (-F(13, 200), F(17, 250)) if r["beta"] == 0 else (-F(51, 500), -F(1, 1000))
        for name in ("v", "b"):
            contained(coordinates[name]["imag"], typed_height)
        # Original S(e) is the canonical cap branch on this full e box.
        # These saved auxiliary intervals also keep every original J
        # argument in its regular real strip, without evaluating a root.
        xir = interval(coordinates["xi"]["real"])
        assert 0 < xir[0] <= xir[1] < F(1, 2)
        assert 0 < er[0]-xir[1] <= er[1]-xir[0] < 1
        height_groups[(r["beta"], r["external_domain"])].append(eh)
    trees, accepted_nodes, excluded = defaultdict(list), set(), 0
    for row in geometry:
        beta, chart, address = row["beta"], row["chart"], row["address"]
        assert beta in (0, 1) and chart in CHARTS
        assert row["external_domain"] == CHARTS[chart][0]
        param = parameter(address)
        assert tuple(map(F, row["parameter_interval"])) == param
        box = image(chart, param)
        assert tuple(map(F, row["external_coordinate_box"])) == box
        trees[(beta, chart)].append(address)
        if row["status"] == "excluded":
            exclusion(row, param, box)
            excluded += 1
        else:
            assert row["status"] == "accepted boundary estimate"
            node = row["source_node_index"]
            assert node in lookup and node not in accepted_nodes
            accepted_nodes.add(node)
            r = lookup[node]
            assert refs[row["accepted_reference_index"]] is r
            for name in ("beta", "chart", "address", "parameter_interval", "external_coordinate_box", "source_node_canonical_sha256"):
                assert row[name] == r[name]
    assert excluded == 114 and accepted_nodes == set(lookup)
    assert set(trees) == set(itertools.product((0, 1), CHARTS))
    for addresses in trees.values():
        ordered = sorted(addresses)
        assert len(ordered) == len(set(ordered))
        assert all(not b.startswith(a) for a, b in zip(ordered, ordered[1:]))
        assert sum((F(1, 2**len(a)) for a in ordered), F(0)) == 1
    assert source["full_bank_partition"] == {str(k): len(v) for k, v in trees.items()}

    counts, groups = Counter(), defaultdict(list)
    rows = source["references"]
    assert len(rows) == len(refs)
    for row, r in zip(rows, refs):
        for name in ("source_node_index", "beta", "external_domain", "chart", "address"):
            assert row[name] == r[name]
        assert row["source_payload_sha256"] == r["compact_payload_canonical_sha256"]
        assert row["right_response"] == r["response"]["details"]["right_product_modulus"]
        right_upper = interval(row["right_response"])[1]
        keys = list(itertools.product(("main", "left"), ("main", "half") if row["beta"] == 0 else ("main",), (0, 1), (0, 1)))
        assert len(row["profiles"]) == len(keys)
        uppers = []
        for profile, key in zip(row["profiles"], keys):
            cap, right, nu1, nu2 = key
            assert tuple(profile[k] for k in ("cap", "right", "nu1", "nu2")) == key
            box = target_box(row["beta"], cap, right)
            trial = tuple(map(F, profile["trial"]))
            assert len(trial) == 6 and len(profile["support_terms"]) == 6
            assert all(lo <= x <= hi for x, (lo, hi) in zip(trial, box))
            support = []
            for name, x, (lo, hi), term in zip(NAMES, trial, box, profile["support_terms"]):
                assert term["name"] == name and F(term["trial"]) == x
                assert F(term["lower"]) == lo and F(term["upper"]) == hi
                gl, gh = interval(term["gradient"])
                products = [gl*(lo-x), gh*(lo-x), gl*(hi-x), gh*(hi-x)]
                assert list(map(F, term["corner_products"])) == products
                value = max(products)
                assert value >= 0 and F(term["upper_rational"]) == value
                support.append(value)
                counts["support_terms_checked"] += 1
            upper = interval(profile["trial_defect"])[1]+sum(support, F(0))
            assert F(profile["upper_rational"]) == upper
            interval(profile["outgoing_marginal"]["real"])
            interval(profile["outgoing_marginal"]["imag"])
            assert profile["primitive_calls"] == {"g": 40, "gp": 46, "auxiliary": 2}
            assert isinstance(profile["proposal"]["success"], bool)
            counts["optimizer_not_successful"] += int(not profile["proposal"]["success"])
            counts["finite_bounds"] += 1
            counts["strict_negative_bounds"] += int(upper < 0)
            counts.update(profile["primitive_calls"])
            uppers.append(upper)
        groups[(row["beta"], row["external_domain"])].append((max(uppers), right_upper))
    assert counts["finite_bounds"] == 17728 and counts["support_terms_checked"] == 106368
    assert dict(source["counts"]) == {k: v for k, v in counts.items() if k != "support_terms_checked"}
    assert len(source["summaries"]) == 4
    summaries = []
    for row, key in zip(source["summaries"], itertools.product((0, 1), ("k3", "k4"))):
        assert (row["beta"], row["domain"]) == key
        values = groups[key]
        assert row["reference_count"] == len(values)
        upper, response = max(v[0] for v in values), max(v[1] for v in values)
        factor = F(6889, 2000000) if key[1] == "k3" else F(9, 5000)
        corrected = upper+factor*response
        for field, expected in (("boundary_upper_rational", upper), ("response_upper_rational", response), ("barrier_factor_rational", factor), ("corrected_upper_rational", corrected)):
            assert F(row[field]) == expected
        summaries.append({"beta": key[0], "domain": key[1], "reference_count": len(values),
                          "boundary_upper_rational": str(upper), "right_response_upper_rational": str(response),
                          "barrier_factor_rational": str(factor), "corrected_upper_rational": str(corrected),
                          "corrected_gap_rational": str(-corrected), "corrected_gap_decimal_display": float(-corrected)})
    strict = all(F(row["corrected_upper_rational"]) < 0 for row in summaries)
    assert source["strict_corrected_bounds_on_evaluated_references"] is strict
    verify(source["input_sha256"])
    verify(PINNED)
    result = {
        "status": "independent exact double-selection tangent saved-data audit passed",
        "source": SOURCE, "source_sha256": PINNED[SOURCE], "reference_bank": BANK,
        "reference_bank_sha256": PINNED[BANK], "checker_sha256": sha(Path(__file__)),
        "source_bindings_checked": len(source["input_sha256"]), "complete_chart_cases": 18,
        "terminal_geometry_leaves": 1545, "accepted_reference_cells": 1431,
        "strict_geometry_exclusions": 114, "counts": dict(counts), "domain_summaries": summaries,
        "all_profile_trial_support_arithmetic_checked": True,
        "all_saved_target_height_and_real_domain_guards_checked": True,
        "original_private_cap_regular_strip_guards_checked": True,
        "stronger_private_height_range_minus_051_minus_019_verified": strongest_private_height,
        "private_height_extrema": [{"beta": beta, "domain": domain,
            "lower_rational": str(min(x[0] for x in values)),
            "upper_rational": str(max(x[1] for x in values))}
            for (beta, domain), values in sorted(height_groups.items())],
        "height_extension_scope": "Individual harmonic coordinate bounds only; no independent interior joint correlation is inferred.",
        "separate_global_boundary_and_right_response_maxima_checked": True,
        "strict_corrected_whole_domain_bounds_proved": strict,
        "common_corrected_gap_rational": str(min(-F(r["corrected_upper_rational"]) for r in summaries)) if strict else None,
        "source_root_optimizer_primitive_or_interval_provider_evaluations": 0,
        "full_source_or_filling_theorem_claimed": False,
        "scope": "Saved tangent upper arithmetic and boundary correction; analytic concavity, source reduction and marking use their separately bound proofs.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "strict": strict, "summaries": summaries,
                      "audit_sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
