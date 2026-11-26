#!/usr/bin/env python3
"""Exact scalar inequalities for the positive-path tangent-sector theorem."""

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-positive-path-tangent-sector.json")
    args = parser.parse_args()
    x, y = Q(69, 80), Q(23, 20)
    tail_ratio = y * y / 20
    assert tail_ratio < 1
    sinh_upper = y + y ** 3 / (6 * (1 - tail_ratio))
    assert sinh_upper < Q(10, 7)
    margin = 24 * (x + x ** 3 / 6) ** 2 - 11 * Q(10, 7) ** 2
    assert margin == Q(683309192723, 6422528000000) > 0
    assert (Q(7, 4) ** 2 - 1) / 3 == Q(11, 16) < Q(3, 4)
    result = {
        "status": "passed",
        "arithmetic": "exact fractions",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sinh_upper_at_23_over_20": str(sinh_upper),
        "margin_below_10_over_7": str(Q(10, 7) - sinh_upper),
        "positive_comparison_margin": str(margin),
        "scope": "scalar inequalities only; the maximum-ratio proof is written",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
