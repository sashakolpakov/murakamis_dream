import sys,itertools,json
sys.path.insert(0,'/Users/sasha/volume-conjecture/experiments')
import numpy as np
from audit_actual_simultaneous_small_circle_face_correspondence import Local,morse_faces,setup,local_polynomials,mul,substitute,scalar,physical_colors,apply_pair
from audit_actual_small_circle_polynomial_face_insertion import insertions
from audit_actual_signed_small_circle_face_kernel import kernel_poly
from audit_actual_braided_two_cut_source_adapter import original_crossings

def one_kernel(loc,h,eps):
 out=[]
 for j in range(loc.N):
  P=insertions({(0,j,0):1},0,1,2,loc)[h]
  if eps:P=kernel_poly(P,0,1,2,loc,eps)
  for (a,i,b),v in P.items():
   assert i+a+b==j and min(a,i,b)>=0
   out.append((j,a,i,b,v))
 return out

def case(N,boxes,ports,hs,epss,marked=1,k=2):
 loc=Local(N);p,q,d=loc.p,loc.q,loc.d
 ch=morse_faces(k,boxes,marked);nf=ch['faces']
 edges=[(ch['circles'][e][1],ch['circles'][e][2],e) for e in ports]
 M=d//2;D,F=local_polynomials(loc,M);P={(0,)*nf:1};coupons=[];signs=[]
 for e,(x,b,c,y) in enumerate(ch['circles']):
  eps=(-1,0,1)[e%3];signs.append(eps)
  if e in ports:coupons.append(None);continue
  for fac,ids in ((D,(x,b,y)),(D,(x,c,y)),(F,(x,y))):P=mul(P,substitute(fac,ids,list(range(nf)),p),p)
  coupons.append(loc.h0[M]*pow(loc.omega[M],eps,p)*(loc.W[M][0]@loc.pi[M][0]%p)%p)
 kernel={(0,)*nf:1}
 for par,child,e in edges:
  x,_,_,y=ch['circles'][e];local={}
  for j,a,i,b,v in one_kernel(loc,hs[ports.index(e)],epss[ports.index(e)]):
   n=[0]*nf;n[child]-=j;n[par]+=i;n[x]+=a;n[y]+=b;n=tuple(n)
   local[n]=(local.get(n,0)+v)%p
  kernel=mul(kernel,local,p)
 indegree=[0]*nf
 for par,child,e in edges:indegree[child]+=1
 target=[d*((f not in (0,ch['v']))-indegree[f]) for f in range(nf)]
 coeff=0;terms=0
 for ex,v in kernel.items():
  n=tuple(t-e for t,e in zip(target,ex))
  if n in P:coeff=(coeff+v*P[n])%p;terms+=1
 lam=pow(loc.eta,d*d,p)
 pref=pow(N,len(boxes)-len(ports),p)*scalar(loc,[M]*(len(boxes)-len(ports)),[e for ii,e in enumerate(signs) if ii not in ports])*pow(lam,sum(epss),p)%p
 predicted=pref*coeff%p
 state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
 marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
 for jj in range(k):
  state=np.kron(state,loc.cup[0].reshape(-1))%p
  mark=np.kron(mark,(marker if jj==marked else loc.cap[0]).reshape(-1))%p
 state=state.reshape((N,)*(2*k));colors=physical_colors(loc);_,_,_,Rs=original_crossings(N)
 for e,slot in enumerate(boxes):
  if e in ports:
   j=ports.index(e);coupon=colors[hs[j]]
   if epss[j]:coupon=coupon@Rs[0 if epss[j]>0 else 1][0]%p
  else:coupon=coupons[e]
  state=apply_pair(coupon,state,slot,N,p)
 actual=int(mark@state.reshape(-1)%p)
 assert predicted==actual,(N,boxes,ports,hs,epss,marked,predicted,actual)
 return dict(N=N,ports=ports,h=hs,eps=epss,mark=marked,actual=actual,terms=terms,kernel_terms=len(kernel),P_terms=len(P))

if __name__=='__main__':
 rows=[]
 for N in (3,4,5,6):
  for marked in (0,1):
   for ports,hs in (([0,2],[2,2]),([0,3],[1,1]),([0,1,3],[1,2,1]),([0,1,2,3],[1,1,1,1])):
    for epss in (([1]*len(ports)),([-1 if j%2 else 1 for j in range(len(ports))]),([0]*len(ports))):
     rows.append(case(N,[1,0,2,1],ports,hs,epss,marked))
 print(json.dumps(dict(status='PASS',cases=len(rows),nonzero=sum(r['actual']!=0 for r in rows),rows=rows),indent=2))
