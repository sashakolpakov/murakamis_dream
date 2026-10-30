#!/usr/bin/env python3
"""Full cyclic-word correspondence versus original tensor contractions.

No state-dependent truncation is made in the formal band polynomials.
Negative Laurent coefficients are retained until the COMPLETE sum.
"""
import argparse
import itertools
import json
from pathlib import Path
import numpy as np
from audit_actual_small_circle_polynomial_face_insertion import *

def bands(loc,h):
    p,q,Q=loc.p,loc.q,loc.Q
    one={(0,0,0):1}
    two={(0,1,0):2,(0,0,1):2,(0,1,1):(q+pow(q,-1,p))%p}
    for step in(-1,1):
        for a,b,c in [(0,0,1),(1,0,pow(q,step,p)),(0,1,pow(q,step,p)),(1,1,pow(q,2*step,p))]:two[(step,a,b)]=c
    if h==1:return one
    old,now=one,two
    for degree in range(2,h):
        out={}
        for (t,a,b),v in two.items():
          for (s,c,d),w in now.items():
            key=(t+s,a+c,b+d)
            out[key]=(out.get(key,0)+v*w*pow(Q,t*(c+d),p))%p
        for key,v in old.items():out[key]=(out.get(key,0)-v)%p
        old,now=now,{key:v for key,v in out.items() if v}
    return now

def setup(ch,ports,allow_cycles=False):
    nf=ch['faces'];adj=[[] for _ in range(nf)]
    for i in ports:
        _,b,c,_=ch['circles'][i];adj[b].append((c,i));adj[c].append((b,i))
    roots=[];comp={};parent={};edges=[]
    seen=set();protected=(0,ch['v'])
    for f in range(nf):
        if f in seen:continue
        component={f};todo=[f]
        while todo:
            a=todo.pop()
            for b,i in adj[a]:
                if b not in component:component.add(b);todo.append(b)
        seen|=component
        pp=component.intersection(protected);assert len(pp)<=1
        root=next(iter(pp)) if pp else min(component);ci=len(roots);roots.append(root)
        for v in component:comp[v]=ci
        walked={root};todo=[root]
        while todo:
            a=todo.pop(0)
            for b,i in adj[a]:
                if b in walked:continue
                walked.add(b);todo.append(b);parent[b]=(a,i);edges.append((a,b,i))
    chords=[]
    if allow_cycles:
        used={i for a,b,i in edges}
        chords=[(ch['circles'][i][1],ch['circles'][i][2],i) for i in ports if i not in used]
    else:assert len(edges)==len(ports)
    for a,b,i in edges:
        x,bb,cc,y=ch['circles'][i]
        assert comp[x]!=comp[a] and comp[y]!=comp[a]
    return (roots,comp,edges,chords) if allow_cycles else (roots,comp,edges)

