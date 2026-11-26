#!/usr/bin/env python3
"""Independent reflected-primitive replay of the sharper cap exterior."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,ctx
from replay_three_cap_wire_complement import value,partition
ROOT=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',default='repro/results/research-three-prepared-cap-exterior-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
 path=ROOT/'repro/results/research-three-prepared-cap-exterior.json';data=json.loads(path.read_text())
 assert data['status']=='passed'and data['threshold']=='158/125'
 expected={('contour',r,k):2 for r in range(4)for k in range(6)}
 expected.update({('tail',r):1 for r in (1,2)})
 seen=set();original=refined=visits=0
 for dom in data['domains']:
  key=tuple(dom['domain']);assert key in expected and key not in seen and dom['dimension']==expected[key];seen.add(key)
  for original_box in partition(dom['leaves'],dom['dimension']):
   original+=1;todo=[original_box]
   while todo:
    box=todo.pop();visits+=1
    if value(key,box)<arb(158)/125:refined+=1;continue
    axis=max(range(len(box)),key=lambda j:box[j][1]-box[j][0]);a,b=box[axis]
    assert b-a>R(1,2**28),(key,box);mid=(a+b)/2
    for ends in ((a,mid),(mid,b)):
     child=list(box);child[axis]=ends;todo.append(tuple(child))
    assert visits<500000,'Replay unfinished'
 assert seen==set(expected)and original==data['leaf_count']
 for f,h in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h,f
 assert sha256((ROOT/'experiments/certify_three_prepared_cap_exterior.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'threshold':'158/125',
         'domain_count':len(seen),'original_leaf_count':original,'replayed_leaf_count':refined,'visited':visits,
         'exact_binary_cover':True,'elapsed_seconds':time.monotonic()-start,
         'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'independent_helper_sha256':sha256((ROOT/'experiments/replay_three_cap_wire_complement.py').read_bytes()).hexdigest()}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
