#!/usr/bin/env python3
"""Certify pair-height support bounds on the proved angular sector.

The geometric reductions are proved in research_pair_support_boundary_reduction.md.
This is a separate, resumable implementation; it does not modify the earlier
unrestricted-angle certificate. Floating point optimization only proposes rational
slopes and budgets. Arb inequalities certify every accepted closed box and arc.
An incomplete checkpoint is never labelled as a successful certificate.
"""
import argparse
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from flint import acb, arb, ctx

from certify_positive_path_maximum_height import interval, rat, clipped, monotone_clipped


def angle_bounds(box):
    xl, xh, hl, hh = box
    cuts = [(rat(h).sinh()/arb(3).sqrt()).asin() for h in (hl, hh)]
    corners = [arb.pi()*rat(x)+(1-2*rat(x))*c for x in (xl,xh) for c in cuts]
    return interval(min(c.lower() for c in corners), max(c.upper() for c in corners))


def coordinates(cap, u, kind):
    if kind == "arc":
        t = arb.pi()*u/2
        return (cap/2).cosh()*clipped(t.cos(),0), (cap/2).sinh()*clipped(t.sin(),0)
    cut = monotone_clipped(cap.sinh()/arb(3).sqrt(),0,1,"asin")
    if kind == "left":
        beta = cut*u
        h = monotone_clipped(arb(3).sqrt()*clipped(beta.sin(),0),0,None,"asinh")
    elif kind == "right":
        beta = arb.pi()-cut*u
        h = monotone_clipped(arb(3).sqrt()*clipped(beta.sin(),0),0,None,"asinh")
    elif kind == "top":
        beta = cut+(arb.pi()-2*cut)*u
        h = cap
    else:
        raise ValueError(kind)
    return clipped((beta/2).cos(),0)*(h/2).cosh(), clipped((beta/2).sin(),0)*(h/2).sinh()


def support(a, height, cap, u, kind, slope):
    den = a.cos()+height.cosh()
    if not den > 0:
        return arb("nan")
    re_a, neg_im_a = clipped(a.sin(),0)/den, height.sinh()/den
    cx,cy = coordinates(cap,u,kind)
    zx,zy = re_a*cx+neg_im_a*cy, re_a*cy-neg_im_a*cx
    # A positive real part selects the proved right-half-plane branch.
    # At c=0 (the right sector endpoint) use the exact entire value 0.
    direct = None
    if zx > 0:
        r = acb(zx,zy).asinh()
        direct = r.real-rat(slope)*r.imag
    # The distance formula also covers a segment containing that endpoint.
    # It can be much sharper on a broad arc than complex ball evaluation.
    plus = (zx**2+(zy+1)**2).nonnegative_part().sqrt()
    minus = (zx**2+(zy-1)**2).nonnegative_part().sqrt()
    k = monotone_clipped((plus+minus)/2,1,None,"acosh")
    g = monotone_clipped((plus-minus)/2,-1,1,"asin")
    distance = k-rat(slope)*g
    if direct is not None and direct.is_finite() and direct.upper() < distance.upper():
        return direct
    return distance


def target(a,height,hh,slope,mode):
    s = rat(slope)
    if mode == "scaled":
        return (rat(F(3,2))+arb.pi()*s*50/59)*height-3*s*a/2
    if hh <= F(111,100):
        return (rat(F(3,2))+arb.pi()*s*40/37)*height-3*s*a/2-arb.pi()*s/5
    return 3*height/2-3*s*a/2+arb.pi()*s


def samples(a,h,cap,mode):
    u = np.linspace(0,1,193)
    if mode == "scaled":
        c = np.cosh(cap/2)*np.cos(np.pi*u/2)+1j*np.sinh(cap/2)*np.sin(np.pi*u/2)
    else:
        cut = np.arcsin(np.sinh(cap)/np.sqrt(3))
        beta = np.r_[cut*u,cut+(np.pi-2*cut)*u,np.pi-cut*u]
        heights = np.minimum(cap,np.arcsinh(np.sqrt(3)*np.maximum(np.sin(beta),0)))
        c = np.cos((beta-1j*heights)/2)
    return np.arcsinh(np.tan((a-1j*h)/2)*c)


