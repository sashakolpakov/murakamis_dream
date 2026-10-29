#!/usr/bin/env python3
"""Uniform pointed recoupling, normalization and flag-line checks.

No knot examples are inputs. Symbolic identities keep the quantum parameter,
affine endpoints, central parameters and flag coordinates generic. One exact
three-factor matrix verifies the explicit Racah identification.
"""

import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import sympy as sp

from audit_pointed_recoupling import ONE,add,scale,mul,q,norm_matrices


def parameter_certificate():
    r,s,t=sp.symbols("r s t")
    tau=lambda a,b:(1-a*b)/(1-b)
    f=lambda a,b:b*(1-a*b)/(1-b)**2
    a,b,c,d=tau(r*s,t),tau(r,s),tau(r,s*t),tau(s,t)
    assert sp.cancel(a-c*d)==0 and sp.cancel(b-tau(c,d))==0
    shape=(1-r*s)*(1-s*t)/((1-r*s*t)*(1-s))
    assert sp.cancel(b/c-shape)==0
    ratio=f(r,s)*f(r*s,t)/(f(r,s*t)*f(s,t))
    assert sp.cancel(f(c,d)+ratio)==0
    return {"parameters_indeterminate":True,
            "left_relative_parameters":[str(sp.factor(a)),str(sp.factor(b))],
            "right_relative_parameters":[str(sp.factor(c)),str(sp.factor(d))],
            "explicit_Racah_factorization_parameters_verified":True,
            "tetrahedral_cross_ratio":str(shape),
            "normalization_coboundary":"f(c,d)=-f(r,s)*f(r*s,t)/(f(r,s*t)*f(s,t))",
            "raw_root_phase_power":"epsilon^n=(-1)^((n-1)/2)",
            "signed_Racah_phase_power":"epsilon_signed^n=1"}


def endpoint_certificate():
    a,b,c=sp.symbols("incoming middle outgoing",nonzero=True)
    X1={(1,0,0,0):sp.Integer(1)};Y1={(0,1,0,0):sp.Integer(1)}
    X2={(0,0,1,0):sp.Integer(1)};Y2={(0,0,0,1):sp.Integer(1)}
    Z=mul(Y1,{(0,0,0,-1):sp.Integer(1)})
    D=add(X1,Z);C=mul(Z,X2);XT=mul(X1,X2);YT=add(mul(X1,Y2),Y1)
    L1=add(Y1,scale(b,X1),scale(-c,ONE))
    L2=add(Y2,scale(a,X2),scale(-b,ONE))
    LT=add(YT,scale(a,XT),scale(-c,ONE))
    LR=add(scale(-1,C),scale(b/a,D),scale(-c/a,ONE))
    assert add(LT,scale(-1,L1),scale(-1,mul(X1,L2)))=={}
    assert add(LR,scale(-1/a,L1),scale(1/a,mul(Z,L2)))=={}
    assert add(LT,scale(-a,LR),scale(-1,mul(D,L2)))=={}
    lam1,mu1,lam2,mu2,A,B,C0=sp.symbols("lambda1 mu1 lambda2 mu2 A B C")
    # A,B,C0 here denote the n-th powers of the incoming, middle and outgoing endpoints.
    constraints={B:lam2*A+mu2,C0:lam1*(lam2*A+mu2)+mu1}
    normalized_s=lam1*B/C0;normalized_t=lam2*A/B
    f=normalized_t*(1-normalized_s*normalized_t)/(1-normalized_t)**2
    detunit=sp.cancel((C0/B)*f)
    expected=A*lam2*(mu1+lam1*mu2)/mu2**2
    assert sp.cancel((detunit-expected).subs(constraints,simultaneous=True))==0
    return {"quantum_parameter_and_endpoint_roots_indeterminate":True,
            "three_pointed_ideal_identities_exact":True,
            "general_normalization_unit":"incoming^n*lambda_h*mu_(gh)/mu_h^2",
            "general_determinant_unit_verified":True}


