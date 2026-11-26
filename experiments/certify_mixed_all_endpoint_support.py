#!/usr/bin/env python3
"""Whole-source endpoint supports for the seven remaining typed orientations.

Source proposals are accepted only by exact dyadic interval covers. Original
logarithmic Newton maps, not polynomial roots alone, certify reference branches.
"""
import argparse,hashlib,json,math,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.special import spence
from scipy.optimize import differential_evolution
from flint import arb,acb,ctx
ctx.prec=160;pi=arb.pi();ii=acb(0,1)
ar=lambda v:arb(Q(v).numerator)/Q(v).denominator
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_all_endpoint_support.md'
RECTS={0:['3/10','39/100','-3/100','1/50'],1:['27/100','33/100','-57/1000','-1/50']}
FAMILIES=[(eta,eps,c)for eta in(0,1)for eps in(0,1)for c in(0,1)if(eta,eps,c)!=(1,0,1)]
SOURCES=sorted(set((eps,eps if c==0 else eta,c)for eta,eps,c in FAMILIES))
KAPPAS=[Q(-1,2)+Q(j,10)for j in range(11)]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def g(z):return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
def gp(z):return (1-(-2*pi*ii*z).exp()).log()
def gpp(z):
 E=(-2*pi*ii*z).exp();return 2*pi*ii*E/(1-E)
def J(u):
 u=Q(u);u-=u.numerator//u.denominator
 return arb(0)if u==0 else g(acb(ar(u))).real
def Jrange(lo,hi):
 v=[J(t)for t in[lo,hi]+[Q(k)+z for k in range(-1,3)for z in[Q(1,6),Q(5,6)]if lo<=Q(k)+z<=hi]]
 return min(x.lower()for x in v),max(x.upper()for x in v)
def box(ad):
 b=[Q(0),Q(1),Q(0),Q(1)]
 for j,bit in enumerate(ad):
  k=2*(j%2);m=(b[k]+b[k+1])/2;b[k+1-int(bit)]=m
 return b
def cover(ads):
 ads=sorted(ads);assert len(set(ads))==len(ads)
 assert all(not b.startswith(a)for a,b in zip(ads,ads[1:]))
 assert sum((Q(1,2**len(a))for a in ads),Q(0))==1
 return ads
def heights(beta):return [Q(-3,100),Q(0),Q(1,50)]if beta==0 else[Q(-57,1000),Q(0),Q(7,500)]
def source_bound(bb,h,k,q,eps,beta,c):
 ul,uh,xl,xh=bb;u=(ul+uh)/2;x=(xl+xh)/2;ru=(uh-ul)/2;rx=(xh-xl)/2
 if h==0 and not(ul>0 and uh<1 and xl>0 and xh<1 and(uh+xh<1 or ul+xl>1)):
  jm=Jrange(ul,uh)[0];xm=Jrange(xl,xh)[0];sm=Jrange(ul+xl,uh+xh)[1]
  return sm-(1+ar(Q(q,2)))*xm-(1+eps)*jm-min((ar(k)*ar(xl)).lower(),(ar(k)*ar(xh)).lower())
 U=ar(ul).union(ar(uh));X=ar(xl).union(ar(xh));H=abs(h);hp=max(h,Q(0));sigma=int(beta and h>0)
 cu=2*pi*ar(hp-c*h);const=pi*ar(hp)*(beta-ar(Q(q,2)))-pi*ar(beta*sigma*h)
 kap=ar(k)+q*pi*ar(hp);coef=1+ar(Q(q,2))
 z=acb(ar(x+u),-ar(H));xx=acb(ar(x),-ar(H))
 B=g(z).real-coef*g(xx).real+cu*ar(u)+const-kap*ar(x)
 Bu=gp(z).real+cu;Bx=gp(z).real-coef*gp(xx).real-kap
 suu=gpp(acb(X+U,-ar(H))).real;sux=suu;sxx=suu-coef*gpp(acb(X,-ar(H))).real
 if ul>0 and uh<1:
  val=B-(1+eps)*J(u);du=Bu-(1+eps)*(2*(pi*ar(u)).sin()).log()
  suu-= (1+eps)*pi*(pi*U).cot()
  out=val+abs(du)*ar(ru)+abs(Bx)*ar(rx)+abs(suu)*ar(ru)**2/2+abs(sux)*ar(ru*rx)+abs(sxx)*ar(rx)**2/2
 else:
  out=B-(1+eps)*Jrange(ul,uh)[0]+abs(Bu)*ar(ru)+abs(Bx)*ar(rx)+abs(suu)*ar(ru)**2/2+abs(sux)*ar(ru*rx)+abs(sxx)*ar(rx)**2/2
 return out

