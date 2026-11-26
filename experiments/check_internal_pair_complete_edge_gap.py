#!/usr/bin/env python3
"""Exact rational constants for the complete-edge gap of an internal pair."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="repro/results/research-internal-pair-complete-edge-gap.json")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    h = Q(107, 100)
    lower_sqrt = Q(707, 500)
    upper_sqrt = Q(99, 70)
    upper_pi = Q(22, 7)
    cosh_lower = sum(h ** (2*j) / factorial(2*j) for j in range(4))
    sinh_072_lower = sum(Q(18, 25) ** (2*j+1) / factorial(2*j+1) for j in range(4))
    sinh_0882_lower = sum(Q(441, 500) ** (2*j+1) / factorial(2*j+1) for j in range(4))
    blocks = [
        Q(1, (8*j+1)**2) + Q(1, (8*j+3)**2)
        - Q(1, (8*j+5)**2) - Q(1, (8*j+7)**2)
        for j in range(3)
    ]
    psi_lower = 2*lower_sqrt*sum(blocks)/upper_pi
    correction = (h*h/2-h**4/24)/(upper_sqrt*upper_pi)
    gap_margin = Q(239, 250)-h+correction-Q(1, 500)
    margins = {
        "sqrt2_lower": 2-lower_sqrt**2,
        "sqrt2_upper": upper_sqrt**2-2,
        "cosh_sinh_squared": cosh_lower*sinh_072_lower**2-1,
        "sinh_0882": sinh_0882_lower-1,
        "height_period_contradiction": 3*h/2-Q(18, 25)-Q(441, 500),
        "psi_pi_over_2": psi_lower-Q(239, 250),
        "edge_gap_above_1_over_500": gap_margin,
    }
    assert all(b > 0 for b in blocks)
    assert all(v > 0 for v in margins.values())
    assert gap_margin == Q(261699551, 522720000000)
    script = Path(__file__).resolve()
    proof = root/"notes/research_internal_pair_complete_edge_gap.md"
    record = {
        "status": "passed",
        "arithmetic": "exact rational",
        "positive_scalar_margins": len(margins),
        "positive_fourier_blocks": len(blocks),
        "exact_margin_identity": True,
        "margins": {name: {"numerator": v.numerator, "denominator": v.denominator}
                    for name, v in margins.items()},
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
        "scope": "Scalar constants only; analytic and original-source arguments are in the proof note.",
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = root/output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print("Passed: 7 strict rational margins, 3 positive Fourier blocks, and the exact gap identity.")
    print(f"Result: {output}")


if __name__ == "__main__":
    main()
