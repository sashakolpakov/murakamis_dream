#!/usr/bin/env python3
"""Outward tangent bounds after the analytic triangle-to-edge reduction.

Two strict concave-edge tangent inequalities, together with the written
monotonicity lemma, cover the entire real triangle outside [1/5,2/5]^2.
No grid sample or complex contour estimate is used.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-power-four-real-complement.json")
    args = parser.parse_args()
    ctx.prec = args.precision

    def rational(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    reference_path = ROOT/"repro/results/research-three-four-source-interface.json"
    reference = json.loads(reference_path.read_text())
    assert reference["status"] == "passed"
    assert reference["script_sha256"] == sha256(
        (ROOT/"experiments/check_three_four_source_interface.py").read_bytes()).hexdigest()
    for path, expected in reference["dependencies_sha256"].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == expected, path
    ar, ai = reference["root_certificate"]["center"]
    radius = rational(reference["root_certificate"]["complex_disk_radius"])
    root = acb(rational(ar)+arb(0,radius), rational(ai)+arb(0,radius))
    beta = root**2*(2*root-1)**2/(2*(root-1))
    pi, ii = arb.pi(), acb(0,1)
    x = (root**2*beta/(root**2+beta)).sqrt().asin()/pi
    K = (2*pi*ii*x).exp()
    a, b = rational("1/5"), rational("2/5")
    ratio = abs(K)/abs(1-K)
    comparisons = []

    def positive(name, value):
        assert value > 0, (name,str(value))
        comparisons.append({"name":name,"strict_positive_margin":str(value)})

    positive("inside unit disk",1-abs(K))
    positive("positive real parameter",K.real)
    positive("positive imaginary parameter",K.imag)
    positive("argument sector lower",2*x.real-a)
    positive("argument sector upper",b-2*x.real)
    positive("small-index derivative lower ratio",
             ratio-1/(2*(pi/5).cos()))
    positive("large-index derivative upper ratio",
             (2*pi/5).sin()-ratio)
    positive("squared lower algebraic ratio",
             ratio**2-(3-arb(5).sqrt())/2)
    positive("squared upper algebraic ratio",
             (5+arb(5).sqrt())/8-ratio**2)
    positive("displayed phase lower",2*x.real-rational(".365"))
    positive("displayed phase upper",rational(".367")-2*x.real)
    positive("displayed ratio lower",ratio-rational(".652"))
    positive("displayed ratio upper",rational(".653")-ratio)

    def sine_primitive(value):
        value = acb(value)
        return -ii*pi*(value*value-value)/2 \
            +ii*(2*pi*ii*value).exp().polylog(2)/(2*pi)-ii*pi/12

    def denominator_primitive(value):
        return ((K*(-2*pi*ii*value).exp()).polylog(2)-K.polylog(2))/(2*pi*ii)

    def entropy(s,t):
        return (sine_primitive(s+t)-sine_primitive(s)-sine_primitive(t)
                -denominator_primitive(s)-denominator_primitive(t)).real \
            +(s+t)*abs(K).log()-abs(K).log()

    edges = []
    for c_value,t_value in [("1/5","312863/1000000"),("2/5","2888/10000")]:
        c,t = rational(c_value),rational(t_value)
        positive(f"edge {c_value} support interior lower",t-a)
        positive(f"edge {c_value} support interior upper",b-t)
        value = entropy(c,t)
        derivative = (abs(K)*(pi*(c+t)).sin() /
                      ((pi*t).sin()*abs(1-K*(-2*pi*ii*t).exp()))).log()
        tangent_correction = max((derivative*(a-t)).upper(),
                                 (derivative*(b-t)).upper())
        upper = value+tangent_correction
        positive(f"edge {c_value} entire tangent below .841",
                 rational(".841")-upper)
        edges.append({
            "fixed_coordinate":c_value,
            "support_coordinate":t_value,
            "entropy_at_support":str(value),
            "derivative_at_support":str(derivative),
            "whole_interval_tangent_upper":str(upper),
        })

    dependencies = [
        "notes/research_power_four_real_complement.md",
        "notes/research_power_four_finite_source.md",
        "notes/research_three_four_source_interface.md",
        "notes/research_root_pochhammer_interpolation.md",
        "notes/exact_factorial_interpolation_and_complex_contours.md",
    ]
    result = {
        "status":"passed",
        "precision_bits":args.precision,
        "scope":"Strict parameter-region inequalities and two outward tangent bounds. The written analytic reduction covers the full real index triangle outside [1/5,2/5]^2 and extends to nearby independent boundary parameters. No complex index contour or alias bound is checked.",
        "strict_comparison_count":len(comparisons),
        "comparisons":comparisons,
        "edge_bounds":edges,
        "global_real_complement_rate":"841/1000",
        "inherited_reference":{
            "path":str(reference_path.relative_to(ROOT)),
            "sha256":sha256(reference_path.read_bytes()).hexdigest(),
            "script_and_all_dependency_hashes_verified":True,
        },
        "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256":{
            path:sha256((ROOT/path).read_bytes()).hexdigest()
            for path in dependencies
        },
    }
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in
                    ["status","strict_comparison_count","global_real_complement_rate"]},indent=2))
    for edge in edges:
        print("Edge",edge["fixed_coordinate"],"upper",
              edge["whole_interval_tangent_upper"])


if __name__ == "__main__":
    main()
