#!/usr/bin/env python3
"""Exact outer positivity identities and diagnostics of the proved curve."""

import json
from pathlib import Path

import mpmath as mp
import sympy as S


def identities():
    a,b,r,d,w,T=S.symbols('a b r d w T',real=True)
    v=a+S.I*b
    R=(v*v+v+4)*(v*v+v-1)/(1-v**4)
    numerator=S.expand(S.im(S.cancel(R))*S.expand_complex((1-v**4)*(1-S.conjugate(v)**4)))
    numerator=S.cancel(numerator/b)
    poly=S.Poly(S.expand(numerator),b)
    in_r=S.expand(sum(coef*(r-a*a)**(mon[0]//2) for mon,coef in poly.terms()))
    relation=r*r+(3-d)*r+1+2*a*(r-1)-4*a*a
    reduced=S.rem(in_r,relation,a)
    expected=a*(2*r*r+(6*d+4)*r-8)+2*r**3+2*r*r+(13-5*d)*r+8
    assert S.cancel(reduced-expected)==0
    L=expected.subs({a:w,r:w*w})
    L4=2*w**6+2*w**5+2*w**4+7*w*w*(4*w-1)+8*(1-w)
    L1=2*w**6+2*w**5+2*w**4+10*w**3+8*(w*w-w+1)
    assert S.expand(L.subs(d,4)-L4)==0
    assert S.expand(L.subs(d,1)-L1)==0
    vv=S.symbols('v')
    rational=(vv*vv+vv+4)*(vv*vv+vv-1)/(1-vv**4)
    TT=vv-1/vv;ss=vv+1/vv
    assert S.cancel(rational-(TT+1)/(2*TT)*((3*TT-2)/ss-5))==0
    assert S.Rational(63)**2 < S.Rational(31)**2*5
    return {'circle_reduced_ImR_numerator':True,'positive_endpoint_polynomials':True,
            'equivalent_T_Hessian_formula':True,'strict_negative_real_bound':True}


def branch(x):
    X=mp.exp(2*mp.pi*1j*x);T=1/X-1
    roots=((T+mp.sqrt(T*T+4))/2,(T-mp.sqrt(T*T+4))/2)
    v=next(v for v in roots if mp.re(v)>0)
    y=mp.mpf('.5')+mp.log(v)/(2*mp.pi*1j)
    R=(v*v+v+4)*(v*v+v-1)/(1-v**4)
    return v,y,R


def main():
    mp.mp.dps=50
    exact=identities()
    rho=mp.findroot(lambda r:r**3+r*r-1,.75)
    aa=(1+rho)/2;bb=mp.sqrt(1/rho-aa*aa);vg=aa+1j*bb
    Xg=1/(1+vg*vg);xg=1+mp.log(Xg)/(2*mp.pi*1j)
    yg=mp.mpf('.5')+mp.log(vg)/(2*mp.pi*1j)
    ug,eta=mp.re(xg),mp.im(xg);c=eta/(1-ug)
    f=lambda z:mp.log(2*mp.sin(mp.pi*z))
    J=lambda z:(mp.polylog(2,1)-mp.polylog(2,mp.exp(2*mp.pi*1j*z)))/(2*mp.pi*1j)-mp.pi*1j*(z*z-z)/2
    phase=lambda x,y:3*J(x)-J(y)-J(x-y)+mp.pi*1j*(3*x+2*y-x*x-x*y-y*y)
    gx=3*f(xg)-f(xg-yg)+mp.pi*1j*(3-2*xg-yg)
    gy=-f(yg)+f(xg-yg)+mp.pi*1j*(2-xg-2*yg)
    assert abs(gx)+abs(gy)<mp.mpf('1e-45')
    assert abs(abs(vg*vg)-1/rho)<mp.mpf('1e-45')
    horizontal=sloped=0
    max_phase=mp.re(phase(xg,yg))
    for h in range(9):
        hh=mp.log(2)/(2*mp.pi)*h/8
        for k in range(1,200):
            u=mp.mpf('.5')+mp.mpf('.5')*k/200
            _,_,R=branch(u+1j*hh)
            assert mp.im(R)>0
            horizontal+=1
    for k in range(1,200):
        u=ug+(1-ug)*k/200;x=u+1j*c*(1-u)
        _,y,R=branch(x)
        assert mp.re(R)<0 and mp.im(R)>0
        assert 2*c*mp.re(R)-(1-c*c)*mp.im(R)<0
        assert mp.re(phase(x,y))<max_phase
        sloped+=1
    result={'status':'PASS','exact_identities':exact,'horizontal_diagnostic_points':horizontal,
            'sloped_diagnostic_points':sloped,'rho':str(rho),'x_cubic':str(xg),'y_cubic':str(yg),
            'slope':str(c),'explicit_cubic_real_action':str(max_phase),
            'scope':'Proved reduced-outer maximum; original source contour and regulator calibration remain separate.'}
    Path(__file__).with_name('five_two_reduced_outer_concavity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
