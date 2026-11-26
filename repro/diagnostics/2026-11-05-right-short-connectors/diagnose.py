"""Bounded h=3,4,5 original R-interface diagnostics, never a certificate."""
from pathlib import Path
import hashlib,itertools,json,time
import numpy as np
from scipy.optimize import root,minimize_scalar,differential_evolution,minimize
from phase_helpers import Candidate,phase,g,THETA,PI

HERE=Path(__file__).resolve().parent

def reference(word):
 m=len(word)
 def grad(z):
  ans=np.zeros(m,dtype=complex)
  for j in range(m):
   gg=phase(z[j-1],z[j],word[j-1],word[j])[1]
   ans[j-1]+=gg[0];ans[j]+=gg[1]
  return ans
 def eq(v):
  gg=grad(v[:m]+1j*v[m:]);return np.r_[gg.real,gg.imag]
 z=np.array([.35-.01j if t==0 else .30-.052j for t in word])
 sol=root(eq,np.r_[z.real,z.imag],tol=1e-11)
 z=sol.x[:m]+1j*sol.x[m:]
 assert sol.success and np.max(np.abs(grad(z)))<1e-10
 return z,float(np.max(np.abs(grad(z))))

def path_values(cc,mode,i,h,state,sig,free,selection):
 nf=h-3;free=np.asarray(free).reshape(-1,nf) if nf else np.zeros((1,0))
 n=len(free)
 if mode=='incoming':
  first=i-h
  base=np.broadcast_to([cc.r(j).real for j in range(first-2,first+1)],(n,3))
  xx=np.column_stack((base,free,np.broadcast_to(state,(n,3))))
  ss=(0,0,0,*selection,*sig)
 else:
  first=i
  base=np.broadcast_to([cc.r(j).real for j in range(i+h-2,i+h+1)],(n,3))
  xx=np.column_stack((np.broadcast_to(state,(n,3)),free,base))
  ss=(*sig,*selection,0,0,0)
 return sum((cc.w(first+k,xx[:,k:k+4],ss[k:k+4]) for k in range(h)),np.zeros(n))

def optimize_path(cc,mode,i,h,state,sig,seed):
 positions=list(range(i-h+1,i-2)) if mode=='incoming' else list(range(i+1,i+h-2))
 nf=len(positions);all_choices=[]
 for selection in itertools.product(*[range(cc.t(j)+1) for j in positions]):
  fn=lambda x:path_values(cc,mode,i,h,state,sig,x,selection)
  if nf==0:
   trial=np.zeros((1,0));values=fn(trial)
  elif nf==1:
   grid=np.unique(np.r_[np.linspace(.1,.5,401),.12,.22,.45,cc.r(positions[0]).real])
   vals=fn(grid[:,None]);candidates=[np.array([grid[vals.argmax()]])]
   for k in range(1,len(grid)-1):
    if vals[k]>=vals[k-1] and vals[k]>=vals[k+1]:
     opt=minimize_scalar(lambda x:-fn([[x]])[0],bounds=(grid[k-1],grid[k+1]),
                         method='bounded',options={'xatol':1e-13,'maxiter':100})
     candidates.append(np.array([opt.x]))
   trial=np.vstack(candidates);values=fn(trial)
  else:
   opt=differential_evolution(lambda x:-fn(np.asarray(x).T),[(.1,.5)]*nf,
       seed=seed+len(all_choices),maxiter=70,popsize=8,polish=False,
       vectorized=True,updating='deferred',tol=1e-11)
   loc=minimize(lambda x:-fn(x)[0],opt.x,method='L-BFGS-B',bounds=[(.1,.5)]*nf,
                options={'maxiter':100,'ftol':1e-14,'gtol':1e-8})
   corners=list(itertools.product((.1,.12,.22,.45,.5),repeat=nf))
   trial=np.vstack([opt.x,loc.x,[cc.r(j).real for j in positions],*corners]);values=fn(trial)
  k=int(values.argmax())
  all_choices.append(dict(selection=list(selection),value=float(values[k]),free_reals=trial[k].tolist()))
 best=max(all_choices,key=lambda row:row['value'])
 return dict(mode=mode,depth=h,layer=i,state=list(map(float,state)),state_selection=list(sig),
             free_positions=positions,maximum_found=best['value'],best=best,all_free_selections=all_choices)

