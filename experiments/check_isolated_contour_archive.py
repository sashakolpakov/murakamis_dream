#!/usr/bin/env python3
"""Check finite coverage and integrity of the completed contour archive.

This is an archive check, not a replacement for the outward phase
verifier or the written finite-source lifting proof.
"""

import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path

import certify_isolated_vertex_scaled_contours as verifier


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_partition(surface, local_rectangle):
    """Reconstruct the full rational binary subdivision, independently of bounds."""
    leaves = {}
    for entry in surface["cover"]:
        box = tuple(map(Fraction, entry["box"]))
        assert box not in leaves
        assert box[0] < box[1] and box[2] < box[3]
        if entry["method"] == "local Hessian":
            assert surface["surface"] == "central"
            assert (local_rectangle[0] <= box[0] < box[1] <= local_rectangle[1]
                    and local_rectangle[2] <= box[2] < box[3] <= local_rectangle[3])
        else:
            assert entry["method"] in ("Taylor", "direct")
            assert "upper_bound" in entry
        leaves[box] = entry
    initial = tuple(map(Fraction, surface["initial_box"]))
    kind = surface["surface"]
    scale = (Fraction(1, 3) if kind.startswith("outer_")
             else Fraction(1, 2) if kind.startswith("bottom_endpoint_")
             else Fraction(1))
    todo = [initial]
    visited = 0
    budget = 2 * len(leaves) - 1
    while todo:
        box = todo.pop()
        visited += 1
        assert visited <= budget, "A branch of the claimed cover has no saved leaf."
        if box in leaves:
            del leaves[box]
            continue
        a, b, c, d = box
        if b - a >= (d - c) * scale:
            middle = (a + b) / 2
            todo.extend(((a, middle, c, d), (middle, b, c, d)))
        else:
            middle = (c + d) / 2
            todo.extend(((a, b, c, middle), (a, b, middle, d)))
    assert not leaves, "The report contains a duplicate, overlapping or unreachable leaf."
    assert visited == budget == surface["counts"]["visited"]
    return visited


def check_root_degree(root, degree, power):
    assert root["variable"] == "w=exp(i*t/2)"
    assert root["polynomial"] == "(-i)^d*(w+i)^d+w^n*(w-i)^d"
    units = ((1, 0), (0, 1), (-1, 0), (0, -1))
    expected = []
    for k in range(degree + power + 1):
        value = [0, 0]
        if k <= degree:
            for component in (0, 1):
                value[component] += comb(degree, k) * units[-k % 4][component]
        j = k - power
        if 0 <= j <= degree:
            for component in (0, 1):
                value[component] += comb(degree, j) * units[(j-degree) % 4][component]
        expected.append(value)
    assert root["gaussian_integer_coefficients"] == expected
    assert root["Rouche_disk_radius"] == "2^-100"
    assert "original_cone_equation_residual" in root
    assert len(root["logarithmic_gradient_enclosures"]) == 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw_manifest = args.manifest.read_bytes()
    manifest = json.loads(raw_manifest)
    assert manifest["status"] == "certified"
    assert not manifest["failures"]
    assert manifest["degree_range"] == [3, 127]
    expected = {(d, n) for d in range(3, 128) for n in range(1, 128)
                if d*d + n*n < max(1024, 128*d)}
    assert len(expected) == 6369
    listed = [(item["degree"], item["power"]) for item in manifest["pairs"]]
    assert len(listed) == len(set(listed))
    assert set(listed) == expected
    hashes = {
        "verifier_sha256": digest(Path(verifier.__file__).read_bytes()),
        "degree_two_engine_sha256": digest(Path(verifier.c.__file__).read_bytes()),
        "primitive_engine_sha256": digest(Path(verifier.e.__file__).read_bytes()),
    }
    assert all(manifest[k] == v for k, v in hashes.items())
    alpha, beta = "1/128", "63/128"
    domains = {
        ("central", None): [alpha, beta, "0", "1/3"],
        ("negative", None): [alpha, beta, "-1/3", "0"],
        ("lower", None): [alpha, beta, "-1/3", "1/3"],
    }
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            domains[(prefix + sign, None)] = [alpha, beta, "0", "1"]
    for endpoint in (alpha, beta):
        for side in ("upper", "lower"):
            domains[("bottom_endpoint_" + side, endpoint)] = ["-1/3", "1/3", "0", "1"]
            for sign in ("positive", "negative"):
                domains[("nested_" + side + "_" + sign, endpoint)] = ["0", "1", "0", "1"]
    assert len(domains) == 19
    totals = {"pairs": 0, "surfaces": 0, "accepted_boxes": 0,
              "visited_boxes": 0, "compressed_bytes": 0}
    for item in manifest["pairs"]:
        data = Path(item["certificate"]).read_bytes()
        assert digest(data) == item["certificate_sha256"]
        report = json.loads(gzip.decompress(data))
        assert report["status"] == "certified"
        assert all(report[k] == v for k, v in hashes.items())
        assert report["wire_interval"] == [alpha, beta]
        result = report["result"]
        assert (result["degree"], result["power"]) == (item["degree"], item["power"])
        assert result["wire_interval"] == [alpha, beta]
        check_root_degree(result["root"], result["degree"], result["power"])
        local_rectangle = tuple(map(
            Fraction, result["local_Hessian"]["rectangle_in_x_and_t_over_2pi"]))
        assert Fraction(alpha) < local_rectangle[0] < local_rectangle[1] < Fraction(beta)
        assert 0 < local_rectangle[2] < local_rectangle[3] < Fraction(1, 3)
        assert result["local_Hessian"]["subrectangles"] == 24**2
        observed = set()
        for surface in result["surfaces"]:
            key = (surface["surface"], surface["endpoint"])
            assert key not in observed
            observed.add(key)
            assert surface["initial_box"] == domains[key]
            assert Fraction(surface["certified_gap"]) > 0
            assert surface["cover"]
            assert len(surface["cover"]) == sum(
                count for name, count in surface["counts"].items()
                if name != "visited")
            check_partition(surface, local_rectangle)
            totals["accepted_boxes"] += len(surface["cover"])
            totals["visited_boxes"] += surface["counts"]["visited"]
        assert observed == set(domains)
        totals["pairs"] += 1
        totals["surfaces"] += len(result["surfaces"])
        totals["compressed_bytes"] += len(data)
    assert totals["pairs"] == 6369
    assert totals["surfaces"] == 6369 * 19
    output = {
        "status": "complete finite coverage and archive integrity verified",
        "scope": "Hashes, complete parameter and surface coverage, exact rational subdivision reconstruction, local-Hessian leaf containment and root-polynomial degrees; not an independent phase re-evaluation.",
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "manifest": str(args.manifest),
        "manifest_sha256": digest(raw_manifest),
        **hashes,
        **totals,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
