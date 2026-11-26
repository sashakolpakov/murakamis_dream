#!/usr/bin/env python3
"""Outward tilted condensed Hessian bounds for one or two unselected right tapers.

The full canonical source and global holomorphic root are proved inputs.
Acceptance uses original logarithmic affine Newton self-maps, both tilt
endpoints, exact binary coverage and the integrated rational gap.
"""
import argparse, hashlib, itertools, json, math, time
from pathlib import Path
import numpy as np
from fractions import Fraction as R
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_unselected_right_taper_products.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=250000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-taper-products.json')
args=parser.parse_args()
assert args.precision>=128
DEPENDENCIES=[
 'experiments/certify_mixed_right_square_conditional_packets.py',
 'repro/results/research-mixed-right-square-conditional-packets.json',
 'notes/research_mixed_right_taper_tilt.md',
 'notes/research_mixed_right_guard_conditional_packets.md',
 'experiments/certify_mixed_right_guard_conditional_packets.py',
 'repro/results/research-mixed-right-guard-conditional-packets.json',
 'notes/research_mixed_plateau_accretivity.md',
 'notes/research_mixed_type_four_height_refinement.md',
 'notes/research_mixed_transition_conditional_rectangles.md',
 'experiments/certify_mixed_transition_conditional_rectangles.py',
 'repro/results/research-mixed-transition-conditional-rectangles.json',
 'notes/research_mixed_central_conditional_rectangles.md',
 'experiments/certify_mixed_central_conditional_rectangles.py',
 'repro/results/research-mixed-central-conditional-rectangles.json',
 'notes/research_mixed_type_three_window_strip.md',
 'experiments/certify_mixed_type_three_window_strip.py',
 'experiments/replay_mixed_type_three_window_strip.py',
 'repro/results/research-mixed-type-three-window-strip.json',
 'repro/results/research-mixed-type-three-window-strip-replay.json',
 'notes/research_mixed_shifted_conditional_packets.md',
 'notes/research_mixed_reoptimized_alias_action.md',
 'experiments/check_mixed_reoptimized_alias_action.py',
 'repro/results/research-mixed-reoptimized-alias-action.json',
 'notes/research_mixed_conditional_image_contours.md',
 'notes/research_mixed_conditional_critical_images.md',
 'experiments/certify_mixed_conditional_critical_images.py',
 'experiments/replay_mixed_conditional_critical_images.py',
 'repro/results/research-mixed-conditional-critical-images.json',
 'repro/results/research-mixed-conditional-critical-images-replay.json',
 'notes/research_mixed_cyclic_critical_height_bounds.md',
 'notes/research_mixed_three_canonical_conditional.md',
 'notes/research_mixed_four_conditional_complex_neighbors.md',
 'notes/exact_factorial_interpolation_and_complex_contours.md',
 'notes/research_mixed_fourier_weight_continuation.md',
 'notes/research_mixed_conditional_torus_composition.md',
]
initial_hashes={p:sha(ROOT/p)for p in DEPENDENCIES}
proof_hash=sha(PROOF);script_hash=sha(__file__)
for name,script,proof in [
 ('research-mixed-reoptimized-alias-action','check_mixed_reoptimized_alias_action.py','research_mixed_reoptimized_alias_action.md'),
 ('research-mixed-conditional-critical-images','certify_mixed_conditional_critical_images.py','research_mixed_conditional_critical_images.md'),
]:
 rec=json.loads((ROOT/f'repro/results/{name}.json').read_text())
 assert rec['status']=='passed'
 assert rec['script_sha256']==sha(ROOT/'experiments'/script)
 assert rec['proof_sha256']==sha(ROOT/'notes'/proof)
