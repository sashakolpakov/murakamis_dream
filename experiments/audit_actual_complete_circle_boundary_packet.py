#!/usr/bin/env python3
"""Literal boundary-packet checks; the analytic theorem is proved in the note.

Finite calibrations below are supplementary and do not prove an asymptotic
or certify the size of its existential complex neighborhood.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from diagnose_pretzel_coherent_radial_capacity import evaluate, source_polynomial


def symbolic_transport():
    Q, Y, lam = sp.symbols('Q Y lam')
    a = (2*Q**3*Y**2+Q+1)/(Q*(1-Q*Y)**2)
    b = -(1-Q**3*Y**2)*(1+Q**2*Y)/(Q*(1-Q*Y)**2*(1-Q**2*Y))
    a0, b0 = a.subs(Q, 1), b.subs(Q, 1)
    assert sp.factor(a0+b0-1) == 0
    fast = ((Y+1)/(Y-1))**2
    assert sp.factor(lam**2-a0*lam-b0-(lam-1)*(lam-fast)) == 0
    assert sp.factor(a0+2*b0+4*Y/(1-Y)**2) == 0
    ode = sp.factor(-2*sp.I*sp.diff(a+b, Q).subs(Q, 1)/(a0+2*b0))
    assert sp.factor(ode-sp.I*Y/(Y-1)) == 0
    # q-chirping the literal normalized U recurrence, with nu_(r+1)/nu_r=-QY.
    p = -(2*Q**3*Y**2+Q+1)/(Q**2*Y*(1-Q*Y)**2)
    q2 = -(1-Q**3*Y**2)*(1+Q**2*Y)/(Q**4*Y**2*(1-Q*Y)**2*(1-Q**2*Y))
    assert sp.factor(p*(-Q*Y)-a) == 0
    assert sp.factor(q2*(Q**3*Y**2)-b) == 0
    return {'exact_high_to_low_chirped_recurrence': True,
            'simple_roots_one_and_negative_cotangent_squared': True,
            'exact_first_transport_equation': str(ode)}


def finite_original_sources():
    rows = []
    for N in range(2, 13):
        mp.mp.dps = 120
        d, M = N-1, (N-1)//2
        q = mp.exp(mp.j*mp.pi/N)
        Q, kappa = q*q, mp.exp(mp.j*mp.pi*d*d/(2*N))
        F, s = [mp.mpc(1)], [mp.mpf(1)]
        for r in range(1, N):
            F.append(F[-1]*(1-Q**r))
            s.append(s[-1]*2*mp.sin(mp.pi*r/N))
        A = [mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r])
                     for v in range(r, M+1)) for r in range(M+1)]
        U = [A[r]/(Q**(-r*r)*F[2*r]/F[r]**3) for r in range(M+1)]
        W = [mp.exp(mp.j*mp.pi*d/4)*U[r]/(kappa*(-1)**r*q**(r*(r+1)))
             for r in range(M+1)]
        for r in range(max(0, M-1)):
            Y = Q**r
            a = (2*Q**3*Y**2+Q+1)/(Q*(1-Q*Y)**2)
            b = -(1-Q**3*Y**2)*(1+Q**2*Y)/(Q*(1-Q*Y)**2*(1-Q**2*Y))
            error = abs(W[r]-a*W[r+1]-b*W[r+2])
            assert error < mp.mpf('1e-90')*max(1, abs(W[r]), abs(a*W[r+1]), abs(b*W[r+2]))
        _, coefficients = source_polynomial(N, 120)
        maximum_error = mp.mpf(0)
        for c in (mp.mpf(-2), mp.mpc('-2.01', '.007'), mp.mpc('.31', '.29')):
            B, z, dz, dB = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(0)
            for r in range(M+1):
                coefficient = N*N*mp.exp(-mp.j*mp.pi*d/4)*s[2*r]*W[r]/s[r]**6
                direct = N*N/kappa*(-1)**r*q**(2*r*r+r)*A[r]/F[r]**3
                assert abs(coefficient-direct) < mp.mpf('1e-90')*max(1, abs(direct))
                z += coefficient*B
                dz += coefficient*dB
                node = q**(2*r+1)+q**(-2*r-1)
                dB, B = dB*(node-c)-B, B*(node-c)
            actual, derivative = evaluate(coefficients, c)
            error = max(abs(z-actual), abs(dz-derivative))/max(1, abs(actual), abs(derivative))
            maximum_error = max(maximum_error, error)
            assert error < mp.mpf('1e-85')
        # Actual parity-sensitive terminal source remains exactly W_M, not an assumed normalization.
        assert abs(U[M]-1) < mp.mpf('1e-90')
        rows.append({'N': N, 'literal_full_kappa_source_and_first_normal': True,
                     'all_regular_high_to_low_grid_steps': max(0, M-1),
                     'maximum_relative_source_error': float(maximum_error)})
    return rows


def j_action(eta):
    return 4*mp.catalan/mp.pi + eta*mp.quad(
        lambda t: mp.atan(mp.sinh(eta*t/2))/mp.pi, [0, 1])


def amplitude(eta):
    u = mp.atan(mp.cosh(eta/2))
    T = 2*mp.cosh(eta)
    return mp.exp(mp.j*u/2)/(2*((T+2)*(T+6))**mp.mpf('.25'))


def boundary_calibrations():
    rows, errors = [], {}
    points = [mp.mpc(0), mp.mpc('.04'), mp.mpc(0, '.04'), mp.mpc('.025', '.025')]
    for N in (32, 33, 64, 65, 128, 129):
        q, coefficients = source_polynomial(N, max(180, N+80))
        Q, d, M = q*q, N-1, (N-1)//2
        kappa = mp.exp(mp.j*mp.pi*d*d/(2*N))
        F = [mp.mpc(1)]
        for r in range(1, N):
            F.append(F[-1]*(1-Q**r))
        quarter_rows = []
        for r in sorted({N//4-1, N//4, N//4+1}):
            A = mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r, M+1))
            U = A/(Q**(-r*r)*F[2*r]/F[r]**3)
            W = mp.exp(mp.j*mp.pi*d/4)*U/(kappa*(-1)**r*q**(r*(r+1)))
            u = mp.pi*r/N
            scaled_error = N*abs(W/(mp.exp(mp.j*u/2)*mp.sqrt(mp.sin(u)))-1)
            assert scaled_error < 2
            quarter_rows.append({'r': r, 'N_times_actual_inner_amplitude_error': float(scaled_error)})
        phase = mp.exp(-mp.j*mp.pi*(N-1)/4)
        ratios = []
        for point_index, eta in enumerate(points):
            value, _ = evaluate(coefficients, -2*mp.cosh(eta))
            ratio = value/(phase*amplitude(eta)*mp.exp(N*j_action(eta)))
            errors[N, point_index] = abs(ratio-1)
            assert N*abs(ratio-1) < 3
            ratios.append({'eta': [float(mp.re(eta)), float(mp.im(eta))],
                           'ratio': [float(mp.re(ratio)), float(mp.im(ratio))]})
        z0, derivative = evaluate(coefficients, -2)
        normal = (derivative/z0)/(-mp.mpf(N)/(4*mp.pi))
        assert abs(normal-1) < mp.mpf(6)/N
        nodes = [q**(2*a+1)+q**(-2*a-1) for a in range(N)]
        values = [evaluate(coefficients, c)[0] for c in nodes]
        belts = []
        for k in (1, 2):
            actual = N*mp.fsum(abs(z)**(2*k) for z in values)
            prediction = (mp.mpf(N)**mp.mpf('1.5')*2**(-mp.mpf(9*k+1)/2)/mp.sqrt(k)
                          *mp.exp(2*k*N*j_action(0)))
            ratio = actual/prediction
            assert N*abs(ratio-1) < 8
            belts.append({'k': k, 'literal_complete_belt_over_predicted': float(ratio)})
        rows.append({'N': N, 'complex_boundary_packet_calibrations': ratios,
                     'actual_inner_source_on_both_sides_of_quarter': quarter_rows,
                     'first_normal_over_predicted': [float(mp.re(normal)), float(mp.im(normal))],
                     'whole_original_retained_belt': belts})
        print(f'N={N} boundary ratio={mp.nstr(ratios[0]["ratio"], 10)} '
              f'normal={mp.nstr(normal, 10)} belt1={belts[0]["literal_complete_belt_over_predicted"]:.9f}', flush=True)
    for parity in (0, 1):
        for point_index in range(len(points)):
            assert errors[128+parity, point_index] < errors[64+parity, point_index] < errors[32+parity, point_index]
    return rows


def analytic_local_constants():
    mp.mp.dps = 80
    assert abs(mp.diff(j_action, 0, 2)-1/(2*mp.pi)) < mp.mpf('1e-70')
    assert abs(amplitude(0)-2**(-mp.mpf(9)/4)*mp.exp(mp.j*mp.pi/8)) < mp.mpf('1e-70')
    delta = mp.mpf('.0001')
    anchor, halfwidth = mp.pi/4+2*delta, delta/4
    actions = [mp.quad(lambda v: 2*mp.log(mp.cot(v)), [u, anchor])/mp.pi
               for u in (mp.pi/4-halfwidth, mp.pi/4, mp.pi/4+halfwidth)]
    assert max(actions) < -delta**2
    # The chosen numerical delta illustrates only the SIGN; the proof additionally
    # chooses it below the computed superadiabatic remainder barrier.
    return {'action_second_derivative_at_boundary': mp.nstr(1/(2*mp.pi), 25),
            'amplitude_at_boundary': [mp.nstr(mp.re(amplitude(0)), 25), mp.nstr(mp.im(amplitude(0)), 25)],
            'high_to_low_fast_action_samples': [mp.nstr(a, 25) for a in actions],
            'barrier_comparison_proved_analytically_not_inferred_from_samples': True}


if __name__ == '__main__':
    result = {'status': 'PASS', 'symbolic_actual_transport': symbolic_transport(),
              'local_analytic_constants': analytic_local_constants(),
              'literal_original_source_families': finite_original_sources(),
              'supplementary_all_parity_calibrations': boundary_calibrations(),
              'scope': 'Finite source/chirp/normal identities and supplementary asymptotic calibrations. '
                       'The fixed complex-neighborhood theorem and endpoint-current estimates are the written proof; '
                       'the finite tests do not certify its neighborhood size. Spectral eta is not identified '
                       'with independently changed physical auxiliary color.'}
    Path(__file__).with_name('actual_complete_circle_boundary_packet_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: symbolic backward source, eleven literal full sources/normals, six all-parity boundary/belt calibrations.')
