#!/usr/bin/env python3
"""Exact-field original cap/CROSS contiguity and cutoff-flux audit.
Finite source-identity checks do not replace the analytic all-demand bound.
"""
import sys,json,argparse
from pathlib import Path
import numpy as np
SCRIPT_DIR=Path(__file__).resolve().parent
sys.path.insert(0,str(SCRIPT_DIR))
from audit_actual_small_circle_polynomial_face_insertion import Local,casimir
from original_source_tensor import apply_pair

def chi(N):
 a=[2];b=[0,1]
 for j in range(2,N+1):
  c=[0]+b
  for k,v in enumerate(a):c[k]-=v
  a,b=b,c
 b=b[:];b[0]+=2;return b

def quotient(c,s):
 out=[c[-1]]
 for v in reversed(c[1:-1]):out.append(v+s*out[-1])
 assert c[0]+s*out[-1]==sum(v*s**j for j,v in enumerate(c))
 return list(reversed(out))

def matpoly(c,A,p):
 I=np.eye(len(A),dtype=np.int64);B=np.zeros_like(A)
 for v in reversed(c):B=(B@A+int(v%p)*I)%p
 return B

def run():
 counts={'levels':0,'original_projected_flux':0,'literal_contiguity':0,'original_physical_three_port_scalars':0,'full_source_recurrences':0,'low_original_projected_identifications':0,'newton_resolvent_entries':0}
 for N in range(3,11):
  l=Local(N);p,q,d=l.p,l.q,N-1;M=N//2-1;H=d//2;counts['levels']+=1
  # Every NumPy multiplication is reduced modulo p before the next.
  # The largest dot-product dimension is N^4 (the final physical closure).
  assert (N**4+N**2+2)*(p-1)**2 < np.iinfo(np.int64).max
  O=casimir(l);I=np.eye(N*N,dtype=np.int64);E=matpoly(quotient(chi(N),-2),O,p);F=matpoly(quotient(chi(N),2),O,p)
  assert np.array_equal(E,E.T)
  cc=[(pow(q,2*r+1,p)+pow(q,-2*r-1,p))%p for r in range(N)]
  a=[(2+v)%p for v in cc];ga=[(2-v)%p for v in cc]
  be=[(2-pow(q,2*r,p)-pow(q,-2*r,p))%p for r in range(N)]
  ep=lambda r:(q+pow(q,-1,p)-pow(q,2*r-1,p)-pow(q,-2*r+1,p))%p
  K=[[1],[be[1],be[1]]]
  for r in range(2,N):
   row=[0]*(r+1)
   for j,v in enumerate(K[-1]):row[j]=(row[j]+be[r]*v)%p;row[j+1]=(row[j+1]+be[r]*v)%p
   for j,v in enumerate(K[-2]):row[j+1]=(row[j+1]+ep(r)*a[r-1]*v)%p
   K.append(row)
  def prod(v):
   z=1
   for t in v:z=z*int(t)%p
   return z
  def C(j,h):return K[d-h][j]*prod(a[d-h+1:])%p
  U=[4*pow(ga[0],-1,p)%p]
  for j in range(1,N):U.append(U[-1]*be[j]*pow(ga[j],-1,p)%p)
  V=[prod(be[1:j+1])*prod(a[j+1:])%p for j in range(N)]
  Z=np.diag(cc).astype(np.int64)
  for j in range(1,N):Z[j,j-1]=-be[j]%p
  FZ=matpoly(quotient(chi(N),2),Z,p)
  w=np.array(V,dtype=np.int64)@FZ%p
  prev=0
  prev_projected=0
  sums=[]
  for n in range(N):
   S=sum((-1)**j*U[j]*C(j,n-j) for j in range(n+1))%p;sums.append(S)
   assert (ga[n]*S+be[n]*prev-4*C(0,n))%p==0
   assert S==int(w[d-n]);assert C(0,n)==V[d-n]
   counts['full_source_recurrences']+=1;counts['newton_resolvent_entries']+=1;prev=S
   # Keep BOTH original half-block cutoffs.  The auxiliary full slice
   # is identified with this projected source only in the low range.
   J_n=range(max(0,n-H),min(M,n)+1)
   projected=0
   for j in J_n:
    h=n-j
    assert 0<=j<=M and 0<=h<=H and j+h==n
    assert M+1<=d-h<=d and j<=d-h
    projected=(projected+(-1)**j*U[j]*C(j,h))%p
   for j in range(n):
    h=n-j
    assert (be[j+1]*C(j+1,h-1)-(cc[j]-cc[n])*C(j,h)-be[n]*C(j,h-1))%p==0,(N,n,j)
    counts['literal_contiguity']+=1
   if n<=M:
    flux=4*C(0,n)
   elif n==H:
    flux=4*C(0,n)-ga[M+1]*(-1)**(M+1)*U[M+1]*C(M+1,n-M-1)
   else:
    L=n-H
    left=(-1)**(L-1)*U[L-1]*C(L-1,H+1)
    right=(-1)**(M+1)*U[M+1]*C(M+1,n-M-1)
    flux=(ga[L-1]-ga[n])*left-ga[M+1]*right
   assert (ga[n]*projected+be[n]*prev_projected-flux)%p==0,(N,n)
   counts['original_projected_flux']+=1
   prev_projected=projected
   if n<=M:
    assert list(J_n)==list(range(n+1))
    assert projected==S,(N,n,projected,S)
    counts['low_original_projected_identifications']+=1
  state0=np.kron(l.cup[0].reshape(-1),l.cup[0].reshape(-1)).reshape((N,)*4)%p
  mark=np.array([[pow(l.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
  boundary=np.kron(mark.reshape(-1),l.cap[0].reshape(-1))%p
  G=I.copy();P2=1
  for n in range(N):
   if n:G=((O-cc[n-1]*I)@G)%p;P2=P2*be[n]%p
   state=apply_pair(E,state0,1,N,p);state=apply_pair(F,state,0,N,p);state=apply_pair(G,state,1,N,p)
   actual=int(boundary@state.reshape(-1)%p)
   expected=(-1)**(d+n)*P2*sums[n]%p
   assert actual==expected,(N,n,actual,expected)
   counts['original_physical_three_port_scalars']+=1
 return {'status':'PASS','scope':'Exact all-parity original-demand contiguity and both cutoff fluxes, with physical/Newton checks; no asymptotic estimate inferred.','counts':counts}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(SCRIPT_DIR/'research_cap_cross_all_demand_subexponential_contraction_results.json'));ar=ap.parse_args();result=run();Path(ar.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
