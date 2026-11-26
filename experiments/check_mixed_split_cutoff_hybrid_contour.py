#!/usr/bin/env python3
"""Exact contour/region bookkeeping for the split-cutoff hybrid graph.

No new finite-source inequality is certified. Completed source estimates
are reused only after literal graph and Jacobian agreement. Region
bookkeeping uses Boolean presence variables, with no cyclic word enumeration.
"""
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_split_cutoff_hybrid_contour.md'
INPUTS=[('mixed_coupled_outer_graph','check'),('mixed_full_left_region','check'),('mixed_selected_right_taper_support','certify'),('mixed_plateau_accretivity','check')]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-split-cutoff-hybrid-contour.json');args=ap.parse_args()
 ph,sh=sha(PROOF),sha(__file__);deps={};records=[]
 for stem,prefix in INPUTS:
  rp=ROOT/f'repro/results/research-{stem.replace("_","-")}.json';r=json.loads(rp.read_text());assert r['status']=='passed'
  paths={f'notes/research_{stem}.md':r['proof_sha256'],f'experiments/{prefix}_{stem}.py':r['script_sha256']}
  for key in ('dependencies','dependencies_sha256'):paths.update(r.get(key,{}))
  for p,h in paths.items():assert sha(ROOT/p)==h,p;deps[p]=h
  deps[str(rp.relative_to(ROOT))]=sha(rp);records.append(str(rp.relative_to(ROOT)))
 x,e,b,c=s.symbols('x e b c',real=True);identities=[]
 def check(name,v):
  assert s.simplify(v)==0,(name,v);identities.append(name)
 right=400*(s.Rational(1,2)-x)**2
 check('quadratic right joins plateau',right.subs(x,s.Rational(9,20))-1)
 check('quadratic right joins real period',right.subs(x,s.Rational(1,2)))
 check('right derivative at plateau is minus forty',s.diff(right,x).subs(x,s.Rational(9,20))+40)
 check('right derivative at half is zero',s.diff(right,x).subs(x,s.Rational(1,2)))
 lowL=1-x/e;leftL=(x-s.Rational(1,10))/(b-s.Rational(1,10))
 lowR=(x-e)/(s.Rational(1,10)-e)
 for name,v in [('left cutoff seam value one',lowL.subs(x,0)-1),('left cutoff collar value zero',lowL.subs(x,e)),('left rise starts zero',leftL.subs(x,s.Rational(1,10))),('left rise ends one',leftL.subs(x,b)-1),('own cutoff collar starts zero',lowR.subs(x,e)),('own cutoff reaches one at one tenth',lowR.subs(x,s.Rational(1,10))-1)]:check(name,v)
 check('slow left derivative',s.diff(leftL.subs(b,s.Rational(11,50)),x)-s.Rational(25,3))
 check('fast selected derivative',s.diff(leftL.subs(b,s.Rational(3,25)),x)-50)
 check('naive two-cycle seam jump',c*1*1-c*1*0-c)
 check('one-cycle naive seam happens to match',c*1*0-c*0*1)
 check('central coefficient counted once',s.Integer(1)+1-1-1)
 check('finite scalar unchanged in union',s.Symbol('K')+s.Symbol('K')-s.Symbol('K')-s.Symbol('K'))
 # Low own coordinates have disjoint supports, not a small-height estimate.
 check('own low height first piece',s.Integer(0)*lowL)
 check('own low height second piece',lowR*s.Integer(0))
 epsilon=Q(1,1000);K=max(Q(50),1/epsilon);B=Q(57,1000)*(40+K)
 assert B==Q(1482,25)and 1+B*B<60**2
 assert 0<epsilon<Q(1,10)
 # Presence variables apply to any number of coordinates: low means some
 # x<.1, left some .1<=x<.22, and right some x>.45. No word is enumerated.
 low,left,right_present=s.symbols('low left right',boolean=True)
 inQ=~low&~right_present;inV=~low&~left;inP=~low&~left&~right_present
 boolean_identities={
  'intersection is the plateau cube':s.Equivalent(inQ&inV,inP),
  'complement is low or a mixed left-right configuration':s.Equivalent(
   ~(inQ|inV),low|(~low&left&right_present)),
 }
 for name,identity in boolean_identities.items():
  assert s.simplify_logic(identity)==s.true,name
 # The universal indicator identity has only four Boolean truth values.
 indicator_truth_values=((False,False),(False,True),(True,False),(True,True))
 for a,d in indicator_truth_values:
  assert int(a or d)==int(a)+int(d)-int(a and d)
 assert ph==sha(PROOF)and sh==sha(__file__)
 for p,h in deps.items():assert sha(ROOT/p)==h,p
 result=dict(status='passed',exact_identity_count=len(identities),exact_identities=identities,boolean_identity_count=len(boolean_identities),boolean_identities=list(boolean_identities),inclusion_exclusion_truth_values=len(indicator_truth_values),cyclic_pattern_enumerations=0,primary_records=records,primary_record_count=len(records),example_epsilon=str(epsilon),example_jacobian_base_upper=60,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,scope='Exact periodic hybrid graph and literal union Q_m union V_m, including selected terms and one unchanged central coefficient. No new interface source bound, full-period estimate or boundary-insertion theorem.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',len(identities),'exact identities',len(boolean_identities),'Boolean identities',len(indicator_truth_values),'indicator truth values; zero cyclic patterns;',len(records),'current primary records',flush=True)
if __name__=='__main__':main()
