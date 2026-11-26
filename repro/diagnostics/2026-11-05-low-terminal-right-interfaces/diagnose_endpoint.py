"""Bounded actual-reference low-terminal interface pilot, not a certificate."""
from pathlib import Path
import importlib.util,itertools,json,time,hashlib
import numpy as np
from scipy.optimize import root,differential_evolution,minimize

HERE=Path(__file__).resolve().parent
HELPER=HERE.parent/'2026-11-05-right-short-connectors/phase_helpers.py'
sp=importlib.util.spec_from_file_location('phase_helpers',HELPER)
hh=importlib.util.module_from_spec(sp);sp.loader.exec_module(hh)
Candidate,phase,g,PI,THETA=hh.Candidate,hh.phase,hh.g,hh.PI,hh.THETA

def reference(word):
 m=len(word)
 def grad(z):
  ans=np.zeros(m,dtype=complex)
  for j in range(m):
   gr=phase(z[j-1],z[j],word[j-1],word[j])[1]
   ans[j-1]+=gr[0];ans[j]+=gr[1]
  return ans
 def eq(v):
  gr=grad(v[:m]+1j*v[m:]);return np.r_[gr.real,gr.imag]
 z=np.array([.35-.01j if not t else .30-.052j for t in word])
 sol=root(eq,np.r_[z.real,z.imag],tol=1e-11)
 z=sol.x[:m]+1j*sol.x[m:];error=float(np.max(np.abs(grad(z))))
 assert sol.success and error<1e-10
 return z,error

def raw_endpoint(cc,j,other,selection,other_first):
 other=np.asarray(other,dtype=complex);eps=cc.t(j)
 y,h=other.real,other.imag;H=np.abs(h);rad=np.exp(-2*PI*H)
 lam=2*PI*(np.maximum(h,0)-int(other_first)*h)
 lo=np.full(other.shape,1e-12);hi=np.full(other.shape,.5-1e-12)
 for _ in range(44):
  u=(lo+hi)/2
  mod2=(1-rad)**2+4*rad*np.sin(PI*(y+u))**2
  deriv=np.log(2*np.cos(PI*u))+.5*np.log(mod2)-(2+eps)*np.log(2*np.sin(PI*u))+lam
  lo=np.where(deriv>0,u,lo);hi=np.where(deriv>0,hi,u)
 u=(lo+hi)/2
 val=g(u+.5).real+(g(y+u-1j*H)-g(y-1j*H)).real-(2+eps)*g(u).real+lam*u
 kind=cc.t(j-1) if other_first else cc.t(j)
 val+=kind*.5*(np.maximum(-g(other).real,2*PI*np.maximum(h,0))-2*PI*selection*h)
 a,b=(other,np.full(other.shape,.5+0j)) if other_first else (np.full(other.shape,.5+0j),other)
 f,gr=cc.base[j%cc.m]
 gamma=(f+gr[0]*(a-cc.r(j-1))+gr[1]*(b-cc.r(j))).real
 return val-gamma,u

def evaluator(cc,selected):
 bonus=.09-7.55*cc.r(-2).imag**2-5.5*cc.r(0).imag**2
 def evaluate(v,details=False):
  v=np.asarray(v).reshape(-1,3);x,y,z=v.T
  Y=cc.target(1,.5,y,z,selected)
  dl,ul=raw_endpoint(cc,0,x.astype(complex),0,True)
  dr,ur=raw_endpoint(cc,1,Y,selected,False)
  out=np.column_stack((np.full(len(x),cc.r(-2).real),x,np.full(len(x),cc.r(0).real)))
  ent=np.column_stack((np.full(len(x),cc.r(0).real),y,z))
  ex=cc.E3(0,out,(0,0,0));entry=cc.V(2,ent,(0,selected,0))
  psi=cc.om(-1,x,0)
  val=dl+dr-ex-entry-(1-THETA)*psi-bonus
  assert np.isfinite(val).all()
  if details:return val,dict(raw_left=dl,raw_right=dr,left_row=ul,right_row=ur,
       exit=ex,entry=entry,exit_occupation=psi,terminal_bonus=np.full(len(x),bonus),
       right_height=Y.imag)
  return val
 return evaluate

def main():
 start=time.monotonic();rows=[]
 words=[(0,),(1,),(0,1),(1,0),(0,0,1),(0,1,0),(1,0,0),(0,1,1),(1,0,1),(1,1,0)]
 for word in words:
  ref,error=reference(word);cc=Candidate(word,ref)
  for selection in range(cc.t(1)+1):
   ev=evaluator(cc,selection)
   opt=differential_evolution(lambda v:-ev(np.asarray(v).T),[(.1,.1),(.1,.5),(.1,.5)],
      seed=17000+len(rows),maxiter=65,popsize=8,polish=False,vectorized=True,
      updating='deferred',tol=1e-10)
   local=minimize(lambda v:-ev(v)[0],opt.x,method='L-BFGS-B',
      bounds=[(.1,.1),(.1,.5),(.1,.5)],options={'maxiter':100,'ftol':1e-13,'gtol':1e-8})
   trial=np.vstack([opt.x,local.x,*itertools.product((.1,),(.1,.12,.22,.4,.45,.5),(.1,.12,.22,.45,.5))])
   values=ev(trial);k=int(values.argmax());v=trial[k];value,parts=ev(v,True)
   row=dict(word=word,right_neighbor_selection=selection,maximum_found=float(value[0]),
      reals=v.tolist(),parts={k:float(vv[0]) for k,vv in parts.items()},
      reference=[[float(z.real),float(z.imag)] for z in ref],reference_residual=error)
   rows.append(row);print(json.dumps(row),flush=True)
 out=dict(scope='Bounded floating pilot of the PROVED low-terminal incoming upper formula plus literal A3 right entry and full raw edge envelopes. Low terminal is fixed at .1 after the exact potential-transport and raw monotonicity reduction. Ten fixed actual periodic references, all right-neighbor selections; no word-length search. Raw row maximizers use bisection of the strictly concave row derivative. All right reals fixed at .5 using the separate analytic reduction. The outer DE/grid values are lower trials for a maximum, not certified upper bounds or a uniform interface theorem. No AA occupation share was subtracted; arbitrary first-terminal occupation was conservatively discarded.',
   cases=rows,maximum=max(rows,key=lambda r:r['maximum_found']),elapsed_seconds=time.monotonic()-start,
   dependencies={str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HELPER)})
 (HERE/'endpoint-results.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
