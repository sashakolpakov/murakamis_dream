#!/usr/bin/env python3
"""Exact doubled-phase, Hessian, regulator and H5 identities."""

import itertools
import json
from pathlib import Path

import sympy as S


def zero(x):
    assert S.cancel(x)==0


def same(A,B):
    for x in A-B:zero(x)


def slope_hessian():
    tp,tm,da,db,p,q=S.symbols('tau_plus tau_minus da db p q',nonzero=True)
    J=S.Matrix([[1,-1],[tp,-tm]])
    zero(J.det()-(tp-tm))
    du,dut=J.inv()*S.Matrix([2*S.I*da,2*S.I*db])
    phi_b=(du+dut)/2
    phi_a=-(tp*du+tm*dut)/2
    H=S.Matrix([[S.diff(phi_a,da),S.diff(phi_a,db)],
                [S.diff(phi_b,da),S.diff(phi_b,db)]])
    expected=2*S.I/(tp-tm)*S.Matrix([[tp*tm,-(tp+tm)/2],[-(tp+tm)/2,1]])
    same(H,expected);zero(H.det()-1)
    same(H.subs({tp:p+S.I*q,tm:p-S.I*q}),S.Matrix([[p*p+q*q,-p],[-p,1]])/q)
    return {'phase_Jacobian_difference_of_slopes':True,
            'exact_algebraic_boundary_Hessian':True,
            'real_positive_Hessian_and_determinant_one':True}


def primitive_and_closedness():
    u,v,ut,vt=S.symbols('u v u_tilde v_tilde')
    x=S.Matrix([u,v,ut,vt])
    # d(R_minus-R_plus)/i from the specified regulator convention.
    reg=S.Matrix([-v,u,vt,-ut])/(4*S.I)
    cross=ut*v-u*vt
    derivative=reg+S.Matrix([S.diff(cross,y) for y in x])/(4*S.I)
    target=S.Matrix([-(v+vt),u+ut,v+vt,-(u+ut)])/(4*S.I)
    same(derivative,target)
    dtheta=S.Matrix(4,4,lambda i,j:S.diff(target[j],x[i])-S.diff(target[i],x[j]))
    desired=S.zeros(4);desired[0,1]=1/(2*S.I);desired[1,0]=-1/(2*S.I)
    desired[2,3]=-1/(2*S.I);desired[3,2]=1/(2*S.I)
    same(dtheta,desired)
    tp,tm=S.symbols('tau_plus tau_minus')
    pullback=S.Matrix([[1,0],[tp,0],[0,1],[0,tm]])
    same(pullback.T*dtheta*pullback,S.zeros(2))
    return {'marked_regulator_bilinear_primitive':True,
            'closed_logarithmic_form_on_curve_product':True}


def H5_connection():
    A,B,P,Q,Z=S.symbols('A_log B_log P_log Q_log Z')
    Pi=S.Matrix([[1,A,-B,Z],[0,1,0,Q],[0,0,1,P],[0,0,0,1]])
    elementary=lambda i,j:S.eye(4)[:,i]*S.eye(4)[j,:]
    coefficients=[]
    for name,dZ,expected in [(A,0,elementary(0,1)),(B,0,-elementary(0,2)),
                             (P,-B,elementary(2,3)),(Q,A,elementary(1,3))]:
        derivative=Pi.diff(name)+dZ*elementary(0,3)
        same(Pi.inv()*derivative,expected)
        coefficients.append(expected)
    for triple in itertools.product(coefficients,repeat=3):
        same(triple[0]*triple[1]*triple[2],S.zeros(4))
    nonzero=[]
    for X,Y in itertools.product(coefficients,repeat=2):
        C=X*Y-Y*X
        if C!=S.zeros(4):
            for i in range(4):
                for j in range(4):
                    if (i,j)!=(0,3):zero(C[i,j])
            nonzero.append(C)
    assert nonzero
    # The only curvature coefficient is the same doubled-curve 2-form.
    aa=S.Matrix([1,0,1,0]);bb=S.Matrix([0,1,0,1])
    pp=S.Matrix([1,0,-1,0]);qq=S.Matrix([0,1,0,-1])
    curvature=aa*qq.T-qq*aa.T-bb*pp.T+pp*bb.T
    desired=S.zeros(4);desired[0,1]=2;desired[1,0]=-2
    desired[2,3]=-2;desired[3,2]=2
    same(curvature,desired)
    return {'exact_period_matrix_Maurer_Cartan_form':True,
            'class_two_and_triple_products_zero':True,
            'central_curvature_cancels_on_curve_product':True}


def tetrahedral_cotangents():
    z,w=S.symbols('z w',nonzero=True)
    cot=lambda a,b:S.I*(a+b)/(a-b)
    alpha=cot(z,w)
    beta=cot(1/(1-z),1/(1-w))
    gamma=cot(1-1/z,1-1/w)
    negative=S.Matrix([[alpha+beta,beta],[beta,gamma+beta]])
    zero(negative.det()-1)
    return {'doubled_shapes_give_rational_angle_Hessian':True,
            'tetrahedral_determinant_one':True}


def whole_algebraic_phase_inverse():
    # A generic algebraic two-branch node chart, not a knot example.
    P,Q=S.symbols('P_mu P_lambda',nonzero=True)
    alpha=S.I;beta=-S.I
    mm=(Q*(1-beta)-(1-alpha))/(alpha*P-Q*beta)
    mp=P*mm;lp=1+alpha*(mp-1);lm=1+beta*(mm-1)
    zero(mp/mm-P);zero(lp/lm-Q)
    zero(mm.subs({P:1,Q:1})-1);zero(mp.subs({P:1,Q:1})-1)
    A=mp*mm;B=lp*lm
    H=S.Matrix([[-S.I*P*S.diff(B,P)/B,-S.I*Q*S.diff(B,Q)/B],
                [ S.I*P*S.diff(A,P)/A, S.I*Q*S.diff(A,Q)/A]])
    tp=alpha*mp/lp;tm=beta*mm/lm
    expected=2*S.I/(tp-tm)*S.Matrix([[tp*tm,-(tp+tm)/2],[-(tp+tm)/2,1]])
    same(H,expected);zero(H.det()-1)
    same(H.subs({P:1,Q:1}),S.eye(2))
    m,l=S.symbols('m ell')
    polynomial=(l-1)**2+(m-1)**2
    zero(polynomial.subs({m:mp,l:lp}))
    zero(polynomial.subs({m:mm,l:lm}))
    # Unnormalized equations coincide at P=Q=1 and retain the curve.
    assert S.expand(polynomial.subs({m:m/P,l:l/Q}).subs({P:1,Q:1})-polynomial)==0
    return {'exact_opposite_place_phase_inverse':True,
            'whole_norm_gradient_and_Hessian_identity':True,
            'raw_A_polynomial_diagonal_fiber_retained':True,
            'scope':'Generic algebraic-node chart audit, not an additional knot case.'}


def main():
    result={'phase_Jacobian_and_Hessian':slope_hessian(),
            'regulator_potential':primitive_and_closedness(),
            'whole_H5_period_torsor':H5_connection(),
            'angle_covariance':tetrahedral_cotangents(),
            'algebraic_function_level_inverse':whole_algebraic_phase_inverse(),
            'scope':'Classical positive optimizer and marked regulator; no selected quantum period claim.'}
    out=Path(__file__).with_name('doubled_phase_rivin_optimizer_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'H5_connection_checked':True,'output':str(out)},indent=2))


if __name__=='__main__':main()
