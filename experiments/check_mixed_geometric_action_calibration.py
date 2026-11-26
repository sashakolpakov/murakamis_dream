#!/usr/bin/env python3
"""Check exact algebra used in the geometric mixed-path action calibration.

The written continuation and calibration arguments are essential inputs;
this script neither proves them nor checks a finite quantum asymptotic.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_geometric_action_calibration.md"
INPUTS = [
    "notes/research_mixed_geometric_source_log_lifts.md",
    "notes/research_mixed_wire_before_inverse_leg.md",
    "notes/research_mixed_all_leg_half_plane.md",
    "notes/research_positive_path_fractional_charge_cube.md",
    "notes/research_positive_path_real_wire_order.md",
    "notes/research_mixed_unit_period_leg_elimination.md",
    "notes/research_three_chain_action_volume_calibration.md",
    "notes/research_power_four_source_packet.md",
    "notes/research_exterior_crossing_phase.md",
    "notes/research_mixed_contracted_phase.md",
    "notes/research_mixed_endpoint_action_calibration.md",
    "notes/research_mixed_open_word_hessian.md",
    "notes/research_positive_edge_volume_identity.md",
    "notes/research_positive_point_marked_completion.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-geometric-action-calibration.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    dependencies = {name: sha(ROOT/name) for name in INPUTS}
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    U, V, X, W = sp.symbols("U V X W")
    inverse = (1-X)/(1+X*(1+W))
    check("inverse incidence gives the angular derivative exponential",
          sp.factor((X*inverse-1)/(inverse*(1-X))
                    +(X*X+W*X+1)/(X-1)**2) == 0)
    u0 = (-1-2*sp.I)/5
    check("complete inverse leg and logarithmic calibration product",
          sp.simplify(inverse.subs({X: sp.I, W: 2})-u0) == 0
          and sp.simplify(1-sp.I*u0+u0*(1-sp.I)) == 0)
    check("isolated fourth-power equation factors with the stated cubic",
          sp.expand((U-1)*(U**3-U**2-U-1)-(U**4-2*U**3+1)) == 0)
    p = U**3-U**2-U-1
    check("the isolated cubic has two negative critical values",
          sp.factor(sp.diff(p, U)) == (U-1)*(3*U+1)
          and p.subs(U, -sp.Rational(1, 3)) == -sp.Rational(22, 27)
          and p.subs(U, 1) == -2 and p.subs(U, 2) == 1)
    check("the cubic product and discriminant select a conjugate pair",
          -sp.Poly(p, U).TC() == 1 and sp.discriminant(p, U) == -44)
    x4 = 1/(1+2*U)
    check("isolated fourth-power point lies on the calibrated diagonal branch",
          sp.factor(2*x4/(1-x4)-1/U) == 0
          and sp.factor(1-1/x4+2*U) == 0
          and sp.factor(x4*(1-U**2)-(1-U)*(1-x4*U)) == 0)
    r = sp.symbols("r", real=True)
    check("the real cubic root gives the strict disk margin",
          sp.factor(2*(1-r)+4/r-2*(2-r)*(r+1)/r) == 0)

    xc = (1-U*V)/(U+V-2*U*V)
    check("shared-wire stationary identity",
          sp.factor((1-xc*U)*(1-xc*V)-U*V*(1-xc)**2) == 0)
    check("first shared-leg derivative identity",
          sp.factor(xc/(1-xc*U)-(1-U*V)/(V*(1-U)**2)) == 0)
    check("second shared-leg derivative identity",
          sp.factor(xc/(1-xc*V)-(1-U*V)/(U*(1-V)**2)) == 0)
    check("diagonal shared-wire formulas and complete endpoint",
          sp.factor(xc.subs(V, U)-(1+U)/(2*U)) == 0
          and sp.simplify(xc.subs({U: u0, V: u0})-sp.I) == 0)

    t = sp.symbols("t", real=True)
    a = -sp.Rational(1, 2)+3*t/10
    b = -sp.sqrt(3)/2+(sp.sqrt(3)/2-sp.Rational(2, 5))*t
    norm = sp.expand(a*a+b*b)
    disk = sp.Rational(3, 5)*(1-t)*(5-(5-2*sp.sqrt(3))*t)
    real = (1-t)*(5-(10-4*sp.sqrt(3))*t)/10
    check("exact diagonal-path disk polynomial",
          sp.expand(3*norm-2*a-1-disk) == 0)
    check("exact diagonal-path first-quadrant polynomial",
          sp.expand(norm+a-real) == 0)
    check("both path braces are strictly positive on the unit interval",
          5 > 0 and 2*sp.sqrt(3) > 0 and 4*sp.sqrt(3)-5 > 0)
    check("diagonal path joins the two specified original legs",
          sp.simplify((a+sp.I*b).subs(t, 0)+sp.Rational(1, 2)
                      +sp.sqrt(3)*sp.I/2) == 0
          and sp.simplify((a+sp.I*b).subs(t, 1)-u0) == 0)

    a, b = sp.symbols("a b")
    phi = lambda z: (z-z*z)/2  # phi/pi
    check("the local quadratic identity telescopes at every incidence",
          sp.expand(phi(a+b)-phi(a)-phi(b)+a*b) == 0)
    for m in range(1, 5):
        s = sp.symbols("s0:"+str(m))
        t = sp.symbols("t0:"+str(m))
        u, v = sp.symbols("u v")
        eps = sp.symbols("e0:"+str(m))
        contracted = (sum(phi(s[j]+t[j])-eps[j]*(phi(s[j])+phi(t[j]))
                          for j in range(m))
                      -sum(phi(t[j]+s[j+1]) for j in range(m-1))
                      -phi(s[0])-phi(t[-1])+s[0]*u+t[-1]*v)
        expected = (sum(t[j]*s[j+1] for j in range(m-1))
                    -sum(s[j]*t[j] for j in range(m))+s[0]*u+t[-1]*v
                    -sum(eps[j]*(phi(s[j])+phi(t[j])) for j in range(m)))
        check("literal endpoint quadratic normalization, length %d" % m,
              sp.expand(contracted-expected) == 0)

    result = dict(status="passed", arithmetic="exact symbolic",
        exact_check_count=len(checks), checks=checks,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=dependencies, new_root_proposals=0,
        numerical_parameter_cells=0,
        scope="Algebra for the written geometric-point action and absolute constants. Does not identify the localized source point or prove complete finite-source dominance.")
    if old is not None:
        expected = dict(result)
        expected["input_sha256"] = old.get("input_sha256")
        assert old == expected
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks;", len(dependencies), "written inputs")


if __name__ == "__main__":
    main()
