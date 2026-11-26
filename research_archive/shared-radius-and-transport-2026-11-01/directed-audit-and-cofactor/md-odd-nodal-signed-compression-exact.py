#!/usr/bin/env python3
"""Bounded exact checks of the original cofactor nodal decomposition.

The all-level positivity and coefficientwise mass bound are proved in the
companion note. This executes exact cyclotomic polynomial identities only;
no fit, sampled norm, or finite calculation is an asymptotic proof.
"""
from pathlib import Path
import json, hashlib, argparse
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path('/private/tmp/md-odd-nodal-signed-compression-exact-results.json'))
args=parser.parse_args()

class Field:
    def __init__(self,N):
        self.N=N; self.z=sp.Symbol('z')
        self.mod=sp.Poly(sp.cyclotomic_poly(2*N,self.z),self.z,domain=sp.QQ)
        self.zero=self.red(0); self.one=self.red(1)
        self.q=[self.red(self.z**k) for k in range(2*N)]
    def red(self,x):
        if isinstance(x,sp.Poly):return x.rem(self.mod)
        return sp.Poly(x,self.z,domain=sp.QQ).rem(self.mod)
    def mul(self,x,y):return (x*y).rem(self.mod)
    def inv(self,x):return sp.invert(x,self.mod)
    def div(self,x,y):return self.mul(x,self.inv(y))
    def cos2(self,k):return self.q[k%(2*self.N)]+self.q[-k%(2*self.N)]
    def sin2(self,k):return self.red(2)-self.cos2(2*k)
    def pair(self,i,j):return self.cos2(i-j)-self.cos2(i+j)

def check(N):
    f=Field(N); m=N//2
    one={(0,0,0):f.one}; B={(1,0,0):f.one}; A={(0,1,0):f.one}; P={(0,0,1):f.one}
    def add(*ps):
        out={}
        for p in ps:
            for k,v in p.items():out[k]=f.red(out.get(k,f.zero)+v)
        return {k:v for k,v in out.items() if not v.is_zero}
    def scale(p,c):return {k:f.mul(v,c) for k,v in p.items() if not f.mul(v,c).is_zero}
    def mul(p,q):
        out={}
        for k,v in p.items():
            for l,w in q.items():
                t=tuple(k[i]+l[i] for i in range(3))
                out[t]=f.red(out.get(t,f.zero)+f.mul(v,w))
        return {k:v for k,v in out.items() if not v.is_zero}
    def shift_b(p,j):return {(k[0]+j,k[1],k[2]):v for k,v in p.items()}
    def equal(p,q):return not add(p,scale(q,f.red(-1)))
    aa=[f.red(2)+f.cos2(2*j+1) for j in range(m+1)]
    def source(u):
        rows=[one]; prod=f.one
        for j in range(1,m+1):
            prod=f.mul(prod,aa[j-1]+u)
            v=add(shift_b(scale(one,prod),j),scale(mul(A,rows[-1]),f.sin2(j)))
            if j>=2:v=add(v,scale(mul(P,rows[-2]),f.mul(f.pair(j,j-1),aa[j-1]+u)))
            rows.append(v)
        return rows
    # Independently form the leading-principal endpoint determinant by
    # its Hermitian tridiagonal determinant recursion, without source R.
    dets=[one]
    for n in range(1,m+1):
        diag=f.div(f.red(2),f.mul(f.cos2(n-1),f.cos2(n)))
        v=mul(add(B,scale(A,diag)),dets[-1])
        if n>=2:
            j=n-1
            beta=f.div(f.sin2(j),f.mul(f.mul(f.cos2(j),f.cos2(j)),f.pair(2*j-1,2*j+1)))
            # beta is B_j/4, since s_j^2=4sin^2 and
            # pair(2j-1,2j+1)=4sin((2j-1)theta)sin((2j+1)theta).
            correction=add(scale(mul(A,A),-beta),scale(P,f.mul(beta,f.mul(f.cos2(j),f.cos2(j)))))
            v=add(v,mul(correction,dets[-2]))
        dets.append(v)
    endpoint=source(f.zero)
    assert equal(endpoint[m],scale(dets[m],f.red(N))),('endpoint determinant',N)
    assembled={}; scalar_sum=f.zero; nodal_identities=0
    for k in range(1,m+1):
        a=m-k; u=-aa[a]; rows=source(u)
        prefix=f.one
        for r in range(a):prefix=f.mul(prefix,aa[r]-aa[a])
        assert equal(rows[a],scale(dets[a],prefix)),('principal determinant',N,k)
        tails=[one]
        for n in range(1,m-a+1):
            j=a+n
            v=scale(mul(A,tails[-1]),f.sin2(j))
            if n>=2:v=add(v,scale(mul(P,tails[-2]),f.mul(f.pair(j,j-1),aa[j-1]-aa[a])))
            tails.append(v)
            assert equal(rows[j],mul(rows[a],v)),('tail factor',N,k,j)
            nodal_identities+=1
        weight=f.cos2(k) if k%2 else -f.cos2(k)
        assembled=add(assembled,scale(rows[m-1],weight));scalar_sum+=weight
        # Independently evaluate the cardinal weight using the node product.
        derivative=f.one
        for r in range(m):
            if r!=a:derivative=f.mul(derivative,aa[r]-aa[a])
        cardinal=f.div(f.red(N),f.mul(aa[a],derivative))
        assert f.red(cardinal-weight).is_zero,('cardinal weight',N,k)
    assert f.red(scalar_sum-1).is_zero,('constant interpolation',N)
    assert equal(assembled,endpoint[m-1]),('original D reconstruction',N)
    return {'N':N,'field_order':2*N,'principal_determinants':m,'factorizations':nodal_identities,
            'exact_cardinal_weights':m,'D_polynomial_reconstructed':True,
            'checked_D_coefficients':len(endpoint[m-1]),'endpoint_G_identity':True}

rows=[check(N) for N in (3,5,7,9,11)]
out={'scope':'Exact finite polynomial identities at five odd levels. All-level positivity, mass inequalities, and asymptotic implications are not inferred from these checks.',
     'source':'Original row-replacement recurrence; independent tridiagonal endpoint determinant recurrence; independent product cardinal weights.',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows}
args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
