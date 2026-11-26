#!/usr/bin/env python3
"""Exact outward scalar rate bounds for the remaining adjacent source.

All asserted comparisons use rational intervals.  The imported helper
supplies the already documented logarithm/dilogarithm series with explicit
tails; no numerical quadrature or floating-point root selection is used.
"""

from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import json

import verify_next_crossing_complex_phase as base


R, C, PI, IM, DEN = base.R, base.C, base.PI, base.IM, base.DEN
ROOT = Path(__file__).resolve().parents[1]


def sqrt_real(x):
    x = base.real(x)
    assert x.lo >= 0
    lo = (x.lo * DEN**2)
    hi = (x.hi * DEN**2)
    lower = isqrt(lo.numerator // lo.denominator)
    upper = isqrt(-((-hi.numerator) // hi.denominator)) + 1
    return R(F(lower, DEN), F(upper, DEN))


def sqrt_upper(z):
    """Square root with positive imaginary part, Re z arbitrary."""
    assert z.im.lo >= 0
    radius = sqrt_real(z.re.square() + z.im.square())
    u = sqrt_real((radius + z.re) / 2)
    v = sqrt_real((radius - z.re) / 2)
    return C(u, v)


def unit_dilogarithm(z):
    """Principal Li_2 on the nonreal unit circle, or z=-1.

    Reflection is used near 1; elsewhere the Mobius identity sends the
    point strictly inside the convergence disk.  Both identities use
    principal logarithms and follow by differentiating along the ray.
    """
    if z.re.lo == z.re.hi == -1 and z.im.lo == z.im.hi == 0:
        return C(-PI.square() / 12)
    one_minus = 1 - z
    assert one_minus.re.lo > 0
    if one_minus.radius_upper() < F(9,10):
        # The only use of this branch has Re z>0.
        assert z.re.lo > 0
        return (C(PI.square()/6) - base.logarithm(z)*base.logarithm(one_minus)
                - base.dilogarithm(one_minus))
    transformed = z/(z-1)
    assert transformed.radius_upper() < 1
    return -base.dilogarithm(transformed)-base.logarithm(one_minus)**2/2


def stationary_real_rate(X):
    """A(x)=Re S(e^-2piix) on 0<x<=1/2, selected from x=0."""
    assert X.im.hi <= 0
    delta = 4*X.inverse()-3
    if delta.im.lo < 0:
        # At X=-1 the imaginary part is exactly zero, not a sign choice.
        raise AssertionError("selected upper square-root input left its half-plane")
    tau = (3-sqrt_upper(delta))/2
    Y = tau.inverse()
    logY = base.logarithm(Y)
    z = logY/(2*IM*C(PI))
    if X.re.lo == X.re.hi == -1:
        logX = -IM*C(PI)
    else:
        logX = base.logarithm(IM*X)-IM*C(PI/2)
    numerator = (unit_dilogarithm(X)-base.dilogarithm(X*Y)
                 -C(PI.square()/2)+3*base.dilogarithm(Y))
    action = ((1-z)*logX+numerator/(2*IM*C(PI))
              +2*IM*C(PI)*(z*z-z))
    return action.re, {"clock":X.record(),"tau":tau.record(),
                       "saddle":z.record(),"action":action.record()}


def sine_integral_from_clock(Y):
    # J(t)=-Im Li_2(e^{2piit})/(2pi), including its real-axis limits.
    return -unit_dilogarithm(Y).im/(2*PI)


def cubic_real_root():
    def polynomial(t):
        return t**3-2*t**2-t+3
    lo, hi = F(-2), F(-1)
    assert polynomial(lo)<0<polynomial(hi)
    # Its derivative is positive throughout [-2,-1].
    for _ in range(150):
        mid=(lo+hi)/2
        if polynomial(mid)<0:
            lo=mid
        else:
            hi=mid
    return R(lo,hi)


def run():
    sqrt5 = sqrt_real(R(5))
    cos5 = (1+sqrt5)/4
    sin5 = sqrt_real(R(10)-2*sqrt5)/4
    X10 = C(cos5,-sin5)
    A10, A10_data = stationary_real_rate(X10)
    assert A10.hi < F(1,3)

    # g(1/10)=J(1/5)-4J(1/10).
    Y10 = C(cos5,sin5)
    g10 = sine_integral_from_clock(Y10**2)-4*sine_integral_from_clock(Y10)
    assert g10.hi < F(9,20)

    peak_cubic = cubic_real_root()
    peakX = C(peak_cubic/2,-sqrt_real(1-(peak_cubic/2).square()))
    Apeak, Apeak_data = stationary_real_rate(peakX)
    assert Apeak.hi < F(23,50)

    # At x=1/2, J(1/2)=0; hence A(1/2)=B(1/2).
    Bhalf, Bhalf_data = stationary_real_rate(C(-1))
    assert Bhalf.hi < F(43,100)

    # Maximum of J(2y)-6J(y): cos(pi y)=(sqrt(17)-1)/4.
    cosine = (sqrt_real(R(17))-1)/4
    sine = sqrt_real(1-cosine.square())
    Ymax = C(2*cosine.square()-1,2*cosine*sine)
    ymax = sine_integral_from_clock(Ymax**2)-6*sine_integral_from_clock(Ymax)
    assert ymax.hi < F(9,10)

    # Catalan's alternating series gives an elementary b_2 bound.
    catalan_upper = sum((F((-1)**m,(2*m+1)**2) for m in range(65)),F(0))
    b2 = R(0,catalan_upper)*2/PI
    assert b2.hi < F(73,125)

    targets = {
        "A_one_tenth": {"interval":A10.record(),"upper_bound":"1/3",**A10_data},
        "Newton_g_one_tenth": {"interval":g10.record(),"upper_bound":"9/20"},
        "A_global_peak": {"interval":Apeak.record(),"upper_bound":"23/50",
                          "cubic_root":peak_cubic.record(),**Apeak_data},
        "B_half": {"interval":Bhalf.record(),"upper_bound":"43/100",**Bhalf_data},
        "max_J2y_minus_6Jy": {"interval":ymax.record(),"upper_bound":"9/10",
                              "unit_clock":Ymax.record()},
        "b2": {"interval":b2.record(),"upper_bound":"73/125"},
    }
    # Include the whole ordinary-boundary perturbation cost <1/1000.
    rates = {
        "left_x": F(1,3)+2*F(73,125)+F(1,1000),
        "low_y": F(9,20)+F(73,125)+F(23,50)+F(1,1000),
        "high_j": F(43,100)+F(1,6)+F(9,10)+F(1,1000),
    }
    assert all(value < F(153,100) for value in rates.values())
    return {
        "status":"passed",
        "method":"Exact rational outward intervals and explicit analytic series tails",
        "rounding_denominator":str(DEN),
        "certificates":targets,
        "boundary_radius":"1/1000000",
        "combined_rate_bounds":{key:str(value) for key,value in rates.items()},
        "selected_rate_lower_bound":"153/100",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies":{str(Path(base.__file__).relative_to(ROOT)):
                        hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest()},
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-three-crossing-real-tail-rates.json")
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("All exact real-tail rate certificates passed.")
    print(f"Saved {args.output}")
