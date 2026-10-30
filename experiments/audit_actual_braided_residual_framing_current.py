#!/usr/bin/env python3
"""Original routed off-diagonal Ward flux and genuine first quantum jets."""
import argparse
import math
import json
from pathlib import Path

import numpy as np
import sympy as sp
import mpmath as mp

from audit_actual_braided_two_cut_source_adapter import (
    original_crossings, embed_pair, embed_one, product, partial, eye, eq,
    Local, const, mm, kron, module_jet)


def fixture(N, width, kind):
    p, q, g, (Rp, Rm) = original_crossings(N)
    plus = [embed_pair(Rp,i,width,N,p) for i in range(width-1)]
    minus = [embed_pair(Rm,i,width,N,p) for i in range(width-1)]
    if kind == 'braid':
        word = [plus[0]]*3 if width == 2 else [plus[0],minus[1],plus[0],minus[1]]
    else:
        local = Local(N)
        sectors = [mm(local.W[a],local.pi[a],p) for a in local.W]
        weights = [local.h0[a] for a in local.W]
        C = tuple(sum((h*S[r] for h,S in zip(weights,sectors)),np.zeros_like(Rp[r]))%p
                  for r in range(2))
        word = [embed_pair(C,0,width,N,p),plus[0],embed_pair(C,width-2,width,N,p)]
    A = product(word[1:],N**width,p)
    B = word[0]
    U = product([plus[i] for i in range(width-2,-1,-1)],N**width,p)
    Ui = product([minus[i] for i in range(width-1)],N**width,p)
    return p,q,g,A,B,U,Ui,width,width


def rectangular_fixture(N):
    p,q,g,(Rp,Rm) = original_crossings(N)
    local=Local(N)
    # A real birth, routed crossings, and death; exposed widths one and three.
    birth=kron(eye(N),tuple(x.reshape(N*N,1) for x in local.cup),p)
    death=kron(eye(N),tuple(x.reshape(1,N*N) for x in local.cap),p)
    R0=embed_pair(Rp,0,3,N,p)
    R1=embed_pair(Rp,1,3,N,p)
    A=mm(death,mm(R0,R0,p),p)
    B=birth
    U=mm(R0,R1,p)
    Ui=mm(embed_pair(Rm,1,3,N,p),embed_pair(Rm,0,3,N,p),p)
    return p,q,g,A,B,U,Ui,1,3


