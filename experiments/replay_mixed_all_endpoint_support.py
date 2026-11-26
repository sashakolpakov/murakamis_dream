#!/usr/bin/env python3
"""Independent positive-frequency and sine/cotangent replay of all endpoints.

No author implementation or optimizer is imported. Exact saved covers and
affine root witnesses are replayed using independently evaluated derivatives.
"""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_all_endpoint_support.md'
AUTHOR=ROOT/'experiments/certify_mixed_all_endpoint_support.py'
INPUT=ROOT/'repro/results/research-mixed-all-endpoint-support.json'
I=acb(0,1);PI=arb.pi()
RECTS={0:['3/10','39/100','-3/100','1/50'],1:['27/100','33/100','-57/1000','-1/50']}
FAMILIES={(a,b,c) for a in(0,1) for b in(0,1) for c in(0,1)}-{(1,0,1)}
SOURCES={(b,b if c==0 else a,c) for a,b,c in FAMILIES}
KS=[Q(-1,2)+Q(j,10)for j in range(11)]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(v):
 v=Q(v);return arb(v.numerator)/v.denominator
def decode(ad):
 lo=[Q(0),Q(0)];hi=[Q(1),Q(1)]
 for j,v in enumerate(ad):
  assert v in'01';k=j%2;mid=(lo[k]+hi[k])/2
  if v=='0':hi[k]=mid
  else:lo[k]=mid
 return lo,hi
def cover(addresses):
 # A complete full binary tree independently checks partition exhaustion.
 tree={}
 for address in addresses:
  node=tree
  for bit in address:
   assert bit in'01' and 'leaf'not in node
   node=node.setdefault(bit,{})
  assert not node
  node['leaf']=1
 def visit(node):
  if 'leaf'in node:
   assert node=={'leaf':1}
   return 1
  assert set(node)=={'0','1'}
  return visit(node['0'])+visit(node['1'])
 assert visit(tree)==len(addresses)
def G(z):
 assert 0<z.real<1
 return -((2*PI*I*z).exp().polylog(2)-PI*PI/6)/(2*PI*I)+I*PI*(z-z*z)
def realG(x,H):
 x=Q(x);x-=x.numerator//x.denominator
 # The negative-height primitive is purely imaginary at every integer.
 return arb(0)if x==0 else G(acb(ar(x),-ar(H))).real
def J(x):return realG(x,Q(0))
def Jrange(lo,hi):
 xs=[lo,hi]+[Q(j)+r for j in range(-1,3)for r in(Q(1,6),Q(5,6))if lo<=Q(j)+r<=hi]
 vals=[J(x)for x in xs]
 return min(v.lower()for v in vals),max(v.upper()for v in vals)
def first(x,H):
 z=acb(x,-ar(H));return abs(2*(PI*z).sin()).log()-PI*ar(H)
def second(x,H):
 z=acb(x,-ar(H));return (PI*(PI*z).cos()/(PI*z).sin()).real
def GP(z):
 assert 0<z.real<1
 return (2*(PI*z).sin()).log()+I*PI*(1-2*z)/2
def GPP(z):return PI*(PI*z).cos()/(PI*z).sin()-PI*I
def heights(beta):return [Q(-3,100),Q(0),Q(1,50)]if beta==0 else[Q(-57,1000),Q(0),Q(7,500)]

