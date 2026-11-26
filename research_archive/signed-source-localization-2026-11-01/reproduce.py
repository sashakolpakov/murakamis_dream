#!/usr/bin/env python3
"""Replay the three finite algebra suites and compare with saved records.

Run from any directory. NumPy and SymPy are needed for the continuant
suite. These checks do not establish the all-level analytic estimates.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


def stable_result(value):
    if isinstance(value, dict):
        return {
            key: stable_result(item)
            for key, item in value.items()
            if key != "elapsed_seconds"
        }
    if isinstance(value, list):
        return [stable_result(item) for item in value]
    return value


def main():
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=base / "reproduction-output")
    args = parser.parse_args()
    missing = [name for name in ("numpy", "sympy") if importlib.util.find_spec(name) is None]
    if missing:
        parser.error(
            "Missing " + ", ".join(missing)
            + ". Install requirements-reproduction.txt with this Python interpreter."
        )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    suites = [
        ("continuant", "md-fixed-spectrum-audit-continuant.py",
         "md-fixed-spectrum-continuant-results.json"),
        ("excursion", "md-shifted-cyclic-excursion-audit.py",
         "md-shifted-cyclic-excursion-results.json"),
        ("half-charge", "md-filled-complement-half-charge-audit.py",
         "md-filled-complement-half-charge-results.json"),
    ]
    report = []
    for name, script, record in suites:
        output = args.output_dir / record
        run = subprocess.run(
            [sys.executable, str(base / "reproduction" / script), "--output", str(output)],
            text=True, capture_output=True,
        )
        (args.output_dir / f"{name}.stdout.txt").write_text(run.stdout)
        (args.output_dir / f"{name}.stderr.txt").write_text(run.stderr)
        if run.returncode:
            print(run.stderr, file=sys.stderr)
            raise SystemExit(f"{name} exited with code {run.returncode}; see {args.output_dir}")
        actual = json.loads(output.read_text())
        expected = json.loads((base / "evidence" / "originals" / record).read_text())
        if stable_result(actual) != stable_result(expected):
            raise SystemExit(f"{name} differs from the saved record; inspect {output}")
        report.append({"suite": name, "matches_saved_result": True, "output": str(output)})
        print(f"{name}: reproduced the saved finite checks")
    result = {
        "scope": "Finite algebra only; the written proofs contain the all-level arguments.",
        "results": report,
    }
    (args.output_dir / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"Results: {args.output_dir / 'summary.json'}")


if __name__ == "__main__":
    main()
