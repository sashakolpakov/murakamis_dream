#!/usr/bin/env python3
"""Replay the exact certificates used in the Conway composition manuscript.

Only the Python standard library is required. Verification is serial and
does not modify the stored expected records. This program checks the stated
finite certificates; it does not mechanically verify the whole volume proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    {
        "name": "two-leaf-block",
        "script": "experiments/verify_conway_two_leaf_block_alias_certificate.py",
        "data": "experiments/conway_two_leaf_block_alias_certificate.json",
        "expected": "experiments/conway_two_leaf_block_alias_certificate_results.json",
        "scope": "Both alias configurations on the entire original two-leaf domain; 16 slope intervals and 288 endpoint/vertex comparisons.",
    },
    {
        "name": "single-leaf-attachment",
        "script": "experiments/verify_conway_single_leaf_attachment_certificate.py",
        "data": "experiments/conway_single_leaf_attachment_certificate.json",
        "expected": "experiments/conway_single_leaf_attachment_certificate_results.json",
        "scope": "Single-leaf dual gap on the full slope square and product tetrahedron; 55 rectangles and 880 corner/vertex comparisons.",
    },
    {
        "name": "single-leaf-endpoint",
        "script": "experiments/verify_conway_single_leaf_endpoint_certificate.py",
        "expected": "experiments/conway_single_leaf_endpoint_certificate_results.json",
        "scope": "Four-vertex endpoint certificate used with the separately proved monotone-response lemma.",
    },
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def elementary_bounds() -> dict:
    """Check rational endpoints after the analytic series bounds in the paper."""
    f = Fraction
    x = f(2, 3)
    ti_lower = sum((-1)**j*x**(2*j+1)/((2*j+1)**2) for j in range(4))
    y = f(1, 5)
    log_upper = 2*(y + y**3/3 + y**5/5 + y**7/(7*(1-y*y)))
    leaf_gap = f(7, 11)*ti_lower-log_upper
    isolated_gap = f(2)*f(7, 22)*(f(32, 9)-3*f(273, 256))
    checks = [
        ti_lower == f(1708762, 2679075),
        log_upper == f(177391, 437500),
        leaf_gap == f(57269, 136687500),
        leaf_gap > f(1, 2500),
        isolated_gap == f(5747, 25344),
        isolated_gap > f(1, 100),
    ]
    if not all(checks):
        raise ArithmeticError("An elementary rational endpoint identity failed")
    return {
        "name": "elementary-rational-endpoints",
        "status": "PASS",
        "leaf_gap_lower": str(leaf_gap),
        "isolated_three_leaf_gap_lower": str(isolated_gap),
        "scope": "Exact rational arithmetic only. The alternating-series, logarithm-tail and geometric volume inequalities are proved in the manuscript and source notes.",
    }


def run_case(case: dict, output: Path) -> dict:
    destination = output / (case["name"] + ".json")
    command = [sys.executable, "-I", "-B", str(ROOT / case["script"])]
    if "data" in case:
        command += ["--data", str(ROOT / case["data"])]
    command += ["--output", str(destination)]
    # Isolated mode prevents PYTHONOPTIMIZE from disabling verifier assertions.
    process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if process.returncode:
        raise RuntimeError(case["name"] + " failed:\n" + process.stdout + process.stderr)
    if process.stderr.strip():
        raise RuntimeError(case["name"] + " wrote unexpected diagnostics:\n" + process.stderr)
    actual = json.loads(destination.read_text())
    expected = json.loads((ROOT / case["expected"]).read_text())
    if actual != expected:
        raise ValueError(case["name"] + " differs from its stored exact record")
    if actual.get("status") != "PASS" or not actual.get("exact_rational_arithmetic"):
        raise ValueError(case["name"] + " did not produce an exact PASS")
    return {"name": case["name"], "status": "PASS", "scope": case["scope"],
            "matches_stored_record": True, "minimum_lower": actual["minimum_lower"],
            "output": destination.name}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List checks without executing them")
    parser.add_argument("--plan", action="store_true", help="Show inputs and verification scope")
    parser.add_argument("--output", type=Path, help="Save fresh records here; default is a temporary directory")
    args = parser.parse_args()
    if args.list or args.plan:
        print(json.dumps({"checks": CASES, "additional_check": "elementary-rational-endpoints",
                          "dependencies": "Python standard library",
                          "execution": "Serial; no proof check is run by --list or --plan"}, indent=2))
        return 0
    with tempfile.TemporaryDirectory(prefix="conway-certificates-") as temporary:
        output = args.output.resolve() if args.output else Path(temporary)
        output.mkdir(parents=True, exist_ok=True)
        records = []
        for case in CASES:
            print("Checking " + case["name"] + " …", flush=True)
            records.append(run_case(case, output))
        records.append(elementary_bounds())
        sources = {"repro/verify.py"}
        for case in CASES:
            sources.update(case[key] for key in ("script", "data", "expected") if key in case)
        result = {
            "status": "PASS", "python": sys.version.split()[0], "checks": records,
            "source_sha256": {name: digest(ROOT / name) for name in sorted(sources)},
            "scope": "Exact finite certificates and rational endpoint identities. This does not certify the topological invariant dictionary, geometric gluing, analytic interpolation, or filling-period theorem.",
        }
        (output / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, ArithmeticError, RuntimeError) as exc:
        print("FAIL: " + str(exc).replace(str(ROOT), "<repository>"), file=sys.stderr)
        raise SystemExit(1)
