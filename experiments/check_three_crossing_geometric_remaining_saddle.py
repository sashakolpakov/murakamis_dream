#!/usr/bin/env python3
"""Exact canonical maps and local remaining-row saddle bounds.

No finite-source complex interpolation or asymptotic is inferred.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp
from check_three_crossing_geometric_branch import ComplexRectangle as R, Interval

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_three_crossing_geometric_remaining_saddle.md"
DEPENDENCY = ROOT / "experiments/check_three_crossing_geometric_branch.py"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-three-crossing-geometric-remaining-saddle.json",
    )
    args = parser.parse_args()
    tau = sp.Symbol("tau")
    r = tau**2 - 3*tau + 3
    z = 4 - 5*tau + 4*tau**2 - tau**3
    p = z*r - 1
    v = (tau-2)**2*(tau**2-2*tau+2)
    f = sp.Poly(v + 2*sp.I, tau, extension=sp.I)
    e = -(tau-1)**2/(tau-2)
    xclock = 1/r
    yclock = r/p
    lam = -(tau-2)**3/r
    mu = (tau-1)**3/r

    def crossing(clock, shift):
        k = sp.factor((-1+(clock-1)*shift)/clock)
        new_clock = sp.factor(clock+clock*k+1)
        new_k = -1/clock
        return new_clock, sp.factor((new_clock*new_k+1)/(new_clock-1))

    gamma_clock, gamma_shift = crossing(1/tau, -(tau-1)**2)
    c1, e1 = crossing(gamma_clock, gamma_shift)
    c2, e2 = crossing(c1, e1)
    t1 = lam*xclock*(xclock-yclock)/(yclock*(1-xclock)**4)
    t2 = yclock*(yclock-xclock)*(1+yclock)**2/(1-yclock)**4
    identities = {
        "gamma_physical_clock": gamma_clock-r,
        "gamma_backward_shift": gamma_shift-e,
        "first_remaining_clock": c1-(z-tau),
        "second_remaining_clock": c2-(z-1/r),
        "final_wire_clock": 1/c2-yclock,
        "final_backward_shift": 1/e2+(tau-2)**3*(tau**2-2*tau+2)**2/(tau-1)**2,
        "characteristic_sum": lam+mu-(3-2*xclock),
        "characteristic_difference": lam-mu-(3-2*tau),
        "characteristic_product": lam*mu-(2-xclock-1/xclock)*(1-xclock),
        "radicand": (3-2*tau)**2-(4/xclock-3),
        "original_coefficient_ratio": -lam/(2-xclock-1/xclock)-1/e,
        "first_logarithmic_exponential": t1-1,
        "second_logarithmic_exponential":
            t2-1-r*p*(v**2+4)/((tau-2)**7*(tau**2-2*tau+2)**4),
        "mixed_hessian_factor": 2/(r*yclock-1)-2*p/((tau-2)*(tau-1)**4),
    }
    for name, expr in identities.items():
        assert sp.cancel(expr) == 0, name

    factors = {
        "r": r, "P": p, "tau_minus_1": tau-1, "tau_minus_2": tau-2,
        "two_tau_minus_3": 2*tau-3,
        "quadratic": tau**2-2*tau+2,
        "Y_minus_1": p-r, "Y_plus_1": p+r,
        "rY_minus_1": r*r-p,
        "quartic_derivative": sp.diff(v,tau),
    }
    for name, factor in factors.items():
        assert sp.gcd(f, sp.Poly(factor,tau,extension=sp.I)).degree() == 0, name

    # The conjugate of the previously isolated geometric disk.
    tb = R(Interval(F(943,1000),F(945,1000)),
           Interval(-F(1304,1000),-F(1302,1000)))
    rb = (tb-F(3,2))*(tb-F(3,2))+F(3,4)
    zb = 2+(1-tb)*(1-tb)*(2-tb)
    pb = zb*rb-1
    yb = rb/pb
    assert -F(13,20) < rb.real.lo < rb.real.hi < -F(63,100)
    assert F(36,25) < rb.imag.lo < rb.imag.hi < F(73,50)
    assert F(9,100) < yb.real.lo < yb.real.hi < F(4,25)
    assert F(3,5) < yb.imag.lo < yb.imag.hi < F(7,10)
    assert F(13,20)**2+F(73,50)**2 < F(8,5)**2
    assert F(63,100)/F(73,50) > F(2,5)
    assert F(13,20)/F(36,25) < F(1,2)
    assert F(4,25)**2+F(7,10)**2 < 1
    assert 4*F(1703665,10**6)**3 < F(2808229,10**6)**3

    denominator_boxes = {
        "r": rb, "P": pb, "tau_minus_2":tb-2, "two_tau_minus_3":2*tb-3,
        "r_minus_1":rb-1, "rY_minus_1":rb*yb-1,
        "Y_minus_1":yb-1, "Y_squared_minus_1":yb*yb-1,
    }
    denominator_lower = {}
    for name, box in denominator_boxes.items():
        squared = box.real*box.real+box.imag*box.imag
        assert squared.lo > 0, name
        denominator_lower[name] = str(squared.lo)

    hxx = 6*rb/((tb-2)*(2*tb-3))-1+(rb*yb+1)/(rb*yb-1)-4*(rb+1)/(rb-1)
    hxy = R(2)/(rb*yb-1)
    hyy = (rb*yb+1)/(rb*yb-1)-6*(yb+1)/(yb-1)+4*(yb*yb+1)/(yb*yb-1)+1
    assert hxx.imag.lo > 2
    assert hyy.imag.lo > 4
    assert -F(1,5) < hxy.imag.lo < hxy.imag.hi < F(1,5)

    record_box = lambda a: {"real":a.real.record(),"imaginary":a.imag.record()}
    result = {
        "status":"passed",
        "scope": (
            "Exact canonical-map and stationary-equation identities, root-chart "
            "regularity, rational coordinate bounds and local Hessian negativity. "
            "No finite-source complex WKB or contour-cycle conclusion."
        ),
        "python_version":platform.python_version(),
        "sympy_version":sp.__version__,
        "script_sha256":digest(Path(__file__).resolve()),
        "note_sha256":digest(NOTE),
        "dependency_sha256":{str(DEPENDENCY.relative_to(ROOT)):digest(DEPENDENCY)},
        "identities":list(identities),
        "excluded_factors":list(factors),
        "r_rectangle":record_box(rb),
        "Y_rectangle":record_box(yb),
        "denominator_norm_squared_lower_bounds":denominator_lower,
        "scaled_hessian": {
            "xx":record_box(hxx), "xy":record_box(hxy), "yy":record_box(hyy)
        },
        "proved_minus_real_hessian_lower_bound":"(9*pi/5)*identity",
        "proved_geometric_characteristic_modulus_ratio_bound":"1/2",
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({
        "status":"passed","identities":len(identities),
        "excluded_factors":len(factors),"denominator_boxes":len(denominator_boxes),
        "output":str(args.output),"script_sha256":result["script_sha256"],
    },indent=2))


if __name__ == "__main__":
    main()
