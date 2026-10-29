#!/usr/bin/env python3
"""Actual endpoint q-connection/current and mixed underclock transport."""
from collections import Counter
import itertools
import json
from pathlib import Path

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import (
    setup,graph_blocks,charged_coefficient,evaluate_forms)
from audit_actual_general_flow_fusion import normalized_graph,contract_edge,graph_coefficient
from audit_actual_clock_feedback_normal_form import feedback_metadata,own_charged_data


def forms(H,edges):
    out=[]
    for e in edges:
        for r in range(e['L']):
            f={e['u']:1};j=e['v']
            f[j]=(f.get(j,0)-e['a']*pow(H.Q,r,H.p))%H.p
            out.append({i:c for i,c in f.items() if c})
    return out


def endpoint_data(H,edges,i):
    """Actual endpoint deletion, no inverse in the jet algebra."""
    p,Q=H.p,H.Q;remaining=[];den=[];num=[];phase=1
    for e in edges:
        u,v,L,a=e['u'],e['v'],e['L'],e['a']
        ee=forms(H,[e])
        if u==v:
            if u==i:phase=phase*pow(Q,L,p)%p
            remaining+=ee
        elif u==i:
            remaining+=ee[:-1];den.append(ee[-1])
            num.append({i:1,v:-pow(Q,-1,p)*a%p})
            phase=phase*pow(Q,L,p)%p
        elif v==i:
            remaining+=ee[1:];den.append(ee[0])
            num.append({u:1,i:-pow(Q,L,p)*a%p})
        else:remaining+=ee
    return remaining,den,num,phase


def endpoint_checks():
    rows=[]
    cases=[(2,3,[1,-2,1,-2],(0,0,0,1)),
           (3,3,[1,-2,1,-2],(0,1,1,2)),
           (4,3,[1,-2,1,-2],(1,1,2,2)),
           (3,3,[1,1,1,2,-1,2],(1,1,1,0,1,2))]
    for N,width,word,h in cases:
        H=HardyNetwork(N,1);p,Q,d=H.p,H.Q,N-1
        S=setup(H,width,word);G=graph_blocks(H,S,h)
        scalar,edges,nodes=normalized_graph(H,G);k=len(nodes)
        P=forms(H,edges);value=charged_coefficient(P,k,d,p)
        for i in nodes:
            deleted,D,A,phase=endpoint_data(H,edges,i)
            assert len(deleted)+len(D)==len(P) and len(D)==len(A)
            left=phase*charged_coefficient(deleted+A,k,d,p)%p
            assert left==pow(Q,d,p)*value%p
            for seed in range(4):
                xx=[11+seed+3*j for j in range(k)];yy=xx.copy();yy[i]=yy[i]*Q%p
                lhs=evaluate_forms(D,xx,p)*evaluate_forms(P,yy,p)%p
                rhs=phase*evaluate_forms(A,xx,p)*evaluate_forms(P,xx,p)%p
                assert lhs==rhs
        rows.append({'N':N,'word':word,'actual_clocks':h,'anchors':k,
                     'source_current_endpoint_deletions':k,'all_shifted_polynomial_identities':4*k,
                     'actual_selected_coefficient':scalar*value%p})
    return rows


def independent_parameters(H,S,R,path):
    p,q,x,Q=H.p,H.q,H.x,H.Q
    event=next(e for e in S['events'] if e['kind']=='bridge' and e['path']==path)
    V,W=R['z',event['input']],R['z',event['output']]
    aa=[R['a',j] for j in path];m=len(path);ts=[1];w=0
    for r,(j,a) in enumerate(zip(path,aa),1):
        w+=S['records'][j]['sign']
        ts.append(pow(-1,r,p)*pow(q,2+w,p)*pow(V*a,-1,p)%p)
    zs=[Q*Q*x*pow(aa[0]*V,-1,p)%p]
    zs += [pow(x,-1,p)*a*pow(b,-1,p)%p for a,b in zip(aa,aa[1:])]
    zs.append(aa[-1]*W%p)
    return ts,zs,w


def independent_coefficient(H,S,h,R):
    p,Q,d=H.p,H.Q,H.N-1;out=1
    for event in S['events']:
        V,W=R['z',event['input']],R['z',event['output']]
        if event['kind']=='closure':
            eta,t=(1,1) if event['head']==0 else (H.x*pow(pow(H.x,H.N,p),-1,p)%p,pow(Q,-1,p))
            out=out*eta*sum(pow(t*W*pow(V,-1,p)%p,a,p) for a in range(H.N))%p
            continue
        path=event['path'];ts,zs,w=independent_parameters(H,S,R,path)
        hs=[h[j] for j in path];ns=[d-hs[0]]+[a-b for a,b in zip(hs,hs[1:])]+[hs[-1]]
        out=out*H.N*pow(H.kappa,w,p)%p
        for n,z,t in zip(ns,zs,ts):
            out=out*H.inv[n]*pow(t,n,p)%p
            for r in range(n):out=out*(1-z*pow(Q,r,p))%p
    return out


