#!/usr/bin/env python3
"""Replay the fixed planar certificates and their finite oriented gluings.

The interval verifiers check rational witnesses with explicit Lobachevsky
tails. The additional checks below inspect the oriented source table and
the stated finite attachments. No level sampling is used. The uniform
local envelopes, entropy argument, arbitrary-iteration proof, filling
asymptotic and geometric volume identity remain written theorems.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys

if not __debug__:
    raise SystemExit("Run without -O: the imported exact verifiers use assertions.")

ROOT = Path(__file__).resolve().parents[2]
PAPER = Path(__file__).resolve().parent
CERTIFICATES = {
    "experiments/actual_sector_cover_certificate.json":
        "54f6087e25e9e6c48e123ea61497cab2a2bb2eb3e4d92a2eb3f9b6e76452eadb",
    "experiments/actual_shared_radius_anchor_obstruction_certificate.json":
        "8e9ca9b9baf9383449a54840a4204ac4008b20cd9a56684ffc9a0a45c65bba27",
}
QUARTETS = [
    (1, 0, 4, 2), (2, 0, 5, 3), (0, 1, 6, 4), (4, 2, 7, 5),
    (5, 3, 8, 0), (6, 4, 9, 7), (7, 5, 10, 8), (0, 6, 11, 9),
    (9, 7, 12, 10), (10, 8, 13, 0), (11, 9, 14, 12),
    (12, 10, 15, 13), (0, 11, 16, 14), (14, 12, 17, 15),
    (15, 13, 18, 0), (16, 14, 0, 17), (17, 15, 0, 18),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_orientations(quartets: list[tuple[int, int, int, int]]) -> int:
    """Every directed boundary edge is cancelled by its opposite."""
    occurrences: dict[tuple[int, int], list[int]] = defaultdict(list)
    for x, b, c, y in quartets:
        for triangle in ((x, b, y), (x, y, c)):
            for i in range(3):
                a, z = triangle[i], triangle[(i + 1) % 3]
                occurrences[tuple(sorted((a, z)))].append(1 if a < z else -1)
    assert all(sorted(signs) == [-1, 1] for signs in occurrences.values())
    return len(occurrences)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PAPER / "build" / "checks")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").unlink(missing_ok=True)
    for relative, expected in CERTIFICATES.items():
        actual = digest(ROOT / relative)
        if actual != expected:
            raise SystemExit(f"Certificate hash changed: {relative}: {actual}")
    cover = json.loads((ROOT / next(iter(CERTIFICATES))).read_text())
    assert list(map(tuple, cover["ports"])) == QUARTETS
    assert cover["protected"] == [0, 16]
    assert cover["bad_ports"] == [2, 4, 7, 12]

    # Reuse the original exact interval and topology verifiers. Their saved
    # inequalities, rather than a previous report, are evaluated afresh.
    command = [
        sys.executable, "-I", str(ROOT / "repro/check_protected_sums.py"),
        "--attachments", "8", "--output", str(output / "protected-sums"),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (output / "protected-sums.log").write_text(result.stdout)
    if result.returncode:
        raise SystemExit(result.stdout)
    result_dir = output / "protected-sums"
    protected = json.loads((result_dir / "summary.json").read_text())
    sector = json.loads((result_dir / "sector-cover.json").read_text())
    anchor = json.loads((result_dir / "anchor-obstruction.json").read_text())
    assert sector["counts"]["rational_shared_radius_branches"] == 40
    assert sector["counts"]["nonempty_bad_R_branches"] == 15
    assert sector["counts"]["no_bad_R_anchors"] == 25
    assert sector["uniform_certified_gap"] == ".04"
    assert anchor["uniform_certified_excess"] == "0.025"

    # Independently replay the local oriented update, not just the final
    # unoriented manifold counts in the existing helper.
    sys.path.insert(0, str(ROOT / "repro"))
    from check_protected_sums import attach_tetrahedron, check_sphere
    q = list(QUARTETS)
    join = 15
    stages = []
    for step in range(9):
        counts = check_sphere(q, {0, 16})
        assert check_orientations(q) == 3 * (17 + step)
        assert all(q[e] == QUARTETS[e] for e in (2, 4, 7, 12))
        stages.append({"attachments": step, **counts})
        if step < 8:
            join = attach_tetrahedron(q, join, {0, 16})
    assert list(map(tuple, protected["final_ordered_quartets"])) == q

    source_paths = [
        Path(__file__), PAPER / "main.tex",
        PAPER / "figures/shared-weight-gain.tex",
        PAPER / "figures/protected-triangle.tex",
        ROOT / "repro/check_protected_sums.py",
        ROOT / "experiments/audit_actual_sector_cover.py",
        ROOT / "experiments/audit_actual_shared_radius_anchor_obstruction.py",
        ROOT / "experiments/audit_actual_original_marked_face_coefficient.py",
        *(ROOT / p for p in CERTIFICATES),
    ]
    record = {
        "scope": (
            "Fresh rigorous interval evaluation of two fixed rational "
            "certificates; exact source-table, complete forty-branch cover "
            "and oriented finite attachment checks. The general analytic, "
            "arbitrary-iteration and volume implications are written proofs."
        ),
        "seed_regions": 17,
        "unabridged_branches": 40,
        "uniform_source_gap": "1/25",
        "restricted_comparison_excess": "1/40",
        "unchanged_possible_failed_balance_regions": [2, 4, 7, 12],
        "oriented_stages": stages,
        "input_sha256": {str(p.relative_to(ROOT)): digest(p) for p in source_paths},
        "result_files": {
            str(p.relative_to(output)): digest(p)
            for p in (result_dir / "summary.json", result_dir / "sector-cover.json",
                      result_dir / "anchor-obstruction.json")
        },
    }
    (output / "summary.json").write_text(json.dumps(record, indent=2) + "\n")
    print("Replayed both rational certificates and nine oriented source tables.")
    print(f"Results: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
