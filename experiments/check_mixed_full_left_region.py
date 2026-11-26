#!/usr/bin/env python3
"""Complete-input/provenance and exact bookkeeping check for the left region.

No interval inequalities, optimizer, cycle enumeration, or induction is run.
The arbitrary-length assembly is the written proof. Missing/partial numerical
inputs are fatal; no output is written until every required input passes.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
PROOF='notes/research_mixed_full_left_region.md'
FAMILIES=[
 ('minimum_level_half_stencils',192,3415762,22874),
 ('constant_selected_height_transport',78,817218,3226),
 ('frozen_outer_half_stencils',50,132360,877),
 ('one_early_neighbor_transport',175,354894,6542),
]
# stem, checker prefix, optional distinct proof stem
SOURCES=[
 ('early_selected_source_cap','certify',None),
 ('right_square_conditional_packets','certify','unselected_right_taper_products'),
 ('early_transition_support','certify',None),
 ('early_plateau_clusters','check',None),
 ('frozen_early_transport','check',None),
 ('plateau_accretivity','check',None),
 ('selected_plateau_support','certify',None),
 ('selected_minimum_flow_obstruction','check',None),
 ('central_outer_integral','check',None),
 ('local_outer_contribution','check',None),
 ('fourier_weight_continuation','check',None),
 ('conditional_torus_composition','check',None),
 ('coupled_outer_graph','check',None),
 ('minimum_neighbor_contour','check',None),
 ('cyclic_block_localization','certify','cyclic_critical_localization'),
 ('cyclic_block_localization-replay','replay','cyclic_critical_localization'),
 ('neighbor_conditioned_critical_boxes','certify',None),
 ('four_before_four_height','certify',None),
 ('four_before_four_height-replay','certify','four_before_four_height'),
 ('three_consecutive_four_height','check',None),
]
TEXT_INPUTS=[
 'notes/research_mixed_minimum_level_transport.md',
 'notes/research_mixed_early_selected_transport.md',
 'notes/research_mixed_partial_selected_heights.md',
]

def record_path(stem):return 'repro/results/research-mixed-'+stem.replace('_','-')+'.json'
def proof_path(stem):return 'notes/research_mixed_'+stem+'.md'
def script_path(stem,prefix):return 'experiments/'+prefix+'_mixed_'+stem+'.py'
def file_sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb')as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()

def specs(stem):
 out=[]
 if stem=='minimum_level_half_stencils':
  for tn,tc,side,chi in itertools.product((0,1),repeat=4):out.append([[0,tn,tc],side,chi,0,0])
  for to,tn,tc,side,chi in itertools.product((0,1),repeat=5):
   for face in range(6 if to==0 else 5):out.append([[to,tn,tc],side,chi,1,face])
 elif stem=='constant_selected_height_transport':
  for tc in (0,1,2):
   for side in (0,1):
    for chi in ((0,)if tc==2 else(0,1)):out.append([[0,2,tc],side,chi,0,0])
  for tn,side in itertools.product((0,1),repeat=2):out.append([[0,tn,2],side,0,0,0])
  for tn,side in itertools.product((0,1),repeat=2):
   for to in (0,1,2):
    for face in range((6,5,1)[to]):out.append([[to,tn,2],side,0,1,face])
  for tn,tc,side,chi in itertools.product((0,1),repeat=4):out.append([[2,tn,tc],side,chi,1,0])
 elif stem=='frozen_outer_half_stencils':
  for tc in (0,1,2):
   for side,chi in itertools.product((0,1),(0,)if tc==2 else(0,1)):out.append([[0,2,tc],side,chi,0,0,0])
  for tc in (0,1,2):
   for tn,side,chi,face in itertools.product((0,1),(0,1),(0,)if tc==2 else(0,1),(0,1)):out.append([[1,tn,tc],side,chi,1,face,1])
 else:
  assert stem=='one_early_neighbor_transport'
  macros=([[0,c,e,0,s]for e,c,s in itertools.product((0,1),repeat=3)]+
          [[1,c,n,0,s]for c,n,s in itertools.product((0,1),repeat=3)]+
          [[2,c,n,o,s]for c,n,o,s in itertools.product((0,1),repeat=4)])
  assert len(macros)==32
  for kind,center,neighbor,outer,side in macros:
   signs=(-1,1)if center==1 and((kind==0 and side==1)or(kind!=0 and side==0))else(0,)
   faces=range(1 if kind==0 else(6 if(neighbor if kind==1 else outer)==0 else 5))
   for sign,face in itertools.product(signs,faces):out.append([kind,center,neighbor,outer,side,sign,face])
 return out

class Inputs:
 def __init__(self):self.bindings={};self.records={};self.expanded=set()
 def bind(self,path,expected=None):
  path=str(path);p=Path(path);p=p if p.is_absolute()else BASE/p
  assert p.is_file(),'required input missing: '+path
  key=str(p.relative_to(BASE));digest=self.bindings.get(key)
  if digest is None:digest=file_sha(p);self.bindings[key]=digest
  assert expected is None or digest==expected,'stale binding: '+key
  return digest
 def read(self,path):
  self.bind(path)
  if path not in self.records:self.records[path]=json.loads((BASE/path).read_text())
  return self.records[path]
 def expand(self,path):
  if path in self.expanded:return
  self.expanded.add(path);r=self.read(path);deps={}
  for field in ('dependencies','dependencies_sha256'):
   values=r.get(field,{})
   assert isinstance(values,dict),(path,field)
   for p,h in values.items():
    assert p not in deps or deps[p]==h,(path,p,'inconsistent duplicate binding')
    deps[p]=h
  for p,h in deps.items():
   self.bind(p,h)
   # Nested JSON dependencies may contain diagnostic proposals: only their
   # hashes are checked here. Every theorem input is explicitly required below.
   if p.startswith('repro/results/')and p.endswith('.json'):self.expand(p)
  if 'cover_path'in r:self.bind(r['cover_path'],r['cover_sha256'])
 def require(self,stem,prefix,proof_stem=None):
  name=record_path(stem);r=self.read(name);assert r['status']=='passed',(name,'incomplete input')
  clean=stem.removesuffix('-replay');proof=proof_path(proof_stem or clean);script=script_path(clean,prefix)
  ph,sh=self.bind(proof),self.bind(script)
  assert r['script_sha256']==sh,(name,'script')
  deps={**r.get('dependencies',{}),**r.get('dependencies_sha256',{})}
  assert r.get('proof_sha256',deps.get(proof))==ph,(name,'proof')
  self.expand(name);return r
 def unchanged(self):
  for p,h in self.bindings.items():assert file_sha(BASE/p)==h,'input changed during assembly: '+p


def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,default=BASE/'repro/results/research-mixed-full-left-region.json')
 parser.add_argument('--check-only',action='store_true')
 parser.add_argument('--list-inputs',action='store_true')
 args=parser.parse_args()
 if args.list_inputs:
  print(json.dumps({'derivative_author_replay_pairs':[record_path(s)for s,_,_,_ in FAMILIES],
   'additional_required_records':[record_path(s)for s,_,_ in SOURCES],
   'required_texts':[PROOF,*TEXT_INPUTS],
   'note':'Every derivative family also requires its separately named -replay record and shared complete cover; resumed192 additionally requires its old-code partial provenance.'},indent=2));return
 inp=Inputs();ph=inp.bind(PROOF);sh=inp.bind(str(Path(__file__).relative_to(BASE)))
 # Fail before creating any canonical output if even one independent record is absent.
 for stem,_,_,_ in FAMILIES:
  inp.bind(record_path(stem));inp.bind(record_path(stem+'-replay'))
 summaries=[]
 for stem,total,leaves,monotonic in FAMILIES:
  a=inp.require(stem,'certify');r=inp.require(stem+'-replay','replay')
  assert a['precision_bits']>=256 and r['precision_bits']>=320,stem
  expected=specs(stem);assert len(expected)==total and len({json.dumps(v)for v in expected})==total
  for d in (a,r):
   assert d.get('domains',d.get('charts'))==total and len(d['cases'])==total,stem
   assert [v['case']for v in d['cases']]==expected,(stem,'ordered complete domain list')
   assert sum(v['accepted']for v in d['cases'])==d.get('accepted',d.get('cells'))==leaves
   assert sum(v['visits']for v in d['cases'])==d.get('visited',d.get('visits'))
   assert sum(v['monotonic_reductions']for v in d['cases'])==d['monotonic_reductions']==monotonic
   assert d['cover_sha256']==inp.bind(a['cover_path'])
  assert a.get('visited',a.get('visits'))==r.get('visited',r.get('visits'))
  if stem=='minimum_level_half_stencils':
   assert r['input_sha256']==inp.bind(record_path(stem))
   assert r['resumed_domains']+r['fresh_domains']==total
   if r['resumed_domains']:
    p='repro/results/research-mixed-minimum-level-half-stencils-independent-partial.json';old=inp.read(p)
    assert old['status']=='passed_partial'and old['domains']==r['resumed_domains']
    assert r['resume_record_sha256']==inp.bind(p)
    assert old['script_sha256']==inp.bind('experiments/capture_mixed_half_stencil_partial_replay.py')
    assert old['numerical_script_sha256']==inp.bind(old['numerical_script_path'])
    assert old['author_record_sha256']==inp.bind(record_path(stem))
    assert old['proof_sha256']==inp.bind(proof_path(stem))and old['cover_sha256']==a['cover_sha256']
    ids=[v['index']for v in old['cases']];assert len(set(ids))==old['domains']
    for row in old['cases']:
     j=row['index'];assert 0<=j<total and row['case']==expected[j]
     assert r['cases'][j]['method']=='original_independent_cone'
    assert sum(v['method']=='original_independent_cone'for v in r['cases'])==old['domains']
    inp.expand(p)
  else:assert r['author_script_sha256']==inp.bind(script_path(stem,'certify'))
  if stem=='one_early_neighbor_transport':assert a['macro_domains']==r['macro_domains']==32
  summaries.append(dict(stem=stem,domains=total,accepted=leaves,visited=r.get('visited',r.get('visits')),monotonic_reductions=monotonic))
 sources={}
 for stem,prefix,proof in SOURCES:sources[stem]=inp.require(stem,prefix,proof)
 for p in TEXT_INPUTS:inp.bind(p)
 assert sources['cyclic_block_localization-replay']['input_sha256']==inp.bind(record_path('cyclic_block_localization'))
 four=sources['four_before_four_height'];four_replay=sources['four_before_four_height-replay']
 assert four_replay['primitive']=='independent sine/logarithm and cotangent'
 assert four_replay['input_sha256']==inp.bind(record_path('four_before_four_height'))
 assert four['boundary_products']==four_replay['boundary_products']==512
 assert four['accepted_cells']==four_replay['accepted_cells']==4745
 assert sources['three_consecutive_four_height']['boundary_products']==256
 assert sources['three_consecutive_four_height']['accepted_cells']==2372
 cap=sources['early_selected_source_cap'];assert cap['products']==len(cap['cases'])==161
 assert cap['accepted']==71240 and {mode:sum(v['mode']==mode for v in cap['cases'])for mode in ('TT','TB','BT')}=={'TT':49,'TB':56,'BT':56}
 early=sources['early_transition_support'];assert early['reference_products']==len(early['cases'])==64 and early['cells']==251 and F(early['phase_gap'])==F(1,100)
 endpoint=sources['early_plateau_clusters'];assert F(endpoint['phase_gap'])==F(1,1000)and F(endpoint['finite_gap'])==F(1,2000)
 selected=sources['selected_plateau_support'];assert F(selected['reference_defect_upper'])==-F(1,100)and F(selected['finite_block_gap'])==F(1,200)
 assert selected['target_products']==36 and selected['reference_products']==96
 assert F(sources['plateau_accretivity']['effective_cyclic_accretivity'])>0
 # Exact arbitrary-length scalar accounting, not finite-word enumeration.
 assert (F(27,100)-F(22,100))**2/2==F(1,800)
 assert F(1,800)-F(1,1600)==F(1,1600)
 assert F(1,100)-F(1,200)==F(1,200)
 assert F(1,1000)-F(1,2000)==F(1,2000)
 assert 1+(F(57,50))**2<(F(38,25))**2
 # Coefficients of (m,k): torus, conditional kernels, Fourier weights, Gaussian.
 assert tuple(sum(v[j]for v in [(F(1),F(1)),(-F(1,2),-F(1,2)),(F(0),-F(1,2)),(-F(1,2),F(0))])for j in (0,1))==(0,0)
 inp.unchanged()
 result=dict(status='passed',complete_input_requirement=True,derivative_families=summaries,
  derivative_domain_count=sum(v['domains']for v in summaries),independently_verified_leaves=sum(v['accepted']for v in summaries),
  primary_record_count=2*len(FAMILIES)+len(SOURCES),recursive_records_checked=len(inp.expanded),exact_bookkeeping_checks=6,
  numerical_inequalities_repeated=0,cyclic_pattern_enumerations=0,region='[1/10,9/20]^m',central_region='[11/50,9/20]^m',
  finite_gap='min(1/2000,mu/1600), with mu>0 the proved plateau Hessian lower bound',level_power=0,
  proof_sha256=ph,script_sha256=sh,dependencies_sha256=inp.bindings,
  scope='Complete-input validation of the written arbitrary-length full-left assembly for all original selections and integer parities. No new numerical inequalities, no replacement of induction by finite patterns, and no whole-period, boundary-insertion or finite-exception theorem.')
 if not args.check_only:
  args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS full-left:',result['derivative_domain_count'],'complete domains;',result['independently_verified_leaves'],'independent leaves;',result['primary_record_count'],'primary records;',len(inp.bindings),'current file bindings',flush=True)
if __name__=='__main__':main()
