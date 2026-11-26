#!/usr/bin/env python3
"""Finite arithmetic for the directed-message criterion; no invariant evaluation."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, math

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/private/tmp/md-variable-local-volume-budget-results.json"))
    args=parser.parse_args()
    k=F(1,2**16); c=k/2; t=F(1,2**14); rho=F(1,16); b0=F(1,2**11)
    pi_lo=F(3); pi_hi=F(22,7)
    chi_lo=rho*rho/2-rho**4/24
    chi_hi=rho*rho/2
    delta_lo=c*chi_lo/(4*(1+c))
    delta_hi=c*chi_hi/(4*(1+c))
    checks=[]
    def check(name,left,right):
        ok=left<right
        checks.append({"name":name,"strict_less":ok,"left":str(left),"right":str(right),"ratio":float(left/right)})
        if not ok: raise AssertionError(name)
    check("delta lower", F(1,2**30),delta_lo)
    check("tail first branch for n>=2^27",64*pi_hi/(t*delta_lo),F(2**54))
    check("tail second branch for n>=2^27",32*pi_hi*pi_hi/(t*t*k),F(2**54))
    check("outgoing rational patch",F(330,361),F(3071,3072))
    check("uniform charge cutoff",F(2),t*F(2**27)/(2*pi_hi))

    # Conservatively chosen heights are below each branch of the actual min.
    n=2**60+1
    Dl=F(n)/(2*pi_hi); Du=F(n+1)/(2*pi_lo)
    Al=2*k/(pi_hi*pi_hi); Bu=F(16)
    Cu=Bu+(F(n)/(2*pi_lo))**2/(4*Al)
    yl=t*k/(2*n)
    check("leaf height strip",yl,b0/2)
    check("leaf height chirp",yl,t*Dl/(4*Cu))
    check("leaf height endpoint",yl,2*k/(8*(F(n,2)+t*Du)))
    check("leaf height square",yl*yl,k/64)
    betal=420*pi_hi/(361*n*n)
    etal=[t*Dl*yl/2,k,Al*rho*rho,F(1)/(2*pi_hi)*rho*rho/8]
    for j,eta in enumerate(etal): check(f"leaf action branch {j}",2*betal,eta)
    check("leaf patch",betal,(k-c)*chi_lo)
    check("leaf cutoff",F(2),t*Dl)

    d=30_000_001
    Dl=F(d)/(2*pi_hi); Du=F(d+1)/(2*pi_lo)
    Al=F(d)*c/(pi_hi*pi_hi)
    Cu=F(d)+(1/pi_lo)**2/(4*Al)
    ys=delta_lo/2
    check("center height chirp",ys,t*Dl/(4*Cu))
    check("center height endpoint",ys,F(d)*c/(8*(1+t*Du)))
    check("center height square",ys*ys,c/8)
    betas=420*pi_hi*d/(361*(d*d+4))
    etas=[t*Dl*ys/2,F(d)*c/2,Al*rho*rho,F(d)/(2*pi_hi)*rho*rho/8]
    for j,eta in enumerate(etas): check(f"center action branch {j}",2*betas,eta)
    check("center cutoff",F(2),t*Dl)
    check("outside old summed criterion",F(1,2**25),F(d,d*d+4))
    check("center cannot pay any outgoing patch",k*chi_hi,420*pi_lo*d/(361*(d*d+4)))

    result={
      "scope":"Exact rational enclosures of the displayed finite inequalities. No quantum finite sum or asymptotic theorem is numerically tested.",
      "uniform_corollary":{"minimum_abs_power":2**27,"alternative_minimum_degree":2**28,"all_degrees":"proved by symbolic inequalities (49)-(53), without a degree scan"},
      "star":{"central_degree":d,"central_power":2,"leaf_power":n,"leaf_budget":str(c),"center_upper_2beta_over_lower_eta":float(2*betas/min(etas)),"leaf_upper_2beta_over_lower_eta":float(2*betal/min(etal))},
      "checks":checks,
      "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"all_strict":True,"output":str(args.output),"center_ratio":result["star"]["center_upper_2beta_over_lower_eta"]}))
if __name__=="__main__":main()
