#!/usr/bin/env python3
"""Literal Morse birth order, full small-color sources, protected mark adapter."""
import argparse
import json
from pathlib import Path

import numpy as np

from audit_actual_small_circle_polynomial_face_insertion import (
    Local, insertions, local_polynomials, morse_faces, mul,
    physical_colors, scalar, substitute, apply_pair, casimir,
)


def merge_keep_slots(poly,keep,kill,p):
    out={}
    for n,c in poly.items():
        nn=list(n);nn[keep]+=nn[kill];nn[kill]=0;nn=tuple(nn)
        out[nn]=(out.get(nn,0)+c)%p
    return {n:c for n,c in out.items() if c}


def compose(poly,chart,ports,hs,loc,reverse=True,protected_adapter=False):
    par=list(range(chart['faces']));protected=(0,chart['v'])
    def root(f):
        while par[f]!=f:f=par[f]
        return f
    pairs=list(zip(ports,hs))
    if reverse:pairs.reverse()
    for i,h in pairs:
        x,b,c,y=map(root,chart['circles'][i])
        keep,kill=b,c
        if protected_adapter and kill in protected:keep,kill=c,b
        assert kill not in protected and keep!=kill and kill not in(x,y)
        poly=insertions(poly,x,kill,y,loc)[h]
        poly=merge_keep_slots(poly,keep,kill,loc.p);par[kill]=keep
    target=tuple(loc.d if root(f)==f and f not in protected else 0 for f in range(chart['faces']))
    return poly,target


def source_case(N,k,boxes,ports,hs,marked=None,protected_adapter=False,wrong_order=False):
    loc=Local(N);p,d=loc.p,loc.d;chart=morse_faces(k,boxes,marked)
    marked=chart['marked'];nf=chart['faces'];a=d//2
    variables=list(range(nf));poly={(0,)*nf:1};D,F=local_polynomials(loc,a)
    coupons=[];signs=[]
    for i,(x,b,c,y) in enumerate(chart['circles']):
        eps=(-1,0,1)[i%3];signs.append(eps)
        if i in ports:coupons.append(None);continue
        for fac,ids in [(D,(x,b,y)),(D,(x,c,y)),(F,(x,y))]:poly=mul(poly,substitute(fac,ids,variables,p),p)
        coupons.append(loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p)
    result,target=compose(poly,chart,ports,hs,loc,protected_adapter=protected_adapter)
    assert sum(target)==d*(len(boxes)-len(ports))
    assert all(min(n)>=0 and sum(n)==sum(target) for n in result)
    alias=0
    for n in result:
        if all((n[f]-target[f])%N==0 for f in range(1,nf)):
            assert n==target;alias+=1
    pref=pow(N,len(boxes)-len(ports),p)*scalar(loc,[a]*(len(boxes)-len(ports)),[e for i,e in enumerate(signs) if i not in ports])%p
    predicted=pref*result.get(target,0)%p
    state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
    for j in range(k):
        state=np.kron(state,loc.cup[0].reshape(-1))%p
        mark=np.kron(mark,(marker if j==marked else loc.cap[0]).reshape(-1))%p
    state=state.reshape((N,)*(2*k));colors=physical_colors(loc)
    for i,slot in enumerate(boxes):state=apply_pair(colors[hs[ports.index(i)]] if i in ports else coupons[i],state,slot,N,p)
    actual=int(mark@state.reshape(-1)%p)
    assert actual==predicted,(N,k,ports,hs,actual,predicted)
    bad=None
    if wrong_order:
        pp,tt=compose(poly,chart,ports,hs,loc,reverse=False)
        bad=pref*pp.get(tt,0)%p
    return dict(N=N,width=k,boxes=boxes,ports=ports,small_colors=hs,marked=marked,
                original_source=actual,coefficient_value=result.get(target,0),
                polynomial_monomials=len(result),unique_alias_checks=alias,
                wrong_forward_order_source=bad,field=p)