def source_upper(ad,h,k,q,eps,beta,c):
 lo,hi=decode(ad);ul,xl=lo;uh,xh=hi
 u=(ul+uh)/2;x=(xl+xh)/2;ru=(uh-ul)/2;rx=(xh-xl)/2
 coefficient=1+ar(Q(q,2))
 if h==0 and not(ul>0 and uh<1 and xl>0 and xh<1 and(uh+xh<1 or ul+xl>1)):
  return Jrange(ul+xl,uh+xh)[1]-coefficient*Jrange(xl,xh)[0]-(1+eps)*Jrange(ul,uh)[0]-min((ar(k)*ar(xl)).lower(),(ar(k)*ar(xh)).lower())
 H=abs(h);hp=max(h,Q(0));sigma=int(beta and h>0)
 linear=2*PI*ar(hp-c*h)
 constant=PI*ar(hp)*(beta-ar(Q(q,2)))-PI*ar(beta*sigma*h)
 slope=ar(k)+q*PI*ar(hp)
 value=realG(x+u,H)-coefficient*realG(x,H)+linear*ar(u)+constant-slope*ar(x)
 du=first(ar(x+u),H)+linear
 dx=first(ar(x+u),H)-coefficient*first(ar(x),H)-slope
 U=ar(ul).union(ar(uh));X=ar(xl).union(ar(xh))
 huu=second(X+U,H);hux=huu;hxx=huu-coefficient*second(X,H)
 if ul>0 and uh<1:
  value-=(1+eps)*J(u)
  du-=(1+eps)*(2*(PI*ar(u)).sin()).log()
  huu-=(1+eps)*PI*(PI*U).cos()/(PI*U).sin()
 else:value-=(1+eps)*Jrange(ul,uh)[0]
 return value+abs(du)*ar(ru)+abs(dx)*ar(rx)+abs(huu)*ar(ru)**2/2+abs(hux)*ar(ru*rx)+abs(hxx)*ar(rx)**2/2

def edge(kind,f,lo,hi):
 xl,xh,yl,yh=map(Q,RECTS[kind]);v=ar(lo).union(ar(hi))
 if f in(0,2):return acb(ar(xl)+ar(xh-xl)*v,ar(yl if f==0 else yh))
 assert f in(1,3)
 return acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*v)
def tangent(kind,f):
 xl,xh,yl,yh=map(Q,RECTS[kind])
 return acb(ar(xh-xl))if f in(0,2)else I*ar(yh-yl)
def parameters(ad,family,faces):
 lo,hi=decode(ad);eta,eps,_=family
 v=[edge(k,f,lo[j],hi[j])for j,(k,f)in enumerate(zip((eta,eps),faces))]
 p=[edge(k,f,(lo[j]+hi[j])/2,(lo[j]+hi[j])/2)for j,(k,f)in enumerate(zip((eta,eps),faces))]
 r=[ar((hi[j]-lo[j])/2)for j in(0,1)]
 return v,p,r

def enclose_root(a,b,a0,b0,eps,witness,origin=None):
 d=2+eps
 z0=acb(ar(witness['center'][0]),ar(witness['center'][1]))
 der=[acb(ar(v[0]),ar(v[1]))for v in witness['derivatives']]
 if origin is not None:
  # Refined cells use the exact affine prediction at their new midpoint.
  olda,oldb=origin
  pred=z0+der[0]*(a0-olda)+der[1]*(b0-oldb)
  z0=acb(pred.real.mid(),pred.imag.mid())
  # Point Newton steps propose a new exact binary center, never acceptance.
  for _ in range(4):
   ff=GP(z0+a0)+GP(z0+b0)-d*GP(z0)+2*PI*I*a0
   hh=GPP(z0+a0)+GPP(z0+b0)-d*GPP(z0)
   pred=z0-ff/hh
   z0=acb(pred.real.mid(),pred.imag.mid())
 f0=GP(z0+a0)+GP(z0+b0)-d*GP(z0)+2*PI*I*a0
 h0=GPP(z0+a0)+GPP(z0+b0)-d*GPP(z0)
 inv=1/h0
 ext=[GPP(z0+a0)+2*PI*I,GPP(z0+b0)]
 dp=[a-a0,b-b0]
 dz=sum((der[j]*dp[j]for j in(0,1)),acb(0))
 linear=f0+sum(((h0*der[j]+ext[j])*dp[j]for j in(0,1)),acb(0))
 def second_remainder(z,delta):
  hull=z+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not 0<hull.real<1:return arb.pos_inf()
  return PI**2*abs(1/(PI*hull).sin()**2)*abs(delta)**2/2
 error=abs(inv)*(abs(linear)+second_remainder(z0+a0,dz+dp[0])+second_remainder(z0+b0,dz+dp[1])+d*second_remainder(z0,dz))
 if not error.is_finite():return None
 radius=ar(witness['radius'])
 if origin is not None:
  # Fresh rational-free outward radius is accepted only by the self-map test.
  radius=max(ar('1e-12').upper(),(2*error).upper())
 if not radius<ar('1/20'):return None
 delta=dz+acb(arb(0,radius),arb(0,radius));z=z0+delta
 if not ar('1/5')<z.real<ar('11/25')or not abs(z.imag)<ar('3/20'):return None
 # Direct independently evaluated sine/cotangent Jacobian.
 jac=1-inv*(GPP(z+a)+GPP(z+b)-d*GPP(z))
 if not error+abs(jac)*radius<radius:return None
 rr=ar('1e-10')
 point=z0+acb(arb(0,rr),arb(0,rr))
 jacp=1-inv*(GPP(point+a0)+GPP(point+b0)-d*GPP(point))
 if not abs(inv*f0)+abs(jacp)*rr<rr:return None
 return z,point

