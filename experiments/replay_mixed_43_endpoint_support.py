#!/usr/bin/env python3
"""Independent positive-frequency/sine replay of source grids and (4,3) support.

The author is not imported. Values use the positive-frequency dilogarithm;
derivatives use original sine logarithms/cotangents, and the conditional
quadratic is evaluated by the complementary reciprocal root formula.
"""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)
PI=arb.pi()
RECTS=[['27/100','33/100','-57/1000','-1/50'],['3/10','39/100','-3/100','1/50']]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(v):
 v=Q(v);return arb(v.numerator)/v.denominator
def decode(ad):
 low=[Q(0),Q(0)];high=[Q(1),Q(1)]
 for j,bit in enumerate(ad):
  assert bit in'01';k=j%2;mid=(low[k]+high[k])/2
  if bit=='0':high[k]=mid
  else:low[k]=mid
 return low,high
def cover(addresses):
 a=sorted(addresses);assert len(a)==len(set(a))
 assert all(not y.startswith(x)for x,y in zip(a,a[1:]))
 assert sum((Q(1,2**len(x))for x in a),Q(0))==1
def G(z):
 assert z.real>0 and z.real<1
 return -((2*PI*I*z).exp().polylog(2)-PI*PI/6)/(2*PI*I)+I*PI*(z-z*z)
def realG(x,H):
 x=Q(x);x-=x.numerator//x.denominator
 if x==0:return arb(0)
 return G(acb(ar(x),-ar(H))).real
def JJ(x):return realG(x,Q(0))
def J_range(lo,hi):
 xs=[lo,hi]+[Q(j)+r for j in range(-1,3)for r in[Q(1,6),Q(5,6)]if lo<=Q(j)+r<=hi]
 vv=[JJ(x)for x in xs]
 return min(v.lower()for v in vv),max(v.upper()for v in vv)
def real_first(x,H):
 z=acb(x,-ar(H));return abs(2*(PI*z).sin()).log()-PI*ar(H)
def real_second(x,H):
 z=acb(x,-ar(H));return (PI*(PI*z).cos()/(PI*z).sin()).real
def source_upper(ad,h,k,q):
 lo,hi=decode(ad);ul,xl=lo;uh,xh=hi;u=(ul+uh)/2;x=(xl+xh)/2;ru=(uh-ul)/2;rx=(xh-xl)/2
 if h==0 and not(ul>0 and uh<1 and xl>0 and xh<1 and(uh+xh<1 or ul+xl>1)):
  return J_range(ul+xl,uh+xh)[1]-(1+ar(Q(q,2)))*J_range(xl,xh)[0]-J_range(ul,uh)[0]-min((ar(k)*ar(xl)).lower(),(ar(k)*ar(xh)).lower())
 H=abs(h);hp=max(h,Q(0));sigma=int(h>0);c=1+ar(Q(q,2));cu=2*PI*ar(max(-h,Q(0)))
 constant=PI*ar(hp)*(1-ar(Q(q,2)))-PI*ar(sigma*h);kap=ar(k)+q*PI*ar(hp)
 B=realG(x+u,H)-c*realG(x,H)+cu*ar(u)+constant-kap*ar(x)
 Bu=real_first(ar(x+u),H)+cu
 Bx=real_first(ar(x+u),H)-c*real_first(ar(x),H)-kap
 U=ar(ul).union(ar(uh));X=ar(xl).union(ar(xh))
 Huu=real_second(X+U,H);Hux=Huu;Hxx=Huu-c*real_second(X,H)
 if ul>0 and uh<1:
  value=B-JJ(u);du=Bu-(2*(PI*ar(u)).sin()).log()
  Huu-=PI*(PI*U).cos()/(PI*U).sin()
 else:value=B-J_range(ul,uh)[0];du=Bu
 return value+abs(du)*ar(ru)+abs(Bx)*ar(rx)+abs(Huu)*ar(ru)**2/2+abs(Hux)*ar(ru*rx)+abs(Hxx)*ar(rx)**2/2
def edge(t,f,lo,hi):
 xl,xh,yl,yh=map(Q,RECTS[t]);p=ar(lo).union(ar(hi))
 if f in(0,2):return acb(ar(xl)+ar(xh-xl)*p,ar(yl if f==0 else yh))
 assert f in(1,3);return acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*p)
def tangent(t,f):
 xl,xh,yl,yh=map(Q,RECTS[t]);return acb(ar(xh-xl))if f in(0,2)else I*ar(yh-yl)
