#!/usr/bin/env python3
"""Floating reevaluation of existing seam witnesses; no optimization or proof."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'repro/results/research-mixed-height-resolved-seam-sources.json'
CASES=ROOT/'repro/diagnostics/2026-11-05-seam-actual-plane/seam-actual-plane-common-a3-diagnostic.json'
DEPTHS=ROOT/'repro/diagnostics/2026-11-05-seam-actual-plane/seam-actual-plane-worst-depths-diagnostic.json'
OUTPUT=Path(__file__).with_name('saved-case-evaluation.json')

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 assert not OUTPUT.exists(),'refuse overwrite'
 inputs={str(p.relative_to(ROOT)):sha(p) for p in (SOURCE,CASES,DEPTHS)}
 source=json.loads(SOURCE.read_text());cases=json.loads(CASES.read_text());depths=json.loads(DEPTHS.read_text())
 assert source['status']=='passed' and source['extracted_zero_slope_knots']==19
 def profile(name,h):
  knots=[(float(F(v['height'])),float(F(v['upper']))) for v in source['profiles'][name]]
  assert knots[0][0]<=h<=knots[-1][0]
  for (lo,a),(hi,b) in zip(knots,knots[1:]):
   if lo<=h<=hi:return a+(h-lo)/(hi-lo)*(b-a)
  raise AssertionError((name,h))
 rows=[]
 for c in cases['cases']:
  word=c['word'];alpha,beta,gamma=word[-1],word[0],word[1%len(word)]
  sl,sr=c['selection_xm2_xm1_xp1'][1:]
  hl,hr=c['physical_left_height'],c['physical_right_height']
  for d,s,h in ((alpha,sl,hl),(gamma,sr,hr)):
   assert (not s and -.03<=h<=.02) if d==0 else ((0<=h<=.014) if s else (-.057<=h<=0))
  left,right=profile(f'A{beta}{alpha}',hl),profile(f'B{gamma}',hr)
  change=left+right-c['source_ceiling']
  rows.append(dict(word=word,selection_xm2_xm1_xp1=c['selection_xm2_xm1_xp1'],physical_variables=c['variables_xm2_xm1_xp1_xp2_lambda'],physical_heights=[hl,hr],old_constant_source=c['source_ceiling'],height_resolved_source=left+right,left_profile=left,right_profile=right,source_change=change,old_A3_comparison=c['value'],new_A3_comparison=c['value']+change))
 assert len(rows)==29
 old=depths['witness'];w=next(r for r in rows if r['word']==old['word'] and r['selection_xm2_xm1_xp1']==old['selection_xm2_xm1_xp1'])
 assert w['physical_variables']==old['variables_xm2_xm1_xp1_xp2_lambda']
 corrected_depths=[dict(h=r['h'],old_comparison=r['actual_plane_comparison'],height_resolved_comparison=r['actual_plane_comparison']+w['source_change']) for r in depths['comparisons']]
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 out=dict(scope='Only a floating substitution of the proved height profiles at 29 previously saved witnesses. No new optimization, coverage, or universal comparison. A3 is not the incoming supremum; A4/A5 are differences of lower maximum estimates.',input_sha256=inputs,script_sha256=sha(Path(__file__)),cases=rows,case_count=29,maximum_saved_A3=max(rows,key=lambda r:r['new_A3_comparison']),previous_worst_depth_comparisons=corrected_depths,optimization_jobs=0)
 OUTPUT.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(worst_saved=out['maximum_saved_A3'],previous_worst_depth_comparisons=corrected_depths),indent=2))
if __name__=='__main__':main()
