#!/usr/bin/env python3
"""Rational certificates for an abstract algebraic-pressure obstruction.

Every asserted bound below uses Fraction arithmetic and alternating-series
or positive-series remainder bounds. No floating-point result is a premise.
This does not construct a knot source or test a Kashaev invariant.
"""
from fractions import Fraction as F
import json

if not __debug__:
    raise RuntimeError("Assertions must remain enabled")

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other=box(other); return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other): return self+-box(other)
    def __rsub__(self, other): return box(other)+-self
    def __mul__(self, other):
        other=box(other)
        v=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self, other):
        other=box(other); assert not other.lo <= 0 <= other.hi
        return self*I(1/other.hi,1/other.lo)
    def __rtruediv__(self, other): return box(other)/self
    def inside(self, lo, hi):
        assert F(lo)<self.lo and self.hi<F(hi), (self.lo,self.hi,lo,hi)
    def record(self):
        return {"lower":str(self.lo),"upper":str(self.hi),
                "decimal_display_only":[float(self.lo),float(self.hi)]}

def box(x): return x if isinstance(x,I) else I(x)

def alternating(x, power, terms=48):
    x=F(x); assert 0 <= x < 1
    s=sum(((-1)**k*x**(2*k+1)/F((2*k+1)**power)
           for k in range(terms)),F(0))
    t=(-1)**terms*x**(2*terms+1)/F((2*terms+1)**power)
    return I(min(s,s+t),max(s,s+t))

def atan(x): return alternating(x,1)
def ti(x): return alternating(x,2)

def log_rational(x, terms=48):
    x=F(x); assert x>=1
    y=(x-1)/(x+1)
    s=2*sum((y**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    tail=2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
    return I(s,s+tail)

pi=16*atan(F(1,5))-4*atan(F(1,239))
pi.inside(F(25,8),F(22,7))
ln2=log_rational(2)
ln2.inside(F(2,3),F(7,10))
eps=F(1,16)
C=4/pi*ti(eps)
C.inside(0,F(2,25))

# z=log w=2 log t. The formula uses Ti2(x)-Ti2(1/x)=pi log(x)/2.
def value_at(t):
    t=F(t); assert 1<t<16
    return (-log_rational(t)/3+4/(3*pi)*ti(eps/t)
            +8/(3*pi)*ti(eps*t)+2/pi*ti(1/t)-C)

def derivative_at(t):
    t=F(t)
    return -F(1,6)+4/(3*pi)*atan(eps*t)-2/(3*pi)*atan(eps/t)-atan(1/t)/pi

# Using log 8=3 log 2 is both exact and gives a shorter rational certificate.
v8=-ln2+4/(3*pi)*ti(F(1,128))+8/(3*pi)*ti(F(1,2))+2/pi*ti(F(1,8))-C
d8=derivative_at(8); d9=derivative_at(9)
v8.inside(-F(277,1000),-F(276,1000))
d8.inside(-F(12,1000),-F(11,1000))
d9.inside(F(14,1000),F(15,1000))
width=2*log_rational(F(9,8))
lower_tangent=v8+d8*width
lower_tangent.inside(-F(28,100),-F(27,100))
# Strict convexity brackets the unique minimum between t=8 and t=9.
# Hence 27/100 < D=-min V < 28/100, whereas chi=C<2/25.
assert v8.hi < -F(27,100)
assert lower_tangent.lo > -F(28,100)

nu=F(1,3)+2/(3*pi)*atan(eps)
kappa=16/(257*pi)
nu.inside(F(1,3),F(7,20))
kappa.inside(F(19,1000),F(21,1000))
assert kappa.hi < (nu*(1-nu)).lo

# alpha=asin(sqrt(2) cos(pi nu)) > 7/10, using rational Taylor bounds.
cos_lower=F(1,2)-F(1,2304)-F(7,192)
sin_upper=F(7,10)-F(7,10)**3/6+F(7,10)**5/120
assert F(7,5)*cos_lower>sin_upper
assert 1-F(7,10)**2/2>F(3,4)
# W/pi > (7/5pi) asinh(3/4)=(7/5pi) log2 >49/165.
assert F(49,165)>F(28,100)+F(1,100)

out={
 "scope":"Abstract algebraic boundary pressure; not a realized knot source",
 "arithmetic":"Exact rational interval certificates; decimals are display only",
 "epsilon":str(eps), "pi":pi.record(), "loss_chi":C.record(),
 "value_at_t8":v8.record(), "derivative_at_t8":d8.record(),
 "derivative_at_t9":d9.record(), "minimum_lower_tangent":lower_tangent.record(),
 "nu":nu.record(), "kappa":kappa.record(),
 "certified_deficit_interval":["27/100","28/100"],
 "certified_pyramid_budget_lower":"49/165",
 "strict_budget_slack_lower":"1/100",
 "failed_comparison_margin_lower":"19/100"
}
print(json.dumps(out,indent=2))
