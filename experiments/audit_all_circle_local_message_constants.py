"""Exact rational checks for constants in the local tree-message proof.
These check the stated numerical margins, not the induction or its source identities.
"""
from fractions import Fraction as F
import json
import hashlib
from pathlib import Path

r,cK,c,y0,rho,t0 = (F(1,2**p) for p in (12,16,18,56,14,16))
A0,kappa,delta = F(1,2**41),F(1,2**120),F(1,20)
pi_lo, pi_hi = F(3),F(22,7)
a_lo,a_hi = 1/(2*pi_hi),1/(2*pi_lo)
alpha_lo,etaK_lo=F(1,250),pi_lo/200
eta=F(1,2**80)
tests=[]
def check(name,lhs,rhs):
    if not lhs < rhs:
        raise AssertionError((name,lhs,rhs))
    tests.append({"name":name,"left":str(lhs),"right":str(rhs),"relation":"<"})
check("real full-kernel discarded angular cost",4*cK,etaK_lo)
check("retained real angular decay",cK,alpha_lo/2)
check("complex complementary kernel gap",r+r*r+y0+2*cK,etaK_lo/2)
# sin(1/16)>1/(8*pi), pi^2<10.
check("far kernel conditional normalization",2*r*r,alpha_lo/F(1280))
check("far kernel decay margin",cK,alpha_lo/4)
check("conditional saddle maps disk into itself",t0+delta*r,r)
check("outgoing curvature class",F(1,50)+F(20,19*2500),F(1,20))
check("one-vertex action drop",420*pi_hi/361,F(4))
# 1-cos(r/2)>=r^2/(2*pi^2)>r^2/20.
check("Poisson strip patch",(1+c)*y0,c*r*r/40)
# Global kernel plus children: smallest angular coefficient is c/2.
check("conditional angular Gaussian",F(1,2**20)/(2*pi_lo),c/F(10))
check("conditional imaginary Gaussian",16,F(128)/(2*pi_hi))
check("charge-tail quadratic cost",2**18*A0,F(1,2))
check("tail strip lies inside message strip",A0*t0,y0)
check("tail absolute gap",F(1,2**77),A0*t0*t0*a_lo/2)
endpoint_cost = pi_hi*A0*t0 + A0*t0*t0 + 128*A0*A0*t0*t0
check("endpoint connectors",endpoint_cost,F(1,2**21)*pi_lo*pi_lo)
check("real interval discard",F(1,2**51),F(1,2**20)*a_lo*rho*rho)
check("local connector charge sign",F(300,361),F(7,8))
check("local connector loss",F(1,2**34),a_lo*rho*rho/8)
check("first charge above conditional errors",4*kappa,eta/2)
check("outgoing real envelope after normalization",4*kappa,(cK-c)*r*r/20)
check("geometric branch in positive disk",2*pi_hi*F(20,19)/2**60,F(1,100))
out={"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"scope":"Exact numerical margins only; does not certify the tree induction, knot invariant, or metric completion.","count":len(tests),"comparisons":tests}
Path(__file__).with_name('all_circle_local_message_constants_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({"exact_comparisons":len(tests),"status":"passed"}))
