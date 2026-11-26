"""Independent stdlib-only audit of one completed external-boundary record."""
import argparse, hashlib, json
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
ROOT=Path('/Users/sasha/volume-conjecture')
SOURCE='repro/results/research-mixed-second-selected-external-boundary-attempt01.json'
EXPECTED='2b720b596209b1c2f86f2a40d6cc4e946b3470e3e905a609a54bfe42ffbff5d7'
D={3:(F('0.35'),F('-.01'),F('.083'),F('-.072'),F('.068')),
   4:(F('.30'),F('-.052'),F('.060'),F('-.108'),F('-.001'))}
CHARTS=['k3_circle_right','k3_circle_left','k3_lower_chord','k3_upper_chord','k3_oblique_chord',
        'k4_circle_right','k4_circle_left','k4_lower_chord','k4_upper_chord']
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(2**20),b''):h.update(b)
 return h.hexdigest()
def iv(r):
 assert r.get('finite') is True
 lo,hi=F(r['lower_rational']),F(r['upper_rational']);assert lo<=hi
 return lo,hi
def cv(r):return (*iv(r['real']),*iv(r['imag']))
def box(addr):
 assert set(addr)<=set('01')
 lo,hi=F(-1),F(1)
 for t in addr:
  mid=(lo+hi)/2
  if t=='0':hi=mid
  else:lo=mid
 return lo,hi
def line(chart):
 k=int(chart[1]);x,y,r,bot,top=D[k]
 if chart.endswith('lower_chord'):return x,bot,r,F(0)
 if chart.endswith('upper_chord'):return x,top,r,F(0)
 assert chart=='k3_oblique_chord';return F(301,500),F(-1,500),F(21,100),F(7,100)
def image(chart,l,h):
 k=int(chart[1]);x,y,r,_,_=D[k]
 if 'circle' in chart:
  near=F(0) if l<=0<=h else min(abs(l),abs(h));far=max(abs(l),abs(h))
  rr=[(1-far**2)/(1+far**2),(1-near**2)/(1+near**2)]
  ii=[2*l/(1+l*l),2*h/(1+h*h)];sign=1 if chart.endswith('right') else -1
  xx=[x+sign*r*t for t in rr]; yy=[y+sign*r*t for t in ii]
 else:
  a,b,dx,dy=line(chart);xx=[a+dx*l,a+dx*h];yy=[b+dy*l,b+dy*h]
 return min(xx),max(xx),min(yy),max(yy)
def exclusion(chart,l,h,z,w):
 k=int(chart[1]);x,y,r,bot,top=D[k];xl,xh,yl,yh=z
 criterion=w['criterion']; margin=F(w['strict_margin_rational'])
 assert margin>0 and w['chart']==chart and w['domain']=='k'+str(k)
 assert tuple(map(F,w['parameter_interval']))==(l,h)
 assert tuple(map(F,w['coordinate_box']))==z
 if criterion=='below_lower_height':assert margin==bot-yh
 elif criterion=='above_upper_height':assert margin==yl-top
 elif criterion=='above_oblique_halfplane':
  assert k==3
  if 'circle' in chart:lower=xl-3*yh
  else:
   a,b,dx,dy=line(chart);lower=min(a-3*b+(dx-3*dy)*l,a-3*b+(dx-3*dy)*h)
  assert margin==lower-F(76,125)
 elif criterion=='outside_typed_disk':
  assert 'circle' not in chart
  a,b,dx,dy=line(chart);a-=x;b-=y
  t=max(l,min(h,-(a*dx+b*dy)/(dx*dx+dy*dy)))
  assert margin==(a+dx*t)**2+(b+dy*t)**2-r*r
 else:raise AssertionError(criterion)
def minbound(r):
 vals=[F(x['upper_rational']) for x in r['candidates']]
 j=min(range(len(vals)),key=vals.__getitem__)
 assert r['selected_candidate_index']==j and F(r['upper_rational'])==vals[j]
 return vals[j]
