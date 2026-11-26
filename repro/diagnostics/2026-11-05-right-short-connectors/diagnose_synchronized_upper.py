"""Bounded local synchronized-tail envelope; floating values are not bounds."""
import itertools,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from phase_helpers import Candidate,THETA
from diagnose import reference,path_values

HERE=Path(__file__).resolve().parent

def correction(cc,i,state,free,selection):
 free=np.asarray(free).reshape(-1,2);n=len(free)
 # The first predecessor letter cancels because terminal first/third
 # are the baseline letters. The next two predecessor letters are free.
 u=np.column_stack((np.full(n,cc.r(i-5).real),free))
 v=np.broadcast_to(state,(n,3))
 p=np.broadcast_to([cc.r(j).real for j in range(i-2,i+1)],(n,3))
 x=np.column_stack((u,v));y=np.column_stack((u,p))
 sig=(0,0,selection,0,0,0)
 return sum((cc.w(i-3+k,x[:,k:k+4],sig[k:k+4])-
             cc.w(i-3+k,y[:,k:k+4],sig[k:k+4]) for k in range(3)),np.zeros(n))

def main():
 start=time.monotonic();ref,res=reference((0,1));cc=Candidate((0,1),ref)
 previous=json.loads((HERE/'results.json').read_text());cases=[]
 for index,row in enumerate(previous['cases']):
  xl=row['left'];state=(cc.r(-2).real,xl,cc.r(0).real);choices=[]
  for selection in (0,1):
   fn=lambda v:correction(cc,0,state,v,selection)
   opt=differential_evolution(lambda x:-fn(np.asarray(x).T),[(.1,.5)]*2,
      seed=8801+2*index+selection,maxiter=60,popsize=8,polish=False,
      vectorized=True,updating='deferred',tol=1e-11)
   loc=minimize(lambda x:-fn(x)[0],opt.x,method='L-BFGS-B',bounds=[(.1,.5)]*2,
                options={'maxiter':100,'ftol':1e-14,'gtol':1e-8})
   grid=np.array(list(itertools.product(np.unique(np.r_[np.linspace(.1,.5,81),.12,.22,.45]),repeat=2)))
   trial=np.vstack([grid,opt.x,loc.x,ref.real]);values=fn(trial);k=int(values.argmax())
   choices.append(dict(selection=selection,maximum_found=float(values[k]),predecessor_reals=trial[k].tolist()))
  best=max(choices,key=lambda d:d['maximum_found'])
  Ain=next(p['maximum_found'] for p in row['paths'] if p['mode']=='incoming' and p['depth']==5 and p['layer']==2)
  comp=row['comparisons'][-1]
  result=dict(name=row['name'],out_state=list(state),choices=choices,
      synchronized_upper_trial=best['maximum_found'],A5_incoming_trial=Ain,
      adjusted_trial=comp['raw_defect_sum']+best['maximum_found']-Ain-comp['endpoint_occupation_share'])
  cases.append(result);print(json.dumps(result),flush=True)
 output=dict(scope='Finite synchronized-tail formula is a proved algebraic upper for H when its maximum is actually bounded. Here the maxima and A5 are floating lower trials only, so the displayed adjusted values are diagnostics, not certified upper bounds. Two fixed actual-reference configurations, all predecessor selections, no outer-state or word search.',
   cases=cases,elapsed_seconds=time.monotonic()-start,dependencies={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'phase_helpers.py',HERE/'diagnose.py',HERE/'results.json')})
 (HERE/'synchronized-upper.json').write_text(json.dumps(output,indent=2)+'\n')
if __name__=='__main__':main()
