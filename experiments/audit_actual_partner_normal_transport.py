#!/usr/bin/env python3
"""Audit the restricted first-normal partner theorem, not all partner jets."""
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sy

from audit_actual_supported_racah_common_phase_and_normal_metric import (
    divide, factorials_without, forms, germ, mul, quantum_units, root_field,
)


def symbolic_recurrence():
    a,u,v,w,Q,T,K=sy.symbols('a u v w Q T K')
    P=u*v*w/a**2
    A=(1-u*T)*(1-v*T)*(1-w*T)*(1-P*T/Q)/(a*(1-P*T*T/Q)*(1-P*T*T))
    C=a*(1-T)*(1-u*v*T/(a*a*Q))*(1-u*w*T/(a*a*Q))*(1-v*w*T/(a*a*Q))/((1-P*T*T/Q**2)*(1-P*T*T/Q))
    plus=(1-1/(Q*T))*(1-P*T*K/Q)/((1-K/(Q*T))*(1-P*T/Q))
    minus=(1-K/T)*(1-P*T/Q**2)/((1-1/T)*(1-P*T*K/Q**2))
    back=(1-K)*(1-u*K/Q)*(1-v*K/Q)*(1-w*K/Q)/(Q*(1-K/(Q*T))*(1-P*T*K/Q**2))
    residue=a*K+1/(a*K)-Q*back/(a*K)-A*plus-(a+1/a-A-C)-C*minus
    assert sy.cancel(residue)==0
    return {'exact_generic_coefficient_identity':True,'independent_parameters':7}


def data(N,ext,f):
    a,b,c,d=ext;D=N-1
    p=min(a+d,b+c);s=sum(ext);h=max(abs(a-b),abs(c-d))
    return p,s,h,s-2*p,a+b-h,c+d-h,2*p-D,p-f,p+f-D


def rates(N,ext,f):
    p,s,h,t0,rA,rC,L,n,t=data(N,ext,f);th=math.pi/N
    aa=[];bb=[]
    for j in range(t):
        a=4*math.sin((t0+1+j)*th)*math.sin((rA-j)*th)*math.sin((rC-j)*th)*math.sin((L-j)*th)/(math.sin((L-2*j)*th)*math.sin((L-2*j-1)*th))
        b=0 if j==0 else 4*math.sin(j*th)*math.sin((rA-L+j)*th)*math.sin((rC-L+j)*th)*math.sin((s+2-N-j)*th)/(math.sin((L-2*j+1)*th)*math.sin((L-2*j)*th))
        aa.append(a);bb.append(b)
    return np.array(aa),np.array(bb)


def numerical_root_family(N):
    D=N-1;M=D//2;count=0;min_drift=math.inf;min_gap=math.inf
    sine=np.r_[1.,np.cumprod(2*np.sin(np.arange(1,N)*math.pi/N))]
    for ext in itertools.product(range(M+1),repeat=4):
        a,b,c,d=ext
        for f in range(max(D-a-d,D-b-c,0),M+1):
            p,s,h,t0,rA,rC,L,n,t=data(N,ext,f)
            lo=max(h,D-a-b,D-c-d)
            if t==0 or lo>M:continue
            assert 0<t<=n and n+t==L and min(rA,rC)>=L
            aa,bb=rates(N,ext,f)
            assert np.all(aa>=64/N**4-1e-10) and np.all(aa>=bb-1e-10)
            mat=np.diag(aa+bb)
            if t>1:
                off=-np.sqrt(aa[:-1]*bb[1:]);mat+=np.diag(off,1)+np.diag(off,-1)
            ev=np.linalg.eigvalsh(mat)
            assert ev[0]>=64/N**6-1e-9
            c0=2*math.cos((2*h+1)*math.pi/N)
            # Independent finite Newton coefficients versus the Jacobi determinant.
            coeff=np.zeros(t+1);bas=np.array([1.])
            for k in range(t+1):
                Ak=sine[n]/sine[n-k]*sine[t]/sine[t-k]*sine[rA-k]/sine[rA]*sine[rC-k]/sine[rC]*sine[t0]/sine[k]/sine[t0+k]
                coeff[:len(bas)]+=Ak*bas
                if k<t:bas=np.polynomial.polynomial.polymul(bas,[2*math.cos((2*(h+k)+1)*math.pi/N),-1])
            for e in sorted(set((lo,M))):
                lam=2*math.cos((2*e+1)*math.pi/N)
                value=np.polynomial.polynomial.polyval(lam,coeff)
                detvalue=np.prod((ev+c0-lam)/ev)
                assert abs(value/detvalue-1)<2e-8
                derivative=np.polynomial.polynomial.polyval(lam,np.polynomial.polynomial.polyder(coeff))
                assert abs(derivative/value)<=N**7/64+1e-7
            min_drift=min(min_drift,float(np.min(aa-bb)));min_gap=min(min_gap,float(ev[0]));count+=1
    return {'N':N,'all_admissible_external_right_families':count,'minimum_drift':min_drift if count else None,'minimum_gap':min_gap if count else None,'spectral_not_generic_jet_bound':True}


def poch(q,Q,m,p):
    ans=1
    for k in range(m):ans=ans*(1-q*pow(Q,k,p))%p
    return ans


