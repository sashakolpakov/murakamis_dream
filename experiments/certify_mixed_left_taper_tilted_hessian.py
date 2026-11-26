#!/usr/bin/env python3
"""Certify the effective Hessian along the original unselected left taper."""
from pathlib import Path
from fractions import Fraction as R
import itertools,json,math,time,argparse,hashlib
import sympy as sp
import numpy as np
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_left_taper_tilted_hessian.md'
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--precision',type=int,default=256)
ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-left-taper-tilted-hessian.json')
args=ap.parse_args();assert args.precision>=192
ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=[
 'notes/research_mixed_asymmetric_wide_conditional_packets.md',
 'experiments/certify_mixed_asymmetric_wide_conditional_packets.py',
 'repro/results/research-mixed-asymmetric-wide-conditional-packets.json',
 'notes/research_mixed_transition_conditional_rectangles.md',
 'experiments/certify_mixed_transition_conditional_rectangles.py',
 'repro/results/research-mixed-transition-conditional-rectangles.json',
 'notes/research_mixed_plateau_accretivity.md',
 'notes/research_mixed_right_half_block_bound.md',
 'notes/research_mixed_type_three_window_strip.md',
 'notes/research_mixed_type_four_height_refinement.md',
 'notes/research_mixed_fourier_weight_continuation.md']
deps={p:sha(ROOT/p)for p in DEPS};ph=sha(PROOF);sh=sha(__file__)
for stem in ('asymmetric_wide_conditional_packets','transition_conditional_rectangles'):
 d=json.loads((ROOT/('repro/results/research-mixed-'+stem.replace('_','-')+'.json')).read_text())
 assert d['status']=='passed'
 assert d['script_sha256']==sha(ROOT/('experiments/certify_mixed_'+stem+'.py'))
 assert d['proof_sha256']==sha(ROOT/('notes/research_mixed_'+stem+'.md'))
 for p,h in d['dependencies'].items():assert sha(ROOT/p)==h,p
 assert d['boundary_pieces']==(32 if stem.startswith('asymmetric')else 64)
# Exact tilted Hessian identity, matrix concavity, and all taper reserves.
rho,A,B,C,E,G=sp.symbols('rho A B C E G',real=True)
assert sp.expand(sp.re((1+sp.I*rho)**2*(A+sp.I*B))-((1-rho**2)*A-2*rho*B))==0
assert sp.expand(sp.re((1+sp.I*rho)*(C+sp.I*E))-(C-rho*E))==0
assert sp.diff((1-rho**2)*A-2*rho*B,rho,2)==-2*A
x0,l,r3,r4=R('0.15'),R('.22'),R('.30'),R('.27')
assert x0*x0-2*r4*x0+l*l<0 and l<r4
f=lambda r:(1-(x0/l)**2)/(r-x0)
assert R('.03')*f(r3)<R('.13') and R('.057')*f(r4)<R('.26')
assert (r4-l)**2/4==R(1,1600)
assert R(1,1600)-R(1,8000)==R(1,2000)
ar=lambda x:arb(R(x).numerator)/R(x).denominator
rects={0:list(map(R,['.15','.45','-.03','.02'])),1:list(map(R,['.15','.45','-.057','0'])),2:list(map(R,['.24','.45','-.057','-.02']))}
gp=lambda z:(1-(-2*P*I*z).exp()).log()
gpp=lambda z:P*(P*z).cot()-P*I
pt=lambda z:acb(ar(str(z.real)),ar(str(z.imag)))
def box(ad):
 b=[R(0),R(1),R(0),R(1)]
 for j,c in enumerate(ad):
  k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(c)]=mid
 return b
def par(kind,face,lo,hi):
 xl,xh,yl,yh=rects[kind];cc=[acb(ar(xl),ar(yl)),acb(ar(xh),ar(yl)),acb(ar(xh),ar(yh)),acb(ar(xl),ar(yh))]
 return cc[face]+(cc[(face+1)%4]-cc[face])*ar(lo).union(ar(hi))
