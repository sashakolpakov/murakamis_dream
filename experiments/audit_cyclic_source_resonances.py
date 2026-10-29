#!/usr/bin/env python3
"""Exact source connections and resonant flags, with norm diagnostics.

No knot period is replaced or evaluated by the local regulator norms.
Finite-field identities include every residue r at the tested levels.
Complex calculations check the marked phase and an explicit proved bound.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_peripheral_fusion import inverse_mod
from audit_cyclic_steinberg_lattice import determinant
from audit_finite_sum_annihilator import field
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import dual_data


def rank_mod(matrix, prime):
    rows = np.array(matrix, dtype=np.int64).copy() % prime
    rank = 0
    for column in range(rows.shape[1]):
        pivot = next((j for j in range(rank, len(rows)) if rows[j, column]), None)
        if pivot is None:
            continue
        rows[[rank, pivot]] = rows[[pivot, rank]]
        rows[rank] = rows[rank] * pow(int(rows[rank, column]), -1, prime) % prime
        for j in range(rank + 1, len(rows)):
            rows[j] = (rows[j] - rows[j, column] * rows[rank]) % prime
        rank += 1
        if rank == len(rows):
            break
    return rank


def factorials(N, Q, z, prime):
    values = [1]
    for j in range(1, N):
        values.append(values[-1] * (1 - pow(Q, j, prime) * z) % prime)
    return values


def factorial_derivatives(N, Q, z, prime):
    values, derivatives = [1], [0]
    for j in range(1, N):
        qj = pow(Q, j, prime)
        derivatives.append((derivatives[-1] * (1 - qj * z) - qj * values[-1]) % prime)
        values.append(values[-1] * (1 - qj * z) % prime)
    return values, derivatives


def cap_moment(N, prime, q, M):
    Q, z = q * q % prime, M * M % prime
    p, dp = factorial_derivatives(N, Q, z, prime)
    pv, dpv = factorial_derivatives(N, Q, pow(z, -1, prime), prime)
    H, Hprime = 0, 0
    for a in range(N):
        b = N - 1 - a
        gaussian = pow(M, a, prime) * pow(q, a * a, prime) % prime
        H += pv[a] * gaussian * p[b]
        Hprime += ((-2 * pow(M, -3, prime) * dpv[a]) * gaussian * p[b]
                   + pv[a] * a * pow(M, -1, prime) * gaussian * p[b]
                   + pv[a] * gaussian * 2 * M * dp[b])
    S = sum(pow(z, j, prime) for j in range(N)) % prime
    Sprime = sum(2 * j * pow(M, 2 * j - 1, prime) for j in range(1, N)) % prime
    G = sum(pow(-1, a, prime) * pow(M, -a, prime) * pow(q, 2 * a * a + a, prime)
            for a in range(N)) % prime
    assert H % prime == S * G % prime
    if S == 0:
        assert Hprime % prime == Sprime * G % prime
    return G


def matrix_connection(N):
    """Evaluate T and its derivative without the asserted product formula."""
    prime, _, q = field(N)
    Q = q * q % prime
    records = []
    for z in range(1, prime):
        if pow(z, N, prime) == 1:
            continue
        X = np.zeros((N, N), dtype=np.int64)
        Xprime = X.copy()
        X[0, N - 1] = (1 - pow(z, N, prime)) % prime
        Xprime[0, N - 1] = -N * pow(z, N - 1, prime) % prime
        for j in range(N - 1):
            X[j + 1, j] = 1
        ident = np.eye(N, dtype=np.int64)
        power, derivative = ident.copy(), np.zeros_like(X)
        T, Tprime = ident.copy(), np.zeros_like(X)
        coefficient, logarithmic_derivative = 1, 0
        for j in range(1, N):
            derivative = (mm(prime, derivative, X) + mm(prime, power, Xprime)) % prime
            power = mm(prime, power, X)
            denominator = (pow(Q, j, prime) - z) % prime
            coefficient = coefficient * pow(Q, j - 1, prime) * pow(denominator, -1, prime) % prime
            logarithmic_derivative = (logarithmic_derivative + pow(denominator, -1, prime)) % prime
            T = (T + coefficient * power) % prime
            Tprime = (Tprime + coefficient * (derivative + logarithmic_derivative * power)) % prime
        det = determinant(T, prime)
        direct_D_ratio = 1
        for k in range(1, N):
            ratio = (1 - pow(Q, k, prime) * z) * pow((1 - pow(Q, k, prime)) % prime, -1, prime) % prime
            direct_D_ratio = direct_D_ratio * pow(ratio, k, prime) % prime
        assert pow(z, N * (N - 1) // 2, prime) * pow(det, -1, prime) % prime == direct_D_ratio
        S = sum(pow(z, j, prime) for j in range(N)) % prime
        Sprime = sum(j * pow(z, j - 1, prime) for j in range(1, N)) % prime
        trace = int(np.trace(mm(prime, inverse_mod(T, prime), Tprime))) % prime
        via_matrix = (-trace * pow(N, -1, prime) - Sprime * pow(S, -1, prime)) % prime
        via_connection = (-(N - 1) * pow(2 * z, -1, prime) - Sprime * pow(S, -1, prime)) % prime
        via_connection -= sum(k * pow(Q, k, prime) * pow((1 - pow(Q, k, prime) * z) % prime, -1, prime)
                              for k in range(1, N)) * pow(N, -1, prime)
        assert via_matrix == via_connection % prime
        shifted, power, coefficient = ident.copy(), ident.copy(), 1
        for j in range(1, N):
            coefficient = coefficient * pow(Q, j - 1, prime) * pow((pow(Q, j, prime) - Q * z) % prime, -1, prime) % prime
            power = mm(prime, power, X)
            shifted = (shifted + coefficient * power) % prime
        assert np.array_equal((1 - z) * shifted % prime, pow(Q, -1, prime) * mm(prime, X, T) % prime)
        records.append({"z": z, "independent_matrix_determinant_and_connection": True,
                        "full_discrete_norm_root_transport_exact": True})
        if len(records) == 3:
            break
    assert len(records) == 3
    for M in range(1, 5):
        cap_moment(N, prime, q, M)
    return {"level": N, "prime": prime, "cases": records}


def resonant_flags(N):
    prime, _, q = field(N)
    Q = q * q % prime
    c = [1]
    for s in range(1, N):
        c.append(c[-1] * pow(Q, s - 1, prime) * pow((pow(Q, s, prime) - 1) % prime, -1, prime) % prime)
    p_at_one = factorials(N, Q, 1, prime)
    X = np.zeros((N, N), dtype=np.int64)
    for j in range(N - 1):
        X[j + 1, j] = 1
    powers = [np.eye(N, dtype=np.int64)]
    for j in range(1, N):
        powers.append(mm(prime, powers[-1], X))
    J = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        J[N - 1 - a, a] = pow(Q, a + 1, prime)
    results = []
    for r in range(1, N):
        z, M = pow(Q, r, prime), pow(q, r, prime)
        assert M * M % prime == z
        gamma = pow(M, -(N - 1), prime) * p_at_one[r] * pow(N, -1, prime) % prime
        p_at_z, dp_at_z = factorial_derivatives(N, Q, z, prime)
        actual = [gamma * pow(Q, -j, prime) * p_at_z[N - 1 - j] % prime for j in range(N)]
        expected = [0] * r + [pow(M, -(N + 1), prime) * value % prime for value in c[:N - r]]
        assert actual == expected
        operator = sum((actual[j] * powers[j] for j in range(N)), start=np.zeros_like(X)) % prime
        assert rank_mod(operator, prime) == N - r
        assert np.array_equal(operator[:r], np.zeros((r, N), dtype=np.int64))
        # The first normal derivative induces an isomorphism from kernel
        # to cokernel. Thus every nonunit Smith factor has exponent one.
        Xprime = np.zeros_like(X)
        Xprime[0, N - 1] = 1
        power, power_derivative = powers[0], np.zeros_like(X)
        operator_derivative = np.zeros_like(X)
        for j in range(N):
            coefficient_derivative = gamma * pow(Q, -j, prime) * dp_at_z[N - 1 - j] * (-z) * pow(N, -1, prime) % prime
            operator_derivative = (operator_derivative + coefficient_derivative * power + actual[j] * power_derivative) % prime
            power_derivative = (mm(prime, power_derivative, X) + mm(prime, power, Xprime)) % prime
            power = mm(prime, power, X)
        assert determinant(operator_derivative[:r, N - r:], prime) != 0
        for j in range(N):
            residual = ((pow(Q, j, prime) - z) * actual[j]
                        - pow(Q, j - 1, prime) * actual[(j - 1) % N]) % prime
            assert residual == (-gamma % prime if j == 0 else 0)

        # Use the common local parameter u=1-z^N in the two dual lines.
        # The paired branch is fixed by its proved product, not reset radially.
        paired = pow(M, N - 1, prime) * (1 - z) * pow(N, -1, prime) % prime
        gamma_dual = paired * pow(gamma, -1, prime) % prime
        B, Bd = gamma * J % prime, gamma_dual * J % prime
        x = -M * pow(q, -1, prime) % prime
        _, _, C, _ = dual_data(N, prime, q, x, 0)
        transformed = mm(prime, inverse_mod(Bd, prime).T, C.T, inverse_mod(B, prime))
        predicted = N * pow(Q * pow(M, N - 1, prime) * (1 - z) % prime, -1, prime) * C % prime
        assert np.array_equal(transformed, predicted)
        assert np.array_equal(transformed[N - r:, r:], np.zeros((r, N - r), dtype=np.int64))
        G = cap_moment(N, prime, q, M)
        if N % 2 == 0 and r % 4 == 3:
            assert G == 0
        if N % 2 and r % 2 == 0:
            conjugate = sum(pow(-1, a, prime) * pow(M, a, prime) * pow(q, -(2 * a * a + a), prime)
                            for a in range(N)) % prime
            assert G * conjugate % prime == N % prime
        results.append({"residue": r, "primitive_rank": N - r,
                        "all_nonunit_Smith_exponents_exactly_one": True,
                        "source_support_and_recurrence_exact": True,
                        "actual_cap_regularization_exact": True,
                        "complementary_flags_are_orthogonal": True,
                        "first_normal_cap_moment": int(G)})
    return {"level": N, "prime": prime, "all_nontrivial_deck_lifts": results}


def phase_and_radial_evaluations():
    mp.mp.dps = 90
    phases, deck, radial = [], [], []
    for N in range(2, 25):
        Q = mp.exp(2j * mp.pi / N)
        actual_log = sum(mp.mpf(k) / N * mp.log(1 - Q**k) for k in range(1, N))
        expected_log = mp.log(N) / 2 + 1j * mp.pi * (N - 1) * (N - 2) / (12 * N)
        assert abs(actual_log - expected_log) < mp.mpf('1e-85')
        phases.append(N)
        z = mp.mpc('.35', '.2')
        q = mp.exp(1j * mp.pi / N)
        M = mp.exp(mp.log(z) / 2)
        u = 1 - z**N

        def coefficient_vector(zz, MM):
            log_D = sum(mp.mpf(k) / N * mp.log(1 - Q**k * zz) for k in range(1, N))
            gamma = MM**(-(N - 1)) * mp.exp(log_D - expected_log) / sum(zz**j for j in range(N))
            return [gamma * Q**(-j) * mp.fprod(1 - Q**k * zz for k in range(1, N - j)) for j in range(N)]

        original = coefficient_vector(z, M)
        shifted = coefficient_vector(Q * z, q * M)
        factor = q**(-(N + 1)) * mp.exp(-mp.log(u) / N)
        predicted = [factor * u * original[-1]] + [factor * value for value in original[:-1]]
        assert max(abs(a - b) for a, b in zip(shifted, predicted)) < mp.mpf('1e-83')
        deck.append(N)
        if N not in [3, 6, 10, 12, 18, 24]:
            continue
        for r in sorted({1, N // 2, N - 1}):
            phi = 2 * mp.pi * r / N
            zeta = mp.exp(1j * phi)
            t = 1 - mp.mpf('1e-35')
            z = t * zeta
            log_D = sum(mp.mpf(k) / N * mp.log(1 - Q**k * z) for k in range(1, N))
            gamma = mp.exp(-(N - 1) * (mp.log(t) + 1j * phi) / 2 + log_D - expected_log) * (1 - z) / (1 - z**N)
            regularized = (1 - z**N)**(mp.mpf(r) / N) * gamma
            expected = mp.exp(-1j * phi * (N - 1) / 2) * mp.fprod(1 - Q**j for j in range(1, r + 1)) / N
            relative_error = abs(regularized / expected - 1)
            assert relative_error < mp.mpf('1e-30')
            radial.append({"level": N, "residue": r, "marked_radial_relative_error": float(relative_error)})
    return {"complete_anchor_phase_levels": phases,
            "full_marked_discrete_transport_levels": deck,
            "radial_evaluation_diagnostics": radial}


def norm_error_bound():
    mp.mp.dps = 65
    samples = [mp.mpc('.2', '.3'), mp.mpc('.7', '.4'), mp.mpc('-.65', '.2'),
               mp.mpc('1.4', '.6'), mp.mpc('-.8', '1.1')]
    results = []
    for z in samples:
        radius = abs(z)
        delta = abs(radius - 1)
        second_derivative_bound = 4 * mp.pi**2 * radius / delta**2 + 4 * mp.pi / delta
        if radius < 1:
            G, w = -mp.log(radius) / 2 - mp.im(mp.polylog(2, z)) / (2 * mp.pi), z
        else:
            G, w = -mp.log(radius) + mp.im(mp.polylog(2, 1 / z)) / (2 * mp.pi), 1 / z
        for N in [32, 64, 128, 256]:
            Q = mp.exp(2j * mp.pi / N)
            log_abs_gamma = -(N - 1) * mp.log(radius) / 2 - mp.log(N) / 2
            log_abs_gamma += sum(mp.mpf(N - k) / N * mp.log(abs(z - Q**k)) for k in range(1, N))
            log_abs_gamma -= mp.log(abs((1 - z**N) / (1 - z)))
            prediction = N * G - mp.log(N) / 2 + mp.log(radius) / 2 + mp.log(abs(1 - z)) / 2 - mp.log(abs(1 - w**N))
            error = abs(log_abs_gamma - prediction)
            proved_bound = second_derivative_bound / (12 * N)
            assert error <= proved_bound + mp.mpf('1e-55')
            results.append({"z": [float(z.real), float(z.imag)], "level": N,
                            "error": float(error), "proved_error_bound": float(proved_bound),
                            "observed_rate": float(log_abs_gamma / N), "generating_rate": float(G)})
    return results


def main():
    connection = [matrix_connection(N) for N in range(2, 13)]
    flags = [resonant_flags(N) for N in range(2, 17)]
    phases = phase_and_radial_evaluations()
    norms = norm_error_bound()
    result = {
        "scope": "Local exact cyclic source periods, resonant source flags and actual duality; no selected knot-volume theorem.",
        "independent_matrix_connection_checks": connection,
        "resonant_source_flags_and_caps": flags,
        "complex_mark_and_radial_checks": phases,
        "uniform_error_bound_diagnostics": norms,
    }
    path = Path(__file__).with_name('cyclic_source_resonance_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"result": str(path),
                      "independent_matrix_connections": sum(len(c['cases']) for c in connection),
                      "exact_resonant_flags_and_caps": sum(len(c['all_nontrivial_deck_lifts']) for c in flags),
                      "anchor_phase_levels": len(phases['complete_anchor_phase_levels']),
                      "radial_evaluations": len(phases['radial_evaluation_diagnostics']),
                      "proved_error_bound_samples": len(norms)}, indent=2))


if __name__ == '__main__':
    main()
