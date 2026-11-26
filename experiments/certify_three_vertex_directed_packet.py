#!/usr/bin/env python3
"""Outward compact certificate for the actual retained three-crossing packet.

No sampled inequality is accepted.  Each leaf is a rational binary rectangle;
its full interval, or a first-derivative mean-value enclosure, is checked.
The paths in the result preserve the complete partition for independent replay.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse
import json
import time
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
U, VL, VH = Q(13, 1000), Q(-3, 2000), Q(1, 1000)
A, B, HEIGHT = Q(1, 4), Q(9, 20), Q(1, 50)
REGIONS = [(Q(0), Q(1, 50), Q(1, 50)),
           (Q(1, 50), Q(1, 4), Q(0)), (B, B, Q(0))]
I = acb(0, 1)


def ball(x):
    return arb(x.numerator) / x.denominator if isinstance(x, Q) else arb(x)


def interval(a, b):
    return ball(a).union(ball(b))


def wire(face, z):
    base = acb(arb(1) / 6, arb(2).log() / (2 * arb.pi()))
    if face < 2:
        return (base + (1 - 4 * I / 5) * ball(0 if face == 0 else U)
                + I * (ball(VL) + ball(VH - VL) * z), I * ball(VH - VL))
    return (base + (1 - 4 * I / 5) * ball(U) * z
            + I * ball(VL if face == 2 else VH), (1 - 4 * I / 5) * ball(U))


def full_wire(u, v):
    return (acb(arb(1) / 6, arb(2).log() / (2 * arb.pi()))
            + (1 - 4 * I / 5) * ball(U) * u
            + I * (ball(VL) + ball(VH - VL) * v))


def critical(x, y):
    pi = arb.pi()
    X, Y = (2 * pi * I * x).exp(), (2 * pi * I * y).exp()
    a, b = 1 / X - 1, 1 / Y - 1
    delta = 1 - 2 * (a + b) + (a - b)**2
    assert delta.imag > 0
    root = delta.sqrt()
    u, v = (1 + a - b - root) / 2, (1 - a + b - root) / 2
    assert u.real < 0 and u.imag < 0 and v.real < 0 and v.imag < 0
    return X, Y, u, v, I * u.log() / (2 * pi), I * v.log() / (2 * pi)


def primitive(z):
    z, pi = acb(z), arb.pi()
    return -I * pi * (z*z-z) / 2 + I * (2*pi*I*z).exp().polylog(2)/(2*pi) - I*pi/12


def phase(s, t, X, Y):
    pi = arb.pi()
    def integral(z, w):
        return ((w * (-2*pi*I*z).exp()).polylog(2)-w.polylog(2))/(2*pi*I)
    return (primitive(s+t)+I*pi*((s+t)-(s+t)**2)/2+s*X.log()+t*Y.log()
            - integral(s, X)-integral(t, Y))


def derivatives(s, t, X, Y):
    u, v = (-2*arb.pi()*I*s).exp(), (-2*arb.pi()*I*t).exp()
    return (X.log()+(1-u*v).log()-(1-X*u).log(),
            Y.log()+(1-u*v).log()-(1-Y*v).log(), u, v)


def index_side(face, z):
    if face < 2:
        return acb(ball(A if face == 0 else B), -ball(HEIGHT)+2*ball(HEIGHT)*z), 2*I*ball(HEIGHT)
    return acb(ball(A)+ball(B-A)*z, ball(-HEIGHT if face == 2 else HEIGHT)), acb(ball(B-A))


def domains():
    yield ('geometry',), 4
    for f, g in product(range(4), repeat=2):
        yield ('floor', f, g), 2
        for r in range(3):
            yield ('exterior', f, g, r), 4
        for j, k in product(range(4), repeat=2):
            yield ('contour', f, g, j, k), 4


def abs_upper(x):
    return max(abs(x.lower()), abs(x.upper()))


def evaluate(domain, box):
    p = [interval(a, b) for a, b in box]
    c = [ball((a+b)/2) for a, b in box]
    radii = [ball((b-a)/2) for a, b in box]
    if domain[0] == 'geometry':
        X, Y, u, v, s, t = critical(full_wire(p[0], p[1]), full_wire(p[2], p[3]))
        margins = [X.real-ball(Q(2,25)), X.imag-ball(Q(2,25)),
                   Y.real-ball(Q(2,25)), Y.imag-ball(Q(2,25)),
                   ball(Q(27,50))-abs(X), ball(Q(27,50))-abs(Y)]
        for z in (s, t):
            margins += [z.real-ball(Q(3,10)), ball(Q(2,5))-z.real,
                        ball(Q(3,200))-abs(z.imag)]
        return all(z > 0 for z in margins), None, min(z.lower() for z in margins)
    _, f, g, *extra = domain
    x, dx = wire(f, p[0]); y, dy = wire(g, p[1])
    X, Y, u, v, sc, tc = critical(x, y)
    if domain[0] == 'floor':
        grads = [(2*arb.pi()*I*sc+(1-X*u).log()-(1-X).log())*dx,
                 (2*arb.pi()*I*tc+(1-Y*v).log()-(1-Y).log())*dy]
        Xc, Yc, _, _, ss, tt = critical(wire(f,c[0])[0],wire(g,c[1])[0])
        value = phase(ss,tt,Xc,Yc).real
        costs = [radii[k]*abs_upper(grads[k].real) for k in range(2)]
        lower = value-sum(costs)
        return lower > -ball(Q(7,100)), costs, lower
    if domain[0] == 'exterior':
        sl, sr, tl = REGIONS[extra[0]]
        ds = ball(sr-sl)
        s = ball(sl)+ds*p[2]; t = ball(tl)+(arb(99)/100-s-ball(tl))*p[3]
        fs, ft, us, vt = derivatives(s,t,X,Y)
        last = [ds*(-fs+p[3]*ft).real, -(arb(99)/100-s-ball(tl))*ft.real]
        ss = ball(sl)+ds*c[2]; tt = ball(tl)+(arb(99)/100-ss-ball(tl))*c[3]
        threshold = ball(Q(1,200))
    else:
        j, k = extra
        s, ds = index_side(j,p[2]); t, dt = index_side(k,p[3])
        fs, ft, us, vt = derivatives(s,t,X,Y)
        last = [(-fs*ds).real, (-ft*dt).real]
        ss, _ = index_side(j,c[2]); tt, _ = index_side(k,c[3])
        threshold = ball(Q(1,1000) if min(j,k)<2 else Q(-1,20))
    gx = (2*arb.pi()*I*(sc-s)+(1-X*u).log()-(1-X*us).log())*dx
    gy = (2*arb.pi()*I*(tc-t)+(1-Y*v).log()-(1-Y*vt).log())*dy
    grads = [gx.real,gy.real]+last
    Xc,Yc,_,_,scc,tcc = critical(wire(f,c[0])[0],wire(g,c[1])[0])
    value = (phase(scc,tcc,Xc,Yc)-phase(ss,tt,Xc,Yc)).real
    costs = [radii[k]*abs_upper(grads[k]) for k in range(4)]
    lower = value-sum(costs)
    return lower>threshold, costs, lower


def scalar_checks():
    r, pi = arb(27)/50, arb.pi()
    comparisons = {
        'wire_radius': arb(1)/2*(2*pi*arb(119)/10000).exp() < r,
        'log_radius': r.log() < -arb(3)/5,
        'dilog_majorant': r+r*r/4+r**3/(9*(1-r)) < arb(2)/3,
        'top_log': arb(25).log() < arb(10)/3,
        'top_gap': -arb(7)/100-(-arb(3)/5*arb(99)/100+arb(4)/9+arb(13)/300) > arb(3)/100,
        'high_index_first': 2*r < (1+r*r).sqrt(),
        'high_index_last': 2*r*pi/10 < 1-r,
        'high_index_rotation': 2*pi*(arb(1)/6+arb(13)/1000-arb(9)/20) < -pi/2,
        'high_index_rotation_other': 2*pi*(arb(1)/6-arb(9)/10) > -3*pi/2,
        'alias_margin': 2*pi/50-arb(1)/20 > arb(7)/100,
    }
    assert all(comparisons.values()), comparisons
    return list(comparisons)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--precision',type=int,default=160)
    parser.add_argument('--output',default='repro/results/research-three-vertex-directed-packet.json')
    args=parser.parse_args();ctx.prec=args.precision
    scalars=scalar_checks();start=time.monotonic();results=[];visited=0
    for domain, dim in domains():
        stack=[('',tuple((Q(0),Q(1)) for _ in range(dim)))];leaves=[]
        while stack:
            path,box=stack.pop();visited+=1
            try: passed,costs,_=evaluate(domain,box)
            except (AssertionError,ValueError,ZeroDivisionError): passed,costs=False,None
            if passed: leaves.append(path);continue
            if costs is not None and all(c.is_finite() for c in costs):
                axis=max(range(dim),key=lambda k:float(costs[k].upper()))
            else:
                weights=([.013,.0025,.013,.0025] if domain[0]=='geometry' else [.08,.08,.5,.8])
                if domain[0]=='exterior' and domain[-1]==2:weights[2]=0
                axis=max(range(dim),key=lambda k:float(box[k][1]-box[k][0])*weights[k])
            lo,hi=box[axis]
            assert hi-lo>Q(1,2**24), ('unproved',domain,box)
            mid=(lo+hi)/2
            for side,(a,b) in enumerate(((lo,mid),(mid,hi))):
                child=list(box);child[axis]=(a,b)
                stack.append((path+str(2*axis+side),tuple(child)))
            assert visited<1000000,'Coverage unfinished; no certificate saved.'
        results.append({'domain':list(domain),'dimension':dim,'leaves':leaves})
    paths=['notes/research_three_vertex_directed_packet.md',
           'notes/research_three_vertex_central_index_chart.md',
           'notes/research_traced_three_vertex_endpoint.md',
           'notes/research_root_pochhammer_interpolation.md',
           'notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,'domains':results,
            'domain_count':len(results),'leaf_count':sum(len(d['leaves'])for d in results),
            'visited':visited,'scalar_checks':scalars,'elapsed_seconds':time.monotonic()-start,
            'scope':'Uniform original corner-deleted vertex packet on the stated directed tube; no complete-chain cycle assertion.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in paths if (ROOT/p).exists()}}
    output=ROOT/args.output;output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
    print(output)


if __name__=='__main__':main()