def propose(h,k,eps,beta,c):
 hf=float(h);kf=float(k);hp=max(hf,0);H=abs(hf);sig=int(beta and h>0)
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 JJ=lambda u:0 if u in(0,1)else gg(complex(u))
 def ev(u,x,q):return gg(x+u-1j*H)-(1+q/2)*gg(x-1j*H)-(1+eps)*JJ(u)+2*np.pi*(hp-c*hf)*u+np.pi*hp*(beta-q/2)-np.pi*beta*sig*hf-(kf+q*np.pi*hp)*x
 vals=[]
 for q in sorted({0,beta}):
  opt=differential_evolution(lambda v:-ev(*v,q),[(1e-12,1-1e-12),(0,1)],seed=27,popsize=8,maxiter=120,tol=1e-9)
  vals.append(ev(*opt.x,q));vals.extend(ev(u,x,q)for u in(0,1)for x in(0,1))
 return Q(math.ceil((max(vals)+.002)*1000000),1000000)

def edge(kind,f,lo,hi):
 xl,xh,yl,yh=map(Q,RECTS[kind]);v=ar(lo).union(ar(hi))
 return acb(ar(xl)+ar(xh-xl)*v,ar(yl if f==0 else yh))if f in(0,2)else acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*v)
def direction(kind,f):
 xl,xh,yl,yh=map(Q,RECTS[kind]);return acb(ar(xh-xl))if f in(0,2)else ii*ar(yh-yl)
