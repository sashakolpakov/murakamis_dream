#!/usr/bin/env python3
"""Exact saved-data audit of the third-selection product-boundary record.

This standalone stdlib checker imports no provider and evaluates no root,
primitive, source, or interval function.  The completed source identity and
its concrete record schema must be pinned before execution is enabled.
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
SOURCE = "repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz"
ANCHOR_SOURCE = "repro/results/research-mixed-third-selected-eight-center-diagnostic.json"
EXPECTED_SOURCE_SHA256 = "e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e"
EXPECTED_COUNTS = {
    "input_bindings": 27, "nodes": 26, "pending": 170,
    "split": 17, "excluded": 6, "accepted": 2, "unresolved": 1, "error": 0,
}
MANDATORY_INPUTS = {
    "experiments/certify_mixed_third_selected_product_boundary.py":
        "1ae53a3563dba750137b9b48b00ad3437c936606d981b7a0c93c29afd48f92c3",
    "experiments/mixed_third_selected_external_reference.py":
        "bfc1057caf82d14c34878f9e822570f087cd7c8d2f6632c39d88bd052eed9158",
    "experiments/evaluate_mixed_third_selected_tangent.py":
        "e8ec90f9024a9242961a23e81fa31843c9abf519d7eecdbecc68495822d07b13",
    "notes/research_mixed_third_selected_implementation.md":
        "74c898dcb903dc09c3d907c1e2a197083ec5f7b09cd3595d1287a2927527e155",
    "notes/research_mixed_third_selected_center_comparison.md":
        "2e5305f3e37b3b50cfc5fdfae7d33b3a4b6cf7bf455381a635029c7ff7f5aff4",
    ANCHOR_SOURCE:
        "69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a",
    "experiments/check_mixed_third_selected_eight_center_record.py":
        "347d1015bce33c1761609467ce9e96e331fb5f81107ba37dc62933230ee48998",
    "repro/results/research-mixed-third-selected-eight-center-saved-audit.json":
        "14e3f08a8113a501b3073298fff532c9f9c4c4b2552c84f6d8aaecc6d43b9d14",
}
SCHEMA_FROZEN = True
LIMITS = {
    "visited_cells": 4000, "provider_invocations": 2000,
    "reference_proposals": 2000, "combined_binary_depth": 16,
    "newton_steps_per_proposal": 20, "target_iterations_per_proposal": 200,
    "precision_bits": 256, "target_proposals_per_label": 1,
}
NAMES = ("a", "u", "z", "v", "b")
QNAMES = NAMES[1:]
DOMAINS = {
    "k3": (F(".35"), F("-.01"), F(".083"), F("-.072"), F(".068")),
    "k4": (F(".30"), F("-.052"), F(".060"), F("-.108"), F("-.001")),
}
CHARTS = (
    "k3_circle_right", "k3_circle_left", "k3_lower_chord",
    "k3_upper_chord", "k3_oblique_chord", "k4_circle_right",
    "k4_circle_left", "k4_lower_chord", "k4_upper_chord",
)


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify(bindings):
    assert bindings
    for name, digest in bindings.items():
        assert isinstance(name, str) and isinstance(digest, str)
        assert len(digest) == 64 and set(digest) <= set("0123456789abcdef")
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name


def interval(row):
    assert row["finite"] is True
    lo, hi = F(row["lower_rational"]), F(row["upper_rational"])
    assert lo <= hi
    return lo, hi


def complex_box(row):
    return (*interval(row["real"]), *interval(row["imag"]))


def product_parameter(address):
    """Decode deterministic longest-normalized-side splits, left on ties."""
    assert isinstance(address, str) and set(address) <= {"0", "1"}
    sides = [[F(-1), F(1)], [F(-1), F(1)]]
    for digit in address:
        widths = [(hi-lo)/2 for lo, hi in sides]
        axis = 0 if widths[0] >= widths[1] else 1
        middle = sum(sides[axis])/2
        sides[axis][1 if digit == "0" else 0] = middle
    return tuple(tuple(x) for x in sides)


def split_axis(address):
    left, right = product_parameter(address)
    return 0 if left[1]-left[0] >= right[1]-right[0] else 1


def line(chart):
    assert chart in CHARTS and "circle" not in chart
    x, _, radius, bottom, top = DOMAINS[chart[:2]]
    if chart.endswith("lower_chord"):
        return x, bottom, radius, F(0)
    if chart.endswith("upper_chord"):
        return x, top, radius, F(0)
    assert chart == "k3_oblique_chord"
    return F(301, 500), -F(1, 500), F(21, 100), F(7, 100)


def image(chart, bounds):
    assert chart in CHARTS
    lo, hi = bounds
    assert -1 <= lo <= hi <= 1
    x, y, radius, _, _ = DOMAINS[chart[:2]]
    if "circle" in chart:
        near = F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))
        far = max(abs(lo), abs(hi))
        rr = ((1-far*far)/(1+far*far), (1-near*near)/(1+near*near))
        ii = (2*lo/(1+lo*lo), 2*hi/(1+hi*hi))
        sign = 1 if chart.endswith("right") else -1
        xx = [x+sign*radius*t for t in rr]
        yy = [y+sign*radius*t for t in ii]
    else:
        a, b, dx, dy = line(chart)
        xx = [a+dx*lo, a+dx*hi]
        yy = [b+dy*lo, b+dy*hi]
    return min(xx), max(xx), min(yy), max(yy)


def geometry_exclusion(chart, bounds, witness):
    """A strict whole-factor exclusion, never a pointwise feasibility test."""
    lo, hi = bounds
    box = image(chart, bounds)
    xl, xh, yl, yh = box
    cx, cy, radius, floor, ceiling = DOMAINS[chart[:2]]
    assert witness["chart"] == chart and witness["domain"] == chart[:2]
    assert tuple(map(F, witness["parameter_interval"])) == bounds
    assert tuple(map(F, witness["coordinate_box"])) == box
    margin = F(witness["strict_margin_rational"])
    assert margin > 0
    criterion = witness["criterion"]
    if criterion == "below_lower_height":
        expected = floor-yh
    elif criterion == "above_upper_height":
        expected = yl-ceiling
    elif criterion == "above_oblique_halfplane":
        assert chart[:2] == "k3"
        if "circle" in chart:
            lower = xl-3*yh
        else:
            x, y, dx, dy = line(chart)
            lower = min(x-3*y+(dx-3*dy)*lo, x-3*y+(dx-3*dy)*hi)
        expected = lower-F(76, 125)
    elif criterion == "outside_typed_disk":
        x, y, dx, dy = line(chart)
        x, y = x-cx, y-cy
        t = min(hi, max(lo, -(x*dx+y*dy)/(dx*dx+dy*dy)))
        expected = (x+dx*t)**2+(y+dy*t)**2-radius*radius
    else:
        raise AssertionError(criterion)
    assert margin == expected > 0


def case_inventory():
    """Exactly 2*(5+4)^2 cases; the chart types determine alpha,sigma."""
    return tuple(sorted((beta, left, right) for beta in (0, 1)
                        for left in CHARTS for right in CHARTS))


def associated_case(beta, left, right):
    assert beta in (0, 1) and left in CHARTS and right in CHARTS
    return {"beta": beta, "alpha": int(left[1])-3,
            "sigma": int(right[1])-3, "chart_a": left, "chart_c": right}


def check_cell_geometry(cell, cases):
    assert type(cell["case_index"]) is int
    case = cases[cell["case_index"]]
    for key, value in case.items():
        assert cell[key] == value
    address = cell["address"]
    aa, cc = product_parameter(address)
    abox, cbox = image(case["chart_a"], aa), image(case["chart_c"], cc)
    assert tuple(map(F, cell["interval_a"])) == aa
    assert tuple(map(F, cell["interval_c"])) == cc
    assert tuple(map(F, cell["abox"])) == abox
    assert tuple(map(F, cell["cbox"])) == cbox
    return case, aa, cc, abox, cbox


def interval_sum(left, right):
    return left[0]+right[0], left[1]+right[1]


def interval_difference(left, right):
    return left[0]-right[1], left[1]-right[0]


def interval_product(left, right):
    products = [x*y for x in left for y in right]
    return min(products), max(products)


def interval_contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def real_conjugate_product(left, right):
    """Exact Cartesian range of Re(z*conjugate(w)) for independent boxes."""
    return interval_sum(interval_product(left[:2], right[:2]),
                        interval_product(left[2:], right[2:]))


def check_modulus_upper(row, bound):
    box = complex_box(row)
    squared = max(abs(box[0]), abs(box[1]))**2+max(abs(box[2]), abs(box[3]))**2
    assert F(bound) >= 0 and F(bound)**2 >= squared


def complex_sum(left, right):
    return (*interval_sum(left[:2], right[:2]),
            *interval_sum(left[2:], right[2:]))


def complex_product(left, right):
    return (*interval_difference(interval_product(left[:2], right[:2]),
                                 interval_product(left[2:], right[2:])),
            *interval_sum(interval_product(left[:2], right[2:]),
                          interval_product(left[2:], right[:2])))


def exact_complex(pair):
    x, y = map(F, pair)
    return x, x, y, y


def complex_contains(outer, inner):
    return interval_contains(outer[:2], inner[:2]) and interval_contains(outer[2:], inner[2:])


def squared_box_modulus(box):
    return max(abs(box[0]), abs(box[1]))**2+max(abs(box[2]), abs(box[3]))**2


def residual_terms(beta):
    return (((1, "u+z"), (1, "a+u"), (-3, "u")),
            ((1, "u+z"), (1, "z+v"), (-3, "z")),
            ((1, "z+v"), (1, "v+b"), (-(2+beta), "v")),
            ((1, "v+b"), (1, "b+c"), (-(2+beta), "b")))


def check_reference(reference, case, abox, cbox):
    """Check saved analytic-witness arithmetic; never evaluate its functions."""
    assert reference["alpha"] == case["alpha"] and reference["beta"] == case["beta"]
    assert reference["precision_bits"] == 256
    assert reference["status"] in ("enclosed", "inconclusive", "error")
    d = reference["diagnostics"]
    if reference["status"] == "error" and "input_abox" not in d:
        assert reference.get("reason")
        return
    assert tuple(map(F, d["input_abox"])) == abox
    assert tuple(map(F, d["input_cbox"])) == cbox
    count = reference["counts"]
    assert 0 <= count.get("proposal_calls", 0) <= 1
    assert 0 <= count.get("newton_steps", 0) <= 20
    assert 0 <= count.get("floating_gradient_calls", 0) <= 20
    assert count.get("floating_predictor_solves", 0) in (0, 2)
    assert count.get("direct_residual_evaluations", 0) in (0, 1)
    assert count.get("taylor_residual_evaluations", 0) in (0, 1)
    if reference["status"] != "enclosed":
        return
    assert count["proposal_calls"] == 1 and count["floating_predictor_solves"] == 2
    assert count["direct_residual_evaluations"] == count["taylor_residual_evaluations"] == 1
    qlimits = (F(".23"), F(".45"), F("-.12"), F(".12"))
    for entries in d["common_product_checks"].values():
        for row in entries.values():
            box = complex_box(row["coordinate"])
            assert row["contained"] is True and complex_contains(qlimits, box)
    assert set(d["common_product_checks"]) == {
        "full external boxes", "full affine unknowns",
        "actual-reference images after necessary intersections"}
    for label, entries in d["regular_strip_checks"].items():
        assert label in ("midpoint", "full affine")
        assert set(entries) == {"u+z", "a+u", "u", "z+v", "z", "v+b", "v", "b+c", "b"}
        for row in entries.values():
            lo, hi = interval(row["argument"]["real"])
            assert row["regular_strip"] is True and 0 < lo <= hi < 1
    assert set(d["regular_strip_checks"]) == {"midpoint", "full affine"}
    midpoints = {}
    deltas = {}
    for name, box in (("a", abox), ("c", cbox)):
        midpoint = ((box[0]+box[1])/2, (box[2]+box[3])/2)
        midpoints[name] = midpoint
        assert tuple(map(F, d["external_midpoints"][name])) == midpoint
        delta = (box[0]-midpoint[0], box[1]-midpoint[0],
                 box[2]-midpoint[1], box[3]-midpoint[1])
        deltas[name] = complex_box(d["external_displacements"][name])
        assert complex_contains(deltas[name], delta)
        assert complex_contains(complex_box(d["common_product_checks"]["full external boxes"][name]["coordinate"]), box)
    proposal = d["proposal"]
    assert proposal["precision_decimal_digits"] == 50
    assert proposal["maximum_newton_steps"] == 20 and proposal["rounding_decimal_places"] == 40
    assert proposal["convergence_used_as_certificate"] is False
    assert len(proposal["trace"]) <= 20
    assert [r["iteration"] for r in proposal["trace"]] == list(range(len(proposal["trace"])))
    model = d["exact_affine_model"]
    assert set(model) == {"q0", "Ta", "Tc"}
    assert all(set(model[key]) == set(QNAMES) for key in model)
    for name in QNAMES:
        predicted = exact_complex(model["q0"][name])
        predicted = complex_sum(predicted, complex_product(exact_complex(model["Ta"][name]), deltas["a"]))
        predicted = complex_sum(predicted, complex_product(exact_complex(model["Tc"][name]), deltas["c"]))
        affine = complex_box(d["full_affine_coordinates"][name])
        assert complex_contains(affine, predicted)
        assert d["common_product_checks"]["full affine unknowns"][name]["coordinate"] == d["full_affine_coordinates"][name]
    alternatives = []
    if "direct_residual" in d:
        row = d["direct_residual"]
        uppers = list(map(F, row["row_modulus_uppers"]))
        assert len(uppers) == len(row["values"]) == 4
        for value, upper in zip(row["values"], uppers):
            check_modulus_upper(value, upper)
        alternatives.append(uppers)
    if "taylor_residual" in d:
        row = d["taylor_residual"]
        remainder = d["taylor_log_remainders"]
        assert set(remainder) == {"u+z", "a+u", "u", "z+v", "z", "v+b", "v", "b+c", "b"}
        amounts = {}
        for name, term in remainder.items():
            assert term["argument"] == d["regular_strip_checks"]["full affine"][name]["argument"]
            inc2 = squared_box_modulus(complex_box(term["increment"]))
            assert F(term["increment_modulus_squared_upper"]) == inc2
            sine = complex_box(term["sine"])
            sep = max(F(0), sine[0], -sine[1], sine[2], -sine[3])
            assert F(term["cartesian_separation_lower"]) == sep > 0
            bound = F(term["third_derivative_modulus_upper"])
            check_modulus_upper(term["third_derivative"], bound)
            amounts[name] = bound*inc2/2
            assert F(term["single_log_remainder_upper"]) == amounts[name]
        quadratic = [sum((abs(n)*amounts[name] for n, name in terms), F(0))
                     for terms in residual_terms(case["beta"])]
        assert list(map(F, row["quadratic_remainder_uppers"])) == quadratic
        linear = list(map(F, row["linear_modulus_uppers"]))
        assert len(linear) == len(d["linear_defect"]["whole_linear_residual"]) == 4
        for value, bound in zip(d["linear_defect"]["whole_linear_residual"], linear):
            check_modulus_upper(value, bound)
        total = [x+y for x, y in zip(linear, quadratic)]
        assert list(map(F, row["row_modulus_uppers"])) == total
        alternatives.append(total)
    assert alternatives
    certificate = d["residual_certificate"]
    selected = [min(row[i] for row in alternatives) for i in range(4)]
    assert list(map(F, certificate["selected_row_modulus_uppers"])) == selected
    squared = sum((x*x for x in selected), F(0))
    assert F(certificate["squared_norm_upper"]) == squared
    assert F(certificate["pi_lower_rational"]) == F(157, 50)
    target = F(200, 157)**2*squared
    radius = F(certificate["coordinate_radius_rational"])
    assert F(certificate["radius_squared_target"]) == target
    assert radius >= 0 and F(certificate["radius_squared_margin_rational"]) == radius*radius-target >= 0
    for name in QNAMES:
        affine = complex_box(d["full_affine_coordinates"][name])
        expanded = (affine[0]-radius, affine[1]+radius, affine[2]-radius, affine[3]+radius)
        assert complex_contains(complex_box(d["raw_root_coordinates"][name]), expanded)
    assert set(d["necessary_intersections"]) == set(NAMES)
    assert set(reference["coordinates"]) == set(NAMES)
    for name, entry in d["necessary_intersections"].items():
        if name == "a":
            necessary = (".267", ".433", "-.072", ".068") if case["alpha"] == 0 else (".24", ".36", "-.108", "-.001")
            original = complex_box(d["common_product_checks"]["full external boxes"]["a"]["coordinate"])
        else:
            own = 1 if name in ("u", "z") else case["beta"]
            necessary = (".24", ".36", "-.102", "-.001") if own else (".267", ".433", "-.065", ".068")
            original = complex_box(d["raw_root_coordinates"][name])
        necessary = tuple(map(F, necessary))
        assert tuple(map(F, entry["raw_box"])) == original
        assert tuple(map(F, entry["necessary_box"])) == necessary
        intersection = (max(original[0], necessary[0]), min(original[1], necessary[1]),
                        max(original[2], necessary[2]), min(original[3], necessary[3]))
        assert tuple(map(F, entry["intersection_box"])) == intersection
        assert intersection[0] <= intersection[1] and intersection[2] <= intersection[3]
        assert complex_contains(complex_box(entry["outward_coordinate"]), intersection)
        assert reference["coordinates"][name] == entry["outward_coordinate"]
    assert reference["coordinate_canonical_sha256"] == canonical_hash(reference["coordinates"])


def check_frontier(addresses):
    assert addresses
    ordered = sorted(addresses)
    assert len(set(ordered)) == len(ordered)
    for address in ordered:
        product_parameter(address)
    assert all(not right.startswith(left) for left, right in zip(ordered, ordered[1:]))
    assert sum((F(1, 2**len(x)) for x in ordered), F(0)) == 1
    return {"leaves": len(ordered), "normalized_mass_rational": "1",
            "full_tree_nodes": 2*len(ordered)-1,
            "maximum_depth": max(map(len, ordered))}


def check_geometry_forest(data):
    """Audit visited nodes and untouched pending roots as one full frontier."""
    cases = [associated_case(*key) for key in case_inventory()]
    assert len(cases) == 162
    assert len(data["cases"]) == 162
    for number, (saved, expected) in enumerate(zip(data["cases"], cases)):
        for key, value in expected.items():
            assert saved[key] == value
        if "case_index" in saved:
            assert saved["case_index"] == number
    nodes, pending = data["nodes"], data["pending"]
    index, pending_index, frontiers = {}, {}, defaultdict(list)
    counts = Counter()
    for number, node in enumerate(nodes):
        assert node["node_index"] == number
        case, aa, cc, _, _ = check_cell_geometry(node, cases)
        key = (node["case_index"], node["address"])
        assert key not in index
        index[key] = number
        status = node["status"]
        assert status in {"excluded", "accepted", "split", "unresolved", "error"}
        counts[status] += 1
        if status == "excluded":
            witness = node["geometry_witness"]
            factor = witness["factor"]
            assert factor in ("a", "c")
            geometry_exclusion(case["chart_"+factor], aa if factor == "a" else cc,
                               witness["witness"])
        if status == "split":
            assert node["split_axis"] == ("a" if split_axis(node["address"]) == 0 else "c")
        if status != "split":
            frontiers[node["case_index"]].append(node["address"])
    for number, cell in enumerate(pending):
        check_cell_geometry(cell, cases)
        key = (cell["case_index"], cell["address"])
        assert key not in index and key not in pending_index
        pending_index[key] = number
        frontiers[cell["case_index"]].append(cell["address"])
    all_keys = set(index) | set(pending_index)
    for key in all_keys:
        case_id, address = key
        if address:
            parent = (case_id, address[:-1])
            assert parent in index and nodes[index[parent]]["status"] == "split"
            if key in index:
                assert index[parent] < index[key]
        if key in index and nodes[index[key]]["status"] == "split":
            assert (case_id, address+"0") in all_keys
            assert (case_id, address+"1") in all_keys
    assert set(frontiers) == set(range(162))
    summaries = [dict(case_index=i, **cases[i], **check_frontier(frontiers[i]))
                 for i in range(162)]
    leaves = sum(row["leaves"] for row in summaries)
    assert len(nodes)+len(pending) == 2*leaves-162
    assert counts["split"] == leaves-162
    return cases, summaries, counts


def target_box(beta, left, right):
    plateau = (F(11, 50), F(9, 20))
    assert beta in (0, 1) and left in ("main", "left", "half")
    assert right in (("main", "half") if beta == 0 else ("main",))
    box = [plateau, (F(1, 8), F(1, 2)), plateau,
           (F(3, 20) if beta == 0 else F(1, 8), F(1, 2)), plateau]
    if left != "main":
        x = F(1, 8) if left == "left" else F(1, 2)
        box[1] = (x, x)
    if right == "half":
        box[3] = (F(1, 2), F(1, 2))
    return box


def support_upper(profile, beta):
    left, right, nu = (profile[key] for key in
                        ("incoming_profile", "outgoing_profile", "nu"))
    assert nu in (0, 1)
    box = target_box(beta, left, right)
    trial = list(map(F, profile["trial"]))
    terms = profile["support_terms"]
    assert len(trial) == len(terms) == 5
    total = F(0)
    for name, x, (lo, hi), term in zip(NAMES, trial, box, terms):
        assert lo <= x <= hi and term["name"] == name
        assert tuple(F(term[k]) for k in ("lower", "upper", "trial")) == (lo, hi, x)
        gl, gh = interval(term["gradient"])
        corners = [gl*(lo-x), gh*(lo-x), gl*(hi-x), gh*(hi-x)]
        assert list(map(F, term["corner_products"])) == corners
        assert F(term["upper_rational"]) == max(corners) >= 0
        total += max(corners)
    upper = interval(profile["trial_defect"])[1]+total
    assert F(profile["upper_rational"]) == upper
    return upper


def check_compensation(profile, reference, anchor):
    saved = profile["compensation_record"]
    current_hash = canonical_hash(reference["coordinates"])
    anchor_hash = canonical_hash(anchor["reference_certificate"]["coordinates"])
    assert profile["reference_coordinate_sha256"] == saved["reference_coordinate_sha256"] == current_hash
    assert profile["anchor_coordinate_sha256"] == saved["anchor_coordinate_sha256"] == anchor_hash
    current, anchored = saved["current"], saved["anchor"]
    assert set(current) == set(anchored) == {"pL", "pR", "a", "b"}
    assert current["pL"] == profile["incoming_marginal"]
    assert current["pR"] == profile["outgoing_marginal"]
    for name in ("a", "b"):
        assert complex_contains(complex_box(current[name]), complex_box(reference["coordinates"][name]))
        assert complex_contains(complex_box(anchored[name]),
                                complex_box(anchor["reference_certificate"]["coordinates"][name]))
    pieces = []
    for side, pname, qname in (("left", "pL", "a"), ("right", "pR", "b")):
        row = saved[side]
        for part in ("real", "imag"):
            marginal = interval_difference(interval(current[pname][part]), interval(anchored[pname][part]))
            coordinate = interval_difference(interval(current[qname][part]), interval(anchored[qname][part]))
            assert interval(row["delta_marginal"][part]) == marginal
            assert interval(row["delta_coordinate"][part]) == coordinate
            product = interval_product(marginal, coordinate)
            assert interval(row["real_times_real" if part == "real" else "imag_times_imag"]) == product
        piece = interval_sum(interval(row["real_times_real"]), interval(row["imag_times_imag"]))
        assert interval(row["real_product"]) == piece
        pieces.append(piece)
    added = interval_sum(*pieces)
    compensation = (added[0]/2, added[1]/2)
    assert interval(saved["C0"]) == compensation
    compensated = F(profile["upper_rational"])-compensation[0]
    assert F(profile["compensated_upper_rational"]) == compensated
    return compensated


def profile_inventory(beta):
    return list(itertools.product(("main", "left", "half"),
                                  ("main", "half") if beta == 0 else ("main",), (0, 1)))


def check_profiles(node, anchor, delta):
    beta, alpha = node["beta"], node["alpha"]
    reference = node["reference"]
    assert reference["status"] == "enclosed"
    assert node["anchor_reference_canonical_sha256"] == canonical_hash(anchor)
    assert node["reference_coordinate_canonical_sha256"] == canonical_hash(reference["coordinates"])
    profiles = node["profiles"]
    expected = profile_inventory(beta)
    assert len(profiles) <= len(expected)
    if node["status"] != "error" and node.get("reason") != "interrupted during evaluation":
        assert len(profiles) == len(expected)
    compensated = []
    for profile, (left, right, nu) in zip(profiles, expected):
        assert (profile["incoming_profile"], profile["outgoing_profile"], profile["nu"]) == (left, right, nu)
        if profile.get("proposal_failed") is True:
            assert profile["status"] == "inconclusive"
            assert "compensated_upper_rational" not in profile
            continue
        if "proposal" in profile:
            proposal = profile["proposal"]
            assert proposal["maximum_iterations"] == 200 and proposal["proposal_calls"] == 1
            assert 0 <= proposal["iterations"] <= 200
        if profile["status"] != "enclosed":
            assert profile["status"] in ("inconclusive", "error")
            continue
        assert profile["alpha"] == alpha and profile["beta"] == beta
        assert profile["left"] == left and profile["right"] == right
        assert profile["precision_bits"] == 256
        assert profile["primitive_calls"] == {"g": 27, "gp": 39}
        support_upper(profile, beta)
        compensated.append(check_compensation(profile, reference, anchor))
    if len(compensated) == len(expected) and node["status"] != "error":
        maximum = max(compensated)
        assert F(node["maximum_compensated_upper_rational"]) == maximum
        assert (node["status"] == "accepted") == (maximum < -delta)
    else:
        assert node["status"] != "accepted"
    return compensated


def check_anchor_inventory(data, anchors):
    assert data["anchor_source"] == ANCHOR_SOURCE
    rows = anchors["references"]
    required = list(itertools.product((0, 1), repeat=3))
    assert [(r["alpha"], r["beta"], r["external_right_type_flag"]) for r in rows] == required
    assert len(data["anchor_inventory"]) == 8
    result = {}
    for number, (row, key, saved) in enumerate(zip(rows, required, data["anchor_inventory"])):
        assert row["status"] == "fixed canonical reference certified"
        assert saved["source_reference_index"] == number
        assert (saved["alpha"], saved["beta"], saved["sigma"]) == key
        assert saved["reference_canonical_sha256"] == canonical_hash(row)
        assert saved["coordinate_canonical_sha256"] == canonical_hash(row["reference_certificate"]["coordinates"])
        result[key] = row
    return result


def main():
    if (not SCHEMA_FROZEN or EXPECTED_SOURCE_SHA256 is None
            or EXPECTED_COUNTS is None or not MANDATORY_INPUTS):
        raise RuntimeError("checker guarded: final record schema/source identity/counts are pending")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    verify(MANDATORY_INPUTS)
    source = ROOT/SOURCE
    assert sha(source) == EXPECTED_SOURCE_SHA256
    with gzip.open(source, "rt", encoding="utf-8") as stream:
        data = json.load(stream)
    bindings = data["input_sha256"]
    for name, digest in MANDATORY_INPUTS.items():
        assert bindings[name] == digest
    assert len(bindings) == EXPECTED_COUNTS["input_bindings"]
    verify(bindings)
    assert data["limits"] == LIMITS and data["precision_bits"] == 256
    assert F(data["delta"]) == F(1, 2000)
    assert data["input_bindings_unchanged"] is True
    for info_key in ("provider_initialization", "evaluator_initialization"):
        info = data[info_key]
        assert info["precision_bits"] == 256
        assert all(bindings[name] == digest for name, digest in info["bindings"].items())
    anchors = json.loads((ROOT/ANCHOR_SOURCE).read_text())
    assert anchors["status"] == "fixed eight-center diagnostic completed"
    assert all(bindings[name] == digest for name, digest in anchors["input_sha256"].items())
    anchor_index = check_anchor_inventory(data, anchors)
    cases, frontier, status_counts = check_geometry_forest(data)
    assert data["complete_partition"] is True
    partition = [{"case_index": row["case_index"], "leaf_count": row["leaves"],
                  "normalized_mass_rational": "1", "full_tree_node_count": row["full_tree_nodes"],
                  "maximum_depth": row["maximum_depth"]} for row in frontier]
    assert data["partition_summary"] == partition
    nodes, pending = data["nodes"], data["pending"]
    assert len(nodes) == EXPECTED_COUNTS["nodes"] <= LIMITS["visited_cells"]
    assert len(pending) == EXPECTED_COUNTS["pending"]
    assert max(row["maximum_depth"] for row in frontier) <= LIMITS["combined_binary_depth"]
    reference_count = enclosed_count = proposal_count = evaluation_count = support_count = 0
    provider_counts = Counter()
    upper_bounds, accepted_bounds = [], defaultdict(list)
    for node in nodes:
        case = cases[node["case_index"]]
        assert len(node["address"]) <= LIMITS["combined_binary_depth"]
        if "reference" in node:
            reference_count += 1
            reference = node["reference"]
            provider_counts.update(reference["counts"])
            check_reference(reference, case, tuple(map(F, node["abox"])), tuple(map(F, node["cbox"])))
            if reference["status"] == "enclosed":
                enclosed_count += 1
                anchor = anchor_index[(node["alpha"], node["beta"], node["sigma"])]
                values = check_profiles(node, anchor, F(data["delta"]))
                upper_bounds.extend(values)
                support_count += 5*len(values)
                if node["status"] == "accepted":
                    accepted_bounds[(node["alpha"], node["beta"], node["sigma"])].append(max(values))
            else:
                assert not node["profiles"] and node["status"] != "accepted"
        else:
            assert node["status"] in ("excluded", "error", "unresolved")
            assert not node["profiles"]
        proposal_count += len(node["profiles"])
        evaluation_count += sum("proposal" in p for p in node["profiles"])
    counts = data["counts"]
    assert counts["visited_cells"] == len(nodes)
    assert counts["pending"] == len(pending)
    for status in ("excluded", "accepted", "split", "unresolved", "error"):
        assert counts.get(status, 0) == status_counts[status] == EXPECTED_COUNTS.get(status, 0)
    assert data["provider_counts"] == dict(provider_counts)
    assert counts["reference_proposals"] == provider_counts["proposal_calls"] <= LIMITS["reference_proposals"]
    unreturned = counts.get("provider_invocations", 0)-reference_count
    assert unreturned == 0 or (unreturned == 1 and data.get("unexpected_error") and status_counts["error"])
    assert counts.get("provider_invocations", 0) <= LIMITS["provider_invocations"]
    assert counts.get("enclosed_references", 0) == enclosed_count
    assert counts.get("target_proposals", 0) == proposal_count
    assert counts.get("profile_interval_bounds", 0) == evaluation_count
    complete = (not pending and not status_counts["unresolved"] and not status_counts["error"]
                and data["stop_reason"] is None)
    assert data["full_domain_proved"] is complete
    assert data["status"] == ("complete domain comparison" if complete
                              else "bounded pass stopped without a full-domain conclusion")
    if complete:
        assert set(accepted_bounds) == set(itertools.product((0, 1), repeat=3))
    summaries = [{"alpha": key[0], "beta": key[1], "sigma": key[2],
                  "accepted_cells": len(values), "maximum_compensated_upper_rational": str(max(values)),
                  "strict_gap_lower_rational": str(-max(values))}
                 for key, values in sorted(accepted_bounds.items())]
    verify(bindings)
    assert sha(source) == EXPECTED_SOURCE_SHA256
    result = {
        "status": "exact saved product-boundary audit passed",
        "source": SOURCE, "source_sha256": EXPECTED_SOURCE_SHA256,
        "checker_sha256": sha(Path(__file__)), "input_bindings_checked": len(bindings),
        "cases_checked": 162, "visited_nodes": len(nodes), "pending_cells": len(pending),
        "frontier_leaves": sum(row["leaves"] for row in frontier),
        "accepted_cells": status_counts["accepted"], "strict_geometry_exclusions": status_counts["excluded"],
        "enclosed_reference_certificates_checked": enclosed_count,
        "profile_upper_bounds_checked": len(upper_bounds), "support_terms_checked": support_count,
        "all_raw_chart_images_reconstructed": True,
        "all_pending_frontiers_preserved": True,
        "all_residual_minima_radii_and_necessary_intersections_checked": True,
        "all_same_reference_anchor_compensations_checked": True,
        "full_domain_proved": complete, "delta_rational": data["delta"],
        "accepted_domain_summaries": summaries,
        "maximum_evaluated_compensated_upper_rational": str(max(upper_bounds)) if upper_bounds else None,
        "source_root_primitive_or_interval_evaluations": 0,
        "whole_source_or_knot_asymptotic_claimed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "full_domain_proved": complete,
                      "visited": len(nodes), "pending": len(pending),
                      "profile_bounds": len(upper_bounds), "sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
