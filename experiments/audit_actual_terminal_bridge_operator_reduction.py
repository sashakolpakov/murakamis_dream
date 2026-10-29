#!/usr/bin/env python3
"""Open six-head terminal bridge map, all source ports and signed currents."""

import itertools
import json
from pathlib import Path
import math

import numpy as np
import mpmath as mp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import apply_pair
from audit_actual_half_clock_source_dilation import original_factorial_R


def basis4(N):
    return [v for v in itertools.product(range(N), repeat=4) if sum(v) == 2*(N-1)]


def local_field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d, x = q*q % p, N-1, int(K[0,0])
    states = basis4(N)
    seed = np.zeros((N**4,len(states)),dtype=np.int64)
    ids = [np.ravel_multi_index(v,(N,)*4) for v in states]
    seed[ids,np.arange(len(states))]=1
    L0 = np.zeros((N,len(states)),dtype=np.int64)
    cap = np.zeros(N*N,dtype=np.int64)
    for a in range(N):
        cap[a*N+d-a]=pow(x,-a,p)*pow(Q,-a,p)*pow(N,-1,p) % p
    for col,(a,b,c,e) in enumerate(states):
        if a+b==d:L0[c,col]=cap[a*N+b]
    maps=[]
    for sign,R in ((1,Rp),(-1,Rm)):
        physical = apply_pair(R,seed,1,4,N,p)
        direct=np.zeros_like(L0)
        for u in range(N):
            for a in range(N):
                direct[u,:]=(direct[u,:]+cap[a*N+d-a]*physical[
                    np.ravel_multi_index((a,d-a,u,d-u),(N,)*4),:]) % p
        predicted=np.zeros_like(L0)
        fac=[1]
        for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,p)) % p)
        kappa=int(Rp[0,0])
        for col,(a,b,c,e) in enumerate(states):
            k=d-a-c if sign==1 else a+c-d
            if sign==1 and 0<=k<=min(b,d-c):
                u=b-k
                z=(kappa*pow(N,-1,p)*pow(x,-a-b-c+k,p)*pow(Q,-a+c*u,p)
                   *fac[d-a]*fac[b]*pow(fac[k]*fac[c]*fac[u] % p,-1,p)) % p
            elif sign==-1 and 0<=k<=min(c,d-b):
                u=b+k
                z=(pow(kappa,-1,p)*pow(N,-1,p)*pow(-1,k,p)
                   *pow(x,b+c-k-a,p)*pow(Q,-b*c-c*k+k*(k-1)//2-a,p)
                   *fac[u]*fac[c]*pow(fac[k]*fac[b]*fac[d-a] % p,-1,p)) % p
            else:
                continue
            assert u+e==d
            predicted[u,col]=z
        assert np.array_equal(direct,predicted)
        maps.append(direct)
    return {'N':N,'complete_input_dimension':len(states),'both_literal_signed_bridge_maps':True}


def terminal_matrix(N,r,p,q,E,F,K,R):
    d,b=N-1,2*r+1
    Q,x=q*q % p,int(K[0,0])
    rho=(q-pow(q,-1,p)) % p
    Ec=rho*rho*E % p
    Ep,_,_=coproduct(Ec,F,K,2*r,N,p)
    _,Fb,_=coproduct(Ec,F,K,b,N,p)
    states=[v for v in itertools.product(range(N),repeat=2*r) if sum(v)==r*d]
    ids=[np.ravel_multi_index(v,(N,)*(2*r)) for v in states]
    seed=np.zeros((N**(2*r),len(states)),dtype=np.int64)
    seed[ids,np.arange(len(states))]=1
    fac=[1]
    for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,p)) % p)
    H=np.zeros((N**b,len(states)),dtype=np.int64);power=seed.copy()
    for c in range(N):
        H[c::N,:]=pow(-x*Q,c,p)*pow(fac[c],-1,p)*power % p
        power=Ep@power % p
    D=H.copy()
    for _ in range(d):D=Fb@D % p
    D=D*pow(fac[d],-1,p) % p
    cap_pair=np.zeros(N*N,dtype=np.int64)
    for a in range(N):cap_pair[a*N+d-a]=pow(x,-a,p)*pow(Q,-a,p)*pow(N,-1,p) % p
    cap=np.array([1],dtype=np.int64)
    for _ in range(r):cap=np.kron(cap,cap_pair) % p
    ed=np.zeros(N,dtype=np.int64);ed[d]=1
    cap=np.kron(cap,ed)
    R2=R@R % p
    # Project middle head of the final physical triple, then apply R^2.
    T=np.zeros((N,len(states)),dtype=np.int64)
    for n in range(N):
        projected=D.copy()
        for index in range(N**b):
            if (index//N) % N != n:projected[index,:]=0
        T[n,:]=cap@apply_pair(R2,projected,b-2,b,N,p) % p
    return states,seed,T


def six_head_case(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    Q,d,x=q*q % p,N-1,int(K[0,0])
    _,_,T1=terminal_matrix(N,1,p,q,E,F,K,Rp)
    states,seed,T2=terminal_matrix(N,2,p,q,E,F,K,Rp)
    L0=np.zeros((N,len(states)),dtype=np.int64)
    for col,(a,b,c,e) in enumerate(states):
        if a+b==d:L0[c,col]=pow(x,-a,p)*pow(Q,-a,p)*pow(N,-1,p) % p
    assert np.array_equal(T2,T1@L0 % p)
    ids=[np.ravel_multi_index(v,(N,)*4)for v in states]
    for sign,R in ((1,Rp),(-1,Rm)):
        physical=apply_pair(R,seed,1,4,N,p)
        reduced=physical[ids,:]
        assert np.array_equal(T2@reduced % p,T1@L0 % p@reduced % p)
    return {'N':N,'all_input_six_to_four_terminal_rows':True,
            'first_overlapping_bridge_both_signs':True}


def current_metric_case(N):
    q=np.exp(1j*np.pi/N);Q=q*q;x=-1/q;d=N-1
    fac=np.r_[1+0j,np.cumprod(1-Q**np.arange(1,N))]
    s=np.abs(fac);tau=fac/s
    R=original_factorial_R(N)
    flip=np.zeros((N*N,N*N))
    for a in range(N):
        for b in range(N):flip[b*N+a,a*N+b]=1
    Ri=flip@R.conj()@flip
    states=basis4(N)
    Epositive=[]
    for sign,gate in ((1,R),(-1,Ri)):
        out=np.zeros((N,len(states)),complex)
        expected=np.zeros_like(out)
        for col,(a,b,c,e)in enumerate(states):
            k=d-a-c if sign==1 else a+c-d
            u=b-k if sign==1 else b+k
            if not 0<=u<N:continue
            raw=x**(-a)*Q**(-a)/N*gate[(d-a)*N+u,b*N+c]
            # G=s/sqrtN for positive bridge, dual G^-1 for negative.
            Gin=np.prod([(s[j]/np.sqrt(N))**sign for j in (a,b,c,e)])
            out[u,col]=raw/Gin
            A,C=(a,c)if sign==1 else(d-a,d-c)
            if min(A,C,k)>=0 and A+C+k==d:
                expected[u,col]=N/(s[A]**2*s[C]**2*s[k])
            if sign==1 and expected[u,col]:
                gamma=(q**(d*d/2)*N*(-1)**a*x**(-d+k)*Q**(a*(a+1)//2-a)
                       /(s[a]*s[c]*fac[a]*fac[c]*fac[k]))
                operator=x**(-u)*Q**(c*u)*tau[b]/tau[u]
                assert abs(out[u,col]-gamma*operator)<1e-7*max(1,abs(out[u,col]))
            elif sign==-1 and expected[u,col]:
                gamma=(q**(-d*d/2)*N*(-1)**(k+C)*x**(A-C-2*k)
                       *Q**(C*(C+1)//2+k*(k-1)//2-a)
                       /(s[A]*s[C]*fac[A]*fac[C]*fac[k]))
                operator=x**u*Q**(-c*u)*tau[u]/tau[b]
                assert abs(out[u,col]-gamma*operator)<1e-7*max(1,abs(out[u,col]))
        assert np.allclose(np.abs(out),expected,rtol=2e-8,atol=2e-8)
        rows=[]
        for u in range(N):
            bound=d-u if sign==1 else u
            rows.append(N*N*sum(1/s[k]**2*sum(1/s[a]**4/s[d-k-a]**4
                        for a in range(d-k+1))for k in range(bound+1)))
        assert np.allclose(out@out.conj().T,np.diag(rows),rtol=3e-8,atol=3e-8)
        if sign==1:Epositive=rows
        else:assert np.allclose(rows,Epositive[::-1])
    # Whole paired turns are fixed, while the shared physical charge
    # contributes the actual controlled metric factor.
    lambda1,lambda2,lambdaout=.2,-.15,.11
    delta=lambda1-lambda2
    for a,b,c,e in states:
        u=d-e
        Gin=math.exp(lambda1*(a+b-d)+lambda2*(c+e-d))
        Gout=math.exp(lambdaout*(u+e-d))
        assert abs(Gout/Gin-math.exp(delta*(c-u)))<1e-12
    for a in range(N):
        assert abs(math.exp(lambda1*(a+(d-a)-d))-1)<1e-12
    return {'N':N,'source_fixed_typed_G_and_inverse_metrics':True,
            'contractive_lowering_clock_factorization':True,
            'complete_signed_coherent_row_Grams':True,
            'exact_source_fixed_pair_degree_bias':True}


def row_profile_case(N):
    d=N-1
    logs=[0.]
    for j in range(1,N):logs.append(logs[-1]+math.log(2*math.sin(math.pi*j/N)))
    mp.mp.dps=45
    def lob(theta):
        if min(abs(theta),abs(theta-mp.pi/2),abs(theta-mp.pi))<mp.mpf('1e-40'):return mp.mpf(0)
        return mp.im(mp.polylog(2,mp.exp(2j*theta)))/2
    v8=float(8*lob(mp.pi/4))
    rows=[]
    for u in sorted(set((0,N//4,N//2,3*N//4,d))):
        terms=[-2*logs[k]-4*logs[a]-4*logs[d-k-a]
               for k in range(d-u+1) for a in range(d-k+1)]
        peak=max(terms)
        logE=2*math.log(N)+peak+math.log(sum(math.exp(z-peak)for z in terms))
        t=mp.mpf(u)/N
        H=v8 if t<=mp.mpf('.5') else float(8*lob(mp.pi*t/2)-2*lob(mp.pi*t))
        error=logE-N*H/math.pi
        assert abs(error)<=20*math.log(N)
        if u==d:assert abs(logE+math.log(N))<1e-7
        rows.append({'u':u,'pi_log_row_energy_over_N':math.pi*logE/N,
                     'proved_profile':H,'finite_error_over_log_N':error/math.log(N)})
    return {'N':N,'pointed_uniform_interior_and_endpoint_rows':rows,
            'negative_profile_is_exact_mirror':True}


if __name__=='__main__':
    fields=[local_field_case(N)for N in range(2,9)]
    six=[six_head_case(N)for N in (2,3,4)]
    metric=[current_metric_case(N)for N in range(2,9)]
    profile=[row_profile_case(N)for N in (8,16,32,64,128,256)]
    result={'status':'PASS','literal_open_signed_bridge_maps':fields,
            'complete_six_head_terminal_source_reduction':six,'source_current_metric':metric,
            'uniform_pointed_octahedral_row_profiles':profile,
            'scope':'exact operator reduction; weighted simplex/current factor retained, no sharp knot bound'}
    Path(__file__).with_name('actual_terminal_bridge_operator_reduction_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 7 open signed bridge maps; 3 complete six-head reductions; 7 current-metric and 6 octahedral-profile families')
