#!/usr/bin/env python3
"""One saved-family witness diagnostic; no uniform source assertion."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import spence
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"experiments"))
import certify_mixed_reduced_disk_conditional_packets as old

SOURCE=ROOT/"repro/results/research-mixed-reduced-disk-conditional-packets.json"
PI=np.pi
CENTERS=[.35-.01j,.30-.052j]
RADII=[.083,.06]

def gp(z):
    return np.log(1-np.exp(-2j*PI*z))

def g(z):
    return (spence(1-np.exp(-2j*PI*z))-PI*PI/6)/(2j*PI)

def phase(s,a,b,eps):
    return g(s+a)+g(s+b)-(2+eps)*g(s)+2j*PI*a*s

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def encode(z):
    return [float(z.real),float(z.imag)]

def main():
    data=json.loads(SOURCE.read_text())
    domain=next(d for d in data["domains"] if d["types"]==[1,0,1])
    eps,ta,tb=domain["types"]
    todo=[[(Q(0),Q(1)),(Q(0),Q(1))]]
    candidates=[]
    for address,node in enumerate(domain["tree"]):
        box=todo.pop()
        if node[0]=="S":
            left,right=old.split(box,node[1])
            # Exact author convention: append left then right, pop RIGHT first.
            todo.extend([left,right])
            continue
        witness=node[1]
        midpoint=[(lo+hi)/2 for lo,hi in box]
        pp=[CENTERS[t]+RADII[t]*np.exp(2j*PI*float(q))
            for q,t in zip(midpoint,(ta,tb))]
        zz=[complex(float(v[0]),float(v[1])) for v in witness["centers"]]
        for side in (0,1):
            a,s,b=pp[side],zz[side],zz[1-side]
            gap=(phase(s,a,b,eps)-phase(.15,a,b,eps)).real
            candidates.append((gap,address,side,box,witness,pp,zz))
    assert not todo and len(candidates)==2*domain["leaves"]
    # Only select among already saved midpoint values; no reference optimization.
    gap,address,side,box,witness,pp,zz=min(candidates,key=lambda v:v[0])
    a,s,b=pp[side],zz[side],zz[1-side]
    eta=(ta,tb)[side]
    M=(phase(s,a,b,eps)-(1+eta/2)*g(a)-(1+eps/2)*g(b)).real
    pa=(gp(s+a)-(1+eta/2)*gp(a)+2j*PI*s).real
    pb=(gp(s+b)-(1+eps/2)*gp(b)).real

    def optimize(z0,lam,p):
        def derivative(x):
            z=x+1j*z0.imag
            return (gp(.15+z)-lam*gp(z)).real-p
        lo,hi=.22,.45
        if derivative(lo)<=0:
            x=lo
        elif derivative(hi)>=0:
            x=hi
        else:
            x=brentq(derivative,lo,hi,xtol=1e-14)
        return x,float(derivative(x))
    xa,da=optimize(a,1+eta/2,pa)
    xb,db=optimize(b,1+eps/2,pb)
    aa,bb=xa+1j*a.imag,xb+1j*b.imag
    row=(phase(.15,aa,bb,eps)-(1+eta/2)*g(aa)
         -(1+eps/2)*g(bb)).real
    excess=row-M-pa*(xa-a.real)-pb*(xb-b.real)

    # Revalidate only this unchanged saved original-log witness, not a new root.
    ctx.prec=256
    old.PI=arb.pi();old.II=acb(0,1)
    old.base.PI=arb.pi();old.base.I=acb(0,1)
    pp_iv=old.parameter(box,(ta,tb))
    p0_iv=old.parameter([((lo+hi)/2,)*2 for lo,hi in box],(ta,tb))
    verified=old.root_box(witness,pp_iv,p0_iv,eps)
    assert verified is not None
    residual,_=old.base.evalf(list(map(old.cp,witness["centers"])),
                            *p0_iv,2+eps)
    result={
        "status":"diagnostic_only",
        "scope":"One weakest saved midpoint in own4/ext3,4; both target scalars "
                "optimized using strict concavity. No reference-angle optimization, "
                "new roots, refinement, full cover, or actual-word claim.",
        "source_sha256":sha(SOURCE),
        "helper_sha256":sha(ROOT/"experiments/certify_mixed_reduced_disk_conditional_packets.py"),
        "driver_sha256":sha(Path(__file__)),
        "family":domain["types"],"saved_leaves_examined":domain["leaves"],
        "tree_address":address,"orientation":side,
        "angle_box":[[str(v) for v in axis] for axis in box],
        "midpoint_original_root_witness_revalidated":True,
        "original_equation_residual_upper":[str(abs(v).upper()) for v in residual],
        "external_inputs":[encode(v) for v in pp],
        "reference":{"a":encode(a),"s":encode(s),"b":encode(b),
                     "M":float(M),"pa":float(pa),"pb":float(pb)},
        "matched_left_gap":float(gap),
        "target":[xa,xb],"target_stationarity":[da,db],
        "left_cut_excess_over_affine_plane":float(excess),
        "left_cut_excess_over_quadratic_plane":
            float(excess+((xa-a.real)**2+(xb-b.real)**2)/2500000),
    }
    output=Path(__file__).with_name("result.json")
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
