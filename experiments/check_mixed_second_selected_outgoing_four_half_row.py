#!/usr/bin/env python3
"""32 fixed whole-height tests for the outgoing own-four half row.

The analytic reduction costs 3/800 in the outgoing real coordinate.
The midpoint correction uses the proved height Lipschitz constant.
No roots, finite sums, adaptive subdivisions or prior replay are used.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = (
    "notes/research_mixed_second_selected_outgoing_four_half_row.md",
    "notes/research_mixed_second_selected_left_half_row_domination.md",
    "notes/research_mixed_selected_four_left_row_corners.md",
    "notes/research_mixed_second_selected_outgoing_four_left_cut.md",
    "notes/research_mixed_second_selected_plateau_reduction.md",
)
PARTS = 32
REAL_LOSS = F(3, 800)
GAP = F(1, 20)


def rat(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def endpoint(q, side):
    return F(str(getattr(q, side)().fmpq()))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite an existing result.")
    script = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings = {path: sha(path) for path in (*DEPENDENCIES, script)}
    ctx.prec = 160
    pi, ii = arb.pi(), acb(0, 1)

    def primitive(w):
        if not (w.is_finite() and w.real > 0 and w.real < 1):
            raise ArithmeticError("Primitive argument left its regular strip.")
        z = (-2*pi*ii*w).exp()
        if not (z.imag > 0 or z.imag < 0 or z.real < 1):
            raise ArithmeticError("Dilogarithm cut not separated.")
        value = (z.polylog(2)-pi*pi/6)/(2*pi*ii)
        if not value.is_finite():
            raise ArithmeticError("Nonfinite primitive enclosure.")
        return value

    bounds = F(-51, 500), F(-1, 1000)
    step = (bounds[1]-bounds[0])/PARTS
    half = acb(rat(F(1, 2)))
    a = acb(rat(F(11, 50)), rat(F(1, 100)))
    b = acb(rat(F(11, 50)), rat(F(-1, 1000)))
    records = []
    for j in range(PARTS):
        lo, hi = bounds[0]+j*step, bounds[0]+(j+1)*step
        mid = (lo+hi)/2
        s = acb(rat(F(3, 10)), rat(mid))
        value = (
            primitive(s+a)-primitive(half+a)
            +primitive(s+b)-primitive(half+b)
            -3*primitive(s)+3*primitive(half)
            +2*pi*ii*a*(s-half)
        ).real
        height_correction = rat(F(9, 10))*pi*rat((hi-lo)/2)
        whole = value-rat(REAL_LOSS)-height_correction
        lower, upper = endpoint(whole, "lower"), endpoint(whole, "upper")
        records.append({
            "index": j,
            "height_interval": [str(lo), str(hi)],
            "height_midpoint": str(mid),
            "midpoint_lower_rational": str(endpoint(value, "lower")),
            "midpoint_upper_rational": str(endpoint(value, "upper")),
            "height_correction_lower_rational": str(endpoint(height_correction, "lower")),
            "height_correction_upper_rational": str(endpoint(height_correction, "upper")),
            "real_target_correction": str(REAL_LOSS),
            "lower_rational": str(lower),
            "upper_rational": str(upper),
            "pass": lower > GAP,
        })
    passed = len(records) == PARTS and all(row["pass"] for row in records)
    for path, digest in bindings.items():
        if sha(path) != digest:
            raise RuntimeError(f"Input changed during calculation: {path}")
    result = {
        "status": "complete" if passed else "failed",
        "precision_bits": ctx.prec,
        "python_flint": flint.__version__,
        "height_interval": list(map(str, bounds)),
        "partition_count": PARTS,
        "real_targets": ["11/50", "11/50"],
        "incoming_height": "1/100",
        "outgoing_height": "-1/1000",
        "trial_real_part": "3/10",
        "half_row": "1/2",
        "gap": str(GAP),
        "real_target_correction": str(REAL_LOSS),
        "lipschitz_constant": "9*pi/10",
        "checks": records,
        "worst_lower_rational": str(min(F(row["lower_rational"])
                                         for row in records)),
        "input_sha256": bindings,
        "source_root_evaluations": 0,
        "finite_sum_evaluations": 0,
        "adaptive_subdivisions": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({
        "status": result["status"],
        "checks": len(records),
        "worst_lower": float(F(result["worst_lower_rational"])),
        "output": str(args.output),
    }))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
