#!/usr/bin/env python3
"""Literal Morse regions -> signed monomial -> exact original coefficient.

All source comparisons use the original finite W/pi, cups, caps and mark.
The face determinant is independently built by its scalar continuant.
"""
import argparse
from collections import Counter, defaultdict
import itertools
import json
from pathlib import Path
import numpy as np

def morse_faces(k, boxes, marked=None):
    if marked is None:
        marked=k-1
    parent=list(range(k+1))
    gap=[0]*(2*k+1)
    parity={0:0}
    for j in range(k):
        gap[2*j+1]=j+1
        parity[j+1]=1
    bottom=gap[:]
    circles=[]
    for slot in boxes:
        before=tuple(gap[slot:slot+3])
        new=len(parent)
        parent.append(new)
        parity[new]=(slot+1)%2
        gap[slot+1]=new
        circles.append((before[0],before[1],new,before[2]))
    top=gap[:]
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for j in range(0,2*k+1,2):
        parent[root(gap[j])]=root(0)
    representatives=sorted({root(j) for j in range(len(parent))})
    assert representatives[0]==0
    idx={r:j for j,r in enumerate(representatives)}
    translate=lambda x:idx[root(x)]
    ff=[tuple(translate(x) for x in f) for f in circles]
    bb=[translate(x) for x in bottom]
    tt=[translate(x) for x in top]
    pf={translate(x):value for x,value in parity.items()}
    assert all(pf[translate(x)]==value for x,value in parity.items())
    middles=Counter()
    turns=Counter()
    for _,b,c,_ in ff:
        middles[b]+=1
        middles[c]+=1
    for line in (bb,tt):
        for j in range(k):
            assert line[2*j]==line[2*j+2]
            turns[line[2*j]]+=1
            turns[line[2*j+1]]-=1
    assert all(any(slot==2*j-1 for slot in boxes) for j in range(1,k))
    assert len(representatives)==len(boxes)+2
    for f in range(len(representatives)):
        assert middles[f]-turns[f]==(-2 if f==0 else 2)
    v=tt[2*marked+1]
    assert v!=0 and pf[v]==1
    return {'k':k,'boxes':boxes,'marked':marked,'circles':ff,
            'bottom':bb,'top':tt,'faces':len(representatives),'v':v,
            'parity':pf,'middle':middles,'turns':turns}


def mul(A,B,p,cap=None):
    out=defaultdict(int)
    for aa,va in A.items():
        for bb,vb in B.items():
            cc=tuple(x+y for x,y in zip(aa,bb))
            if cap is not None and max(cc,default=0)>cap:
                continue
            out[cc]=(out[cc]+va*vb)%p
    return {a:v for a,v in out.items() if v}


def add(A,B,p,scale=1):
    out=dict(A)
    for a,v in B.items():
        out[a]=(out.get(a,0)+scale*v)%p
    return {a:v for a,v in out.items() if v}


def local_polynomials(loc,a):
    p,q,Q=loc.p,loc.q,loc.Q
    imag=pow(loc.eta,loc.N,p)
    inv2=pow(2,-1,p)
    def sin(n):return (pow(q,n,p)-pow(q,-n,p))*pow(2*imag,-1,p)%p
    def cos(n):return (pow(q,n,p)+pow(q,-n,p))*inv2%p
    old={(0,0,0):1}
    prev={}
    for n in range(a):
        diag=pow(cos(n)*cos(n+1),-1,p)*inv2%p
        linear={(1,0,0):diag,(0,1,0):1,(0,0,1):diag}
        now=mul(linear,old,p)
        if n:
            b=sin(n)**2*pow(cos(n)**2*sin(2*n-1)*sin(2*n+1),-1,p)%p
            factor=b*pow(4,-1,p)%p
            quadratic={(2,0,0):factor,(0,0,2):factor,
                       (1,0,1):-2*factor*cos(2*n)%p}
            now=add(now,mul(quadratic,prev,p),p,-1)
        prev,old=old,now
    assert all(sum(e)==a for e in old)
    forced={(0,0):1}
    for j in range(a+1,loc.d-a+1):
        forced=mul(forced,{(1,0):1,(0,1):-pow(Q,j,p)%p},p)
    s=loc.d-2*a
    assert all(sum(e)==s for e in forced)
    return old,forced


