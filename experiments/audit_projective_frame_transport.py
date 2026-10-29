#!/usr/bin/env python3
"""Generic projective coefficient identities and an exact inversion tensor.

No knot data. The finite diagnostic keeps the unnormalized scalar rather
than selecting numerical determinant roots. The accompanying proof fixes
the normalized scalar on the component anchored at the identity frame.
"""

import json
from itertools import combinations
from pathlib import Path

import sympy as sp

from audit_affine_frame_transport import n,q,I,coefficient,reduce,product,inverse,kron,module,operators,clebsch


def symbolic_certificate():
    p=sp.symbols("p0:4")
    a,b,c,d=sp.symbols("a b c d")
    transformed=[(a*x+b)/(c*x+d) for x in p]
    central=lambda points,i,j,k:((points[i]-points[k])/(points[j]-points[k]),
                                 -(points[i]-points[j])/(points[j]-points[k]))
    for i,j,k in combinations(range(4),3):
        lam,mu=central(p,i,j,k);lp,mp=central(transformed,i,j,k)
        assert sp.cancel(lp-lam*(c*p[j]+d)/(c*p[i]+d))==0
        assert sp.cancel(mp-mu*(c*p[k]+d)/(c*p[i]+d))==0
    D=sp.symbols("D0:4",nonzero=True)
    scales=lambda i,j,k:(D[j]/D[i],D[k]/D[i])
    ka,va=scales(0,2,3);kb,vb=scales(0,1,2)
    kc,vc=scales(0,1,3);kd,vd=scales(1,2,3)
    for expression in [ka-kc*kd,va-kc*vd,va-vc,kb-kc,kb-vc/vd,vb-vc*kd/vd]:
        assert sp.cancel(expression)==0
    face=lambda i,j,k:p[k]*(p[i]-p[k])/(p[j]-p[k])**2
    delta=face(1,2,3)*face(0,1,3)/(face(0,2,3)*face(0,1,2))
    fgen=-(p[2]/p[3])*(p[0]-p[2])*(p[1]-p[3])/(p[1]-p[2])**2
    assert sp.cancel(fgen+1/delta)==0
    return {"Mobius_coefficients_and_flags_indeterminate":True,
            "all_four_triangle_central_character_covariances_exact":True,
            "all_six_ordered_Racah_rescaling_coefficients_match":True,
            "general_endpoint_Racah_determinant_unit_is_signed_face_coboundary":True}


def norm_one_intertwiner(g,gprime):
    lam,mu,a,b=g;lp,mp,ap,bp=gprime
    assert lam==lp and mu==mp
    X,Y,_=operators(g);_,Yprime,_=operators(gprime)
    # Explicit Hilbert-90 averaging. One Fourier test vector must work.
    for m in range(n):
        H=sp.zeros(n);R=I
        for j in range(n):
            H+=R*(q**(-j)*X)**m
            denominator=b*I-a*q**(-j)*X
            numerator=bp*I-ap*q**(-j)*X
            R=product(R,numerator,inverse(denominator))
        H=reduce(H)
        assert R==I
        if H!=sp.zeros(n):
            assert product(H,Y)==product(Yprime,H) and product(H,X)==product(X,H)
            assert coefficient(H.det())!=0
            return H
    raise AssertionError("All Hilbert-90 Fourier tests vanished")


def inversion_certificate():
    roots=list(map(sp.Rational,[-1,-9,-10,-12]))
    newroots=[1/a for a in roots]
    edge=lambda A,i,j:module(1,A[i]**n-A[j]**n,A[j],A[i])
    old_faces={};new_faces={};S={}
    for i,j,k in combinations(range(4),3):
        _,_,old=clebsch(edge(roots,i,j),edge(roots,j,k))
        _,_,new=clebsch(edge(newroots,i,j),edge(newroots,j,k))
        kappa=roots[j]/roots[i];nu=roots[k]/roots[i]
        lam,mu,a,b=old
        scaled=module(kappa**n*lam,nu**n*mu,nu*a/kappa,nu*b)
        K=sp.diag(*[kappa**(-j) for j in range(n)])
        X,Y,_=operators(old);Xp,Yp,_=operators(scaled)
        assert product(K,kappa*X)==product(Xp,K)
        assert product(K,nu*Y)==product(Yp,K)
        H=norm_one_intertwiner(scaled,new)
        S[i,j,k]=product(H,K)
        old_faces[i,j,k]=old;new_faces[i,j,k]=new
    Rold,_,_=clebsch(old_faces[0,1,3],old_faces[1,2,3])
    Rnew,_,_=clebsch(new_faces[0,1,3],new_faces[1,2,3])
    for endpoints,R in [(roots,Rold),(newroots,Rnew)]:
        p=[A**n for A in endpoints]
        fgen=-(p[2]/p[3])*(p[0]-p[2])*(p[1]-p[3])/(p[1]-p[2])**2
        assert coefficient(R.det()-fgen**(n*(n-1)//2))==0
    source=kron(S[0,2,3],S[0,1,2]);target=kron(S[0,1,3],S[1,2,3])
    left=product(Rnew,source);right=product(target,Rold)
    chosen=next((i,j) for i in range(n*n) for j in range(n*n) if right[i,j]!=0)
    scalar=coefficient(left[chosen]/right[chosen])
    assert scalar!=0 and left==reduce(scalar*right)
    detS={ijk:coefficient(M.det()) for ijk,M in S.items()}
    detratio=coefficient(Rnew.det()/Rold.det())
    determinant_rhs=coefficient(detratio*(detS[0,2,3]*detS[0,1,2]
                                      /(detS[0,1,3]*detS[1,2,3]))**n)
    assert coefficient(scalar**(n*n)-determinant_rhs)==0
    return {"level":n,"Mobius_map":"p -> 1/p",
            "four_triangle_rescaled_intertwiners_exact":True,
            "full_inversion_Racah_covariance_up_to_exact_scalar":True,
            "both_general_endpoint_Racah_determinants_verified":True,
            "unnormalized_scalar":str(scalar),
            "determinant_power_identity_exact":True,
            "numerical_root_choices_used":False,
            "normalized_scalar_proof":"mu_(n^2)-valued; identity-frame anchor fixes it on its irreducible lifted component."}


def main():
    result={"scope":"Uniform projective-frame descent at a fixed odd level, not a global growth theorem.",
            "generic_projective_certificate":symbolic_certificate(),
            "exact_inversion_tensor":inversion_certificate(),
            "remaining":"Intrinsic gluing and selected literature period/cycle; compatibility across levels."}
    Path(__file__).with_name("projective_frame_transport_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
