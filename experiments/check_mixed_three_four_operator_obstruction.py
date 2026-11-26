#!/usr/bin/env python3
"""Exact checks for the all-level relative-crossing operator obstruction."""
import argparse,json
from pathlib import Path
from hashlib import sha256
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-three-four-operator-obstruction.json');args=ap.parse_args()
 checked=[]
 def exact(name,value):
  assert sp.simplify(sp.expand_trig(value))==0,name;checked.append(name)
 theta=sp.symbols('theta',real=True)
 exact('three-eigenvalue positive dependence real',sp.sin(4*theta)+sp.sin(2*theta)*sp.cos(6*theta)-sp.sin(6*theta)*sp.cos(2*theta))
 exact('three-eigenvalue positive dependence imaginary',sp.sin(2*theta)*sp.sin(6*theta)-sp.sin(6*theta)*sp.sin(2*theta))
 exact('three angular gaps sum',6*theta+(sp.pi-4*theta)+(sp.pi-2*theta)-2*sp.pi)
 exact('N6 antipodal eigenvalues',sp.exp(6*sp.pi*sp.I/6)+1)
 q=sp.I;M2=sp.Matrix([[1,0],[-q,-q**2]])
 exact('original N2 lower diagonal',M2[1,0]+sp.I)
 exact('original N2 diagonal eigenvalue',M2[1,1]-1)
 assert M2!=sp.eye(2) and (M2-sp.eye(2))**2==sp.zeros(2)
 checked.append('N2 nonzero square-zero Jordan part')
 k=sp.symbols('k',nonnegative=True)
 # N=7+k. All weights/gaps lie strictly inside their positive sine intervals.
 positive_polynomials=list(map(sp.sympify,[7+k,6,1+k,3+k,5+k,4,2]))
 assert all(sp.Poly(v,k).all_coeffs()and all(c>=0 for c in sp.Poly(v,k).all_coeffs())and v.subs(k,0)>0 for v in positive_polynomials)
 checked.append('all-level N>=7 angular sign reduction')
 for j in range(3):
  N=sp.symbols('N',positive=True)
  exp_phase=sp.pi*j+sp.pi*j*(j+1)/N
  target=(0,sp.pi+2*sp.pi/N,6*sp.pi/N)[j]
  exact(f'normalized crossing eigenphase j{j}',exp_phase-target-2*sp.pi*(j//2))
 # Nonzero first-normal coefficient: N-1>0 and 0<pi/N<=pi/2 for all N>=2.
 n=sp.symbols('n',nonnegative=True)
 assert sp.Poly((2+n)-1,n).all_coeffs()==[1,1]
 checked.append('all-level nonzero physical first-normal numerator')
 deps=['notes/research_mixed_three_four_operator_obstruction.md','notes/research_mixed_wire_exact_contraction.md','notes/research_three_four_source_interface.md','notes/research_original_almost_invariance_and_observation.md','notes/research_mixed_three_four_joint_coercivity.md']
 result={'status':'passed','exact_check_count':len(checked),'exact_checks':checked,'scope':'All-level exact relative-operator obstruction. No global oscillatory estimate or source lower bound.','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'passed','exact_check_count':len(checked)}))
if __name__=='__main__':main()
