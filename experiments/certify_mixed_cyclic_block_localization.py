#!/usr/bin/env python3
"""Universal two-leg blocks for all cyclic words in 3 and 4.

Only interval self-map inequalities decide acceptance. Double precision is
an untrusted proposer. Each accepted address is independently replayable.
No individual cyclic word is sampled or used as a premise.
"""
import argparse, hashlib
from pathlib import Path
import numpy as np, json, time, sys
from fractions import Fraction as Q
from flint import arb,acb,ctx
ctx.prec=128
I=acb(0,1);PI=arb.pi()
cs=[(Q(7,20),-Q(1,100)),(Q(3,10),-Q(13,250))];rs=[Q(9,100),Q(8,125)]
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def pt(z):return acb(ar(Q(str(z.real))),ar(Q(str(z.imag))))
def iv(x,y):return ar(x).union(ar(y))
def pars(lo,hi,ta,tb):
 return [acb(ar(cs[t][0])+ar(rs[t])*iv(lo[k],hi[k]),ar(cs[t][1])+ar(rs[t])*iv(lo[k+1],hi[k+1])) for k,t in [(0,ta),(2,tb)]]
def outside(lo,hi):
 for k in (0,2):
  ds=sum((min(abs(lo[j]),abs(hi[j]))**2 if lo[j]*hi[j]>0 else Q(0)) for j in (k,k+1))
  if ds>1:return True
 return False

def block(x,eps):
 a=x[0]+1j*x[1];b=x[2]+1j*x[3];A=np.exp(-2j*np.pi*a);B=np.exp(-2j*np.pi*b)
 d=2+eps
 z=np.array([.333333333+0j,.333333333+0j]) if not eps else np.array([.3075-.0552j]*2)
 for it in range(60):
  U,V=np.exp(-2j*np.pi*z)
  f=np.array([np.log(1-U*V)+np.log(1-U*A)-d*np.log(1-U)+2j*np.pi*a,
              np.log(1-U*V)+np.log(1-V*B)-d*np.log(1-V)+2j*np.pi*b])
  off=2j*np.pi*U*V/(1-U*V)
  J=np.array([[off+2j*np.pi*(U*A/(1-U*A)-d*U/(1-U)),off],
              [off,off+2j*np.pi*(V*B/(1-V*B)-d*V/(1-V))]])
  step=np.linalg.solve(J,f)
  if np.max(abs(step))>.1:step*=.1/np.max(abs(step))
  z-=step
  if np.max(abs(step))<1e-13:break
 U,V=np.exp(-2j*np.pi*z)
 E=np.diag([2j*np.pi/(1-U*A),2j*np.pi/(1-V*B)])
 deriv=-np.linalg.solve(J,E)
 return z,deriv,np.max(abs(f))


def evalf(z,a,b,d):
 u=(-2*PI*I*z[0]).exp();v=(-2*PI*I*z[1]).exp();A=(-2*PI*I*a).exp();B=(-2*PI*I*b).exp()
 ff=[(1-u*v).log()+(1-u*A).log()-d*(1-u).log()+2*PI*I*a,
     (1-u*v).log()+(1-v*B).log()-d*(1-v).log()+2*PI*I*b]
 off=2*PI*I*u*v/(1-u*v)
 jj=[[off+2*PI*I*(u*A/(1-u*A)-d*u/(1-u)),off],[off,off+2*PI*I*(v*B/(1-v*B)-d*v/(1-v))]]
 return ff,jj

def certify(lo,hi,eps,ta,tb):
 a,b=pars(lo,hi,ta,tb); pp=[a,b]
 mid=tuple((lo[k]+hi[k])/2 for k in range(4));a0,b0=pars(mid,mid,ta,tb);p0=[a0,b0]
 af=complex(float(a0.real.mid()),float(a0.imag.mid()));bf=complex(float(b0.real.mid()),float(b0.imag.mid()))
 z,D,err=block([af.real,af.imag,bf.real,bf.imag],eps)
 if err>1e-9:return False
 zz=[pt(v)for v in z];dd=2+eps
 f0,j0=evalf(zz,a0,b0,dd)
 jf=np.array([[complex(float(v.real.mid()),float(v.imag.mid()))for v in row]for row in j0])
 yy=[[pt(v)for v in row]for row in np.linalg.inv(jf)]
 if not abs(yy[0][0]*yy[1][1]-yy[0][1]*yy[1][0])>0:return False
 der=[[pt(v)for v in row]for row in D]
 dp=[pp[i]-p0[i]for i in range(2)]
 dz=[sum((der[i][j]*dp[j]for j in range(2)),acb(0))for i in range(2)]
 e0=[2*PI*I/(1-(-2*PI*I*(zz[i]+p0[i])).exp())for i in range(2)]
 lin=[f0[i]+sum(((sum((j0[i][k]*der[k][j]for k in range(2)),acb(0))+ (e0[i] if i==j else 0))*dp[j]for j in range(2)),acb(0))for i in range(2)]
 # Integral Taylor remainder for every g-log; enlarged rectangular hull of all segments.
 def rem(base,delta):
  box=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not (box.real>0 and box.real<1):return arb.pos_inf()
  q=(-2*PI*I*box).exp();bound=(2*PI)**2*abs(q/(1-q)**2)*abs(delta)**2/2
  return bound
 shared=rem(zz[0]+zz[1],dz[0]+dz[1])
 rr=[shared+rem(zz[i]+p0[i],dz[i]+dp[i])+dd*rem(zz[i],dz[i])for i in range(2)]
 bb=[abs(sum((yy[i][k]*lin[k]for k in range(2)),acb(0)))+sum((abs(yy[i][k])*rr[k]for k in range(2)),arb(0))for i in range(2)]
 if any(not v.is_finite()for v in bb):return False
 for fac in [1.25,1.5,2]:
  rad=[Q(max(1,int(np.ceil(float(v.upper())*fac*2**40))),2**40)for v in bb]
  ctr=acb(ar(cs[eps][0]),ar(cs[eps][1]))
  if not all(abs(zz[i]+dz[i]-ctr)+ar(rad[i])<ar(rs[eps])for i in range(2)):continue
  def qdiff(base,delta):
   q0=(-2*PI*I*base).exp();dq=q0*((-2*PI*I*delta).exp()-1)
   return dq/((1-q0-dq)*(1-q0))
  ddz=[dz[i]+acb(arb(0,ar(rad[i])),arb(0,ar(rad[i])))for i in range(2)]
  allz=[zz[i]+ddz[i]for i in range(2)]+pp
  if not all(v.real>ar(Q(23,100)) and v.real<ar(Q(9,20)) and abs(v.imag)<ar(Q(3,25)) for v in allz):continue
  dc=qdiff(zz[0]+zz[1],ddz[0]+ddz[1])
  ds=[qdiff(zz[i]+p0[i],ddz[i]+dp[i])-dd*qdiff(zz[i],ddz[i])for i in range(2)]
  ee=[[acb(int(i==j))-sum((yy[i][k]*j0[k][j]for k in range(2)),acb(0))-2*PI*I*((yy[i][0]+yy[i][1])*dc+yy[i][j]*ds[j])for j in range(2)]for i in range(2)]
  if all(bb[i]+sum((abs(ee[i][j])*ar(rad[j])for j in range(2)),arb(0))<ar(rad[i])for i in range(2)):
   return True
 return False



