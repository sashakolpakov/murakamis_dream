#!/usr/bin/env python3
"""Exact composed bridge Gram, genuine source bias and coherent optimization."""

import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_half_clock_source_dilation import original_factorial_R


def data(N):
    q=np.exp(1j*np.pi/N);Q=q*q;x=q**(N-1);d=N-1
    F=np.r_[1+0j,np.cumprod(1-Q**np.arange(1,N))]
    s=np.abs(F)
    P=[1+0j]
    for t in range(1,N):P.append((1-Q**t)**2*P[-1]+Q**t)
    V=np.zeros((N,N),complex)
    for n in range(N):
        V[n,0]=1
        for t in range(1,n+1):V[n,t]=V[n,t-1]*(1-Q**(-n+t-1))
    T=(np.diag([(-1)**n*Q**(-n*(n+3)//2)*F[n]for n in range(N)])
       @V@np.diag([Q**t*P[t]/F[t]**4 for t in range(N)])@V.T
       @np.diag([x**(j-d)/F[d-j]for j in range(N)]))
    R=original_factorial_R(N)
    states=[z for z in itertools.product(range(N),repeat=4)if sum(z)==2*d]
    L=np.zeros((N,len(states)),complex)
    charges=np.array([a+b-d for a,b,c,e in states],float)
    cup=np.zeros(len(states),complex)
    for j,(a,b,c,e)in enumerate(states):
        u=d-e
        Gin=np.prod([s[z]/np.sqrt(N)for z in (a,b,c,e)])
        L[u,j]=x**(-a)*Q**(-a)/N*R[(d-a)*N+u,b*N+c]/Gin
        if a+b==d and c+e==d:cup[j]=N*N*x**(-b-e)
    return q,Q,x,F,s,T,L,charges,cup


def row_potential(N,s,delta):
    d=N-1
    E=np.zeros(N);derivative=np.zeros(N)
    for u in range(N):
        for k in range(d-u+1):
            for a in range(d-k+1):
                c=d-k-a
                term=N*N*math.exp(2*delta*(c-u))/(s[a]**4*s[c]**4*s[k]**2)
                E[u]+=term
                derivative[u]+=2*(c-u)*term
    return E,derivative


def run_case(N):
    q,Q,x,F,s,T,L,charges,cup=data(N)
    d=N-1
    def matrices(delta):
        E,derivative=row_potential(N,s,delta)
        M=(T*E[None,:])@T.conj().T
        M=(M+M.conj().T)/2
        D=(T*derivative[None,:])@T.conj().T
        eig,U=np.linalg.eigh(M)
        assert eig[-1]>0
        return math.log(eig[-1]),M,D,U[:,-1]
    rng=np.random.default_rng(89400+N)
    source_image=T@L@cup
    for delta in (-.55,0.,.35):
        E,_=row_potential(N,s,delta)
        Ld=L*np.exp(-delta*charges)[None,:]
        assert np.allclose(Ld@Ld.conj().T,np.diag(E),rtol=2e-7,atol=2e-7)
        K=T@Ld
        lognorm,M,D,eta=matrices(delta)
        assert np.allclose(K@K.conj().T,M,rtol=2e-7,atol=2e-7)
        assert np.allclose(K@cup,source_image,rtol=2e-7,atol=2e-7)
        # An operator-valued exterior: retain both independent Hilbert columns.
        w=rng.normal(size=(len(charges),2))+1j*rng.normal(size=(len(charges),2))
        biased=np.exp(delta*charges)[:,None]*w
        lhs=np.linalg.norm(T@L@w,'fro')**2
        rhs=math.exp(lognorm)*np.linalg.norm(biased,'fro')**2
        assert lhs<=rhs*(1+2e-7)
        assert lognorm>=2*delta*d-4*math.log(N)-1e-7
        assert lognorm>=-2*delta*d-2*math.log(N)-1e-7
        if N<=5:
            epsilon=.25
            completed=K.conj().T@K+epsilon*np.diag(np.exp(-2*delta*charges))
            eigen=np.linalg.eigvalsh((completed+completed.conj().T)/2)
            assert eigen[0]>=epsilon*math.exp(-2*abs(delta)*d)*(1-2e-7)
            assert eigen[-1]>=math.exp(lognorm)*(1-2e-7)
            assert eigen[-1]<=math.exp(lognorm)+epsilon*math.exp(2*abs(delta)*d)+1e-7
    grid=np.linspace(-1.,1.,17)
    values=[matrices(z)[0]for z in grid]
    for i in range(1,len(grid)-1):
        assert values[i]<=(values[i-1]+values[i+1])/2+2e-8
    lo,hi=-2.,2.
    for _ in range(85):
        m1=lo+(hi-lo)/3;m2=hi-(hi-lo)/3
        if matrices(m1)[0]<=matrices(m2)[0]:hi=m2
        else:lo=m1
    optimum=(lo+hi)/2
    value,M,D,eta=matrices(optimum)
    derivative=float(np.vdot(eta,D@eta).real/math.exp(value))
    assert abs(derivative)<2e-5
    assert value<=matrices(0.)[0]+1e-8
    return {'N':N,'full_composed_Gram_and_all_spectator_columns':True,
            'literal_paired_source_fixed_for_all_biases':True,
            'all_input_operator_inequality_and_coercive_bounds':True,
            'log_convexity_grid':True,'optimal_typed_degree_bias':float(optimum),
            'log_optimal_coherent_bridge_constant':float(value),
            'log_unbiased_constant':float(matrices(0.)[0]),
            'optimal_normalized_pair_charge_derivative':derivative}


if __name__=='__main__':
    rows=[run_case(N)for N in range(2,13)]
    result={'status':'PASS','coherent_terminal_bridge_optimization':rows,
            'scope':'sharp local all-input norm in a typed one-parameter family; no global source-volume bound'}
    Path(__file__).with_name('actual_coherent_terminal_bridge_metric_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 11 coherent composed-bridge metrics, source/spectator identities and convex charge optimizations')
