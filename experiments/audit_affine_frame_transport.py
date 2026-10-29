#!/usr/bin/env python3
"""Exact full-matrix affine-frame transport, without knot examples.

The proof is uniform in the accompanying note. This independent diagnostic
uses four rational endpoint pairs with the same common cube translation,
so every coefficient lies in Q(omega), not in a numerical root field.
"""

import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import sympy as sp


n=3
q=sp.Symbol("q")
modulus=sp.Poly(q*q+q+1,q,domain=sp.QQ)


@lru_cache(maxsize=None)
def coefficient(value):
    numerator,denominator=sp.fraction(sp.cancel(value))
    numerator=sp.Poly(numerator,q,domain=sp.QQ).rem(modulus)
    if numerator.is_zero:return sp.Integer(0)
    denominator=sp.Poly(denominator,q,domain=sp.QQ)
    return (numerator*denominator.invert(modulus)).rem(modulus).as_expr()


def reduce(M):return M.applyfunc(coefficient)
def product(*matrices):
    result=matrices[0]
    for M in matrices[1:]:result=reduce(result*M)
    return result
def inverse(M):return reduce(M.inv(method="DM"))
kron=sp.kronecker_product
I=sp.eye(n)


def module(lam,mu,a,b):
    lam,mu,a,b=map(sp.Rational,[lam,mu,a,b])
    assert lam*mu*a*b!=0 and b**n-lam*a**n==mu
    return lam,mu,a,b


@lru_cache(maxsize=None)
def operators(g):
    lam,mu,a,b=g
    X=sp.zeros(n)
    for j in range(n):X[(j+1)%n,j]=lam if j==n-1 else 1
    S=sp.diag(*[q**(-j) for j in range(n)])
    Y=reduce((b*I-a*X)*S)
    polynomial=sp.zeros(n)
    for j in range(n):polynomial+=b**(n-1-j)*a**j*X**j
    Yinv=reduce(sp.diag(*[q**j for j in range(n)])*polynomial/mu)
    assert product(Y,Yinv)==I
    return X,Y,Yinv


@lru_cache(maxsize=None)
def clebsch(g,h):
    lg,mg,ag,bg=g;lh,mh,ah,bh=h
    assert ag==bh
    total=module(lg*lh,mg+lg*mh,ah,bg)
    relative=module(total[1]/mh,-mg*lh/mh,ag/ah,bg/ah)
    X1,Y1,_=operators(g);X2,_,Y2inv=operators(h)
    XT=kron(X1,X2);D=reduce(kron(X1,I)+kron(Y1,Y2inv))
    vacuum=sp.zeros(n*n,1);vacuum[0]=1
    columns=[]
    for i in range(n):
        for j in range(n):columns.append(product(XT**i,D**j,vacuum))
    return sp.Matrix.hstack(*columns),total,relative


@lru_cache(maxsize=None)
def endpoint_intertwiner(g,gprime):
    lam,mu,a,b=g;lp,mp,ap,bp=gprime
    assert lam==lp==1 and mu==mp
    values=[sp.Integer(1)]
    for j in range(1,n):
        values.append(coefficient(values[-1]*(bp-ap*q**j)/(b-a*q**j)))
    assert coefficient(values[-1]*(bp-ap)/(b-a))==1
    X,Y,_=operators(g);_,Yprime,_=operators(gprime)
    H=sp.zeros(n)
    for k in range(n):
        c=coefficient(sum(values[j]*q**(-j*k) for j in range(n))/n)
        H+=c*X**k
    H=reduce(H)
    assert product(H,X)==product(X,H)
    assert product(H,Y)==product(Yprime,H)
    assert coefficient(sum(H[k,0] for k in range(n)))==1
    return H


