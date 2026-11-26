#!/usr/bin/env python3
"""Exact Hessian algebra and outward scalar bound for the exterior core."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_right_half_concavity.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-right-half-concavity.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    U, P, Q = sp.symbols("U P Q", real=True)
    epsilon, q = sp.symbols("epsilon q", real=True)
    denominator = (U + P)**2 + Q**2
    C = sp.re((U*(P + sp.I*Q) - 1)/(U + P + sp.I*Q))
    identities = []

    def check(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        identities.append(name)

    check("cotangent addition real part",
          C - ((U*P-1)*(U+P) + U*Q**2)/denominator)
    check("positive first Hessian minor",
          U-C - (U+P)*(U**2+1)/denominator)
    check("positive Hessian determinant",
          (U-C)*(P-C)-C**2 -
          ((U+P)**2-U**2*Q**2)/denominator)
    # This is positive for U>0, P>=0 and |Q|<1, including P=0.
    check("strict determinant numerator",
          (U+P)**2-U**2*Q**2 -
          (U**2*(1-Q**2) + 2*U*P + P**2))
    # The real half-period identity is cot(theta+pi/2)=-1/cot(theta).
    theta = sp.symbols("theta", real=True)
    assert sp.trigsimp(sp.cot(theta+sp.pi/2)+sp.tan(theta)) == 0
    identities.append("real half-period cotangent identity")
    A = 1/U + (1+epsilon)*U
    base = sp.Matrix([[U-C, -C], [-C, P-C]])
    total = base + sp.diag(A, q*P/2)
    check("negative Hessian diagonal addition",
          total.det() - (base.det() + A*(P-C) +
                         q*P*(U-C)/2 + A*q*P/2))
    # Expand the nonlinear phase decomposition with independent formal values.
    gus, gu, gz, gshift, ghalf = sp.symbols("gus gu gz gshift ghalf")
    original = gshift-ghalf + gus-gz - (2+epsilon)*gu - q*gz/2
    decomposed = gus-gu-gz + gshift-ghalf - (1+epsilon)*gu - q*gz/2
    check("complex-triangle decomposition", original-decomposed)

    pi = arb.pi()
    margin = (-57*pi/500).exp() - (13*pi/50).cos()
    assert margin > 0
    dependencies = [
        "notes/research_mixed_right_half_source_reduction.md",
        "notes/research_mixed_boundary_strip_bounds.md",
        "notes/research_mixed_fourier_weight_continuation.md",
    ]
    result = {
        "status": "passed",
        "precision_bits": args.precision,
        "exact_identity_count": len(identities),
        "exact_identities": identities,
        "strict_scalar_count": 1,
        "height_cone_margin": str(margin),
        "domain": {"u": ["0", "1/2"], "y": ["13/100", "1/2"],
                   "height_abs_upper": "57/1000"},
        "scope": (
            "Strict concavity of each row-angle branch and convexity in "
            "height on the stated core with the right angle fixed at 1/2. "
            "No exterior gap or mixed-word knot theorem is checked."
        ),
        "script_sha256": sha(__file__),
        "proof_sha256": sha(PROOF),
        "dependencies": {p: sha(ROOT / p) for p in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(len(identities), "exact identities and one strict scalar comparison passed")


if __name__ == "__main__":
    main()
