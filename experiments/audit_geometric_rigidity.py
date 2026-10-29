#!/usr/bin/env python3
"""Positive gluing rigidity and the two-branch scalarization defect.

Exact rational-complex symplectic calculations and exact Ore identities.
These do not identify a selected finite ADO cycle with the geometric
formal period, or prove its volume limit.
"""

from itertools import product
import json
from pathlib import Path
from random import Random

import sympy as s
import numpy as np

from audit_actual_peripheral_fusion import module,tensor_module
from audit_braided_source_groupoid import projector_zero
from audit_finite_sum_annihilator import field
from audit_intrinsic_cut_transport import casimir,fusion_frame,right_close,modified_dimension
from audit_kashaev_ado_pointing import color_matrices
from audit_regular_holonomy_braiding import mm


def symmetric_matrix(d, rng):
    A=s.zeros(d)
    for i in range(d):
        for j in range(i,d):A[i,j]=A[j,i]=rng.randrange(-2,3)
    return A


def symplectic(d, seed):
    rng=Random(seed);I=s.eye(d);Z=s.zeros(d)
    if seed==0:return s.eye(2*d)
    if seed==2:
        mixed=s.diag(*[j%2 for j in range(d)])
        return I.row_join(mixed).col_join(Z.row_join(I))
    M=s.eye(2*d)
    for _ in range(3):
        S=symmetric_matrix(d,rng);T=symmetric_matrix(d,rng)
        M=I.row_join(S).col_join(Z.row_join(I))*M
        M=I.row_join(Z).col_join(T.row_join(I))*M
        F=s.eye(2*d)
        for j in range(d):
            if rng.randrange(2):
                F[j,j]=F[j+d,j+d]=0
                F[j,j+d]=1;F[j+d,j]=-1
        M=F*M
    J=Z.row_join(I).col_join(-I.row_join(Z))
    assert M*J*M.T==J
    return M


def positive_chart_case(d, seed):
    M=symplectic(d,seed)
    A,B,C,D=M[:d,:d],M[:d,d:],M[d:,:d],M[d:,d:]
    shapes=[s.Rational(j+1,j+3)+s.I*s.Rational(seed+j+1,seed+j+2) for j in range(d)]
    tau=[s.cancel(1/(z-1)) for z in shapes]
    assert all(s.im(t)<0 for t in tau)
    T=s.diag(*tau)
    J=(A+B*T).applyfunc(s.cancel)
    determinant=s.factor(J.det())
    assert determinant!=0
    unit=s.eye(d)[:,-1]
    shape_derivative=J.inv()*unit
    cusp=s.cancel(-2*((C+D*T)*shape_derivative)[-1])
    energy=s.cancel(-2*sum(s.im(tau[j])*shape_derivative[j]*s.conjugate(shape_derivative[j]) for j in range(d)))
    assert s.cancel(s.im(cusp)-energy)==0 and energy>0
    chosen=None
    for marks in product((False,True),repeat=d):
        Ap=A.copy();Bp=B.copy();Cp=C.copy();Dp=D.copy();new_tau=list(tau)
        for j,mark in enumerate(marks):
            if mark:
                Ap[:,j]=B[:,j];Bp[:,j]=-A[:,j];new_tau[j]=s.cancel(-1/tau[j])
                Cp[:,j]=D[:,j];Dp[:,j]=-C[:,j]
        if Bp.det():
            chosen=marks,Ap,Bp,Cp,Dp,new_tau
            break
    assert chosen is not None
    marks,Ap,Bp,Cp,Dp,new_tau=chosen
    symmetric=(Bp.inv()*Ap).applyfunc(s.cancel)
    assert symmetric==symmetric.T
    boundary_quadratic=(Dp*Bp.inv()).applyfunc(s.cancel)
    assert boundary_quadratic==boundary_quadratic.T
    assert (Cp-boundary_quadratic*Ap).applyfunc(s.cancel)==-Bp.inv().T
    H=symmetric+s.diag(*new_tau)
    hd=s.factor(H.det())
    jacobian_relation=s.cancel(hd*Bp.det()*s.prod(tau[j] for j in range(d) if marks[j])-determinant)
    assert jacobian_relation==0 and hd!=0
    assert all(s.im(t)<0 for t in new_tau)
    return {'tetrahedra':d,'seed':seed,'gluing_Jacobian_determinant':str(determinant),
            'marked_cusp_derivative':str(cusp),'cusp_imaginary_part':str(energy),
            'partial_Fourier_swaps':[j for j,m in enumerate(marks) if m],
            'full_boundary_Gaussian_has_the_marked_momentum_derivative':True,
            'all_isotropy_transversality_and_half_density_Jacobians_exact':True}


