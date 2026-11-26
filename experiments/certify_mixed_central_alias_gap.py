#!/usr/bin/env python3
"""Global central alias budget via conditional Schur quadratic forms.

The original logarithmic root is certified by rational affine Newton
witnesses. All matrix inequalities are outward interval comparisons.
Floating roots propose witnesses only. The harmonic extension and
Taylor summation are separate written proofs.
"""
import argparse,hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from fractions import Fraction as R
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_central_alias_gap.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=100000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-central-alias-gap.json')
args=parser.parse_args()
DEPS=[
 'notes/research_mixed_central_conditional_rectangles.md',
 'experiments/certify_mixed_central_conditional_rectangles.py',
 'repro/results/research-mixed-central-conditional-rectangles.json',
 'notes/research_mixed_type_three_window_strip.md',
 'repro/results/research-mixed-type-three-window-strip.json',
 'repro/results/research-mixed-type-three-window-strip-replay.json',
 'notes/research_mixed_cyclic_critical_height_bounds.md',
 'notes/research_mixed_conditional_torus_composition.md',
 'notes/research_mixed_central_outer_integral.md',
 'repro/results/research-mixed-central-outer-integral.json',
 'notes/research_mixed_fourier_weight_continuation.md',
 'repro/results/research-mixed-fourier-weight-continuation.json',
]
hashes={p:sha(ROOT/p)for p in DEPS};proof_hash=sha(PROOF);script_hash=sha(__file__)
for p in DEPS:
 if p.endswith('.json'):assert json.loads((ROOT/p).read_text())['status']=='passed'
source=json.loads((ROOT/'repro/results/research-mixed-central-conditional-rectangles.json').read_text())
assert source['proof_sha256']==sha(ROOT/'notes/research_mixed_central_conditional_rectangles.md')
assert source['script_sha256']==sha(ROOT/'experiments/certify_mixed_central_conditional_rectangles.py')
for p,h in source['dependencies'].items():assert sha(ROOT/p)==h
ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
def ar(x):x=R(x);return arb(x.numerator)/x.denominator
def pt(z):return acb(ar(str(z.real)),ar(str(z.imag)))
def cot(z):return (P*z).cot()
def gp(z):return (1-(-2*P*I*z).exp()).log()
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def phase(s,a,b,d):return g(s+a)+g(s+b)-d*g(s)+2*P*I*a*s
def fp(s,a,b,d):return gp(s+a)+gp(s+b)-d*gp(s)+2*P*I*a
def hs(s,a,b,d):return P*(cot(s+a)+cot(s+b)-d*cot(s))+(d-2)*P*I
RECTS={'3':['1/4','2/5','-3/100','1/50'],'4':['1/4','2/5','-57/1000','141/10000']}
def corners(kind):
 a,b,c,d=map(ar,RECTS[kind]);return[acb(a,c),acb(b,c),acb(b,d),acb(a,d)]
def params(kinds,parts,box):
 pp=[];p0=[];vel=[]
 for j,(kind,part)in enumerate(zip(kinds,parts)):
  cc=corners(kind);v=cc[(part+1)%4]-cc[part];lo,hi=box[2*j:2*j+2];pp.append(cc[part]+v*ar(lo).union(ar(hi)));p0.append(cc[part]+v*ar((lo+hi)/2));vel.append(v)
 return pp,p0,vel

def decode(ad):
 z=[R(0),R(1),R(0),R(1)]
 for j,c in enumerate(ad):
  k=2*(j%2);mid=(z[k]+z[k+1])/2;z[k+1-int(c)]=mid
 return z