window=json.loads((ROOT/'repro/results/research-mixed-type-three-window-strip.json').read_text())
assert window['status']=='passed' and window['accepted_cells']==8525
assert window['script_sha256']==sha(ROOT/'experiments/certify_mixed_type_three_window_strip.py')
assert window['proof_sha256']==sha(ROOT/'notes/research_mixed_type_three_window_strip.md')
wr=json.loads((ROOT/'repro/results/research-mixed-type-three-window-strip-replay.json').read_text())
assert wr['status']=='passed' and wr['accepted_cells']==8525
assert wr['input_sha256']==sha(ROOT/'repro/results/research-mixed-type-three-window-strip.json')
assert wr['script_sha256']==sha(ROOT/'experiments/replay_mixed_type_three_window_strip.py')
assert wr['proof_sha256']==window['proof_sha256']
review=json.loads((ROOT/'repro/results/research-mixed-conditional-critical-images-replay.json').read_text())
assert review['status']=='passed'
ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
def ar(x):x=R(x);return arb(x.numerator)/x.denominator
def pt(z):return acb(ar(str(z.real)),ar(str(z.imag)))
def cot(z):return (P*z).cot()
def gp(z):return (1-(-2*P*I*z).exp()).log()
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def phase(s,a,b,d):return g(s+a)+g(s+b)-d*g(s)+2*P*I*a*s
def fp(s,a,b,d):return gp(s+a)+gp(s+b)-d*gp(s)+2*P*I*a
def hs(s,a,b,d):return P*(cot(s+a)+cot(s+b)-d*cot(s))+(d-2)*P*I
RECTS={'p3':['11/50','9/20','-3/100','1/50'],'p4':['11/50','9/20','-57/1000','-1/50'],'e3':['11/50','9/20','-3/100','1/50'],'e4':['11/50','9/20','-57/1000','0'],'r3':['11/50','1/2','-3/100','1/50'],'r4':['11/50','1/2','-57/1000','0']}
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

def check(ad,eta,eps,side,region,kinds,parts):
 box=decode(ad);pp,p0,vel=params(kinds,parts,box);a,b=pp;a0,b0=p0;d=2+eps
 af=complex(float(a0.real),float(a0.imag));bf=complex(float(b0.real),float(b0.imag));A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
 co=[A*(B-1),A-B,1-A]if eps==0 else[A,A*(B-3),2*A-B,1-A]
 zs=[1j*np.log(v)/(2*np.pi)for v in np.roots(co)]
 roots=[z for z in zs if .15<z.real<.49 and abs(z.imag)<.17 and abs(np.log(1-np.exp(-2j*np.pi*(z+af)))+np.log(1-np.exp(-2j*np.pi*(z+bf)))-d*np.log(1-np.exp(-2j*np.pi*z))+2j*np.pi*af)<1e-7]
 if len(roots)!=1:return None,('rootproposal',zs)
 z0=pt(roots[0]);H0=hs(z0,a0,b0,d);Y=1/H0;f0=fp(z0,a0,b0,d);E0=[P*cot(z0+a0)+P*I,P*cot(z0+b0)-P*I]
 deriv_proposals=[complex(float((-Y*v).real.mid()),float((-Y*v).imag.mid()))for v in E0];deriv=[pt(v)for v in deriv_proposals];dp=[pp[j]-p0[j]for j in(0,1)];dz=sum((deriv[j]*dp[j]for j in(0,1)),acb(0))
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
 if not(ar('1/5')<z.real<ar('23/50') and abs(z.imag)<ar('17/100')):return None,'root rectangle'
 def dc(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 ee=1-Y*H0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):return None,'selfmap'
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*hs(zp,a0,b0,d)
 if not abs(Y*f0)+abs(ep)*rr<rr:return None,'point'
 Hss=hs(z,a,b,d)
 hsa=P*cot(z+a)+P*I;hsb=P*cot(z+b)-P*I
 haa=P*cot(z+a)-(1+ar(eta)/2)*P*cot(a)+ar(eta)*P*I/2
 hbb=P*cot(z+b)-(1+ar(eps)/2)*P*cot(b)+ar(eps)*P*I/2
 HH=[-haa+hsa*hsa/Hss,-hbb+hsb*hsb/Hss];off=hsa*hsb/Hss
 if not all(v.real>ar('1/100')for v in HH):return None,'tilt concavity'
 tilts=[(R(0),R(7,20))if typ else(R(-1,5),R(3,10))for typ in(eta,eps)]
 threshold=ar('11/100')if region=='e'else -ar('7/20');margins=[]
 for ta,tb in itertools.product(*tilts):
  da=1+I*ar(ta);db=1+I*ar(tb);aa=(da*da*HH[0]).real-threshold;bb=(da*db*off).real;cc=(db*db*HH[1]).real-threshold
  determinant=aa*cc-bb*bb
  if not(aa>0 and cc>0 and determinant>0):return None,('matrix',str(aa),str(cc),str(determinant))
  margins.append([str(aa),str(cc),str(determinant)])
 return {'center':[str(roots[0].real),str(roots[0].imag)],'deriv':[[str(v.real),str(v.imag)]for v in deriv_proposals],'radius':str(rad),'margins':margins,'tiltconcavity':str(HH[side].real)},None