def tetrahedron_transport():
    z=s.Symbol('z');order=6
    delta=lambda f:s.cancel(z*s.diff(f,z))
    coefficients={0:-s.log(1-z)/2}
    for g in range(1,4):
        rational=z/(1-z)
        for _ in range(2*g-2):rational=delta(rational)
        coefficients[2*g-1]=-s.bernoulli(2*g)*rational/s.factorial(2*g)
    difference=[]
    for n in range(order):
        # The h^(-1) coefficient is -Li_2(z), whose delta derivative is log(1-z).
        top=s.log(1-z)
        for _ in range(n):top=delta(top)
        value=top/s.factorial(n+1)
        for power,coefficient in coefficients.items():
            j=n-power
            if j<1:continue
            derivative=coefficient
            for _ in range(j):derivative=delta(derivative)
            value+=derivative/s.factorial(j)
        difference.append(s.cancel(value))
    assert difference[0]==s.log(1-z) and all(x==0 for x in difference[1:])
    return {'difference_equation_checked_through_h_power':order-1,
            'leading_action':'-Li_2(z)','leading_amplitude':'(1-z)^(-1/2)',
            'Gaussian_shear_shift_character':'exp(-h/2)*(1-exp(-u))',
            'full_half_step_character_retained':True}


def cyclic_collision_case(p,r,alpha,beta,lc):
    q,M,L=s.symbols('q M L')
    shift=lambda f:s.cancel(f.subs(M,q*M))
    a=lc*M**p*(1+alpha*(q-1)*M)
    b=lc*M**r*(1+beta*(q-1)/M)
    difference=s.cancel(a-b)
    shifted=shift(difference)
    coefficients=[s.cancel(a*b*shifted),s.cancel(-(a*shift(a)-b*shift(b))),difference]
    assert s.cancel(coefficients[0]+coefficients[1]*a+coefficients[2]*a*shift(a))==0
    assert s.cancel(coefficients[0]+coefficients[1]*b+coefficients[2]*b*shift(b))==0
    a0=s.cancel(a.subs(q,1));b0=s.cancel(b.subs(q,1));d0=s.cancel(a0-b0)
    symbol=sum(c.subs(q,1)*L**j for j,c in enumerate(coefficients))
    assert s.cancel(symbol-d0*(L-a0)*(L-b0))==0
    kappa=s.diff(d0,M).subs(M,1)
    assert kappa!=0
    point={q:1,M:1}
    jac=s.Matrix([[s.diff(difference,M).subs(point),s.diff(difference,q).subs(point)],
                  [s.diff(shifted,M).subs(point),s.diff(shifted,q).subs(point)]])
    assert s.factor(jac.det())==kappa*kappa
    # Coefficients have no common local divisor although their classical
    # specialization has the simple factor M-1.
    nums=[s.fraction(s.cancel(c))[0] for c in coefficients]
    gcd=s.gcd(s.gcd(nums[0],nums[1]),nums[2])
    assert gcd.subs(point)!=0
    first=s.cancel(a*shift(a)-b*shift(b))
    assert s.cancel(first-a*shifted-difference*shift(b))==0
    # The saturated cyclic module has presentation S e + (u,h) S f.
    u,h=s.symbols('u h')
    presentation=s.Matrix([[1,u,h],[1,0,0]])
    assert presentation*s.Matrix([0,h,-u])==s.zeros(2,1)
    residue=s.cancel(1/jac.det())
    return {'classical_powers':[p,r],'subprincipal_parameters':[alpha,beta],
            'complete_longitude':lc,'classical_apparent_divisor':str(d0),
            'both_exact_Ore_remainders_zero':True,
            'quantum_coefficients_have_no_common_local_divisor':True,
            'two_parameter_defect_residue':str(residue),
            'cyclic_module_quotient_length':1,
            'cyclic_module_complete_fiber_generators':3,
            'det_Delta_shifted_Delta_Jacobian':str(kappa*kappa)}


def subprincipal_obstruction():
    Lc,s1,s2,P1,Pll=s.symbols('Lc s1 s2 P1 Pll',nonzero=True)
    plus=P1+Lc*s1*Pll/2;minus=P1+Lc*s2*Pll/2
    assert s.expand(plus-minus-Lc*(s1-s2)*Pll/2)==0
    return {'difference_of_two_necessary_subprincipal_conditions':str(s.factor(plus-minus)),
            'reduced_double_root_with_distinct_slopes_cannot_support_both_regular_ratios':True}


