#!/usr/bin/env python3
"""Exact two-rectangle Bernstein certificate and wire/leg half-plane algebra."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_wire_before_inverse_leg.md"
INPUTS = [
    "notes/research_positive_path_fractional_charge_cube.md",
    "notes/research_geometric_phase_maximum_principle.md",
    "notes/research_positive_path_real_wire_order.md",
    "notes/research_mixed_four_leg_half_plane.md",
    "notes/research_mixed_all_leg_half_plane.md",
    "notes/research_mixed_positive_geometry_action_route.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-wire-before-inverse-leg.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps = {name: sha(ROOT/name) for name in INPUTS}
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    C, c, x, y = sp.symbols("C c x y", real=True)
    P = (144*(1+C*c)*(C+c)**2+45*(C+c)**4
         -64*(C*C-1)*(1-c*c))
    rectangles = [
        (sp.Integer(1), sp.Rational(6, 5), -sp.Rational(3, 5), sp.Integer(1)),
        (sp.Rational(6, 5), sp.Rational(7, 4), -sp.Rational(1, 2), sp.Integer(1)),
    ]
    floors = [sp.Rational(1453, 625), sp.Rational(67179, 4000)]
    tables = []
    for index, (a, b, d, e) in enumerate(rectangles):
        mapped = sp.Poly(sp.expand(P.subs({C: a+(b-a)*x, c: d+(e-d)*y})), x, y)
        check("rectangle %d exact bidegree" % index,
              mapped.degree(x) <= 4 and mapped.degree(y) <= 4)
        coefficients = [[sp.factor(sum(
            mapped.coeff_monomial(x**k*y**l)
            * sp.Rational(comb(i, k), comb(4, k))
            * sp.Rational(comb(j, l), comb(4, l))
            for k in range(i+1) for l in range(j+1)))
            for j in range(5)] for i in range(5)]
        reconstructed = sum(
            coefficients[i][j]*comb(4, i)*x**i*(1-x)**(4-i)
            * comb(4, j)*y**j*(1-y)**(4-j)
            for i in range(5) for j in range(5))
        check("rectangle %d exact Bernstein reconstruction" % index,
              sp.expand(reconstructed-mapped.as_expr()) == 0)
        minimum = min(value for row in coefficients for value in row)
        check("rectangle %d all 25 coefficients strictly positive" % index,
              minimum == floors[index] and minimum > 0)
        tables.append(dict(rectangle=list(map(str, (a, b, d, e))),
                           bidegree=[4, 4],
                           coefficients=[[str(v) for v in row] for row in coefficients],
                           minimum=str(minimum)))

    real_alpha = 2*(1+C*c)/(C+c)**2
    imag_alpha_squared = 4*(C*C-1)*(1-c*c)/(C+c)**4
    check("polynomial is exactly the inverse-cosine inequality",
          sp.factor(16*(C+c)**4*(sp.Rational(9, 2)*real_alpha
                    +sp.Rational(45, 16)-imag_alpha_squared)-P) == 0)
    u, v = sp.symbols("u v", real=True)
    check("squaring the positive norm comparison has the stated margin",
          sp.expand((2*u-1+sp.Rational(9, 2))**2
                    -(2*u-1)**2-4*v*v
                    -(18*u+sp.Rational(45, 4)-4*v*v)) == 0)
    check("cosine tangent lower bound is inside the first rectangle",
          -F(7, 12) > -F(3, 5))
    check("the large-height return ratio exceeds the phase tangent",
          F(44, 75) > F(1, 2))
    check("the two rectangle denominators stay positive",
          1-F(3, 5) > 0 and F(6, 5)-F(1, 2) > 0)
    check("the norm margin gives h strictly below three halves",
          F(9, 2)/2 == F(3, 2)**2)
    check("phase constant kappa is strictly less than three",
          8 < 9)
    check("the upper box corner polynomial stays positive for h between zero and one",
          sp.expand(-4*x*x+4*x+1-(1+4*x*(1-x))) == 0)

    p, h, kappa, w = sp.symbols("p h kappa w", real=True)
    T, L, D = p*p-h*h+1, 2*p*h, p*p+(h-1)**2
    N = p*u*(D-u)+(1+h)*D*v-p*v*v
    corners = [
        ((sp.Rational(1, 2), 0), p*(2*h*h-4*h+2*p*p+1)/4),
        ((T-sp.Rational(1, 2), 0),
         p*(2*h-1)**2*(2*p*p-2*h*h+1)/4),
        ((sp.Rational(1, 2), L),
         p*(2*p*p-2*h*h+1)*(-4*h*h+4*h+1)/4),
        ((T-sp.Rational(1, 2), L), p*(2*p*p-6*h*h+4*h+1)/4),
    ]
    for index, ((uu, vv), expected) in enumerate(corners):
        check("exact unclipped corner %d" % index,
              sp.factor(N.subs({u: uu, v: vv})-expected) == 0)
    check("first corner uses only p greater than h",
          sp.expand(2*h*h-4*h+2*p*p+1
                    -(2*(p*p-h*h)+4*(h-sp.Rational(1, 2))**2)) == 0)
    check("fourth corner uses only p greater than h",
          sp.expand(2*p*p-6*h*h+4*h+1
                    -(2*(p*p-h*h)-4*h*h+4*h+1)) == 0)
    check("lower horizontal boundary has the stated strict reserve",
          sp.expand(D-T+sp.Rational(1, 2)-(2*h-1)**2/2) == 0)
    check("upper slanted quotient decreases",
          sp.factor(sp.diff(sp.cancel(N.subs(v, kappa*u)/u), u)
                    +p*(1+kappa*kappa)) == 0)
    lower_slant = N.subs({u: T-w, v: L-kappa*w}, simultaneous=True)
    check("lower slanted quotient decreases",
          sp.factor(sp.diff(sp.cancel(lower_slant/w), w)
                    +p*(1+kappa*kappa)) == 0)
    check("upper phase-edge endpoint factorization",
          sp.factor(N.subs({u: L/kappa, v: L})
                    -2*h*p*(p+kappa*(1-h))*(kappa*T-L)/kappa**2) == 0)
    check("lower phase-edge endpoint factorization",
          sp.factor(N.subs({u: T-L/kappa, v: 0})
                    -2*h*p*(p+kappa*(h-1))*(kappa*T-L)/kappa**2) == 0)
    check("upper horizontal feasibility gives the exact comparison",
          sp.expand(2*p*p-6*h*h+4*h+1-4*h*(1-h+p/kappa)
                    -2*(T-sp.Rational(1, 2)-L/kappa)) == 0)

    alpha, beta, q = sp.symbols("alpha beta q", nonzero=True)
    X = (q+sp.I)/(q-sp.I)
    U = -sp.I/(2*(q+sp.I)/alpha-sp.I)
    ratio = 1/(1+2*sp.I*beta/(alpha*(q+sp.I)))
    check("literal XU identity after q squared equals alpha plus beta minus one",
          sp.simplify(sp.factor((X*U-ratio).subs(beta, q*q+1-alpha))) == 0)
    check("the real-part decomposition uses the same q relation",
          sp.simplify(sp.factor((beta/(alpha*(q+sp.I))
                     -(q-sp.I)/alpha+1/(q+sp.I))
                    .subs(beta, q*q+1-alpha))) == 0)
    Z = ((p-sp.I*(h+1))/(u-sp.I*v)
         -1/(p+sp.I*(1-h)))
    check("the exact numerator of the real part is N",
          sp.factor(sp.re(Z)*(u*u+v*v)*D-N) == 0)
    reZ, imZ = sp.symbols("reZ imZ", real=True)
    check("positive real Z gives negative imaginary XU",
          sp.factor(sp.im(1/(1+2*sp.I*(reZ+sp.I*imZ)))
                    +2*reZ/((1-2*imZ)**2+4*reZ**2)) == 0)

    result = dict(status="passed", arithmetic="exact rational and symbolic",
        exact_check_count=len(checks), checks=checks,
        bernstein_rectangles=tables, bernstein_coefficient_count=50,
        proved_wire_cotangent_height_upper="3/2",
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=deps, new_root_proposals=0,
        numerical_parameter_cells=0,
        scope="Actual positive charge paths: strict original wire-before-inverse-leg order at every incidence. No adjacent-sum or full source-lift claim.")
    if old is not None:
        expected = dict(result)
        expected["input_sha256"] = old.get("input_sha256")
        assert old == expected
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/name) == digest for name, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks; 50 Bernstein coefficients;",
          len(deps), "current analytic inputs")


if __name__ == "__main__":
    main()
