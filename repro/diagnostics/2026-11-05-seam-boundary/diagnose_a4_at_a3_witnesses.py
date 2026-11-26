"""Bounded scalar incoming A4 searches at preserved A3 witness points."""
from pathlib import Path
import importlib.util,json,time
import numpy as np
from scipy.optimize import minimize_scalar
s=importlib.util.spec_from_file_location('a3','/tmp/diagnose_a3_incoming_residuals.py');a3=importlib.util.module_from_spec(s);s.loader.exec_module(a3)

def scalar_values(cc,i,state,sig,y,selected):
 y=np.asarray(y,dtype=float).reshape(-1);n=len(y)
 xx=np.column_stack((np.broadcast_to([cc.r(j).real for j in range(i-6,i-3)],(n,3)),y,np.broadcast_to(state,(n,3))))
 ss=(0,0,0,selected,*sig)
 return sum((cc.w(i-4+k,xx[:,k:k+4],ss[k:k+4])for k in range(4)),np.zeros(n))

def A4(cc,i,state,sig):
 best=None
 for selected in range(cc.t(i-3)+1):
  knots=np.unique(np.r_[np.linspace(.1,.5,401),state,.12,.22,.45,[cc.r(j).real for j in range(i-6,i)]])
  vv=scalar_values(cc,i,state,sig,knots,selected);idx=int(vv.argmax());candidates=[(float(vv[idx]),float(knots[idx]))]
  peaks=[j for j in range(1,len(knots)-1)if vv[j]>=vv[j-1]and vv[j]>=vv[j+1]]
  for j in sorted(peaks,key=lambda j:vv[j],reverse=True)[:8]:
   opt=minimize_scalar(lambda y:-scalar_values(cc,i,state,sig,[y],selected)[0],bounds=(knots[j-1],knots[j+1]),method='bounded',options={'xatol':1e-12,'maxiter':60})
   candidates.append((-float(opt.fun),float(opt.x)))
  value,y=max(candidates)
  if best is None or value>best['value']:best=dict(value=value,free_real=y,free_selected=selected,grid_size=len(knots))
 return best

def main():
 data=json.load(open('/tmp/a3-incoming-residuals-diagnostic.json'));out=[];start=time.time();cache={}
 for family in ['bellman_cases','component_cases']:
  for index,row in enumerate(data[family]):
   word=tuple(row['word'])
   if word not in cache:
    r,_,_=a3.reference(word);cache[word]=a3.Candidate(word,r)
   cc=cache[word]
   if family=='bellman_cases':
    x=np.array(row['target_reals']);sig=tuple(row['selection']);prev=A4(cc,0,x[:3],sig[:3]);nxt=A4(cc,1,x[1:],sig[1:]);base=row['original_weight'];estimate=base+prev['value']-nxt['value']
   else:
    x=np.array(row['variables']);length=row['right_length'];ss,sl,sr=row['selection_secondA_leftA_rightA']
    prev=A4(cc,0,[x[1],x[0],cc.r(0).real],(ss,sl,0));nxt=A4(cc,length+1,[cc.r(length-1).real,x[2],x[3]],(0,sr,0));base=sum(row['raw_defects']);estimate=base+prev['value']-nxt['value']
   rr=dict(family=family,index=index,word=word,original_A3_value=row.get('original_w_residual',row.get('adjusted_component')),A4_estimated_value=estimate,plus_potential=prev,minus_potential=nxt)
   out.append(rr);print(json.dumps(rr),flush=True)
 Path('/tmp/a4-at-a3-witnesses-diagnostic.json').write_text(json.dumps(dict(scope='A4 scalar suprema estimated by401-point grid plus bounded local searches, including both allowed selections. Differences of these lower estimates are not rigorous upper bounds. Only the stored A3 witness configurations were evaluated; no new outer search.',cases=out,elapsed_seconds=time.time()-start),indent=2)+'\n')
if __name__=='__main__':main()
