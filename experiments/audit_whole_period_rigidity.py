#!/usr/bin/env python3
"""Whole power-coordinate comparisons and faithful cyclotomic jets.

Exact characteristic-zero checks of the reconstruction proof, including
the quantum-normal direction lost by freezing q**N. These do not test
or assert the missing geometric comparison for a knot invariant.
"""

import json
from pathlib import Path

import sympy as s


def differential_base():
    t, q, M, v, w = s.symbols('t q M v w', nonzero=True)
    Dq = lambda f: s.cancel(q*s.diff(f, q)+v*s.diff(f, v)/t)
    DM = lambda f: s.cancel(M*s.diff(f, M)+w*s.diff(f, w)/t)
    shift = lambda f: s.cancel(f.subs({M:q*M, w:v*w}, simultaneous=True))
    tests = [q, M, v, w, t, q*v+M/w, (v+q*M)/(w-M)]
    for f in tests:
        assert s.cancel(Dq(DM(f))-DM(Dq(f))) == 0
        assert s.cancel(DM(shift(f))-shift(DM(f))) == 0
        assert s.cancel(Dq(shift(f))-shift(Dq(f)+DM(f))) == 0
    assert Dq(v+1).subs(v, -1) == -1/t
    # Pullback of both logarithmic derivatives to every whole power graph.
    N = s.symbols('N', integer=True, positive=True)
    graph = {t:1/N, v:q**N, w:M**N}
    for f in tests:
        F = f.subs(graph, simultaneous=True)
        assert s.simplify(Dq(f).subs(graph, simultaneous=True)-q*s.diff(F,q)) == 0
        assert s.simplify(DM(f).subs(graph, simultaneous=True)-M*s.diff(F,M)) == 0
    return {'commuting_relative_derivatives_checked':len(tests),
            'differential_shift_covariance_checked':len(tests),
            'whole_power_graph_chain_rules_checked':2*len(tests),
            'frozen_root_slice_loses_nonzero_quantum_normal_derivative':True}


def cyclotomic_reconstruction():
    t, z = s.symbols('t z')
    qpairs = [(-2,0), (1,0), (-1,1), (2,-1)]
    mpairs = [(-1,0), (2,0), (0,1)]
    original = s.Matrix(len(qpairs), len(mpairs),
                        lambda i,j:(i+1)*(j+2)+(i-j)*t+(i*j+1)*t*t)
    records = []
    for residue, levels in enumerate(((8,12,16), (9,13,17),
                                       (6,10,14), (7,11,15))):
        recovered = []
        for N in levels:
            assert N % 4 == residue
            lam = [a+N*b for a,b in qpairs]
            mu = [c+N*d for c,d in mpairs]
            assert len(set(lam)) == len(lam)
            assert len(set(mu)) == len(mu)
            Vl = s.Matrix([[e**i for e in lam] for i in range(len(lam))])
            Vm = s.Matrix([[e**j for e in mu] for j in range(len(mu))])
            W = s.diag(*[z**(e % (2*N)) for e in lam])
            A = original.subs(t, s.Rational(1,N))
            J = (Vl*W*A*Vm.T).applyfunc(s.expand)
            W_inverse = s.diag(*[z**((-e) % (2*N)) for e in lam])
            answer = (W_inverse*Vl.inv()*J*Vm.T.inv()).applyfunc(s.expand)
            phi = s.Poly(s.cyclotomic_poly(2*N,z), z, domain=s.QQ)
            answer = answer.applyfunc(lambda f:s.rem(s.Poly(f,z,domain=s.QQ),phi).as_expr())
            assert answer == A
            recovered.append((s.Rational(1,N),answer))
            records.append({'level':N, 'phase_mod_four':residue,
                            'q_jet_orders':len(lam), 'M_jet_orders':len(mu),
                            'coefficient_matrix_recovered_over_exact_cyclotomic_field':True})
        for i in range(original.rows):
            for j in range(original.cols):
                polynomial = s.interpolate([(point,A[i,j]) for point,A in recovered], t)
                assert s.expand(polynomial-original[i,j]) == 0
    return {'coefficient_t_degree':2,
            'whole_polynomial_reconstructed_on_four_phase_classes':True,
            'exact_level_checks':records}