def raw_row_values(cc,j,a,b,sa,sb,u):
 u=np.asarray(u)
 def I(z):
  return (g(z.real+u-1j*abs(z.imag))-g(z.real-1j*abs(z.imag))).real+2*PI*max(z.imag,0)*u
 def fw(z,s):return max(-float(g(z).real),2*PI*max(z.imag,0))-2*PI*s*z.imag
 eta,eps=cc.t(j-1),cc.t(j)
 f,gr=cc.base[j%cc.m]
 gamma=(f+gr[0]*(a-cc.r(j-1))+gr[1]*(b-cc.r(j))).real
 return I(a)+I(b)-(2+eps)*g(u).real-2*PI*a.imag*u+.5*eta*fw(a,sa)+.5*eps*fw(b,sb)-gamma

def raw_max(cc,j,a,b,sa,sb):
 grid=np.unique(np.r_[np.linspace(0,1,2001),np.mod(-a.real,1),np.mod(-b.real,1),.5])
 fn=lambda u:raw_row_values(cc,j,a,b,sa,sb,u)
 values=fn(grid);candidates=[(float(values[k]),float(grid[k])) for k in (0,len(grid)-1)]
 for k in range(1,len(grid)-1):
  if values[k]>=values[k-1] and values[k]>=values[k+1]:
   candidates.append((float(values[k]),float(grid[k])))
   op=minimize_scalar(lambda u:-float(fn(u)),bounds=(grid[k-1],grid[k+1]),method='bounded',
                      options={'xatol':1e-13,'maxiter':100})
   candidates.append((-float(op.fun),float(op.x)))
 value,u=max(candidates)
 return dict(edge=j,value=value,row=u,grid_points=len(grid),local_candidates=len(candidates),
             targets=[[float(z.real),float(z.imag)] for z in (a,b)])

def main():
 start=time.monotonic();word=(0,1);ref,res=reference(word);cc=Candidate(word,ref)
 cases=[]
 for index,(name,xl,xr,xR) in enumerate((('endpoint',.1,.5,.5),('strict_interior',.1001,.4999,.5001))):
  out=(cc.r(-2).real,xl,cc.r(0).real);incoming=(cc.r(0).real,xr,cc.r(2).real)
  sig=(0,0,0)
  zl=cc.target(-1,out[0],xl,xR,0);zr=cc.target(1,xR,xr,incoming[2],0)
  raw=[raw_max(cc,0,zl,complex(xR),0,0),raw_max(cc,1,complex(xR),zr,0,0)]
  rawsum=sum(r['value'] for r in raw)
  paths=[];rows=[]
  for h in (3,4,5):
   Aout=optimize_path(cc,'incoming',0,h,out,sig,5100+index*100+h)
   Ain=optimize_path(cc,'incoming',2,h,incoming,sig,5200+index*100+h)
   Eout=optimize_path(cc,'exit',0,h,out,sig,5300+index*100+h)
   paths.extend((Aout,Ain,Eout))
   psi=sum(cc.om(j,x,s) for j,x,s in zip(range(-2,1),out,sig))
   endpoint_share=THETA*.5*(cc.om(-1,xl,0)+cc.om(1,xr,0))
   rows.append(dict(depth=h,same_incoming_trial=rawsum+Aout['maximum_found']-Ain['maximum_found']-endpoint_share,
                    optimized_entry_exit_trial=rawsum-Eout['maximum_found']-Ain['maximum_found']-endpoint_share,
                    strengthened_entry_exit_trial=rawsum-Eout['maximum_found']-Ain['maximum_found']-endpoint_share-(1-THETA)*psi,
                    raw_defect_sum=rawsum,endpoint_occupation_share=float(endpoint_share),exit_occupation=float(psi)))
   print(name,h,json.dumps(rows[-1]),flush=True)
  cases.append(dict(name=name,reference_word=word,reference=[[float(z.real),float(z.imag)] for z in ref],
                    reference_residual=res,right=xR,left=xl,right_neighbor=xr,raw=raw,paths=paths,comparisons=rows))
 out=dict(scope='Bounded floating diagnostic at two preserved actual-reference right-singleton configurations only. Every permitted free selection is evaluated. Incoming/exit optimization gives lower trials, so neither their differences nor displayed interface values are certified upper bounds. Raw row maxima also use bounded floating scalar searches. No global support, subaction, or full-period claim.',
          theta=THETA,depths=[3,4,5],cases=cases,elapsed_seconds=time.monotonic()-start,
          dependencies={str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (HERE/'phase_helpers.py',Path(__file__))})
 (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
