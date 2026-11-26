#!/usr/bin/env python3
"""Exact constants for the adjacent degree-power source theorem.

The linked proof supplies the original finite-trace and contour argument.
This checks its rational inequalities and exact matrix identities; no
finite-level numerical pattern is used.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def main():
    root = Path(__file__).resolve().parents[1]
    margins = {}
    identities = []

    def less(name, lower, upper):
        assert lower < upper, (name, lower, upper)
        margins[name] = str(upper-lower)

    def equal(name, left, right):
        assert left == right, (name, left, right)
        identities.append(name)

    def symbolic(name, expression):
        result = sp.factor(sp.together(expression))
        assert result == 0, (name, result)
        identities.append(name)

    r, pi_upper = F(1, 10), F(22, 7)
    cosh = 1+r*r/(2*(1-r*r/12))
    sinh_ratio = 1/(1-r*r/6)
    less("complex tangent linear majorant",
         sinh_ratio/(2-cosh), F(51, 50))
    less("integrated tangent remainder", F(51, 50)**2/24, F(1, 16))
    less("cosine remainder coefficient", 1/(8*(1-r*r/12)), F(1, 7))
    less("cosine disk modulus", cosh, F(101, 100))
    less("asinh argument disk", F(51, 100)*F(1, 5)*F(101, 100), F(11, 100))
    less("asinh remainder squared comparison", F(25),
         36*(1-F(11, 100)**2)**3)
    f_coefficient = (F(1, 8)+F(2, 5)*(F(51, 100)*F(101, 100))**3
                     +F(51, 350))
    less("incidence remainder coefficient", f_coefficient, F(1, 3))

    eps = r*r/3
    equal("relative C error", eps, F(1, 300))
    equal("C derivative row bound", 8*r/3, F(4, 15))
    maximum = 2*pi_upper/(64*(1-eps))
    equal("fixed-point radius exact bound", maximum, F(825, 8372))
    less("fixed-point stays inside radius", maximum, r)
    contraction = 2*pi_upper*F(4, 15)/(64*(1-eps)**2)
    equal("fixed-point contraction exact bound", contraction, F(16500, 625807))
    less("fixed-point contraction", contraction, F(1, 32))
    height = 2*pi_upper*(1+eps)/(1-eps)**2
    equal("height coefficient exact bound", height, F(567600, 89401))
    less("height coefficient", height, F(32, 5))
    equal("maximum contour height", F(32, 5)/64, r)
    equal("activation cost per incidence", F(16, 5)/64**2, F(1, 1280))
    less("positive edge square-root margin",
         F(99, 100)**2, 1-2*F(51, 1000)**2)
    less("positive edge real tangent norm", 2*F(51, 1000)**2, F(1, 10)**2)

    equal("complex s lower factor", 1-4*r*r, F(24, 25))
    less("matrix derivative Frobenius bound",
         2/F(24, 25)**3, F(8, 5)**2)
    equal("vertical matrix variation", 2*r*F(8, 5), F(8, 25))
    less("real eigenvalue lower comparison", F(4, 7)**2, F(1, 3))
    less("real eigenvalue upper comparison", F(3), F(7, 4)**2)
    less("real matrix lower bound", F(1, 4), F(4, 7)-F(8, 25))
    less("real matrix upper bound", F(7, 4)+F(8, 25), F(21, 10))
    equal("Young B coefficient", F(16, 25)**2/(4*F(1, 8)), F(512, 625))
    less("combined B coefficient", F(21, 10)+F(512, 625), F(3))
    equal("vertical real displacement floor", F(3, 2)-r, F(7, 5))
    equal("vertical imaginary displacement ceiling", 2*r, F(1, 5))
    equal("mixed-current gap coefficient",
          F(7, 5)**2/32-F(3, 4)*F(1, 5)**2, F(1, 32))
    less("mixed-current strict gap", F(1, 110), 1/(32*pi_upper))
    less("removed-row strict gap", F(1, 10), F(21, 200)-F(1, 1280))

    A, B = sp.symbols("A B", nonnegative=True)
    P = A*(1+A+2*B)**2+(2*B+A)*(1+B)**2
    positive = (A**3+2*A**2*B+4*A**2+A*B**2
                +6*A*B+4*A+2*B**2+4*B+2)
    symbolic("matrix derivative positive polynomial",
             2*(1+A+B)**3-P-positive)
    w, z = sp.symbols("w z")
    s = sp.sqrt(1+w*w+z*z)
    K = sp.Matrix([[1+w*w, -w*z], [-w*z, 1+z*z]])/s
    dw = sp.Matrix([[w*(1+w*w+2*z*z), -z*(1+z*z)],
                    [-z*(1+z*z), -w*(1+z*z)]])/s**3
    for a in range(2):
        for b in range(2):
            symbolic(f"literal K derivative entry {a}{b}",
                     sp.diff(K[a,b],w)-dw[a,b])
    symbolic("real K determinant", K.det()-1)
    symbolic("real K trace", sp.trace(K)-(s+1/s))
    m, e = sp.symbols("m e")
    symbolic("original trace power of N", 2*m-sp.Rational(3,2)*e
             -m/2-sp.Rational(3,2)*(m-e))

    # Nodewise mixed regime: existing power-dominated rows and new R>=512 rows.
    less("hybrid K derivative in tangent variable", F(2)/F(3,4)**3,
         F(9,4)**2)
    equal("hybrid K derivative in angle variable", F(9,4)*F(2,3), F(3,2))
    equal("hybrid C derivative row", F(3,4)+F(3,2), F(9,4))
    equal("hybrid quotient radius", 2*pi_upper/(F(3,5)*512), F(55,2688))
    less("hybrid quotient interior", F(55,2688), F(1,40))
    equal("hybrid quotient contraction", 2*pi_upper*F(9,4)/(F(3,5)**2*512),
          F(550,7168))
    less("hybrid quotient contraction strict", F(550,7168), F(1,12))
    less("hybrid direct-return contraction", F(43,90), F(1,2))
    equal("hybrid height coefficient", 2*F(7,5)/F(3,5)**2, F(70,9))
    less("hybrid activation cost", F(35,9)*pi_upper/512**2, F(3,40))
    less("wide Hessian lower endpoint x0", F(1,3), F(41,109))
    less("wide Hessian lower endpoint x2 squared", F(209,123)**2, F(3))
    less("wide K norm denominator", F(9,10)**2, F(41,50))
    equal("hybrid Young B coefficient", F(20,3)**2/(4*F(1,6)), F(200,3))
    equal("hybrid combined B coefficient", F(10,3)+F(200,3), F(70))
    equal("hybrid D displacement", F(3,2)-F(1,40), F(59,40))
    equal("hybrid D vertical loss",
          F(59,40)**2/24-F(35,2)*F(1,20)**2, F(1801,38400))
    less("hybrid D current margin", F(1,70), F(1801,38400)/pi_upper)
    less("hybrid P current margin", F(1,220), F(3,200)/pi_upper)
    equal("hybrid removed-row loss", F(21,200)-F(3,40), F(3,100))
    x = sp.symbols("x", nonnegative=True)
    quotient = sp.Rational(41,50)*sp.sqrt(1+x)/(x+sp.Rational(109,50))
    symbolic("wide Hessian one-variable derivative",
             sp.diff(quotient,x) -
             sp.Rational(41,50)*(sp.Rational(9,50)-x)/
             (2*sp.sqrt(1+x)*(x+sp.Rational(109,50))**2))
    xr, yr, dot = sp.symbols("xr yr dot", real=True)
    symbolic("wide determinant lower numerator",
             1+xr-yr-(xr*yr-dot**2)-((1-yr)*(1+xr)+dot**2))
    symbolic("wide s modulus comparison",
             (1+xr+yr)**2-((1+xr-yr)**2+4*dot**2)
             -4*((1+xr)*yr-dot**2))

    dependencies = [
        "notes/research_network_degree_power_source.md",
        "notes/research_bare_kernel_thin_rectangle.md",
        "notes/research_path_mixed_trace_currents.md",
        "notes/research_small_charge_path_source.md",
        "notes/research_positive_edge_global_monotonicity.md",
        "notes/research_exact_complete_trace_contour.md",
        "notes/research_positive_point_marked_completion.md",
        "notes/research_degree_controlled_network_source.md",
        "notes/research_edge_hessian_and_phase_response.md",
    ]
    result = {
        "status": "passed",
        "strict_rational_comparisons": len(margins),
        "exact_identities": len(identities),
        "scope": (
            "Exact elementary and matrix constants for the original adjacent "
            "graph source under n_v^2+d_v^2>=4096, and its nodewise mixed "
            "extension |n_v|>=max(8,4d_v) or n_v^2+d_v^2>=512^2. The linked proof retains "
            "the full finite trace, endpoints, aliases and ordinary normals. "
            "No arbitrary-graph knot identification is tested."),
        "positive_margins": margins,
        "identities": identities,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: sha256((root/name).read_bytes()).hexdigest()
            for name in dependencies},
    }
    output = root/"repro/results/research-network-degree-power-source.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed {len(margins)} strict rational comparisons and "
          f"{len(identities)} exact identities.")
    print(output)


if __name__ == "__main__":
    main()
