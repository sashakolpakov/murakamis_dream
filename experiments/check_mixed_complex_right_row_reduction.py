#!/usr/bin/env python3
"""Check the scalar margins and algebra in the complex-neighbor row reduction.

The written proof performs the continuous maximization. This script checks
its three remaining constants using outward arithmetic; it does not sample
the parameter domain or test a finite kernel's nonvanishing.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sy
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_complex_right_row_reduction.md"
SOURCES = (
    "notes/research_mixed_right_pair_raw_reduction.md",
    "notes/research_mixed_right_half_source_reduction.md",
    "notes/research_mixed_split_cutoff_hybrid_contour.md",
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-mixed-complex-right-row-reduction.json",
    )
    args = parser.parse_args()
    if args.precision < 160:
        parser.error("use at least 160 bits")
    ctx.prec = args.precision
    bindings = {name: sha(ROOT / name) for name in SOURCES}
    proof_hash, script_hash = sha(PROOF), sha(__file__)

    y, v = sy.symbols("y v", real=True)
    identity = (
        sy.cos(2 * sy.pi * (y + sy.Rational(1, 4)))
        - sy.cos(2 * sy.pi * (y - v))
        + 2 * sy.sin(sy.pi * (2 * y + sy.Rational(1, 4) - v))
        * sy.sin(sy.pi * (sy.Rational(1, 4) + v))
    )
    assert sy.trigsimp(sy.expand_trig(identity)) == 0

    # This is the exact subtraction in (8), with the common -G_H(y)
    # omitted from both sides, and J(3/4) = c_* = -J(1/4).
    Gyv, Gyq, Jv, lam, eps, c = sy.symbols("Gyv Gyq Jv lam eps c")
    upper = Gyv + (1 + eps) * Jv + lam * (1 - v)
    quarter = Gyq + (3 + eps) * c + lam / 4
    reduced = Gyv - Gyq + (1 + eps) * Jv + lam * (sy.Rational(3, 4) - v) - (3 + eps) * c
    assert sy.expand(upper - quarter - reduced) == 0

    H = sy.symbols("H", nonnegative=True)
    height_cases = []
    for sign in (-1, 1):
        for first_argument in (0, 1):
            coefficient = max(sign, 0) - first_argument * sign
            assert coefficient in (0, 1)
            height_cases.append({
                "height_sign": sign,
                "complex_target_first": first_argument,
                "lambda_over_2piH": coefficient,
            })
            assert sy.expand(max(sign, 0) * H - first_argument * sign * H - coefficient * H) == 0

    pi = arb.pi()
    imaginary = acb(0, 1)

    def G(t, height=0):
        exponent = -2 * pi * (ar(height) + imaginary * ar(t))
        return ((exponent.exp().polylog(2) - pi * pi / 6) / (2 * pi * imaginary)).real

    c_value = -G(Fraction(1, 4))
    max_height = ar(Fraction(57, 1000))
    gap = ar(Fraction(3, 50))
    bounds = (
        ("y=0, v<=1/4", -G(Fraction(1, 4), Fraction(57, 1000)) + 3 * pi * max_height / 2 - 3 * c_value),
        ("y=1/2, v<=1/4", 3 * pi * max_height / 2 - 3 * c_value),
        ("v>=1/4", -2 * G(Fraction(3, 8)) + pi * max_height - 3 * c_value),
    )
    rows = []
    for name, value in bounds:
        assert value < -gap, (name, value)
        rows.append({
            "case": name,
            "outward_upper_expression": str(value),
            "positive_margin_below_minus_3_over_50": str(-gap - value),
        })
    assert c_value > 0
    assert 4 * c_value > gap  # RR upper rows versus the fixed lower row.

    assert proof_hash == sha(PROOF)
    assert script_hash == sha(__file__)
    assert bindings == {name: sha(ROOT / name) for name in SOURCES}
    result = {
        "status": "passed",
        "precision_bits": args.precision,
        "exact_identities": 2,
        "height_cases": height_cases,
        "scalar_bounds": rows,
        "quarter_constant": str(c_value),
        "rr_lower_row_reserve": str(4 * c_value),
        "proof_sha256": proof_hash,
        "script_sha256": script_hash,
        "dependencies": bindings,
        "scope": (
            "Three outward scalar bounds and exact algebra supporting the written continuous "
            "maximization proof. Strong row concavity and its quadratic tangent consequence "
            "are proved analytically in the note, not by these scalar checks. "
            "Every original upper row is bounded by the fixed lower-row "
            "envelope, with gap 3/50. No kernel lower bound, interface sign, full-period "
            "asymptotic, or knot-family conclusion is checked."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("Passed: 3 outward scalar margins, 2 exact identities, 4 signed-height cases.")


if __name__ == "__main__":
    main()
