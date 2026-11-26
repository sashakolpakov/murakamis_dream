#!/usr/bin/env python3
"""Outward original selected-block support bound on the entire plateau.

Every true Fourier branch is retained. Floating optimizers propose rational
support points only; acceptance uses exact logarithmic Newton self-maps,
outward mean-value estimates, strong concavity and complete dyadic covers.
"""
import argparse,hashlib,json,time,math,itertools
from pathlib import Path
from fractions import Fraction as R
import numpy as np
from scipy.special import spence
from scipy.optimize import minimize
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_selected_plateau_support.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=250000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-selected-plateau-support.json')
args=parser.parse_args();assert args.precision>=128
DEPS=['notes/research_mixed_transition_conditional_rectangles.md','experiments/certify_mixed_transition_conditional_rectangles.py','repro/results/research-mixed-transition-conditional-rectangles.json','notes/research_mixed_fourier_weight_continuation.md','notes/research_mixed_type_three_window_strip.md','notes/research_mixed_type_four_height_refinement.md','notes/research_mixed_plateau_accretivity.md','notes/research_mixed_right_half_block_bound.md','notes/research_mixed_outer_graph_contours.md','notes/research_mixed_conditional_torus_composition.md']
initial={x:sha(ROOT/x)for x in DEPS};proof_hash=sha(PROOF);script_hash=sha(__file__)
up=json.loads((ROOT/DEPS[2]).read_text());assert up['status']=='passed'
assert up['proof_sha256']==initial[DEPS[0]]and up['script_sha256']==initial[DEPS[1]]
for q,h in up['dependencies'].items():assert sha(ROOT/q)==h
ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
def ar(x):x=R(x);return arb(x.numerator)/x.denominator
def pt(z):return acb(ar(str(z.real)),ar(str(z.imag)))
def cot(z):return (P*z).cot()
def gp(z):return (1-(-2*P*I*z).exp()).log()
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def phase(s,a,b,d):return g(s+a)+g(s+b)-d*g(s)+2*P*I*a*s
def fp(s,a,b,d):return gp(s+a)+gp(s+b)-d*gp(s)+2*P*I*a
def hs(s,a,b,d):return P*(cot(s+a)+cot(s+b)-d*cot(s))+(d-2)*P*I
def rootbox(a,b,a0,b0,eps):
 d=2+eps
 af=complex(float(a0.real),float(a0.imag));bf=complex(float(b0.real),float(b0.imag));A=np.exp(-2j*np.pi*af);B=np.exp(-2j*np.pi*bf)
 co=[A*(B-1),A-B,1-A]if eps==0 else[A,A*(B-3),2*A-B,1-A]
 zs=[1j*np.log(v)/(2*np.pi)for v in np.roots(co)]
 roots=[z for z in zs if .15<z.real<.49 and abs(z.imag)<.17 and abs(np.log(1-np.exp(-2j*np.pi*(z+af)))+np.log(1-np.exp(-2j*np.pi*(z+bf)))-d*np.log(1-np.exp(-2j*np.pi*z))+2j*np.pi*af)<1e-7]
 if len(roots)!=1:raise ValueError('rootproposal')
 z0=pt(roots[0]);H0=hs(z0,a0,b0,d);Y=1/H0;f0=fp(z0,a0,b0,d);E0=[P*cot(z0+a0)+P*I,P*cot(z0+b0)-P*I]
 deriv_proposals=[complex(float((-Y*v).real.mid()),float((-Y*v).imag.mid()))for v in E0];deriv=[pt(v)for v in deriv_proposals];dp=[a-a0,b-b0];dz=sum((deriv[j]*dp[j]for j in(0,1)),acb(0))
 lin=f0+sum(((H0*deriv[j]+E0[j])*dp[j]for j in(0,1)),acb(0))
 def rem(base,delta):
  v=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(0<v.real<1):return arb.pos_inf()
  return P*P*abs(1/(P*v).sin()**2)*abs(delta)**2/2
 er=abs(Y)*(abs(lin)+rem(z0+a0,dz+dp[0])+rem(z0+b0,dz+dp[1])+d*rem(z0,dz))
 if not er.is_finite():raise ValueError('infinite')
 rad=R(max(1,math.ceil(float(er.upper())*1.5*2**40)),2**40)
 if rad>R(1,20):raise ValueError('large radius')
 delta=dz+acb(arb(0,ar(rad)),arb(0,ar(rad)));z=z0+delta
 if not(ar('1/5')<z.real<ar('23/50') and abs(z.imag)<ar('17/100')):raise ValueError('root rectangle')
 def dc(base,delta):return -P*(P*delta).sin()/((P*base).sin()*(P*(base+delta)).sin())
 ee=1-Y*H0-Y*(dc(z0+a0,delta+dp[0])+dc(z0+b0,delta+dp[1])-d*dc(z0,delta))
 if not er+abs(ee)*ar(rad)<ar(rad):raise ValueError('selfmap')
 rr=ar('1e-11');zp=z0+acb(arb(0,rr),arb(0,rr));ep=1-Y*hs(zp,a0,b0,d)
 if not abs(Y*f0)+abs(ep)*rr<rr:raise ValueError('point')
 return {'s':z,'sp':zp,'center':[str(roots[0].real),str(roots[0].imag)],'deriv':[[str(v.real),str(v.imag)]for v in deriv_proposals],'radius':str(rad)}
