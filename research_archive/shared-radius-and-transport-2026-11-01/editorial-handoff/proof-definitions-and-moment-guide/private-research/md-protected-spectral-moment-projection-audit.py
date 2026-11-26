#!/usr/bin/env python3
"""Exact bounded algebra checks for the separated spectral projections.

The tests compare original unused-row products with the two phase-retaining
factors, and direct monomial projections with the terminating product formula.
They do not test or prove a bound for the coupled Hankel dual norm.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sympy as sp


def check(N):
    r = sp.Symbol('r')
    F = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(4*N,r),0))
    root, one, zero = F.unit, F.one, F.zero
    q, Q, imag = root**2, root**4, root**N
    d, M = N-1, N//2-1
    def sin_half(k): return (root**k-root**(-k))/(2*imag)
    def prod(seq):
        out = one
        for x in seq: out *= x
        return out
    moments = [one]
    for j in range(1,2*M+1):
        moments.append(moments[-1]*sin_half(2*j)/sin_half(2*j+1))
    polys=[]
    counts=Counter()
    for n in range(M+1):
        p=[one]
        for j in range(n):
            p.append(-p[-1]*sin_half(2*n+2*j+1)*sin_half(2*n-2*j)
                     /sin_half(2*j+2)**2)
        polys.append(p)
        norm=sum((a*b*moments[i+j] for i,a in enumerate(p)
                  for j,b in enumerate(p)),zero)
        assert norm == sin_half(1)/sin_half(4*n+1)
        counts['direct_single_factor_norms']+=1
        for k in range(n):
            assert sum((a*moments[j+k] for j,a in enumerate(p)),zero)==zero
            counts['direct_single_factor_orthogonality']+=1
    nodes=[q**(2*j+1)+q**(-2*j-1) for j in range(N)]
    Ssquare=[one]
    for j in range(1,N): Ssquare.append(Ssquare[-1]*(2-q**(2*j)-q**(-2*j)))
    U0=one/sin_half(1)**2
    for ell in sorted(set((0,1,N//2))):
        w=q**(2*ell)
        sigma=w+one/w
        vectors={}
        for eps in (1,-1):
            C=F.convert((-1)**ell)*sin_half(1)/sin_half(1+2*eps*ell)
            v=[]
            for j in range(M+1):
                v.append(C*q**(-eps*j*ell)
                         *prod(sin_half(2*k)/sin_half(2*k+1+2*eps*ell)
                               for k in range(1,j+1)))
            vectors[eps]=v
            for n,p in enumerate(polys):
                direct=sum((a*v[j] for j,a in enumerate(p)),zero)
                claimed=C*(q*Q**n)**n*prod(1-Q**(1-n+k)*w**eps for k in range(n))\
                                      /prod(1-q*Q**(k+1)*w**eps for k in range(n))
                assert direct==claimed
                counts['direct_versus_terminating_projections']+=1
        for j in range(M+1):
            original=Ssquare[j]*prod(sigma-nodes[k] for k in range(j+1,N))/U0
            assert vectors[1][j]*vectors[-1][j]==original
            counts['original_unused_row_spectral_factorizations']+=1
    return dict(counts)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('md-protected-spectral-moment-projection-results.json'))
    args=parser.parse_args()
    if not __debug__: raise SystemExit('Do not run with -O')
    levels=(4,5,6,7,8)
    cases={str(N):check(N) for N in levels}
    result={'status':'passed','levels':list(levels),'checks':cases,
            'arithmetic':'exact cyclotomic fields of order 4N',
            'scope':'Finite source factorization, direct orthogonality/norms, and terminating projection identities at both parities.',
            'limits':'No numerical evidence is used for the proved exponential limitation. No coupled kappa bound, spectator-energy bound, or knot-volume claim is tested.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','levels':list(levels),'output':str(args.output)}))


if __name__=='__main__':main()
