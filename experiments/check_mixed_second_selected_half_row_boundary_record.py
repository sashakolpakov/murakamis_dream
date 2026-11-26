#!/usr/bin/env python3
"""Independent exact audit of the saved half-row boundary pass.

Only stdlib rational operations on saved enclosures are used. There is no
root, source, primitive, transcendental or interval-provider evaluation.
"""
import argparse, hashlib, json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE='repro/results/research-mixed-second-selected-half-row-boundary-attempt01.json'
BANK='repro/results/research-mixed-second-selected-boundary-reference-bank.json'
PINNED={SOURCE:'4911ec98e375e034fa1830a35f710635b9afc8944352faf58a5cc598f062aaba',BANK:'3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb'}
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
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();assert not args.output.exists()
 for name,digest in PINNED.items():assert sha(ROOT/name)==digest,name
 data=json.loads((ROOT/SOURCE).read_text());bank=json.loads((ROOT/BANK).read_text())
 assert data['status']=='complete saved-reference pass' and data['alpha']==1 and data['beta']==0 and data['precision_bits']==256
 assert data['complete_reference_inventory'] and data['complete_boundary_evaluation'] and data['uniform_half_row_gap_proved'] and data['common_gap_1_over_3200_proved']
 for k in ['pending_bank_reference_indices','unresolved_bank_reference_indices','changed_inputs','unexpected_errors','stop_signals']:assert not data[k],k
 for k in ['source_root_evaluations','new_reference_derivative_evaluations','parameter_subdivisions','full_source_theorem_claimed','global_filling_volume_theorem_claimed']:assert not data[k],k
 assert data['reference_bank']==BANK and data['reference_bank_sha256']==PINNED[BANK]
 assert len(data['input_sha256'])==88
 for name,digest in data['input_sha256'].items():
  path=Path(name);assert sha(path if path.is_absolute() else ROOT/path)==digest,name
 selected={i:r for i,r in enumerate(bank['accepted_references']) if r['beta']==0}
 geometry=[r for r in bank['terminal_geometry'] if r['beta']==0]
 assert len(selected)==785 and len(geometry)==843 and data['terminal_geometry']==geometry
 cases=defaultdict(list);seen=set();exc=0
 for g in geometry:
  cases[g['chart']].append(g['address'])
  if g['status']=='excluded':exc+=1;assert F(g['source_exclusion']['strict_margin_rational'])>0
  else:
   i=g['accepted_reference_index'];assert i in selected and i not in seen;seen.add(i);r=selected[i]
   for k in ['source_node_index','chart','address','parameter_interval','external_coordinate_box','source_node_canonical_sha256']:assert g[k]==r[k]
 assert exc==58 and len(cases)==9 and seen==set(selected)
 for aa in cases.values():
  ss=sorted(aa);assert len(ss)==len(set(ss)) and all(not b.startswith(a) for a,b in zip(ss,ss[1:]))
  assert sum((F(1,2**len(a)) for a in ss),F())==1
 rows=data['rows'];assert len(rows)==785;visited=set();groups=defaultdict(list);bounds_checked=0
 for j,row in enumerate(rows):
  i=row['bank_reference_index'];assert i in selected and i not in visited;visited.add(i);r=selected[i]
  for k in ['source_node_index','chart','address','external_domain','compact_payload_canonical_sha256']:assert row[k]==r[k]
  payload=dict(r);ph=payload.pop('compact_payload_canonical_sha256');assert canon(payload)==ph
  assert row['status']=='finite bound' and F(row['boundary_response_upper_rational'])==F(r['response']['B_upper_rational'])
  s=row['scalar'];q=s['details'];assert s['alpha']==1 and s['beta']==0 and s['precision_bits']==256 and s['fully_evaluated_pair'] and s['both_branches_use_full_plateau']
  assert s['status']=='accepted' and not s['additional_reference_calls'] and not s['additional_source_calls']
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
  left=iv(q['left_index_gain']['value'])[1];out=quadratic(q['outgoing_gain'],Db,coords['b'][0],F(57,10));uppers=[]
  for label,nu in [('forced',0),('factorial',1)]:
   b=q['branches'][label];assert b['nu']==nu and tuple(map(F,b['selected_target_interval']))==P
   force=iv(b['P_nu']);inside(sub(add(logs['L1'],logs['Lplus']),scale(logs['Lminus'],2+nu)),force,f'P {j} {nu}')
   trial=iv(b['T_nu']);inside(sub(sub(savedcommon[0],scale(gg['zH'][0],nu)),scale(pi,2*nu*H)),trial,f'T {j} {nu}')
   sel=quadratic(b['selected_gain'],force,coords['z'][0],F(32,5) if nu==0 else F(69,10))
   components={'trial':trial[1],'left':left,'selected':sel,'outgoing':out}
   assert {k:F(v) for k,v in b['component_upper_rationals'].items()}==components
   upper=sum(components.values(),F());assert iv(b['budget'])==(upper,upper) and upper<0 and b['strictly_below_zero'];uppers.append(upper);bounds_checked+=1
  gap=-max(uppers);assert F(row['boundary_gap_lower_rational'])==gap==F(s['proved_margin_lower_rational'])
  groups[row['external_domain']].append((gap,F(row['boundary_response_upper_rational'])))
  calls=row['counts'];assert calls['half_row_reference_attempts']==calls['node_conjugates']==1 and calls['half_row_branch_attempts']==2 and calls['centered_primitive_calls']==11
 assert visited==set(selected) and bounds_checked==1570
 summaries=[]
 for row in data['domain_summaries']:
  k=row['domain'];group=groups[k];assert len(group)==(388 if k=='k3' else 397)
  gamma=min(x[0] for x in group);B=max(x[1] for x in group);factor=F(6889,2000000) if k=='k3' else F(9,5000);gap=gamma-factor*B
  assert F(row['observed_boundary_gap_lower_rational'])==gamma and F(row['saved_response_upper_rational'])==B and F(row['barrier_factor_rational'])==factor and F(row['compensated_gap_rational'])==gap
  assert gap>F(1,20) and row['valid_positive_whole_domain_gap'] and row['strictly_above_common_gap_1_over_3200']
  coarse_gamma,coarse_B=(F(68,1000),F(1645,1000)) if k=='k3' else (F(77,1000),F(2055,1000))
  coarse_gap=coarse_gamma-factor*coarse_B
  assert gamma>coarse_gamma and B<coarse_B and coarse_gap>F(1,20)
  summaries.append({'domain':k,'reference_count':len(group),'gamma_min_rational':str(gamma),'B_max_rational':str(B),'barrier_factor_rational':str(factor),'corrected_gap_rational':str(gap),'corrected_gap_decimal_display':float(gap),'strictly_above_1_over_20':True,'conservative_gamma_lower_rational':str(coarse_gamma),'conservative_B_upper_rational':str(coarse_B),'conservative_corrected_gap_rational':str(coarse_gap)})
 result={'status':'independent exact half-row saved-data audit passed','source':SOURCE,'source_sha256':PINNED[SOURCE],'reference_bank':BANK,'reference_bank_sha256':PINNED[BANK],
 'checker_sha256':sha(Path(__file__)),'source_bindings_checked':88,'complete_chart_cases':9,'terminal_leaves':843,'accepted_reference_cells':785,'strict_geometry_exclusions':58,'branch_upper_bounds_checked':1570,
 'all_bank_input_boxes_contained_in_evaluated_boxes':True,'all_saved_force_trial_and_argument_recombinations_checked':True,'all_quadratic_sides_clips_minima_and_component_sums_checked':True,
 'separate_global_gamma_and_B_aggregation_checked':True,'domain_summaries':summaries,'uniform_half_row_gap_strict_lower_rational':'1/20',
 'source_root_primitive_transcendental_or_interval_provider_evaluations':0,'scope':'half-row boundary and corrected domain comparison only; no full-source or filling assembly asserted'}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'gaps':[(r['domain'],r['corrected_gap_decimal_display']) for r in summaries],'output_sha256':sha(args.output)}))
if __name__=='__main__':main()
