#!/usr/bin/env python3
"""Certify adjacent activation using the actual cosine unit-disk/ellipse domain.

Floating optimization proposes rational slopes and offsets only. Every accepted
parameter box and boundary arc is bounded by outward Arb arithmetic, using a
mean-value enclosure in the two geometric parameters. No incomplete result is
saved. The normalized real angle is z=a/H.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize_scalar
from flint import arb, acb, ctx


def rat(x):
    if isinstance(x,F): return arb(x.numerator)/x.denominator
    return arb(x)


def span(a,b): return rat(a).union(rat(b))


def maxabs(x): return max(abs(x.lower()),abs(x.upper()))


def positive(x):
    lo=max(x.lower(),arb(0));hi=x.upper()
    assert lo<=hi
    return lo.union(hi)


def chi(height, mode, slope=False):
    if mode=='scaled': return rat(F(50,59)) if slope else height*50/59
    if height.upper()<=rat(F(111,100)):
        return rat(F(40,37)) if slope else (height-rat(F(37,200)))*40/37
    if height.lower()>=rat(F(111,100)):
        return arb(0) if slope else arb(1)
    # Closed intervals meeting the exact rational kink can straddle it solely
    # because its enclosing Arb endpoints round. Use the side chosen by caller.
    raise ValueError('Charge kink must be split exactly')


def charge(height, mode, low, high):
    if mode=='scaled': return height*50/59,rat(F(50,59))
    if high<=F(111,100):return (height-rat(F(37,200)))*40/37,rat(F(40,37))
    assert low>=F(111,100)
    return arb(1),arb(0)


def target(z,H,s,mode,hl,hh):
    ch,chp=charge(H,mode,hl,hh)
    T=3*H/2-s*(3*z*H/2-arb.pi()*ch)
    return T,-3*s*H/2,arb(3)/2-s*(3*z/2-arb.pi()*chp)


def excluded(box,mode):
    zl,zh,hl,hh=box; z,H=span(zl,zh),span(hl,hh);a=z*H
    ch,_=charge(H,mode,hl,hh)
    checks={
        'unit cosine':H.cosh()+a.cos()-2,
        'sector':H.sinh()-arb(3).sqrt()*positive(a.sin()),
        'charge angle':a-rat(F(11,108))*a.sin()-2*arb.pi()*ch/3,
    }
    for label,v in checks.items():
        if v>0:return label
    sin=positive(a.sin()); sh=H.sinh(); b=1/arb(2).sqrt()
    numerator=sh-b*sin
    if numerator>=0:
        d=numerator/(sin+b*sh)
        v=3*a/2+(d*(3*H/2).tanh()).atan()-arb.pi()*ch
        if v>0:return 'negative return'
    return None


def cosine_boundary(cap,p,kind):
    C,S=(cap/2).cosh(),(cap/2).sinh();b=1/arb(2).sqrt()
    if kind=='circle':
        beta=p*(S*S).asin()
        bp=p*S*C/(1-S**4).sqrt()
        c=acb(beta.cos(),beta.sin())
        return c,acb(0,bp)*c
    low=S.asin(); high=(b*C/S).atan()
    lp=C/(2*(1-S*S).sqrt())
    hp=-b/(2*(S*S+b*b*C*C))
    theta=low+p*(high-low);tp=lp+p*(hp-lp)
    co,si=theta.cos(),theta.sin()
    c=acb(C*co,S*si)
    cp=acb(S*co/2-C*si*tp,C*si/2+S*co*tp)
    return c,cp


def return_data(z,H,p,kind,partner):
    a=z*H; den=a.cos()+H.cosh()
    if not den>0:return None
    A=acb(a.sin(),-H.sinh())/den
    c,cp=cosine_boundary(H if partner else rat(F(23,20)),p,kind)
    w=A*c
    if not w.real>0:return None
    r=w.asinh();root=(1+w*w).sqrt()
    az=H*(1+A*A)/2
    ah=acb(z,-1)*(1+A*A)/2
    rz=az*c/root
    rh=(ah*c+(A*cp if partner else 0))/root
    return r,rz,rh


def L(w,s):return w.real-s*w.imag


def bound_arc(box,slope,offset,mode,partner,kind,pl,ph):
    zl,zh,hl,hh=box;z,H,p=span(zl,zh),span(hl,hh),span(pl,ph)
    zm,hm=rat((zl+zh)/2),rat((hl+hh)/2)
    s=rat(slope);off=rat(offset if not partner else -offset)
    center=return_data(zm,hm,p,kind,partner)
    full=return_data(z,H,p,kind,partner)
    if center is None or full is None:return None
    tm,_,_=target(zm,hm,s,mode,hl,hh)
    _,tz,th=target(z,H,s,mode,hl,hh)
    fcenter=L(center[0],s)-tm/2-off
    fz=L(full[1],s)-tz/2;fh=L(full[2],s)-th/2
    return (fcenter+maxabs(fz)*rat((zh-zl)/2)
            +maxabs(fh)*rat((hh-hl)/2))


def sampled(z,H,cap):
    p=np.linspace(0,1,161);C,S=np.cosh(cap/2),np.sinh(cap/2)
    beta=p*np.arcsin(S*S)
    theta=np.arcsin(S)+p*(np.arctan(C/(np.sqrt(2)*S))-np.arcsin(S))
    c=np.r_[0,np.exp(1j*beta),C*np.cos(theta)+1j*S*np.sin(theta)]
    return np.arcsinh(np.tan((z-1j)*H/2)*c)


def certify(box,mode,max_segments):
    reason=excluded(box,mode)
    if reason:return {'box':list(map(str,box)),'reason':reason}
    zl,zh,hl,hh=box;z,H=float((zl+zh)/2),float((hl+hh)/2)
    r=[sampled(z,H,c) for c in (1.15,H)]
    ch=50*H/59 if mode=='scaled' else min(1,(H-.185)*40/37)
    def objective(s):
        return sum(float(np.max(v.real-s*v.imag)) for v in r)-1.5*H+s*(1.5*z*H-math.pi*ch)
    fit=minimize_scalar(objective,bounds=(-16,0),method='bounded')
    ss=min([fit.x,-16.,0.],key=objective)
    slope=F(round(ss*8192),8192)
    maxima=[float(np.max(v.real-float(slope)*v.imag)) for v in r]
    offset=F(round((maxima[0]-maxima[1])*2**22/2),2**22)
    if objective(float(slope))>=0:return None
    zball,Hball=span(zl,zh),span(hl,hh)
    T,_,_=target(zball,Hball,rat(slope),mode,hl,hh)
    if not (T/2+rat(offset)>0 and T/2-rat(offset)>0):return None
    counts=[];worst=None
    for partner in (False,True):
        pc={}
        for kind in ('circle','ellipse'):
            stack=[(F(0),F(1))];visits=accepted=0
            while stack:
                pl,ph=stack.pop();visits+=1
                value=bound_arc(box,slope,offset,mode,partner,kind,pl,ph)
                if value is not None and value<0:
                    accepted+=1
                    worst=value.upper() if worst is None else max(worst,value.upper())
                    continue
                if visits>=max_segments:return None
                mid=(pl+ph)/2
                point=bound_arc(box,slope,offset,mode,partner,kind,mid,mid)
                if point is None or not point<0:return None
                stack.extend(((pl,mid),(mid,ph)))
            pc[kind]=accepted
        counts.append(pc)
    return {'box':list(map(str,box)),'reason':'support','slope':str(slope),
            'offset':str(offset),'boundary_segments':counts,'maximum_bound':str(worst)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['scaled','affine'],required=True)
    ap.add_argument('--precision',type=int,default=128)
    ap.add_argument('--maximum-boxes',type=int,default=400000)
    ap.add_argument('--maximum-segments',type=int,default=512)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();ctx.prec=args.precision;assert ctx.prec>=100
    zrange=(F(1),F(2) if args.mode=='scaled' else F(17,8))
    hs=([F(3,100),F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(23,20)]
        if args.mode=='scaled' else [F(37,40),F(1),F(111,100),F(23,20)])
    zs=[zrange[0]+(zrange[1]-zrange[0])*i/8 for i in range(9)]
    stack=[(zl,zh,hl,hh) for zl,zh in zip(zs,zs[1:]) for hl,hh in zip(hs,hs[1:])]
    accepted=[];visits=0;start=last=time.monotonic()
    while stack:
        box=stack.pop();visits+=1
        assert visits<=args.maximum_boxes,'Incomplete cover; no result saved'
        row=certify(box,args.mode,args.maximum_segments)
        if row is not None:accepted.append(row)
        else:
            zl,zh,hl,hh=box
            assert min(zh-zl,hh-hl)>F(1,2**40),('Unresolved box; no result saved',list(map(str,box)))
            if float(zh-zl)*float((hl+hh)/2)>=float(hh-hl):
                mid=(zl+zh)/2;stack.extend(((zl,mid,hl,hh),(mid,zh,hl,hh)))
            else:
                mid=(hl+hh)/2;stack.extend(((zl,zh,hl,mid),(zl,zh,mid,hh)))
        now=time.monotonic()
        if now-last>20:
            print(json.dumps({'mode':args.mode,'accepted':len(accepted),'visited':visits,
                              'pending':len(stack),'seconds':round(now-start,1),
                              'current':list(map(str,box))}),flush=True);last=now
    area=sum((F(r['box'][1])-F(r['box'][0]))*(F(r['box'][3])-F(r['box'][2])) for r in accepted)
    assert area==(zrange[1]-zrange[0])*(hs[-1]-hs[0])
    path=Path(__file__).resolve()
    out=args.output or path.parents[1]/f'repro/results/research-pair-activation-geometric-support-{args.mode}.json'
    counts={key:sum(r['reason']==key for r in accepted) for key in sorted({r['reason'] for r in accepted})}
    result={'status':'passed','mode':args.mode,'precision_bits':ctx.prec,'domain':{
        'angle_over_height':list(map(str,zrange)),'height':[str(hs[0]),str(hs[-1])]},
        'script_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'accepted_boxes':len(accepted),
        'visited_boxes':visits,'counts':counts,'elapsed_seconds':time.monotonic()-start,
        'certificate':accepted}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='certificate'},indent=2));print(out)


if __name__=='__main__':main()
