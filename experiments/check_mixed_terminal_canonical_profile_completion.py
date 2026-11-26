#!/usr/bin/env python3
"""Exact final minima of the saved canonical terminal face extraction.

Standard library only; no source, root, primitive or interval evaluator.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE='repro/results/research-mixed-terminal-canonical-face-reserve.json'
PROOF='notes/research_mixed_terminal_canonical_profile_completion.md'
PINNED={'experiments/check_mixed_terminal_canonical_face_reserve.py': '4cbeda03dfee69565262e5e25486d261f97e6cbc417934e7ed417f19d75cce04',
 'notes/research_mixed_terminal_canonical_face_reserve.md': '45d3def413d15478b3fe968409f98b3730f686a9124195b1e718b5afe027ed8e',
 'notes/research_mixed_terminal_canonical_profile_completion.md': 'a56f2ab3d8c3c4b2b3d6820b5790d4471b0ef2a186900044992cec9de650cd9e',
 'notes/research_mixed_terminal_concave_profile_envelope.md': '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd',
 'notes/research_mixed_terminal_joint_main_budget.md': '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
 'notes/research_mixed_terminal_joint_main_curvature_completion.md': '5e627111f330e9a190d71113e4fbf484a2f9f964b8719078870f29f9d6443343',
 'notes/research_mixed_terminal_reserved_profile_completion.md': '503651546aad495cde602dde2893c49bde4b802ba442b4f4e83cf259c31cdb25',
 'repro/results/research-mixed-terminal-canonical-face-reserve.json': 'c85ef62dd25724f6bed335dc16982c2133e4f991a5badcd68e038a57b1a513aa'}
TABLE=(
 ('-.096265803','-.030905970','-.142512363','-.142282471','-.246456292','-.224958536','-.261295714','-.340662678','-.029157040'),
 ('-.010518297','-.094767177','+.040487366','-.035272525','-.057820883','-.071383939','-.066723020','-.341709413','-.043041634'),
 ('-.088561372','-.014585852','-.131003881','-.130732097','-.239397956','-.217900200','-.244511642','-.323878606','-.012372968'),
 ('-.004665950','-.076810061','+.050485036','-.023011977','-.052488169','-.066051225','-.048182761','-.323169155','-.024501375'))


def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as stream:
  for b in iter(lambda:stream.read(1048576),b''):h.update(b)
 return h.hexdigest()


def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 assert not args.output.exists() and PINNED and PROOF in PINNED
 inputs=dict(PINNED)
 own=Path(__file__).resolve().relative_to(ROOT).as_posix()
 inputs[own]=sha(ROOT/own)
 for name,digest in inputs.items():assert sha(ROOT/name)==digest,name
 data=json.loads((ROOT/SOURCE).read_text())
 assert data['status']=='completed saved-only extraction' and data['changed_inputs']==[]
 assert data['canonical_reference_cases_checked']==4 and data['required_family_cases_checked']==36
 assert data['unresolved_family_cases']==0
 assert data['insufficient_reserve_family_cases']==3 and data['insufficient_case_plane_family_cases']==2
 assert data['analytic_evaluations']==data['root_or_source_replays']==data['new_parameter_cells']==0
 assert data['checker_sha256']==inputs['experiments/check_mixed_terminal_canonical_face_reserve.py']
 assert data['proof_sha256']==inputs['notes/research_mixed_terminal_canonical_face_reserve.md']
 for name,digest in data['input_sha256'].items():
  assert name not in inputs or inputs[name]==digest,name
  assert sha(ROOT/name)==digest,name
  inputs[name]=digest
 expected=list(itertools.product((0,1),repeat=2))
 assert [(c['beta'],c['epsilon']) for c in data['canonical_cases']]==expected
 failures=[];common_failures=[];passed=[];summaries=[]
 for index,(case,table) in enumerate(zip(data['canonical_cases'],TABLE)):
  beta,eps=case['beta'],case['epsilon']
  assert len(case['intersecting_original_cells'])==1
  assert case['intersecting_original_cells'][0]['index']==(2343,1157,2363,1291)[index]
  plane={k:F(v) for k,v in case['joined_plane_upper_rational'].items()}
  assert set(plane)=={'factorial','forced'}
  plane_upper=max(plane.values())
  assert plane_upper==F(case['largest_case_plane_upper_rational'])<F(11,200)
  inventory=[('three_mixed',i) for i in range(8)]+[('three_half',0)] if eps==0 else [('four',i) for i in range(8)]+[('four',20)]
  assert [(f['series'],f['family']) for f in case['families']]==inventory
  rows=[];local=[]
  for fi,(family,decimal) in enumerate(zip(case['families'],table)):
   assert family['complete_finite_coverage'] and family['null_jobs_unresolved']==[]
   values=[F(c['decoded_upper_rational']) for c in family['contributing_jobs']]
   assert values and max(values)==F(family['maximum_upper_rational'])
   raw=max(values);upper=raw+plane_upper
   assert upper==F(family['case_joined_upper_rational'])
   assert -upper==F(family['case_joined_gap_rational'])
   assert {k:raw+v for k,v in plane.items()}=={k:F(v) for k,v in family['case_branch_joined_uppers_rational'].items()}
   assert F(decimal)>upper  # Published decimal table is conservative.
   assert family['strictly_pays_11over200']==(raw<-F(11,200))
   assert family['strictly_pays_case_plane']==(upper<0)
   key=(beta,eps,family['series'],family['family'])
   if raw>=-F(11,200):common_failures.append(key)
   if upper<0:
    assert upper<-F(1,250)
    passed.append((upper,key));local.append(upper)
   else:
    assert upper>0 and eps==1 and fi==2
    failures.append(key)
   rows.append({'series':family['series'],'family':family['family'],
      'bare_upper_rational':str(raw),'joined_upper_rational':str(upper),
      'published_decimal_upper':decimal,'strict_gap_1over250':upper<-F(1,250)})
  assert len(local)==(9 if eps==0 else 8)
  summaries.append({'beta':beta,'epsilon':eps,'source_index':case['source_index'],
      'source_case_sha256':case['source_case_sha256'],
      'original_cell_index':case['intersecting_original_cells'][0]['index'],
      'face_comparisons':rows,'completed_face_count':len(local),
      'weakest_completed_joined_upper_rational':str(max(local)),
      'completed_terminal_label_count':27 if eps==0 else 26,
      'remaining_terminal_labels':[] if eps==0 else [['0','L']]})
 assert len(passed)==34
 assert failures==[(0,1,'four',2),(1,1,'four',2)]
 assert common_failures==[(0,1,'four',0),(0,1,'four',2),(1,1,'four',2)]
 worst,key=max(passed)
 assert key==(1,1,'four',0)
 assert min(F(1,800),F(1,250),F(1,125))==F(1,800)
 assert F(1,800)-F(1,3200)-F(1,1600)>0
 changed=[n for n,h in inputs.items() if sha(ROOT/n)!=h]
 assert not changed
 out={'status':'passed','source_path':SOURCE,'source_sha256':inputs[SOURCE],
      'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
      'input_sha256':inputs,'changed_inputs':changed,'same_selected_height_rational':'1/100',
      'family_cases_checked':36,'strict_gap_1over250_cases':34,
      'unresolved_null_cases':0,'insufficient_case_plane_comparisons':failures,
      'insufficient_common_threshold_comparisons':common_failures,
      'weakest_completed_joined_upper_rational':str(worst),'attaining_case_family':key,
      'reserve_beyond_1over250_rational':str(-worst-F(1,250)),
      'canonical_cases':summaries,'common_completed_profile_gap_rational':'1/800',
      'terminal_three_complete_finite_kernel_gap_rational':'1/1600',
      'analytic_evaluations':0,'old_record_or_source_replays':0,
      'uniform_reference_domain_claimed':False,'finite_word_realization_claimed':False,
      'complete_terminal_four_kernel_claimed':False}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('x') as stream:stream.write(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':'passed','record_sha256':sha(args.output),
   'face_cases_checked':36,'strict_gap_1over250_cases':34,'terminal_label_counts':[27,26,27,26]}))


if __name__=='__main__':main()
