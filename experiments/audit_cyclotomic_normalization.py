#!/usr/bin/env python3
"""Independent finite-product diagnostics for the local normalization tower."""

from math import gcd
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def d_product(n, prime, root, x):
    value = 1
    for j in range(1, n):
        value = value*pow((1-pow(root, j, prime)*x) % prime, j, prime) % prime
    return value


def q_product(n, prime, root, x):
    d = d_product(n, prime, root, x)
    return d*d*pow((1-pow(x, n, prime)) % prime, -(n-1), prime) % prime


def field(n):
    prime = next(4*n*k+1 for k in range(1, 1000) if sp.isprime(4*n*k+1))
    x = int(sp.primitive_root(prime))
    root = pow(x, (prime-1)//n, prime)
    return prime, root, x


def exact_level(n):
    prime, root, x = field(n)
    d = d_product(n, prime, root, x)
    q = q_product(n, prime, root, x)
    assert d_product(n, prime, root, root*x % prime)*pow(d, -1, prime) % prime == (
        pow(1-x, n, prime)*pow(1-pow(x, n, prime), -1, prime) % prime)
    inverse = pow(x, -1, prime)
    s = n*(n-1)//2
    t = n*(n-1)*(2*n-1)//6
    expected_d = (pow(-1, s, prime)*pow(root, t, prime)*pow(x, -s, prime)
                  *pow((1-pow(x, n, prime))*pow(1-x, -1, prime) % prime, n, prime)) % prime
    assert d*d_product(n, prime, root, inverse) % prime == expected_d
    expected_q = (pow(-1, n-1, prime)*pow(root, 2*t, prime)
                  *pow(1-pow(x, n, prime), 2, prime)*pow(1-x, -2*n, prime)) % prime
    assert q*q_product(n, prime, root, inverse) % prime == expected_q
    certificates = 0
    for a in range(1, n):
        if gcd(a, n) != 1:
            continue
        ai = pow(a, -1, n)
        b = 1
        for k in range(1, n):
            numerator = a*(ai*k % n)-k
            assert numerator % n == 0
            b = b*pow((1-pow(root, k, prime)*x) % prime, numerator//n, prime) % prime
        da = d_product(n, prime, pow(root, a, prime), x)
        qa = q_product(n, prime, pow(root, a, prime), x)
        assert pow(da, a, prime)*pow(d, -1, prime) % prime == pow(b, n, prime)
        assert pow(qa, a, prime)*pow(q, -1, prime) % prime == (
            pow(b, 2*n, prime)*pow(1-pow(x, n, prime), -(a-1)*(n-1), prime) % prime)
        certificates += 1
    return {"level": n, "finite_field_prime": prime, "shift_exact": True,
            "both_inversion_identities_exact": True, "galois_certificates": certificates}


def exact_distribution(m, n):
    level = m*n
    prime, root, x = field(level)
    dm = d_product(m, prime, pow(root, n, prime), pow(x, n, prime))
    qm = q_product(m, prime, pow(root, n, prime), pow(x, n, prime))
    for b in range(m):
        z = pow(root, b, prime)*x % prime
        dm = dm*pow(d_product(n, prime, pow(root, m, prime), z), m, prime) % prime
        qm = qm*pow(q_product(n, prime, pow(root, m, prime), z), m, prime) % prime
    assert dm == d_product(level, prime, root, x)
    assert qm == q_product(level, prime, root, x)
    return {"factors": [m, n], "finite_field_prime": prime,
            "D_and_Q_distribution_exact": True}


def log_frame(n, x):
    if n == 1:
        return mp.mpc(0)
    root = mp.exp(2j*mp.pi/n)
    return (mp.fsum(j*mp.log(1-root**j*x) for j in range(1, n))/n
            -mp.mpf(n-1)/(2*n)*mp.log(1-x**n))


def numerical_diagnostics():
    mp.mp.dps = 70
    points = [mp.mpc("0.3", "0.4"), mp.mpc("0.8", "0.1"), mp.mpc("-0.2", "0.7")]
    distributions = []
    for m, n in ((2, 3), (3, 3), (3, 5), (4, 5), (5, 7)):
        x = points[1]
        root = mp.exp(2j*mp.pi/(m*n))
        rhs = log_frame(m, x**n)/n+mp.fsum(log_frame(n, root**b*x) for b in range(m))
        error = abs(log_frame(m*n, x)-rhs)
        assert error < mp.mpf("1e-60")
        distributions.append({"factors": [m, n], "pointed_log_error": float(error)})
    series = []
    for n in (7, 10, 15):
        x = points[1]
        root = mp.exp(2j*mp.pi/n)
        value = mp.fsum(x**k/(k*(1-root**k)) for k in range(1, 801) if k % n)
        error = abs(log_frame(n, x)-value)
        assert error < mp.mpf("1e-60")
        series.append({"level": n, "series_error": float(error)})
    estimates = []
    levels = (31, 32, 63, 64, 127, 128, 255, 256, 511, 512)
    for x in points:
        r = abs(x)
        regulator = mp.im(mp.polylog(2, x))+mp.log(r)*mp.arg(1-x)
        target = -1j*mp.pi*x/(6*(1-x))
        final_error = None
        for n in levels:
            value = log_frame(n, x)
            residual = value+n*mp.polylog(2, x)/(2j*mp.pi)+mp.log(1-x)/2
            bound = mp.pi*r/(4*n*(1-r))+2*r**(n//2+1)/(1-r)
            assert abs(residual) <= bound
            log_norm = -mp.re(value)+n*mp.log(r)*mp.arg(1-x)/(2*mp.pi)
            corrected_norm_error = (2*mp.pi*log_norm/n-regulator
                                    -mp.pi*mp.log(abs(1-x))/n)
            assert abs(corrected_norm_error+2*mp.pi*mp.re(residual)/n) < mp.mpf("1e-60")
            final_error = abs(n*residual-target)
            if n in (31, 32, 511, 512):
                estimates.append({"point": str(x), "level": n,
                                  "logarithm_error": float(abs(residual)),
                                  "proven_error_bound": float(bound),
                                  "corrected_regulator_error": float(corrected_norm_error),
                                  "next_coefficient_error": float(final_error)})
        assert final_error < mp.mpf("0.001")
    return {"precision_digits": mp.mp.dps, "pointed_distribution": distributions,
            "exact_series_diagnostics": series, "local_estimates": estimates}


def main():
    results = {"scope": "Local normalization identities and regulator diagnostics; no global knot comparison.",
               "exact_levels": [exact_level(n) for n in (2, 3, 4, 5, 6, 8, 9, 10, 15, 25, 35)],
               "exact_distributions": [exact_distribution(m, n) for m, n in
                                       ((2, 3), (3, 3), (3, 5), (4, 5), (5, 7),
                                        (3, 9), (5, 5), (2, 9))],
               "numerical": numerical_diagnostics()}
    Path(__file__).with_name("cyclotomic_normalization_results.json").write_text(
        json.dumps(results, indent=2)+"\n")
    print(json.dumps(results), flush=True)


if __name__ == "__main__":
    main()