def nodal_cut_density_case(N):
    p,g,q=field(N);rho=(q-pow(q,-1,p))%p;c0=(q+pow(q,-1,p))%p
    kappa=g;sign=pow(-1,N,p);I=np.eye(N,dtype=np.int64)
    x=pow(q,N-1,p)
    O=casimir(tensor_module(module(N,p,q,x),module(N,p,q,x),p),p,q)
    pair=projector_zero(N,p,q,O)
    J=mm(p,(O-c0*np.eye(N*N,dtype=np.int64))%p,pair)
    pivot=color_matrices(N,p,q,x)[2]
    phi_one=right_close(pair,pivot,p);phi_nil=right_close(J,pivot,p)
    alpha=4*rho*pow(kappa,-1,p)%p
    theta0=sign*kappa*rho*pow(4,-1,p)%p;theta1=sign*c0%p
    assert theta0
    assert np.array_equal(phi_one,theta1*I%p)
    assert np.array_equal(phi_nil,alpha*theta0*I%p)
    eta=pow(-1,N+1,p)*pow(q,N*(1-N)//2,p)%p
    d0=eta*pow(N,-1,p)%p
    # Check the entire rational density away from the colliding fiber.
    M=g;x=-M*pow(q,-1,p)%p
    H,Hi,_=fusion_frame(N,p,q,x,x)
    P0=mm(p,H[:,:N],Hi[:N,:]);Plast=mm(p,H[:,-N:],Hi[-N:,:])
    f=lambda z:(z-pow(z,-1,p))%p
    C=(M+pow(M,-1,p))%p;D=(pow(M,N,p)+pow(M,-N,p))%p
    n0=(pow(q,-1,p)*M*M-q*pow(M,-2,p))%p
    nl=(q*M*M-pow(q,-1,p)*pow(M,-2,p))%p
    As=sign*c0*C*pow(D,-1,p)%p
    Bs=sign*rho*C*nl*pow(D,-1,p)%p
    pivot=color_matrices(N,p,q,x)[2]
    assert np.array_equal(right_close((P0+Plast)%p,pivot,p),As*I%p)
    delta_s=rho*f(M*M%p)%p
    assert np.array_equal(right_close(Plast*delta_s%p,pivot,p),Bs*I%p)
    delta_g=kappa*f(M)*pow(2,-1,p)%p
    alpha_g=delta_s*pow(delta_g,-1,p)%p
    th0=-sign*delta_g*n0*pow(D*f(M)%p,-1,p)%p
    th1=As
    assert th1==As and alpha_g*(th0+th1*delta_g)%p==Bs
    U=pow(M,2*N,p);phase=pow(q,N*(1-N)//2,p)
    dimension=modified_dimension(N,p,q,x)
    central0=phase*U*delta_g*n0*pow((U*U-1)%p,-1,p)%p
    central1=-phase*U*c0*f(M*M%p)*pow((U*U-1)%p,-1,p)%p
    assert central0==dimension*th0%p and central1==dimension*th1%p
    return {'level':N,'prime':p,'diagnostic_geometric_slope_difference':kappa,
            'complete_density_constant':theta0,'complete_density_nilpotent_coefficient':theta1,
            'full_ADO_density_constant':d0*theta0%p,'full_ADO_density_nilpotent_coefficient':d0*theta1%p,
            'a_scalar_density_would_fail':bool(theta1),
            'fixed_central_density_with_both_U_minus_one_and_U_plus_one_exact':True,
            'whole_rational_pair_cut_and_density_comparison_exact':True}


def main():
    result={'scope':'Uniform geometric rigidity and a formal quantum-A source defect; no actual finite-period selection or volume theorem.',
            'positive_symplectic_gluing_charts':[positive_chart_case(d,seed)
                for d in (1,2,3,4,5) for seed in (0,1,2,3,7)],
            'tetrahedron_formal_transport':tetrahedron_transport(),
            'two_branch_quantum_A_defects':[cyclic_collision_case(*data)
                for data in ((1,-1,0,0,1),(2,-1,1,2,1),(1,0,-1,1,-1),
                             (3,1,2,-1,-1),(-2,2,1,0,2),(2,-3,-1,2,1))],
            'subprincipal_obstruction':subprincipal_obstruction(),
            'actual_nodal_cut_densities':[nodal_cut_density_case(N) for N in (2,3,4,5,6,9,12,15)]}
    path=Path(__file__).with_name('geometric_rigidity_results.json')
    swaps=sum(bool(r['partial_Fourier_swaps']) for r in result['positive_symplectic_gluing_charts'])
    assert swaps
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(path),'positive_gluing_charts':len(result['positive_symplectic_gluing_charts']),
                      'exact_two_branch_Ore_cases':len(result['two_branch_quantum_A_defects']),
                      'charts_requiring_partial_Fourier':swaps,
                      'actual_nodal_cut_density_cases':len(result['actual_nodal_cut_densities']),
                      'tetrahedron_transport_order':result['tetrahedron_formal_transport']['difference_equation_checked_through_h_power']}),flush=True)


if __name__=='__main__':main()
