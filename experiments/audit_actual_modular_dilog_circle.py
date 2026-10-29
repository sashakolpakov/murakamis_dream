#!/usr/bin/env python3
"""Independent analytic checks of the full-dilogarithm relative moments.

The proof is in notes/actual_modular_dilog_circle_and_boundary_source.md.
The numerical moment evaluates the entire circle plus its radial source;
it does not truncate the full function to the target Taylor polynomial.
"""

import json
from pathlib import Path

import mpmath as mp


def log_psi_inside(N, epsilon, z):
    t = mp.exp(z)
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    log_v = (mp.mpf(N - 1) / (2 * N) * mp.log(1 - t**N)
             - sum(mp.mpf(ell) / N * mp.log(1 - Q**ell * t)
                   for ell in range(1, N)))
    log_f = (log_v + (mp.mpf(N + 1) / (2 * N)
                     + epsilon * 1j * z / (2 * mp.pi)) * mp.log(1 - t**N)
             + epsilon * 1j * mp.polylog(2, t**N) / (2 * mp.pi * N))
    return log_f


def psi(N, epsilon, z):
    return mp.exp(log_psi_inside(N, epsilon, z))


def log_derivative(N, epsilon, z):
    t = mp.exp(z)
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    finite = sum(mp.mpf(ell) / N * Q**ell * t / (1 - Q**ell * t)
                 for ell in range(1, N))
    return finite - N * (1 + epsilon * 1j * z / (2 * mp.pi)) * t**N / (1 - t**N)


def strip_leading_checks():
    rows = []
    for N in [12, 24, 48]:
        for radius, theta in [(mp.mpf('.7'), mp.mpf('.8')),
                              (mp.mpf('1'), mp.mpf('1.3')),
                              (mp.mpf('1.6'), mp.mpf('2.2')),
                              (mp.mpf('3'), mp.mpf('4.4'))]:
            z = mp.log(radius) + 1j * theta
            start = mp.log(mp.mpf('.55'))
            # Continue the exact meromorphic logarithmic derivative;
            # no independent principal branches are assigned outside |t|<1.
            actual = log_psi_inside(N, 1, start + 1j * theta)
            actual += mp.quad(lambda u: log_derivative(N, 1, u + 1j * theta),
                              [start, 0, mp.re(z)] if radius >= 1
                              else [start, mp.re(z)])
            t = mp.exp(z)
            leading = N * mp.polylog(2, t) / (2j * mp.pi) + mp.log(1 - t) / 2
            scaled = N * abs(actual - leading)
            assert scaled < mp.mpf('2'), (N, radius, theta, scaled)
            rows.append({'N': N, 'radius': str(radius), 'theta': str(theta),
                         'N_times_log_remainder': float(scaled)})
    return rows


