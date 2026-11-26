#!/usr/bin/env python3
"""Exact normalization, reflection, and endpoint identities for the factorial."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_lower_half_factorial_continuation.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-lower-half-factorial-continuation.json")
    args = parser.parse_args()
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    dependencies = {
        "notes/exact_factorial_interpolation_and_complex_contours.md":
            sha(ROOT / "notes/exact_factorial_interpolation_and_complex_contours.md")
    }
    identities = []

    def zero(name, value):
        assert sp.simplify(sp.expand(value)) == 0, name
        identities.append(name)

    N, x, y, a, b, eps, t = sp.symbols("N x y a b eps t", real=True)
    I, pi = sp.I, sp.pi
    E = lambda w: -I * pi * w * (w + 1) / (2 * N) + I * pi * w / 2
    w = N * (x + I * y)
    zero("marked prefactor real part", sp.re(E(w)) - (pi * N * y * (x - sp.Rational(1, 2)) + pi * y / 2))
    zero("exact two-height factorial ratio", sp.re(E(w) - E(sp.conjugate(w))) - (pi * N * y * (2 * x - 1) + pi * y))
    w0 = -sp.Rational(1, 2) + I * N * y
    zero("midpoint quadratic is real", w0 * (w0 + 1) + sp.Rational(1, 4) + N**2 * y**2)
    zero("midpoint marked modulus", 2 * sp.re(E(w0)) + pi * N * y)
    k = sp.symbols("k", real=True)
    zero("midpoint Gamma factors are conjugate", N * k - w0 - sp.conjugate(N * k + w0 + 1))
    zero("midpoint product denominator has unit modulus", sp.re(2 * w0 + 1))
    zero("Gamma reflection gives left endpoint modulus", N / (t + 1 / t) / t - N / (1 + t**2))
    zero("full-period multiplier gives right endpoint modulus", N / (1 + t) * (1 + t)**2 - N * (1 + t))
    theta = sp.symbols("theta", real=True)
    zero("numerator multiplier is bounded by one plus t", (1 + t)**2 - (1 + t**2 + 2 * t * sp.cos(theta)) - 2 * t * (1 - sp.cos(theta)))
    d = 2 + eps
    row_prefactor = lambda s: 2 * pi * I * N * a * s + E(N * (s + a)) + E(N * (s + b)) - d * E(N * s)
    reflection = sp.re(row_prefactor(x - I * y) - row_prefactor(x + I * y))
    zero("exact original row reflection including chirp", reflection - (2 * pi * N * y * (a - b + eps * (x - sp.Rational(1, 2))) + eps * pi * y))
    zero("midpoint reflection cancels the bounded epsilon correction", reflection.subs(x, -1 / (2 * N)) - 2 * pi * N * y * (a - b - eps / 2))
    zero("endpoint power of N", 1 - d / 2 + eps / 2)
    zero("stationary-phase source power of N", 1 - eps / 2 - sp.Rational(1, 2) - (1 - eps) / 2)
    z = sp.symbols("z")
    sin_exp = (sp.exp(I * pi * z) - sp.exp(-I * pi * z)) / (2 * I)
    zero("marked primitive derivative fixes the lower branch", 2 * I * sp.exp(-I * pi * z) * sin_exp - (1 - sp.exp(-2 * I * pi * z)))
    zero("lower-half nonzero symbol normalization", 2 * sp.exp(-I * pi * z) * sin_exp + I * (1 - sp.exp(-2 * I * pi * z)))

    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT / p) == h for p, h in dependencies.items())
    result = {
        "status": "passed",
        "arithmetic": "exact symbolic identities; no numerical precision parameter",
        "exact_identity_count": len(identities),
        "exact_identities": identities,
        "proof_sha256": proof_hash,
        "script_sha256": script_hash,
        "dependencies": dependencies,
        "scope": "Original factorial normalization, midpoint moduli, full-period multiplier bounds, and exact row reflection. Uniform Stirling remainders and endpoint estimates are established by the written proof; the complete source requires separate contour assembly.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(identities)} exact identities")


if __name__ == "__main__":
    main()
