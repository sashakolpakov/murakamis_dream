#!/usr/bin/env python3
"""Exact saved-data audit of the new alpha-zero half-row boundary pass.

Only stdlib rational operations on saved enclosures are used. There is no
root, source, primitive, transcendental or interval-provider evaluation.
"""
import argparse, gzip, hashlib, json
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE='repro/results/research-mixed-second-selected-first-three-half-row-boundary-attempt01.json.gz'
BANK='repro/results/research-mixed-second-selected-first-three-boundary-reference-bank.json.gz'
CENTRAL_AUDIT='repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json'
DRIVER='experiments/certify_mixed_second_selected_first_three_half_row_boundary.py'
PINNED={
 SOURCE:'9cce79a1199aa10e32ee0642dc150e2f94e97d85831c8daea75edcc458db553f',
 BANK:'4b0bfa3cb2bfb68b622487c390879312b7d0832a056f03c3675a38cedeb8c323',
 DRIVER:'f74c1d2892abd60b7a1f059819e00aebff5684cfd5675249f1ef40434ecd4f27',
 CENTRAL_AUDIT:'88d8f8177a439f4268980e7467fffc576b558776c22f2a6067361d0ab8b6a047',
 'experiments/check_mixed_second_selected_half_row_boundary_record.py':
  'c554713b8a93ba435b345d0f9b0fa92a9c39ffabaae14466f0ea17c5a6c4320e',
 'experiments/evaluate_mixed_second_selected_first_three_half_row_budget.py':
  'b40de9e7c5b215ada0213010a0fe0569ca86a6c1e16277257b8c76750315e059',
 'notes/research_mixed_second_selected_first_three_extension.md':
  'd488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2',
}
# Final result identity and counts must be frozen after its sole prescribed run.
EXPECTED_COUNTS={'accepted':782,'terminal_geometry':840,
 'geometry_excluded':58,'reference_excluded':0,'accepted_k3':387,'accepted_k4':395}
EXPECTED_SOURCE_BINDINGS=73
# Optional human-readable strict bounds are frozen only from the saved result.
CONSERVATIVE_TABLE={'k3':('73/1000','1637/1000'),'k4':('41/500','41/20')}
CHOSEN_COMMON_GAP='1/20'
CHARTS=frozenset(('k3_circle_right','k3_circle_left','k3_lower_chord',
 'k3_upper_chord','k3_oblique_chord','k4_circle_right','k4_circle_left',
 'k4_lower_chord','k4_upper_chord'))

P=(F(11,50),F(9,20));H=F(1,100)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(2**20),b''):h.update(x)
 return h.hexdigest()
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def iv(x):
 assert x.get('finite') is True
 lo,hi=F(x['lower_rational']),F(x['upper_rational']);assert lo<=hi
 return lo,hi
def cv(x):return iv(x['real']),iv(x['imag'])
def pt(x):return F(x),F(x)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def scale(a,n):return mul(a,pt(n))
def cadd(a,b):return add(a[0],b[0]),add(a[1],b[1])
def cneg(a):return neg(a[0]),neg(a[1])
def csub(a,b):return cadd(a,cneg(b))
def cmul(a,b):return sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))
def cscale(a,n):return scale(a[0],n),scale(a[1],n)
def inside(a,b,label):
 assert b[0]<=a[0]<=a[1]<=b[1],label

def cin(a,b,label):
 inside(a[0],b[0],label+' real');inside(a[1],b[1],label+' imag')