def certify(box,mode,maximum_segments):
    xl,xh,hl,hh = box
    a,height = angle_bounds(box),interval(hl,hh)
    hm = float((hl+hh)/2)
    cut = math.asin(math.sinh(hm)/math.sqrt(3))
    am = cut+(math.pi-2*cut)*float((xl+xh)/2)
    returns = [samples(am,hm,c,mode) for c in (1.15,hm)]
    charge = hm*50/59 if mode == "scaled" else min(1,(hm-.185)*40/37)
    def objective(s):
        return sum(np.max(r.real-s*r.imag) for r in returns)-1.5*hm+s*(1.5*am-math.pi*charge)
    opt = minimize_scalar(objective,bounds=(-64,0),method="bounded")
    slope = min(F(round(opt.x*4096),4096),F(0))
    lower = target(a,height,hh,slope,mode).lower()
    maxima = [float(np.max(r.real-float(slope)*r.imag)) for r in returns]
    gap = float(lower)-sum(maxima)
    if gap <= 0:
        return None
    budgets = [F.from_float(m+.45*gap) for m in maxima]
    if not sum((rat(b) for b in budgets),arb(0)) < lower:
        return None
    kinds = ("arc",) if mode == "scaled" else ("left","top","right")
    arcs = []
    for cap,budget in zip((rat(F(23,20)),height),budgets):
        record = {}
        for kind in kinds:
            stack,accepted,visits = [(F(0),F(1))],[],0
            while stack:
                lo,hi = stack.pop()
                visits += 1
                bound = support(a,height,cap,interval(lo,hi),kind,slope)
                if bound.is_finite() and bound.upper() < rat(budget):
                    accepted.append([str(lo),str(hi)])
                    continue
                mid = (lo+hi)/2
                point = support(a,height,cap,rat(mid),kind,slope)
                if (not point.is_finite() or not point.upper() < rat(budget)
                        or visits >= maximum_segments or hi-lo < F(1,2**20)):
                    return None
                stack.extend(((lo,mid),(mid,hi)))
            record[kind] = accepted
        arcs.append(record)
    return {"box":list(map(str,box)),"slope":str(slope),
            "support_budgets":list(map(str,budgets)),"arcs":arcs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=("scaled","affine"),required=True)
    parser.add_argument("--precision",type=int,default=100)
    parser.add_argument("--maximum-boxes",type=int,default=300000)
    parser.add_argument("--maximum-segments",type=int,default=2048)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--resume",action="store_true")
    args = parser.parse_args()
    ctx.prec = args.precision
    assert ctx.prec >= 100
    here = Path(__file__).resolve()
    output = args.output or here.parents[1]/("repro/results/research-pair-height-sector-"+args.mode+".json")
    checkpoint = output.with_suffix(".checkpoint.json")
    inputs = [here,here.with_name("certify_positive_path_maximum_height.py"),
              here.parents[1]/"notes/research_pair_support_boundary_reduction.md"]
    hashes = {str(p.relative_to(here.parents[1])):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    lower = F(3,100) if args.mode == "scaled" else F(37,40)
    upper = F(23,20)
    heights = ([lower,F(1,10),F(1,4),F(1,2),F(3,4),F(1),upper]
               if args.mode == "scaled" else [lower,F(1),F(111,100),upper])
    stack = [(F(i,8),F(i+1,8),lo,hi) for i in range(8) for lo,hi in zip(heights,heights[1:])]
    accepted,visits,prior_seconds = [],0,0
    if args.resume:
        old = json.loads(checkpoint.read_text())
        assert old["sha256"] == hashes and old["mode"] == args.mode
        assert old["precision_bits"] == ctx.prec
        accepted,visits,prior_seconds = old["certificate"],old["visited_boxes"],old["elapsed_seconds"]
        stack = [tuple(map(F,b)) for b in old["pending"]]
    start = last = time.monotonic()
    def save(complete=False):
        record = {"status":"passed" if complete else "incomplete","mode":args.mode,
                  "precision_bits":ctx.prec,"sha256":hashes,
                  "domain":{"sector_coordinate":["0","1"],"height":[str(lower),str(upper)]},
                  "visited_boxes":visits,"accepted_boxes":len(accepted),
                  "elapsed_seconds":prior_seconds+time.monotonic()-start,
                  "pending":[list(map(str,b)) for b in stack],"certificate":accepted}
        destination = output if complete else checkpoint
        destination.parent.mkdir(parents=True,exist_ok=True)
        temporary = destination.with_suffix(destination.suffix+".tmp")
        temporary.write_text(json.dumps(record,separators=(",",":"))+"\n")
        temporary.replace(destination)
    while stack and visits < args.maximum_boxes:
        box = stack.pop()
        visits += 1
        result = certify(box,args.mode,args.maximum_segments)
        if result is not None:
            accepted.append(result)
        else:
            xl,xh,hl,hh = box
            if max(xh-xl,hh-hl) < F(1,2**40):
                stack.append(box)
                save()
                print("Coverage incomplete: a tiny parameter box remains uncertified; checkpoint saved.",flush=True)
                return
            if math.pi*float(xh-xl) >= float(hh-hl):
                mid = (xl+xh)/2
                stack.extend(((xl,mid,hl,hh),(mid,xh,hl,hh)))
            else:
                mid = (hl+hh)/2
                stack.extend(((xl,xh,hl,mid),(xl,xh,mid,hh)))
        now = time.monotonic()
        if now-last >= 30:
            save()
            print(json.dumps({"mode":args.mode,"accepted":len(accepted),"visited":visits,
                              "pending":len(stack),"seconds":round(prior_seconds+now-start,1)}),flush=True)
            last = now
    if stack:
        save()
        print("Coverage incomplete; resumable checkpoint saved.",flush=True)
        return
    area = sum((F(r["box"][1])-F(r["box"][0]))*(F(r["box"][3])-F(r["box"][2])) for r in accepted)
    assert area == upper-lower
    save(complete=True)
    print(json.dumps({"status":"passed","output":str(output),"accepted_boxes":len(accepted),
                      "visited_boxes":visits,"seconds":prior_seconds+time.monotonic()-start}),flush=True)


if __name__ == "__main__":
    main()