def check(ad,eps,kinds,parts):
 box=decode(ad);pp,p0,vel=params(kinds,parts,box);a,b=pp;a0,b0=p0;d=2+eps
 af=complex(float(a0.real),float(a0.imag));bf=complex(float(b0.real),float(b0.imag));A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
 co=[A*(B-1),A-B,1-A]if eps==0 else[A,A*(B-3),2*A-B,1-A]
 zs=[1j*np.log(v)/(2*np.pi)for v in np.roots(co)]
 roots=[z for z in zs if .15<z.real<.49 and abs(z.imag)<.15 and abs(np.log(1-np.exp(-2j*np.pi*(z+af)))+np.log(1-np.exp(-2j*np.pi*(z+bf)))-d*np.log(1-np.exp(-2j*np.pi*z))+2j*np.pi*af)<1e-7]
 if len(roots)!=1:return None,('rootproposal',zs)
 z0=pt(roots[0]);H0=hs(z0,a0,b0,d);Y=1/H0;f0=fp(z0,a0,b0,d);E0=[P*cot(z0+a0)+P*I,P*cot(z0+b0)-P*I]
 deriv=[pt(complex(float((-Y*v).real.mid()),float((-Y*v).imag.mid())))for v in E0];dp=[pp[j]-p0[j]for j in(0,1)];dz=sum((deriv[j]*dp[j]for j in(0,1)),acb(0))
 lin=f0+sum(((H0*deriv[j]+E0[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,delta):
  v=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(0<v.real<1):return arb.pos_inf()
  return P*P*abs(1/(P*v).sin()**2)*abs(delta)**2/2
 er=abs(Y)*(abs(lin)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+d*rem(z0,dz))
 if not er.is_finite():return None,'infinite'
 rad=R(max(1,math.ceil(float(er.upper())*1.5*2**40)),2**40)
 if rad>R(1,20):return None,'large radius'
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not(ar('3/20')<z.real<ar('49/100') and abs(z.imag)<ar('3/20')):return None,'root rectangle'
 def dc(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 ee=1-Y*H0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):return None,'selfmap'
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*hs(zp,a0,b0,d)
 if not abs(Y*f0)+abs(ep)*rr<rr:return None,'point'
 return {'z':z,'a':a,'b':b,'center':[str(roots[0].real),str(roots[0].imag)],'D':[[str(float(v.real.mid())),str(float(v.imag.mid()))]for v in deriv],'rad':str(rad)},None
def gpp(z):return P*cot(z)-P*I
def budget(ad,e,kinds,parts):
 rr,why=check(ad,e,kinds,parts)
 if rr is None:return None,why
 s,a,b=rr['z'],rr['a'],rr['b'];p,q=gpp(s+a),gpp(s+b);u,v=p+2*P*I,q;H=p+q-(2+e)*gpp(s)
 ha=p-gpp(a)-u*u/H;hb=q-(1+e)*gpp(b)-v*v/H;hc=-u*v/H
 A,C,E=-ha.real,-hb.real,-hc.real;U,W,V=ha.imag,hb.imag,hc.imag
 det=A*C-E*E
 if not(A>0 and C>0 and det>0):return None,'positive'
 ca=A+(C*U*U-2*E*U*V+A*V*V)/det
 cb=C+(C*V*V-2*E*V*W+A*W*W)/det
 cc=E+(C*U*V-E*(U*W+V*V)+A*V*W)/det
 if kinds[0]=='4' and not ca<10:return None,('a',str(ca))
 if kinds[1]=='4' and not cb<15:return None,('b',str(cb))
 if kinds==('4','4') and not cc<0:return None,('cross',str(cc))
 return {'ca':ca,'cb':cb,'cc':cc,'root':rr},None
families=[(0,('3','3')),(0,('4','3')),(1,('3','4')),(1,('4','4'))]
allout=[];visits=0;start=time.time()
for e,kinds in families:
 for parts in itertools.product(range(4),repeat=2):
  pending=[''.join(x)for x in itertools.product('01',repeat=6)];accepted=[];witnesses=[];mxa=0;mxb=0;mxc=-100
  while pending:
   ad=pending.pop();ret,why=budget(ad,e,kinds,parts);visits+=1
   if ret:
    accepted.append(ad);w=ret['root'];witnesses.append({'address':ad,'center':w['center'],'affine_derivatives':w['D'],'remainder_radius':w['rad']});mxa=max(mxa,float(ret['ca'].upper()));mxb=max(mxb,float(ret['cb'].upper()));mxc=max(mxc,float(ret['cc'].upper()))
   elif len(ad)<22:pending.extend([ad+'0',ad+'1'])
   else:raise RuntimeError((e,kinds,parts,ad,why))
   assert visits<args.max_visits,'bounded pilot'
  row={'eps':e,'kinds':kinds,'parts':parts,'accepted':len(accepted),'ca':mxa,'cb':mxb,'cc':mxc,'addresses':accepted,'witnesses':witnesses};allout.append(row)
  print(json.dumps({k:v for k,v in row.items()if k not in ('addresses','witnesses')}),flush=True)
# Exact dyadic coverage is independent of every analytic predicate.
for c in allout:
 codes=set(c['addresses'])
 assert len(codes)==len(c['addresses'])==len(c['witnesses'])
 assert codes=={w['address']for w in c['witnesses']}
 assert sum((R(1,2**len(a))for a in codes),R(0))==1
 prefixes={a[:j]for a in codes for j in range(len(a))}
 assert not(codes & prefixes)
 for p in prefixes:assert all(p+b in codes or p+b in prefixes for b in '01')
 for w in c['witnesses']:
  for x in w['center']:R(x)
  for row in w['affine_derivatives']:
   for x in row:R(x)
  assert R(w['remainder_radius'])>0
assert len(allout)==64
assert {(c['eps'],tuple(c['kinds']),tuple(c['parts']))for c in allout}=={
 (e,ks,ps)for e,ks in families for ps in itertools.product(range(4),repeat=2)}
h=ar('7/500');z=acb(ar('2/5'),h);nu=-g(z).real
scalar=[]
def pos(name,value):
 assert value>0,(name,str(value))
 scalar.append({'name':name,'margin':str(value)})
pos('minimum true Fourier exponent exceeds 721/10000',nu-ar('721/10000'))
pos('frequency penalty exceeds 721/10000',2*P*h-ar('721/10000'))
margin=R(721,10000)-R(25,2)*R(71,1000)**2-R(1,1000)-R(1,125)
assert margin==R(7,80000)
pos('final exact rational reserve',ar(margin))
assert hashes=={p:sha(ROOT/p)for p in DEPS}
assert proof_hash==sha(PROOF) and script_hash==sha(__file__)
out={
 'status':'passed','precision_bits':args.precision,
 'scope':'Complete nonempty alias terms on the whole central outer real box; no estimate of its exterior complement.',
 'boundary_pieces':64,'accepted_cells':sum(c['accepted']for c in allout),
 'visited_cells':visits,'parameter_rectangles':RECTS,'families':families,
 'matrix_requirements':{'A':'positive definite','Kaa_when_left_four':'<10','Kbb_when_own_four':'<15','Kab_in_four_four':'<0'},
 'height':'7/500','height_displacement_upper':'71/1000','total_action_coefficient':'25/2',
 'true_weight_exponent_lower':'721/10000','weight_epsilon':'1/1000','final_gap_per_alias':'1/125',
 'strict_scalar_comparisons':scalar,'exact_scalar_identity_count':1,
 'cases':allout,'elapsed_seconds':time.time()-start,
 'script_sha256':script_hash,'proof_sha256':proof_hash,'dependencies':hashes,
 'summary_scope':'Decimal extrema are diagnostics only; all acceptance comparisons use outward Arb intervals and exact rational thresholds.',
}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(allout),'pieces,',out['accepted_cells'],'cells,',visits,'visits;3 scalar bounds+1 exact identity',flush=True)