def quadratic(r,force,center,mu):
 assert tuple(map(F,r['force_interval']))==force and tuple(map(F,r['center_interval']))==center
 assert tuple(map(F,r['target_interval']))==P and F(r['curvature_lower_rational'])==mu
 vals=[]
 for label,p,l in [('negative',max(F(0),-force[0]),center[1]-P[0]),('positive',max(F(0),force[1]),P[1]-center[0])]:
  assert l>=0;t=min(l,p/mu);v=p*t-mu*t*t/2;row=r['sides'][label]
  assert F(row['nonnegative_force_upper_rational'])==p and F(row['displacement_length_upper_rational'])==l
  assert F(row['clipped_displacement_rational'])==t and F(row['gain_upper_rational'])==v;vals.append(v)
 clip=max(vals);free=max(force[0]**2,force[1]**2)/(2*mu);upper=min(clip,free)
 assert F(r['clipped_upper_rational'])==clip and F(r['unrestricted_upper_rational'])==free and F(r['upper_rational'])==upper
 assert r['selected_method']==('clipped' if clip<=free else 'unrestricted')
 return upper

def main():
 if (any(digest is None for digest in PINNED.values()) or EXPECTED_COUNTS is None
     or EXPECTED_SOURCE_BINDINGS is None):
  raise RuntimeError('checker not frozen: saved result identities/counts are pending')
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();assert not args.output.exists()
 for name,digest in PINNED.items():assert sha(ROOT/name)==digest,name
 with gzip.open(ROOT/SOURCE,'rt',encoding='utf-8') as stream:data=json.load(stream)
 with gzip.open(ROOT/BANK,'rt',encoding='utf-8') as stream:bank=json.load(stream)
 central=json.loads((ROOT/CENTRAL_AUDIT).read_text())
 assert central['status']=='exact saved-data check passed' and central['alpha']==0 and central['complete_chart_cases']==18
 central_groups={(r['beta'],r['domain']):r for r in central['domain_summaries']}
 assert len(central_groups)==len(central['domain_summaries'])==4
 assert all(F(r['corrected_gap_rational'])>0 for r in central_groups.values())
 assert data['status']=='complete saved-reference pass' and data['alpha']==0 and data['beta']==0 and data['precision_bits']==256
 assert data['complete_reference_inventory'] and data['complete_boundary_evaluation']
 assert data['alpha_one_reference_data_used'] is False
 for k in ['pending_bank_reference_indices','unresolved_bank_reference_indices','changed_inputs','unexpected_errors','stop_signals']:assert not data[k],k
 for k in ['source_root_evaluations','new_reference_derivative_evaluations','parameter_subdivisions','full_source_theorem_claimed','global_filling_volume_theorem_claimed']:assert not data[k],k
 assert data['reference_bank']==BANK and data['reference_bank_sha256']==PINNED[BANK]
 assert data['saved_central_audit']==CENTRAL_AUDIT and data['saved_central_audit_sha256']==PINNED[CENTRAL_AUDIT]
 assert data['saved_central_source']==central['source'] and data['saved_central_source_sha256']==central['source_sha256']
 assert bank['schema']=='mixed-second-selected-first-three-certified-boundary-references-v1'
 assert bank['alpha']==0 and bank['beta_cases']==[0,1] and bank['precision_bits']==256
 assert not bank['pending_frontier'] and not bank['unresolved_frontier'] and bank['alpha_one_reference_data_used'] is False
 assert bank['saved_data_audit']==CENTRAL_AUDIT and bank['saved_data_audit_sha256']==PINNED[CENTRAL_AUDIT]
 assert bank['source']==central['source'] and bank['source_sha256']==central['source_sha256']
 assert len(data['input_sha256'])==EXPECTED_SOURCE_BINDINGS
 assert data['input_sha256'][DRIVER]==PINNED[DRIVER]
 for name,digest in data['input_sha256'].items():
  path=Path(name);assert sha(path if path.is_absolute() else ROOT/path)==digest,name
 for name,digest in bank['input_sha256'].items():assert data['input_sha256'][name]==digest,name
 selected={i:r for i,r in enumerate(bank['accepted_references']) if r['beta']==0}
 geometry=[r for r in bank['terminal_geometry'] if r['beta']==0]
 observed={'accepted':len(selected),'terminal_geometry':len(geometry),
  'geometry_excluded':sum(r['status']=='excluded' for r in geometry),
  'reference_excluded':sum(r['status']=='excluded by certified reference domain' for r in geometry),
  'accepted_k3':sum(r['external_domain']=='k3' for r in selected.values()),
  'accepted_k4':sum(r['external_domain']=='k4' for r in selected.values())}
 assert observed==EXPECTED_COUNTS==data['expected_reference_inventory']==data['observed_reference_inventory']
 assert data['terminal_geometry']==geometry and data['boundary_chart_count']==9
 assert data['inherited_geometric_exclusions']==observed['geometry_excluded']
 assert data['inherited_certified_reference_exclusions']==observed['reference_excluded']
 cases=defaultdict(list);seen=set();source_nodes=set();exc=0;reference_exc=0
 for g in geometry:
  assert g['alpha']==0 and g['beta']==0 and g['chart'] in CHARTS and g['external_domain']==g['chart'][:2]
  assert g['source_node_index'] not in source_nodes;source_nodes.add(g['source_node_index'])
  cases[g['chart']].append(g['address'])
  if g['status']=='excluded':exc+=1;assert F(g['source_exclusion']['strict_margin_rational'])>0
  elif g['status']=='excluded by certified reference domain':
   reference_exc+=1;assert g['certified_reference_exclusion']['status']=='excluded'
   assert g['certified_reference_exclusion']['alpha']==0
  else:
   assert g['status']=='accepted boundary estimate'
   i=g['accepted_reference_index'];assert i in selected and i not in seen;seen.add(i);r=selected[i]
   for k in ['alpha','beta','source_node_index','chart','address','external_domain','parameter_interval','external_coordinate_box','source_node_canonical_sha256']:assert g[k]==r[k]
 assert exc==observed['geometry_excluded'] and reference_exc==observed['reference_excluded'] and set(cases)==CHARTS and seen==set(selected)
 assert len(bank['coverage']['cases'])==18
 assert {(c['beta'],c['chart']) for c in bank['coverage']['cases']}=={(beta,chart) for beta in (0,1) for chart in CHARTS}
 for aa in cases.values():
  assert all(isinstance(a,str) and not set(a)-set('01') for a in aa)
  ss=sorted(aa);assert len(ss)==len(set(ss)) and all(not b.startswith(a) for a,b in zip(ss,ss[1:]))
  assert sum((F(1,2**len(a)) for a in ss),F())==1
 rows=data['rows'];assert len(rows)==observed['accepted'];visited=set();groups=defaultdict(list);bounds_checked=0;counts=Counter()
 assert [r['bank_reference_index'] for r in rows]==list(selected)
 for j,row in enumerate(rows):
  i=row['bank_reference_index'];assert i in selected and i not in visited;visited.add(i);r=selected[i]
  assert row['alpha']==r['alpha']==0 and row['beta']==r['beta']==0
  for k in ['source_node_index','chart','address','external_domain','compact_payload_canonical_sha256']:assert row[k]==r[k]
  payload=dict(r);ph=payload.pop('compact_payload_canonical_sha256');assert canon(payload)==ph
  assert r['response']['alpha']==0 and r['response']['beta']==0 and r['response']['status']=='enclosed'
  assert r['response']['height_conditions_verified'] and r['response']['common_prefix_product_verified']
  rb=iv(r['response']['B']);assert rb[0]>=0 and rb[1]==F(r['response']['B_upper_rational'])
  assert row['status']=='finite bound' and F(row['boundary_response_upper_rational'])==rb[1]
  s=row['scalar'];q=s['details'];assert s['alpha']==0 and s['beta']==0 and s['precision_bits']==256 and s['fully_evaluated_pair'] and s['both_branches_use_full_plateau']
  assert not s['additional_reference_calls'] and not s['additional_source_calls']
  adapter=s['alpha_adapter'];assert adapter['frozen_reported_alpha']==1 and adapter['frozen_helper_calls']==1
  assert adapter['arithmetic_details_and_status_unchanged'] is True
  assert adapter['remove_for_original_result']==['alpha_adapter'] and adapter['restore_original_metadata']['alpha']==1
  original=dict(s);del original['alpha_adapter'];original.update(adapter['restore_original_metadata'])
  assert canon(original)==adapter['frozen_result_canonical_sha256']
  assert original['alpha']==1 and original['details']==q and original['status']==s['status']
  assert adapter['reference_existence_and_stationarity_are_caller_premises'] is True
  for k in ['additional_primitive_calls','additional_conjugate_calls','additional_reference_calls','additional_response_calls']:assert adapter[k]==0
  for name,digest in adapter['input_sha256'].items():assert data['input_sha256'][name]==digest,name
  assert F(s['height_rational'])==H and set(q['branches'])=={'forced','factorial'}
  coords={k:cv(v) for k,v in q['coordinates'].items()};shapes={k:cv(v) for k,v in q['negative_shapes'].items()}
  assert set(coords)=={'a','u','z','v','b'} and set(shapes)=={'u','z','v','b'}
  for k,v in coords.items():cin(cv(r['coordinates'][k]),v,f'bank coordinate {j} {k}')
  for k,v in shapes.items():cin(cv(r['negative_shapes'][k]),v,f'bank shape {j} {k}')
  assert all(x['whole_box_contained'] for x in q['coordinate_checks'].values())
  pi=iv(q['pi']);assert F(157,50)<pi[0]<=pi[1]<F(22,7)
  lam=iv(q['radial_multiplier']);assert lam[0]>0
  logs={k:iv(v['value']) for k,v in q['logarithms'].items()};one=(pt(1),pt(0));lz=(mul(lam,shapes['z'][0]),mul(lam,shapes['z'][1]))
  logargs={'L1':csub(one,cmul(shapes['u'],lz)),'L0':csub(one,cmul(shapes['u'],shapes['z'])),'Lplus':cadd(one,lz),'Lminus':csub(one,lz),'Lb':cadd(one,shapes['b']),'Lvb':csub(one,cmul(shapes['v'],shapes['b']))}
  # Direct expressions are checked as rectangular recombinations of saved inputs.
  for k,v in logargs.items():cin(v,cv(q['logarithms'][k]['argument']),f'log argument {j} {k}')
  A,Db=iv(q['common_forces']['A']),iv(q['common_forces']['D_b']);assert A[0]>0
  inside(sub(logs['L1'],logs['L0']),A,f'A {j}');inside(sub(logs['Lb'],logs['Lvb']),Db,f'Db {j}')
  # Original bank boxes are the certified input sets. Re-serialized live
  # ball endpoints can add a final outward ulp; do not treat that extra
  # endpoint padding as a new mathematical argument domain.
  actual={k:cv(r['coordinates'][k]) for k in coords}
  zH=(actual['z'][0],pt(H));half=(pt(F(1,2)),pt(0))
  gargs={'u_plus_zH':cadd(actual['u'],zH),'u_plus_z':cadd(actual['u'],actual['z']),'half_plus_zH':cadd(half,zH),'v_plus_z':cadd(actual['v'],actual['z']),'half_plus_b':cadd(half,actual['b']),'v_plus_b':cadd(actual['v'],actual['b']),'v':actual['v'],'z':actual['z'],'zH':zH}
  for k,v in gargs.items():cin(v,cv(q['primitive_values'][k]['argument']),f'g argument {j} {k}')
  gg={k:cv(v['value']) for k,v in q['primitive_values'].items()}
  gh=cv(q['trial']['g_half']);cin((pt(0),scale(pi,F(1,8))),gh,f'g half {j}')
  chirp=cv(q['trial']['original_chirp']);x=csub(cscale(zH,F(1,2)),cmul(actual['z'],actual['v']));ch=(neg(mul(scale(pi,2),x[1])),mul(scale(pi,2),x[0]))
  cin(ch,chirp,f'chirp {j}')
  common=cadd(csub(cadd(csub(gg['u_plus_zH'],gg['u_plus_z']),csub(gg['half_plus_zH'],gg['v_plus_z'])),cscale(csub(gh,gg['v']),2)),cadd(csub(gg['half_plus_b'],gg['v_plus_b']),cadd(csub(cscale(gg['z'],3),cscale(gg['zH'],2)),chirp)))
  savedcommon=cv(q['trial']['common_complex_trial_before_nu']);cin(common,savedcommon,f'common trial {j}')
  left_record=q['left_index_gain']
  assert iv(left_record['force'])==A and iv(left_record['center'])==coords['u'][0] and iv(left_record['height'])==coords['u'][1]
  assert F(left_record['coefficient'])==1 and tuple(map(F,left_record['target_interval']))==(P[0],F(1,2))
  assert iv(left_record['value'])==iv(left_record['candidate_value'])
  left=iv(left_record['value'])[1];out=quadratic(q['outgoing_gain'],Db,coords['b'][0],F(57,10));uppers=[]
  for label,nu in [('forced',0),('factorial',1)]:
   b=q['branches'][label];assert b['nu']==nu and tuple(map(F,b['selected_target_interval']))==P
   force=iv(b['P_nu']);inside(sub(add(logs['L1'],logs['Lplus']),scale(logs['Lminus'],2+nu)),force,f'P {j} {nu}')
   trial=iv(b['T_nu']);inside(sub(sub(savedcommon[0],scale(gg['zH'][0],nu)),scale(pi,2*nu*H)),trial,f'T {j} {nu}')
   sel=quadratic(b['selected_gain'],force,coords['z'][0],F(32,5) if nu==0 else F(69,10))
   components={'trial':trial[1],'left':left,'selected':sel,'outgoing':out}
   assert {k:F(v) for k,v in b['component_upper_rationals'].items()}==components
   upper=sum(components.values(),F());assert iv(b['budget'])==(upper,upper) and b['strictly_below_zero']==(upper<0)
   assert b['strictly_below_candidate_gap']==(upper < -F(s['candidate_gap']))
   uppers.append(upper);bounds_checked+=1
  gap=-max(uppers);assert F(row['boundary_gap_lower_rational'])==gap
  assert s['status']==('accepted' if gap>0 else 'inconclusive')
  assert s['proved_margin_lower_rational']==(str(gap) if gap>0 else None)
  groups[row['external_domain']].append((gap,F(row['boundary_response_upper_rational'])))
  calls=row['counts'];counts.update(calls)
  assert calls['half_row_reference_attempts']==calls['node_conjugates']==1 and calls['half_row_branch_attempts']==2 and calls['centered_primitive_calls']==11
  assert calls['half_row_direct_primitive_calls']==9 and calls['half_row_direct_log_abs_calls']==6
 assert visited==set(selected) and bounds_checked==2*observed['accepted'] and dict(counts)==data['counts']
 summaries=[];summary_keys=set()
 for row in data['domain_summaries']:
  k=row['domain'];assert k in ('k3','k4') and k not in summary_keys;summary_keys.add(k)
  assert row['alpha']==0 and row['beta']==0
  group=groups[k];assert len(group)==observed['accepted_'+k]==row['finite_bound_cells']
  gamma=min(x[0] for x in group);B=max(x[1] for x in group);factor=F(6889,2000000) if k=='k3' else F(9,5000);gap=gamma-factor*B
  assert B==F(central_groups[(0,k)]['B_max_rational'])
  assert F(row['observed_boundary_gap_lower_rational'])==gamma and F(row['saved_response_upper_rational'])==B and F(row['barrier_factor_rational'])==factor and F(row['compensated_gap_rational'])==gap
  assert row['valid_positive_whole_domain_gap']==(gap>0)
  assert row['strictly_above_candidate_gap_1_over_3200']==(gap>F(1,3200))
  summary={'alpha':0,'beta':0,'domain':k,'reference_count':len(group),'gamma_min_rational':str(gamma),'B_max_rational':str(B),'barrier_factor_rational':str(factor),'corrected_gap_rational':str(gap),'corrected_gap_decimal_display':float(gap)}
  lower=gap
  if CONSERVATIVE_TABLE is not None:
   coarse_gamma,coarse_B=map(F,CONSERVATIVE_TABLE[k]);coarse_gap=coarse_gamma-factor*coarse_B
   assert gamma>coarse_gamma and B<coarse_B
   summary.update({'conservative_gamma_lower_rational':str(coarse_gamma),'conservative_B_upper_rational':str(coarse_B),'conservative_corrected_gap_rational':str(coarse_gap)})
   lower=coarse_gap
  if CHOSEN_COMMON_GAP is not None:
   assert 0<F(CHOSEN_COMMON_GAP)<lower
   summary['strictly_above_chosen_common_gap']=True
  summaries.append(summary)
 assert summary_keys=={'k3','k4'}
 if CONSERVATIVE_TABLE is not None:assert set(CONSERVATIVE_TABLE)==summary_keys
 minimum=min(F(r['corrected_gap_rational']) for r in summaries)
 assert F(data['candidate_gap_rational'])==F(1,3200)
 assert data['uniform_half_row_gap_proved']==(minimum>0)
 assert data['candidate_gap_1_over_3200_proved']==(minimum>F(1,3200))
 for name,digest in data['input_sha256'].items():
  path=Path(name);assert sha(path if path.is_absolute() else ROOT/path)==digest,name
 for name,digest in PINNED.items():assert sha(ROOT/name)==digest,name
 result={'status':'independent exact half-row saved-data audit passed','alpha':0,'beta':0,
 'source':SOURCE,'source_sha256':PINNED[SOURCE],'reference_bank':BANK,'reference_bank_sha256':PINNED[BANK],
 'central_audit':CENTRAL_AUDIT,'central_audit_sha256':PINNED[CENTRAL_AUDIT],
 'checker_sha256':sha(Path(__file__)),'source_bindings_checked':EXPECTED_SOURCE_BINDINGS,'complete_chart_cases':9,
 'terminal_leaves':observed['terminal_geometry'],'accepted_reference_cells':observed['accepted'],
 'strict_geometry_exclusions':observed['geometry_excluded'],'certified_reference_exclusions':observed['reference_excluded'],
 'branch_upper_bounds_checked':bounds_checked,'all_alpha_zero_metadata_and_legacy_payload_restoration_checked':True,
 'all_bank_input_boxes_contained_in_evaluated_boxes':True,'all_saved_force_trial_and_argument_recombinations_checked':True,
 'all_quadratic_sides_clips_minima_and_component_sums_checked':True,
 'separate_global_gamma_and_B_aggregation_checked':True,'unchanged_central_response_extrema_checked':True,
 'domain_summaries':summaries,'exact_minimum_corrected_gap_rational':str(minimum),
 'uniform_positive_half_row_gap_proved':minimum>0,
 'chosen_common_gap_rational':None if CHOSEN_COMMON_GAP is None else str(F(CHOSEN_COMMON_GAP)),
 'input_sha256':dict(PINNED),'counts':dict(counts),
 'source_root_primitive_transcendental_or_interval_provider_evaluations':0,
 'scope':'alpha0 beta0 half-row boundary and corrected domain comparison only; no full-source or filling assembly asserted'}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'gaps':[(r['domain'],r['corrected_gap_decimal_display']) for r in summaries],'output_sha256':sha(args.output)}))
if __name__=='__main__':main()
