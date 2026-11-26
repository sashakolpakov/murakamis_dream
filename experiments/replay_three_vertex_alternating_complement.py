#!/usr/bin/env python3
"""Independent opposite-frequency replay of the undeleted alternating V3 tail."""
import argparse,json,time
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import partition
ROOT=Path(__file__).resolve().parents[1];ii=acb(0,1)
def a(v):
 q=Q(v);return arb(q.numerator)/q.denominator

def reference():
 path=ROOT/'repro/results/research-three-four-source-interface.json';rec=json.loads(path.read_text());assert rec['status']=='passed'
 assert rec['script_sha256']==sha256((ROOT/'experiments/check_three_four_source_interface.py').read_bytes()).hexdigest()
 for dep,digest in rec['dependencies_sha256'].items():assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,dep
 root=rec['root_certificate'];c=acb(*map(a,root['center']));radius=a(root['complex_disk_radius']);z=acb(arb(c.real,radius),arb(c.imag,radius))
 coeff=(1,-2,4,-6,4)
 f=lambda v:sum(coeff[j]*v**j for j in range(5))
 df=lambda v:sum(j*coeff[j]*v**(j-1)for j in range(1,5))
 cinv=1/df(c);pre=acb(cinv.real.mid(),cinv.imag.mid());defect=abs(1-pre*df(z));shift=abs(pre*f(c))
 p=arb.pi();B=z*z*(2*z-1)**2/(2*(z-1));k=z*z*B/(z*z+B);cosine=1-2*k
 K=cosine+ii*(1-cosine*cosine).sqrt();x=K.log()/(2*p*ii);r=abs(K)
 margins={'contraction':1-defect,'self-map':radius-shift-radius*defect,'wire lower':x.real,'wire upper':arb(1)/4-x.real,'K above real line':K.imag,'radius':1-r,'r squared minus real K':r*r-K.real,'high half':1-3*r*r+2*K.real,'short interval':abs(1-K.conjugate()*(arb(9)*p*ii/10).exp())**2-4*r*r}
 assert all(v>0 for v in margins.values()),margins
 return K,margins

def primitive(p):
 pi=arb.pi()
 if p.contains(0)and p.upper()<arb(1)/20:
  rad=p.upper()
  if rad==0:return arb(0)
  return arb(0,(rad*(-(2*pi*rad).log()+pi+1+arb(1)/199)).upper())
 return (-2*pi*ii*p).exp().polylog(2).imag/(2*pi)

def entropy(s,t,K):
 pi=arb.pi();L=K.conjugate();rad=abs(K)
 term=((L*(2*pi*ii*s).exp()).polylog(2)+(L*(2*pi*ii*t).exp()).polylog(2)-2*L.polylog(2)).imag/(2*pi)
 return -rad.log()+primitive(s+t)+(s+t)*rad.log()+term

def maps(kind,values):
 if kind=='low':return values[0]/4,9*values[1]/20
 return arb(9)/20,9*values[0]/20

def check(kind,box,K):
 vals=[a(lo).union(a(hi))for lo,hi in box];mid=[a((lo+hi)/2)for lo,hi in box];width=[a((hi-lo)/2)for lo,hi in box]
 s,t=maps(kind,vals);upper=entropy(s,t,K)
 if s+t>0:
  pi=arb.pi();L=K.conjugate();common=(2*abs(K)*(pi*(s+t)).sin()).log()
  ds=common-abs(1-L*(2*pi*ii*s).exp()).log();dt=common-abs(1-L*(2*pi*ii*t).exp()).log()
  grad=[ds/4,9*dt/20]if kind=='low'else[9*dt/20]
  cs,ct=maps(kind,mid);bound=entropy(cs,ct,K)+sum(w*abs(g)for w,g in zip(width,grad))
  if bound.upper()<upper.upper():upper=bound
 return upper<arb(13)/20

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-vertex-alternating-complement-replay.json');args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
 path=ROOT/'repro/results/research-three-vertex-alternating-complement.json';data=json.loads(path.read_text());assert data['status']=='passed'
 K,margins=reference();seen=set();original=accepted=visits=0
 for row in data['domains']:
  kind=row['domain'];assert kind in {'low','high'}and kind not in seen;seen.add(kind);dim=2 if kind=='low' else 1
  assert row['dimension']==dim
  for box in partition(row['leaves'],dim):
   original+=1;todo=[box]
   while todo:
    current=todo.pop();visits+=1
    if check(kind,current,K):accepted+=1;continue
    axis=max(range(dim),key=lambda j:current[j][1]-current[j][0]);lo,hi=current[axis];assert hi-lo>Q(1,2**25),(kind,current);mid=(lo+hi)/2
    for ends in ((lo,mid),(mid,hi)):
     child=list(current);child[axis]=ends;todo.append(tuple(child))
    assert visits<100000
 assert seen=={'low','high'}and original==data['leaf_count']
 assert data['script_sha256']==sha256((ROOT/'experiments/certify_three_vertex_alternating_complement.py').read_bytes()).hexdigest()
 for dep,digest in data['dependencies_sha256'].items():assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,dep
 deps=['experiments/replay_three_cap_wire_complement.py','notes/research_three_vertex_alternating_reference_complement.md']
 result={'status':'passed','precision_bits':args.precision,'exact_domain_cover':True,'original_leaves':original,'replayed_leaves':accepted,'visits':visits,
 'strict_comparison_count':len(margins),'margins':{k:str(v)for k,v in margins.items()},'method':'Opposite-frequency primitive, conjugated denominator, cosine-square-root wire, fresh polynomial Newton and exact binary cover; no author imports.',
 'artifact_sha256':sha256(path.read_bytes()).hexdigest(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'elapsed_seconds':time.monotonic()-start}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS',original,accepted,'leaves',len(margins),'comparisons')
if __name__=='__main__':main()
