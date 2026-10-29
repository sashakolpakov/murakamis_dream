#!/usr/bin/env python3
"""Source-preserving jet transport, tempered residues and growth estimates.

Uniform arguments are in notes/tempered_a_growth_bound.md. Exact tests
of the selected scalar use rational cyclotomic reductions, not a numerical
fit. Numerical growth and denominator checks validate estimates only.
No Kashaev volume theorem is asserted.
"""

from math import log, pi, sin
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_peripheral_normal_period import coefficient_terms, operator_calibration
from audit_pointed_a_gram_period import calibration_color, monomial_jet


def leading_at(expr, variable, point):
    u = sp.Dummy('u')
    shifted = sp.cancel(expr.subs(variable, 1/u if point == sp.oo else point+u))
    n, d = sp.fraction(shifted)
    pn, pd = sp.Poly(n, u), sp.Poly(d, u)
    vn, vd = min(k[0] for k in pn.monoms()), min(k[0] for k in pd.monoms())
    return vn-vd, sp.cancel(pn.coeff_monomial(u**vn)/pd.coeff_monomial(u**vd))


def tame_symbol(f, g, variable, point):
    vf, uf = leading_at(f, variable, point)
    vg, ug = leading_at(g, variable, point)
    sign = sp.Integer(-1)**(vf*vg)
    return sp.cancel(sign*uf**vg/ug**vf)


def residue_certificates():
    t = sp.Symbol('t')
    shapes = [t, 1-t, t**-2*(1+t), (t-1)**3/(1+t*t), (t-2)/(t+1)]
    records = []
    for z in shapes:
        for point in (0, 1, -1, 2, sp.oo):
            value = tame_symbol(z, 1-z, t, point)
            assert value == 1
            records.append({'shape': str(z), 'place': str(point), 'Steinberg_residue': 1})
    # A rational Steinberg example with a nontrivial root-of-unity edge.
    assert tame_symbol(t, 1/(t+1), t, -1) == -1
    assert tame_symbol(t, 1/(t-2), t, 2) == sp.Rational(1, 2)
    return records


def companion_certificates():
    p, mu = sp.symbols('p mu')
    for d in range(1, 7):
        coefficients = sp.symbols(f'a0:{d}')
        numerator = sp.zeros(d)
        for j in range(d-1):
            numerator[j, j+1] = p
        numerator[d-1, :] = sp.Matrix(1, d, [-a for a in coefficients])
        expected = mu**d+sum(coefficients[i]*p**(d-1-i)*mu**i for i in range(d))
        assert sp.expand(numerator.charpoly(mu).as_expr()-expected) == 0
    return {'generic_numerator_companion_dimensions_checked': list(range(1, 7)),
            'classical_roots_are_p_times_longitude_roots': True}


def build_lifts(N, terms, B, q, p, colors, j0=1):
    d = max(terms)
    invN = pow(N, -1, p)
    scales = np.array([pow(invN, r, p) for r in range(B+1)], dtype=np.int64)
    source = np.zeros(d*(B+1), dtype=np.int64)
    for j in range(d):
        jet = colors(j0+j, q, B, p)*scales % p
        for r in range(B+1):
            source[r*d+j] = int(jet[r])
    transfers, orders, etas = [], [], []
    for j in range(j0, N-d+1):
        coeff = {}
        for i, summands in terms.items():
            jet = np.zeros(B+1, dtype=np.int64)
            for c, eM, eq in summands:
                jet = (jet+c*pow(-1, eM, p)*monomial_jet(q, eq+j*eM, B, p)) % p
            coeff[i] = jet*scales % p
        m = next(r for r, v in enumerate(coeff[d]) if v)
        orders.append(m); etas.append(int(coeff[d][m]))
        K = np.zeros((d*(B+1), d*(B+1)), dtype=np.int64)
        for r in range(B+1):
            block = np.zeros((d, d), dtype=np.int64)
            for i in range(d-1):
                block[i, i+1] = coeff[d][r]
            block[-1, :] = [-int(coeff[i][r]) % p for i in range(d)]
            for col in range(B+1-r):
                K[(col+r)*d:(col+r+1)*d, col*d:(col+1)*d] = block
        transfers.append(K)
    beta = sum(orders)
    assert beta <= B
    eta = 1
    for value in etas:
        eta = eta*value % p
    return source, transfers, beta, eta


