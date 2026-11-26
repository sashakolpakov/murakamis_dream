"""Bounded diagnostics of the explicit A_theta^[3] candidate, theta=1/2."""
from pathlib import Path
import importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import differential_evolution

s=importlib.util.spec_from_file_location('adj','/tmp/diagnose_adjusted_right_components.py')
core=importlib.util.module_from_spec(s);s.loader.exec_module(core)
phase,g,reference=core.phase,core.g,core.reference
THETA=.5;OUT=Path('/tmp/a3-incoming-residuals-diagnostic.json')

class Candidate:
 def __init__(self,word,ref):
  self.word=tuple(word);self.ref=ref;self.m=len(word)
  self.base={j:phase(self.r(j-1),self.r(j),self.t(j-1),self.t(j))for j in range(self.m)}
 def t(self,j):return self.word[j%self.m]
 def r(self,j):return self.ref[j%self.m]
 def om(self,j,x,s):return np.minimum(1,s+400*(np.clip(x,.22,.45)-self.r(j).real)**2)/4000+.1*np.maximum(x-.45,0)
 def w(self,j,x,sig,details=False):
  x=np.asarray(x).reshape(-1,4);z=[]
  for k,col in enumerate((1,2)):
   pos=j-1+k;sel=sig[col];xx=x[:,col];b=.12 if sel else .22
   R=np.where(xx<=.45,1,400*(.5-xx)**2)
   h=(.014 if sel else self.r(pos).imag)*R*np.clip((x[:,col-1:col+2]-.1)/(b-.1),0,1).min(axis=1)
   z.append(xx+1j*h)
  f,gr=self.base[j%self.m];gamma=f+gr[0]*(z[0]-self.r(j-1))+gr[1]*(z[1]-self.r(j))
  val=(phase(z[0],z[1],self.t(j-1),self.t(j))[0]-gamma).real
  for k,col in enumerate((1,2)):val+=.5*sig[col]*np.maximum(g(z[k]).real,-2*np.pi*z[k].imag)
  shares=.5*(self.om(j-1,x[:,1],sig[1])+self.om(j,x[:,2],sig[2]))
  if details:return val,shares
  return val+THETA*shares
 def V(self,i,x,sig):
  x=np.asarray(x).reshape(-1,3);n=len(x)
  allx=np.column_stack((np.broadcast_to([self.r(j).real for j in range(i-5,i-2)],(n,3)),x))
  alls=(0,0,0,*sig)
  return sum((self.w(i-3+k,allx[:,k:k+4],alls[k:k+4])for k in range(3)),np.zeros(n))
 def bellman(self,x,sig,details=False):
  x=np.asarray(x).reshape(-1,4);w,share=self.w(0,x,sig,True)
  vp=self.V(0,x[:,:3],sig[:3]);vn=self.V(1,x[:,1:],sig[1:]);res=w+vp-vn
  if details:return res,w,share,vp,vn
  return res
 def component(self,length,sel,x,details=False):
  x=np.asarray(x).reshape(-1,2*length+5);leftsel,sl,sr=sel
  old=core.evaluator(self.word,self.ref,length,(sl,sr));_,raw,ex,en,occ,hh=old(x,True)
  leftstate=np.column_stack((x[:,1],x[:,0],np.full(len(x),self.r(0).real)))
  rightstate=np.column_stack((np.full(len(x),self.r(length-1).real),x[:,2],x[:,3]))
  vl=self.V(0,leftstate,(leftsel,sl,0));vr=self.V(length+1,rightstate,(0,sr,0))
  adjusted=raw.sum(axis=1)+vl-vr
  if details:return adjusted,raw,vl,vr,hh
  return adjusted

def optimize(fun,bounds,index,extras):
 opt=differential_evolution(lambda x:-fun(np.asarray(x).T),bounds,maxiter=30,popsize=5,polish=False,seed=58100+index,vectorized=True,updating='deferred',tol=1e-9)
 vv=np.vstack((opt.x,*extras));vals=fun(vv);k=int(vals.argmax())
 return vv[k],opt

def main():
 assert not OUT.exists(),'refuse overwrite';start=time.time();br=[];cr=[];refs=[]
 for word in [(0,),(1,),(0,1),(1,0)]:
  ref,M,err=reference(word);cc=Candidate(word,ref);refs.append(dict(word=word,reference=[[z.real,z.imag]for z in ref],gradient_residual=err))
  for bits in itertools.product(*[range(cc.t(j)+1)for j in (-2,-1,0)]):
   sig=(*bits,0);extras=[np.array([cc.r(j).real for j in range(-2,2)]),np.array([.1,.22,.45,.5]),np.array([.5,.45,.22,.1])]
   v,opt=optimize(lambda x:cc.bellman(x,sig),[(.1,.5)]*4,len(br),extras)
   res,w,share,vp,vn=cc.bellman(v,sig,True)
   row=dict(word=word,selection=sig,target_reals=v.tolist(),original_w_residual=float(res[0]),t_residual=float(res[0]+THETA*share[0]),theta_occupation_share=float(THETA*share[0]),original_weight=float(w[0]),V_previous=float(vp[0]),V_next=float(vn[0]),iterations=opt.nit,optimizer_success=bool(opt.success))
   br.append(row);print('BELLMAN',len(br),json.dumps(row),flush=True)
  for length in (1,2):
   for bits in itertools.product(*[range(cc.t(j)+1)for j in (-2,-1,length)]):
    fun=lambda x:cc.component(length,bits,x)
    extras=[np.r_[.1,cc.r(-2).real,.5,cc.r(length+1).real,[.5]*length,[.28]+[.23]*length],np.r_[.5,cc.r(-2).real,.1,cc.r(length+1).real,[.5]*length,[.25]*(length+1)]]
    v,opt=optimize(fun,[(.1,.5)]*4+[(.5,1)]*length+[(0,1)]*(length+1),100+len(cr),extras)
    adj,raw,vl,vr,hh=cc.component(length,bits,v,True)
    row=dict(word=word,right_length=length,selection_secondA_leftA_rightA=bits,variables=v.tolist(),adjusted_component=float(adj[0]),raw_defects=raw[0].tolist(),V_exit=float(vl[0]),V_entry=float(vr[0]),endpoint_heights=hh[0].tolist(),iterations=opt.nit,optimizer_success=bool(opt.success))
    cr.append(row);print('COMPONENT',len(cr),json.dumps(row),flush=True)
 assert len(br)==15 and len(cr)==30
 out=dict(scope='Bounded floating diagnostics of an EXPLICIT finite A_theta^[3] function; no connector maximization or difference of lower maxima. Critical references are actual periodic solutions. Candidate maxima are not upper bounds, and no universal Bellman or source inequality is asserted.',theta=THETA,reference_data=refs,bellman_cases=br,component_cases=cr,bellman_jobs=len(br),component_jobs=len(cr),maximum_bellman=max(br,key=lambda x:x['original_w_residual']),maximum_component=max(cr,key=lambda x:x['adjusted_component']),elapsed_seconds=time.time()-start)
 OUT.write_text(json.dumps(out,indent=2)+'\n');print('DONE maxima',out['maximum_bellman']['original_w_residual'],out['maximum_component']['adjusted_component'],flush=True)
if __name__=='__main__':main()
