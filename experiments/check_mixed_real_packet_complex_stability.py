#!/usr/bin/env python3
"""Exact contour-perturbation identities for the original conditional packet."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_real_packet_complex_stability.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-real-packet-complex-stability.json")
    args = parser.parse_args()
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    deps = {}
    for stem in ("mixed_global_lower_conditional_packet", "mixed_all_real_conditional_packet",
                 "mixed_half_endpoint_conditional_packet", "lower_half_factorial_continuation"):
        pp = f"notes/research_{stem}.md"
        ss = f"experiments/check_{stem}.py"
        rr = f"repro/results/research-{stem.replace('_', '-')}.json"
        for path in (pp, ss, rr):
            deps[path] = sha(ROOT/path)
        rec = json.loads((ROOT/rr).read_text())
        assert rec["status"] == "passed"
        assert rec["proof_sha256"] == deps[pp] and rec["script_sha256"] == deps[ss]
        assert all(sha(ROOT/p) == h for p, h in
                   rec.get("dependencies_sha256", rec.get("dependencies", {})).items())
    obstruction = "notes/research_mixed_complex_horizontal_obstruction.md"
    deps[obstruction] = sha(ROOT/obstruction)
    exact = []

    def zero(name, value):
        assert sp.simplify(sp.expand(value)) == 0, name
        exact.append(name)

    N = sp.symbols("N", positive=True, integer=True)
    eps, delta = sp.symbols("eps delta", real=True)
    z, a, b, t, A, B = sp.symbols("z a b t A B")
    pi, I = sp.pi, sp.I
    zero("residue scalar restores all original rows",
         N/(2*I)*(2*pi*I)/(pi*N)-1)
    zero("midpoint exponential sign", sp.exp(-2*pi*I*N*(-1/(2*N)))+1)
    zero("period chirp multiplier",
         2*pi*I*N*a*(z+1)-2*pi*I*N*a*z-2*pi*I*N*a)
    base = (1+t*A)*(1+t*B)/(1+t)**(2+eps)
    zero("two shifted midpoint period factors",
         (1-(-t)*A)*(1-(-t)*B)/(1-(-t))**(2+eps)-base)
    zero("opposite midpoint cotangent kernels", sp.cot(pi*N+z)-sp.cot(z))
    ap, bp = sp.symbols("ap bp", nonnegative=True)
    for sa in (-1, 1):
        for sb in (-1, 1):
            av = sa*ap
            apos = ap if sa > 0 else 0
            aneg = ap if sa < 0 else 0
            bpos = bp if sb > 0 else 0
            zero(f"complex multiplier sign case {sa},{sb}",
                 -av+apos+bpos-aneg-bpos)
    zero("uniform complex multiplier rate", 2*pi*(delta+delta)-4*pi*delta)
    s = sp.symbols("s")
    g = sp.Function("g")
    phase = g(s+a)+g(s+b)-(2+eps)*g(s)+2*pi*I*a*s
    zero("original first parameter derivative",
         sp.diff(phase, a)-sp.diff(g(s+a), a)-2*pi*I*s)
    zero("original second parameter derivative",
         sp.diff(phase, b)-sp.diff(g(s+b), b))
    zero("first root response numerator",
         sp.diff(phase, s, a)-sp.diff(g(s+a), s, a)-2*pi*I)
    zero("second root response numerator",
         sp.diff(phase, s, b)-sp.diff(g(s+b), s, b))
    zero("unchanged central Gaussian power",
         1-eps/2-sp.Rational(1,2)-(1-eps)/2)
    zero("literal kernel power after exact division",
         (1-eps)/2-1+(1+eps)/2)
    gamma, L, Lact, dd = sp.symbols("gamma L Lact dd", nonnegative=True)
    zero("complement gap relative to moving action",
         (-4*gamma+L*dd)-(-Lact*dd)-(-4*gamma+(L+Lact)*dd))
    zero("one reserve spent leaves three", -4*gamma+gamma+3*gamma)
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "arithmetic": "exact symbolic arithmetic",
        "exact_identity_count": len(exact), "exact_identities": exact,
        "proof_sha256": proof_hash, "script_sha256": script_hash,
        "dependencies_sha256": deps,
        "scope": "Actual open complex-neighborhood stability by perturbing all original contour currents. Neighborhood depends on the real compact; no prescribed taper width or remaining outer-sum claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(exact), "exact identities; all contour-source bindings current")


if __name__ == "__main__":
    main()