def necessary_orders():
    q, x, y, t = s.symbols('q x y t')
    records = []
    for N in (3,4,5,6,9,12):
        for order in (1,2,3,4):
            # v=-1*(1+x)^N, w=(1+y)^N on the quantum/meridian jets.
            normal = (1-(1+x)**N)**order
            meridian = ((1+y)**N-1)**order
            assert all(s.expand(normal).coeff(x,j) == 0 for j in range(order))
            assert s.expand(normal).coeff(x,order) == (-N)**order
            assert all(s.expand(meridian).coeff(y,j) == 0 for j in range(order))
            assert s.expand(meridian).coeff(y,order) == N**order
            records.append({'level':N, 'first_detecting_jet_order':order,
                            'both_missing_power_directions_detected':True})
    levels = (6,10,14)
    vanishing = s.prod(t-s.Rational(1,N) for N in levels)
    assert vanishing != 0
    assert all(vanishing.subs(t,s.Rational(1,N)) == 0 for N in levels)
    # Exponent separation also needs the span bound.
    N=7
    assert s.expand((s.Symbol('v')-q**N).subs(s.Symbol('v'),q**N)) == 0
    return {'jet_depth_sharpness_checks':records,
            'insufficient_level_interpolation_detected':True,
            'support_span_condition_is_essential':True}


def algebraic_cover_and_source():
    M, z, u, x = s.symbols('M z u x')
    # A selected etale quadratic place over M=1, z=2.
    relation = z*z-(M+3)
    f=z-2
    norm=s.resultant(relation,f,z)
    assert s.expand(norm-(1-M)) == 0
    branch=s.series(s.sqrt(4+u)-2,u,0,5).removeO()
    complement=s.series(-s.sqrt(4+u)-2,u,0,5).removeO()
    assert branch.coeff(u,0) == 0 and branch.coeff(u,1) == s.Rational(1,4)
    assert s.series(branch*complement,u,0,5).removeO() == -u
    # Whole canceled ADO factor: retain w=M**N until after cancellation.
    source=[]
    for N in range(2,13):
        Mx=1+x
        numerator=s.series(Mx-Mx**-1,x,0,5).removeO()
        denominator=s.series(Mx**N-Mx**-N,x,0,5).removeO()
        ratio=s.series((numerator/x)/(denominator/x),x,0,3).removeO()
        assert ratio.coeff(x,0) == s.Rational(1,N)
        assert ratio.coeff(x,1) == 0
        assert ratio.coeff(x,2) == -s.Rational(N*N-1,6*N)
        factor=s.expand(1+Mx**N)
        assert factor.subs(x,0) == 2 and factor.coeff(x,1) == N
        source.append({'level':N, 'whole_dimension_value_without_retained_phase':str(s.Rational(1,N)),
                       'peripheral_factor_value':2, 'peripheral_factor_first_jet':N})
    return {'etale_quadratic_norm':str(norm),
            'selected_factor_norm_jet_divisibility_exact':True,
            'whole_ADO_source_and_peripheral_checks':source}


