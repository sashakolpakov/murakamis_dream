#!/usr/bin/env python3
"""Pair-height support on the proved maximum-phase domain.

This verifies a different, smaller geometric domain than the earlier authors.
It does not import or modify them. Numerical optimization proposes slopes;
only outward Arb inequalities and complete rational coverage certify a result.
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
from flint import acb, arb, ctx


def rat(q):
    q = F(q)
    return arb(q.numerator)/q.denominator


def box(lo, hi):
    return rat(lo).union(rat(hi))


def nonnegative(x):
    return x.nonnegative_part()


def sq(x):
    lo, hi = x.lower(), x.upper()
    if lo >= 0:
        return (lo*lo).lower().union((hi*hi).upper())
    if hi <= 0:
        return (hi*hi).lower().union((lo*lo).upper())
    return arb(0).union(max((lo*lo).upper(), (hi*hi).upper()))


def bounded_function(x, low, high, name):
    lo = max(x.lower(), rat(low))
    hi = x.upper() if high is None else min(x.upper(), rat(high))
    if not lo <= hi:
        return arb("nan")
    return getattr(lo, name)().lower().union(getattr(hi, name)().upper())


def charge(h, mode):
    return 50*h/59 if mode == "scaled" else min(F(1), (h-F(37,200))*40/37)


def angle_at(x, h, mode):
    lower = (rat(h).sinh()/arb(3).sqrt()).asin()
    upper = 2*rat(h) if mode == "scaled" else 2*arb.pi()*rat(charge(h, mode))/3
    return (1-rat(x))*lower+rat(x)*upper


def angle_bounds(rectangle, mode):
    xl, xh, hl, hh = rectangle
    # Both lower and upper endpoints increase with h, and upper>lower.
    return angle_at(xl, hl, mode).lower().union(angle_at(xh, hh, mode).upper())


def support(a, h, cap, u, slope):
    denominator = a.cos()+h.cosh()
    if not denominator > 0:
        return arb("nan")
    ax, ay = nonnegative(a.sin())/denominator, -h.sinh()/denominator
    half = cap/2
    endpoint = (half.cosh()/(arb(2).sqrt()*half.sinh())).atan()
    theta = endpoint*u
    cx = half.cosh()*nonnegative(theta.cos())
    cy = half.sinh()*nonnegative(theta.sin())
    x, y = nonnegative(ax*cx-ay*cy), ax*cy+ay*cx
    candidates = []
    if x > 0:
        value = acb(x,y).asinh()
        value = value.real-rat(slope)*value.imag
        if value.is_finite():
            candidates.append(value)
    norm2 = sq(x)+sq(y)
    if norm2.upper() < 1:
        base = 1-norm2
        t = 2*sq(x)/((sq(base)+4*sq(x)).sqrt()+base)
        k = nonnegative(t).sqrt().asinh()
        g = bounded_function(y/(1+t).sqrt(), -1, 1, "asin")
        value = k-rat(slope)*g
        if value.is_finite():
            candidates.append(value)
    dp = nonnegative(sq(x)+sq(y+1)).sqrt()
    dm = nonnegative(sq(x)+sq(y-1)).sqrt()
    k = bounded_function((dp+dm)/2, 1, None, "acosh")
    g = bounded_function((dp-dm)/2, -1, 1, "asin")
    value = k-rat(slope)*g
    if value.is_finite():
        candidates.append(value)
    return min(candidates, key=lambda z:z.upper()) if candidates else arb("nan")


def target_lower(a, hl, hh, slope, mode):
    hs = [hl, hh]
    if hl < F(111,100) < hh:
        hs.append(F(111,100))
    values = [
        3*rat(h)/2-rat(slope)*(3*x/2-arb.pi()*rat(charge(h,mode)))
        for h in hs for x in (a.lower(), a.upper())
    ]
    return min(v.lower() for v in values)


def numerical_returns(a, h, cap):
    endpoint = math.atan(1/(math.sqrt(2)*math.tanh(cap/2)))
    theta = np.linspace(0, endpoint, 257)
    c = np.cosh(cap/2)*np.cos(theta)+1j*np.sinh(cap/2)*np.sin(theta)
    return np.r_[0, np.arcsinh(np.tan((a-1j*h)/2)*c)]


def certify(rectangle, mode, maximum_segments):
    xl,xh,hl,hh = rectangle
    a, h = angle_bounds(rectangle,mode), box(hl,hh)
    hm, xm = float((hl+hh)/2), float((xl+xh)/2)
    lower = math.asin(math.sinh(hm)/math.sqrt(3))
    chi = 50*hm/59 if mode=="scaled" else min(1,(hm-.185)*40/37)
    upper = 2*hm if mode=="scaled" else 2*math.pi*chi/3
    am = (1-xm)*lower+xm*upper
    returns = [numerical_returns(am,hm,c) for c in (1.15,hm)]
    def objective(s):
        return sum(np.max(r.real-s*r.imag) for r in returns)-1.5*hm+s*(1.5*am-math.pi*chi)
    opt = minimize_scalar(objective,bounds=(-16,0),method="bounded")
    slope = min(F(round(opt.x*4096),4096), F(0))
    lower_target = target_lower(a,hl,hh,slope,mode)
    maxima = [float(np.max(r.real-float(slope)*r.imag)) for r in returns]
    gap = float(lower_target)-sum(maxima)
    if not math.isfinite(gap) or gap <= 0:
        return None
    budgets = [F.from_float(m+.45*gap) for m in maxima]
    if not all(b>0 for b in budgets) or not sum(map(rat,budgets),arb(0)) < lower_target:
        return None
    arcs = []
    for cap,budget in zip((rat(F(23,20)),h),budgets):
        pending,accepted,visits = [(F(0),F(1))],[],0
        while pending:
            left,right = pending.pop()
            visits += 1
            value = support(a,h,cap,box(left,right),slope)
            if value.is_finite() and value.upper() < rat(budget):
                accepted.append([str(left),str(right)])
                continue
            middle = (left+right)/2
            point = support(a,h,cap,rat(middle),slope)
            if (not point.is_finite() or not point.upper() < rat(budget)
                    or visits >= maximum_segments or right-left < F(1,2**20)):
                return None
            pending.extend(((left,middle),(middle,right)))
        arcs.append(accepted)
    return {"box":list(map(str,rectangle)), "slope":str(slope),
            "support_budgets":list(map(str,budgets)), "arcs":arcs}


def run(mode,args):
    here = Path(__file__).resolve()
    root = here.parents[1]
    output = root/("repro/results/research-pair-height-phase-cap-"+mode+".json")
    checkpoint = output.with_suffix(".checkpoint.json")
    inputs = [here,root/"notes/research_geometric_phase_maximum_principle.md"]
    hashes = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    low, high = (F(3,100) if mode=="scaled" else F(37,40)),F(23,20)
    heights = ([low,F(1,10),F(1,4),F(1,2),F(3,4),F(1),high]
               if mode=="scaled" else [low,F(1),F(111,100),high])
    pending = [(F(i,8),F(i+1,8),lo,hi)
               for i in range(8) for lo,hi in zip(heights,heights[1:])]
    rows,visits,old_seconds = [],0,0
    if args.resume:
        old=json.loads(checkpoint.read_text())
        assert old["sha256"]==hashes and old["precision_bits"]==ctx.prec and old["mode"]==mode
        rows,visits,old_seconds=old["certificate"],old["visited_boxes"],old["elapsed_seconds"]
        pending=[tuple(map(F,b)) for b in old["pending"]]
    start=last=time.monotonic()
    def save(complete=False):
        data={"status":"passed" if complete else "incomplete",
              "domain_type":"phase-cap", "mode":mode, "precision_bits":ctx.prec,
              "sha256":hashes, "domain":{"coordinate":["0","1"],"height":[str(low),str(high)]},
              "accepted_boxes":len(rows),"visited_boxes":visits,
              "elapsed_seconds":old_seconds+time.monotonic()-start,
              "pending":[list(map(str,b)) for b in pending],"certificate":rows}
        destination=output if complete else checkpoint
        destination.parent.mkdir(parents=True,exist_ok=True)
        tmp=destination.with_suffix(destination.suffix+".tmp")
        tmp.write_text(json.dumps(data,separators=(",",":"))+"\n")
        tmp.replace(destination)
    while pending and visits<args.maximum_boxes:
        rectangle=pending.pop();visits+=1
        accepted=certify(rectangle,mode,args.maximum_segments)
        if accepted is not None:
            rows.append(accepted)
        else:
            xl,xh,hl,hh=rectangle
            if max(xh-xl,hh-hl)<F(1,2**40):
                pending.append(rectangle);save()
                print(json.dumps({"status":"incomplete","mode":mode,"reason":"tiny uncertified rectangle"}),flush=True)
                return False
            if 2*float(xh-xl)>=float(hh-hl):
                mid=(xl+xh)/2
                pending.extend(((xl,mid,hl,hh),(mid,xh,hl,hh)))
            else:
                mid=(hl+hh)/2
                pending.extend(((xl,xh,hl,mid),(xl,xh,mid,hh)))
        now=time.monotonic()
        if now-last>=30:
            save()
            print(json.dumps({"mode":mode,"accepted":len(rows),"visited":visits,
                              "pending":len(pending),"seconds":round(old_seconds+now-start,1)}),flush=True)
            last=now
    if pending:
        save()
        print(json.dumps({"status":"incomplete","mode":mode,"reason":"box budget","checkpoint":str(checkpoint)}),flush=True)
        return False
    assert sum((F(r["box"][1])-F(r["box"][0]))*(F(r["box"][3])-F(r["box"][2])) for r in rows)==high-low
    save(True)
    print(json.dumps({"status":"passed","mode":mode,"output":str(output),
                      "accepted":len(rows),"visited":visits}),flush=True)
    return True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=("affine","scaled","both"),default="both")
    parser.add_argument("--precision",type=int,default=100)
    parser.add_argument("--maximum-boxes",type=int,default=150000)
    parser.add_argument("--maximum-segments",type=int,default=2048)
    parser.add_argument("--resume",action="store_true")
    args=parser.parse_args();ctx.prec=args.precision
    assert ctx.prec>=100
    for mode in (("affine","scaled") if args.mode=="both" else (args.mode,)):
        if not run(mode,args):
            break


if __name__=="__main__":
    main()
