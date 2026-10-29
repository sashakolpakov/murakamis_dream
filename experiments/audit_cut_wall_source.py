#!/usr/bin/env python3
"""Actual cut walls and the formal geometric cyclic source.

The root checks use original tensor matrices and pivotal contractions.
The universal wall and calibration certificates use exact rational
functions. No global selected-period or volume assertion is made.
"""

import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_actual_peripheral_fusion import module,tensor_module
from audit_braided_source_groupoid import projector_zero
from audit_finite_sum_annihilator import field
from audit_intrinsic_cut_transport import casimir,fusion_frame,right_close,modified_dimension
from audit_kashaev_ado_pointing import color_matrices
from audit_regular_holonomy_braiding import mm


def universal_wall_certificate():
    q,M,d,kappa=s.symbols('q M d kappa',nonzero=True)
    shift=lambda f:s.cancel(f.subs(M,q*M))
    p=q**-1*M**2-q*M**-2;r=q*M**2-q**-1*M**-2
    assert s.cancel(shift(p)-r)==0
    assert s.cancel(p*r-((M**2-M**-2)**2-(q-q**-1)**2))==0
    assert s.cancel(p-q**-1*M**-2*(M**2-q)*(M**2+q))==0
    assert s.cancel(r-q*M**-2*(M**2-q**-1)*(M**2+q**-1))==0
    point={M:1,q:1}
    jac=s.Matrix([[s.diff(z,v).subs(point) for v in (M,q)] for z in (p,r)])
    assert jac.det()==16
    coefficient=s.cancel((p+r)/d)
    multiplication=s.Matrix([[-p,0],[coefficient,r]])
    residue_pairing=s.Matrix([[0,1],[1,d]])
    gram=(residue_pairing*multiplication).applyfunc(s.cancel)
    assert gram==gram.T and s.cancel(gram.det()-p*r)==0
    L=s.Matrix([[1,0],[-r/coefficient,1]])
    R=s.Matrix([[1,-r/coefficient],[0,1]])
    assert (L*gram*R-s.diag(coefficient,p*r/coefficient)).applyfunc(s.cancel)==s.zeros(2)
    # The regularized cut row has the single primitive relation below.
    assert (s.Matrix([[r,p]])*s.Matrix([p,-r])).applyfunc(s.cancel)==s.zeros(1,1)
    gamma=s.Symbol('gamma',nonzero=True)
    marked_jac=s.Matrix(
        [[s.diff(z,v).subs(point) for v in (M,q)] for z in (-gamma*p,gamma*r)])
    assert s.cancel(marked_jac.det().subs(gamma,kappa/4)+kappa**2)==0
    return {'source_wall':str(p),'its_exact_meridian_translate':str(r),
            'wall_Jacobian_at_q_M_one':16,
            'normalized_regularized_cut_image':'(M-1,q-1)',
            'cut_pairing_determinant':str(s.factor(p*r)),
            'cut_pairing_cokernel':'S/(p*sigma(p))',
            'normalization_quotient_and_cyclic_defect':'S/(M-1,q-1)',
            'ordered_normalized_wall_residue':'1/16',
            'ordered_calibrated_branch_density_residue':'-1/kappa^2',
            'full_root_normalization_not_removed_from_the_period':True}


def calibration_case(power_a,power_b,alpha,beta,longitude):
    # q=z^2 retains the specified local square root without fractional powers.
    z,M=s.symbols('z M');q=z*z
    shift=lambda f:s.cancel(f.subs(M,q*M))
    a=longitude*M**power_a*(1+alpha*(q-1)*M)
    b=longitude*M**power_b*(1+beta*(q-1)/M)
    ratio=s.cancel((b/a).subs(M,z))
    coefficient=s.cancel((ratio-1)/(q**3-q))
    assert s.denom(coefficient).subs(z,1)!=0
    g=s.cancel(1+(M*M-q)*coefficient)
    assert s.cancel(g.subs(M,z)-1)==0
    assert s.cancel(g.subs(M,z**3)-ratio)==0
    calibrated=s.cancel(a*shift(g)/g)
    assert s.cancel((calibrated-b).subs(M,z))==0
    p=q**-1*M*M-q/(M*M)
    unit=s.cancel((calibrated-b)/p)
    numerator,denominator=s.fraction(unit)
    assert denominator.subs({z:1,M:1})!=0
    kappa=longitude*(power_a-power_b)
    assert kappa and s.cancel(unit.subs({z:1,M:1})-kappa/4)==0
    assert s.cancel(calibrated.subs(z,1)-longitude*M**power_a)==0
    return {'classical_powers':[power_a,power_b],'subprincipal_parameters':[alpha,beta],
            'complete_longitude':longitude,'calibrating_unit':str(s.factor(g)),
            'calibrated_branch_difference_divided_by_actual_wall_is_a_unit':True,
            'difference_unit_at_the_complete_point':str(s.Rational(kappa,4)),
            'exact_half_meridian_wall_and_shift_condition_checked':True,
            'actual_selected_knot_generator_not_identified':True}


