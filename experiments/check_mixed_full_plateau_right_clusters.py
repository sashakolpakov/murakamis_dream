#!/usr/bin/env python3
"""Exact, non-overlapping plateau/right incidence allocation with current source records."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,itertools,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];PROOF=ROOT/'notes/research_mixed_full_plateau_right_clusters.md'
SOURCES=[
 ('right-pair-correlated-support','certify_mixed_right_pair_correlated_support.py','research_mixed_right_pair_correlated_support.md'),
 ('right-run-supports','certify_mixed_right_run_supports.py','research_mixed_right_run_supports.md'),
 ('same-sign-height-reset','certify_mixed_same_sign_height_reset.py','research_mixed_same_sign_height_reset.md'),
 ('full-height-reset','certify_mixed_full_height_reset.py','research_mixed_full_height_reset.md'),
 ('oriented-height-reset','certify_mixed_oriented_height_reset.py','research_mixed_oriented_height_reset.md'),
 ('two-right-source-bound','certify_mixed_two_right_source_bound.py','research_mixed_two_right_source_bound.md'),
 ('selected-reset-plateau-support','certify_mixed_selected_reset_plateau_support.py','research_mixed_selected_reset_plateau_support.md'),
 ('selected-plateau-support','certify_mixed_selected_plateau_support.py','research_mixed_selected_plateau_support.md'),
 ('plateau-accretivity','check_mixed_plateau_accretivity.py','research_mixed_plateau_accretivity.md'),
 ('coupled-outer-graph','check_mixed_coupled_outer_graph.py','research_mixed_coupled_outer_graph.md')]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-full-plateau-right-clusters.json');args=ap.parse_args();ctx.prec=256
 deps={};records={};ph,sh=sha(PROOF),sha(__file__)
 for name,script,proof in SOURCES:
  paths=[f'repro/results/research-mixed-{name}.json','experiments/'+script,'notes/'+proof];deps.update({p:sha(ROOT/p)for p in paths});r=json.loads((ROOT/paths[0]).read_text());assert r['status']=='passed'
  assert r['script_sha256']==deps[paths[1]]and r['proof_sha256']==deps[paths[2]]
  for key in('dependencies','dependencies_sha256'):
   for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,(name,p)
  records[name]=r
 L,R=F(151,20),F(11,2);fL,fR=F(1683,100000),F(1202,100000);h3,h4=F(3,100),F(57,1000)
 assert (10-R)*h3*h3+(10-L)*h4*h4==F(240201,20000000)<fR
 assert (10-R)*h4*h4+(10-L)*h3*h3==F(33651,2000000)<fL
 assert (10-R)*h3*h3+(10-L)*h3*h3<fR
 table=dict(zip(itertools.product((0,1),repeat=3),map(F,['.0695','.024','.138','.077','.0487','.0002','.098','.035'])))
 for c in records['right-pair-correlated-support']['cases']:
  w=c['word'];base=table[tuple(w[1:4])];assert arb(c['min_gap'])>arb(base.numerator)/base.denominator
  fee=(fL if w[1]==0 else 0)+(fR if w[3]==0 else 0)
  assert arb(c['min_gap'])-arb(fee.numerator)/fee.denominator>arb(1)/5000
 assert records['right-run-supports']['boundary_products']==8192
 assert arb(records['right-run-supports']['minimum_gap'])>arb(1)/5000
 patterns=0;loops=0;parallel=0;right_total=0
 for m in range(1,13):
  for bits in itertools.product((0,1),repeat=m):
   if not any(bits):continue
   patterns+=1;right_total+=sum(bits);loops+=m==1;parallel+=m==2
   if all(bits):assert F(m,100)>=F(m,20000);continue
   runs=[]
   for j in range(m):
    if bits[j]and not bits[(j-1)%m]:
     run=[];k=j
     while bits[k]:run.append(k);k=(k+1)%m
     runs.append(run)
   components=[];singles=[];boundary_charge={};fees={}
   for nr,run in enumerate(runs):
    start,end=run[0],run[-1];a,c=(start-1)%m,(end+1)%m;assert not bits[a]and not bits[c]
    boundary_charge[nr,'L']=(a,L);boundary_charge[nr,'R']=(c,R);fees[nr,'L']=a;fees[nr,'R']=c
    if len(run)==1:components.append([(start-1)%m,start])
    elif len(run)==2:components.append([(start-1)%m,start,end])
    else:
     components.extend([[(start-1)%m,start],[(end-1)%m,end]]);singles.extend(run[1:-2])
   used=[e for c in components for e in c]+singles;assert len(used)==len(set(used));assert set(used)=={j for j in range(m)if bits[j]or bits[(j+1)%m]}
   zero=[bool(bits[j]or bits[(j-1)%m]or bits[(j+1)%m])for j in range(m)]
   possible_fee_uses=[]
   for j in range(m):
    k=(j+1)%m
    if bits[j]or bits[k]:continue
    left=[key for key,(v,coef)in boundary_charge.items()if key[1]=='R'and v==j]
    right=[key for key,(v,coef)in boundary_charge.items()if key[1]=='L'and v==k]
    assert len(left)==int(zero[j])and len(right)==int(zero[k])
    if zero[j]and zero[k]:
     assert fees[left[0]]==j and fees[right[0]]==k;possible_fee_uses.extend([left[0],right[0]])
   assert len(possible_fee_uses)==len(set(possible_fee_uses))
   loss=F(len(components),10000)+F(len(singles),100);assert loss>=F(sum(bits),20000)
 assert F(1,10000)>=F(1,20000)and F(1,10000)==F(2,20000)
 assert F(2,10000)-F(3,20000)==F(1,20000)and F(1,100)>F(1,20000)
 assert ph==sha(PROOF)and sh==sha(__file__)and deps=={p:sha(ROOT/p)for p in deps}
 out=dict(status='passed',source_records=len(SOURCES),isolated_pair_products_checked=len(records['right-pair-correlated-support']['cases']),exact_scalar_checks=9,cyclic_patterns=patterns,loop_patterns=loops,parallel_patterns=parallel,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,scope='Exact incidence allocation for all P/R configurations and selections, using the listed completed full finite-source inequalities. No transition/low-angle or full outer-period conclusion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(SOURCES),'records',patterns,'cyclic patterns',flush=True)
if __name__=='__main__':main()
