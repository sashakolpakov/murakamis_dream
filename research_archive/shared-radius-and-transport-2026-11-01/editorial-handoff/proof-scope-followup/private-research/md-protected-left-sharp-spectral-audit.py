#!/usr/bin/env python3
"""Exact finite algebra checks for the protected original LEFT coefficient.

The original bidiagonal Casimir is powered to construct its full polynomial
resolvent numerator. Only afterward is that result compared with the unique
path, Laurent factorization, node normals, sewn equation, and inverse.
These finite checks do not prove the uniform inequalities or a source gap.
Requires SymPy; no repository or private-module imports.
"""
from pathlib import Path
from collections import Counter, defaultdict
from math import comb
import argparse
import hashlib
import json
import sympy as sp

if not __debug__:
    raise SystemExit('Do not run with -O')


def level(N):
    r,z=sp.symbols('r z')
    field=sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2*N,r),0))
    q,zero,one=field.unit,field.zero,field.one
    d,m=N-1,N//2
    nodes=[q**(2*j+1)+q**(-2*j-1) for j in range(N)]
    sq=[2-q**(2*j)-q**(-2*j) for j in range(N+1)]
    sprod=[one]
    for j in range(1,N):sprod.append(sprod[-1]*sq[j])
    C=[[zero for j in range(N)] for i in range(N)]
    for j in range(N):
        C[j][j]=nodes[j]
        if j:C[j-1][j]=-sq[j]
    identity=[[one if i==j else zero for j in range(N)] for i in range(N)]
    powers=[identity]
    for k in range(N):
        old=powers[-1]
        powers.append([[sum((old[i][a]*C[a][j] for a in range(N)),zero)
                        for j in range(N)] for i in range(N)])
    chi=sp.Poly(2*sp.chebyshevt(N,z/2)+2,z)
    h=[field.convert(chi.nth(k)) for k in range(N+1)]
    # Construct [V_N(sigma;C)]_0j by polynomial functional calculus.
    direct=[]
    for j in range(N):
        direct.append([sum((h[k]*powers[k-l-1][0][j] for k in range(l+1,N+1)),zero)
                       for l in range(N)])

    def mul(a,b):
        ans=[zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):ans[i+j]+=x*y
        return ans
    def ev(a,x):
        out=zero
        for v in a[::-1]:out=out*x+v
        return out
    def der(a):return [field.convert(k)*a[k] for k in range(1,len(a))]
    def pad(a):return a+[zero]*(N-len(a))
    def pair(a,b):return sum((a[k]*b[d-k] for k in range(N)),zero)
    def Dop(a,sigma):
        return [(sigma-nodes[k])*a[k]+(sq[k]*a[k-1] if k else zero) for k in range(N)]
    counts=Counter()
    for j in range(N):
        product=[field.convert((-1)**j)*sprod[j]]
        for k in range(j+1,N):product=mul(product,[-nodes[k],one])
        assert direct[j]==pad(product)
        counts['original_resolvent_path_coefficients']+=1
    for j in range(m):
        poly=direct[j]
        lhs=defaultdict(lambda:zero)
        for k,a in enumerate(poly):
            for b in range(k+1):lhs[k-2*b]+=a*field.convert(comb(k,b))
        n=N-2*j-2
        B=[one]
        for k in range(n):B=mul(B,[q**(2*k-n+1),one])
        T=[one]
        for k in range(1,N):T.append(T[-1]*(q**k-q**(-k)))
        assert B==[T[n]/(T[k]*T[n-k]) for k in range(n+1)]
        rhs=defaultdict(lambda:zero)
        for k,a in enumerate(B):
            for offset in (0,N):rhs[k+j+1-N+offset]+=field.convert((-1)**j)*sprod[j]*a
        assert {k:v for k,v in lhs.items() if v}=={k:v for k,v in rhs.items() if v}
        counts['exact_Laurent_factorizations']+=1
        for a in range(m):
            assert not ev(poly,nodes[a])
            derivative=ev(der(poly),nodes[a])
            expected=zero
            if a<=j:
                expected=field.convert((-1)**j)*sprod[j]
                for k in range(j+1,N):
                    if k!=d-a:expected*=nodes[a]-nodes[k]
            assert derivative==expected
            counts['paired_node_value_and_normal_checks']+=1
        if N%2:
            assert not ev(poly,field.convert(-2))
            normal=field.convert((-1)**j)*sprod[j]
            for k in range(j+1,N):
                if k!=m:normal*=-2-nodes[k]
            assert ev(der(poly),field.convert(-2))==normal and normal
            counts['odd_simple_value_and_normal_checks']+=1
    UM=field.convert((-1)**(m-1))*ev(direct[m-1],field.convert(2))
    assert sq[m]*UM==field.convert(4*N)
    if N%2==0:assert UM==field.convert(N)
    else:assert UM*sq[m]==field.convert(4*N)
    counts['both_parity_endpoint_current']+=1
    # Original polynomial values, compared to the independently assembled
    # q-shift operator and paired against a full degree-d spectator.
    B=[field.convert((k+1)**2+(-1)**k) for k in range(N)]
    for sigma in (field.convert(-2),zero,field.convert(2),nodes[0]):
        G=[ev(direct[j],sigma) if j<m else zero for j in range(N)]
        shift=[sigma*G[k]-q*Qpow*G[k]-q**(-1)/Qpow*G[k]
               for k,Qpow in enumerate(q**(2*k) for k in range(N))]
        for k in range(1,N):
            shift[k]+=(2-q**(2*k)-q**(-2*k))*G[k-1]
        assert shift==Dop(G,sigma)
        rhs=[zero]*N;rhs[0]=ev(h,sigma);rhs[m]+=sq[m]*G[m-1]
        assert shift==rhs
        assert pair(shift,B)==pair(G,Dop(B,sigma))
        assert pair(G,Dop(B,sigma))==ev(h,sigma)*B[d]+sq[m]*G[m-1]*B[d-m]
        counts['q_difference_and_sewn_current_checks']+=1
    # Independent forward triangular inversion of D_2.
    inverse=[]
    for i in range(N):
        col=[]
        for k in range(N):
            col.append(((one if k==i else zero)-(sq[k]*col[-1] if k else zero))/(2-nodes[k]))
        inverse.append(col)
        assert Dop(col,field.convert(2))==[one if k==i else zero for k in range(N)]
    assert inverse[0][d]==field.convert((-1)**d*N*N)/4
    for i in range(N):
        for k in range(i,N):
            v=one
            for a in range(i+1,k+1):v*=-sq[a]
            for a in range(i,k+1):v/=2-nodes[a]
            assert inverse[i][k]==v
            counts['inverse_entries']+=1
    assert inverse[0][d]*2**d==field.convert((-1)**d*N*N*2**d)/4
    counts['exact_expanding_radius_entry']+=1
    return dict(counts)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('md-protected-left-sharp-spectral-audit-results.json'))
    args=parser.parse_args()
    results={str(N):level(N) for N in range(2,9)}
    totals=Counter()
    for row in results.values():totals.update(row)
    out={'status':'verified','levels':results,'counts':dict(totals),
         'scope':'Exact finite algebra in cyclotomic fields: original matrix-power numerator versus path and Laurent identities, both normal types, sewn q-difference currents, and inverse entries. No numerical rate samples; no source-gap or volume claim.',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'levels':[2,8],'counts':out['counts'],'output':str(args.output)},indent=2))
if __name__=='__main__':main()
