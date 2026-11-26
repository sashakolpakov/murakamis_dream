#!/usr/bin/env python3
"""Certify wavefront clamping of full plateau aliases, with all Fourier branches."""
from pathlib import Path
import argparse,itertools,json,math,time,hashlib
from fractions import Fraction as Q
import numpy as np
from flint import arb,acb,ctx
ctx.prec=192;P=arb.pi();I=acb(0,1)
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_plateau_alias_clamping.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
ar=lambda v:arb(Q(v).numerator)/Q(v).denominator
gp=lambda z:(1-(-2*P*I*z).exp()).log()
gpp=lambda z:P*(P*z).cot()-P*I
def qroot(e,a,b):
 af=complex(float(a.real.mid()),float(a.imag.mid()));bf=complex(float(b.real.mid()),float(b.imag.mid()))
 A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
 co=[A*(B-1),A-B,1-A]if e==0 else[A,A*(B-3),2*A-B,1-A]
 out=[]
 for U in np.roots(co):
  s=1j*np.log(U)/(2*np.pi)
  f=lambda z:np.log(1-np.exp(-2j*np.pi*z))
  if .19<s.real<.47 and abs(s.imag)<.18 and abs(f(s+af)+f(s+bf)-(2+e)*f(s)+2j*np.pi*af)<1e-6:out.append(s)
 assert len(out)==1,(e,af,bf,out)
 z=out[0];center=[str(z.real),str(z.imag)];return acb(ar(center[0]),ar(center[1])),center
