#!/usr/bin/env python3
"""Outward certificate for the selected action of the remaining contraction.

This certifies a phase value, not its global contribution or its volume
interpretation. The root is the previously isolated geometric root.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from verify_next_crossing_complex_phase import (
    C, R, PI, IM, logarithm, dilogarithm, phase, run as verify_inner,
)


ROOT=Path(__file__).resolve().parents[1]


def inverse_dilog(z):
    """Principal Li_2(z) in this calculation, with -z in the right half-plane."""
    return -dilogarithm(z.inverse(),terms=1000)-C(PI.square()/6)-logarithm(-z)**2/2


def left_dilog(z):
    """Move a left-half-plane argument into a smaller disk."""
    assert z.re.hi<0
    return -dilogarithm(z/(z-1))-logarithm(1-z)**2/2


def J(z,li):
    return IM*C(PI)*(z-z*z)/2+IM*(li-C(PI.square()/6))/(2*C(PI))


def run():
    inner_record=verify_inner()
    tr=F(inner_record["root_center"][0])
    ti=F(inner_record["root_center"][1])
    eps=F(inner_record["root_radius"])
    tau=C(R(tr-eps,tr+eps),R(ti-eps,ti+eps))
    r=(tau-F(3,2))**2+F(3,4)
    trace=4-5*tau+4*tau**2-tau**3
    X=r.inverse()
    Y=r/(trace*r-1)
    Yh=tau.inverse()
    logX=logarithm(IM*X)-IM*C(PI/2)
    x=-logX/(2*IM*C(PI))
    y=logarithm(Y)/(2*IM*C(PI))
    zh=logarithm(Yh)/(2*IM*C(PI))
    selected_inner=phase(zh,X,Yh,logX,dilogarithm(Yh))
    Jx=J(x,inverse_dilog(X.inverse()))
    Jy=J(y,dilogarithm(Y))
    Jxy=J(x+y,left_dilog(Y/X))
    J2y=J(2*y,dilogarithm(Y*Y))
    outer=(Jxy-2*Jx-6*Jy+J2y
           +IM*C(PI)*((x-y)**2+x+y)/2)
    selected=selected_inner+outer+IM*C(PI)*x
    assert selected.re.lo>F(153,100)
    assert selected.re.hi<F(77,50)
    assert F(3,10)<x.re.lo and x.re.hi<F(1,3)
    assert F(-3,40)<x.im.lo and x.im.hi<F(-7,100)
    assert F(1,5)<y.re.lo and y.re.hi<F(1,4)
    assert F(3,50)<y.im.lo and y.im.hi<F(7,100)
    # The exact whole-error estimate is independent of the contour.
    zero_radius_bound=F(1291410721,861616000)
    full_error_bound=zero_radius_bound+F(1,1000)
    assert full_error_bound<F(3,2)
    assert selected.re.lo-full_error_bound>F(3,100)
    path=Path(__file__).resolve()
    dependency=path.with_name("verify_next_crossing_complex_phase.py")
    return {
        "status":"passed",
        "scope":"Selected action exceeds 1.53; no assertion of global saddle survival or volume identification.",
        "root_certificate":inner_record,
        "inverse_clock":X.record(),
        "remaining_wire":Y.record(),
        "remaining_color_x":x.record(),
        "remaining_color_y":y.record(),
        "selected_action":selected.record(),
        "whole_error_bound_on_radius_1e_minus_6":str(full_error_bound),
        "action_minus_error_lower_bound":str(selected.re.lo-full_error_bound),
        "script_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "dependency_sha256":{str(dependency.relative_to(ROOT)):
                            hashlib.sha256(dependency.read_bytes()).hexdigest()},
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-three-crossing-closing-action.json")
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("Selected closing action and whole-error separation certified.")
    print(f"Saved {args.output}")
