#!/usr/bin/env python3
"""Exact left-half circle algebra and an outward complex-horizontal obstruction."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_complex_horizontal_obstruction.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-complex-horizontal-obstruction.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    deps = {}
    for stem in ("mixed_global_cotangent_roots", "lower_half_factorial_continuation",
                 "mixed_all_real_conditional_packet"):
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

    exact = []

    def zero(name, value):
        assert sp.simplify(sp.expand(value)) == 0, name
        exact.append(name)

    P, Q, S = sp.symbols("P Q S")
    A, B, U = (P-sp.I)/(P+sp.I), (Q-sp.I)/(Q+sp.I), (S-sp.I)/(S+sp.I)
    for eps in (0, 1):
        zero(f"original exponential derivative type{3+eps}",
             (1-A*U)*(1-B*U)/(A*(1-U)**(2+eps))
             -(S+P)*(S+Q)*(S+sp.I)**eps/((2*sp.I)**eps*(P-sp.I)*(Q+sp.I)))
    p, alpha, v0, rad, th = sp.symbols("p alpha v0 rad th", real=True)
    circ = rad*sp.sin(th)+sp.I*(v0+rad*sp.cos(th))
    modsq = p*p+(v0+alpha)**2+rad*rad+2*rad*(p*sp.sin(th)+(v0+alpha)*sp.cos(th))
    zero("circle factor modulus", sp.expand_complex((circ+p+sp.I*alpha)*sp.conjugate(circ+p+sp.I*alpha))-modsq)
    zero("circle factor first derivative", sp.diff(modsq, th)-2*rad*(p*sp.cos(th)-(v0+alpha)*sp.sin(th)))
    zero("circle factor second derivative", sp.diff(modsq, th, 2)+2*rad*(p*sp.sin(th)+(v0+alpha)*sp.cos(th)))
    z = sp.symbols("z")
    zero("upper primitive full-period multiplier",
         sp.I*sp.pi*((z+1)-(z+1)**2)-sp.I*sp.pi*(z-z*z)+2*sp.pi*sp.I*z)
    ya, yb, y, ar = sp.symbols("ya yb y ar", real=True)
    increment = -2*sp.pi*sp.I*(sp.I*y+ar+sp.I*yb)+2*sp.pi*sp.I*(ar+sp.I*ya)
    zero("mixed upper-lower endpoint rate", sp.re(increment)-2*sp.pi*(y+yb-ya))

    def rat(value):
        f = Fraction(value)
        return arb(f.numerator)/f.denominator

    I, pi = acb(0, 1), arb.pi()
    pc = acb(rat("1/10"), rat("7/20"))
    qc = acb(rat("1/10"), -rat("9/20"))
    disc = (pc+qc)**2+4-4*I*(qc-pc)
    square = disc.sqrt()
    scot = (-(pc+qc)+square)/2
    angle = lambda zz: ((zz+I)/(zz-I)).log()/(2*pi*I)
    a, b, s = angle(pc), angle(qc), angle(scot)
    checks = []

    def positive(name, margin):
        assert margin > 0, (name, margin)
        checks.append({"name": name, "margin": str(margin)})

    positive("P right half-plane", pc.real)
    positive("Q right half-plane", qc.real)
    positive("P imaginary half-strip", rat("1/2")-abs(pc.imag))
    positive("Q imaginary half-strip", rat("1/2")-abs(qc.imag))
    positive("selected radical positive real part", square.real)
    positive("selected cotangent positive real part", scot.real)
    positive("selected cotangent positive imaginary part", scot.imag)
    positive("selected cotangent below upper boundary", 1-scot.imag)
    for name, val in (("a", a), ("b", b), ("s", s)):
        positive(name+" real lower", val.real)
        positive(name+" real upper", rat("1/2")-val.real)
    positive("negative selected height", -s.imag)
    positive("first shifted factor lower", -(s+a).imag)
    positive("second shifted factor upper", (s+b).imag)
    for name, val in (("s+a", s+a), ("s+b", s+b)):
        positive(name+" original regular strip lower", val.real)
        positive(name+" original regular strip upper", 1-val.real)
    # The radical identity is exact; this enclosure also detects a coding error.
    polynomial = scot**2+(pc+qc)*scot-1+I*(qc-pc)
    assert polynomial.contains(0)
    gp = lambda z: (1-(-2*pi*I*z).exp()).log()
    lift = gp(s+a)+gp(s+b)-2*gp(s)+2*pi*I*a
    positive("original zero lift strip", pi-abs(lift.imag))

    def lower_g(z):
        assert z.imag < 0
        u = (-2*pi*I*z).exp()
        assert abs(u) < 1
        return (u.polylog(2)-pi*pi/6)/(2*pi*I)

    def marked_g(z):
        if z.imag < 0:
            return lower_g(z)
        assert z.imag > 0
        return lower_g(z.conjugate()).conjugate()+pi*I*(z-z*z)

    def phase(z):
        return marked_g(z+a)+marked_g(z+b)-2*marked_g(z)+2*pi*I*a*z

    z0, z1 = acb(0, s.imag), acb(1, s.imag)
    main, left, right = phase(s).real, phase(z0).real, phase(z1).real
    gpp = lambda z: 2*pi*I/((2*pi*I*z).exp()-1)
    curvature = -(gpp(s+a)+gpp(s+b)-2*gpp(s)).real
    positive("selected horizontal coercivity", curvature)
    positive("critical rate lower", main-rat("22/25"))
    positive("critical rate upper", rat("9/10")-main)
    positive("right endpoint rate lower", right-rat("157/100"))
    positive("right endpoint rate upper", rat("159/100")-right)
    positive("right endpoint excess greater than two thirds", right-main-rat("2/3"))
    monodromy = 2*pi*(s.imag+b.imag-a.imag)
    assert (right-left-monodromy).contains(0)
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "precision_bits": args.precision,
        "exact_identity_count": len(exact), "exact_identities": exact,
        "strict_comparison_count": len(checks), "strict_comparisons": checks,
        "parameters": {"P": "1/10+7i/20", "Q": "1/10-9i/20", "epsilon": 0},
        "enclosures": {"a": str(a), "b": str(b), "s": str(s),
                       "critical_rate": str(main), "left_endpoint_rate": str(left),
                       "right_endpoint_rate": str(right), "endpoint_excess": str(right-main),
                       "period_increment": str(monodromy), "horizontal_curvature": str(curvature)},
        "proof_sha256": proof_hash, "script_sha256": script_hash,
        "dependencies_sha256": deps,
        "scope": "Left-half derivative lemma and failure of whole selected-horizontal dominance on the broad cotangent domain. No failure of a finite-sum asymptotic or smaller taper-domain theorem is inferred.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(exact), "exact identities,", len(checks), "strict outward comparisons")


if __name__ == "__main__":
    main()
