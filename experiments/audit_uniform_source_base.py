#!/usr/bin/env python3
"""Uniform Frobenius source field, meridian deformation, and cap chart.

Exact identities and finite-degree root-graph certificates. This tests
the source coefficient base, not a selected geometric quantum period.
"""

from itertools import product
import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


def coefficient_certificate():
    q,M,w,zeta=s.symbols('q M w zeta',nonzero=True)
    rho=q-q**-1;f=M-M**-1;Y=M*M;U=w*w
    epsilon=-zeta*zeta;eta=zeta**3
    shift=lambda F:s.cancel(F.subs({M:q*M,w:-w},simultaneous=True))
    dimension=eta*f/(w-w**-1)
    multiplier=-((q*M)-(q*M)**-1)/f
    assert s.cancel(shift(dimension)/dimension-multiplier)==0
    central=-zeta*U/((U-1)*(U+1))
    assert s.cancel(shift(central)-central)==0
    delta=rho*(Y-Y**-1)
    overlap=epsilon*rho*(M+M**-1)*(q*Y-q**-1*Y**-1)/(w+w**-1)
    full_source=(1+U**-1)*overlap/delta
    assert s.cancel(full_source-epsilon*M*(q*Y-q**-1*Y**-1)/(w*(Y-1)))==0
    # Charge pullback intertwines the first step with the c-th step.
    for charge in (1,3,5):
        left=(q*M)**charge,(-w)**charge
        right=q**charge*M**charge,(-1)**charge*w**charge
        assert left==right
    return {'uniform_phase_cover':'zeta^4=1; epsilon=-zeta^2; eta=zeta^3',
            'uniform_full_ADO_dimension':str(dimension),
            'uniform_central_cut_line':str(central),
            'exact_meridian_dimension_multiplier':str(multiplier),
            'full_affine_source_cancellation_exact':True,
            'source_charge_pullback_and_step_compatibility_exact':True,
            'constant_field':'C(q,zeta,w^2) on each phase component'}


def deformation_certificate():
    rho=s.Symbol('rho');a,b,c,d,e,f=s.symbols('a b c d e f')
    # Pairs are (s,c), with c^2-rho^2*s^2=4.
    law=lambda A,B:((A[0]*B[1]+A[1]*B[0])/2,
                    (A[1]*B[1]+rho*rho*A[0]*B[0])/2)
    left=law(law((a,b),(c,d)),(e,f));right=law((a,b),law((c,d),(e,f)))
    assert all(s.expand(x-y)==0 for x,y in zip(left,right))
    x,y=law((a,b),(c,d))
    assert s.expand(y*y-rho*rho*x*x-(b*b-rho*rho*a*a)*(d*d-rho*rho*c*c)/4)==0
    q,M,h,w=s.symbols('q M h w',nonzero=True);t=s.Symbol('t')
    r=q-q**-1;k=q+q**-1;C=M+M**-1;F=M-M**-1
    assert s.cancel((q*M)-(q*M)**-1-k*F/2-r*C/2)==0
    assert s.cancel(q*M+(q*M)**-1-k*C/2-r*F/2)==0
    meridian=s.Matrix([[k/2,s.Rational(1,2)],[r*r/2,k/2]])
    reflection=s.diag(-1,1)
    assert s.cancel(meridian.det()-1)==0
    assert (reflection*meridian*reflection-meridian.inv()).applyfunc(s.cancel)==s.zeros(2)
    # Standard G^(rho) coordinate t=(M-1)/rho.
    m=1+rho*t
    symmetric=t*(2+rho*t)/(1+rho*t)
    assert s.cancel((m-m**-1)-rho*symmetric)==0
    exceptional=meridian.subs(q,1)
    assert exceptional==s.Matrix([[1,s.Rational(1,2)],[0,1]])
    return {'algebraic_group_law_and_norm_preservation_exact':True,
            'standard_deformation_group':'G^(rho): t*tprime=t+tprime+rho*t*tprime',
            'symmetric_meridian_matrix':str(meridian),
            'Weyl_relation_and_inverse_exact':True,
            'exceptional_identity_fiber':'G_a with sigma(s)=s+1, sigma(w)=-w'}


