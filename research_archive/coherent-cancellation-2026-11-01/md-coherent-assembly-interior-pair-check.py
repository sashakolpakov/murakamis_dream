#!/usr/bin/env python3
"""Bounded finite source checks for the interior-spectrum paired-reference obstruction.

Exact finite-field polynomial face operators are compared with the continuant
and its two recurrences. Numerical ratios only check transcription of a proved
all-level inequality; they do not establish asymptotics or a filling bound.
"""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as sp
import mpmath as mp

if not __debug__:
    raise SystemExit("Assertions must be enabled.")

def chi(N):
    a,b=[2],[0,1]
    for _ in range(2,N+1):
        c=[0]+b
        for j,v in enumerate(a):c[j]-=v
        a,b=b,c
    b=b[:];b[0]+=2
    return b

def quotient(poly,t,p):
    out=[poly[-1]%p]
    for v in reversed(poly[1:-1]):out.append((v+t*out[-1])%p)
    return list(reversed(out))

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c

def evaluate(a,x,p):
    v=0
    for b in reversed(a):v=(v*x+b)%p
    return v

counts=dict(face_coefficients=0,cap_coefficients=0,contiguity=0,
            reference_recurrences=0,normal_reductions=0,odd_simple_values=0)
records=[]
for N in [4,5,6,7,8,12,16,32]:
    p=2*N+1
    while not sp.isprime(p):p+=2*N
    q=pow(int(sp.primitive_root(p)),(p-1)//(2*N),p)
    assert pow(q,N,p)==p-1
    d=N-1;m=N//2;M=m-1
    cc=[(pow(q,2*r+1,p)+pow(q,-2*r-1,p))%p for r in range(N)]
    aa=[(2+x)%p for x in cc]
    be=[(2-pow(q,2*r,p)-pow(q,-2*r,p))%p for r in range(N)]
    ee=[(q+pow(q,-1,p)-pow(q,2*r-1,p)-pow(q,-2*r+1,p))%p for r in range(N)]
    assert 8*p*p<np.iinfo(np.int64).max
    def matrix_source(sigma,cap=False):
        # Original Omega=-T in the monomial basis. For the central coupon
        # outer faces are (A,1); for the cap they are (0,C).
        V=np.zeros((N,N,N),dtype=np.int64)
        for coef in reversed(quotient(chi(N),sigma,p)):
            W=V*np.array(cc,dtype=np.int64)[None,:,None]
            if not cap:
                W[:,:-1,:]-=V[:,1:,:]*np.array(be[1:])[None,:,None]
            W[1:,:-1,:]-=V[:-1,1:,:]*np.array(be[1:])[None,:,None]
            if not cap:
                W[1:,:-2,:]-=V[:-1,2:,:]*np.array(ee[2:])[None,:,None]
            W[0]+=int(coef)*np.eye(N,dtype=np.int64)
            V=W%p
        return V
    full=matrix_source(-2)
    cap0=matrix_source(0,cap=True)
    capminus=matrix_source(-2,cap=True)
    K=[[1],[be[1],be[1]]]
    for r in range(2,N):
        row=[0]*(r+1)
        for j,v in enumerate(K[-1]):
            row[j]=(row[j]+be[r]*v)%p
            row[j+1]=(row[j+1]+be[r]*v)%p
        for j,v in enumerate(K[-2]):
            row[j+1]=(row[j+1]+ee[r]*aa[r-1]*v)%p
        K.append(row)
    def product(values):
        out=1
        for x in values:out=out*x%p
        return out
    def C(j,h):
        if j<0 or h<0 or j+h>d:return 0
        return K[d-h][j]*product(aa[d-h+1:])%p
    def directC(j,h):
        return (-1)**d*int(full[j,0,d-h])%p
    for h in range(M+1):
        for j in range(d-h+1):
            assert directC(j,h)==C(j,h)
            counts["face_coefficients"]+=1
    B=[1]
    for j in range(1,N):B.append(B[-1]*be[j]%p)
    for j in range(M+1):
        b0=B[j]*product([-c%p for c in cc[j+1:]])%p
        assert int(cap0[j,d-j,d])==(-1)**j*b0%p
        counts["cap_coefficients"]+=1
    limit=min(M,7*N//32)
    previous=previousD=0
    for ell in range(limit+1):
        direct=sum(int(cap0[j,d-j,d])*directC(j,ell-j)
                   for j in range(ell+1))%p
        assert (-cc[ell]*direct+be[ell]*previous-
                evaluate(chi(N),0,p)*C(0,ell))%p==0
        counts["contiguity"]+=1
        previous=direct
        if N%2==0:
            D=sum((-1)**d*int(capminus[j,d-j,d])*directC(j,ell-j)
                  for j in range(ell+1))%p
            assert (aa[ell]*D-be[ell]*previousD-4*C(0,ell))%p==0
            previousD=D;counts["reference_recurrences"]+=1
        # Build the actual cap polynomial before specializing sigma.
        T=[0]*N
        for j in range(ell+1):
            term=[1]
            for c in cc[j+1:]:term=mul(term,[-c%p,1],p)
            scale=(-1)**j*B[j]*directC(j,ell-j)%p
            for k,v in enumerate(term):T[k]=(T[k]+scale*v)%p
        derivative=[k*T[k]%p for k in range(1,N)]
        for a in range(m):
            assert evaluate(T,cc[a],p)==0
            if a>ell:
                assert evaluate(derivative,cc[a],p)==0
                counts["normal_reductions"]+=1
        if N%2:
            assert evaluate(T,-2,p)==0
            counts["odd_simple_values"]+=1
    records.append({"N":N,"prime":p,"root":q,"demand_range":[0,limit]})

mp.mp.dps=100
numerical=[]
for N in [32,64,96,128]:
    d=N-1;m=N//2;ell=7*N//32;theta=mp.pi/N
    c=[2*mp.cos((2*r+1)*theta) for r in range(N)]
    a=[2+x for x in c];s=[2*mp.sin(r*theta) for r in range(N)]
    K=[[mp.mpf(1)],[s[1]**2,s[1]**2]]
    for r in range(2,N):
        row=[mp.mpf(0)]*(r+1)
        for j,v in enumerate(K[-1]):
            row[j]+=s[r]**2*v;row[j+1]+=s[r]**2*v
        for j,v in enumerate(K[-2]):row[j+1]+=s[r]*s[r-1]*a[r-1]*v
        K.append(row)
    def C(j,h):return K[d-h][j]*mp.fprod(a[d-h+1:])
    raw=mp.mpf(0);reference=mp.mpf(0);B=mp.mpf(1)
    for j in range(ell+1):
        if j:B*=s[j]**2
        raw+=(-1)**j*B*mp.fprod(-x for x in c[j+1:])*C(j,ell-j)
        reference+=B*mp.fprod(a[j+1:])*C(j,ell-j)
    rho=mp.tan(7*mp.pi/32)**4;tau=5*mp.sqrt(5)-10
    bound=(1-rho)*tau**(mp.mpf(3)*N/160-1)
    ratio=abs(raw)/reference
    assert raw<0 and ratio>=bound
    numerical.append({"N":N,"demand":ell,"ratio":mp.nstr(ratio,20),
                      "proved_lower_bound":mp.nstr(bound,20),
                      "log_ratio_per_N":mp.nstr(mp.log(ratio)/N,20)})

x=(5-sp.sqrt(5))/8
assert sp.simplify(2*x*x/((1-x)*(1-2*x))-(5*sp.sqrt(5)-10))==0
result={
 "scope":__doc__.strip(),"counts":counts,"exact_fields":records,
 "numerical_diagnostics_only":numerical,
 "excluded":["all-level proof from samples","physical closure of an exterior",
             "bound on actual filled period","odd-level exponential obstruction"],
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "sympy_version":sp.__version__,"numpy_version":np.__version__,
 "mpmath_version":mp.__version__}
out=Path("/private/tmp/md-coherent-assembly-interior-pair-check-results.json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"counts":counts,"output":str(out)},indent=2))
