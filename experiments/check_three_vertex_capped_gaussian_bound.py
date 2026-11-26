#!/usr/bin/env python3
"""Focused exact/outward checks for the global L40 capped Gaussian proof.

The continuous covering and monotonicity arguments are in the note.
No sampled wire or index maximum is used by this checker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from flint import arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    q = sp.Rational
    identities, rational, outward = [], [], []

    def zero(name, expression):
        value = sp.simplify(expression)
        assert value == 0, (name, value)
        identities.append({"name": name, "difference": "0"})

    def positive(name, expression):
        value = sp.factor(expression)
        assert value.is_Rational and value > 0, (name, value)
        rational.append({"name": name, "positive_margin": str(value)})

    def ar(value):
        value = q(value)
        return arb(int(value.p)) / int(value.q)

    def margin(name, value):
        assert value > 0, (name, value)
        outward.append({"name": name, "positive_margin": str(value)})

    theta = sp.Symbol("theta", real=True)
    coefficient = sp.pi*sp.sin(theta)/(q(5, 4)-sp.cos(theta))
    zero("wire coefficient derivative",
         sp.diff(coefficient, theta)
         -sp.pi*(q(5, 4)*sp.cos(theta)-1)/(q(5, 4)-sp.cos(theta))**2)
    s = sp.Symbol("s", real=True)
    d = (sp.pi/2)*sp.sin(sp.pi*s)/(q(5, 4)-sp.cos(sp.pi*s))
    zero("index coefficient is half the wire coefficient",
         2*d-coefficient.subs(theta, sp.pi*s))
    delta = sp.Symbol("delta", real=True)
    squared_difference = ((q(5, 4)-sp.cos(2*sp.pi*(delta+s/2)))
                          -(q(5, 4)-sp.cos(2*sp.pi*(delta-s/2))))
    zero("centered interval derivative sign",
         sp.trigsimp(squared_difference-2*sp.sin(2*sp.pi*delta)*sp.sin(sp.pi*s)))
    zero("homogeneous index stationarity squared",
         sp.sin(2*sp.pi/3)**2-(q(5, 4)-sp.cos(sp.pi/3)))
    zre, zim = sp.symbols("zre zim", real=True)
    zero("imaginary quotient identity",
         sp.im((zre+sp.I*zim)/(1-zre-sp.I*zim))
         -zim/((1-zre)**2+zim**2))

    positive("central index lower boundary distance", q(1, 3)-q(3, 10))
    zero("central index first exit distance", q(1, 3)-q(3, 10)-q(1, 30))
    positive("upper index boundary is farther", q(19, 50)-q(1, 3)-q(1, 30))
    zero("nearest wire boundary distance", q(1, 6)-q(3, 20)-q(1, 60))
    positive("upper wire boundary is farther", q(19, 100)-q(1, 6)-q(1, 60))
    zero("index box centers fill wire box lower endpoint", q(3, 10)/2-q(3, 20))
    zero("index box centers fill wire box upper endpoint", q(19, 50)/2-q(19, 100))
    positive("sum indices above one half", 2*q(3, 10)-q(1, 2))
    positive("sum indices below one", 1-2*q(19, 50))
    zero("least index minus wire phase", q(3, 10)-q(19, 100)-q(11, 100))
    zero("largest index minus wire phase", q(19, 50)-q(3, 20)-q(23, 100))
    positive("difference lies below one half", q(1, 2)-q(23, 100))

    c_lower = q(25, 8)*q(23, 25)/(q(5, 4)-q(9, 25))
    zero("coefficient elementary lower bound", c_lower-q(575, 178))
    positive("wire coefficient above16/5", c_lower-q(16, 5))
    zero("index exterior gap", q(4, 5)*q(1, 30)**2-q(1, 1125))
    zero("wire exterior gap", q(8, 5)*q(1, 60)**2-q(1, 2250))
    zero("maximum capped loss", 2*q(8, 5)*q(1, 100)**2-q(1, 3125))
    positive("index gap exceeds capped loss", q(1, 1125)-q(1, 3125))
    positive("wire gap exceeds capped loss", q(1, 2250)-q(1, 3125))
    positive("one-third J endpoint below -7/100", q(323, 3000)-q(7, 100))
    zero("low-sum envelope upper bound", q(347, 500)-q(7, 100)-q(78, 125))
    positive("low-sum gap exceeds index gap",
             2*q(323, 1000)-q(78, 125)-q(1, 1125))
    positive("monotonic smaller-index squared gap using sqrt2>7/5",
             q(3, 4)-(q(5, 4)-q(7, 10)))
    positive("sqrt2 exceeds7/5", 2-q(7, 5)**2)

    pi = arb.pi()
    margin("pi>25/8", pi-ar(q(25, 8)))
    margin("sin(19pi/50)>23/25", (19*pi/50).sin()-ar(q(23, 25)))
    margin("cos(19pi/50)>9/25", (19*pi/50).cos()-ar(q(9, 25)))
    margin("cos(3pi/10)<4/5", ar(q(4, 5))-(3*pi/10).cos())
    margin("log2<347/500", ar(q(347, 500))-arb(2).log())
    margin("J(1/40) tangent upper bound below -7/100",
           -ar(q(7, 100))-((pi/20).log()-1)/40)
    # Positive blocks of the original Clausen/Lobachevsky calibration.
    d3 = sum(q(1, (3*j+1)**2)-q(1, (3*j+2)**2) for j in range(40))
    margin("forty positive D3 blocks give c>323/1000",
           3*arb(3).sqrt()*ar(d3)/(4*pi)-ar(q(323, 1000)))

    root = Path(__file__).resolve().parents[1]
    paths = [Path(__file__).resolve(),
             root / "notes/research_three_vertex_capped_gaussian_bound.md",
             root / "notes/research_three_vertex_global_wire_bound.md",
             root / "notes/research_three_vertex_joint_concavity.md",
             root / "notes/research_traced_three_vertex_endpoint.md",
             root / "notes/research_positive_three_crossing_cycle.md"]
    record = {
        "status": "passed",
        "scope": "Analytic global L40 real-index capped Gaussian bound, both wire radii1/2; no varied-height or arbitrary-cap assertion.",
        "constants": {"gaussian_coefficient": "8/5", "cap_radius": "1/100",
                      "index_exterior_gap": "1/1125", "wire_exterior_gap": "1/2250",
                      "maximum_required_capped_loss": "1/3125"},
        "precision_bits": ctx.prec,
        "exact_identity_count": len(identities), "exact_identities": identities,
        "rational_comparison_count": len(rational), "rational_comparisons": rational,
        "outward_scalar_comparison_count": len(outward), "outward_scalar_comparisons": outward,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in paths},
    }
    output = args.output or root / "repro/results/research-three-vertex-capped-gaussian-bound.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(identities)} exact identities, {len(rational)} rational comparisons, "
          f"and {len(outward)} outward scalar comparisons.\n{output}")


if __name__ == "__main__":
    main()
