"""Bounded h5/h6 scalar-state diagnostics; no outer search or upper claim."""
from pathlib import Path
import importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import differential_evolution,minimize
s=importlib.util.spec_from_file_location('a4','/tmp/diagnose_a4_at_a3_witnesses.py');a4=importlib.util.module_from_spec(s);s.loader.exec_module(a4)

def value(cc,i,h,state,sig,free,selection):
 free=np.asarray(free).reshape(-1,h-3);n=len(free)
 initial=np.broadcast_to([cc.r(j).real for j in range(i-h-2,i-h+1)],(n,3))
 xx=np.column_stack((initial,free,np.broadcast_to(state,(n,3))))
 ss=(0,0,0,*selection,*sig)
 return sum((cc.w(i-h+k,xx[:,k:k+4],ss[k:k+4])for k in range(h)),np.zeros(n))

def main():
 src=json.load(open('/tmp/a3-incoming-residuals-diagnostic.json'));rows=[];start=time.time();jobs=0
 for ix in [0,11]:
  old=src['bellman_cases'][ix];word=tuple(old['word']);r,_,_=a4.a3.reference(word);cc=a4.a3.Candidate(word,r);state=np.array(old['target_reals'][1:]);sig=tuple(old['selection'][1:]);i=1
  A3=float(cc.V(i,state,sig)[0]);A4=a4.A4(cc,i,state,sig);prev=dict(value=A4['value'],free=[A4['free_real']],selection=[A4['free_selected']]);levels=[dict(h=3,value=A3),dict(h=4,**prev)]
  for h in [5,6]:
   positions=list(range(i-h+1,i-2));best=None
   for selection in itertools.product(*[range(cc.t(j)+1)for j in positions]):
    fn=lambda x:value(cc,i,h,state,sig,x,selection)
    opt=differential_evolution(lambda x:-fn(np.asarray(x).T),[(.1,.5)]*(h-3),maxiter=45,popsize=6,polish=False,seed=64100+jobs,vectorized=True,updating='deferred',tol=1e-10)
    jobs+=1
    local=minimize(lambda x:-fn(x)[0],opt.x,method='L-BFGS-B',bounds=[(.1,.5)]*(h-3),options=dict(maxiter=60,ftol=1e-13,gtol=1e-8))
    candidates=[opt.x,local.x,np.array([cc.r(j).real for j in positions])]
    if selection==(0,*prev['selection']):candidates.append(np.r_[cc.r(positions[0]).real,prev['free']])
    vv=np.array(candidates);vals=fn(vv);k=int(vals.argmax());entry=dict(value=float(vals[k]),free=vv[k].tolist(),selection=list(selection),DE_success=bool(opt.success))
    if best is None or entry['value']>best['value']:best=entry
   levels.append(dict(h=h,**best));prev=best
  budget=float(a4.a3.THETA*.5*(cc.om(i-2,state[0],sig[0])+cc.om(i-1,state[1],sig[1])))
  for j in range(1,len(levels)):levels[j]['estimated_increment']=levels[j]['value']-levels[j-1]['value'];levels[j]['increment_minus_budget']=levels[j]['estimated_increment']-budget
  row=dict(word=word,state=state.tolist(),selection=sig,theta_occupation_budget=budget,levels=levels);rows.append(row);print(json.dumps(row),flush=True)
 Path('/tmp/incoming-depth-increments-diagnostic.json').write_text(json.dumps(dict(scope='Only two preserved output states. All allowed free predecessor selections included. A4 by scalar grid/local search, A5/A6 by bounded DE+local search. Values are lower estimates; their differences are not certified increment bounds or global subaction assertions.',jobs=jobs,cases=rows,elapsed_seconds=time.time()-start),indent=2)+'\n')
if __name__=='__main__':main()
