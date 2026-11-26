#!/usr/bin/env python3
"""Exact source profiles; numerical optimizers propose rational tangent points only."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,time,math
import numpy as np
from scipy.special import spence
from scipy.optimize import minimize
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_right_core_support.md'
ap=argparse.ArgumentParser(description='Outward concavity bounds for right-core source support grids, including the u=1 row profile.')
ap.add_argument('--precision',type=int,default=256)
ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-core-support-grid.json')
args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision
pi=arb.pi();ii=acb(0,1)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=['notes/research_mixed_right_half_concavity.md','experiments/check_mixed_right_half_concavity.py','repro/results/research-mixed-right-half-concavity.json','notes/research_mixed_right_half_source_reduction.md','experiments/check_mixed_right_half_source_reduction.py','repro/results/research-mixed-right-half-source-reduction.json','notes/research_mixed_fourier_weight_continuation.md','notes/research_mixed_endpoint_support_grid.md']
hashes={p:sha(ROOT/p)for p in DEPS};ph=sha(PROOF);sh=sha(__file__)
for name,script,proof in [('research-mixed-right-half-concavity','check_mixed_right_half_concavity.py','research_mixed_right_half_concavity.md'),('research-mixed-right-half-source-reduction','check_mixed_right_half_source_reduction.py','research_mixed_right_half_source_reduction.md')]:
 rec=json.loads((ROOT/f'repro/results/{name}.json').read_text());assert rec['status']=='passed'
 assert rec['script_sha256']==sha(ROOT/'experiments'/script)
 assert rec['proof_sha256']==sha(ROOT/'notes'/proof)
 for key in ['dependencies','dependencies_sha256']:
  for p,v in rec.get(key,{}).items():assert sha(ROOT/p)==v,(name,p)

def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
def g(z):return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real
def gp(z):return (1-(-2*pi*ii*z).exp()).log().real
parts=[(Q(13,100),Q(1,5)),(Q(1,5),Q(11,50)),(Q(11,50),Q(1,4)),(Q(1,4),Q(2,5)),(Q(2,5),Q(1,2))]
def oldchi(x):
 return (x/Q(1,4))**2 if x<Q(1,4) else ((Q(1,2)-x)/Q(1,10))**2 if x>Q(2,5) else Q(1)
def newchi(x):
 return (x/Q(11,50))**2 if x<Q(11,50) else ((Q(1,2)-x)/Q(1,20))**2 if x>Q(9,20) else Q(1)
profiles=[]
for e,b,c in [(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)]:
 if b==0:
  for h in[Q(-3,100),Q(1,50)]:profiles.append(dict(e=e,b=b,c=c,h=str(h),sig=0,ylo='13/100',yhi='1/2',name='all3'))
 else:
  for j,(lo,hi)in enumerate(parts):
   xs=[lo,hi]+[x for x in[Q(1,4),Q(2,5),Q(11,50),Q(9,20)]if lo<=x<=hi]
   chimin=min(oldchi(x)for x in xs);chimax=max(newchi(x)for x in xs)
   for sig,hs in[(0,[-Q(57,1000)*chimax,-Q(1,50)*chimin]),(1,[Q(7,500)*chimin,Q(7,500)*chimax])]:
    for h in sorted(set(hs)):profiles.append(dict(e=e,b=b,c=c,h=str(h),sig=sig,ylo=str(lo),yhi=str(hi),name=f'part{j}'))
  # Small-angle elimination moves y to .13 at its original height.
  chi=newchi(Q(13,100))
  for sig,hs in[(0,[-Q(57,1000)*chi,Q(0)]),(1,[Q(0),Q(7,500)*chi])]:
   for h in hs:profiles.append(dict(e=e,b=b,c=c,h=str(h),sig=sig,ylo='13/100',yhi='13/100',name='small'))
def ev(u,y,p,k,q):
 e,b,c=p['e'],p['b'],p['c'];h=float(Q(p['h']));H=abs(h);hp=max(h,0);sig=p['sig']
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 lp=lambda z:np.log(abs(1-np.exp(-2j*np.pi*z)))
 cu=2*np.pi*(hp-c*h);co=np.pi*hp*(b-q/2)-b*np.pi*sig*h;kap=float(k)+q*np.pi*hp
 val=gg(.5+u)+gg(y+u-1j*H)-(1+q/2)*gg(y-1j*H)-(2+e)*gg(u)+cu*u+co-kap*y
 du=np.log(2*np.cos(np.pi*u))+lp(y+u-1j*H)-(2+e)*np.log(2*np.sin(np.pi*u))+cu
 dy=lp(y+u-1j*H)-(1+q/2)*lp(y-1j*H)-kap
 return val,np.array([du,dy])
def bound(p,k,q,pt):
 e,b,c=p['e'],p['b'],p['c'];h=Q(p['h']);H=abs(h);hp=max(h,Q(0));sig=p['sig'];lo=Q(p['ylo']);hi=Q(p['yhi']);u,y=map(Q,pt)
 cu=2*pi*ar(hp-c*h);co=pi*ar(hp)*(b-ar(Q(q,2)))-b*pi*ar(sig*h);kap=ar(k)+q*pi*ar(hp);z=acb(ar(y+u),-ar(H));w=acb(ar(y),-ar(H))
 val=g(acb(ar(Q(1,2)+u)))+g(z)-(1+ar(Q(q,2)))*g(w)-(2+e)*g(acb(ar(u)))+cu*ar(u)+co-kap*ar(y)
 du=(2*(pi*ar(u)).cos()).log()+gp(z)-(2+e)*(2*(pi*ar(u)).sin()).log()+cu
 dy=gp(z)-(1+ar(Q(q,2)))*gp(w)-kap
 sup=val+max((du*ar(x-u)).upper()for x in[Q(1,5),Q(1,2)])+max((dy*ar(x-y)).upper()for x in[lo,hi])
 return sup
def endpoint_ev(y,p,k,q):
 e,b,c=p['e'],p['b'],p['c'];h=float(Q(p['h']));hp=max(h,0);H=abs(h);sig=p['sig']
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 lp=lambda z:np.log(abs(1-np.exp(-2j*np.pi*z)))
 co=2*np.pi*(hp-c*h)+np.pi*hp*(b-q/2)-b*np.pi*sig*h;kap=float(k)+q*np.pi*hp
 return -q/2*gg(y-1j*H)+co-kap*y,-q/2*lp(y-1j*H)-kap
def endpoint_bound(p,k,q,yt):
 b,c=p['b'],p['c'];h=Q(p['h']);hp=max(h,Q(0));H=abs(h);sig=p['sig'];y=Q(yt);lo=Q(p['ylo']);hi=Q(p['yhi']);z=acb(ar(y),-ar(H))
 co=2*pi*ar(hp-c*h)+pi*ar(hp)*(b-ar(Q(q,2)))-b*pi*ar(sig*h);kap=ar(k)+q*pi*ar(hp)
 val=-ar(Q(q,2))*g(z)+co-kap*ar(y);dy=-ar(Q(q,2))*gp(z)-kap
 return val+max((dy*ar(x-y)).upper()for x in[lo,hi])
start=time.time();rows=[]
for i,p in enumerate(profiles):
 lo=float(Q(p['ylo']));hi=float(Q(p['yhi']));prev=[.28,(lo+hi)/2];vals=[]
 for k in[Q(-1,5)+Q(j,20)for j in range(10)]:
  trials=[]
  for q in sorted(set([0,p['b']])):
   if lo<hi:
    res=minimize(lambda z: (-ev(*z,p,k,q)[0],-ev(*z,p,k,q)[1]),prev,jac=True,bounds=[(.20000000001,.49999999999),(lo,hi)],method='L-BFGS-B',options=dict(ftol=1e-14,gtol=1e-11,maxiter=300))
    pp=res.x;prev=pp
   else:
    res=minimize(lambda z:(-ev(z[0],lo,p,k,q)[0],np.array([-ev(z[0],lo,p,k,q)[1][0]])),[.28],jac=True,bounds=[(.20000000001,.49999999999)],method='L-BFGS-B',options=dict(ftol=1e-14,gtol=1e-11,maxiter=300));pp=[res.x[0],lo]
   pt=[str(float(x))for x in pp];pt[1]=str(min(max(Q(pt[1]),Q(p['ylo'])),Q(p['yhi'])))
   bb=bound(p,k,q,pt);trials.append(dict(q=q,point=pt,upper=str(bb.upper())))
  endpoints=[]
  for q in sorted(set([0,p['b']])):
   if lo<hi:
    res=minimize(lambda z:(-endpoint_ev(z[0],p,k,q)[0],np.array([-endpoint_ev(z[0],p,k,q)[1]])),[(lo+hi)/2],jac=True,bounds=[(lo,hi)],method='L-BFGS-B',options=dict(ftol=1e-14,gtol=1e-11,maxiter=100));yt=str(min(max(Q(str(float(res.x[0]))),Q(p['ylo'])),Q(p['yhi'])))
   else:yt=p['ylo']
   bb=endpoint_bound(p,k,q,yt);endpoints.append(dict(q=q,point=yt,upper=str(bb.upper())))
  ub=max(arb(t['upper']).upper()for t in trials+endpoints);n=int(float(ub)*100000000)+2;up=Q(n,100000000)
  assert all(bound(p,k,t['q'],t['point'])<ar(up)for t in trials)
  assert all(endpoint_bound(p,k,t['q'],t['point'])<ar(up)for t in endpoints)
  vals.append(dict(k=str(k),upper=str(up),trials=trials,endpoint_trials=endpoints))
 rows.append(dict(**p,grid=vals))
 if i%10==9:print('profiles',i+1,len(profiles),time.time()-start,flush=True)
assert len(rows)==75 and all(len(p['grid'])==10 for p in rows)
assert hashes=={p:sha(ROOT/p)for p in DEPS};assert ph==sha(PROOF)and sh==sha(__file__)
record=dict(status='passed',precision_bits=args.precision,profiles=rows,source_profiles=len(rows),support_values=sum(len(p['grid'])for p in rows),slope_grid=[str(Q(-1,5)+Q(j,20))for j in range(10)],elapsed_seconds=time.time()-start,proof_sha256=ph,script_sha256=sh,dependencies_sha256=hashes,scope='Certified low-row core and exact u=1 source supports, with both Fourier branches and union taper-height profiles. No geometric-intercept or entire exterior assertion.')
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS source',len(rows),sum(len(p['grid'])for p in rows),time.time()-start,flush=True)
