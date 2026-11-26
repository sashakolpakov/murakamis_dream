#!/usr/bin/env python3
"""Outward full-face bounds for the actual first-attachment index currents.

Every accepted leaf is a complete rational rectangle, not a sampled point.
The narrow wire-height interval is retained as an interval in every leaf.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse, json, time
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)
A, B, H = Q(1, 4), Q(9, 20), Q(1, 50)
XL, XR = Q(7, 50), Q(1, 5)
YL, YR = Q(10135867, 10**8), Q(10135871, 10**8)


def ball(x):
    return arb(x.numerator) / x.denominator if isinstance(x, Q) else arb(x)


def interval(a, b):
    return ball(a).union(ball(b))


def side(k, z):
    if k < 2:
        return acb(ball(A if k == 0 else B), -ball(H)+2*ball(H)*z), 2*I*ball(H)
    return acb(ball(A)+ball(B-A)*z, ball(-H if k == 2 else H)), acb(ball(B-A))


def parameters(p, height):
    x = acb(ball(XL)+ball(XR-XL)*p, height)
    y = acb(arb(1)/6, arb(2).log()/(2*arb.pi()))
    return x, y, (2*arb.pi()*I*x).exp(), (2*arb.pi()*I*y).exp()


def phase(s, t, x, y, X, Y):
    pi = arb.pi()
    U, V = (-2*pi*I*s).exp(), (-2*pi*I*t).exp()
    return ((U*V).polylog(2)-pi*pi/6-(X*U).polylog(2)+X.polylog(2)
            -(Y*V).polylog(2)+Y.polylog(2))/(2*pi*I)+s*X.log()+t*Y.log()-pi*I*(x+y)


def derivatives(s, t, X, Y):
    pi = arb.pi()
    U, V = (-2*pi*I*s).exp(), (-2*pi*I*t).exp()
    assert abs(X*U) < 1 and abs(Y*V) < 1
    assert (1-U*V).real > 0 or (1-U*V).imag < 0
    return (X.log()+(1-U*V).log()-(1-X*U).log(),
            Y.log()+(1-U*V).log()-(1-Y*V).log(),
            2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I)


def upperabs(v):
    return max(abs(v.lower()), abs(v.upper()))


def bound(key):
    return ball(Q(323, 500) if min(key) < 2 else Q(7, 10))


def evaluate(key, box):
    p = [interval(a,b) for a,b in box]
    c = [ball((a+b)/2) for a,b in box]
    radii = [ball((b-a)/2) for a,b in box]
    x,y,X,Y = parameters(p[0], interval(YL,YR))
    s,ds = side(key[0],p[1]);t,dt=side(key[1],p[2])
    fs,ft,fx=derivatives(s,t,X,Y)
    grads=[ball(XR-XL)*fx.real,(fs*ds).real,(ft*dt).real]
    costs=[r*upperabs(g) for r,g in zip(radii,grads)]
    height_cost=ball((YR-YL)/2)*upperabs(fx.imag)
    xc,yc,XX,YY=parameters(c[0],ball((YL+YR)/2))
    sc,_=side(key[0],c[1]);tc,_=side(key[1],c[2])
    top=phase(sc,tc,xc,yc,XX,YY).real+sum(costs)+height_cost
    return top<bound(key),costs,top


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-attachment-index-currents.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    domains=[];visited=0
    for key in product(range(4),repeat=2):
        todo=[('',tuple((Q(0),Q(1))for _ in range(3)))];leaves=[];max_upper=None
        while todo:
            path,box=todo.pop();visited+=1
            try:passed,costs,top=evaluate(key,box)
            except (AssertionError,ValueError,ZeroDivisionError):passed,costs=False,None
            if passed:
                leaves.append(path)
                max_upper=top.upper() if max_upper is None else max(max_upper,top.upper())
                continue
            if costs is not None and all(c.is_finite()for c in costs):
                axis=max(range(3),key=lambda k:float(costs[k].upper()))
            else:axis=max(range(3),key=lambda k:float(box[k][1]-box[k][0])*[.06,.2,.2][k])
            lo,hi=box[axis];assert hi-lo>Q(1,2**24),(key,box)
            mid=(lo+hi)/2
            for b,ends in enumerate(((lo,mid),(mid,hi))):
                child=list(box);child[axis]=ends;todo.append((path+str(2*axis+b),tuple(child)))
            assert visited<500000,'Incomplete coverage: no artifact saved.'
        domains.append({'domain':list(key),'dimension':3,'leaves':leaves,'upper_bound':str(max_upper)})
        print('face',key,'leaves',len(leaves),'upper',max_upper,flush=True)
    margins=[2*arb.pi()/50-arb(7)/10+arb(19113)/10000-arb(253)/200,
             arb(19113)/10000-arb(253)/200-arb(323)/500,
             arb('0.101358689576302370861575311618')-arb('0.00000001')-ball(YL),
             ball(YR)-arb('0.101358689576302370861575311618')-arb('0.00000001')]
    assert all(m>0 for m in margins)
    dependencies=['notes/research_three_attachment_index_currents.md',
                  'notes/research_three_vertex_joint_concavity.md',
                  'notes/research_root_pochhammer_interpolation.md',
                  'notes/research_three_cap_first_attachment.md']
    result={'status':'passed','precision_bits':args.precision,'domains':domains,
            'domain_count':len(domains),'leaf_count':sum(len(d['leaves'])for d in domains),
            'visited':visited,'scalar_margins':[str(m)for m in margins],
            'elapsed_seconds':time.monotonic()-start,
            'scope':'All exact interpolated index-side products and horizontal alias products for the first complete-cap attachment. No cap or real-index complement bound is inferred.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in dependencies}}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','domain_count','leaf_count','visited','elapsed_seconds']}))


if __name__=='__main__':main()
