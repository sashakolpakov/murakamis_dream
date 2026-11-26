#!/usr/bin/env python3
"""Independent positive-frequency source replay for the undeleted V3 packet.

Uses the original sine primitive and sine-log derivatives, the principal
acos angular lift, and exact binary cover reconstruction. No author imports.
"""
import argparse,json,time
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import sympy as sp
from flint import arb,acb,ctx
from replay_three_cap_wire_complement import partition
ROOT=Path(__file__).resolve().parents[1];ii=acb(0,1)
LOWER,UPPER=Q(1,4),Q(9,20);BOT,TOP=Q(-3,100),Q(3,200)
def h(p):return sha256(p.read_bytes()).hexdigest()
def a(v):
 q=Q(v);return arb(q.numerator)/q.denominator

def original_J(z):
 p=arb.pi()
 return -ii*p*(z*z-z)/2+ii*(2*p*ii*z).exp().polylog(2)/(2*p)-ii*p/12

def value(s,t,K):
 p=arb.pi();z=s+t
 den=((K*(-2*p*ii*s).exp()).polylog(2)+(K*(-2*p*ii*t).exp()).polylog(2)-2*K.polylog(2))/(2*p*ii)
 return original_J(z)+ii*p*(z-z*z)/2+z*K.log()-den

def gradients(s,t,K):
 p=arb.pi();z=s+t
 common=(2*(p*z).sin()).log()+ii*p*(1-2*z)/2+K.log()
 return common-(1-K*(-2*p*ii*s).exp()).log(),common-(1-K*(-2*p*ii*t).exp()).log()

def sides(k,v):
 if k in (0,1):
  return acb(a((LOWER,UPPER)[k]),a(BOT)+a(TOP-BOT)*v),ii*a(TOP-BOT)
 assert k in (2,3)
 return acb(a(LOWER)+a(UPPER-LOWER)*v,a((BOT,TOP)[k-2])),acb(a(UPPER-LOWER))

def source_record(path,script):
 rec=json.loads(path.read_text());assert rec['status']=='passed'
 assert rec['script_sha256']==h(ROOT/'experiments'/script)
 for dep,digest in rec.get('dependencies_sha256',{}).items():assert h(ROOT/dep)==digest,dep
 return rec

def reference():
 path=ROOT/'repro/results/research-three-four-source-interface.json'
 rec=source_record(path,'check_three_four_source_interface.py')
 rr=rec['root_certificate'];center=acb(*map(a,rr['center']));radius=a(rr['complex_disk_radius'])
 z=acb(arb(center.real,radius),arb(center.imag,radius))
 coeff=(1,-2,4,-6,4)
 poly=lambda v:sum(coeff[j]*v**j for j in range(5))
 deriv=lambda v:sum(j*coeff[j]*v**(j-1)for j in range(1,5))
 raw=1/deriv(center);pre=acb(raw.real.mid(),raw.imag.mid());defect=abs(1-pre*deriv(z));shift=abs(pre*poly(center))
 root_margins={'fresh quartic contraction':1-defect,'fresh quartic self-map':radius-shift-defect*radius}
 assert all(v>0 for v in root_margins.values()),root_margins
 # Use the geometric cosine rather than the author's rational K formula.
 B=z*z*(2*z-1)**2/(2*(z-1));k=z*z*B/(z*z+B);c=1-2*k
 K=c+ii*(1-c*c).sqrt();U=1-2*z;p=arb.pi();x=K.log()/(2*p*ii);s=-U.log()/(2*p*ii)
 return K,U,x,s,path,root_margins

def exact_identities():
 z=sp.symbols('z');U=1-2*z;K=1/(1+U-U**2)
 B=z*z*(2*z-1)**2/(2*(z-1));k=z*z*B/(z*z+B)
 checks={'geometric selected exponential polynomial':K**2-(2-4*k)*K+1,
         'stationary logarithm exponential':K*(1-U**2)-(1-K*U)}
 for name,v in checks.items():assert sp.cancel(v)==0,name
 return list(checks)

def scalars(K,U,x,s,root_margins):
 p=arb.pi();out=dict(root_margins)
 def pos(name,v):assert v>0,(name,v);out[name]=v
 pos('K first quadrant real',K.real);pos('K first quadrant imaginary',K.imag);pos('K unit disk',1-abs(K))
 pos('wire upper quarter',arb(1)/4-x.real);pos('wire positive',x.real)
 pos('argument lower',K.arg()-p/5);pos('argument upper',2*p/5-K.arg())
 pos('denominator uniform disk',arb(7)/10-abs(K)*(2*p*a(TOP)).exp())
 pos('critical index left',s.real-a(LOWER));pos('critical index right',a(UPPER)-s.real)
 pos('critical index bottom',s.imag-a(BOT));pos('critical index top',a(TOP)-s.imag)
 grad=gradients(s,s,K)[0];assert grad.contains(0)
 pos('unexponentiated gradient lift',p-abs(grad.imag))
 pos('original full action', (value(s,s,K)-2*p*ii*x).real-arb(3281)/5000)
 d0=2*p*a(LOWER)-K.arg();d1=2*p*a(UPPER)-K.arg()
 pos('angle lower',d0);pos('angle upper',p-d1);pos('minimum sine at left endpoint',d1.sin()-d0.sin())
 rmin=abs(K)*(2*p*a(BOT)).exp();rmax=abs(K)*(2*p*a(TOP)).exp()
 pos('whole rectangle coercivity',2*p*rmin*d0.sin()/(1+rmax)**2-arb(2)/5)
 pos('upper nonconstant penalty reserve',2*p*a(TOP)-arb(1)/50-arb(7)/100)
 return out

