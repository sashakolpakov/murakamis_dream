"""Finite diagnostic only. No identity or asymptotic claim follows from a fit."""
import numpy as np
from math import comb

def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v!=0}
def scale(p,c):return {k:c*v for k,v in p.items()}
def mul(p,q):
 out={}
 for (i,j,k),v in p.items():
  for (a,b,c),w in q.items():
   t=(i+a,j+b,k+c);out[t]=out.get(t,0)+v*w
 return out
one={(0,0,0):1.};B={(1,0,0):1.};A={(0,1,0):1.};P={(0,0,1):1.}
def power(p,n):
 q=one
 for _ in range(n):q=mul(q,p)
 return q

def instance(N):
 m=N//2;th=np.pi/N
 si=lambda j:2*np.sin(j*th)
 aa=lambda j:4*np.cos((j+.5)*th)**2
 dg=np.array([1/(np.cos(j*th)*np.cos((j+1)*th)) for j in range(m)])
 be=np.zeros(m)
 for j in range(1,m):be[j]=np.sin(j*th)**2/(np.cos(j*th)**2*np.sin((2*j-1)*th)*np.sin((2*j+1)*th))
 def interval(l,r):
  prev2={};prev=one
  for j in range(l,r):
   nxt=mul(add(B,scale(A,dg[j]/2)),prev)
   if j>l:nxt=add(nxt,mul(add(scale(power(A,2),-be[j]/4),scale(P,be[j]*np.cos(j*th)**2)),prev2))
   prev2,prev=prev,nxt
  return prev
 def real_chain(i,j):
  # Re product of [sqrt(beta)/2 (A sin + i D cos)], D=y-x.
  p={0:one}
  for n in range(i+1,j+1):
   nxt={}
   for k,z in p.items():
    nxt[k]=add(nxt.get(k,{}),scale(mul(z,A),np.sqrt(be[n])/2*np.sin(n*th)))
    nxt[k+1]=add(nxt.get(k+1,{}),scale(z,np.sqrt(be[n])/2*np.cos(n*th)))
   p=nxt
  out={}
  for k,z in p.items():
   if k%2==0:out=add(out,scale(mul(z,power(add(power(A,2),scale(P,-4)),k//2)),(-1)**(k//2)))
  return out
 labels=[];cols=[]
 for i in range(m):
  for j in range(i,m):
   labels.append((i,j));v=mul(interval(0,i),interval(j+1,m))
   if j>i:v=scale(mul(v,real_chain(i,j)),2*(-1)**(i+j))
   cols.append(v)
 r=[one]
 for j in range(1,m):
  v=add(scale(power(B,j),np.prod([aa(k) for k in range(j)])),scale(mul(A,r[j-1]),si(j)**2))
  if j>=2:v=add(v,scale(mul(P,r[j-2]),si(j)*si(j-1)*aa(j-1)))
  r.append(v)
 target=scale(r[-1],1/N)
 keys=sorted(set(target).union(*map(set,cols)))
 X=np.array([[c.get(k,0.) for c in cols] for k in keys]);y=np.array([target.get(k,0.) for k in keys])
 weights=np.maximum(abs(y),np.max(abs(X),axis=1));X=X/weights[:,None];y=y/weights
 def coords(W):return np.array([W[i,j] for i,j in labels])
 def fit(name,bs):
  Z=np.column_stack([coords(W) for W in bs]);q,_,rank,_=np.linalg.lstsq(X@Z,y,rcond=1e-13);v=Z@q
  W=np.zeros((m,m))
  for z,(i,j) in zip(v,labels):W[i,j]=W[j,i]=z
  print(N,name,'rank',rank,'res',np.max(abs(X@v-y)),'op',np.linalg.norm(W,2),'fro',np.linalg.norm(W),'eig',np.linalg.eigvalsh(W).round(6),flush=True)
  return W
 J=np.diag(dg)
 for j in range(1,m):J[j-1,j]=J[j,j-1]=np.sqrt(be[j])*np.sin(j*th)
 _,V=np.linalg.eigh(J)
 fit('commuteA',[np.outer(v,v) for v in V.T])
 H=np.diag(dg).astype(complex)
 for j in range(1,m):H[j-1,j]=np.sqrt(be[j])*(np.sin(j*th)+1j*np.cos(j*th));H[j,j-1]=H[j-1,j].conjugate()
 _,V=np.linalg.eigh(H)
 fit('realcommuteH',[np.outer(v,v.conjugate()).real for v in V.T])
 W=fit('full',[np.eye(m)[i:i+1].T@np.eye(m)[j:j+1]+(np.eye(m)[j:j+1].T@np.eye(m)[i:i+1] if i!=j else 0) for i,j in labels])
 if N<=9:print('W',W.round(8),flush=True)
 return W
if __name__=='__main__':
 for N in [5,7,9,11,13,17,21]:instance(N)
