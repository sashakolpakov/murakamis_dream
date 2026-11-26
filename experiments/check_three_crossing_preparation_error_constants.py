#!/usr/bin/env python3
"""Exact rational constants in the full preparation-error norm bound."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_three_crossing_global_preparation_error.md"
DEPENDENCY = ROOT / "notes/research_three_crossing_next_step_profile.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-three-crossing-preparation-error-constants.json",
    )
    args = parser.parse_args()
    catalan_upper = sum(F((-1)**j, (2*j+1)**2) for j in range(65))
    assert catalan_upper < F(229,250)
    crossing_upper = F(286009121,861616000)
    entropy_upper = 4*F(229,250)/F(157,50)+crossing_upper
    assert entropy_upper == F(1291410721,861616000)
    rho = F(1,10**6)
    sqrt_rho = F(1,1000)
    assert sqrt_rho**2 == rho
    gap = F(3,2)-entropy_upper-sqrt_rho
    assert gap == F(151663,861616000) > 0
    result = {
        "status":"passed",
        "scope": (
            "Exact rational constants only. The matrix entropy maximizations, "
            "Newton-vector bound and original polynomial identities are proved "
            "in the cited written notes."
        ),
        "script_sha256":digest(Path(__file__).resolve()),
        "note_sha256":digest(NOTE),
        "dependency_sha256":{str(DEPENDENCY.relative_to(ROOT)):digest(DEPENDENCY)},
        "catalan_upper_terms":65,
        "catalan_partial_sum_upper":str(catalan_upper),
        "catalan_simplified_upper":"229/250",
        "one_crossing_exponent_upper":str(crossing_upper),
        "zero_radius_error_exponent_upper":str(entropy_upper),
        "boundary_radius":str(rho),
        "arcosh_increment_strict_upper":str(sqrt_rho),
        "gap_below_three_halves":str(gap),
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({
        "status":"passed","gap_below_three_halves":str(gap),
        "output":str(args.output),"script_sha256":result["script_sha256"],
    },indent=2))


if __name__ == "__main__":
    main()
