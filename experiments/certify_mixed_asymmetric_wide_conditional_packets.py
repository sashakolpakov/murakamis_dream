#!/usr/bin/env python3
"""Outward full-source certificate on two independent asymmetric products with a wider own-four angle.

Floating polynomial roots are proposals only. Acceptance uses the original
logarithmic equation, rational affine Newton witnesses, full real-row tails,
and both horizontal aliases. No upstream certificates are rerun.
"""
import argparse, hashlib, itertools, json, math, time
from pathlib import Path
import numpy as np
from fractions import Fraction as R
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_asymmetric_wide_conditional_packets.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=50000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-asymmetric-wide-conditional-packets.json')
args=parser.parse_args()
assert args.precision>=128
DEPENDENCIES=[
 'notes/research_mixed_asymmetric_low_conditional_packets.md',
 'experiments/certify_mixed_asymmetric_low_conditional_packets.py',
 'repro/results/research-mixed-asymmetric-low-conditional-packets.json',
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
narrow=json.loads((ROOT/'repro/results/research-mixed-asymmetric-low-conditional-packets.json').read_text())
assert narrow['status']=='passed'
assert narrow['proof_sha256']==sha(ROOT/'notes/research_mixed_asymmetric_low_conditional_packets.md')
assert narrow['script_sha256']==sha(ROOT/'experiments/certify_mixed_asymmetric_low_conditional_packets.py')
for p,h in narrow['dependencies'].items():assert sha(ROOT/p)==h,p
transition=json.loads((ROOT/'repro/results/research-mixed-transition-conditional-rectangles.json').read_text())
assert transition['status']=='passed'
assert transition['proof_sha256']==sha(ROOT/'notes/research_mixed_transition_conditional_rectangles.md')
assert transition['script_sha256']==sha(ROOT/'experiments/certify_mixed_transition_conditional_rectangles.py')
for p,h in transition['dependencies'].items():assert sha(ROOT/p)==h,p
# Exact inclusions used in the holomorphic joining corollary.
assert R(2,25)<R(1,10)<R(49,100)
assert -R(11,50)<-R(17,100)<R(3,20)
assert R(6,25)>R(11,50)and R(9,20)<R(23,50)
ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
def ar(x):x=R(x);return arb(x.numerator)/x.denominator
def pt(z):return acb(ar(str(z.real)),ar(str(z.imag)))
def cot(z):return (P*z).cot()
def gp(z):return (1-(-2*P*I*z).exp()).log()
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def phase(s,a,b,d):return g(s+a)+g(s+b)-d*g(s)+2*P*I*a*s
def fp(s,a,b,d):return gp(s+a)+gp(s+b)-d*gp(s)+2*P*I*a
def hs(s,a,b,d):return P*(cot(s+a)+cot(s+b)-d*cot(s))+(d-2)*P*I
RECTS={'a3':['3/20','11/50','-3/100','1/50'],'a4':['3/20','11/50','-57/1000','141/10000'],'b4':['6/25','23/50','-57/1000','141/10000']}
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
 roots=[z for z in zs if .15<z.real<.49 and abs(z.imag)<.23 and abs(np.log(1-np.exp(-2j*np.pi*(z+af)))+np.log(1-np.exp(-2j*np.pi*(z+bf)))-d*np.log(1-np.exp(-2j*np.pi*z))+2j*np.pi*af)<1e-7]
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
 if not(ar('6/25')<z.real<ar('21/50') and -ar('21/100')<z.imag<ar('3/20')):return None,'root rectangle'
 def dc(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 ee=1-Y*H0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):return None,'selfmap'
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*hs(zp,a0,b0,d)
 if not abs(Y*f0)+abs(ep)*rr<rr:return None,'point'
 selected=phase(zp,a0,b0,d);qa=gp(z+a)+2*P*I*z;qb=gp(z+b);dt=[ar((box[2*j+1]-box[2*j])/2)for j in(0,1)]
 def lower(v,ga,gb):return v.real-abs((ga*vel[0]).real)*dt[0]-abs((gb*vel[1]).real)*dt[1]
 gaps=[]
 for cut in('2/25','49/100'):
  c=acb(ar(cut));gaps.append(lower(selected-phase(c,a0,b0,d),qa-gp(c+a)-2*P*I*c,qb-gp(c+b)))
 for u,v in itertools.product((0,1),repeat=2):gaps.append(lower(selected-g(a0)-g(b0)-2*P*I*u*a0+2*P*I*v*b0,qa-gp(a)-2*P*I*u,qb-gp(b)+2*P*I*v))
 if not all(v>ar('1/10000')for v in gaps):return None,('gap',[str(v)for v in gaps])
 va=(2*P*a.real).sin()/((2*P*a.imag).cosh()-(2*P*a.real).cos());vb=(2*P*b.real).sin()/((2*P*b.imag).cosh()-(2*P*b.real).cos());wl=-(49*P/100).cot();wr=max(va.upper(),vb.upper());factor=(2*P*(b.imag-a.imag)).exp()/4**eps;ca,sa=(P*a).cos(),(P*a).sin();cb,sb=(P*b).cos(),(P*b).sin();worst=arb(0)
 for j in range(12):
  w=(wl+(wr-wl)*j/12).union(wl+(wr-wl)*(j+1)/12);v=factor*abs(ca-w*sa)**2*abs(cb-w*sb)**2*(1+w*w)**eps;worst=max(worst,v.upper())
 if not worst<1:return None,('shape',str(worst))
 aliases=[]
 for height in('-1/4','1/5'):
  for j in range(8):
   # Global real-index concavity bounds this entire horizontal segment
   # by its midpoint tangent, retaining the original logarithmic derivative.
   x=ar(R(2,25)+R(41,100)*R(2*j+1,16));c=acb(x,ar(height))
   v=lower(selected-phase(c,a0,b0,d),qa-gp(c+a)-2*P*I*c,qb-gp(c+b))+2*P*abs(ar(height))
   v-=abs(fp(c,a,b,d).real)*ar('41/1600')
   if not v>ar('1/1000'):return None,('alias',height,j,str(v))
   aliases.append(v)
 return {'gaps':gaps,'shape':worst,'aliases':aliases,'center':[str(roots[0].real),str(roots[0].imag)],'deriv':[[str(v.real),str(v.imag)]for v in deriv_proposals],'radius':str(rad)},None

families=[(1,('a3','b4')),(1,('a4','b4'))]
# Global root existence precedes the distinguished-boundary source estimates.
root_faces=[]
edges={}
for kind in RECTS:
 cc=corners(kind)
 edges[kind]=[cc[j]+(cc[(j+1)%4]-cc[j])*ar(R(k,32)).union(ar(R(k+1,32)))
              for j in range(4) for k in range(32)]
for eps,kinds in families:
 bottom=R(-11,50)
 top=R(3,20)
 for face in range(4):
  margins=[]
  for j in range(128):
   xx=ar(R(2,25)+R(41,100)*R(j,128)).union(ar(R(2,25)+R(41,100)*R(j+1,128)))
   yy=ar(bottom+(top-bottom)*R(j,128)).union(ar(bottom+(top-bottom)*R(j+1,128)))
   z=(acb(ar('2/25'),yy),acb(ar('49/100'),yy),acb(xx,ar(bottom)),acb(xx,ar(top)))[face]
   component=(lambda v:v.real)if face<2 else(lambda v:v.imag)
   left=[component(gp(z+a)+2*P*I*a)for a in edges[kinds[0]]]
   right=[component(gp(z+b))for b in edges[kinds[1]]]
   constant=component(-(2+eps)*gp(z))
   margin=(min(v.lower()for v in left)+min(v.lower()for v in right)+constant.lower())if face in(0,2)else -(max(v.upper()for v in left)+max(v.upper()for v in right)+constant.upper())
   assert margin>ar('1/50'),('root face',eps,kinds,face,j,str(margin))
   margins.append(margin)
  root_faces.append({'eps':eps,'kinds':kinds,'face':face,'slabs':128,'bottom':str(bottom),'top':str(top),'margin':str(min(v.lower() for v in margins))})
# Positive shifted cotangents decrease throughout the actual real ranges:
# their smallest real argument is .08+.15=.23, and |Im|<=.307.
shifted_monotonicity=1-(46*P/100).cos()*(614*P/1000).cosh()
assert shifted_monotonicity>0
curvature_min=None
curvature_cells=0
for eps,kinds in families:
 for ix in range(192):
  x=ar(R(2,25)+R(27,100)*R(ix,192)).union(ar(R(2,25)+R(27,100)*R(ix+1,192)))
  for iy in range(320):
   y=ar(-R(1,4)+R(9,20)*R(iy,320)).union(ar(-R(1,4)+R(9,20)*R(iy+1,320)))
   own=(2*P*x).sin()/((2*P*y).cosh()-(2*P*x).cos())
   shifted=[]
   for kind in kinds:
    lo=(y.lower()+ar(RECTS[kind][2])).lower()
    hi=(y.upper()+ar(RECTS[kind][3])).upper()
    near=lo if lo>0 else -hi if hi<0 else arb(0)
    xx=x+ar(RECTS[kind][0])
    v=(2*P*xx).sin()/((2*P*near).cosh()-(2*P*xx).cos())
    shifted.append(max(arb(0),v.upper()))
   bound=P*(3*own.lower()-sum(shifted,arb(0)))
   assert bound>ar('1/8'),('curvature',kinds,ix,iy,str(bound))
   curvature_min=bound.lower() if curvature_min is None else min(curvature_min,bound.lower())
   curvature_cells+=1
far_curvature=3*P*(49*P/50).sin()/((P/2).cosh()-(49*P/50).cos())
assert far_curvature>ar('1/8')
left_tail_slope=(4*(3*P/20).sin()*(6*P/25).sin()).log()-3*(2*(2*P/25).sin()).log()-2*P/25
assert left_tail_slope>2

start=time.time();count=0;allout=[]
for eps,kinds in families:
 for parts in itertools.product(range(4),repeat=2):
  pending=[''.join(x)for x in itertools.product('01',repeat=4)];accepted=[];witnesses=[];mn=1;ma=100;ms=0
  while pending:
   ad=pending.pop();count+=1;ret,why=check(ad,eps,kinds,parts)
   if ret:
    accepted.append(ad);witnesses.append({'address':ad,'center':ret['center'],'affine_derivatives':ret['deriv'],'remainder_radius':ret['radius']});mn=min(mn,*[float(v.lower())for v in ret['gaps']]);ma=min(ma,*[float(v.lower())for v in ret['aliases']]);ms=max(ms,float(ret['shape'].upper()))
   elif len(ad)<24:pending.extend([ad+'0',ad+'1'])
   else:raise RuntimeError((eps,kinds,parts,ad,why))
   if count>args.max_visits:raise RuntimeError('explicit budget')
   if count%1000==0:print('progress',count,'currentaccepted',len(accepted),'pending',len(pending),round(time.time()-start,1),flush=True)
  row={'eps':eps,'kinds':kinds,'parts':parts,'accepted':len(accepted),'addresses':accepted,'witnesses':witnesses,'mingap':mn,'minalias':ma,'maxshape':ms};allout.append(row);print(json.dumps({k:v for k,v in row.items()if k not in ('addresses','witnesses')}),flush=True)
# Binary addresses encode alternating coordinate bisections of [0,1]^2.
for case in allout:
 codes=set(case['addresses'])
 assert len(codes)==len(case['addresses'])==len(case['witnesses'])
 assert codes=={w['address']for w in case['witnesses']}
 assert sum((R(1,2**len(v))for v in codes),R(0))==1
 prefixes={a[:j]for a in codes for j in range(len(a))}
 assert not(codes & prefixes)
 for p in prefixes:assert all(p+b in codes or p+b in prefixes for b in '01')
 for w in case['witnesses']:
  for x in w['center']:R(x)
  for row in w['affine_derivatives']:
   for x in row:R(x)
  assert R(w['remainder_radius'])>0
assert len(allout)==32
assert {(c['eps'],tuple(c['kinds']),tuple(c['parts']))for c in allout}=={
 (e,ks,ps)for e,ks in families for ps in itertools.product(range(4),repeat=2)}
assert initial_hashes=={p:sha(ROOT/p)for p in DEPENDENCIES}
assert proof_hash==sha(PROOF) and script_hash==sha(__file__)
out={
 'status':'passed',
 'scope':'Full canonical conditional sources on independent asymmetric products with own angle[.24,.46], including all original and upward-shifted critical heights; no remaining outer supporting-plane bound.',
 'precision_bits':args.precision,'visited_cells':count,
 'accepted_cells':sum(v['accepted']for v in allout),'boundary_pieces':32,
 'families':families,'parameter_rectangles':RECTS,
 'middle_rectangle':['2/25','49/100','-1/4','1/5'],
 'root_rectangle':['6/25','21/50','-21/100','3/20'],
 'root_existence_rectangle':['2/25','49/100','-11/50','3/20'],
 'root_pointing_faces':root_faces,'root_pointing_slabs':8*128,'root_pointing_threshold':'1/50',
 'curvature_cells':curvature_cells,'left_strip_curvature_lower':str(curvature_min),'right_strip_curvature_lower':str(far_curvature),'left_tail_slope_lower':str(left_tail_slope),'shifted_cotangent_monotonicity_margin':str(shifted_monotonicity),
 'real_endpoint_gap':'1/10000','horizontal_alias_gap':'1/1000',
 'right_tail_shape_threshold':'1','point_newton_radius':'1e-11',
 'cases':allout,'elapsed_seconds':time.time()-start,
 'proof_sha256':proof_hash,'script_sha256':script_hash,
 'dependencies':initial_hashes,
 'summary_float_scope':'Decimal summaries are diagnostic; acceptance uses strict outward Arb comparisons with exact rational thresholds.',
 'upstream_scope':'Global conditional root holomorphy is certified here; earlier contour reductions and actual geometric strip are explicit cited inputs, not rerun.',
}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(allout),'pieces,',out['accepted_cells'],'accepted,',count,'visited',flush=True)