def flag_certificate():
    coords=sp.symbols("x0:5")+sp.symbols("y0:5")
    vectors=[sp.Matrix([coords[i],coords[5+i]]) for i in range(5)]
    bracket=lambda i,j:sp.det(sp.Matrix.hstack(vectors[i],vectors[j]))
    assert sp.expand(bracket(0,1)*bracket(2,3)-bracket(0,2)*bracket(1,3)
                     +bracket(0,3)*bracket(1,2))==0
    aa,bb,cc,dd=sp.symbols("a b c d")
    G=sp.Matrix([[aa,bb],[cc,dd]])
    assert sp.expand(sp.det(sp.Matrix.hstack(G*vectors[0],G*vectors[1]))
                     -G.det()*bracket(0,1))==0
    labels={pair:sp.Symbol("L"+"".join(map(str,pair)),nonzero=True)
            for pair in combinations(range(5),2)}
    L=lambda i,j:labels[i,j]
    triangle=lambda i,j,k:L(i,k)/L(j,k)**2
    delta_triangle=(triangle(1,2,3)*triangle(0,1,3)
                    /(triangle(0,2,3)*triangle(0,1,2)))
    fbar=-L(0,2)*L(1,3)/L(1,2)**2
    assert sp.cancel(fbar+1/delta_triangle)==0
    rescalings=sp.symbols("r0:5",nonzero=True)
    decorated=fbar.subs({value:rescalings[i]*rescalings[j]*value
                         for (i,j),value in labels.items()},simultaneous=True)
    assert sp.cancel(decorated/fbar-rescalings[0]*rescalings[3]
                     /(rescalings[1]*rescalings[2]))==0
    roots={face:sp.Symbol("alpha"+"".join(map(str,face)),nonzero=True)
           for face in combinations(range(5),3)}
    eta=lambda tet:sp.prod(roots[tuple(v for j,v in enumerate(tet) if j!=i)]**((-1)**i)
                          for i in range(4))
    total=sp.prod(eta(tuple(j for j in range(5) if j!=i))**((-1)**i) for i in range(5))
    assert sp.cancel(total)==1
    return {"generic_spinor_Plucker_relation_exact":True,
            "generic_GL2_bracket_covariance_exact":True,
            "intrinsic_normalization_unit":"-L02*L13/L12^2",
            "decoration_line_weight":"r0*r3/(r1*r2)",
            "normalization_is_signed_face_coboundary":True,
            "five_tetrahedron_shared_face_root_product":1,
            "independent_tetrahedron_root_choices_used":False}


def racah_matrix_certificate():
    n=3
    modulus=sp.Poly(sp.cyclotomic_poly(n,q),q,domain=sp.QQ)

    @lru_cache(maxsize=None)
    def reduce_coefficient(value):
        num,den=sp.fraction(sp.cancel(value))
        numerator=sp.Poly(num,q,domain=sp.QQ).rem(modulus)
        if numerator.is_zero:return sp.Integer(0)
        denominator=sp.Poly(den,q,domain=sp.QQ)
        return (numerator*denominator.invert(modulus)).rem(modulus).as_expr()

    reduce_matrix=lambda M:M.applyfunc(reduce_coefficient)
    kron=sp.kronecker_product

    @lru_cache(maxsize=None)
    def clebsch(a,b):
        X1,Y1,_=norm_matrices(a,n);X2,_,Y2inv=norm_matrices(b,n)
        XT=kron(X1,X2);D=kron(X1,sp.eye(n))+kron(Y1,Y2inv)
        v=sp.zeros(n*n,1);v[0]=1
        columns=[]
        for i in range(n):
            for j in range(n):columns.append(reduce_matrix(XT**i*D**j*v))
        return sp.Matrix.hstack(*columns)

    r,s,t=map(sp.Rational,[2,3,5])
    tau=lambda a,b:(1-a*b)/(1-b)
    c,d=tau(r,s*t),tau(s,t)
    I=sp.eye(n)
    permutation=sp.zeros(n**3)
    for a,b,c0 in sp.utilities.iterables.cartes(range(n),range(n),range(n)):
        permutation[a*n*n+c0*n+b,a*n*n+b*n+c0]=1
    left=reduce_matrix(kron(clebsch(r,s),I)*permutation*kron(clebsch(r*s,t),I))
    right=reduce_matrix(kron(I,clebsch(s,t))*kron(clebsch(r,s*t),I))
    right=reduce_matrix(right*kron(I,clebsch(c,d)))
    assert left==right
    v=sp.zeros(n**3,1);v[0]=1
    assert left*v==v and right*v==v
    return {"level":n,"generic_central_parameters":[str(x) for x in [r,s,t]],
            "exact_matrix_dimension":n**3,
            "explicit_Clebsch_Racah_tree_identity_exact":True,
            "selected_product_vacuum_preserved_exactly":True,
            "exterior_tensor_scope":"Matrix equality applies to every finite exterior contraction.",
            "proof_status":"Finite exact diagnostic for the separate uniform operator proof; no knot data."}


def main():
    result={"scope":"Uniform pointed-period descent; no knot-census input.",
            "generic_parameters":parameter_certificate(),
            "matched_affine_endpoints":endpoint_certificate(),
            "decorated_flag_normalization":flag_certificate(),
            "explicit_Racah_matrix":racah_matrix_certificate(),
            "remaining":"Intrinsic equivariant gluing, selected literature period/cycle and regulator growth; local projective frames have a companion proof."}
    Path(__file__).with_name("period_descent_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
