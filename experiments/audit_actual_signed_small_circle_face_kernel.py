#!/usr/bin/env python3
"""Actual R face kernel, full signed sources, and explicit norm bounds.

Original balanced crossings supply the source side independently of the
Casimir polynomial. All level carries, endpoints and Cartan phases remain.
"""
import argparse
import itertools
import json
from pathlib import Path
import sympy as sp
from audit_actual_small_circle_polynomial_face_insertion import Local,physical_colors
from audit_actual_braided_two_cut_source_adapter import original_crossings

def symbolic():
 q,I,K,L=sp.symbols('q I K L',nonzero=True);Q=q*q;J=I*K*L
 c=lambda Z:q*Z+1/(q*Z)
 b=lambda Z:2-Z-1/Z
 e=lambda Z:q+1/q-q/Z-Z/q
 lhs=c(I)-b(Q*I)*q*I*(2-K-L)/(1-Q*I)-e(Q*Q*I)*Q*Q*I*I*(1-K)*(1-L)/((1-Q*I)*(1-Q*Q*I))
 rhs=c(J)+b(J)/q*(2-K-L)/(1-J)-e(J)/Q*(1-K)*(1-L)/((1-J)*(1-J/Q))
 assert sp.factor(lhs-rhs)==0
 return 1

def calc(loc,j,x,c,y,eps):
 p,q,Q=loc.p,loc.q,loc.Q;period,j0=divmod(j,loc.N)
 if eps<0:q=pow(q,-1,p);Q=pow(Q,-1,p)
 fac=[1]
 for n in range(1,loc.N):fac.append(fac[-1]*(1-pow(Q,n,p))%p)
 val=0
 for i in range(j0+1):
  for k in range(j0-i+1):
   l=j0-i-k
   coeff=pow(-1,j0,p)*pow(q,j0+i*i,p)*fac[j0]*pow(fac[i]*fac[k]*fac[l],-1,p)%p
   val+=coeff*pow(c,i+period*loc.N,p)*pow(x,k,p)*pow(y,l,p)
 return val%p

def local_paths():
 count=high=0
 for N in range(3,11):
  loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
  _,_,_,Rs=original_crossings(N)
  lam=pow(loc.eta,d*d,p)
  for eps,R in zip((1,-1),Rs):
   for u,v in itertools.product(range(N),repeat=2):
    x=-q*pow(Q,u,p)%p;y=-pow(q,-1,p)*pow(Q,-v,p)%p
    for j in list(range(N))+[N,N+1,2*N+1]:
     actual=0
     for r in range(max(0,u+v-d),min(d,u+v)+1):
      step=r-u
      actual+=int(R[0][r*N+u+v-r,u*N+v])*pow(q,d*step,p)*pow(Q,-step*j,p)
     predicted=pow(lam,eps,p)*calc(loc,j,x,1,y,eps)%p
     assert actual%p==predicted,(N,u,v,j,eps,actual%p,predicted)
     count+=1;high+=u+v>d
 return dict(status='PASS',symbolic=symbolic(),actual_original_crossing_monomial_paths=count,high_totals=high)

def kernel_poly(poly,x,c,y,loc,eps):
 p,q,Q=loc.p,loc.q,loc.Q
 if eps<0:q=pow(q,-1,p);Q=pow(Q,-1,p)
 fac=[1]
 for n in range(1,loc.N):fac.append(fac[-1]*(1-pow(Q,n,p))%p)
 out={}
 for n,weight in poly.items():
  j=n[c]%loc.N
  for i in range(j+1):
   for k in range(j-i+1):
    l=j-i-k
    coeff=pow(-1,j,p)*pow(q,j+i*i,p)*fac[j]*pow(fac[i]*fac[k]*fac[l],-1,p)%p
    nn=list(n);nn[c]-=j-i;nn[x]+=k;nn[y]+=l;nn=tuple(nn)
    out[nn]=(out.get(nn,0)+weight*coeff)%p
 return {n:a for n,a in out.items() if a}

