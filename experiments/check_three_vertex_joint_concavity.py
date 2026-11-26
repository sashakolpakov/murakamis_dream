#!/usr/bin/env python3
"""Exact derivative identities and rational bounds for joint concavity."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import factorial
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    identities, comparisons = [], []

    def zero(name, expression):
        if isinstance(expression, sp.MatrixBase):
            difference = expression.applyfunc(sp.simplify)
            assert difference == sp.zeros(*difference.shape), (name, difference)
        else:
            difference = sp.simplify(expression)
            assert difference == 0, (name, difference)
        identities.append(name)

    def positive(name, expression):
        difference = sp.factor(expression)
        assert difference.is_Rational and difference > 0, (name, difference)
        comparisons.append({"name": name, "positive_margin": str(difference)})

    q, pi, ii = sp.Rational, sp.pi, sp.I
    X, Y, U, V, s = sp.symbols("X Y U V s")
    fs = sp.log(X)+sp.log(1-U*V)-sp.log(1-X*U)
    fx = 2*pi*ii*s+sp.log(1-X*U)-sp.log(1-X)
    zero("Fss differentiated from original log equation",
         -2*pi*ii*U*sp.diff(fs, U)
         -2*pi*ii*(U*V/(1-U*V)-X*U/(1-X*U)))
    zero("Fst differentiated from original log equation",
         -2*pi*ii*V*sp.diff(fs, V)-2*pi*ii*U*V/(1-U*V))
    zero("Fsx differentiated from original log equation",
         2*pi*ii*X*sp.diff(fs, X)-2*pi*ii/(1-X*U))
    zero("Fxx differentiated from original wire equation",
         2*pi*ii*X*sp.diff(fx, X)
         -2*pi*ii*(X/(1-X)-X*U/(1-X*U)))

    a, dx, dy, cx, cy = sp.symbols("a dx dy cx cy", real=True)
    ds, dt, vx, vy = sp.symbols("ds dt vx vy", real=True)
    form = a*(ds+dt)**2+dx*(ds-vx)**2+dy*(dt-vy)**2+cx*vx**2+cy*vy**2
    claimed = sp.Matrix([[a+dx, a, -dx, 0],
                         [a, a+dy, 0, -dy],
                         [-dx, 0, dx+cx, 0],
                         [0, -dy, 0, dy+cy]])
    zero("full joint positive quadratic form", sp.hessian(form, (ds, dt, vx, vy))/2-claimed)
    rank_one = sp.Matrix([[2, -3], [-3, 5]])
    zero("one-third pair bound matrix",
         3*sp.Matrix([[1, -1], [-1, 2]])-sp.eye(2)-rank_one)
    positive("one-third pair bound first minor", rank_one[0, 0])
    positive("one-third pair bound determinant", rank_one.det())

    positive("height exponent 7pi/25 below 9/10", q(9, 10)-7*q(22, 7)/25)
    ex = sum(q(9, 10)**k/factorial(k) for k in range(7))
    ex += (q(9, 10)**7/factorial(7))/(1-q(9, 80))
    positive("exp(9/10)<5/2", q(5, 2)-ex)
    positive("sin(pi/10)>3/10 via sqrt(5)>11/5", 5-q(11, 5)**2)
    zero("positive coefficient budget", 2*q(2, 5)*q(3, 10)/4-q(3, 50))
    zero("retained coercivity budget", q(3, 50)/3-q(1, 50))
    positive("wire-minus-index height stays positive", q(9, 100)-q(1, 50))
    zero("minimum real index-wire difference", q(1, 4)-q(1, 5)-q(1, 20))
    zero("maximum real index-wire difference", q(9, 20)-q(7, 50)-q(31, 100))

    positive("cap regular wall margin from pi>3", q(3, 10)-q(9, 10)/q(25, 8))
    positive("sine numerator above 2/3", q(21, 25)-q(21, 25)**3/6-q(2, 3))
    r = q(132, 175)
    positive("cosh(6pi/25)<4/3", q(4, 3)-(1+(r*r/2)/(1-r*r/12)))
    positive("positive mixed-cotangent real argument exceeds 1/3",
             q(7, 50)+q(1, 5)-q(1, 3))
    zero("mixed-cotangent height threshold",
         q(97, 100)+2*3*q(9, 100)-q(151, 100))
    positive("cosh(151/100)>2", 1+q(151, 100)**2/2-2)
    zero("mixed-cotangent upper budget", 1/(2+q(1, 2))-q(2, 5))
    positive("sin(pi/5)>11/20", q(3, 5)-q(3, 5)**3/6-q(11, 20))
    zero("sinh(1/2) geometric bound", q(1, 2)/(1-q(1, 4)/6)-q(12, 23))
    positive("sinh bound below 11/20", q(11, 20)-q(12, 23))
    zero("cosh(1/2) geometric bound", 1+q(1, 8)/(1-q(1, 4)/12)-q(53, 47))
    positive("cosh bound below 5/4", q(5, 4)-q(53, 47))
    zero("cap Hessian reserve", q(1, 2)-q(2, 5)-q(1, 10))
    zero("angular-coordinate coercivity", (pi/5)/(2*pi)**2-1/(20*pi))

    cosine_lower = 1-q(9, 5)**2/2+q(9, 5)**4/24-q(9, 5)**6/720
    positive("cos(9/5)>-1/4", cosine_lower+q(1, 4))
    positive("cosh(1)<2", 2-(1+q(1, 2)/(1-q(1, 12))))

    # Stronger grounded coefficient bounds, reduced to angular endpoints.
    r = q(22, 25)
    positive("cosh(7pi/25)<29/20", q(29, 20)-(1+(r*r/2)/(1-r*r/12)))
    positive("cos(pi/10)>19/20", 1-q(11, 35)**2/2-q(19, 20))
    positive("sqrt(2)>7/5", 2-q(7, 5)**2)
    positive("cos(pi/8)>9/10 from sqrt(2)>7/5",
             (2+q(7, 5))/4-q(9, 10)**2)
    positive("sin(pi/8)<2/5 from sqrt(2)>7/5",
             q(2, 5)**2-(2-q(7, 5))/4)
    positive("sin(7pi/25)>3/4", q(7, 8)-q(7, 8)**3/6-q(3, 4))
    positive("cos(7pi/25)>3/5", 1-q(22, 25)**2/2-q(3, 5))
    positive("d coefficient above 3/2", 18*q(25, 8)/37-q(3, 2))
    positive("left c coefficient above 5/2", 45*3/q(44)-q(5, 2))
    positive("right c coefficient above 5/2", 57*3/q(62)-q(5, 2))
    shifted = sp.Matrix([[q(3, 4), -q(3, 2)], [-q(3, 2), q(13, 4)]])
    zero("three-quarter bound determinant", shifted.det()-q(3, 16))
    positive("three-quarter bound first minor", shifted[0, 0])
    positive("three-quarter bound determinant", shifted.det())

    root = Path(__file__).resolve().parents[1]
    dependencies = [Path(__file__).resolve(),
                    root/"notes/research_three_vertex_joint_concavity.md",
                    root/"notes/research_three_vertex_central_index_chart.md",
                    root/"notes/research_mixed_wire_phase_concavity.md",
                    root/"notes/research_three_cap_first_attachment.md",
                    root/"notes/research_three_vertex_directed_packet.md"]
    result = {
        "status": "passed",
        "scope": "Exact derivatives, positive quadratic-form identity and rational compact-box constants. No contour-side, alias or complementary-source claim is inferred from these checks.",
        "exact_identity_count": len(identities), "exact_identities": identities,
        "rational_comparison_count": len(comparisons), "rational_comparisons": comparisons,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = args.output or root/"repro/results/research-three-vertex-joint-concavity.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed {len(identities)} exact identities and {len(comparisons)} rational comparisons.\n{output}")


if __name__ == "__main__":
    main()
