#!/usr/bin/env python3
"""Proved candidate-series algebra and actual mixed highest-chart operators.

This historical audit checks neither the separate completed source
coefficient bridge nor its proof. Candidate normalization equivalence is
a separate identity, and the actual source chart is checked independently.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data,coproduct


def poch(a,k,Q,p):
    z=1
    for i in range(k):z=z*(1-a*pow(Q,i,p))%p
    return z


def series(nums,dens,n,Q,p,F):
    return sum(pow(Q,k,p)*math.prod(poch(a,k,Q,p) for a in nums)
               *pow(F[k]*math.prod(poch(a,k,Q,p) for a in dens)%p,-1,p)
               for k in range(n+1))%p


def series_case(N):
    p,eta,q,*_=balanced_data(N);d=N-1;Q=q*q%p;imag=pow(eta,N,p)
    F,s=[1],[1]
    for k in range(1,N):
        F.append(F[-1]*(1-pow(Q,k,p))%p)
        s.append(pow(imag,k,p)*pow(q,-k*(k+1)//2,p)*F[k]%p)
    cases=0
    for a,b,c in itertools.product(range(d//2+1),repeat=3):
        J=a+b+c;delta=J-d;r=b+c-a
        if a<max(b,c) or delta<0:continue
        R=0
        for t in range(a,b+c+1):
            den=math.prod(s[t-j]*s[J-j-t] for j in (a,b,c))%p
            R=(R+s[t]*s[J-t]*pow(den,-1,p))%p
        R0=N*s[a]*pow(s[a-b]*s[a-c]*s[a-delta]*s[b]*s[c]*s[r]%p,-1,p)%p
        nums=[pow(Q,k,p) for k in (-r,a+1,-b,-c)]
        dens=[pow(Q,k,p) for k in (a-b+1,a-c+1,-b-c)]
        Hlong=series(nums,dens,r,Q,p,F)
        assert R==R0*Hlong%p
        Hshort=series([pow(Q,k,p) for k in (-delta,-r,-b,-b)],
                      [pow(Q,k,p) for k in (-b-c,-b-c,-2*b)],delta,Q,p,F)
        Sp=poch(pow(Q,a+1,p),r,Q,p)*poch(pow(Q,-2*b,p),r,Q,p)
        Sp=Sp*pow(poch(pow(Q,a-b+1,p),r,Q,p)*poch(pow(Q,-b,p),r,Q,p)%p,-1,p)%p
        assert Hlong==Sp*Hshort%p
        # Exact equivalence of candidate normalization and missing coefficient target.
        CR=s[a]*s[b]*s[c]*pow(N*s[delta],-1,p)*R%p
        e=2*a*a-a*b-a*c+b*c-J-3
        candidate=(-1)**(N+J)*pow(q,e,p)*CR%p
        E=3*a*a+b*b+c*c-2*a*b-2*a*c+2*b*c-2*c-2
        Ks=N*pow(q,E+2*b*(b+1)-2*c*(c-1),p)*pow(F[a]*F[b]*F[c]*F[r],-1,p)%p
        pref=pow(Q,b*(a+c-b)+c*(2*c+1),p)*F[2*b]*pow(F[a+b-c],-1,p)*F[a]**2*pow(F[delta]*F[a-delta]**2%p,-1,p)%p
        assert candidate==Ks*pref*Hshort%p
        cases+=1
    return {'N':N,'prime':p,'ordered_supported_candidate_objects':cases,
            'exact_long_series_Sears_short_series':True,
            'candidate_normalization_equivalence_NOT_source_identity':True}


def mixed_case(N,a,b):
    p,eta,q,E,F,K,pivot,R,Ri=balanced_data(N)
    d=N-1;Q=q*q%p;x=pow(q,d,p);D=d+a-b;l=2*a+1
    rho=(q-pow(q,-1,p))%p;Ec=rho*rho*E%p
    E2,F2,K2=coproduct(Ec,F,K,2,N,p)
    EQ=np.zeros((l,l),dtype=np.int64);FQ=EQ.copy()
    KQ=np.diag([pow(q,2*a,p)*pow(Q,-r,p)%p for r in range(l)])
    for r in range(1,l):
        EQ[r-1,r]=pow(q,-2*a-1,p)*(1-pow(Q,2*a+1-r,p))%p
        FQ[r,r-1]=(1-pow(Q,r,p))%p
    e23=np.kron(Ec,KQ)+np.kron(np.eye(N,dtype=np.int64),EQ)
    ki=np.diag([pow(int(k),-1,p) for k in np.diag(K)])
    f23=np.kron(F,np.eye(l,dtype=np.int64))+np.kron(ki,FQ)
    k23=np.kron(K,KQ)%p
    o23=(f23@e23+q*k23+pow(q,-1,p)*np.diag([pow(int(z),-1,p) for z in np.diag(k23)]))%p
    physical=list(range(max(0,D-d),min(d,D)+1));width=len(physical)
    source=np.zeros((N*N,width),dtype=np.int64)
    for col,A in enumerate(physical):source[A*N+D-A,col]=1
    Fct=[1]
    for r in range(1,N):Fct.append(Fct[-1]*(1-pow(Q,r,p))%p)
    HL=np.zeros((N,N,l,width),dtype=np.int64);power=source.copy()
    for u in range(l):
        alpha=(-1)**u*pow(q,u*(4*a+1),p)*pow(Q,-u*(u-1)//2,p)*Fct[2*a-u]*pow(Fct[2*a],-1,p)%p
        HL[:,:,u,:]=(alpha*power%p).reshape(N,N,width)
        power=E2@power%p
    right=list(range(max(0,D-2*a),min(d,D)+1))
    Jactual=np.array([HL[0,B,D-B,:] for B in right])
    Jformula=np.zeros_like(Jactual)
    for row,B in enumerate(right):
        u=D-B
        alpha=(-1)**u*pow(q,u*(4*a+1),p)*pow(Q,-u*(u-1)//2,p)*Fct[2*a-u]*pow(Fct[2*a],-1,p)%p
        for col,A in enumerate(physical):
            if A+B>D:continue
            Jformula[row,col]=alpha*pow(x,A,p)*pow(Q,(B*(B+1)-D*(D+1))//2,p)*Fct[D-B]*Fct[D-A]*pow(Fct[D-B-A]*Fct[B],-1,p)%p
    assert np.array_equal(Jactual,Jformula)
    acted=np.zeros_like(HL)
    for first in range(N):acted[first]=(o23@HL[first].reshape(N*l,width)%p).reshape(N,l,width)
    Bactual=np.array([acted[A,D-A,0,:] for A in physical])
    Bformula=np.zeros_like(Bactual)
    idx={A:i for i,A in enumerate(physical)}
    for col,A in enumerate(physical):
        Bformula[col,col]=-(pow(Q,A+b+1,p)+pow(Q,-A-b-1,p))%p
        if A-1 in idx:Bformula[idx[A-1],col]=pow(q,2*b+1,p)*(1-pow(Q,A,p))*(1-pow(Q,D-A+1,p))%p
    assert np.array_equal(Bactual,Bformula)
    ell=np.zeros(width,dtype=np.int64);star=d-b
    for k in range(min(a,b)+1):
        ell[idx[star+k]]=pow(-pow(q,-1,p),k,p)*pow(Q,k*(k+1),p)*Fct[a]*Fct[b]*pow(Fct[k]**2*Fct[a-k]*Fct[b-k],-1,p)%p
    assert np.array_equal(ell@Bformula%p,(-2*ell)%p)
    assert sum(1 for i in range(width) if Bformula[i,i]==p-2)==1
    return {'N':N,'ordinary_outer_labels':[a,b],'physical_degree':D,
            'literal_mixed_Casimir_and_highest_chart':True,
            'rectangular_anti_Pascal_coefficient':True,
            'simple_right_channel_and_closed_left_eigenrow':True}


if __name__=='__main__':
    series_rows=[series_case(N) for N in range(2,17)]
    mixed_rows=[]
    for N in range(3,10):
        M=(N-1)//2
        mixed_rows.extend(mixed_case(N,a,b) for a in range(1,M+1) for b in range(M+1))
    result={'status':'PASS','candidate_Racah_series_algebra':series_rows,
            'actual_mixed_highest_source_operators':mixed_rows,
            'scope':'Historical candidate-series algebra and actual mixed highest-chart operators only. The general source coefficient bridge is proved separately in finite_trivalent_euler_racah_transform.md and actual_trivalent_square_linearization_bridge.md; this audit does not prove that bridge.'}
    Path(__file__).with_name('actual_trivalent_general_finite_transform_port_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(series_rows)} root long/short candidate-series families; {len(mixed_rows)} literal mixed highest-chart/Casimir families; source bridge proved separately')
