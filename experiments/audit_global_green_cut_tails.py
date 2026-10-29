"""Literal Green cut tails, returning wall, and cochain excursion identity."""
from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np
import sympy as sp


def cut_tail_case(N):
    rng=random.Random(961+N)
    # Keep two other labels unsummed: the identity is checked separately
    # at every pair, never after summing them.
    checks=0
    for b in range(-1,3):
        for t in range(-2,2):
            values={a:rng.randrange(-20,21) for a in range(-4,N+5)}
            val=lambda a:values.get(a,0)
            C=sp.diag(*[val(a) for a in range(N)])
            U=sp.zeros(N)
            for a in range(N-1):U[a+1,a]=1
            plus=sp.diag(*[val(a+1) for a in range(N)])
            minus=sp.diag(*[val(a-1) for a in range(N)])
            P0,Pt=sp.zeros(N),sp.zeros(N)
            P0[0,0]=1;Pt[N-1,N-1]=1
            assert plus==U.T*C*U+val(N)*Pt
            assert minus==U*C*U.T+val(-1)*P0
            assert sp.trace(plus-C)==val(N)-val(0)
            # Full zero-extended difference vanishes including both tails.
            assert sum(val(a+1)-val(a) for a in range(-6,N+7))==0
            checks+=4
    e=sp.zeros(N+1)
    for k in range(1,N+1):e[k-1,k]=N-k+1
    wall=sp.zeros(N+1);wall[N,0]=1
    assert sp.trace(wall)==0
    assert sp.trace(e**N*wall)==sp.factorial(N)
    assert sp.trace(wall*e**N)==sp.factorial(N)
    checks+=3
    return {'N':N,'unsummed_label_cases':16,'exact_checks':checks}


def contraction_case(N):
    p=1009
    Q=7
    inv=lambda a:pow(int(a)%p,-1,p)
    r=2*N+1
    dims=[r,2*r,r]
    cuts=np.cumsum([0]+dims)
    size=sum(dims)
    d=np.zeros((size,size),dtype=np.int64)
    h=np.zeros_like(d)
    proj=np.zeros((2,size),dtype=np.int64)
    inc=np.zeros((size,2),dtype=np.int64)
    for j in range(r):
        A=(pow(Q,N-j,p)-1)%p
        d[cuts[1]+j,j]=A
        if j<r-1:d[cuts[1]+r+j+1,j]=1
        c=(pow(Q,N-j,p)-inv(Q))%p
        d[cuts[2]+j,cuts[1]+r+j]=c
        if j<r-1:d[cuts[2]+j+1,cuts[1]+j]=-inv(Q)%p
    for j in range(r-1):
        h[j,cuts[1]+r+j+1]=1
        h[cuts[1]+j,cuts[2]+j+1]=-Q%p
    h[cuts[1]+r,cuts[2]]=inv(pow(Q,N,p)-inv(Q))
    proj[0,r-1]=1;proj[1,cuts[1]+r-1]=1
    inc[r-1,0]=1;inc[cuts[1]+r-1,1]=1
    dr=np.array([[0,0],[(pow(Q,-N,p)-1)%p,0]],dtype=np.int64)
    assert not np.any(d@d%p)
    assert np.array_equal((d@h+h@d)%p,(np.eye(size,dtype=np.int64)-inc@proj)%p)
    rng=np.random.default_rng(664+N)
    for _ in range(8):
        ops=[]
        for __ in range(2):
            O=np.zeros_like(d)
            for a,b in zip(cuts[:-1],cuts[1:]):
                O[a:b,a:b]=rng.integers(0,p,size=(b-a,b-a))
            ops.append(O)
        O1,O2=ops
        delta1=(d@O1-O1@d)%p
        delta2=(d@O2-O2@d)%p
        H=proj@O2%p@h%p@O1%p@inc%p
        lhs=(proj@O2%p@O1%p@inc-(proj@O2%p@inc)@(proj@O1%p@inc))%p
        rhs=(dr@H+H@dr-proj@delta2%p@h%p@O1%p@inc+proj@O2%p@h%p@delta1%p@inc)%p
        assert np.array_equal(lhs,rhs)
    return {'N':N,'prime':p,'non_chain_operator_tests':8,
            'endpoint_and_current_terms_retained':True}


def main():
    result={'status':'pass','cut_tail_cases':[cut_tail_case(N) for N in range(2,10)],
            'cochain_excursion_cases':[contraction_case(N) for N in range(2,7)],
            'scope':'Exact actual cut-source identities and universal memory-contraction residual; no Gaussian/current identification.'}
    path=Path(__file__).with_name('global_green_cut_tails_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','cut_levels':8,'contraction_levels':5,
                      'results':str(path)},indent=2))


if __name__=='__main__':main()
