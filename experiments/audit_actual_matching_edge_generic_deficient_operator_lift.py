#!/usr/bin/env python3
"""The literal exceptional generic germ, its marked root character, and normals."""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet,matrix
from audit_actual_matching_edge_polynomial_finite_propagation import source_polynomial
from audit_actual_matching_edge_antidiagonal_operator_packet import factorials,clebsch,cup
from audit_actual_q_hahn_small_channel_generic_normals import source_S
from audit_actual_q_hahn_joint_complex_amplitude import Source
from audit_exact_factorial_interpolation import factorial as root_factorial
from audit_actual_moving_period_factorial_normals import factorial as moving_factorial,period


def white(N,a,q,sigma,i,F):
    d=N-1;m=d-a;r=sigma-m;U=q**(2*i);T=q**(2*sigma)
    H=source_S(N,q,m,U,T)/U**m
    return (-1)**m*q**(-d*r+d*i-m*(m-1))*H/F[m]


def scalar(N,a,q):
    d=N-1;unit=lambda n:(q**n-q**(-n))/(q-q**-1)
    sf=[q**0]
    for n in range(1,d+1):sf.append(sf[-1]*unit(n))
    den=q**0
    for n in range(1,d+a+2):
        if n!=N:den*=unit(n)
    D=(-1)**a*sf[a]**2*sf[d-a]/den
    return N*N*q**(a*a-2*d*d)*sf[2*a]/sf[a]**2*D,D