def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def scalar_checks():
 checks={
  "cosh":(6*PI/25).cosh()<ar(Q(4,3)),
  "sin_short":(PI/25).sin()<ar(Q(1,7)),
  "tan_short":(PI/25).tan()<ar(Q(1,7)),
  "sin_long":(PI/10).sin()>ar(Q(3,10)),
  "cos_short":(PI/25).cos()>ar(Q(4,5)),
  "small_pair":ar(Q(24,55)-Q(2,7))>ar(Q(1,8)),
  "single":ar(Q(9,70))>ar(Q(1,8)),
 }
 for t in (0,1):
  cr,ci=cs[t];r=rs[t]
  checks[f"disk_{t}_left"]=cr-r>Q(23,100)
  checks[f"disk_{t}_right"]=cr+r<Q(9,20)
  checks[f"disk_{t}_height"]=abs(ci)+r<Q(3,25)
 assert all(checks.values()),checks
 return checks

def run_case(eps,ta,tb,limit):
 stack=[('',(Q(-1),)*4,(Q(1),)*4)];accepted=[];excluded=[];vis=0;mx=0;volume=Q(0);t0=time.time()
 while stack:
  if vis>=limit:raise RuntimeError(f"budget exhausted in {(eps,ta,tb)}")
  adr,lo,hi=stack.pop();vis+=1;mx=max(mx,len(adr))
  if outside(lo,hi):excluded.append(adr);volume+=Q(16,2**len(adr));continue
  try:ok=certify(lo,hi,eps,ta,tb)
  except (ValueError,ZeroDivisionError,OverflowError):ok=False
  if ok:accepted.append(adr);volume+=Q(16,2**len(adr))
  else:
   k=len(adr)%4;mi=(lo[k]+hi[k])/2;loh=list(lo);hih=list(hi);loh[k]=mi;hih[k]=mi
   stack.extend([(adr+'1',tuple(loh),hi),(adr+'0',lo,tuple(hih))])
  if vis%50000==0:print(f"case{eps}{ta}{tb}: visited={vis} accepted={len(accepted)} covered={float(volume/16):.6f}",flush=True)
 assert volume==16
 out={"types":[eps,ta,tb],"accepted":accepted,"excluded":excluded,"visited":vis,"max_depth":mx,"elapsed_seconds":time.time()-t0}
 print(f"PASS case{eps}{ta}{tb}: {len(accepted)} accepted, {len(excluded)} excluded, {vis} visited",flush=True)
 return out

def main():
 global PI
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160);ap.add_argument('--max-boxes',type=int,default=2000000);ap.add_argument('--output',default='repro/results/research-mixed-cyclic-block-localization.json');ap.add_argument('--case',nargs=3,type=int)
 args=ap.parse_args();ctx.prec=args.precision;PI=arb.pi()
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 cases=[tuple(args.case)] if args.case else [(e,a,b)for e in (0,1)for a,b in [(0,0),(0,1),(1,1)]]
 out={"schema":"mixed-cyclic-block-localization-v1","precision":ctx.prec,"status":"running","scalar_checks":scalar_checks(),"cases":[]}
 for case in cases:
  out['cases'].append(run_case(*case,args.max_boxes));Path(str(dest)+'.partial').write_text(json.dumps(out,separators=(',',':'))+'\n')
 out['status']='passed';out['script_sha256']=sha(__file__)
 proof=Path('notes/research_mixed_cyclic_critical_localization.md')
 out['proof_sha256']=sha(proof) if proof.exists() else None
 out['dependencies']={p:sha(p)for p in ['notes/research_mixed_contracted_phase.md']}
 dest.write_text(json.dumps(out,separators=(',',':'))+'\n');Path(str(dest)+'.partial').unlink(missing_ok=True)
 print(f"PASS {len(cases)} universal block domains, {len(out['scalar_checks'])} scalar inequalities",flush=True)
if __name__=='__main__':main()
