"""Exact degree-elevation wall, selected source and moment residuals."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def generators(N):
    e,f=sp.zeros(N+1),sp.zeros(N+1)
    h=sp.diag(*[N-2*k for k in range(N+1)])
    for k in range(1,N+1):
        e[k-1,k]=N-k+1
        f[k,k-1]=k
    return e,f,h


def elevate(C):
    N=C.rows
    E0,E1=sp.zeros(N+1),sp.zeros(N+1)
    for i in range(N+1):
        for j in range(N+1):
            if i<N and j<N:E0[i,j]=sp.Rational(N-i,N)*C[i,j]
            if i and j:E1[i,j]=sp.Rational(i,N)*C[i-1,j-1]
    return E0+E1,E0,E1


def wall(D,u):
    N=D.rows-1
    return sp.expand(sum((-1)**j*sp.binomial(N,i)*D[i,j]*u**(N+i-j)
                         for i in range(N+1) for j in range(N+1)))


def zero(M):return all(sp.expand(x)==0 for x in M)


def case(N):
    u,w,Q,m=sp.symbols('u w Q m',nonzero=True)
    e,f,h=generators(N)
    checks=0
    for i in range(N):
        for j in range(N):
            C=sp.zeros(N);C[i,j]=1
            E,_,_=elevate(C)
            assert wall(E,u)==0
            checks+=1
    for i in range(N+1):
        for j in range(N+1):
            D=sp.zeros(N+1);D[i,j]=1
            p=wall(D,u)
            for g,target in ((e,sp.diff(p,u)),(f,2*N*u*p-u*u*sp.diff(p,u)),
                             (h,2*N*p-2*u*sp.diff(p,u))):
                assert sp.expand(wall(g*D-D*g,u)-target)==0
            K=sp.diag(*[Q**(-k) for k in range(N+1)])
            assert sp.expand(wall(K*D*K.inv(),u)-Q**N*p.subs(u,u/Q))==0
            checks+=4
    C=sp.Matrix(N,N,lambda i,j:i+2*j+3)
    E,E0,E1=elevate(C)
    Wold=sp.diag(*[w**k for k in range(N)])
    Wnew=sp.diag(*[w**k for k in range(N+1)])
    assert zero(elevate(Wold*C)[0]-Wnew*(E+(1/w-1)*E1))
    assert zero(elevate(C*Wold)[0]-(E+(1/w-1)*E1)*Wnew)
    checks+=2
    source=sp.ones(N+1,1)
    row=sp.Matrix([[sp.binomial(N,k)*((1+m)/2)**(N-k)*((1-m)/2)**k
                    for k in range(N+1)]])
    coupon=source*row
    assert sp.expand(wall(coupon,u)-((1+u)*((1+m)*u-(1-m))/2)**N)==0
    wrap=sp.zeros(N+1);wrap[N,0]=1
    assert sp.expand((row*wrap*source)[0]-((1-m)/2)**N)==0
    assert f**N==sp.factorial(N)*wrap
    checks+=3
    # Full selected coupled source: its Fr blocks are literal head matrices.
    block_wall=sp.zeros(N)
    for i in range(N+1):
        for j in range(N+1):
            si,sj=i%N,j%N
            block_wall[si,sj]+=sp.Rational(1,2**N)*sp.binomial(N,i)*sp.binomial(N,j)*(-1)**j*u**(N+i-j)
    a=sp.Matrix([1+u**N]+[sp.binomial(N,k)*u**k for k in range(1,N)])
    b=sp.Matrix([[1+(-1)**N/u**N]+[(-1)**k*sp.binomial(N,k)/u**k for k in range(1,N)]])
    assert zero(block_wall-sp.Rational(1,2**N)*u**N*a*b)
    checks+=1
    # The upper-only external source is correlated, not a product dual.
    I=sp.zeros(2*N,N+1);P=sp.zeros(N+1,2*N)
    for k in range(N):
        I[2*k,k]=1;I[2*k+1,k+1]=1
        P[k,2*k]=sp.Rational(N-k,N)
        P[k+1,2*k+1]=sp.Rational(k+1,N)
    assert P*I==sp.eye(N+1)
    word=sp.kronecker_product(C,sp.eye(2))
    assert P*word*I==E
    psi=I*sp.ones(N+1,1)
    dual=sp.ones(1,N+1)*P/(N+1)
    assert (dual*psi)[0]==1
    assert (dual*word*psi)[0]==sum(C)/N
    D=sp.Matrix(N,N,lambda i,j:2*i-j+1)
    fullC=sp.kronecker_product(C,sp.eye(2))
    fullD=sp.kronecker_product(D,sp.eye(2))
    assert zero(elevate(C*D)[0]-E*elevate(D)[0]-P*fullC*(sp.eye(2*N)-I*P)*fullD*I)
    checks+=5
    return {'N':N,'exact_checks':checks,'source_wrap_weight':str(sp.Rational(1,2**N)),
            'uniform_wrap_weight':str(sp.Rational(1,N+1))}


def main():
    cases=[case(N) for N in range(2,8)]
    result={'status':'pass','cases':cases,'checks':sum(c['exact_checks'] for c in cases),
            'scope':'Exact degree-elevation/source residual and auxiliary word identity; no Gaussian/selected-volume map.'}
    path=Path(__file__).with_name('degree_elevation_wall_residual_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','levels':len(cases),'checks':result['checks'],
                      'results':str(path)},indent=2))


if __name__=='__main__':main()
