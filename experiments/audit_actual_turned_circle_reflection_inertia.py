#!/usr/bin/env python3
"""Actual turned circle: all-normal identity and source-relative inertia.

Finite fields check the literal physical turn and completed p,t packet.
Complex square-root/inertia checks supplement the all-N congruence proof;
positivity is not inferred from residues or a sampled graph scalar.
"""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_high_color_first_normal_r_degree import root_field
from audit_actual_complete_circle_reflection_positive import omega_block


def physical_omega(N,q,p):
    d,Q=N-1,q*q%p;x=pow(q,d,p)
    E=np.zeros((N,N),dtype=np.int64);F=E.copy()
    for u in range(1,N):E[u-1,u]=(pow(Q,-u,p)-1)%p
    for u in range(d):F[u+1,u]=(1-pow(Q,u+1,p))%p
    K=np.diag([x*pow(Q,-u,p)%p for u in range(N)])
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    I=np.eye(N,dtype=np.int64)
    Et=(np.kron(E,K)+np.kron(I,E))%p
    Ft=(np.kron(F,I)+np.kron(Ki,F))%p
    Kt=np.kron(K,K)%p
    Kti=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    return (Ft@Et+q*Kt+pow(q,-1,p)*Kti)%p


def field_packet(N,q,p):
    d,Q=N-1,q*q%p;M=d//2
    fac=[1]
    for v in range(1,N):fac.append(fac[-1]*(1-pow(Q,v,p))%p)
    s2=[(-1)**v*pow(q,-v*(v+1),p)*fac[v]**2%p for v in range(N)]
    O=physical_omega(N,q,p);I=np.eye(N*N,dtype=np.int64)
    basis=I.copy();f=np.zeros_like(I);alphas=[]
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(N)]
    for v in range(M+1):
        alpha=0
        for j in range(v,M+1):
            k=1 if 2*j==d else 2
            z=(pow(q,v*(v-2*j),p)*fac[j+v]
               *pow(fac[j-v]*fac[v]**2,-1,p))%p
            alpha=(alpha+N*k*z)%p
        alphas.append(alpha);f=(f+alpha*basis)%p
        if v<M:
            basis=(nodes[v]*I-O)@basis%p
            basis=basis*pow(s2[v+1]*pow(s2[v],-1,p)%p,-1,p)%p
    L0,L1=I.copy(),O.copy()
    for _ in range(2,N):L0,L1=L1,(O@L1-L0)%p
    LN=(-1)**d*(L0 if N==1 else L1)%p
    x=pow(q,d,p)
    turned=np.empty_like(I)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for e in range(N):
                    turned[a*N+b,c*N+e]=pow(x,a-e,p)*int(LN[(d-a)*N+c,b*N+d-e])%p
    assert np.array_equal(f,turned)
    return O,f,alphas


def field_case(N):
    p,eta=root_field(N);q=eta*eta%p;qi=pow(q,-1,p);d=N-1
    O,f,alpha=field_packet(N,q,p)
    Ob,fb,alphab=field_packet(N,qi,p)
    assert alpha==alphab
    P=np.zeros((N*N,)*2,dtype=np.int64)
    for a in range(N):
        for b in range(N):P[b*N+a,a*N+b]=1
    H=P@f%p
    assert np.array_equal(H,(P@fb%p).T)
    ids=[u*N+d-u for u in range(N)]
    Hd=H[np.ix_(ids,ids)]
    def source(z):
        Q=z*z%p;x=pow(z,d,p);rho=(z-pow(z,-1,p))%p
        harmonic=[0]
        for u in range(1,N):harmonic.append((harmonic[-1]+pow(1-pow(Q,u,p),-1,p))%p)
        mean=sum(harmonic)*pow(N,-1,p)%p
        cup=np.array([N*pow(x,u-d,p)%p for u in range(N)],dtype=np.int64)
        t=np.array([(-1)**(N+1)*N*rho*pow(x,u-d,p)*(harmonic[u]-mean)%p for u in range(N)],dtype=np.int64)
        return np.stack((cup,t),axis=1)
    V,Vb=source(q),source(qi)
    source_form=Vb.T@Hd%p@V%p
    assert int(source_form[0,0])==0
    assert int(source_form[0,1])==int(source_form[1,0])==pow(N,4,p)
    assert (int(source_form[0,0])*int(source_form[1,1])-int(source_form[0,1])*int(source_form[1,0]))%p==(-pow(N,8,p))%p
    assert alpha[0]==N*N%p
    return {'N':N,'prime':p,'literal_full_physical_turn_identity':True,
            'completed_original_source_determinant':f'-{N}^8',
            'all_Hermite_normals_retained':True}


