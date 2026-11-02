#!/usr/bin/env python3
"""Exact finite-field checks of the polynomial identities used in Sections 2–4.
These checks do not test the analytic inequalities or the asymptotic theorem.
"""
from __future__ import annotations
import argparse, hashlib, json, math, random
from pathlib import Path


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def add(a, b, p):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return trim([x % p for x in c])

def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] = (c[i+j] + x*y) % p
    return trim(c)

def scale(a, x, p): return trim([v*x % p for v in a])

def remainder(a, b, p):
    a = a.copy()
    while len(a) >= len(b):
        j, v = len(a)-len(b), a[-1] * pow(b[-1], -1, p) % p
        for i, x in enumerate(b): a[i+j] = (a[i+j] - v*x) % p
        trim(a)
    return a

def coeff(a, i): return a[i] if i < len(a) else 0

def prime(p): return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))

def field(N):
    p = 4*N + 1
    while not prime(p): p += 4*N
    factors = [d for d in range(2,p) if (p-1)%d == 0 and prime(d)]
    g = next(g for g in range(2,p) if all(pow(g,(p-1)//d,p)!=1 for d in factors))
    return p, pow(g,(p-1)//(2*N),p), pow(g,(p-1)//4,p)

def laurent(a, p):
    out = {}
    for j, v in enumerate(a):
        for r in range(j+1):
            k = j-2*r
            out[k] = (out.get(k,0) + v*(-1)**j*math.comb(j,r)) % p
    return out

def cheb(N, p):
    a,b=[2],[0,1]
    for _ in range(1,N): a,b=b,add(mul([0,1],b,p),scale(a,-1,p),p)
    return b

def U(j, x, p):
    a,b=1,2*x%p
    if j==0:return a
    for _ in range(1,j): a,b=b,(2*x*b-a)%p
    return b

def run():
    counts=dict(levels=0,newton_laurent_coefficients=0,full_fourier_traces=0,
                dual_pairings=0,fusion_identities=0,odd_cardinal_identities=0)
    rng=random.Random(730519)
    for N in range(2,13):
        p,q,ii=field(N); d=N-1; m=d//2; counts['levels']+=1
        S=[1]
        for r in range(1,N): S.append(S[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(ii,-1,p)%p)
        e=[[1]]
        for r in range(1,N):
            c=(pow(q,2*r-1,p)+pow(q,-(2*r-1),p))%p
            e.append(scale(mul(e[-1],[c,-1],p),pow((S[r]*pow(S[r-1],-1,p))**2,-1,p),p))
        for r in range(N):
            A=laurent(e[r],p)
            for k in range(-r,r+1):
                if r<=m:
                    expected=S[2*r]*pow(S[r]**2*S[r+k]*S[r-k],-1,p)%p
                elif abs(k)<N-r: expected=0
                else: expected=(-1)**(r-abs(k))*S[2*r-N]*pow(S[r]**2*S[abs(k)-(N-r)]*S[r-abs(k)],-1,p)%p
                assert A.get(k,0)==expected%p,(N,r,k)
                counts['newton_laurent_coefficients']+=1
        T=cheb(N,p)
        def phi(F,x):
            P=T.copy();P[0]=(P[0]+2*x)%p
            return (-1)**d*N*N*coeff(remainder(F,P,p),d)%p
        polynomials=[mul(e[i],e[j],p) for i in range(N) for j in range(N)]
        for _ in range(24):
            F=[1]
            for _ in range(rng.randrange(3,8)): F=mul(F,e[rng.randrange(N)],p)
            polynomials.append(F)
        for F in polynomials:
            A=laurent(F,p)
            for x in [0,1,p-1,2,3]:
                rhs=sum((-1)**((N+1)*(l+1))*(A.get(l*N-1,0)-A.get(l*N+1,0))*U(l-1,x,p) for l in range(1,(len(F)+1)//N+2))*N*N%p
                assert phi(F,x)==rhs,(N,len(F),x)
                counts['full_fourier_traces']+=1
        for i in range(N):
            for j in range(N):
                for x in [1,p-1,2]:
                    assert phi(mul(e[i],e[j],p),x)==int(i+j==d)
                    counts['dual_pairings']+=1
        for _ in range(12):
            A=[rng.randrange(p) for _ in range(N)]
            B=[rng.randrange(p) for _ in range(N)]
            rhs=sum(phi(mul(A,e[i],p),1)*phi(mul(e[d-i],B,p),1) for i in range(N))%p
            assert rhs==phi(mul(A,B,p),1)
            counts['fusion_identities']+=1
        if N%2:
            for r in range(N):
                assert phi(mul(mul(e[m],e[m],p),e[r],p),1)==sum(a*pow(-2,j,p) for j,a in enumerate(e[r]))%p
                counts['odd_cardinal_identities']+=1
    return counts

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'build/check')
    args=ap.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    dest=args.output/'summary.json';dest.unlink(missing_ok=True)
    if not __debug__: raise SystemExit('This exact checker requires assertions; do not use -O.')
    base=Path(__file__).resolve().parent
    inputs=sorted(list(base.glob('*.tex'))+list((base/'figures').glob('*.tex'))+[Path(__file__).resolve()])
    hashes={str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    counts=run()
    assert hashes=={str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'inputs changed during check'
    data={'scope':'Exact polynomial quotient, Fourier coefficient, reflected Newton support, full metric and odd projector identities at N=2,...,12. No analytic inequality, uniform rate, contour or volume proof is inferred.','checks':counts,'source_sha256':hashes}
    dest.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');print(json.dumps(counts,sort_keys=True))
if __name__=='__main__':main()
