#!/usr/bin/env python3
"""Exact completion of all terminal labels at four canonical references.

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
PROOF='notes/research_mixed_terminal_private_left_joint_transfer.md'
ASSEMBLY='notes/research_mixed_terminal_all_profile_completion.md'
ORIGINAL='repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
PLANE='repro/results/research-mixed-terminal-reserved-plane-transfer.json'
CURVATURE='repro/results/research-mixed-terminal-joint-main-curvature-budget.json'
COMMON='repro/results/research-mixed-terminal-joint-main-common-height.json'
PINNED={'experiments/check_mixed_terminal_canonical_face_reserve.py': '4cbeda03dfee69565262e5e25486d261f97e6cbc417934e7ed417f19d75cce04',
 'experiments/check_mixed_terminal_joint_main_common_height.py': '1f9680fc15362516df2b82c8bbcdb99e9720f2861e04209641669ddb191d2e03',
 'experiments/check_mixed_terminal_joint_main_curvature_budget.py': '4362cd068f55a15d74afa3530c37631b6ea515e5de76592583152870f28551db',
 'experiments/check_mixed_terminal_reserved_plane_transfer.py': 'b471d62e1f672d6ce15959de609ddd5e06d9372d5c394a2d1960332fe3294c36',
 'notes/research_mixed_pair_curvature_composition.md': 'b0ee9b836af171147647b6c93f0a3c1651c909867fb828184a7afdc4251a1f73',
 'notes/research_mixed_reference_shape_half_plane.md': '28c1d35c39ac2290733d6cada8e4ae1d1e6fd58ebf641c0aef9168f962e7a143',
 'notes/research_mixed_terminal_all_profile_completion.md': 'dd6fe0212bbaf450680a65d33114d30ed5203aeeaf25956d7d070bb44046daa3',
 'notes/research_mixed_terminal_canonical_face_reserve.md': '45d3def413d15478b3fe968409f98b3730f686a9124195b1e718b5afe027ed8e',
 'notes/research_mixed_terminal_concave_profile_envelope.md': '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd',
 'notes/research_mixed_terminal_four_selected_height_completion.md': '5b688d2adf67895f430a2fef77a5d98fcb8ac74846ebc2bbe1027cd6e3414127',
 'notes/research_mixed_terminal_joint_main_budget.md': '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
 'notes/research_mixed_terminal_joint_main_common_height.md': '3c7a3ef14df887676ca8e35c1b9b37957f2e09d0945fcadc15c947f687b9fbab',
 'notes/research_mixed_terminal_joint_main_curvature_budget.md': '90b947d752c6ed646b897945ff3eb3b1beffe45074dce80087c87379e1ef04ee',
 'notes/research_mixed_terminal_joint_main_curvature_completion.md': '5e627111f330e9a190d71113e4fbf484a2f9f964b8719078870f29f9d6443343',
 'notes/research_mixed_terminal_private_left_joint_transfer.md': '41de4b6ab3197e2180bab6174fe01406d525a551ae470f964d0478e8171075ff',
 'notes/research_mixed_terminal_reserved_plane_transfer.md': '0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70',
 'notes/research_mixed_terminal_reserved_profile_completion.md': '503651546aad495cde602dde2893c49bde4b802ba442b4f4e83cf259c31cdb25',
 'repro/results/research-mixed-terminal-canonical-face-reserve.json': 'c85ef62dd25724f6bed335dc16982c2133e4f991a5badcd68e038a57b1a513aa',
 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json': '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
 'repro/results/research-mixed-terminal-joint-main-common-height.json': '53789515f1b33ffe9397c7a4405be7bcaa3db865267ad1e7da0495399c691cba',
 'repro/results/research-mixed-terminal-joint-main-curvature-budget.json': '12677b1d1b20ece4ffe61c7a370cf54b3c98233fb81f082e0220435b30a89495',
 'repro/results/research-mixed-terminal-reserved-plane-transfer.json': 'b9ce042d50911acbd5e87fa755a5b9a50393845035b3dba984c07f7e6d759ffe'}
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


def interval(value):
 assert value['finite'] is True
 lo,hi=F(value['lower_rational']),F(value['upper_rational'])
 assert lo<=hi
 return lo,hi


def inside(value,lo,hi):
 return F(lo)<value[0]<=value[1]<F(hi)


def left_face_rational_witnesses():
 x,y,z=F(2041,5000),F(5809,12500),F(341,350)
 assert x==F(13,100)*F(157,50)
 assert y==F(148,1000)*F(157,50)
 assert z==F(31,100)*F(22,7)
 assert 0<x<1 and 0<y<1 and 0<z<1
 values={
  'radius_r_exponential_lower':1+x+x*x/2+x**3/6-F(3,2),
  'new_sum_cosine_upper':F(9,10)-(1-y*y/2+y**4/24),
  'old_sum_cosine_lower':1-z*z/2+z**4/24-z**6/720-F(11,20),
  'increment_exponential_lower':1+F(2,5)+F(2,5)**2/2+F(2,5)**3/6-F(119,81)}
 expected={
  'radius_r_exponential_lower':F(2137369921,750000000000),
  'new_sum_cosine_upper':F(3538461877040639,585937500000000000),
  'old_sum_cosine_lower':F(15537434123058959,1323551250000000000),
  'increment_exponential_lower':F(218,10125)}
 assert values==expected and all(v>0 for v in values.values())
 k=F(17,25)
 exponential_upper=1+k+k*k/(2*(1-k/3))
 assert exponential_upper<2 and F(208,1000)*F(22,7)<k
 values['radius_rho_exponential_upper_gap']=2-exponential_upper
 ratio=(1+F(4,9)+F(9,5)*F(2,3))/(1+F(1,4)+F(11,20))
 assert ratio==F(119,81)
 values['squared_modulus_ratio_upper']=ratio
 return {name:str(value) for name,value in values.items()}


def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 assert not args.output.exists() and PINNED and PROOF in PINNED and ASSEMBLY in PINNED
 inputs=dict(PINNED)
 own=Path(__file__).resolve().relative_to(ROOT).as_posix()
 inputs[own]=sha(ROOT/own)
 for name,digest in inputs.items():assert sha(ROOT/name)==digest,name
 data=json.loads((ROOT/SOURCE).read_text())
 assert data['status']=='completed saved-only extraction' and data['changed_inputs']==[]
 assert data['source_path']==ORIGINAL and data['source_sha256']==inputs[ORIGINAL]
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
      'inherited_completed_terminal_label_count':27 if eps==0 else 26,
      'inherited_remaining_terminal_labels':[] if eps==0 else [['0','L']]})
 assert len(passed)==34
 assert failures==[(0,1,'four',2),(1,1,'four',2)]
 assert common_failures==[(0,1,'four',0),(0,1,'four',2),(1,1,'four',2)]
 worst,key=max(passed)
 assert key==(1,1,'four',0)
 assert min(F(1,800),F(1,250),F(1,125))==F(1,800)
 assert F(1,800)-F(1,3200)-F(1,1600)>0
 # Read only the four fixed saved records; no evaluator modules are imported.
 original,plane,curvature,common=[json.loads((ROOT/n).read_text())
     for n in (ORIGINAL,PLANE,CURVATURE,COMMON)]
 assert original['status']=='complete fixed diagnostic' and original['changed_inputs']==[]
 assert original['precision_bits']==256 and F(original['height_rational'])==F(1,100)
 for record in (plane,curvature,common):
  assert record['status']=='passed' and record['changed_inputs']==[]
  assert record['source_path']==ORIGINAL and record['source_sha256']==inputs[ORIGINAL]
  assert record['canonical_reference_cases_checked']==4
 audit_sources=(
  (plane,'experiments/check_mixed_terminal_reserved_plane_transfer.py',
   'notes/research_mixed_terminal_reserved_plane_transfer.md'),
  (curvature,'experiments/check_mixed_terminal_joint_main_curvature_budget.py',
   'notes/research_mixed_terminal_joint_main_curvature_budget.md'),
  (common,'experiments/check_mixed_terminal_joint_main_common_height.py',
   'notes/research_mixed_terminal_joint_main_common_height.md'))
 for record,checker,proof in audit_sources:
  assert record['checker_sha256']==inputs[checker]
  assert record['proof_sha256']==inputs[proof]
 for name,record in ((ORIGINAL,original),(PLANE,plane),(CURVATURE,curvature),(COMMON,common)):
  for file,digest in record['input_sha256'].items():
   assert file not in inputs or inputs[file]==digest,file
   assert sha(ROOT/file)==digest,file
   inputs[file]=digest
 assert F(plane['selected_height_rational'])==F(1,100)
 assert common['curvature_audit_path']==CURVATURE and common['curvature_audit_sha256']==inputs[CURVATURE]
 assert F(common['initial_height_rational'])==F(1,100)
 assert common['both_branches_bound_on_full_P']
 for rows in (original['cases'],plane['canonical_cases'],curvature['canonical_cases'],common['canonical_cases']):
  assert [(r['beta'],r['epsilon']) for r in rows]==expected
 witnesses=left_face_rational_witnesses()
 new_faces=[];main_bounds=[]
 for index,(row,pl,cv,ch,faces) in enumerate(zip(original['cases'],plane['canonical_cases'],curvature['canonical_cases'],common['canonical_cases'],data['canonical_cases'])):
  beta,eps=row['beta'],row['epsilon']
  for other in (pl,cv,ch,faces):
   assert (row['source_index'],row['source_case_sha256'])==(other['source_index'],other['source_case_sha256'])
  assert faces['joined_plane_upper_rational']==pl['joined_plane_upper_rational']
  assert row['status']=='both main-current bounds enclosed' and row['ordinary_label_reduction_height_verified']
  q=row['actual_coordinate_enclosures']
  for name,value in cv['coordinate_guards'].items():assert q[name]==value
  sr,ar,tr=(interval(q[n]['real']) for n in ('s','a','t'))
  hs,ha,ht=(interval(q[n]['imag']) for n in ('s','a','t'))
  assert inside(sr,'.28','.314') and inside(ar,'.28','.314') and inside(tr,'.18','.35')
  assert inside(hs,'-.102','-.001') and inside(ha,'-.108','-.001')
  assert max(map(abs,hs))<F(61,1000) and max(map(abs,ht))<F(33,500)
  v='xi' if eps==0 else 'e'
  if eps==0:
   assert inside(ht,'-.072','.021') and inside(interval(q[v]['imag']),'.049','.077')
   assert inside(interval(q[v]['real']),'.1','.4')
  else:
   assert inside(ht,'-.108','-.020') and inside(interval(q[v]['imag']),'-.051','-.019')
   assert inside(interval(q[v]['real']),'.27','.49')
  br,bh=map(F,row['outside_coordinate_rational'])
  assert (br,bh)==((F(7,20),-F(1,100)) if beta==0 else (F(3,10),-F(13,250)))
  assert F(-39,500)<=bh<=F(21,1000)
  assert [b['nu'] for b in row['branches']]==[1,0]
  fac,force=row['branches']
  As,At,Aa1,Aa0=interval(row['force_s']),interval(row['force_t']),interval(fac['force_a']),interval(force['force_a'])
  T1,T0=interval(fac['lifted_reference_value']),interval(force['lifted_reference_value'])
  assert row['force_s']==cv['force_intervals']['s'] and row['force_t']==cv['force_intervals']['t']
  assert fac['force_a']==cv['force_intervals']['a'] and fac['lifted_reference_value']==cv['factorial_trial_value']
  assert force['force_a']==ch['new_guards']['A_a0'] and force['lifted_reference_value']==ch['new_guards']['T0']
  assert q['a']['real']==ch['new_guards']['a_real']
  assert inside(As,0,'.141') and inside(At,'-.255',0)
  assert inside(Aa1,'-.255',0) and inside(Aa0,0,'.315')
  assert T1[1]<-F(463,10000) and T0[1]<-F(109,1000)
  d=F(1,2)-sr[1]
  assert d>F(93,500)
  gains={'s':15*As[1]**2/(128*d),'t':At[0]**2/3,
         'factorial_a':Aa1[0]**2/6,'forced_a':Aa0[1]*(F(9,20)-ar[0])}
  old1=T1[1]+gains['s']+gains['t']+gains['factorial_a']
  old0=T0[1]+gains['s']+gains['t']+gains['forced_a']
  assert old1==F(cv['factorial_upper_rational'])
  assert old0==F(ch['full_P_forced_upper_at_H0_rational'])
  assert old1 < -F(50063,39680000)
  assert old0 < -F(843167,39680000)
  assert old1<-F(1,800) and old0<-F(1,800)
  main_bounds.append({'beta':beta,'epsilon':eps,'factorial_upper_rational':str(old1),
    'full_P_forced_upper_at_H0_rational':str(old0),'same_height_rational':'1/100'})
  if eps==1:
   er,he=interval(q['e']['real']),interval(q['e']['imag'])
   assert inside(tr,'.304','.308') and inside(er,'.345','.347')
   assert inside(ht,'-.066','-.065') and inside(he,'-.038','-.037')
   assert At[1]<-F(23,100)
   assert At[1]+F(1,5)<0  # The proved 0<d_shift<.2 keeps the t-force negative.
   face=faces['families'][2]
   assert (face['series'],face['family'])==('four',2)
   assert face['complete_finite_coverage'] and face['null_jobs_unresolved']==[]
   U=F(face['maximum_upper_rational']);assert U<0
   new1,new0=old1+U,old0+U
   assert new1<-F(1,800) and new0<-F(1,800)
   new_faces.append({'beta':beta,'epsilon':eps,'source_index':row['source_index'],
      'source_case_sha256':row['source_case_sha256'],
      'coordinate_guards':{n:q[n] for n in ('t','e')},
      'original_t_force':row['force_t'],
      't_force_shift_strict_bounds_rational':['0','1/5'],
      'shifted_t_force_containing_bounds_rational':[str(At[0]),str(At[1]+F(1,5))],
      'bare_face_upper_for_trial_offset_rational':str(U),
      'trial_uppers_rational':{'factorial':str(T1[1]+U),'forced':str(T0[1]+U)},
      'unchanged_gain_uppers_rational':{k:str(v) for k,v in gains.items()},
      'new_face_upper_rational':{'factorial':str(new1),'full_P_forced':str(new0)},
      'strict_gap_1over800':True})
 assert len(new_faces)==2
 changed=[n for n,h in inputs.items() if sha(ROOT/n)!=h]
 assert not changed
 out={'status':'passed','source_path':SOURCE,'source_sha256':inputs[SOURCE],
      'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
      'assembly_sha256':inputs[ASSEMBLY],
      'input_sha256':inputs,'changed_inputs':changed,'same_selected_height_rational':'1/100',
      'face_cases_recombined':36,'inherited_strict_gap_1over250_cases':34,
      'previously_insufficient_case_plane_comparisons':failures,
      'previously_insufficient_common_threshold_comparisons':common_failures,
      'weakest_inherited_completed_joined_upper_rational':str(worst),'attaining_case_family':key,
      'inherited_reserve_beyond_1over250_rational':str(-worst-F(1,250)),
      'canonical_cases':summaries,'main_branch_bounds_at_H0':main_bounds,
      'left_face_rational_witnesses':witnesses,'new_private_left_face_bounds':new_faces,
      'coarse_main_upper_at_H0_rational':{'factorial':str(-F(50063,39680000)),
                                        'full_P_forced':str(-F(843167,39680000))},
      'completed_terminal_labels_per_case':[27,27,27,27],
      'complete_labeled_Fourier_comparisons':216,
      'common_raw_profile_gap_rational':'1/800',
      'complete_finite_two_factor_kernel_gap_rational':'1/1600',
      'analytic_evaluations':0,'old_record_or_source_replays':0,
      'uniform_reference_domain_claimed':False,'finite_word_realization_claimed':False,
      'whole_word_or_global_knot_theorem_claimed':False}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('x') as stream:stream.write(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':'passed','record_sha256':sha(args.output),
   'inherited_faces_checked':36,'new_left_face_cases':2,'terminal_label_counts':[27,27,27,27]}))


if __name__=='__main__':main()
