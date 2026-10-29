#!/usr/bin/env python3
"""Exact cubic-field Bloch identities and independent marked-action diagnostic."""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp
v=sp.symbols("v"); p=v**3-v**2+1
def red(expr):
    a,b=sp.cancel(expr).as_numer_denom()
    return sp.rem(a*sp.invert(b,p,v),p,v).expand()
X=1/(1+v*v);Y=-v;Z=X/Y;A=v*(1+v)/(1+v*v)
identities=[
    1-v-v**-2,
    v**5+1+v,
    -v**4-(-v-1)/(-v),
    A-v**8/(v**8-1),
    -v*(1-v)/(1+v*v)-Z,
    (1-X)**3-X**2*Y*(1-Z),
    1-Z-X*(1-Y),
]
assert all(red(t)==0 for t in identities)
r=sp.symbols("r")
f=lambda q:q**3+q*q-1
assert f(sp.Rational(7548,10000))<0<f(sp.Rational(7549,10000))
mp.mp.dps=75
rho=mp.findroot(lambda q:q**3+q*q-1,(mp.mpf(".75"),mp.mpf(".76")))
vv=(1+rho)/2+1j*mp.sqrt(1/rho-(1+rho)**2/4)
xx=1/(1+vv*vv);yy=-vv;zz=xx/yy
x=1+mp.log(xx)/(2j*mp.pi);y=1+mp.log(yy)/(2j*mp.pi)
J=lambda z:(mp.polylog(2,1)-mp.polylog(2,mp.exp(2j*mp.pi*z)))/(2j*mp.pi)-.5j*mp.pi*z*z+.5j*mp.pi*z
S=3*J(x)-J(y)-J(x-y)+1j*mp.pi*(3*x+2*y-x*x-x*y-y*y)
gx=3*mp.log(1-xx)-mp.log(1-zz)-4j*mp.pi*x-2j*mp.pi*y+4j*mp.pi
gy=-mp.log(1-yy)+mp.log(1-zz)-2j*mp.pi*x+2j*mp.pi
D=lambda z:mp.im(mp.polylog(2,z))+mp.log(abs(z))*mp.arg(1-z)
theta=mp.arg(vv);angles=[mp.pi-3*theta,2*theta,theta]
assert min(angles)>0
assert abs(mp.sin(angles[0])**3-mp.sin(angles[1])**2*mp.sin(angles[2]))<mp.mpf("1e-65")
regulator=-3*D(xx)+D(yy)+D(zz)
assert max(abs(gx),abs(gy),abs(2*mp.pi*S.real-regulator),abs(regulator-3*D(vv)))<mp.mpf("1e-65")
result={"status":"PASS","exact_field_identities":len(identities),
        "rho_isolation":["7548/10000","7549/10000"],
        "marked_stationary_residual":float(max(abs(gx),abs(gy))),
        "critical_rate":mp.nstr(S.real,65),
        "three_tetrahedron_volume":mp.nstr(3*D(vv),65),
        "positive_angles":[mp.nstr(a,30) for a in angles],
        "scope":"Exact Bloch calibration plus independently audited classical three-tetrahedron geometry; selected quantum contour is separate."}
out=Path(__file__).with_name("five_two_selected_bloch_calibration_results.json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
if __name__=="__main__":pass

