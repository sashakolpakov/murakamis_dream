#!/usr/bin/env python3
"""Exact checks for Fourier recovery of the tensor-derived meridian state.

The six-tetrahedron fixture has a moving longitude plane. Its complete
positive shapes, gluing branches, reference angles and symplectic identities
are certified independently of the numerical search that located it.
Optional topology calibration replays three legal Pachner moves from the
already audited three-tetrahedron twist-knot chart.
"""

import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_two_bridge import ANGLE_INDEX, ordered_faces, transformed_incidence
from certify_six_three import (PI, ab, angle_intervals, complex_l1,
                               disc_image, zero_winding)
from reduce_singular_faces import exact_reduction, kernel, peripheral_cycles


FACES = [("f0","f2","f1","f3"), ("f1","f2","f4","f5"),
         ("f6","f4","f7","f8"), ("f5","f9","f10","f7"),
         ("f3","f11","f10","f8"), ("f9","f11","f0","f6")]
SIGNS = [1,-1,-1,-1,1,-1]
ORDERS = [(0,2,1,3),(0,3,1,2),(0,1,2,3),(0,1,2,3),(0,1,3,2),(1,2,0,3)]
RAW_ROWS = [
 [0,0,0,0,0,1,0,2,0,0,0,1,0,0,1,1,0,0],
 [1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0],
 [1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0],
 [0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,2],
 [0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0],
 [0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0],
 [0,0,0,0,0,-1,0,0,1,0,0,0,0,1,0,0,0,1],
 [0,0,1,0,-2,2,0,0,-3,0,2,0,0,-5,0,0,0,-1],
]
MOVES = [(1,1),(0,3),(2,0)]
ISOSIG = "gLLPQcdefeffikdqhtk"


