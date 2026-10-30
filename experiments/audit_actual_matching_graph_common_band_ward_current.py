#!/usr/bin/env python3
"""Typed charge charts and actual independent-head composed Ward currents."""
import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

from audit_actual_braided_two_cut_source_adapter import original_crossings
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet


def actual_plat_graph(k,d):
    edges=[];last=[];nv=0
    def vertex():
        nonlocal nv
        v=nv;nv+=1;return v
    for _ in range(k):
        v=vertex();last.extend([v,v])
    # Includes an explicit positive route and its inverse, with all channels.
    route=list(range(2*k-2,-1,-1))
    word=list(range(2*k-1))+route+route[::-1]+list(range(2*k-2,-1,-1))
    for n,slot in enumerate(word):
        low=vertex();high=vertex();g=n%(d+1)
        edges.extend([(last[slot],low,d),(last[slot+1],low,d),(low,high,2*g)])
        last[slot]=last[slot+1]=high
    for i in range(k):
        v=vertex();edges.extend([(last[2*i],v,d),(last[2*i+1],v,d)])
    return nv,edges


def components(n,edges,ids):
    adj=[[] for _ in range(n)]
    for e in ids:
        u,v,_=edges[e];adj[u].append(v);adj[v].append(u)
    unseen=set(range(n));out=[]
    while unseen:
        seed=min(unseen);part={seed};stack=[seed];unseen.remove(seed)
        while stack:
            for v in adj[stack.pop()]:
                if v in unseen:unseen.remove(v);part.add(v);stack.append(v)
        out.append(part)
    return out


def tree_edges(n,edges,ids):
    seen={0};todo=[0];out=[]
    while todo:
        v=todo.pop()
        for e in ids:
            u,w,_=edges[e]
            other=w if u==v else u if w==v else None
            if other is not None and other not in seen:
                seen.add(other);todo.append(other);out.append(e)
    assert len(seen)==n and len(out)==n-1
    return out


def tree_solve(n,edges,tree,b):
    b=list(b);adj=[set() for _ in range(n)]
    for e in tree:
        u,v,_=edges[e];adj[u].add(e);adj[v].add(e)
    queue=[v for v in range(n) if len(adj[v])==1];out={}
    while queue:
        v=queue.pop()
        if len(adj[v])!=1:continue
        e=next(iter(adj[v]));u,w,_=edges[e]
        sign=1 if u==v else -1;other=w if u==v else u
        out[e]=b[v]*sign
        b[other]+=b[v];b[v]=0
        adj[v].remove(e);adj[other].remove(e)
        if len(adj[other])==1:queue.append(other)
    assert not any(b)
    return out


def boundary(n,edges,h):
    out=[0]*n
    for e,v in h.items():
        u,w,_=edges[e];out[u]+=v;out[w]-=v
    return out