def simultaneous(N,boxes,ports,hs,marked=1,k=2,disconnected=False):
    loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
    ch=morse_faces(k,boxes,marked);nf=ch['faces'];a=d//2
    if disconnected:roots,comp,edges,chords=setup(ch,ports,allow_cycles=True)
    else:roots,comp,edges=setup(ch,ports);chords=[]
    beta=len(chords);all_edges=edges+chords;nr=len(roots)
    if disconnected:assert beta>=1 and sum(h-1 for h in hs)<N
    D,F=local_polynomials(loc,a);P={(0,)*nf:1};coupons=[];signs=[]
    for i,(x,b,c,y) in enumerate(ch['circles']):
        eps=(-1,0,1)[i%3];signs.append(eps)
        if i in ports:coupons.append(None);continue
        for fac,ids in [(D,(x,b,y)),(D,(x,c,y)),(F,(x,y))]:P=mul(P,substitute(fac,ids,list(range(nf)),p),p)
        coupons.append(loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p)
    local={i:bands(loc,hs[ports.index(i)]) for i in ports}
    shifts={i:sorted({t for t,a,b in local[i]}) for i in ports}
    result={};negative_before=0;compatible=0
    for ss in itertools.product(*(shifts[i] for i in ports)):
        shift=dict(zip(ports,ss));lift={r:0 for r in roots}
        for par,child,i in edges:lift[child]=lift[par]-shift[i]
        if any(lift[par]-lift[child]!=shift[i] for par,child,i in chords):continue
        compatible+=1
        pp={}
        for n,v in P.items():
            nn=[0]*nr;ex=0
            for f,j in enumerate(n):nn[comp[f]]+=j;ex+=lift[f]*j
            nn=tuple(nn);pp[nn]=(pp.get(nn,0)+v*pow(Q,ex,p))%p
        for par,child,i in all_edges:
            x,_,_,y=ch['circles'][i];lp={}
            for (t,rx,ry),v in local[i].items():
                if t!=shift[i]:continue
                nn=[0]*nr;nn[comp[x]]+=rx;nn[comp[y]]+=ry;nn[comp[par]]-=rx+ry
                ex=lift[x]*rx+lift[y]*ry-lift[par]*(rx+ry)
                nn=tuple(nn);lp[nn]=(lp.get(nn,0)+v*pow(Q,ex,p))%p
            pp=mul(pp,lp,p)
        degree=[0]*nf
        for par,child,i in all_edges:degree[par]+=1;degree[child]+=1
        phase=sum((degree[f]-2*(f not in(0,ch['v'])))*lift[f] for f in range(nf))
        pp={n:v*pow(q,d*phase,p)%p for n,v in pp.items()}
        negative_before+=sum(min(n)<0 for n in pp)
        for n,v in pp.items():result[n]=(result.get(n,0)+v)%p
    result={n:v for n,v in result.items() if v}
    exterior=comp[0]
    assert all(all(n[j]>=0 for j in range(nr) if j!=exterior or not disconnected) for n in result)
    H=sum(h-1 for h in hs)
    if disconnected:assert all(n[exterior]>=-2*H for n in result)
    target=tuple(-d*beta if root==0 else 0 if root==ch['v'] else d for root in roots)
    assert all(sum(n)==sum(target) for n in result)
    averaged=0;surviving=0
    for n,v in result.items():
        if all((n[j]-target[j])%N==0 for j in range(nr) if roots[j]!=0):
            if not disconnected:assert n==target
            surviving+=1
            parity_phase=sum(ch['parity'][root]*(n[j]-target[j]) for j,root in enumerate(roots)) if N%2==0 else 0
            averaged=(averaged+v*pow(q,parity_phase,p))%p
    pref=pow(N,len(boxes)-len(ports)+beta,p)*scalar(loc,[a]*(len(boxes)-len(ports)),[e for i,e in enumerate(signs) if i not in ports])%p
    predicted=pref*averaged%p
    state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
    for j in range(k):
        state=np.kron(state,loc.cup[0].reshape(-1))%p
        mark=np.kron(mark,(marker if j==marked else loc.cap[0]).reshape(-1))%p
    state=state.reshape((N,)*(2*k));colors=physical_colors(loc)
    for i,slot in enumerate(boxes):state=apply_pair(colors[hs[ports.index(i)]] if i in ports else coupons[i],state,slot,N,p)
    actual=int(mark@state.reshape(-1)%p)
    assert actual==predicted
    if disconnected and 2*H<d:assert actual==surviving==0
    return dict(N=N,width=k,boxes=boxes,small_ports=ports,small_colors=hs,
                mark=marked,field=p,actual_source=actual,
                extracted_coefficient=result.get(target,0),grid_average=averaged,
                compatible_band_choices=compatible,cycle_rank=beta,small_degree=H,
                surviving_grid_monomials=surviving,
                simultaneous_polynomial_monomials=len(result),
                negative_exponent_terms_before_full_sum=negative_before,
                negative_exponent_terms_after_full_sum=sum(min(n)<0 for n in result))


def local_band_checks():
    counts=dict(original_full_color_entries=0,formal_band_endpoint_zeros=0,
                high_total_color_columns=0)
    for N in range(3,9):
        loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
        colors=physical_colors(loc)
        for h in range(1,N+1):
            words=bands(loc,h)
            for u,v in itertools.product(range(N),repeat=2):
                x=-q*pow(Q,u,p)%p;y=-pow(q,-1,p)*pow(Q,-v,p)%p
                vals={}
                for (t,a,b),coef in words.items():vals[t]=(vals.get(t,0)+coef*pow(x,a,p)*pow(y,b,p))%p
                column=np.zeros(N*N,dtype=np.int64)
                for t,coef in vals.items():
                    if not(0<=u+t<=d and 0<=v-t<=d):
                        assert coef==0;counts['formal_band_endpoint_zeros']+=1
                    row=((u+t)%N)*N+(v-t)%N
                    column[row]=(column[row]+coef)%p
                assert np.array_equal(column,colors[h][:,u*N+v])
                counts['original_full_color_entries']+=N*N
                counts['high_total_color_columns']+=u+v>d
    return counts


