#!/usr/bin/env python3
"""Sharper original cap exterior bound for quantified outgoing preparation."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,ctx
from certify_three_cap_wire_complement import evaluate,domains,REGIONS,scalar_checks
ROOT=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
 ap.add_argument('--output',default='repro/results/research-three-prepared-cap-exterior.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();scalar=scalar_checks();saved=[];visits=0
 for key,dim in domains():
  todo=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
  while todo:
   path,box=todo.pop();visits+=1;v=evaluate(key,box)
   if v<arb(158)/125:leaves.append(path);continue
   lo,hi=REGIONS[key[1]]
   weights=[float(hi-lo)]if dim==1 else[float(hi-lo),.5 if key[2]<2 else .2]
   axis=max(range(dim),key=lambda j:float(box[j][1]-box[j][0])*weights[j]);a,b=box[axis]
   assert b-a>Q(1,2**26),('unproved',key,box,v);mid=(a+b)/2
   for side,ends in enumerate(((a,mid),(mid,b))):
    child=list(box);child[axis]=ends;todo.append((path+str(2*axis+side),tuple(child)))
   assert visits<500000,'Coverage unfinished; no certificate saved.'
  saved.append({'domain':list(key),'dimension':dim,'leaves':leaves})
 deps=['experiments/certify_three_cap_wire_complement.py','notes/research_three_cap_wire_complement.md',
       'notes/research_three_prepared_cap_quantified_source.md']
 result={'status':'passed','precision_bits':args.precision,'threshold':'158/125',
         'domain_count':len(saved),'domains':saved,'leaf_count':sum(len(d['leaves'])for d in saved),
         'visited':visits,'scalar_checks':scalar,'elapsed_seconds':time.monotonic()-start,
         'scope':'Original complete-cap rate<1.264 outside input wire Re x in [.14,.20] on Im x=log(2)/(2*pi).',
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
if __name__=='__main__':main()
