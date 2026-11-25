#!/usr/bin/env python3
"""Run the local-sector and central-cofactor checks for this paper.

The results check finite algebraic identities at the listed levels. Uniform
spectral bounds, complex contour estimates and Gaussian asymptotics retain
written proofs and are not conclusions of these finite checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCES = (
    "main.tex", "local-bounds.tex", "finite-cofactors.tex",
    "nodal-comparison.tex", "signed-transfer.tex", "triangle-action.tex",
    "one-sided-envelope.tex", "face-phases.tex", "shared-coefficient.tex",
    "positive-matrices.tex", "complex-cofactors.tex", "angular-gap.tex",
    "shared-saddle.tex", "spectral-gap.tex", "filling-input.tex",
    "check_local.py", "check_central.py",
    "references.tex", "figures/local-path-partition.tex",
    "figures/shared-tetrahedral-coefficient.tex", "check.py", "README.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "build" / "check")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "summary.json"
    destination.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Run without -O: the component checks require normal Python execution.")

    before = {str((HERE / name).relative_to(ROOT)): digest(HERE / name)
              for name in SOURCES}
    specifications = (
        ("local_sectors", "check_local.py"),
        ("central_cofactors", "check_central.py"),
    )
    reports = {}
    for name, filename in specifications:
        script = HERE / filename
        result_path = output / (name + ".json")
        result_path.unlink(missing_ok=True)
        command = [sys.executable, "-I", str(script),
                   "--output", str(result_path)]
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        log = output / (name + ".log")
        log.write_text(result.stdout + result.stderr)
        if result.returncode:
            raise SystemExit(f"{filename} failed with exit code {result.returncode}; see {log}")
        report = json.loads(result_path.read_text())
        for relative, expected in report["source_sha256"].items():
            if digest(ROOT / relative) != expected:
                raise SystemExit(f"Input changed during component check: {relative}")
            previous = before.setdefault(relative, expected)
            if previous != expected:
                raise SystemExit(f"Conflicting input hashes: {relative}")
        reports[name] = report
    for relative, expected in before.items():
        if digest(ROOT / relative) != expected:
            raise SystemExit(f"Input changed during check: {relative}")
    report = {
        "scope": "The retained local-sector and central-cofactor finite algebra suites, with the combined paper sources recorded.",
        "excluded_claims": [
            "Finite levels do not prove uniform real spectral or face-phase bounds.",
            "Local zero-free neighborhoods, contour contributions and Gaussian asymptotics retain written proofs.",
            "The full complementary-source estimate and geometric volume identification are separate inputs.",
        ],
        "checks": reports,
        "source_sha256": before,
    }
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary": str(destination), "completed_suites": list(reports)}, sort_keys=True))


if __name__ == "__main__":
    main()
