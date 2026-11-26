"""Bounded floating seam comparison, actual plane and common A3. Not a proof."""
from pathlib import Path
import hashlib, importlib.util, itertools, json, time
import numpy as np
from scipy.optimize import differential_evolution

spec=importlib.util.spec_from_file_location('a3','/tmp/diagnose_a3_incoming_residuals.py')
a3=importlib.util.module_from_spec(spec);spec.loader.exec_module(a3)
OUT=Path('/tmp/seam-actual-plane-common-a3-diagnostic.json')
THETA=.5;RHO=.001
A=np.array([[.360050,.447948],[.485081,.551147]])
B=np.array([.347548,.515591])
NU=-float(a3.g(complex(RHO)).real)
DELTA=RHO*np.log(2)+NU
WORDS=[(0,),(1,),(0,1),(1,0),(0,1,1),(1,0,1),(1,1,0)]

def evaluator(cc,selection):
 sm2,sl,sr=selection
 alpha,beta,gamma=[cc.t(j) for j in (-1,0,1)]
 fl,gl=cc.base[0];fr,gr=cc.base[1%cc.m]
 pl,pr=gl[0],gr[1]
 intercept=fl+fr-pl*cc.r(-1)-pr*cc.r(1)
 middle_gradient=gl[1]+gr[0]
 source=A[beta,alpha]+B[gamma]
 collar=2*DELTA+beta*NU
 def evaluate(v,details=False):
  v=np.asarray(v).reshape(-1,5);xm2,xm1,xp1,xp2,lam=v.T
  bL=.12 if sl else .22;bR=.12 if sr else .22
  xiL=.1+(bL-.1)*lam;xiR=.1+(bR-.1)*lam
  left=np.column_stack((xm2,xm1,xiL));right=np.column_stack((xiR,xp1,xp2))
  vout=cc.V(0,left,(sm2,sl,0));vin=cc.V(2,right,(0,sr,0))
  def height(x,other,b,selected,reference):
   R=np.where(x<=.45,1,400*(.5-x)**2)
   attenuation=np.minimum(lam,np.minimum(np.clip((x-.1)/(b-.1),0,1),np.clip((other-.1)/(b-.1),0,1)))
   return (.014 if selected else reference.imag)*R*attenuation
  hl=height(xm1,xm2,bL,sl,cc.r(-1));hr=height(xp1,xp2,bR,sr,cc.r(1))
  zL=xm1+1j*hl;zR=xp1+1j*hr
  plane=(intercept+pl*zL+pr*zR).real
  endpoint=THETA*.5*(cc.om(-1,xm1,sl)+cc.om(1,xp1,sr))
  result=vout-vin-endpoint+source+collar-plane
  if details:return dict(value=result,A3_out=vout,A3_in=vin,difference=vout-vin,endpoint_debit=endpoint,plane=plane,physical_left_height=hl,physical_right_height=hr,virtual_left=xiL,virtual_right=xiR,source_ceiling=np.full(len(v),source),collar=np.full(len(v),collar),middle_gradient_residual=np.full(len(v),abs(middle_gradient)))
  return result
 return evaluate

def main():
 assert not OUT.exists(),'refuse overwrite'
 start=time.time();rows=[];references=[]
 for word in WORDS:
  ref,M,err=a3.reference(word);cc=a3.Candidate(word,ref)
  references.append(dict(word=word,reference=[[z.real,z.imag] for z in ref],critical_rate=M,gradient_residual=err))
  for selection in itertools.product(*[range(cc.t(j)+1) for j in (-2,-1,1)]):
   fn=evaluator(cc,selection)
   opt=differential_evolution(lambda z:-fn(np.asarray(z).T),[(.1,.5)]*4+[(0,1)],maxiter=60,popsize=6,polish=False,vectorized=True,updating='deferred',tol=1e-9,seed=71900+len(rows))
   extras=[opt.x]
   for xl,xr,lam in itertools.product([.1,.22,.45,.5],[.1,.22,.45,.5],[0,.5,1]):
    extras.append([cc.r(-2).real,xl,xr,cc.r(2).real,lam])
   vs=np.asarray(extras);v=vs[int(np.argmax(fn(vs)))];details=fn(v,True)
   row=dict(word=word,selection_xm2_xm1_xp1=list(selection),variables_xm2_xm1_xp1_xp2_lambda=v.tolist(),iterations=int(opt.nit),optimizer_success=bool(opt.success),**{k:float(a[0]) for k,a in details.items()})
   rows.append(row);print('CASE',len(rows),json.dumps(row),flush=True)
 assert len(rows)==29
 out=dict(scope='Bounded floating maxima of the explicit common incoming A_theta^[3] difference plus the actual geometric seam-pair plane and already-proved constant source ceilings. A3 is not the incoming supremum H or a proved subaction. Neither negative found values nor optimizer status certifies a universal upper bound. No interval cover, finite-source asymptotic or cyclic theorem is asserted.',theta=THETA,rho=RHO,nu_rho=NU,Delta_rho=DELTA,source_A=A.tolist(),source_B=B.tolist(),formula='A3out-A3in-theta*(omega_left+omega_right)/2 + A[beta,alpha]+B[gamma]+2Delta+beta*nu - Re Gamma_pair. No Q subtraction.',selection_scope='All allowed bits at physical positions -2,-1,1. Position2 is halo-only in A3in and the seam source; its selection is irrelevant. Seam selection has modulus1 and height0. This expands the old18 closure-proxy cases to29 common-incoming cases.',physical_parameters='Four independent A-symbol reals in [.1,.5] and seam lambda in[0,1], with literal split-cutoff hybrid neighbor heights. Virtual halos use each adjacent row cutoff .22 or .12.',references=references,cases=rows,jobs=len(rows),maximum=max(rows,key=lambda r:r['value']),elapsed_seconds=time.time()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 OUT.write_text(json.dumps(out,indent=2)+'\n');print('MAX',json.dumps(out['maximum']),flush=True)
if __name__=='__main__':main()
