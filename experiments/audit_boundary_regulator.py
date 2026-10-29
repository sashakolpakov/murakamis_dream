#!/usr/bin/env python3
"""Exact branch, connection, norm and affine-centering certificates.

All parameters are symbolic. The Darboux diagnostic has two independent
edge constraints and the recorded full peripheral pairing -2. It checks
the reference term and volume-norm constants without a knot example.
"""

import json
from pathlib import Path

import sympy as sp


def primitive_certificate():
    u,v=sp.symbols("u v")
    k=sp.Symbol("k",integer=True);w=u+v+sp.pi*sp.I*k
    polynomial=u*w/2+sp.pi*sp.I*k*u/2
    assert sp.expand(-w+sp.diff(polynomial,u)+v/2)==0
    assert sp.expand(sp.diff(polynomial,v)-u/2)==0
    ur,ui,vr,vi,lr,li=sp.symbols("ur ui vr vi LiReal LiImag",real=True)
    uc=ur+sp.I*ui;vc=vr+sp.I*vi;wc=uc+vc+sp.pi*sp.I*k
    T=lr+sp.I*li+uc*wc/2+sp.pi*sp.I*k*uc/2
    D=li+ur*sp.im(wc)
    assert sp.expand(sp.im(T)-D+(ur*vi-vr*ui)/2)==0
    return {"matched_logarithms_and_branch_integer_symbolic":True,
            "dT_half_symplectic_potential_exact":True,
            "imaginary_part_Bloch_Wigner_identity_exact":True}


def line_certificate():
    a,b,c,d=sp.symbols("a b c d",integer=True)
    U,V=sp.symbols("U V")
    exponent=(b*(U+2*sp.pi*sp.I*c)-a*(V+2*sp.pi*sp.I*d)
              +d*U-c*V-((b+d)*U-(a+c)*V))
    assert sp.expand(exponent-2*sp.pi*sp.I*(b*c-a*d))==0
    assert sp.simplify(sp.exp(exponent))==1
    dU,dV=sp.symbols("dU dV")
    A=-(U*dV-V*dU)/(2*sp.pi*sp.I)
    shifted=A.subs({U:U+2*sp.pi*sp.I*a,V:V+2*sp.pi*sp.I*b},simultaneous=True)
    assert sp.expand(shifted-A-(b*dU-a*dV))==0
    ur,ui,vr,vi=sp.symbols("ur ui vr vi",real=True)
    B=ur*vi-vr*ui
    shifted_B=B.subs({ui:ui+2*sp.pi*a,vi:vi+2*sp.pi*b},simultaneous=True)
    assert sp.expand(shifted_B-B-2*sp.pi*(b*ur-a*vr))==0
    return {"peripheral_deck_action_composes_exactly":True,
            "connection_automorphy_exact":True,
            "Hermitian_norm_deck_invariance_exact":True}


def centered_reduction_certificate():
    re_u=sp.symbols("ru0:3",real=True);im_u=sp.symbols("iu0:3",real=True)
    ref_u=sp.symbols("a0:3",real=True)
    nu0,nu1,rv,iv,beta=sp.symbols("nu0 nu1 rv iv beta",real=True)
    u=sp.Matrix([re_u[i]+sp.I*im_u[i] for i in range(3)])
    v=sp.Matrix([sp.I*nu0,sp.I*nu1,rv+sp.I*iv])
    u0=sp.I*sp.Matrix(ref_u);v0=sp.I*sp.Matrix([nu0,nu1,beta])
    du=sp.Matrix(sp.symbols("du0:3"));dv2=sp.Symbol("dv2");dv=sp.Matrix([0,0,dv2])
    omega=lambda a,b,c,d:(a.dot(d)-b.dot(c))
    U=u[2]-u0[2];V=-2*(v[2]-v0[2])
    dU=du[2];dV=-2*dv2
    centered=omega(u-u0,v-v0,du,dv)
    assert sp.expand(centered+(U*dV-V*dU)/2)==0
    # Removing the centering term is detected for generic affine data.
    uncentered=omega(u,v,du,dv)
    assert sp.expand(uncentered-centered)!=0
    R=sp.re(u);I=sp.im(u);S=sp.re(v);J=sp.im(v)
    sympl_real_imag=omega(R,S,I-sp.Matrix(ref_u),J-sp.Matrix([nu0,nu1,beta]))
    boundary_B=sp.re(U)*sp.im(V)-sp.re(V)*sp.im(U)
    assert sp.expand(sympl_real_imag+boundary_B/2)==0
    volume=sp.Symbol("Volume",real=True)
    imaginary_period=volume-sympl_real_imag/2
    log_absolute_period=2*imaginary_period/sp.pi
    log_norm=log_absolute_period-boundary_B/(2*sp.pi)
    assert sp.expand(log_norm-2*volume/sp.pi)==0
    return {"two_affine_edge_constraints_and_all_coordinates_symbolic":True,
            "full_peripheral_pairing":-2,
            "centered_symplectic_reduction_exact":True,
            "omitting_reference_term_detected":True,
            "log_norm_equals_two_volume_over_pi_exact":True}


def quantum_constants_certificate():
    n=sp.Symbol("n",integer=True,positive=True)
    h=n/(n+1)**2;volume=sp.Symbol("Volume",real=True)
    required_logJ=-volume/(2*sp.pi*h)
    assert sp.cancel(4*h*required_logJ+2*volume/sp.pi)==0
    return {"h_at_rational_level":"n/(n+1)^2",
            "four_h_log_J_plus_classical_log_norm_has_correct_constants":True,
            "quantum_norm_comparison_proved":False}


def main():
    result={"scope":"Exact classical boundary period and volume norm; no quantum growth claim.",
            "primitive":primitive_certificate(),"line":line_certificate(),
            "coisotropic_centering":centered_reduction_certificate(),
            "quantum_comparison_constants":quantum_constants_certificate()}
    Path(__file__).with_name("boundary_regulator_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
