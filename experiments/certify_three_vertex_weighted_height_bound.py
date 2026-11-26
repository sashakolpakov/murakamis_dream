#!/usr/bin/env python3
"""Uniform real Newton certificate for the joint weighted height bound."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time
import mpmath as mp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]

def a(value):
    value=Q(value)
    return arb(value.numerator)/value.denominator

def interval(lo,hi):
    return a((lo+hi)/2)+arb(0,a((hi-lo)/2))

def data(z,v):
    s,t,x=z; pi=arb.pi(); r=(-2*pi*v).exp()/2
    def f(u): return (a(Q(5,4))-(2*pi*u).cos()).log()/2
    def fp(u): return pi*(2*pi*u).sin()/(a(Q(5,4))-(2*pi*u).cos())
    den=1+r*r-2*r*(pi*t).cos()
    k=-pi/(pi*(s+t)).tan();D=-fp(x-s);C=fp(x)
    d=pi*r*(pi*t).sin()/den
    q=2*pi*(1-r*(pi*t).cos())/den
    fvalue=[(2*(pi*(s+t)).sin()).log()-arb(2).log()-f(x-s),
            (2*(pi*(s+t)).sin()).log()+r.log()-den.log()/2,
            f(x-s)-f(x)+3*(x-arb(1)/6)]
    H=[[k+D,k,-D],[k,k+d,arb(0)],[-D,arb(0),D+C-3]]
    # Eliminate the xi variable, then invert the two-index matrix.
    e=D+C-3
    h11=k+D-D*D/e
    h22inv=1/(k+d-k*k/h11)
    second=4*d+q*q*h22inv
    return fvalue,H,q,second,(k,D,C,d,e,h11)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--mesh',type=int,default=2048)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=55
    assert args.mesh%2==0
    start=time.monotonic();checks=[]
    def positive(name,value):
        assert value>0,(name,str(value))
        checks.append({'name':name,'margin':str(value)})
    pi=arb.pi()
    positive('refined index lower face',a(Q(1,3)-Q(221,14400)-Q(317,1000)))
    positive('refined index upper face',a(Q(35,100)-Q(1,3)-Q(221,14400)))
    positive('input-radius monotonicity',a(2*Q(12,25)/(1+Q(12,25)**2))-(7*pi/25).cos())
    r=a(Q(12,25));s=a(Q(39,100))
    d=pi*r*(pi*s).sin()/(1+r*r-2*r*(pi*s).cos())
    positive('larger-index-square coercivity',d-a(Q(3,2)))
    budget=15*Q(1,200)**2+Q(3,2)*Q(1,100)**2
    positive('index exterior budget',a(Q(3,4)*Q(37,1000)**2-budget))
    positive('small-p budget',a(Q(323,500)-Q(129,200)-Q(3,20000)))
    def fp(u):return pi*(2*pi*a(u)).sin()/(a(Q(5,4))-(2*pi*a(u)).cos())
    positive('right-interval derivative low endpoint',fp(Q(7,100))-3)
    positive('right-interval derivative high endpoint',fp(Q(21,100))-3)
    positive('left-first derivative low endpoint',fp(Q(12,100))-3)
    positive('left-first derivative high endpoint',fp(Q(39,200))-3)
    positive('left-second derivative low endpoint',fp(Q(14,100))-2)
    positive('left-second derivative high endpoint',fp(Q(27,100))-2)
    positive('right-phase exterior budget',a(3*Q(3,200)**2-budget))
    positive('left-phase exterior budget',a(Q(5,2)*Q(1,50)**2-budget))
    positive('integrated height budget',a(13-Q(251,20)-75*Q(1,200)))

    def mpdata(s,t,x,v):
        p=mp.pi;r=mp.exp(-2*p*v)/2
        f=lambda u:mp.log(mp.mpf(5)/4-mp.cos(2*p*u))/2
        return (mp.log(2*mp.sin(p*(s+t)))-mp.log(2)-f(x-s),
                mp.log(2*mp.sin(p*(s+t)))+mp.log(r)-mp.log(1+r*r-2*r*mp.cos(p*t))/2,
                f(x-s)-f(x)+3*(x-mp.mpf(1)/6))
    def mpq(q):return mp.mpf(q.numerator)/q.denominator
    cells=[];step=Q(1,100*args.mesh)
    for j in range(args.mesh):
        lo=Q(-1,200)+j*step;hi=lo+step;mid=(lo+hi)/2
        vm=mpq(mid)
        center=mp.findroot(lambda s,t,x:mpdata(s,t,x,vm),
                           (mp.mpf(1)/3+mp.mpf('2.18')*vm,
                            mp.mpf(1)/3-mp.mpf('2.82')*vm,
                            mp.mpf(1)/6+mp.mpf('1.86')*vm))
        cs=[str(Q(str(z))) for z in center]
        zs=[a(z) for z in cs]
        # A rational approximation to the inverse Jacobian is a proposal.
        jm=mp.matrix([[mp.diff(lambda w:mpdata(*(list(center[:i])+[w]+list(center[i+1:])),vm)[jrow],center[i])
                       for i in range(3)]for jrow in range(3)])
        cm=jm**-1
        cstrings=[[str(Q(str(cm[i,j])))for j in range(3)]for i in range(3)]
        C=[[a(s)for s in row]for row in cstrings]
        dv=a(step/2);rads=[4*dv,4*dv,3*dv]
        box=[z+arb(0,rad)for z,rad in zip(zs,rads)]
        vb=interval(lo,hi)
        residual=data(zs,a(mid))[0]
        _,H,q,second,parts=data(box,vb)
        J=[[-v for v in row]for row in H]
        qparam=data(zs,vb)[2]
        contractions=[];margins=[]
        for i in range(3):
            contraction=sum(abs(arb(int(i==j))-sum(C[i][k]*J[k][j]for k in range(3)))*rads[j]
                            for j in range(3))/rads[i]
            displacement=abs(sum(C[i][k]*residual[k]for k in range(3)))+abs(C[i][1])*qparam*dv
            margin=rads[i]*(1-contraction)-displacement
            assert contraction<arb(1)/10,(j,i,str(contraction))
            assert margin>0,(j,i,str(margin))
            contractions.append(str(contraction));margins.append(str(margin))
        s,t,x=box
        assert s>a('.28') and s<a('.39') and t>a('.28') and t<a('.39')
        assert x>a(Q(1,6)-Q(1,100)) and x<a(Q(1,6)+Q(1,100)),(j,str(x))
        assert all(z>0 for z in parts)
        # Compare to the minimum of the affine majorant on this interval.
        ceiling=a(Q(251,10)+450*max(lo,Q(0)))
        assert second<ceiling,(j,str(second),str(ceiling))
        cells.append({'index':j,'height_interval':[str(lo),str(hi)],'center':cs,
                      'preconditioner':cstrings,'radii':[str(z)for z in rads],
                      'Newton_contractions':contractions,'self_map_margins':margins,
                      'critical_boxes':[str(z)for z in box],
                      'height_second_derivative':str(second),'ceiling':str(Q(251,10)+450*max(lo,Q(0)))})
        if j%256==0:print(f'height cells {j}/{args.mesh}',flush=True)
    proof=ROOT/'notes/research_three_vertex_weighted_height_bound.md'
    paths=[proof,ROOT/'notes/research_three_vertex_symmetric_height_bound.md',
           ROOT/'notes/research_three_vertex_global_wire_bound.md']
    result={'status':'passed','precision_bits':ctx.prec,'height_cell_count':args.mesh,
            'exact_interval_cover':True,'scalar_comparison_count':len(checks),
            'scalar_comparisons':checks,'height_cells':cells,
            'elapsed_seconds':time.monotonic()-start,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest()for p in paths},
            'scope':'Global weighted original summand bound using the written reduction and a uniform critical-height Newton cover; no quantum lower bound.'}
    out=args.output or ROOT/'repro/results/research-three-vertex-weighted-height-bound.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(checks)} scalar comparisons and {args.mesh} height cells. {out}')

if __name__=='__main__':main()