def values(s,a,b,eta,eps):
 v=phase(s,a,b,2+eps)-(1+ar(eta)/2)*g(a)-(1+ar(eps)/2)*g(b)
 ga=gp(s+a)+2*P*I*s-(1+ar(eta)/2)*gp(a)
 gb=gp(s+b)-(1+ar(eps)/2)*gp(b)
 return v,[ga,gb]
def Hess(s,a,b,eta,eps):
 q=hs(s,a,b,2+eps);va=P*cot(s+a)+P*I;vb=P*cot(s+b)-P*I
 aa=P*cot(s+a)-(1+ar(eta)/2)*P*cot(a)+ar(eta)*P*I/2
 bb=P*cot(s+b)-(1+ar(eps)/2)*P*cot(b)+ar(eps)*P*I/2
 return [[-aa+va*va/q,va*vb/q],[va*vb/q,-bb+vb*vb/q]]
FP=np.pi
def fg(z):return(spence(1-np.exp(-2j*FP*z))-FP*FP/6)/(2j*FP)
def fgp(z):return np.log(1-np.exp(-2j*FP*z))
def fv(a,b,eta,eps):
 A=np.exp(-2j*FP*a);B=np.exp(-2j*FP*b)
 co=[A*(B-1),A-B,1-A]if not eps else[A,A*(B-3),2*A-B,1-A]
 zz=[1j*np.log(u)/(2*FP)for u in np.roots(co)]
 ss=[s for s in zz if .1<s.real<.49 and abs(s.imag)<.18 and abs(fgp(s+a)+fgp(s+b)-(2+eps)*fgp(s)+2j*FP*a)<1e-7]
 if len(ss)!=1:raise ValueError('float root')
 s=ss[0];v=fg(s+a)+fg(s+b)-(2+eps)*fg(s)+2j*FP*a*s-(1+eta/2)*fg(a)-(1+eps/2)*fg(b)
 gg=np.array([fgp(s+a)+2j*FP*s-(1+eta/2)*fgp(a),fgp(s+b)-(1+eps/2)*fgp(b)])
 return v,gg
RECT={0:[R('.30'),R('.39'),R('-.03'),R('.02')],1:[R('.27'),R('.33'),R('-.057'),R('-.02')]}
def decode(ad,dim):
 out=[R(0),R(1)]*dim
 for j,c in enumerate(ad):
  k=2*(j%dim);md=(out[k]+out[k+1])/2;out[k+1-int(c)]=md
 return out
def params(types,selected,parts,box):
 pp=[];p0=[];rv=[];tv=[];pos=0
 for j,(ty,sel,part)in enumerate(zip(types,selected,parts)):
  a,b,c,d=RECT[ty]
  if sel:
   corners=[acb(ar(a),ar(c)),acb(ar(b),ar(c)),acb(ar(b),ar(d)),acb(ar(a),ar(d))]
   vel=corners[(part+1)%4]-corners[part];lo,hi=box[2*pos:2*pos+2]
   pp.append(corners[part]+vel*ar(lo).union(ar(hi)));p0.append(corners[part]+vel*ar((lo+hi)/2))
   rr=[acb(0),acb(0)];rr[j]=vel;rv.append(rr);tv.append([acb(0),acb(0)]);pos+=1
  else:
   lo,hi=box[2*pos:2*pos+2];lo2,hi2=box[2*pos+2:2*pos+4]
   pp.append(acb(ar(a+(b-a)*lo).union(ar(a+(b-a)*hi)),ar(c+(d-c)*lo2).union(ar(c+(d-c)*hi2))))
   p0.append(acb(ar(a+(b-a)*(lo+hi)/2),ar(c+(d-c)*(lo2+hi2)/2)))
   rr=[acb(0),acb(0)];rr[j]=acb(ar(b-a));rv.append(rr);tv.append([acb(0),acb(0)])
   rr=[acb(0),acb(0)];rr[j]=I*ar(d-c);rv.append(rr);tv.append(rr.copy());pos+=2
 return pp,p0,rv,tv

