#!/usr/bin/env python3
"""Independent opposite-frequency and reflected-row replay; no author import."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
import sympy as sy
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_small_angle_high_rows.md'
AUTHOR=ROOT/'experiments/certify_mixed_small_angle_high_rows.py'
INPUT=ROOT/'repro/results/research-mixed-small-angle-high-rows.json'
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-small-angle-high-rows-replay.json')
args=ap.parse_args();ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ar=lambda x:arb(Q(x).numerator)/Q(x).denominator
raw=INPUT.read_bytes();rec=json.loads(raw);assert rec['status']=='passed'
assert rec['script_sha256']==sha(AUTHOR)and rec['proof_sha256']==sha(PROOF)
deps=dict(rec['dependencies']);deps[str(PROOF.relative_to(ROOT))]=sha(PROOF);deps[str(AUTHOR.relative_to(ROOT))]=sha(AUTHOR)
for p,h in deps.items():assert sha(ROOT/p)==h
selfhash=sha(__file__)
def G(z):
 assert 0<z.real<1
 return (-( (2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)+I*P*(z-z*z)).real
def J(t):
 t=Q(t);t-=t.numerator//t.denominator
 return arb(0)if t==0 else G(acb(ar(t)))
def jr(lo,hi):
 xs=[lo,hi]
 for k in range(-2,3):
  for r in[Q(1,6),Q(5,6)]:
   if lo<=k+r<=hi:xs.append(k+r)
 vv=[J(t)for t in xs]
 return arb(min(v.lower()for v in vv)).union(arb(max(v.upper()for v in vv)))
def primitive_strip(lo,hi,hl,hh):
 assert 0<=lo<=hi<=1
 if lo==hi and lo in(0,1):return arb(0)
 H=ar(hl).union(ar(hh));X=ar(lo).union(ar(hi))
 if 0<lo and hi<1:
  v=G(acb(X,-H))
  if v.is_finite():return v
 if hl>0 and(lo==0 or hi==1):
  # Real primitive vanishes at every integer; integrate its sine-log derivative.
  L=abs(2*(P*acb(X,-H)).sin()).log()-P*H
  if L.is_finite():
   length=hi if lo==0 else 1-lo
   return arb(0,(abs(L)*ar(length)).upper())
 omega=(P*P/6-(-2*P*ar(hh)).exp().polylog(2))/(2*P)
 return jr(lo,hi)+arb(0,omega.upper())
def gr(lo,hi,hl,hh):
 cuts=sorted(set([lo,hi]+[Q(k)for k in range(-2,4)if lo<k<hi]))
 if len(cuts)==1:cuts.append(cuts[0])
 out=None
 for left,right in zip(cuts,cuts[1:]):
  shift=left.numerator//left.denominator
  if right==left and left.denominator==1:return arb(0)
  value=primitive_strip(left-shift,right-shift,hl,hh)
  out=value if out is None else out.union(value)
 return out

def decode(ad):
 lo=[Q(3,5),Q(0),Q(0)];hi=[Q(1),Q(13,100),Q(3,100)]
 for j,c in enumerate(ad):
  assert c in'01';k=j%3;m=(lo[k]+hi[k])/2
  if c=='0':hi[k]=m
  else:lo[k]=m
 return lo,hi

def bound(ad):
 lo,hi=decode(ad);ul,yl,hl=lo;uh,yh,hh=hi
 # Independent row reflection v=1-u, J(1-v)=-J(v), G_H(1-v)=-G_H(v).
 vl,vh=1-uh,1-ul
 return (jr(Q(1,2)-vh,Q(1,2)-vl)-gr(vl-yh,vh-yl,hl,hh)
         -gr(Q(63,100),Q(63,100),hl,hh)-gr(yl,yh,hl,hh)
         +gr(Q(13,100),Q(13,100),hl,hh)+2*jr(vl,vh)
         +2*P*ar(hl).union(ar(hh))*ar(Q(1,2)-vh).union(ar(Q(1,2)-vl))
         +ar(Q(1,4))*ar(Q(13,100)-yh).union(ar(Q(13,100)-yl)))
def cover(codes):
 tree={}
 for code in codes:
  node=tree
  for c in code:
   assert c in'01'and'L'not in node
   node=node.setdefault(c,{})
  assert not node;node['L']=1
 def visit(node):
  if'L'in node:assert node=={'L':1};return 1
  assert set(node)=={'0','1'}
  return visit(node['0'])+visit(node['1'])
 assert visit(tree)==len(codes)
q,hp,a,b,delta,piconst=sy.symbols('q hp a b delta piconst')
assert sy.expand(-q*(a-b)/2+q*piconst*hp*delta+q*(a-b-2*piconst*hp*delta)/2)==0
H=ar('3/100');r=(2*P*H).exp();co=(13*P/50).cos()
assert 1+r*r-2*r*co<1 and 1+1/(r*r)-2*co/r<1
row=(2*(P/10).sin()).log()+(2*(P*H).cosh()).log()+P*H-2*(2*(2*P/5).sin()).log()
ratio=((2*P*H).cosh()+co)/((2*P*H).cosh()-co)
assert row<ar('-9/10')and ratio.log()/2-ar('1/4')>ar('1/2')
assert ar('57/1000')*(ar('13/100')/ar('11/50'))**2<ar('3/100')
assert ar('7/500')*(ar('13/100')/ar('11/50'))**2<ar('3/100')
cover(rec['addresses']);start=time.time();accepted=[];refinements=0;worst=None
for original in rec['addresses']:
 stack=[original]
 while stack:
  ad=stack.pop()
  try:v=bound(ad)
  except(ValueError,ZeroDivisionError,AssertionError):v=arb.pos_inf()
  if v<ar('-1/20'):
   accepted.append(ad);worst=v.upper()if worst is None else max(worst,v.upper())
  else:
   assert len(ad)<len(original)+18,(original,ad,str(v))
   refinements+=1;stack.extend([ad+'1',ad+'0'])
cover(accepted)
assert INPUT.read_bytes()==raw and selfhash==sha(__file__)
assert deps=={p:sha(ROOT/p)for p in deps}
out={'status':'passed','precision_bits':args.precision,'original_cells':len(rec['addresses']),'accepted_cells':len(accepted),'refinements':refinements,'addresses':sorted(accepted),'maximum_D_upper':str(worst),'exact_identities':1,'scalar_comparisons':6,'input_sha256':hashlib.sha256(raw).hexdigest(),'script_sha256':selfhash,'proof_sha256':sha(PROOF),'dependencies':deps,'elapsed_seconds':time.time()-start,'scope':'Independent reflected-row positive-frequency replay of the whole compact far-row inequality, exact coverage and six scalar near-row/taper margins.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(accepted),'cells,',refinements,'refinements,1 exact identity+6 scalars',time.time()-start)
