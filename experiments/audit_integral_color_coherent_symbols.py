#!/usr/bin/env python3
"""Exact actual source-frame identities and moving-q pole checks."""

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as S


def qnum(j,q):
    return sum(q**(j-1-2*r) for r in range(j)) if j else S.Integer(0)


def zero(expr):
    assert S.cancel(S.expand(expr))==0


def same(a,b):
    for x in a-b:zero(x)


def exact_symbols():
    q,v,t=S.symbols('q v T',nonzero=True)
    rho=q-1/q; Q=q*q
    records=[]
    for N in range(2,7):
        n=N-1
        E=S.zeros(N);F=S.zeros(N);K=S.diag(*(q**(n-2*j) for j in range(N)))
        Es=S.zeros(N);Fs=S.zeros(N);Eb=S.zeros(N);Fb=S.zeros(N)
        for j in range(N):
            if j:
                E[j-1,j]=rho*qnum(j,q)*qnum(N-j,q)/S.Integer(N-j)
                Es[j-1,j]=rho*qnum(j,q)
                Eb[j-1,j]=-q**(N-2*j)+q**(-N)
            if j<n:
                F[j+1,j]=rho*(n-j)
                Fs[j+1,j]=rho*qnum(n-j,q)
                Fb[j+1,j]=1-Q**(j+1)
        # Use the exactly equivalent T-coordinate kernel, avoiding expansion
        # of the same common (1+vz)^n denominator many times.
        sigma=lambda C:sum(v**(i-j)*C[i,j]*S.binomial(n,j)*t**j*(1-t)**(n-j)
                          for i in range(N) for j in range(N))
        R=lambda x:1+(x-1)*t
        W=q**N+q**(-N)-q**(-N)*R(Q)**N-q**N*R(1/Q)**N
        Eformula=W/(N*rho*v*(1-t))
        zero(sigma(E)-Eformula)
        zero(sigma(F)-n*rho*v*(1-t))
        zero(sigma(K)-q**n*R(1/Q)**n)
        zero(sigma(Es)-(R(q)**n-R(1/q)**n)/v)
        zero(sigma(Fs)-v*(q**n*R(1/q)**n-q**(-n)*R(q)**n))
        H=S.cancel(W/(N*rho*t*(1-t)))
        zero(H.subs(t,0)-(q**n-q**(-n)))
        zero(H.subs(t,1)-(q**n-q**(-n)))
        same(F*E+q*K+K.inv()/q,(q**N+q**(-N))*S.eye(N))
        ds=[S.Integer(1)];gs=[S.Integer(1)]
        for j in range(n):
            ds.append(S.cancel(ds[-1]*(1-Q**(j+1))/(rho*(n-j))))
            gs.append(S.cancel(gs[-1]*(n-j)/qnum(n-j,q)))
        D=S.diag(*ds);G=S.diag(*gs)
        same(D.inv()*Eb*D,E);same(D.inv()*Fb*D,F)
        same(G.inv()*E*G,Es);same(G.inv()*F*G,Fs)
        same(D.inv()*K*D,K)
        same(G.inv()*K*G,K)
        records.append({'level':N,'all_finite_generator_symbols':True,
                        'both_removed_endpoint_values':True,'actual_quantum_Casimir':True,
                        'balanced_ordinary_symmetric_diagonal_adapters':True})
    return records


def principal_flags():
    s,T,v=S.symbols('s T v',nonzero=True)
    m=S.exp(s/2);k=m*S.exp(-s*T)
    es=2*S.sinh(s*T/2)/v
    fs=2*v*S.sinh(s*(1-T)/2)
    expand=lambda x:S.simplify(S.expand_power_exp(S.expand_trig(x.rewrite(S.exp))))
    for expression in [es*fs-(m+1/m-k-1/k),
                       k+es*S.exp(s*(1-T)/2)*v-m]:
        assert expand(expression)==0
    minus=-S.exp(-s*T/2)*S.sinh(s*(1-T)/2)/S.sinh(s*T/2)*v
    assert expand(k+es*minus-1/m)==0
    b=2*S.sinh(s*(1-T)/2)/(s*(1-T))
    eo=(m+1/m-k-1/k)/(s*v*(1-T))
    assert expand(eo-b*es)==0
    return {'both_augmented_flags':True,'ordinary_symmetric_principal_shear':True}


def uniform_pole_checks():
    mp.mp.dps=70
    levels=[8,16,32,64,128]
    lambdas=[mp.mpf(0),mp.mpf('0.125'),mp.mpf('0.5'),mp.mpf('0.9'),mp.mpf(1)]
    base=[mp.mpf(k)/80 for k in range(81)]
    records=[]
    for N in levels:
        worst=mp.mpf(0);n=N-1
        for lam in lambdas:
            s=2j*mp.pi*lam
            q=mp.exp(s/(2*N));rho=q-1/q
            for T in sorted(set(base+[mp.mpf('1e-8'),1-mp.mpf('1e-8'),mp.mpf(1)/N,1-mp.mpf(1)/N])):
                if not s:
                    HN=H=mp.mpf(0)
                elif not T or T==1:
                    HN=q**n-q**(-n)
                    H=2*mp.sinh(s/2)
                else:
                    WN=q**N+q**(-N)-q**(-N)*(1+(q*q-1)*T)**N-q**N*(1+(q**(-2)-1)*T)**N
                    HN=WN/(N*rho*T*(1-T))
                    H=4*mp.sinh(s*T/2)*mp.sinh(s*(1-T)/2)/(s*T*(1-T))
                kN=q**n*(1+(q**(-2)-1)*T)**n
                k=mp.exp(s*(mp.mpf('0.5')-T))
                AN=(1+(q*q-1)*T)**n
                A=mp.exp(s*T)
                errors=[abs(HN-H),abs(n*rho-s),abs(kN-k),abs(AN-A)]
                worst=max(worst,*errors)
        records.append({'level':N,'max_error':float(worst),'N_times_max_error':float(N*worst),
                        'pole_and_near_pole_grid_included':True})
    assert max(x['N_times_max_error'] for x in records)<100
    assert records[-1]['max_error']<records[0]['max_error']/8
    return records


def main():
    result={'exact_frames':exact_symbols(),'principal_flags':principal_flags(),
            'uniform_generator_pole_checks':uniform_pole_checks(),
            'scope':'Generator symbols and exact source frames, not full R-word asymptotics.'}
    out=Path(__file__).with_name('integral_color_coherent_symbols_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact_levels':len(result['exact_frames']),
                      'largest_grid_level':result['uniform_generator_pole_checks'][-1],
                      'all_checks_passed':True,'output':str(out)},indent=2))


if __name__=='__main__':main()