def enclose(e,a,b,a0,b0):
 d=2+e;z0,center=qroot(e,a0,b0);h0=gpp(z0+a0)+gpp(z0+b0)-d*gpp(z0);Y=1/h0
 f0=gp(z0+a0)+gp(z0+b0)-d*gp(z0)+2*P*I*a0
 ext=[gpp(z0+a0)+2*P*I,gpp(z0+b0)]
 D=[];derivatives=[]
 for extj in ext:
  z=-Y*extj;pair=[str(float(z.real.mid())),str(float(z.imag.mid()))]
  derivatives.append(pair);D.append(acb(ar(pair[0]),ar(pair[1])))
 dp=[a-a0,b-b0];dz=sum((D[j]*dp[j]for j in(0,1)),acb(0))
 linear=f0+sum(((h0*D[j]+ext[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,delta):
  z=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not 0<z.real<1:return arb.pos_inf()
  return P**2*abs(1/(P*z).sin()**2)*abs(delta)**2/2
 err=abs(Y)*(abs(linear)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+d*rem(z0,dz))
 if not err.is_finite():return None
 rad=Q(max(1,math.ceil(float(err.upper())*1.75*2**44)),2**44)
 if rad>Q(1,25):return None
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not ar('.2')<z.real<ar('.46')or not abs(z.imag)<ar('.17'):return None
 def diff(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 errjac=1-Y*h0-Y*(diff(z0+a0,delta+dp[0])+diff(z0+b0,delta+dp[1])-d*diff(z0,delta))
 if not err+abs(errjac)*ar(rad)<ar(rad):return None
 return z,{'center':center,'affine_derivatives':derivatives,'remainder_radius':str(rad)}
def decode(ad,n):
 lo=[Q(0)]*n;hi=[Q(1)]*n
 for j,bit in enumerate(ad):
  k=j%n;mid=(lo[k]+hi[k])/2
  if bit=='0':hi[k]=mid
  else:lo[k]=mid
 return lo,hi
def cover(ads):
 aa=sorted(ads);assert len(set(aa))==len(aa)
 assert all(not b.startswith(a)for a,b in zip(aa,aa[1:]))
 assert sum((Q(1,2**len(a))for a in aa),Q(0))==1
HEIGHT={0:[Q('-.03'),Q('.02')],1:[Q('-.057'),Q('.014')]}
def expand(spec,ad,mid=False):
 active=[j for j,(x,y) in enumerate(spec['box']) if x<y]
 low,high=decode(ad,len(active));lo=[Q(0)]*3;hi=[Q(1)]*3
 for j,l,h in zip(active,low,high):lo[j]=l;hi[j]=h
 vals=[]
 for (x,y),l,h in zip(spec['box'],lo,hi):
  vals.append(ar(x+(y-x)*(l+h)/2)if mid else ar(x+(y-x)*l).union(ar(x+(y-x)*h)))
 rho,ownh,nh=vals;et,en=spec['type'],spec['neighbor']
 nr=rho if spec['mode']=='lower'or en==0 and spec['mode']=='upper3'else ar('.4')if spec['mode']=='upper3'else ar('.45')
 target=acb(rho,ownh);neighbor=acb(nr,nh)
 return (neighbor,target)if spec['side']==0 else(target,neighbor)
def value(spec,ad):
 a,b=expand(spec,ad);a0,b0=expand(spec,ad,True)
 et,en=spec['type'],spec['neighbor'];e=et if spec['side']==0 else en
 root=enclose(e,a,b,a0,b0)
 if root is None:return None
 s,witness=root
 result=(gp(s+b)-(1+et)*gp(b)).real if spec['side']==0 else(gp(s+a)+2*P*I*s-gp(a)).real
 return result,witness
TABLE=[
 ['6483/50000','1061/10000'],
 ['-30471/100000','28503/100000'],
 ['-4487/50000','11809/100000'],
 ['-577/5000','14717/100000'],
 ['-1437/10000','869/5000'],
 ['-17473/100000','19797/100000'],
 ['-1547/2500','551/3125'],
 ['-90013/100000','9431/50000'],
 ['-5653/50000','10277/100000'],
 ['-12151/100000','5371/50000'],
 ['-6517/50000','11177/100000'],
 ['-2791/20000','579/5000'],
 ['-2983/20000','747/6250'],
 ['-7957/50000','6147/50000'],
 ['-16953/100000','12607/100000'],
 ['-1127/6250','1289/10000']]
def specs():
 out=[];groups=[]
 configurations=[('lower',0,HEIGHT[0],0),('lower',1,[Q('.014')]*2,1)]
 configurations +=[('lower',1,[Q('-.057')+Q('.037')*j/4,Q('-.057')+Q('.037')*(j+1)/4],2+j)for j in range(4)]
 configurations +=[('upper4',1,[Q('-.057'),Q('-.02')],0),('upper4',1,[Q('.014')]*2,1)]
 configurations +=[('upper3',0,[Q('-.03')+Q('.05')*j/8,Q('-.03')+Q('.05')*(j+1)/8],j)for j in range(8)]
 assert len(configurations)==len(TABLE)==16
 for i,(mode,et,hh,group)in enumerate(configurations):
  rho=[Q('.22'),Q('.25')]if mode=='lower'else[Q('.4'),Q('.45')]if mode=='upper3'else[Q('.4')]*2
  idx=[]
  for side,en in itertools.product((0,1),repeat=2):
   spec={'mode':mode,'type':et,'neighbor':en,'side':side,'group':group,'box':[rho,hh,HEIGHT[en]],'bound':Q(TABLE[i][side])}
   idx.append(len(out));out.append(spec)
  groups.append({'mode':mode,'type':et,'group':group,'indices':idx})
 return out,groups

DEPS=[
 'notes/research_mixed_transition_conditional_rectangles.md',
 'experiments/certify_mixed_transition_conditional_rectangles.py',
 'repro/results/research-mixed-transition-conditional-rectangles.json',
 'notes/research_mixed_plateau_accretivity.md',
 'experiments/check_mixed_plateau_accretivity.py',
 'repro/results/research-mixed-plateau-accretivity.json',
 'notes/research_mixed_central_alias_gap.md',
 'experiments/certify_mixed_central_alias_gap.py',
 'repro/results/research-mixed-central-alias-gap.json',
 'notes/research_mixed_type_four_height_refinement.md',
 'experiments/certify_mixed_type_four_height_refinement.py',
 'experiments/replay_mixed_type_four_height_refinement.py',
 'repro/results/research-mixed-type-four-height-refinement.json',
 'repro/results/research-mixed-type-four-height-refinement-replay.json',
 'notes/research_mixed_fourier_weight_continuation.md',
 'notes/research_mixed_conditional_torus_composition.md']
def bindings():
 data={p:sha(ROOT/p)for p in DEPS}
 for stem,script,proof in[
  ('research-mixed-transition-conditional-rectangles','certify_mixed_transition_conditional_rectangles.py','research_mixed_transition_conditional_rectangles.md'),
  ('research-mixed-plateau-accretivity','check_mixed_plateau_accretivity.py','research_mixed_plateau_accretivity.md'),
  ('research-mixed-central-alias-gap','certify_mixed_central_alias_gap.py','research_mixed_central_alias_gap.md'),
  ('research-mixed-type-four-height-refinement','certify_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md'),
  ('research-mixed-type-four-height-refinement-replay','replay_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md')]:
  r=json.loads((ROOT/f'repro/results/{stem}.json').read_text())
  assert r['status']=='passed'and r['script_sha256']==sha(ROOT/'experiments'/script)
  assert r['proof_sha256']==sha(ROOT/'notes'/proof)
  for f,h in r.get('dependencies',r.get('dependencies_sha256')).items():assert sha(ROOT/f)==h,f
 return data

def main():
 global P
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--precision',type=int,default=256)
 parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-plateau-alias-clamping.json')
 args=parser.parse_args();assert args.precision>=192;ctx.prec=args.precision;P=arb.pi()
 initial=bindings();proof_hash=sha(PROOF);script_hash=sha(__file__);start=time.time()
 source=json.loads((ROOT/'repro/results/research-mixed-transition-conditional-rectangles.json').read_text())
 assert source['boundary_pieces']==64
 rects={k:list(map(Q,v))for k,v in source['parameter_rectangles'].items()}
 assert rects=={'3':list(map(Q,['.22','.45','-.03','.02'])),'4':list(map(Q,['.22','.45','-.057','.0141']))}
 expected={(e,kinds,parts)for e,kinds in[(0,('3','3')),(0,('4','3')),(1,('3','4')),(1,('4','4'))]for parts in itertools.product(range(4),repeat=2)}
 assert len(source['cases'])==64 and {(c['eps'],tuple(c['kinds']),tuple(c['parts']))for c in source['cases']}==expected
 cross_cases=[];cross_cells=0;cross_visits=0
 for case in source['cases']:
  cover(case['addresses']);yes=[];witnesses=[];todo=list(case['addresses']);e=case['eps']
  def pars(ad,mid):
   lo,hi=decode(ad,2);zz=[]
   for j,(kind,part)in enumerate(zip(case['kinds'],case['parts'])):
    xl,xh,yl,yh=rects[kind];cc=[acb(ar(xl),ar(yl)),acb(ar(xh),ar(yl)),acb(ar(xh),ar(yh)),acb(ar(xl),ar(yh))]
    t=ar((lo[j]+hi[j])/2)if mid else ar(lo[j]).union(ar(hi[j]));zz.append(cc[part]+(cc[(part+1)%4]-cc[part])*t)
   return zz
  while todo:
   ad=todo.pop();cross_visits+=1;a,b=pars(ad,False);a0,b0=pars(ad,True);root=enclose(e,a,b,a0,b0)
   ok=False
   if root is not None:
    s,witness=root
    p,q=gpp(s+a),gpp(s+b);d=p+q-(2+e)*gpp(s)
    ok=(-(p+2*P*I)*q/d).real>ar('1/100')
   if ok:yes.append(ad);witnesses.append({'address':ad,**witness})
   else:
    assert len(ad)<26,(case['kinds'],case['parts'],ad)
    todo.extend([ad+'0',ad+'1'])
   assert cross_visits<100000
  cover(yes);cross_cells+=len(yes)
  cross_cases.append({'eps':e,'kinds':case['kinds'],'parts':case['parts'],'addresses':yes,'witnesses':witnesses})
  print('cross',case['kinds'],case['parts'],len(yes),flush=True)
 ss,groups=specs();faces=[];face_visits=0
 for j,spec in enumerate(ss):
  todo=[''];yes=[];witnesses=[]
  while todo:
   ad=todo.pop();face_visits+=1
   try:
    answer=value(spec,ad);ok=False
    if answer is not None:
     v,witness=answer;ok=v>ar(spec['bound'])if spec['mode']=='lower'else v<ar(spec['bound'])
   except(ValueError,ZeroDivisionError):ok=False
   if ok:yes.append(ad);witnesses.append({'address':ad,**witness})
   else:
    assert len(ad)<40,(j,spec,ad)
    todo.extend([ad+'1',ad+'0'])
   assert face_visits<200000
  cover(yes);faces.append({**spec,'addresses':yes,'witnesses':witnesses,'active_parameters':[j for j,(x,y)in enumerate(spec['box'])if x<y]})
  print('face',j,spec['mode'],spec['group'],spec['side'],spec['neighbor'],spec['bound'],len(yes),flush=True)
 for case in cross_cases+faces:
  assert len(case['addresses'])==len(case['witnesses'])
  assert set(case['addresses'])=={w['address'] for w in case['witnesses']}
  for w in case['witnesses']:
   assert Q(w['remainder_radius'])>0
   for z in w['center']:Q(z)
   for pair in w['affine_derivatives']:
    for z in pair:Q(z)
 scalars=[]
 for group in groups:
  bound=[]
  for side in(0,1):
   values=[ss[j]['bound']for j in group['indices']if ss[j]['side']==side]
   assert len(values)==2 and values[0]==values[1]
   bound.append(values[0])
  total=sum(bound);group['bound']=total
  if group['mode']=='lower':
   if group['type']==1 and group['group']==1:
    assert total>Q(-1,50)
   else:assert total>0
  elif group['mode']=='upper4'and group['group']==1:
   forcing=gp(acb(ar('2/5'),ar('7/500'))).real
   assert ar(total)+forcing<0
   scalars.append({'name':'selected-four upper face including forcing','margin':str(-ar(total)-forcing)})
  else:assert total<0
  print('group',group['mode'],group['type'],group['group'],str(total),flush=True)
 assert 2*(ar('11/25')*P).cos()<1
 scalars.append({'name':'positive lower-face forcing derivative','margin':str(1-2*(ar('11/25')*P).cos())})
 assert Q(721,10000)-Q(25,2)*Q(71,1000)**2==Q(727,80000)
 assert Q(727,80000)-Q(3,5000)-Q(1,1000)-Q(1,150)==Q(197,240000)
 assert initial==bindings()and proof_hash==sha(PROOF)and script_hash==sha(__file__)
 result={'status':'passed','precision_bits':args.precision,'cross_products':64,'cross_cells':cross_cells,'cross_visits':cross_visits,
         'face_domains':len(faces),'face_cells':sum(len(c['addresses'])for c in faces),'face_visits':face_visits,
         'cross_lower':'1/100','lower_selected_gradient':'-1/50','clamping_loss_per_alias':'3/5000','final_gap_per_alias':'1/150',
         'cross_cases':cross_cases,'face_cases':faces,'gradient_groups':groups,
         'strict_scalar_comparisons':scalars,'exact_rational_group_checks':16,'exact_budget_identities':2,
         'dependencies':initial,'proof_sha256':proof_hash,'script_sha256':script_hash,'elapsed_seconds':time.time()-start,
         'scope':'Every nonempty original alias on the entire constant-height plateau [.22,.45]^m. Curved tapers/full mixed-word source remain separate.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,default=str,indent=2)+'\n')
 print('PASS',cross_cells,result['face_cells'],'cells;',cross_visits,face_visits,'visits',flush=True)
if __name__=='__main__':main()
