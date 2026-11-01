#!/usr/bin/env python3
"""Recheck the 54-region cap certificates and finite polynomial identities.

The default checks use only Python's standard library. --algebra also checks
the original spectral products in exact cyclotomic fields and requires SymPy.
The all-level estimates and the geometric volume interpretation are written
proofs; finite checks do not establish them by extrapolation.
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Directory for fresh reports and logs.")
    parser.add_argument("--algebra", action="store_true",
                        help="Also run exact cyclotomic checks (requires SymPy).")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="cap-response-") as temporary:
        output = args.output.resolve() if args.output else Path(temporary)
        output.mkdir(parents=True, exist_ok=True)
        jobs = [
            ("topology", "verify_r54_source_topology.py", []),
            ("response", "verify_r54_response.py", []),
            ("complete-flow", "verify_r54_complete_flow_lower.py", []),
            ("tilted-pressure", "verify_r54_tilted_pressure.py",
             ["--response-result", str(output / "response.json")]),
            ("stable-sections", "verify_cap_stable_sections.py", []),
        ]
        if args.algebra:
            jobs.append(("spectral-algebra", "verify_cap_coupled_spectral_algebra.py", []))
        records = {}
        for name, script, extra in jobs:
            target = output / f"{name}.json"
            # A pre-existing report must never replace this invocation's output.
            target.unlink(missing_ok=True)
            command = [sys.executable, "-I", str(ROOT / "experiments" / script),
                       "--output", str(target), *extra]
            print(f"Checking {name}…", flush=True)
            completed = subprocess.run(command, cwd=ROOT, text=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (output / f"{name}.log").write_text(completed.stdout)
            if completed.returncode or not target.is_file():
                raise SystemExit(f"{name} failed:\n{completed.stdout}")
            records[name] = json.loads(target.read_text())
        inputs = [ROOT / "experiments" / script for _, script, _ in jobs]
        inputs += [ROOT / "experiments" / name for name in (
            "actual_singleton_sector_obstruction_certificate.json",
            "r54_response_certificate.json", "r54_complete_flow_lower_certificate.json",
            "r54_tilted_pressure_certificate.json",
            "verify_conway_two_leaf_block_alias_certificate.py")]
        inputs += [ROOT / "notes" / name for name in (
            "research_protected_cap_coupled_norm.md", "research_cap_common_axis_bound.md",
            "research_cap_uniform_spectral_gap.md", "research_cap_dirichlet_response_region.md")]
        inputs.append(Path(__file__).resolve())
        report = {
            "scope": "Exact 54-region topology, response and entropy certificates; finite polynomial checks.",
            "written_proof_inputs": [
                "odd-level determinant stability and coefficient asymptotics",
                "uniform alternating-section and spectral norm estimates",
                "stationary-point localization and response inequalities",
                "strict omitted-coefficient gap and complete geometric volume identity"],
            "not_established": [
                "the even-level exterior bound", "simultaneously varying other spectra",
                "the full filled-knot remainder or a new knot volume theorem"],
            "checks": records,
            "source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in inputs},
        }
        (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
        print(f"Completed {len(jobs)} checks; the proof scopes are recorded separately.")
        if args.output:
            print(f"Report: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
