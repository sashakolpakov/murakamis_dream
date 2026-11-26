#!/usr/bin/env python3
"""Independent cap primitive and exact-cover replay for the direct three-chain complements."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import positive_primitive,partition
ROOT=Path(__file__).resolve().parents[1];ii=acb(0,1)
def r(q):return arb(q.numerator)/q.denominator if isinstance(q,R)else arb(q)
def iv(a,b):return r(a).union(r(b))
def ab(v):return max(abs(v.lower()),abs(v.upper()))
def jr(z):
 z=acb(z);a=z.real;b=abs(z.imag);radius=abs(z).upper();p=arb.pi()
 if a.contains(0)and b.contains(0)and radius<arb(1)/20:
  if radius==0:return arb(0)
  return arb(0,(radius*(-(2*p*radius).log()+p+1+arb(1)/199)).upper())
 if a>=0:return positive_primitive(a,b)
 if a<=0:return -positive_primitive(-a,b)-p*b
 return positive_primitive(arb(0).union(a.upper()),b).union(-positive_primitive(arb(0).union(-a.lower()),b)-p*b)
def bb(x,t):return -jr(arb(1)/2-x+t/(2*arb.pi()))-jr(arb(1)/2-x-t/(2*arb.pi()))-2*jr(x)
def edge(t):return -4*jr(arb(1)/4+t/(4*arb.pi()))-4*jr(arb(1)/4-t/(4*arb.pi()))
def fixed():
 p=arb.pi();return p,arb(2).log()/(2*p),arb(24961509)/25000000
def cap(key,p):
 pi,h,H=fixed();x=acb(arb(7)/50+arb(3)/50*p[0],h);T=arb(41)/20
 if key[0]=='captail':return bb(x,acb(T))+edge(acb(T))
 if key[0]=='capradical':return bb(x,acb(0))
 if key[0]=='capcentral':t=acb(arb(9)/5*p[1],-H)
 elif key[1]<2:t=acb(-T+T*p[1]if key[1]==0 else arb(9)/5+(T-arb(9)/5)*p[1],-H)
 else:
  L=2*pi*h;v=L*p[1]if key[1]%2==0 else L+(H-L)*p[1]
  t=acb(T if key[1]<4 else -T,-v)
 return bb(x,t)+edge(t)+3*t.real*(-t.imag)/(2*pi)+t.imag
def checked(key,box):
 p=[iv(a,b)for a,b in box];c=[r((a+b)/2)for a,b in box];width=[r((b-a)/2)for a,b in box]
 if key[0]!='index':
  v=cap(key,p);target=arb(1267)/1000 if key[0]=='capcentral'else(arb(2)/3 if key[0]=='capradical'else arb(63)/50)
  if key[0]=='capcentral'or(key[0]=='capcontour'and key[1]<2):
   pi,h,H=fixed();x=acb(arb(7)/50+arb(3)/50*p[0],h)
   if key[0]=='capcentral':a=arb(0);d=arb(9)/5
   elif key[1]==0:a=-arb(41)/20;d=arb(41)/20
   else:a=arb(9)/5;d=arb(1)/4
   t=acb(a+d*p[1],-H);lp=(pi*x+t/2).cos().log();lm=(pi*x-t/2).cos().log()
   gx=(lp+lm-2*(pi*x).sin().log()).real*arb(3)/50
   gt=((lp-lm)/(2*pi)-(t/2).tan().asinh()/pi+3*ii*t/(2*pi)-ii).real*d
   m=cap(key,c)+width[0]*ab(gx)+width[1]*ab(gt)
   if m.upper()<v.upper():v=m
  return v<target
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--output',default='repro/results/research-three-chain-three-complements-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();path=ROOT/'repro/results/research-three-chain-three-complements.json';data=json.loads(path.read_text());assert data['status']=='passed'
 expected={('capcentral',):2,('captail',):1,('capradical',):1}
 expected.update({('capcontour',k):2 for k in range(6)})
 seen=set();original=refined=visits=0
 for dom in data['domains']:
  key=tuple(dom['domain']);assert key in expected and key not in seen and dom['dimension']==expected[key];seen.add(key)
  for box in partition(dom['leaves'],dom['dimension']):
   original+=1;todo=[box]
   while todo:
    current=todo.pop();visits+=1
    if checked(key,current):refined+=1;continue
    axis=max(range(len(current)),key=lambda j:current[j][1]-current[j][0]);a,b=current[axis];assert b-a>R(1,2**27),(key,current);mid=(a+b)/2
    for ends in ((a,mid),(mid,b)):
     child=list(current);child[axis]=ends;todo.append(tuple(child))
    assert visits<300000,'Replay unfinished'
 assert seen==set(expected)and original==data['leaf_count']
 p,h,H=fixed();c=arb(161533)/500000;M=arb(63519)/20000
 margins={
  'wire lower':h-arb(9)/100,'wire upper':arb(3)/25-h,
  'angle lower':H-arb(97)/100,'angle upper':1-H,
  'real color compact half-plane':2+2*(arb(41)/20).cos()*H.cosh(),
  'small primitive bound':arb(1)/200-(20*(p/20).sinh()/p-1),
  'small p left endpoint':arb(623)/1000-arb(2).log()-((p/20).log()-1)/40,
  'small p right endpoint':arb(623)/1000-arb(2).log()+arb(8)/75,
  'smaller coordinate increases':(p/4).cos()-arb(1)/2,
  'index diagonal curvature':p*(arb(9)*p/20).sin()/(arb(5)/2-2*(arb(9)*p/20).cos())-arb(7)/5,
  'curvature decreases':arb(4)/5-(p/4).cos(),
  'full real index complement':arb(6413)/10000-2*c+arb(7)/1440,
  'small p compared to complement':arb(6413)/10000-arb(623)/1000,
  'single exterior pair':M-arb(158)/125-arb(38233)/20000-arb(1)/4000,
  'double exterior pair':M-arb(316)/125-2*c-arb(1)/1000,
  'Fourier corner in exterior':M-arb(158)/125-arb(343)/200,
  'two caps index complement':M-arb(1267)/500-arb(6413)/10000-arb(3)/5000,
  'one remainder with coherent factor':M-arb(63)/50-arb(957)/500-arb(1)/1000,
  'two remainders':M-arb(63)/25-2*c-arb(1)/200,
  'index side':M-arb(317)/100-arb(1)/200,
  'nonconstant mode':arb(78)/25-arb(1591)/500+p/50,
  'initial connecting face':M-arb(1587)/500-arb(1)/1000,
  'ordinary corner':3-5*c-arb(550)/471-arb(27)/200}
 for name,value in margins.items():assert value>0,(name,value)
 identities={'curvature loss':R(7,10)*R(1,12)**2==R(7,1440),
             'initial depth':R(24961509,25000000)==R('.99846036')}
 assert all(identities.values())
 for suffix,script in (('', 'check_three_chain_three_central_currents.py'),
                       ('-replay','replay_three_chain_three_central_currents.py')):
  cp=ROOT/f'repro/results/research-three-chain-three-central-currents{suffix}.json'
  record=json.loads(cp.read_text());assert record['status']=='passed'and record['support_plane_count']==28
  assert record['script_sha256']==sha256((ROOT/'experiments'/script).read_bytes()).hexdigest()
  for dep,digest in record['dependencies_sha256'].items():assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,dep
  if suffix:
   ap=ROOT/'repro/results/research-three-chain-three-central-currents.json'
   assert record['artifact_sha256']==sha256(ap.read_bytes()).hexdigest()and record['exact_domain_cover'] is True
 for f,hsh in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==hsh,f
 assert sha256((ROOT/'experiments/certify_three_chain_three_complements.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
         'original_leaf_count':original,'replayed_leaf_count':refined,'visited':visits,
         'strict_scalar_comparisons':len(margins),'scalar_margins':{k:str(v)for k,v in margins.items()},'rational_identities':len(identities),'exact_binary_cover':True,
         'elapsed_seconds':time.monotonic()-start,'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'primitive':'Reflected positive-strip sine primitive and independent inverse-asinh angular derivative; no author imports.',
         'checked_central_provenance_records':2,'author_script_sha256':data['script_sha256'],'checked_dependency_count':len(data['dependencies_sha256']),
         'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in
           ['experiments/replay_three_cap_wire_complement.py','notes/research_three_chain_three_closure.md']}}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
