#!/usr/bin/env python3
"""Actual generic large-H hard-edge packet and retained order derivatives.

Exact original-source comparisons are separate from finite convergence
diagnostics. No source period or nonvanishing across Bessel zeros is tested.
"""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S
from audit_high_color_first_normal_r_degree import root_field


def reindexed(q,N,m,U,V):
    Q=q*q;B=Q**(-N);term=q**0;total=term
    for ell in range(m):
        k=m-ell
        ratio=(-B**-1*Q**(-k)*(1-Q**k)*(1-B*Q**k)
               /((1-Q**(ell+1))*(1-B*Q**(ell+1)))
               *(V-Q**ell)/(U*V*(1-Q**(k-1)/U)))
        term*=ratio;total+=term
    return total


def top(q,N,m,U,V):
    Q=q*q;B=Q**(-N)
    out=(-B)**m*Q**(m*(m+1)//2)*(U*V)**m
    for r in range(m):out*=1-Q**r/U
    return out


def exact():
    Q,B=sp.symbols('Q B',nonzero=True)
    def poch(x,n):return sp.prod(1-x*Q**r for r in range(n))
    def c(m,k):return ((-B)**k*Q**(k*(k+1)//2)*poch(Q,m)
                      /poch(Q,k)/poch(Q,m-k)*poch(B*Q**(m-k+1),k)/poch(B*Q,k))
    ratios=0
    for m in range(1,6):
        assert sp.cancel(c(m,m)-(-B)**m*Q**(m*(m+1)//2))==0
        for ell in range(m+1):
            target=((-1)**ell*B**(-ell)*Q**(-m*ell+ell*(ell-1)//2)
                    *poch(Q,m)/poch(Q,ell)/poch(Q,m-ell)
                    *poch(B*Q**(m-ell+1),ell)/poch(B*Q,ell))
            assert sp.cancel(c(m,m-ell)/c(m,m)-target)==0
            ratios+=1
    generic=root=coefficients=0
    for N in range(3,12):
        for atroot in (False,True):
            if atroot:
                p,eta=root_field(N);q0=eta*eta%p
            else:p=1000000007;q0=2
            Jet.p=p;Jet.order=4
            q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
            forbidden={pow(q0,2*r,p) for r in range(N)}
            u=next(n for n in range(2,p) if n not in forbidden)
            U=Jet([u,7,11,13]);V=Jet([u+1,17,19,23])
            for m in range(1,N):
                original=source_S(N,q,m,U,U*V)/U**m
                value=top(q,N,m,U,V)*reindexed(q,N,m,U,V)
                assert original==value
                coefficients+=4
                if atroot:root+=1
                else:generic+=1
    return dict(symbolic_generic_reindexed_coefficients=ratios,
                original_nonroot_H_four_jets=generic,original_root_H_four_jets=root,
                retained_original_coefficients=coefficients)


def packet(N,m,kappa,V0,t):
    q0=mp.exp(mp.pi*1j/N)
    x=mp.log(N*N*kappa)/(2*mp.log(q0));y=mp.log(V0)/(2*mp.log(q0))
    q=mp.exp(mp.pi*1j/N+t/N**2)
    U=mp.exp(2*x*mp.log(q));V=mp.exp(2*y*mp.log(q))
    return reindexed(q,N,m,U,V)


def numeric():
    packet_values=jets=source=top_checks=0
    max_error=mp.mpf(0);max_scaled=mp.mpf(0);max_jet_scaled=mp.mpf(0)
    rows=[]
    kappa=mp.mpc('1.1','.3');V0=mp.mpc('.4','.2')
    for N in (32,65,128,257):
        for fraction in (mp.mpf('.37'),mp.mpf('.5'),mp.mpf('.7')):
            m=int(mp.floor(fraction*(N-1)));mu=mp.mpf(m)/N
            K=mp.sin(mp.pi*mu)**2*(V0-1)/(mp.pi**2*kappa*V0)
            model=lambda t:mp.hyp0f1(1-t/(mp.pi*1j),-K)
            for t in (mp.mpf(0),mp.mpc('.3','.2'),mp.mpc('-.4','.6'),mp.mpc(0,'.7')):
                actual=packet(N,m,kappa,V0,t);pred=model(t)
                err=abs(actual-pred);scaled=N*err/(1+mp.log(N))
                assert scaled<20
                max_error=max(max_error,err);max_scaled=max(max_scaled,scaled);packet_values+=1
            for order in (1,2):
                actual=mp.diff(lambda t:packet(N,m,kappa,V0,t),0,order)
                pred=mp.diff(model,0,order)
                scaled=N*abs(actual-pred)/(1+mp.log(N))
                assert scaled<20
                max_jet_scaled=max(max_jet_scaled,scaled);jets+=1
            rows.append(dict(N=N,m=m,root_error=str(abs(packet(N,m,kappa,V0,0)-model(0)))))
    # Direct terminating source comparisons, not just a ratio recurrence.
    for N in (9,16,25):
        for m in (N//2,2*N//3):
            for t in (mp.mpc('.2','.1'),mp.mpc('-.3','.4')):
                q0=mp.exp(mp.pi*1j/N);q=mp.exp(mp.pi*1j/N+t/N**2)
                x=mp.log(N*N*kappa)/(2*mp.log(q0));y=mp.log(V0)/(2*mp.log(q0))
                U=mp.exp(2*x*mp.log(q));V=mp.exp(2*y*mp.log(q))
                original=source_S(N,q,m,U,U*V)/U**m
                err=abs(original/(top(q,N,m,U,V)*packet(N,m,kappa,V0,t))-1)
                assert err<mp.mpf('1e-65');source+=1
            def Z(t):
                q=mp.exp(mp.pi*1j/N+t/N**2)
                return top(q,N,m,mp.exp(2*x*mp.log(q)),mp.exp(2*y*mp.log(q)))
            Q=q0*q0;U=N*N*kappa
            expected=mp.mpf(-2*N*m+m*(m+1))/N**2+2*m*(x+y)/N**2
            expected-=mp.fsum(2*(r-x)/N**2*(Q**r/U)/(1-Q**r/U) for r in range(m))
            assert abs(mp.diff(Z,0)/Z(0)-expected)<mp.mpf('1e-65')
            top_checks+=1
    # The harmonic currents are independently differentiated from the series.
    K=mp.mpc('.4','.2')
    first=mp.fsum((-K)**ell*mp.harmonic(ell)/mp.factorial(ell)**2 for ell in range(80))/(mp.pi*1j)
    second=mp.fsum((-K)**ell*(mp.harmonic(ell)**2+mp.fsum(mp.mpf(1)/r**2 for r in range(1,ell+1)))
                      /mp.factorial(ell)**2 for ell in range(80))/(mp.pi*1j)**2
    model=lambda t:mp.hyp0f1(1-t/(mp.pi*1j),-K)
    assert abs(first-mp.diff(model,0))<mp.mpf('1e-70')
    assert abs(second-mp.diff(model,0,2))<mp.mpf('1e-70')
    return dict(complex_scaled_parameter_packets=packet_values,genuine_scaled_first_second_normals=jets,
                independent_terminating_source_values=source,retained_top_term_normalizations=top_checks,
                explicit_harmonic_normal_limits=2,maximum_packet_absolute_error=str(max_error),
                maximum_N_over_logN_error=str(max_scaled),maximum_scaled_normal_error=str(max_jet_scaled),
                root_diagnostics=rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    mp.mp.dps=95
    result=dict(status='PASS',precision_digits=mp.mp.dps,exact=exact(),numeric=numeric(),
                scope='Original generic white-numerator hard edge with retained top term and true quantum-normal parameter. No discarded Bessel zeros, whole-operator packet or global period.')
    target=args.output or Path(__file__).with_name('actual_q_hahn_generic_resonant_hard_edge_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
