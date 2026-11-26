#!/usr/bin/env python3
"""Independent primitive and exact-cover replay of first-attachment currents.

No author checker is imported. The phase uses the positive-exponential
sine primitive rather than the author's negative-exponential dilogarithm.
"""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse, json, time
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)


def scalar(r):
    return arb(r.numerator)/r.denominator if isinstance(r,R) else arb(r)


def interval(a,b):
    return scalar(a).union(scalar(b))


def partition(paths,dim):
    assert len(paths)==len(set(paths))
    trie={}
    for path in paths:
        node=trie
        for digit in path:
            assert '$' not in node
            k=int(digit);assert 0<=k<2*dim
            node=node.setdefault(k,{})
        assert not node
        node['$']=True
    stack=[(trie,tuple((R(0),R(1))for _ in range(dim)))]
    while stack:
        node,box=stack.pop()
        if '$'in node:
            assert len(node)==1
            yield box;continue
        keys=sorted(node);assert len(keys)==2 and keys[0]%2==0 and keys[1]==keys[0]+1
        axis=keys[0]//2;lo,hi=box[axis];mid=(lo+hi)/2
        for digit,ends in zip(keys,((lo,mid),(mid,hi))):
            child=list(box);child[axis]=ends;stack.append((node[digit],tuple(child)))


def index(k,p):
    if k<2:return acb(arb(1)/4 if k==0 else arb(9)/20,-arb(1)/50+p/25)
    return acb(arb(1)/4+p/5,arb(-1 if k==2 else 1)/50)


def coordinates(key,p,height):
    pi=arb.pi()
    x=acb(arb(7)/50+arb(3)/50*p[0],height)
    y=acb(arb(1)/6,arb(2).log()/(2*pi))
    X=(2*pi*I*x).exp();Y=(2*pi*I*y).exp()
    s=index(key[0],p[1]);t=index(key[1],p[2])
    return x,y,X,Y,s,t


def action(key,box):
    p=[interval(a,b)for a,b in box];pi=arb.pi()
    x,y,X,Y,s,t=coordinates(key,p,interval(R(10135867,10**8),R(10135871,10**8)))
    U=(-2*pi*I*s).exp();V=(-2*pi*I*t).exp()
    assert abs(X*U)<1 and abs(Y*V)<1
    sine=2*(pi*(s+t)).sin();assert sine.real>0
    common=sine.log()+pi*I*(arb(1)/2-s-t)
    fs=common+X.log()-(1-X*U).log()
    ft=common+Y.log()-(1-Y*V).log()
    fx=2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I
    ds=I/25 if key[0]<2 else acb(arb(1)/5)
    dt=I/25 if key[1]<2 else acb(arb(1)/5)
    grads=[arb(3)/50*fx.real,(ds*fs).real,(dt*ft).real]
    error=sum(scalar((b-a)/2)*abs(g)for (a,b),g in zip(box,grads))
    error+=arb(2)/10**8*abs(fx.imag)
    center=[scalar((a+b)/2)for a,b in box]
    x,y,X,Y,s,t=coordinates(key,center,arb(10135869)/10**8)
    z=s+t
    J=-I*pi*(z*z-z)/2+I*(2*pi*I*z).exp().polylog(2)/(2*pi)-I*pi/12
    def integ(w,Z):return ((Z*(-2*pi*I*w).exp()).polylog(2)-Z.polylog(2))/(2*pi*I)
    return (J+I*pi*(z-z*z)/2+s*X.log()+t*Y.log()-integ(s,X)-integ(t,Y)-pi*I*(x+y)).real+error


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',default='repro/results/research-three-attachment-index-currents-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    artifact=ROOT/'repro/results/research-three-attachment-index-currents.json'
    data=json.loads(artifact.read_text());assert data['status']=='passed'
    expected=set(product(range(4),repeat=2));seen=set();original=refined=visited=0
    for domain in data['domains']:
        key=tuple(domain['domain']);assert key in expected and key not in seen;seen.add(key)
        assert domain['dimension']==3
        threshold=arb(323)/500 if min(key)<2 else arb(7)/10
        for box in partition(domain['leaves'],3):
            original+=1;todo=[box]
            while todo:
                current=todo.pop();visited+=1
                if action(key,current)<threshold:refined+=1;continue
                axis=max(range(3),key=lambda k:(current[k][1]-current[k][0])*[R(3,50),R(1,5)if key[0]>1 else R(1,25),R(1,5)if key[1]>1 else R(1,25)][k])
                lo,hi=current[axis];assert hi-lo>R(1,2**25),(key,current)
                mid=(lo+hi)/2
                for ends in ((lo,mid),(mid,hi)):
                    child=list(current);child[axis]=ends;todo.append(tuple(child))
                assert visited<1000000,'Incomplete replay: no result saved.'
        print('replayed',key,'leaves_so_far',refined,flush=True)
    assert seen==expected and original==data['leaf_count']
    margins=[2*arb.pi()/50-arb(7)/10+arb(19113)/10000-arb(253)/200,
             arb(19113)/10000-arb(253)/200-arb(323)/500]
    assert all(m>0 for m in margins)
    for p,h in data['dependencies_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert sha256((ROOT/'experiments/certify_three_attachment_index_currents.py').read_bytes()).hexdigest()==data['script_sha256']
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
            'original_leaf_count':original,'replayed_leaf_count':refined,'visited':visited,
            'exact_binary_cover':True,'scalar_margins':[str(m)for m in margins],
            'elapsed_seconds':time.monotonic()-start,
            'artifact_sha256':sha256(artifact.read_bytes()).hexdigest(),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Independent complete rational partition and positive-exponential primitive with outward sine-log derivative enclosures; no author-code import or sampled maximum.',
            'earlier_attempt':'An initial direct full-interval primitive replay exhausted its visit cap and saved no result. The present replay uses a center primitive and rigorous interval derivatives, retaining complete coverage.'}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
