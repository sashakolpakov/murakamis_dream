"""Incomplete bounded outward prototype; not a completed certificate."""
import importlib.util,json,time,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'experiments/certify_mixed_minimum_level_half_stencils.py'
spec=importlib.util.spec_from_file_location('helper',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.configure(256)
ar=m.ar;ii=m.ii;pi=m.pi;gp=m.m.core.gp;gpp=m.gpp

def params(v):
 t=ar('.12')+ar('.10')*v[0];rho=(t-ar('.1'))/ar('.12')
 y=t+(ar('.45')-t)*v[1];cc=ar('-.053')+ar('.017')*v[2];cn=ar('-.025')+ar('.014')*v[3]
 a=acb(t,cc*rho);b=acb(y,cn*rho)
 ap=[ar('.1')+ii*cc*ar(F(5,6)),acb(0),ii*ar('.017')*rho,acb(0)]
 bp=[ar('.1')*(1-v[1])+ii*cn*ar(F(5,6)),acb(ar('.45')-t),acb(0),ii*ar('.014')*rho]
 return a,b,cc,cn,ap,bp

def T(u,b):return (gp(acb(u+ar('.5')))+gp(b+u)-3*gp(acb(u))+2*pi*ii*b).real

def row(b,b0):
 lo,hi=F(1,5),F(2,5)
 for k in range(20):
  mid=(lo+hi)/2;v=T(ar(mid),b0)
  if v>0:lo=mid
  elif v<0:hi=mid
  else:break
 u0=ar((lo+hi)/2);rad=(abs(T(u0,b))/(2*pi)).upper()
 return (u0+arb(0,rad)).intersection(ar(F(1,5)).union(ar(F(2,5))))

def test(box,switch):
 v=[ar(lo).union(ar(hi)) for lo,hi in box];vm=[ar((lo+hi)/2) for lo,hi in box]
 a,b,cc,cn,ap,bp=params(v);a0,b0,cc0,cn0,_,_=params(vm)
 packet=m.root_box(a,b,a0,b0,0)
 if packet is None:return None,None,None
 s,s0,wit=packet
 if not F(0)<F(wit['radius'])<=F(1,20):return None,None,None
 G,H=m.gradH(s,a,b,1,0);G0,H0=m.gradH(s0,a0,b0,1,0)
 if not all(z.is_finite() for z in G+G0+[z for r in H+H0 for z in r]):return None,None,None
 u=row(b,b0);u0=row(b0,b0)
 K=gp(b+u)-gp(b)+2*pi*ii*u;K0=gp(b0+u0)-gp(b0)+2*pi*ii*u0
 Kz=gpp(b+u)-gpp(b);Ku=gpp(b+u)+2*pi*ii
 Tu=(gpp(acb(u+ar('.5')))+gpp(b+u)-3*gpp(acb(u))).real
 if not Tu.is_finite():return None,None,None
 Tu=Tu.intersection(Tu.lower().union((-2*pi).upper()))
 if not Tu<0:return None,None,None
 up=[-(Ku*z).real/Tu for z in bp]
 lows=[];grads=[]
 for chi in (switch[0],):
  for xi in (switch[1],):
   q=1+ii*chi*cc/ar('.12');v=ii*xi*cn/ar('.12')
   q0=1+ii*chi*cc0/ar('.12');v0=ii*xi*cn0/ar('.12')
   qp=[acb(0),acb(0),ii*chi*ar('.017')/ar('.12'),acb(0)]
   vp=[acb(0),acb(0),acb(0),ii*xi*ar('.014')/ar('.12')]
   direct=(q*(G[0]-ii*ar('1.5'))+v*(G[1]+K)).real
   point=(q0*(G0[0]-ii*ar('1.5'))+v0*(G0[1]+K0)).real
   grad=[(dq*(G[0]-ii*ar('1.5'))+q*(H[0][0]*da+H[0][1]*db)+dv*(G[1]+K)+v*(H[1][0]*da+H[1][1]*db+Kz*db+Ku*du)).real for da,db,dq,dv,du in zip(ap,bp,qp,vp,up)]
   if not all(z.is_finite() for z in [direct,point]+grad):return None,None,None
   bound=point-sum((abs(z)*ar((hi-lo)/2) for z,(lo,hi) in zip(grad,box)),arb(0))
   lows.append(max(direct.lower(),bound.lower()));grads.append(grad)
 return min(lows),grads,wit

ap=argparse.ArgumentParser();ap.add_argument('--max-visits',type=int,default=1023);ap.add_argument('--seconds',type=float,default=10);args=ap.parse_args()
monotonic=0
start=time.monotonic();stack=[((chi,xi),[(F(0),F(1))]*4) for chi in (0,1) for xi in (0,1)];nodes=[];leaves=visits=0;lowest=None;remaining=0
while stack and visits<args.max_visits and time.monotonic()-start<args.seconds:
 switch,box=stack.pop();visits+=1
 low,grads,wit=test(box,switch)
 if low is not None and low>0:
  leaves+=1;lowest=low if lowest is None else min(lowest,low);nodes.append(['L',list(switch),wit]);continue
 if grads is not None:
  choices=[]
  for j,(lo,hi) in enumerate(box):
   if lo==hi:continue
   if all(g[j]>0 for g in grads):choices.append((j,0))
   elif all(g[j]<0 for g in grads):choices.append((j,1))
  if choices:
   axis,bit=choices[0];lo,hi=box[axis];value=(lo,hi)[bit]
   child=list(box);child[axis]=(value,value);stack.append((switch,child))
   nodes.append(['M',list(switch),axis,bit,wit]);monotonic+=1;continue
 if grads is None:
  *_,aa,bb=params([ar((lo+hi)/2) for lo,hi in box])
  axis=max((((abs(aa[j])+abs(bb[j]))*ar(hi-lo)).upper(),j) for j,(lo,hi) in enumerate(box))[1]
 else:axis=max((max((abs(g[j])*ar(hi-lo)).upper() for g in grads),j) for j,(lo,hi) in enumerate(box))[1]
 nodes.append(['S',list(switch),axis]);lo,hi=box[axis];mid=(lo+hi)/2
 for pair in [(lo,mid),(mid,hi)]:
  child=list(box);child[axis]=pair;stack.append((switch,child))
result=dict(status='passed' if not stack else 'incomplete',maximum_visits=args.max_visits,time_limit_seconds=args.seconds,accepted=leaves,monotonic=monotonic,visits=visits,remaining=len(stack),pending=[dict(switch=list(sw),box=[[str(a),str(b)] for a,b in bx]) for sw,bx in stack],seconds=time.monotonic()-start,min_lower=str(lowest),nodes=nodes,scope='Bounded prototype only: all four unselected switches for right half word1101 on t[.12,.22],y[t,.45],cc[-.053,-.036],cn[-.025,-.011]. No independent replay or other class.',inputs={str(p):hashlib.sha256(p.read_bytes()).hexdigest(),__file__:hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
Path(__file__).with_name('probe_result.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k not in ['nodes','inputs','pending']})