def GP(z):
 assert z.real>0 and z.real<1
 return (2*(PI*z).sin()).log()+I*PI*(1-2*z)/2
def GPP(z):return PI*(PI*z).cos()/(PI*z).sin()-PI*I
def critical(a,b):
 A=(-2*PI*I*a).exp();B=(-2*PI*I*b).exp();disc=((A-B)**2-4*A*(B-1)*(1-A)).sqrt()
 choices=[]
 for sign in[-1,1]:
  U=2*(1-A)/(B-A-sign*disc)
  s=I*U.log()/(2*PI)
  if not(s.real>ar('1/5')and s.real<ar('11/25')and abs(s.imag)<ar('3/20')):continue
  residual=GP(s+a)+GP(s+b)-2*GP(s)+2*PI*I*a
  if abs(residual)<1:choices.append(s)
 if len(choices)!=1:return None
 return choices[0]
def phase(a,b,with_value=False):
 s=critical(a,b)
 if s is None:return None
 da=GP(s+a)+2*PI*I*s-ar('3/2')*GP(a);db=GP(s+b)-GP(b)
 ss=GPP(s+a)+GPP(s+b)-2*GPP(s);sa=GPP(s+a)+2*PI*I;sb=GPP(s+b)
 aa=GPP(s+a)-ar('3/2')*GPP(a)-sa*sa/ss;ab=-sa*sb/ss;bb=GPP(s+b)-GPP(b)-sb*sb/ss
 f=G(s+a)+G(s+b)-2*G(s)+2*PI*I*a*s-ar('3/2')*G(a)-G(b)if with_value else None
 return f,da,db,aa,ab,bb
def references(ad,faces):
 lo,hi=decode(ad);p=[edge(j,faces[j],lo[j],hi[j])for j in(0,1)]
 mid=[edge(j,faces[j],(lo[j]+hi[j])/2,(lo[j]+hi[j])/2)for j in(0,1)]
 rad=[ar((hi[j]-lo[j])/2)for j in(0,1)]
 return p,mid,rad
def slope_ok(ad,faces):
 pp,_,_=references(ad,faces);v=phase(*pp)
 return v is not None and v[1].real>ar('-2/5')and v[1].real<ar('3/10')
def geometry_ok(ad,faces,grid):
 (a,b),(a0,b0),(ra,rb)=references(ad,faces)
 vv=phase(a,b);mm=phase(a0,b0,True)
 if vv is None or mm is None:return False
 _,da,db,aa,ab,bb=vv;f0,da0,db0,*_=mm;k=da.real
 if not(k>ar('-2/5')and k<ar('3/10')):return False
 va,vb=[tangent(j,faces[j])for j in(0,1)]
 def upper(alpha,beta,h,e):
  C=f0-a0*da0+(e-b0)*db0+I*ar(h)*da0
  la=(ar(alpha)+a-I*ar(h))*aa-(e-b)*ab
  lb=(ar(alpha)+a-I*ar(h))*ab-(e-b)*bb
  return (ar(alpha)*da0+beta-C).real+abs((la*va).real)*ra+abs((lb*vb).real)*rb
 for h,rows in grid.items():
  for e in(0,1):
   used=0
   for r1,r2 in zip(rows,rows[1:]):
    kl,kh=Q(r1['kappa']),Q(r2['kappa'])
    if k<ar(kl)or k>ar(kh):continue
    used+=1;alpha=(Q(r2['upper'])-Q(r1['upper']))/(kh-kl);beta=Q(r1['upper'])-alpha*kl
    if not upper(alpha,ar(beta),h,e)<ar('-1/1000'):return False
   assert used
 for sigma,hs in[(0,[Q(-57,1000),Q(0)]),(1,[Q(0),Q(7,500)])]:
  for h in hs:
   source=-2*PI*ar(h)if sigma==0 else ar('1/20')
   for x in(0,1):
    for e in(0,1):
     if not upper(Q(-x),source,h,e)<ar('-1/1000'):return False
 return True
def verify_addresses(addresses,fn):
 cover(addresses);accepted=[];refinements=0
 for original in addresses:
  todo=[original]
  while todo:
   a=todo.pop()
   try:ok=fn(a)
   except(ValueError,ZeroDivisionError):ok=False
   if ok:accepted.append(a)
   else:
    assert len(a)<len(original)+12,a
    refinements+=1;todo.extend([a+'1',a+'0'])
 cover(accepted)
 return len(accepted),refinements
