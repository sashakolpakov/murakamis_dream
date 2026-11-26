#!/usr/bin/env python3
"""Independent primitive and exact-cover replay of central cap remainders."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import positive_primitive,partition
from replay_three_vertex_directed_packet import action
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
def fixed():return arb.pi(),arb('.10135867').union(arb('.10135871')),arb('.97895508').union(arb('.97895512'))
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
def indices(key,p):
 pi,h,H=fixed();x=acb(arb(7)/50+arb(3)/50*p[0],h);y=acb(arb(1)/6,arb(2).log()/(2*pi))
 X=(2*pi*ii*x).exp();Y=(2*pi*ii*y).exp()
 ends=[(R(0),R(1,50),R(1,50)),(R(1,50),R(1,4),R(0)),(R(9,20),R(9,20),R(0))]
 lo,hi,tl=map(r,ends[key[2]]);s=lo+(hi-lo)*p[1];t=tl+(arb(99)/100-s-tl)*p[2]
 if key[1]:s,t=t,s
 return x,y,X,Y,s,t,hi-lo,tl
def val(key,p):
 x,y,X,Y,s,t,_,_=indices(key,p)
 return(action(s,t,X,Y)-arb.pi()*ii*(x+y)).real
def checked(key,box):
 p=[iv(a,b)for a,b in box];c=[r((a+b)/2)for a,b in box];width=[r((b-a)/2)for a,b in box]
 if key[0]!='index':
  v=cap(key,p);target=arb(253)/200 if key[0]=='capcentral'else(arb(2)/3 if key[0]=='capradical'else arb(63)/50)
  if key[0]=='capcentral'or(key[0]=='capcontour'and key[1]<2):
   pi,h,H=fixed();x=acb(arb(7)/50+arb(3)/50*p[0],h)
   if key[0]=='capcentral':a=arb(0);d=arb(9)/5
   elif key[1]==0:a=-arb(41)/20;d=arb(41)/20
   else:a=arb(9)/5;d=arb(1)/4
   t=acb(a+d*p[1],-H);lp=(pi*x+t/2).cos().log();lm=(pi*x-t/2).cos().log()
   gx=(lp+lm-2*(pi*x).sin().log()).real*arb(3)/50
   gt=((lp-lm)/(2*pi)-((t/2).tan()+1/(t/2).cos()).log()/pi+3*ii*t/(2*pi)-ii).real*d
   m=cap(key,c)+width[0]*ab(gx)+width[1]*ab(gt)
   if m.upper()<v.upper():v=m
  return v<target
 direct=val(key,p);x,y,X,Y,s,t,ds,tl=indices(key,p);pi=arb.pi()
 U=(-2*pi*ii*s).exp();V=(-2*pi*ii*t).exp()
 fs=(X.log()+(1-U*V).log()-(1-X*U).log()).real
 ft=(Y.log()+(1-U*V).log()-(1-Y*V).log()).real
 gx=((1-X*U).log()-(1-X).log()).real*arb(3)/50
 if key[1]:fs,ft=ft,fs;s,t=t,s
 deriv=[gx,ds*(fs-p[2]*ft),(arb(99)/100-s-tl)*ft]
 m=val(key,c)+sum(w*ab(g)for w,g in zip(width,deriv))
 if m.upper()<direct.upper():direct=m
 return direct<arb(16)/25
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--output',default='repro/results/research-three-cap-central-complement-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();path=ROOT/'repro/results/research-three-cap-central-complement.json';data=json.loads(path.read_text());assert data['status']=='passed'
 expected={('capcentral',):2,('captail',):1,('capradical',):1}
 expected.update({('capcontour',k):2 for k in range(6)})
 expected.update({('index',s,k):3 for s in range(2)for k in range(3)})
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
 pi,h,H=fixed();rr=arb(27)/50;yh=arb(2).log()/(2*pi)
 margins=[rr-(-2*pi*h).exp(),h-arb(9)/100,arb(3)/25-h,H-arb(97)/100,1-H,
          -arb(3)/5-rr.log(),arb(2)/3-rr-rr**2/4-rr**3/(9*(1-rr)),
          arb(10)/3-arb(25).log(),arb(7)/10-pi*(h+yh),
          arb(16)/25+arb(3)/5*arb(99)/100-arb(4)/9-arb(13)/300-arb(7)/10,
          (1+rr*rr).sqrt()-2*rr,1-rr-rr*pi/4,arb(3)/4-arb(7)/8+arb(7)/50,
          arb(19113)/10000-arb(253)/200-arb(16)/25-arb(1)/200,
          arb(19113)/10000-arb(63)/50-arb(3237)/5000-arb(3)/1000]
 assert all(z>0 for z in margins)and R(9,20)-R(1,5)==R(1,4)
 for f,hsh in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==hsh,f
 assert sha256((ROOT/'experiments/certify_three_cap_central_complement.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
         'original_leaf_count':original,'replayed_leaf_count':refined,'visited':visits,
         'strict_scalar_comparisons':len(margins),'rational_identities':1,'exact_binary_cover':True,
         'elapsed_seconds':time.monotonic()-start,'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'primitive':'Negative-frequency retained action and reflected positive-strip cap primitive; no author imports.'}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
