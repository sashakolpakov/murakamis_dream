#!/usr/bin/env python3
"""Compile the Lean proofs and audit every exported theorem's axioms.

This checks the stated algebraic and conditional limit implications, not the
analytic or geometric premises of their applications. Axiom inspection follows a successful library
build. Requires the pinned Lean toolchain; no external Lean packages are used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FORMAL = ROOT / "formal"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default=shutil.which("lake"),
                        help="Path to Lake; the project pins Lean 4.32.2.")
    parser.add_argument("--output", type=Path,
                        help="Save the report and compiler output in this directory.")
    args = parser.parse_args()
    if not args.lake:
        raise SystemExit("Lake is missing. Install the toolchain in formal/lean-toolchain.")
    temporary = tempfile.TemporaryDirectory(prefix="volume-proof-logic-")
    output = args.output.resolve() if args.output else Path(temporary.name)
    output.mkdir(parents=True, exist_ok=True)

    source_files = sorted((FORMAL / "VolumeLogic").glob("*.lean"))
    # Attributes may precede a theorem on the same line. Such declarations
    # need the same axiom inspection as unannotated public theorems.
    declaration = re.compile(
        r"^[ \t]*(?:@\[[^\n]*\][ \t]*)*theorem[ \t]+(\w+)", re.M)
    names = ["VolumeLogic." + name for path in source_files
             for name in declaration.findall(path.read_text())]
    inspected = re.findall(r"^#print axioms (\S+)",
                           (FORMAL / "AxiomAudit.lean").read_text(), re.M)
    if len(names) != len(set(names)) or sorted(names) != sorted(inspected):
        raise SystemExit("AxiomAudit.lean must inspect every theorem exactly once.")

    commands = [[args.lake, "build"],
                [args.lake, "env", "lean", "AxiomAudit.lean"]]
    logs = []
    for index, command in enumerate(commands):
        completed = subprocess.run(command, cwd=FORMAL, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = completed.stdout
        logs.append(log)
        (output / ("build.txt" if index == 0 else "axioms.txt")).write_text(log)
        if completed.returncode or re.search(r"\b(?:warning|error):", log):
            raise SystemExit(log + "\nLean verification did not complete cleanly.")

    axioms = {}
    for name, dependencies in re.findall(
            r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", logs[1]):
        axioms[name] = [a.strip() for a in dependencies.split(",") if a.strip()]
    for name in re.findall(r"'([^']+)' does not depend on any axioms", logs[1]):
        axioms[name] = []
    if sorted(axioms) != sorted(names):
        raise SystemExit("The compiler did not report every expected theorem.")
    unexpected = {name: sorted(set(items) - ALLOWED)
                  for name, items in axioms.items() if set(items) - ALLOWED}
    if unexpected:
        raise SystemExit("Unexpected logical assumptions: " + json.dumps(unexpected))

    inputs = source_files + [FORMAL / name for name in
                            ("VolumeLogic.lean", "AxiomAudit.lean", "lakefile.toml",
                             "lean-toolchain", "lake-manifest.json")]
    inputs.append(Path(__file__).resolve())
    report = {
        "scope": "Finite support, root-grid exponent selection, canonical polynomial reduction and products, resolvent reproduction, formal regrading, local composition comparisons, whole finite-sector filling bounds, epsilon limits with both parities, strict-gap noncancellation, scalar normalization, and conditional fixed-filling volume transfer for the same indexed invariant and diagram.",
        "not_formalized": ["the actual Chebyshev root data and crossing-operator functional",
                           "the exact knot-diagram adapter", "uniform analytic estimates",
                           "geometric realization and filling",
                           "complex modulus and log(x)/N realization (checked separately by the optional formal-real Mathlib package)",
                           "verification of the analytic and geometric premises for each knot family"],
        "toolchain": (FORMAL / "lean-toolchain").read_text().strip(),
        "commands": [["lake", *command[1:]] for command in commands],
        "theorems": axioms,
        "source_sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in inputs},
        "result": "All listed declarations compiled; only the permitted foundational axioms occur.",
    }
    (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Checked {len(names)} Lean theorems and their axiom dependencies.")
    print("The analytic and geometric hypotheses remain separate written proofs.")
    if args.output:
        print(f"Report: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
