#!/usr/bin/env python3
"""Exact algebra and source provenance for the global real support corollary."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_real_outer_support.md"
DEPS = [
    "notes/research_mixed_global_cotangent_roots.md",
    "experiments/check_mixed_global_cotangent_roots.py",
    "repro/results/research-mixed-global-cotangent-roots.json",
    "notes/research_mixed_all_real_conditional_packet.md",
    "experiments/check_mixed_all_real_conditional_packet.py",
    "repro/results/research-mixed-all-real-conditional-packet.json",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_left_support_obstructions.md",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-mixed-real-outer-support.json")
args = parser.parse_args()
initial = {p: sha(ROOT / p) for p in DEPS}
proof_hash, script_hash = sha(PROOF), sha(__file__)
for j in (0, 3):
    rec = json.loads((ROOT / DEPS[j + 2]).read_text())
    assert rec["status"] == "passed"
    assert rec["proof_sha256"] == initial[DEPS[j]]
    assert rec["script_sha256"] == initial[DEPS[j + 1]]
    inherited = dict(rec.get("dependencies", {}))
    for path, digest in rec.get("dependencies_sha256", {}).items():
        assert path not in inherited or inherited[path] == digest
        inherited[path] = digest
    for path, digest in inherited.items():
        assert sha(ROOT / path) == digest, path

identities = []


def identity(name, expression):
    assert s.simplify(expression) == 0, name
    identities.append(name)


u, v, p = s.symbols("u v p", real=True)
C = ((u * p - 1) * (u + p) + p * v**2) / ((u + p)**2 + v**2)
T = s.Matrix([[u - C, -C], [-C, p - C]])
det = ((u + p)**2 - p**2 * v**2) / ((u + p)**2 + v**2)
identity("triangle determinant", T.det() - det)
identity("positive determinant numerator",
         (u + p)**2 - p**2 * v**2 - (u * (u + 2 * p) + p**2 * (1 - v**2)))
identity("cotangent addition real part",
         s.re(((u + s.I * v) * p - 1) / (u + s.I * v + p)) - C)

c, d = s.symbols("c d", nonzero=True, real=True)
u0, u1, w0, w1 = s.symbols("u0 u1 w0 w1", real=True)
U, W = s.Matrix([u0, u1]), s.Matrix([w0, w1])
left = U * U.T / c - s.re((U + s.I * W) * (U + s.I * W).T / (c + s.I * d))
right = (d * U - c * W) * (d * U - c * W).T / (c * (c**2 + d**2))
for j in range(2):
    for k in range(j, 2):
        identity(f"complex Schur correction {j},{k}", left[j, k] - right[j, k])

eta, eps = s.symbols("eta eps")
identity("allocated source power",
         -(1 + eps) / 2 - (eta + eps) / 4 + (2 + eta + 3 * eps) / 4)
identity("allocated source phase at first leg", -1 - eta / 2 + (1 + eta / 2))
identity("allocated source phase at second leg", -1 - eps / 2 + (1 + eps / 2))

assert initial == {p: sha(ROOT / p) for p in DEPS}
assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
out = {
    "status": "passed",
    "scope": "Exact analytic real-reference support corollary only; no complex-reference or boundary-uniform conclusion.",
    "exact_identities": len(identities),
    "identities": identities,
    "validated_source_records": 2,
    "proof_sha256": proof_hash,
    "script_sha256": script_hash,
    "dependencies": initial,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2) + "\n")
print("PASS", len(identities), "exact identities + 2 source-record bindings")