def matrix_json(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def rational_disc_image(function, variable, center, radius):
    numerator,denominator=sp.fraction(sp.cancel(function))
    nb=disc_image(numerator,variable,center,radius)
    db=disc_image(denominator,variable,center,radius)
    nc=sp.expand(numerator.subs(variable,center))
    dc=sp.expand(denominator.subs(variable,center))
    ne=(nb[1]-nb[0])/2
    de=(db[1]-db[0])/2
    lower=max(abs(sp.re(dc)),abs(sp.im(dc)))-de
    assert lower>0
    value=sp.cancel(nc/dc)
    error=(ne+complex_l1(value)*de)/lower
    return (sp.re(value)-error,sp.re(value)+error,
            sp.im(value)-error,sp.im(value)+error)


def geometry_certificate():
    a,w=sp.symbols("a w")
    P=a**3+3*a*a+2*a+1
    center=sp.Rational(-337641021,10**9)+sp.I*sp.Rational(562279512,10**9)
    radius=sp.Rational(1,10**8)
    expansion=sp.Poly(sp.expand(P.subs(a,center+w)),w)
    error=complex_l1(expansion.nth(0))+sum(
        complex_l1(expansion.nth(k))*radius**k for k in (2,3))
    lower=radius*max(abs(sp.re(expansion.nth(1))),abs(sp.im(expansion.nth(1))))
    assert 10*error<lower
    native=[a,a,(a+2)/a**2,a-1,a*a/((a-1)*(a+2)),-(a+1)**2/a]
    triple=lambda q:[q,1/(1-q),1-1/q]
    native_triples=[triple(q) for q in native]
    boxes=[rational_disc_image(q,a,center,radius) for q in native]
    native_angles=[angle_intervals(box) for box in boxes]
    native_flat=sum(native_triples,[])
    native_angle_flat=sum(native_angles,[])

    def polynomial_identity(value):
        num,den=sp.fraction(sp.cancel(value))
        assert sp.rem(num,P,a)==0
        # Every possible denominator is nonzero throughout the isolating disc.
        box=rational_disc_image(den,a,center,radius)
        assert not(box[0]<=0<=box[1] and box[2]<=0<=box[3])

    native_branches=[]
    for j,row in enumerate(RAW_ROWS):
        polynomial_identity(sp.prod(q**k for q,k in zip(native_flat,row))-1)
        native_branches.append(zero_winding(row,native_angle_flat,1 if j<6 else 0))
    proper=[]
    physical_angles=[]
    for t,order in enumerate(ORDERS):
        for k in (1,2,3):
            old=ANGLE_INDEX[tuple(sorted((order[0],order[k])))]
            physical_angles.append(native_angles[t][old])
            if k==1:
                proper.append(native_triples[t][old])
    proper_angles=[angle_intervals(rational_disc_image(q,a,center,radius)) for q in proper]
    physical=transformed_incidence(RAW_ROWS,ORDERS)
    # Reverse the source longitude so the audited intersection convention is +1.
    physical[-1,:]=-physical[-1,:]
    proper_branches=[]
    for j,row in enumerate(physical.tolist()):
        A,B,nu=ab(row,SIGNS)
        target=nu+(2 if j<6 else 0)
        polynomial_identity(sp.prod(proper[t]**A[t]*(1-1/proper[t])**B[t]
                                   for t in range(6))-(-sp.Integer(1))**target)
        coefficients=[c for t in range(6) for c in (A[t],0,B[t])]
        branch=zero_winding(coefficients,sum(proper_angles,[]),target/2)
        branch["target_multiple_of_two_pi"]=str(target/2)
        proper_branches.append(branch)
    minimum=min(q[0] for q in physical_angles)
    assert minimum>sp.Rational(1,100)
    result={"polynomial":str(P),"root_center":str(center),"root_radius":str(radius),
            "rouche_remainder_to_linear_bound":float(error/lower),
            "native_shapes":[str(q) for q in native],
            "literature_shapes":[str(q) for q in proper],
            "minimum_physical_angle_lower_bound":float(minimum),
            "native_multiplicative_equations_and_branches":native_branches,
            "literature_multiplicative_equations_and_branches":proper_branches,
            "orientation_note":"The positive native quads themselves satisfy these source equations; no inverse-conjugation is made."}
    return result,a,P,proper,physical,physical_angles


def linear_certificate(data,physical,physical_angles):
    n=len(FACES);S=data["S"];G=data["Gambient"]
    edge=data["Aed"].row_join(data["Bed"])
    Am,Bm,_=ab(physical[-2,:],SIGNS)
    Al,Bl,_=ab(physical[-1,:],SIGNS)
    assert (Am*Bl.T-Bm*Al.T)[0]==-2
    selected=list(edge.T.rref()[1])
    A=data["Aed"][selected,:].col_join(Al)
    B=data["Bed"][selected,:].col_join(Bl)
    assert data["Bed"].rank()==B.rank()==S.cols==4
    assert S*data["Sinv"]*Bl.T==Bl.T
    assert S.T*(Al.T-G*Bl.T)==sp.zeros(S.cols,1)
    # Compare the longitude to an independently nullhomologous normal curve.
    curves=peripheral_cycles(FACES,SIGNS,data)
    An,Bn,_=ab(curves["longitude_holonomy"],SIGNS)
    normal_rows=edge[selected,:].col_join(An.row_join(Bn))
    longitude_coeffs,parameters=normal_rows.T.gauss_jordan_solve(Al.row_join(Bl).T)
    assert parameters.rows==0 and abs(longitude_coeffs[-1])==1
    sums=sp.Matrix(n,3*n,lambda i,j:int(j//3==i))
    constraints=sums.col_join(data["incidence"]).col_join(physical[-2:,:])
    rhs=sp.ones(n,1).col_join(2*sp.ones(n,1)).col_join(sp.zeros(2,1))
    solution,parameters=constraints.gauss_jordan_solve(rhs)
    replacements={}
    for parameter in parameters:
        i=next(i for i,value in enumerate(solution) if value==parameter)
        mid=float(sum(physical_angles[i])/2)/float(sum(PI)/2)
        replacements[parameter]=sp.Rational(round(1000*mid),1000)
    reference=solution.subs(replacements)
    assert constraints*reference==rhs and min(reference)>0
    tangent_rhs=sp.zeros(constraints.rows,1);tangent_rhs[-1]=1
    direction,parameters=constraints.gauss_jordan_solve(tangent_rhs)
    direction=direction.subs({p:0 for p in parameters})
    first=sp.Matrix(n,3*n,lambda i,j:int(j==3*i))
    dprime=sp.Matrix(n,3*n,lambda i,j:int(j==3*i+(1 if SIGNS[i]==1 else 2)))
    d0=sp.ones(n,1)-first*reference
    W0=dprime*reference-G*d0
    a1=first*direction;b1=dprime*direction;d1=-a1;W1=b1-G*d1
    Sext=S.row_join(-d1)
    assert Sext.rank()==S.cols+1
    zero_peripheral=kernel(constraints)
    dd=-first*zero_peripheral
    dW=dprime*zero_peripheral-G*dd
    assert S*data["Sinv"]*dd==dd and S.T*dW==sp.zeros(S.cols,dd.cols)
    assert d1.T*dW-W1.T*dd==sp.zeros(1,dd.cols)
    # Keep both peripheral variables free on the entire balanced angle space.
    balanced=kernel(sums.col_join(data["incidence"]))
    mu_row=physical[-2,:]*balanced
    lambda_row=physical[-1,:]*balanced
    assert mu_row.col_join(lambda_row).rank()==2
    dd_general=-first*balanced-d1*lambda_row
    dW_general=(dprime+G*first)*balanced-W1*lambda_row
    assert S*data["Sinv"]*dd_general==dd_general
    assert S.T*dW_general==sp.zeros(S.cols,balanced.cols)
    assert d1.T*dW_general-W1.T*dd_general==-mu_row/2
    z=sp.Matrix(sp.symbols(f"z0:{S.cols}"));tau,x=sp.symbols("tau x")
    perp=kernel(S.T);kappa=sp.Matrix(sp.symbols(f"k0:{perp.cols}"))
    r=S*z-tau*d1;D=-tau*W1+perp*kappa
    u=-r;v=G*r+D
    assert sp.simplify(data["Aed"]*u+data["Bed"]*v)==sp.zeros(n,1)
    assert sp.expand((Al*u+Bl*v)[0]+tau)==0
    Hm=(Am*u+Bm*v)[0]
    canonical=(b1.T*u-a1.T*v)[0]
    assert sp.expand(canonical+Hm/2)==0
    derivative=-sp.I*(d1.T*D)[0]+sp.I*(W1.T*r)[0]-sp.I*x/2
    assert sp.expand(derivative-sp.I*(Hm-x)/2)==0
    result={"tetrahedra":n,"kernel_dimension":data["K"].cols,
            "reduced_dimension":S.cols,"edge_B_rank":data["Bed"].rank(),
            "edge_and_longitude_B_rank":B.rank(),"extended_rank":Sext.rank(),
            "reduction_constant":str(data["normalization"]),
            "reference_angles_in_pi_units":[str(q) for q in reference],
            "angle_direction":[str(q) for q in direction],
            "transverse_d1":[str(q) for q in d1],"W1":[str(q) for q in W1],
            "preferred_longitude_normal_curve_coefficient":str(longitude_coeffs[-1]),
            "preferred_longitude_dual_boundary":[str(q) for q in curves["longitude_boundary"]],
            "zero_peripheral_variations_checked":zero_peripheral.cols,
            "balanced_angle_dimension":balanced.cols,"peripheral_variation_rank":2,
            "general_mu_lambda_phase_and_contour_identity_exact":True,
            "path_phase_and_contour_tau_cancellation_exact":True,
            "critical_equations":"H_edge=0, H_l=-tau, partial_tau F=i(H_m-x)/2"}
    return result,reference,d0,W0,d1,W1


def fourier_constants():
    h,beta,tau,u=sp.symbols("h beta tau u",positive=True)
    # Completing the tau square gives the old exact Fresnel kernel.
    phase=-beta*tau*tau/(8*sp.pi*h)+tau*u/(4*sp.pi*h)
    assert sp.expand(phase+beta*(tau-u/beta)**2/(8*sp.pi*h)-u*u/(8*sp.pi*beta*h))==0
    inverse_normalization=1/(8*sp.pi**2*h)
    fresnel_squared=8*sp.pi**2*h/(sp.I*beta)
    old_normalization_squared=1/(8*sp.pi**2*h*sp.I*beta)
    assert sp.cancel(inverse_normalization**2*fresnel_squared-old_normalization_squared)==0
    return {"inverse_fourier_prefactor":"1/(8*pi^2*h)",
            "ordinary_fiber_gaussian_recovered_exactly":True,
            "square_root_branch":"sqrt(2*i*beta)=sqrt(2*abs(beta))*exp(i*pi*sign(beta)/4)",
            "beta_zero_limit":"delta(p.z-x), with positive coarea measure"}


def saddle_diagnostic(data,proper,variable,reference,d0,W0,d1,W1):
    mp.mp.dps=70
    root=mp.findroot(lambda a:a**3+3*a*a+2*a+1,mp.mpc('-.337641','.562280'))
    cv=lambda q:mp.mpf(str(q.p))/int(q.q) if q.is_Rational else mp.mpc(str(sp.re(q).evalf(75)),str(sp.im(q).evalf(75)))
    q=[mp.mpc(str(sp.re(f.subs(variable,sp.Float(str(root.real),75)+sp.I*sp.Float(str(root.imag),75))).evalf(75)),
                str(sp.im(f.subs(variable,sp.Float(str(root.real),75)+sp.I*sp.Float(str(root.imag),75))).evalf(75))) for f in proper]
    mat=lambda M:mp.matrix([[cv(t) for t in row] for row in M.tolist()])
    y=mp.matrix([-mp.log(t)+mp.pi*1j for t in q])
    S=mat(data["S"]);Sinv=mat(data["Sinv"]);G=mat(data["Gambient"])
    dref=mp.pi*mat(d0);Wref=mp.pi*mat(W0);r=y-1j*dref
    residual=mp.norm(r-S*Sinv*r)
    D=mp.matrix([mp.log(1-1/t) for t in q])-1j*mp.pi*mat(
        sp.Matrix([reference[3*j+(1 if SIGNS[j]==1 else 2)] for j in range(6)]))-G*r
    gradient=mp.norm(S.T*D)
    tau_gradient=abs(-1j*(mat(d1).T*D)[0]+1j*(mat(W1).T*r)[0])
    F=(-.5j*(y.T*G*y)[0]+(Wref.T*y)[0]
       -1j*sum(mp.polylog(2,-mp.exp(t)) for t in y))
    volume=sum(mp.im(mp.polylog(2,t))+mp.arg(1-t)*mp.log(abs(t)) for t in q)
    assert residual<mp.mpf('1e-55') and gradient<mp.mpf('1e-55')
    assert tau_gradient<mp.mpf('1e-55') and abs(F.real+volume)<mp.mpf('1e-55')
    return {"numerical_diagnostic_only":True,"precision_digits":70,
            "affine_plane_residual":float(residual),"internal_gradient_residual":float(gradient),
            "new_transverse_gradient_residual":float(tau_gradient),
            "volume":mp.nstr(volume,45),"real_saddle_phase":mp.nstr(F.real,45)}


def topology_calibration():
    import snappy,regina
    from layered_two_bridge import regina_triangulation
    from twist_family_certificates import twist_faces
    from twist_topology_audit import pairings,peripheral_audit
    initial=snappy.Manifold("5_2")
    family,_=twist_faces(0,"odd")
    T=regina.Triangulation3()
    for _ in family:T.newTetrahedron()
    _,adjacency=pairings(family)
    for (t,f),(u,_,p,_,sign) in adjacency.items():
        if sign==1:T.tetrahedron(t).join(f,T.tetrahedron(u),regina.Perm4(*[p[v] for v in range(4)]))
    iso=T.isIsomorphicTo(regina_triangulation(initial._get_tetrahedra_gluing_data()))
    assert iso is not None
    peripheral_audit(0,"odd")  # Includes the independently marked meridian certificate.
    marked_meridian=sp.zeros(9,1)
    for t,coefficient in [(0,1),(1,-1)]:
        p=iso.facetPerm(t);image=iso.tetImage(t)
        marked_meridian[3*image+ANGLE_INDEX[tuple(sorted((p[0],p[1])))]]+=coefficient
    original_rows=sp.Matrix([list(map(int,row)) for row in initial.gluing_equations()])
    sums=sp.Matrix(3,9,lambda i,j:int(j//3==i))
    marking_system=sums.col_join(original_rows)
    coefficients,parameters=marking_system.T.gauss_jordan_solve(marked_meridian)
    coefficients=coefficients.subs({p:0 for p in parameters})
    assert list(coefficients[-2:,:])==[-1,0]
    assert sum(coefficients[:3,:])+2*sum(coefficients[3:6,:])==0
    signatures=[]
    for t,f in MOVES:
        R=regina_triangulation(initial._get_tetrahedra_gluing_data())
        assert R.pachner(R.tetrahedron(t).triangle(f))
        assert initial._two_to_three(t,f)==0
        assert R.isIsomorphicTo(regina_triangulation(initial._get_tetrahedra_gluing_data())) is not None
        signatures.append(initial.triangulation_isosig(decorated=False))
    assert initial.triangulation_isosig(decorated=False)==ISOSIG
    assert ordered_faces(initial._get_tetrahedra_gluing_data(),ORDERS)==FACES
    assert [list(map(int,row)) for row in initial.gluing_equations()]==RAW_ROWS
    return {"initial_isomorphic_to_independently_audited_twist_chart":True,
            "initial_twist_isosig":T.isoSig(),"moves":[list(t) for t in MOVES],
            "marked_twist_meridian_in_source_basis":[-1,0],
            "initial_meridian_additive_angle_correction":0,
            "each_move_legal_independently_in_regina":True,"intermediate_isosigs":signatures,
            "peripheral_incidence_rows_reproduced":True,
            "quantum_state_move_identity_asserted":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topology",action="store_true")
    args=parser.parse_args()
    geometry,variable,P,proper,physical,physical_angles=geometry_certificate()
    data=exact_reduction(FACES,SIGNS)
    linear,reference,d0,W0,d1,W1=linear_certificate(data,physical,physical_angles)
    result={"scope":"Independent moving-plane meridian-state audit; quantum factors are not specialized.",
            "manifold":"5_2","isosig":ISOSIG,"geometry":geometry,
            "linear_algebra":linear,"fourier_normalization":fourier_constants(),
            "saddle_diagnostic":saddle_diagnostic(data,proper,variable,reference,d0,W0,d1,W1)}
    if args.topology:result["topology_calibration"]=topology_calibration()
    Path(__file__).with_name("fourier_boundary_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