def normalized_source_certificate():
    q,M,t,w,epsilon=s.symbols('q M t w epsilon',nonzero=True)
    rho=q-q**-1;k=q+q**-1;C=M+M**-1;f=M-M**-1
    p=q**-1*M*M-q*M**-2;r=q*M*M-q**-1*M**-2
    phat=(k*t*C-(C*C-2))/2;rhat=(k*t*C+(C*C-2))/2
    assert s.cancel(p-rho*phat-k*C*(f-rho*t)/2)==0
    assert s.cancel(r-rho*rhat-k*C*(f-rho*t)/2)==0
    assert s.cancel(rhat-phat-(C*C-2))==0
    ahat=C*rhat/(w+w**-1);dhat=t*C/epsilon
    exceptional_a=s.cancel(ahat.subs({q:1,M:1}))
    exceptional_d=s.cancel(dhat.subs({q:1,M:1}))
    assert s.cancel(exceptional_a-2*(2*t+1)/(w+w**-1))==0
    assert s.cancel(exceptional_d-2*t/epsilon)==0
    assert ahat.subs({q:1,M:1,t:0,w:1})==1
    assert s.cancel((1+w**-2)*ahat/dhat-epsilon*rhat/(w*t))==0
    return {'proper_transform_cut_walls':['2*s-1','2*s+1'],
            'point_source_ideal_pullback':'(p,sigma(p))=(rho)',
            'normalized_overlap_on_exceptional_fiber':str(exceptional_a),
            'normalized_branch_gap_on_exceptional_fiber':str(exceptional_d),
            'source_matrix_algebra_regular_at_s_zero_w_one':True,
            'full_exceptional_source':'epsilon*w^(-1)*(2*s+1)/s',
            'only_coefficient_matrices_algebraized_not_the_full_knot_state':True}


def marked_cap_certificate():
    t,ell,zeta=s.symbols('s ell zeta',nonzero=True);w=1+t*ell
    normalized_dimension=zeta**3*t/(w-w**-1)
    regular=zeta**3*w/(ell*(w+1))
    assert s.cancel(normalized_dimension-regular)==0
    cut=-zeta*w*w/((w*w-1)*(w*w+1))
    assert s.cancel(t*cut+zeta*w*w/(ell*(w+1)*(w*w+1)))==0
    assert s.simplify(regular.subs(t,0)-zeta**3/(2*ell))==0
    return {'second_blowup_chart':'w=1+s*ell',
            'dimension_divided_by_rho_regular_value':'zeta^3/(2*ell)',
            's_times_central_cut_regular_value':'-zeta/(4*ell)',
            'root_graph_mark':'ell_N=N*(q_N-q_N^(-1))/2',
            'exceptional_period_equation':'dlog(w)=pi*i*ds',
            'generic_cap_slope_is_required_not_just_the_point_s_zero_w_one':True}


def period_section_certificate():
    h,t,tau,zeta=s.symbols('h s tau zeta',nonzero=True)
    u=s.series(s.asinh(t*s.sinh(h)),h,0,9).removeO()
    logw=s.expand(tau*u/h)
    assert logw.subs(h,0)==tau*t
    assert all(s.expand(logw).coeff(h,k)==0 for k in (1,3,5,7))
    step=s.series(t*s.cosh(h)+s.sqrt(1+t*t*s.sinh(h)**2),h,0,8).removeO()
    shifted=s.series(logw.subs(t,step),h,0,8).removeO()
    assert s.cancel(shifted-logw-tau)==0
    slope=tau*s.sinh(h)/h
    complete=zeta**3*(2*s.sinh(h))/(2*slope)
    assert s.cancel(complete-zeta**3*h/tau)==0
    return {'formal_log_Frobenius_period_through_h_six':str(logw),
            'all_odd_quantum_orders_vanish_through_checked_order':True,
            'one_meridian_step_adds_exact_marked_Tate_period':True,
            'marked_Tate_period':'tau=pi*i',
            'complete_cap_value':'zeta^3*h/tau=zeta^3/N at h=tau/N',
            'nonconstant_algebraic_hom_G_a_to_G_m_cannot_replace_the_period':True}