def audit_case(N, width, kind):
    data=rectangular_fixture(N) if kind=='rectangular' else fixture(N,width,kind)
    p,q,g,A,B,U,Ui,outwidth,inwidth=data
    d=N-1
    H=partial(mm(A,B,p),g,outwidth,N,p)
    z=tuple(int(h[0,0]) for h in H)
    assert eq(H,tuple(zz*np.eye(N,dtype=np.int64)%p for zz in z))
    t=2*pow(3,-1,p)%p
    beta=np.array([math.comb(d,a)*pow(t,a,p)*pow(1-t,d-a,p)%p
                   for a in range(N)],dtype=np.int64)
    assert int(sum(beta))%p==1
    ecut=np.outer(beta,np.ones(N,dtype=np.int64))
    E,F,K=module_jet(d,q,p)
    Ki=(np.diag([pow(int(K[0][a,a]),-1,p) for a in range(N)]),
        np.diag([-(d-2*a)*pow(int(K[0][a,a]),-1,p)%p for a in range(N)]))
    EK=mm(E,Ki,p)
    dualE=tuple((x-y)%p for x,y in zip(mm(mm(Ki,const(ecut),p),E,p),
                                       mm(EK,const(ecut),p)))
    dualF=tuple((x-y)%p for x,y in zip(mm(const(ecut),F,p),
                                       mm(mm(mm(K,F,p),const(ecut),p),Ki,p)))
    dualK=tuple((x-y)%p for x,y in zip(mm(mm(Ki,const(ecut),p),K,p),const(ecut)))
    L=np.zeros((2,N+1),dtype=np.int64)
    normal_defects=0
    for a in range(d):
        for jet in range(2):
            L[jet,a+1]=(int(F[jet][a+1,a])*int(beta[a])
                       +int(EK[jet][a,a+1])*int(beta[a+1]))%p
        root=(1-pow(q,2*(a+1),p))*(int(beta[a])-q*int(beta[a+1]))%p
        assert L[0,a+1]==root
        falsejet=(-2*(a+1)*pow(q,2*(a+1),p)*(int(beta[a])-q*int(beta[a+1]))
                  -(1-pow(q,2*(a+1),p))*q*int(beta[a+1]))%p
        defect=-2*N*pow(q,2*a+3,p)*int(beta[a+1])%p
        assert (L[1,a+1]-falsejet)%p==defect
        normal_defects+=int(defect!=0)
    for jet in range(2):
        assert np.array_equal(np.diag((dualF[jet]-dualE[jet]-2*dualK[jet])%p),
                              (L[jet,1:]-L[jet,:-1])%p)
    J=np.zeros((2,N,N),dtype=np.int64)
    T={}
    for ell in range(N):
        bands=[(ell,ell)]+([(ell+1,ell),(ell,ell+1)] if ell<d else [])
        for r,s in bands:
            unit=np.zeros((N,N),dtype=np.int64);unit[r,s]=1
            X=mm(mm(Ui,embed_one(const(unit),0,inwidth,N,p),p),U,p)
            C=partial(mm(mm(A,X,p),B,p),g,outwidth,N,p)
            T[r,s]=tuple(int(np.trace(ecut@C[j])%p) for j in range(2))
            if r==s:
                for jet in range(2):
                    assert np.array_equal(C[jet],np.diag(np.diag(C[jet])))
                    J[jet,:,ell]=np.diag(C[jet])
    M=np.zeros((2,N+1),dtype=np.int64)
    for ell in range(d):
        for jet in range(2):
            M[jet,ell+1]=sum(int(F[j][ell+1,ell])*T[ell+1,ell][jet-j]
                             +int(EK[j][ell,ell+1])*T[ell,ell+1][jet-j]
                             for j in range(jet+1))%p
    R=np.zeros((2,N),dtype=np.int64)
    for ell in range(N):
        for jet in range(2):
            R[jet,ell]=sum(int(L[j,a+1]-L[j,a])*int(J[jet-j,a,ell])
                           for j in range(jet+1) for a in range(N))%p
            assert (M[jet,ell+1]-M[jet,ell])%p==R[jet,ell]
            rhs=sum(int(L[j,a+1])*int(J[jet-j,a,ell]-J[jet-j,a+1,ell])
                    for j in range(jet+1) for a in range(d))%p
            assert rhs==R[jet,ell]
    assert np.all(np.sum(R,axis=1)%p==0)
    assert np.all(np.sum(J,axis=2)%p==np.array(z)[:,None])
    for jet in range(2):
        assert sum(T[ell,ell][jet] for ell in range(N))%p==z[jet]
    # Root-only cyclic completion: no generic endpoint or q-normal substituted.
    fourier_entries=fourier_currents=0
    Dcdual=(dualF[0]-dualE[0]-2*dualK[0])%p
    for j in range(N):
        X=np.array([[pow(q,2*j*(s-r),p)*pow(N,-1,p)%p
                     for s in range(N)] for r in range(N)],dtype=np.int64)
        routed=mm(mm(Ui,embed_one(const(X),0,inwidth,N,p),p),U,p)
        CX=partial(mm(mm(A,routed,p),B,p),g,outwidth,N,p)
        assert np.array_equal(CX[0],z[0]*X%p)
        E0,F0,K0,Ki0=E[0],F[0],K[0],Ki[0]
        adF=(F0@X-Ki0@X@K0@F0)%p
        adE=((E0@X-X@E0)@Ki0)%p
        adK=(K0@X@Ki0-X)%p
        DX=(adF-adE-2*adK)%p
        routedD=mm(mm(Ui,embed_one(const(DX),0,inwidth,N,p),p),U,p)
        CD=partial(mm(mm(A,routedD,p),B,p),g,outwidth,N,p)
        actual=int(np.trace(ecut@CD[0])%p)
        predicted=z[0]*((3-q)*int(j==0)+(q-2)*int(j==N-1)-int(j==1))%p
        assert actual==predicted
        assert int(np.trace(Dcdual@CX[0])%p)==predicted
        fourier_entries+=N*N
        fourier_currents+=1
    # Source-defined off-node matrix, with every unwrapped charge retained.
    toeplitz_entries=offnode_entries=offnode_pairings=0
    offnode_normal_defects=offnode_coherent_defects=0
    for charge in range(-d,d+1):
        X=np.diag(np.ones(N-abs(charge),dtype=np.int64),-charge)
        routed=mm(mm(Ui,embed_one(const(X),0,inwidth,N,p),p),U,p)
        CX=partial(mm(mm(A,routed,p),B,p),g,outwidth,N,p)
        assert np.array_equal(CX[0],z[0]*X%p)
        toeplitz_entries+=N*N
    for momentum in (1,2,3):
        X=np.array([[pow(momentum,r-s,p)*pow(N,-1,p)%p
                     for s in range(N)] for r in range(N)],dtype=np.int64)
        routed=mm(mm(Ui,embed_one(const(X),0,inwidth,N,p),p),U,p)
        CX=partial(mm(mm(A,routed,p),B,p),g,outwidth,N,p)
        assert np.array_equal(CX[0],z[0]*X%p)
        factor=(sum(pow(momentum,r,p) for r in range(N))*pow(N,-1,p)
                *pow((1-t+t*pow(momentum,-1,p))%p,d,p))%p
        assert int(np.trace(ecut@CX[0])%p)==z[0]*factor%p
        defect=(CX[1]-z[1]*X)%p
        offnode_entries+=N*N;offnode_pairings+=1
        offnode_normal_defects+=int(np.count_nonzero(defect))
        offnode_coherent_defects+=int(int(np.trace(ecut@defect)%p)!=0)
    # Genuine q-dependent test weights, every subinterval and both jet orders.
    h=np.array([[((ell+2)+pow(q,2*ell,p))%p for ell in range(N)],
                [2*ell*pow(q,2*ell,p)%p for ell in range(N)]],dtype=np.int64)
    intervals=0
    for left in range(N):
        for right in range(left,N):
            for jet in range(2):
                lhs=sum(int(h[j,ell])*int(R[jet-j,ell])
                        for j in range(jet+1) for ell in range(left,right+1))%p
                rhs=sum(int(h[j,right])*int(M[jet-j,right+1])
                        -int(h[j,left])*int(M[jet-j,left])
                        +sum(int(h[j,ell]-h[j,ell+1])*int(M[jet-j,ell+1])
                             for ell in range(left,right)) for j in range(jet+1))%p
                assert lhs==rhs
                intervals+=1
    return dict(N=N,width_in=inwidth,width_out=outwidth,kind=kind,
                actual_band_coefficients=2*(N+2*d),flux_coefficients=2*N,
                finite_interval_jet_identities=intervals,
                nonzero_retained_normal_defects=normal_defects,
                nonzero_current_coefficients=int(np.count_nonzero(M)),
                complete_fourier_matrix_entries=fourier_entries,
                three_node_current_values=fourier_currents,
                unwrapped_toeplitz_entries=toeplitz_entries,
                offnode_root_entries=offnode_entries,
                offnode_coherent_pairings=offnode_pairings,
                nonzero_offnode_normal_entries=offnode_normal_defects,
                nonzero_offnode_coherent_normal_defects=offnode_coherent_defects,
                exposed_scalar=list(z),field=p)


