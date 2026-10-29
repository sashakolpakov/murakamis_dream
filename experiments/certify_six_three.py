#!/usr/bin/env python3
"""Exact geometric, face, and preferred-longitude certificate for 6_3.

Only rational/polynomial arithmetic is used in the certificate. Root existence
uses an explicit Rouche inequality. Arguments are bounded with rational
alternating arctangent series. Optional Regina/SnapPy recognition is separate.
"""

import argparse
import json
from functools import reduce
from math import gcd, lcm
from pathlib import Path

import sympy as sp

from layered_two_bridge import layered_gluings, orientation_signs, regina_triangulation
from audit_two_bridge import ANGLE_INDEX, ordered_faces, parity
from twist_family_certificates import combinatorial_data
from twist_topology_audit import curve_chain, curve_holonomy, dual_complex, intersection


ORDERS = [(0, 1, 2, 3), (0, 1, 2, 3), (0, 2, 1, 3),
          (0, 1, 2, 3), (0, 2, 1, 3), (0, 2, 1, 3)]
# Exact relabelling from the folded-layer tetrahedra to the all-positive
# shape convention: z at 01, z' at 02, z'' at 03.
SHAPE_ORDERS = [(0, 1, 2, 3)] * 2 + [(0, 1, 3, 2)] * 2 + [(0, 1, 2, 3)] * 2
RAW_LOG_ROWS = [
 [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0],
 [0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0],
 [0,1,2,0,1,2,0,1,0,0,1,0,0,0,0,0,0,0],
 [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0],
 [0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0],
 [0,0,0,0,0,0,0,1,0,0,1,0,1,0,2,1,0,2],
 [0,-1,-1,1,0,0,-1,0,0,2,0,-1,0,-1,0,1,0,1],
 [1,0,0,1,0,0,0,0,-1,1,0,0,0,-1,0,0,-1,0],
]
ALPHA = [((0,1),0), ((3,1),3), ((1,1),2)]
BETA = [((0,2),3), ((1,3),1), ((2,3),0), ((5,3),1),
        ((4,3),2), ((5,2),0), ((2,2),1), ((0,1),3),
        ((1,1),0), ((0,0),2), ((2,0),3), ((4,0),2),
        ((5,0),1), ((4,1),2), ((5,1),2), ((3,2),0)]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(k, a):
    return (k*a[0], k*a[1]) if k >= 0 else (k*a[1], k*a[0])


def small_atan(q, terms=24):
    if q < 0:
        return scale(-1, small_atan(-q, terms))
    assert 0 <= q <= sp.Rational(1, 2)
    total = sum((-1)**k * q**(2*k+1) / (2*k+1) for k in range(terms))
    next_term = (-1)**terms * q**(2*terms+1) / (2*terms+1)
    return min(total, total+next_term), max(total, total+next_term)


PI = add(scale(16, small_atan(sp.Rational(1, 5))),
         scale(-4, small_atan(sp.Rational(1, 239))))


def atan(q):
    if q < 0:
        return scale(-1, atan(-q))
    if q > 1:
        return add(scale(sp.Rational(1, 2), PI), scale(-1, atan(1/q)))
    if q > sp.Rational(1, 2):
        return add(scale(sp.Rational(1, 4), PI), atan((q-1)/(q+1)))
    return small_atan(q)


def complex_l1(z):
    z = sp.expand(z)
    return abs(sp.re(z)) + abs(sp.im(z))


def disc_image(poly, variable, center, radius):
    w = sp.Symbol("w")
    expansion = sp.Poly(sp.expand(poly.subs(variable, center+w)), w)
    value = expansion.nth(0)
    bound = sum(complex_l1(expansion.nth(k))*radius**k
                for k in range(1, expansion.degree()+1))
    # A rectangular enclosure of the image of the closed complex disc.
    return (sp.re(value)-bound, sp.re(value)+bound,
            sp.im(value)-bound, sp.im(value)+bound)