def spectral_value_derivative(N,lab,q,p):
    a,b,c,d,e,f=lab
    p0,s,h,t0,rA,rC,L,n,t=data(N,(a,b,c,d),f)
    Q=q*q%p;alpha=pow(q,2*h+1,p);lam=(pow(q,2*e+1,p)+pow(q,-2*e-1,p))%p
    ans=der=0;M=1;Md=0
    for k in range(t+1):
        num=poch(pow(Q,-n,p),Q,k,p)*poch(pow(Q,-t,p),Q,k,p)*pow(Q,k,p)%p
        den=poch(Q,Q,k,p)*poch(pow(Q,t0+1,p),Q,k,p)*poch(pow(Q,-rA,p),Q,k,p)*poch(pow(Q,-rC,p),Q,k,p)%p
        coeff=num*pow(den,-1,p)%p
        ans=(ans+coeff*M)%p;der=(der+coeff*Md)%p
        z=alpha*pow(Q,k,p)%p;fac=(1+z*z-z*lam)%p
        M,Md=M*fac%p,(Md*fac-M*z)%p
    return ans,der


def metric_and_s0den(N,lab,q,p):
    D=N-1;faces,F,quads=forms(lab)
    units=quantum_units(q,p,3*N,2)
    fac=factorials_without(units,p,set());noN=factorials_without(units,p,{N})
    metric=[1,0]
    for tri,z in zip(faces,F):
        num=[1,0]
        for j in tri:num=mul(num,fac[z-2*j],p)
        df=divide(num,noN[z+1],p);df=[(-1)**(z-D)*v%p for v in df]
        metric=mul(metric,df,p)
    a,b,c,d,e,f=lab;s=a+b+c+d;small=min(a+d,b+c);t0=s-2*small
    ap,bp,cp,dp=(a,b,c,d) if a+d<=b+c else (b,a,d,c)
    inds=[c+d-e,a+b-e,t0,ap-bp+e,dp-cp+e]
    assert all(0<=v<=D for v in inds)
    den=[1,0]
    for z in inds:den=mul(den,fac[z],p)
    return metric,den


def first_normal_level(N):
    p,eta=root_field(N);q=eta*eta%p;D=N-1;M=D//2;count=0;nonzero=0
    supported=[lab for lab in itertools.product(range(M+1),repeat=6) if min(forms(lab)[1])>=D]
    # Exhaust all first-normal data through N8, then a deterministic coverage selection.
    selected=supported if N<=8 else supported[::max(1,len(supported)//75)]
    for lab in selected:
        high=lab[:4]+(D-lab[4],lab[5])
        C,T,G,u=germ(N,lab,q,p,2);Ch,Th,Gh,uh=germ(N,high,q,p,2)
        met,den=metric_and_s0den(N,lab,q,p);meth,denh=metric_and_s0den(N,high,q,p)
        K=mul(mul(G,G,p),met,p);Kh=mul(mul(Gh,Gh,p),meth,p)
        ratio=mul(divide(meth,met,p),mul(divide(den,denh,p),divide(den,denh,p),p),p)
        assert ratio[0]==1 and K[0]==Kh[0]
        R,Rd=spectral_value_derivative(N,lab,q,p)
        e=lab[4];lamdot=(-2*N*(pow(q,2*e+1,p)-pow(q,-2*e-1,p)))%p
        assert ((Kh[1]-K[1]-ratio[1]*K[0])*R-2*lamdot*Rd*K[0])%p==0
        nonzero+=bool((Kh[1]-K[1])%p);count+=1
    return {'N':N,'prime':p,'literal_full_first_normal_cases':count,'nonidentical_partner_first_normals':nonzero,'one_flip_tail_is_empty_by_untouched_opposite_sum':True}


def central_harmonic(N):
    assert N%2;m=(N-1)//2;p,eta=root_field(N);q=eta*eta%p;Q=q*q%p;i=pow(eta,N,p)
    R,Rd=spectral_value_derivative(N,(m,m,m,m,0,m),q,p)
    sin2=(q-pow(q,-1,p))*pow(i,-1,p)%p
    cot=sum((pow(q,u,p)+pow(q,-u,p))*i*pow(pow(q,u,p)-pow(q,-u,p),-1,p)for u in range(1,m+1))%p
    assert R==1 and (Rd+cot*pow(sin2,-1,p))%p==0
    with mp.workdps(70):
        th=mp.pi/N;val=-mp.fsum(mp.cot(u*th)for u in range(1,m+1))/(2*mp.sin(th))
        assert abs(val)<N*N*(1+mp.log(N))
    return {'N':N,'prime':p,'exact_cotangent_derivative_identity':True,'complex_value':mp.nstr(val,20)}


if __name__=='__main__':
    sym=symbolic_recurrence()
    root=[numerical_root_family(N)for N in range(3,15)]
    normal=[first_normal_level(N)for N in range(3,12)]
    central=[central_harmonic(N)for N in range(3,32,2)]
    prime,eta=root_field(5);q=eta*eta%prime;Q=q*q%prime
    C,T,G,u=germ(5,(3,3,2,2,2,2),q,prime,2)
    assert C[0]==(2+Q+pow(Q,-1,prime))%prime and T[0]==(-1)%prime
    adjacent={'N':5,'partner_labels':[3,3,2,2,2,2],'true_range':[8,9],
              'C0':'(3+sqrt(5))/2','T0':-1,'full_normal_bound_NOT_proved':True}
    result={'status':'PASS','symbolic_degree_recurrence':sym,'full_chamber_drift_and_spectrum':root,'actual_first_normals':normal,'exact_central_normals':central,
            'first_nonempty_tail_regression':adjacent,
            'scope':'New every-fixed-root-spectral-derivative estimate. Tail-free partner generic-q jets follow from existing positive-core theorem; one-flip first-normal identity is exact but its tail is empty. No nonempty-tail jet bound or sequential high-external transport inferred.'}
    Path(__file__).with_name('actual_partner_normal_transport_results.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print('PASS symbolic degree recurrence /',sum(x['all_admissible_external_right_families']for x in root),'root families /',sum(x['literal_full_first_normal_cases']for x in normal),'full first normals /',len(central),'exact cotangent identities')