def phase(s,a,b,eta,eps,value):
 d=2+eps;ca=1+ar(Q(eta,2));cb=1+ar(Q(eps,2))
 da=GP(s+a)+2*PI*I*s-ca*GP(a);db=GP(s+b)-cb*GP(b)
 sa=GPP(s+a)+2*PI*I;sb=GPP(s+b);ss=GPP(s+a)+GPP(s+b)-d*GPP(s)
 aa=GPP(s+a)-ca*GPP(a)-sa*sa/ss
 ab=-sa*sb/ss;bb=GPP(s+b)-cb*GPP(b)-sb*sb/ss
 f=G(s+a)+G(s+b)-d*G(s)+2*PI*I*a*s-ca*G(a)-cb*G(b)if value else None
 return f,[da,db],[[aa,ab],[ab,bb]]
def seam_bounds(eps,beta,c):
 intervals=[(Q(-3,100),Q(0)),(Q(0),Q(1,50))]if beta==0 else[(Q(-57,1000),Q(0)),(Q(0),Q(7,500))]
 out=[]
 for low,high in intervals:
  if (eps,beta,c)==(1,1,1)and high==0:
   out.extend((h,ar('9/25'))for h in(low,high));continue
  sigma=1-2*c
  if min(sigma*low,sigma*high)>=0:
   out.extend((h,2*PI*ar(sigma*h)+ar(Q(eps,6)))for h in(low,high))
  else:
   radius=(2*PI*ar(min(sigma*low,sigma*high))).exp()
   bound=((1-radius)/2).asinh()+ar(Q(eps,6))
   out.extend((h,bound)for h in(low,high))
 return out

def reference_ok(ad,family,faces,grid,witness,original_ad):
 eta,eps,c=family;beta=eps if c==0 else eta;moving=1-c
 (a,b),(a0,b0),radii=parameters(ad,family,faces)
 origin=None if ad==original_ad else parameters(original_ad,family,faces)[1]
 root=enclose_root(a,b,a0,b0,eps,witness,origin)
 if root is None:return False
 s,s0=root
 _,grad,H=phase(s,a,b,eta,eps,False)
 f0,grad0,_=phase(s0,a0,b0,eta,eps,True)
 slope=grad[moving].real
 if not ar('-1/2')<slope<ar('1/2'):return False
 refs=[a,b];ref0=[a0,b0];vel=[tangent(eta,faces[0]),tangent(eps,faces[1])]
 def defect(chord_slope,intercept,h,e):
  target=[acb(e),acb(e)];target[moving]=I*ar(h)
  center=f0+sum(((target[j]-ref0[j])*grad0[j]for j in(0,1)),acb(0))
  coefficients=[refs[j]-target[j]+(ar(chord_slope)if j==moving else 0)for j in(0,1)]
  derivative=[sum((coefficients[j]*H[j][k]for j in(0,1)),acb(0))for k in(0,1)]
  return (ar(chord_slope)*grad0[moving]+intercept-center).real+sum((abs((derivative[j]*vel[j]).real)*radii[j]for j in(0,1)),arb(0))
 for h,rows in grid.items():
  for e in(0,1):
   used=0
   for l,r in zip(rows,rows[1:]):
    kl,kr=Q(l['kappa']),Q(r['kappa'])
    if slope<ar(kl)or slope>ar(kr):continue
    used+=1
    alpha=(Q(r['upper'])-Q(l['upper']))/(kr-kl)
    intercept=Q(l['upper'])-alpha*kl
    if not defect(alpha,ar(intercept),h,e)<ar('-1/1000'):return False
   assert used
 for h,bound in seam_bounds(eps,beta,c):
  for x in(0,1):
   for e in(0,1):
    if not defect(Q(-x),bound,h,e)<ar('-1/1000'):return False
 return True