def angle_intervals(box):
    # Outward rational rounding keeps the alternating-series denominators small.
    precision = 10**6
    x0, x1, y0, y1 = [sp.floor(t*precision)/precision if i % 2 == 0
                       else sp.ceiling(t*precision)/precision for i,t in enumerate(box)]
    assert x0 <= x1 and 0 < y0 <= y1
    def upper_arg(x,y):
        if x>0:
            return atan(y/x)
        if x<0:
            return add(PI,scale(-1,atan(-y/x)))
        return scale(sp.Rational(1,2),PI)
    def rectangle_arg(a,b,c,d):
        corners=[upper_arg(x,y) for x in (a,b) for y in (c,d)]
        return min(q[0] for q in corners),max(q[1] for q in corners)
    z = rectangle_arg(x0,x1,y0,y1)
    zp = rectangle_arg(1-x1,1-x0,y0,y1)
    zpp = add(PI, scale(-1, add(z, zp)))
    assert zpp[0] > 0
    return [z, zp, zpp]


def sum_intervals(coefficients, intervals):
    result = (sp.Integer(0), sp.Integer(0))
    for k, interval in zip(coefficients, intervals):
        result = add(result, scale(k, interval))
    return result


def verify_polynomial_row(row, p, a, b, c):
    u,v,z = sp.symbols("u v z")
    variables = [u,u,v,v,z,z]
    A = [row[3*j]-row[3*j+2] for j in range(6)]
    B = [row[3*j+2]-row[3*j+1] for j in range(6)]
    sign = (-sp.Integer(1))**sum(row[2::3])
    positive = sp.prod(variables[j]**max(A[j],0)*(1-variables[j])**max(B[j],0)
                       for j in range(6))
    negative = sign*sp.prod(variables[j]**max(-A[j],0)*(1-variables[j])**max(-B[j],0)
                            for j in range(6))
    substituted = sp.Poly(positive-negative,u,v,z).as_expr().subs(
        {u:a,v:b,z:c},simultaneous=True)
    assert sp.rem(sp.expand(substituted),p,c) == 0


def zero_winding(coefficients, intervals, target_multiple):
    bounds = sum_intervals(coefficients, intervals)
    shifted = add(bounds, scale(-2*target_multiple, PI))
    assert -PI[0] < shifted[0] <= shifted[1] < PI[0]
    return {"target_multiple_of_two_pi": target_multiple,
            "maximum_distance_bound": float(max(abs(t) for t in shifted))}


