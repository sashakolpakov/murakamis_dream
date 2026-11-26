"""Bounded seam upper-proxy diagnostic with exact virtual halos; no proof."""
from pathlib import Path
import importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import differential_evolution
s=importlib.util.spec_from_file_location('a3','/tmp/diagnose_a3_incoming_residuals.py');a3=importlib.util.module_from_spec(s);s.loader.exec_module(a3)
THETA=.5;G=.28;OUT=Path('/tmp/seam-three-step-closure-diagnostic.json')

def exit3(cc,i,state,sig):
 state=np.asarray(state).reshape(-1,3);n=len(state)
 x=np.column_stack((state,np.broadcast_to([cc.r(j).real for j in range(i+1,i+4)],(n,3))))
 ss=(*sig,0,0,0)
 return sum((cc.w(i+k,x[:,k:k+4],ss[k:k+4])for k in range(3)),np.zeros(n))

def evaluator(cc,selection):
 sl,sr=selection;Q=7.55*cc.r(-1).imag**2+5.5*cc.r(1).imag**2
 def evaluate(v,details=False):
  v=np.asarray(v).reshape(-1,5);xm2,xm1,xp1,xp2,lam=v.T
  xiL=.1+(.02 if sl else .12)*lam;xiR=.1+(.02 if sr else .12)*lam
  left=np.column_stack((xm2,xm1,xiL));right=np.column_stack((xiR,xp1,xp2))
  E=exit3(cc,0,left,(0,sl,0));A=cc.V(2,right,(0,sr,0))
  psi=cc.om(-2,xm2,0)+cc.om(-1,xm1,sl)+cc.om(0,xiL,0)
  endpointshare=THETA*.5*(cc.om(-1,xm1,sl)+cc.om(1,xp1,sr))
  proxy=-E-A-(1-THETA)*psi-endpointshare-G-Q
  if details:return proxy,E,A,psi,endpointshare,xiL,xiR,np.full(len(v),Q)
  return proxy
 return evaluate

def main():
 assert not OUT.exists(),'refuse overwrite';start=time.time();rows=[];refs=[]
 for word in [(0,),(1,),(0,1),(1,0),(0,1,1),(1,0,1),(1,1,0)]:
  ref,M,err=a3.reference(word);cc=a3.Candidate(word,ref);refs.append(dict(word=word,reference=[[z.real,z.imag]for z in ref],gradient_residual=err))
  for sl,sr in itertools.product(range(cc.t(-1)+1),range(cc.t(1)+1)):
   fn=evaluator(cc,(sl,sr));bounds=[(.1,.5)]*4+[(0,1)]
   opt=differential_evolution(lambda z:-fn(np.asarray(z).T),bounds,maxiter=40,popsize=6,polish=False,vectorized=True,updating='deferred',tol=1e-9,seed=45300+len(rows))
   extra=[opt.x]
   for x,y,lam in itertools.product([.1,.22,.45,.5],[.1,.22,.45,.5],[0,.5,1]):extra.append([cc.r(-2).real,x,y,cc.r(2).real,lam])
   vv=np.array(extra);k=int(fn(vv).argmax());v=vv[k];p,E,A,psi,share,l,r,Q=fn(v,True)
   row=dict(word=word,endpoint_selection=[sl,sr],variables_xm2_xm1_xp1_xp2_lambda=v.tolist(),maximum_found=float(p[0]),exit_cost=float(E[0]),entry_cost=float(A[0]),unweighted_closure=float(-E[0]-A[0]),psi_out=float(psi[0]),endpoint_occupation_debit=float(share[0]),Q=float(Q[0]),virtual_halos=[float(l[0]),float(r[0])],iterations=opt.nit,optimizer_success=bool(opt.success))
   rows.append(row);print('CASE',len(rows),json.dumps(row),flush=True)
 assert len(rows)==18
 out=dict(scope='Bounded floating search of a GUARANTEED upper proxy, not its global maximum. Exact virtual halos preserve physical AA heights. All five physical real/cutoff parameters independent, all endpoint selections. Second-neighbor selections only worsen the proxy, so they are unselected. Only old-half neighboring symbols[.1,.5] tested; no extension to prescribed deep endpoints inferred.',theta=THETA,G=G,cases=rows,references=refs,jobs=len(rows),maximum=max(rows,key=lambda r:r['maximum_found']),elapsed_seconds=time.time()-start)
 OUT.write_text(json.dumps(out,indent=2)+'\n');print('MAX',json.dumps(out['maximum']),flush=True)
if __name__=='__main__':main()