def root_matrix_cases(N):
    p,generator,q=field(N);I=np.eye(N,dtype=np.int64)
    inverse=lambda x:pow(int(x),-1,p)
    rho=(q-inverse(q))%p;c=(q+inverse(q))%p
    sign=pow(-1,N,p);phase=pow(q,N*(1-N)//2,p);kappa=generator
    records=[];seen=set()
    for power in range(1,p):
        M=pow(generator,power,p)
        if M in seen:continue
        seen.add(M)
        U=pow(M,2*N,p)
        if (U*U-1)%p==0 or (M*M-1)%p==0:continue
        x=-M*inverse(q)%p
        H,Hi,_=fusion_frame(N,p,q,x,x)
        P0=mm(p,H[:,:N],Hi[:N,:]);Plast=mm(p,H[:,-N:],Hi[-N:,:])
        pivot=color_matrices(N,p,q,x)[2]
        f=(M-inverse(M))%p;gap=kappa*f*inverse(2)%p
        D=(pow(M,N,p)+pow(M,-N,p))%p
        gamma=sign*gap*inverse(f*D%p)%p
        wall=(inverse(q)*M*M-q*pow(M,-2,p))%p
        shifted=(q*M*M-inverse(q)*pow(M,-2,p))%p
        weights=[gamma*wall*inverse(gap)%p,gamma*shifted*inverse(gap)%p]
        for projector,weight in zip((P0,Plast),weights):
            assert np.array_equal(right_close(projector,pivot,p),weight*I%p)
        full_gamma=modified_dimension(N,p,q,x)*gamma%p
        central_gamma=-phase*U*gap*inverse((U*U-1)%p)%p
        assert full_gamma==central_gamma
        records.append({'level':N,'prime':p,'meridian':M,
                        'actual_projector_cuts':weights,'full_common_density_frame':full_gamma,
                        'both_original_tensor_projector_cuts_match_translated_walls':True,
                        'full_common_factor_has_both_U_minus_one_and_U_plus_one':True})
        if len(records)==2:break
    assert len(records)==2
    x=-inverse(q)%p
    O=casimir(tensor_module(module(N,p,q,x),module(N,p,q,x),p),p,q)
    pair=projector_zero(N,p,q,O)
    J=mm(p,(O-c*np.eye(N*N,dtype=np.int64))%p,pair)
    pivot=color_matrices(N,p,q,x)[2]
    assert np.array_equal(right_close(pair,pivot,p),sign*c*I%p)
    assert np.array_equal(right_close(J,pivot,p),sign*rho*rho*I%p)
    gamma0=sign*kappa*inverse(4)%p
    dimension0=-sign*phase*inverse(N)%p
    assert gamma0*dimension0%p==-phase*kappa*inverse(4*N)%p
    complete={'level':N,'prime':p,'complete_pivotal_pair_cut':sign*c%p,
              'complete_pivotal_nilpotent_cut':sign*rho*rho%p,
              'complete_full_common_frame':gamma0*dimension0%p,
              'complete_original_tensor_cuts_and_full_phase_checked':True}
    return records,complete


def main():
    generic=[];complete=[]
    for N in (2,3,4,5,6,9):
        rows,point=root_matrix_cases(N);generic.extend(rows);complete.append(point)
    result={'scope':'Actual cut-wall presentation and formal model cyclic-source comparison; no global affine extension or selected-period identification.',
            'universal_certificate':universal_wall_certificate(),
            'formal_calibrations':[calibration_case(*row) for row in
                ((1,-1,0,0,1),(2,-1,1,2,1),(1,0,-1,1,-1),(3,1,2,-1,-1))],
            'generic_actual_root_cuts':generic,'complete_actual_root_cuts':complete}
    output=Path(__file__).with_name('cut_wall_source_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(output),'universal_wall_and_source_certificate':True,
                      'exact_formal_calibrations':len(result['formal_calibrations']),
                      'generic_original_tensor_cases':len(generic),
                      'complete_original_tensor_cases':len(complete)}),flush=True)


if __name__=='__main__':main()