def source_transport_case(N, terms, B, colors, label, actual=False):
    p, _, q = field(N)
    source, lifts, beta, eta = build_lifts(N, terms, B, q, p, colors)
    dual_source, dual_lifts, dual_beta, dual_eta = build_lifts(N, terms, B, pow(q, -1, p), p, colors)
    assert beta == dual_beta
    state, dual_state = source.copy(), dual_source.copy()
    density = np.outer(source, dual_source) % p
    for K, Ks in zip(lifts, dual_lifts):
        state = K@state % p
        dual_state = Ks@dual_state % p
        density = K@density % p@Ks.T % p
        assert np.array_equal(density, np.outer(state, dual_state) % p)
    d = max(terms); observed = beta*d+d-1
    scalar = int(state[observed])*pow(eta, -1, p) % p
    expected = int(colors(N, q, B, p)[0])
    assert scalar == expected
    norm = int(density[observed, observed])*pow(eta*dual_eta % p, -1, p) % p
    assert norm == expected*int(colors(N, pow(q, -1, p), B, p)[0]) % p
    if actual:
        x = pow(q, N-1, p)
        value = reduced_period(N, p, *color_matrices(N, p, q, x), WORDS[0])
        assert value == scalar
    return {'level': N, 'model': label, 'fixed_transfer_dimension': d*(B+1),
            'selected_jet_degree': beta, 'prime': p,
            'exact_whole_germ_scalar_and_paired_transfer': True,
            'original_Kashaev_cut_compared_at_this_level': actual}


def denominator_checks():
    records = []
    # Analytic root branches, including multiple roots and exact grid zeros.
    factors = [(1, 6, 1, 1), (1, 2, 2, 2), (-1, 2, 3, 1)]
    for N in (31, 32, 63, 64, 127, 128, 257, 512, 1024):
        residual = 0.0
        zeros = 0
        for j in range(1, N-2):
            for sigma, u, v, multiplicity in factors:
                E = u+2*v*j
                exact_zero = (E % (2*N) == (0 if sigma == 1 else N))
                if exact_zero:
                    # Leading coefficient in the correctly scaled variable s.
                    residual += multiplicity*log(abs(E/N))
                    zeros += multiplicity
                else:
                    angle = pi*E/N+(0 if sigma == 1 else pi)
                    residual += multiplicity*log(2*abs(sin(angle/2)))
        # The classical circle mean of the displayed binomial product is zero.
        assert abs(residual) <= 40*log(N)
        records.append({'level': N, 'quantum_leading_model': 'analytic_binomial_roots',
                        'exact_zero_orders_retained': zeros,
                        'leading_germ_log_minus_N_circle_mean': residual,
                        'absolute_residual_over_log_N': abs(residual)/log(N)})

    # A deformation whose analytic roots are not monomials in q.
    mp.mp.dps = 60
    for N in (31, 64, 127, 256, 512):
        q = mp.exp(mp.pi*1j/N)
        total = mp.mpf(0)
        for j in range(1, N-2):
            y = q**(2*j)
            value = (y-1-(q-1)**2)*(y-1+(q-1)**2)
            assert abs(value) > 0
            total += mp.log(abs(value))
        assert abs(total) <= 40*mp.log(N)
        records.append({'level': N, 'quantum_leading_model': 'two_analytic_nonmonomial_branches',
                        'leading_germ_log_minus_N_circle_mean': float(total),
                        'absolute_residual_over_log_N': float(abs(total)/mp.log(N))})
    for N in (31, 64, 127, 256, 512):
        q = mp.exp(mp.pi*1j/N)
        total = sum(mp.log(abs(2*q**(2*j)-3*q)) for j in range(1, N-2))
        residual = total-N*mp.log(3)
        assert abs(residual) < 10
        records.append({'level': N, 'quantum_leading_model': 'nonunit_root_with_nonzero_circle_mean',
                        'leading_germ_log_minus_N_circle_mean': float(residual),
                        'absolute_residual_over_log_N': float(abs(residual)/mp.log(N))})
    return records


