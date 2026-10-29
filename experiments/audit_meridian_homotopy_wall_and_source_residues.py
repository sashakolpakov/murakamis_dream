#!/usr/bin/env python3
"""Exact Gauss-wall tube, varying meridian clutch and actual source charges."""

import json
from pathlib import Path

import sympy as s


def meridian_chart_checks():
    v, eta, m = s.symbols('v eta m', nonzero=True)
    V, kappa = 1/v, m-1/m
    ep = -v*v*eta+kappa*v
    mu = s.Matrix([[m-eta*v, eta],
                   [kappa*v-eta*v*v, 1/m+eta*v]])
    assert s.cancel(mu.det()-1) == 0
    assert s.cancel(s.trace(mu)-m-1/m) == 0
    assert (mu*s.Matrix([1, v])-m*s.Matrix([1, v])).applyfunc(s.cancel) == s.zeros(2, 1)
    gs = s.Matrix([[V, -1], [1, 0]])
    south = gs*s.Matrix([[m, -ep], [0, 1/m]])*gs.inv()
    assert (mu-south).applyfunc(s.cancel) == s.zeros(2)
    f = m-eta*v
    assert s.cancel(f-1/m-ep*V) == 0
    # Cech peripheral two-form coefficient after expressing the south chart
    # in north variables. All coefficients below multiply dv wedge dm.
    coeff_n = -eta/(m*f)
    coeff_s = -(1+1/m**2)/(v*f)-ep/(m*v*v*f)
    assert s.cancel(coeff_s-coeff_n+2/(m*v)) == 0
    # Global exponential homotopy algebra: u=m^(-2)*u_south.
    uS = s.symbols('uS', nonzero=True)
    u = uS/m**2
    etaN = m*(1-u)/v
    etaS = (uS-1)/(m*V)
    assert s.cancel(-v*v*etaN+kappa*v-etaS) == 0
    c, lam, a = s.symbols('c lam a')
    etaNexp = m*(1-s.exp(-c*lam*v*a))/v
    assert s.simplify(s.limit(etaNexp, v, 0)-m*c*lam*a) == 0
    VV, aa = s.symbols('V aa')
    etaSexp = (s.exp(c*lam*VV*aa)-1)/(m*VV)
    assert s.simplify(s.limit(etaSexp, VV, 0)-c*lam*aa/m) == 0
    return {'SL2_determinant_trace_eigenflag': True,
            'whole_Grothendieck_affine_transition': True,
            'peripheral_Cech_form_difference': True,
            'global_pole_regular_exponential_detour': True}


def wall_and_cycle_checks():
    lam, T = s.symbols('lambda T', real=True)
    c = 2*s.pi*s.I
    f = 1-lam+lam*s.exp(-c*T)
    point = {lam: s.Rational(1, 2), T: s.Rational(1, 2)}
    assert s.simplify(f.subs(point)) == 0
    dl, dt = s.diff(f, lam).subs(point), s.diff(f, T).subs(point)
    assert s.simplify(dl+2) == 0
    assert s.simplify(dt-s.pi*s.I) == 0
    normal_jacobian = s.Matrix([[s.re(dl), s.re(dt)],
                                [s.im(dl), s.im(dt)]]).det()
    assert normal_jacobian == -2*s.pi
    # Compact orientation dv wedge da=-i dT wedge dphi.
    source_period = -2*s.pi*s.I
    physical_period = c*source_period
    tube_period = c*c
    assert s.simplify(physical_period+tube_period) == 0
    # The fixed-Y logarithmic interpolation has exactly the missing pole.
    e = s.symbols('e', nonzero=True)  # e=exp(-c lambda)
    eta_south_pole = e-1
    assert eta_south_pole.subs(e, 1) == 0
    # Both actual principal-Gaussian residues, with normal chosen first.
    eta, v, ff = s.symbols('eta v f', nonzero=True)
    assert s.limit(eta*(-1/(eta*(1-eta*v))), eta, 0) == -1
    assert s.limit(ff*(1/(ff*(1-ff))), ff, 0) == 1
    # Exact compact primitive on the wall intersection a=1/(2v).
    assert s.simplify(v*s.diff(1/(2*v), v)+1/(2*v)) == 0
    N = s.symbols('N', positive=True, integer=True)
    h = c/N
    period_lam = -c*c*lam
    assert s.simplify(period_lam/(c*h)+N*lam) == 0
    assert s.simplify(-period_lam/(c*h)-N*lam) == 0
    assert s.simplify(s.exp(period_lam.subs(lam, 1)/h)-1) == 0
    return {'straight_homotopy_negative_wall_intersection': True,
            'physical_minus_exceptional_equals_negative_wall_tube': True,
            'Gaussian_residue_signs_and_half_wall_current': True,
            'signed_curvature_and_positive_Chern_convention': True,
            'integer_flux_exponential': True}


