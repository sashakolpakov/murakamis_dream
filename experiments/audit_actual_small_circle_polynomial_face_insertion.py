#!/usr/bin/env python3
"""Actual small-circle tensors versus polynomial face insertion.

The physical Casimir is built from the original coproduct matrices.
No source coefficient is obtained by dropping modular aliases first.
"""
import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_original_marked_face_coefficient import (
    Local, add, local_polynomials, morse_faces, mul, substitute,
)
from audit_general_odd_endpoint_matching_network import apply_pair


def casimir(loc):
    p,q,N=loc.p,loc.q,loc.N
    K=loc.Kpair[0]
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    return (loc.Fpair[0]@loc.Epair[0]+q*K+pow(q,-1,p)*Ki)%p


def physical_colors(loc):
    O=casimir(loc);I=np.eye(loc.N**2,dtype=np.int64)
    out=[np.zeros_like(I),I,-O%loc.p]
    for h in range(2,loc.N):out.append((-O@out[-1]-out[-2])%loc.p)
    return out


def T(poly,x,c,y,loc):
    p,q,Q=loc.p,loc.q,loc.Q;out={}
    for n,coef in poly.items():
        j=n[c];Z=pow(Q,j,p)
        aa=-(q*Z+pow(q*Z,-1,p))%p
        bb=(2-Z-pow(Z,-1,p))%p
        ee=(q+pow(q,-1,p)-q*pow(Z,-1,p)-pow(q,-1,p)*Z)%p
        assert j or bb==0
        assert j>=2 or ee==0
        for lower,raised,weight in [(0,(),aa),(1,(x,),bb),(1,(y,),bb),(2,(x,y),ee)]:
            if not weight:continue
            nn=list(n);nn[c]-=lower
            for f in raised:nn[f]+=1
            assert min(nn)>=0 and sum(nn)==sum(n)
            nn=tuple(nn);out[nn]=(out.get(nn,0)+coef*weight)%p
    return {n:v for n,v in out.items() if v}


def insertions(poly,x,c,y,loc):
    seq=[{},poly,T(poly,x,c,y,loc)]
    for h in range(2,loc.N):seq.append(add(T(seq[-1],x,c,y,loc),seq[-2],loc.p,-1))
    return seq


def merge(poly,b,c,p):
    out={}
    for n,v in poly.items():
        nn=list(n);nn[b]+=nn[c];del nn[c];nn=tuple(nn)
        out[nn]=(out.get(nn,0)+v)%p
    return {n:v for n,v in out.items() if v}


