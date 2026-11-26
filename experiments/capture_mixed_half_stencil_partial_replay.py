#!/usr/bin/env python3
"""Record completed original independent workers after an explicit partial failure.

This does not rerun numerical inequalities. It binds retained successful worker
outputs to the exact original script and canonical author trees, and validates
all coverage/counts before a separate resumed numerical replay.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[1]
AUTHOR=BASE/'repro/results/research-mixed-minimum-level-half-stencils.json'
PROOF=BASE/'notes/research_mixed_minimum_level_half_stencils.md'
OLD=BASE/'repro/snapshots/replay_mixed_minimum_level_half_stencils-before-cone-refinement.py'
NUMERICAL=BASE/'experiments/replay_mixed_minimum_level_half_stencils.py'
OUT=BASE/'repro/results/research-mixed-minimum-level-half-stencils-independent-partial.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def unpack(row):
 pool=row['witness_pool'];used=set();nodes=[]
 for v in row['nodes']:
  if v[0]=='S':nodes.append(v);continue
  ids=v[-1];assert len(ids)==(1 if row['case'][3]==0 else 2)
  assert all(type(j)is int and 0<=j<len(pool) for j in ids)
  used.update(ids);nodes.append(v[:-1]+[[pool[j]for j in ids]])
 assert used==set(range(len(pool)))
 return nodes
def coverage(nodes):
 stack=[[(F(0),F(1))for _ in range(5)]];leaves=monotonic=0
 for v in nodes:
  box=stack.pop()
  if v[0]=='S':
   assert len(v)==2 and type(v[1])is int and 0<=v[1]<5
   j=v[1];a,b=box[j];assert a<b;mid=(a+b)/2
   for pair in ((a,mid),(mid,b)):
    child=list(box);child[j]=pair;stack.append(child)
  elif v[0]=='M':
   assert len(v)==4 and type(v[1])is int and 0<=v[1]<5 and v[2]in(0,1)
   j,bit=v[1:3];a,b=box[j];assert a<b;child=list(box);child[j]=(box[j][bit],)*2;stack.append(child);monotonic+=1
  else:assert v[0]=='L'and len(v)==2;leaves+=1
 assert not stack
 return leaves,len(nodes),monotonic
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--directory',type=Path,required=True);p.add_argument('--output',type=Path,default=OUT);args=p.parse_args();ctx.prec=320
 sh=sha(__file__);oh=sha(OLD);assert oh==sha(NUMERICAL),'capture precedes numerical-script refinement'
 snap=json.loads((args.directory/'snapshot.json').read_text());assert snap['script_sha256']==oh and snap['proof_sha256']==sha(PROOF)
 ah=sha(AUTHOR);author=json.loads(AUTHOR.read_text());assert author['status']=='passed'and author['domains']==192
 assert author['proof_sha256']==sha(PROOF)
 deps=dict(author['dependencies_sha256'])
 for f,h in deps.items():assert sha(BASE/f)==h,f
 cover=BASE/author['cover_path'];ch=sha(cover);assert ch==author['cover_sha256']
 rows=[];retained=[]
 with gzip.open(cover,'rt')as stream:
  for j,line in enumerate(stream):
   original=json.loads(line);assert original['case']==author['cases'][j]['case']
   fp=args.directory/f'{j:03d}-checked.json.gz'
   if not fp.exists():continue
   ih=sha(fp)
   with gzip.open(fp,'rt')as f:checked=json.load(f)
   assert checked['case']==original['case']
   on,cn=unpack(original),unpack(checked);assert on==cn
   counts=coverage(cn);assert counts==(checked['accepted'],checked['visits'],checked['monotonic_reductions'])
   assert counts==(original['accepted'],original['visits'],original['monotonic_reductions'])
   assert arb(checked['minimum'])>0 and ih==sha(fp)
   row={k:checked[k]for k in ('case','accepted','visits','monotonic_reductions','minimum')}
   row.update(index=j,retained_worker_output_sha256=ih,canonical_tree_sha256=hashlib.sha256(json.dumps(original,sort_keys=True,separators=(',',':')).encode()).hexdigest())
   rows.append(row);retained.append(str(fp));print('CAPTURE',j+1,len(rows),flush=True)
 assert j==191 and len(rows)<192 and rows
 assert sh==sha(__file__)and oh==sha(OLD)==sha(NUMERICAL)and ah==sha(AUTHOR)and ch==sha(cover)
 for f,h in deps.items():assert sha(BASE/f)==h,f
 for f in (AUTHOR,PROOF,OLD):deps[str(f.relative_to(BASE))]=sha(f)
 result=dict(status='passed_partial',precision_bits=320,domains=len(rows),expected_domains=192,cases=rows,accepted=sum(v['accepted']for v in rows),visited=sum(v['visits']for v in rows),monotonic_reductions=sum(v['monotonic_reductions']for v in rows),script_sha256=sh,numerical_script_sha256=oh,numerical_script_path=str(OLD.relative_to(BASE)),author_record_sha256=ah,proof_sha256=sha(PROOF),cover_sha256=ch,dependencies_sha256=deps,
 scope='Completed full-domain outputs of the original independent320 numerical worker, captured after aggregate root-cone failure at domain125/node19811. Numerical inequalities are not rerun by capture. Exact canonical trees, witness data, complete coverage and output counts are rechecked; omitted domains require a new numerical replay.')
 args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS PARTIAL',len(rows),result['accepted'],flush=True)
if __name__=='__main__':main()
