#!/usr/bin/env python3
"""Replay finite block identities and rational constants used by this paper.

This does not verify the cut topology, global developing maps, contraction
theorem, metric completion, or absolute volume identity.  The two imported
checks run with private output paths; no repository reference output is changed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

if not __debug__:
    raise SystemExit("Run without -O: the imported exact verifiers use assertions.")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    paper = Path(__file__).resolve().parent
    root = paper.parents[1]
    names = ["audit_two_octahedron_angular_edge_block.py",
             "audit_all_circle_vertexwise_geometry.py"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.unlink(missing_ok=True)
    paths = [Path(__file__).resolve(), paper / "main.tex"]
    paths += sorted((paper / "figures").glob("*.tex"))
    paths += [root / "papers/marked-fillings/main.tex"]
    paths += [root / "experiments" / name for name in names]
    before = {str(p.relative_to(root)): sha(p) for p in paths}
    records = []
    with tempfile.TemporaryDirectory(prefix="circle-tree-geometry-") as tmp:
        for name in names:
            source = root / "experiments" / name
            destination = Path(tmp) / (source.stem + ".json")
            subprocess.run([sys.executable, "-I", str(source), "--output", str(destination)],
                           check=True, capture_output=True, text=True)
            records.append({"source": str(source.relative_to(root)),
                            "sha256": sha(source),
                            "result": json.loads(destination.read_text())})
    # Extra finite dictionary: affine multipliers after sending Z to infinity.
    # These identities are symbolic in E,Z, not tests at sampled shapes.
    import sympy as s
    E, Z = s.symbols("E Z")
    R = Z * (1 + E - Z) / E
    Q = (E - Z) / (Z - 1)
    rho = Z / (1 + E - Z)
    W0 = s.Matrix([[1, 0], [0, E]])
    W2 = s.Matrix([[E-R, R*(1-E)], [E-1, 1-E*R]])
    S = s.Matrix([[0, -E*R], [1, -1-E]])
    A = s.Matrix([[R, -R], [1, E*R-1-E]])
    B = s.Matrix([[R/E-1-1/E, R], [-1, R]])
    dictionary = [("longitude", W2.inv()*W0, Q**2),
                  ("pure meridian", S.inv(), rho),
                  ("negative odd meridian", A.inv()*W0, rho*Q),
                  ("positive odd meridian", W0.inv()*B, rho/Q)]
    identities = []
    for name, matrix, expected in dictionary:
        fixed = matrix[0, 0]*Z + matrix[0, 1] - Z*(matrix[1, 0]*Z + matrix[1, 1])
        multiplier = (matrix[1, 0]*Z + matrix[1, 1])**2 / matrix.det()
        if s.factor(fixed) != 0 or s.factor(multiplier-expected) != 0:
            raise AssertionError(name)
        identities.append(name)
    # The reciprocal convention must not be silently substituted.
    if s.factor(rho - 1/rho) == 0:
        raise AssertionError("the multiplier/derivative negative control collapsed")
    if any(sha(root / p) != value for p, value in before.items()):
        raise SystemExit("A recorded input changed during the replay; rerun on stable sources.")
    output = {
        "scope": "Finite rational identities and enclosures only; not a verification of topology, analytic existence, metric completion, or volume calibration.",
        "source_sha256": before,
        "replays": records,
        "peripheral_multiplier_identities": identities,
        "negative_control": "The derivative at Z differs from the affine multiplier at the selected infinity flag.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "replays": len(records),
                      "peripheral_identities": len(identities)}, sort_keys=True))


if __name__ == "__main__":
    main()
