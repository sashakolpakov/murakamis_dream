"""Bounded floating incoming-connector values at the preserved one-R example."""
from pathlib import Path
import importlib.util,json,time
import numpy as np
from scipy.optimize import differential_evolution
s=importlib.util.spec_from_file_location('adj','/tmp/diagnose_adjusted_right_components.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
ref,M,err=c.reference((0,1));theta=.5
def rr(j):return ref[j%2]
def incoming(depth,target_middle):
 i=0;start=i-depth;idx=np.arange(start-2,i+1);free=list(range(start+1,i-2));nf=len(free)
 constants={j:c.phase(rr(j-1),rr(j),(j-1)%2,j%2)for j in range(start,i)}
 def val(v):
  v=np.asarray(v).reshape(-1,nf)if nf else np.zeros((1,0));n=len(v)
  x=np.broadcast_to(np.array([rr(j).real for j in idx]),(n,len(idx))).copy()
  for k,j in enumerate(free):x[:,j-idx[0]]=v[:,k]
  x[:,-2]=target_middle
  # All symbols unselected in this bounded first pilot.
  hh=np.zeros_like(x)
  for j in range(start-1,i):
   col=j-idx[0];xx=x[:,col]
   hh[:,col]=rr(j).imag*np.where(xx<=.45,1,400*(.5-xx)**2)*np.clip((x[:,col-1:col+2]-.1)/.12,0,1).min(axis=1)
  z=x+1j*hh
  omega=np.minimum(1,400*(np.clip(x,.22,.45)-np.array([rr(j).real for j in idx]))**2)/4000+.1*np.maximum(x-.45,0)
  result=np.zeros(n)
  for j in range(start,i):
   l=j-1-idx[0];k=j-idx[0];f,gr=constants[j]
   gg=f+gr[0]*(z[:,l]-rr(j-1))+gr[1]*(z[:,k]-rr(j))
   result+=(c.phase(z[:,l],z[:,k],(j-1)%2,j%2)[0]-gg).real+theta*.5*(omega[:,l]+omega[:,k])
  return result
 return val,free
def main():
 rows=[];start=time.time()
 for depth in [3,4,6,8]:
  row=dict(depth=depth,theta=theta)
  for name,target in [('exit_state',.1),('entry_state',.5)]:
   fun,free=incoming(depth,target)
   if not free:point=[];value=float(fun([])[0]);success=True
   else:
    opt=differential_evolution(lambda x:-fun(np.asarray(x).T),[(.1,.5)]*len(free),seed=2300+depth+(name=='entry_state'),maxiter=40,popsize=6,polish=False,vectorized=True,updating='deferred',tol=1e-9)
    candidates=np.vstack([opt.x,np.array([rr(j).real for j in free])]);k=int(fun(candidates).argmax());point=candidates[k].tolist();value=float(fun(candidates)[k]);success=bool(opt.success)
   row[name]=dict(value=value,free_positions=free,point=point,optimizer_success=success)
  row['adjusted_with_same_incoming_values']=-.102490981932-.095060240928+row['exit_state']['value']-row['entry_state']['value']
  rows.append(row);print(json.dumps(row),flush=True)
 Path('/tmp/same-incoming-potential-diagnostic.json').write_text(json.dumps(dict(scope='Floating incoming-connector trial values on unselected free symbols only, theta=.5. Both values are lower bounds on their suprema, so their difference is not a rigorous upper bound. No universal potential or interface claim.',cases=rows,seconds=time.time()-start),indent=2)+'\n')
if __name__=='__main__':main()
