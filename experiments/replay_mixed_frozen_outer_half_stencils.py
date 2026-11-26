#!/usr/bin/env python3
"""Independent sine-log replay of 50 frozen-outer half-stencil domains."""
import argparse,gzip,hashlib,importlib.util,itertools,json,time,tempfile
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
PROOF=BASE/'notes/research_mixed_frozen_outer_half_stencils.md'
LIB=BASE/'experiments/replay_mixed_constant_selected_height_transport.py'
LIB_SHA=hashlib.sha256(LIB.read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('frozen_outer_replay_arithmetic',LIB);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
assert LIB_SHA==hashlib.sha256(LIB.read_bytes()).hexdigest()
ar=m.ar;n=5
H={0:(F('-.03'),F('.02')),1:(F('-.057'),F('-.02'))}

def params(box,types):
 v=[ar(a).union(ar(b))for a,b in box];tn,tc=types[1:]
 t=ar('.12')+ar('.10')*v[0];rho=ar('1/6')+ar('5/6')*v[0];x=t+(ar('.45')-t)*v[1]
 hc=arb(0)if tc==2 else ar(H[tc][0])+ar(H[tc][1]-H[tc][0])*v[3]
 hn=arb(0)if MODE==0 else ar(H[tn][0])+ar(H[tn][1]-H[tn][0])*v[4]
 u=v[4]if MODE==0 else v[2];cap=-ar('.02')*rho+(ar('.014')+ar('.02')*rho)*u
 cap0=-ar('.02')*ar('5/6')*(1-u);capu=ar('.014')+ar('.02')*rho
 zz=[acb(ar('.45')),acb(x,cap if MODE==0 else hn*rho),acb(t,ar('.014')if tc==2 else hc*rho)]
 dz=[[acb(0)for _ in range(5)]for _ in range(3)]
 dz[1][0]=acb(ar('.10')*(1-v[1]),cap0 if MODE==0 else hn*ar('5/6'));dz[1][1]=acb(ar('.45')-t)
 dz[1][4]=acb(0,capu if MODE==0 else ar(H[tn][1]-H[tn][0])*rho)
 if MODE==1:
  zz[0]=acb(t if FACE==0 else ar('.45'),cap)
  dz[0][0]=acb(ar('.10')if FACE==0 else arb(0),cap0);dz[0][2]=acb(0,capu)
 dz[2][0]=acb(ar('.10'),hc*ar('5/6'))
 if tc!=2:dz[2][3]=acb(0,ar(H[tc][1]-H[tc][0])*rho)
 dhc=[arb(0)for _ in range(5)];dhn=dhc.copy()
 if tc!=2:dhc[3]=ar(H[tc][1]-H[tc][0])
 if MODE!=0:dhn[4]=ar(H[tn][1]-H[tn][0])
 return zz,dz,m.Parameter(hc,dhc),m.Parameter(hn,dhn)

m.params=params

def specs():
 cases=[]
 for tc in range(3):
  for side,chi in itertools.product((0,1),(0,)if tc==2 else(0,1)):cases.append([[0,2,tc],side,chi,0,0,0])
 for tc in range(3):
  for tn,side,chi,face in itertools.product((0,1),(0,1),(0,)if tc==2 else(0,1),(0,1)):cases.append([[1,tn,tc],side,chi,1,face,1])
 assert len(cases)==50 and len(set(map(str,cases)))==50
 return cases

def test(box,case,witness=None):return m.test(box,case,witness)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def configure(bits):m.configure(bits)

def check_record(stem,prefix):
 rr=json.loads((BASE/f'repro/results/research-{stem.replace("_","-")}.json').read_text())
 assert rr['status']=='passed'
 assert rr['proof_sha256']==sha(BASE/f'notes/research_{stem}.md')
 assert rr['script_sha256']==sha(BASE/f'experiments/{prefix}_{stem}.py')
 if 'cover_path'in rr:
  cover=Path(rr['cover_path']);cover=cover if cover.is_absolute()else BASE/cover
  assert sha(cover)==rr['cover_sha256']
 for key in ('dependencies','dependencies_sha256'):
  for path,value in rr.get(key,{}).items():assert sha(BASE/path)==value,path

def check_inherited_selected_record():
 rr=json.loads((BASE/'repro/results/research-mixed-constant-selected-height-transport-replay.json').read_text())
 assert rr['status']=='passed'
 assert rr['proof_sha256']==sha(BASE/'notes/research_mixed_constant_selected_height_transport.md')
 assert rr['script_sha256']==sha(BASE/'experiments/replay_mixed_constant_selected_height_transport.py')
 assert rr['author_script_sha256']==sha(BASE/'experiments/certify_mixed_constant_selected_height_transport.py')
 assert rr['cover_sha256']==sha(BASE/rr['cover_path'])
 assert all(sha(BASE/p)==h for p,h in rr['dependencies_sha256'].items())

def exact_checks():
 global FACE,MODE
 assert F('.005')/F(1,6)==F('.03')
 assert F(1,300)/F(1,6)==F('.02')
 assert F('.0095')/F(1,6)==F('.057')
 assert sum(c[5]==0 for c in specs())==10 and sum(c[5]==1 for c in specs())==40
 assert len(specs())==50
 FACE=MODE=0
 z,dz,hc,hn=params([(F(1,2),F(1,2))]*5,[0,2,2])
 assert hc.v==0 and hn.v==0 and z[2].imag.contains(ar('.014'))and dz[1][4].imag>0
 return dict(exact_checks=6)

DEPS=list(dict.fromkeys(m.DEPS+['experiments/certify_mixed_constant_selected_height_transport.py','experiments/replay_mixed_constant_selected_height_transport.py','notes/research_mixed_constant_selected_height_transport.md','repro/results/research-mixed-constant-selected-height-transport.json','repro/results/research-mixed-constant-selected-height-transport-replay.json','repro/results/research-mixed-constant-selected-height-transport-cover.jsonl.gz','notes/research_mixed_early_selected_source_cap.md','experiments/certify_mixed_early_selected_source_cap.py','repro/results/research-mixed-early-selected-source-cap.json','notes/research_mixed_minimum_level_half_stencils.md','experiments/certify_mixed_minimum_level_half_stencils.py','repro/results/research-mixed-minimum-level-half-stencils.json','repro/results/research-mixed-minimum-level-half-stencils-cover.jsonl.gz']))
def replay_domain_job(job):
 global FACE,MODE,case
 number,entry,path,expected_sha,bits=job
 configure(bits)
 assert sha(path)==expected_sha
 data=json.loads(Path(path).read_text());assert data['case']==entry
 case=entry[:4];FACE=entry[4];MODE=entry[5];nodes=iter(data['nodes']);stack=[[(F(0),F(1))for _ in range(n)]]
 visits=accepted=monotonic=0;lo=None
 while stack:
  box=stack.pop();visits+=1;node=next(nodes)
  if node[0]=='S':
   assert len(node)==2 and type(node[1])is int and 0<=node[1]<n
   j=node[1];a,b=box[j];assert a<b;mid=(a+b)/2
   for pair in ((a,mid),(mid,b)):
    bb=list(box);bb[j]=pair;stack.append(bb)
   continue
  assert node[0]in('L','M')
  supplied=node[-1]
  assert isinstance(supplied,list)and len(supplied)==(1 if case[3]==0 else 2)
  assert all(isinstance(w,dict)and set(w)=={'center','derivatives','radius'}for w in supplied)
  lower,grads,wits=test(box,case,supplied)
  assert lower is not None,(number,visits,'root witness')
  if node[0]=='L':
   assert len(node)==2 and lower>0,(number,visits,'positive half',lower)
   accepted+=1;lo=lower.lower()if lo is None else min(lo,lower.lower())
  else:
   assert len(node)==4
   j,bit=node[1:3];assert type(j)is int and 0<=j<n and bit in(0,1)
   assert box[j][0]<box[j][1]and (grads[j]>0 if bit==0 else grads[j]<0),(number,visits,'monotonicity')
   bb=list(box);end=box[j][bit];bb[j]=(end,end);stack.append(bb);monotonic+=1
 assert next(nodes,None)is None,(number,'unused tree nodes')
 assert visits==data['visits']and accepted==data['accepted']and monotonic==data['monotonic_reductions']
 assert sha(path)==expected_sha
 return number,dict(case=entry,accepted=accepted,visits=visits,monotonic_reductions=monotonic,minimum=str(lo))

def replay_parallel(source,bits,jobs,start):
 assert 1<jobs<=16
 rows=[None]*50
 with tempfile.TemporaryDirectory(prefix='selected-height-independent-')as temp:
  with ProcessPoolExecutor(max_workers=jobs)as pool:
   pending={}
   with gzip.open(source,'rt')as stream:
    for number,entry in enumerate(specs()):
     line=stream.readline();assert line,(number,'missing domain')
     path=Path(temp)/f'{number:02d}.json';path.write_text(line)
     future=pool.submit(replay_domain_job,(number,entry,str(path),sha(path),bits));pending[future]=path
    assert not stream.read().strip(),'extra domains'
   for future in as_completed(pending):
    number,row=future.result();assert rows[number]is None and row['case']==specs()[number]
    rows[number]=row;pending[future].unlink()
    print('PASS domain',number+1,50,'leaves',row['accepted'],'monotonic',row['monotonic_reductions'],'minimum',row['minimum'],'elapsed',time.time()-start,flush=True)
 assert all(row is not None for row in rows)
 return rows,sum(row['visits']for row in rows),sum(row['accepted']for row in rows),sum(row['monotonic_reductions']for row in rows),min(arb(row['minimum']).lower()for row in rows)

def main():
 global FACE,MODE,case
 ap=argparse.ArgumentParser(description=__doc__)
 group=ap.add_mutually_exclusive_group()
 group.add_argument('--input',type=Path)
 group.add_argument('--witnesses',type=Path,help='Independently verify an untrusted complete cover before the author record exists.')
 ap.add_argument('--precision',type=int,default=320)
 ap.add_argument('--jobs',type=int,default=1)
 ap.add_argument('--output',type=Path,default=BASE/'repro/results/research-mixed-frozen-outer-half-stencils-replay.json')
 args=ap.parse_args();assert args.precision>=160;configure(args.precision)
 if args.input is None and args.witnesses is None:args.input=BASE/'repro/results/research-mixed-frozen-outer-half-stencils.json'
 ph,sh=sha(PROOF),sha(__file__);deps={p:sha(BASE/p)for p in DEPS}
 assert sha(LIB)==LIB_SHA
 author_script=BASE/'experiments/certify_mixed_frozen_outer_half_stencils.py';ash=sha(author_script)
 for stem in ('mixed_closed_cotangent_roots','mixed_minimum_neighbor_contour'):check_record(stem,'check')
 check_record('mixed_constant_selected_height_transport','certify')
 check_record('mixed_minimum_level_half_stencils','certify')
 check_inherited_selected_record()
 check_record('mixed_early_selected_source_cap','certify')
 checks=exact_checks();ih=None;saved=None
 if args.input:
  ih=sha(args.input);saved=json.loads(args.input.read_text());assert saved['status']=='passed'
  assert saved['proof_sha256']==ph and saved['script_sha256']==ash and saved['dependencies_sha256']==deps
  source=Path(saved['cover_path']);source=source if source.is_absolute()else BASE/source
  assert sha(source)==saved['cover_sha256']
 else:source=args.witnesses
 cover_hash=sha(source);start=time.time();rows=[];totalvis=totalaccepted=totalmonotonic=0;minimum=None
 if args.jobs>1:
  rows,totalvis,totalaccepted,totalmonotonic,minimum=replay_parallel(source,args.precision,args.jobs,start)
 else:
  with gzip.open(source,'rt')as stream:
   for number,entry in enumerate(specs()):
    line=stream.readline();assert line,(number,'missing domain')
    data=json.loads(line);assert data['case']==entry
    case=entry[:4];FACE=entry[4];MODE=entry[5];nodes=iter(data['nodes']);stack=[[(F(0),F(1))for _ in range(n)]]
    visits=accepted=monotonic=0;lo=None
    while stack:
     box=stack.pop();visits+=1;node=next(nodes)
     if node[0]=='S':
      assert len(node)==2 and type(node[1])is int and 0<=node[1]<n
      j=node[1];a,b=box[j];assert a<b;mid=(a+b)/2
      for pair in ((a,mid),(mid,b)):
       bb=list(box);bb[j]=pair;stack.append(bb)
      continue
     assert node[0]in('L','M')
     supplied=node[-1]
     assert isinstance(supplied,list)and len(supplied)==(1 if case[3]==0 else 2)
     assert all(isinstance(w,dict)and set(w)=={'center','derivatives','radius'}for w in supplied)
     lower,grads,wits=test(box,case,supplied)
     assert lower is not None,(number,visits,'root witness')
     if node[0]=='L':
      assert len(node)==2 and lower>0,(number,visits,'positive half',lower)
      accepted+=1;lo=lower.lower()if lo is None else min(lo,lower.lower())
     else:
      assert len(node)==4
      j,bit=node[1:3];assert type(j)is int and 0<=j<n and bit in(0,1)
      assert box[j][0]<box[j][1]and (grads[j]>0 if bit==0 else grads[j]<0),(number,visits,'monotonicity')
      bb=list(box);end=box[j][bit];bb[j]=(end,end);stack.append(bb);monotonic+=1
    assert next(nodes,None)is None,(number,'unused tree nodes')
    assert visits==data['visits']and accepted==data['accepted']and monotonic==data['monotonic_reductions']
    totalvis+=visits;totalaccepted+=accepted;totalmonotonic+=monotonic
    minimum=lo if minimum is None else min(minimum,lo)
    rows.append(dict(case=entry,accepted=accepted,visits=visits,monotonic_reductions=monotonic,minimum=str(lo)))
    print('PASS domain',number+1,50,'leaves',accepted,'monotonic',monotonic,'minimum',lo,'elapsed',time.time()-start,flush=True)
   assert not stream.read().strip(),'extra domains'
 assert ph==sha(PROOF)and sh==sha(__file__)and deps=={p:sha(BASE/p)for p in DEPS}and cover_hash==sha(source)
 if args.input:assert ih==sha(args.input)
 assert ash==sha(author_script)
 try:sourcepath=str(source.resolve().relative_to(BASE))
 except ValueError:sourcepath=str(source.resolve())
 out=dict(status='passed',precision_bits=args.precision,jobs=args.jobs,domains=50,cells=totalaccepted,visits=totalvis,monotonic_reductions=totalmonotonic,minimum_half=str(minimum),cases=rows,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,cover_path=sourcepath,cover_sha256=cover_hash,elapsed_seconds=time.time()-start,**checks,author_script_sha256=ash,input_source_kind='bound_author_record'if args.input else'untrusted_complete_cover',scope='Independent sine-logarithm and explicit-parameter-derivative replay of all50 frozen-outer half stencils.')
 if args.input:out.update(input_path=str(args.input),input_sha256=ih)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('FULL PASS',50,totalaccepted,totalmonotonic,checks,flush=True)
if __name__=='__main__':main()