def pt(z):return acb(ar(str(z.real)),ar(str(z.imag)))
def root_box(a,b,a0,b0,eps,witness=None):
 d=2+eps
 if witness is None:
  af=complex(float(a0.real),float(a0.imag));bf=complex(float(b0.real),float(b0.imag));A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
  co=[A*(B-1),A-B,1-A]if eps==0 else[A,A*(B-3),2*A-B,1-A]
  candidates=[1j*np.log(U)/(2*np.pi)for U in np.roots(co)]
  candidates=[s for s in candidates if .2<s.real<.44 and abs(s.imag)<.15 and abs(np.log(1-np.exp(-2j*np.pi*(s+af)))+np.log(1-np.exp(-2j*np.pi*(s+bf)))-d*np.log(1-np.exp(-2j*np.pi*s))+2j*np.pi*af)<1e-7]
  if len(candidates)!=1:return None
  z0=pt(candidates[0]);center=[str(candidates[0].real),str(candidates[0].imag)]
 else:center=witness['center'];z0=acb(ar(center[0]),ar(center[1]))
 H0=gpp(z0+a0)+gpp(z0+b0)-d*gpp(z0);Y=1/H0
 f0=gp(z0+a0)+gp(z0+b0)-d*gp(z0)+2*pi*ii*a0
 E=[gpp(z0+a0)+2*pi*ii,gpp(z0+b0)];dp=[a-a0,b-b0]
 if witness is None:
  deriv=[];dd=[]
  for e in E:
   v=-Y*e;f=complex(float(v.real.mid()),float(v.imag.mid()));deriv.append(pt(f));dd.append([str(f.real),str(f.imag)])
 else:dd=witness['derivatives'];deriv=[acb(ar(v[0]),ar(v[1]))for v in dd]
 dz=sum((deriv[j]*dp[j]for j in(0,1)),acb(0));lin=f0+sum(((H0*deriv[j]+E[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,delta):
  v=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(0<v.real<1):return arb.pos_inf()
  return pi*pi*abs(1/(pi*v).sin()**2)*abs(delta)**2/2
 er=abs(Y)*(abs(lin)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+d*rem(z0,dz))
 if not er.is_finite():return None
 rad=Q(witness['radius'])if witness is not None else Q(max(1,math.ceil(float(er.upper())*1.5*2**42)),2**42)
 if rad>Q(1,20):return None
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not(ar('1/5')<z.real<ar('11/25')and abs(z.imag)<ar('3/20')):return None
 def dc(base,delta):return -pi*(pi*delta).sin()/((pi*base).sin()*(pi*(base+delta)).sin())
 ee=1-Y*H0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):return None
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*(gpp(zp+a0)+gpp(zp+b0)-d*gpp(zp))
 if not abs(Y*f0)+abs(ep)*rr<rr:return None
 return z,zp,{'center':center,'derivatives':dd,'radius':str(rad)}

def phase(s,a,b,eta,eps):
 d=2+eps;ca=1+ar(Q(eta,2));cb=1+ar(Q(eps,2))
 f=g(s+a)+g(s+b)-d*g(s)+2*pi*ii*a*s-ca*g(a)-cb*g(b)
 da=gp(s+a)+2*pi*ii*s-ca*gp(a);db=gp(s+b)-cb*gp(b)
 sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=gpp(s+a)+gpp(s+b)-d*gpp(s)
 aa=gpp(s+a)-ca*gpp(a)-sa*sa/ss;ab=-sa*sb/ss;bb=gpp(s+b)-cb*gpp(b)-sb*sb/ss
 return f,[da,db],[[aa,ab],[ab,bb]]

# Every seam bound below is for the absolute row sum, not coherent cancellation.
def seam_cases(eps,beta,c):
 intervals=[(Q(-3,100),Q(0)),(Q(0),Q(1,50))]if beta==0 else[(Q(-57,1000),Q(0)),(Q(0),Q(7,500))]
 out=[]
 for lo,hi in intervals:
  sign=1-2*c;lrs=[2*pi*ar(sign*v)for v in(lo,hi)]
  expanding=(sign*lo>=0 and sign*hi>=0)
  if eps==1 and beta==1 and c==1 and hi==0:
   rate=ar('9/25');out.extend((h,rate)for h in(lo,hi));continue
  if expanding:out.extend((h,2*pi*ar(sign*h)+ar(Q(eps,6)))for h in(lo,hi))
  else:
   logmin=min(sign*lo,sign*hi);alpha=((1-(2*pi*ar(logmin)).exp())/2).asinh()
   out.extend((h,alpha+ar(Q(eps,6)))for h in(lo,hi))
 return out

def reference_test(ad,fa,fb,family,rows,witness=None):
 eta,eps,c=family;beta=eps if c==0 else eta;moving=1-c
 al,ah,bl,bh=box(ad);a=edge(eta,fa,al,ah);b=edge(eps,fb,bl,bh);a0=edge(eta,fa,(al+ah)/2,(al+ah)/2);b0=edge(eps,fb,(bl+bh)/2,(bl+bh)/2)
 roots=root_box(a,b,a0,b0,eps,witness)
 if roots is None:return None
 s,s0,wit=roots;_,grad,H=phase(s,a,b,eta,eps);f0,grad0,_=phase(s0,a0,b0,eta,eps)
 kap=grad[moving].real
 if not(ar(KAPPAS[0])<kap<ar(KAPPAS[-1])):return None
 refs=[a,b];ref0=[a0,b0];vel=[direction(eta,fa),direction(eps,fb)];rads=[ar((ah-al)/2),ar((bh-bl)/2)]
 worst=None
 def estimate(alpha,intercept,h,e):
  target=[acb(e),acb(e)];target[moving]=ii*ar(h)
  C0=f0+sum(((target[j]-ref0[j])*grad0[j]for j in(0,1)),acb(0))
  coeff=[refs[j]-target[j]+(ar(alpha)if j==moving else 0)for j in(0,1)]
  der=[sum((coeff[j]*H[j][k]for j in(0,1)),acb(0))for k in(0,1)]
  return (ar(alpha)*grad0[moving]+intercept-C0).real+sum((abs((der[j]*vel[j]).real)*rads[j]for j in(0,1)),arb(0))
 for h,rr in rows.items():
  for e in(0,1):
   for r1,r2 in zip(rr,rr[1:]):
    kl=Q(r1['kappa']);kh=Q(r2['kappa'])
    if kap<ar(kl)or kap>ar(kh):continue
    sl=(Q(r2['upper'])-Q(r1['upper']))/(kh-kl);it=Q(r1['upper'])-sl*kl
    v=estimate(sl,ar(it),h,e)
    if not v<ar('-1/1000'):return None
    worst=v.upper()if worst is None else max(worst,v.upper())
 for h,raw in seam_cases(eps,beta,c):
  for x in(0,1):
   for e in(0,1):
    v=estimate(-x,raw,h,e)
    if not v<ar('-1/1000'):return None
    worst=v.upper()if worst is None else max(worst,v.upper())
 return wit,worst

DEPS=['notes/research_mixed_boundary_strip_bounds.md','notes/research_mixed_angular_support_candidates.md','notes/research_mixed_central_conditional_rectangles.md','experiments/certify_mixed_central_conditional_rectangles.py','repro/results/research-mixed-central-conditional-rectangles.json','notes/research_mixed_type_four_height_refinement.md','experiments/certify_mixed_type_four_height_refinement.py','experiments/replay_mixed_type_four_height_refinement.py','repro/results/research-mixed-type-four-height-refinement.json','repro/results/research-mixed-type-four-height-refinement-replay.json','notes/research_mixed_43_endpoint_support.md','experiments/check_mixed_43_endpoint_support.py','experiments/replay_mixed_43_endpoint_support.py','repro/results/research-mixed-43-endpoint-support.json','repro/results/research-mixed-43-endpoint-support-replay.json']
def bindings():
 out={p:sha(ROOT/p)for p in DEPS}
 central=json.loads((ROOT/'repro/results/research-mixed-central-conditional-rectangles.json').read_text())
 assert central['status']=='passed'and central['script_sha256']==sha(ROOT/'experiments/certify_mixed_central_conditional_rectangles.py')
 assert central['proof_sha256']==sha(ROOT/'notes/research_mixed_central_conditional_rectangles.md')
 for f,v in central['dependencies'].items():assert sha(ROOT/f)==v
 for stem,author,replayer,proof in [('research-mixed-type-four-height-refinement','certify_mixed_type_four_height_refinement.py','replay_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md'),('research-mixed-43-endpoint-support','check_mixed_43_endpoint_support.py','replay_mixed_43_endpoint_support.py','research_mixed_43_endpoint_support.md')]:
  a=json.loads((ROOT/f'repro/results/{stem}.json').read_text());r=json.loads((ROOT/f'repro/results/{stem}-replay.json').read_text())
  for d,sc in[(a,author),(r,replayer)]:
   assert d['status']=='passed'and d['script_sha256']==sha(ROOT/'experiments'/sc)
   if 'proof_sha256'in d:assert d['proof_sha256']==sha(ROOT/'notes'/proof)
   for f,v in d['dependencies'].items():assert sha(ROOT/f)==v
  assert r.get('input_sha256',r.get('geometry_input_sha256'))==sha(ROOT/f'repro/results/{stem}.json')
 return out

def main():
 global pi
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-all-endpoint-support.json')
 args=ap.parse_args();ctx.prec=args.precision;pi=arb.pi()
 deps=bindings();ph=sha(PROOF);sh=sha(__file__);start=time.time()
 # Exact one-variable seam classification and all scalar budgets.
 assert J(Q(1,6))>ar('-1/6')
 R=(57*pi/500).exp();v=(R+(R*R+4*(R-1)**2).sqrt())/8;u=v.sqrt().asin()/pi
 assert 0<v<1
 seam=(g(acb(u,-ar('57/1000')))-g(acb(0,-ar('57/1000')))).real-2*g(acb(u)).real+57*pi*u/500
 assert seam<ar('7/25')and 57*pi/500<ar('9/25')
 source=[]
 for eps,beta,c in SOURCES:
  for h in heights(beta):
   for k in KAPPAS:
    target=propose(h,k,eps,beta,c);stack=[''];yes=[];vis=0
    while stack:
     ad=stack.pop();vis+=1;assert len(ad)<40,(eps,beta,c,h,k,ad)
     try:ok=all(source_bound(box(ad),h,k,q,eps,beta,c)<ar(target)for q in sorted({0,beta}))
     except(ValueError,ZeroDivisionError):ok=False
     if ok:yes.append(ad)
     else:stack.extend([ad+'1',ad+'0'])
    yes=cover(yes);row={'source':[eps,beta,c],'height':str(h),'selected_alias':int(beta and h>0),'kappa':str(k),'upper':str(target),'addresses':yes,'accepted':len(yes),'visited':vis};source.append(row)
    print('source',eps,beta,c,h,k,target,len(yes),flush=True)
  Path('/tmp/mixed-all-endpoint-source-checkpoint.json').write_text(json.dumps(source))
 cases=[]
 for fam in FAMILIES:
  eta,eps,c=fam;beta=eps if c==0 else eta;rows={h:sorted([r for r in source if r['source']==[eps,beta,c]and Q(r['height'])==h],key=lambda r:Q(r['kappa']))for h in heights(beta)}
  for fa in range(4):
   for fb in range(4):
    stack=[''];yes=[];vis=0;maximum=None
    while stack:
     ad=stack.pop();vis+=1;assert len(ad)<32,(fam,fa,fb,ad)
     try:ans=reference_test(ad,fa,fb,fam,rows)
     except(ValueError,ZeroDivisionError):ans=None
     if ans is None:stack.extend([ad+'1',ad+'0'])
     else:
      wit,up=ans;yes.append({'address':ad,**wit});maximum=up if maximum is None else max(maximum,up)
    cover([v['address']for v in yes]);row={'family':list(fam),'faces':[fa,fb],'cells':yes,'accepted':len(yes),'visited':vis,'maximum_defect_upper':str(maximum)};cases.append(row)
    print('reference',fam,fa,fb,len(yes),maximum,flush=True)
   Path('/tmp/mixed-all-endpoint-reference-checkpoint.json').write_text(json.dumps(cases))
 assert len(source)==165 and len(cases)==112
 assert deps==bindings()and ph==sha(PROOF)and sh==sha(__file__)
 result={'status':'passed','precision_bits':args.precision,'source_grid':source,'reference_cases':cases,'source_values':len(source),'source_cells':sum(r['accepted']for r in source),'reference_products':len(cases),'reference_cells':sum(r['accepted']for r in cases),'scalar_comparisons':4,'gap':'1/1000','reference_rectangles':RECTS,'dependencies':deps,'proof_sha256':ph,'script_sha256':sh,'elapsed_seconds':time.time()-start,'scope':'Seven remaining typed endpoint orientations; all rows/angles, full unselected or selected graph target heights, raw seam bounds and both geometric endpoint representatives. Existing (4,3)-right theorem completes all eight. No full mixed cyclic-source theorem.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',result['source_values'],result['source_cells'],result['reference_products'],result['reference_cells'],flush=True)
if __name__=='__main__':main()
