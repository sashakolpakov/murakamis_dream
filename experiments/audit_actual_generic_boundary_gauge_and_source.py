#!/usr/bin/env python3
"""Actual generic cup gauge, large white numerator, and marked trace normal.

The off-grid ambiguity is an exact scope obstruction, not an assertion
that the physical gauge estimates control complex magnetic coordinates.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_q_hahn_physical_generic_jet_bound import Jet, original
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_matching_edge_antidiagonal_operator_packet import factorials, clebsch, cup
from audit_actual_q_hahn_small_channel_generic_normals import source_S, scalar_K, determinant
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local, mm, kron, trans
from audit_general_odd_endpoint_matching_network import apply_pair


def sqrt_one(x):
    assert x.c[0] == 1
    out = [1]
    for k in range(1, Jet.order):
        out.append((x.c[k]-sum(out[j]*out[k-j] for j in range(1,k)))
                   *pow(2,-1,Jet.p)%Jet.p)
    y=Jet(out)
    assert y*y == x
    return y


def four_jets():
    cups=whites=source=small_fail=0
    for N in range(3,12):
        p,eta=root_field(N);Jet.p=p;Jet.order=4;q0=eta*eta%p
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        qr=Jet(q0);d=N-1;F=factorials(q,d);Fr=factorials(qr,d)
        gauges={}
        for L in range(N):
            gs=[]
            for r in range(L+1):
                b=q**(r*(L-r))*F[r]*F[L-r]/F[L]
                b0=qr**(r*(L-r))*Fr[r]*Fr[L-r]/Fr[L]
                g=sqrt_one(b/b0);gs.append(g)
                actual=cup(L,q,F,r)/g/g
                assert actual == (-1)**r*q**(-r)*b0
                if L==d:assert b0 == 1
                cups+=1
            assert gs == gs[::-1]
            gauges[L]=gs
        for a in range(d//2+1):
            m=d-a
            for r in range(2*a+1):
                t=m+r
                endpoint=q**(-d*r)*F[t]/F[m]/F[r] if r<=a else None
                for i in range(max(0,t-d),min(d,t)+1):
                    U=q**(2*i);T=q**(2*t)
                    H=source_S(N,q,m,U,T)/U**m
                    expected=(-1)**m*q**(-d*r+d*i-m*(m-1))*H/F[m]
                    actual=clebsch(d,a,q,F,i,t-i,r)
                    assert actual == expected
                    if r<=a:assert actual == endpoint*original(N,q,t,m,i,F)
                    source+=1
                    gp=gauges[2*a][r]/gauges[d][i]/gauges[d][t-i]
                    assert gp*actual == gp*expected
                    whites+=1
            if a==0:
                for i in range(1,d):
                    actual=clebsch(d,0,q,F,i,d-i,0)
                    assert actual.c[0] == (q**(d*i)).c[0]
                    assert actual != q**(d*i)
                    primed=actual/gauges[d][i]/gauges[d][d-i]
                    assert primed == (-1)**i*q**(-i)
                    small_fail+=1
    return dict(actual_cup_four_jets=cups,
                original_large_column_and_newton_four_jets=source,
                transformed_white_four_jets=whites,
                retained_small_vs_large_generic_counterexamples=small_fail)


def gauge_jet(loc,L):
    p=loc.p
    h=np.diag([(r*(L-r)+loc.logfac[r]+loc.logfac[L-r]-loc.logfac[L])
               *pow(2,-1,p)%p for r in range(L+1)]).astype(np.int64)
    eye=np.eye(L+1,dtype=np.int64)
    return (eye,h),(eye,-h%p)


def transformed_local(loc):
    p,N=loc.p,loc.N
    G,Gi=gauge_jet(loc,N-1);Gp=kron(G,G,p);Gpi=kron(Gi,Gi,p)
    pc=mm(mm(Gi,loc.cup,p),trans(Gi),p)
    ell=mm(mm(trans(G),loc.cap,p),G,p)
    assert np.array_equal(pc[0],loc.cup[0])
    assert np.array_equal(ell[0],loc.cap[0])
    Wp={};pip={};sectors={};changed=0
    for a in loc.W:
        A,Ai=gauge_jet(loc,2*a)
        Wp[a]=mm(mm(Gpi,loc.W[a],p),A,p)
        pip[a]=mm(mm(Ai,loc.pi[a],p),Gp,p)
        qa=mm(mm(Ai,loc.qcups[a][0],p),trans(Ai),p)
        dual=mm(mm(mm(trans(qa),trans(Wp[a]),p),
                      kron(trans(ell),trans(ell),p),p),loc.P,p)
        dual=tuple(v*pow(loc.gamma[a],-1,p)%p for v in dual)
        assert all(np.array_equal(x,y) for x,y in zip(dual,pip[a]))
        sectors[a]=mm(Wp[a],pip[a],p)
        direct=mm(mm(Gpi,mm(loc.W[a],loc.pi[a],p),p),Gp,p)
        assert all(np.array_equal(x,y) for x,y in zip(sectors[a],direct))
        pair=mm(pip[a],Wp[a],p)
        old=mm(loc.pi[a],loc.W[a],p)
        assert all(np.array_equal(x,y) for x,y in zip(pair,mm(mm(Ai,old,p),A,p)))
        changed+=int(not np.array_equal(Wp[a][1],loc.W[a][1]))
    trace=mm(ell,trans(pc),p)
    assert int(np.trace(trace[0])%p)==0
    assert int(np.trace(trace[1])%p)==loc.nu
    return pc,ell,sectors,changed


def marked_plat(loc,k,primed):
    N,p=loc.N,loc.p
    pc,cap,sectors,_=primed
    oldsectors={a:mm(loc.W[a],loc.pi[a],p) for a in loc.W}
    slots=list(range(1,2*k-2,2))+list(range(0,2*k-1,2))+list(range(1,2*k-2,2))
    signs=[(-1,0,1)[i%3] for i in range(len(slots))]
    marker=np.array([[pow(loc.x,b,p)*pow(N*N,-1,p)%p for b in range(N)]
                     for _ in range(N)],dtype=np.int64)
    def close(cup_,cap_,boxes):
        state=(np.array([1],dtype=np.int64),np.array([0],dtype=np.int64))
        row=state;marked=np.array([1],dtype=np.int64)
        for n in range(k):
            state=kron(state,tuple(v.reshape(-1) for v in cup_),p)
            row=kron(row,tuple(v.reshape(-1) for v in cap_),p)
            marked=np.kron(marked,(marker if n==k-1 else cap_[0]).reshape(-1))%p
        s0=state[0].reshape((N,)*(2*k));s1=state[1].reshape((N,)*(2*k))
        for slot,B in zip(slots,boxes):
            s1=(apply_pair(B[0],s1,slot,N,p)+apply_pair(B[1],s0,slot,N,p))%p
            s0=apply_pair(B[0],s0,slot,N,p)
        z=int(marked@s0.reshape(-1)%p)
        F0=int(row[0]@s0.reshape(-1)%p)
        F1=int((row[1]@s0.reshape(-1)+row[0]@s1.reshape(-1))%p)
        assert F0==0 and F1==loc.nu*z%p
        return F0,F1,z
    low=list(loc.W);M=max(low)
    labels=[tuple([0]*len(slots)),tuple([M]*len(slots)),
            tuple(low[i%len(low)] for i in range(len(slots)))]
    checks=0;nonzero=0
    for js in labels:
        before=close(loc.cup,loc.cap,[oldsectors[a] for a in js])
        after=close(pc,cap,[sectors[a] for a in js])
        assert before==after;checks+=1;nonzero+=int(before[2]!=0)
    def summed(sec):
        return [tuple(sum((loc.h0[a]*pow(loc.omega[a],e,p)*sec[a][j]%p
                           for a in low),np.zeros((N*N,N*N),dtype=np.int64))%p
                      for j in range(2)) for e in signs]
    before=close(loc.cup,loc.cap,summed(oldsectors));after=close(pc,cap,summed(sectors))
    assert before==after;checks+=1;nonzero+=int(before[2]!=0)
    return dict(N=N,bridge_width=k,circles=len(slots),
                marked_trace_normal_equalities=checks,nonzero_marked_values=nonzero,
                complete_label_sum_and_signed_exponents=True)


def large_numerator_checks():
    exact=deficient=retained=0
    for N in range(3,12):
        p,eta=root_field(N);Jet.p=p;Jet.order=4;q0=eta*eta%p
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        d=N-1;F=factorials(q,d);Q=q*q
        for a in range((d-1)//2+1):
            m=d-a;s=m-a
            gap=(q**(2*N-1-2*m)+q**(-2*N+1+2*m)
                 -q**(2*N-1-2*a)-q**(-2*N+1+2*a))
            assert gap == -(q**s-q**(-s))*(q**N-q**(-N))
            for t in sorted(set((m,d))):
                for i in sorted(set((0,t//2,t))):
                    U=q**(2*i);T=q**(2*t)
                    ha=source_S(N,q,a,U,T)/U**a
                    hm=source_S(N,q,m,U,T)/U**m
                    P=math.prod((T-Q**r for r in range(a,m)),start=Jet(1))
                    D=math.prod((T-Q**r for r in range(m)),start=Jet(1))
                    actual=D*(original(N,q,t,m,i,F)-original(N,q,t,a,i,F))/q**(d*i)
                    assert hm-P*ha == actual
                    assert actual.c[0]==0
                    retained+=int(actual.c[1]!=0)
                    exact+=1
            for t in range(a):
                U=Jet(17);T=q**(2*t)
                ha=source_S(N,q,a,U,T)/U**a
                hm=source_S(N,q,m,U,T)/U**m
                P=math.prod((T-Q**r for r in range(a,m)),start=Jet(1))
                assert (hm-P*ha).c[0]==0
                deficient+=1
    mp.mp.dps=150
    circles=roots=cofactors=0;worst=mp.mpf(0);profiles=[]
    for N in (16,17,32,33):
        q0=mp.exp(mp.pi*1j/N);base=1 if N%2==0 else 2
        for s in (base,base+2):
            a=(N-1-s)//2;m=N-1-a
            sigma=N*mp.mpc(str(mp.mpf(1)/6),'.003')
            z=mp.mpc(60,11 if N%2 else -11)
            i=(sigma-mp.log(z)/(mp.pi*1j/N))/2
            def H(n,q):
                U=q**(2*i);T=q**(2*sigma)
                return source_S(N,q,n,U,T)/U**n
            ha0=H(a,q0);hm0=H(m,q0)
            P0=mp.fprod(q0**(2*sigma)-q0**(2*r) for r in range(a,m))
            assert abs(hm0/(P0*ha0)-1)<mp.mpf('1e-110')
            roots+=1
            rho=mp.mpf('.05')/N**10
            maxratio=mp.mpf(0)
            for omega in (1,1j,-1,-1j):
                q=q0*mp.exp(rho*omega);svar=q**sigma;zq=q**(sigma-2*i)
                actual=H(m,q)
                via=svar**m*scalar_K(N,q,m)*determinant(N,q,svar,m,zq)
                error=abs(actual/via-1)
                assert error<mp.mpf('1e-95');worst=max(worst,error);circles+=1
                cofactor=determinant(N,q,svar,a-1,zq)/determinant(N,q,svar,a,zq)
                assert abs(cofactor)<1;cofactors+=1
                maxratio=max(maxratio,abs(actual/hm0))
            profiles.append(dict(N=N,separation=s,
                                 maximum_large_numerator_circle_ratio=mp.nstr(maxratio,30)))
    return dict(original_divided_numerator_four_jets=exact,
                nonzero_transverse_first_normals=retained,
                deficient_integer_total_collision_checks=deficient,
                complex_deficient_root_collisions=roots,
                genuine_large_deficient_circle_identities=circles,
                actual_small_inverse_cofactor_checks=cofactors,
                precision_digits=mp.mp.dps,
                maximum_literal_large_numerator_error=mp.nstr(worst,35),
                profiles=profiles)


def main():
    out=four_jets();rows=[];dualcount=changed=0
    for N in range(3,8):
        loc=Local(N);primed=transformed_local(loc)
        dualcount+=len(loc.W);changed+=primed[3]
        if N<=6:rows.append(marked_plat(loc,2,primed))
        if N in (3,4):rows.append(marked_plat(loc,3,primed))
    out.update(status='PASS',exact_actual_categorical_duals=dualcount,
               changed_white_first_normals=changed,whole_original_plats=rows,
               deficient_large_numerators=large_numerator_checks(),
               scope='Exact physical tensor gauge and actual LARGE generic white numerator. Shrinking-fold numerator and specified unprimed-white upper bounds; no off-grid gauge bound or full exceptional generic operator packet.')
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();path=args.output or Path(__file__).with_name('actual_generic_boundary_gauge_and_source_results.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
