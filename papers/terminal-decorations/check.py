#!/usr/bin/env python3
"""Replay finite identities supporting terminal tangle decorations.

The imported standard-library verifier compares polynomial identities,
rational constants, oriented face updates and endpoint components.
Its rational count examples and sixteen stellar patches are bounded
checks; the all-real count algorithm, arbitrary local construction and
volume implication remain written proofs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

if not __debug__:
    raise SystemExit("Run without -O: the exact verifier uses assertions.")

ROOT = Path(__file__).resolve().parents[2]
PAPER = Path(__file__).resolve().parent
VERIFIER = ROOT / "experiments/audit_actual_balanced_terminal_fans.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PAPER / "build/checks")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name in ("summary.json", "finite-identities.json"):
        (output / name).unlink(missing_ok=True)
    sources = [Path(__file__), PAPER / "main.tex", VERIFIER]
    sources += sorted((PAPER / "figures").glob("*.tex"))
    before = {str(path.relative_to(ROOT)): digest(path) for path in sources}
    command = [
        sys.executable, "-I", str(VERIFIER), "--output",
        str(output / "finite-identities.json"),
    ]
    process = subprocess.run(
        command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    (output / "finite-identities.log").write_text(process.stdout)
    if process.returncode:
        raise SystemExit(process.stdout)
    results = json.loads((output / "finite-identities.json").read_text())
    if results["status"] != "passed":
        raise SystemExit("The exact verifier did not finish successfully.")
    if results["rational_gap_lower"] != "3347/27720":
        raise SystemExit("Unexpected rational balance constant.")
    if len(results["ordered_patches"]) != 16:
        raise SystemExit("Unexpected oriented patch record.")
    if len(results["even_count_examples"]) != 49:
        raise SystemExit("Unexpected bounded count-example record.")
    # Every claimed endpoint identity is recomputed by the helper's graph
    # traversal, rather than supplied as an expected scalar source value.
    required = {
        "interstice square recurrence", "closed fan recurrence",
        "closed normalized square", "odd pairing quarter-turn",
        "odd pair stack", "identity on left", "identity on right",
    }
    if not required <= set(results["checks"]):
        raise SystemExit("Required finite identities are absent.")
    if any(digest(ROOT / path) != value for path, value in before.items()):
        raise SystemExit("A recorded input changed during the replay; rerun on stable sources.")
    record = {
        "scope": (
            "Exact polynomial and rational identities, sixteen oriented "
            "stellar patches with matching/mark/parity, and endpoint graph "
            "components. Forty-nine count examples supplement the written "
            "all-real construction. No invariant, analytic asymptotic, "
            "global packing or volume theorem is proved by this runner."
        ),
        "arithmetic": "Python integers and fractions only",
        "rational_gap_lower": results["rational_gap_lower"],
        "ordered_patch_count": len(results["ordered_patches"]),
        "count_example_count": len(results["even_count_examples"]),
        "input_sha256": before,
        "finite_record_sha256": digest(output / "finite-identities.json"),
    }
    (output / "summary.json").write_text(json.dumps(record, indent=2) + "\n")
    print("Replayed the exact terminal recurrence, oriented patches and pairings.")
    print(f"Results: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
