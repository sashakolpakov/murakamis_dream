#!/usr/bin/env python3
"""Literal marked Morse source versus actual fixed-label cycle Fourier sums."""
import json
from pathlib import Path
import numpy as np
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from audit_general_odd_endpoint_matching_network import apply_pair
from audit_actual_q_hahn_partner_normal_collision import original_column


def convolution(a,b,p):
    n=len(a);out=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[(i+j)%n]=(out[(i+j)%n]+x*y)%p
    return out


def run(N,k,pattern):
    loc=Local(N);p,q,d=loc.p,loc.q,N-1;Q=q*q%p;M=d//2
    boxes=list(range(1,2*k-2,2))+list(range(0,2*k-1,2))+list(range(1,2*k-2,2))
    labels=[]
    for i in range(len(boxes)):
        a=M if pattern<3 else (i+pattern)%(M+1)
        r=[0,a,2*a,(2*i+pattern)%(2*a+1)][min(pattern,3)]
        labels.append((a,r))
    marker=np.array([[pow(loc.x,b,p)*pow(N*N,-1,p)%p for b in range(N)] for a in range(N)],dtype=np.int64)
    nodes=[];edges={}
    def node(kind,T,mat,a=None):
        idx=len(nodes);nodes.append(dict(kind=kind,T=T,mat=mat,a=a));return idx
    def connect(a,b):edges[a]=b;edges[b]=a
    current=[]
    state=np.array([1],dtype=np.int64)
    for h in range(k):
        v=node('cup',d,loc.cup[0]);current.extend([(v,0),(v,1)])
        state=np.kron(state,loc.cup[0].reshape(-1))%p
    state=state.reshape((N,)*(2*k))
    for slot,(a,r) in zip(boxes,labels):
        T=d-a+r
        white=loc.pi[a][0][r,:].reshape(N,N)
        black=loc.W[a][0][:,r].reshape(N,N)
        vin=node('pi',T,white,a);vout=node('W',T,black,a)
        connect(current[slot],(vin,0));connect(current[slot+1],(vin,1))
        current[slot],current[slot+1]=(vout,0),(vout,1)
        coupon=np.outer(loc.W[a][0][:,r],loc.pi[a][0][r,:])%p
        state=apply_pair(coupon,state,slot,N,p)
    row=np.array([1],dtype=np.int64)
    mark_id=None
    for h in range(k):
        mat=marker if h==k-1 else loc.cap[0]
        v=node('mark' if h==k-1 else 'cap',None if h==k-1 else d,mat)
        if h==k-1:mark_id=v
        connect(current[2*h],(v,0));connect(current[2*h+1],(v,1))
        row=np.kron(row,mat.reshape(-1))%p
    literal=int(row@state.reshape(-1)%p)
    polynomial_cache={}
    count=dict(physical_vertex_polynomials=0,first_failure_zero_cases=0,
               coherent_components=0,even_carrier_components=0,marked_paths=0,
               exact_charged_mark_coefficients=0)
    def poly(t,a):
        key=t,a
        if key in polynomial_cache:return polynomial_cache[key]
        values=[]
        for u in range(N):
            f=original_column(N,t,a,u,p,q)[0] if u<=t else 0
            values.append(f*pow(q,-(d-2*a)*u,p)%p)
        coeff=[sum(values[u]*pow(Q,-u*h,p) for u in range(N))*pow(N,-1,p)%p for h in range(N)]
        assert all(v==0 for v in coeff[a+1:])
        polynomial_cache[key]=coeff[:a+1]
        return coeff[:a+1]
    for data in nodes:
        if data['kind'] not in ('W','pi'):continue
        T,a=data['T'],data['a'];t=min(T,2*d-T);offset=max(0,T-d)
        coeff=poly(t,a);base=int(data['mat'][offset,T-offset]);assert base
        for u in range(N):
            v=T-u
            if 0<=v<N:
                y=u-offset
                f=sum(c*pow(q,(d-2*a+2*h)*y,p) for h,c in enumerate(coeff))%p
                assert int(data['mat'][u,v])==base*f%p
        data['base']=base;data['coeff']=coeff;data['offset']=offset
        count['physical_vertex_polynomials']+=1
    visited=set();cycle_product=fourier_product=charged_product=1;divergences=[]
    def follow(start,entry):
        order=[];v,port=start,entry
        while True:
            order.append((v,port));v,port=edges[(v,1-port)]
            if (v,port)==(start,entry):break
        return order
    while len(visited)<len(nodes):
        start=next(v for v in range(len(nodes)) if v not in visited)
        order=follow(start,0);ids={v for v,_ in order};visited|=ids
        outgoing=sum(nodes[v]['kind'] in ('W','cup') for v in ids)
        incoming=sum(nodes[v]['kind'] in ('pi','cap','mark') for v in ids)
        assert outgoing==incoming
        div=sum(nodes[v]['T']-d for v in ids if nodes[v]['kind']=='W')-sum(nodes[v]['T']-d for v in ids if nodes[v]['kind']=='pi')
        divergences.append(div)
        marked=mark_id in ids
        if marked:
            order=[];v,port=edges[(mark_id,1)]
            while v!=mark_id:
                order.append((v,port));v,port=edges[(v,1-port)]
            assert port==0;count['marked_paths']+=1
        # Literal source contraction of this component.
        direct=0;continued_modular=0
        for x in range(N):
            u=x;value=1;continued=1;valid=True
            for v,entry in order:
                data=nodes[v];out=data['T']-u
                first=u if entry==0 else out;second=out if entry==0 else u
                if not(0<=first<N and 0<=second<N):valid=False;value=0
                elif valid:value=value*int(data['mat'][first,second])%p
                if data['kind'] in ('W','pi'):
                    y=first-data['offset'];a=data['a']
                    f=sum(c*pow(q,(d-2*a+2*h)*y,p) for h,c in enumerate(data['coeff']))%p
                    continued=continued*data['base']*f%p
                else:
                    continued=continued*int(data['mat'][0,d])*pow(q,d*first,p)%p
                u=out
            if not valid:
                assert continued==0;count['first_failure_zero_cases']+=1
            if marked:
                if valid:direct=(direct+value*int(marker[u,x]))%p
                continued_modular=(continued_modular+continued*pow(N,-2,p)*pow(q,d*x,p))%p
            else:
                if valid and u==x:direct=(direct+value)%p
                if (u-x)%N==0:continued_modular=(continued_modular+continued)%p
        assert direct==continued_modular
        # Independent Fourier multiplication with literal affine lifts.
        coeff=[1]+[0]*(2*N-1);eps=1;shift=0
        for v,entry in order:
            data=nodes[v]
            se=eps if entry==0 else -eps
            sb=shift if entry==0 else data['T']-shift
            local=[0]*(2*N)
            if data['kind'] in ('W','pi'):
                sb-=data['offset'];a=data['a']
                for h,g in enumerate(data['coeff']):
                    carrier=d-2*a+2*h
                    pos=carrier*se%(2*N)
                    local[pos]=(local[pos]+data['base']*g*pow(q,carrier*sb,p))%p
            else:
                local[d*se%(2*N)]=int(data['mat'][0,d])*pow(q,d*sb,p)%p
            coeff=convolution(coeff,local,p)
            eps,shift=-eps,data['T']-shift
        if marked:
            ordinary_cap=[0]*(2*N)
            ordinary_cap[d*eps%(2*N)]=pow(N,-1,p)*pow(q,d*shift,p)%p
            ordinary_coeff=convolution(coeff,ordinary_cap,p)
            charged=pow(q,-d*d,p)*ordinary_coeff[2]%p
            if div==0:
                assert eps==-1 and shift==d
                count['exact_charged_mark_coefficients']+=1
            extra=[0]*(2*N);extra[d%(2*N)]=pow(N,-2,p)
        else:
            assert eps==1
            if div==0:assert shift==0
            else:assert direct==0
            charged=N*coeff[0]%p if div==0 else 0
            extra=[0]*(2*N)
            for h in range(N):
                pos=2*h*(eps-1)%(2*N)
                extra[pos]=(extra[pos]+pow(N,-1,p)*pow(q,2*h*shift,p))%p
        coeff=convolution(coeff,extra,p);transformed=0
        assert all(coeff[m]==0 for m in range(1,2*N,2))
        count['even_carrier_components']+=1
        for m,c in enumerate(coeff):
            kernel=N if m==0 else 0 if m%2==0 else 2*pow(1-pow(q,m,p),-1,p)%p
            assert kernel%p==sum(pow(q,m*x,p) for x in range(N))%p
            transformed=(transformed+c*kernel)%p
        assert transformed==direct
        cycle_product=cycle_product*direct%p;fourier_product=fourier_product*transformed%p
        charged_product=charged_product*charged%p
        count['coherent_components']+=1
    assert sum(divergences)==0
    if all(v==0 for v in divergences):assert literal==charged_product
    else:assert literal==0
    assert literal==cycle_product==fourier_product
    return dict(N=N,plat_width=k,pattern=pattern,circles=len(boxes),literal_source=literal,
                nonzero_source=bool(literal),kirchhoff_flow=all(v==0 for v in divergences),**count)


def main():
    rows=[run(N,k,pattern) for N,k in [(2,2),(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(3,4)] for pattern in range(5)]
    assert sum(r['first_failure_zero_cases'] for r in rows)>0
    assert any(r['kirchhoff_flow'] for r in rows) and not all(r['kirchhoff_flow'] for r in rows)
    result=dict(status='PASS',cases=rows,
                scope='Exact original marked complete-circle fixed-label contractions, actual white maps, first-failure extension and shared cycle Fourier sums at both parities. No global energy asymptotic or noncancellation follows.')
    Path(__file__).with_name('actual_matching_graph_shared_cycle_fourier_compiler_results.json').write_text(json.dumps(result,indent=2)+'\n')
    totals={key:sum(r[key] for r in rows) for key in ['nonzero_source','kirchhoff_flow','physical_vertex_polynomials','first_failure_zero_cases','coherent_components','even_carrier_components','marked_paths','exact_charged_mark_coefficients']}
    print(json.dumps(dict(status='PASS',actual_fixed_label_plats=len(rows),**totals),indent=2))


if __name__=='__main__':main()