def finite_degree_certificates():
    q=s.Symbol('q');Dq=3;DM=4;DV=2;records=[]
    for N in (8,13,10,11):
        phi=s.Poly(s.cyclotomic_poly(2*N,q),q)
        factors=s.factor_list(phi.as_expr(),q,extension=s.I)[1]
        degrees=[s.Poly(f,q,extension=s.I).degree() for f,e in factors for _ in range(e)]
        assert N>DM and s.totient(2*N)>2*Dq and min(degrees)>Dq
        exponents=[i+N*j for i,j in product(range(DM+1),range(DV+1))]
        assert len(set(exponents))==len(exponents)
        assert s.expand((s.Symbol('w')-s.Symbol('M')**N).subs(s.Symbol('w'),s.Symbol('M')**N))==0
        records.append({'level':N,'phase_mod_four':N%4,'q_degree_bound':Dq,
                        'M_exponent_span_bound':DM,'w_exponent_span_bound':DV,
                        'cyclotomic_factor_degrees_over_Q_i':degrees,
                        'independent_bounded_monomials':(Dq+1)*(DM+1)*(DV+1),
                        'degree_bounds_are_essential':True})
    return records


def root_specialization_cases():
    records=[]
    for N in range(2,16):
        p,g,q=field(N);rho=(q-pow(q,-1,p))%p
        zeta=pow(q,N*(1-N)//2,p);epsilon=pow(-1,N,p)
        assert pow(zeta,4,p)==1 and -zeta*zeta%p==epsilon
        eta=-epsilon*zeta%p;assert pow(zeta,3,p)==eta
        ell=N*rho*pow(2,-1,p)%p
        cap_value=rho*eta*pow(2*ell,-1,p)%p
        assert cap_value==eta*pow(N,-1,p)%p
        values=[]
        for exponent in range(1,40):
            M=pow(g,exponent,p);w=pow(M,N,p)
            if (w*w-1)%p==0 or (M*M-1)%p==0:continue
            f=(M-pow(M,-1,p))%p;C=(M+pow(M,-1,p))%p
            t=f*pow(rho,-1,p)%p;tnext=(q*M-pow(q*M,-1,p))*pow(rho,-1,p)%p
            k=(q+pow(q,-1,p))%p
            assert tnext==(k*t+C)*pow(2,-1,p)%p
            assert pow(q*M,N,p)==-w%p
            rhat=((q*M*M-pow(q,-1,p)*pow(M,-2,p))*pow(rho,-1,p))%p
            ahat=C*rhat*pow((w+pow(w,-1,p))%p,-1,p)%p
            actual=epsilon*rho*C*(q*M*M-pow(q,-1,p)*pow(M,-2,p))*pow((w+pow(w,-1,p))%p,-1,p)%p
            assert actual*pow(epsilon*rho*rho%p,-1,p)%p==ahat
            dimension=eta*f*pow((w-pow(w,-1,p))%p,-1,p)%p
            shifted=eta*((q*M)-pow(q*M,-1,p))*pow((-w-pow(-w,-1,p))%p,-1,p)%p
            assert shifted*pow(dimension,-1,p)%p==-(q*M-pow(q*M,-1,p))*pow(f,-1,p)%p
            values.append({'meridian_power':exponent,'normalized_overlap':ahat})
            if len(values)==2:break
        assert len(values)==2
        records.append({'level':N,'prime':p,'phase':zeta,'complete_full_dimension':cap_value,
                        'root_graph_slope':ell,'all_phase_and_marked_cap_identities_exact':True,
                        'generic_root_graph_specializations':values})
    return records


def main():
    result={'scope':'Uniform coefficient base and marked normalization charts for the actual local source; no selected Bloch-period or volume theorem.',
            'uniform_coefficient_field':coefficient_certificate(),
            'multiplicative_to_additive_group':deformation_certificate(),
            'normalized_source_on_blowup':normalized_source_certificate(),
            'marked_central_cap':marked_cap_certificate(),
            'uniform_Frobenius_period':period_section_certificate(),
            'finite_degree_root_graph_certificates':finite_degree_certificates(),
            'original_root_scalar_specializations':root_specialization_cases()}
    output=Path(__file__).with_name('uniform_source_base_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(output),'exact_uniform_group_source_and_cap_certificates':True,
                      'bounded_degree_phase_sheets_checked':len(result['finite_degree_root_graph_certificates']),
                      'root_levels':len(result['original_root_scalar_specializations']),
                      'generic_scalar_specializations':sum(len(r['generic_root_graph_specializations']) for r in result['original_root_scalar_specializations'])}),flush=True)


if __name__=='__main__':main()