def exact():
    e,x=sp.symbols('e x',real=True)
    delta=-1-e+sp.I*x;A2=-1-2/delta
    assert sp.simplify((sp.diff(A2,e)/A2).subs(e,0)+2/(1+x*x))==0
    reversals=entries=jets=0
    for N in range(3,10):
        p,e=root_field(N);q0=e*e%p;Jet.p=p;Jet.order=4
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        d=N-1;F=factorials(q,d)
        for a in range(d//2+1):
            m=d-a;s=d-2*a
            for r in range(2*a+1):
                sigma=m+r
                for i in range(max(0,sigma-d),min(d,sigma)+1):
                    j=sigma-i
                    left=clebsch(d,a,q,F,d-j,d-i,2*a-r)
                    right=q**(s*(a-r))*clebsch(d,a,q,F,i,j,r)
                    assert left==right;reversals+=1
        if N>7:continue
        for t in range(N):
            Dg,up,low=matrix(N,q,t)
            for v in range(t+1):
                vec=[Jet(int(k==v)) for k in range(t+1)]
                for a in range(d//2+1):
                    actual,_,_=source_polynomial(N,q,a,Dg,up,low,vec,Jet(3))
                    c,D=scalar(N,a,q)
                    for u in range(t+1):
                        h=v-u
                        if abs(h)>a:assert actual[u]==0;continue
                        sigma=d-h;r=a-h;ell=t-v;s=d-2*a
                        expected=(c*q**(s*h)*white(N,a,q,sigma,sigma-u,F)
                                  *white(N,a,q,sigma,ell,F)*cup(2*a,q,F,r)
                                  /((-1)**d*q**(-d+2*v)
                                    *cup(d,q,F,v,N*q**(-d*d))
                                    *cup(d,q,F,ell,N*q**(-d*d))))
                        assert actual[u]==expected,(N,a,t,u,v)
                        assert actual[u]/D==expected/D
                        entries+=1;jets+=int(any(actual[u].c[1:]))
    return dict(actual_high_adapter_four_jets=reversals,
                original_completed_polynomial_four_jets=entries,
                nonzero_retained_generic_jet_entries=jets,
                exact_actual_nonreal_frame_variations=1,
                exact_moving_face_scalar_retained=True)


def continued(N,a,eps,t,u,v,mode='moving',completed=False):
    q=mp.exp(mp.pi*1j/N+eps);P=period(N,eps);d=N-1
    F=factorials(q,d);h=v-u;r=a-h;ell=t-v;sigma=d-h;s=d-2*a
    c,D=scalar(N,a,q)
    def ff(z):
        if mode=='root':return root_factorial(N,z)
        if mode=='finite':
            n=int(mp.nint(mp.re(z)));assert z==n and 0<=n<N
            return F[n]
        return moving_factorial(P,z,N)
    def pc(L,x,scale=1):
        return scale*mp.exp(mp.pi*1j*x)*q**(x*(L-x-1))*ff(x)*ff(L-x)/F[L]
    value=(c*q**(s*h)*white(N,a,q,sigma,sigma-u,F)*white(N,a,q,sigma,ell,F)
           *pc(2*a,r)/((-1)**d*q**(-d+2*v)*pc(d,v,N*q**(-d*d))*pc(d,ell,N*q**(-d*d))))
    return value/D if completed else value


def entire(N,a,t,u,v):
    src=Source(N,a);d=N-1;h=v-u;ell=t-v;sigma=d-h;c=mp.cos(mp.pi*h/N)
    q=mp.exp(mp.pi*1j/N)
    def R(z):
        if a==0:return mp.mpf(1)
        old,new=mp.mpf(1),z+c/src.cos[1]
        for n in range(1,a):
            old,new=new,(z+c/(src.cos[n]*src.cos[n+1]))*new+src.B[n]*(src.cos[n]**2-c*c)*old
        return new
    return (src.central_beta**2/N*mp.fprod(2*mp.sin(mp.pi*(h+j)/N) for j in range(a+1,d-a+1))
            *R(q**(2*u-sigma))*R(q**(sigma-2*ell)))


def numeric():
    mp.mp.dps=95
    rootchecks=genericphysical=normals=circles=0
    worstroot=worstphysical=mp.mpf(0);profiles=[]
    for N in (9,10,13,14):
        for a in ((N-1)//2,(N-1)//2-1):
            sigma=N*mp.mpc('.166','.02');h=N-1-sigma
            u=N*mp.mpc('.07','.11');ell=N*mp.mpc('.09','-.12');v=u+h;t=v+ell
            val=continued(N,a,0,t,u,v,'root')
            expected=mp.exp(-2*mp.pi*1j*v)*entire(N,a,t,u,v)
            err=abs(val/expected-1);assert err<mp.mpf('1e-70')
            worstroot=max(worstroot,err);rootchecks+=1
    for N,a,t,u,v in ((5,2,3,1,2),(6,2,4,1,3),(7,2,4,2,1),(8,3,5,1,3)):
        eps=mp.mpc('.003','.002')/N**3
        direct=continued(N,a,eps,t,u,v,'finite',True)
        val=continued(N,a,eps,t,u,v,'moving',True)
        err=abs(val/direct-1);assert err<mp.mpf('1e-60')
        worstphysical=max(worstphysical,err);genericphysical+=1
        for k in (1,2):
            direct=mp.diff(lambda e:continued(N,a,e,t,u,v,'finite',True),0,k)
            val=mp.diff(lambda e:continued(N,a,e,t,u,v,'moving',True),0,k)
            err=abs(val-direct)/max(1,abs(direct))
            assert err<mp.mpf('1e-50');worstphysical=max(worstphysical,err);normals+=1
    for N in (12,13,24,25):
        a=(N-1)//2;sigma=N*mp.mpc('.166','.015')
        logq=mp.pi*1j/N;z1=mp.mpc(80,20);z2=mp.mpc(70,-22)
        u=(sigma+mp.log(z1)/logq)/2;ell=(sigma-mp.log(z2)/logq)/2
        h=N-1-sigma;v=u+h;t=v+ell
        base=continued(N,a,0,t,u,v,'moving',True)
        root=mp.exp(-2*mp.pi*1j*v)*entire(N,a,t,u,v)
        assert abs(base/root-1)<mp.mpf('1e-60')
        ratios=[];rho=mp.mpf('.02')/N**10
        for direction in (1,-1,1j,-1j):
            ratio=abs(continued(N,a,rho*direction,t,u,v,'moving',True)/base)
            assert mp.mpf('.1')<ratio<10
            ratios.append(ratio);circles+=1
        derivative=mp.diff(lambda e:continued(N,a,e,t,u,v,'moving',True),0)
        normalized=abs(derivative/base)/N**10
        assert normalized<100;normals+=1
        profiles.append(dict(N=N,separation=N-1-2*a,
                             maximum_generic_circle_ratio=mp.nstr(max(ratios),30),
                             relative_first_normal_over_N10=mp.nstr(normalized,30)))
    return dict(precision_digits=mp.mp.dps,
                independent_root_Barnes_character_checks=rootchecks,
                literal_generic_supported_completed_entries=genericphysical,
                actual_full_generic_normal_checks=normals,
                nonreal_deficient_full_operator_circle_checks=circles,
                maximum_root_character_relative_error=mp.nstr(worstroot,35),
                maximum_literal_generic_or_normal_error=mp.nstr(worstphysical,35),profiles=profiles)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=dict(status='PASS',exact=exact(),numeric=numeric(),
                scope='Specified meromorphic lift of the literal generic exceptional operator. Root character retained; nonreal deficient shrinking-fold normal upper bound, no nonzero normal amplitude or global degree-cycle claim.')
    path=args.output or Path(__file__).with_name('actual_matching_edge_generic_deficient_operator_lift_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