def scalarcheck(s,coords,shapes,beta):
 assert s['beta']==beta and s['fully_evaluated_pair'] and s['frozen_helper_calls']==1
 det=s['details']; old=det['frozen_result']; assert old['beta']==beta
 for name in ('u','z','v'):assert det['input_enclosures']['coordinates'][name]==coords[name]
 assert det['input_enclosures']['negative_shapes']['v']==shapes['v']
 assert s['additional_primitive_calls']==s['additional_conjugate_calls']==s['additional_reference_calls']==0
 components=det['component_bounds']; left,right,vert=[minbound(components[x]) for x in ('left','right','vertical')]
 original=old['details']; pi_lo,pi_hi=iv(det['input_enclosures']['pi']); assert F(157,50)<pi_lo<=pi_hi<F(22,7)
 assert iv(original['scalars']['A'])[0]>0 and iv(original['scalars']['d'])[0]>0
 for label,nu in [('forced',0),('factorial',1)]:
  r=det['branches'][label];o=original['branches'][label]; assert r['nu']==nu and r['selected_gain_keeps_its_sign']
  sel,trial=minbound(r['selected_bound']),minbound(r['trial_bound'])
  final=minbound(r['final_bound']);assert final==min(iv(o['budget'])[1],trial+left+right+sel)
  assert iv(r['budget'])==(final,final) and final<0 and r['strictly_below_zero']
  assert F(r['trial_bound']['candidates'][1]['upper_rational'])==vert+(iv(original['scalars']['g_zH_real'])[1] if nu==0 else -pi_lo/50)
 assert F(s['proved_margin_lower_rational'])==min(-iv(r['budget'])[1] for r in det['branches'].values())
 return max(iv(det['branches'][x]['budget'])[1] for x in ('forced','factorial')),max(iv(original['branches'][x]['budget'])[1]-iv(original['branches'][x]['budget'])[0] for x in ('forced','factorial'))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();assert not args.output.exists()
 p=ROOT/SOURCE;assert sha(p)==EXPECTED
 data=json.loads(p.read_text());assert data['status']=='complete boundary coverage'
 assert data['alpha']==1 and data['beta_cases']==[0,1] and data['boundary_case_count']==18
 assert data['coverage_verified'] and data['complete_boundary_coverage'] and data['uniform_central_gap_proved']
 assert not data['pending_frontier_next_is_first'] and not data['unresolved_leaves'] and not data['changed_inputs'] and not data['stop_signals_received']
 assert not any(data[k] for k in ['half_row_bound_claimed','full_source_theorem_claimed','global_filling_volume_theorem_claimed'])
 assert len(data['input_sha256'])==76
 for name,digest in data['input_sha256'].items():
  path=Path(name);path=path if path.is_absolute() else ROOT/path
  assert sha(path)==digest,name
 nodes=data['nodes'];leaves=data['terminal_leaves'];assert len(nodes)==3072 and len(leaves)==1545
 index={};buckets=defaultdict(list);accepted=defaultdict(list);counts=Counter()
 for i,n in enumerate(nodes):
  key=(n['beta'],n['chart'],n['address']);assert key not in index and key[0] in(0,1) and key[1] in CHARTS
  index[key]=i;l,h=box(key[2]);z=image(key[1],l,h)
  assert tuple(map(F,n['parameter_interval']))==(l,h) and tuple(map(F,n['external_coordinate_box']))==z
  action=n['action'];counts[action]+=1
  if action=='split':assert n['children']==[key[2]+'0',key[2]+'1']
  elif action=='excluded':exclusion(key[1],l,h,z,n['source_exclusion'])
  else:
   assert action=='accepted boundary estimate'
   ref=n['reference'];assert ref['status']=='enclosed';rd=ref['details'];assert rd['status']=='enclosed' and rd['beta']==key[0]
   coords=rd['actual_coordinate_enclosures']; shapes=rd['negative_shapes']
   response=n['response'];assert response['status']=='enclosed' and response['height_conditions_verified'] and response['common_prefix_product_verified']
   assert response['details']['coordinates']==coords
   assert response['details']['qprime']==rd['response_verification']['derivative_enclosures']
   for name in ('e','xi','a','u','z','v','b'):
    a,b,c,d=cv(coords[name]); limits=('.33','.47','-.09','.08') if name=='e' else (('.21','.25','.01','.10') if name=='xi' else ('.23','.45','-.12','.12'))
    ll,hh,bb,tt=map(F,limits);assert ll<=a<=b<=hh and bb<=c<=d<=tt
   for name in ('a','u','v','b'):
    lo,hi=iv(coords[name]['imag']);L,U=map(F,('-.078','.021') if name=='a' else (('-.102','-.001') if name=='u' or key[0]==1 else ('-.065','.068')))
    assert L<lo<=hi<U
   lm=iv(response['details']['left_product_modulus']);rm=iv(response['details']['right_product_modulus']);bl,bh=iv(response['B'])
   assert bl==max(0,lm[0])+max(0,rm[0]) and bh==lm[1]+rm[1]==F(response['B_upper_rational'])
   upper,width=scalarcheck(n['scalar'],coords,shapes,key[0]); gap=-upper
   assert gap==F(n['boundary_gap_lower_rational']) and bh==F(n['boundary_response_upper_rational'])
   assert gap>0 and(gap>=F(1,200) or width<=gap/2) and bh-bl<=max(F(1,100),bh/4)
   assert n['resolution_test']['passed']
   accepted[(key[0],key[1][:2])].append((gap,bh))
 for key,i in index.items():
  n=nodes[i]
  if key[2]:
   parent=index[(key[0],key[1],key[2][:-1])];assert parent<i and nodes[parent]['action']=='split'
  if n['action']=='split':
   for child in n['children']:assert (key[0],key[1],child) in index
 for leaf in leaves:
  key=(leaf['beta'],leaf['chart'],leaf['address']);i=leaf['node_index'];assert index[key]==i and nodes[i]['action']==leaf['status'] and leaf['status']!='split'
  buckets[key[:2]].append(key[2])
 assert set(buckets)=={(b,c) for b in (0,1) for c in CHARTS}
 coverage=[]
 for (b,c),addresses in sorted(buckets.items()):
  ss=sorted(addresses);assert len(ss)==len(set(ss))
  assert all(not y.startswith(x) for x,y in zip(ss,ss[1:]));assert sum((F(1,2**len(x)) for x in ss),F())==1
  row={'beta':b,'chart':c,'leaf_count':len(ss),'normalized_mass_rational':'1','full_tree_node_count':2*len(ss)-1,'maximum_depth':max(map(len,ss))};coverage.append(row)
 assert data['coverage']=={'case_count':18,'chart_count':9,'cases':coverage,'total_frontier_leaves':len(leaves)}
 assert counts=={'split':1527,'excluded':114,'accepted boundary estimate':1431}
 summaries=[]
 coarse={(0,'k3'):(F('.01634'),F('1.645')),(0,'k4'):(F('.01510'),F('2.055')),(1,'k3'):(F('.00504'),F('1.369')),(1,'k4'):(F('.00817'),F('1.677'))}
 for row in data['domain_summaries']:
  key=(row['beta'],row['domain']);vals=accepted[key];g=min(x[0] for x in vals);B=max(x[1] for x in vals);r=D[int(key[1][1])][2];loss=r*r/2;delta=g-loss*B
  assert row['accepted_cells']==len(vals) and F(row['observed_boundary_gap_lower_rational'])==g and F(row['observed_response_upper_rational'])==B
  assert F(row['disk_barrier_factor_rational'])==loss and F(row['compensated_gap_rational'])==delta and row['valid_for_whole_domain'] and delta>F(1,4000)
  gl,bu=coarse[key];cg=gl-loss*bu
  assert gl<g and B<bu and cg>F(1,3200)
  if key[0]==0: assert cg>F(1,100)
  if key==(1,'k4'):assert cg>F(1,200)
  summaries.append({'rounded_gamma_lower_rational':str(gl),'rounded_B_upper_rational':str(bu),'rounded_corrected_gap_rational':str(cg),'strictly_above_common_gap_1_over_3200':True,'beta':key[0],'domain':key[1],'accepted_cells':len(vals),'gamma_min_rational':str(g),'B_max_rational':str(B),'corrected_gap_rational':str(delta),'corrected_gap_decimal_display':float(delta),'strictly_above_common_gap_1_over_4000':True})
 out={'status':'independent exact saved-data audit passed','source':SOURCE,'source_sha256':EXPECTED,'checker_sha256':sha(Path(__file__)),
      'input_bindings_checked':76,'visited_nodes':len(nodes),'complete_chart_cases':18,'terminal_leaves':len(leaves),'accepted_leaves':1431,'strict_geometry_exclusions':114,
      'all_address_images_reconstructed':True,'all_accepted_reference_response_scalar_associations_checked':True,'all_common_product_and_strict_height_checks_recomputed':True,
      'all_candidate_minima_and_four_component_sums_checked':True,'all_global_gamma_B_extrema_recomputed_separately':True,'domain_summaries':summaries,
      'uniform_corrected_gap_strict_lower_rational':'1/3200','source_root_primitive_or_interval_evaluations':0,
      'half_row_bound_claimed':False,'full_source_theorem_claimed':False,'global_filling_volume_theorem_claimed':False,'scope':'central original comparison only; no half-row, full-source or filling theorem'}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps({'status':out['status'],'summaries':[(r['beta'],r['domain'],r['corrected_gap_decimal_display']) for r in summaries],'output':str(args.output),'sha256':sha(args.output)}))
if __name__=='__main__':main()
