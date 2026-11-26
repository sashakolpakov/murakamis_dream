#!/usr/bin/env python3
"""Exact omitted-half products and their charge modes; no period bound.

Integral arithmetic in Z[q]/Phi_(2N)(q), with q=exp(pi*i/N).
The independent input is the actual product over c_r-sigma.
"""
import argparse
import functools
import hashlib
import json
from pathlib import Path

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:
        a.pop()
    return a

def divide_monic(a,b):
    a=trim(a);b=trim(b)
    assert b[-1]==1
    out=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b);c=a[-1];out[k]=c
        for j,v in enumerate(b):
            a[j+k]-=c*v
        a=trim(a)
    assert a==[0]
    return trim(out)

@functools.lru_cache(None)
def cyclotomic(n):
    p=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            p=divide_monic(p,cyclotomic(d))
    return tuple(p)

class Ring:
    def __init__(self,n):
        self.order=2*n;self.mod=cyclotomic(self.order)
        self.degree=len(self.mod)-1
        self.zero=(0,)*self.degree
        self.one=(1,)+(0,)*(self.degree-1)
    def reduce(self,a):
        a=trim(a)
        for k in range(len(a)-1,self.degree-1,-1):
            c=a[k]
            if c:
                for j,v in enumerate(self.mod):
                    a[k-self.degree+j]-=c*v
        return tuple((a+[0]*self.degree)[:self.degree])
    def power(self,k):
        k%=self.order
        return self.reduce([0]*k+[1])
    def add(self,a,b):
        return tuple(x+y for x,y in zip(a,b))
    def mul(self,a,b):
        c=[0]*(2*self.degree-1)
        for j,x in enumerate(a):
            for k,y in enumerate(b):
                c[j+k]+=x*y
        return self.reduce(c)
    def scale(self,a,n):
        return tuple(n*x for x in a)

def run():
    counts={};levels=[]
    def check(name,condition):
        assert condition,name
        counts[name]=counts.get(name,0)+1
    for n in range(3,19):
        ring=Ring(n)
        def multiply(a,b):
            out={}
            for j,x in a.items():
                for k,y in b.items():
                    out[j+k]=ring.add(out.get(j+k,ring.zero),ring.mul(x,y))
            return {k:v for k,v in out.items() if v!=ring.zero}
        def product(indices):
            out={0:ring.one}
            for j in indices:
                c=ring.add(ring.power(2*j+1),ring.power(-2*j-1))
                out=multiply(out,{2:ring.one,-2:ring.one,0:c})
            return out
        left=product(range(n//2,n))
        right=product(range(0,n-n//2))
        if n%2==0:
            expected={n:ring.one,-n:ring.one}
        else:
            expected=multiply({1:ring.one,-1:ring.scale(ring.one,-1)},
                              {n:ring.one,-n:ring.scale(ring.one,-1)})
        check("literal_half_product_modes",left==expected)
        check("literal_reflected_half_product",left==right)
        val=ring.zero
        deriv2=ring.zero
        for k,v in left.items():
            val=ring.add(val,v)
            deriv2=ring.add(deriv2,ring.scale(v,k*(k-1)))
        if n%2:
            check("odd_complete_zero",val==ring.zero)
            # sigma=-(w^2+w^-2), so sigma''(1)=-8.
            # A_half''(1)=8N gives the exact spectral slope -N.
            check("odd_spectral_first_normal",
                  deriv2==ring.scale(ring.one,8*n))
        else:
            check("even_complete_value",val==ring.scale(ring.one,2))
        for ell in [-3,-2,-1,1,2,3]:
            for eps in [-1,1]:
                # Exponents in w=e^(i*pi*delta) are integers.
                check("half_charge_exponent",
                      2*n*ell+eps*n==n*(2*ell+eps))
                check("half_charge_is_not_integer",
                      (2*ell+eps)%2==1)
        levels.append(n)
    return {"levels":levels,"exact_ring":"Z[q]/Phi_(2N)(q)",
            "counts":counts,"total_checks":sum(counts.values()),
            "scope":"Finite identities only; no representation assignment, cancellation, or remainder bound."}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,
      default=Path("/private/tmp/md-filled-complement-half-charge-results.json"))
    args=p.parse_args()
    result=run()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