def forests():
    counts=dict(connected_deleted_subsets=0,exact_component_scalar_identities=0,
                monochrome_components=0,opposite_outer_incidences=0,
                genuine_cyclic_dependencies=0,protected_root_cases=0)
    fixtures=[(2,[1,0,2,1]),(2,[1,0,2,1,0,2,1]),(3,[1,3,0,2,4,1,3])]
    for k,boxes in fixtures:
      for marked in range(k):
        ch=morse_faces(k,boxes,marked)
        for mask in range(1,1<<len(boxes)):
            ports=[i for i in range(len(boxes)) if mask>>i&1]
            remain=[slot for i,slot in enumerate(boxes) if i not in ports]
            if not all(slot in remain for slot in range(1,2*k-2,2)):continue
            short=morse_faces(k,remain,marked)
            roots,comp,edges=setup(ch,ports)
            assert len(roots)==short['faces']==ch['faces']-len(ports)
            counts['connected_deleted_subsets']+=1
            counts['protected_root_cases']+=sum(r in(0,ch['v']) for r in roots)
            for ci,r in enumerate(roots):
                vv=[f for f in range(ch['faces']) if comp[f]==ci]
                assert len({ch['parity'][f] for f in vv})==1
                counts['monochrome_components']+=1
            for par,child,i in edges:
                x,b,c,y=ch['circles'][i]
                assert ch['parity'][x]!=ch['parity'][b] and ch['parity'][y]!=ch['parity'][b]
                counts['opposite_outer_incidences']+=2
            lift={r:0 for r in roots};shifts={i:((i*7+marked)%5)-2 for i in ports}
            degree=[0]*ch['faces']
            for par,child,i in edges:
                lift[child]=lift[par]-shifts[i];degree[par]+=1;degree[child]+=1
            for ci,r in enumerate(roots):
                lhs=sum((degree[f]-2*(f not in(0,ch['v'])))*lift[f] for f in range(ch['faces']) if comp[f]==ci)
                rhs=sum(shifts[i] for par,child,i in edges if comp[par]==ci)
                assert lhs==rhs;counts['exact_component_scalar_identities']+=1
            # A cycle in the naive face-elimination dependency graph is
            # retained as a diagnostic; no DAG is used in the theorem.
            pred={i:set() for i in ports}
            for par,child,i in edges:
                pred[i]={j for j in ports if j!=i and child in ch['circles'][j]}
            todo=set(ports)
            while todo:
                free={i for i in todo if not(pred[i]&todo)}
                if not free:break
                todo-=free
            counts['genuine_cyclic_dependencies']+=bool(todo)
    assert counts['genuine_cyclic_dependencies']>0
    return counts


def original_sources():
    rows=[]
    for N in(3,4,5):
      for ports in([0,2],[0,1,2],[1,2,3]):
        for hs in([2]*len(ports),[N]*len(ports)):
            rows.append(simultaneous(N,[1,0,2,1],ports,hs))
    for N in(3,4):
        rows.append(simultaneous(N,[1,0,2,1],[0,1],[N,2],marked=0))
        rows.append(simultaneous(N,[1,0,2,1,0,2,1],[0,2,5],[2,N,2]))
    rows.append(simultaneous(3,[1,3,0,2,4,1,3],[1,4],[3,2],marked=2,k=3))
    return dict(full_original_simultaneous_sources=len(rows),
                negative_Laurent_terms_canceled=sum(r['negative_exponent_terms_before_full_sum'] for r in rows),
                cases=rows)


