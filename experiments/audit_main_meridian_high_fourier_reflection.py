#!/usr/bin/env python3
"""Exact finite checks; not a proof of a coupled geometric inequality."""
from collections import Counter
from pathlib import Path
import argparse,hashlib,json
import sympy as sp

def cheb(n,z):
 a,b=sp.Integer(2),z
 for _ in range(1,n):a,b=b,sp.expand(z*b-a)
 return b

def multiply(a,b,zero):
 out={}
 for i,x in a.items():
  for j,y in b.items():out[i+j]=out.get(i+j,zero)+x*y
 return {k:v for k,v in out.items() if v}

def check(N):
 z,D,x=sp.symbols('z D x')
 K=sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2*N,x),0))
 q,zero,one=K.unit,K.zero,K.one
 d=N-1;m=d//2
 T=[one];S2=[one];basis=[sp.Poly(1,z,D,domain=K)];fourier=[{0:one}]
 for n in range(1,N):
  den=2-q**(2*n)-q**(-2*n);c=q**(2*n-1)+q**(1-2*n)
  T.append(T[-1]*(q**n-q**(-n)));S2.append(S2[-1]*den)
  basis.append((basis[-1]*(sp.Poly(z,z,D,domain=K).neg()+sp.Poly(1,z,D,domain=K).mul_ground(c))).mul_ground(one/den))
  fourier.append({k:v/den for k,v in multiply(fourier[-1],{-1:one,0:c,1:one},zero).items()})
 p0=sp.Poly(cheb(N,z)+2,z,D,domain=K);ps=p0+sp.Poly(D,z,D,domain=K)
 def trace(poly,mod):
  result={}
  for (j,l),v in poly.rem(mod).rep.to_dict().items():
   if j==d:result[(0,l)]=K.convert((-1)**d*N*N)*v
  return sp.Poly.from_dict(result,(z,D),domain=K)
 counts=Counter()
 for h in range(m+1,N):
  a=N-h;t=2*h-N
  predicted={}
  for k in range(a,h+1):
   val=K.convert((-1)**k)*T[t]/(T[h]**2*T[k-a]*T[h-k])
   predicted[k]=predicted[-k]=val
  assert fourier[h]==predicted,(N,h,'high formula')
  counts['high_polynomials']+=1
  counts['zero_middle_coefficients']+=2*a-1
  for length in range(2,9):
   for low in sorted(set([0,max(0,m//2),m])):
    inds=[h]+[low]*length
    F=sp.Poly(1,z,D,domain=K);A={0:one}
    for i in inds:F=F*basis[i];A=multiply(A,fourier[i],zero)
    direct=trace(F,ps)-trace(F,p0)
    spectral=sp.Poly(0,z,D,domain=K)
    for ell in range(2,(sum(inds)+1)//N+1):
     tail=A.get(ell*N-1,zero)-A.get(ell*N+1,zero)
     multiplier=sp.chebyshevu(ell-1,1+D/2)-ell
     spectral+=sp.Poly(multiplier,z,D,domain=K).mul_ground(K.convert(N*N*(-1)**((N-1)*(ell+1)))*tail)
    assert direct==spectral,(N,inds,'difference aliases')
    counts['one_high_trace_differences']+=1
    counts['nonzero_differences']+=bool(direct)
    if sum(inds)<2*N-1:assert not direct
 # The derivative of P0 is zero at every repeated node, but its
 # top trace is nonzero: this checks full first-normal information.
 radical=p0.diff(z)
 for Bpoly in [basis[m],basis[m]**2+sp.Poly(z+1,z,D,domain=K),basis[d]+sp.Poly(2,z,D,domain=K)]:
  lhs=sp.Poly(0,z,D,domain=K)
  for i in range(N):lhs+=trace(radical*basis[i],p0)*trace(basis[d-i]*Bpoly,p0)
  assert lhs==trace(radical*Bpoly,p0),(N,'complete Frobenius fusion')
  counts['normal_sensitive_fusion_identities']+=1
 assert trace(radical,p0)==sp.Poly((-1)**d*N**3,z,D,domain=K)
 return {'N':N,'counts':dict(counts)}

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('high_fourier_reflection_results.json'))
args=parser.parse_args()
rows=[check(n) for n in range(2,13)]
counts=Counter()
for r in rows:counts.update(r['counts'])
record={'scope':'Exact high Laurent coefficients, first-alias cancellation in the trace difference, and complete Frobenius fusion with first normals. These finite checks do not prove the uniform inequalities or a volume theorem.','construction':'Newton product over Q[q]/Phi_(2N), independent monic quotient remainder, symbolic Delta','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'levels':rows,'counts':dict(counts),'result':'all exact checks passed'}
args.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record['counts']))
