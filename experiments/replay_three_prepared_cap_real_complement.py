#!/usr/bin/env python3
"""Independent negative-frequency replay of the L40 prepared real-index complement."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_vertex_bidisk_packet import action,partition
ROOT=Path(__file__).resolve().parents[1];I=acb(0,1)


def a(q):return arb(q.numerator)/q.denominator if isinstance(q,R)else arb(q)
def iv(x,y):return a(x).union(a(y))
def absupper(z):return max(abs(z.lower()),abs(z.upper()))


def data(key,p):
    pi=arb.pi();height=arb(2).log()/(2*pi)
    x=acb(arb(7)/50+arb(3)/50*p[0],iv(R(10135867,10**8),R(10135871,10**8)))
    base=acb(arb(1)/6,height);f=key[0]
    if f in (0,1):
        y=base+arb(2*f-1)/200+I*(arb(2)*p[1]-1)/200;yp=I/100
    else:
        y=base+(arb(2)*p[1]-1)/200+I*arb(2*f-5)/200;yp=acb(arb(1)/100)
    if key[2]==0:
        s=p[2]/40;t=arb(1)/40+arb(17)/40*p[3];sp=arb(1)/40;tp=arb(17)/40
    elif key[2]==1:
        s=arb(1)/40+arb(9)/40*p[2];t=arb(9)/20*p[3];sp=arb(9)/40;tp=arb(9)/20
    else:
        s=arb(9)/20;t=arb(9)/20*p[3];sp=arb(0);tp=arb(9)/20
    if key[1]:s,t=t,s
    X=(2*pi*I*x).exp();Y=(2*pi*I*y).exp()
    return x,y,X,Y,s,t,arb(3)/50,yp,sp,tp


def check(key,box):
    p=[iv(lo,hi)for lo,hi in box];center=[a((lo+hi)/2)for lo,hi in box]
    widths=[a((hi-lo)/2)for lo,hi in box];pi=arb.pi()
    x,y,X,Y,s,t,xh,yp,sp,tp=data(key,p)
    U=(-2*pi*I*s).exp();V=(-2*pi*I*t).exp()
    common=(2*(pi*(s+t)).sin()).log()+I*pi*(arb(1)/2-s-t)
    fs=common+X.log()-(1-X*U).log();ft=common+Y.log()-(1-Y*V).log()
    fx=2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I
    fy=2*pi*I*t+(1-Y*V).log()-(1-Y).log()-pi*I
    if key[1]:fs,ft=ft,fs
    derivatives=[xh*fx.real,(yp*fy).real,sp*fs.real,tp*ft.real]
    xc,yc,XX,YY,sc,tc,*_=data(key,center)
    upper=(action(sc,tc,XX,YY)-pi*I*(xc+yc)).real
    upper+=sum(w*absupper(g)for w,g in zip(widths,derivatives))
    assert upper<arb(6455)/10000,(key,box,upper)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',default='repro/results/research-three-prepared-cap-real-complement-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    path=ROOT/'repro/results/research-three-prepared-cap-real-complement.json'
    d=json.loads(path.read_text());assert d['status']=='passed'
    expected=set(product(range(4),range(2),range(3)));seen=set();count=0
    for dom in d['domains']:
        key=tuple(dom['domain']);assert key in expected and key not in seen;seen.add(key)
        assert dom['dimension']==4
        for box in partition(dom['leaves'],4):check(key,box);count+=1
    assert seen==expected and count==d['leaf_count']
    pi=arb.pi();r=arb(27)/50
    margins=[r-(-2*pi*arb(10135867)/10**8).exp(),r-(pi/100).exp()/2,
             (1+r*r).sqrt()-2*r,1-r-r*pi/4,
             arb(3)/4-arb(7)/8+arb(7)/50]
    assert all(m>0 for m in margins)
    for f,h in d['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h,f
    assert sha256((ROOT/'experiments/certify_three_prepared_cap_real_complement.py').read_bytes()).hexdigest()==d['script_sha256']
    out={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
         'leaf_count':count,'exact_binary_cover':True,'scalar_comparisons':len(margins),
         'phase':'Independent negative-frequency primitive and sine-log derivatives, no author imports',
         'elapsed_seconds':time.monotonic()-start,'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'independent_helper_sha256':sha256((ROOT/'experiments/replay_three_vertex_bidisk_packet.py').read_bytes()).hexdigest()}
    (ROOT/args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
