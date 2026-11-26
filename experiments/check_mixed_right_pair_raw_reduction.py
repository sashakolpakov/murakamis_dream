#!/usr/bin/env python3
"""Exact whole-row right-angle reduction and outward concave support grid."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,itertools
import numpy as np
import sympy as sy
from scipy.optimize import minimize
from scipy.special import spence
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1];PROOF=ROOT/'notes/research_mixed_right_pair_raw_reduction.md'
DEPS=['notes/research_mixed_boundary_strip_bounds.md','notes/research_mixed_fourier_weight_continuation.md','notes/research_mixed_real_outer_support.md','notes/research_mixed_conditional_torus_composition.md','notes/research_mixed_oriented_height_reset.md']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-pair-raw-reduction.json');args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision
 hashes={p:sha(ROOT/p)for p in DEPS};ph,sh=sha(PROOF),sha(__file__);pi=arb.pi();ii=acb(0,1)
 def J(x):return (((-2*pi*ii*x).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real
 def L(x):return (2*(pi*x).sin()).log()
 def fj(x):return ((spence(1-np.exp(-2j*np.pi*x))-np.pi**2/6)/(2j*np.pi)).real
 x,u,p=sy.symbols('x u p',real=True)
 assert sy.trigsimp(sy.expand_trig(sy.sin(sy.pi*(x+u))**2-sy.sin(sy.pi*x)**2-sy.sin(sy.pi*u)*sy.sin(sy.pi*(2*x+u))))==0
 assert sy.trigsimp(sy.expand_trig(sy.sin(sy.pi*u)**2-sy.sin(sy.pi*(p-u))**2-sy.sin(sy.pi*p)*sy.sin(sy.pi*(2*u-p))))==0
 a,b=sy.symbols('a b');c=(a*b-1)/(a+b);assert sy.cancel((a-c)*(b-c)-c*c-1)==0
 A,B,C,D,E,Ff=sy.symbols('A B C D E F');assert sy.expand(A+B+C*(x-D)+E*(p-Ff)-C*x-(A+B-C*D+E*(p-Ff)))==0
 rows=[]
 for e,al in itertools.product((0,1),repeat=2):
  vals=[]
  for j in range(19):
   k=F(-1,5)+F(j,40)
   def ff(v):
    uu,pp=v;return fj(uu+.5)+fj(uu+pp)-(2+e)*fj(uu)-(1+al/2)*fj(pp)-float(k)*pp
   op=minimize(lambda v:-ff(v),[.27,.33],bounds=[(.001,.499),(.22,.45)],method='L-BFGS-B',options={'ftol':1e-14,'gtol':1e-10})
   uu,pp=[F(round(float(v)*10**10),10**10)for v in op.x];assert 0<uu<F(1,2)and F(11,50)<=pp<=F(9,20)
   U,P=ar(uu),ar(pp);val=J(U+ar(F(1,2)))+J(U+P)-(2+e)*J(U)-ar(1+F(al,2))*J(P)-ar(k)*P
   du=L(U+ar(F(1,2)))+L(U+P)-(2+e)*L(U);dp=L(U+P)-ar(1+F(al,2))*L(P)-ar(k)
   upper=val+max((du*(ar(v)-U)).upper()for v in(0,F(1,2)))+max((dp*(ar(v)-P)).upper()for v in(F(11,50),F(9,20)))
   n=int((upper*10**9).ceil().unique_fmpz());bound=F(n+1,10**9);assert ar(bound)>upper
   vals.append(dict(slope=str(k),point=[str(uu),str(pp)],upper=str(bound),outward_tangent=str(upper)))
  rows.append(dict(epsilon=e,other_halfweight=al,grid=vals))
 assert hashes=={p:sha(ROOT/p)for p in DEPS}and ph==sha(PROOF)and sh==sha(__file__)
 result=dict(status='passed',precision_bits=args.precision,exact_identities=4,source_supports=76,profiles=rows,target_interval=['11/50','9/20'],slope_interval=['-1/5','1/4'],slope_step='1/40',proof_sha256=ph,script_sha256=sh,dependencies=hashes,scope='Full original real-right raw-envelope reduction and certified low-row supports. No correlated reference gap or cycle asymptotic.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS 4 exact identities; 76 outward supports',flush=True)
if __name__=='__main__':main()
