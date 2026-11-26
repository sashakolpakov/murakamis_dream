"""Bounded floating diagnostic of the literal one-right raw/coherent envelope."""
from pathlib import Path
import importlib.util,itertools,json,time,hashlib
import numpy as np
from scipy.optimize import root,differential_evolution

HELPER=Path('/tmp/diagnose_mixed_hybrid_conditioned_interface_phase.py')
sp=importlib.util.spec_from_file_location('existing_phase',HELPER)
hh=importlib.util.module_from_spec(sp);sp.loader.exec_module(hh)
phase,g=hh.phase,hh.g
PI=np.pi;H=.014
WORDS=[(0,1),(1,1),(0,1,1),(1,1,1),(0,1,0,1),(1,1,1,1)]
OUT=Path('/tmp/actual-cyclic-one-right-raw-envelope-diagnostic.json')

def reference(word):
 m=len(word)
 def grad(z):
  ans=np.zeros(m,dtype=complex)
  for j in range(m):
   v=phase(z[j],z[(j+1)%m],word[j],word[(j+1)%m])[1]
   ans[j]+=v[0];ans[(j+1)%m]+=v[1]
  return ans
 def fun(v):
  zz=v[:m]+1j*v[m:];gg=grad(zz)
  return np.r_[gg.real,gg.imag]
 zz=np.array([.35-.01j if not t else .30-.052j for t in word])
 sol=root(fun,np.r_[zz.real,zz.imag],tol=1e-11)
 z=sol.x[:m]+1j*sol.x[m:]
 err=float(np.max(np.abs(grad(z))))
 assert sol.success and err<1e-9,(word,sol.message,err)
 assert np.all((z.real>.27)&(z.real<.39))
 vals=np.array([phase(z[j],z[(j+1)%m],word[j],word[(j+1)%m])[0] for j in range(m)])
 return z,float(vals.real.sum()),err

def evaluate(v,word,sigma,ref,M,details=False):
 v=np.asarray(v,dtype=float).reshape(-1,len(word)+2)
 m=len(word);x=v[:,:m];rows=v[:,m:];sigma=np.array(sigma)
 R=np.where(x<=.45,1,np.where(x<.5,400*(.5-x)**2,0))
 heights=np.empty_like(x)
 for j in range(m):
  b=.12 if sigma[j] else .22
  lf=np.clip((x[:,[(j-1)%m,j,(j+1)%m]]-.1)/(b-.1),0,1).min(axis=1)
  heights[:,j]=(.014 if sigma[j] else ref[j].imag)*R[:,j]*lf
 z=x+1j*heights
 weight=np.maximum(-g(z).real,2*PI*np.maximum(heights,0))-2*PI*sigma*heights
 incident=(0,m-1);values=[]
 for j in range(m):
  k=(j+1)%m;eta,e=word[j],word[k]
  if j in incident:
   u=rows[:,0 if j==0 else 1]
   def I(hh,xx):
    return (g(xx+u-1j*np.abs(hh))-g(xx-1j*np.abs(hh))).real+2*PI*np.maximum(hh,0)*u
   val=I(heights[:,j],x[:,j])+I(heights[:,k],x[:,k])-(2+e)*g(u).real-2*PI*heights[:,j]*u
   val+=.5*eta*weight[:,j]+.5*e*weight[:,k]
  else:
   val=phase(z[:,j],z[:,k],eta,e)[0].real
   val+=.5*sigma[j]*np.maximum(g(z[:,j]).real,-2*PI*heights[:,j])
   val+=.5*sigma[k]*np.maximum(g(z[:,k]).real,-2*PI*heights[:,k])
  values.append(val)
 values=np.stack(values,axis=1);defect=values.sum(axis=1)-M
 assert np.all(np.isfinite(defect)),(word,v)
 if details:return defect,heights,values,weight
 return defect

def main():
 assert not OUT.exists(),'Refuse to overwrite diagnostic'
 start=time.monotonic();cases=[];refs=[]
 for word in WORDS:
  ref,M,err=reference(word);m=len(word)
  refs.append(dict(word=word,reference=[[float(z.real),float(z.imag)]for z in ref],critical_rate=M,gradient_residual=err))
  for rest in itertools.product(*[range(t+1)for t in word[1:]]):
   sigma=(0,*rest);index=len(cases)
   bounds=[(.5,1)]+[(.1,.5)]*(m-1)+[(0,1),(0,1)]
   opt=differential_evolution(lambda a:-evaluate(np.asarray(a).T,word,sigma,ref,M),bounds,
       maxiter=40,popsize=6,tol=1e-8,polish=False,seed=92100+index,
       vectorized=True,updating='deferred')
   trial=[opt.x]
   for xr,ur,vl in itertools.product((.5,.75,1),(.2,.3,.5),(.2,.3,.5)):
    trial.append(np.r_[xr,ref.real[1:],ur,vl])
   trial=np.asarray(trial);vv=evaluate(trial,word,sigma,ref,M);ii=int(vv.argmax())
   choice=trial[ii];de,he,ed,wt=evaluate(choice,word,sigma,ref,M,True)
   row=dict(word=word,selection=sigma,maximum_found=float(de[0]),target_reals=choice[:m].tolist(),
            raw_rows=choice[m:].tolist(),target_heights=he[0].tolist(),edge_rates=ed[0].tolist(),
            full_weight_rates=wt[0].tolist(),critical_rate=M,reference=refs[-1]['reference'],
            reference_gradient_residual=err,de_iterations=int(opt.nit),de_population=int(opt.population.shape[0]),
            de_success=bool(opt.success),scope='Floating candidate only; no certified global maximization.')
   cases.append(row)
   print('CASE',index+1,word,sigma,'defect',row['maximum_found'],flush=True)
   OUT.with_suffix('.partial.json').write_text(json.dumps(dict(cases=cases),indent=2)+'\n')
 assert len(cases)==24
 result=dict(scope='Bounded floating diagnostic only. Six actual original zero-lift cyclic critical references; exactly one real right coordinate; full hybrid row heights, all 24 allowed remaining selections, two independent original raw rows and coherent other edges. No finite-sum or integral counterexample claimed.',
             helper=str(HELPER),helper_sha256=hashlib.sha256(HELPER.read_bytes()).hexdigest(),
             references=refs,cases=cases,jobs=24,max_de_iterations=40,popsize_multiplier=6,
             maximum=max(cases,key=lambda z:z['maximum_found']),elapsed_seconds=time.monotonic()-start)
 OUT.write_text(json.dumps(result,indent=2)+'\n');OUT.with_suffix('.partial.json').unlink()
 print('DONE',len(cases),'seconds',result['elapsed_seconds'],'MAX',json.dumps(result['maximum']),flush=True)
if __name__=='__main__':main()
