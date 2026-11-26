#!/usr/bin/env python3
"""One exact quadratic criterion and one outward target; no roots or cover."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_horizontal_root_obstruction.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-horizontal-root-obstruction.json")
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    dependencies = {name: sha(ROOT / name) for name in (
        "notes/research_mixed_closed_cotangent_roots.md",
        "notes/research_mixed_cyclic_critical_height_bounds.md",
    )}
    checks = []

    def check(label, condition):
        assert condition, label
        checks.append(label)

    A, B, C, D = sp.symbols("A B C D", real=True)
    R = -(D/A)**2-B*D/A-C
    L = A*A+B*B-4*C
    delta = (A+sp.I*B)**2+4*(C+sp.I*D)
    check("the imaginary-axis candidate has real residual R",
          sp.expand((sp.I*D/A)**2+(A+sp.I*B)*(sp.I*D/A)-C-sp.I*D-R) == 0)
    check("the comparison L is positive when R is nonnegative",
          sp.cancel(L-(A*A+(B+2*D/A)**2+4*R)) == 0)
    check("the discriminant difference has the exact residual sign",
          sp.cancel(sp.expand(delta*sp.conjugate(delta)-L*L+16*A*A*R)) == 0)
    check("the real-square comparison threshold is exactly A squared",
          sp.expand((L+sp.re(delta))/2-A*A) == 0)
    check("both rational targets are in the closed source rectangle",
          F(23,100) >= F(23,100) and F(23,100) <= F(45,100)
          and abs(-F(1,10)) < F(12,100) and abs(F(13,200)) < F(12,100))
    check("the released heights are strictly within their typed intervals",
          -F(51,500) < -F(1,10) < -F(1,1000)
          and -F(13,200) < F(13,200) < F(17,250))

    a = acb(arb(23)/100, -arb(1)/10)
    b = acb(arb(23)/100, arb(13)/200)
    P, Q = (arb.pi()*a).cot(), (arb.pi()*b).cot()
    p, alpha, q, beta = P.real, P.imag, Q.real, Q.imag
    v = (p-q)/(p+q)
    residual = -1-v*v-(alpha+beta)*v+alpha-beta
    check("both outer real cotangents are positive", p > 0 and q > 0)
    check("the only axis candidate is in the recorded interval",
          v > -arb(59)/1000 and v < -arb(58)/1000)
    check("the imaginary-axis residual exceeds three fiftieths",
          residual > arb(3)/50)

    metadata = dict(status="passed", proof_sha256=ph, script_sha256=sh,
                    dependencies_sha256=dependencies, checks=checks,
                    exact_checks=6, outward_checks=3,
                    rational_target={"a": ["23/100", "-1/10"],
                                     "b": ["23/100", "13/200"]},
                    residual_lower="3/50", new_root_proposals=0,
                    parameter_cover_cells=0, actual_word_realization_proved=False,
                    finite_kernel_counterexample_proved=False)
    if old:
        for key, value in metadata.items():
            assert old[key] == value, key
        assert args.precision >= old["precision_bits"]
    for name, digest in dependencies.items():
        assert sha(ROOT/name) == digest, name
    assert sha(PROOF) == ph and sha(__file__) == sh
    result = dict(metadata, precision_bits=args.precision,
                  bounds={"P": str(P), "Q": str(Q), "axis_imaginary": str(v),
                          "axis_real_residual": str(residual)})
    if ih:
        assert sha(args.input) == ih
        result["input_sha256"] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS 6 exact/domain checks, 3 outward checks, one rational target; no root or cover.")


if __name__ == "__main__":
    main()
