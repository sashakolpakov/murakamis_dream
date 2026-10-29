#!/usr/bin/env python3
"""Actual odd Steinberg Clebsch columns and the trivalent invariant anchor.

No unproved positive evaluation or scalar asymptotic is tested or assumed.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_trivalent_complete_circle_vertex_kernel import vertex_formula


def closed_columns(N,q,p):
    m,d=(N-1)//2,N-1;Q=q*q%p;x=pow(q,d,p)
    fac=[1]
    for r in range(1,N):fac.append(fac[-1]*(1-pow(Q,r,p))%p)
    W=np.zeros((N*N,N),dtype=np.int64)
    for r in range(N):
        for a in range(N):
            b=m+r-a
            if not 0<=b<N:continue
            value=0
            for s in range(max(0,a-r),min(m,a)+1):
                den=fac[s]**2*fac[m-s]**2*fac[a-s]*fac[r-a+s]%p
                value+=pow(q,s*s,p)*pow(x,-r+a-s,p)*pow(Q,s*(r-a+s),p)*pow(den,-1,p)
            W[a*N+b,r]=fac[a]*fac[b]*fac[m]*value%p
    return W,fac


def axis(A,v,i,p):
    u=np.moveaxis(v,i,0)
    z=np.tensordot(A,u,axes=(1,0))%p
    return np.moveaxis(z,0,i)


def case(N):
    p,eta,q,E,F,K,pivot,R,Ri=balanced_data(N)
    m,d=(N-1)//2,N-1;Q=q*q%p;x=pow(q,d,p)
    rho=(q-pow(q,-1,p))%p;Ec=rho*rho*E%p
    Et,Ft,Kt=coproduct(Ec,F,K,2,N,p)
    Wclosed,fac=closed_columns(N,q,p)
    Wbar,_=closed_columns(N,pow(q,-1,p),p)
    h=np.zeros(N*N,dtype=np.int64)
    for a in range(m+1):
        h[a*N+m-a]=pow(q,a*a,p)*fac[m]*pow(fac[a]*fac[m-a],-1,p)%p
    W=np.zeros_like(Wclosed);W[:,0]=h
    for r in range(1,N):W[:,r]=Ft@W[:,r-1]%p*pow(1-pow(Q,r,p),-1,p)%p
    assert np.array_equal(W,Wclosed)
    for pair,single in ((Et,Ec),(Ft,F),(Kt,K)):
        assert np.array_equal(pair@W%p,W@single%p)
    P=np.zeros((N*N,N*N),dtype=np.int64)
    for a,b in itertools.product(range(N),repeat=2):P[a*N+b,b*N+a]=1
    assert np.array_equal(Wbar.T@P%p@W%p,np.eye(N,dtype=np.int64))
    for t in range(m+1):assert W[(m+t)*N+d-t,d]==h[t*N+m-t]
    assert W[d,m]==pow(q,-m*m,p)
    # Direct finite Vandermonde scalar in the lowest source normalization.
    vand=sum(pow(Q,a*a,p)*(fac[m]*pow(fac[a]*fac[m-a],-1,p)%p)**2 for a in range(m+1))%p
    assert vand==fac[d]*pow(fac[m]**2,-1,p)%p
    # Every simple CD row, all physical degrees, with the true root half-phase.
    imag=pow(eta,N,p)
    sine=[pow(imag,a,p)*pow(q,-a*(a+1)//2,p)*fac[a]%p for a in range(N)]
    for r in range(N):
        T=m+r;low=min(T,2*d-T);off=max(0,T-d)
        first=off*N+T-off
        w0=int(W[first,r]);assert w0
        v=W[:,r]*pow(w0,-1,p)%p
        vb=Wbar[:,r]*pow(int(Wbar[first,r]),-1,p)%p
        positive=sine[low]**2*pow(sine[low-m]**2,-1,p)%p
        assert np.array_equal(N*np.outer(W[:,r],Wbar[:,r])%p,
                              positive*np.outer(v,vb)%p)
    # Complete central black vertex, in the specified Hopf basis, not a generic 6j.
    labels=[(m+r,m) for r in range(N)]
    U,V,Vm=vertex_formula(N,x,p,labels,Wbar)
    Theta=np.zeros((N,N,N),dtype=np.int64)
    for a,b,c in itertools.product(range(N),repeat=3):
        Theta[a,b,c]=N*pow(x,-c,p)*int(W[a*N+b,d-c])%p
    A=sum(pow(x,k-d,p)*int(Wbar[k*N+m-k,0])**2*int(Wbar[(m+k)*N+m-k,m])
          for k in range(m+1))%p
    scalar=N*N*pow(q,-m*m,p)*A%p
    assert np.array_equal(U,scalar*Theta%p)
    assert int(U[d,m,0])==N**3*A%p
    for z in (U,Theta):
        outE=np.zeros_like(z);outF=np.zeros_like(z)
        Ki=np.diag([pow(int(c),-1,p) for c in np.diag(K)])
        for k in range(3):
            e,f=z.copy(),z.copy()
            for j in range(3):
                e=axis(Ec if j==k else K if j>k else np.eye(N,dtype=np.int64),e,j,p)
                f=axis(F if j==k else Ki if j<k else np.eye(N,dtype=np.int64),f,j,p)
            outE=(outE+e)%p;outF=(outF+f)%p
        assert not np.any(outE) and not np.any(outF)
    # Full anti-Pascal frame: root inversion and the exact coherent quartic transform.
    def recoupling(q0):
        Q0=q0*q0%p;x0=pow(q0,d,p);f0=[1]
        for t in range(1,N):f0.append(f0[-1]*(1-pow(Q0,t,p))%p)
        J=np.zeros((N,N),dtype=np.int64)
        for i in range(N):
            for j in range(N-i):
                J[i,j]=pow(-x0*Q0,d-i,p)*pow(x0,j,p)*pow(Q0,(i*(i+1)-d*(d+1))//2,p)*f0[d-j]*pow(f0[i]*f0[d-i-j],-1,p)%p
        return J,f0
    J,_=recoupling(q);Jbar,facbar=recoupling(pow(q,-1,p))
    rev=np.eye(N,dtype=np.int64)[::-1]
    assert np.array_equal(Jbar@rev%p@J%p,rev)
    f=pow(q,m*m,p)*W[[a*N+d-a for a in range(N)],m]%p
    fb=pow(q,-m*m,p)*Wbar[[a*N+d-a for a in range(N)],m]%p
    beta2=np.array([pow(Q,-k*(m-k),p)*(fac[m]*pow(fac[k]*fac[m-k],-1,p)%p)**2%p for k in range(m+1)],dtype=np.int64)
    y=np.concatenate((np.zeros(m,dtype=np.int64),beta2))
    assert np.array_equal(J@f%p,y)
    assert int(pow(q,-3*m*m,p)*(fb@(J@f%p)%p)%p)==A
    transformed=[]
    for k in range(m+1):
        ck=0
        for i in range(k,m+1):
            gaussian=facbar[i]*pow(facbar[k]*facbar[i-k],-1,p)%p
            ck+=int(beta2[i])*pow(-pow(q,-1,p),i,p)*gaussian
        ck%=p
        expected=(-1)**m*pow(q,k*k-m*(m+1),p)*int(beta2[k])%p
        assert ck==expected
        transformed.append(ck)
    hankel=int(x*sum(pow(Q,-k*k,p)*int(c)**2 for k,c in enumerate(transformed))%p)
    assert hankel==int(fb@y%p)
    quartic=sum(int(b)**2 for b in beta2)%p
    assert A==pow(q,m*(2-m),p)*quartic%p
    return {'N':N,'prime':p,'all_actual_Clebsch_entries_and_Hopf_arrows':True,
            'highest_lowest_middle_source_phases':True,'full_simple_CD_normalization':True,
            'whole_central_black_vertex_is_explicit_3j':True,
            'finite_coherent_scalar_image':int(A),
            'full_P_unitary_anti_Pascal_and_second_Chu_transform':True,
            'exact_original_coherent_positive_quartic_transform':True,
            'marked_white_packet_retained_separately':True}


def scalar_profile(N):
    mp.mp.dps=90
    m=(N-1)//2
    s=[mp.mpf(1)]
    for r in range(1,m+1):s.append(s[-1]*2*mp.sin(mp.pi*r/N))
    value=sum((s[m]/s[k]/s[m-k])**4 for k in range(m+1))
    normalized=4*N**mp.mpf('1.5')*mp.exp(-N*4*mp.catalan/mp.pi)*value
    assert abs(normalized-1)<3/N
    return {'N':N,'positive_finite_quartic_sum':True,
            'normalized_all_odd_Laplace_prefactor':float(normalized)}


if __name__=='__main__':
    rows=[case(N) for N in range(3,22,2)]
    out={'status':'PASS','actual_odd_central_levels':rows,
         'positive_scalar_Laplace_calibration':[scalar_profile(N) for N in (33,65,129,257,513)],
         'scope':'Exact actual odd root Clebsch/source identities and proven finite coherent quartic transform; scalar asymptotic only. No even confluence, marked-white/global geometric maximum, or sewn-source survival claim.'}
    Path(__file__).with_name('actual_trivalent_steinberg_central_anchor_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(rows)} actual odd Clebsch/Hopf/CD, whole trivalent-3j and quartic-transform levels; 5 scalar Laplace calibrations')
