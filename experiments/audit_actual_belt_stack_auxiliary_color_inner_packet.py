#!/usr/bin/env python3
"""Actual mixed-color quarter-source audits; estimates are proved in the note."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_pretzel_cusp_color_two_band_bound import field_case as actual_two_band
from audit_actual_pretzel_global_alias_and_colored_source_gap import field_case as actual_alias
from audit_actual_pretzel_mixed_inner_source_wkb import (
    literal_U, mu, nu_over_mu, pq,
)
from audit_exact_factorial_interpolation import factorial
from diagnose_pretzel_coherent_radial_capacity import evaluate


def symbolic_curvature():
    # Principal V=q^(h^2)A/D0 has source endpoint one in the limit.
    t, z = sp.symbols('t z', positive=True)
    c = t*t
    Y = (t+sp.I)**2/(t*t+1)
    b = (c-1)*(1-z)-2*sp.I*t*z
    v0 = -1
    derivative_log_root = sp.factor(sp.diff(b, z).subs(z, 0)/(2*v0-b.subs(z, 0)))
    assert sp.factor(derivative_log_root-Y) == 0
    # Y(1/2)=-1. This endpoint fixes the actual chi^2 primitive,
    # including its imaginary constant; it is not fitted to a scalar.
    u = sp.symbols('u', real=True)
    primitive = -(1+sp.exp(2*sp.I*u))/(2*sp.pi*sp.I)
    assert sp.simplify(primitive.subs(u, sp.pi/4)-(-1+sp.I)/(2*sp.pi)) == 0
    return {'principal_V_selected_log_root_color_derivative': str(derivative_log_root),
            'source_endpoint_Y_equals_minus_one_retained': True,
            'actual_inner_action_quadratic': '(-1+i)/(2*pi)'}


def canonical_source_across_quarter(N):
    mp.mp.dps = 65
    q = mp.exp(mp.j*mp.pi/N)
    Q, M = q*q, (N-1)//2
    F = [mp.mpc(1)]
    for k in range(1, N):
        F.append(F[-1]*(1-Q**k))
    chi = mp.mpc('.008', '.004')
    h = N*chi/mp.pi
    rows = []
    for r in sorted({N//4-1, N//4, N//4+1}):
        fm, fp = factorial(N, r-h), factorial(N, r+h)
        D = Q**(-r*r)*F[2*r]/(F[r]*fm*fp)
        a, b, A = fm, fp, mp.mpc(0)
        for v in range(r, M+1):
            A += Q**(-v*r)*F[2*v]/(F[v]*a*b*F[v-r])
            a *= 1-Q**(v+1-h)
            b *= 1-Q**(v+1+h)
        actual = literal_U(N, r, chi)
        error = abs(A/D-actual)/max(1, abs(actual))
        assert error < mp.mpf('1e-44')
        if r+2 <= M:
            p, q2 = pq(mp.mpf(r)/N, chi, mp.mpf(1)/N)
            residual = actual-p*literal_U(N, r+1, chi)-q2*literal_U(N, r+2, chi)
            assert abs(residual) < mp.mpf('1e-44')*max(1, abs(actual))
        rows.append({'r': r, 'canonical_marked_factorial_relative_error': float(error)})
    return {'N': N, 'complex_chi': [float(mp.re(chi)), float(mp.im(chi))],
            'literal_factorial_source_on_both_sides_of_quarter': rows}


def actual_selected_complex_profiles(N):
    mp.mp.dps = 55
    rows = []
    # This is a calibration of literal finite source values and their
    # explicitly endpoint-normalized transport, not a test of a formal branch alone.
    for offset, chi in ((-1, mp.mpc('.008', '.004')),
                        (0, mp.mpc('.012')),
                        (1, mp.mpc('.008', '.004'))):
        r = N//4+offset
        tau = mp.mpf(r)/N
        S = mp.quad(lambda t: mp.log(mu(t, chi)), [tau, mp.mpf('.5')])
        C = mp.sqrt(mu(tau, chi))*mp.exp(
            mp.quad(lambda t: nu_over_mu(t, chi), [tau, mp.mpf('.5')]))
        actual = literal_U(N, r, chi)
        prediction = C*mp.exp(N*S)
        ratio = actual/prediction
        assert N*abs(ratio-1) < 6
        assert actual != 0 and abs(C) > mp.mpf('.1')
        rows.append({'r': r, 'chi': [float(mp.re(chi)), float(mp.im(chi))],
                     'actual_source_over_calibrated_transport': [float(mp.re(ratio)), float(mp.im(ratio))],
                     'N_times_relative_error': float(N*abs(ratio-1))})
    print(f'N={N} literal complex-color quarter packet Nerr='
          f'{max(row["N_times_relative_error"] for row in rows):.8f}', flush=True)
    return {'N': N, 'selected_original_complex_source_profiles': rows}


def crossing_first_normal(N):
    mp.mp.dps = 110
    d = N-1
    q = mp.exp(mp.j*mp.pi/N)
    Q, x = q*q, q**d
    kappa = mp.exp(mp.j*mp.pi*d*d/(2*N))
    diagonal = [q+1/q-q*(1-Q**v)**2-(1-Q**(v+1))**2/q for v in range(N)]
    off = [-(1-Q**(v+1))**2 for v in range(N)]
    f = [[mp.mpc(1)]]
    f.append([-diagonal[0]/off[0], 1/off[0]])
    for v in range(1, d):
        out = [mp.mpc(0)]*(v+2)
        for k, a in enumerate(f[v]):
            out[k] -= diagonal[v]*a
            out[k+1] += a
        for k, a in enumerate(f[v-1]):
            out[k] -= off[v-1]*a
        f.append([a/off[v] for a in out])
    # Literal physical continuant identity f_d=x^d R/kappa.
    Rcoeff = [kappa*x**(-d)*a for a in f[d]]
    normals = 0
    for j in range((N+1)//2):
        theta = (2*j-d)*mp.pi/N
        c = -2*mp.cos(theta)
        value, derivative = evaluate(Rcoeff, c)
        gauss = mp.exp(mp.j*mp.pi*d*d/(4*N)+mp.j*N*theta*theta/(4*mp.pi))
        assert abs(value-gauss) < mp.mpf('1e-85')
        if 2*j != d:
            actual_theta_derivative = derivative*2*mp.sin(theta)
            predicted = gauss*mp.j*N*theta/(2*mp.pi)
            assert abs(actual_theta_derivative-predicted) < mp.mpf('1e-85')
            normals += 1
    return {'N': N, 'literal_physical_continuant_crossing_value_and_first_normal': normals,
            'odd_simple_node_only_value_when_present': True}


if __name__ == '__main__':
    result = {'status': 'PASS', 'symbolic_selected_color_curvature': symbolic_curvature(),
              'full_physical_mixed_circle_input': [actual_two_band(N) for N in range(2, 9)],
              'all_physical_low_color_alias_input': [actual_alias(N) for N in range(2, 9)],
              'canonical_complex_factorial_source': [canonical_source_across_quarter(N) for N in (12, 13)],
              'full_crossing_normals_for_outer_source': [crossing_first_normal(N) for N in range(2, 11)],
              'supplementary_complex_selected_quarter_profiles': [actual_selected_complex_profiles(N)
                    for N in (32, 33, 64, 65, 128, 129)],
              'scope': 'Actual finite mixed-circle and alias operators, canonical complex factorial continuation, '
                       'selected finite source across quarter, and original crossing first normals. '
                       'The written analytic barrier/cotangent/frozen-block proofs establish uniform domains and gaps; '
                       'finite profiles do not prove them. No outer-color transfer or moving-q turn jet is inferred.'}
    Path(__file__).with_name('actual_belt_stack_auxiliary_color_inner_packet_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: seven full physical mixed-circle and alias families; two canonical complex-source families; '
          'nine original crossing-normal families; six all-parity actual complex quarter-source profiles.')