def poly_value(coeff,z):
    ans=mp.mpf(0)
    for a in reversed(coeff):ans=ans*z+a
    return ans


def matrix_value(coeff,O):
    I=mp.eye(O.rows);out=mp.matrix(O.rows)
    for a in reversed(coeff):out=out*O+a*I
    return out


def complex_case(N):
    mp.mp.dps=100;d=N-1;M=d//2
    q=mp.exp(mp.pi*1j/N);Q=q*q;x=q**d;rho=q-1/q
    s=[mp.mpf(1)]
    for r in range(1,N):s.append(s[-1]*2*mp.sin(mp.pi*r/N))
    nodes=[2*mp.cos(mp.pi*(2*j+1)/N) for j in range(M+1)]
    coeff=[mp.mpf(0)]*N;basis=[mp.mpf(1)]
    for v in range(M+1):
        alpha=N*sum((1 if 2*j==d else 2)*s[j+v]/(s[j-v]*s[v]**2) for j in range(v,M+1))
        for i,b in enumerate(basis):coeff[i]+=alpha*b
        if v<M:
            ratio=(s[v+1]/s[v])**2
            nxt=[mp.mpf(0)]*(len(basis)+1)
            for i,b in enumerate(basis):nxt[i]+=nodes[v]*b/ratio;nxt[i+1]-=b/ratio
            basis=nxt
    deriv=[(i+1)*coeff[i+1] for i in range(N-1)]
    interpolation=mp.matrix(N);rhs=mp.matrix(N,1);row=0
    minimum=None
    for j,c in enumerate(nodes):
        fc=poly_value(coeff,c);assert fc>N*N-mp.mpf('1e-70')
        minimum=fc if minimum is None else min(minimum,fc)
        gc=mp.sqrt(fc)
        for k in range(N):interpolation[row,k]=c**k
        rhs[row]=gc;row+=1
        if 2*j<d:
            for k in range(1,N):interpolation[row,k]=k*c**(k-1)
            rhs[row]=poly_value(deriv,c)/(2*gc);row+=1
    assert row==N
    g=list(mp.lu_solve(interpolation,rhs))
    positive=negative=0
    source_checks=False
    for T in range(d+1):
        O=omega_block(N,T);P=mp.matrix(T+1)
        for u in range(T+1):P[u,T-u]=1
        F,G=matrix_value(coeff,O),matrix_value(g,O)
        H=P*F;scale=max(1,max(abs(v) for v in H))
        assert max(abs(v) for v in (G*G-F))<mp.mpf('1e-65')*scale
        assert max(abs(v) for v in (G.H*P*G-H))<mp.mpf('1e-65')*scale
        eig=list(mp.eighe((H+H.H)/2,eigvals_only=True))
        pos=sum(v>mp.mpf('1e-65') for v in eig);neg=sum(v<-mp.mpf('1e-65') for v in eig)
        assert (pos,neg)==((T+2)//2,(T+1)//2)
        factor=1 if T==d else 2;positive+=factor*pos;negative+=factor*neg
        if T==d:
            cup=mp.matrix([N*x**(u-d) for u in range(N)])
            ell=mp.matrix([[x**u/N for u in range(N)]])
            cost=(cup.H*G.H*G*cup)[0]
            erow=ell*(G**-1)
            dual=(erow*erow.H)[0]
            assert abs(cost-N**5)<mp.mpf('1e-60')*N**5
            assert abs(dual-mp.mpf(1)/N**3)<mp.mpf('1e-60')
            source_checks=True
    assert (positive,negative)==(N*(N+1)//2,N*(N-1)//2)
    return {'N':N,'positive':positive,'negative':negative,
            'full_Hermite_square_root_congruence':True,
            'minimum_nodal_value_over_N_squared':str(minimum/N**2),
            'literal_positive_metric_cup_and_cap_costs':source_checks}


if __name__=='__main__':
    exact=[field_case(N) for N in range(2,13)]
    complex_rows=[complex_case(N) for N in (2,3,4,6,9,12)]
    out={'status':'PASS','exact_full_physical_levels':exact,'complex_inertia_and_source_metrics':complex_rows,
         'scope':'Genuine turned complete-circle form has full swap inertia, already indefinite on completed original c0 source; explicit positive metric has polynomial ordinary boundaries. No general graph energy bound.'}
    Path(__file__).with_name('actual_turned_circle_reflection_inertia_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS11 exact literal turn/source packets;6 full-Hermite congruence/inertia/positive-metric families')
