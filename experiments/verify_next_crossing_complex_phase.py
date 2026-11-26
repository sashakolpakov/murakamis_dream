#!/usr/bin/env python3
"""Outward rational certificates for the next-crossing factorial contour.

All enclosures use rational interval arithmetic with outward rounding.
Logarithms, exponentials and dilogarithms have explicit series remainders.
No floating-point evaluation is used in any asserted inequality.
"""

from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import argparse
import hashlib
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEN = 10**50


def down(value):
    value = F(value)*DEN
    return F(value.numerator//value.denominator, DEN)


def up(value):
    return -down(-F(value))


class R:
    def __init__(self, lo, hi=None):
        self.lo = down(lo)
        self.hi = up(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = real(other)
        return R(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return R(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-real(other)

    def __rsub__(self, other):
        return real(other)+-self

    def __mul__(self, other):
        other = real(other)
        values = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return R(min(values),max(values))

    __rmul__ = __mul__

    def inverse(self):
        assert self.lo*self.hi > 0
        return R(1/self.hi,1/self.lo)

    def __truediv__(self, other):
        return self*real(other).inverse()

    def square(self):
        a,b=self.lo*self.lo,self.hi*self.hi
        return R(0 if self.lo <= 0 <= self.hi else min(a,b),max(a,b))

    def record(self):
        return [str(self.lo),str(self.hi)]


def real(value):
    return value if isinstance(value,R) else R(value)


class C:
    def __init__(self, re=0, im=0):
        self.re,self.im=real(re),real(im)

    def __add__(self, other):
        other=complex_box(other)
        return C(self.re+other.re,self.im+other.im)

    __radd__=__add__

    def __neg__(self):
        return C(-self.re,-self.im)

    def __sub__(self,other):
        return self+-complex_box(other)

    def __rsub__(self,other):
        return complex_box(other)+-self

    def __mul__(self,other):
        other=complex_box(other)
        return C(self.re*other.re-self.im*other.im,
                 self.re*other.im+self.im*other.re)

    __rmul__=__mul__

    def inverse(self):
        denominator=(self.re.square()+self.im.square()).inverse()
        return C(self.re*denominator,-self.im*denominator)

    def __truediv__(self,other):
        return self*complex_box(other).inverse()

    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        answer=C(1)
        for _ in range(n):
            answer=answer*self
        return answer

    def radius_upper(self):
        re=max(abs(self.re.lo),abs(self.re.hi))
        im=max(abs(self.im.lo),abs(self.im.hi))
        scaled=(re*re+im*im)*DEN**2
        upper_integer=-((-scaled.numerator)//scaled.denominator)
        return F(isqrt(upper_integer)+1,DEN)

    def widen(self,error):
        return C(self.re+R(-error,error),self.im+R(-error,error))

    def record(self):
        return {"real":self.re.record(),"imaginary":self.im.record()}


def complex_box(value):
    return value if isinstance(value,C) else C(value)


def atan_real(value,terms=90):
    value=F(value)
    partial=sum(((-1)**n*value**(2*n+1)/F(2*n+1) for n in range(terms)),F(0))
    error=value**(2*terms+1)/F(2*terms+1)
    return R(partial-error,partial+error)


PI=16*atan_real(F(1,5))-4*atan_real(F(1,239))
IM=C(0,1)


def logarithm(z,terms=250):
    """Principal logarithm in the right half-plane."""
    z=complex_box(z)
    assert z.re.lo>0
    w=(z-1)/(z+1)
    radius=w.radius_upper()
    assert radius<1
    partial=C(0)
    power=w
    square=w*w
    for n in range(terms):
        partial+=2*power/F(2*n+1)
        power=power*square
    error=2*radius**(2*terms+1)/(F(2*terms+1)*(1-radius*radius))
    return partial.widen(error)


def dilogarithm(z,terms=250):
    z=complex_box(z)
    radius=z.radius_upper()
    assert radius<1
    partial=C(0)
    power=z
    for n in range(1,terms+1):
        partial+=power/F(n*n)
        power=power*z
    error=radius**(terms+1)/(F((terms+1)**2)*(1-radius))
    return partial.widen(error)


def exponential(z,terms=100):
    z=complex_box(z)
    radius=z.radius_upper()
    assert radius<terms+2
    partial=C(1)
    power=C(1)
    for n in range(1,terms+1):
        power=power*z/n
        partial+=power
    error=radius**(terms+1)/F(factorial(terms+1))/(1-radius/F(terms+2))
    return partial.widen(error)


def phase(z,X,Y,logX,liY):
    numerator=dilogarithm(X)-dilogarithm(X*Y)-C(PI.square()/2)+3*liY
    return (1-z)*logX+numerator/(2*IM*C(PI))+2*IM*C(PI)*(z*z-z)


def run():
    t=sp.symbols("t")
    polynomial=(t-2)**2*(t*t-2*t+2)+2*sp.I
    center=sp.Rational(943582111384816,10**15)-sp.I*sp.Rational(1303235290550143,10**15)
    radius=sp.Rational(1,10**14)
    coefficients=[sp.expand(sp.diff(polynomial,t,k).subs(t,center)/sp.factorial(k))
                  for k in range(5)]
    l1=lambda z:abs(sp.re(z))+abs(sp.im(z))
    linf=lambda z:max(abs(sp.re(z)),abs(sp.im(z)))
    margin=radius*linf(coefficients[1])-l1(coefficients[0])-sum(
        radius**k*l1(coefficients[k]) for k in range(2,5))
    assert margin>0
    # This disk lies inside the previously isolated selected geometric disk.
    assert l1(center-(sp.Rational(944,1000)-sp.I*sp.Rational(1303,1000)))+radius<sp.Rational(1,1000)
    tr=F(943582111384816,10**15)
    ti=-F(1303235290550143,10**15)
    eps=F(1,10**14)
    tau=C(R(tr-eps,tr+eps),R(ti-eps,ti+eps))
    X=((tau-F(3,2))**2+F(3,4)).inverse()
    Y=tau.inverse()
    symbolic_X=1/(t*t-3*t+3)
    symbolic_Y=1/t
    assert sp.cancel((1-3*symbolic_X)*symbolic_Y**2
                     +3*symbolic_X*symbolic_Y-symbolic_X)==0
    normX=X.re.square()+X.im.square()
    assert F(31,50)**2<normX.lo and normX.hi<F(16,25)**2
    assert X.im.hi<0 and X.re.hi<0
    logX=logarithm(IM*X)-IM*C(PI/2)
    logY=logarithm(Y)
    z=logY/(2*IM*C(PI))
    assert -2<logX.im.lo and logX.im.hi<F(-39,20)
    assert F(7,50)<z.re.lo and z.re.hi<F(4,25)
    assert F(3,40)<z.im.lo and z.im.hi<F(19,250)
    main=phase(z,X,Y,logX,dilogarithm(Y))
    assert main.re.lo>F(1,20)
    gradient=(-logX+logarithm(1-X*Y)-3*logarithm(1-Y)
              +2*logY-2*IM*C(PI))
    # The exact quadratic gives exp(gradient)=1; this interval selects
    # the zero logarithmic lift rather than another multiple of 2 pi i.
    assert -F(1,1000)<gradient.im.lo and gradient.im.hi<F(1,1000)
    assert -F(1,1000)<gradient.re.lo and gradient.re.hi<F(1,1000)

    # Rational equality of the squared amplitudes; the interval signs
    # below select the same square root for the actual Gaussian contour.
    rr=t*t-3*t+3
    symbolic_lam=-(t-2)**3/rr
    symbolic_mu=(t-1)**3/rr
    dd=2-symbolic_X-1/symbolic_X
    saddle_den=(2+3*symbolic_Y/(1-symbolic_Y)
                -symbolic_X*symbolic_Y/(1-symbolic_X*symbolic_Y))
    amplitude_square=(-symbolic_Y**2*(1-symbolic_X)
        /(symbolic_X**2*(1-symbolic_Y)**3*(1-symbolic_X*symbolic_Y)*saddle_den))
    expected_square=symbolic_lam/((symbolic_lam-symbolic_mu)*symbolic_X**2*dd)
    assert sp.cancel(amplitude_square-expected_square)==0
    x=-logX/(2*IM*C(PI))
    sin2x=(exponential(IM*C(PI)*x)-exponential(-IM*C(PI)*x))/IM
    sin2z=(exponential(IM*C(PI)*z)-exponential(-IM*C(PI)*z))/IM
    lam=-(tau-2)**3*X
    mu=(tau-1)**3*X
    second=2*IM*C(PI)*(2+3*Y/(1-Y)-X*Y/(1-X*Y))
    logB=(IM*C(PI)*z/2-logX-F(3,2)*logarithm(sin2z)
          +(logarithm(1-X)-logarithm(1-X*Y))/2
          +(logarithm(C(2*PI))-logarithm(-second))/2)
    logExpected=(logarithm(lam)-logarithm(lam-mu))/2-logX-logarithm(sin2x)
    B=exponential(logB)
    expectedB=exponential(logExpected)
    assert B.im.lo>F(4,5) and expectedB.im.lo>F(4,5)

    # At the right real cutoff, transform Li_2 from the unit circle to
    # a disk of radius <1, retaining the principal logarithm.
    cutoff=C(F(3,10))
    boundaryY=exponential(2*IM*C(PI)*cutoff)
    transformed=boundaryY/(boundaryY-1)
    li_boundary=-dilogarithm(transformed)-logarithm(1-boundaryY)**2/2
    boundary=phase(cutoff,X,boundaryY,logX,li_boundary)
    assert boundary.re.hi<0

    scalar_checks={
        "X_modulus_squared":normX.record(),
        "arg_X":logX.im.record(),
        "selected_saddle":z.record(),
        "selected_action":main.record(),
        "selected_logarithmic_gradient":gradient.record(),
        "gaussian_amplitude":B.record(),
        "continued_recurrence_amplitude":expectedB.record(),
        "right_real_cutoff_action":boundary.record(),
    }
    return {
        "status":"passed",
        "method":"Rational outward intervals and explicit power-series tails",
        "rounding_denominator":str(DEN),
        "root_center":[str(tr),str(ti)],
        "root_radius":str(eps),
        "rouche_margin":str(margin),
        "selected_inverse_clock":X.record(),
        "selected_exponentiated_saddle":Y.record(),
        "certificates":scalar_checks,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-next-crossing-complex-phase.json")
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("All rational contour-phase certificates passed.")
    print(f"Saved {args.output}")
