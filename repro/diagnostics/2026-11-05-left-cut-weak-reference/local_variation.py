#!/usr/bin/env python3
"""One local external-angle variation; any positive point is checked outward."""
from fractions import Fraction as Q
import json
import hashlib
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq, minimize
from flint import arb, acb, ctx

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import diagnose as d
old=d.old
P=np.pi

def evaluate(theta, details=False):
    pp=[d.CENTERS[t]+d.RADII[t]*np.exp(2j*P*float(q))
        for q,t in zip(theta,(0,1))]
    zz,_,res=old.base.block([pp[0].real,pp[0].imag,
                            pp[1].real,pp[1].imag],1)
    assert res<1e-10
    a,s,b=pp[0],zz[0],zz[1]
    M=(d.phase(s,a,b,1)-d.g(a)-1.5*d.g(b)).real
    pa=(d.gp(s+a)-d.gp(a)+2j*P*s).real
    pb=(d.gp(s+b)-1.5*d.gp(b)).real
    target=[]
    for z0,lam,p in ((a,1,pa),(b,1.5,pb)):
        der=lambda x:(d.gp(.15+x+1j*z0.imag)
                      -lam*d.gp(x+1j*z0.imag)).real-p
        if der(.22)<=0:x=.22
        elif der(.45)>=0:x=.45
        else:x=brentq(der,.22,.45,xtol=1e-14)
        target.append(x)
    aa,bb=target[0]+1j*a.imag,target[1]+1j*b.imag
    row=(d.phase(.15,aa,bb,1)-d.g(aa)-1.5*d.g(bb)).real
    excess=float(row-M-pa*(target[0]-a.real)-pb*(target[1]-b.real))
    return (excess,pp,zz,res,target,M,pa,pb) if details else excess

def main():
    start=[float(Q(11,32)),float(Q(17,32))]
    opt=minimize(lambda t:-evaluate(t),start,method="L-BFGS-B",
                 bounds=[(0,1),(0,1)],
                 options={"maxiter":60,"maxfun":220,"ftol":1e-13,"gtol":1e-8})
    theta=[Q(round(float(v)*10**12),10**12) for v in opt.x]
    excess,pp,zz,res,target,M,pa,pb=evaluate(theta,True)
    target=[Q(round(v*10**12),10**12) for v in target]
    out={"scope":"One local optimization from the saved weakest midpoint, "
                  "own4/ext3,4 only. No word realization or universal theorem.",
         "status":"diagnostic_only","start":start,"success":bool(opt.success),
         "message":str(opt.message),"iterations":int(opt.nit),
         "function_evaluations":int(opt.nfev),
         "angles":[str(v) for v in theta],"target":[str(v) for v in target],
         "floating_original_residual":float(res),"floating_excess":excess,
         "external_inputs":[d.encode(v) for v in pp],
         "roots":[d.encode(v) for v in zz],
         "M":M,"pa":pa,"pb":pb,
         "source_sha256":d.sha(d.SOURCE),
         "helper_sha256":d.sha(d.ROOT/"experiments/certify_mixed_reduced_disk_conditional_packets.py"),
         "driver_sha256":d.sha(Path(__file__))}
    if excess>0:
        ctx.prec=256;old.PI=arb.pi();old.II=acb(0,1)
        old.base.PI=arb.pi();old.base.I=acb(0,1)
        box=[(v,v) for v in theta]
        w=old.propose(box,1,(0,1))
        assert w is not None
        p0=old.parameter(box,(0,1))
        cert=old.root_box(w,p0,p0,1)
        assert cert is not None
        s,b=cert["point"];a=p0[0]
        aa=acb(old.ar(target[0]),a.imag)
        bb=acb(old.ar(target[1]),b.imag)
        lam=old.ar("3/2")
        F=old.phase(s,a,b,1)-old.g(a)-lam*old.g(b)
        pa=(old.gp(s+a)-old.gp(a)+2*old.PI*old.II*s).real
        pb=(old.gp(s+b)-lam*old.gp(b)).real
        row=(old.phase(acb(old.ar("3/20")),aa,bb,1)
             -old.g(aa)-lam*old.g(bb)).real
        interval=row-F.real-pa*(aa.real-a.real)-pb*(bb.real-b.real)
        assert interval>0
        out["point_witness"]=w
        out["outward_point_excess"]=str(interval)
        out["outward_positive_verified"]=True
        out["point_bound_scope"]="One auxiliary coupled original reference. "
        out["point_bound_scope"]+="No claim that it occurs in an actual finite word."
    HERE.joinpath("local-result.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":main()
