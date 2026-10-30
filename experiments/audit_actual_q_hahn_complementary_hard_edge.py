#!/usr/bin/env python3
"""Exact generic complementation and original outgoing root determinants."""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S, gauss
from audit_high_color_first_normal_r_degree import root_field


def exact():
    checks=0
    for N in range(3,12):
        for root in (False,True):
            if root:p,eta=root_field(N);q0=eta*eta%p
            else:p=1000000007;q0=2
            Jet.p=p;Jet.order=4
            q=Jet([q0*pow(math.factorial(j),-1,p)%p for j in range(4)])
            U=Jet([3,5,7,11]);V=Jet([17,19,23,29]);A0=q**(2*(N-1))
            for m in range(N):
                H=lambda u,v:source_S(N,q,m,u,u*v)/u**m
                assert H(A0/V,A0/U)==A0**m/(U*V)**m*H(U,V)
                checks+=1
    # Independent exact actual paired-circle matrix, no numerical framing.
    a,b,z,e=sp.symbols('a b z e',nonzero=True)
    A=sp.Matrix([[a,-(a+1)**2/4],[4,-2-a]])
    B=sp.Matrix([[-1,-1],[0,-1]]);P=B*A;C=sp.eye(2)+b*(P+sp.eye(2))
    W=A.inv()*e*sp.Matrix([[1,z],[0,1]])
    O=C.inv()*A*C*W
    assert sp.cancel(W[1,0]+4*e)==0
    assert sp.cancel(O[1,0]-16*e*b*b)==0
    assert sp.cancel(-W[1,0]/O[1,0]-1/(4*b*b))==0
    return dict(actual_generic_reciprocity_four_jets=checks,
                retained_reciprocity_coefficients=4*checks,actual_paired_circle_identities=3)


def matrices(N,a):
    th=np.pi/N;n=np.arange(a);j=np.arange(1,a)
    diag=1/(np.cos(n*th)*np.cos((n+1)*th))
    bn=np.sin(j*th)**2/(np.cos(j*th)**2*np.sin((2*j-1)*th)*np.sin((2*j+1)*th))
    upper=np.sqrt(bn)*(np.sin(j*th)+1j*np.cos(j*th))
    Hp=np.diag(diag).astype(complex)+np.diag(upper,1)+np.diag(np.conj(upper),-1)
    return Hp,np.conj(Hp)


