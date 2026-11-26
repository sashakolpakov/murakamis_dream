#!/usr/bin/env python3
"""Exact finite checks for the fixed positive-end interval proof.

The original three-arrow Casimir is built first. Its full polynomial resolvent
numerator is computed by polynomial division and matrix powers; it is then
compared with the separately constructed interval Green expansion. Arithmetic
uses exact finite fields with q of order 2N. Symbolic checks retain independent
perturbations. These checks do not prove real inequalities or asymptotic gaps.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp


def field(N):
    p = int(sp.nextprime(10000))
    while (p - 1) % (2*N):
        p = int(sp.nextprime(p))
    q = pow(int(sp.primitive_root(p)), (p-1)//(2*N), p)
    assert all(pow(q, k, p) != 1 for k in sp.divisors(2*N)[:-1])
    return p, q


def add(a, b, p):
    return [( (a[k] if k < len(a) else 0)
             +(b[k] if k < len(b) else 0)) % p
            for k in range(max(len(a), len(b)))]


def mul(a, b, p):
    ans = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            ans[i+j] = (ans[i+j]+x*y) % p
    return ans


def matrix_powers(A, B, N, p):
    powers = [[np.eye(N,dtype=np.int64)]]
    for _ in range(N):
        old=powers[-1]
        new=[np.zeros((N,N),dtype=np.int64) for _ in range(len(old)+1)]
        for k,C in enumerate(old):
            new[k]=(new[k]+C@A) % p
            new[k+1]=(new[k+1]+C@B) % p
        powers.append(new)
    return powers


def run_level(N):
    p,q=field(N);d=N-1
    qp=lambda k:pow(q,k,p)
    c=[(qp(2*j+1)+qp(-2*j-1)) % p for j in range(N)]
    aa=[(2-qp(2*j)-qp(-2*j)) % p for j in range(N)]
    bb=[(qp(1)+qp(-1)-qp(2*j-1)-qp(-2*j+1)) % p for j in range(N)]
    for j in range(2,N):
        assert bb[j] and (c[0]-c[j-1]) % p == bb[j]
    A=np.zeros((N,N),dtype=np.int64);B=A.copy()
    for j in range(N):
        A[j,j]=c[j]
        if j:A[j-1,j]=B[j-1,j]=-aa[j] % p
        if j>=2:B[j-2,j]=-bb[j] % p
    powers=matrix_powers(A,B,N,p)
    z=sp.Symbol('z')
    chi=sp.Poly(2*sp.chebyshevt(N,z/2)+2,z)
    coeff=[int(chi.nth(k)) % p for k in range(N+1)]
    annihilator=[np.zeros_like(A) for _ in range(N+1)]
    for k in range(N+1):
        for e,C in enumerate(powers[k]):
            annihilator[e]=(annihilator[e]+coeff[k]*C) % p
    assert all(not np.any(C) for C in annihilator)
    tests=0;green_tests=0
    spectra=list(dict.fromkeys([2,c[0],(c[0]-1)%p,(c[0]+1)%p,0]))
    for sigma in spectra:
        f=[sum(coeff[k]*pow(sigma,k-1-r,p)
               for k in range(r+1,N+1)) % p for r in range(N)]
        V=[np.zeros_like(A) for _ in range(N)]
        for k in range(N):
            for e,C in enumerate(powers[k]):V[e]=(V[e]+f[k]*C) % p
        for i in range(N):
            hs=[[1]]
            if i<d:hs.append([1,1])
            for k in range(2,N-i):
                a=(c[0]-sigma)*pow(bb[i+k],-1,p) % p
                direct=add(mul([1,1],hs[-1],p),
                           [0]+[((a-1)*v)%p for v in hs[-2]],p)
                green=[1]*(k+1)
                for r in range(2,k+1):
                    ar=(c[0]-sigma)*pow(bb[i+r],-1,p) % p
                    part=mul([1]*(k-r+1),hs[r-2],p)
                    green=add(green,[0]+[(ar*v)%p for v in part],p)
                assert direct==green
                hs.append(direct);green_tests+=1
            for j in range(i,N):
                factor=pow(-1,j-i,p)
                for r in range(i+1,j+1):factor=factor*aa[r] % p
                for r in list(range(i))+list(range(j+1,N)):
                    factor=factor*(sigma-c[r]) % p
                h=hs[j-i]
                for e in range(N):
                    expected=(factor*h[e]) % p if e<len(h) else 0
                    assert int(V[e][i,j]) == expected,(N,sigma,i,j,e)
                    tests+=1
    return {'N':N,'prime':p,'q':q,'spectra':spectra,
            'full_numerator_coefficient_checks':tests,'green_checks':green_tests}


def symbolic():
    S=sp.Symbol('S');params=sp.symbols('a2:8');h=[sp.Integer(1),1+S]
    checks=0
    for k in range(2,8):
        value=sp.expand((1+S)*h[k-1]-S*h[k-2]+params[k-2]*S*h[k-2])
        green=sum(S**j for j in range(k+1))
        for r in range(2,k+1):
            green+=params[r-2]*S*sum(S**j for j in range(k-r+1))*h[r-2]
        assert sp.expand(value-green)==0
        # All coefficients in S and the independent perturbations are positive.
        assert all(v>0 for _,v in sp.Poly(value,S,*params[:k-1]).terms())
        h.append(value);checks+=1
    t,Y,Z=sp.symbols('t Y Z',positive=True)
    difference=sp.expand((1+t+t*t)*(Y+Z/t)
                         -((1+t*t)*Y+Z+(t*t*Y+Z)/t))
    assert difference==t*Z
    return {'independent_parameter_green_identities':checks,
            'positive_coefficient_checks':checks,
            'weighted_norm_exact_difference':str(difference)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,
        default=Path('/private/tmp/md-fixed-spectrum-continuant-results.json'))
    args=ap.parse_args()
    data={'scope':__doc__,'symbolic':symbolic(),
          'levels':[run_level(N) for N in [3,4,7,8]],
          'limits':'Finite algebra only. Real norm inequalities, Markov bounds and asymptotic localization are proved in the accompanying text.'}
    data['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'levels':[x['N'] for x in data['levels']],
        'full_coefficient_checks':sum(x['full_numerator_coefficient_checks'] for x in data['levels']),
        'green_checks':sum(x['green_checks'] for x in data['levels']),
        'output':str(args.output)},indent=2))

if __name__=='__main__':main()
