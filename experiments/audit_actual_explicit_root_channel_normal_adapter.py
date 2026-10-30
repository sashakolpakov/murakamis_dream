#!/usr/bin/env python3
"""Actual divided descendants, routed first normals, and finite Plancherel."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_braided_residual_framing_current import fixture, rectangular_fixture
from audit_actual_braided_two_cut_source_adapter import embed_one, partial, eq
from audit_actual_nc_morse_graph_first_normal_source_reduction import const, mm
from audit_high_color_first_normal_r_degree import root_field


def symbolic_descendants():
    Q=sp.symbols('Q',nonzero=True)
    ladder_entries=descendant_entries=0
    for N in range(2,8):
        d=N-1
        hs=[sp.Integer(1)]
        for s in range(1,N):
            hs.append(sp.cancel(-Q**s*(1-Q**(N-s))/(1-Q**s)*hs[-1]))
        F=sp.zeros(N); K=sp.diag(*[Q**(-a) for a in range(N)])
        for a in range(d):F[a+1,a]=1-Q**(a+1)
        Ki=K.inv()
        def ad(X):return F*X-Ki*X*K*F
        bands={}
        for n in range(-d,d+1):
            V=sp.zeros(N)
            for s in range(max(-n,0),min(d,d-n)+1):
                V[s+n,s]=sp.cancel(hs[s]/hs[max(-n,0)])
            bands[n]=V
        for n in range(-d,d):
            c=1-Q**(n if n<0 else N+n)
            residual=ad(bands[n])-c*bands[n+1]
            for s in range(max(-n-1,0),min(d,d-n-1)+1):
                assert sp.cancel(residual[s+n+1,s])==0
                ladder_entries+=1
            assert all(sp.cancel(x)==0 for x in residual)
        if N<=5:
            raw=sp.zeros(N);raw[0,d]=1
            fac=sp.Integer(1)
            for k in range(2*d+1):
                n=k-d
                expected=fac*hs[max(-n,0)]/hs[d]*bands[n]
                for s in range(max(-n,0),min(d,d-n)+1):
                    assert sp.cancel(raw[s+n,s]-expected[s+n,s])==0
                    descendant_entries+=1
                if k<2*d:
                    raw=ad(raw).applyfunc(sp.expand)
                    fac*=1-Q**(k+1)
    return dict(exact_generic_ladder_entries=ladder_entries,
                exact_canceled_raw_descendants=descendant_entries,
                physical_missing_endpoint_arrows_retained=True)


def root_diagonal(N,q,p):
    hs=[0]
    for s in range(1,N):
        hs.append((hs[-1]+2*N*pow((1-pow(q,2*s,p))%p,-1,p))%p)
    return np.diag(hs).astype(np.int64)


def source_channel(data):
    p,q,g,A,B,U,Ui,outwidth,inwidth=data
    N=len(g[0])
    def channel(X):
        inserted=mm(mm(Ui,embed_one(X,0,inwidth,N,p),p),U,p)
        return partial(mm(mm(A,inserted,p),B,p),g,outwidth,N,p)
    return channel


def source_case(N,width,kind):
    data=rectangular_fixture(N) if kind=='rectangular' else fixture(N,width,kind)
    p,q,g,A,B,U,Ui,outwidth,inwidth=data
    C=source_channel(data)
    I=np.eye(N,dtype=np.int64)
    H=root_diagonal(N,q,p)
    whole=C(const(I));z=tuple(int(x[0,0]) for x in whole)
    assert eq(whole,tuple(zz*I%p for zz in z))
    CH=C(const(H))
    eta=int((CH[0]-z[0]*H)[0,0]%p)
    assert np.array_equal((CH[0]-z[0]*H)%p,eta*I%p)
    extreme=np.zeros_like(I);extreme[0,N-1]=1
    CE=C(const(extreme));lam=tuple(int(x[0,N-1]) for x in CE)
    assert eq(CE,tuple(ll*extreme%p for ll in lam))
    assert lam[0]==z[0] and (lam[1]-z[1])%p==eta
    band_entries=0
    for n in range(1-N,N):
        T=np.diag(np.ones(N-abs(n),dtype=np.int64),-n)
        CT=C(const(T));CTH=C(const(T@H%p))
        assert np.array_equal(CT[0],z[0]*T%p)
        lhs=(CT[1]-z[1]*T)%p
        rhs=(eta*T-CTH[0]+z[0]*(T@H%p))%p
        assert np.array_equal(lhs,rhs)
        # The normalized generic descendant has the actual first jet J_n.
        s0=max(-n,0)
        J=(T@H-int(H[s0,s0])*T)%p
        CJ=C((T,J))
        assert np.array_equal(CJ[1],(lam[1]*T+lam[0]*J)%p)
        band_entries+=N*N
    t=2*pow(3,-1,p)%p
    beta=np.array([int(sp.binomial(N-1,a))*pow(t,a,p)*pow(1-t,N-1-a,p)%p
                   for a in range(N)],dtype=np.int64)
    row=np.outer(beta,np.ones(N,dtype=np.int64))
    offnode_entries=pairings=0
    for momentum in (1,2,3):
        X=np.array([[pow(momentum,r-s,p)*pow(N,-1,p)%p
                     for s in range(N)] for r in range(N)],dtype=np.int64)
        CX=C(const(X));CXH=C(const(X@H%p))
        delta=(CX[1]-z[1]*X)%p
        expected=(eta*X-CXH[0]+z[0]*(X@H%p))%p
        assert np.array_equal(delta,expected)
        b=int(np.trace(row@X)%p)
        assert b!=0
        paired=int(np.trace(row@delta)%p)
        source=(eta*b-int(np.trace(row@CXH[0])%p)
                +z[0]*int(np.trace(row@X@H)%p))%p
        assert paired==source
        assert paired*pow(b,-1,p)%p==source*pow(b,-1,p)%p
        # Actual p(epsilon) dependence adds no first-defect term.
        X1=np.array([[(r-s)*int(X[r,s])%p for s in range(N)]
                     for r in range(N)],dtype=np.int64)
        moving=C((X,X1))
        assert np.array_equal((moving[1]-z[1]*X-z[0]*X1)%p,delta)
        offnode_entries+=N*N;pairings+=1
    return dict(N=N,width_in=inwidth,width_out=outwidth,kind=kind,
                scalar_eta_identity=1,actual_extreme_normal=1,
                actual_band_adapter_entries=band_entries,
                actual_normalized_descendant_jet_entries=band_entries,
                actual_offnode_adapter_entries=offnode_entries,
                original_coherent_period_identities=pairings,
                genuine_moving_momentum_identities=pairings,
                field=p,root_scalar=z[0],eta=eta)


def composition_checks():
    count=0
    for N in (2,3,4):
        dc=fixture(N,2,'braid');dd=fixture(N,2,'complete')
        p,q=dc[:2];C=source_channel(dc);D=source_channel(dd)
        I=np.eye(N,dtype=np.int64);H=root_diagonal(N,q,p)
        CI=C(const(I));DI=D(const(I))
        zc=int(CI[0][0,0]);zd=int(DI[0][0,0])
        ec=int((C(const(H))[0]-zc*H)[0,0]%p)
        ed=int((D(const(H))[0]-zd*H)[0,0]%p)
        for first,second,z1,z2,e1,e2 in ((C,D,zc,zd,ec,ed),(D,C,zd,zc,ed,ec)):
            for X in (I,H):
                actual=first(second(const(X)))[0]
                predicted=z1*z2*X
                if X is H:predicted=predicted+(z1*e2+e1*z2)*I
                assert np.array_equal(actual%p,predicted%p)
                count+=1
    return dict(actual_composed_channel_restrictions=count)


def finite_fourier_and_pivot():
    dft=variance=pivots=0
    for N in range(2,33):
        p,eta=root_field(N);q=eta*eta%p;Q=q*q%p
        H=np.diag(root_diagonal(N,q,p)).tolist()
        invN=pow(N,-1,p)
        mean=sum(H)*invN%p
        Hb=[0]
        for s in range(1,N):
            Hb.append((Hb[-1]+2*N*pow((1-pow(Q,-s,p))%p,-1,p))%p)
        meanb=sum(Hb)*invN%p
        for k in range(1,N):
            ahat=sum(pow(Q,-k*s,p)*pow((1-pow(Q,s,p))%p,-1,p)
                     for s in range(1,N))%p
            assert ahat==((N-1)*pow(2,-1,p)-k)%p
            hhat=sum(int(H[s])*pow(Q,-k*s,p) for s in range(N))%p
            assert hhat==(-2*N*k*pow((1-pow(Q,-k,p))%p,-1,p))%p
            dft+=1
        lhs=sum((int(H[s])-mean)*(int(Hb[s])-meanb) for s in range(N))*invN%p
        rhs=4*sum(k*k*pow(((1-pow(Q,k,p))*(1-pow(Q,-k,p)))%p,-1,p)
                  for k in range(1,N))%p
        assert lhs==rhs;variance+=1
        g=[pow(-1,N-1,p)*pow(q,N-1-2*s,p)%p for s in range(N)]
        nu=sum((N-1-2*s)*g[s] for s in range(N))%p
        assert sum(g)%p==0 and nu!=0
        assert sum(g[s]*int(H[s]) for s in range(N))%p==-nu%p
        for momentum in (1,2):
            X=np.array([[pow(momentum,r-s,p)*invN%p for s in range(N)]
                         for r in range(N)],dtype=np.int64)
            tau1=sum((N-1-2*s)*g[s]*int(X[s,s]) for s in range(N))%p
            B1=(nu*X-tau1*np.eye(N,dtype=np.int64))%p
            expected=nu*(X-invN*np.eye(N,dtype=np.int64))%p
            assert np.array_equal(B1,expected);pivots+=1
    return dict(exact_nonzero_fourier_modes=dft,exact_parseval_variances=variance,
                actual_pivotal_free_channel_normals=pivots)


def analytic_norm_checks():
    mp.mp.dps=90
    worst=mp.mpf(0);cases=0
    for N in (2,3,4,5,8,11,20,31,64,101):
        Q=mp.exp(2j*mp.pi/N)
        hs=[mp.mpc(0)]
        for s in range(1,N):hs.append(hs[-1]+2*N/(1-Q**s))
        avg=mp.fsum(hs)/N
        R2=mp.fsum(abs(x-avg)**2 for x in hs)/N
        exact=4*mp.fsum(k*k/abs(1-Q**k)**2 for k in range(1,N))
        err=abs(R2/exact-1)
        assert err<mp.mpf('1e-80')
        assert R2<=mp.mpf(N*N*(N*N-1))/3
        worst=max(worst,err)
        for rho in (mp.mpc('1','.3'),mp.mpc('-.7','.8')):
            momentum=1-1/(N*rho+mp.mpf('.2'))
            bound=mp.exp(N*abs(mp.log(abs(momentum))))
            norm2=mp.fsum(abs(momentum**(r-s)/N)**2 for r in range(N) for s in range(N))
            prod2=mp.fsum(abs(momentum**(r-s)*(hs[s]-avg)/N)**2
                         for r in range(N) for s in range(N))
            assert norm2<=bound**2*(1+mp.mpf('1e-80'))
            assert prod2<=bound**2*R2*(1+mp.mpf('1e-80'))
            cases+=1
    return dict(precision_digits=90,actual_boundary_norm_checks=cases,
                maximum_relative_parseval_error=str(worst))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    symbolic=symbolic_descendants()
    rows=[source_case(N,2,k) for N in range(2,7) for k in ('braid','complete')]
    rows += [source_case(N,3,k) for N in (2,3,4) for k in ('braid','complete')]
    rows += [source_case(N,3,'rectangular') for N in (2,3,4)]
    keys=('scalar_eta_identity','actual_extreme_normal','actual_band_adapter_entries',
          'actual_normalized_descendant_jet_entries','actual_offnode_adapter_entries',
          'original_coherent_period_identities','genuine_moving_momentum_identities')
    totals={key:sum(row[key] for row in rows) for key in keys}
    result=dict(status='PASS',symbolic=symbolic,source_cases=len(rows),totals=totals,
                cases=rows,composition=composition_checks(),finite=finite_fourier_and_pivot(),
                norm=analytic_norm_checks(),
                scope='Explicit genuine first-normal defect from two full-root channel insertions. Polynomial adapter norm, not a bound by the scalar z or a geometric period coefficient.')
    target=args.output or Path(__file__).with_name('actual_explicit_root_channel_normal_adapter_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
