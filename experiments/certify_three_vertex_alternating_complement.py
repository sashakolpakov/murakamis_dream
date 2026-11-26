#!/usr/bin/env python3
"""Full undeleted V3 real-index complement at the validated alternating reference."""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from flint import arb,acb,ctx
from certify_three_cap_central_complement import jreal
ROOT=Path(__file__).resolve().parents[1];ii=acb(0,1)
def a(v):
 q=Q(v);return arb(q.numerator)/q.denominator

def reference():
 path=ROOT/'repro/results/research-three-four-source-interface.json'
 record=json.loads(path.read_text());assert record['status']=='passed'
 assert record['script_sha256']==sha256((ROOT/'experiments/check_three_four_source_interface.py').read_bytes()).hexdigest()
 for dep,digest in record['dependencies_sha256'].items():assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,dep
 rr=record['root_certificate'];center=acb(*map(a,rr['center']));radius=a(rr['complex_disk_radius'])
 box=acb(arb(center.real,radius),arb(center.imag,radius))
 poly=lambda z:(((4*z-6)*z+4)*z-2)*z+1
 derivative=lambda z:((16*z-18)*z+8)*z-2
 raw=1/derivative(center);pre=acb(raw.real.mid(),raw.imag.mid())
 contraction=abs(1-pre*derivative(box));displacement=abs(pre*poly(center))
 margins={'Newton contraction':1-contraction,'Newton strict self-map':radius-displacement-contraction*radius}
 p=arb.pi();B=box**2*(2*box-1)**2/(2*(box-1))
 x=(box**2*B/(box**2+B)).sqrt().asin()/p;K=(2*p*ii*x).exp();r=abs(K)
 margins.update({'wire lower':x.real,'wire upper':arb(1)/4-x.real,'positive imaginary K':K.imag,
  'radius below one':1-r,'r squared exceeds ReK':r*r-K.real,
  'high half derivative':1-3*r*r+2*K.real,
  'short high interval derivative':abs(1-K*(-arb(9)*p*ii/10).exp())**2-4*r*r})
 assert all(v>0 for v in margins.values()),margins
 return K,x,path,margins

def value(s,t,K):
 p=arb.pi();rad=abs(K)
 Is=((K*(-2*p*ii*s).exp()).polylog(2)-K.polylog(2))/(2*p*ii)
 It=((K*(-2*p*ii*t).exp()).polylog(2)-K.polylog(2))/(2*p*ii)
 return -rad.log()+jreal(acb(s+t))+(s+t)*rad.log()-Is.real-It.real

def domain(kind,coords):
 if kind=='low':return a('1/4')*coords[0],a('9/20')*coords[1],[a('1/4'),a('9/20')]
 return a('9/20'),a('9/20')*coords[0],[a('9/20')]

def evaluate(kind,box,K):
 p=arb.pi();coords=[a(lo).union(a(hi))for lo,hi in box];centers=[a((lo+hi)/2)for lo,hi in box];widths=[a((hi-lo)/2)for lo,hi in box]
 s,t,scale=domain(kind,coords);v=value(s,t,K);costs=None
 if s+t>0:
  lp=(2*abs(K)*(p*(s+t)).sin()).log()
  ds=lp-abs(1-K*(-2*p*ii*s).exp()).log();dt=lp-abs(1-K*(-2*p*ii*t).exp()).log()
  gradients=[scale[0]*ds,scale[1]*dt]if kind=='low'else[scale[0]*dt]
  costs=[widths[j]*abs(g)for j,g in enumerate(gradients)]
  cs,ct,_=domain(kind,centers);mv=value(cs,ct,K)+sum(costs)
  if mv.upper()<v.upper():v=mv
 return v<a('13/20'),costs,v

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-vertex-alternating-complement.json');args=ap.parse_args();ctx.prec=args.precision
 K,x,reference_path,margins=reference();start=time.monotonic();domains=[];visits=0
 for kind,dim in [('low',2),('high',1)]:
  todo=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
  while todo:
   path,box=todo.pop();visits+=1;passed,costs,v=evaluate(kind,box,K)
   if passed:leaves.append(path);continue
   axis=max(range(dim),key=lambda j:float(costs[j])if costs and all(c.is_finite()for c in costs)else float(box[j][1]-box[j][0]))
   lo,hi=box[axis];assert hi-lo>Q(1,2**24),(kind,box,v);mid=(lo+hi)/2
   for bit,part in enumerate(((lo,mid),(mid,hi))):
    child=list(box);child[axis]=part;todo.append((path+str(2*axis+bit),tuple(child)))
   assert visits<100000
  domains.append({'domain':kind,'dimension':dim,'leaves':leaves});print(kind,len(leaves),flush=True)
 deps=['notes/research_three_vertex_alternating_reference_complement.md','experiments/certify_three_cap_central_complement.py','experiments/certify_three_cap_wire_complement.py','notes/research_traced_three_vertex_endpoint.md','notes/research_three_four_source_interface.md',str(reference_path.relative_to(ROOT))]
 result={'status':'passed','precision_bits':args.precision,'scope':'Full undeleted reference V3 real-index complement only; no central-current or mixed-word theorem.',
 'domain_count':len(domains),'domains':domains,'leaf_count':sum(len(d['leaves'])for d in domains),'visited':visits,'threshold':'13/20','wire':str(x),'K':str(K),
 'strict_comparison_count':len(margins),'margins':{k:str(v)for k,v in margins.items()},'elapsed_seconds':time.monotonic()-start,
 'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS',result['leaf_count'],'leaves',len(margins),'scalar comparisons')
if __name__=='__main__':main()
