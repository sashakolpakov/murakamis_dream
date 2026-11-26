#!/usr/bin/env python3
"""Exact complex-triangle algebra and outward full-source endpoint budgets."""
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
import sympy as sp
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_boundary_strip_bounds.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-boundary-strip-bounds.json');args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=90
 def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
 pi=arb.pi();ii=acb(0,1)
 def J(x):return (((-2*pi*ii*x).exp().polylog(2)-pi*pi/6)/(2*pi*ii)-ii*pi*(x-x*x)/2).real
 u,p,v,q=sp.symbols('u p v q',real=True);c=sp.re(((u+sp.I*v)*(p+sp.I*q)-1)/(u+p+sp.I*(v+q)))
 assert sp.factor((u*p-(u+p)*c)-((u+p)**2-(p*v-u*q)**2)/((u+p)**2+(v+q)**2))==0
 x=sp.symbols('x',positive=True);C=sp.symbols('C',real=True)
 # Derivative ratio reduces exactly after sin(u)=2sin(u/2)cos(u/2).
 assert sp.cancel((2*sp.sqrt(1-x))**2/((4*sp.sqrt(x)*sp.sqrt(1-x))**4)*sp.exp(2*C)-sp.exp(2*C)/(64*x*x*(1-x)))==0
 # The original derivative includes 2 sin(pi u), including its leading factor.
 assert sp.expand((8*x*sp.sqrt(1-x))**2-64*x*x*(1-x))==0
 symbolic=['complex triangle determinant','half-angle derivative quotient','critical cubic']
 # Literal endpoint polynomial identities in an exact cyclotomic field.
 field=sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3));one,zero=field.one,field.zero;cv=lambda x:field.from_sympy(sp.sympify(x));endpoint_identities=[]
 def prod(xs):
  ans=one
  for x in xs:ans*=x
  return ans
 for N,qe in[(2,sp.I),(3,(1+sp.I*sp.sqrt(3))/2),(4,(1+sp.I)/sp.sqrt(2)),(6,(sp.sqrt(3)+sp.I)/2)]:
  qq=cv(qe);rr=qq**-2;P=[prod(one-rr**j for j in range(1,l+1))for l in range(N)];polys=[]
  for l in range(N):
   co=[one]
   for j in range(1,l+1):
    new=[zero]*(len(co)+1)
    for h,vv in enumerate(co):new[h]+=vv;new[h+1]-=rr**j*vv
    co=new
   polys.append(co)
  dd=[sum((rr**(-j*h)/P[j]for j in range(N)),zero)/N for h in range(N)]
  for h in range(N):
   left=sum((polys[l][h]/P[l]for l in range(h,N)),zero)
   assert left==N*dd[h];endpoint_identities.append(f'N{N} left polynomial coefficient{h}')
   right=sum((polys[l][l-h]/P[l]for l in range(h,N)),zero)
   assert right==N*cv(sp.conjugate(field.to_sympy(dd[h])));endpoint_identities.append(f'N{N} right Laurent coefficient{-h}')
 rows=[]
 for label,e,Cq,addq,thresholdq in[
  ('left own3',0,'1/25','0','37/100'),('left own4',1,'0','1/12','11/20'),
  ('left selected own4',1,'7/250','1/12','57/100'),
  ('right left3 own3',0,'3/50','0','2/5'),('right left4 own3',0,'57/500','1/12','14/25'),
  ('right left3 own4',1,'3/50','0','51/100'),('right left4 own4',1,'57/500','1/12','16/25')]:
  cc=ar(Cq)*pi;add=ar(addq);target=ar(thresholdq)
  if e==0:
   uu=2*((cc.exp()/2).asin())/pi;assert 0<uu<1
   root=None
  else:
   cm=mp.mpf(Q(Cq).numerator)/Q(Cq).denominator*mp.pi
   vv=mp.findroot(lambda vv:64*vv*vv*(1-vv)-mp.exp(2*cm),(.12,.23))
   lo=Q(mp.nstr(vv,80))-Q(1,10**75);hi=Q(mp.nstr(vv,80))+Q(1,10**75)
   assert 0<ar(lo)<ar(hi)<ar('2/3')
   assert 64*ar(lo)**2*(1-ar(lo))< (2*cc).exp()<64*ar(hi)**2*(1-ar(hi))
   vv=ar(lo).union(ar(hi));uu=2*vv.sqrt().asin()/pi;root=[str(lo),str(hi)]
  val=-2*J((1-uu)/2)-(1+e)*J(uu)+cc*uu
  assert val>cc and val>0
  assert val+add<target
  rows.append({'name':label,'epsilon':e,'C_pi':Cq,'weight_cost':addq,'threshold':thresholdq,'critical_u':str(uu),'v_root_bracket':root,'rate_upper':str((val+add).upper()),'strict_margin':str((target-val-add).lower())})
 assert J(ar('5/6'))<ar('1/6')
 assert ar('1/6')+pi/25<ar('3/10')
 # Whole-period maxima for the unchanged-height seam majorants.
 axis_rows=[]
 for eta,e,selected,thresholdq in[
  (0,0,False,'227/500'),(0,1,False,'153/250'),(0,1,True,'317/500'),
  (1,0,False,'267/500'),(1,1,False,'673/1000'),(1,1,True,'697/1000')]:
  Hq=Q(3,100) if eta==0 else Q(57,1000)
  hq=Q(1,50) if e==0 else(Q(7,500)if selected else Q(0))
  H=ar(Hq);hh=ar(hq);R=(2*pi*H).exp();E=(4*pi*hh).exp();A=(R-1)**2
  if e==0:assert 256-4*E*(3*A+16*R)>0
  else:assert 4096-4*E*(10*A+48*R)>0
  def polynomial(v):return 16**(2+e)*v**(2+e)*(1-v)**(1+e)-4*E*(A+16*R*v*(1-v))
  assert polynomial(ar('1/2'))>0
  Rm=mp.exp(2*mp.pi*mp.mpf(Hq.numerator)/Hq.denominator);Em=mp.exp(4*mp.pi*mp.mpf(hq.numerator)/hq.denominator)
  pm=lambda v:16**(2+e)*v**(2+e)*(1-v)**(1+e)-4*Em*((Rm-1)**2+16*Rm*v*(1-v))
  guess=mp.mpf('.35')if e==0 else mp.mpf('.16')
  vm=mp.findroot(pm,(guess*.8,guess));lo=Q(mp.nstr(vm,80))-Q(1,10**75);hi=Q(mp.nstr(vm,80))+Q(1,10**75)
  assert 0<ar(lo)<ar(hi)<ar('1/2') and polynomial(ar(lo))<0<polynomial(ar(hi))
  vv=ar(lo).union(ar(hi));uu=2*vv.sqrt().asin()/pi
  zz=acb(uu,-H);gg=((-2*pi*ii*zz).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
  val=gg.real-2*J((1-uu)/2)-(2+e)*J(uu)+2*pi*(H+hh)*uu
  assert val>0 and val>2*pi*(H+hh)
  val+=ar(Q(e,12));assert val<ar(thresholdq)-ar('1/8000')
  axis_rows.append({'left_type':eta,'own_type':e,'other_selected_alias':selected,'H':str(Hq),'other_positive_height':str(hq),'v_root_bracket':[str(lo),str(hi)],'critical_u':str(uu),'rate_upper':str(val.upper()),'threshold':thresholdq,'strict_margin':str((ar(thresholdq)-val).lower())})
 delta=ar('1/1000000')
 strip_margins={}
 def stripcheck(name,v):assert v>0,(name,v);strip_margins[name]=str(v)
 for Hq in['3/100','57/1000']:
  R=(2*pi*ar(Hq)).exp();stripcheck('product Lipschitz H='+Hq,37-2*pi*R/(R-1))
 stripcheck('negative weight derivative',ar('51/10')+(1-(-pi/500).exp()).log())
 stripcheck('selected lower-reflection derivative',ar('5/2')+(1-(-7*pi/250).exp()).log())
 stripcheck('selected forcing branch',7*pi/500-ar('15/2')*delta)
 Rmax=(7*pi/250).exp()
 stripcheck('negative forced multiplier',ar('1/2')-(1-(-57*pi/500).exp())-6*pi*Rmax*delta)
 stripcheck('positive forced multiplier',ar('1/2')-(Rmax-1)-6*pi*Rmax*delta)
 stripcheck('strip cost below scalar reserve',ar('1/8000')-43*delta)
 deps=['notes/research_mixed_central_outer_integral.md','notes/research_mixed_fourier_weight_continuation.md','notes/research_mixed_conditional_torus_composition.md','notes/research_mixed_type_three_window_strip.md','notes/research_mixed_cyclic_critical_height_bounds.md']
 out={'status':'passed','precision_bits':args.precision,'exact_identity_count':len(symbolic),'exact_identities':symbolic,'exact_endpoint_normalization_count':len(endpoint_identities),'exact_endpoint_normalizations':endpoint_identities,'strict_endpoint_budget_count':len(rows),'endpoint_budgets':rows,'quantified_strip_half_width':'1/1000000','strip_scalar_count':len(strip_margins),'strip_scalar_margins':strip_margins,'axis_budget_count':len(axis_rows),'axis_budgets':axis_rows,'scope':'Whole original local kernels near tapered endpoints and the unchanged-height left period seam, true Fourier/alias weights included. No supporting-plane or intermediate-region conclusion.','script_sha256':sha(__file__),'proof_sha256':sha(PROOF),'dependencies':{p:sha(ROOT/p)for p in deps}}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(symbolic),'exact identities,',len(rows),'whole-source endpoint budgets,',len(endpoint_identities),'exact endpoint coefficients,',len(axis_rows),'unchanged-height seam budgets,',len(strip_margins),'strip scalars')
if __name__=='__main__':main()
