"""Bounded floating diagnostic; no source or supporting-plane certificate."""
from pathlib import Path
import argparse,itertools,json,time,hashlib
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.special import spence
from scipy.optimize import differential_evolution
ROOT=Path('/Users/sasha/volume-conjecture');P=np.pi;H=.014
R={0:(.30,.39,-.03,.02),1:(.27,.33,-.057,-.02)}
CIM_PATH=ROOT/'repro/results/research-mixed-neighbor-conditioned-critical-boxes.json'
CIM=json.loads(CIM_PATH.read_text())['limits_in_thousandths']
BITS=np.array(list(itertools.product((0,1),repeat=2)))
Q=np.array([7.55,5.5])
OBJECTIVES=['bare','left_outside_debit','right_outside_debit','both_outside_debits']
def g(z):return (spence(1-np.exp(-2j*P*z))-P*P/6)/(2j*P)
def phase(a,b,eta,eps):
 a,b=np.broadcast_arrays(np.asarray(a,dtype=complex),np.asarray(b,dtype=complex))
 p,q=1/np.tan(P*a),1/np.tan(P*b)
 if not eps:
  c=p+q;d=-1+1j*(q-p);disc=np.sqrt(c*c-4*d)
  roots=np.stack(((-c+disc)/2,(-c-disc)/2),axis=-1)
 else:
  comp=np.zeros(a.shape+(3,3),dtype=complex)
  comp[...,0,0]=-(p+q+1j);comp[...,0,1]=-(p*q+1j*(p+q));comp[...,0,2]=-(1j*p*q-2j*(p-1j)*(q+1j))
  comp[...,1,0]=1;comp[...,2,1]=1;roots=np.linalg.eigvals(comp)
 selected=(roots.real>0)&(abs(roots.imag)<1)
 assert np.all(selected.sum(axis=-1)==1),(a,b,roots)
 cot=np.take_along_axis(roots,selected.argmax(axis=-1)[...,None],axis=-1)[...,0]
 s=np.log((cot+1j)/(cot-1j))/(2j*P)
 gp=lambda z:np.log(1-np.exp(-2j*P*z))
 value=g(s+a)+g(s+b)-(2+eps)*g(s)+2j*P*a*s-(1+eta/2)*g(a)-(1+eps/2)*g(b)
 grad=np.stack((gp(s+a)+2j*P*s-(1+eta/2)*gp(a),gp(s+b)-(1+eps/2)*gp(b)),axis=-1)
 return value,grad

def box(triple):
 own=triple[1];base=R[own];lim=CIM[''.join(map(str,triple))]
 out=[max(base[0],lim[0][0]/1000),min(base[1],lim[0][1]/1000),max(base[2],lim[1][0]/1000),min(base[3],lim[1][1]/1000)]
 if triple[1:]==(1,1):out[3]=min(out[3],-.048)
 if triple==(1,1,1):out[3]=min(out[3],-.053)
 assert out[0]<out[1] and out[2]<out[3]
 return out

def vertices(b):return [complex(x,y)for x,y in itertools.product(b[:2],b[2:])]
def specifications():
 jobs=[]
 for word in itertools.product((0,1),repeat=4):
  types=word[1:3];boxes=[box(word[:3]),box(word[1:])]
  for sigma in itertools.product(*[range(t+1)for t in types]):
   for side in (0,1):
    for ia,ib in itertools.product(range(4),repeat=2):
     jobs.append(dict(id=len(jobs),word=word,types=types,selected=sigma,left_side=side,ref_corners=(ia,ib),reference_boxes=boxes))
 return jobs

def run(job):
 refs=np.array([vertices(b)[corner] for b,corner in zip(job['reference_boxes'],job['ref_corners'])]);types=tuple(job['types']);sigma=np.array(job['selected']);side=job['left_side']
 value,grad=phase(*refs,*types)
 def defects(v):
  v=np.asarray(v);v=v.reshape(-1,2);x,t=v[:,0],v[:,1]
  rt=400*(.5-t)**2;slow=(x-.1)/.12;fast=np.minimum(1,(x-.1)/.02)
  re=np.stack((x,t) if side==0 else(t,x),axis=-1)
  rho=np.stack([(fast if sigma[j] else slow)*(1 if j==side else rt)for j in(0,1)],axis=-1)
  fracs=rho[:,None,:]*BITS[None,:,:];height=fracs*np.where(sigma,H,refs.imag)
  w=re[:,None,:]+1j*height
  vals=phase(w[...,0],w[...,1],*types)[0].real
  vals+=.5*np.sum(sigma*np.maximum(g(w).real,-2*P*height),axis=-1)
  bare=vals-(value+np.sum(grad*(w-refs),axis=-1)).real
  fee=np.where(sigma,Q*(1-fracs)*refs.imag**2-.01*fracs,Q*(1-fracs)**2*refs.imag**2)
  allvals=np.stack((bare,bare+fee[...,0],bare+fee[...,1],bare+fee.sum(axis=-1)),axis=-1)
  return allvals.max(axis=1),allvals.argmax(axis=1)
 grid=np.array(list(itertools.product(np.unique(np.r_[np.linspace(.1,.22,13),.12]),np.linspace(.45,.5,9))))
 candidates=[grid]
 for k in range(4):
  opt=differential_evolution(lambda x:-defects(np.asarray(x).T)[0][:,k],[(.1,.22),(.45,.5)],seed=3100+4*job['id']+k,maxiter=16,popsize=5,tol=1e-7,polish=False,vectorized=True,updating='deferred')
  candidates.append(np.asarray(opt.x).reshape(1,2))
 candidates=np.concatenate(candidates);values,which=defects(candidates)
 results={}
 for k,name in enumerate(OBJECTIVES):
  j=int(values[:,k].argmax());results[name]=dict(maximum=float(values[j,k]),target_left_right=candidates[j].tolist(),height_endpoints=BITS[which[j,k]].tolist())
 return dict(**job,reference=[[float(z.real),float(z.imag)]for z in refs],maxima=results)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=2);ap.add_argument('--output',type=Path,default=Path('/tmp/mixed-hybrid-conditioned-interface-phase-diagnostic.json'));ap.add_argument('--limit',type=int);args=ap.parse_args()
 jobs=specifications();assert len(jobs)==1152
 if args.limit:jobs=jobs[:args.limit]
 start=time.time();rows=[]
 with ProcessPoolExecutor(max_workers=args.workers)as pool:
  for row in pool.map(run,jobs,chunksize=1):
   rows.append(row)
   if len(rows)%32==0:print('COMPLETED',len(rows),'/',len(jobs),'seconds',round(time.time()-start,1),flush=True)
 summary={name:max(rows,key=lambda r:r['maxima'][name]['maximum']) for name in OBJECTIVES}
 result=dict(scope='Floating bounded diagnostic on proved neighbor-conditioned reference BOX CORNERS only. Target search uses a fixed mesh plus four bounded optimizations. No reference-boundary or continuum certificate.',geometry_input=str(CIM_PATH),geometry_sha256=hashlib.sha256(CIM_PATH.read_bytes()).hexdigest(),coefficient_refinements=['own-next4 upper-.048','previous-own-next444 upper-.053'],case_count=len(rows),cases=rows,summary=summary,elapsed_seconds=time.time()-start)
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 for name,row in summary.items():print('MAX',name,json.dumps(row),flush=True)
 print('DONE',len(rows),time.time()-start,flush=True)
if __name__=='__main__':main()
