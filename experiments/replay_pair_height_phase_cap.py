#!/usr/bin/env python3
"""Independent 160-bit replay of the maximum-phase pair-height certificate.

No author or optimizer is imported. The earlier independent replayer supplies
only arithmetic and exact partition checks; all new geometry is evaluated here.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
from replay_pair_height_sector import (
    rational, hull, clipped, increasing, square,
    verify_cover, verify_arc_partition,
)


def charge(height, mode):
    if mode=="scaled":
        return F(50,59)*height
    return min(F(1), F(40,37)*(height-F(37,200)))


def angles(rectangle, mode):
    xl,xh,hl,hh=map(F,rectangle)
    values=[]
    for h in (hl,hh):
        low=(rational(h).sinh()/arb(3).sqrt()).asin()
        high=2*rational(h) if mode=="scaled" else 2*arb.pi()*rational(charge(h,mode))/3
        assert low>0 and high>low and high<arb.pi()
        for x in (xl,xh):
            values.append(low+rational(x)*(high-low))
    return hull(min(v.lower() for v in values),max(v.upper() for v in values))


def support_upper(angle,height,cap,parameter,slope):
    denominator=height.cosh()+angle.cos()
    assert denominator>0
    a=clipped(angle.sin(),0)/denominator
    b=height.sinh()/denominator
    limit=(1/(arb(2).sqrt()*(cap/2).tanh())).atan()
    theta=parameter*limit
    cx=(cap/2).cosh()*clipped(theta.cos(),0)
    cy=(cap/2).sinh()*clipped(theta.sin(),0)
    x,y=clipped(a*cx+b*cy,0),a*cy-b*cx
    upper=[]
    if x>0:
        z=acb(x,y)
        r=(z+(1+z*z).sqrt()).log()
        value=r.real-slope*r.imag
        if value.is_finite():
            upper.append(value.upper())
    norm2=square(x)+square(y)
    if norm2.upper()<1:
        delta=1-norm2
        root_t=arb(2).sqrt()*x/((square(delta)+4*square(x)).sqrt()+delta).sqrt()
        value=root_t.asinh()-slope*increasing(
            y/(1+square(root_t)).sqrt(),-1,1,"asin")
        if value.is_finite():
            upper.append(value.upper())
    dp=(square(x)+square(y+1)).nonnegative_part().sqrt()
    dm=(square(x)+square(y-1)).nonnegative_part().sqrt()
    value=increasing((dp+dm)/2,1,None,"acosh")-slope*increasing(
        (dp-dm)/2,-1,1,"asin")
    if value.is_finite():
        upper.append(value.upper())
    assert upper,"No finite enclosure"
    return min(upper)


def replay_row(row,mode):
    xl,xh,hl,hh=map(F,row["box"])
    angle=angles(row["box"],mode)
    height=hull(rational(hl),rational(hh))
    sf=F(row["slope"]);assert sf<=0
    slope=rational(sf)
    budgets=[rational(v) for v in row["support_budgets"]]
    assert len(budgets)==len(row["arcs"])==2
    assert all(b>0 for b in budgets)  # Includes the exact origin value.
    hs=[hl,hh]
    if hl<F(111,100)<hh:
        hs.append(F(111,100))
    targets=[
        3*rational(h)/2-slope*(3*a/2-arb.pi()*rational(charge(h,mode)))
        for h in hs for a in (angle.lower(),angle.upper())
    ]
    margin=(min(v.lower() for v in targets)-sum(budgets,arb(0))).lower()
    assert margin>0,"Target budgets fail"
    leaves=refinements=0
    for cap,budget,segments in zip((rational(F(23,20)),height),budgets,row["arcs"]):
        for lo,hi in verify_arc_partition(segments):
            pending=[(lo,hi,0)]
            while pending:
                left,right,depth=pending.pop()
                bound=support_upper(angle,height,cap,hull(rational(left),rational(right)),slope)
                if bound<budget.lower():
                    leaves+=1
                    margin=min(margin,(budget.lower()-bound).lower())
                    continue
                assert depth<24,("Unverified support segment",row["box"],str(left),str(right))
                mid=(left+right)/2
                point=support_upper(angle,height,cap,rational(mid),slope)
                assert point<budget.lower(),("Failed midpoint",row["box"],str(mid))
                pending.extend(((left,mid,depth+1),(mid,right,depth+1)))
                refinements+=1
    return leaves,refinements,margin


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate",type=Path)
    parser.add_argument("--precision",type=int,default=160)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    assert args.precision>=160
    ctx.prec=args.precision
    here=Path(__file__).resolve();root=here.parents[1]
    raw=args.certificate.read_bytes();data=json.loads(raw)
    assert data["status"]=="passed" and not data["pending"]
    assert data["domain_type"]=="phase-cap"
    mode=data["mode"];assert mode in ("affine","scaled")
    low,high=(F(3,100) if mode=="scaled" else F(37,40)),F(23,20)
    assert data["domain"]=={"coordinate":["0","1"],"height":[str(low),str(high)]}
    for filename,digest in data["sha256"].items():
        assert hashlib.sha256((root/filename).read_bytes()).hexdigest()==digest
    rows=data["certificate"];assert len(rows)==data["accepted_boxes"]
    cover=verify_cover(rows,low,high)
    start=last=time.monotonic();leaves=refinements=0;minimum=None
    for index,row in enumerate(rows,1):
        count,extra,margin=replay_row(row,mode)
        leaves+=count;refinements+=extra
        minimum=margin if minimum is None else min(minimum,margin)
        now=time.monotonic()
        if now-last>=30:
            print(json.dumps({"mode":mode,"replayed":index,"total":len(rows),
                              "leaves":leaves,"seconds":round(now-start,1)}),flush=True)
            last=now
    output=args.output or args.certificate.with_name(args.certificate.stem+"-replay.json")
    report={"status":"passed","mode":mode,"precision_bits":ctx.prec,
            "accepted_boxes":len(rows),"cover":cover,"arc_leaves":leaves,
            "additional_subdivisions":refinements,"minimum_strict_margin":str(minimum),
            "elapsed_seconds":time.monotonic()-start,
            "certificate_sha256":hashlib.sha256(raw).hexdigest(),
            "author_dependencies":data["sha256"],
            "replayer_sha256":hashlib.sha256(here.read_bytes()).hexdigest(),
            "coverage_helper_sha256":hashlib.sha256(here.with_name("replay_pair_height_sector.py").read_bytes()).hexdigest()}
    output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":"passed","mode":mode,"output":str(output),
                      "boxes":len(rows),"arc_leaves":leaves}),flush=True)


if __name__=="__main__":
    main()
