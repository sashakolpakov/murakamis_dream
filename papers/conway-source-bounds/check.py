#!/usr/bin/env python3
"""Replay the two exact supporting-plane certificates used by this paper.

The written proofs supply the source identities, concavity, recurrence
estimates and tree induction. This command validates only the fixed
rational tables, their full-domain coverage and their interval margins.
Python's standard library is sufficient.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PAPER = Path(__file__).resolve().parent
INPUTS = [
    "papers/conway-source-bounds/main.tex",
    "papers/conway-source-bounds/local.tex",
    "papers/conway-source-bounds/composition.tex",
    "papers/conway-source-bounds/arithmetic.tex",
    "papers/conway-source-bounds/figures/tangent-propagation.tex",
    "papers/conway-source-bounds/check.py",
    "papers/newton-tangles/main.tex",
    "experiments/verify_conway_two_leaf_block_alias_certificate.py",
    "experiments/conway_two_leaf_block_alias_certificate.json",
    "experiments/verify_conway_single_leaf_attachment_certificate.py",
    "experiments/conway_single_leaf_attachment_certificate.json",
]


def hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in INPUTS}


def replay(name, script, data, output):
    record = output / f"{name}.json"
    log = output / f"{name}.log"
    record.unlink(missing_ok=True)
    run = subprocess.run(
        [sys.executable, "-I", str(ROOT / script),
         "--data", str(ROOT / data), "--output", str(record)],
        cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(run.stdout)
    if run.returncode:
        raise RuntimeError(f"{name} failed; see {log}")
    result = json.loads(record.read_text())
    if result.get("status") != "PASS" or result.get("exact_rational_arithmetic") is not True:
        raise RuntimeError(f"{name} did not return an exact certificate record")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PAPER / "build" / "check",
                        help="output directory; default: paper-local build/check")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    summary_path = output / "summary.json"
    summary_path.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Run without -O: the certificate verifiers require assertions")
    before = hashes()

    two = replay("two-leaf", INPUTS[7], INPUTS[8], output)
    single = replay("single-attachment", INPUTS[9], INPUTS[10], output)
    F = Fraction
    assert two["cells"] == 16 and len(two["records"]) == 32
    assert F(two["minimum_lower"]) == F(
        210002102902309638093785766005979344329,
        5000000000000000000000000000000000000000)
    assert F(two["minimum_lower"]) > F(1, 25) > F(1, 100)
    assert single["rectangle_count"] == 55
    assert single["endpoint_vertex_inequalities"] == 880
    assert F(single["minimum_lower"]) == F(
        55437191760019874892517972684020763373, 10**40)
    assert F(single["minimum_lower"]) > F(1, 1000)
    x = F(2, 3)
    ti_lower = sum(((-1)**j*x**(2*j+1)/F((2*j+1)**2)
                    for j in range(4)), F(0))
    z = F(1, 5)
    log_upper = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(3)), F(0))
    log_upper += 2*z**7/(7*(1-z*z))
    assert ti_lower == F(1708762, 2679075)
    assert log_upper == F(177391, 437500)
    leaf_margin = F(7, 11)*ti_lower-log_upper
    assert leaf_margin == F(57269, 136687500) > F(1, 2500)

    after = hashes()
    if before != after:
        raise RuntimeError("An input changed during verification; no summary written")
    result = {
        "verified": True,
        "scope": {
            "two_leaf": "16 complete slope intervals; 288 vertex/endpoint inequalities",
            "single_attachment": "55 recursively covering rectangles; 880 vertex/corner inequalities",
            "elementary_leaf": "exact rational lower bound after written alternating-series remainders",
            "excluded": [
                "all-level physical polynomial identities",
                "uniform recurrence-product estimates",
                "whole-tree propagation",
                "filled-invariant or hyperbolic-volume asymptotics",
            ],
        },
        "two_leaf": {
            "cells": 16, "inequalities": 288,
            "minimum_lower": two["minimum_lower"], "claimed_gap": "1/100",
        },
        "single_attachment": {
            "rectangles": 55, "inequalities": 880,
            "minimum_lower": single["minimum_lower"], "claimed_gap": "1/1000",
        },
        "elementary_leaf": {
            "lower": str(leaf_margin), "claimed_gap": "1/2500",
        },
        "input_hashes": before,
    }
    summary_path.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"verified": True, "summary": str(summary_path),
                      "two_leaf_inequalities": 288,
                      "attachment_inequalities": 880,
                      "elementary_leaf_lower": str(leaf_margin)}, indent=2))


if __name__ == "__main__":
    main()
