"""Bounded floating test of the FOUR-cost adjusted R-component, not a proof."""
from pathlib import Path
import importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import differential_evolution

spec=importlib.util.spec_from_file_location('whole_ref','/tmp/diagnose_actual_cyclic_one_right_raw_envelope.py')
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
g,phase,reference=core.g,core.phase,core.reference
PI=np.pi;OUT=Path('/tmp/adjusted-right-components-diagnostic.json')

def radial(x):return np.where(x<=.45,1,400*(.5-x)**2)
def height(x,other,typ,sel,ref):
 b=.12 if sel else .22
 return (.014 if sel else ref.imag)*radial(x)*np.minimum(np.clip((x-.1)/(b-.1),0,1),np.clip((other-.1)/(b-.1),0,1))
def chi(z):return np.maximum(g(z).real,-2*PI*z.imag)

def evaluator(word,ref,length,selection):
 m=len(word)
 def typ(j):return word[j%m]
 def rr(j):return ref[j%m]
 phi0={};gr={}
 for j in range(-1,length+2):phi0[j],gr[j]=phase(rr(j-1),rr(j),typ(j-1),typ(j))
 def gamma(j,a,b):return (phi0[j]+gr[j][0]*(a-rr(j-1))+gr[j][1]*(b-rr(j))).real
 def w(j,a,b,sa=0,sb=0):return phase(a,b,typ(j-1),typ(j))[0].real-gamma(j,a,b)+.5*sa*chi(a)+.5*sb*chi(b)
 def evaluate(arr,details=False):
  v=np.asarray(arr,dtype=float).reshape(-1,2*length+5)
  # Two A symbols at each end, length R reals, length+1 raw row fractions.
  xl,prev,xr,nxt=v[:,0],v[:,1],v[:,2],v[:,3]
  rx=v[:,4:4+length];rows=v[:,4+length:]
  sl,sr=selection
  zl=xl+1j*height(xl,prev,typ(-1),sl,rr(-1))
  zr=xr+1j*height(xr,nxt,typ(length),sr,rr(length))
  # Two reference vertices next to the A-run become attenuated in the
  # synthetic closure; omitting these is precisely the invalid shortcut.
  pl=rr(0).real+1j*rr(0).imag*np.clip((xl-.1)/.12,0,1)
  pr=rr(length-1).real+1j*rr(length-1).imag*np.clip((xr-.1)/.12,0,1)
  exit_cost=w(0,zl,pl,sl,0)+w(1,pl,rr(1))
  entry_cost=w(length-1,rr(length-2),pr)+w(length,pr,zr,0,sr)
  z=np.column_stack((zl,rx,zr));raw=[]
  for j in range(length+1):
   a,b=z[:,j],z[:,j+1];u=rows[:,j];eta,e=typ(j-1),typ(j)
   def I(z):return (g(z.real+u-1j*np.abs(z.imag))-g(z.real-1j*np.abs(z.imag))).real+2*PI*np.maximum(z.imag,0)*u
   sa=sl if j==0 else 0;sb=sr if j==length else 0
   wa=np.maximum(-g(a).real,2*PI*np.maximum(a.imag,0))-2*PI*sa*a.imag
   wb=np.maximum(-g(b).real,2*PI*np.maximum(b.imag,0))-2*PI*sb*b.imag
   val=I(a)+I(b)-(2+e)*g(u).real-2*PI*a.imag*u+.5*eta*wa+.5*e*wb
   raw.append(val-gamma(j,a,b))
  raw=np.stack(raw,axis=1)
  def omega(x,s,j):return np.minimum(1,s+400*(np.clip(x,.22,.45)-rr(j).real)**2)/4000+.1*np.maximum(x-.45,0)
  occupation=.5*(omega(xl,sl,-1)+omega(xr,sr,length))
  adjusted=raw.sum(axis=1)-exit_cost-entry_cost-occupation
  assert np.isfinite(adjusted).all()
  if details:return adjusted,raw,exit_cost,entry_cost,occupation,np.column_stack((zl.imag,zr.imag))
  return adjusted
 return evaluate

def main():
 assert not OUT.exists(),'refuse overwrite'
 start=time.time();results=[];refs=[]
 for word in [(0,),(1,),(0,1),(1,0)]:
  ref,M,err=reference(word);refs.append(dict(word=word,reference=[[z.real,z.imag]for z in ref],rate=M,residual=err))
  for length in [1,2]:
   for sl,sr in itertools.product(range(word[-1]+1),range(word[length%len(word)]+1)):
    ev=evaluator(word,ref,length,(sl,sr));bounds=[(.1,.5)]*4+[(.5,1)]*length+[(0,1)]*(length+1)
    opt=differential_evolution(lambda z:-ev(np.asarray(z).T),bounds,seed=76100+len(results),maxiter=45,popsize=6,polish=False,vectorized=True,updating='deferred',tol=1e-8)
    candidates=[opt.x]
    for x in [.1,.22,.30,.45,.5]:
     candidates.append(np.r_[x,ref[-2%len(word)].real,x,ref[(length+1)%len(word)].real,[.5]*length,[.27]*(length+1)])
    cc=np.array(candidates);idx=int(ev(cc).argmax());v=cc[idx];ad,raw,ex,en,occ,hh=ev(v,True)
    row=dict(word=word,right_length=length,selection=(sl,sr),maximum_found=float(ad[0]),variables=v.tolist(),raw_defects=raw[0].tolist(),left_exit_cost=float(ex[0]),right_entry_cost=float(en[0]),occupation=float(occ[0]),endpoint_heights=hh[0].tolist(),reference=refs[-1]['reference'],de_iterations=int(opt.nit),de_success=bool(opt.success))
    results.append(row);print('CASE',len(results),word,length,(sl,sr),row['maximum_found'],flush=True)
 out=dict(scope='Bounded floating diagnostic only; entire adjusted R-component retains two raw interface edges, all interior RR edges, four synthetic AA closure costs and endpoint occupation. Genuine repeated critical references; both A-runs assumed to have at least two symbols. No universal envelope bound or finite-sum failure claimed.',jobs=len(results),cases=results,references=refs,maximum=max(results,key=lambda r:r['maximum_found']),elapsed_seconds=time.time()-start)
 OUT.write_text(json.dumps(out,indent=2)+'\n');print('DONE',json.dumps(out['maximum']),flush=True)
if __name__=='__main__':main()
