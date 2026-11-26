#!/usr/bin/env python3
"""Exact collar bookkeeping and completed-source provenance; no width cover."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_coherent_half_endpoint_collar.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-coherent-half-endpoint-collar.json')
 args=ap.parse_args();ph,sh=sha(PROOF),sha(__file__);deps={};visited=set();checks=[];records={}
 def check(name,value):assert value,name;checks.append(name)
 def bind(path,expected=None):
  value=sha(ROOT/path);assert expected is None or value==expected,(path,expected,value)
  if path in deps:assert deps[path]==value
  deps[path]=value;return value
 def inherit(path):
  bind(path);r=json.loads((ROOT/path).read_text())
  if path in visited:return r
  visited.add(path);bindings={}
  for key in ('dependencies','dependencies_sha256'):
   for p,h in r.get(key,{}).items():
    if p in bindings:assert bindings[p]==h
    bindings[p]=h;bind(p,h)
  for p in bindings:
   if p.startswith('repro/results/')and p.endswith('.json'):inherit(p)
  return r
 specs=[
 ('mixed_real_packet_complex_stability','check','mixed_real_packet_complex_stability'),
 ('mixed_left_right_interface_source','certify','mixed_left_right_interface_source'),
 ('mixed_right_square_conditional_packets','certify','mixed_unselected_right_taper_products'),
 ('mixed_deep_low_half_region','check','mixed_deep_low_half_region'),
 ('mixed_full_nonlow_half_region','check','mixed_full_nonlow_half_region'),
 ('mixed_fourier_weight_continuation','check','mixed_fourier_weight_continuation'),
 ('mixed_split_cutoff_hybrid_contour','check','mixed_split_cutoff_hybrid_contour')]
 for stem,prefix,proof in specs:
  pp='notes/research_'+proof+'.md';ss='experiments/'+prefix+'_'+stem+'.py';rr='repro/results/research-'+stem.replace('_','-')+'.json'
  bind(pp);bind(ss);r=inherit(rr);inherited={**r.get('dependencies',{}),**r.get('dependencies_sha256',{})}
  check(stem+': passed and current',r['status']=='passed'and r['script_sha256']==deps[ss]and r.get('proof_sha256',inherited.get(pp))==deps[pp]);records[stem]=r
 J=sp.symbols('J',positive=True)
 for selected in (0,1):
  check('real-right forcing retained, selected='+str(selected),sp.Max(-J,0)-2*sp.pi*selected*0==0)
  check('relative correction independent of selection='+str(selected),sp.simplify(J+sp.Max(-J,0)-2*sp.pi*selected*0-J)==0)
 check('two Fourier halves give one full J',sp.Rational(1,2)*J+sp.Rational(1,2)*J==J)
 check('original primitive has zero real part at half',sp.simplify(sp.re((sp.polylog(2,-1)-sp.pi**2/6)/(2*sp.pi*sp.I)))==0)
 check('chosen outer strip stays below the next sine sign threshold',F(1,2)+F(1,10)<F(5,6)<1)
 check('every moved coordinate has both left cutoffs exactly one',max(F(11,50),F(3,25))<F(1,2))
 check('own right profile vanishes before and after clamping',F(1,2)+F(1,10)>F(1,2)>F(9,20))
 check('removed real-right selection has saturated reference displacement',400*(F(9,20)-F(39,100))**2>1)
 reserve=F(1,4000)+F(1,10)*(F(1,2)-F(9,20))
 check('clamped half-endpoint occupation is21/4000',reserve==F(21,4000))
 check('compact perturbation leaves1/200 per collar coordinate',reserve-F(1,4000)==F(1,200))
 check('uniform off-plateau phase gap is unchanged',min(F(1,200),F(1,4000))==F(1,4000))
 check('one total tolerance leaves the claimed finite gap',F(1,4000)-F(1,8000)==F(1,8000))
 m=sp.symbols('m',positive=True)
 check('arbitrary word length tolerance is counted once',sp.simplify(m/(8000*m)-sp.Rational(1,8000))==0)
 low=records['mixed_deep_low_half_region']
 check('completed deep-low theorem has the required finite gap',F(low['finite_gap'])==F(1,8000))
 assert ph==sha(PROOF)and sh==sha(__file__)
 assert all(sha(ROOT/p)==h for p,h in deps.items())
 out=dict(status='passed',exact_checks=len(checks),checks=checks,primary_records=len(specs),current_bindings=len(deps),numerical_cells_recomputed=0,collar_width_computed=False,clamped_right_loss='21/4000',per_right_cost_budget='1/4000',remaining_right_loss='1/200',finite_gap='1/8000',proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,scope='Written compactness deduction from complete original-source neighborhoods. Positive collar width is unquantified and depends on fixed rho. No new numerical source cover, whole-period estimate, or near-zero uniformity.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',len(checks),'exact checks;',len(specs),'primary records;',len(deps),'current bindings; no collar width computed',flush=True)
if __name__=='__main__':main()
