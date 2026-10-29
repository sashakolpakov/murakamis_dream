"""Exact checks of the actual source's cotangent and Weyl cocycles."""

from __future__ import annotations

import json
from math import lcm
from pathlib import Path

import sympy as sp


def matmul(a,b,p):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))%p
             for j in range(n)] for i in range(n)]


def scaled(a,c,p):
    return [[c*x%p for x in row] for row in a]


def module(N,q,M,p):
    Q=q*q%p
    invM=pow(M,-1,p)
    K=[[0]*N for _ in range(N)]
    E=[[0]*N for _ in range(N)]
    F=[[0]*N for _ in range(N)]
    for j in range(N):
        K[j][j]=-M*pow(q,-1,p)*pow(Q,-j,p)%p
        if j:
            E[j-1][j]=(M*pow(Q,-j,p)-invM)%p
        if j<N-1:
            F[j+1][j]=(1-pow(Q,j+1,p))%p
    return K,E,F


def adapter(N,Q,M,p):
    d=[1]
    for j in range(1,N):
        d.append(d[-1]*M*(1-pow(Q,j,p))
                 *pow((1-M*M*pow(Q,j,p))%p,-1,p)%p)
    W=[[0]*N for _ in range(N)]
    for j in range(N):
        W[j][N-1-j]=d[j]
    return W


def beta(N,Q,M,ii,p):
    m=N//2
    answer=1
    for r in range(1,m+1 if N%2 else m):
        answer=answer*(1-M*M*pow(Q,r,p))*pow((1-pow(Q,r,p))%p,-1,p)%p
    if not N%2:
        answer=answer*(1+ii*M)*pow((1+ii)%p,-1,p)%p
    return answer


def finite_checks():
    results=[]
    for N in range(2,15):
        modulus=lcm(2*N,4)
        p=next(modulus*k+1 for k in range(2,1000) if sp.isprime(modulus*k+1))
        g=int(sp.primitive_root(p))
        q=pow(g,(p-1)//(2*N),p)
        Q=q*q%p
        ii=pow(g,(p-1)//4,p)
        identity=[[int(i==j) for j in range(N)] for i in range(N)]
        cases=0
        for M in range(1,p):
            if any((1-M*M*pow(Q,r,p))%p==0 for r in range(1,N)):
                continue
            Mi=pow(M,-1,p)
            W=adapter(N,Q,M,p)
            Wi=adapter(N,Q,Mi,p)
            K,E,F=module(N,q,M,p)
            Ki,Ei,Fi=module(N,q,Mi,p)
            Ki_inverse=[[pow(Ki[i][i],-1,p) if i==j else 0
                         for j in range(N)] for i in range(N)]
            assert matmul(W,K,p)==matmul(Ki_inverse,W,p)
            assert matmul(W,E,p)==matmul(scaled(Fi,-1,p),W,p)
            assert matmul(W,F,p)==matmul(scaled(Ei,-1,p),W,p)
            S=sum(pow(M,2*r,p) for r in range(N))%p
            c=N*pow(M,N-1,p)*pow(S,-1,p)%p
            assert matmul(Wi,W,p)==scaled(identity,c,p)
            b=beta(N,Q,M,ii,p)
            bi=beta(N,Q,Mi,ii,p)
            assert b*bi*c%p==1
            assert matmul(scaled(Wi,bi,p),scaled(W,b,p),p)==identity
            if M==1:
                assert c==b==1
                assert all(sum(W[i])%p==1 for i in range(N))
            cases+=1
            if cases==6:
                break
        assert cases==6
        results.append({'level':N,'prime':p,'meridian_cases':cases,
                        'three_actual_generator_intertwiners':True,
                        'square_is_full_modified_dimension_adapter':True,
                        'marked_rational_norm_split':True,
                        'normalized_reflection_involution':True,
                        'complete_source_is_fixed':True})
    return results


def symbolic_checks():
    w,b=sp.symbols('w b',nonzero=True)
    wp,bp=1/w,w-w*w*b
    jac=sp.det(sp.Matrix([[sp.diff(wp,w),sp.diff(wp,b)],
                         [sp.diff(bp,w),sp.diff(bp,b)]]))
    assert sp.simplify(jac-1)==0
    assert sp.simplify(-bp*sp.diff(wp,w)+b-1/w)==0
    u=sp.symbols('u')
    expansions=[]
    for N in range(2,15):
        # Use sinh's removable series, retaining precisely the level shift.
        c=sp.series(N*sp.sinh(u)/sp.sinh(N*u),u,0,4).removeO()
        assert sp.simplify(c-(1-sp.Rational(N*N-1,6)*u*u))==0
        expansions.append(N)
    return {'cotangent_affine_transition_symplectic':True,
            'Chern_primitive_transition_dlog':True,
            'whole_peripheral_second_normal':expansions}


def main():
    result={'geometry':symbolic_checks(),'actual_Weyl_source':finite_checks(),
            'scope':'Exact source/gluing formulas; no selected-volume estimate.'}
    Path(__file__).with_name('twisted_source_weyl_gluing_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
