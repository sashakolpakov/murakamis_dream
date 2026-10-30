#!/usr/bin/env python3
"""Exact magnetic continuation and focused complex-amplitude calibrations."""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_q_hahn_uniform_complex_amplitude import chosen_packet, sine_data, exact_equation
from audit_actual_q_hahn_selected_complex_action import energy


def mul(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    return c


def add(*arrays, p):
    out = [0]*max(map(len, arrays))
    for a in arrays:
        for k, c in enumerate(a):
            out[k] = (out[k]+c) % p
    return out


def scale(a, c, p):
    return [x*c % p for x in a]


def exact_level(N):
    p, eta, q, *_ = balanced_data(N)
    Q = q*q % p
    imag = pow(eta, N, p)
    sine = lambda r: (pow(q, r, p)-pow(q, -r, p))*pow(2*imag, -1, p) % p
    sf = [1]
    for r in range(1, N):
        sf.append(sf[-1]*2*sine(r) % p)
    beta = lambda t, j: sf[t]*pow(sf[j]*sf[t-j] % p, -1, p) % p
    count = shifts = equations = 0
    d = N-1
    for j in range(d//2+1):
        previous = None
        residual = [1]
        for t in range(d-j, N):
            T = pow(Q, t, p)
            h, n = d-t, t+j-d
            w = pow(q, n, p)
            G = [0]*(j+1)
            for a in range(j+1):
                m = j-a
                term = [1]
                for r in range(a):
                    term = mul(term, [-pow(Q, r, p), 1], p)
                for r in range(m):
                    term = mul(term, [T, -pow(Q, r, p)], p)
                coefficient = (pow(w, a, p)*pow(q, -m*t-(a*(a-1)+m*(m-1))//2, p)
                               *pow(sf[a]**2*sf[m]**2 % p, -1, p)) % p
                G = add(G, scale(term, coefficient, p), p=p)
            G = scale(G, pow(imag, -j, p)*sf[j]*pow(beta(t, j), -1, p), p)
            assert sum(G) % p == 1
            if previous is not None:
                prior = t-1
                first = mul([1, -1], [c*pow(Q, -k, p) % p for k, c in enumerate(previous)], p)
                second = mul([-pow(Q, t, p), 1], previous, p)
                result = scale(add(scale(first, pow(Q, j, p), p), second, p=p),
                               pow(1-pow(Q, t, p), -1, p), p)
                assert result[:j+1] == G and all(c == 0 for c in result[j+1:])
                shifts += 1
            else:
                base = [1]
                denominator = 1
                for k in range(1, j+1):
                    base = mul(base, [1, -pow(Q, k, p)], p)
                    denominator = denominator*(1-pow(Q, k, p)) % p
                assert scale(base, pow(denominator, -1, p), p) == G

            B = [1]
            for r in range(h):
                B = mul(B, [1, pow(q, h-1-2*r, p)], p)
            denominator = 1
            for k in range(1, j+1):
                denominator = denominator*(1-pow(Q, k, p)) % p
            c = pow(q, j*n, p)*pow(denominator, -1, p) % p
            rotated = [co*pow(q, t*k, p) % p for k, co in enumerate(G)]
            assert rotated == scale(mul(B, residual, p), c, p)

            # Entire magnetic Casimir identity, independent of sampling.
            rj = pow(q, 2*j+1, p)
            Aplus = scale(mul([-T, 1], [1, -Q], p), pow(T, -1, p), p)
            Aminus = scale(mul([-Q*T, 1], [1, -1], p), pow(Q*T % p, -1, p), p)
            diagonal = [-(rj+pow(rj, -1, p)),
                        2*(pow(q, -1, p)+q*T)*pow(T, -1, p),
                        -(q+pow(q, -1, p))*pow(T, -1, p)]
            residual_equation = add(
                scale(mul(Aplus, [co*pow(Q, k, p) % p for k, co in enumerate(G)], p), -pow(rj, -1, p), p),
                scale(mul(Aminus, [co*pow(Q, -k, p) % p for k, co in enumerate(G)], p), -rj, p),
                mul(diagonal, G, p), p=p)
            assert not any(residual_equation)
            equations += 1
            count += 1
            previous = G
            if h:
                at = lambda k: residual[k] if 0 <= k < len(residual) else 0
                residual = [(sine(j+h-k)*at(k)+2*sine(j-k+1)*at(k-1)
                             +sine(n-k+2)*at(k-2))*pow(sine(h), -1, p) % p
                            for k in range(n+2)]
    return dict(N=N, entire_polynomials=count, exact_coproduct_steps=shifts,
                exact_root_factorizations=count, entire_Casimir_identities=equations)


def exact_joint_continuation():
    """Independent finite sine products at unconstrained square-root values."""
    checks = nontrivial = phase_regressions = 0
    for N in range(3, 16):
        p, eta, q, *_ = balanced_data(N)
        Q = q*q % p
        imag = pow(eta, N, p)
        sf = [1]
        for k in range(1, N):
            sf.append(sf[-1]*(pow(q, k, p)-pow(q, -k, p))*pow(imag, -1, p) % p)

        def beta(z, a):
            value = 1
            for k in range(a):
                value = value*(z*pow(q, -k, p)-pow(z, -1, p)*pow(q, k, p))*pow(imag, -1, p) % p
            return value*pow(sf[a], -1, p) % p

        for j in range((N-1)//2+1):
            for qu, qv in ((2, 3), (5, 7), (11, 13)):
                U, V = qu*qu % p, qv*qv % p
                qt = qu*qv % p
                denominator = beta(qt, j)
                if not denominator:
                    continue
                w = qt*pow(q, j-(N-1), p) % p
                direct = sum(pow(w, a, p)*beta(pow(q, j, p), a)*beta(qu, a)*beta(qv, j-a)
                             for a in range(j+1)) % p
                direct = direct*pow(qu, -j, p)*pow(denominator, -1, p) % p
                H = wrong = 0
                for a in range(j+1):
                    term = pow(beta(pow(q, j, p), a), 2, p)*pow(V, a, p) % p
                    for k in range(a):
                        term = term*(U-pow(Q, k, p)) % p
                    for k in range(j-a):
                        term = term*(V-pow(Q, k, p)) % p
                    H = (H+term*pow(q, a*(2*j-a-(N-1)), p)) % p
                    wrong = (wrong+term*pow(q, a*(a-(N-1)), p)) % p
                D = 1
                for k in range(j):
                    D = D*(U*V-pow(Q, k, p)) % p
                assert direct == H*pow(D, -1, p) % p
                checks += 1
                nontrivial += j >= 2
                phase_regressions += j >= 2 and H != wrong
    assert phase_regressions > 0
    return dict(exact_bivariate_sine_product_checks=checks,
                checks_with_channel_at_least_two=nontrivial,
                detected_sine_vs_Gaussian_phase_mismatches=phase_regressions)


def residual_coefficients(N, j, t):
    theta = mp.pi/N
    coefficients = [mp.mpf(1)]
    for h in range(j, N-1-t, -1):
        n = j-h
        at = lambda k: coefficients[k] if 0 <= k < len(coefficients) else mp.mpf(0)
        coefficients = [(mp.sin((j+h-k)*theta)*at(k)
                         +2*mp.sin((j-k+1)*theta)*at(k-1)
                         +mp.sin((n-k+2)*theta)*at(k-2))/mp.sin(h*theta)
                        for k in range(n+2)]
        assert all(c > 0 for c in coefficients)
    return coefficients


def factored_source(N, t, j, upsilon, coefficients=None):
    q = mp.exp(mp.pi*1j/N)
    Q = q*q
    h, n = N-1-t, t+j-(N-1)
    z = mp.exp(2*mp.pi*1j*upsilon)/q**t
    if coefficients is None:
        coefficients = residual_coefficients(N, j, t)
    A = mp.polyval(list(reversed(coefficients)), z)
    B = mp.fprod(1+q**(h-1-2*r)*z for r in range(h))
    c = q**(j*n)/mp.fprod(1-Q**k for k in range(1, j+1))
    return mp.exp(mp.pi*1j*(N-1-2*j)*upsilon)*c*B*A


def direct_source(N, t, j, upsilon):
    q = mp.exp(mp.pi*1j/N)
    sf = [mp.mpf(1)]
    for k in range(1, N):
        sf.append(sf[-1]*2*mp.sin(mp.pi*k/N))
    beta = lambda z, a: mp.fprod(2*mp.sin(mp.pi*(z-r)/N) for r in range(a))/sf[a]
    u = N*upsilon
    value = mp.fsum(q**((t+j-N+1)*a)*beta(j, a)*beta(u, a)*beta(t-u, j-a)
                   for a in range(j+1))/beta(t, j)
    return mp.exp(mp.pi*1j*u)*q**(-(j+1)*u)*value


def complex_packet(tau, xi, upsilon):
    real_u = mp.re(upsilon)
    w = mp.exp(mp.pi*1j*(tau+xi-1))
    _, amplitude0, alpha, _ = chosen_packet(tau, xi, real_u, w)
    _, B, Fs, _ = sine_data(tau, xi, real_u, alpha, w)
    previous = B*Fs
    phase = mp.arg(previous)
    # Recover the amplitude's actual square-root sheet at the real anchor.
    C0 = mp.sin(mp.pi*xi)*mp.sqrt(mp.sin(mp.pi*real_u)*mp.sin(mp.pi*(tau-real_u))
                                *mp.sin(mp.pi*(tau-xi))/mp.sin(mp.pi*tau))/2
    root0 = mp.sqrt(2*mp.pi)*C0/amplitude0
    phase = 2*mp.arg(root0)
    for k in range(1, 61):
        u = real_u+(upsilon-real_u)*k/60
        alpha = mp.findroot(lambda a: sine_data(tau, xi, u, a, w)[0]
                                    -w*sine_data(tau, xi, u, a, w)[1],
                            (alpha, alpha+mp.mpf('0.000001')), tol=mp.mpf('1e-105'))
        A, B, Fs, _ = sine_data(tau, xi, u, alpha, w)
        current = B*Fs
        increment = mp.arg(current/previous)
        assert abs(increment) < mp.pi/2
        phase += increment
        previous = current
        args = (alpha, xi-alpha, u-alpha, tau-u-xi+alpha)
        assert all(0 < mp.re(v) < 1 for v in args)
    C = mp.sin(mp.pi*xi)*mp.sqrt(mp.sin(mp.pi*upsilon)*mp.sin(mp.pi*(tau-upsilon))
                               *mp.sin(mp.pi*(tau-xi))/mp.sin(mp.pi*tau))/2
    Acal = mp.sqrt(2*mp.pi)*C/(mp.sqrt(abs(previous))*mp.exp(1j*phase/2))
    amplitude = Acal*mp.exp(mp.pi*1j*(alpha-upsilon))
    action = energy(tau, xi, upsilon, alpha)+alpha*mp.log(w)+mp.pi*1j*upsilon*(1-xi)
    return action, amplitude


def numerical():
    mp.mp.dps = 130
    direct_checks = 0
    for N, t, j in ((7, 5, 3), (11, 8, 4), (20, 16, 8), (11, 5, 5)):
        for nu in (mp.mpc('0.24', '0.03'), mp.mpc('0.41', '-0.04')):
            direct = direct_source(N, t, j, nu)
            factor = factored_source(N, t, j, nu)
            assert abs(direct/factor-1) < mp.mpf('1e-100')
            direct_checks += 1

    roots = 0
    maximum_imaginary = 0.0
    for N in range(3, 24):
        for j in range(1, (N-1)//2+1):
            for t in range(N-1-j, N):
                co = residual_coefficients(N, j, t)
                if len(co) == 1:
                    continue
                values = np.roots(np.array([float(c/max(co)) for c in reversed(co)]))
                error = max(abs(values.imag))/max(1, max(abs(values)))
                assert error < 1e-7
                assert max(values.real) < 0
                maximum_imaginary = max(maximum_imaginary, float(error))
                roots += 1

    rows = []
    maximum_error = 0.0
    for tau_target, xi_target in ((mp.mpf('.8'), mp.mpf('.4')),
                                  (mp.mpf('.8'), mp.mpf('.5')),
                                  (mp.mpf('.9'), mp.mpf(1)/3),
                                  (mp.mpf('.7'), mp.mpf('.3'))):
        for N in (32, 65, 128, 257):
            j = (N-1)//2 if xi_target == mp.mpf('.5') else int(mp.floor(xi_target*N))
            t = N-1-j if tau_target == mp.mpf('.7') else int(mp.floor(tau_target*N))
            tau, xi = mp.mpf(t)/N, mp.mpf(j)/N
            co = residual_coefficients(N, j, t)
            for fraction, imaginary in ((mp.mpf('.5'), mp.mpf('.06')),
                                         (mp.mpf('.35'), mp.mpf('-.04'))):
                nu = tau*fraction+1j*imaginary
                phase, amplitude = complex_packet(tau, xi, nu)
                predicted = amplitude*mp.exp(N*phase)/mp.sqrt(N)
                actual = factored_source(N, t, j, nu, co)
                error = N*abs(actual/predicted-1)
                assert error < 10
                maximum_error = max(maximum_error, float(error))
                rows.append(dict(N=N, t=t, j=j, upsilon=[float(mp.re(nu)), float(mp.im(nu))],
                                 N_times_relative_error=float(error), amplitude_modulus=float(abs(amplitude))))
    return dict(precision_digits=mp.mp.dps, direct_entire_source_comparisons=direct_checks,
                negative_residual_root_regressions=roots, maximum_relative_root_imaginary=maximum_imaginary,
                complex_magnetic_amplitudes=len(rows), maximum_N_times_relative_error=maximum_error,
                cases=rows)


def main():
    levels = [exact_level(N) for N in range(2, 18)]
    original = [exact_equation(N, physical=True) for N in (3, 5, 8, 11)]
    result = dict(status='PASS', exact_levels=levels,
                  independent_original_Casimir_entries=sum(r['original_Casimir_entries'] for r in original),
                  joint_continuation=exact_joint_continuation(),
                  numerical=numerical(),
                  scope='Exact terminating magnetic continuation, actual coproduct factorization and full Casimir difference equation. Complex amplitudes are finite regressions of the proved theorem. The amplitude theorem keeps t and j real and discrete; the appendix gives an exact joint rational continuation, without a joint complex asymptotic or assembled-source claim.')
    Path(__file__).with_name('actual_q_hahn_magnetic_complex_corridor_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', entire_polynomials=sum(r['entire_polynomials'] for r in levels),
                          exact_coproduct_steps=sum(r['exact_coproduct_steps'] for r in levels),
                          entire_Casimir_identities=sum(r['entire_Casimir_identities'] for r in levels),
                          independent_original_Casimir_entries=result['independent_original_Casimir_entries'],
                          **result['joint_continuation'],
                          **{k: v for k, v in result['numerical'].items() if k != 'cases'}), indent=2))


if __name__ == '__main__':
    main()
