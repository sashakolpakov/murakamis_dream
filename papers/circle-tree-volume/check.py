#!/usr/bin/env python3
"""Run the two retained circle-tree checks without copying their implementations.

The checks cover exact edge identities, rational budgets, endpoint pairings
and finite quotient/root-grid comparisons. They do not prove uniform contour
estimates, recursive asymptotics or geometric volume identities.
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
    "main.tex", "finite-bounds.tex", "edge-packet.tex", "fourier-trace.tex",
    "summed-filling.tex", "summed-conclusion.tex", "directed-criterion.tex",
    "directed-kernels.tex", "directed-recursion.tex", "directed-applications.tex",
    "reproduction.tex", "references.tex", "figures/joint-contour.tex",
    "figures/normalized-recursion.tex", "figures/paired-leaves.tex",
    "check.py", "README.md",
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
        ("summed_criterion", "papers/circle-tree-asymptotics/check.py",
         output / "summed.json", output / "summed.json", "source_sha256"),
        ("directed_criterion", "papers/directed-tree-asymptotics/check.py",
         output / "directed.json", output / "directed.json", "source_sha256"),
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
        "scope": "The retained summed and directed finite check suites, with the combined paper sources recorded.",
        "excluded_claims": [
            "Finite samples do not prove the uniform complex kernel or contour estimates.",
            "Fourier tails, Gaussian asymptotics and the normalized subtree induction retain written proofs.",
            "The original diagram normalization and the hyperbolic metric-volume identification are separate written inputs.",
        ],
        "checks": reports,
        "source_sha256": before,
    }
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary": str(destination), "completed_suites": list(reports)}, sort_keys=True))


if __name__ == "__main__":
    main()
