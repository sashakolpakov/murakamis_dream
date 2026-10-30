#!/usr/bin/env python3
"""Analytic cancellation identities and actual-source interpolation diagnostics.

The proof uses exact analytic functions on nested disks. The finite Cauchy
polynomial projections used here are numerical diagnostics, not an extra
premise of that analytic theorem.
"""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_positive_face_channel_rate import continuants, forced, sine_factorials


def symbolic():
    z,h,tp,tm,Fp,Fm,Gp,Gm=sp.symbols('z h tp tm Fp Fm Gp Gm')
    a=z-h/2;b=z+h/2
    numerator=(b*tp*(a*a*Fm+a*Gm)+a*tm*(b*b*Fp-b*Gp))
    divided=(tp*Fm+tm*Fp+h/(2*z)*(tm*Fp-tp*Fm)+(tp*Gm-tm*Gp)/z)
    assert sp.factor(numerator-z*a*b*divided)==0
    w,B,C,v=sp.symbols('w B C v')
    F=B*(sp.cosh(z*v)-1)/(z*z)+C*sp.sinh(z*v)/z
    G=C*(sp.cosh(z*v)-1)+B*sp.sinh(z*v)/z
    assert sp.simplify(sp.diff(F,v).subs(v,0)-C)==0
    assert sp.simplify(sp.diff(G,v).subs(v,0)-B)==0
    t=sp.symbols('t')
    for k in range(17):
        average=sp.integrate((z+t)**k,(t,-h/2,h/2))/h
        exact=sum(sp.binomial(k,2*r)*z**(k-2*r)*h**(2*r)/(2**(2*r)*(2*r+1)) for r in range(k//2+1))
        assert sp.expand(average-exact)==0
    return {'cleared_single_loss_decomposition':1,'pointwise_linearizations':2,
            'exact_centered_polynomial_averages':17}


def horner(coeff,w):
    result=mp.mpc(0)
    for c in reversed(coeff):result=result*w+c
    return result


def cauchy_series(fun,r,degree,nodes=None):
    nodes=nodes or 2*degree+8
    roots=[mp.exp(2j*mp.pi*j/nodes) for j in range(nodes)]
    values=[fun(r*z) for z in roots]
    return [mp.fsum(values[j]*roots[j]**(-k) for j in range(nodes))/nodes/r**k for k in range(degree+1)]


class PivotModel:
    def __init__(self,N,x,b,y,degree=24):
        self.N=N;self.h=1/mp.mpf(N);self.x=x;self.b=b;self.y=y;self.A=x+y
        self.T2=b*self.A+x*y;self.degree=degree
        self.coeff=[mp.mpc(0)];self.residuals=[]
        if self.T2==0:return
        r=mp.mpf('.04')
        coeff=cauchy_series(lambda w:self.h*self.correction(mp.sqrt(w))/mp.sqrt(w),r,degree)
        while r-2*self.h>mp.mpf('.01'):
            newr=r-2*self.h;old=coeff
            coeff=cauchy_series(lambda w:horner(old,w)-self.G(old,w)/self.L(w),newr,degree)
            r=newr
            self.residuals.append(max(abs(self.G(coeff,mp.mpf('.006')*mp.exp(2j*mp.pi*j/7))) for j in range(7)))
        self.coeff=coeff

    def E(self,z):
        if self.T2==0:return self.A
        s=mp.sin(mp.pi*z)
        return self.A+2*self.b*s*s+2*s*mp.sqrt(self.T2+self.b*self.b*s*s)

    def J(self,z):
        if self.T2==0:return mp.mpf(1)
        return mp.cos(mp.pi*z)*mp.sqrt(self.T2+self.b*self.b*mp.sin(mp.pi*z)**2)/mp.sqrt(self.T2)

    def correction(self,z):
        if self.T2==0:return mp.mpf(0)
        s,c=mp.sin(mp.pi*z),mp.cos(mp.pi*z)
        return mp.pi/2*(-s/c+self.b*self.b*s*c/(self.T2+self.b*self.b*s*s))

    def L(self,w):
        z=mp.sqrt(w)
        return mp.tan(mp.pi*z)*(self.E(z)-self.E(-z))/w

    def G(self,coeff,w):
        z=mp.sqrt(w);a=z-self.h/2;b=z+self.h/2
        e=lambda zz:self.E(zz)*mp.exp(zz*horner(coeff,zz*zz))
        numerator=(mp.tan(mp.pi*b)*e(a)+mp.tan(mp.pi*a)*e(-b)
                   -(mp.tan(mp.pi*b)+mp.tan(mp.pi*a))
                    *(self.A+2*self.b*mp.sin(mp.pi*a)*mp.sin(mp.pi*b)))
        return numerator/(z*a*b)

    def value(self,z):
        return self.E(z)*mp.exp(z*horner(self.coeff,z*z))


def exact_decomposition():
    count=0;worst=mp.mpf(0)
    for N in (128,257):
        h=1/mp.mpf(N);x,b,y=mp.mpf('1.3'),mp.mpc('.7','.013'),mp.mpf('2.1');A=x+y;T2=b*A+x*y
        E=lambda z:A+2*b*mp.sin(mp.pi*z)**2+2*mp.sin(mp.pi*z)*mp.sqrt(T2+b*b*mp.sin(mp.pi*z)**2)
        B0=lambda w:A+2*b*mp.sin(mp.pi*mp.sqrt(w))**2
        C0=lambda w:(E(mp.sqrt(w))-E(-mp.sqrt(w)))/(2*mp.sqrt(w))
        t=lambda w:mp.tan(mp.pi*mp.sqrt(w))/mp.sqrt(w)
        v=lambda w:h*(mp.mpc('.2','.1')+w+3*w*w)
        FF=lambda w:B0(w)*(mp.cosh(mp.sqrt(w)*v(w))-1)/w+C0(w)*mp.sinh(mp.sqrt(w)*v(w))/mp.sqrt(w)
        GG=lambda w:C0(w)*(mp.cosh(mp.sqrt(w)*v(w))-1)+B0(w)*mp.sinh(mp.sqrt(w)*v(w))/mp.sqrt(w)
        for j in range(12):
            w=mp.mpf('.02')*mp.exp(2j*mp.pi*j/12);z=mp.sqrt(w);aa=z-h/2;bb=z+h/2;wm=aa*aa;wp=bb*bb
            def residual(vv):
                e=lambda zz:E(zz)*mp.exp(zz*vv(zz*zz))
                return (mp.tan(mp.pi*bb)*e(aa)+mp.tan(mp.pi*aa)*e(-bb)
                        -(mp.tan(mp.pi*bb)+mp.tan(mp.pi*aa))*(A+2*b*mp.sin(mp.pi*aa)*mp.sin(mp.pi*bb)))/(z*aa*bb)
            direct=residual(v)-residual(lambda w:0)
            expected=(t(wp)*FF(wm)+t(wm)*FF(wp)+h/(2*z)*(t(wm)*FF(wp)-t(wp)*FF(wm))
                      +(t(wp)*GG(wm)-t(wm)*GG(wp))/z)
            error=abs(direct-expected);worst=max(worst,error)
            assert error<mp.mpf('1e-55');count+=1
    return {'complex_face_single_loss_identities':count,'maximum_absolute_error':str(worst)}


def pivot_diagnostics():
    rows=[]
    for N in (128,256,512,1024):
        x,b,y=map(mp.mpf,['1.3','.7','2.1'])
        model=PivotModel(N,x,b,y)
        M=(N-1)//2;S=sine_factorials(N);D=continuants(N,M,x,b,y)
        errors=[]
        for a in [M,M-int(N*mp.mpf('.02')),M-int(N*mp.mpf('.04'))]:
            z=(mp.mpf(N)/2-a)/N
            actual=(S[2*a]/S[a]**2*D[a])/(S[2*a-2]/S[a-1]**2*D[a-1])
            errors.append(abs(actual/model.value(z)-1))
        assert max(errors)<mp.mpf('1e-5')
        rows.append({'N':N,'analytic_correction_steps':len(model.residuals),
                     'final_sampled_residual':str(model.residuals[-1]),
                     'maximum_actual_pivot_relative_error':str(max(errors))})
    return rows


def average(coeff,h):
    result=[mp.mpc(0)]*len(coeff)
    for k,c in enumerate(coeff):
        for r in range(k//2+1):
            result[k-2*r]+=c*math.comb(k,2*r)*h**(2*r)/(mp.mpf(2)**(2*r)*(2*r+1))
    return result


def circle_diagnostics():
    rows=[]
    for N,complex_faces in ((256,False),(257,False),(512,True),(513,True)):
        x,b,c,y=map(mp.mpf,['1.3','.7','1.9','2.1'])
        if complex_faces:
            x*=mp.exp(mp.mpc('.0002','.0001'))
            b*=mp.exp(mp.mpc('-.0001','.0002'))
            c*=mp.exp(mp.mpc('.0001','-.0001'))
        mb=PivotModel(N,x,b,y);mc=PivotModel(N,x,c,y)
        h=1/mp.mpf(N);M=(N-1)//2;s0=N-1-2*M
        Dfun=lambda z:(x+y)**2-4*x*y*mp.sin(mp.pi*z)**2
        ell=lambda z:mp.log(mb.value(z)*mc.value(z)/Dfun(z))
        coeff=cauchy_series(ell,mp.mpf('.07'),48,nodes=112)
        # Preserve the exact odd symmetry of the analytic construction.
        for j in range(0,len(coeff),2):coeff[j]=mp.mpc(0)
        mcoeff=coeff[:]
        # On polynomials A_h-I lowers degree by2, so this finite Neumann
        # inversion is exact up to arithmetic precision.
        for _ in range((len(coeff)+1)//2):
            am=average(mcoeff,h)
            mcoeff=[v+target-got for v,target,got in zip(mcoeff,coeff,am)]
        residual=max(abs(a-b) for a,b in zip(average(mcoeff,h),coeff))
        assert residual<mp.mpf('1e-50')
        H=lambda z:-mp.fsum(v*z**(j+1)/(j+1)/h for j,v in enumerate(mcoeff))
        S=sine_factorials(N);Db=continuants(N,M,x,b,y);Dc=continuants(N,M,x,c,y)
        def B(a):return (S[2*a]/S[a]**2)**2*Db[a]*Dc[a]*forced(N,a,x,y)
        d0=mp.mpf(s0)/(2*N)
        for t in (int(N*mp.mpf('.02')),int(N*mp.mpf('.04'))):
            a=M-t;delta=mp.mpf(s0+2*t)/(2*N)
            expected=mp.exp(H(delta)-H(d0));actual=B(a)/B(M)
            error=abs(actual/expected-1)
            assert error<mp.mpf('1e-7')
            rows.append({'N':N,'complex_face_parameters':complex_faces,'t':t,
                         'actual_circle_relative_error':str(error),
                         'centered_polynomial_inverse_residual':str(residual)})
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_positive_face_exponential_fold_interpolation_results.json');args=ap.parse_args()
    mp.mp.dps=65
    data={'status':'PASS','precision_digits':65,'symbolic':symbolic(),
          'analytic_identity':exact_decomposition(),'pivot_prototypes':pivot_diagnostics(),
          'original_circle_prototypes':circle_diagnostics(),
          'scope':'Exact algebra of the regularized single-loss operator and centered polynomial averages; numerical Cauchy-polynomial prototypes compared with ORIGINAL beta/D/P factors, including fixed complex faces and both parity anchors. Prototypes diagnose the construction; the uniform exponential estimates are the analytic theorem, not inferred from sampled convergence.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))


if __name__=='__main__':main()