def check(ad,case,flags,parts):
 eta,eps,sa,sb=case;fa,fb=flags;dim=4-sa-sb;box=decode(ad,dim)
 pp,p0,rv,tv=params((eta,eps),(sa,sb),parts,box);a,b=pp;a0,b0=p0
 rr=rootbox(a,b,a0,b0,eps)
 rf=[complex(float(v.real),float(v.imag))for v in p0];rv0,rg0=fv(*rf,eta,eps)
 heights=[.014 if sel else rf[j].imag for j,sel in enumerate((sa,sb))]
 def objective(x):
  zz=np.array([x[j]+1j*heights[j]for j in range(2)]);val,gg=fv(*zz,eta,eps)
  val+=.5*(fa*fg(zz[0])+fb*fg(zz[1]));gg+=.5*np.array([fa*fgp(zz[0]),fb*fgp(zz[1])])
  val-=rv0+rg0@(zz-np.array(rf))+np.pi*.014*(sa-fa+sb-fb)
  return -val.real,-(gg-rg0).real
 opt=minimize(objective,np.clip([v.real for v in rf],.22,.45),jac=True,bounds=[(.22,.45)]*2,method='L-BFGS-B',options={'ftol':1e-14,'gtol':1e-10,'maxiter':50})
 cc=[R(str(float(v)))for v in opt.x]
 if not all(R('11/50')<=v<=R('9/20')for v in cc):raise ValueError('target center')
 target=[acb(ar(cc[j]),ar('7/500')if sel else pp[j].imag)for j,sel in enumerate((sa,sb))]
 target0=[acb(ar(cc[j]),ar('7/500')if sel else p0[j].imag)for j,sel in enumerate((sa,sb))]
 tr=rootbox(*target,*target0,eps)
 vr0,gr0=values(rr['sp'],a0,b0,eta,eps);vt0,gt0=values(tr['sp'],*target0,eta,eps)
 fc=(vt0+(ar(fa)*g(target0[0])+ar(fb)*g(target0[1]))/2-vr0-sum((gr0[j]*(target0[j]-p0[j])for j in range(2)),acb(0))).real-P*ar('7/500')*(sa-fa+sb-fb)
 _,gr=values(rr['s'],a,b,eta,eps);_,gt=values(tr['s'],*target,eta,eps)
 gt=[gt[j]+ar((fa,fb)[j])*gp(target[j])/2 for j in range(2)];gg=[gt[j]-gr[j]for j in range(2)]
 HH=Hess(rr['s'],a,b,eta,eps);delta=[target[j]-pp[j]for j in range(2)]
 cost=arb(0)
 for k in range(dim):
  der=sum((gg[j]*tv[k][j]for j in range(2)),acb(0))+sum((HH[j][l]*delta[j]*rv[k][l]for j in range(2)for l in range(2)),acb(0))
  cost+=abs(der.real)*ar((box[2*k+1]-box[2*k])/2)
 upper=fc+cost+sum((abs(v.real)**2 for v in gg),arb(0))/3
 if not upper < -ar('1/100'):raise ValueError(('gap',str(upper)))
 return {'address':ad,'target_center':list(map(str,cc)),'reference_root':{k:v for k,v in rr.items()if k not in('s','sp')},'target_root':{k:v for k,v in tr.items()if k not in('s','sp')},'upper':str(upper)}
CASES=[(0,1,0,1),(1,0,1,0),(1,1,1,0),(1,1,0,1),(1,1,1,1)]
def target_params(case,parts,box):
 eta,eps,sa,sb=case;pp=[];p0=[]
 for j,(ty,sel,part)in enumerate(zip((eta,eps),(sa,sb),parts)):
  lo,hi=box[2*j:2*j+2]
  if sel:
   cc=acb(ar('11/50'),ar('7/500'));vel=acb(ar('23/100'))
  else:
   h0,h1=RECT[ty][2:];corners=[acb(ar('11/50'),ar(h0)),acb(ar('9/20'),ar(h0)),acb(ar('9/20'),ar(h1)),acb(ar('11/50'),ar(h1))]
   cc=corners[part];vel=corners[(part+1)%4]-cc
  pp.append(cc+vel*ar(lo).union(ar(hi)));p0.append(cc+vel*ar((lo+hi)/2))
 return pp,p0

