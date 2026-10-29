#!/usr/bin/env python3
"""Local exact and numerical checks for the triangulation bridge.

No global quantum state comparison is assumed. Matrix checks retain
the half-root parity convention and the cyclic dilogarithm's full
norm denominator. Numerical checks distinguish fixed centers from
fixed small coordinates; they are not knot-volume tests.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import cyclic_matrices, power, rank


def field(n):
    prime = next(2*n*k+1 for k in range(2, 1000) if sp.isprime(2*n*k+1))
    generator = int(sp.primitive_root(prime))
    half = pow(generator, (prime-1)//(2*n), prime)
    omega = half*half % prime
    chosen_half = -half % prime if n % 2 else half
    assert pow(chosen_half, 2, prime) == omega
    assert pow(chosen_half, n, prime) == pow(-1, n-1, prime)
    return prime, generator, omega, half, chosen_half


def signed_power(matrix, exponent, center, prime):
    if exponent >= 0:
        return power(matrix, exponent, prime)
    inverse = power(matrix, len(matrix)-1, prime)*pow(center, -1, prime) % prime
    return power(inverse, -exponent, prime)


def exact_local_check(n):
    prime, generator, omega, raw_half, half = field(n)
    shape = 2
    X, Y, _, _ = cyclic_matrices(n, prime, omega, shape)
    eye = np.eye(n, dtype=np.int64)
    assert not np.any((X@Y-omega*Y@X) % prime)
    assert np.array_equal(power(X, n, prime), shape*eye % prime)
    assert np.array_equal(power(Y, n, prime), (1-shape)*eye % prime)
    assert np.array_equal(power((X+Y) % prime, n, prime), eye)
    vacuum = np.zeros(n, dtype=np.int64)
    vacuum[0] = 1
    assert not np.any(((X+Y-eye) % prime)@vacuum % prime)
    assert rank((X+Y-eye) % prime, prime) == n-1
    for a in range(-2, 3):
        for b in range(-2, 3):
            W = pow(half, -a*b, prime)*signed_power(X, a, shape, prime) % prime
            W = W@signed_power(Y, b, 1-shape, prime) % prime
            expected = pow(shape, a, prime)*pow(1-shape, b, prime) % prime
            assert np.array_equal(power(W, n, prime), expected*eye % prime)

    wrong_phase_observed = None
    if n % 2:
        raw = pow(raw_half, -1, prime)*X@Y % prime
        actual = power(raw, n, prime)
        expected = shape*(1-shape)*eye % prime
        assert np.array_equal(actual, -expected % prime)
        wrong_phase_observed = True

    x = generator

    def cyclic_power(point):
        value = 1
        for k in range(1, n):
            value = value*pow((1-pow(omega, k, prime)*point) % prime, k, prime) % prime
        return value

    actual_ratio = cyclic_power(omega*x % prime)*pow(cyclic_power(x), -1, prime) % prime
    expected_ratio = pow(1-x, n, prime)*pow(1-pow(x, n, prime), -1, prime) % prime
    assert actual_ratio == expected_ratio

    commuting = False
    if n <= 6:
        X2, Y2, _, _ = cyclic_matrices(n, prime, omega, 3)
        Y2_inverse = power(Y2, n-1, prime)*pow(1-3, -1, prime) % prime
        first = np.kron(X, X2) % prime
        second = np.kron(Y, Y2_inverse) % prime
        assert not np.any((first@second-second@first) % prime)
        big_eye = np.eye(n*n, dtype=np.int64)
        assert np.array_equal(power(first, n, prime), 6*big_eye % prime)
        expected = (1-shape)*pow(1-3, -1, prime) % prime
        assert np.array_equal(power(second, n, prime), expected*big_eye % prime)
        commuting = True
    return {"root_order": n, "finite_field_prime": prime,
            "tetrahedron_Frobenius_and_vacuum_exact": True,
            "Weyl_monomial_power_checks": 25,
            "unadapted_half_root_changes_odd_center": wrong_phase_observed,
            "cyclic_dilog_norm_ratio_exact": True,
            "two_tetrahedron_isotropic_monomials_checked": commuting}


def log_modulus_cyclic_dilog(n, x):
    return mp.fsum(mp.mpf(k)/n*mp.log(abs(1-mp.exp(2*mp.pi*mp.j*k/n)*x))
                   for k in range(1, n))


def numerical_regime_checks():
    mp.mp.dps = 75
    levels = (16, 32, 64, 128, 256, 512)
    real_shapes = []
    for z in (mp.mpf(2), mp.mpf(1)/3):
        for n in (7, 8, 12, 16, 32):
            x = mp.exp(mp.log(z)/n)
            value = 2*log_modulus_cyclic_dilog(n, x)
            exact = mp.log(abs((1-z)/(1-x)))
            assert abs(value-exact) < mp.mpf("1e-60")
            real_shapes.append({"root_order": n, "center": str(z),
                                "exact_modulus_identity_verified_numerically": True})

    geometric_shape = mp.exp(mp.j*mp.pi/3)
    w = mp.log(geometric_shape)
    fixed_center = []
    for n in levels:
        value = log_modulus_cyclic_dilog(n, mp.exp(w/n))
        fixed_center.append({"root_order": n,
                             "log_modulus": mp.nstr(value, 30),
                             "log_modulus_over_n": mp.nstr(value/n, 30),
                             "log_modulus_over_log_n": mp.nstr(value/mp.log(n), 30)})

    x = mp.mpc("0.3", "0.4")
    radius = abs(x)
    target = -mp.im(mp.polylog(2, x))/(2*mp.pi)
    lipschitz = -mp.log(1-radius)+2*mp.pi*radius/(1-radius)
    fixed_small_coordinate = []
    for n in levels:
        value = log_modulus_cyclic_dilog(n, x)/n
        error = abs(value-target)
        assert error <= lipschitz/n
        fixed_small_coordinate.append({"root_order": n,
                                        "log_modulus_over_n": mp.nstr(value, 30),
                                        "target": mp.nstr(target, 30),
                                        "error": mp.nstr(error, 15),
                                        "proved_Riemann_error_bound_passes": True})
    return {"scope": "Numerical local checks; no global knot-period comparison.",
            "positive_real_center_exact_identity": real_shapes,
            "fixed_geometric_center": fixed_center,
            "fixed_small_coordinate": fixed_small_coordinate}


def main():
    results = {"scope": "Local central algebra and cyclic-dilog regimes, not a volume proof.",
               "exact_root_checks": [exact_local_check(n) for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)],
               "numerical_regimes": numerical_regime_checks()}
    path = Path(__file__).with_name("triangulation_regulator_bridge_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"exact_root_orders": len(results["exact_root_checks"]),
                      "Weyl_power_checks": 250,
                      "central_and_semiclassical_regimes": "checked",
                      "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