def collision_and_entropy_checks():
    collisions = []
    for N in (64, 128, 256, 512, 1024):
        # All eigenvalues collide at every step; nonnormality is retained.
        shear = sum(20*sin(pi*j/N) for j in range(1, N+1))
        matrix = np.array([[1.0, shear], [0.0, 1.0]])
        rate = log(float(np.linalg.norm(matrix, 2)))/N
        assert rate <= log(50*N)/N
        collisions.append({'level': N, 'every_step_has_a_Jordan_collision': True,
                           'observed_log_norm_per_level': rate,
                           'classical_spectral_radius_integral': 0.0})
    mp.mp.dps = 60
    endpoint = 2*mp.pi/3
    half_entropy = mp.quad(lambda t: mp.acosh(max(mp.mpf(1), 1+mp.cos(t)-mp.cos(2*t))), [0, endpoint/2, endpoint])
    volume = 2*mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
    assert abs(half_entropy-volume) < mp.mpf('1e-50')
    return {'collision_models': collisions,
            'geometric_calibration': {'full_circle_largest_root_integral': str(2*half_entropy),
                                       'marked_figure_eight_volume': str(volume),
                                       'ratio_is_two_not_one': True,
                                       'no_actual_all_level_operator_identification_inferred': True}}


def main():
    residues = residue_certificates()
    P, _, _ = operator_calibration()
    calibration = {i: [(c, 2*eY, 2*eQ) for c, eY, eQ in row]
                   for i, row in coefficient_terms(P).items()}
    calibration_cases = [source_transport_case(N, calibration, 2, calibration_color,
                                              'existing_telescoping_calibration', actual=N in (4, 5, 6))
                         for N in range(4, 17)]
    def one_color(j, q, B, p):
        answer = np.zeros(B+1, dtype=np.int64); answer[0] = 1
        return answer
    singular = {0: [(-1, 0, 0), (1, 2, 2)], 1: [(1, 0, 0), (-1, 2, 2)]}
    fake_growth = {0: [(3, 0, 0)], 1: [(-4, 0, 0)], 2: [(1, 0, 0)]}
    source_cases = [source_transport_case(N, singular, 1, one_color, 'actual_unknot_singular_left_factor')
                    for N in range(3, 17)]
    source_cases += [source_transport_case(N, fake_growth, 0, one_color, 'actual_unknot_unexcited_root_three')
                     for N in range(3, 17)]
    def growing_color(j, q, B, p):
        return np.array([pow(2, j, p)]+[0]*B, dtype=np.int64)
    scaled_growth = {0: [(-6, 0, 0)], 1: [(3, 0, 0)]}
    source_cases += [source_transport_case(N, scaled_growth, 0, growing_color,
                                          'scalar_growth_with_exponential_denominator_norm')
                     for N in range(3, 17)]
    a_plus_one = [(1, 4, 0), (-1, 2, 0), (-1, 0, 0), (-1, -2, 0), (1, -4, 0)]
    tempered_fake = {0: [(-1, 0, 0)], 1: a_plus_one,
                     2: [(-c, em, eq) for c, em, eq in a_plus_one], 3: [(1, 0, 0)]}
    source_cases += [source_transport_case(N, tempered_fake, 0, one_color,
                                          'actual_unknot_with_tempered_geometric_dummy_factor')
                     for N in range(3, 17)]
    denominators = denominator_checks()
    numerical = collision_and_entropy_checks()
    result = {'scope': 'Exact finite source transport and checks of a one-sided growth theorem under stated leading-divisor conditions. No sharp volume law or all-knot hypothesis verification is claimed.',
              'exact_tame_residue_certificates': residues,
              'exact_companion_characteristic_certificates': companion_certificates(),
              'exact_calibration_jet_transports': calibration_cases,
              'exact_actual_unknot_source_obstructions': source_cases,
              'numerical_leading_germ_diagnostics': denominators,
              'numerical_collision_and_geometric_entropy_diagnostics': numerical}
    path = Path(__file__).with_name('tempered_a_growth_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'results': str(path), 'exact_Steinberg_residues': len(residues),
                      'exact_jet_source_transports': len(calibration_cases)+len(source_cases),
                      'leading_germ_asymptotic_diagnostics': len(denominators),
                      'original_quantum_cut_levels': [r['level'] for r in calibration_cases if r['original_Kashaev_cut_compared_at_this_level']],
                      'geometric_largest_root_entropy_to_volume_ratio': 2}, indent=2))


if __name__ == '__main__':
    main()
