#!/usr/bin/env python3
"""Literal complete-color Casimir coupons and every original top-cap mark.
Finite root identities only; no generic-q proof, sector transport or asymptotic.
"""
import argparse, json
from pathlib import Path
import numpy as np
from audit_actual_small_circle_polynomial_face_insertion import Local, physical_colors
from audit_actual_braided_two_cut_source_adapter import original_crossings
from original_source_tensor import apply_pair

def chi(N):
    a,b=[2],[0,1]
    for _ in range(2,N+1):
        c=[0]+b
        for j,v in enumerate(a): c[j]-=v
        a,b=b,c
    b[0]+=2
    return b

def numerator(O,sigma,N,p):
    I=np.eye(N*N,dtype=np.int64); powers=[I]
    for _ in range(1,N): powers.append(powers[-1]@O%p)
    coeff=chi(N); V=np.zeros_like(O)
    for a in range(1,N+1):
        for j in range(a): V=(V+(coeff[a]*pow(sigma,a-1-j,p)%p)*powers[j])%p
    ch=sum(v*pow(sigma,j,p) for j,v in enumerate(coeff))%p
    assert np.array_equal((sigma*I-O)@V%p,ch*I%p)
    return V

def top_components(k,slots,eps):
    perm=list(range(2*k)); parent=list(range(2*k))
    def find(a):
        while parent[a]!=a: a=parent[a]
        return a
    def union(a,b): parent[find(a)]=find(b)
    for j in range(k): union(2*j,2*j+1)
    for a,e in zip(slots,eps):
        if e: perm[a],perm[a+1]=perm[a+1],perm[a]
    for j in range(k): union(perm[2*j],perm[2*j+1])
    return [find(perm[2*j]) for j in range(k)]

def run(N,k,slots,variant):
    loc=Local(N); p=loc.p; colors=physical_colors(loc)
    O=(-colors[2])%p; I=np.eye(N*N,dtype=np.int64)
    rp,rq,_,R=original_crossings(N)
    assert (rp,rq)==(p,loc.q), (N,"root-field mismatch")
    assert 16*N*N*p**3 < np.iinfo(np.int64).max, (N,p,"int64 bound")
    eps=[0]*len(slots) if variant==0 else [(0,1,-1)[j%3] for j in range(len(slots))]
    operators=[]
    for j,e in enumerate(eps):
        if variant==0: F=numerator(O,(-2,2,0,3)[j%4],N,p)
        else: F=(3*I+(7+j)*O+11*(O@O%p))%p
        if e: F=F@R[0 if e>0 else 1][0]%p
        operators.append(F)
    state=np.array([1],dtype=np.int64)
    for _ in range(k): state=np.kron(state,loc.cup[0].reshape(-1))%p
    state=state.reshape((N,)*(2*k))
    for a,op in zip(slots,operators):state=apply_pair(op,state,a,N,p)
    paired=state.reshape((N*N,)*k)
    marker=np.array([pow(loc.x,j,p)*pow(N*N,-1,p)%p for i in range(N) for j in range(N)],dtype=np.int64)
    cup=loc.cup[0].reshape(-1);cap=loc.cap[0].reshape(-1)
    assert int(marker@cup%p)==1
    values=[]; entries=0
    for mark in range(k):
        v=paired
        for other in reversed(range(k)):
            if other!=mark:v=np.tensordot(cap,v,axes=(0,other))%p
        value=int(marker@v%p)
        assert np.array_equal(v,value*cup%p),(N,k,slots,variant,mark,'not scalar cup')
        values.append(value);entries+=N*N
    assert len(set(values))==1,(N,k,slots,variant,values)
    comps=top_components(k,slots,eps)
    same=sum(comps[i]==comps[j] for i in range(k) for j in range(i+1,k))
    different=k*(k-1)//2-same
    return dict(N=N,width=k,slots=slots,variant=variant,half_twists=eps,
                top_component_labels=comps,values=values,scalar_cup_entries=entries,
                same_component_pairs=same,different_component_pairs=different,
                nonzero=bool(values[0]))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=Path(__file__).with_name('research_arbitrary_casimir_top_mark_transport_results.json'));args=ap.parse_args()
    rows=[]
    fixtures=[(2,[1,2,1],range(3,9)),(2,[1,0,2,1],range(3,9)),
              (3,[1,3,2,4,1,3],range(3,6)),
              (4,[1,3,5,2,4,6,1,3,5],(3,4))]
    for k,word,levels in fixtures:
        for N in levels:
            for variant in (0,1): rows.append(run(N,k,word,variant))
    data=dict(status='PASS',cases=len(rows),nonzero_cases=sum(r['nonzero'] for r in rows),
              marked_contractions=sum(len(r['values']) for r in rows),
              scalar_cup_entries=sum(r['scalar_cup_entries'] for r in rows),
              same_component_comparisons=sum(r['same_component_pairs'] for r in rows),
              different_component_comparisons=sum(r['different_component_pairs'] for r in rows),
              cases_detail=rows,
              scope='Original physical matrices, actual cups/ordinary caps/unrestricted mark; full divided-polynomial V at ±2/0/3 and arbitrary polynomial coupons with original signed crossings. No projected-sector mark transport, generic-q derivative or asymptotic claim.')
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='cases_detail'},indent=2))
if __name__=='__main__':main()