def root(a,b,a0,b0):
 af=complex(float(a0.real),float(a0.imag));bf=complex(float(b0.real),float(b0.imag));A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
 zs=[1j*np.log(v)/(2*np.pi)for v in np.roots([A,A*(B-3),2*A-B,1-A])]
 f=lambda z:np.log(1-np.exp(-2j*np.pi*z))
 zz=[z for z in zs if .19<z.real<.47 and -.22<z.imag<.16 and abs(f(z+af)+f(z+bf)-3*f(z)+2j*np.pi*af)<1e-7]
 if len(zz)!=1:return None
 z0=pt(zz[0]);h0=gpp(z0+a0)+gpp(z0+b0)-3*gpp(z0);Y=1/h0
 f0=gp(z0+a0)+gp(z0+b0)-3*gp(z0)+2*P*I*a0
 E=[gpp(z0+a0)+2*P*I,gpp(z0+b0)];dp=[a-a0,b-b0];D=[]
 for z in E:
  v=-Y*z;D.append(pt(complex(float(v.real.mid()),float(v.imag.mid()))))
 dz=sum((D[j]*dp[j]for j in(0,1)),acb(0));lin=f0+sum(((h0*D[j]+E[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,d):
  v=base+acb(arb(0,abs(d.real).upper()),arb(0,abs(d.imag).upper()))
  if not 0<v.real<1:return arb.pos_inf()
  return P*P*abs(1/(P*v).sin()**2)*abs(d)**2/2
 er=abs(Y)*(abs(lin)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+3*rem(z0,dz))
 if not er.is_finite():return None
 rad=R(max(1,math.ceil(float(er.upper())*1.5*2**42)),2**42)
 if rad>R(1,20):return None
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not ar('.19')<z.real<ar('.47')or not -ar('.22')<z.imag<ar('.16'):return None
 def dc(base,d):return -P*(P*d).sin()/((P*base).sin()*(P*(base+d)).sin())
 err=1-Y*h0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-3*dc(z0,delta))
 if not er+abs(err)*ar(rad)<ar(rad):return None
 return z,{'center':[str(zz[0].real),str(zz[0].imag)],'derivatives':[[str(float(v.real.mid())),str(float(v.imag.mid()))]for v in D],'radius':str(rad)}

def check(eta,fa,fb,ad):
 al,ah,bl,bh=box(ad);a=par(eta,fa,al,ah);b=par(2,fb,bl,bh);a0=par(eta,fa,(al+ah)/2,(al+ah)/2);b0=par(2,fb,(bl+bh)/2,(bl+bh)/2)
 rr=root(a,b,a0,b0)
 if rr is None:return None
 s,witness=rr
 p=gpp(s+a);q=gpp(s+b);den=p+q-3*gpp(s);U=p+2*P*I
 aa=-p+ar(1+R(eta,2))*gpp(a)+U*U/den;ab=U*q/den;bb=-q+ar('1.5')*gpp(b)+q*q/den
 if not aa.real>0:return None
 for rho in [R('-.13'),R('.13')]if eta==0 else[R('-.26'),R(0)]:
  tilt=acb(1,ar(rho));A=(tilt*tilt*aa).real-ar('.5');B=(tilt*ab).real;C=bb.real-ar('.5')
  if not A>0 or not A*C-B*B>0:return None
 return witness
start=time.time();out=[];total=0
for eta,fa,fb in itertools.product((0,1),range(4),range(4)):
 todo=[''];yes=[];witnesses=[];vis=0
 while todo:
  ad=todo.pop();vis+=1;total+=1
  try:ok=check(eta,fa,fb,ad)
  except(ValueError,ZeroDivisionError):ok=False
  if ok:yes.append(ad);witnesses.append({'address':ad,**ok})
  else:
   assert len(ad)<30,(eta,fa,fb,ad)
   todo.extend([ad+'0',ad+'1'])
  assert total<150000
 yes.sort();assert sum((R(1,2**len(a))for a in yes),R(0))==1
 assert all(not b.startswith(a)for a,b in zip(yes,yes[1:]))
 out.append(dict(eta=eta,faces=[fa,fb],addresses=yes,witnesses=witnesses,visited=vis));print(eta,fa,fb,len(yes),vis,time.time()-start,flush=True)
assert len(out)==32
assert {(c['eta'],*c['faces'])for c in out}==set(itertools.product((0,1),range(4),range(4)))
for c in out:
 assert len(c['addresses'])==len(set(c['addresses']))
 assert set(c['addresses'])=={w['address']for w in c['witnesses']}
assert deps=={p:sha(ROOT/p)for p in DEPS}and ph==sha(PROOF)and sh==sha(__file__)
record=dict(status='passed',precision_bits=args.precision,cases=out,boundary_products=32,
 visited_cells=total,accepted_cells=sum(len(c['addresses'])for c in out),elapsed_seconds=time.time()-start,
 rectangles={str(k):[str(v)for v in r]for k,r in rects.items()},
 tilt_intervals={'0':['-13/100','13/100'],'1':['-13/50','0']},
 strict_hessian_lower='1/2',action_gap='1/1600',finite_source_gap='1/2000',
 exact_matrix_identity_count=3,exact_rational_checks=5,
 proof_sha256=ph,script_sha256=sh,dependencies=deps,
 scope='Unselected own-four source with left angle [.15,.22] and own angle [.24,.45], original critical heights and quadratic left taper. No selected alias, both-low pair or full cyclic theorem.')
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(record,indent=2)+'\n')
print('Certified',record['accepted_cells'],'boundary cells; all tilted Hessians exceed I/2.')