def disconnected_topology():
    counts=dict(disconnected_original_subsets=0,exterior_cycle_localizations=0,
                exact_background_degrees=0,tree_component_phases=0)
    for k,boxes in [(2,[1,0,2,1]),(2,[1,0,2,1,0,2,1]),(3,[1,3,0,2,4,1,3])]:
      for marked in range(k):
        ch=morse_faces(k,boxes,marked)
        for mask in range(1,1<<len(boxes)):
            ports=[i for i in range(len(boxes)) if mask>>i&1]
            missing=[slot for slot in range(1,2*k-2,2) if all(i in ports for i,s in enumerate(boxes) if s==slot)]
            if not missing:continue
            roots,comp,edges,chords=setup(ch,ports,allow_cycles=True)
            beta=len(chords);assert beta==len(missing)
            assert len(roots)==len(boxes)-len(ports)+beta+2
            counts['disconnected_original_subsets']+=1
            for par,child,i in chords:
                assert comp[par]==comp[child]==comp[0]
                counts['exterior_cycle_localizations']+=1
            for ci,root in enumerate(roots):
                vertices=[f for f in range(ch['faces']) if comp[f]==ci]
                ne=sum(comp[ch['circles'][i][1]]==ci for i in ports)
                expected=beta if root==0 else 0 if root==ch['v'] else -1
                actual=ne-sum(f not in(0,ch['v']) for f in vertices)
                assert actual==expected;counts['exact_background_degrees']+=1
                if root!=0:assert ne==len(vertices)-1;counts['tree_component_phases']+=1
    return counts


def disconnected_matrix(N,k,boxes,ports,hs,marked):
    loc=Local(N);p,d=loc.p,loc.d;a=d//2;colors=physical_colors(loc)
    state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
    for j in range(k):
        state=np.kron(state,loc.cup[0].reshape(-1))%p
        mark=np.kron(mark,(marker if j==marked else loc.cap[0]).reshape(-1))%p
    state=state.reshape((N,)*(2*k))
    for i,slot in enumerate(boxes):
        if i in ports:op=colors[hs[ports.index(i)]]
        else:
            eps=(-1,0,1)[i%3]
            op=loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p
        state=apply_pair(op,state,slot,N,p)
    actual=int(mark@state.reshape(-1)%p);H=sum(h-1 for h in hs)
    assert 2*H<d and actual==0
    return dict(N=N,width=k,boxes=boxes,small_ports=ports,small_colors=hs,
                marked=marked,small_degree=H,actual_source=actual,field=p)


def disconnected_sources():
    rows=[]
    for N in(6,7):
      for marked in(0,1):
        rows.append(simultaneous(N,[1,0,2,1],[0,3],[2,2],marked=marked,disconnected=True))
    outside=simultaneous(5,[1,0,2,1],[0,3],[3,3],disconnected=True)
    assert outside['actual_source']!=0
    matrices=[]
    for N in(6,7,8,9):
      for marked in(0,1):
        matrices.append(disconnected_matrix(N,2,[1,0,2,1],[0,3],[2,2],marked))
    for marked in(0,2):
        matrices.append(disconnected_matrix(6,3,[1,3,0,2,4,1,3],[0,5],[2,2],marked))
    return dict(exact_cycle_correspondence_zero_cases=len(rows),
                original_matrix_zero_cases=len(matrices),
                nonzero_outside_sufficient_window=1,
                cycles=rows,original_matrices=matrices,outside_window=outside)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_simultaneous_small_circle_face_correspondence_results.json');args=ap.parse_args()
    data=dict(status='PASS',formal_words=local_band_checks(),forests=forests(),source=original_sources(),
              disconnected_topology=disconnected_topology(),disconnected_source=disconnected_sources(),
              scope='All formal cyclic Chebyshev words and literal endpoint zeros; simultaneous component correspondence retaining full background phase before Laurent cancellation; original E/F/K, W/pi, cups and mark at both parities, dependency cycles and protected faces. Connected-subset polynomial identity plus exact disconnected vanishing when2sum(h_i-1)<N-1. No signed small port or generic normal claim.')
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':data['status'],'formal_words':data['formal_words'],'forests':data['forests'],
                      'source':{k:v for k,v in data['source'].items() if k!='cases'},
                      'disconnected_topology':data['disconnected_topology'],
                      'disconnected_source':{k:v for k,v in data['disconnected_source'].items() if k not in('cycles','original_matrices','outside_window')}},indent=2))


if __name__=='__main__':main()
