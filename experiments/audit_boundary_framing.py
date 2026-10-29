#!/usr/bin/env python3
"""Exact peripheral-coordinate and Fourier/Gaussian shear checks.

The theorem is in general_boundary_state_and_framing.md. These checks keep
generic quantum-torus variables and do not specialize the meridian to one.
The framed operator is asserted to annihilate the transformed state; its
minimality after changing polarization is not assumed.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from audit_two_bridge import branchings,ordered_faces,parity
from certify_six_three import ab
from layered_two_bridge import layered_gluings,orientation_signs
from reduce_singular_faces import exact_reduction,peripheral_cycles


V=sp.Symbol("v",positive=True)
Q=sp.Symbol("Q")


def multiply(left,right):
    result={}
    for (j,k),a in left.items():
        for (l,m),b in right.items():
            key=(j+l,k+m)
            result[key]=result.get(key,0)+a*b*V**(2*k*l)
    return {key:sp.cancel(a) for key,a in result.items() if sp.cancel(a)!=0}


def shear(operator,n):
    return {(j,k+2*n*j):sp.cancel(a*V**(2*n*j*j))
            for (j,k),a in operator.items()}


def equal(left,right):
    return all(sp.cancel(left.get(key,0)-right.get(key,0))==0
               for key in set(left)|set(right))


def quantum_torus_certificate():
    cases=0
    monomials=[{(j,k):sp.Integer(1)} for j in [-2,0,1] for k in [-1,0,2]]
    for n in [-1,sp.Rational(-1,2),sp.Rational(1,2),1,2]:
        for a in monomials:
            assert equal(shear(shear(a,n),-n),a)
            for b in monomials:
                assert equal(shear(multiply(a,b),n),multiply(shear(a,n),shear(b,n)))
                cases+=1
    q=V**2
    R=q**4*Q**4-q**3*Q**3-q*(q*q+1)*Q**2-q*Q+1
    coefficients=[q*q*Q**2*(q**3*Q**2-1),
                  V*(q*q*Q**2-1)*R,
                  q**3*Q**2*(q*Q**2-1)]
    source={}
    for k,coefficient in enumerate(coefficients):
        for (j,),value in sp.Poly(coefficient,Q).terms():
            source[j,k]=value
    transformed=shear(source,1)
    assert equal(shear(transformed,-1),source)
    source_terms=[{"Q_power":j,"E_power":k,"coefficient":str(a)}
                  for (j,k),a in sorted(source.items())]
    transformed_terms=[{"Q_power":int(j),"E_power":int(k),"coefficient":str(a)}
                       for (j,k),a in sorted(transformed.items())]
    return {"multiplicativity_identities":cases,
            "conjugation":"Q -> q^n Q E^(2n); E -> E; q=v^2",
            "monomial_rule":"Q^j E^k -> q^(n*j^2) Q^j E^(k+2*n*j)",
            "figure_eight_source":"audited two-tetrahedron operator in audit_figure_eight_move.py",
            "source_terms":source_terms,"unit_shear_terms":transformed_terms,
            "unit_shear_E_exponent_range":[min(int(k) for j,k in transformed),max(int(k) for j,k in transformed)],
            "inverse_recovers_all_source_coefficients":True,
            "minimality_of_transformed_polynomial_asserted":False,
            "generic_peripheral_factors_retained":True}


def gaussian_certificate():
    a,n,t,u=sp.symbols("a n t u",nonzero=True)
    M=a-sp.I/(2*n)
    assert sp.cancel(2*sp.I*n*M-(1+2*sp.I*n*a))==0
    exponent=sp.I*t*t/(2*n)-t*t/(4*n*n*M)
    assert sp.cancel(exponent+a*t*t/(1+2*sp.I*n*a))==0
    # Laplace parameterization uses exp(2*pi*u*t).
    laplace_exponent=u*u*(1+2*sp.I*n*a)/a
    assert sp.expand(laplace_exponent-u*u/a-2*sp.I*n*u*u)==0
    return {"fresnel_kernel_normalization_squared_exact":True,
            "gaussian_image":"(1+2*i*n*a)^(-1/2)*exp(-pi*a*t^2/(1+2*i*n*a))",
            "gaussian_laplace_multiplier":"exp(2*pi*i*n*u^2)",
            "root_branch":"sqrt(2*i*n)=sqrt(2*abs(n))*exp(i*pi*sign(n)/4)"}


def boundary_certificate(word):
    gluings=layered_gluings(word)
    orders=next(branchings(gluings,10000))
    faces=ordered_faces(gluings,orders)
    signs=[e*parity(p) for e,p in zip(orientation_signs(gluings),orders)]
    data=exact_reduction(faces,signs)
    curves=peripheral_cycles(faces,signs,data)
    hm=curves["alpha_holonomy"]
    hl=curves["intersection"]*curves["longitude_holonomy"]
    Am,Bm,_=ab(hm,signs)
    Al,Bl,_=ab(hl,signs)
    rows=data["Aed"].row_join(data["Bed"])
    selected=list(rows.T.rref()[1])
    B=data["Bed"][selected,:].col_join(Bl)
    S=data["S"]
    assert data["Bed"].rank()==S.cols-1
    target=sp.zeros(len(faces),1)
    target[-1]=2
    r,parameters=(B*S).gauss_jordan_solve(target)
    assert parameters.rows==0
    v=S*r
    p=S.T*v
    beta=(Bm*v)[0]/2
    assert S*data["Sinv"]*Bm.T==Bm.T
    assert (Am-Bm*data["Gambient"])*S==-p.T
    assert ((data["Sinv"]*Bl.T).T*p)[0]==2
    assert ((data["Sinv"]*Bm.T).T*p)[0]==2*beta
    # Deliberately change the tested curve to m+2*l. This is a recorded
    # boundary basis change, not an assertion that it is the S^3 meridian.
    Am2,Bm2=Am+2*Al,Bm+2*Bl
    beta2=(Bm2*v)[0]/2
    assert beta2==beta+2
    assert (Am2-Bm2*data["Gambient"])*S==-p.T
    reference_comparison=None
    if word=="RRLR":
        from certify_six_two import BETA0,H_EXPECTED,REFERENCE,SIMPLE_SUPPORT
        n=len(faces)
        aq=sp.Matrix(n,3*n,lambda i,j:int(j==3*i))
        cq=sp.diag(*signs)*sp.Matrix(n,3*n,lambda i,j:int(j==3*i+2))
        dref=sp.ones(n,1)-aq*REFERENCE
        Wref=2*data["Qambient"]*dref-cq*REFERENCE
        assert (hm.T*REFERENCE)[0]==(hl.T*REFERENCE)[0]==0
        compact_inverse=(SIMPLE_SUPPORT.T*SIMPLE_SUPPORT).inv()*SIMPLE_SUPPORT.T
        coordinate_change=compact_inverse*S
        offset=compact_inverse*(dref-BETA0)
        compact_p=sp.Matrix([-1,-1,-1,1])
        assert abs(coordinate_change.det())==1
        assert p==coordinate_change.T*compact_p and (compact_p.T*offset)[0]==0
        z=sp.Matrix(sp.symbols("z0:4"))
        y=sp.I*dref+S*z
        compact_z=coordinate_change*z+sp.I*offset
        H=data["Qambient"]-sp.diag(*[int(e==1) for e in signs])/2
        general_phase=sp.I*(y.T*H*y)[0]+(Wref.T*y)[0]
        compact_phase=sp.I*(compact_z.T*H_EXPECTED*compact_z)[0]+(sp.Matrix([-2,-2,-1,1]).T*compact_z)[0]
        assert sp.expand(general_phase-compact_phase-sp.I*sp.Rational(27,35))==0
        reference_comparison={"same_shape_arguments_and_boundary_coordinate":True,
                              "positive_coarea_jacobian":1,
                              "general_state_to_recorded_compact_state_phase":"exp(27*pi*i/(70*h))"}
    return {"word":word,"tetrahedra":len(faces),"reduced_dimension":S.cols,
            "p":[str(q) for q in p],"beta_for_computed_alpha":str(beta),
            "beta_for_alpha_plus_two_longitudes":str(beta2),
            "meridian_and_longitude_projection_identities_exact":True,
            "reference_comparison":reference_comparison,
            "curve_marking_note":"alpha is the computed primitive class; standard S^3 marking requires the separate calibration."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words",nargs="*",default=["RL","RLRL","RRLR","RRLLL","RLRLRLRL"])
    args=parser.parse_args()
    result={"scope":"Exact diagnostics for the independent Gaussian-framing proof, without a meridian specialization.",
            "quantum_torus":quantum_torus_certificate(),"gaussian":gaussian_certificate(),"records":[]}
    for word in args.words:
        record=boundary_certificate(word)
        result["records"].append(record)
        print(json.dumps(record),flush=True)
    Path(__file__).with_name("boundary_framing_results.json").write_text(json.dumps(result,indent=2)+"\n")


if __name__=="__main__":
    main()
