#!/usr/bin/env python3
"""Exact N=3 one-exception identities from the original homogeneous matrix.

All arithmetic is integral. The comparison polynomial is built twice:
direct Casimir matrix powers, and a positive coefficient support count.
No asymptotic estimate is tested or asserted.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

M=6
ZERO=(0,)*M
ONE={ZERO:1}
TARGET=(2,)*M


def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}


def scale(a,c):return {k:c*v for k,v in a.items() if c*v}


def mul(a,b):
    out=defaultdict(int)
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb))
            if max(k)<=2:out[k]+=va*vb
    return {k:v for k,v in out.items() if v}


def var(k):
    a=[0]*M;a[k]=1;return {tuple(a):1}


def rim(k):return var(k%M) if k%M else {}


def faces(j):
    x={} if j%2 else var(0);y=rim(j)
    b,c=(rim(j-1),rim(j+1)) if j%2 else (rim(j+1),rim(j-1))
    return x,b,c,y


def matrix_multiply(A,B):
    C=[[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
    return C


def local_from_matrix(position, spectral_degree=None, cross=False):
    x,b,c,y=faces(position)
    C=[[{} for _ in range(3)] for _ in range(3)]
    for i,v in enumerate((1,-2,1)):C[i][i]=scale(ONE,v)
    C[0][1]=C[1][2]=scale(add(x,y),-3)
    C[0][2]=scale(mul(x,y),-3)
    C2=matrix_multiply(C,C)
    V=[[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            I=ONE if i==j else {}
            if spectral_degree is None:V[i][j]=add(add(C2[i][j],scale(C[i][j],-2)),I)
            elif spectral_degree==0:V[i][j]=add(C2[i][j],scale(I,-3))
            elif spectral_degree==1:V[i][j]=C[i][j]
            else:V[i][j]=I
    bp=[ONE,b,mul(b,b)];cp=[ONE,c,mul(c,c)]
    H={}
    for i in range(3):
        for j in range(i,3):
            if cross and (i==j==0 or i==j==2):continue
            H=add(H,mul(mul(bp[i],V[i][j]),cp[2-j]))
    return H


def source(exception,degree,cross):
    result=ONE
    for j in range(M):result=mul(result,local_from_matrix(j,degree if j==exception else None,cross))
    return result.get(TARGET,0)


def positive_factor(j):
    x,b,c,y=faces(j);a=add(x,y)
    return add(add(mul(b,c),mul(a,add(b,c))),mul(a,a))


def support_count(exception,side):
    _,b,c,_=faces(exception)
    result=mul(b,b) if side=='RIGHT' else mul(c,c)
    for j in range(M):
        if j!=exception:result=mul(result,positive_factor(j))
    return result.get(TARGET,0)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args();rows=[]
    for j in range(M):
        coefficients=[source(j,k,False)-source(j,k,True) for k in range(3)]
        left,right=support_count(j,'LEFT'),support_count(j,'RIGHT')
        K=left+right
        assert coefficients==[9**5*K*v for v in (-2,1,1)]
        rows.append(dict(exceptional_position=j,left_support_coefficient=left,
                         right_support_coefficient=right,K=K,
                         difference_sigma_coefficients=coefficients,
                         difference_at_sigma_2=sum(c*2**k for k,c in enumerate(coefficients)),
                         derivative_at_sigma_minus_2=coefficients[1]-4*coefficients[2]))
    assert [r['K'] for r in rows]==[0,11,4,2,4,11]
    data=dict(status='exact_integer_polynomial_identities_passed',N=3,equator_size=6,
              target='S^2 z1^2 z2^2 z3^2 z4^2 z5^2',protected=['north','z0'],
              rows=rows,construction='Original upper-band C(x,y), then C^2+sigma C+(sigma^2-3)I, then original homogeneous face coefficient.',
              independent_comparison='Direct positive coefficient of b^2 or c^2 times the five complete P factors.',
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              limitation='Finite exact obstruction to all-position one-exception vanishing; no asymptotic spectral-gap statement.')
    args.output.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))


if __name__=='__main__':main()