# The global parameter branch is already proved on every complete product.
right=json.loads((ROOT/'repro/results/research-mixed-right-square-conditional-packets.json').read_text())
assert right['status']=='passed'
assert right['script_sha256']==sha(ROOT/'experiments/certify_mixed_right_square_conditional_packets.py')
assert right['proof_sha256']==proof_hash
for p,dig in right['dependencies'].items():assert sha(ROOT/p)==dig
families=[]
for eta,eps,side,region in itertools.product((0,1),(0,1),(0,),('e','r')):
 kinds=[region+str(3+eta),region+str(3+eps)];families.append((eta,eps,side,region,tuple(kinds)))
start=time.time();count=0;allout=[]
for eta,eps,side,region,kinds in families:
 for parts in itertools.product(range(4),repeat=2):
  pending=[''.join(x)for x in itertools.product('01',repeat=4)];accepted=[];witnesses=[]
  while pending:
   ad=pending.pop();count+=1;ret,why=check(ad,eta,eps,side,region,kinds,parts)
   if ret:
    accepted.append(ad);witnesses.append({'address':ad,'center':ret['center'],'affine_derivatives':ret['deriv'],'remainder_radius':ret['radius']})
   elif len(ad)<28:pending.extend([ad+'0',ad+'1'])
   else:raise RuntimeError((eta,eps,side,region,kinds,parts,ad,why))
   if count>args.max_visits:raise RuntimeError('explicit budget')
   if count%2000==0:print('progress',count,'accepted',len(accepted),'pending',len(pending),round(time.time()-start,1),flush=True)
  row={'eta':eta,'eps':eps,'side':side,'region':region,'kinds':kinds,'parts':parts,'accepted':len(accepted),'addresses':accepted,'witnesses':witnesses};allout.append(row)
  print(json.dumps({k:v for k,v in row.items()if k not in('addresses','witnesses')}),flush=True)
for case in allout:
 codes=set(case['addresses']);assert len(codes)==len(case['addresses'])==len(case['witnesses'])
 assert codes=={w['address']for w in case['witnesses']}
 assert sum((R(1,2**len(v))for v in codes),R(0))==1
 prefixes={a[:j]for a in codes for j in range(len(a))};assert not(codes & prefixes)
 for p in prefixes:assert all(p+b in codes or p+b in prefixes for b in'01')
assert len(allout)==128
assert {(c['eta'],c['eps'],c['side'],c['region'],tuple(c['kinds']),tuple(c['parts']))for c in allout}=={(*f,ps)for f in families for ps in itertools.product(range(4),repeat=2)}
# Exact right-taper tilt bounds and integrated quadratic reserve.
for h,A,T in [(R(3,100),R(11,100),R(3,10)),(R(1,50),R(11,100),R(1,5)),(R(57,1000),R(17,100),R(7,20))]:
 # h*(1-400d^2) <= T*(A-d), 0<=d<=.05; the unconstrained quadratic minimum suffices.
 minimum=T*A-h-T*T/(1600*h)
 assert minimum>0
assert R(11,100)-(R(11,100)+R(7,20))*R(25,121)==R(181,12100)
assert R(3,50)**2*R(181,24200)>R(1,40000)
assert initial_hashes=={p:sha(ROOT/p)for p in DEPENDENCIES}
assert proof_hash==sha(PROOF)and script_hash==sha(__file__)
out={'status':'passed','scope':'Tilted condensed Hessian bounds for one or two unselected right tapers and one unselected plateau leg; no selected-alias claim.','precision_bits':args.precision,'boundary_pieces':128,'accepted_cells':sum(x['accepted']for x in allout),'visited_cells':count,'parameter_rectangles':RECTS,'families':families,'cases':allout,'early_lower':'11/100','late_lower':'-7/20','own_real_diagonal_lower':'1/100','type_three_tilts':['-1/5','3/10'],'type_four_tilts':['0','7/20'],'exact_scalar_checks':5,'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies':initial_hashes,'elapsed_seconds':time.time()-start}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(allout),'products',out['accepted_cells'],'cells',count,'visits',flush=True)
