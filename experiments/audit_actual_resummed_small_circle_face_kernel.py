#!/usr/bin/env python3
"""Exact resummed kernel formulas against the public homogeneous helper.

These are recurrence/formula checks. Original matrix and whole-source
validation are supplied separately by the homogeneous-source audit.
Asymptotic profiles below are diagnostic; the note proves the edge limit.
"""
import argparse
import json
import math
from pathlib import Path
import mpmath as mp
from audit_actual_homogeneous_casimir_face_source import homogeneous
from audit_actual_small_circle_polynomial_face_insertion import Local

def tilings(lo,hi):
 if lo>hi:yield [];return
 for tail in tilings(lo+1,hi):yield tail
 if lo<hi:
  for tail in tilings(lo+2,hi):yield [lo+1]+tail

def run(output):
 counts=dict(full_resolvent_coefficients=0,boundary_fourier_coefficients=0,unique_path_coefficients=0)
 for N in range(3,10):
  loc=Local(N);p,q,d=loc.p,loc.q,loc.d;imag=pow(loc.eta,N,p)
  sn=lambda j:imag*(pow(q,-j,p)-pow(q,j,p))%p
  S=[1]
  for j in range(1,N):S.append(S[-1]*sn(j)%p)
  choose=lambda a,b:S[a]*pow(S[b]*S[a-b],-1,p)%p if 0<=b<=a else 0
  H=[{}]+[homogeneous(loc,h,0) for h in range(1,N+1)]
  for j in range(N):
   for r in range(j+1):
    prod=pow(S[j]*pow(S[j-r],-1,p),2,p)
    for h in range(1,N+1):
     n=h-1-r
     if n<0:pred=0
     else:
      pred=prod*pow(-1,n,p)*sum(choose(r+v,v)*choose(r+n-v,n-v)*pow(q,(2*j-r+1)*(2*v-n),p) for v in range(n+1))%p
     actual=H[h].get((r,j-r,d-j,0),0)
     assert pred==actual,(N,h,j,r,pred,actual)
     counts['boundary_fourier_coefficients']+=1
     if r==h-1:counts['unique_path_coefficients']+=1
    for a in range(r+1):
     beta=r-a;series=[0]*N
     for dims in tilings(j-r+1,j):
      ell=len(dims)
      if ell>min(a,beta):continue
      w=prod*math.comb(r-2*ell,a-ell)%p
      for k in dims:w=w*pow(sn(k)*sn(k-1),-1,p)%p
      shift=r-ell
      g=[1]+[0]*(N-1)
      for v in range(j-r,j+1):
       if v in [k-1 for k in dims]:continue
       cv=(pow(q,2*v+1,p)+pow(q,-2*v-1,p))%p
       f=[]
       for n in range(N):f.append((g[n]-(cv*f[n-1] if n else 0)-(f[n-2] if n>1 else 0))%p)
       g=f
      for n in range(shift,N):series[n]=(series[n]+w*g[n-shift])%p
     for h in range(1,N+1):
      actual=H[h].get((a,j-r,d-j,beta),0)
      assert series[h-1]==actual,(N,h,j,a,beta,series[h-1],actual)
      counts['full_resolvent_coefficients']+=1
 mp.mp.dps=70
 diagnostics=[]
 for N in (16,32,64,128,256,512,1024):
  m=N//4;Sm=mp.fprod(2*mp.sin(mp.pi*j/N) for j in range(1,m+1))
  g=N*mp.sqrt(mp.mpf(N)/2)/Sm**2
  diagnostics.append(dict(N=N,normalized_edge_log_rate=float(mp.log(g)/N)))
 out=dict(status='PASS',counts=counts,asymptotic_diagnostics=diagnostics,limit=float(mp.catalan/mp.pi),scope='Exact resummed homogeneous-kernel formulas, not a global source bound.')
 output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_resummed_small_circle_face_kernel_results.json'))
 args=parser.parse_args()
 run(args.output)