def scalar(loc,labels,signs):
    p,q,N=loc.p,loc.q,loc.N;im=pow(loc.eta,N,p)
    S=[pow(im,j,p)*pow(q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
    result=1
    for a,eps in zip(labels,signs):
        ka=1 if 2*a==loc.d else 2;beta=S[2*a]*pow(S[a]**2,-1,p)%p
        result=result*ka*beta**2*pow(loc.omega[a],eps,p)%p
    return result


def symbolic():
    q,c,x,y,Z=sp.symbols('q c x y Z',nonzero=True)
    terms=[-q**-1*(1+q*(x+y)/c+q*q*x*y/c**2)/Z,
           -q*(1+(x+y)/(q*c)+x*y/(q*q*c**2))*Z,
           2*(x+y)/c+(q+1/q)*x*y/c**2]
    expected=-(q*Z+1/(q*Z))+(2-Z-1/Z)*(x+y)/c+(q+1/q-q/Z-Z/q)*x*y/c**2
    assert sp.simplify(sum(terms)-expected)==0
    assert sp.simplify((2-Z-1/Z).subs(Z,1))==0
    assert sp.simplify((q+1/q-q/Z-Z/q).subs(Z,1))==0
    assert sp.simplify((q+1/q-q/Z-Z/q).subs(Z,q*q))==0
    U,V=sp.symbols('U V',nonzero=True)
    D=2*q*U+2/(q*V)-(q+1/q)*U/V
    Aplus=(1/V-1)*(1-q*q*U);Aminus=(1/(q*q*V)-1)*(1-U)
    values={U:-x/(q*c),V:-c/(q*y)}
    assert sp.simplify(-D.subs(values)-(2*(x+y)/c+(q+1/q)*x*y/c**2))==0
    assert sp.simplify(-Aplus.subs(values)-(1+q*x/c)*(1+q*y/c))==0
    assert sp.simplify(-Aminus.subs(values)-(1+x/(q*c))*(1+y/(q*c)))==0
    return {'exact_operator_and_endpoint_identities':7}


def local_checks():
    counts=dict(original_coproduct_entries=0,physical_endpoint_zeros=0,
                actual_color_monomial_paths=0,high_total_cases=0)
    for N in range(3,10):
        loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
        O=casimir(loc);colors=physical_colors(loc)
        for u,v in itertools.product(range(N),repeat=2):
            U,V=pow(Q,u,p),pow(Q,v,p);col=u*N+v
            row=np.zeros(N*N,dtype=np.int64)
            row[col]=(2*q*U+2*pow(q,-1,p)*pow(V,-1,p)-(q+pow(q,-1,p))*U*pow(V,-1,p))%p
            aa=(pow(V,-1,p)-1)*(1-Q*U)%p
            bb=(pow(Q*V,-1,p)-1)*(1-U)%p
            row[((u+1)%N)*N+(v-1)%N]=(row[((u+1)%N)*N+(v-1)%N]+aa)%p
            row[((u-1)%N)*N+(v+1)%N]=(row[((u-1)%N)*N+(v+1)%N]+bb)%p
            assert np.array_equal(row,O[:,col]);counts['original_coproduct_entries']+=N*N
            if u==d or v==0:assert aa==0;counts['physical_endpoint_zeros']+=1
            if u==0 or v==d:assert bb==0;counts['physical_endpoint_zeros']+=1
        # Independent actual L_h path pairing against c^j; x,y chosen
        # from the literal input clocks, including physical endpoints.
        for u,v in [(0,0),(0,d),(d,0),(d,d),(d//2,d//2),(d,d//2)]:
            xx=-q*pow(Q,u,p)%p;yy=-pow(q,-1,p)*pow(Q,-v,p)%p
            for j in (0,1,2,N-1,N,N+1):
                seq=insertions({(0,j,0):1},0,1,2,loc)
                for h in range(1,N+1):
                    predicted=sum(cc*pow(xx,n[0],p)*pow(yy,n[2],p) for n,cc in seq[h].items())%p
                    actual=0
                    for r in range(max(0,u+v-d),min(d,u+v)+1):
                        step=r-u
                        actual+=int(colors[h][r*N+u+v-r,u*N+v])*pow(q,d*step,p)*pow(Q,-step*j,p)
                    assert actual%p==predicted,(N,u,v,j,h,actual%p,predicted)
                    counts['actual_color_monomial_paths']+=1
                    counts['high_total_cases']+=u+v>d
    return counts


def whole_source_case(N,k,boxes,port,labels,marked):
    loc=Local(N);p,d=loc.p,loc.d;chart=morse_faces(k,boxes,marked)
    x,b,c,y=chart['circles'][port]
    assert len({x,b,c,y})==4 and b not in(0,chart['v']) and c not in(0,chart['v'])
    short=morse_faces(k,boxes[:port]+boxes[port+1:],marked)
    assert short['faces']==chart['faces']-1
    variables=list(range(chart['faces']));P={(0,)*len(variables):1}
    coupons=[];signs=[]
    for ii,((xx,bb,cc,yy),a) in enumerate(zip(chart['circles'],labels)):
        eps=(-1,0,1)[ii%3];signs.append(eps)
        if ii==port:coupons.append(None);continue
        D,F=local_polynomials(loc,a)
        for fac,ids in [(D,(xx,bb,yy)),(D,(xx,cc,yy)),(F,(xx,yy))]:P=mul(P,substitute(fac,ids,variables,p),p)
        coupons.append(loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p)
    seq=insertions(P,x,c,y,loc);colors=physical_colors(loc)
    reps=[f for f in variables if f!=c]
    target=tuple(0 if f in(0,chart['v']) else d for f in reps)
    pref=pow(N,len(boxes)-1,p)*scalar(loc,[a for i,a in enumerate(labels) if i!=port],[e for i,e in enumerate(signs) if i!=port])%p
    state0=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
    for j in range(k):
        state0=np.kron(state0,loc.cup[0].reshape(-1))%p
        mark=np.kron(mark,(marker if j==marked else loc.cap[0]).reshape(-1))%p
    rows=[];alias_candidates=0
    for h in range(1,N+1):
        result=merge(seq[h],b,c,p)
        assert all(sum(n)==d*(len(boxes)-1) and min(n)>=0 for n in result)
        for n in result:
            if all((n[j]-target[j])%N==0 for j in range(1,len(reps))):
                assert n==target;alias_candidates+=1
        predicted=pref*result.get(target,0)%p
        state=state0.reshape((N,)*(2*k))
        for ii,slot in enumerate(boxes):state=apply_pair(colors[h] if ii==port else coupons[ii],state,slot,N,p)
        actual=int(mark@state.reshape(-1)%p)
        assert actual==predicted,(N,k,port,labels,marked,h,actual,predicted)
        rows.append(dict(h=h,actual_source=actual,polynomial_coefficient=result.get(target,0),polynomial_monomials=len(result)))
    return dict(N=N,width=k,boxes=len(boxes),port=port,marked=marked,labels=labels,field=p,cases=rows,unique_alias_checks=alias_candidates)


def whole_sources():
    rows=[]
    for N in range(3,9):
        M=(N-1)//2
        for labels in ([M]*4,[0]*4,[i%(M+1) for i in range(4)]):
            rows.append(whole_source_case(N,2,[1,0,2,1],1,labels,1))
        rows.append(whole_source_case(N,2,[1,0,2,1],2,[M]*4,0))
    for N in (3,4):
        boxes=[1,3,0,2,4,1,3];chart=morse_faces(3,boxes,2)
        port=next(i for i,(x,b,c,y) in enumerate(chart['circles']) if len({x,b,c,y})==4 and b not in(0,chart['v']) and c not in(0,chart['v']) and all(j in boxes[:i]+boxes[i+1:] for j in(1,3)))
        rows.append(whole_source_case(N,3,boxes,port,[0,1,0,1,0,1,0],2))
    return dict(original_fixed_sector_sources=sum(len(r['cases']) for r in rows),
                unique_alias_checks=sum(r['unique_alias_checks'] for r in rows),
                both_original_mark_positions=True,cases=rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_small_circle_polynomial_face_insertion_results.json');args=ap.parse_args()
    data=dict(status='PASS',symbolic=symbolic(),local=local_checks(),whole_sources=whole_sources(),
              scope='Original coproduct and full marked small-circle contractions, all physical endpoint factors, all h up to N in both parities, polynomial output and unique alias after complete path sum. One untwisted port with distinct unmarked middle faces and connected smoothing; no multiple-port or signed-port theorem.')
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='whole_sources'},indent=2))
    print(json.dumps({k:v for k,v in data['whole_sources'].items() if k!='cases'},indent=2))


if __name__=='__main__':main()
