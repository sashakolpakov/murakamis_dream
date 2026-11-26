#!/usr/bin/env python3
"""Exact word, collar and peripheral algebra for the mixed tangle.

The original PD arc assignments are checked explicitly. The companion
note supplies the relative Wirtinger proof and geometric argument.
This verifier uses no floating-point geometric solver.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
from pathlib import Path
import sympy as s
from spherogram import OneTangle

ROOT=Path(__file__).resolve().parents[1]
FIXTURE=ROOT/"repro/fixtures/research-mixed-two-crossing-subdivision.json"
D=json.loads(FIXTURE.read_text())
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output",type=Path,
 default=ROOT/"repro/results/research-mixed-word-collar-representation.json")
ARGS=parser.parse_args()
CHECKS=collections.Counter()
def eq(a,b=0,kind="rational_identities"):
 assert s.cancel(a-b)==0,(a,b)
 CHECKS[kind]+=1
def mat_eq(a,b,kind):
 for x,y in zip(a,b):eq(x,y,kind)

# Literal carrier and oval. The rational-word corners are
# (bottom left, bottom right, top right, top left).
pd=D["pd"]
assert pd[4:]==[[2,11,3,12],[1,16,2,17],[10,15,11,16],
               [14,9,15,10],[17,0,14,1]]
assert [slot for crossing,slot in OneTangle().adjacent]==[0,1,3,2]
assert [pd[4][3],pd[4][2],pd[7][1],pd[8][1]]==[12,3,9,0]
# Check the actual two main strands and oval paths, including directions.
assert [pd[8][1],pd[8][3],pd[5][0],pd[5][2]]==[0,1,1,2]
assert [pd[7][1],pd[7][3],pd[6][0],pd[6][2]]==[9,10,10,11]
assert [(pd[c][a],pd[c][b]) for c,a,b in
        [(5,3,1),(6,3,1),(7,2,0),(8,2,0)]]==[
        (17,16),(16,15),(15,14),(14,17)]
CHECKS["literal_PD_endpoint_and_path_checks"]=6

q,z,X,w,E,R=s.symbols("q z X w E R")
positive=lambda x,v:(s.cancel(x+(x-1)/v),s.cancel(-x*(1+v)))
negative=lambda x,v:(s.cancel(x*v/(v+1-x)),s.cancel(-(v+1)/x))
turn=lambda x,v:(1/x,1/v)
xx,vv=q,(q-1)**2/(z*q-q*q-1)
for op in [positive,positive,turn,negative,negative,turn]:
 xx,vv=op(xx,vv)
Ez=(z**3-5*z**2+10*z-7)/(z-1)
Vz=(z-2)/(z*z-3*z+3)**2
eq(s.limit(xx,q,1),Ez,"resolved_cap_word")
eq(s.limit(vv,q,1),Vz,"resolved_cap_word")
Y=s.factor(Ez.subs(z,1+1/X))
Vx=s.factor(Vz.subs(z,1+1/X))
eq(X**2*Y-X,(1-X)**3,"source_critical_equations")
eq(Vx,-(1-X*Y)/(Y-1)**2,"source_critical_equations")
T=(w*E+1)/(E+w)
RR=(E+w)*(w*E+1)/(E*(w+1)**2)
eq(RR,T*(1+E)**2/(E*(1+T)**2),"actual_leaf_dictionary")
eq((1-RR)/RR,-(E-1)**2/((E+w)*(E+1/w)),
   "actual_leaf_dictionary")
eq((E*T-1)/(E-T),w,"actual_leaf_dictionary")
eq(1/T,(E+w)/(1+w*E),"actual_leaf_dictionary")

# Entire original parabolic matrices and the positive-carrier meridian.
P0=s.Matrix([[1,0],[(E-1)/(E*R),1]])
P1=s.Matrix([[1,E-1],[0,1]])
P2=s.Matrix([[E*R-2*E+1,E-1],[1-E,E*R-1]])/(E*(R-1))
P3=s.Matrix([[(E+R-2)/(R-1),-R*(E-1)/(R-1)],
             [(E-1)/(R*(R-1)),(R-E)/(R-1)]])
a,b,c,d=[p.inv() for p in [P1,P2,P3,P0]]
mu=s.diag(1,1/E)*s.Matrix([[R/E-1-1/E,R],[-1,R]])
L=b*a
mat_eq(d*c*b*a,s.eye(2),"ordered_boundary_relation")
mat_eq(mu*L,L*mu,"entire_peripheral_commutation")
mat_eq(mu*c*mu.inv(),a.inv(),"entire_positive_carrier_relation")
mat_eq(mu*d*mu.inv(),L.inv()*a,"entire_positive_carrier_relation")
for p in [a,b,c,d]:
 eq(s.trace(p),2,"parabolic_lifts")
 eq(p.det(),1,"parabolic_lifts")
# The complete multiplier need not be inferred from a trace sign.
Rc=(E+1)**2/(4*E)
for p in [mu,L]:
 pc=p.subs(R,Rc)
 eq(s.trace(pc)**2,4*pc.det(),"complete_peripheral_parabolicity")

A=Ez+1/Ez+(Ez+1/Ez-2)/Vz
f2=z*z-5*z+7
f3=z**3-3*z*z+5*z-2
eq(A+2,f2*f3,"complete_cap_equation")
for f in [z-1,z-2,z*z-3*z+3,z**3-5*z*z+10*z-7]:
 assert s.gcd(f,f2*f3)==1
 CHECKS["all_complete_roots_in_regular_chart"]+=1
tau=s.Symbol("tau")
poly2=7*tau*tau+20*tau+16
poly3=17*tau**3+58*tau*tau+72*tau+32
tau_eq=s.together((tau+1)*Ez+1).as_numer_denom()[0]
eq(s.resultant(f2,tau_eq,z),poly2,"complete_cusp_polynomials")
eq(s.resultant(f3,tau_eq,z),-poly3,"complete_cusp_polynomials")
assert s.gcd(poly3.subs(tau,-tau),poly2)==1
assert s.gcd(poly3.subs(tau,-tau),poly3)==1
CHECKS["opposite_cusp_embedding_exclusions"]=2
for expr in [Ez-(2*z*z-6*z+9),
             Ez**3-7*Ez**2+7*Ez-17,
             z-(Ez**2-8*Ez+15)/8]:
 numerator,denominator=s.fraction(s.cancel(expr))
 assert s.rem(numerator,f3,z)==0
 assert s.gcd(denominator,f3)==1
 CHECKS["complete_representation_recovered_from_cusp_ratio"]+=1

report={"status":"passed","checks":dict(CHECKS),
 "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "original_diagram_fixture_sha256":hashlib.sha256(FIXTURE.read_bytes()).hexdigest(),
 "scope":"Exact original PD endpoints, resolved cap word, full collar matrices, complete cusp polynomials and regularity. The companion note proves the relative topology and geometric-germ implication."}
ARGS.output.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))

