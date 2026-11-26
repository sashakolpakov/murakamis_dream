#!/usr/bin/env python3
"""Exact extraction of finite-row height profiles; no new outward cover."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sy

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_height_resolved_seam_sources.md'
SOURCES = ((0,0,0),(0,0,1),(1,0,1),(1,1,0),(1,1,1))
TABLE = {
 'A00': (['-.03','0','.02'], ['.360050','.325066','.305497']),
 'A10': (['-.03','0','.02'], ['.485081','.460764','.446493']),
 'B0':  (['-.03','0','.02'], ['.296665','.325066','.347548']),
 'A01': (['-.057','-.02','0','.014'], ['.447948','.404270','.386681','.332579']),
 'A11': (['-.057','0','.014'], ['.551147','.515591','.465875']),
 'B1':  (['-.057','0','.014'], ['.461406','.515591','.487806']),
}

def sha(path):
 return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def cover(addresses):
 assert isinstance(addresses,list) and addresses
 a=sorted(addresses);assert len(a)==len(set(a))
 assert all(isinstance(s,str) and set(s)<=set('01') for s in a)
 assert all(not y.startswith(x) for x,y in zip(a,a[1:]))
 assert sum((F(1,2**len(s)) for s in a),F(0))==1

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-height-resolved-seam-sources.json')
 args=ap.parse_args();ph,sh=sha(PROOF),sha(__file__);deps={};checks=[]
 def bind(path):
  path=str(path);h=sha(ROOT/path)
  if path in deps:assert deps[path]==h,path
  deps[path]=h;return h
 def record(stem,script,proof=None):
  path=f'repro/results/research-mixed-{stem}.json';h=bind(path)
  d=json.loads((ROOT/path).read_text());assert d['status']=='passed'
  assert d['script_sha256']==bind('experiments/'+script)
  if proof is not None:assert d['proof_sha256']==bind('notes/'+proof)
  for field in ('dependencies','dependencies_sha256'):
   for p,v in d.get(field,{}).items():assert bind(p)==v,p
  return d,h

 grid,gh=record('endpoint-support-grid','check_mixed_endpoint_support_grid.py','research_mixed_endpoint_support_grid.md')
 allgrid,ah=record('all-endpoint-support','certify_mixed_all_endpoint_support.py','research_mixed_all_endpoint_support.md')
 geom,gmh=record('43-endpoint-support','check_mixed_43_endpoint_support.py','research_mixed_43_endpoint_support.md')
 rep,rh=record('43-endpoint-support-replay','replay_mixed_43_endpoint_support.py')
 allrep,arh=record('all-endpoint-support-replay','replay_mixed_all_endpoint_support.py','research_mixed_all_endpoint_support.md')
 collar,_=record('real-zero-collar','certify_mixed_real_zero_collar.py','research_mixed_real_zero_collar.md')
 grouped,_=record('hybrid-zero-pair-reduction','check_mixed_hybrid_zero_pair_reduction.py','research_mixed_hybrid_zero_pair_reduction.md')
 assert rep['source_input_sha256']==gh
 assert rep['geometry_input_sha256']==gmh and geom['source_input_sha256']==gh
 assert allrep['input_sha256']==ah
 assert grid['precision_bits']>=160 and allgrid['precision_bits']>=160
 assert rep['precision_bits']>=256 and allrep['precision_bits']>=256
 checks.append('Current author, independent replay, geometry and complete finite-source bindings')

 special_heights=tuple(map(F,['-.057','-.02','0','.014']))
 expected_special={(h,F(-2,5)+F(j,20)) for h in special_heights for j in range(15)}
 expected_all={(s,h,F(-1,2)+F(j,10)) for s in SOURCES for h in map(F,(['-.03','0','.02'] if s[1]==0 else ['-.057','0','.014'])) for j in range(11)}
 assert grid['source_grid_count']==len(grid['source_grid'])==60
 assert allgrid['source_values']==len(allgrid['source_grid'])==165
 assert {(F(r['height']),F(r['kappa'])) for r in grid['source_grid']}==expected_special
 assert {(tuple(r['source']),F(r['height']),F(r['kappa'])) for r in allgrid['source_grid']}==expected_all
 checks.append('All 60 special and 165 general source-grid keys occur exactly once')

 rows={};original_total=0
 for source,rec in [('special',grid),('all',allgrid)]:
  total=0
  for r in rec['source_grid']:
   s=(0,1,1) if source=='special' else tuple(r['source'])
   h,k,U=F(r['height']),F(r['kappa']),F(r['upper'])
   assert U>0 or k!=0
   assert r['selected_alias']==int(s[1]==1 and h>0)
   cover(r['addresses']);n=len(r['addresses'])
   assert n==r['accepted'] and r['visited']==2*n-1
   key=(s,h,k);assert key not in rows
   rows[key]=(U,n,source);total+=n
  assert total==rec['source_cells'];original_total+=total
 assert original_total==57092
 checks.append('Every original full-square prefix cover and exact saved cell count verified')

 replay_total=0
 for source,replay in [('special',rep),('all',allrep)]:
  seen=set();total=0
  for d in replay['details']:
   if d['kind']!='source':continue
   s=(0,1,1) if source=='special' else tuple(d['source'])
   key=(s,F(d['height']),F(d['kappa']))
   assert key not in seen and key in rows and rows[key][2]==source
   seen.add(key);n=rows[key][1]
   assert isinstance(d['refinements'],int) and d['refinements']>=0
   assert d['cells']==n+d['refinements'];total+=d['cells']
  assert seen=={k for k,v in rows.items() if v[2]==source}
  assert total==replay['counts']['source'];replay_total+=total
 assert replay_total==57166
 assert allrep['source_values']==165
 checks.append('Each saved independent source replay matches its exact input grid and binary refinement counts')

 mapping={'A00':(0,0,1),'A10':(1,0,1),'B0':(0,0,0),'A01':(0,1,1),'A11':(1,1,1),'B1':(1,1,0)}
 profiles={};segments=[];knots=0
 for name,(hs,us) in TABLE.items():
  h=list(map(F,hs));u=list(map(F,us));assert all(x<y for x,y in zip(h,h[1:]))
  assert [rows[mapping[name],x,F(0)][0] for x in h]==u
  profiles[name]=[{'height':str(x),'upper':str(y)} for x,y in zip(h,u)]
  knots+=len(h)
  for x,y,U,V in zip(h,h[1:],u,u[1:]):
   slope=(V-U)/(y-x);intercept=U-slope*x
   assert slope*x+intercept==U and slope*y+intercept==V
   assert (U+V)/2==slope*(x+y)/2+intercept
   segments.append(dict(profile=name,lower=str(x),upper=str(y),slope=str(slope),intercept=str(intercept)))
 assert knots==19 and len(segments)==13
 assert F('.404270')<F('.447948')+(F('-.02')-F('-.057'))/F('.057')*(F('.386681')-F('.447948'))
 checks.append('All 19 zero-slope knots, 13 exact affine segments and the improved negative .02 knot extracted')

 maxima={}
 for name in ['A01','A11','B1']:
  hs,us=TABLE[name];pairs=list(zip(map(F,hs),map(F,us)))
  maxima[name]={'0':str(max(u for h,u in pairs if h<=0)), '1':str(max(u for h,u in pairs if h>=0))}
 assert maxima=={'A01':{'0':str(F('.447948')),'1':str(F('.386681'))},'A11':{'0':str(F('.551147')),'1':str(F('.515591'))},'B1':{'0':str(F('.515591')),'1':str(F('.515591'))}}
 checks.append('Selection-dependent full-band maxima')

 X,p,P,D=sy.symbols('X p P D',nonzero=True);j,N=sy.symbols('j N',integer=True)
 identities=0
 for e in (0,1):
  for c in (0,1):
   R=X**(-c*j)*p/P**(1+e)
   assert sy.simplify(X**(-c*j)*p*P/P**(2+e)-R)==0;identities+=1
   for d in (0,1):
    for sig in range(d+1):
     literal=R**2*D**d*X**(-N*d*sig)
     expanded=X**(-2*c*j-N*d*sig)*p**2*D**d/P**(2+2*e)
     assert sy.simplify(literal-expanded)==0
     assert 2*F(d,2)==d and 2*F(d*sig,2)==d*sig
     identities+=1
 for beta in (0,1):
  assert F(beta,2)+F(beta,2)==beta;identities+=1
 checks.append('Literal endpoint rows, squared Laurent powers, selected normalization and middle halfweight recombination')

 assert ph==sha(PROOF) and sh==sha(__file__)
 assert all(sha(ROOT/p)==h for p,h in deps.items())
 result=dict(status='passed',exact_identity_count=identities,checks=checks,primary_records=7,current_bindings=len(deps),source_grid_values=225,original_source_cells=original_total,independent_replay_source_cells=replay_total,extracted_zero_slope_knots=knots,affine_segment_count=len(segments),profiles=profiles,segments=segments,selection_band_maxima=maxima,new_outward_cells=0,source_cells_recomputed=0,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,scope='Complete finite endpoint-row height interpolation and fixed real-collar transfer; extraction from completed source covers and saved independent replays only. No geometric-potential comparison or whole-period bound.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',identities,'identities;',len(checks),'checks;',225,'grid values;',knots,'knots;',len(segments),'segments;',len(deps),'bindings',flush=True)

if __name__=='__main__':main()
