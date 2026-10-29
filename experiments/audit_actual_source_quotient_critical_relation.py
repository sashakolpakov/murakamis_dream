#!/usr/bin/env python3
"""Actual source faithfulness and a geometric-relation moment scale."""

import json
import math
from pathlib import Path

import numpy as np
import sympy as S

from audit_finite_sum_annihilator import field
from audit_cyclic_steinberg_lattice import rank


def actual_source():
    i=S.I;K=S.diag(i,-i)
    F=S.Matrix([[0,0],[2,0]]);E=S.Matrix([[0,S.Rational(1,2)],[0,0]])
    Et=S.kronecker_product(E,K)+S.kronecker_product(S.eye(2),E)
    Ft=S.kronecker_product(F,S.eye(2))+S.kronecker_product(K.inv(),F)
    Kt=S.kronecker_product(K,K)
    Omega=S.simplify(-4*Ft*Et+i*Kt-i*Kt.inv())
    assert Omega != S.zeros(4) and Omega**2 == S.zeros(4)
    assert all(Omega*T==T*Omega for T in (Et,Ft,Kt))
    units=[]
    for a in range(4):
        for b in range(4):
            unit=S.zeros(4);unit[a,b]=1
            units.append(S.Matrix([v for T in (Et,Ft,Kt) for v in unit*T-T*unit]))
    assert 16-S.Matrix.hstack(*units).rank()==2
    pivot=(-i,i)
    def phi(W,b):
        return S.simplify(sum(np.prod([pivot[x] for x in closed])*
               W[c*2**(b-1)+sum(x*2**(b-2-k) for k,x in enumerate(closed)),
                 a*2**(b-1)+sum(x*2**(b-2-k) for k,x in enumerate(closed))]
               for a in range(2) for c in range(2)
               for closed in __import__('itertools').product(range(2),repeat=b-1))/2)
    gram=S.Matrix([[phi(S.eye(4),2),phi(Omega,2)],
                   [phi(Omega,2),phi(Omega**2,2)]])
    assert gram == S.Matrix([[0,-4],[-4,0]]) and gram.det() != 0
    R=S.eye(4)+i*Omega/4;Ri=S.eye(4)-i*Omega/4
    word=S.eye(8)
    for slot,sign in ((0,1),(1,-1),(0,1),(1,-1)):
        local=R if sign>0 else Ri
        op=S.kronecker_product(local,S.eye(2)) if slot==0 else S.kronecker_product(S.eye(2),local)
        word=op*word
    assert phi(word,3)==5 and phi(S.eye(8),3)==0
    return {"N2_two_head_Gram":str(gram),"original_figure_eight_period":5,
            "local_character_substitution_value":0}


def insertion_rank():
    rows=[]
    for N in range(2,18):
        p,_,q=field(N);Q=q*q%p
        plus=minus=1;weights=[1]
        for n in range(1,N):
            plus=plus*(1-pow(Q,n,p))%p
            minus=minus*(1-pow(Q,-n,p))%p
            weights.append(plus*minus%p)
        assert all(weights)
        gram=np.array([[sum(weights[n]*pow(Q,(a-b)*n,p) for n in range(N))%p
                        for b in range(N)] for a in range(N)],dtype=np.int64)
        rr=rank(gram,p)
        assert rr==N
        B=np.zeros((N,N),dtype=np.int64)
        for n in range(N):
            zn=pow(Q,n+1,p)
            B[n,(n+1)%N]=(2-zn-pow(zn,-1,p))%p
        power=np.eye(N,dtype=np.int64)
        resolvent=np.zeros((N,N),dtype=np.int64)
        for _ in range(N):
            resolvent=(resolvent+power)%p
            power=power@B%p
        assert not power.any()
        eye=np.eye(N,dtype=np.int64);source=np.zeros(N,dtype=np.int64);source[0]=1
        mu=np.array(weights,dtype=np.int64)
        assert np.array_equal(mu@(eye-B)%p,source)
        assert np.array_equal(source@resolvent%p,mu)
        rows.append({"N":N,"field":p,"original_weighted_insertion_rank":rr,
                     "exact_affine_Green_source_and_resolvent":True})
    return rows


def scale(N):
    logs=[0.0];value=0.0
    for n in range(1,N):
        value+=2*math.log(2*math.sin(math.pi*n/N));logs.append(value)
    peak=max(logs);weights=[math.exp(x-peak) for x in logs]
    total=sum(weights)
    moment=sum(w*(2*math.cos(2*math.pi*n/N)-1)**2 for n,w in enumerate(weights))
    return {"N":N,"N_times_critical_relation_moment_ratio":N*moment/total,
            "original_period_exponential_rate":(peak+math.log(total))/N,
            "relation_moment_exponential_rate":(peak+math.log(moment))/N}


def main():
    result={"status":"PASS","actual_source":actual_source(),"exact_insertion_ranks":insertion_rank(),
            "predicted_ratio_limit":2*math.pi*math.sqrt(3),
            "scale_diagnostics":[scale(N) for N in (60,120,240,480,960,1920,3840)],
            "scope":"Original-source algebra obstruction and critical-polynomial insertion; no new general volume theorem."}
    Path(__file__).with_name('actual_source_quotient_critical_relation_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","exact_rank_levels":len(result['exact_insertion_ranks']),
                      "actual_source":result['actual_source'],"last_scale":result['scale_diagnostics'][-1],
                      "predicted_ratio_limit":result['predicted_ratio_limit']}))


if __name__=='__main__':main()
