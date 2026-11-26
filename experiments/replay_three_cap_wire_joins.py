#!/usr/bin/env python3
"""Independent reflection-based replay of the original cap wire joins.

No author module is imported. Negative real factorial arguments are
reflected to positive strips, independently of the author's dilogarithm.
"""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import bphase,edge,partition,interval
ROOT=Path(__file__).resolve().parents[1]
def value(key,box):
 p=[interval(a,b)for a,b in box];pi=arb.pi();Y0=arb(1013)/10000;Y1=arb(2).log()/(2*pi)
 Y=(Y0 if key[2]==0 else Y1)if key[0]=='central'else Y0+(Y1-Y0)*p[0]
 x=acb(arb(7)/50 if key[1]==0 else arb(1)/5,Y);T=arb(41)/20;H=arb(99)/100
 if key[0]=='tail':return bphase(x,acb(T))+edge(acb(T))
 if key[0]=='radical':return bphase(x,acb(0))
 if key[0]=='central':t=acb(arb(9)/5*p[0],-H)
 elif key[2]==0:t=acb(-T+T*p[1],-H)
 elif key[2]==1:t=acb(arb(9)/5+(T-arb(9)/5)*p[1],-H)
 else:
  L=2*pi*Y;h=L*p[1]if key[2]%2==0 else L+(H-L)*p[1]
  t=acb(T if key[2]<4 else -T,-h)
 return bphase(x,t)+edge(t)+3*t.real*(-t.imag)/(2*pi)+t.imag
def bound(key):
 return arb(2)/3 if key[0]=='radical'else(arb(1261)/1000 if key[1]==0 else arb(6319)/5000)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',default='repro/results/research-three-cap-wire-joins-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
 path=ROOT/'repro/results/research-three-cap-wire-joins.json';data=json.loads(path.read_text());assert data['status']=='passed'
 expected={('central',s,e):1 for s in range(2)for e in range(2)}
 expected.update({('contour',s,k):2 for s in range(2)for k in range(6)})
 expected.update({(typ,s):1 for s in range(2)for typ in ('tail','radical')})
 seen=set();original=refined=visits=0
 for dom in data['domains']:
  key=tuple(dom['domain']);assert key in expected and key not in seen;seen.add(key)
  assert dom['dimension']==expected[key]
  for box in partition(dom['leaves'],dom['dimension']):
   original+=1;todo=[box]
   while todo:
    current=todo.pop();visits+=1
    if value(key,current)<bound(key):refined+=1;continue
    axis=max(range(len(current)),key=lambda k:current[k][1]-current[k][0]);a,b=current[axis]
    assert b-a>R(1,2**27),(key,current,value(key,current));mid=(a+b)/2
    for ends in ((a,mid),(mid,b)):
     child=list(current);child[axis]=ends;todo.append(tuple(child))
    assert visits<300000,'Replay unfinished'
 assert seen==set(expected)and original==data['leaf_count']
 p=arb.pi();Y=arb(2).log()/(2*p)
 margins=[Y-arb(1013)/10000,arb(91)/10000-Y+arb(1013)/10000,
          arb(3)/2+2*(arb(41)/20).cos()*(arb(99)/100).cosh(),
          arb(19113)/10000-arb(6319)/5000-arb(3237)/5000-arb(1)/20000,
          arb('0.101358689576302370861575311618')-arb('0.00000001')-arb(1013)/10000,
          Y-arb('0.101358689576302370861575311618')-arb('0.00000001'),
          arb(9)/1000-Y+arb('0.101358689576302370861575311618')-arb('0.00000001')]
 assert all(v>0 for v in margins)
 for file,h in data['dependencies_sha256'].items():assert sha256((ROOT/file).read_bytes()).hexdigest()==h,file
 assert sha256((ROOT/'experiments/certify_three_cap_wire_joins.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
         'original_leaf_count':original,'replayed_leaf_count':refined,'visited':visits,
         'scalar_checks':len(margins),'exact_binary_cover':True,'elapsed_seconds':time.monotonic()-start,
         'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'independent_helper_sha256':sha256((ROOT/'experiments/replay_three_cap_wire_complement.py').read_bytes()).hexdigest()}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