def replay_cover(addresses,test):
 cover(addresses);accepted=[];refinements=0
 for original in addresses:
  todo=[original]
  while todo:
   ad=todo.pop()
   try:ok=test(ad,original)
   except(ValueError,ZeroDivisionError,AssertionError):ok=False
   if ok:accepted.append(ad)
   else:
    assert len(ad)<len(original)+16,(original,ad)
    refinements+=1;todo.extend([ad+'1',ad+'0'])
 cover(accepted)
 return len(accepted),refinements

def scalar_and_exact():
 v,R=sp.symbols('v R',positive=True)
 poly=16*v*v-4*R*v-(R-1)**2
 root=(R+sp.sqrt(R*R+4*(R-1)**2))/8
 assert sp.simplify(poly.subs(v,root))==0
 assert sp.expand((R+(1-R)**2/(4*v))/(4*v)-(4*R*v+(R-1)**2)/(16*v*v))==0
 a,b,t=sp.symbols('a b t')
 assert sp.simplify((a-a*a/t)+(b-b*b/t)-2*(-a*b/t)-(a+b-(a-b)**2/t))==0
 # The Schur identity is checked as a direct symmetric rank-one subtraction.
 H=sp.Matrix([[a,0],[0,b]])-sp.Matrix([a,b])*sp.Matrix([[a,b]])/t
 assert H[0,1]==-a*b/t and H==H.T
 assert J(Q(1,6))>ar('-1/6')
 radius=(57*PI/500).exp()
 vv=(radius+(radius*radius+4*(radius-1)**2).sqrt())/8
 assert 0<vv<1
 u=vv.sqrt().asin()/PI
 # Positive-frequency primitive, avoiding the purely imaginary zero argument.
 seam=G(acb(u,-ar('57/1000'))).real-2*G(acb(u)).real+57*PI*u/500
 assert seam<ar('7/25')
 assert 57*PI/500<ar('9/25')
 return 4,4