def graph_checks():
    cases=cycles=charge_paths=0
    for k in range(2,6):
        d=6;n,edges=actual_plat_graph(k,d);allids=list(range(len(edges)))
        physical=[e for e,(_,_,L) in enumerate(edges) if L==d]
        cut=None
        for e0,e1 in itertools.combinations(physical,2):
            ids=[e for e in allids if e not in (e0,e1)]
            if len(components(n,edges,ids))==1:cut=(e0,e1);break
        assert cut is not None
        ids=[e for e in allids if e not in cut]
        tree=tree_edges(n,edges,ids);free=[e for e in ids if e not in tree]
        target=boundary(n,edges,{e:L//2 for e,(_,_,L) in enumerate(edges)})
        for a,l,delta in ((1,2,0),(2,3,1),(3,1,-1)):
            b=target[:]
            for e,value in zip(cut,(a,l)):
                col=boundary(n,edges,{e:value});b=[x-y for x,y in zip(b,col)]
            first=edges[cut[0]][1];second=edges[cut[1]][1]
            b[first]+=delta;b[second]-=delta
            h=tree_solve(n,edges,tree,b)
            assert boundary(n,edges,h)==b
            charge_paths+=1
        ref=edges[cut[0]][1]
        for e in free:
            u,v,_=edges[e]
            col=boundary(n,edges,{e:1})
            ac=tree_solve(n,edges,tree,[-z for z in col]);ac[e]=1
            assert boundary(n,edges,ac)==[0]*n
            assert all(ac.get(f,0)==int(f==e) for f in free)
            qs=[]
            for endpoint in (u,v):
                q=[0]*n;q[ref]+=1;q[endpoint]-=1
                w=tree_solve(n,edges,tree,q);assert boundary(n,edges,w)==q;qs.append(w)
            # Moving the insertion across e changes its chart by exactly
            # the signed fundamental cycle, including the non-tree head.
            diff={i:qs[1].get(i,0)-qs[0].get(i,0)-int(i==e) for i in ids}
            assert all(diff[i]==-ac.get(i,0) for i in ids)
            cycles+=1;charge_paths+=2
        cases+=1
    # A disconnected typed graph has one balance equation per component.
    ed=[(0,1,2),(2,3,2)];parts=components(4,ed,[0,1])
    assert [sum(q[v] for v in part) for q in ([1,-1,0,0],[1,0,-1,0])
            for part in parts]==[0,0,1,-1]
    return dict(actual_expanded_plats=cases,bridge_widths=[2,3,4,5],
                primitive_cycles=cycles,integer_charge_paths=charge_paths,
                disconnected_balance_checks=2)


def ratio(Q,x,U,V,C,da=0,db=0,dk=0):
    out=1
    for axis,delta in enumerate((da,db,dk)):
        for _ in range(abs(delta)):
            if delta<0:
                if axis==0:U/=Q
                elif axis==1:V/=Q
                else:C/=Q
            f=(V*C/x*(1-x*x/U)/(1-x*x*C/U),
               U/(x*C)*(1-Q*V*C)/(1-Q*V),
               -U/(Q*x*V*C)*(1-Q*V*C)*(1-Q*x*x*C/U)/(1-Q*C))[axis]
            out*=f if delta>0 else 1/f
            if delta>0:
                if axis==0:U*=Q
                elif axis==1:V*=Q
                else:C*=Q
    return sp.cancel(out)


def independent_currents():
    Q,x,U,V,C,W=sp.symbols('Q x U V C W',nonzero=True)
    r1=lambda a=0,b=0,c=0:ratio(Q,x,U,V,C,a,b,c)
    r2=lambda a=0,b=0,c=0:ratio(Q,x,V*C,U/C,W*C/U,a,b,c)
    base=r1(0,0,1)*r2(1,-1,1)
    BF=(1-Q*U)*r1(1)*r2(0,1,-1)+(U/x)*(1-Q*V)*r1(0,1)*r2(1)
    BF-=(1-W)*r2(0,0,-1)+(W-Q*U*V)/x
    JF=r2(0,1,-1)*((U/x)*(1-Q*V)*r1(0,1,-1)-(1-V*C)*r1(0,0,-1))
    assert sp.cancel(BF-base*JF.subs(C,Q*C)+JF)==0
    # Ecal has the common q^-1 factor, retained equally on both sides.
    BE=(1/V-Q*x*x/(U*V))*r1(-1)*r2(0,-1,1)+(1/x-Q*x/V)*r1(0,-1)*r2(-1)
    BE-=Q*(W-x*x)/(U*V)*r2(0,0,1)+(1/x-Q*x*W/(U*V))
    JE=r2(-1)*((C/U-Q*x*x/(U*V))-(1/x-Q*x/V)*r1(0,-1))
    assert sp.cancel(BE-base*JE.subs(C,Q*C)+JE)==0
    return dict(independent_head_composed_F=1,independent_head_composed_E=1)


def poch(a,Q,n):
    out=Jet(1)
    for j in range(n):out*=1-a*Q**j
    return out


def original_source_checks():
    entries=nonzero_endpoint_normals=0
    for N in range(2,9):
        p,q0,_,(R,_)=original_crossings(N);_,eta=root_field(N)
        Jet.p=p;Jet.order=2;q=Jet([q0,q0]);Q=q*q;d=N-1;x=q**d
        cart0=pow(eta,d*d,p)
        cart=Jet([cart0,cart0*d*d*pow(2,-1,p)%p])
        for a,b in itertools.product(range(N),repeat=2):
            for k in range(min(a,d-b)+1):
                r=cart*(-1)**k*x**(-a-b-k)*Q**(a*b+(a-b)*k-k*(k+1)//2)
                r*=poch(Q**(b+1),Q,k)/poch(Q,Q,k)*poch(Q**(N-a),Q,k)
                row=(b+k)*N+a-k;col=a*N+b
                assert r.c==[int(R[0][row,col]),int(R[1][row,col])]
                entries+=1
        interior=1-Q**N
        assert interior.c==[0,-2*N%p]
        nonzero_endpoint_normals+=1
    return dict(original_crossing_value_and_first_jet_entries=entries,
                untruncated_endpoint_normal_defects=nonzero_endpoint_normals)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=dict(status='PASS',graphs=graph_checks(),interior=independent_currents(),
                source=original_source_checks(),scope='Actual typed common charge lattice, independent-head composed Ward currents, and original generic crossing normalization. No equality of charged support cycles or geometric-cycle coefficient.')
    target=args.output or Path(__file__).with_name('actual_matching_graph_common_band_ward_current_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