def birth_checks():
    counts=dict(original_Morse_charts=0,bounded_output_births=0,
                earlier_outer_face_exclusions=0,deleted_forests=0,
                connected_literal_smoothings=0,protected_mark_parities=0,
                genuine_cross_coefficient_incidences=0)
    for k in range(2,8):
        odd=list(range(1,2*k-2,2));even=list(range(0,2*k-1,2))
        for boxes in (odd+even+odd,even+odd+even+odd,odd+even+odd+even+odd):
          for marked in range(k):
            chart=morse_faces(k,boxes,marked);counts['original_Morse_charts']+=1
            eligible=[];born=set()
            assert chart['parity'][0]==0 and chart['parity'][chart['v']]==1
            counts['protected_mark_parities']+=1
            for i,(x,b,c,y) in enumerate(chart['circles']):
                if c!=0:
                    assert c not in born;born.add(c)
                    assert all(c not in earlier for earlier in chart['circles'][:i])
                    assert c not in(x,y)
                    counts['bounded_output_births']+=1
                    counts['earlier_outer_face_exclusions']+=i
                if c not in(0,chart['v']):eligible.append(i)
                assert not(b in(0,chart['v']) and c in(0,chart['v']) and b!=c)
            for ports in (eligible,eligible[::2],eligible[1::2]):
                if not ports:continue
                parent=list(range(chart['faces']))
                def root(f):
                    while parent[f]!=f:f=parent[f]
                    return f
                for i in ports:
                    _,b,c,_=chart['circles'][i]
                    assert root(b)!=root(c);parent[root(c)]=root(b)
                counts['deleted_forests']+=1
                short=morse_faces(k,[slot for i,slot in enumerate(boxes) if i not in ports],marked)
                assert short['faces']==chart['faces']-len(ports)
                counts['connected_literal_smoothings']+=1
                for i in ports:
                    c=chart['circles'][i][2]
                    for j in ports:
                        if j>i and c in (chart['circles'][j][0],chart['circles'][j][3]):
                            counts['genuine_cross_coefficient_incidences']+=1
    return counts


def tensors():
    rows=[]
    boxes=[1,0,2,1,0,2,1]
    for N in (3,4):
      for ports in ([1,2],[1,3],[1,3,4],[0,1,2,3,4]):
        for hs in ([2]*len(ports),[1+i%N for i in range(len(ports))],[N]*len(ports)):
            rows.append(source_case(N,2,boxes,ports,hs,wrong_order=(ports==[1,3] and hs==[2,2])))
    for ports,hs in (([1,3],[2,3]),([0,1,2,3,4],[2,3,4,5,2])):
        rows.append(source_case(5,2,boxes,ports,hs))
    # A wider original source, with one genuine exterior INPUT face.
    rows.append(source_case(3,3,[1,3,0,2,4,1,3],[0,2,3],[2,3,2],marked=2))
    assert any(r['wrong_forward_order_source'] not in(None,r['original_source']) for r in rows)
    adapters=[];transpose_entries=0
    for N in range(3,8):
        loc=Local(N);O=casimir(loc);assert np.array_equal(O,O.T)
        transpose_entries+=O.size
        for mark in(0,1):
          for port in range(4):
            for h in(1,2,N):
                adapters.append(source_case(N,2,[1,0,2,1],[port],[h],marked=mark,protected_adapter=True))
    # Coincident outer face labels are literal substitutions, not omitted.
    for N in(3,4):adapters.append(source_case(N,2,[0,1,2,1],[0],[N],marked=1,protected_adapter=True))
    return dict(multiple_original_sources=len(rows),single_original_boundary_adapters=len(adapters),
                original_transpose_entries=transpose_entries,
                wrong_order_failures=sum(r['wrong_forward_order_source'] not in(None,r['original_source']) for r in rows),
                unique_alias_checks=sum(r['unique_alias_checks'] for r in rows+adapters),
                multiport_cases=rows,boundary_cases=adapters)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_ordered_small_circle_face_insertions_results.json');args=ap.parse_args()
    data=dict(status='PASS',births=birth_checks(),source=tensors(),
              scope='Literal bounded-face birth order and reverse-Morse small-port polynomial composition; all original tensor phases/cups/mark; exact root-transpose adapter for one protected outgoing face. No arbitrary mixed-direction multiple-port theorem or disconnected/signed-port bound.')
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':data['status'],'births':data['births'],
                      'source':{k:v for k,v in data['source'].items() if not k.endswith('_cases')}},indent=2))


if __name__=='__main__':main()
