#!/usr/bin/env python3
"""Exact rational-period transport, Koszul and residue diagnostics.

No knot examples are inputs. Generic coupled two-variable data check the
translation and gluing formulae. An actual Faddeev-ratio period is a
negative control for localization only at gluing solutions.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_local_completion import phi_original_integral


def literature_change_certificate():
    n=sp.Symbol("n",positive=True,integer=True);L=sp.Symbol("L",positive=True,integer=True)
    z=sp.Matrix(sp.symbols("z1 z2"));t0=sp.Symbol("t0")
    h00,h01,h02,h11,h12,h22=sp.symbols("h00 h01 h02 h11 h12 h22")
    H=sp.Matrix([[h00,h01,h02],[h01,h11,h12],[h02,h12,h22]])
    c=sp.Matrix(sp.symbols("c0:3"));v0,v1,v2,rho=sp.symbols("v0 v1 v2 rho")
    tint=L*z/(2*sp.pi*sp.sqrt(n));physical=sp.Matrix([t0,*tint])
    Qb=(n+1)/sp.sqrt(n);cb=sp.I*Qb/2
    original=(sp.pi*sp.I*(physical.T*H*physical)[0]+Qb*sp.pi*c.dot(physical))
    A=L**2*H[1:,1:]
    linear=L*((n+1)*c[1:,0]/(2*n)+sp.I*t0*H[1:,0]/sp.sqrt(n))
    constant=sp.pi*sp.I*h00*t0**2+Qb*sp.pi*c[0]*t0
    transformed=sp.I*(z.T*A*z)[0]/(4*sp.pi*n)+linear.dot(z)+constant
    assert sp.expand(original-transformed)==0
    xi=2*sp.pi*sp.sqrt(n)*v0*t0+2*sp.pi*sp.I*(n+1)*(rho+sp.Rational(1,2))
    Farg=(L*(v1*z[0]+v2*z[1])+xi)/(2*sp.pi*sp.sqrt(n))-cb
    Phiarg=v0*t0+v1*tint[0]+v2*tint[1]+sp.I*Qb*rho
    assert sp.simplify(Farg-Phiarg)==0
    assert sp.simplify(tint.jacobian(z).det()-(L/(2*sp.pi*sp.sqrt(n)))**2)==0
    logQ=-2*sp.pi*t0/sp.sqrt(n)
    assert sp.simplify(xi+n*v0*logQ-2*sp.pi*sp.I*(n+1)*(rho+sp.Rational(1,2)))==0
    return {"all_rational_literature_coefficients_symbolic":True,
            "Gaussian_linear_and_boundary_constant_transform_exact":True,
            "Faddeev_argument_transform_exact":True,"Jacobian_exact":True,
            "generic_Q_to_the_n_peripheral_factor_retained":True}


def coupled_translation_certificate():
    x,y,a,b,c,lam1,lam2,tau=sp.symbols("x y a b c lambda1 lambda2 tau",nonzero=True)
    q=tau**2;A=sp.Matrix([[1,1],[1,2]])
    vectors=[sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([1,1])]
    arguments=[a*x,b*y,c*x*y]
    def local_ratio(argument,m):
        if m>=0:return sp.prod(1/(1-q**r*argument) for r in range(m))
        return sp.prod(1-q**r*argument for r in range(m,0))
    def ratio(k):
        k=sp.Matrix(k);Ak=A*k
        return (tau**(-(k.T*A*k)[0])*lam1**k[0]*lam2**k[1]
                *x**(-Ak[0])*y**(-Ak[1])
                *sp.prod(local_ratio(arg,int(v.dot(k))) for arg,v in zip(arguments,vectors)))
    examples=[((1,0),(0,1)),((1,1),(-1,0)),((-1,2),(1,-1))]
    for k,l in examples:
        shifted=ratio(l).subs({x:q**k[0]*x,y:q**k[1]*y},simultaneous=True)
        total=tuple(k[i]+l[i] for i in range(2))
        assert sp.cancel(ratio(total)-ratio(k)*shifted)==0
    return {"quantum_half_phase_and_root_parameters_indeterminate":True,
            "coupled_translation_cocycle_exact":True,
            "negative_and_mixed_shifts_checked":True,
            "analytic_quantum_half_phase_was_not_dropped":True}


def cyclic_algebra_certificate(n):
    H,T1,T2,H1,H2=sp.symbols("H T1 T2 H1 H2")
    shift=sp.zeros(n)
    for j in range(n):shift[(j+1)%n,j]=H if j==n-1 else 1
    E=sp.eye(n)
    source=sp.Matrix.hstack(*[E[:,j] for j in range(n-1)],sp.ones(n,1))
    target=sp.Matrix.hstack(*[E[:,j]-E[:,j+1] for j in range(n-1)],E[:,0])
    assert abs(source.det())==1 and abs(target.det())==1
    assert (E-shift)*source==target*sp.diag(*([1]*(n-1)+[1-H]))
    trace=sum((shift**k for k in range(n)),sp.zeros(n))
    projector=trace.subs(H,1)/n
    assert projector*projector==projector and sp.trace(projector)==1
    N=sp.prod(sum(T**j for j in range(n)) for T in [T1,T2])
    expression=sp.expand((1-T1)*(1-T2)*N)
    assert sp.expand(expression.subs({T1**n:H1,T2**n:H2},simultaneous=True)-(1-H1)*(1-H2))==0
    return {"level":n,"one_minus_shift_unimodular_Koszul_reduction_exact":True,
            "no_central_norm_factor_inverted":True,"two_dimensional_cube_identity_exact":True,
            "orbit_sum_to_average_factor":n*n,"joint_projector_rank_per_factor":1}


def norm_certificate(n):
    q,X=sp.symbols("q X")
    field=sp.QQ.frac_field(X)
    modulus=sp.Poly(sp.cyclotomic_poly(n,q),q,domain=field)
    product=sp.Poly(sp.prod(1-q**j*X for j in range(n)).expand(),q,domain=field)
    assert product.rem(modulus).as_expr()==1-X**n
    return {"level":n,"generic_cyclic_norm_exact":True,
            "Gaussian_coarse_phases_for_diagonals_1_and_2":[(-1)**n,1]}


def coupled_residue_certificate():
    t=sp.Matrix(sp.symbols("t1 t2",nonzero=True));a,b,c,C1,C2=sp.symbols("a b c C1 C2")
    A=sp.Matrix([[1,1],[1,2]])
    vectors=[sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([1,1])]
    arguments=[a*t[0],b*t[1],c*t[0]*t[1]]
    H=sp.Matrix([C1/(t[0]*t[1]*(1-arguments[0])*(1-arguments[2])),
                 C2/(t[0]*t[1]**2*(1-arguments[1])*(1-arguments[2]))])
    Hess=-A
    for argument,v in zip(arguments,vectors):Hess+=argument/(1-argument)*(v*v.T)
    for i in range(2):
        for j in range(2):assert sp.cancel(t[j]*sp.diff(H[i],t[j])/H[i]-Hess[i,j])==0
    point={t[0]:2,t[1]:3,a:sp.Rational(1,5),b:sp.Rational(1,7),c:sp.Rational(1,11),
           C1:sp.Rational(18,11),C2:sp.Rational(360,77)}
    assert H.subs(point)==sp.ones(2,1)
    hessian=Hess.subs(point)
    assert hessian.det()==-sp.Rational(1,12)
    G=sp.ones(2,1)-H
    jacobian=G.jacobian(t).subs(point)
    numerator=1+t[0]+2*t[1]
    residue_t=(numerator/(t[0]*t[1])).subs(point)/jacobian.det()
    residue_log=numerator.subs(point)/hessian.det()
    assert residue_t==residue_log==-108
    return {"all_coupled_gluing_parameters_symbolic":True,
            "logarithmic_gluing_Jacobian_equals_symmetric_Hessian":True,
            "isolated_diagnostic_point":[2,3],"Hessian_determinant":"-1/12",
            "Leray_residue_in_t_and_log_t_coordinates":str(residue_log),
            "logarithmic_measure_factor_retained":True}


def source_pole_counterexample(n):
    mp.mp.dps=48
    fn=lambda z:1/(2*mp.cosh(z/(2*n)))
    delta=2j*mp.pi
    kernel=lambda z:sum(fn(z+delta*k) for k in range(n))/2
    base=mp.mpc('.7','.2')
    assert abs(fn(base+n*delta)/fn(base)+1)<mp.mpf('1e-43')
    assert abs((kernel(base)-kernel(base+delta))/fn(base)-1)<mp.mpf('1e-43')
    integral=mp.quad(fn,[-mp.inf,0,mp.inf])
    assert abs(integral-n*mp.pi)<mp.mpf('1e-42')
    radius=mp.mpf('0.1');number=64;pole=mp.pi*1j
    residue=radius*sum(kernel(pole+radius*mp.exp(2j*mp.pi*k/number))
                       *mp.exp(2j*mp.pi*k/number) for k in range(number))/number
    assert abs(residue+n*.5j)<mp.mpf('1e-42')
    assert abs(2j*mp.pi*residue-integral)<mp.mpf('1e-40')
    return {"level":n,"coarse_multiplier":-1,"gluing_solutions":[],
            "nonzero_integral":str(integral),"expected_integral":"n*pi",
            "folded_source_pole":"pi*i","residue_expected":"-i*n/2",
            "circle_residue_and_real_integral_agree":True,
            "automatic_gluing_point_only_localization_rejected":True,
            "volume_conjecture_counterexample_claimed":False}


def source_divisor_certificate(n):
    order=lambda ell:-((ell-1)//n)
    for ell in range(-4*n,4*n+1):
        assert order(ell+n)==order(ell)-1
        assert order(ell+1)-order(ell)==(-1 if ell%n==0 else 0)
    for v in [(1,0),(1,1),(2,-3),(-2,1),(-1,-1)]:
        positive=sum(max(x,0) for x in v)
        negative=sum(min(x,0) for x in v)
        for fraction in [sp.Rational(1,4),sp.Rational(1,3),sp.Rational(2,5)]:
            gamma=(n+1)*fraction
            lower=int(sp.floor(gamma+n*negative))-1
            upper=int(sp.ceiling(gamma+n*positive))+1
            for ell in range(lower,upper):
                if gamma+n*negative<=ell<=gamma+n*positive:
                    assert max(0,-order(ell))<=positive
    t=sp.Symbol("t",nonzero=True)
    # The positive-factor counterexample has A=-1, v=1,-1 and a=-1.
    H=-t*(1+t)**(-1)*(1+1/t)
    assert sp.cancel(H+1)==0
    gamma=sp.Rational(n+2,2)
    assert 0<gamma<n+1
    z=sp.Symbol("z");Z=z/(2*sp.pi*sp.sqrt(n));shift=sp.I/(2*sp.sqrt(n))
    combined=(z/(2*n)-sp.I*sp.pi*(Z-shift)**2
              -sp.I*sp.pi*(n+sp.Rational(1,n))/12)
    expected=-sp.I*z*z/(4*sp.pi*n)+sp.I*sp.pi*(sp.Rational(2,n)-n)/12
    assert sp.expand(combined-expected)==0
    return {"level":n,"divisor_orders_from_both_translation_recurrences_exact":True,
            "uniform_pole_bound_for_mixed_sign_vectors_checked":True,
            "same_coorientation_norm_orders_cancel_source_poles":True,
            "positive_factors_without_coorientation_negative_control":True,
            "counterexample_has_exact_positive_pair_expression":True}


def regular_boundary_specialization(n):
    mp.mp.dps=48
    q=mp.exp(2j*mp.pi/n);b=1/mp.sqrt(n);cb=.5j*(b+1/b)
    xi=1j*mp.pi*(n+2)
    constant=mp.exp(1j*mp.pi*(mp.mpf(2)/n-n)/12)
    records=[]
    for size in ['0.001','0.00001']:
        alpha=mp.mpf(size);beta=2*alpha
        a=-mp.exp(alpha);a2=-mp.exp(beta)
        tstar=(1-a2)/(a-1)
        z=mp.log(-tstar)+1j*mp.pi
        F1=phi_original_integral(b,(z+xi+alpha)/(2*mp.pi*mp.sqrt(n))-cb)
        F2=phi_original_integral(b,(-z+xi+beta)/(2*mp.pi*mp.sqrt(n))-cb)
        f=constant*mp.exp(-1j*z*z/(4*mp.pi*n))*F1*F2
        x1=mp.exp((z+xi+alpha)/n);x2=mp.exp((-z+xi+beta)/n)
        orbit=[]
        for k in range(n):
            first=mp.fprod(1/(1-q**r*x1) for r in range(k))
            second=mp.fprod(1-q**r*x2 for r in range(-k,0))
            orbit.append(mp.exp(k*z/n+1j*mp.pi*k*k/n)*first*second)
        derivative_G=tstar*(1-a*a2)/(1-a*tstar)**2
        residue=f*sum(orbit)/derivative_G
        period=2j*mp.pi*residue
        error=abs(period/(n*mp.pi)-1)
        records.append({"shift_size":size,"root":str(tstar),
                        "relative_error_from_regular_value":str(error)})
    assert mp.mpf(records[1]['relative_error_from_regular_value'])<mp.mpf(records[0]['relative_error_from_regular_value'])/30
    assert mp.mpf(records[1]['relative_error_from_regular_value'])<mp.mpf('.001')
    return {"level":n,"method":"Defining Phi integrals and exact finite-shift sum at the moving gluing point",
            "regular_special_value":"n*pi","root_meets_removed_polar_divisor":True,
            "diagnostic_not_a_semiclassical_limit":True,"records":records}


def main():
    result={"scope":"Exact rational-state period pairing and its polar-cycle obligations; no all-knot volume claim.",
            "literature_change":literature_change_certificate(),
            "coupled_translation":coupled_translation_certificate(),
            "cyclic_Koszul":[cyclic_algebra_certificate(n) for n in [3,5,9,15]],
            "generic_norms":[norm_certificate(n) for n in [3,5,9]],
            "coupled_residue":coupled_residue_certificate(),
            "source_divisor_criterion":[source_divisor_certificate(n) for n in [3,5,9,15]],
            "source_pole_negative_controls":[source_pole_counterexample(n) for n in [3,5,9]],
            "regular_boundary_specializations":[regular_boundary_specialization(n) for n in [3,5]],
            "remaining":"Transport and localization of the selected global cycle; quantum regulator norm across levels."}
    Path(__file__).with_name("rational_period_pushforward_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