def chain_checks():
    x=sp.symbols('x')
    S=(x+1)/(x-sp.Rational(1,3))
    w=x*x+2*x+3
    count=0
    for d in range(1,8):
        lhs=sum(w.subs(x,n)*(S.subs(x,n+1)-S.subs(x,n)) for n in range(d+1))
        rhs=sum((w.subs(x,n-1)-w.subs(x,n))*S.subs(x,n) for n in range(d+1))
        rhs+=w.subs(x,d)*S.subs(x,d+1)-w.subs(x,-1)*S.subs(x,0)
        assert sp.simplify(lhs-rhs)==0
        count+=1
    A,B,C=sp.symbols('A B C')
    assert sp.residue(sp.pi*sp.cot(sp.pi*x)*(A/x+B+C*x),x,0)==B
    return dict(integer_shift_cotangent_chains=count,retained_resonant_finite_part=1)


def offnode_boundary_checks():
    mp.mp.dps=70
    checks=[]
    for N in (32,65,128,257):
        for rho,t,c0 in ((mp.mpc('1','.3'),mp.mpc('.3','.1'),mp.mpc('.2','-.1')),
                         (mp.mpc('-.7','.8'),mp.mpc('.6','-.2'),mp.mpc('-.3','.2')),
                         (1/(2*mp.pi*1j),mp.mpf('.4'),mp.mpf('.2'))):
            momentum=1-1/(N*rho+c0)
            actual=mp.fsum(momentum**r for r in range(N))/N*(1-t+t/momentum)**(N-1)
            expected=rho*(1-mp.exp(-1/rho))*mp.exp(t/rho)
            scaled=N*abs(actual-expected)
            assert scaled<50
            checks.append(float(scaled))
    return dict(boundary_profile_checks=len(checks),maximum_N_absolute_error=max(checks),
                scope='Literal finite boundary factor, including a limiting Fourier zero; unknown source scalar is not estimated.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    rows=[audit_case(N,2,k) for N in range(2,7) for k in ('braid','complete')]
    rows += [audit_case(N,3,k) for N in (2,3,4) for k in ('braid','complete')]
    rows += [audit_case(N,3,'rectangular') for N in (2,3,4)]
    totals={k:sum(row[k] for row in rows) for k in ('actual_band_coefficients',
        'flux_coefficients','finite_interval_jet_identities','nonzero_retained_normal_defects',
        'complete_fourier_matrix_entries','three_node_current_values',
        'unwrapped_toeplitz_entries','offnode_root_entries','offnode_coherent_pairings',
        'nonzero_offnode_normal_entries','nonzero_offnode_coherent_normal_defects')}
    assert totals['nonzero_offnode_normal_entries']>0
    assert totals['nonzero_offnode_coherent_normal_defects']>0
    result=dict(status='PASS',source_cases=len(rows),totals=totals,cases=rows,
                chain=chain_checks(),offnode=offnode_boundary_checks(),
                scope='Actual routed off-diagonal current and genuine first jets; literal off-node profile is root-only with nonzero generic defects retained. No stationary pushforward or relative framing coefficient.')
    target=args.output or Path(__file__).with_name('actual_braided_residual_framing_current_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',source_cases=len(rows),**totals),indent=2))


if __name__=='__main__':main()
