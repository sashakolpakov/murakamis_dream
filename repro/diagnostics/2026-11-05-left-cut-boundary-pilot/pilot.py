#!/usr/bin/env python3
"""Bounded, incomplete circle-times-disk pilot for one own-four family.

All accepted leaves use outward original-log root and source inequalities.
The explicit visit/time budgets may leave an untested part of the face.
No partial tree is a complete certificate.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.optimize import brentq
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"experiments"))
import certify_mixed_reduced_disk_conditional_packets as old

ar=old.ar
TYPES=(0,1)
CUT=Q(1,8)
KAPPA=Q(1,2500000)
TARGET_CURVATURE=Q(1)-2*KAPPA

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def iv(pair):
    return ar(pair[0]).union(ar(pair[1]))

def parameters(box):
    """Parameters are (angle of circle3, disk4 radius, angle of disk4)."""
    theta,rho,phi=map(iv,box)
    ca=acb(ar("7/20"),ar("-1/100"))
    cc=acb(ar("3/10"),ar("-13/250"))
    wa=ar("83/1000")*(2*PI*II*theta).exp()
    wc=ar("3/50")*(2*PI*II*phi).exp()
    values=[ca+wa,cc+rho*wc]
    derivative=[
        [2*PI*II*wa,acb(0),acb(0)],
        [acb(0),wc,2*PI*II*rho*wc],
    ]
    return values,derivative

def propose(pp,p0):
    fp=[complex(float(z.real.mid()),float(z.imag.mid())) for z in p0]
    roots,D,res=old.base.block([fp[0].real,fp[0].imag,
                                fp[1].real,fp[1].imag],1)
    if res>1e-9:return None
    centers=[old.encode(z) for z in roots]
    _,J0=old.base.evalf(list(map(old.cp,centers)),*p0,3)
    JJ=np.array([[complex(float(z.real.mid()),float(z.imag.mid())) for z in row]
                 for row in J0])
    Y=np.linalg.inv(JJ)
    witness=dict(centers=centers,
                 inverse=[[old.encode(z) for z in row] for row in Y],
                 affine=[[old.encode(z) for z in row] for row in D])
    *_,bb=old.components(witness,pp,p0,1)
    if any(not z.is_finite() for z in bb):return None
    for factor in (Q(5,4),Q(3,2),Q(2)):
        witness["radii"]=[str(Q(max(1,int(np.ceil(float(z.upper())*
                                               float(factor)*2**40))),2**40))
                          for z in bb]
        certificate=old.root_box(witness,pp,p0,1)
        if certificate is not None:return witness,certificate
    return None

def g2(z):
    q=(-2*PI*II*z).exp()
    return 2*PI*II*q/(1-q)

def phase(s,a,b,eta):
    return old.phase(s,a,b,1)-(1+ar(eta)/2)*old.g(a)-ar("3/2")*old.g(b)

def marginals(s,a,b,eta):
    return [old.gp(s+a)-(1+ar(eta)/2)*old.gp(a)+2*PI*II*s,
            old.gp(s+b)-ar("3/2")*old.gp(b)]

def hessian(s,a,b,eta):
    ss=g2(s+a)+g2(s+b)-3*g2(s)
    assert abs(ss)>0
    off=[g2(s+a)+2*PI*II,g2(s+b)]
    diagonal=[g2(s+a)-(1+ar(eta)/2)*g2(a),
              g2(s+b)-ar("3/2")*g2(b)]
    return [[(diagonal[i] if i==j else acb(0))-off[i]*off[j]/ss
             for j in range(2)] for i in range(2)]

def trial_targets(s,a,b,eta):
    """Floating trial only; outward quadratic bounds handle every target."""
    sf,af,bf=[complex(float(z.real.mid()),float(z.imag.mid())) for z in (s,a,b)]
    gp=lambda z:np.log(1-np.exp(-2j*np.pi*z))
    p=[(gp(sf+af)-(1+eta/2)*gp(af)+2j*np.pi*sf).real,
       (gp(sf+bf)-1.5*gp(bf)).real]
    trial=[]
    for z,lam,marginal in ((af,1+eta/2,p[0]),(bf,1.5,p[1])):
        def f(x):
            zz=x+1j*z.imag
            return (gp(float(CUT)+zz)-lam*gp(zz)).real-marginal
        if f(.22)<=0:x=.22
        elif f(.45)>=0:x=.45
        else:x=brentq(f,.22,.45,xtol=1e-13)
        trial.append(Q(round(x*10**12),10**12))
    return trial

def one_sided_quadratic(slope,length):
    """sup_{0<=d<=length} slope*d-curvature*d^2/2, outward."""
    if length==0 or slope<=0:return arb(0)
    beta=max(slope.upper(),arb(0))
    if beta>=ar(TARGET_CURVATURE*length):
        return beta*ar(length)-ar(TARGET_CURVATURE*length*length)/2
    return beta*beta/(2*ar(TARGET_CURVATURE))

def quadratic_gain(beta,trial):
    # The sign-separated intervals also cover an uncertain sign at zero.
    plus=one_sided_quadratic(beta.upper(),Q(9,20)-trial)
    minus=one_sided_quadratic((-beta).upper(),trial-Q(11,50))
    return max(arb(0),plus.upper(),minus.upper())

def check_source(box,pp,p0,dp,certificate):
    roots=certificate["root"]
    points=certificate["point"]
    response=certificate["response"]
    halfwidth=[ar((hi-lo)/2) for lo,hi in box]
    rows=[]
    for side in (0,1):
        eta=TYPES[side]
        a,s,b=pp[side],roots[side],roots[1-side]
        a0,s0,b0=p0[side],points[side],points[1-side]
        trial=trial_targets(s0,a0,b0,eta)
        aa=acb(ar(trial[0]),a.imag);bb=acb(ar(trial[1]),b.imag)
        aa0=acb(ar(trial[0]),a0.imag);bb0=acb(ar(trial[1]),b0.imag)
        cut=acb(ar(CUT))
        P=marginals(s,a,b,eta)
        P0=marginals(s0,a0,b0,eta)
        Pc=marginals(cut,aa,bb,eta)
        H=hessian(s,a,b,eta)
        delta=[aa.real-a.real,bb.real-b.real]
        delta0=[aa0.real-a0.real,bb0.real-b0.real]
        midpoint=(phase(cut,aa0,bb0,eta)-phase(s0,a0,b0,eta)).real
        midpoint-=sum((P0[i].real*delta0[i] for i in range(2)),arb(0))
        midpoint+=ar(KAPPA)*sum((v*v for v in delta0),arb(0))
        HD=[sum((H[i][j]*delta[j] for j in range(2)),acb(0)) for i in range(2)]
        DU=[-HD[i].real-2*ar(KAPPA)*delta[i] for i in range(2)]
        DH=[(P[i]-Pc[i]+HD[i]).imag for i in range(2)]
        Zder=[dp[side],
              [sum((response[1-side][j]*dp[j][axis] for j in range(2)),acb(0))
               for axis in range(3)]]
        parameter_derivative=[
            sum((DU[i]*Zder[i][axis].real+DH[i]*Zder[i][axis].imag
                 for i in range(2)),arb(0)) for axis in range(3)]
        meanvalue=sum((abs(parameter_derivative[i])*halfwidth[i]
                       for i in range(3)),arb(0))
        slopes=[Pc[i].real-P[i].real+2*ar(KAPPA)*delta[i] for i in range(2)]
        gains=[quadratic_gain(slopes[i],trial[i]) for i in range(2)]
        bound=midpoint+meanvalue+sum(gains,arb(0))
        rows.append(dict(side=side,trial=[str(v) for v in trial],
                         midpoint=str(midpoint),meanvalue=str(meanvalue),
                         gains=[str(v) for v in gains],upper_bound=str(bound.upper())))
        if not bound<0:return None,rows
    return rows,rows

def main():
    global PI,II
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-nodes",type=int,default=511)
    ap.add_argument("--max-seconds",type=float,default=60)
    ap.add_argument("--precision",type=int,default=192)
    ap.add_argument("--output",type=Path,default=Path(__file__).with_name("result.json"))
    args=ap.parse_args()
    ctx.prec=args.precision
    PI=arb.pi();II=acb(0,1)
    old.PI=PI;old.II=II;old.base.PI=PI;old.base.I=II
    # Exact elementary lower bound in the stated scalar-curvature argument.
    assert Q(36,109)*Q(157,50)>1
    start=time.monotonic();visits=leaves=0
    todo=[([(Q(0),Q(1))]*3,0)]
    tree=[];counts={"root":0,"source":0}
    latest_failure=None;depths=[]
    while todo and visits<args.max_nodes and time.monotonic()-start<args.max_seconds:
        box,depth=todo.pop();visits+=1
        pp,dp=parameters(box)
        midbox=[((lo+hi)/2,)*2 for lo,hi in box]
        p0,_=parameters(midbox)
        proposed=propose(pp,p0)
        rows=None
        if proposed is None:reason="root"
        else:
            w,certificate=proposed
            try:rows,detail=check_source(box,pp,p0,dp,certificate)
            except (AssertionError,ValueError,ZeroDivisionError):
                rows=None;detail=[]
            reason="source"
            if rows is None:latest_failure=dict(box=[[str(v) for v in p] for p in box],
                                               depth=depth,details=detail)
        if rows is not None:
            leaves+=1;depths.append(depth)
            tree.append(["L",dict(witness=w,source=rows)])
        else:
            counts[reason]+=1
            axis=depth%3
            lo,hi=box[axis];mid=(lo+hi)/2
            left,right=list(box),list(box)
            left[axis]=(lo,mid);right[axis]=(mid,hi)
            todo.extend([(left,depth+1),(right,depth+1)])
            tree.append(["S",axis])
        if visits%128==0:print("pilot",visits,leaves,len(todo),counts,flush=True)
    result=dict(status="complete_face_only" if not todo else "incomplete_pilot",
                scope="One own4/ext3,4 boundary face, circle3 times disk4, "
                      "both conditional orientations. No other face/family tested.",
                precision_bits=args.precision,visited_nodes=visits,
                accepted_leaves=leaves,unfinished_boxes=len(todo),failure_counts=counts,
                min_accepted_depth=min(depths) if depths else None,
                max_accepted_depth=max(depths) if depths else None,
                elapsed_seconds=time.monotonic()-start,
                last_source_failure=latest_failure,tree=tree,
                pending=[[ [[str(v) for v in p] for p in box],depth] for box,depth in todo],
                driver_sha256=sha(__file__),
                source_helper_sha256=sha(ROOT/"experiments/certify_mixed_reduced_disk_conditional_packets.py"))
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print({k:v for k,v in result.items() if k not in ("tree","pending","last_source_failure")})
    print("latest source failure",latest_failure)

if __name__=="__main__":main()
