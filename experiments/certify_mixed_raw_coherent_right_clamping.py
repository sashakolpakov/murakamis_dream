#!/usr/bin/env python3
"""Outward original-phase derivative on independent right-clamp domains.

Three real parameters are covered; one harmonic neighbor boundary is reduced.
Saved trees retain the original coherent-root witness and monotone faces.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,math,tempfile,time
from concurrent.futures import ProcessPoolExecutor,as_completed
from fractions import Fraction as F
from pathlib import Path
import sympy as sy
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_raw_coherent_right_clamping.md'
HELPER=ROOT/'experiments/certify_mixed_minimum_level_half_stencils.py'
spec=importlib.util.spec_from_file_location('right_clamp_original_arithmetic',HELPER)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ar=m.ar
OMEGA={0:[('.1','0'),('.22','-.03'),('.45','-.03'),('.5','0'),('.45','.02'),('.22','.02')],
       1:[('.1','0'),('.22','-.057'),('.45','-.057'),('.5','0'),('.45','.014'),('.12','.014')]}
K={0:(F('-.03'),F('.02')),1:(F('-.057'),F(0))}
RECORDS=[
 ('mixed_complex_right_row_reduction','check'),
 ('mixed_right_boundary_row_bracket','check'),
 ('mixed_raw_row_stationarity','check'),
 ('mixed_closed_cotangent_roots','check'),
 ('mixed_early_selected_source_cap','certify'),
 ('mixed_left_right_interface_source','certify'),
 ('mixed_right_guard_conditional_packets','certify'),
 ('mixed_right_square_conditional_packets','certify','mixed_unselected_right_taper_products'),
 ('mixed_fourier_weight_continuation','check'),
 ('mixed_split_cutoff_hybrid_contour','check'),
]
HELPERS=['experiments/certify_mixed_minimum_level_half_stencils.py',
 'experiments/certify_mixed_isolated_transition_phase.py',
 'experiments/certify_mixed_real_small_support.py']

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def configure(bits):
 global pi,ii
 m.configure(bits);pi,ii=m.pi,m.ii

def specifications():
 return [list(v) for v in itertools.product((0,1),(0,1),(0,1),(0,1),range(6))]
def edge(ty,face,lo,hi):
 aa,bb=OMEGA[ty][face],OMEGA[ty][(face+1)%6]
 start=acb(ar(aa[0]),ar(aa[1]));vel=acb(ar(F(bb[0])-F(aa[0])),ar(F(bb[1])-F(aa[1])))
 return start+vel*ar(lo).union(ar(hi)),vel

def params(box,case):
 d,alpha,beta,other,face=case
 a,da=edge(other,face,*box[0]);t=ar('.45')+ar('.05')*ar(box[1][0]).union(ar(box[1][1]))
 kl,kh=K[alpha];dk=ar(kh-kl);k=ar(kl)+dk*ar(box[2][0]).union(ar(box[2][1]))
 R=400*(ar('.5')-t)**2;Rp=-800*(ar('.5')-t);q=1+ii*k*Rp;z=acb(t,k*R)
 dz=[acb(0),ar('.05')*q,ii*dk*R];da=[da,acb(0),acb(0)]
 dq=[acb(0),ii*40*k,ii*dk*Rp]
 return a,z,da,dz,q,dq

def gp(z):return m.m.core.gp(z)
def gpp(z):return m.gpp(z)
def T(u,z,eps,d):
 return (gp(u+ar('.5'))+gp(z+u)-(2+eps)*gp(u)+2*pi*ii*(d*z+ar(F(1-d,2)))).real

def raw_row(z,z0,eps,d):
 lo,hi=F(1,5),F(2,5)
 for _ in range(28):
  mid=(lo+hi)/2;v=T(acb(ar(mid)),z0,eps,d)
  if v>0:lo=mid
  elif v<0:hi=mid
  else:break
 u0=ar((lo+hi)/2)
 radius=(abs(T(acb(u0),z,eps,d))/(2*pi)).upper()
 return (u0+arb(0,radius)).intersection(ar(F(1,5)).union(ar(F(2,5))))

def raw_data(z,u,alpha,eps,d):
 K=gp(z+u)-(1+ar(F(alpha,2)))*gp(z)+2*pi*ii*d*u
 Kz=gpp(z+u)-(1+ar(F(alpha,2)))*gpp(z);Ku=gpp(z+u)+2*pi*ii*d
 Tu=(gpp(acb(u+ar('.5')))+gpp(z+u)-(2+eps)*gpp(acb(u))).real
 if not Tu.is_finite():return None
 Tu=Tu.intersection(Tu.lower().union((-2*pi).upper()))
 assert Tu<0
 return K,Kz,Ku,Tu

def test(box,case,witness=None):
 d,alpha,beta,other,face=case;a,z,da,dz,q,dq=params(box,case)
 mid=[((lo+hi)/2,(lo+hi)/2)for lo,hi in box];a0,z0,_,_,q0,_=params(mid,case)
 if d:left,right,l0,r0,eta,eps,ci,oi=a,z,a0,z0,other,alpha,1,0
 else:left,right,l0,r0,eta,eps,ci,oi=z,a,z0,a0,alpha,other,0,1
 if witness is not None:assert F(0)<F(witness['radius'])<=F(1,20)
 packet=m.root_box(left,right,l0,r0,eps,witness)
 if packet is None:return None,None,None
 s,s0,wit=packet;assert F(0)<F(wit['radius'])<=F(1,20)
 G,H=m.gradH(s,left,right,eta,eps);G0,H0=m.gradH(s0,l0,r0,eta,eps)
 epsraw=beta if d else alpha
 u=raw_row(z,z0,epsraw,d);u0=raw_row(z0,z0,epsraw,d)
 raw=raw_data(z,u,alpha,epsraw,d);raw0=raw_data(z0,u0,alpha,epsraw,d)
 if raw is None or raw0 is None:return None,None,None
 K,Kz,Ku,Tu=raw;K0=raw0[0];total=G[ci]+K;total0=G0[ci]+K0
 fv=(q*total).real;fc=(q0*total0).real;grads=[]
 for j in range(3):
  up=-(Ku*dz[j]).real/Tu
  dg=H[ci][oi]*da[j]+H[ci][ci]*dz[j]+Kz*dz[j]+Ku*up
  grads.append((q*dg+dq[j]*total).real)
 if not all(v.is_finite()for v in[fc,fv]+grads):return None,None,None
 mv=fc+sum((abs(g)*ar((hi-lo)/2)for g,(lo,hi)in zip(grads,box)),arb(0))
 upper=min(fv.upper(),mv.upper())
 return upper,grads,wit

def choose(box,case,grads):
 if grads is not None:return max(((abs(grads[j])*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]
 _,_,da,dz,_,_=params([((lo+hi)/2,(lo+hi)/2)for lo,hi in box],case)
 return max((((abs(da[j])+abs(dz[j]))*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]

def bindings():
 deps={p:sha(ROOT/p)for p in HELPERS};records=[]
 for item in RECORDS:
  stem,prefix=item[:2];proof=item[2]if len(item)>2 else stem
  rp=f'repro/results/research-{stem.replace("_","-")}.json';pp=f'notes/research_{proof}.md';ss=f'experiments/{prefix}_{stem}.py'
  rec=json.loads((ROOT/rp).read_text());assert rec['status']=='passed'
  inherited={**rec.get('dependencies',{}),**rec.get('dependencies_sha256',{})}
  assert rec.get('proof_sha256',inherited.get(pp))==sha(ROOT/pp)and rec['script_sha256']==sha(ROOT/ss)
  for field in('dependencies','dependencies_sha256'):
   for path,digest in rec.get(field,{}).items():assert sha(ROOT/path)==digest,path;deps[path]=digest
  for path in(rp,pp,ss):deps[path]=sha(ROOT/path)
  records.append(rp)
 return deps,records

def exact_checks():
 t,k,dt,dk=sy.symbols('t k dt dk',real=True);R=400*(sy.Rational(1,2)-t)**2;q=1+sy.I*k*sy.diff(R,t)
 checks={
  'raw row total differential':sy.diff(t+sy.I*k*R,t)-q,
  'quadratic baseline':R.subs(t,sy.Rational(9,20))-1,
  'quadratic endpoint':R.subs(t,sy.Rational(1,2)),
  'R second derivative':sy.diff(R,t,2)-800,
  'center differential':sy.diff(t+sy.I*k*R,t)*dt+sy.diff(t+sy.I*k*R,k)*dk-q*dt-sy.I*R*dk,
  'direction differential':sy.diff(q,t)*dt+sy.diff(q,k)*dk-sy.I*(sy.diff(R,t)*dk+800*k*dt),
 }
 for name,v in checks.items():assert sy.simplify(v)==0,name
 return list(checks)


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-raw-coherent-right-clamping.json')
 ap.add_argument('--max-visits',type=int,default=100000);ap.add_argument('--seconds',type=float,default=120)
 ap.add_argument('--first',type=int,default=0);ap.add_argument('--last',type=int,default=96)
 args=ap.parse_args();assert args.precision>=160 and 0<=args.first<args.last<=96
 started=time.monotonic();configure(args.precision);ph,sh=sha(PROOF),sha(__file__)
 deps,primary=bindings();exact=exact_checks();specs=specifications();assert len(specs)==96
 ih=sha(args.input)if args.input else None;saved=json.loads(args.input.read_text())if args.input else None
 if saved:
  assert saved['status']=='passed'and saved['products']==96
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
  assert len(saved['cases'])==96
 records=[];totalvisits=0;status='passed'
 for index in range(args.first,args.last):
  case=specs[index];old=saved['cases'][index]if saved else None
  if old:assert old['index']==index and old['case']==case
  stack=[[(F(0),F(1))for _ in range(3)]];nodes=[];cursor=leaves=visits=monotone=0;worst=None
  while stack:
   if saved is None and(totalvisits>=args.max_visits or time.monotonic()-started>=args.seconds):status='incomplete';break
   box=stack.pop();visits+=1;totalvisits+=1
   node=old['nodes'][cursor]if old else None;cursor+=bool(old)
   if node and node[0]=='S':
    _,axis=node;assert type(axis)is int and 0<=axis<3 and box[axis][0]<box[axis][1]
   else:
    assert node is None or node[0]in('L','M')
    upper,grads,wit=test(box,case,node[-1]if node else None)
    if node and node[0]=='M':
     _,axis,bit,_=node;assert type(axis)is int and 0<=axis<3 and bit in(0,1)
     assert box[axis][0]<box[axis][1]and grads is not None
     assert(grads[axis]>0 if bit else grads[axis]<0)
     point=box[axis][bit];reduced=list(box);reduced[axis]=(point,point)
     nodes.append(node);stack.append(reduced);monotone+=1;continue
    if upper is not None and upper<-ar(F(1,20)):
     assert node is None or node[0]=='L';nodes.append(['L',wit]);leaves+=1
     worst=upper if worst is None else max(worst,upper);continue
    assert old is None,('saved leaf failure',index,box,str(upper))
    signed=[]
    if grads is not None:
     for j,(lo,hi)in enumerate(box):
      if hi>lo and(grads[j]>0 or grads[j]<0):signed.append(((abs(grads[j])*ar(hi-lo)).upper(),j,int(grads[j]>0)))
    if signed:
     _,axis,bit=max(signed);nodes.append(['M',axis,bit,wit]);reduced=list(box)
     point=box[axis][bit];reduced[axis]=(point,point);stack.append(reduced);monotone+=1;continue
    assert any(lo<hi for lo,hi in box),('point did not pass',index,box,str(upper))
    axis=choose(box,case,grads)
   lo,hi=box[axis];assert lo<hi and(max(lo.denominator,hi.denominator).bit_length()<65)
   middle=(lo+hi)/2;nodes.append(['S',axis]);left=list(box);right=list(box)
   left[axis]=(lo,middle);right[axis]=(middle,hi);stack.extend((left,right))
  if old:
   assert not stack and cursor==len(old['nodes'])
   assert(leaves,visits,monotone)==(old['leaves'],old['visits'],old['monotone'])
  records.append(dict(index=index,case=case,leaves=leaves,visits=visits,monotone=monotone,nodes=nodes,
                      remaining_boxes=len(stack),maximum_derivative_upper=str(worst)))
  print('product',index+1,'leaves',leaves,'visits',visits,'M',monotone,'elapsed',round(time.monotonic()-started,2),'upper',worst,flush=True)
  if status=='incomplete':break
 if status=='passed'and(args.first,args.last)!=(0,96):status='passed_subset'
 assert ph==sha(PROOF)and sh==sha(__file__)
 assert all(sha(ROOT/path)==digest for path,digest in deps.items())
 if saved:assert ih==sha(args.input)
 result=dict(status=status,precision_bits=args.precision,products=len(records),product_range=[args.first,args.last],cases=records,
             leaves=sum(x['leaves']for x in records),visits=totalvisits,monotone_reductions=sum(x['monotone']for x in records),
             derivative_upper_bound='-1/20',complex_roots_per_cell=1,raw_scalar_roots_per_cell=1,
             exact_identities=exact,primary_records=primary,proof_sha256=ph,script_sha256=sh,
             dependencies_sha256=deps,input_sha256=ih,elapsed_seconds=time.monotonic()-started,
             scope='Unselected upper-taper center, one original coherent neighbor in its full polygon and one raw R at .5. Upper-rate clamping only; no selected-center, opposite-half, or full-period conclusion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(status.upper(),len(records),result['leaves'],result['visits'],flush=True)

if __name__=='__main__':main()
