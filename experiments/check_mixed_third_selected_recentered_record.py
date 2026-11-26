#!/usr/bin/env python3
"""Stdlib-only audit of the one saved-cell centered-defect diagnostic.

No provider, root, logarithm, dilogarithm, cotangent or interval library is
imported. Saved analytic enclosures are combined by exact rational arithmetic.
The old source/frontier is bound and remains a partial parameter cover.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = "repro/results/research-mixed-third-selected-recentered-diagnostic.json"
EXPECTED_RESULT_SHA256 = "951944582a63523c90f6a493fb6665678075acb91fac45c888b9684bb455e713"
EXPECTED_BINDINGS = 33
SOURCE = "repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz"
AUDIT = "repro/results/research-mixed-third-selected-product-boundary-saved-audit.json"
PINNED = {
    SOURCE: "e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e",
    AUDIT: "9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647",
    "experiments/diagnose_mixed_third_selected_recentered_defect.py":
        "5c342fe98f825eb30872e40a987d8bff88ea4cee92968408558a61867e8ea152",
    "notes/research_mixed_third_selected_recentered_diagnostic_protocol.md":
        "ac5885465f6c73cae7db88327f9ae464800a3059f3f19b0298fca763c52f13a5",
    "notes/research_mixed_third_selected_recentered_defect.md":
        "7bb5864714f64eb55792096c12072d59207f37056cef16a4b0ba4ee11e4d4e1d",
    "experiments/check_mixed_third_selected_product_boundary_record.py":
        "7ac82eedb454d2812a0c610b33a54cfb7a96a791cdb8e5844fce60e8c4235615",
}
NAMES = ("a", "u", "z", "v", "b")
ADDRESS = "0000110000111110"
DELTA = F(1, 2000)


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2**20), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        assert isinstance(digest, str) and len(digest) == 64
        path = Path(name)
        assert sha(path if path.is_absolute() else ROOT/path) == digest, name


def interval(row):
    assert row["finite"] is True
    lo, hi = F(row["lower_rational"]), F(row["upper_rational"])
    assert lo <= hi
    return lo, hi


def box(row):
    return (*interval(row["real"]), *interval(row["imag"]))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def subtract(x, y):
    return x[0]-y[1], x[1]-y[0]


def negate(x):
    return -x[1], -x[0]


def multiply(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def ccontains(outer, inner):
    return contains(outer[:2], inner[:2]) and contains(outer[2:], inner[2:])


def cmultiply(x, y):
    return (*subtract(multiply(x[:2], y[:2]), multiply(x[2:], y[2:])),
            *add(multiply(x[:2], y[2:]), multiply(x[2:], y[:2])))


def target_domain(left, right):
    plateau = (F(11, 50), F(9, 20))
    result = [plateau, (F(1, 8), F(1, 2)), plateau,
              (F(3, 20), F(1, 2)), plateau]
    if left != "main":
        fixed = F(1, 8) if left == "left" else F(1, 2)
        result[1] = (fixed, fixed)
    if right == "half":
        result[3] = (F(1, 2), F(1, 2))
    return result


def check_original_support(saved, left, right):
    trial = list(map(F, saved["trial"]))
    terms, domain = saved["support_terms"], target_domain(left, right)
    assert len(trial) == len(terms) == 5
    total = F(0)
    for name, x, (lo, hi), term in zip(NAMES, trial, domain, terms):
        assert lo <= x <= hi and term["name"] == name
        assert tuple(F(term[k]) for k in ("trial", "lower", "upper")) == (x, lo, hi)
        gl, gh = interval(term["gradient"])
        products = [gl*(lo-x), gh*(lo-x), gl*(hi-x), gh*(hi-x)]
        assert list(map(F, term["corner_products"])) == products
        assert F(term["upper_rational"]) == max(products)
        total += max(products)
    assert F(saved["upper_rational"]) == interval(saved["trial_defect"])[1]+total
    assert F(saved["compensated_upper_rational"]) == (
        F(saved["upper_rational"])-interval(saved["compensation_record"]["C0"])[0])
    return trial, total


def check_images(row, coordinates, midpoint, trial, left, right):
    for key in ("reference_box", "target_image", "midpoint_image", "midpoint_target_image"):
        assert set(row[key]) == set(NAMES)
    for j, name in enumerate(NAMES):
        original, reference = box(coordinates[name]), box(row["reference_box"][name])
        assert ccontains(reference, original)
        mx, my = map(F, (midpoint[name]["real"], midpoint[name]["imag"]))
        centered = box(row["midpoint_image"][name])
        assert ccontains(centered, (mx, mx, my, my))
        for source, key in ((reference, "target_image"), (centered, "midpoint_target_image")):
            target = box(row[key][name])
            assert contains(target[:2], (trial[j], trial[j]))
            height = source[2:]
            if name == "z":
                height = (F(1, 100), F(1, 100))
            if (name == "u" and left != "main") or (name == "v" and right == "half"):
                height = (F(0), F(0))
            assert contains(target[2:], height)
    # All logarithms/cotangents occur at own or neighboring sum arguments.
    for key in ("reference_box", "target_image", "midpoint_image", "midpoint_target_image"):
        values = [box(row[key][name]) for name in NAMES]
        assert all(0 < value[0] <= value[1] < 1 for value in values)
        for i, j in ((0, 1), (1, 2), (2, 3), (3, 4)):
            assert 0 < values[i][0]+values[j][0] <= values[i][1]+values[j][1] < 1


def check_derivatives(row, trial, left, right):
    fr, fw = row["reference_gradient"], row["target_gradient"]
    assert set(fr) == set(fw) == set(row["boundary_response_terms"]) == set(NAMES)
    assert set(row["boundary_hessian"]) == {"aa", "au", "bv", "bb"}
    zero = (F(0), F(0))
    for name, j in (("a", 0), ("b", 4)):
        for image_key, displacement_key in (("reference_box", "boundary_displacements"),
                                            ("midpoint_image", "midpoint_boundary_displacements")):
            delta = box(row[displacement_key][name])
            expected = subtract((trial[j], trial[j]), interval(row[image_key][name]["real"]))
            assert contains(delta[:2], expected) and delta[2:] == zero
    for name, hname, dname in (("a", "aa", "a"), ("u", "au", "a"),
                              ("v", "bv", "b"), ("b", "bb", "b")):
        expected = cmultiply(box(row["boundary_hessian"][hname]), box(row["boundary_displacements"][dname]))
        assert ccontains(box(row["boundary_response_terms"][name]), expected)
    assert box(row["boundary_response_terms"]["z"]) == (F(0),)*4
    lambdas = [1, int(left == "main"), 0, int(right == "main"), 1]
    assert row["lambda"] == lambdas
    expected_derivatives = {}
    for name, active in zip(NAMES, lambdas):
        response = box(row["boundary_response_terms"][name])
        reference, target = box(fr[name]), box(fw[name])
        real = negate(add(reference[:2] if name not in ("a", "b") else zero, response[:2]))
        imag = subtract(add(reference[2:], response[2:]), target[2:] if active else zero)
        expected_derivatives[(name, "real")] = real
        expected_derivatives[(name, "imag")] = imag
    terms = row["mean_value_terms"]
    assert [(term["name"], term["part"]) for term in terms] == list(itertools.product(NAMES, ("real", "imag")))
    for term in terms:
        assert contains(interval(term["derivative"]), expected_derivatives[(term["name"], term["part"])])


def main():
    if EXPECTED_RESULT_SHA256 is None or EXPECTED_BINDINGS is None:
        raise RuntimeError("checker guarded: completed result identity and binding count are pending")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    verify(PINNED)
    assert sha(ROOT/RESULT) == EXPECTED_RESULT_SHA256
    data = json.loads((ROOT/RESULT).read_text())
    bindings = data["input_sha256"]
    assert len(bindings) == EXPECTED_BINDINGS
    assert all(bindings[name] == digest for name, digest in PINNED.items())
    verify(bindings)
    with gzip.open(ROOT/SOURCE, "rt", encoding="utf-8") as stream:
        original = json.load(stream)
    assert all(bindings[name] == digest for name, digest in original["input_sha256"].items())
    audit = json.loads((ROOT/AUDIT).read_text())
    assert audit["status"] == "exact saved product-boundary audit passed"
    assert audit["source_sha256"] == PINNED[SOURCE] and not audit["full_domain_proved"]
    assert original["stop_reason"] == "first unresolved depth-limit cell"
    node = original["nodes"][-1]
    assert node["node_index"] == 25 and node["status"] == "unresolved"
    assert node["case_index"] == node["alpha"] == node["beta"] == node["sigma"] == 0
    assert node["chart_a"] == node["chart_c"] == "k3_circle_left"
    assert node["address"] == data["address"] == ADDRESS
    assert tuple(map(F, node["interval_a"])) == (-F(89, 128), -F(11, 16))
    assert tuple(map(F, node["interval_c"])) == (-F(45, 64), -F(89, 128))
    assert data["source"] == SOURCE and data["source_sha256"] == PINNED[SOURCE]
    assert data["source_node_index"] == 25 and data["source_node_sha256"] == canonical_hash(node)
    coordinates = node["reference"]["coordinates"]
    assert data["source_reference_coordinate_sha256"] == canonical_hash(coordinates)
    assert data["precision_bits"] == 256 and F(data["delta_rational"]) == DELTA
    assert data["status"] == "fixed saved-cell diagnostic completed"
    assert data["unexpected_error"] is None and data["changed_inputs"] == []
    assert data["whole_domain_proved"] is False and data["finite_source_suppression_claimed"] is False
    midpoint, displacements = {}, {}
    for name in NAMES:
        midpoint[name], displacements[name] = {}, {}
        for part in ("real", "imag"):
            lo, hi = interval(coordinates[name][part])
            middle = (lo+hi)/2
            midpoint[name][part] = str(middle)
            displacements[name][part] = [str(lo-middle), str(hi-middle)]
    assert data["exact_midpoint"] == midpoint
    assert data["reference_displacements"] == displacements
    labels = list(itertools.product(("main", "left", "half"), ("main", "half"), (0, 1)))
    assert len(data["profiles"]) == len(node["profiles"]) == len(labels) == 12
    upper_bounds, summaries = [], []
    for number, (row, saved, label) in enumerate(zip(data["profiles"], node["profiles"], labels)):
        left, right, nu = label
        assert row["profile_index"] == number
        for item in (row, saved):
            assert (item["incoming_profile"], item["outgoing_profile"], item["nu"]) == label
        assert saved["status"] == "enclosed"
        assert row["saved_profile_sha256"] == canonical_hash(saved) and row["trial"] == saved["trial"]
        assert row["status"] == "centered comparison enclosed"
        assert row["primitive_calls"] == {"g": 27, "gp": 52}
        trial, support = check_original_support(saved, left, right)
        check_images(row, coordinates, midpoint, trial, left, right)
        check_derivatives(row, trial, left, right)
        lower, upper = interval(row["midpoint_defect"])
        derivative_cost = F(0)
        for term in row["mean_value_terms"]:
            dl, dh = map(F, displacements[term["name"]][term["part"]])
            assert list(map(F, term["displacement"])) == [dl, dh]
            gl, gh = interval(term["derivative"])
            products = [gl*dl, gl*dh, gh*dl, gh*dh]
            assert list(map(F, term["corner_products"])) == products
            assert F(term["lower_rational"]) == min(products)
            assert F(term["upper_rational"]) == max(products)
            lower += min(products)
            upper += max(products)
            derivative_cost += max(products)
        assert interval(row["centered_trial_defect"]) == (lower, upper)
        assert row["old_trial_defect"] == saved["trial_defect"]
        old_low, old_high = interval(saved["trial_defect"])
        assert max(lower, old_low) <= min(upper, old_high)
        assert row["original_support_terms"] == saved["support_terms"]
        assert F(row["support_correction_rational"]) == support
        assert row["original_compensation_record"] == saved["compensation_record"]
        assert row["original_compensated_upper_rational"] == saved["compensated_upper_rational"]
        compensation_low = interval(saved["compensation_record"]["C0"])[0]
        final = upper+support-compensation_low
        assert F(row["centered_compensated_upper_rational"]) == final
        assert row["comparison_proved"] is (final < -DELTA)
        upper_bounds.append(final)
        summaries.append({"profile_index": number, "label": list(label),
                          "midpoint_upper_rational": row["midpoint_defect"]["upper_rational"],
                          "mean_value_upper_cost_rational": str(derivative_cost),
                          "unchanged_target_support_rational": str(support),
                          "unchanged_C0_lower_rational": str(compensation_low),
                          "centered_compensated_upper_rational": str(final),
                          "strict_comparison_proved": final < -DELTA})
    assert data["counts"] == {
        "reference_proposals": 0, "target_optimizations": 0, "parameter_subdivisions": 0,
        "midpoint_defect_evaluations": 12, "full_box_gradient_evaluations": 24,
        "cotangent_evaluations": 48, "primitive_g": 324, "primitive_gp": 624}
    proved = all(value < -DELTA for value in upper_bounds)
    assert data["cell_comparison_proved"] is proved
    assert max(upper_bounds) < -F(1, 40)
    verify(bindings)
    assert sha(ROOT/RESULT) == EXPECTED_RESULT_SHA256
    output = {"status": "exact saved centered-defect audit passed",
              "source_result": RESULT, "source_result_sha256": EXPECTED_RESULT_SHA256,
              "checker_sha256": sha(Path(__file__)), "input_bindings_checked": len(bindings),
              "profile_count": 12, "mean_value_terms_checked": 120,
              "mean_value_corner_products_checked": 480, "unchanged_target_support_terms_checked": 60,
              "all_saved_reference_trial_anchor_associations_checked": True,
              "full_box_derivative_recombination_checked": True,
              "cell_comparison_proved": proved, "whole_domain_proved": False,
              "old_pending_count_unchanged": len(original["pending"]),
              "strict_gap_lower_rational": str(-max(upper_bounds)),
              "common_strict_gap_rational": "1/40", "summaries": summaries,
              "new_source_root_primitive_interval_or_target_evaluations": 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": output["status"], "cell_comparison_proved": proved,
                      "largest_upper_display": float(max(upper_bounds)), "sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