def calibration(paths,U1):
 p=arb.pi();U0=acb(-arb(1)/2,-arb(3).sqrt()/2);checked=accepted=0
 for ((initial_lo,initial_hi),) in partition(paths,1):
  todo=[(initial_lo,initial_hi)]
  while todo:
   lo,hi=todo.pop();v=a(lo).union(a(hi));U=U0+(U1-U0)*v
   X=1/(1+U-U*U);x=X.log()/(2*p*ii);s=-U.log()/(2*p*ii);W=(U*U-2*U-1)/2
   tau=W.acos();plus=arb(1)/2-x+tau/(2*p);minus=arb(1)/2-x-tau/(2*p)
   margins=[-U.real,-U.imag,X.real,X.imag,1-abs(X),1-abs(X*U),x.real,arb(1)/4-x.real,x.imag,W.imag,
            s.real,arb(1)/2-s.real,plus.real,1-plus.real,minus.real,1-minus.real,abs(1-2*U),tau.real,p-tau.real,-tau.imag]
   checked+=len(margins)
   if all(q>0 for q in margins):accepted+=1;continue
   assert hi-lo>Q(1,2**20),(lo,hi,margins)
   mid=(lo+hi)/2;todo.extend([(lo,mid),(mid,hi)])
 return checked,accepted

def check(j,k,box,K,fc):
 spans=[a(lo).union(a(hi))for lo,hi in box];centers=[a((lo+hi)/2)for lo,hi in box];radii=[a((hi-lo)/2)for lo,hi in box]
 s,ds=sides(j,spans[0]);t,dt=sides(k,spans[1]);fs,ft=gradients(s,t,K)
 sm,_=sides(j,centers[0]);tm,_=sides(k,centers[1])
 bound=value(sm,tm,K).real+radii[0]*abs((fs*ds).real)+radii[1]*abs((ft*dt).real)
 target=arb(1)/1000 if j<2 or k<2 else -arb(1)/50
 return fc-bound>target

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=320);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-vertex-mixed-reference-replay.json');args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
 path=ROOT/'repro/results/research-three-vertex-mixed-reference.json'
 data=source_record(path,'certify_three_vertex_mixed_reference.py')
 assert data['index_rectangle']=={'real':['1/4','9/20'],'imaginary':['-3/100','3/200']}
 K,U,x,s,ref,margins=reference();assert data['reference']['sha256']==h(ref)
 exact=exact_identities();margins=scalars(K,U,x,s,margins);fc=value(s,s,K).real
 assert data['calibration_path']['leaf_count']==len(data['calibration_path']['leaves'])
 calibration_count,calibration_leaves=calibration(data['calibration_path']['leaves'],U)
 real_path=ROOT/'repro/results/research-three-vertex-alternating-complement.json';real=source_record(real_path,'certify_three_vertex_alternating_complement.py')
 assert data['real_complement_input']['sha256']==h(real_path)
 real_replay=ROOT/'repro/results/research-three-vertex-alternating-complement-replay.json';rr=source_record(real_replay,'replay_three_vertex_alternating_complement.py');assert rr['artifact_sha256']==h(real_path)
 seen=set();original=accepted=visits=0
 for row in data['domains']:
  j,k=row['s_side'],row['t_side'];assert 0<=j<4 and 0<=k<4 and (j,k) not in seen;seen.add((j,k))
  for box in partition(row['leaves'],2):
   original+=1;todo=[box]
   while todo:
    current=todo.pop();visits+=1
    if check(j,k,current,K,fc):accepted+=1;continue
    axis=max(range(2),key=lambda n:current[n][1]-current[n][0]);lo,hi=current[axis];assert hi-lo>Q(1,2**26),(j,k,current);mid=(lo+hi)/2
    for ends in ((lo,mid),(mid,hi)):
     child=list(current);child[axis]=ends;todo.append(tuple(child))
    assert visits<100000
 assert seen=={(j,k)for j in range(4)for k in range(4)}and original==data['leaf_count']
 deps=['experiments/replay_three_cap_wire_complement.py','notes/research_three_vertex_mixed_reference_packet.md',str(ref.relative_to(ROOT)),str(real_path.relative_to(ROOT)),str(real_replay.relative_to(ROOT))]
 result={'status':'passed','precision_bits':args.precision,'domain_count':16,'exact_binary_cover':True,'original_leaf_count':original,'replayed_leaf_count':accepted,'visited':visits,
  'strict_scalar_comparisons':len(margins),'scalar_margins':{name:str(v)for name,v in margins.items()},'exact_identities':exact,'exact_identity_count':len(exact),
  'calibration_path_cells':len(data['calibration_path']['leaves']),'replayed_calibration_cells':calibration_leaves,'calibration_strict_inclusions':calibration_count,'critical_action':str(value(s,s,K)-2*arb.pi()*ii*x),
  'method':'Positive-frequency original J and sine-log gradient; geometric-cosine wire, fresh quartic Newton, principal-acos calibration path; no author imports.',
  'elapsed_seconds':time.monotonic()-start,'artifact_sha256':h(path),'script_sha256':h(Path(__file__)),'dependencies_sha256':{dep:h(ROOT/dep)for dep in deps}}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS',16,'domains',original,accepted,'leaves',len(margins),'scalar margins',len(exact),'exact identities and',result['calibration_path_cells'],'path cells')
if __name__=='__main__':main()
