#!/usr/bin/env python3
"""Eight fixed endpoint diagnostics; no whole-height sign is inferred."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = (
    "notes/research_mixed_selected_four_left_row_corners.md",
    "notes/research_mixed_second_selected_plateau_reduction.md",
)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite.")
    script = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings = {p: sha(p) for p in (*DEPENDENCIES, script)}
    ctx.prec = 160
    pi, ii = arb.pi(), acb(0, 1)

    def rat(q):
        q = F(q)
        return arb(q.numerator) / q.denominator

    def endpoint(q, side):
        return F(str(getattr(q, side)().fmpq()))

    def g(w):
        if not (w.is_finite() and w.real > 0 and w.real < 1):
            raise ArithmeticError("Nonregular primitive input.")
        z = (-2*pi*ii*w).exp()
        if not (z.imag > 0 or z.imag < 0 or z.real < 1):
            raise ArithmeticError("Dilogarithm cut not separated.")
        value = (z.polylog(2) - pi*pi/6) / (2*pi*ii)
        if not value.is_finite():
            raise ArithmeticError("Nonfinite primitive.")
        return value

    left = acb(rat(F(1, 8)))
    rows = []
    for h in (F(-51, 500), F(-1, 1000)):
        s = acb(rat(F(3, 10)), rat(h))
        for x in (F(11, 50), F(9, 20)):
            for y in (F(11, 50), F(9, 20)):
                a = acb(rat(x), rat(F(1, 100)))
                b = acb(rat(y), rat(F(-51, 500)))
                delta = (
                    g(s+a)-g(left+a)+g(s+b)-g(left+b)
                    -3*g(s)+3*g(left)+2*pi*ii*a*(s-left)
                ).real
                rows.append({
                    "index_height": str(h),
                    "real_targets": [str(x), str(y)],
                    "lower_rational": str(endpoint(delta, "lower")),
                    "upper_rational": str(endpoint(delta, "upper")),
                })
    assert len(rows) == 8
    for path, digest in bindings.items():
        if sha(path) != digest:
            raise RuntimeError(f"Input changed: {path}")
    result = {
        "status": "diagnostic_only",
        "precision_bits": ctx.prec,
        "python_flint": flint.__version__,
        "incoming_height": "1/100",
        "outgoing_height": "-51/500",
        "trial_real_part": "3/10",
        "left_cut": "1/8",
        "checks": rows,
        "input_sha256": bindings,
        "source_root_evaluations": 0,
        "finite_sum_evaluations": 0,
        "adaptive_subdivisions": 0,
        "whole_interval_conclusion": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    for row in rows:
        print(row["index_height"], row["real_targets"],
              float(F(row["lower_rational"])),
              float(F(row["upper_rational"])))


if __name__ == "__main__":
    main()
