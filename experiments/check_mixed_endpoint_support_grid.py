#!/usr/bin/env python3
"""Certified convex source support grids for the (4,3) tapered endpoint.

Floating optimization proposes upper targets only; exact dyadic interval
covers of both full Fourier branches decide every acceptance.
"""
import argparse,hashlib,json,math,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.special import spence
from scipy.optimize import differential_evolution
from flint import arb,acb,ctx
ctx.prec=160
pi=arb.pi();ii=acb(0,1)
ar=lambda v:arb(Q(v).numerator)/Q(v).denominator
def g(z):return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real
def J(u):
 u=Q(u);u-=u.numerator//u.denominator
 if u==0:return arb(0)
 return g(acb(ar(u)))
def Jrange(lo,hi):
 points=[lo,hi]+[Q(k)+c for k in range(-1,3)for c in[Q(1,6),Q(5,6)]if lo<=Q(k)+c<=hi]
 values=[J(v)for v in points]
 return min(v.lower()for v in values),max(v.upper()for v in values)
def gp(z):return (1-(-2*pi*ii*z).exp()).log().real
def gpp(z):
 E=(-2*pi*ii*z).exp();return (2*pi*ii*E/(1-E)).real
def bounds(box,h,k,q):
 ul,uh,xl,xh=box;u=(ul+uh)/2;x=(xl+xh)/2;ru=(uh-ul)/2;rx=(xh-xl)/2
 if h==0 and not(ul>0 and uh<1 and xl>0 and xh<1 and(uh+xh<1 or ul+xl>1)):
  jm=Jrange(ul,uh)[0];xm=Jrange(xl,xh)[0];sm=Jrange(ul+xl,uh+xh)[1]
  return sm-(1+ar(Q(q,2)))*xm-jm-min((ar(k)*ar(xl)).lower(),(ar(k)*ar(xh)).lower())
 U=ar(ul).union(ar(uh));X=ar(xl).union(ar(xh));H=abs(h);hp=max(h,Q(0));sigma=int(h>0)
 cu=2*pi*ar(max(-h,Q(0)));const=pi*ar(hp)*(1-ar(Q(q,2)))-pi*ar(sigma*h)
 kap=ar(k)+q*pi*ar(hp)
 zz=acb(ar(x+u),-ar(H));xx=acb(ar(x),-ar(H))
 c=1+ar(Q(q,2))
 B=g(zz)-c*g(xx)+cu*ar(u)+const-kap*ar(x)
 Bu=gp(zz)+cu;Bx=gp(zz)-c*gp(xx)-kap
 huu=gpp(acb(X+U,-ar(H)));hux=huu;hxx=huu-c*gpp(acb(X,-ar(H)))
 if ul>0 and uh<1:
  val=B-J(u);du=Bu-(2*(pi*ar(u)).sin()).log()
  huu=huu-pi*(pi*U).cos()/(pi*U).sin()
  out=val+abs(du)*ar(ru)+abs(Bx)*ar(rx)+abs(huu)*ar(ru)**2/2+abs(hux)*ar(ru*rx)+abs(hxx)*ar(rx)**2/2
 else:
  mins=[J(ul).lower(),J(uh).lower()]
  if ul<=Q(1,6)<=uh:mins.append(J(Q(1,6)).lower())
  out=B-min(mins)+abs(Bu)*ar(ru)+abs(Bx)*ar(rx)+abs(huu)*ar(ru)**2/2+abs(hux)*ar(ru*rx)+abs(hxx)*ar(rx)**2/2
 return out
def propose(h,k):
 hf=float(h);kf=float(k);H=abs(hf);hp=max(hf,0);sig=int(h>0)
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 JJ=lambda u:0 if u in [0,1]else gg(u+0j)
 def ev(u,x,q):return gg(x+u-1j*H)-(1+q/2)*gg(x-1j*H)-JJ(u)+2*np.pi*max(-hf,0)*u+np.pi*hp*(1-q/2)-np.pi*sig*hf-(kf+q*np.pi*hp)*x
 vals=[]
 for q in [0,1]:
  a=differential_evolution(lambda z:-ev(*z,q),[(1e-12,1-1e-12),(0,1)],seed=32,popsize=8,maxiter=100,tol=1e-9)
  vals.append((ev(*a.x,q),a.x.tolist(),q))
  vals.extend((ev(u,x,q),[u,x],q)for u in[0,1]for x in[0,1])
 best=max(vals,key=lambda v:v[0]);target=Q(math.ceil((best[0]+.0004)*1000000),1000000)
 return target,best
def decode(addr):
 b=[Q(0),Q(1),Q(0),Q(1)]
 for j,bit in enumerate(addr):
  k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(bit)]=mid
 return b

rects=[['27/100','33/100','-57/1000','-1/50'],['3/10','39/100','-3/100','1/50']]
def edge(k,f,lo,hi):
 xl,xh,yl,yh=map(Q,rects[k]);v=ar(lo).union(ar(hi))
 return acb(ar(xl)+(ar(xh)-ar(xl))*v,ar(yl if f==0 else yh))if f in[0,2]else acb(ar(xh if f==1 else xl),ar(yl)+(ar(yh)-ar(yl))*v)
def slope_box(ad):
 b=[Q(0),Q(1),Q(0),Q(1)]
 for j,bit in enumerate(ad):
  k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(bit)]=mid
 return b
