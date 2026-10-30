#!/usr/bin/env python3
"""Exact equation and actual finite-source calibration of the amplitude theorem.

The uniform asymptotic is proved in the note. Numerical error rates here
are normalization regressions, not a substitute for that proof.
"""
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_q_hahn_selected_complex_action import J, energy


def exact_equation(N, physical=False):
    p, eta, q, E, F, K, _, _, _ = balanced_data(N)
    imag = pow(eta, N, p)
    sine = lambda k: (pow(q, k, p)-pow(q, -k, p))*pow(2*imag, -1, p) % p
    sf = [1]
    for n in range(1, N):
        sf.append(sf[-1]*2*sine(n) % p)

    def beta(n, a):
        return sf[n]*pow(sf[a]*sf[n-a] % p, -1, p) % p if 0 <= a <= n else 0

    def coeff(t, j, u):
        v = t-u
        return {a: beta(j, a)*beta(u, a)*beta(v, j-a)*pow(beta(t, j), -1, p) % p
                for a in range(max(0, j-v), min(j, u)+1)}

    polynomials = endpoints = coefficient_equations = 0
    for t in range(N):
        for j in range(t+1):
            for u in range(t+1):
                v = t-u
                co = coeff(t, j, u)
                for a in range(min(co), max(co)+2):
                    lhs = sine(a)**2*sine(v-j+a)*co.get(a, 0)
                    rhs = sine(j-a+1)**2*sine(u-a+1)*co.get(a-1, 0)
                    assert (lhs-rhs) % p == 0
                    coefficient_equations += 1
                endpoints += 2
                polynomials += 1

    # Independent physical Casimir columns: this checks that the audited
    # polynomial and both +1 phases are the original source convention.
    original_entries = 0
    if physical:
        rho = (q-pow(q, -1, p)) % p
        Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
        Ki = np.diag([pow(int(k), -1, p) for k in np.diag(Kt)])
        O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
        d = N-1
        for t in range(N):
            ids = [u*N+t-u for u in range(t+1)]
            matrix = O[np.ix_(ids, ids)]
            for j in range(max(0, d-t), min(t, d//2)+1):
                node = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
                values = [1]
                for u in range(t):
                    numerator = (node-int(matrix[u, u]))*values[u]
                    if u:
                        numerator -= int(matrix[u, u-1])*values[u-1]
                    values.append(numerator*pow(int(matrix[u, u+1]), -1, p) % p)
                for u, value in enumerate(values):
                    delta = t+j-d
                    fourier = sum(c*pow(q, a*delta, p) for a, c in coeff(t, j, u).items()) % p
                    fourier = fourier*pow(-1, u, p)*pow(q, -(j+1)*u, p) % p
                    assert value == fourier
                    original_entries += 1
    return dict(N=N, original_polynomials=polynomials,
                coefficient_equations=coefficient_equations,
                support_endpoints=endpoints, original_Casimir_entries=original_entries)


def symbolic_transport():
    w, b0, b1, b2, a1, a2 = sp.symbols('w b0 b1 b2 a1 a2')
    Fs = a1-w*b1
    Fss = a2-w*b2
    da = w*b0/Fs
    dlog_amplitude = -sp.Rational(1, 2)*(b1*da/b0+(Fss*da-w*b1)/Fs)
    assert sp.cancel(dlog_amplitude+da*Fss/(2*Fs)) == 0
    # The exact +1 in the Fourier exponent and in q^{-(j+1)u}.
    N, alpha, upsilon, xi = sp.symbols('N alpha upsilon xi')
    exact_prefactor_log = sp.pi*sp.I*(N*upsilon-(N*xi+1)*upsilon)
    target = N*sp.pi*sp.I*upsilon*(1-xi)+sp.pi*sp.I*(alpha-upsilon)
    assert sp.expand(exact_prefactor_log+sp.pi*sp.I*alpha-target) == 0
    return dict(transport_identity=True, both_integer_offset_phases=True)


def sine_data(t, x, u, a, w):
    s = lambda z: mp.sin(mp.pi*z)
    c = lambda z: mp.cos(mp.pi*z)
    r = t-u-x+a
    A = s(a)**2*s(r)
    B = s(x-a)**2*s(u-a)
    Ap = mp.pi*(2*s(a)*c(a)*s(r)+s(a)**2*c(r))
    Bp = -mp.pi*(2*s(x-a)*c(x-a)*s(u-a)+s(x-a)**2*c(u-a))
    App = mp.pi**2*(2*(c(a)**2-s(a)**2)*s(r)+4*s(a)*c(a)*c(r)-s(a)**2*s(r))
    Bpp = mp.pi**2*(2*(c(x-a)**2-s(x-a)**2)*s(u-a)
                        +4*s(x-a)*c(x-a)*c(u-a)-s(x-a)**2*s(u-a))
    return A, B, Ap-w*Bp, App-w*Bpp


def chosen_packet(t, x, u, w):
    lo = max(mp.mpf(0), u-t+x)
    hi = min(x, u)
    left, right = lo, hi
    for _ in range(420):
        a = (left+right)/2
        A, B, _, _ = sine_data(t, x, u, a, 1)
        if A < B:
            left = a
        else:
            right = a
    a = (left+right)/2
    A, B, Fs, Fss = sine_data(t, x, u, a, 1)
    previous = B*Fs
    assert mp.re(previous) > 0 and abs(mp.im(previous)) < mp.mpf('1e-110')
    phase = mp.mpf(0)
    for step in range(1, 81):
        z = 1+(w-1)*step/80
        a = mp.findroot(lambda b: sine_data(t, x, u, b, z)[0]
                                 -z*sine_data(t, x, u, b, z)[1],
                        (a, a+mp.mpf('0.000001')), tol=mp.mpf('1e-115'))
        A, B, Fs, Fss = sine_data(t, x, u, a, z)
        current = B*Fs
        increment = mp.arg(current/previous)
        assert abs(increment) < mp.pi/2
        phase += increment
        previous = current
        assert lo < mp.re(a) < hi
    assert abs(A-w*B) < mp.mpf('1e-105')
    s = lambda z: mp.sin(mp.pi*z)
    C = s(x)*mp.sqrt(s(u)*s(t-u)*s(t-x)/s(t))/2
    amplitude = mp.sqrt(2*mp.pi)*C/(mp.sqrt(abs(previous))*mp.exp(1j*phase/2))
    action = energy(t, x, u, a)+a*mp.log(w)
    dalpha = w*B/Fs
    transport = -dalpha*Fss/(2*Fs)
    return action, amplitude, a, transport


def original_coefficients(N, t, j, u):
    logs = [mp.mpf(0)]
    for n in range(1, N):
        logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*n/N)))

    def lb(n, a):
        return logs[n]-logs[a]-logs[n-a]

    lo, hi = max(0, j-t+u), min(j, u)
    lc = [lb(j, a)+lb(u, a)+lb(t-u, j-a)-lb(t, j) for a in range(lo, hi+1)]
    scale = max(lc)
    return lo, [mp.exp(c-scale) for c in lc], scale


