#!/usr/bin/env python3
"""Exact height transport and a boundary-root obstruction for the original phase."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_minimizing_height_transport.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-minimizing-height-transport.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    specs = [
        ("mixed_full_height_reset", "certify"),
        ("mixed_coupled_outer_graph", "check"),
        ("mixed_global_cotangent_roots", "check"),
        ("mixed_real_packet_complex_stability", "check"),
        ("mixed_fourier_weight_continuation", "check"),
    ]
    deps = {}
    for stem, prefix in specs:
        pp = f"notes/research_{stem}.md"
        ss = f"experiments/{prefix}_{stem}.py"
        rr = f"repro/results/research-{stem.replace('_', '-')}.json"
        for p in (pp, ss, rr):
            deps[p] = sha(ROOT/p)
        rec = json.loads((ROOT/rr).read_text())
        assert rec["status"] == "passed", stem
        assert rec["script_sha256"] == deps[ss], stem
        inherited = rec.get("dependencies_sha256", rec.get("dependencies", {}))
        assert rec.get("proof_sha256", inherited.get(pp)) == deps[pp], stem
        for key in ("dependencies", "dependencies_sha256"):
            assert all(sha(ROOT/p) == h for p, h in rec.get(key, {}).items()), stem

    identities = []

    def zero(name, expression):
        values = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        assert all(sp.cancel(sp.expand(v)) == 0 for v in values), name
        identities.append(name)

    a, c, d, e, f, g = sp.symbols("a c d e f g", real=True)
    A = sp.Matrix([[a, c], [c, d]])
    B = sp.Matrix([[e, f], [f, g]])
    H = -A+sp.I*B
    D = A.inv()*B
    K = A+B*A.inv()*B
    T = sp.eye(2)+sp.I*D
    u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2", real=True)
    u, v = sp.Matrix([u1, u2]), sp.Matrix([v1, v2])
    polynomial = ((u+sp.I*v).T*H*(u+sp.I*v))[0]/2
    real_polynomial = (-u.T*A*u-2*u.T*B*v+v.T*A*v)[0]/2
    zero("literal real quadratic", sp.re(sp.expand(polynomial))-real_polynomial)
    xx = sp.hessian(real_polynomial, (u1, u2))
    hh = sp.hessian(real_polynomial, (v1, v2))
    hx = sp.Matrix([[sp.diff(real_polynomial, vj, uk) for uk in (u1, u2)] for vj in (v1, v2)])
    zero("real Hessian sign", xx+A)
    zero("height Hessian sign", hh-A)
    zero("height-real mixed sign", hx+B)
    zero("interior height response", -B+A*D)
    zero("reduced interior Hessian", -A-B*D+K)
    zero("free-face response", -B[0, :]+a*(B[0, :]/a))
    zero("complex transported Hessian", H*T+K)
    t00, t01, t10, t11 = sp.symbols("t00 t01 t10 t11")
    generic_T = sp.Matrix([[t00, t01], [t10, t11]])
    zero("Gaussian determinant with graph Jacobian", (generic_T.T*(-H)*generic_T).det()-generic_T.det()**2*(-H).det())

    x, y, z = sp.symbols("x y z", real=True)
    U = -(x-1)**2+y*y+3*y
    zero("polygon constrained branch", U.subs(y, -2*x)-(3*x*x-4*x-1))
    zero("polygon constrained second derivative", sp.diff(U.subs(y, -2*x), x, 2)-6)
    zero("polygon original critical gradient real", sp.diff(U, x).subs({x: 1, y: -sp.Rational(3, 2)}))
    zero("polygon original critical gradient height", sp.diff(U, y).subs({x: 1, y: -sp.Rational(3, 2)}))
    assert U.subs({x: 0, y: 0})-U.subs({x: 1, y: -sp.Rational(3, 2)}) == sp.Rational(5, 4)

    S, P = sp.symbols("S P")
    P0 = 2+sp.I/2
    cubic = S**3+(4+2*sp.I)*S*S+(sp.Rational(11, 4)+6*sp.I)*S+2-sp.Rational(23, 4)*sp.I
    zero("original homogeneous four cubic", ((S+sp.I)*(S+P0)**2-2*sp.I*(P0-sp.I)*(P0+sp.I))-cubic)
    W = (P+sp.I)/(P-sp.I)
    zero("inverse cotangent logarithm", sp.I*(W+1)/(W-1)-P)
    t, cc = sp.symbols("t cc", real=True)
    zero("cotangent fiber width polynomial", 2*t*(t-1/t-(t+1/t)/2+cc)-(t*t+2*cc*t-3))

    center = sp.Rational(46277, 100000)+sp.I*sp.Rational(41841, 100000)
    radius = sp.Rational(1, 10000)
    p0 = sp.expand(cubic.subs(S, center))
    p1 = sp.expand(sp.diff(cubic, S).subs(S, center))
    p2 = 3*center+4+2*sp.I
    margin = radius*max(abs(sp.re(p1)), abs(sp.im(p1)))
    margin -= abs(sp.re(p0))+abs(sp.im(p0))
    margin -= radius**2*(abs(sp.re(p2))+abs(sp.im(p2)))+radius**3
    assert margin > 0
    assert sp.re(center) > radius and abs(sp.im(center))+radius < 1

    def ar(value):
        q = Fraction(str(value))
        return arb(q.numerator)/q.denominator

    pi, ii = arb.pi(), acb(0, 1)
    R = ar("1/10000")
    Sbox = acb(ar("46277/100000")+arb(0, R), ar("41841/100000")+arb(0, R))
    Pbound = acb(2, ar("1/2"))
    zout = ((Pbound+ii)/(Pbound-ii)).log()/(2*pi*ii)
    sinner = ((Sbox+ii)/(Sbox-ii)).log()/(2*pi*ii)
    gp = lambda arg: (1-(-2*pi*ii*arg).exp()).log()
    phase_derivative = 2*gp(sinner+zout)+2*pi*ii*sinner-3*gp(zout)
    lift = 2*gp(sinner+zout)-3*gp(sinner)+2*pi*ii*zout
    inequalities = []

    def compare(name, value):
        assert value, name
        inequalities.append(name)

    compare("outer real location lower", zout.real > ar(".14"))
    compare("outer real location upper", zout.real < ar(".15"))
    compare("outer height lower", zout.imag > ar("-.031"))
    compare("outer height upper", zout.imag < ar("-.030"))
    compare("inner real location lower", sinner.real > ar(".34"))
    compare("inner real location upper", sinner.real < ar(".35"))
    compare("inner height lower", sinner.imag > ar("-.112"))
    compare("inner height upper", sinner.imag < ar("-.110"))
    compare("shifted argument regular lower", (sinner+zout).real > 0)
    compare("shifted argument regular upper", (sinner+zout).real < 1)
    compare("original logarithmic lift strip", abs(lift.imag) < pi)
    compare("positive lower-fiber derivative", -phase_derivative.imag > ar("1/2"))
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "precision_bits": args.precision,
        "exact_identity_count": len(identities), "exact_identities": identities,
        "rouche_center": str(center), "rouche_radius": str(radius),
        "exact_rouche_margin": str(margin),
        "strict_outward_comparisons": len(inequalities), "comparisons": inequalities,
        "boundary_outer_angle": str(zout), "selected_inner_angle_enclosure": str(sinner),
        "height_derivative_lower_bound": str((-phase_derivative.imag).lower()),
        "source_records": len(specs), "proof_sha256": ph, "script_sha256": sh,
        "dependencies_sha256": deps,
        "scope": "Common-box constrained minimizing graph and exact transport; variable-fiber and original cotangent-domain obstructions. No new transition finite-source or whole-period asymptotic.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(identities), "exact identities, 1 rational Rouche disk,", len(inequalities), "outward comparisons")


if __name__ == "__main__":
    main()