def feedback_clock_checks():
    rows=[]
    for N,width,word in [(3,3,[1,-2,1,-2]),(4,3,[1,1,1,2,-1,2])]:
        H=HardyNetwork(N,1);p,Q,d=H.p,H.Q,N-1
        S=setup(H,width,word);_,meta=feedback_metadata(S);k=len(S['events'])
        X=[11+3*a for a in range(k)]
        base={key:pow(Q,r['q'],p)*pow(H.x,r['x'],p)*pow(X[r['anchor']],r['power'],p)%p
              for key,r in meta.items()}
        def shifted(h,extra=None):
            return {key:value*pow(Q,sum(t*h[j] for j,t in meta[key]['T'].items())+
                                 (meta[key]['T'].get(extra,0) if extra is not None else 0),p)%p
                    for key,value in base.items()}
        count=0;pointwise=0
        clocks=itertools.product(range(N),repeat=len(word))
        for h in clocks:
            if any(any(h[a]<h[b] for a,b in zip(path,path[1:])) for path in S['paths']):continue
            R=shifted(h);c=independent_coefficient(H,S,h,R)
            ff,ww,_,_=own_charged_data(H,S,h)
            actual=ww*evaluate_forms(ff,X,p)%p
            actual=actual*pow(math_product((pow(x,d,p) for x in X),p),-1,p)%p
            assert c==actual;pointwise+=1
            for path in S['paths']:
                hs=[h[j] for j in path];ns=[d-hs[0]]+[a-b for a,b in zip(hs,hs[1:])]+[hs[-1]]
                for r,j in enumerate(path,1):
                    if ns[r-1]==0:continue
                    hp=list(h);hp[j]+=1
                    Rp=shifted(hp)
                    assert Rp==shifted(h,extra=j)
                    ts,zs,_=independent_parameters(H,S,Rp,path)
                    den=(1-zs[r-1]*pow(Q,ns[r-1]-1,p))*(1-pow(Q,ns[r]+1,p))%p
                    num=ts[r]*pow(ts[r-1],-1,p)*(1-pow(Q,ns[r-1],p))*(1-zs[r]*pow(Q,ns[r],p))%p
                    lhs=den*independent_coefficient(H,S,hp,Rp)%p
                    rhs=num*independent_coefficient(H,S,h,Rp)%p
                    assert lhs==rhs;count+=1
        rows.append({'N':N,'word':word,'original_actual_feedback_coefficients':pointwise,
                     'cleared_mixed_clock_current_checks':count})
    return rows


def math_product(xs,p):
    answer=1
    for x in xs:answer=answer*x%p
    return answer


def macro_source_zero():
    rows=[]
    for N in range(2,13):
        H=HardyNetwork(N,1);p,Q,q,d=H.p,H.Q,H.q,N-1
        S=setup(H,3,[1,-2,1,-2]);G=graph_blocks(H,S,(d,0,0,0))
        scalar,edges,nodes=normalized_graph(H,G)
        while any(e['closure'] for e in edges):
            e=next(e for e in edges if e['closure'])
            ss,edges,nodes=contract_edge(H,edges,nodes,e['id']);scalar=scalar*ss%p
        target=[(5,0,d,Q),(6,0,d,pow(q,N+3,p)),
                (5,4,d,pow(q,N+1,p)),(0,6,d,pow(q,N-1,p))]
        assert Counter((e['u'],e['v'],e['L'],e['a']) for e in edges)==Counter(target)
        assert graph_coefficient(H,edges,nodes)==0
        incident={v:0 for v in nodes}
        for e in edges:incident[e['u']]+=e['L'];incident[e['v']]+=e['L']
        assert {v:incident[v]-2*d for v in nodes}=={0:d,4:-d,5:0,6:0}
        # Generic Fermat centers: every entire q-orbit endpoint is a unit.
        rr={};used=set()
        for v in sorted(nodes):
            root=next(a for a in range(2,p) if pow(a,N,p) not in used and -pow(a,N,p)%p not in used)
            rr[v]=root;used|={pow(root,N,p),-pow(root,N,p)%p}
        assert all(pow(rr[e['u']],N,p)!=pow(e['a']*rr[e['v']]%p,N,p) for e in edges)
        # Literal source contractions leave the zero loop.
        for u,v in [(5,0),(0,4),(6,4)]:
            e=next(e for e in edges if e['u']==u and e['v']==v)
            ss,edges,nodes=contract_edge(H,edges,nodes,e['id']);scalar=scalar*ss%p
        assert len(edges)==1 and edges[0]['u']==edges[0]['v']==4 and edges[0]['a']==1
        rows.append({'N':N,'actual_clocks':[d,0,0,0],
                     'macro_defects':{0:d,4:-d,5:0,6:0},'actual_source_coefficient':0,
                     'entire_connection_regular_on_generic_Fermat_orbits':True,
                     'source_null_full_loop_after_exact_contractions':True})
    return rows


def main():
    out={'endpoint_connection_and_original_source_current':endpoint_checks(),
         'actual_T_feedback_clock_connection':feedback_clock_checks(),
         'all_N_actual_macro_defect_source_zero':macro_source_zero(),
         'scope':'exact bounded-degree endpoint and mixed clock transport; '
                 'endpoint-deleted source extension required; no geometric noncancellation'}
    Path(__file__).with_name('audit_actual_charged_connection_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS original endpoint/source currents, mixed actual-clock feedback, '
          'and 11 actual macro-defect sectors with regular connection but zero source')


if __name__=='__main__':main()