def whole():
 import numpy as np
 from audit_actual_small_circle_polynomial_face_insertion import morse_faces,local_polynomials,mul,substitute,insertions,merge,scalar,apply_pair
 count=nonzero=highpowers=targetzeros=0
 for N in range(3,8):
  loc=Local(N);p=loc.p;d=loc.d
  _,_,_,Rs=original_crossings(N);lam=pow(loc.eta,d*d,p)
  fixtures=[([1,0,2,1],1,1),([1,0,2,1],2,0)]
  if N in (3,5):fixtures.append(([1,0,1,0,2,1],1,1))
  for boxes,port,marked in fixtures:
   chart=morse_faces(2,boxes,marked);variables=list(range(chart['faces']))
   x,b,c,y=chart['circles'][port]
   for labels in ([d//2]*len(boxes),[j%(d//2+1) for j in range(len(boxes))]):
    poly={(0,)*len(variables):1};coupons=[];signs=[]
    for ii,((xx,bb,cc,yy),a) in enumerate(zip(chart['circles'],labels)):
     ee=(-1,0,1)[ii%3];signs.append(ee)
     if ii==port:coupons.append(None);continue
     D,F=local_polynomials(loc,a)
     for fac,ids in ((D,(xx,bb,yy)),(D,(xx,cc,yy)),(F,(xx,yy))):
      poly=mul(poly,substitute(fac,ids,variables,p),p)
      # The longer fixture uses the actual zero target on protected faces.
      # No operator lowers those exponents, since its middle c is unmarked.
      if len(boxes)>4:poly={n:v for n,v in poly.items() if n[0]==n[chart['v']]==0}
     coupons.append(loc.h0[a]*pow(loc.omega[a],ee,p)*(loc.W[a][0]@loc.pi[a][0]%p)%p)
    highpowers+=sum(n[c]>=N for n in poly)
    seq=insertions(poly,x,c,y,loc);colors=physical_colors(loc)
    high_input={n:v for n,v in poly.items() if n[c]>=N}
    high_seq=insertions(high_input,x,c,y,loc) if high_input else None
    reps=[f for f in variables if f!=c];target=tuple(0 if f in (0,chart['v']) else d for f in reps)
    pref=pow(N,len(boxes)-1,p)*scalar(loc,[a for ii,a in enumerate(labels) if ii!=port],[e for ii,e in enumerate(signs) if ii!=port])%p
    state0=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
    for jj in range(2):
     state0=np.kron(state0,loc.cup[0].reshape(-1))%p
     mark=np.kron(mark,(marker if jj==marked else loc.cap[0]).reshape(-1))%p
    for eps,R in zip((1,-1),Rs):
     for h in sorted(set((1,2,N))):
      out=merge(kernel_poly(seq[h],x,c,y,loc,eps),b,c,p)
      predicted=pref*pow(lam,eps,p)*out.get(target,0)%p
      if high_seq is not None:
       discarded=merge(kernel_poly(high_seq[h],x,c,y,loc,eps),b,c,p)
       assert discarded.get(target,0)==0
       assert all(n[reps.index(b)]>=N for n in discarded)
       targetzeros+=1
      mat=colors[h]@R[0]%p;state=state0.reshape((N,)*4)
      for ii,slot in enumerate(boxes):state=apply_pair(mat if ii==port else coupons[ii],state,slot,N,p)
      actual=int(mark@state.reshape(-1)%p)
      assert actual==predicted,(N,port,marked,labels,eps,h,actual,predicted)
      count+=1;nonzero+=actual!=0
 return dict(full_original_signed_sources=count,nonzero_sources=nonzero,
             unmerged_input_monomials_above_first_period=highpowers,
             exact_discarded_block_target_zeros=targetzeros)

def polynomial_blocks():
 import numpy as np
 count=0
 for N in range(3,16):
  loc=Local(N);p,q,Q=loc.p,loc.q,loc.Q
  C=np.zeros((N,N),dtype=np.int64)
  for j in range(N):
   Z=pow(Q,j,p)
   C[j,j]=(q*Z+pow(q*Z,-1,p))%p
   if j:C[j-1,j]=-(2-Z-pow(Z,-1,p))*5%p
   if j>1:C[j-2,j]=-(q+pow(q,-1,p)-q*pow(Z,-1,p)-pow(q,-1,p)*Z)*6%p
  I=np.eye(N,dtype=np.int64)
  A,B=2*I,C.copy()
  for _ in range(1,N):A,B=B,(C@B-A)%p
  assert np.array_equal((B+2*I)%p,np.zeros_like(I))
  RR=[]
  for eps in (1,-1):
   R=np.zeros_like(C)
   for j in range(N):
    poly=kernel_poly({(0,j,0):1},0,1,2,loc,eps)
    for n,v in poly.items():R[n[1],j]=(R[n[1],j]+v*pow(2,n[0],p)*pow(3,n[2],p))%p
   assert np.array_equal(C@R%p,R@C%p)
   RR.append(R)
  assert np.array_equal(RR[0]@RR[1]%p,I)
  # Independently sum the positive Newton basis with its original phases.
  S=[1]
  imag=pow(loc.eta,N,p)
  for j in range(1,N):S.append(S[-1]*(pow(q,j,p)-pow(q,-j,p))*pow(imag,-1,p)%p)
  H=I.copy();RP=I.copy();RM=I.copy()
  for r in range(1,N):
   node=(pow(q,2*r-1,p)+pow(q,-2*r+1,p))%p
   H=((node*I-C)@H)%p
   normalized=H*pow(S[r]*S[r],-1,p)%p
   RP=(RP+pow(-q,r,p)*normalized)%p
   RM=(RM+pow(-pow(q,-1,p),r,p)*normalized)%p
  assert np.array_equal(RP,RR[0]) and np.array_equal(RM,RR[1])
  count+=1
 return dict(full_blocks=count,annihilators=count,original_phase_newton_expansions=2*count,
             inverse_and_commuting_block_relations=3*count)

def norm_checks():
 import mpmath as mp
 mp.mp.dps=80
 coeffs=transfers=0;worst=mp.mpf(0)
 for N in (5,6,9,10,15,16):
  q=mp.exp(mp.pi*1j/N);Q=q*q
  F=[mp.mpc(1)];S=[mp.mpf(1)]
  for j in range(1,N):
   F.append(F[-1]*(1-Q**j));S.append(S[-1]*2*mp.sin(mp.pi*j/N))
  for j in range(N):
   for i in range(j+1):
    for k in range(j-i+1):
     l=j-i-k;actual=abs(q**(j+i*i)*F[j]/(F[i]*F[k]*F[l]))
     expected=S[j]/(S[i]*S[k]*S[l])
     err=abs(actual-expected)/(1+expected);worst=max(worst,err)
     assert err<mp.mpf('1e-70');coeffs+=1
   for x,b,y in ((mp.mpf('.2'),mp.mpf('1.3'),mp.mpf('.7')),
                 (mp.mpf(2),mp.mpf(1),mp.mpf(3))):
    for block in (0,1,2):
     output=mp.mpf(0)
     for i in range(j+1):
      for k in range(j-i+1):
       l=j-i-k
       output+=S[j]/(S[i]*S[k]*S[l])*b**(i+block*N)*x**k*y**l
     input_weight=(b+x+y)**(j+block*N)
     assert output<=input_weight*(1+mp.mpf('1e-70'));transfers+=1
 obstruction=[]
 for N in (32,33,64,65,128,129):
  a=N//4;j=3*a
  logS=lambda n:sum(mp.log(2*mp.sin(mp.pi*k/N)) for k in range(1,n+1))
  obstruction.append(dict(N=N,j=j,coefficient_log_per_N=str((logS(j)-3*logS(a))/N)))
 # The equal-radius constant uses the absolute source triangle rate.
 # These are constant/finite-source normalization checks, not a numerical
 # proof of the uniform capacity criterion.
 from audit_actual_positive_face_channel_rate import continuants
 lob=lambda t:-mp.quad(lambda u:mp.log(abs(2*mp.sin(u))),[0,t])
 Fstar=3*(lob(mp.pi/6)+lob(mp.pi/3))/mp.pi
 Gstar=4*lob(mp.pi/4)/mp.pi
 profiles=[]
 for N in (16,17,32,33):
  S=[mp.mpf(1)]
  for j in range(1,N):S.append(S[-1]*2*mp.sin(mp.pi*j/N))
  K=mp.mpf(1)
  for j in range(N):
   value=sum(S[j]/(S[i]*S[k]*S[j-i-k]) for i in range(j+1) for k in range(j-i+1))
   K=max(K,value)
  D=continuants(N,(N-1)//2,mp.mpf(1),mp.mpf(1),mp.mpf(1))[-1]
  profiles.append(dict(N=N,original_two_D_minus_exact_kernel_log_per_N=str((2*mp.log(D)-mp.log(K))/N)))
 return dict(precision=80,original_q_coefficient_absolute_values=coeffs,
             split_radius_transfers=transfers,maximum_relative_error=str(worst),
             exponential_norm_values_diagnostic_only=obstruction,
             Fstar=str(Fstar),Gstar=str(Gstar),comparable_radius_threshold=str(mp.exp(2*Fstar-Gstar)),
             finite_original_determinant_gap_diagnostics=profiles)

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--output',default='experiments/actual_signed_small_circle_face_kernel_results.json')
 args=ap.parse_args()
 data=dict(status='PASS',symbolic_commutator=symbolic(),local=local_paths(),
           blocks=polynomial_blocks(),whole=whole(),norms=norm_checks(),
           scope='Original R and inverse, all polynomial degree blocks, true marked one-port signed sources and exact coefficient norms. No universal signed capacity gap or simultaneous signed norm theorem.')
 Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(data,indent=2))

if __name__=='__main__':main()