def positive_checks():
    matrices_count=pivots=0;worst=float('inf')
    for N in (6,9,16,33,64,129):
        for a in sorted(set((1,(N-1)//4,(N-1)//2))):
            if a<1:continue
            Hp,Hm=matrices(N,a)
            ev=np.linalg.eigvalsh(2*Hm+8*np.eye(a)-Hp)
            assert min(ev)>-1e-8
            worst=min(worst,float(min(ev)));matrices_count+=1
            th=np.pi/N
            for n in range(1,a):
                bn=np.sin(n*th)**2/(np.cos(n*th)**2*np.sin((2*n-1)*th)*np.sin((2*n+1)*th))
                pn=np.sin(n*th)/(np.cos(n*th)*np.sin((2*n-1)*th))
                ratio=bn*np.cos(n*th)**2/pn
                assert abs(ratio-np.sin(2*n*th)/(2*np.sin((2*n+1)*th)))<1e-10
                assert ratio<=1+1e-12;pivots+=1
    return dict(actual_folded_matrix_comparisons=matrices_count,
                exact_formula_pivot_evaluations=pivots,minimum_comparison_eigenvalue=worst)


def det_pair(N,a,U,V=None):
    if a==0:return mp.mpf(1)
    th=mp.pi/N;q=mp.exp(1j*th)
    c1=q*U/2;c2=0 if V is None else 1/(2*q*V)
    previous=mp.mpf(1);now=1-(c1+c2)/mp.cos(th)
    for n in range(1,a):
        sn=mp.sin(n*th);cn=mp.cos(n*th)
        bn=sn**2/(cn**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
        prod=bn*((c1+c2)**2*sn**2+(c1-c2)**2*cn**2)
        diag=1-(c1+c2)/(cn*mp.cos((n+1)*th))
        previous,now=now,diag*now-prod*previous
    return now


def low_series(q,N,m,U,V):
    Q=q*q;B=Q**(-N)
    term=mp.fprod(V-Q**r for r in range(m));out=term
    for k in range(m):
        ratio=(-B*Q**(k+1)*(1-Q**(m-k))*(1-B*Q**(m-k))
               /((1-Q**(k+1))*(1-B*Q**(k+1))))
        term*=ratio*V*(U-Q**k)/(V-Q**(m-k-1));out+=term
    return out


def numeric():
    exact_det=large_partners=low=normal=rate=0;max_identity=mp.mpf(0);max_rate=mp.mpf(0)
    for N in (5,8,11,16):
        q=mp.exp(mp.pi*1j/N);Q=q*q
        for a in range((N-1)//2+1):
            U=-(mp.mpf('.7')+.13j)/q;V=mp.mpc(31,7)
            original=source_S(N,q,a,U,U*V)/U**a
            expected=V**a*gauss(Q,2*a,a)*det_pair(N,a,U,V)
            err=abs(original/expected-1)
            assert err<mp.mpf('1e-65');max_identity=max(max_identity,err);exact_det+=1
            m=N-1-a
            big=source_S(N,q,m,U,U*V)/U**m
            expected*=mp.fprod(U*V-Q**r for r in range(a,m))
            err=abs(big/expected-1)
            assert err<mp.mpf('1e-65');max_identity=max(max_identity,err);large_partners+=1
    for N in (32,65,128,257):
        a=(N-1)//2;q=mp.exp(mp.pi*1j/N)
        for beta in (mp.mpf('.3'),mp.mpf('1.4')):
            U=-beta/q;V=N*N*mp.mpc('.8','.2')
            ratio=det_pair(N,a,U,V)/det_pair(N,a,U)
            scaled=N*abs(ratio-1)
            assert scaled<20;max_rate=max(max_rate,scaled);rate+=1
        m=N//2;mu=mp.mpf(m)/N;U0=mp.mpc('.4','.2');v0=mp.mpc('1.1','.3');V0=v0/N**2
        x=mp.log(U0)/(2*mp.log(q));y=mp.log(V0)/(2*mp.log(q));A0=q**(2*(N-1))
        kp=A0/v0;vp=A0/U0;K=mp.sin(mp.pi*mu)**2*(vp-1)/(mp.pi**2*kp*vp)
        def packet(t):
            qt=mp.exp(mp.pi*1j/N+t/N**2);Qt=qt*qt;Bt=Qt**(-N)
            U=mp.exp(2*x*mp.log(qt));V=mp.exp(2*y*mp.log(qt))
            Z=(-1)**m*Qt**(m*(m-1)//2)*mp.fprod(1-Bt*Qt**(r+1)*V for r in range(m))
            return low_series(qt,N,m,U,V)/Z
        model=lambda t:mp.hyp0f1(1-t/(mp.pi*1j),-K)
        for t in (mp.mpf(0),mp.mpc('.3','.4')):
            scaled=N*abs(packet(t)-model(t))/(1+mp.log(N))
            assert scaled<20;low+=1
        for order in (1,2):
            scaled=N*abs(mp.diff(packet,0,order)-mp.diff(model,0,order))/(1+mp.log(N))
            assert scaled<20;normal+=1
    return dict(original_small_H_determinants=exact_det,original_large_partner_determinants=large_partners,
                root_220_relative_rates=rate,generic_002_packets=low,genuine_002_first_second_normals=normal,
                maximum_source_identity_error=str(max_identity),maximum_N_scaled_220_error=str(max_rate))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    mp.mp.dps=95
    result=dict(status='PASS',precision_digits=mp.mp.dps,exact=exact(),positive=positive_checks(),numeric=numeric(),
                scope='Exact generic complemented source and root outgoing numerator packet. No generic220 partner differentiation, completed cup packet or global selected period.')
    target=args.output or Path(__file__).with_name('actual_q_hahn_complementary_hard_edge_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