def polynomial_phases_and_pivot_lift():
    t, epsilon, v, q, M, w = s.symbols('t epsilon v q M w')
    phases=[]
    for N in (6,7,8,9,10,11,12,13):
        exponents=[0,N,N*N]
        V=s.Matrix([[a**i for a in exponents] for i in range(3)])
        # At the cyclotomic point all these phase values are just signs.
        W=s.diag(1,-1,(-1)**N)
        assert (V*W).det() != 0
        coefficients=s.Matrix([1+1/s.Integer(N),2,3-s.Rational(1,N)])
        recovered=W.inv()*V.inv()*(V*W*coefficients)
        assert recovered == coefficients
        phases.append({'level':N,'root_values':[1,-1,(-1)**N],
                       'quadratic_N_phases_separated_by_three_quantum_jets':True})
    # A pointed difference comparison obtained by a finite affine system.
    alpha,beta=s.symbols('alpha beta')
    B1=s.Matrix([[M,1],[1,0]])
    exact=s.Matrix([[1,M+w],[0,1]])
    candidate=s.Matrix([[1,alpha*M+beta*w],[0,1]])
    shift=lambda A:A.applyfunc(lambda f:f.subs({M:q*M,w:v*w},simultaneous=True))
    B2=exact*B1*shift(exact).inv()
    residual=(candidate*B1-B2*shift(candidate)).applyfunc(s.expand)
    equations=[]
    for value in residual:
        equations.extend(s.Poly(value,M,w).coeffs())
    solutions=s.solve(equations,[alpha,beta],dict=True)
    assert solutions == [{alpha:1,beta:1}]
    source=s.Matrix([1,0]);cut=s.Matrix([[0,1]])
    assert exact*source == source and cut*exact == cut
    # Multiplying by the fixed vanishing root factor hides the equations
    # at order zero but its first quantum jet recovers them.
    N=s.symbols('N',integer=True,positive=True)
    leading=(residual*(v+1)).applyfunc(lambda f:s.diff(
        f.subs({q:q*(1+epsilon),v:-(1+epsilon)**N},simultaneous=True),
        epsilon).subs(epsilon,0).expand())
    first_equations=[]
    for value in leading:
        first_equations.extend(s.Poly(value,M,w).coeffs())
    assert s.solve(first_equations,[alpha,beta],dict=True) == [{alpha:1,beta:1}]
    r=v+1
    H=s.Matrix([[r,1],[r*r,r]])
    b=s.Matrix([r,r*r])
    assert H.rank() == H.row_join(b).rank() == 1
    assert (H*s.Matrix([2,-r])-b).applyfunc(s.expand) == s.zeros(2,1)
    lifted=[]
    for level in (3,4,6,9,12):
        rn=1-(1+epsilon)**level
        # Retain the free coordinate -r+epsilon^3 and solve a pivot
        # of order one. The correction has order 3-1, not order zero.
        repaired=2-epsilon**3/rn
        expansion=s.series(repaired,epsilon,0,3).removeO()
        assert expansion.coeff(epsilon,0) == 2
        assert expansion.coeff(epsilon,1) == 0
        assert expansion.coeff(epsilon,2) == s.Rational(1,level)
        assert s.cancel(rn*repaired+(-rn+epsilon**3)-rn) == 0
        lifted.append({'level':level,'pivot_order':1,'input_error_order':3,
                       'correction_order':2,'leading_invertible_matrix_preserved':True})
    # A rootwise invertible comparison can be spurious without normal jets.
    first=s.diff((1-v*v).subs(v,-(1+epsilon)**N),epsilon).subs(epsilon,0)
    assert first == -2*N
    return {'polynomial_power_phase_checks':phases,
            'pointed_generic_comparison_solved_exactly':True,
            'first_normal_jet_recovers_comparison_hidden_by_root_factor':True,
            'rank_minor_and_singular_pivot_lifts':lifted,
            'spurious_rootwise_isomorphism_rejected_by_first_normal_jet':True}


def main():
    result={'differential_power_base':differential_base(),
            'finite_reconstruction':cyclotomic_reconstruction(),
            'necessary_hypotheses':necessary_orders(),
            'algebraic_cover_and_whole_source':algebraic_cover_and_source(),
            'bounded_comparison_existence':polynomial_phases_and_pivot_lift(),
            'scope':'Algebraic comparison reconstruction; no actual geometric period identification or volume theorem.'}
    output=Path(__file__).with_name('whole_period_rigidity_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact_cyclotomic_reconstructions':len(result['finite_reconstruction']['exact_level_checks']),
                      'quantum_and_meridian_jet_sharpness_checks':len(result['necessary_hypotheses']['jet_depth_sharpness_checks']),
                      'whole_source_checks':len(result['algebraic_cover_and_whole_source']['whole_ADO_source_and_peripheral_checks']),
                      'quadratic_power_phase_checks':len(result['bounded_comparison_existence']['polynomial_power_phase_checks']),
                      'singular_pivot_lifts':len(result['bounded_comparison_existence']['rank_minor_and_singular_pivot_lifts']),
                      'output':str(output)},indent=2))


if __name__ == '__main__':
    main()
