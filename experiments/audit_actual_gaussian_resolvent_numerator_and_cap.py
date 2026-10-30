#!/usr/bin/env python3
"""Exact original Gaussian-resolvent numerator checks; no asymptotic test."""
import sys,json,argparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as sp
import numpy as np
import mpmath as mp
from audit_actual_small_circle_polynomial_face_insertion import Local,physical_colors

def paths(N,j):
 def rec(i,edges,visited):
  yield i,edges,visited
  if i>=1:yield from rec(i-1,edges+[(i,1)],visited+[i-1])
  if i>=2:yield from rec(i-2,edges+[(i,2)],visited+[i-2])
 yield from rec(j,[],[j])

def finite_H(loc,z):
 p,q,Q,N=loc.p,loc.q,loc.Q,loc.N
 cs=[(q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
 bs=[(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]
 es=[(q+pow(q,-1,p)-q*pow(Q,-j,p)-pow(q,-1,p)*pow(Q,j,p))%p for j in range(N)]
 out={}
 for j in range(N):
  for i,edges,vis in paths(N,j):
   pol={(0,0):1}
   for v,s in edges:
    nxt={}
    terms=[((1,0),-bs[v]),((0,1),-bs[v])] if s==1 else [((1,1),-es[v])]
    for ex,a in pol.items():
     for inc,b in terms:
      key=(ex[0]+inc[0],ex[1]+inc[1]);nxt[key]=(nxt.get(key,0)+a*b)%p
    pol=nxt
   factor=1
   for v in range(N):
    if v not in vis:factor=factor*(z-cs[v])%p
   for (a,b),v in pol.items():
    ex=(a,i,N-1-j,b);out[ex]=(out.get(ex,0)+factor*v)%p
 return {ex:v for ex,v in out.items() if v}

def run():
 z,s=sp.symbols('z s');symbolic=0
 for N in range(2,19):
  chi=2*sp.chebyshevt(N,z/2)+2
  V=sp.div(chi-chi.subs(z,-2),z+2,z)[0]
  Fej=sp.div(sp.chebyshevt(N,-z/2)-1,-z/2-1,z)[0]
  assert sp.expand((-1)**(N-1)*V-Fej)==0
  L=lambda h:(-1)**(h-1)*sp.chebyshevu(h-1,z/2)
  assert sp.expand(Fej-L(N)-2*sum(L(h) for h in range(1,N)))==0
  assert sp.expand(Fej-N-2*sum((N-j)*sp.chebyshevt(j,-z/2) for j in range(1,N)))==0
  divided=sp.div(chi-chi.subs(z,s),z-s,z)[0]
  assert sp.expand((-1)**(N-1)*divided-L(N)-2*sum(sp.chebyshevt(N-h,-s/2)*L(h) for h in range(1,N)))==0
  if N%2==0:assert sp.expand(-V-(2-z)*sp.chebyshevu(N//2-1,z/2)**2)==0
  symbolic+=4+(N%2==0)
 entries=wrong=0
 for N in range(3,8):
  loc=Local(N);p=loc.p;Omega=(-physical_colors(loc)[2])%p
  coefficients=[int(c)%p for c in sp.Poly(2*sp.chebyshevt(N,z/2)+2,z).all_coeffs()]
  powers=[np.eye(N*N,dtype=np.int64)]
  for _ in range(N-1):powers.append(powers[-1]@Omega%p)
  for zz in (0,2,5,11):
   H=finite_H(loc,zz);op=np.zeros_like(Omega)
   for pos,a in enumerate(coefficients[:-1]):
    degree=N-pos
    for r in range(degree):op=(op+a*pow(zz,degree-1-r,p)*powers[r])%p
   for u in range(N):
    for v in range(N):
     x=-loc.q*pow(loc.Q,u,p)%p;y=-pow(loc.q,-1,p)*pow(loc.Q,-v,p)%p
     for r in range(N):
      s=(u+v-r)%N;delta=r-u;c=pow(loc.Q,-delta,p)
      value=sum(a*pow(x,k,p)*pow(c,t,p)*pow(y,l,p) for (k,i,t,l),a in H.items())%p
      pred=value*pow(N,-1,p)*pow(loc.q,-loc.d*delta,p)*pow(c,-loc.d,p)%p
      assert pred==int(op[r*N+s,u*N+v]),(N,zz,u,v,r,s)
      entries+=1;wrong+=r+s!=u+v
 mp.mp.dps=60;positive=majorants=0;max_error=mp.mpf(0)
 for N in range(3,14):
  th=mp.pi/N;cs=[2*mp.cos((2*j+1)*th) for j in range(N)]
  bs=[4*mp.sin(j*th)**2 for j in range(N)]
  es=[4*mp.sin(j*th)*mp.sin((j-1)*th) for j in range(N)]
  sigma=-2+mp.mpc('.03','.04');radius=abs(sigma+2)
  for j in range(N):
   for i,edges,vis in paths(N,j):
    weight=mp.mpf(1)
    for v,s in edges:weight*=bs[v] if s==1 else es[v]
    bound=weight;actual=weight
    for v in range(N):
     if v not in vis:bound*=2+cs[v]+radius;actual*=sigma-cs[v]
    assert bound>=0
    assert abs(actual)<=bound*(1+mp.mpf('1e-50'))
    positive+=1;majorants+=1
  # Original diagonal entry of the full polynomial numerator, exact parity.
  for uu in (mp.mpf(0),mp.mpf(1)/N**4):
   eta=mp.acosh(1+uu/2)
   numerator=2*mp.cosh(N*eta)+2*(-1)**N
   prod=mp.fprod(2+uu+cc for cc in cs)
   max_error=max(max_error,abs(prod-numerator))
   assert abs(prod-numerator)<mp.mpf('1e-45')
 return dict(status='PASS',symbolic_identities=symbolic,
             original_coproduct_grid_entries=entries,wrong_unwrapped_total_entries=wrong,
             nonnegative_actual_paths=positive,complex_factorwise_majorants=majorants,
             max_diagonal_product_error=str(max_error),
             scope='Exact source numerator, positivity and elementary identities only; no asymptotic/cycle test.')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(Path(__file__).with_name('actual_gaussian_resolvent_numerator_and_cap_results.json')));args=ap.parse_args()
 result=run();Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
