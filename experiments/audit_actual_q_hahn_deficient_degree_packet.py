#!/usr/bin/env python3
"""Original generic deficient numerator, residual, and selected root packet."""
import json
import math
from pathlib import Path
import mpmath as mp
import numpy as np
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S,scalar_K,jacobi,determinant,prod
from audit_actual_q_hahn_joint_complex_amplitude import selected_packet,transport


def forced(q,t,z):return prod(z-q**(t-2*r) for r in range(t+1))


def exact():
    zeros=bridge=tail=source=shift=0
    Jet.order=4
    for N in range(3,16):
        p,eta=root_field(N);q0=eta*eta%p
        for generic in (False,True):
            Jet.p=1000000007 if generic else p
            qval=2 if generic else q0
            q=Jet([qval*pow(math.factorial(k),-1,Jet.p)%Jet.p for k in range(4)])
            Q=q*q
            for a in range(1,(N-1)//2+1):
                for t in range(a):
                    s=q**t;T=s*s;A,B=jacobi(N,q,s,a)
                    for u in range(t+1):
                        assert source_S(N,q,a,Q**u,T)==0
                        assert determinant(N,q,s,a,q**(t-2*u))==0
                        zeros+=1
                    if a>=t+2:
                        assert B[t+1]==0;bridge+=1
                    for zval in (3,7):
                        z=Jet(zval);F=forced(q,t,z)
                        if a==t+1:V=Jet(1)
                        else:
                            old,V=Jet(1),z+A[t+1]
                            for n in range(t+2,a):old,V=V,(z+A[n])*V+B[n]*old
                        assert determinant(N,q,s,a,z)==F*V;tail+=1
                        U=s/z
                        assert z**a*source_S(N,q,a,U,T)==s**(2*a)*scalar_K(N,q,a)*F*V
                        source+=1
        # The root-only finite shift is checked separately, without
        # accidentally differentiating its B=1 specialization.
        Jet.p=p;Jet.order=1;q=Jet(q0);Q=q*q
        for a in range(1,(N-1)//2+1):
            for t in range(a):
                s=q**t;T=s*s
                for zval in (3,7):
                    z=Jet(zval);U=s/z
                    R=lambda w:determinant(N,q,s,a,w)
                    value=((Q*U-1)*(U-T)*R(z/Q)+(Q*T-U)*(1-U)*R(Q*z)
                           +(2*U+2*Q*T*U-(1+Q)*U*U-T*(Q**(-a)+Q**(a+1)))*R(z))
                    assert value==0;shift+=1
        Jet.order=4
    return dict(original_generic_forced_node_four_jets=zeros,
                identically_zero_bridge_four_jets=bridge,
                genuine_generic_tail_factorizations=tail,
                original_Newton_numerator_four_jet_comparisons=source,
                exact_root_finite_shift_equations=shift)


def root_poly(N,t,a,z):
    th=mp.pi/N;c=-mp.cos((t+1)*th)
    old,R=mp.mpf(1),z+c/mp.cos(th)
    for n in range(1,a):
        bn=mp.sin(n*th)**2/(mp.cos(n*th)**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
        old,R=R,(z+c/(mp.cos(n*th)*mp.cos((n+1)*th)))*R+bn*(mp.cos(n*th)**2-c*c)*old
    return R


def packet_ratio(sigma,alpha,z):
    """Independent actual high anchor, then integrate exact transport."""
    hi=1-sigma;nu=hi/2
    _,_,saddle=selected_packet(hi,alpha,nu)
    phinu,_,_,_=transport(hi,alpha,nu,saddle)
    kap=2*mp.pi*1j;p0=mp.mpf('.5')-phinu/kap
    T=mp.exp(2*mp.pi*1j*sigma);J=mp.exp(2*mp.pi*1j*alpha)
    C=mp.cos(mp.pi*sigma);Ca=mp.cos(mp.pi*alpha);sa=mp.sin(mp.pi*alpha)
    disc=mp.sqrt(C*C-Ca*Ca)
    rinv1,rinv2=C+disc,C-disc
    def data(w,sign):
        U=mp.exp(mp.pi*1j*sigma)/w
        A=(U-1)*(U-T);C0=2*U*(1+T-U)-T*(J+1/J)
        sw=mp.sqrt(1-w*rinv1)*mp.sqrt(1-w*rinv2)
        sd=4j*T*sa*sw/w
        E=(-C0+sign*sd)/(2*A)
        Hp=kap*A*(E-1/E);Hpp=kap*kap*A*(E+1/E)
        DA=-2*U*U+(1+T)*U
        Dp=-DA*(E+1/E-2)/Hp
        H1=kap*(U*(U-T)/E+T*(1-U)*E+2*T*U-U*U-T*J)
        rr=-(H1+Dp*Hpp/2)/Hp
        return E,Dp,rr
    target=mp.exp(kap*p0)
    sign=min((1,-1),key=lambda ss:abs(data(-1,ss)[0]-target))
    assert abs(data(-1,sign)[0]-target)<mp.mpf('1e-105')
    ll=mp.log(-z)
    path=lambda s:-mp.exp(s*ll)
    cuts=[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1]
    S=p0*ll+ll*ll*mp.quad(lambda s:(1-s)*data(path(s),sign)[1],cuts)
    logA=ll*mp.quad(lambda s:data(path(s),sign)[2],cuts)
    pend=p0+ll*mp.quad(lambda s:data(path(s),sign)[1],cuts)
    rend=data(z,sign)[2]
    return S,mp.exp(logA),pend,rend


def numerics():
    mp.mp.dps=150;rows=[];worst=gradmax=sourceerr=mp.mpf(0);matrixchecks=normalchecks=0
    for N in (24,25,48,49,96,97):
        t=N//6
        for a in sorted(set((int(mp.mpf('.4')*N),(N-1)//2))):
            sigma,alpha=mp.mpf(t)/N,mp.mpf(a)/N
            th=mp.pi/N;c=-mp.cos((t+1)*th);m=a-t-1
            Jmat=np.zeros((m,m))
            for r,n in enumerate(range(t+1,a)):
                Jmat[r,r]=float(-c/(mp.cos(n*th)*mp.cos((n+1)*th)))
                if r:
                    bn=mp.sin(n*th)**2/(mp.cos(n*th)**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
                    edge=mp.sqrt(bn*(c*c-mp.cos(n*th)**2))
                    Jmat[r-1,r]=Jmat[r,r-1]=float(edge)
            assert np.linalg.eigvalsh(Jmat)[0]>0;matrixchecks+=1
            q0=mp.exp(mp.pi*1j/N)
            for z in (mp.mpc('3','2'),mp.mpc('3','-2')):
                actual=root_poly(N,t,a,z)/root_poly(N,t,a,-1)
                S,A,p,r=packet_ratio(sigma,alpha,z)
                rel=N*abs(actual/(A*mp.exp(N*S))-1)
                grad=N*N*abs(z*mp.diff(lambda w:root_poly(N,t,a,w),z)/root_poly(N,t,a,z)/N-p-r/N)
                assert rel<30 and grad<100,(N,a,z,rel,grad)
                worst=max(worst,rel);gradmax=max(gradmax,grad)
                # Fixed marked branch, with |u|=O(N).
                logz=mp.log(z)
                if mp.im(logz)<0:logz+=2*mp.pi*1j
                u=(t-logz/(mp.pi*1j/N))/2
                base=root_poly(N,t,a,z)
                for phase in (1,1j):
                    eps=mp.mpf('.1')*phase/N**10;q=q0*mp.exp(eps);s=q**t;zz=q**(t-2*u)
                    gen=determinant(N,q,s,a,zz)
                    U=s/zz;literal=zz**a*source_S(N,q,a,U,s*s)/(s**(2*a)*scalar_K(N,q,a))
                    err=abs(literal/gen-1);assert err<mp.mpf('1e-95');sourceerr=max(sourceerr,err)
                    assert abs(gen/base)<3;normalchecks+=1
                derivative=mp.diff(lambda e:determinant(N,q0*mp.exp(e),(q0*mp.exp(e))**t,a,
                                                       (q0*mp.exp(e))**(t-2*u)),0)
                assert abs(derivative/base)/N**10<10;normalchecks+=1
                rows.append(dict(N=N,t=t,a=a,z=str(z),N_times_relative_error=str(rel),
                                 N_squared_gradient_remainder=str(grad)))
    return dict(precision_digits=mp.mp.dps,positive_residual_Jacobi_checks=matrixchecks,
                actual_selected_relative_amplitudes=len(rows),genuine_generic_numerator_checks=normalchecks,
                maximum_N_times_relative_error=str(worst),maximum_N_squared_gradient_remainder=str(gradmax),
                maximum_literal_generic_source_relative_error=str(sourceerr),cases=rows)


def main():
    result=dict(status='PASS',exact=exact(),calibration=numerics(),
                scope='Actual fixed-integer deficient numerator packet and genuine q-numerator jets with bounded marked lifts. No full generic operator lift, joint complex degree or nonzero forbidden-slice period.')
    Path(__file__).with_name('actual_q_hahn_deficient_degree_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'calibration':{k:v for k,v in result['calibration'].items() if k!='cases'}},indent=2))


if __name__=='__main__':main()
