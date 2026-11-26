#!/usr/bin/env python3
"""Independent sine/cotangent replay of the universal block covers.

The generator is not imported. Exact rational binary coverage and every
excluded disk rectangle are checked. Newton proposals use the sine lift;
only outward interval self-maps are accepted.
"""
import argparse, hashlib, json, time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from flint import arb,acb,ctx
I=acb(0,1)
CENTERS=[(Q(7,20),-Q(1,100)),(Q(3,10),-Q(13,250))]
RADII=[Q(9,100),Q(8,125)]
PI=arb.pi()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def pt(z):return acb(ar(Q(str(z.real))),ar(Q(str(z.imag))))
def interval(a,b):return ar(a).union(ar(b))
def params(lo,hi,types):
 return [acb(ar(CENTERS[t][0])+ar(RADII[t])*interval(lo[2*i],hi[2*i]),ar(CENTERS[t][1])+ar(RADII[t])*interval(lo[2*i+1],hi[2*i+1]))for i,t in enumerate(types)]
def excluded(lo,hi):
 return any(sum((min(abs(lo[k]),abs(hi[k]))**2 if lo[k]*hi[k]>0 else Q(0))for k in (j,j+1))>1 for j in (0,2))
def decode(address):
 lo=[Q(-1)]*4;hi=[Q(1)]*4
 for j,bit in enumerate(address):
  assert bit in '01';k=j%4;mid=(lo[k]+hi[k])/2
  if bit=='0':hi[k]=mid
  else:lo[k]=mid
 return tuple(lo),tuple(hi)
def verify_cover(yes,no):
 leaves=sorted(yes+no);assert len(leaves)==len(set(leaves))
 # A finite prefix-free binary code of Kraft mass one covers every branch.
 for a,b in zip(leaves,leaves[1:]):assert not b.startswith(a)
 assert sum((Q(1,2**len(a))for a in leaves),Q(0))==1
 for a in no:assert excluded(*decode(a))

def propose(a,b,eps):
 z=np.array([complex(*map(float,CENTERS[eps]))]*2)
 d=2+eps
 def cot(x):return 1/np.tan(np.pi*x)
 for _ in range(80):
  s,t=z
  f=np.array([np.log(2*np.sin(np.pi*(s+t)))+np.log(2*np.sin(np.pi*(s+a)))-d*np.log(2*np.sin(np.pi*s))+1j*np.pi*(a-t+eps*(s-.5)),np.log(2*np.sin(np.pi*(s+t)))+np.log(2*np.sin(np.pi*(t+b)))-d*np.log(2*np.sin(np.pi*t))+1j*np.pi*(b-s+eps*(t-.5))])
  off=np.pi*cot(s+t)-1j*np.pi
  J=np.array([[np.pi*(cot(s+t)+cot(s+a)-d*cot(s))+1j*np.pi*eps,off],[off,np.pi*(cot(s+t)+cot(t+b)-d*cot(t))+1j*np.pi*eps]])
  step=np.linalg.solve(J,f)
  if max(abs(step))>.08:step*=.08/max(abs(step))
  z-=step
  if max(abs(step))<1e-14:break
 # These are proposals, so using the last Jacobian does not need an error claim.
 Y=np.linalg.inv(J);E=np.diag([np.pi*cot(z[0]+a)+1j*np.pi,np.pi*cot(z[1]+b)+1j*np.pi])
 return z,Y,-Y@E

def fg(z,p,eps):
 s,t=z;a,b=p;d=2+eps
 def logsin(x):return (2*(PI*x).sin()).log()
 def cot(x):return (PI*x).cos()/(PI*x).sin()
 f=[logsin(s+t)+logsin(s+a)-d*logsin(s)+I*PI*(a-t+eps*(s-ar(Q(1,2)))),logsin(s+t)+logsin(t+b)-d*logsin(t)+I*PI*(b-s+eps*(t-ar(Q(1,2))))]
 off=PI*cot(s+t)-I*PI
 J=[[PI*(cot(s+t)+cot(s+a)-d*cot(s))+I*PI*eps,off],[off,PI*(cot(s+t)+cot(t+b)-d*cot(t))+I*PI*eps]]
 E=[PI*cot(s+a)+I*PI,PI*cot(t+b)+I*PI]
 return f,J,E

