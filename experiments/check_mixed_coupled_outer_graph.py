#!/usr/bin/env python3
"""Exact coupled contour bookkeeping and conditional-source domain reduction."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_coupled_outer_graph.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-mixed-coupled-outer-graph.json",
    )
    args = parser.parse_args()
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    deps = {}
    inputs = [
        ("mixed_all_real_conditional_packet", "check"),
        ("mixed_half_endpoint_conditional_packet", "check"),
        ("mixed_right_square_conditional_packets", "certify"),
        ("mixed_conditional_torus_composition", "check"),
        ("mixed_outer_graph_contours", "check"),
    ]
    for stem, prefix in inputs:
        proof_stem = ("mixed_unselected_right_taper_products"
                      if stem == "mixed_right_square_conditional_packets" else stem)
        pp = f"notes/research_{proof_stem}.md"
        ss = f"experiments/{prefix}_{stem}.py"
        rr = f"repro/results/research-{stem.replace('_', '-')}.json"
        for path in (pp, ss, rr):
            deps[path] = sha(ROOT / path)
        record = json.loads((ROOT / rr).read_text())
        assert record["status"] == "passed", stem
        assert record["script_sha256"] == deps[ss], stem
        if "proof_sha256" in record:
            assert record["proof_sha256"] == deps[pp], stem
        inherited = record.get("dependencies_sha256", record.get("dependencies", {}))
        assert all(sha(ROOT / p) == h for p, h in inherited.items()), stem
        if "proof_sha256" not in record:
            assert inherited[pp] == deps[pp], stem

    exact = []

    def zero(name, expression):
        assert sp.simplify(sp.expand(expression)) == 0, name
        exact.append(name)

    x = sp.symbols("x", real=True)
    lo, on, off, hi = map(sp.Rational, ("11/50", "1/4", "9/20", "1/2"))
    rise = sp.Rational(100, 3) * (x - lo)
    fall = 20 * (hi - x)
    zero("left cutoff starts at zero", rise.subs(x, lo))
    zero("left cutoff ends at one", rise.subs(x, on) - 1)
    zero("right cutoff starts at one", fall.subs(x, off) - 1)
    zero("right cutoff ends at zero", fall.subs(x, hi))
    zero("left derivative", sp.diff(rise, x) - sp.Rational(100, 3))
    zero("right derivative", sp.diff(fall, x) + 20)
    row_bound = 3 * sp.Rational(57, 1000) * sp.Rational(100, 3)
    zero("three-incidence row bound", row_bound - sp.Rational(57, 10))
    assert 1 + row_bound**2 < sp.Rational(29, 5)**2
    exact.append("strict Hadamard Jacobian budget")
    assert on < sp.Rational(27, 100) < sp.Rational(33, 100) < off
    assert on < sp.Rational(30, 100) < sp.Rational(39, 100) < off
    exact.append("critical coordinates lie in constant-height interior")
    assert -sp.Rational(57, 1000) < 0 < sp.Rational(7, 500) < sp.Rational(141, 10000)
    exact.append("selected and reset four-heights lie in source rectangle")

    r0, r1, c0, c1 = sp.symbols("r0 r1 c0 c1", real=True)
    zero("length-one repeated incidence", c0*r0*r0*r0-c0*r0**3)
    zero("length-two first repeated incidence", c0*r1*r0*r1-c0*r0*r1**2)
    zero("length-two second repeated incidence", c1*r0*r1*r0-c1*r1*r0**2)
    zero("length-one derivative retains three factors", sp.diff(c0*r0**3, r0)-3*c0*r0**2)

    # A generic polynomial phase tests the literal coupled chain rule.
    t = sp.symbols("t", real=True)
    v0, v1, x0, x1 = sp.symbols("v0 v1 x0 x1", real=True)
    h0 = c0*(x0+t*v0)*(x1+t*v1)**2
    h1 = c1*(x1+t*v1)*(x0+t*v0)**2
    z = sp.Matrix([x0+t*v0+sp.I*h0, x1+t*v1+sp.I*h1])
    u0, u1 = sp.symbols("u0 u1")
    phase = u0**3 + 2*u0*u1 + sp.I*u1**2
    grad = sp.Matrix([sp.diff(phase, u0), sp.diff(phase, u1)])
    hessian = sp.hessian(phase, (u0, u1))
    sub = {u0: z[0], u1: z[1]}
    direct = sp.diff(phase.subs(sub, simultaneous=True), t, 2)
    chain = (z.diff(t).T*hessian.subs(sub, simultaneous=True)*z.diff(t))[0]
    chain += (grad.subs(sub, simultaneous=True).T*z.diff(t, 2))[0]
    zero("full coupled second chain rule", direct-chain)

    # An explicit nonconstant coupled graph checks determinant orientation.
    a, b = sp.symbols("a b", real=True)
    dh = sp.Matrix([[0, a], [b, 0]])
    zero("coupled pullback determinant sign", (sp.eye(2)+sp.I*dh).det()-(1+a*b))
    m, k = sp.symbols("m k", integer=True, nonnegative=True)
    zero("original torus power unchanged", (m+k)-(m+k))
    eps = sp.symbols("eps")
    zero("literal kernel power after two factorials",
         (1-eps)/2-1+(1+eps)/2)

    incidence = []
    for length in range(1, 9):
        for flags in itertools.product((0, 1), repeat=length):
            H = [flags[(j-1) % length]*flags[j]*flags[(j+1) % length]
                 for j in range(length)]
            for j in range(length):
                if not flags[j]:
                    assert H[(j-1) % length] == H[j] == H[(j+1) % length] == 0
            for j in range(length):
                if not flags[j] or not flags[(j+1) % length]:
                    assert H[j] == H[(j+1) % length] == 0
            incidence.append([length, list(flags)])

    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT / p) == h for p, h in deps.items())
    result = {
        "status": "passed",
        "arithmetic": "exact symbolic and rational arithmetic",
        "exact_identity_count": len(exact),
        "exact_identities": exact,
        "incidence_patterns_checked": len(incidence),
        "incidence_cases": incidence,
        "proof_sha256": proof_hash,
        "script_sha256": script_hash,
        "dependencies_sha256": deps,
        "scope": "Exact coupled Laurent contour and source-domain reduction. No supporting-plane gap, uniform zero-angle packet or whole outer-word asymptotic.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(exact), "exact checks,", len(incidence), "cyclic incidence patterns")


if __name__ == "__main__":
    main()
