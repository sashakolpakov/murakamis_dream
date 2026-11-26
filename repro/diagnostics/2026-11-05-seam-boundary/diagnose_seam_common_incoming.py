"""Two fixed seam configurations; common incoming h3/h4/h5 diagnostics."""
from pathlib import Path
import importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import differential_evolution,minimize
s=importlib.util.spec_from_file_location('inc','/tmp/diagnose_incoming_depth_increments.py');inc=importlib.util.module_from_spec(s);s.loader.exec_module(inc)
a4=inc.a4
def A5(cc,i,state,sig,prev,seed):
 positions=list(range(i-4,i-2));best=None
 for si,selection in enumerate(itertools.product(*[range(cc.t(j)+1)for j in positions])):
  fn=lambda x:inc.value(cc,i,5,state,sig,x,selection)
  opt=differential_evolution(lambda x:-fn(np.asarray(x).T),[(.1,.5)]*2,maxiter=40,popsize=6,polish=False,seed=seed+si,vectorized=True,updating='deferred',tol=1e-10)
  local=minimize(lambda x:-fn(x)[0],opt.x,method='L-BFGS-B',bounds=[(.1,.5)]*2,options=dict(maxiter=50,ftol=1e-13,gtol=1e-8))
  candidates=[opt.x,local.x,np.array([cc.r(j).real for j in positions])]
  if selection==(0,prev['free_selected']):candidates.append(np.array([cc.r(positions[0]).real,prev['free_real']]))
  xx=np.array(candidates);vv=fn(xx);k=int(vv.argmax());row=dict(value=float(vv[k]),free=xx[k].tolist(),selection=selection,DE_success=bool(opt.success))
  if best is None or row['value']>best['value']:best=row
 return best
def main():
 src=json.load(open('/tmp/seam-three-step-closure-diagnostic.json'));cases=[src['maximum'],max((r for r in src['cases']if r['word']==[1]),key=lambda r:r['maximum_found'])];out=[];start=time.time()
 for k,case in enumerate(cases):
  word=tuple(case['word']);ref,_,_=a4.a3.reference(word);cc=a4.a3.Candidate(word,ref);xm2,xm1,xp1,xp2,lam=case['variables_xm2_xm1_xp1_xp2_lambda'];sl,sr=case['endpoint_selection'];xiL,xiR=case['virtual_halos']
  states=[(0,[xm2,xm1,xiL],(0,sl,0)),(2,[xiR,xp1,xp2],(0,sr,0))];values=[]
  for n,(i,state,sig)in enumerate(states):
   v3=float(cc.V(i,state,sig)[0]);v4=a4.A4(cc,i,state,sig);v5=A5(cc,i,state,sig,v4,7200+20*k+8*n)
   values.append(dict(state=state,selection=sig,layer=i,A3=v3,A4=v4,A5=v5))
  rows=[]
  for h in (3,4,5):
   vo=values[0]['A'+str(h)];vi=values[1]['A'+str(h)];vo=vo if h==3 else vo['value'];vi=vi if h==3 else vi['value']
   rows.append(dict(h=h,exit_incoming=vo,entry_incoming=vi,difference=vo-vi,proxy_estimate=vo-vi-.28-case['Q']-case['endpoint_occupation_debit']))
  row=dict(word=word,physical_parameters=case['variables_xm2_xm1_xp1_xp2_lambda'],source_pair_constant=.28,Q=case['Q'],endpoint_occupation_debit=case['endpoint_occupation_debit'],states=values,comparisons=rows);out.append(row);print(json.dumps(row),flush=True)
 Path('/tmp/seam-common-incoming-diagnostic.json').write_text(json.dumps(dict(scope='Two fixed configurations only. A3 exact finite formula; A4/A5 are scalar/two-variable maximum lower estimates including all allowed free selections. Their differences are not rigorous upper bounds or counterexamples to the common-potential criterion.',cases=out,elapsed_seconds=time.time()-start),indent=2)+'\n')
if __name__=='__main__':main()
