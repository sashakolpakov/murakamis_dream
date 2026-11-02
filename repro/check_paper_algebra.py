#!/usr/bin/env python3
"""Replay the finite algebra and rational constants used by the companion papers.

Requires SymPy, python-flint and NumPy. These checks do not verify analytic
uniformity, geometric existence, or a volume conjecture. Each result states
its own finite scope.
The scripts run in isolated Python processes with assertions enabled.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    "local-coefficients": "papers/local-coefficients/check.py",
    "source-asymptotics": "papers/source-asymptotics/check.py",
    "oscillatory-fillings": "papers/oscillatory-fillings/check.py",
    "marked-fillings": "papers/marked-fillings/check.py",
    "cyclic-source-constants": "repro/check_cyclic_source_constants.py",
    "planar-certificates": "papers/planar-certificates/check.py",
    "triangular-insertion": "repro/check_triangular_boundary_certificate.py",
    "newton-tangles": "papers/newton-tangles/check.py",
    "terminal-decorations": "papers/terminal-decorations/check.py",
    "circle-tree-geometry": "papers/circle-tree-geometry/check.py",
    "conway-geometry": "papers/conway-geometry/check.py",
    "meridian-tangles": "papers/meridian-tangles/check.py",
    "conway-source-bounds": "papers/conway-source-bounds/check.py",
    "conway-fillings": "papers/conway-fillings/check.py",
    "conway-asymptotics": "papers/conway-asymptotics/check.py",
    "circle-tree-asymptotics": "papers/circle-tree-asymptotics/check.py",
    "quarter-index-asymptotics": "papers/quarter-index-asymptotics/check.py",
    "directed-tree-asymptotics": "papers/directed-tree-asymptotics/check.py",
}
DIRECTORY_CHECKS = {"planar-certificates", "triangular-insertion", "terminal-decorations",
                    "meridian-tangles", "conway-source-bounds", "conway-asymptotics",
                    "quarter-index-asymptotics"}
CERTIFICATE_INPUTS = (
    "repro/check_protected_sums.py",
    "experiments/audit_actual_sector_cover.py",
    "experiments/audit_actual_shared_radius_anchor_obstruction.py",
    "experiments/audit_actual_original_marked_face_coefficient.py",
    "experiments/actual_sector_cover_certificate.json",
    "experiments/actual_shared_radius_anchor_obstruction_certificate.json",
    "experiments/audit_actual_balanced_terminal_fans.py",
    "experiments/audit_two_octahedron_angular_edge_block.py",
    "experiments/audit_all_circle_vertexwise_geometry.py",
    "experiments/verify_conway_two_leaf_block_alias_certificate.py",
    "experiments/conway_two_leaf_block_alias_certificate.json",
    "experiments/verify_conway_single_leaf_attachment_certificate.py",
    "experiments/conway_single_leaf_attachment_certificate.json",
    "experiments/audit_all_circle_curvature_packet.py",
    "experiments/audit_actual_all_circle_directed_volume.py",
    "experiments/audit_all_circle_local_message_recursion.py",
    "experiments/audit_main_meridian_direct_fillings.py",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    summary = output / "summary.json"
    summary.unlink(missing_ok=True)
    sources = [ROOT / script for script in CHECKS.values()]
    sources += sorted(p for p in (ROOT / "papers").rglob("*")
                      if p.suffix in {".tex", ".bib"} and "build" not in p.parts)
    sources += [ROOT / path for path in CERTIFICATE_INPUTS]
    sources.append(Path(__file__).resolve())
    before = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    records = []
    for name, script in CHECKS.items():
        destination = output / name if name in DIRECTORY_CHECKS else output / (name + ".json")
        result_path = destination / "summary.json" if name in DIRECTORY_CHECKS else destination
        result_path.unlink(missing_ok=True)
        command = [sys.executable, "-I", str(ROOT / script),
                   "--output", str(destination)]
        result = subprocess.run(command, cwd=ROOT, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output / (name + ".log")).write_text(result.stdout)
        if result.returncode:
            raise SystemExit(f"{name} failed; see {output / (name + '.log')}\n"
                             + result.stdout[-3000:])
        if not result_path.is_file():
            raise SystemExit(f"{name} returned without its result record.")
        json.loads(result_path.read_text())
        records.append({"name": name, "script": script,
                        "result": str(result_path.relative_to(output)),
                        "sha256": digest(result_path)})
        print(f"Completed {name}.", flush=True)
    if any(digest(ROOT / path) != value for path, value in before.items()):
        raise SystemExit("A recorded input changed during the replay; rerun on stable sources.")
    summary.write_text(json.dumps({
        "scope": "Finite symbolic identities and outward rational constant bounds; "
                 "not verification of analytic or geometric existence theorems.",
        "checks": records,
        "source_sha256": before,
    }, indent=2, sort_keys=True) + "\n")
    print(f"{len(CHECKS)} finite checks completed. Report: {summary}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="Keep result records here; otherwise use a temporary directory.")
    args = parser.parse_args()
    if args.output:
        replay(args.output.resolve())
    else:
        with tempfile.TemporaryDirectory(prefix="murakamis-paper-algebra-") as directory:
            replay(Path(directory))


if __name__ == "__main__":
    main()