def geometry_certificate():
    c, w = sp.symbols("c w")
    p = c**6-3*c**5+5*c**4-4*c**3+2*c**2-c+1
    a = -c**5+2*c**4-3*c**3+2*c**2-c+1
    b = -c**5+3*c**4-5*c**3+4*c**2-c
    center = sp.Rational(841164, 10**6) + sp.I*sp.Rational(1200143, 10**6)
    radius = sp.Rational(1, 10**5)
    taylor = sp.Poly(sp.expand(p.subs(c, center+w)), w)
    derivative_lower = max(abs(sp.re(taylor.nth(1))), abs(sp.im(taylor.nth(1))))
    error_upper = complex_l1(taylor.nth(0)) + sum(
        complex_l1(taylor.nth(k))*radius**k for k in range(2, 7))
    linear_lower = derivative_lower*radius
    assert error_upper < linear_lower
    assert 20*error_upper < linear_lower
    boxes = [disc_image(f, c, center, radius) for f in (a,b,c)]
    assert all(0<box[0]<=box[1]<1 for box in boxes)
    args = [angle_intervals(box) for box in boxes]
    raw_args = [args[t//2][k] for t in range(6) for k in range(3)]
    # Verify all multiplicative edge equations and BOTH peripheral equations.
    for row in RAW_LOG_ROWS:
        verify_polynomial_row(row,p,a,b,c)
    windings = [zero_winding(row,raw_args,1 if j<6 else 0)
                for j,row in enumerate(RAW_LOG_ROWS)]
    ordered_args = []
    for t, order in enumerate(ORDERS):
        pmap = SHAPE_ORDERS[t]
        for k in (1,2,3):
            raw_index = ANGLE_INDEX[tuple(sorted((pmap[order[0]],pmap[order[k]])))]
            ordered_args.append(raw_args[3*t+raw_index])
    assert all(q[0] > sp.Rational(69,100) for q in ordered_args)
    return ordered_args, {"polynomial": str(p), "shape_a": str(a), "shape_b": str(b),
        "disc_center": str(center), "disc_radius": str(radius),
        "rouche_error_to_linear_upper_bound": str(error_upper/linear_lower),
        "shape_boxes": [[str(t) for t in box] for box in boxes],
        "all_eight_polynomial_residuals_zero_mod_p": True,
        "raw_log_winding_certificates": windings,
        "minimum_angle_lower_bound": float(min(q[0] for q in ordered_args))}


def ab(row, signs):
    row = list(row)
    gp = sp.Matrix(1,len(signs),[row[3*j+(2 if s==1 else 1)] for j,s in enumerate(signs)])
    gpp = sp.Matrix(1,len(signs),[row[3*j+(1 if s==1 else 2)] for j,s in enumerate(signs)])
    return sp.Matrix(1,len(signs),row[0::3])-gp, gpp-gp, -sum(gp)


def matrix_and_peripheral_certificate(ordered_args):
    gluings = layered_gluings("RLRL")
    faces = ordered_faces(gluings,ORDERS)
    signs = [e*parity(p) for e,p in zip(orientation_signs(gluings),ORDERS)]
    data = combinatorial_data(faces,signs)
    C = dual_complex(faces)
    assert C["smith"] == [1]*6
    constraints = C["boundary2"].T.col_join(sp.Matrix(len(C["tree"]),12,
                          lambda i,j:int(j==C["tree"][i])))
    h = constraints.nullspace()[0]
    h *= lcm(*[q.q for q in h])
    h /= reduce(gcd,[int(q) for q in h])
    alpha_chain, beta_chain = curve_chain(C,ALPHA),curve_chain(C,BETA)
    assert (h.T*alpha_chain)[0] == (h.T*beta_chain)[0] == 1
    assert intersection(signs,C["adjacency"],ALPHA,BETA) == -1
    longitude_chain = beta_chain-alpha_chain
    boundary = sp.Matrix([-3,1,-2,1,3,-1])
    assert C["boundary2"]*boundary == longitude_chain
    ah = curve_holonomy(faces,signs,C["adjacency"],ALPHA)
    lh = curve_holonomy(faces,signs,C["adjacency"],BETA)-ah
    # Independently verify the multiplicative equations of these explicit
    # normal cycles as well as their winding, rather than infer them from
    # the imported peripheral basis.
    c=sp.Symbol("c")
    polynomial=c**6-3*c**5+5*c**4-4*c**3+2*c**2-c+1
    shape_a=-c**5+2*c**4-3*c**3+2*c**2-c+1
    shape_b=-c**5+3*c**4-5*c**3+4*c**2-c
    for holonomy in (ah,lh):
        raw=[sp.Integer(0)]*18
        for t,order in enumerate(ORDERS):
            pmap=SHAPE_ORDERS[t]
            for k in (1,2,3):
                raw_index=ANGLE_INDEX[tuple(sorted((pmap[order[0]],pmap[order[k]])))]
                raw[3*t+raw_index]+=holonomy[3*t+k-1]
        verify_polynomial_row(raw,polynomial,shape_a,shape_b,c)
    # These winding bounds supplement the exact curve cycles and chain relation.
    alpha_winding = zero_winding(ah,ordered_args,0)
    longitude_winding = zero_winding(lh,ordered_args,0)
    rows = list(map(list,data["incidence"].tolist()))
    Aed = sp.Matrix.vstack(*[ab(row,signs)[0] for row in rows])
    Bed = sp.Matrix.vstack(*[ab(row,signs)[1] for row in rows])
    Al,Bl,nul = ab(lh,signs)
    Am,Bm,num = ab(ah,signs)
    G = -2*data["Qf"]+sp.diag(*[int(s==1) for s in signs])
    assert Aed == Bed*G and Al == Bl*G
    for omitted in range(6):
        selected = [j for j in range(6) if j!=omitted]
        A = Aed[selected,:].col_join(Al)
        B = Bed[selected,:].col_join(Bl)
        if B.det()!=0:
            break
    assert abs(B.det())==2 and B.inv()*A==G
    nu = sp.Matrix([2+ab(rows[j],signs)[2] for j in selected]+[nul])
    residual = Am-Bm*G
    pvec = 2*B.inv()[:,-1]
    assert residual == pvec.T
    gamma = sum(pvec)+(Bm*B.inv()*nu)[0]-num
    mixing = (Bm*B.inv())[0,-1]
    assert mixing == 0
    c0 = B.inv()*nu-G*sp.ones(6,1)
    # Check the source shape convention directly, rather than rely on
    # angle preservation to track the logarithmic moduli. The Gaussian's
    # global orientation uses inverse conjugates of the selected native quads.
    lower=sp.Symbol("lower")
    a_lower=shape_a.subs(c,lower)
    b_lower=shape_b.subs(c,lower)
    source_shapes=[1/a_lower,1/a_lower,b_lower/(b_lower-1),1/b_lower,1-lower,1-lower]
    source_polynomial=polynomial.subs(c,lower)
    for j,row in enumerate(rows+[list(ah),list(lh)]):
        aa,bb,nn=ab(row,signs)
        if j<6:
            nn+=2
        value=sp.prod(source_shapes[k]**aa[k]*(1-1/source_shapes[k])**bb[k] for k in range(6))
        numerator=sp.cancel(value-(-sp.Integer(1))**nn).as_numer_denom()[0]
        assert sp.rem(numerator,source_polynomial,lower)==0
    # Raw edge rows agree after the independently stated vertex relabelling.
    mapped = sp.zeros(6,18)
    for t,order in enumerate(ORDERS):
        q=SHAPE_ORDERS[t]
        for k in (1,2,3):
            raw_index=ANGLE_INDEX[tuple(sorted((q[order[0]],q[order[k]])))]
            mapped[:,3*t+k-1]=sp.Matrix([row[3*t+raw_index] for row in RAW_LOG_ROWS[:6]])
    assert sorted(map(tuple,mapped.tolist()))==sorted(map(tuple,data["incidence"].tolist()))
    return {"faces":faces,"signs":signs,"face_determinant":str(data["face_A"].det()),
            "all_edge_and_preferred_longitude_rows_agree":True,
            "literature_NZ_shapes_in_lower_root":list(map(str,source_shapes)),
            "literature_NZ_polynomial_residuals_exact":True,
            "longitude_homology_boundary_coefficients":list(map(int,boundary)),
            "alpha_beta_intersection":-1,"alpha_and_beta_linking_numbers":[1,1],
            "alpha_angle_coefficients":list(map(int,ah)),
            "preferred_longitude_angle_coefficients":list(map(int,lh)),
            "alpha_zero_winding":alpha_winding,"longitude_zero_winding":longitude_winding,
            "G":[[str(q) for q in row] for row in G.tolist()],
            "omitted_edge":omitted,"completed_B_determinant":str(B.det()),
            "p":[str(q) for q in pvec],"gamma":str(gamma),"c0_over_pi":[str(q) for q in c0],
            "boundary_polarization":"x=-H_alpha; Q=exp(H_alpha); E=exp(H_longitude/2)",
            "longitude_mixing_in_x":str(mixing),
            "alpha_normal_walk":ALPHA,"beta_normal_walk":BETA}


def topology_calibration():
    import snappy
    gluings = layered_gluings("RLRL")
    T = regina_triangulation(gluings)
    M = snappy.Manifold(T.snapPea())
    R = regina_triangulation(M._get_tetrahedra_gluing_data())
    f=T.isIsomorphicTo(R)
    assert f is not None
    assert [f.tetImage(t) for t in range(6)]==list(range(6))
    assert [tuple(f.facetPerm(t)[v] for v in range(4)) for t in range(6)]==SHAPE_ORDERS
    assert [list(map(int,row)) for row in M.gluing_equations()]==RAW_LOG_ROWS
    N=snappy.Manifold("6_3")
    isomorphism=next(k for k in M.isomorphisms_to(N) if k.cusp_maps()[0].det()==1)
    P=sp.Matrix(list(map(list,isomorphism.cusp_maps()[0])))
    assert P==sp.Matrix([[1,1],[-1,0]])
    # Inverse columns give the standard knot meridian and longitude in the
    # imported arbitrary basis. Their exact angle rows in our ordered data:
    mu=sp.Matrix([1,0,0,1,0,0,-1,0,0,1,0,0,-1,0,0,-1,0,0])
    ell=sp.Matrix([0,0,0,0,0,0,-1,1,0,-1,1,0,1,1,1,-1,-1,-1])
    inverse=P.inv()
    M.set_peripheral_curves([[int(inverse[k,j]) for k in range(2)] for j in range(2)])
    changed=[list(map(int,row)) for row in M.gluing_equations()]
    mapped=sp.zeros(18,2)
    for t,order in enumerate(ORDERS):
        pmap=SHAPE_ORDERS[t]
        for k in (1,2,3):
            old=ANGLE_INDEX[tuple(sorted((pmap[order[0]],pmap[order[k]])))]
            for j in range(2):
                mapped[3*t+k-1,j]=changed[-2+j][3*t+old]
    assert mapped==mu.row_join(ell)
    faces=ordered_faces(gluings,ORDERS)
    signs=[e*parity(p) for e,p in zip(orientation_signs(gluings),ORDERS)]
    data=combinatorial_data(faces,signs)
    C=dual_complex(faces)
    ah=curve_holonomy(faces,signs,C["adjacency"],ALPHA)
    lh=curve_holonomy(faces,signs,C["adjacency"],BETA)-ah
    constraints=sp.Matrix(6,18,lambda i,j:int(i==j//3)).col_join(data["incidence"])
    target=sp.Matrix([1]*6+[2]*6)
    certificates=[]
    for difference in (ah-mu,lh+ell):
        solution,parameters=constraints.T.gauss_jordan_solve(difference)
        solution=solution.subs({q:0 for q in parameters})
        assert (target.T*solution)[0]==0
        certificates.append(list(map(str,solution)))
    return {"regina_isosig":T.isoSig(),"combinatorial_isomorphisms_to_standard_6_3":len(M.isomorphisms_to(N)),
            "cusp_basis_matrix":[list(map(int,row)) for row in P.tolist()],
            "alpha_matches_standard_meridian_on_balanced_angles":True,
            "longitude_is_negative_standard_longitude":True,
            "angle_relation_certificates":certificates}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topology",action="store_true")
    args=parser.parse_args()
    intervals,geometry=geometry_certificate()
    matrix=matrix_and_peripheral_certificate(intervals)
    result={"scope":"Exact independent certificate for the specified 6_3 realization; no all-two-bridge claim.",
            "geometry":geometry,"matrices_and_peripherals":matrix}
    if args.topology:
        result["topology_calibration"]=topology_calibration()
    Path(__file__).with_name("six_three_certificate_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"rouche_ratio":float(sp.Rational(geometry["rouche_error_to_linear_upper_bound"])),
          "minimum_angle_radians":geometry["minimum_angle_lower_bound"],
          "face_determinant":matrix["face_determinant"],"B_determinant":matrix["completed_B_determinant"],
          "p":matrix["p"],"gamma":matrix["gamma"],"topology_calibration":args.topology},indent=2))


if __name__=="__main__":
    main()