def substitute(poly,face_ids,variables,p):
    out=defaultdict(int)
    for exponents,c in poly.items():
        new=[0]*len(variables)
        valid=True
        for face,power in zip(face_ids,exponents):
            if face not in variables:
                if power:
                    valid=False
                    break
            else:
                new[variables.index(face)]+=power
        if valid:
            out[tuple(new)]=(out[tuple(new)]+c)%p
    return {a:v for a,v in out.items() if v}


def evaluate(poly,values,p):
    answer=0
    for exponents,c in poly.items():
        value=c
        for x,e in zip(values,exponents):value=value*pow(x,e,p)%p
        answer=(answer+value)%p
    return answer


def original_source(loc,chart,labels,signs):
    from audit_general_odd_endpoint_matching_network import apply_pair

    N,p=loc.N,loc.p
    state=np.array([1],dtype=np.int64)
    marked=np.array([1],dtype=np.int64)
    ordinary=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)]
                     for i in range(N)],dtype=np.int64)
    for j in range(chart['k']):
        state=np.kron(state,loc.cup[0].reshape(-1))%p
        ordinary=np.kron(ordinary,loc.cap[0].reshape(-1))%p
        marked=np.kron(marked,(marker if j==chart['marked'] else loc.cap[0]).reshape(-1))%p
    state=state.reshape((N,)*(2*chart['k']))
    coupons=[]
    for slot,a,eps in zip(chart['boxes'],labels,signs):
        mat=loc.h0[a]*pow(loc.omega[a],eps,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p
        coupons.append(mat)
        state=apply_pair(mat,state,slot,N,p)
    assert int(ordinary@state.reshape(-1)%p)==0
    return int(marked@state.reshape(-1)%p),coupons


def case(N,k,boxes,labels,grid=True,marked=None):
    from audit_actual_nc_morse_graph_first_normal_source_reduction import Local

    loc=Local(N)
    p,q,d=loc.p,loc.q,loc.d
    chart=morse_faces(k,boxes,marked)
    signs=[(-1,0,1)[j%3] for j in range(len(boxes))]
    polys={a:local_polynomials(loc,a) for a in set(labels)}
    variables=[f for f in range(chart['faces']) if f not in (0,chart['v'])]
    product={(0,)*len(variables):1}
    for (x,b,c,y),a in zip(chart['circles'],labels):
        D,P=polys[a]
        for poly,ids in [(D,(x,b,y)),(D,(x,c,y)),(P,(x,y))]:
            product=mul(product,substitute(poly,ids,variables,p),p,d)
    coefficient=product.get((d,)*len(variables),0)
    imag=pow(loc.eta,N,p)
    sine=[pow(imag,j,p)*pow(q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
    scalar=1
    for a,eps in zip(labels,signs):
        beta=sine[2*a]*pow(sine[a]**2,-1,p)%p
        ka=1 if 2*a==d else 2
        scalar=scalar*ka*beta**2*pow(loc.omega[a],eps,p)%p
    original,coupons=original_source(loc,chart,labels,signs)
    predicted=pow(N,len(boxes),p)*scalar*coefficient%p
    assert original==predicted,(N,k,labels,original,predicted)
    stats={'N':N,'width':k,'boxes':len(boxes),'labels':list(labels),
           'marked_cap':chart['marked'],'coefficient':coefficient,
           'original_source':original,'grid_points':0,'supported_grid_states':0,
           'forbidden_grid_states':0,'nontrivial_even_carries':0}
    if not grid:
        return stats
    grid_sum=0
    seen=set()
    t=chart['parity'] if N%2==0 else {f:0 for f in range(chart['faces'])}
    for potentials in itertools.product(range(N),repeat=chart['faces']-1):
        pf=(0,)+potentials
        Z=[pow(q,t[f],p)*pow(loc.Q,pf[f],p)%p for f in range(chart['faces'])]
        value=1
        for (x,b,c,y),a in zip(chart['circles'],labels):
            D,P=polys[a]
            value=value*evaluate(D,(Z[x],Z[b],Z[y]),p)%p
            value=value*evaluate(D,(Z[x],Z[c],Z[y]),p)%p
            value=value*evaluate(P,(Z[x],Z[y]),p)%p
        for f in variables:value=value*pow(Z[f],-d,p)%p
        full_value=value*scalar*pow(N,-1,p)%p
        def head(left,right):
            assert (d+t[left]-t[right])%2==0
            return (d+t[left]-t[right])//2+pf[left]-pf[right]
        physical=[head(l,r)%N for l,r in zip(chart['bottom'],chart['bottom'][1:])]
        path=[tuple(physical)]
        entry=1
        for i in range(k):entry=entry*int(loc.cup[0][physical[2*i],physical[2*i+1]])%p
        supported=True
        carries=0
        for n,((x,b,c,y),a,slot) in enumerate(zip(chart['circles'],labels,boxes)):
            si,sj=head(x,b),head(b,y)
            ro,rj=head(x,c),head(c,y)
            incoming=[si%N,sj%N]
            outgoing=[ro%N,rj%N]
            assert physical[slot:slot+2]==incoming
            ti,to=sum(incoming),sum(outgoing)
            if not (d-a<=ti<=d+a and ti==to):supported=False
            carries+=sum(z//N for z in (si,sj,ro,rj))!=0
            entry=entry*int(coupons[n][outgoing[0]*N+outgoing[1],incoming[0]*N+incoming[1]])%p
            physical[slot:slot+2]=outgoing
            path.append(tuple(physical))
        for i in range(k):
            a,b=physical[2*i:2*i+2]
            assert a+b==d
            factor=pow(loc.x,b,p)*pow(N*N,-1,p)%p if i==chart['marked'] else int(loc.cap[0][a,b])
            entry=entry*factor%p
        assert full_value==entry,(N,k,labels,potentials,full_value,entry)
        if supported:
            key=tuple(path)
            assert key not in seen
            seen.add(key)
            stats['supported_grid_states']+=1
            if N%2==0 and carries:stats['nontrivial_even_carries']+=1
        else:
            assert full_value==0
            stats['forbidden_grid_states']+=1
        grid_sum=(grid_sum+value)%p
        stats['grid_points']+=1
    assert grid_sum==pow(N,chart['faces']-1,p)*coefficient%p
    assert grid_sum*scalar*pow(N,-1,p)%p==original
    return stats


def signed_sweep_audit():
    count=faces=0
    for k in range(2,9):
        odd=list(range(1,2*k-2,2))
        even=list(range(0,2*k-1,2))
        for boxes in [odd+even+odd,odd+even+odd+even+odd,list(reversed(odd+even+odd))]:
            for marked in range(k):
                chart=morse_faces(k,boxes,marked)
                for d in range(2,9):
                    # Integer exponent identity, including even-N half powers.
                    ordinary={f:d*(chart['turns'][f]-chart['middle'][f])//2 for f in range(chart['faces'])}
                    assert ordinary[0]==d
                    assert all(ordinary[f]==-d for f in range(1,chart['faces']))
                    ordinary[0]-=d;ordinary[chart['v']]+=d
                    assert ordinary[0]==ordinary[chart['v']]==0
                    assert sum(ordinary.values())==-d*len(boxes)
                    faces+=chart['faces'];count+=1
    return {'signed_sweep_cases':count,'exact_marked_face_exponents':faces}


def run():
    rows=[]
    for N in range(3,8):
        M=(N-1)//2
        for labels in [(M,)*4,(0,)*4,tuple(j%(M+1) for j in range(4))]:
            rows.append(case(N,2,[1,0,2,1],labels,grid=N<=5))
    for N in [3,4]:
        boxes=[1,3,0,2,4,1,3]
        M=(N-1)//2
        rows.append(case(N,3,boxes,(M,)*len(boxes),grid=N==3,marked=1))
    counts=signed_sweep_audit()
    counts['original_fixed_sector_coefficients']=len(rows)
    for key in ['grid_points','supported_grid_states','forbidden_grid_states','nontrivial_even_carries']:
        counts[key]=sum(r[key] for r in rows)
    return {'status':'PASS','counts':counts,'cases':rows,
            'scope':'Exact original fixed-sector matrices versus positive face coefficient, primitive grid measure, both parity cosets, literal marked-cap sign and support/carry zeros. No asymptotic or nonzero coefficient is inferred.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_original_marked_face_coefficient_results.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['counts']}))
