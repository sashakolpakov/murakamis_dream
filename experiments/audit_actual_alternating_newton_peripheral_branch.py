#!/usr/bin/env python3
"""Focused checks of the retained Newton critical scheme and primitive collar.

Exact identities supplement the analytical proof. Literal finite coefficient
ratios retain all offsets; the unsquared collar checks distinguish its marked
branch from trace-square elimination. This audit proves no contour statement.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def exact_checks():
    x,b,c,y,U,Z,A,B,W,k,t,z,u=sp.symbols('x b c y U Z A B W k t z u')
    C=(Z-A)*(Z-B)
    raw=(Z*W-A*B)*(Z-W)*((W+1)**2-k*W)+Z*(W-A)*(W-B)*(W+1)**2
    quad=C*(W+1)**2+k*(W-Z)*(Z*W-A*B)
    checks=[]
    def check(expr):
        assert sp.factor(expr)==0
        checks.append(True)
    check(raw-W*quad)
    check(sp.discriminant(quad,W)-k*(k*(Z**2-A*B)**2-4*C*(Z+1)*(Z+A*B)))
    L=b+c+x+y;D=x*y-b*c;E=b*c*(x+y)+(b+c)*x*y;aa=x+y
    subst={A:(x*W+t)/(x+t), B:(y*W+t)/(y+t), Z:(t-c*W)/(t-c)}
    f1=b*(Z-1)*(Z*W-A*B)-c*(Z-W)*(Z-A*B)
    f2=x*(Z-A*B)*(W-A)-b*(Z*W-A*B)*(A-1)
    f3=y*(Z-A*B)*(W-B)-b*(Z*W-A*B)*(B-1)
    q1=L*t*t+(1+W)*D*t-W*E
    for f in (f1,f2,f3):
        num=sp.fraction(sp.cancel(f.subs(subst)))[0]
        check(sp.rem(num,q1,t))
    check(L*E+D**2-(b+x)*(b+y)*(c+x)*(c+y))
    rho=k*(t-c)*(t-c*W)+(c+x)*(c+y)*((W+1)**2-k*W)
    wr=t*(L*t+D)/(E-D*t)
    check(sp.cancel((E-D*t)**2*rho.subs(W,wr))-(c+x)*(c+y)*((L*t*t+E)**2-k*t*(t+x)*(t+y)*(E-D*t)))
    check(L*rho-k*q1-(c+x)*(c+y)*(-k*(1+W)*t+L*(W+1)**2-k*aa*W))
    reverse=L*(W+1)/k-aa*W/(W+1)
    rz=(L*L+k*D)*(W+1)**4-k*(2*L*aa+k*x*y)*(W+1)**2*W+k*k*aa*aa*W*W
    check(sp.resultant(q1,rho,t)-(c+x)**2*(c+y)**2*rz)
    check(sp.cancel(q1.subs(t,reverse)*k*k*(W+1)**2)-L*rz)
    p=(L*L+k*D)*z*z-(2*L*aa+k*x*y)*z+aa*aa
    check(sp.discriminant(p,z)-k*(4*aa*E+k*x*x*y*y))
    check(p.subs(z,1)-((b+c)**2-k*b*c))
    check(p.subs(z,aa/L)+k*aa*E/(L*L))
    dg=aa*aa-4*x*y*u;tb=b*aa+x*y+b*b*u;tc=c*aa+x*y+c*c*u
    collar=(k*dg-2*dg-2*(aa+2*b*u)*(aa+2*c*u))**2-64*u*u*tb*tc
    pc=16*((b+c)**2-k*b*c)*u*u-4*(k-4)*(2*aa*(b+c)+k*x*y)*u+(k-4)**2*aa*aa
    check(collar-dg*pc)
    check(sp.cancel(pc.subs(u,(k-4)*z/(4*(1-z)))*(1-z)**2/(k-4)**2)-p)
    return len(checks)


def source_ratio_checks():
    largest=mp.mpf(0);counts=0;errors=[]
    cases=[(8,2,12,1,1),(9,4,14,2,1),(9,5,13,2,2)]
    for N in (80,160,320,640):
        sf=[mp.mpf(1)]
        for j in range(1,N): sf.append(sf[-1]*2*mp.sin(mp.pi*j/N))
        def bino(n,r):return sf[n]/(sf[r]*sf[n-r])
        for hh,rr,mm,ii,jj in cases:
            h,r,m,i,j=[n*N//20 for n in (hh,rr,mm,ii,jj)]
            def literal(r,hh=h):
                bh=sf[r]**2*sf[hh+r]/(sf[2*r+1]*sf[hh-r-1])
                return (-1)**(hh-1+r)*bh*bino(m,r)*bino(m+r-i-j,r)*bino(r,i)*bino(r,j)
            ratio=literal(r+1)/literal(r)
            sine=lambda n:2*mp.sin(mp.pi*n/N)
            telescoped=-(sine(r+1)**2*sine(h+r+1)*sine(h-r-1)*sine(m+r-i-j+1)*sine(m-r))/(sine(2*r+2)*sine(2*r+3)*sine(r-i+1)*sine(r-j+1))
            assert abs(ratio/telescoped-1)<mp.mpf('1e-75')
            external=literal(r,h+1)/literal(r,h)
            assert abs(external/(-sine(h+r+1)/sine(h-r))-1)<mp.mpf('1e-75')
            alpha,rho,mu,xi,eta=[mp.mpf(n)/N for n in (h,r,m,i,j)]
            ss=lambda v:mp.sin(mp.pi*v)
            pred=-ss(mu+rho-xi-eta)*ss(mu-rho)/(ss(rho-xi)*ss(rho-eta))*(ss(alpha)**2-ss(rho)**2)/mp.cos(mp.pi*rho)**2
            assert ratio<0 and pred<0
            err=abs(ratio/pred-1);largest=max(largest,N*err);errors.append(err);counts+=1
            assert N*err<100
    # The same physical fractions at increasing levels genuinely approach the
    # predicted signed ratio; no polynomial elimination is used here.
    for j in range(3): assert errors[j]>errors[j+3]>errors[j+6]>errors[j+9]
    return counts,largest


def branch_checks():
    quartets=[(1,1,1,1),(2,3,5,7),(4,9,1,1),(mp.mpf('0.3'),mp.mpf('1.1'),mp.mpf('2.7'),mp.mpf('0.8'))]
    residual=mp.mpf(0);count=0;reconstructed=0;near=0
    def record(v):
        nonlocal residual
        residual=max(residual,abs(v));assert abs(v)<mp.mpf('1e-65')
    for x,b,c,y in quartets:
        x,b,c,y=map(mp.mpf,(x,b,c,y));aa=x+y;L=aa+b+c;D=x*y-b*c;E=b*c*aa+(b+c)*x*y
        for alpha in map(mp.mpf,('0.005','0.025','0.08','0.2','0.43')):
            kap=4*mp.cos(mp.pi*alpha)**2;lead=L*L+kap*D;mid=2*L*aa+kap*x*y
            dis=kap*(4*aa*E+kap*x*x*y*y)
            zz=[2*aa*aa/(mid+mp.sqrt(dis)),(mid+mp.sqrt(dis))/(2*lead)]
            assert 0<zz[0]<zz[1]<1
            for z in zz:
                rho=mp.acos(mp.sqrt(z)*mp.cos(mp.pi*alpha))/mp.pi
                assert alpha<rho<mp.mpf('.5')
                W=mp.exp(2j*mp.pi*rho)
                qlin=D*(1+W)
                ts=[(-qlin+s*mp.sqrt(qlin**2+4*L*W*E))/(2*L) for s in (1,-1)]
                tr=min(ts,key=lambda t:abs(kap*(t-c)*(t-c*W)+(c+x)*(c+y)*((W+1)**2-kap*W)))
                record(tr-W*(L*z-aa)/(W+1))
                A=(x*W+tr)/(x+tr);B=(y*W+tr)/(y+tr);Z=(tr-c*W)/(tr-c)
                units=[Z,A,B,W,Z-1,Z-W,Z-A*B,Z*W-A*B,A-1,B-1,W-A,W-B,W-1,W+1,W-mp.exp(2j*mp.pi*alpha),W-mp.exp(-2j*mp.pi*alpha),E-D*tr,(c+x)*(c+y)]
                if min(abs(v) for v in units)<mp.mpf('1e-50'):continue
                mu,xi,eta=[mp.log(v)/(2j*mp.pi) for v in (Z,A,B)]
                ss=lambda a:mp.sin(mp.pi*a)
                record(b/c*ss(mu)*ss(mu+rho-xi-eta)/(ss(mu-rho)*ss(mu-xi-eta))-1)
                record(x/b*ss(mu-xi-eta)*ss(rho-xi)/(ss(mu+rho-xi-eta)*ss(xi))-1)
                record(y/b*ss(mu-xi-eta)*ss(rho-eta)/(ss(mu+rho-xi-eta)*ss(eta))-1)
                record(ss(mu+rho-xi-eta)*ss(mu-rho)/(ss(rho-xi)*ss(rho-eta))*(ss(alpha)**2-ss(rho)**2)/mp.cos(mp.pi*rho)**2+1)
                reconstructed+=1
            # UNSQUARED actual marked collar, smaller root and M -> 1.
            u=(kap-4)*zz[0]/(4*(1-zz[0]));delta=1j*mp.asinh(mp.sqrt(-u))/mp.pi
            sn=mp.sin(mp.pi*delta);dg=aa*aa-4*x*y*sn*sn
            tb=mp.sqrt(b*aa+x*y+b*b*sn*sn);tc=mp.sqrt(c*aa+x*y+c*c*sn*sn)
            eb=aa+2*b*sn*sn+2*sn*tb;ec=aa+2*c*sn*sn+2*sn*tc
            R0=eb*ec/dg
            record(R0-mp.exp(2j*mp.pi*alpha));record(mp.exp(-mp.pi*1j*alpha)**2*R0-1)
            rho0=mp.acos(mp.sqrt(zz[0])*mp.cos(mp.pi*alpha))/mp.pi
            momentum=lambda rr:-mp.sin(mp.pi*(alpha+rr))/mp.sin(mp.pi*(alpha-rr))
            record(momentum(1-rho0)-mp.exp(2j*mp.pi*delta))
            record(momentum(rho0)*mp.exp(2j*mp.pi*delta)-1)
            count+=1
        alpha=mp.mpf('1e-8');kap=4*mp.cos(mp.pi*alpha)**2;mid=2*L*aa+kap*x*y
        z=2*aa*aa/(mid+mp.sqrt(kap*(4*aa*E+kap*x*x*y*y)))
        u=(kap-4)*z/(4*(1-z));delta=1j*mp.asinh(mp.sqrt(-u))/mp.pi
        pred=1j*alpha*aa/(mp.sqrt(b*aa+x*y)+mp.sqrt(c*aa+x*y))
        assert abs(delta/pred-1)<mp.mpf('1e-13');near+=1
    return count,reconstructed,near,residual


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_alternating_newton_peripheral_branch_results.json'));args=parser.parse_args()
    mp.mp.dps=85
    exact=exact_checks();ratios,ratioerr=source_ratio_checks();collars,reconstructed,near,err=branch_checks()
    result={'status':'PASS','precision':mp.mp.dps,'exact_symbolic_identities':exact,'literal_signed_finite_ratios':ratios,'exact_finite_ratio_telescopings':ratios,'exact_external_ratio_telescopings':ratios,'unsquared_marked_collars':collars,'reciprocal_external_momentum_pairs':collars,'uncleared_shared_face_reconstructions':reconstructed,'reverse_branch_reconstructions':reconstructed,'selected_complete_germ_checks':near,'max_N_times_ratio_error':mp.nstr(ratioerr,25),'max_uncleared_or_collar_residual':mp.nstr(err,25),'scope':'Exact local scheme and selected collar comparison; no finite-sum contour, endpoint, global contribution, or source asymptotic.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
