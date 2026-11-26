#!/usr/bin/env python3
"""Independent replay of the actual-geometric adjacent activation certificate.

No generator or optimizer is imported. Exact rational rectangles are checked
for multiplicity-one coverage. The support values use the right-half-plane
distance formula for asinh, while derivatives use its analytic square root.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import arb,acb,ctx


def ball(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def span(a,b):return ball(a).union(ball(b))
def absolute_upper(x):return max(abs(x.lower()),abs(x.upper()))
def positive(x):
    lo,hi=max(x.lower(),arb(0)),x.upper()
    assert lo<=hi
    return lo.union(hi)

def monotone(x,low,high,method):
    lo=max(x.lower(),ball(low));hi=x.upper() if high is None else min(x.upper(),ball(high))
    assert lo<=hi
    return getattr(lo,method)().lower().union(getattr(hi,method)().upper())


class Cover:
    def __init__(self,count):
        self.count=count;self.lo=[0]*(4*count);self.hi=[0]*(4*count);self.added=[0]*(4*count)
    def add(self,left,right,value,node=1,start=0,stop=None):
        if stop is None:stop=self.count
        if left>=stop or right<=start:return
        if left<=start and stop<=right:
            self.lo[node]+=value;self.hi[node]+=value;self.added[node]+=value;return
        mid=(start+stop)//2
        self.add(left,right,value,2*node,start,mid);self.add(left,right,value,2*node+1,mid,stop)
        self.lo[node]=self.added[node]+min(self.lo[2*node],self.lo[2*node+1])
        self.hi[node]=self.added[node]+max(self.hi[2*node],self.hi[2*node+1])


def cover(records,zlo,zhi,hlo,hhi):
    points={zlo,zhi};events=defaultdict(list);area=F(0)
    for row in records:
        l,r,b,t=map(F,row['box'])
        assert zlo<=l<r<=zhi and hlo<=b<t<=hhi
        points.update([l,r]);events[b].append((l,r,1));events[t].append((l,r,-1));area+=(r-l)*(t-b)
    points=sorted(points);indices={v:k for k,v in enumerate(points)};tree=Cover(len(points)-1)
    hs=sorted(events);assert hs[0]==hlo and hs[-1]==hhi
    for h in hs:
        for l,r,d in events[h]:tree.add(indices[l],indices[r],d)
        expected=0 if h==hhi else 1
        assert tree.lo[1]==tree.hi[1]==expected,('cover multiplicity',h,tree.lo[1],tree.hi[1])
    assert area==(zhi-zlo)*(hhi-hlo)
    return {'area':str(area),'z_intervals':len(points)-1,'height_slices':len(hs)-1,'multiplicity':1}


def charges(H,mode,b,t):
    if mode=='scaled':return H*50/59,ball(F(50,59))
    if t<=F(111,100):return (H-ball(F(37,200)))*40/37,ball(F(40,37))
    assert b>=F(111,100)
    return arb(1),arb(0)


def excluded(row,mode):
    l,r,b,t=map(F,row['box']);z,H=span(l,r),span(b,t);a=z*H
    c,_=charges(H,mode,b,t);sin=positive(a.sin())
    reason=row['reason']
    if reason=='unit cosine':v=H.cosh()+a.cos()-2
    elif reason=='sector':v=H.sinh()-arb(3).sqrt()*sin
    elif reason=='charge angle':v=a-ball(F(11,108))*sin-2*arb.pi()*c/3
    else:
        assert reason=='negative return';q=1/arb(2).sqrt();num=H.sinh()-q*sin
        assert num>=0
        v=3*a/2+(num/(sin+q*H.sinh())*(3*H/2).tanh()).atan()-arb.pi()*c
    assert v>0,(reason,row)


def geometry(z,H,p,partner,kind):
    cap=H if partner else ball(F(23,20));co,sh=(cap/2).cosh(),(cap/2).sinh()
    phase=1/arb(2).sqrt()
    if kind==0:
        ang=p*(sh*sh).asin();angp=p*sh*co/(1-sh**4).sqrt()
        c=acb(ang.cos(),ang.sin());cp=c*acb(0,angp)
    else:
        start=sh.asin();stop=(phase*co/sh).atan()
        ds=co/(2*(1-sh*sh).sqrt());de=-phase/(2*(sh*sh+phase*phase*co*co))
        ang=start+p*(stop-start);ap=ds+p*(de-ds)
        c=acb(co*ang.cos(),sh*ang.sin())
        cp=acb(sh*ang.cos()/2-co*ang.sin()*ap,co*ang.sin()/2+sh*ang.cos()*ap)
    T=acb(z,-1)*H;A=(T/2).tan();w=A*c
    assert w.real>0
    root=(1+w*w).sqrt()
    dz=H*(1+A*A)*c/(2*root)
    dh=(acb(z,-1)*(1+A*A)*c/2+(A*cp if partner else 0))/root
    # An independent branch-safe value of the return.
    x,y=w.real,w.imag
    plus=(x*x+(y+1)**2).nonnegative_part().sqrt()
    minus=(x*x+(y-1)**2).nonnegative_part().sqrt()
    real=monotone((plus+minus)/2,1,None,'acosh')
    imag=monotone((plus-minus)/2,-1,1,'asin')
    return acb(real,imag),dz,dh


def upper(row,mode,partner,kind,pl,ph):
    l,r,b,t=map(F,row['box']);z,H=span(l,r),span(b,t);p=span(pl,ph)
    zm,hm=ball((l+r)/2),ball((b+t)/2)
    slope=ball(F(row['slope']));off=ball(F(row['offset']))*(-1 if partner else 1)
    current=geometry(z,H,p,partner,kind);center=geometry(zm,hm,p,partner,kind)
    ch,chp=charges(H,mode,b,t);chm,_=charges(hm,mode,b,t)
    target_m=3*hm/2-slope*(3*zm*hm/2-arb.pi()*chm)
    tz=-3*slope*H/2;th=arb(3)/2-slope*(3*z/2-arb.pi()*chp)
    linear=lambda v:v.real-slope*v.imag
    value=linear(center[0])-target_m/2-off
    return (value+absolute_upper(linear(current[1])-tz/2)*ball((r-l)/2)
            +absolute_upper(linear(current[2])-th/2)*ball((t-b)/2))


def verify_support(row,mode):
    l,r,b,t=map(F,row['box']);z,H=span(l,r),span(b,t)
    s=ball(F(row['slope']));off=ball(F(row['offset']));assert s<=0
    ch,_=charges(H,mode,b,t);T=3*H/2-s*(3*z*H/2-arb.pi()*ch)
    if not (T/2+off>0 and T/2-off>0):return 0,None
    count=0;worst=None
    for partner in (False,True):
        for kind in (0,1):
            stack=[(F(0),F(1))]
            while stack:
                lo,hi=stack.pop();count+=1
                try:value=upper(row,mode,partner,kind,lo,hi)
                except (AssertionError,ValueError):value=None
                if value is not None and value<0:
                    worst=value.upper() if worst is None else max(worst,value.upper());continue
                mid=(lo+hi)/2
                try:point=upper(row,mode,partner,kind,mid,mid)
                except (AssertionError,ValueError):point=None
                if point is None or not point<0:return count,None
                assert hi-lo>F(1,2**24),('Unverified support interval',row,partner,kind,lo,hi)
                stack.extend(((lo,mid),(mid,hi)))
    return count,worst


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--precision',type=int,default=160)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();ctx.prec=args.precision;assert ctx.prec>=160
    record=json.loads(args.certificate.read_text());mode=record['mode'];assert record['status']=='passed'
    zlo,zhi=map(F,record['domain']['angle_over_height']);hlo,hhi=map(F,record['domain']['height'])
    assert (zlo,zhi,hlo,hhi)==((F(1),F(2),F(3,100),F(23,20)) if mode=='scaled' else (F(1),F(17,8),F(37,40),F(23,20)))
    covered=cover(record['certificate'],zlo,zhi,hlo,hhi)
    started=last=time.monotonic();count=0;worst=None;refinements=0
    for i,row in enumerate(record['certificate']):
        if row['reason']!='support':excluded(row,mode)
        else:
            stack=[row]
            while stack:
                current=stack.pop();visits,value=verify_support(current,mode);count+=visits
                if value is not None:
                    worst=value if worst is None else max(worst,value)
                    continue
                # Different interval formulas can be wider than those used by
                # the author. Refine the same exact box with the stored slope
                # and offset, without optimizing either or removing a point.
                l,r,b,t=map(F,current['box'])
                assert min(r-l,t-b)>F(1,2**32),('Unverified parameter box',current)
                if (r-l)*(b+t)/2>=t-b:
                    mid=(l+r)/2;children=[(l,mid,b,t),(mid,r,b,t)]
                else:
                    mid=(b+t)/2;children=[(l,r,b,mid),(l,r,mid,t)]
                for box in children:stack.append(dict(current,box=list(map(str,box))))
                refinements+=1
        now=time.monotonic()
        if now-last>20:
            print(json.dumps({'mode':mode,'verified':i+1,'total':len(record['certificate']),'segments':count,'seconds':round(now-started,1)}),flush=True);last=now
    path=Path(__file__).resolve();root=path.parents[1]
    result={'status':'passed','mode':mode,'precision_bits':ctx.prec,'parameter_boxes':len(record['certificate']),
        'cover':covered,'boundary_visits':count,'parameter_refinements':refinements,'maximum_support_bound':str(worst),'elapsed_seconds':time.monotonic()-started,
        'sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (path,args.certificate.resolve())}}
    out=args.output or root/f'repro/results/research-pair-activation-geometric-support-{mode}-replay.json'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));print(out)


if __name__=='__main__':main()