def main():
    old_roots=list(map(sp.Rational,[-1,-9,-10,-12]))
    new_roots=list(map(sp.Rational,[12,10,9,1]))
    common_translation=sp.Rational(1729)
    assert all(b**n-a**n==common_translation for a,b in zip(old_roots,new_roots))

    edge=lambda roots,i,j:module(1,roots[i]**n-roots[j]**n,roots[j],roots[i])
    old_edges={(i,j):edge(old_roots,i,j) for i,j in combinations(range(4),2)}
    new_edges={(i,j):edge(new_roots,i,j) for i,j in combinations(range(4),2)}
    H={ij:endpoint_intertwiner(old_edges[ij],new_edges[ij]) for ij in old_edges}
    face_gauges={};old_faces={};new_faces={}

    for i,j,k in combinations(range(4),3):
        Cold,totalold,relativeold=clebsch(old_edges[i,j],old_edges[j,k])
        Cnew,totalnew,relativenew=clebsch(new_edges[i,j],new_edges[j,k])
        assert totalold==old_edges[i,k] and totalnew==new_edges[i,k]
        transformed=product(kron(inverse(H[i,k]),I),inverse(Cnew),
                            kron(H[i,j],H[j,k]),Cold)
        S=transformed[:n,:n]
        assert transformed==kron(I,S)
        Xold,Yold,_=operators(relativeold);Xnew,Ynew,_=operators(relativenew)
        assert product(S,Xold)==product(Xnew,S)
        assert product(S,Yold)==product(Ynew,S)
        assert product(kron(H[i,j],H[j,k]),Cold)==product(Cnew,kron(H[i,k],S))
        face_gauges[i,j,k]=S;old_faces[i,j,k]=relativeold;new_faces[i,j,k]=relativenew

    Rold,totalold,relativeold=clebsch(old_faces[0,1,3],old_faces[1,2,3])
    Rnew,totalnew,relativenew=clebsch(new_faces[0,1,3],new_faces[1,2,3])
    assert (totalold,relativeold)==(old_faces[0,2,3],old_faces[0,1,2])
    assert (totalnew,relativenew)==(new_faces[0,2,3],new_faces[0,1,2])
    source=kron(face_gauges[0,2,3],face_gauges[0,1,2])
    target=kron(face_gauges[0,1,3],face_gauges[1,2,3])
    assert product(Rnew,source)==product(target,Rold)

    vacuum=sp.zeros(n,1);vacuum[0]=1
    nonconstant=[ij for ij,T in H.items() if T*vacuum!=vacuum]
    moved_faces=[ijk for ijk,S in face_gauges.items()
                 if any(coefficient(x)!=0 for x in (S*vacuum)[1:,0])]
    assert len(nonconstant)==6 and len(moved_faces)==4
    for ij,T in H.items():
        reverse=endpoint_intertwiner(new_edges[ij],old_edges[ij])
        assert product(reverse,T)==I

    # A third pointing on one central fibre tests the composition scalar.
    g0=module(1,728,10,12);g1=module(1,728,1,9);g2=module(1,728,-12,-10)
    assert product(endpoint_intertwiner(g1,g2),endpoint_intertwiner(g0,g1))==endpoint_intertwiner(g0,g2)

    result={"scope":"Full-matrix affine-frame covariance; no knot examples.",
            "level":n,"coefficient_field":"Q[q]/(q^2+q+1)",
            "old_endpoint_roots":[str(a) for a in old_roots],
            "new_endpoint_roots":[str(a) for a in new_roots],
            "common_translation":str(common_translation),
            "six_edge_intertwiners_exact":True,
            "four_triangle_gauges_factor_as_identity_tensor_S":True,
            "four_triangle_intertwining_equations_exact":True,
            "full_Racah_matrix_covariance_exact":True,
            "edge_inverse_and_three_pointing_cocycle_exact":True,
            "edges_with_nonconstant_transported_vacuum":len(nonconstant),
            "faces_with_nonconstant_transported_vacuum":len(moved_faces),
            "scalar_factors_suppressed":False,
            "remaining":"Intrinsic selected literature period and growth comparison; projective frames have a companion proof."}
    Path(__file__).with_name("affine_frame_transport_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
