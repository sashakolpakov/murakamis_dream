"""Local floating original-phase helpers; diagnostic arithmetic only.

Formulas are extracted unchanged from the archived phase and A3 drivers.
No optimizer or proof/certificate implementation is imported.
"""
import numpy as np
from scipy.special import spence

PI=np.pi
THETA=.5

def g(z):
 z=np.asarray(z,dtype=complex)
 return (spence(1-np.exp(-2j*PI*z))-PI*PI/6)/(2j*PI)

def phase(a,b,eta,eps):
 a,b=np.broadcast_arrays(np.asarray(a,dtype=complex),np.asarray(b,dtype=complex))
 p,q=1/np.tan(PI*a),1/np.tan(PI*b)
 if not eps:
  c=p+q;d=-1+1j*(q-p);disc=np.sqrt(c*c-4*d)
  roots=np.stack(((-c+disc)/2,(-c-disc)/2),axis=-1)
 else:
  comp=np.zeros(a.shape+(3,3),dtype=complex)
  comp[...,0,0]=-(p+q+1j)
  comp[...,0,1]=-(p*q+1j*(p+q))
  comp[...,0,2]=-(1j*p*q-2j*(p-1j)*(q+1j))
  comp[...,1,0]=1;comp[...,2,1]=1
  roots=np.linalg.eigvals(comp)
 selected=(roots.real>0)&(abs(roots.imag)<1)
 assert np.all(selected.sum(axis=-1)==1),(a,b,roots)
 cot=np.take_along_axis(roots,selected.argmax(axis=-1)[...,None],axis=-1)[...,0]
 s=np.log((cot+1j)/(cot-1j))/(2j*PI)
 gp=lambda z:np.log(1-np.exp(-2j*PI*z))
 value=g(s+a)+g(s+b)-(2+eps)*g(s)+2j*PI*a*s-(1+eta/2)*g(a)-(1+eps/2)*g(b)
 grad=np.stack((gp(s+a)+2j*PI*s-(1+eta/2)*gp(a),gp(s+b)-(1+eps/2)*gp(b)),axis=-1)
 assert np.isfinite(value).all() and np.isfinite(grad).all()
 return value,grad

class Candidate:
 def __init__(self,word,ref):
  self.word=tuple(word);self.ref=np.asarray(ref,dtype=complex);self.m=len(word)
  self.base={j:phase(self.r(j-1),self.r(j),self.t(j-1),self.t(j)) for j in range(self.m)}
 def t(self,j):return self.word[j%self.m]
 def r(self,j):return self.ref[j%self.m]
 def om(self,j,x,s):
  return np.minimum(1,s+400*(np.clip(x,.22,.45)-self.r(j).real)**2)/4000+.1*np.maximum(x-.45,0)
 def target(self,j,left,x,right,selected):
  left,x,right=np.broadcast_arrays(left,x,right);b=.12 if selected else .22
  R=np.where(x<=.45,1,400*(.5-x)**2)
  fraction=np.minimum(np.clip((left-.1)/(b-.1),0,1),np.minimum(np.clip((x-.1)/(b-.1),0,1),np.clip((right-.1)/(b-.1),0,1)))
  h=(.014 if selected else self.r(j).imag)*R*fraction
  return x+1j*h
 def w(self,j,x,sig,details=False):
  x=np.asarray(x).reshape(-1,4)
  z=[self.target(j-1,x[:,0],x[:,1],x[:,2],sig[1]),self.target(j,x[:,1],x[:,2],x[:,3],sig[2])]
  f,gr=self.base[j%self.m]
  gamma=f+gr[0]*(z[0]-self.r(j-1))+gr[1]*(z[1]-self.r(j))
  val=(phase(z[0],z[1],self.t(j-1),self.t(j))[0]-gamma).real
  for k,col in enumerate((1,2)):
   val+=.5*sig[col]*np.maximum(g(z[k]).real,-2*PI*z[k].imag)
  share=.5*(self.om(j-1,x[:,1],sig[1])+self.om(j,x[:,2],sig[2]))
  return (val,share) if details else val+THETA*share
 def V(self,i,x,sig):
  x=np.asarray(x).reshape(-1,3);n=len(x)
  allx=np.column_stack((np.broadcast_to([self.r(j).real for j in range(i-5,i-2)],(n,3)),x))
  alls=(0,0,0,*sig)
  return sum((self.w(i-3+k,allx[:,k:k+4],alls[k:k+4]) for k in range(3)),np.zeros(n))
 def E3(self,i,x,sig):
  x=np.asarray(x).reshape(-1,3);n=len(x)
  allx=np.column_stack((x,np.broadcast_to([self.r(j).real for j in range(i+1,i+4)],(n,3))))
  alls=(*sig,0,0,0)
  return sum((self.w(i+k,allx[:,k:k+4],alls[k:k+4]) for k in range(3)),np.zeros(n))
 def reference_residual(self):
  residual=np.zeros(self.m,dtype=complex)
  for j in range(self.m):
   gr=self.base[j][1];residual[(j-1)%self.m]+=gr[0];residual[j]+=gr[1]
  return float(np.max(np.abs(residual)))