def main():
 global PI
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-43-endpoint-support-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;PI=arb.pi()
 paths=[ROOT/'repro/results/research-mixed-endpoint-support-grid.json',ROOT/'repro/results/research-mixed-43-endpoint-support.json']
 raw=[p.read_bytes()for p in paths];source,geom=map(json.loads,raw)
 initial={}
 for d,script,proof in[(source,'check_mixed_endpoint_support_grid.py','research_mixed_endpoint_support_grid.md'),(geom,'check_mixed_43_endpoint_support.py','research_mixed_43_endpoint_support.md')]:
  assert d['status']=='passed'
  assert d['script_sha256']==sha(ROOT/'experiments'/script)
  assert d['proof_sha256']==sha(ROOT/'notes'/proof)
  for p,v in d['dependencies'].items():assert sha(ROOT/p)==v
  initial.update(d['dependencies']);initial['experiments/'+script]=d['script_sha256'];initial['notes/'+proof]=d['proof_sha256']
 assert geom['source_input_sha256']==hashlib.sha256(raw[0]).hexdigest()
 assert source['source_grid_count']==60 and geom['case_count']==16
 assert [[Q(x)for x in r]for r in source['reference_rectangles']]==[[Q(x)for x in r]for r in RECTS]
 assert geom['reference_rectangles']==source['reference_rectangles']
 assert Q(geom['gap'])==Q(1,1000)
 assert Q(geom['raw_positive_seam_rate'])==Q(1,20)
 assert 1-(-7*PI/250).exp()<ar('1/10')
 expected={(h,Q(-2,5)+Q(j,20))for h in[Q(-57,1000),Q(-1,50),Q(0),Q(7,500)]for j in range(15)}
 assert {(Q(r['height']),Q(r['kappa']))for r in source['source_grid']}==expected
 assert len(source['source_grid'])==60
 script_hash=sha(__file__);start=time.time();counts={'source':0,'slope':0,'geometry':0};refined=0;details=[]
 for row in source['source_grid']:
  h,k=Q(row['height']),Q(row['kappa']);target=ar(row['upper'])
  assert row['selected_alias']==int(h>0)
  n,r=verify_addresses(row['addresses'],lambda a:all(source_upper(a,h,k,q)<target for q in(0,1)))
  counts['source']+=n;refined+=r;details.append({'kind':'source','height':str(h),'kappa':str(k),'cells':n,'refinements':r})
  print('source',str(h),str(k),n,r,flush=True)
 expected_faces={(a,b)for a in range(4)for b in range(4)}
 for cases in[source['slope_boundary'],geom['cases']]:
  assert len(cases)==16 and {tuple(r['faces'])for r in cases}==expected_faces
 for row in source['slope_boundary']:
  n,r=verify_addresses(row['addresses'],lambda a:slope_ok(a,row['faces']))
  counts['slope']+=n;refined+=r;details.append({'kind':'slope','faces':row['faces'],'cells':n,'refinements':r});print('slope',row['faces'],n,r,flush=True)
 grid={h:sorted([r for r in source['source_grid']if Q(r['height'])==h],key=lambda r:Q(r['kappa']))for h in[Q(-57,1000),Q(-1,50),Q(0),Q(7,500)]}
 for row in geom['cases']:
  n,r=verify_addresses(row['addresses'],lambda a:geometry_ok(a,row['faces'],grid))
  counts['geometry']+=n;refined+=r;details.append({'kind':'geometry','faces':row['faces'],'cells':n,'refinements':r});print('geometry',row['faces'],n,r,flush=True)
 assert raw==[p.read_bytes()for p in paths]
 assert initial=={p:sha(ROOT/p)for p in initial}
 assert script_hash==sha(__file__)
 out={'status':'passed','precision_bits':args.precision,'counts':counts,'refinements':refined,'details':details,
      'source_input_sha256':hashlib.sha256(raw[0]).hexdigest(),'geometry_input_sha256':hashlib.sha256(raw[1]).hexdigest(),
      'script_sha256':script_hash,'dependencies':initial,'elapsed_seconds':time.time()-start,
      'analytic_independence':'Positive-frequency primitive, sine/cotangent derivatives and complementary reciprocal quadratic root; no author implementation imported.',
      'scope':geom['scope']}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',counts,'refinements',refined,flush=True)
if __name__=='__main__':main()
