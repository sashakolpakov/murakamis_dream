#!/usr/bin/env python3
"""Outward whole-contour upper bounds for the actual complete cap.

The 24 two-dimensional domains include reflected factorials, both folded
verticals, and both real-angle signs. Closed rational binary leaves are
saved for independent replay. No optimizer or sampled acceptance is used.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)
REGIONS=[(Q(-1,8),Q(0)),(Q(0),Q(7,50)),
         (Q(1,5),Q(1,2)),(Q(1,2),Q(7,8))]


def rat(x):
    return arb(x.numerator)/x.denominator if isinstance(x,Q)else arb(x)


def interval(a,b):return rat(a).union(rat(b))


def jreal(z):
    """Re J_side, with original upper/lower continuation through negative Re."""
    z=acb(z);y=abs(z.imag);z=acb(z.real,y);pi=arb.pi()
    if z.real.contains(0) and y.contains(0) and abs(z)<arb(1)/20:
        # Uniform analytic primitive bound, proved in the source note.
        return arb(0,arb(3)/10)
    return (-I*pi*(z*z-z)/2+I*(2*pi*I*z).exp().polylog(2)/(2*pi)-I*pi/12).real


def bupper(x,t):
    return (-jreal(arb(1)/2-x+t/(2*arb.pi()))
            -jreal(arb(1)/2-x-t/(2*arb.pi()))-2*jreal(x))


def psi(t):
    return -4*jreal(arb(1)/4+t/(4*arb.pi()))-4*jreal(arb(1)/4-t/(4*arb.pi()))


def evaluate(domain,box):
    p=[interval(a,b)for a,b in box];lo,hi=REGIONS[domain[1]]
    pi=arb.pi();L=arb(2).log();Y=L/(2*pi);T=arb(41)/20;H=arb(99)/100
    x=acb(rat(lo)+rat(hi-lo)*p[0],Y)
    if domain[0]=='tail':return bupper(x,acb(T))+psi(acb(T))
    kind=domain[2]
    if kind<2:t=acb(-T+T*p[1] if kind==0 else T*p[1],-H)
    else:
        h=L*p[1] if kind%2==0 else L+(H-L)*p[1]
        t=acb(T if kind<4 else -T,-h)
    return bupper(x,t)+psi(t)+3*t.real*(-t.imag)/(2*pi)+t.imag


def domains():
    for r in range(4):
        for kind in range(6):yield ('contour',r,kind),2
    for r in (1,2):yield ('tail',r),1


def scalar_checks():
    pi=arb.pi();L=arb(2).log();Y=L/(2*pi);T=arb(41)/20
    radius=arb(1)/20;w=pi*radius
    # |sin(w)/w-1| <= sinh(|w|)/|w|-1 <1/200.
    primitive_bound=radius*(-(2*pi*radius).log()+pi+1+arb(1)/199)
    checks={
        'local sine remainder':w.sinh()/w-1<arb(1)/200,
        'local primitive bound':primitive_bound<arb(3)/10,
        'local logarithmic monotonicity':2*pi*radius<(-arb(1)).exp(),
        'factorial real-strip margin':arb(1)/2+arb(1)/8+T/(2*pi)<arb(24)/25,
        'complete low-kernel half-plane':-2*T.cos()*(arb(99)/100).cosh()<arb(3)/2,
        'negative and high wire physical tail':psi(acb(T))+pi*Y<arb(23)/20,
        'radical physical exponent':bupper(acb(arb(1)/4,Y),acb(0))<arb(2)/3,
        'high wire radical exponent':pi*Y<arb(2)/3,
        'crossing entropy upper':2*jreal(acb(arb(5)/6))<arb(161533)/500000,
        'attachment margin':arb(19113)/10000-(2*arb(161533)/500000+arb(253)/200)>arb(1)/10000,
    }
    assert all(checks.values()),checks
    return list(checks)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-cap-wire-complement.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    scalar=scalar_checks();saved=[];visits=0
    for domain,dim in domains():
        stack=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
        while stack:
            path,box=stack.pop();visits+=1
            value=evaluate(domain,box)
            if value<arb(253)/200:leaves.append(path);continue
            widths=[float(b-a)for a,b in box]
            lo,hi=REGIONS[domain[1]]
            scales=[float(hi-lo)] if dim==1 else [float(hi-lo),.5 if domain[2]<2 else .2]
            axis=max(range(dim),key=lambda k:widths[k]*scales[k])
            a,b=box[axis];assert b-a>Q(1,2**24),('unproved',domain,box,value)
            mid=(a+b)/2
            for side,(left,right)in enumerate(((a,mid),(mid,b))):
                child=list(box);child[axis]=(left,right)
                stack.append((path+str(2*axis+side),tuple(child)))
            assert visits<500000,'Coverage unfinished; no certificate saved.'
        saved.append({'domain':list(domain),'dimension':dim,'leaves':leaves})
    deps=['notes/research_three_cap_wire_complement.md',
          'notes/research_uniform_factorial_and_boundary_decay.md',
          'notes/research_newton_interpolation_finite_fourier_band.md',
          'notes/research_homogeneous_wire_complete_cap.md',
          'notes/research_three_vertex_global_wire_bound.md',
          'notes/research_three_cap_first_attachment.md']
    record={'status':'passed','precision_bits':args.precision,'domain_count':len(saved),
            'leaf_count':sum(len(z['leaves'])for z in saved),'visited':visits,
            'domains':saved,'scalar_checks':scalar,'elapsed_seconds':time.monotonic()-start,
            'scope':'Original complete-cap upper bound on the exterior wire intervals; full complementary wire integral with retained vertex. Central wire assembly remains separate.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps if(ROOT/p).exists()}}
    path=ROOT/args.output;path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}));print(path)


if __name__=='__main__':main()