def verify_cell(lo,hi,eps,ta,tb):
 pp=params(lo,hi,[ta,tb]);mid=tuple((a+b)/2 for a,b in zip(lo,hi));p0=params(mid,mid,[ta,tb])
 pf=[complex(float(v.real.mid()),float(v.imag.mid()))for v in p0]
 z,Y,D=propose(*pf,eps);zz=[pt(v)for v in z];yy=[[pt(v)for v in row]for row in Y];dd=[[pt(v)for v in row]for row in D]
 assert abs(yy[0][0]*yy[1][1]-yy[0][1]*yy[1][0])>0
 f0,J0,E0=fg(zz,p0,eps);d=2+eps;dp=[pp[i]-p0[i]for i in range(2)]
 dz=[sum((dd[i][j]*dp[j]for j in range(2)),acb(0))for i in range(2)]
 lin=[f0[i]+sum(((sum((J0[i][k]*dd[k][j]for k in range(2)),acb(0))+(E0[i]if i==j else 0))*dp[j]for j in range(2)),acb(0))for i in range(2)]
 def rem(base,delta):
  box=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not(box.real>0 and box.real<1):return arb.pos_inf()
  return PI**2*abs(1/(PI*box).sin()**2)*abs(delta)**2/2
 shared=rem(zz[0]+zz[1],dz[0]+dz[1])
 rema=[shared+rem(zz[i]+p0[i],dz[i]+dp[i])+d*rem(zz[i],dz[i])for i in range(2)]
 bb=[abs(sum((yy[i][j]*lin[j]for j in range(2)),acb(0)))+sum((abs(yy[i][j])*rema[j]for j in range(2)),arb(0))for i in range(2)]
 if any(not b.is_finite()for b in bb):return False
 for factor in [1.25,1.5,2,1.375,1.75]:
  rad=[Q(max(1,int(np.ceil(float(b.upper())*factor*2**40))),2**40)for b in bb]
  ctr=acb(ar(CENTERS[eps][0]),ar(CENTERS[eps][1]))
  if not all(abs(zz[i]+dz[i]-ctr)+ar(rad[i])<ar(RADII[eps])for i in range(2)):continue
  hz=[dz[i]+acb(arb(0,ar(rad[i])),arb(0,ar(rad[i])))for i in range(2)]
  if not all(v.real>ar(Q(23,100)) and v.real<ar(Q(9,20)) and abs(v.imag)<ar(Q(3,25))for v in [zz[i]+hz[i]for i in range(2)]+pp):continue
  def cdiff(base,delta):return -(PI*delta).sin()/((PI*(base+delta)).sin()*(PI*base).sin())
  cross=cdiff(zz[0]+zz[1],hz[0]+hz[1])
  diag=[cdiff(zz[i]+p0[i],hz[i]+dp[i])-d*cdiff(zz[i],hz[i])for i in range(2)]
  ee=[[acb(int(i==j))-sum((yy[i][k]*J0[k][j]for k in range(2)),acb(0))-PI*((yy[i][0]+yy[i][1])*cross+yy[i][j]*diag[j])for j in range(2)]for i in range(2)]
  if all(bb[i]+sum((abs(ee[i][j])*ar(rad[j])for j in range(2)),arb(0))<ar(rad[i])for i in range(2)):return True
 return False

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 global PI
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--input',default='repro/results/research-mixed-cyclic-block-localization.json');ap.add_argument('--output',default='repro/results/research-mixed-cyclic-block-localization-replay.json');ap.add_argument('--allow-partial-cases',action='store_true')
 args=ap.parse_args();ctx.prec=args.precision;PI=arb.pi()
 scalar=[(6*PI/25).cosh()<ar(Q(4,3)),(PI/25).sin()<ar(Q(1,7)),(PI/25).tan()<ar(Q(1,7)),(PI/10).sin()>ar(Q(3,10)),(PI/25).cos()>ar(Q(4,5)),Q(24,55)-Q(2,7)>Q(1,8),Q(9,70)>Q(1,8)]
 for (cr,ci),r in zip(CENTERS,RADII):scalar.extend([cr-r>Q(23,100),cr+r<Q(9,20),abs(ci)+r<Q(3,25)])
 assert len(scalar)==13 and all(scalar)
 record=json.loads(Path(args.input).read_text());assert record['status']=='passed'
 assert record['script_sha256']==sha('experiments/certify_mixed_cyclic_block_localization.py')
 if record['proof_sha256'] is not None:assert record['proof_sha256']==sha('notes/research_mixed_cyclic_critical_localization.md')
 for p,h in record['dependencies'].items():assert sha(p)==h
 cases=record['cases'];expected={(e,a,b)for e in (0,1)for a,b in [(0,0),(0,1),(1,1)]}
 if not args.allow_partial_cases:assert {tuple(c['types'])for c in cases}==expected
 total=refined=0;results=[]
 for c in cases:
  e,a,b=c['types'];verify_cover(c['accepted'],c['excluded']);start=time.time();count=0;extra=0
  for address in c['accepted']:
   work=[address]
   while work:
    adr=work.pop();lo,hi=decode(adr)
    if excluded(lo,hi):continue
    if verify_cell(lo,hi,e,a,b):count+=1;continue
    assert len(adr)<len(address)+12,(c['types'],adr)
    work.extend([adr+'0',adr+'1']);extra+=1
  print(f'PASS {e}{a}{b}: original={len(c["accepted"])} replay={count} refinements={extra} seconds={time.time()-start:.2f}',flush=True)
  total+=count;refined+=extra;results.append({'types':c['types'],'original_boxes':len(c['accepted']),'replay_boxes':count,'refinements':extra})
 out={'status':'passed','precision':ctx.prec,'cases':results,'replay_boxes':total,'refinements':refined,'scalar_comparisons':len(scalar),'input_sha256':sha(args.input),'script_sha256':sha(__file__),'proof_sha256':sha('notes/research_mixed_cyclic_critical_localization.md')}
 Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