def test(ad,fa,fb):
 al,ah,bl,bh=slope_box(ad);a=edge(0,fa,al,ah);b=edge(1,fb,bl,bh);A=(-2*pi*ii*a).exp();B=(-2*pi*ii*b).exp()
 root=((A-B)**2-4*A*(B-1)*(1-A)).sqrt()
 choices=[]
 for sign in[-1,1]:
  U=(B-A+sign*root)/(2*A*(B-1));st=ii*U.log()/(2*pi)
  if not(st.real>ar('1/5')and st.real<ar('11/25')and abs(st.imag)<ar('3/20')):continue
  gp=lambda z:(1-(-2*pi*ii*z).exp()).log()
  f=gp(st+a)+gp(st+b)-2*gp(st)+2*pi*ii*a
  if not abs(f)<1:continue
  k=(gp(st+a)+2*pi*ii*st-ar('3/2')*gp(a)).real
  if k>ar('-2/5')and k<ar('3/10'):choices.append(k)
 return len(choices)==1

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_endpoint_support_grid.md'
DEPS=['notes/research_mixed_angular_support_candidates.md',
      'notes/research_mixed_boundary_strip_bounds.md',
      'notes/research_mixed_right_half_concavity.md',
      'notes/research_mixed_central_conditional_rectangles.md',
      'notes/research_mixed_type_four_height_refinement.md',
      'repro/results/research-mixed-type-four-height-refinement.json',
      'repro/results/research-mixed-type-four-height-refinement-replay.json']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 global pi
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-endpoint-support-grid.json')
 args=ap.parse_args();ctx.prec=args.precision;pi=arb.pi()
 initial={p:sha(ROOT/p)for p in DEPS};ph=sha(PROOF);sh=sha(__file__)
 for p in DEPS[-2:]:assert json.loads((ROOT/p).read_text())['status']=='passed'
 a=json.loads((ROOT/DEPS[-2]).read_text());r=json.loads((ROOT/DEPS[-1]).read_text())
 assert a['script_sha256']==sha(ROOT/'experiments/certify_mixed_type_four_height_refinement.py')
 assert r['script_sha256']==sha(ROOT/'experiments/replay_mixed_type_four_height_refinement.py')
 assert r['input_sha256']==sha(ROOT/DEPS[-2])
 for d in[a,r]:
  assert d['proof_sha256']==sha(ROOT/'notes/research_mixed_type_four_height_refinement.md')
  for f,v in d['dependencies'].items():assert sha(ROOT/f)==v
 rows=[];start=time.time()
 for h in [Q(-57,1000),Q(-1,50),Q(0),Q(7,500)]:
  for k in [Q(-2,5)+Q(j,20)for j in range(15)]:
   target,best=propose(h,k);stack=[''];yes=[];vis=0;least=None
   while stack:
    addr=stack.pop();bb=decode(addr);vis+=1
    assert len(addr)<40,(h,k,addr)
    try:
     values=[bounds(bb,h,k,q)for q in[0,1]]
     ok=all(v<ar(target)for v in values)
    except(ValueError,ZeroDivisionError):ok=False
    if ok:
     yes.append(addr);margin=min((ar(target)-v).lower()for v in values)
     least=margin if least is None else min(least,margin)
    else:stack.extend([addr+'1',addr+'0'])
   yes.sort();assert len(set(yes))==len(yes)
   assert all(not b.startswith(a)for a,b in zip(yes,yes[1:]))
   assert sum((Q(1,2**len(a))for a in yes),Q(0))==1
   row={'height':str(h),'selected_alias':int(h>0),'kappa':str(k),'upper':str(target),
        'accepted':len(yes),'visited':vis,'minimum_interval_reserve':str(least),'addresses':yes}
   rows.append(row)
   print(json.dumps({z:v for z,v in row.items()if z!='addresses'}),flush=True)
 slopes=[]
 for fa in range(4):
  for fb in range(4):
   stack=[''];yes=[];vis=0
   while stack:
    ad=stack.pop();vis+=1;assert len(ad)<24,(fa,fb,ad)
    try:ok=test(ad,fa,fb)
    except(ValueError,ZeroDivisionError):ok=False
    if ok:yes.append(ad)
    else:stack.extend([ad+'1',ad+'0'])
   yes.sort();assert len(set(yes))==len(yes)
   assert all(not b.startswith(a)for a,b in zip(yes,yes[1:]))
   assert sum((Q(1,2**len(x))for x in yes),Q(0))==1
   slopes.append({'faces':[fa,fb],'addresses':yes,'accepted':len(yes),'visited':vis})
   print('slope boundary',fa,fb,len(yes),flush=True)
 assert len(rows)==60 and len(slopes)==16
 assert initial=={p:sha(ROOT/p)for p in DEPS}
 assert ph==sha(PROOF)and sh==sha(__file__)
 out={'status':'passed','precision_bits':args.precision,'source_grid':rows,
      'source_grid_count':len(rows),'source_cells':sum(r['accepted']for r in rows),
      'kappa_interval':['-2/5','3/10'],'kappa_step':'1/20',
      'reference_rectangles':rects,'slope_boundary':slopes,
      'slope_cells':sum(r['accepted']for r in slopes),
      'elapsed_seconds':time.time()-start,'dependencies':initial,
      'proof_sha256':ph,'script_sha256':sh,
      'scope':'Whole original (4,3) right-endpoint row/angle source support grids at two negative heights, zero, and the selected+.014 height; convex chords cover the certified actual reference slope range. No source-versus-geometric-intercept inequality or intermediate-height seam comparison.'}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',len(rows),'support values,',out['source_cells'],'source cells,',out['slope_cells'],'reference slope cells',flush=True)
if __name__=='__main__':main()