def main():
 global PI
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=320)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-all-endpoint-support-replay.json')
 args=ap.parse_args();assert args.precision>=192;ctx.prec=args.precision;PI=arb.pi()
 raw=INPUT.read_bytes();data=json.loads(raw);assert data['status']=='passed'
 assert data['proof_sha256']==sha(PROOF)and data['script_sha256']==sha(AUTHOR)
 assert data['reference_rectangles']=={str(k):v for k,v in RECTS.items()}
 assert Q(data['gap'])==Q(1,1000)
 dependencies=dict(data['dependencies']);dependencies[str(PROOF.relative_to(ROOT))]=sha(PROOF);dependencies[str(AUTHOR.relative_to(ROOT))]=sha(AUTHOR)
 pending=list(dependencies);seen=set()
 while pending:
  p=pending.pop()
  if p in seen:continue
  seen.add(p);assert sha(ROOT/p)==dependencies[p],p
  if p.endswith('.json'):
   record=json.loads((ROOT/p).read_text());assert record['status']=='passed'
   for f,digest in record.get('dependencies',{}).items():
    assert f not in dependencies or dependencies[f]==digest
    dependencies[f]=digest;pending.append(f)
 for stem,script,proof in[
  ('research-mixed-central-conditional-rectangles','certify_mixed_central_conditional_rectangles.py','research_mixed_central_conditional_rectangles.md'),
  ('research-mixed-type-four-height-refinement','certify_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md'),
  ('research-mixed-43-endpoint-support','check_mixed_43_endpoint_support.py','research_mixed_43_endpoint_support.md')]:
  d=json.loads((ROOT/f'repro/results/{stem}.json').read_text())
  assert d['script_sha256']==sha(ROOT/'experiments'/script)
  assert d['proof_sha256']==sha(ROOT/'notes'/proof)
 for stem,script in[
  ('research-mixed-type-four-height-refinement','replay_mixed_type_four_height_refinement.py'),
  ('research-mixed-43-endpoint-support','replay_mixed_43_endpoint_support.py')]:
  d=json.loads((ROOT/f'repro/results/{stem}-replay.json').read_text())
  assert d['script_sha256']==sha(ROOT/'experiments'/script)
  assert d.get('input_sha256',d.get('geometry_input_sha256'))==sha(ROOT/f'repro/results/{stem}.json')
 expected={(source,h,k)for source in SOURCES for h in heights(source[1])for k in KS}
 rows=data['source_grid']
 assert len(rows)==165 and {(tuple(r['source']),Q(r['height']),Q(r['kappa']))for r in rows}==expected
 cases=data['reference_cases']
 assert len(cases)==112 and {(tuple(r['family']),tuple(r['faces']))for r in cases}=={(fam,(a,b))for fam in FAMILIES for a in range(4)for b in range(4)}
 script_hash=sha(__file__);start=time.time();exact,scalars=scalar_and_exact()
 counts={'source':0,'reference':0};refinements=0;details=[]
 for row in rows:
  eps,beta,c=row['source'];h=Q(row['height']);k=Q(row['kappa']);target=ar(row['upper'])
  assert row['selected_alias']==int(beta and h>0)
  assert len(row['addresses'])==row['accepted']
  n,r=replay_cover(row['addresses'],lambda ad,orig:all(source_upper(ad,h,k,q,eps,beta,c)<target for q in sorted({0,beta})))
  counts['source']+=n;refinements+=r
  details.append({'kind':'source','source':row['source'],'height':str(h),'kappa':str(k),'cells':n,'refinements':r})
  print('source',row['source'],str(h),str(k),n,r,flush=True)
 for case in cases:
  fam=tuple(case['family']);eta,eps,c=fam;beta=eps if c==0 else eta
  grid={h:sorted([r for r in rows if r['source']==[eps,beta,c]and Q(r['height'])==h],key=lambda r:Q(r['kappa']))for h in heights(beta)}
  witnesses={w['address']:w for w in case['cells']};assert len(witnesses)==case['accepted']
  n,r=replay_cover(list(witnesses),lambda ad,orig:reference_ok(ad,fam,case['faces'],grid,witnesses[orig],orig))
  counts['reference']+=n;refinements+=r
  details.append({'kind':'reference','family':case['family'],'faces':case['faces'],'cells':n,'refinements':r})
  print('reference',fam,case['faces'],n,r,flush=True)
 assert sum(len(r['addresses'])for r in rows)==data['source_cells']
 assert sum(len(r['cells'])for r in cases)==data['reference_cells']
 assert INPUT.read_bytes()==raw and sha(__file__)==script_hash
 assert all(sha(ROOT/p)==digest for p,digest in dependencies.items())
 output={'status':'passed','precision_bits':args.precision,'source_values':165,'reference_products':112,
         'counts':counts,'refinements':refinements,'exact_identities':exact,'scalar_comparisons':scalars,
         'input_sha256':hashlib.sha256(raw).hexdigest(),'proof_sha256':sha(PROOF),
         'script_sha256':script_hash,'dependencies':dependencies,'details':details,
         'elapsed_seconds':time.time()-start,
         'analytic_independence':'Positive-frequency dilogarithm, original sine logarithms/cotangents, direct Jacobian, and exact binary-tree coverage; no author import or optimization.',
         'scope':data['scope']}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(output,indent=2)+'\n')
 print('PASS',counts,'refinements',refinements,flush=True)

if __name__=='__main__':main()
