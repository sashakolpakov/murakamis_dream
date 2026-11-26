#!/usr/bin/env python3
"""Exact scalar and algebra checks for the large-angle incidence bound.

The uniform finite-kernel, branch, and derivative arguments are proved in
the linked note. This checker does not infer an asymptotic from samples.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    comparisons = []
    identities = []

    def less(name, left, right):
        assert left < right, (name, left, right)
        comparisons.append({
            "name": name,
            "left": str(left),
            "right": str(right),
            "positive_margin": str(right - left),
        })

    def equal(name, left, right):
        assert left == right, (name, left, right)
        identities.append({"name": name, "kind": "rational"})

    def symbolic(name, expression):
        result = sp.factor(sp.together(sp.trigsimp(expression)))
        assert result == 0, (name, result)
        identities.append({"name": name, "kind": "symbolic"})

    hmax = F(3, 10)
    cosh_majorant = 1 + hmax*hmax/(2*(1-hmax*hmax/12))
    less("cosh(3/10) rational majorant", cosh_majorant, F(21, 20))
    less("reflected-ratio coefficient stays below two", F(21, 20), F(2))
    less("sqrt(5) upper square", F(5), F(81, 16))
    less("critical q stays above cos(2pi/5)", F(5, 16), F(20, 61))
    equal("uniform critical-q lower bound", 1/(F(21, 20)+2), F(20, 61))
    equal("tan(2pi/5) square upper bound", 5+2*F(9, 4), F(19, 2))
    less("tan(2pi/5) stays below pi via squares", F(19, 2), F(31, 10)**2)
    less("Archimedean pi lower bound exceeds 31/10", F(31, 10), F(333, 106))
    height_cost = hmax*hmax/4
    equal("height cost", height_cost, F(9, 400))

    less("sqrt(2) upper square", F(2), F(100, 49))
    d_lower = (13*F(2, 3)-1)/(12*F(22, 7)*F(10, 7))
    equal("real loss rational lower bound", d_lower, F(1127, 7920))
    centered_margin = d_lower-height_cost
    equal("wide centered margin", centered_margin, F(593, 4950))
    less("claimed incidence loss", F(21, 200), centered_margin)
    equal("spare derivative-neighborhood margin",
          centered_margin-F(21, 200), F(293, 19800))
    less("double removed loss", 2*F(21, 200), 2*d_lower)

    catalan_lower = sum(
        (F((-1)**k, (2*k+1)**2) for k in range(6)), F(0)
    )
    equal("six-term Catalan lower sum", catalan_lower,
          F(10956424, 12006225))
    complete_lower = F(14, 11)*catalan_lower
    equal("complete rate rational lower bound", complete_lower,
          F(21912848, 18866925))
    less("complete rate exceeds 29/25", F(29, 25), complete_lower)
    less("inverse sqrt(2) upper square", F(1, 2), F(25, 49))
    equal("selected complete action loss ceiling",
          F(22, 7)*F(5, 7)/8, F(55, 196))
    selected_lower = F(29, 25)-F(55, 196)
    equal("selected phase lower bound", selected_lower, F(4309, 4900))
    less("full radical retains the incidence loss",
         hmax+F(21, 200), selected_lower)

    q, C, v, h, ell = sp.symbols("q C v h ell", real=True)
    symbolic("regular critical majorant numerator",
             q*(q+C)-(1-q)**2-((C+2)*q-1))
    ratio = q*(q+C)/(1-q)**2
    symbolic("regular real-ratio monotonic derivative",
             sp.diff(ratio, q)-(C+(C+2)*q)/(1-q)**3)
    symbolic("critical majorant equals one",
             ratio.subs(q, 1/(C+2))-1)
    symbolic("reflected ratio difference",
             (1+v)**2-v*(C+v)-(1+(2-C)*v))
    cr, ci = sp.symbols("cr ci", real=True)
    symbolic("complex reciprocal real-part upper bound",
             1/q-(q+cr)/((q+cr)**2+ci**2)
             -(cr*(q+cr)+ci**2)/(q*((q+cr)**2+ci**2)))
    a = sp.symbols("a", real=True)
    symbolic("tan-cubed primitive",
             sp.diff(sp.tan(a)**2/2+sp.log(sp.cos(a)), a)
             -sp.tan(a)**3)
    symbolic("integrated asinh lower polynomial",
             2/sp.sqrt(2)*(ell/2-(1-ell)/24)
             -(13*ell-1)/(12*sp.sqrt(2)))
    symbolic("asinh polynomial derivative comparison",
             (1-q**2/2)**2*(1+q**2)
             -(1-3*q**4/4+q**6/4))

    dependencies = [
        "notes/research_path_mixed_trace_currents.md",
        "notes/research_zero_power_internal_boundary_theorem.md",
        "notes/research_three_crossing_real_period_newton_bound.md",
        "notes/research_uniform_factorial_and_boundary_decay.md",
        "notes/research_high_newton_radical_contraction.md",
        "notes/research_unsummed_network_phase_coercivity.md",
        "notes/research_internal_pair_reflected_current_identity.md",
    ]
    record = {
        "status": "passed",
        "scope": (
            "Exact scalar comparisons and maximizer algebra only. "
            "The note proves the uniform original-kernel implication, "
            "all endpoints, and ordinary derivatives. No path assembly "
            "or finite-level extrapolation is tested."
        ),
        "strict_rational_comparisons": len(comparisons),
        "rational_identities": sum(x["kind"] == "rational" for x in identities),
        "symbolic_identities": sum(x["kind"] == "symbolic" for x in identities),
        "checks": comparisons,
        "identities": identities,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: sha256((root/name).read_bytes()).hexdigest()
            for name in dependencies
        },
    }
    output = args.output or root/"repro/results/research-path-large-angle-incidence.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(
        f"passed: {len(comparisons)} strict rational comparisons, "
        f"{record['rational_identities']} rational identities, "
        f"{record['symbolic_identities']} symbolic identities"
    )
    print(output)


if __name__ == "__main__":
    main()