def original_v(N, epsilon, a):
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    factorial = mp.fprod(1 - Q**j for j in range(1, a + 1))
    return (-1)**a * Q**(a * (a - 1) // 2) / factorial


def exact_function_checks():
    rows = []
    for N in [2, 3, 5, 8, 11]:
        for epsilon in [-1, 1]:
            for t in [mp.mpf('.17'), mp.mpf('.71'), mp.mpf('.96')]:
                z = mp.log(t)
                f = psi(N, epsilon, z)
                whole = psi(N, epsilon, z + epsilon * 2j * mp.pi)
                step = psi(N, epsilon, z + epsilon * 2j * mp.pi / N)
                errors = [abs(whole / f - 1 / (1 - t**N)),
                          abs(step / f - 1 / (1 - t)),
                          abs(abs(f)**2 - (1 - t) * (1 - t**N))]
                assert max(errors) < mp.mpf('1e-38'), errors
                rows.append({'N': N, 'epsilon': epsilon, 't': str(t),
                             'max_error': float(max(errors))})
    return rows


def relative_moment(N, epsilon, a, R):
    logR = mp.log(R)

    def angular(theta):
        z = logR + epsilon * 1j * theta
        return psi(N, epsilon, z) * mp.exp(-a * z) / (2 * mp.pi)

    # Split at all angular root directions; every calculation has R<1,
    # so the explicit anchored formula requires no implicit continuation.
    cuts = [2 * mp.pi * j / N for j in range(N + 1)]
    bulk = mp.quad(angular, cuts)

    def radial(t):
        if not t:
            return mp.mpf(1) if a == N - 1 else mp.mpf(0)
        return psi(N, epsilon, mp.log(t)) * t**(N - a - 1) / (1 - t**N)

    error = epsilon * mp.quad(radial, [0, R / 2, R]) / (2j * mp.pi)
    expected = original_v(N, epsilon, a)
    residual = abs(bulk - error - expected)
    assert residual < mp.mpf('1e-30'), (N, epsilon, a, R, residual)
    bound = R**(N - a) / (2 * mp.pi * (N - a))
    assert abs(error) <= bound + mp.mpf('1e-35')
    return {'N': N, 'epsilon': epsilon, 'a': a, 'R': str(R),
            'relative_cycle_error': float(residual),
            'radial_modulus': float(abs(error)), 'radial_bound': float(bound),
            'bare_circle_error': float(abs(bulk - expected))}


def reflection_and_operator_checks():
    rows = []
    for N in range(2, 16):
        Q = mp.exp(2j * mp.pi / N)
        F = [mp.mpc(1)]
        for a in range(1, N):
            F.append(F[-1] * (1 - Q**a))
        for a in range(N):
            reciprocal = Q**(-a) * original_v(N, -1, a)
            positive = N * Q**(N - 1 - a) * original_v(N, 1, N - 1 - a)
            assert abs(reciprocal - 1 / F[a]) < mp.mpf('1e-37')
            assert abs(positive - F[a]) < mp.mpf('1e-37')
        harmonic = mp.fsum(mp.mpf(1) / a for a in range(1, N + 1))
        # The complete row of coefficient bounds sums to the claimed
        # nilpotent unit-shift bound, including the endpoint coefficient.
        error_bounds = [1 / (2 * mp.pi * (N - a)) for a in range(N)]
        assert abs(mp.fsum(error_bounds) - harmonic / (2 * mp.pi)) < mp.mpf('1e-40')
        rows.append({'N': N, 'all_original_diagonal_reflections': True,
                     'unit_shift_radial_norm_bound': float(harmonic / (2 * mp.pi)),
                     'reciprocal_diagonal_bound': float(1 / (2 * mp.pi)),
                     'positive_diagonal_bound': float(N / (2 * mp.pi))})
    return rows


def main():
    mp.mp.dps = 48
    function_rows = exact_function_checks()
    moment_rows = []
    for N, R in [(2, mp.mpf('.7')), (3, mp.mpf('.8')), (5, mp.mpf('.9'))]:
        for epsilon in [-1, 1]:
            for a in sorted({0, N // 2, N - 1}):
                moment_rows.append(relative_moment(N, epsilon, a, R))
    assert any(row['bare_circle_error'] > .001 for row in moment_rows)
    results = {'status': 'PASS',
               'exact_shift_monodromy_modulus_checks': function_rows,
               'full_circle_plus_radial_moments': moment_rows,
               'full_strip_interior_unit_and_exterior_phase_checks': strip_leading_checks(),
               'original_factorial_and_operator_bounds': reflection_and_operator_checks(),
               'scope': 'Local exact full-function relative source; no geometric-cycle selection inferred.'}
    path = Path(__file__).with_name('actual_modular_dilog_circle_results.json')
    path.write_text(json.dumps(results, indent=2) + '\n')
    print(f'PASS {len(function_rows)} shifts/moduli, {len(moment_rows)} full relative moments, '
          f'{len(results["original_factorial_and_operator_bounds"])} original diagonal/operator families, '
          f'{len(results["full_strip_interior_unit_and_exterior_phase_checks"])} full-strip phases')


if __name__ == '__main__':
    main()