def evaluate(N, co, w):
    lo, coefficients, scale = co
    moments = [mp.fsum(((lo+i)**k)*c*w**(lo+i) for i, c in enumerate(coefficients))
               for k in range(2)]
    return mp.exp(scale)*moments[0], moments[1]/(N*moments[0])


def numerical_calibration():
    mp.mp.dps = 140
    cases = [(mp.mpf(4)/5, mp.mpf(2)/5, mp.mpf(7)/20),
             (mp.mpf(4)/5, mp.mpf(1)/2, mp.mpf(7)/20),
             (mp.mpf(9)/10, mp.mpf(1)/3, mp.mpf(2)/5)]
    levels = (40, 81, 160, 321, 642)
    targets = (mp.mpc(1), mp.mpc('1.3', '0.8'), mp.mpc('0.2', '-1.1'))
    output = []
    max_scaled = max_derivative = max_physical = 0.0
    for target in cases:
        for N in levels:
            t = int(mp.floor(target[0]*N))
            j = (N-1)//2 if target[1] == mp.mpf('0.5') else int(mp.floor(target[1]*N))
            u = int(mp.floor(target[2]*N))
            tau, xi, upsilon = (mp.mpf(n)/N for n in (t, j, u))
            co = original_coefficients(N, t, j, u)
            rows = []
            for w in targets:
                psi, amplitude, alpha, transport = chosen_packet(tau, xi, upsilon, w)
                predicted = amplitude*mp.exp(N*psi)/mp.sqrt(N)
                actual, actual_alpha = evaluate(N, co, w)
                relative = actual/predicted-1
                scaled = N*abs(relative)
                derivative = N*N*abs(actual_alpha-alpha-transport/N)
                assert scaled < 10
                assert derivative < 10
                max_scaled = max(max_scaled, float(scaled))
                max_derivative = max(max_derivative, float(derivative))
                rows.append(dict(w=[float(mp.re(w)), float(mp.im(w))],
                                 N_times_relative_error=float(scaled),
                                 N_squared_derivative_remainder=float(derivative),
                                 amplitude_modulus=float(abs(amplitude))))
            # Original physical source, expanded at w_star rather than
            # at w_star exp(pi i/N): verifies BOTH integer offsets.
            w_star = mp.exp(mp.pi*1j*(tau+xi-1))
            psi, amplitude, alpha, _ = chosen_packet(tau, xi, upsilon, w_star)
            predicted = (amplitude/mp.sqrt(N)*mp.exp(mp.pi*1j*(alpha-upsilon))
                         *mp.exp(N*(psi+mp.pi*1j*upsilon*(1-xi))))
            q = mp.exp(mp.pi*1j/N)
            exact, _ = evaluate(N, co, q**(t+j-(N-1)))
            exact *= (-1)**u*q**(-(j+1)*u)
            physical_error = N*abs(exact/predicted-1)
            assert physical_error < 10
            max_physical = max(max_physical, float(physical_error))
            output.append(dict(N=N, t=t, j=j, u=u, complex_amplitudes=rows,
                               physical_N_times_relative_error=float(physical_error)))
    return dict(precision_digits=mp.mp.dps, finite_polynomials=len(output),
                complex_amplitude_cases=len(output)*len(targets),
                physical_offset_cases=len(output),
                maximum_N_times_relative_error=max_scaled,
                maximum_N_squared_derivative_remainder=max_derivative,
                maximum_physical_N_times_relative_error=max_physical, cases=output)


def main():
    levels = [exact_equation(N, physical=N <= 11) for N in range(2, 18)]
    result = dict(status='PASS', exact_levels=levels, symbolic=symbolic_transport(),
                  numerical=numerical_calibration(),
                  scope='Exact original finite equation and local nonzero complex amplitude, with actual real scaled parameters and both physical integer offsets. Numerical rates are regressions; the all-level uniform error is proved analytically. No complex magnetic interpolation, generic-q normal, or assembled-source asymptotic.')
    Path(__file__).with_name('actual_q_hahn_uniform_complex_amplitude_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS',
                          exact_polynomials=sum(x['original_polynomials'] for x in levels),
                          coefficient_equations=sum(x['coefficient_equations'] for x in levels),
                          support_endpoints=sum(x['support_endpoints'] for x in levels),
                          original_Casimir_entries=sum(x['original_Casimir_entries'] for x in levels),
                          **{k: v for k, v in result['numerical'].items() if k != 'cases'}), indent=2))


if __name__ == '__main__':
    main()
