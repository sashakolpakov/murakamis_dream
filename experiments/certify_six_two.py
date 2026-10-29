#!/usr/bin/env python3
"""Exact singular-face state, geometric, and peripheral certificates for 6_2.

The existing charged tensor is Fourier-reduced before extracting its fiber.
Shape/root and all matrix/branch decisions use rational arithmetic. Optional
SnapPy/Regina calibration of the standard peripheral marking is separate.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from audit_two_bridge import ANGLE_INDEX, branchings, ordered_faces, parity
from certify_six_three import (ab, angle_intervals, complex_l1, disc_image,
                               verify_polynomial_row, zero_winding)
from layered_two_bridge import layered_gluings, orientation_signs, regina_triangulation
from reduce_singular_faces import exact_reduction, kernel, peripheral_cycles


RAW_LOG_ROWS = [
 [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0],
 [0,1,2,0,1,2,0,2,0,0,2,0,0,0,1,0,0,1],
 [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0],
 [0,0,0,0,0,0,1,0,0,1,0,0,2,0,1,2,0,1],
 [0,0,-1,0,-1,-1,0,-1,0,0,0,1,1,0,-1,-2,1,0],
 [0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,1,0,0],
]
SHAPE_ORDERS = [(0,1,2,3)]*2+[(0,1,3,2)]*2+[(0,1,2,3)]*2
SIMPLE_SUPPORT = sp.Matrix([[1,0,0,0],[0,1,0,0],[-1,-1,0,0],[-1,-1,0,0],
                            [0,0,1,0],[0,0,0,1]])
BETA0 = sp.Matrix([0,0,1,1,0,0])
H_EXPECTED = sp.Matrix([[-sp.Rational(3,2),-sp.Rational(3,2),-sp.Rational(3,2),sp.Rational(1,2)],
                        [-sp.Rational(3,2),-sp.Rational(3,2),-sp.Rational(3,2),sp.Rational(1,2)],
                        [-sp.Rational(3,2),-sp.Rational(3,2),-2,1],
                        [sp.Rational(1,2),sp.Rational(1,2),1,-sp.Rational(1,2)]])
REFERENCE = sp.Matrix([sp.Rational(j,7) for j in
                     [5,1,1,5,1,1,4,2,1,4,1,2,5,1,1,1,5,1]])


def json_matrix(M):
    return [[str(q) for q in row] for row in M.tolist()]


def geometric_certificate(orders,signs,data,peripheral):
    c,w = sp.symbols("c w")
    P = c**5-3*c**4+5*c**3-5*c**2+4*c-1
    a = c**3-2*c**2+2*c-1
    b = 2*c**4-5*c**3+8*c**2-7*c+6
    center = sp.Rational(1186078,10**6)+sp.I*sp.Rational(874646,10**6)
    radius = sp.Rational(1,10**5)
    taylor = sp.Poly(sp.expand(P.subs(c,center+w)),w)
    error = complex_l1(taylor.nth(0))+sum(complex_l1(taylor.nth(k))*radius**k for k in range(2,6))
    lower = radius*max(abs(sp.re(taylor.nth(1))),abs(sp.im(taylor.nth(1))))
    assert 10*error<lower
    boxes = [disc_image(f,c,center,radius) for f in (a,b,c)]
    angles = [angle_intervals(box) for box in boxes]
    assert all(q[0]>sp.Rational(1,4) for triple in angles for q in triple)
    raw_args = [angles[t//2][k] for t in range(6) for k in range(3)]
    for row in RAW_LOG_ROWS:
        verify_polynomial_row(row,P,a,b,c)
    raw_windings=[zero_winding(row,raw_args,1 if j<6 else 0) for j,row in enumerate(RAW_LOG_ROWS)]
    proper_args=[]
    for t,order in enumerate(orders):
        q=SHAPE_ORDERS[t]
        for k in (1,2,3):
            old=ANGLE_INDEX[tuple(sorted((q[order[0]],q[order[k]])))]
            proper_args.append(raw_args[3*t+old])
    peripheral_windings=[]
    for holonomy in (peripheral["alpha_holonomy"],peripheral["longitude_holonomy"]):
        raw=[sp.Integer(0)]*18
        for t,order in enumerate(orders):
            q=SHAPE_ORDERS[t]
            for k in (1,2,3):
                old=ANGLE_INDEX[tuple(sorted((q[order[0]],q[order[k]])))]
                raw[3*t+old]+=holonomy[3*t+k-1]
        verify_polynomial_row(raw,P,a,b,c)
        peripheral_windings.append(zero_winding(holonomy,proper_args,0))
    # The Gaussian signs use the opposite global orientation from the native
    # all-positive shape convention. On the lower root w=conj(c), the required
    # positive literature shapes are the rational functions below. This is a
    # uniform inversion/conjugation after choosing each new quad, not a
    # tetrahedron-by-tetrahedron inversion based on its individual sign.
    aw=a.subs(c,w)
    bw=b.subs(c,w)
    shapes=[1/aw,1/aw,1/bw,1/bw,1-w,1/w]
    Pw=P.subs(c,w)
    rows=list(data["incidence"].tolist())+[list(peripheral["alpha_holonomy"]),
                                        list(peripheral["longitude_holonomy"])]
    for j,row in enumerate(rows):
        A,B,nu=ab(row,signs)
        if j<6:
            nu+=2
        residual=sp.prod(shapes[k]**A[k]*(1-1/shapes[k])**B[k] for k in range(6))-(-sp.Integer(1))**nu
        numerator=sp.fraction(sp.cancel(residual))[0]
        assert sp.rem(numerator,Pw,w)==0
    # The affine support is y_0+y_1+y_2=i*pi, y_2=y_3.
    assert sp.rem(sp.together(aw**2*bw-1).as_numer_denom()[0],Pw,w)==0
    zero_winding([1,0,0,1,0,0,1,0,0]+[0]*9,proper_args,1)
    return {"polynomial":str(P),"shape_a":str(a),"shape_b":str(b),
            "disc_center":str(center),"disc_radius":str(radius),"rouche_ratio":str(error/lower),
            "shape_boxes":[list(map(str,box)) for box in boxes],
            "raw_edge_and_peripheral_polynomial_identities":True,
            "literature_NZ_polynomial_identities_in_lower_root":True,
            "raw_winding_certificates":raw_windings,"normal_peripheral_windings":peripheral_windings,
            "affine_support_branch_certified":True,
            "minimum_angle_lower_bound":float(min(q[0] for q in proper_args)),
            "geometric_literature_shapes_in_lower_root":list(map(str,shapes))}


def state_certificate(data,signs,peripheral):
    S=SIMPLE_SUPPORT
    change=data["Sinv"]*S
    assert data["S"]*change==S and change.det()==1
    assert data["normalization"]==1
    Si=(S.T*S).inv()*S.T
    n=6
    constraints=sp.Matrix(n,18,lambda i,j:int(j//3==i)).col_join(data["incidence"])
    rhs=sp.Matrix([1]*n+[2]*n)
    assert constraints*REFERENCE==rhs and min(REFERENCE)>0
    tangent=kernel(constraints)
    Aangle=sp.Matrix(n,18,lambda i,j:int(j==3*i))
    Cangle=sp.diag(*signs)*sp.Matrix(n,18,lambda i,j:int(j==3*i+2))
    dref=sp.ones(n,1)-Aangle*REFERENCE
    assert S*Si*(dref-BETA0)==dref-BETA0
    assert (sp.eye(n)-S*Si)*Aangle*tangent==sp.zeros(n,tangent.cols)
    longitude=peripheral["longitude_holonomy"].T
    meridian=peripheral["alpha_holonomy"].T
    assert (longitude*REFERENCE)[0]==0
    Wref=2*data["Qambient"]*dref-Cangle*REFERENCE
    Wvar=(-2*S.T*data["Qambient"]*Aangle-S.T*Cangle)*tangent
    lambda_var=longitude*tangent
    chosen=next(j for j in range(lambda_var.cols) if lambda_var[j])
    p=2*Wvar[:,chosen]/lambda_var[chosen]
    assert p==sp.Matrix([-1,-1,-1,1]) and Wvar==p*lambda_var/2
    mu_difference=-p.T*Si*Aangle-meridian
    affine,parameters=constraints.T.gauss_jordan_solve(mu_difference.T)
    affine=affine.subs({q:0 for q in parameters})
    gamma=(p.T*Si*(sp.ones(n,1)-BETA0))[0]+(rhs.T*affine)[0]
    assert gamma==0
    H=data["Qambient"]-sp.diag(*[int(e==1) for e in signs])/2
    Hred=S.T*H*S
    linear=S.T*Wref-2*S.T*H*BETA0
    phase_constant=-(BETA0.T*H*BETA0)[0]+(Wref.T*BETA0)[0]
    assert Hred==H_EXPECTED and linear==sp.Matrix([-2,-2,-1,1])
    assert phase_constant==sp.Rational(27,35)
    # Exact classical critical-equation certificates, including constants.
    G=data["Gambient"]
    offset=linear+S.T*G*(sp.ones(n,1)-BETA0)
    edge_coordinates=Si*data["Bed"].T
    assert edge_coordinates.rank()==3 and p.T*edge_coordinates==sp.zeros(1,6)
    classical=[]
    rows=list(data["incidence"].tolist())+[list(peripheral["alpha_holonomy"]),
                                        list(peripheral["longitude_holonomy"])]
    for j,row in enumerate(rows):
        A,B,nu=ab(row,signs)
        if j<6:
            nu+=2
        assert S*Si*B.T==B.T
        R=A-B*G
        constant=(R*(sp.ones(n,1)-BETA0))[0]+((Si*B.T).T*offset)[0]-nu
        assert constant==0
        if j<6:
            assert R*S==sp.zeros(1,4)
        else:
            classical.append({"row":j,"residual_on_support":list(map(str,R*S)),
                              "B_coordinate_pairing_with_p":str(((Si*B.T).T*p)[0])})
    assert classical[0]["residual_on_support"]==["1","1","1","-1"]
    assert classical[0]["B_coordinate_pairing_with_p"]=="0"
    assert classical[1]["residual_on_support"]==["0"]*4
    assert classical[1]["B_coordinate_pairing_with_p"]=="2"
    # A square collection of the edge/longitude equations forces all four
    # full critical equations at the complete geometric point.
    _,Bl,_=ab(peripheral["longitude_holonomy"],signs)
    assert edge_coordinates.row_join(Si*Bl.T).rank()==4
    return {"S":json_matrix(S),"Hred":json_matrix(Hred),"linear":list(map(str,linear)),
            "reference_angles_over_pi":list(map(str,REFERENCE)),
            "p":list(map(str,p)),"gamma":str(gamma),"normalization":str(data["normalization"]),
            "removed_constant_phase":"exp(27*pi*i/(70*h))",
            "affine_angle_relations_exact":True,"critical_equations_and_constants_exact":True,
            "classical_peripheral_rows":classical,
            "classical_polarization":"Q=exp(-H_alpha); E=exp(H_l/2)",
            "quantum_parameter":"q=exp(2*pi*i*b^2); h=b^2/(1+b^2)^2"}


def topology_calibration(gluings,orders,peripheral,data):
    import snappy
    T=regina_triangulation(gluings)
    M=snappy.Manifold(T.snapPea())
    R=regina_triangulation(M._get_tetrahedra_gluing_data())
    f=T.isIsomorphicTo(R)
    assert [f.tetImage(t) for t in range(6)]==list(range(6))
    assert [tuple(f.facetPerm(t)[v] for v in range(4)) for t in range(6)]==SHAPE_ORDERS
    assert [list(map(int,row)) for row in M.gluing_equations()]==RAW_LOG_ROWS
    N=snappy.Manifold("6_2").canonical_retriangulation()
    candidates=M.isomorphisms_to(N)
    iso=next(k for k in candidates if k.cusp_maps()[0].det()==1)
    P=sp.Matrix(list(map(list,iso.cusp_maps()[0])))
    inverse=P.inv()
    M.set_peripheral_curves([[int(inverse[k,j]) for k in range(2)] for j in range(2)])
    raw=[list(map(int,row)) for row in M.gluing_equations()]
    marked=sp.zeros(18,2)
    for t,order in enumerate(orders):
        q=SHAPE_ORDERS[t]
        for k in (1,2,3):
            old=ANGLE_INDEX[tuple(sorted((q[order[0]],q[order[k]])))]
            for j in range(2):
                marked[3*t+k-1,j]=raw[-2+j][3*t+old]
    constraints=sp.Matrix(6,18,lambda i,j:int(j//3==i)).col_join(data["incidence"])
    target=sp.Matrix([1]*6+[2]*6)
    # The exact equality on balanced angles includes the affine constant.
    augmented=marked.col_join(sp.zeros(1,2)).row_join(constraints.T.col_join(target.T))
    comparison=[]
    for holonomy in (peripheral["alpha_holonomy"],peripheral["longitude_holonomy"]):
        solution,parameters=augmented.gauss_jordan_solve(holonomy.col_join(sp.zeros(1,1)))
        solution=solution.subs({q:0 for q in parameters})
        comparison.append(list(map(str,solution[:2,0])))
    return {"regina_isosig":T.isoSig(),"combinatorial_isomorphisms_to_canonical_6_2":len(candidates),
            "cusp_basis_matrix":json_matrix(P),"alpha_and_l_in_standard_meridian_longitude":comparison}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topology",action="store_true")
    args=parser.parse_args()
    gluings=layered_gluings("RRLR")
    orders=next(branchings(gluings,10000))
    faces=ordered_faces(gluings,orders)
    signs=[e*parity(p) for e,p in zip(orientation_signs(gluings),orders)]
    data=exact_reduction(faces,signs)
    peripheral=peripheral_cycles(faces,signs,data)
    geometry=geometric_certificate(orders,signs,data,peripheral)
    state=state_certificate(data,signs,peripheral)
    result={"scope":"Exact certificate for the Fourier-reduced literature tensor and its selected 6_2 fiber; no uniform all-knot claim.",
            "faces":faces,"signs":signs,"orders":orders,
            "face_rank":data["D"].col_join(data["R"]).rank(),
            "kernel_dimension":data["K"].cols,"fourier_constraint_rank":data["C"].rank(),
            "reduced_dimension":data["S"].cols,"geometry":geometry,"state":state,
            "peripheral":{"alpha":peripheral["alpha"],"beta":peripheral["beta"],
               "beta_linking":peripheral["beta_linking"],"intersection":peripheral["intersection"],
               "longitude_boundary_coefficients":list(map(str,peripheral["longitude_boundary"])),
               "alpha_holonomy":list(map(str,peripheral["alpha_holonomy"])),
               "longitude_holonomy":list(map(str,peripheral["longitude_holonomy"]))}}
    if args.topology:
        result["topology_calibration"]=topology_calibration(gluings,orders,peripheral,data)
    Path(__file__).with_name("six_two_certificate_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"rouche_ratio":float(sp.Rational(geometry["rouche_ratio"])),
         "minimum_angle_lower_bound":geometry["minimum_angle_lower_bound"],
         "face_rank":result["face_rank"],"reduced_dimension":result["reduced_dimension"],
         "critical_equations_exact":True,"topology":result.get("topology_calibration")},indent=2))


if __name__=="__main__":
    main()
