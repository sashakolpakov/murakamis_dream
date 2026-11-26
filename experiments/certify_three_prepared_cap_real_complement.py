#!/usr/bin/env python3
"""Exact retained L40 real-index complement for the prepared cap output square."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse,json,time
from flint import arb,acb,ctx
from certify_three_vertex_bidisk_packet import phase

ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)


def scalar(q):return arb(q.numerator)/q.denominator if isinstance(q,Q)else arb(q)
def interval(a,b):return scalar(a).union(scalar(b))
def mag(v):return max(abs(v.lower()),abs(v.upper()))


def outgoing(face,z):
    base=acb(arb(1)/6,arb(2).log()/(2*arb.pi()))
    if face<2:return base+arb(-1 if face==0 else 1)/200+I*(2*z-1)/200,I/100
    return base+(2*z-1)/200+I*arb(-1 if face==2 else 1)/200,acb(arb(1)/100)


def coordinates(key,p):
    pi=arb.pi()
    x=acb(arb(7)/50+arb(3)/50*p[0],interval(Q(10135867,10**8),Q(10135871,10**8)))
    y,fy=outgoing(key[0],p[1]);X=(2*pi*I*x).exp();Y=(2*pi*I*y).exp()
    ranges=[(Q(0),Q(1,40),Q(1,40),Q(9,20)),
            (Q(1,40),Q(1,4),Q(0),Q(9,20)),
            (Q(9,20),Q(9,20),Q(0),Q(9,20))]
    sl,sr,tl,tr=ranges[key[2]]
    ds,dt=scalar(sr-sl),scalar(tr-tl)
    s=scalar(sl)+ds*p[2];t=scalar(tl)+dt*p[3]
    if key[1]:s,t=t,s
    return x,y,X,Y,s,t,arb(3)/50,fy,ds,dt


def value(key,p):
    x,y,X,Y,s,t,*_=coordinates(key,p)
    return (phase(acb(s),acb(t),X,Y)-arb.pi()*I*(x+y)).real


def evaluate(key,box):
    p=[interval(a,b)for a,b in box];c=[scalar((a+b)/2)for a,b in box];r=[scalar((b-a)/2)for a,b in box]
    x,y,X,Y,s,t,dx,dy,ds,dt=coordinates(key,p);pi=arb.pi()
    U=(-2*pi*I*s).exp();V=(-2*pi*I*t).exp()
    fx=2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I
    fy=2*pi*I*t+(1-Y*V).log()-(1-Y).log()-pi*I
    fs=X.log()+(1-U*V).log()-(1-X*U).log()
    ft=Y.log()+(1-U*V).log()-(1-Y*V).log()
    if key[1]:fs,ft=ft,fs
    gradients=[dx*fx.real,(dy*fy).real,ds*fs.real,dt*ft.real]
    costs=[rr*mag(g)for rr,g in zip(r,gradients)]
    upper=value(key,c)+sum(costs)
    return upper<arb(6455)/10000,costs


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-prepared-cap-real-complement.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();visited=0;domains=[]
    for key in product(range(4),range(2),range(3)):
        todo=[('',tuple((Q(0),Q(1))for _ in range(4)))];leaves=[]
        while todo:
            path,box=todo.pop();visited+=1
            try:ok,costs=evaluate(key,box)
            except (ValueError,ZeroDivisionError):ok,costs=False,None
            if ok:leaves.append(path);continue
            if costs is not None and all(c.is_finite()for c in costs):axis=max(range(4),key=lambda j:float(costs[j].upper()))
            else:
                weights=[.06,.01,0 if key[2]==2 else .45,.45]
                axis=max(range(4),key=lambda j:float(box[j][1]-box[j][0])*weights[j])
            lo,hi=box[axis];assert hi-lo>Q(1,2**24),(key,box)
            mid=(lo+hi)/2
            for b,ends in enumerate(((lo,mid),(mid,hi))):
                child=list(box);child[axis]=ends;todo.append((path+str(2*axis+b),tuple(child)))
            assert visited<800000,'Incomplete coverage; no result saved.'
        domains.append({'domain':list(key),'dimension':4,'leaves':leaves})
        print(key,len(leaves),'visited',visited,flush=True)
    pi=arb.pi();r=arb(27)/50
    margins=[r-(-2*pi*arb(10135867)/10**8).exp(),r-arb(1)/2*(2*pi/200).exp(),
             (1+r*r).sqrt()-2*r,1-r-r*pi/4,
             arb(3)/4-(arb(7)/8-arb(7)/50)]
    assert all(m>0 for m in margins)
    deps=['notes/research_three_prepared_cap_real_complement.md','experiments/certify_three_vertex_bidisk_packet.py','notes/research_three_vertex_bidisk_packet.md']
    result={'status':'passed','precision_bits':args.precision,'domains':domains,'domain_count':len(domains),
            'leaf_count':sum(len(d['leaves'])for d in domains),'visited':visited,
            'scalar_margins':[str(m)for m in margins],'elapsed_seconds':time.monotonic()-start,
            'scope':'Original L40 retained real-index complement outside [.25,.45]^2 on the central input-wire segment and outgoing square radius1/200; cap bounds are separate.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','domain_count','leaf_count','visited','elapsed_seconds']}))


if __name__=='__main__':main()