def check_target(ad,case,flags,parts):
 eta,eps,sa,sb=case;fa,fb=flags;pp,p0=target_params(case,parts,decode(ad,2));rr=rootbox(*pp,*p0,eps)
 HH=Hess(rr['s'],*pp,eta,eps)
 HH[0][0]-=ar(fa)*(P*cot(pp[0])-P*I)/2;HH[1][1]-=ar(fb)*(P*cot(pp[1])-P*I)/2
 aa=HH[0][0].real-ar('3/2');bb=HH[0][1].real;cc=HH[1][1].real-ar('3/2');det=aa*cc-bb*bb
 if not(aa>0 and cc>0 and det>0):raise ValueError(('target matrix',str(aa),str(cc),str(det)))
 return {'address':ad,'root':{k:v for k,v in rr.items()if k not in('s','sp')}}
def cover(checker,case,flags,parts,dim,counter):
 pending=[''.join(v)for v in itertools.product('01',repeat=2*dim)];acc=[]
 while pending:
  ad=pending.pop();counter[0]+=1
  try:row=checker(ad,case,flags,parts)
  except ValueError as exc:
   if len(ad)>=27:raise RuntimeError((case,flags,parts,ad,exc))
   pending.extend((ad+'0',ad+'1'))
  else:acc.append(row)
  if counter[0]%2000==0:print('progress',counter[0],'accepted',len(acc),'pending',len(pending),round(time.time()-start,1),flush=True)
  if counter[0]>args.max_visits:raise RuntimeError('explicit budget')
 codes={w['address']for w in acc};assert len(codes)==len(acc)
 assert sum((R(1,2**len(v))for v in codes),R(0))==1
 prefixes={v[:j]for v in codes for j in range(len(v))};assert not(codes & prefixes)
 for p in prefixes:assert all(p+b in codes or p+b in prefixes for b in'01')
 return acc
start=time.time();counter=[0];targets=[];references=[]
for case in CASES:
 sa,sb=case[2:]
 for flags in itertools.product(range(sa+1),range(sb+1)):
  for parts in itertools.product((0,)if sa else range(4),(0,)if sb else range(4)):
   acc=cover(check_target,case,flags,parts,2,counter)
   targets.append({'case':case,'flags':flags,'parts':parts,'cells':acc})
   print('target',case,flags,parts,'passed',len(acc),flush=True)
for case in CASES:
 sa,sb=case[2:];dim=4-sa-sb
 for flags in itertools.product(range(sa+1),range(sb+1)):
  for parts in itertools.product(range(4)if sa else(None,),range(4)if sb else(None,)):
   acc=cover(check,case,flags,parts,dim,counter)
   references.append({'case':case,'flags':flags,'parts':parts,'cells':acc})
   print('reference',case,flags,parts,'passed',len(acc),flush=True)
assert len(targets)==36 and len(references)==96
assert {(tuple(c['case']),tuple(c['flags']),tuple(c['parts']))for c in targets}=={(case,flags,parts)for case in CASES for flags in itertools.product(range(case[2]+1),range(case[3]+1))for parts in itertools.product((0,)if case[2]else range(4),(0,)if case[3]else range(4))}
assert {(tuple(c['case']),tuple(c['flags']),tuple(c['parts']))for c in references}=={(case,flags,parts)for case in CASES for flags in itertools.product(range(case[2]+1),range(case[3]+1))for parts in itertools.product(range(4)if case[2]else(None,),range(4)if case[3]else(None,))}
assert initial=={q:sha(ROOT/q)for q in DEPS}
assert proof_hash==sha(PROOF)and script_hash==sha(__file__)
out={'status':'passed','scope':'Original full conditional kernel on plateau targets with at least one selected type-four coordinate; all12 true Fourier forcing/frequency branches; local geometric support gap1/200 after tolerance.','precision_bits':args.precision,'selected_height':'7/500','target_real_interval':['11/50','9/20'],'reference_rectangles':{str(k):list(map(str,v))for k,v in RECT.items()},'target_concavity':'3/2','reference_defect_upper':'-1/100','finite_block_gap':'1/200','target_products':36,'reference_products':96,'target_accepted_cells':sum(len(c['cells'])for c in targets),'reference_accepted_cells':sum(len(c['cells'])for c in references),'visited_cells':counter[0],'target_cases':targets,'reference_cases':references,'elapsed_seconds':time.time()-start,'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies':initial,'optimizer_scope':'Floating roots and optimizers are proposals only; every rational support point is accepted by outward original-source inequalities.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['target_accepted_cells'],'target cells',out['reference_accepted_cells'],'reference cells',counter[0],'visits',flush=True)
