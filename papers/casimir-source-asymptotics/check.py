#!/usr/bin/env python3
"""Run the two retained finite Casimir-source checks without copying their code.

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
        raise SystemExit("Run without -O: the delegated checks retain their original assertions.")

    before = {str((HERE / name).relative_to(ROOT)): digest(HERE / name)
              for name in SOURCES}
    specifications = (
        ("local_sectors", "local-coefficients", "source_sha256"),
        ("central_cofactors", "source-asymptotics", "paper_sha256"),
    )
    for _, directory, _ in specifications:
        for name in ("main.tex", "check.py"):
            relative = f"papers/{directory}/{name}"
            before[relative] = digest(ROOT / relative)

    reports = {}
    for name, directory, paper_key in specifications:
        script = f"papers/{directory}/check.py"
        result_path = output / (name + ".json")
        result_path.unlink(missing_ok=True)
        command = [sys.executable, "-I", str(ROOT / script),
                   "--output", str(result_path)]
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        log = output / (name + ".log")
        log.write_text(result.stdout + result.stderr)
        if result.returncode:
            raise SystemExit(f"{script} failed with exit code {result.returncode}; see {log}")
        report = json.loads(result_path.read_text())
        expected_sources = {
            f"papers/{directory}/main.tex": report[paper_key],
            script: report["script_sha256"],
        }
        for relative, expected in expected_sources.items():
            if digest(ROOT / relative) != expected or before[relative] != expected:
                raise SystemExit(f"Input changed during delegated check: {relative}")
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
