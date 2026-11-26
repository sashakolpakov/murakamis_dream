#!/usr/bin/env python3
"""A single local own-four reference test at the new left cut 1/8."""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq, minimize

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import diagnose as d
P=np.pi
CUT=1/8

def evaluate(theta,details=False):
    pp=[d.CENTERS[t]+d.RADII[t]*np.exp(2j*P*float(q))
        for q,t in zip(theta,(0,1))]
    zz,_,res=d.old.base.block([pp[0].real,pp[0].imag,
                              pp[1].real,pp[1].imag],1)
    assert res<1e-10
    a,s,b=pp[0],zz[0],zz[1]
    M=(d.phase(s,a,b,1)-d.g(a)-1.5*d.g(b)).real
    pa=(d.gp(s+a)-d.gp(a)+2j*P*s).real
    pb=(d.gp(s+b)-1.5*d.gp(b)).real
    target=[]
    for z0,lam,p in ((a,1,pa),(b,1.5,pb)):
        der=lambda x:(d.gp(CUT+x+1j*z0.imag)
                      -lam*d.gp(x+1j*z0.imag)).real-p
        if der(.22)<=0:x=.22
        elif der(.45)>=0:x=.45
        else:x=brentq(der,.22,.45,xtol=1e-14)
        target.append(x)
    aa,bb=target[0]+1j*a.imag,target[1]+1j*b.imag
    row=(d.phase(CUT,aa,bb,1)-d.g(aa)-1.5*d.g(bb)).real
    excess=float(row-M-pa*(target[0]-a.real)-pb*(target[1]-b.real))
    return (excess,pp,zz,res,target,M,pa,pb) if details else excess

def main():
    old=json.loads(HERE.joinpath("local-result.json").read_text())
    start=[float(Q(v)) for v in old["angles"]]
    initial=evaluate(start,True)
    opt=minimize(lambda t:-evaluate(t),start,method="L-BFGS-B",
                 bounds=[(0,1),(0,1)],
                 options={"maxiter":60,"maxfun":220,"ftol":1e-13,"gtol":1e-8})
    theta=[Q(round(float(v)*10**12),10**12) for v in opt.x]
    excess,pp,zz,res,target,M,pa,pb=evaluate(theta,True)
    out={
        "status":"diagnostic_only",
        "scope":"Single local external-circle optimization for own4/ext3,4 at "
                "cut1/8, starting the fixed3/20 obstruction. Targets use clipped "
                "scalar stationarity. No cover, universal sign, or word realization.",
        "cut":"1/8","starting_old_point_sha256":d.sha(HERE/"local-result.json"),
        "source_sha256":d.sha(d.SOURCE),
        "helper_sha256":d.sha(d.ROOT/"experiments/certify_mixed_reduced_disk_conditional_packets.py"),
        "driver_sha256":d.sha(Path(__file__)),
        "start":start,"start_excess":float(initial[0]),
        "start_optimal_target":initial[4],
        "success":bool(opt.success),"message":str(opt.message),
        "iterations":int(opt.nit),"function_evaluations":int(opt.nfev),
        "angles":[str(v) for v in theta],"target":target,
        "floating_original_residual":float(res),"floating_excess":excess,
        "external_inputs":[d.encode(v) for v in pp],
        "roots":[d.encode(v) for v in zz],"M":M,"pa":pa,"pb":pb,
    }
    HERE.joinpath("new-cut-result.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":main()
