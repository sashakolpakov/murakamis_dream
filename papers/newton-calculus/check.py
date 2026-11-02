#!/usr/bin/env python3
"""Run the two retained Newton checks without duplicating their implementations.

The checks cover bounded exact finite algebra, supports and rational stationary
identities. The written all-level and variational proofs are not tested by
running a finite sample.
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
    "main.tex", "finite.tex", "supports.tex", "variation.tex", "profiles.tex",
    "completed.tex", "conclusion.tex", "figures/tangle-construction.tex",
    "figures/reduced-tree.tex", "check.py", "README.md",
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
        raise SystemExit("Run without -O: the delegated checks require assertions.")

    before = {str((HERE / name).relative_to(ROOT)): digest(HERE / name)
              for name in SOURCES}
    specifications = (
        ("physical_newton", "papers/newton-tangles/check.py",
         output / "physical-newton.json", output / "physical-newton.json",
         "source_sha256"),
        ("strict_supports_profiles", "papers/strict-newton-profiles/check.py",
         output / "strict-supports", output / "strict-supports" / "summary.json",
         "source_hashes"),
    )
    reports = {}
    for name, script, argument, result_path, hash_key in specifications:
        result_path.unlink(missing_ok=True)
        command = [sys.executable, "-I", str(ROOT / script), "--output", str(argument)]
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        (output / (name + ".log")).write_text(result.stdout + result.stderr)
        if result.returncode:
            raise SystemExit(f"{script} failed with exit code {result.returncode}; "
                             f"see {output / (name + '.log')}")
        report = json.loads(result_path.read_text())
        for relative, expected in report[hash_key].items():
            if digest(ROOT / relative) != expected:
                raise SystemExit(f"Input changed during delegated check: {relative}")
            previous = before.setdefault(relative, expected)
            if previous != expected:
                raise SystemExit(f"Conflicting input hashes: {relative}")
        reports[name] = report
    for relative, expected in before.items():
        if digest(ROOT / relative) != expected:
            raise SystemExit(f"Input changed during check: {relative}")
    report = {
        "scope": "The two retained bounded exact Newton check suites, with the merged paper sources recorded.",
        "excluded_claims": [
            "Finite examples do not prove the all-level polynomial identities.",
            "The boundary argument, unique optimizer and positive-source limit retain written proofs.",
            "No signed filling, invariant asymptotic or hyperbolic volume statement is certified here.",
        ],
        "checks": reports,
        "source_sha256": before,
    }
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary": str(destination), "completed_suites": list(reports)}, sort_keys=True))


if __name__ == "__main__":
    main()
