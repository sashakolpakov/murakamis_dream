#!/usr/bin/env python3
from fractions import Fraction as Q
from flint import arb,acb,ctx
import sympy as sy
import argparse,hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_small_angle_high_rows.md'
ap=argparse.ArgumentParser(description='Whole small-angle high-row scalar reduction, with all endpoint singularities retained.')
ap.add_argument('--precision',type=int,default=192)
ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-small-angle-high-rows.json')
args=ap.parse_args();ctx.prec=args.precision;pi=arb.pi();ii=acb(0,1)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=['notes/research_mixed_boundary_strip_bounds.md','notes/research_mixed_angular_support_candidates.md','notes/research_mixed_high_row_endpoint_reduction.md']
deps={p:sha(ROOT/p)for p in DEPS};ph=sha(PROOF);sh=sha(__file__)
ar=lambda x:arb(Q(x).numerator)/Q(x).denominator
def g(z):return(((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real
def J(x):
 x=Q(x);x-=x.numerator//x.denominator
 return arb(0)if x==0 else g(acb(ar(x)))
def jr(lo,hi):
 v=[J(t)for t in[lo,hi]+[Q(k)+c for k in range(-1,3)for c in[Q(1,6),Q(5,6)]if lo<=Q(k)+c<=hi]]
 return arb(min(x.lower()for x in v)).union(arb(max(x.upper()for x in v)))
def gr(lo,hi,hl,hh):
 v=g(acb(ar(lo).union(ar(hi)),-ar(hl).union(ar(hh))))
 if v.is_finite():return v
 delta=2*pi*ar(hh);om=(pi*pi/6-(-delta).exp().polylog(2))/(2*pi)
 return jr(lo,hi)+arb(0,om.upper())
def decode(ad):
 b=[Q(3,5),Q(1),Q(0),Q(13,100),Q(0),Q(3,100)]
 for i,bit in enumerate(ad):
  k=2*(i%3);m=(b[k]+b[k+1])/2;b[k+1-int(bit)]=m
 return b
def bound(b):
 ul,uh,yl,yh,hl,hh=b
 val=jr(ul+Q(1,2),uh+Q(1,2))+gr(ul+yl,uh+yh,hl,hh)-gr(Q(63,100),Q(63,100),hl,hh)-gr(yl,yh,hl,hh)+gr(Q(13,100),Q(13,100),hl,hh)-2*jr(ul,uh)+2*pi*ar(hl).union(ar(hh))*ar(ul-Q(1,2)).union(ar(uh-Q(1,2)))+ar(Q(1,4))*ar(Q(13,100)-yh).union(ar(Q(13,100)-yl))
 return val
q,hp,a,b,delta,piconst=sy.symbols('q hp a b delta piconst')
assert sy.expand(-q*(a-b)/2+q*piconst*hp*delta+q*(a-b-2*piconst*hp*delta)/2)==0
H=ar('3/100');cc=(13*pi/50).cos();radius=(2*pi*H).exp()
moduli=[1+R*R-2*R*cc for R in[radius,1/radius]]
assert all(v<1 for v in moduli)
row=(2*(pi/10).sin()).log()+(2*(pi*H).cosh()).log()+pi*H-2*(2*(2*pi/5).sin()).log()
angle=(((2*pi*H).cosh()+cc)/((2*pi*H).cosh()-cc)).log()/2-ar('1/4')
assert row<ar('-9/10')and angle>ar('1/2')
assert ar('57/1000')*(ar('13/100')/ar('11/50'))**2<ar('3/100')
assert ar('7/500')*(ar('13/100')/ar('11/50'))**2<ar('3/100')
start=time.time();stack=[''];yes=[];vis=0;worst=None
while stack:
 ad=stack.pop();vis+=1;assert len(ad)<60,(ad,bound(decode(ad)))
 v=bound(decode(ad))
 if v<ar('-1/20'):
  yes.append(ad);worst=v.upper()if worst is None else max(worst,v.upper())
 else:stack.extend([ad+'1',ad+'0'])
 if vis%10000==0:print(vis,len(yes),len(stack),time.time()-start,flush=True)
assert sum((Q(1,2**len(a))for a in yes),Q(0))==1
yes.sort();assert len(yes)==len(set(yes))
assert all(not b.startswith(a)for a,b in zip(yes,yes[1:]))
assert deps=={p:sha(ROOT/p)for p in DEPS}and ph==sha(PROOF)and sh==sha(__file__)
record={'status':'passed','precision_bits':args.precision,'addresses':yes,'accepted_cells':len(yes),'visited_cells':vis,'maximum_D_upper':str(worst),'exact_identities':1,'scalar_comparisons':6,'row_derivative_upper':str(row),'half_row_angle_derivative_lower':str(angle),'dependencies':deps,'proof_sha256':ph,'script_sha256':sh,'elapsed_seconds':time.time()-start,'scope':'Universal same-height reduction of all high-row/small-angle branches to(u,y)=(.5,.13), |h|<=.03 and slope<=.25. No independent geometric-intercept claim.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS',len(yes),'cells,',vis,'visits,1 exact identity+6 scalar comparisons',time.time()-start)