def actual_source_residues():
    M, Y = s.symbols('M Y', nonzero=True)
    records = []
    # These are universal scalar identities, independent of the value of F.
    for N in range(2, 13):
        n = N-1
        SN = sum(Y**j for j in range(N))
        reciprocal = s.cancel(SN.subs(Y, 1/Y)-Y**(-n)*SN)
        assert reciprocal == 0
        epsilon = s.I**(N+3)
        d = epsilon*M**n/SN.subs(Y, M*M)
        assert s.cancel(d.subs(M, -M)-(-1)**n*d) == 0
        assert s.cancel(d.subs(M, 1/M)-d) == 0
        assert s.limit(d, M, 1) == epsilon/N
        assert s.limit(d, M, -1) == epsilon*(-1)**n/N
        # Simple-pole coefficient in the canonical meridian one-form.
        # Modulo S_N(M²), [M*S_M'] times the proposed scalar residue is
        # epsilon*M^n. This proves the formula simultaneously at all walls.
        denominator = SN.subs(Y, M*M)
        candidate = -epsilon*M**n*(1-M*M)/(2*N)
        check = s.expand(M*s.diff(denominator, M)*candidate-epsilon*M**n)
        assert s.rem(check, denominator, M) == 0
        # Exact reduced/full source relation at the opposite meridian lift.
        reciprocalF = 3+2*(M*M+1/(M*M))+(M**4+M**-4)
        full = d*reciprocalF
        assert s.cancel(full.subs(M, -M)-(-1)**n*full) == 0
        assert s.cancel(full.subs(M, 1/M)-full) == 0
        # Check the marked root/parity conversion to the real sine weight.
        for k in range(1, N):
            Mk = s.exp(-s.pi*s.I*s.Rational(k, N))
            left = Mk**n*(1-Mk**2)
            right = (-1)**k*2*s.I*s.sin(s.pi*s.Rational(k, N))
            assert abs(complex(s.N(left-right, 50))) < 1e-40
        sine_sum = sum(s.sin(s.pi*s.Rational(k, N)) for k in range(1, N))
        assert abs(complex(s.N(sine_sum-s.cot(s.pi/(2*N)), 50))) < 1e-40
        records.append({'level': N, 'all_wall_residues_polynomial_identity': True,
                        'actual_modified_dimension_central_sign': (-1)**n,
                        'exact_scalar_Weyl_invariance': True,
                        'marked_sine_weights_and_total_bound': True})
    return records


def main():
    result = {'varying_meridian_geometry': meridian_chart_checks(),
              'fixed_meridian_wall_and_cycles': wall_and_cycle_checks(),
              'actual_source_wall_levels': actual_source_residues(),
              'scope': 'Universal orbit/relative wall and exact actual meridian-source charges; no full A-branch or Kashaev point-integral identification.'}
    target = Path(__file__).with_name('meridian_homotopy_wall_and_source_residues_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'global_meridian_and_wall_geometry': 'passed',
                      'actual_all_parity_source_levels': len(result['actual_source_wall_levels'])}))


if __name__ == '__main__':
    main()
