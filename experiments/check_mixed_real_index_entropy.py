#!/usr/bin/env python3
"""Exact identities and outward constants for the full cyclic real entropy."""
from pathlib import Path
from hashlib import sha256
import argparse,json
import sympy as sp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-real-index-entropy.json')
 args=ap.parse_args();ctx.prec=args.precision;ids=[]
 def exact(name,value):
  assert sp.simplify(sp.trigsimp(sp.expand_trig(value)))==0,name;ids.append(name)
 x,y=sp.symbols('x y',real=True)
 # Angles here are x and y, with the displayed pi factored out.
 c1,c2=sp.symbols('c1 c2',real=True);cp=(c1*c2-1)/(c1+c2)
 exact('tetrahedral Hessian determinant',(c1-cp)*(c2-cp)-cp*cp-1)
 exact('positive tetrahedral diagonal',sp.cos(x)*sp.sin(x+y)-sp.cos(x+y)*sp.sin(x)-sp.sin(y))
 exact('reflection first derivative comparison',sp.sin(x-y)-sp.sin(x+y)+2*sp.cos(x)*sp.sin(y))
 exact('reflection second derivative',-sp.cos(x-y)*sp.sin(x+y)-sp.cos(x+y)*sp.sin(x-y)+sp.sin(2*x))
 m,k=sp.symbols('m k',integer=True)
 exact('absolute symbol N power',k+(2*m-(4*m+2*k))/2+m)
 exact('absolute lattice Gaussian N power',-m+2*m-m)
 l,h=sp.Rational(13,50),sp.Rational(39,100)
 exact('lower pair minimum',2*l-sp.Rational(13,25));exact('mixed pair endpoint',l+h-sp.Rational(13,20));exact('upper pair endpoint',2*h-sp.Rational(39,50))
 exact('lower clearance',l-sp.Rational(1,4)-sp.Rational(1,100));exact('upper clearance',sp.Rational(2,5)-h-sp.Rational(1,100))
 exact('single reflection quadratic cost',sp.Rational(1,4)*sp.Rational(1,4)**2-sp.Rational(1,64))
 exact('two reflection incidences',2*sp.Rational(1,64)-sp.Rational(1,32))
 p=arb.pi();margins={}
 def pos(name,v):assert v>0,(name,str(v));margins[name]=str(v)
 lower=2*(13*p/50).sin();upper=2*(39*p/100).sin();mixed=4*(13*p/20).sin()**2
 pos('lower leg base exceeds one',lower-1);pos('upper leg base exceeds one',upper-1)
 pos('lower inward derivative both types',mixed-lower**3)
 pos('upper inward derivative both types',upper**2-mixed)
 pos('central curvature constant',p/(2*p/5).tan()-1)
 pos('high reflection sine',(p/5).sin()-arb(1)/2)
 pos('high reflection stronger than uniform gap',p/32-arb(1)/10000)
 deps=['notes/research_mixed_real_index_entropy.md','notes/research_mixed_wire_exact_contraction.md','notes/research_mixed_contracted_phase.md','notes/exact_factorial_interpolation_and_complex_contours.md']
 result={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(ids),'exact_identities':ids,'strict_comparison_count':len(margins),'margins':margins,
         'scope':'All cyclic3/4 words: global real entropy maximum and complement relative to that real maximum only. No geometric-action comparison or oscillatory lower bound.',
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies_sha256':{f:sha256((ROOT/f).read_bytes()).hexdigest()for f in deps}}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'passed','exact_identity_count':len(ids),'strict_comparison_count':len(margins)}))
if __name__=='__main__':main()
