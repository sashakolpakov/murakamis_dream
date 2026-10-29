#!/usr/bin/env python3
"""Exact-source and high-precision checks of the whole Ward atom.

Analytic proofs, domains and marks are in the accompanying note.  Fixed-root
normal limits below keep the root order fixed; they are not uniform-in-level
asymptotics or a selected knot-period comparison.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


mp.mp.dps = 80
TWO_PI_I = 2j * mp.pi
SERIES_TOL = mp.mpf("1e-65")


def log_f(q, z):
    """Convergent logarithm of 1/(z;q)_infinity, marked at z=0."""
    assert abs(q) < 1 and abs(z) < 1
    if not z:
        return mp.mpc(0)
    # The extra denominator margin makes the omitted tail negligible even
    # at the small radial normal parameters used in these tests.
    cutoff = int(mp.ceil(mp.log(SERIES_TOL * (1 - abs(q)) *
                                (1 - abs(z))) / mp.log(abs(z)))) + 8
    zp, qp, result = mp.mpc(1), mp.mpc(1), mp.mpc(0)
    for m in range(1, max(1, cutoff) + 1):
        zp *= z
        qp *= q
        result += zp / (m * (1 - qp))
    return result


def log_d(n, z):
    zeta = mp.exp(TWO_PI_I / n)
    return sum((mp.mpf(j) / n * mp.log(1 - zeta**j * z)
                for j in range(1, n)), mp.mpc(0))


def log_psi(h, x):
    q = mp.exp(h)
    qt = mp.exp(4 * mp.pi**2 / h)
    z = mp.exp(x)
    w = qt * mp.exp(TWO_PI_I * x / h)
    assert abs(w) < 1
    return log_f(q, z) - log_f(qt, w)


def log_root_psi(n, x):
    z = mp.exp(x)
    central = z**n
    return (log_d(n, z) + mp.polylog(2, central) / (TWO_PI_I * n)
            + (x / TWO_PI_I - 1) * mp.log(1 - central))


def root_expansions():
    records = []
    for n in range(2, 9):
        for z in (mp.mpf("0.2"), mp.mpf("0.65"),
                  mp.mpc("0.3", "0.2")):
            constant = log_d(n, z) - mp.log(1 - z**n) / 2
            errors = []
            for radius in (mp.mpf("1e-3"), mp.mpf("1e-5")):
                epsilon = -radius
                actual = log_f(mp.exp(TWO_PI_I / n + epsilon), z)
                polar = -mp.polylog(2, z**n) / (n*n*epsilon)
                error = abs(actual - polar - constant)
                assert error < 20 * radius
                errors.append(error)
            assert errors[1] < errors[0] / 50
            records.append({"level": n, "z": str(z),
                            "small_normal_error": float(errors[1]),
                            "error_ratio": float(errors[0] / errors[1])})
    # A nonzero resonant polar coefficient is checked independently of D_n.
    for n in (2, 3, 5, 8):
        z = mp.mpf("0.7")
        radius = mp.mpf("1e-6")
        value = radius * mp.re(log_f(mp.exp(TWO_PI_I / n-radius), z))
        expected = mp.polylog(2, z**n) / (n*n)
        assert abs(value-expected) < 2*radius
    return records


def exceptional_slope():
    records = []
    slopes = (mp.mpf("0.5"), mp.mpf(2)/3, mp.mpf(1),
              mp.mpf("1.5"), mp.mpf("-0.5"), mp.mpc("0.3", "0.2"))
    for n in (2, 3, 5, 8):
        z = mp.mpc("0.4", "0.1")
        for slope in slopes:
            errors = []
            for radius in (mp.mpf("1e-3"), mp.mpf("1e-5")):
                epsilon = -radius
                q = mp.exp(TWO_PI_I/n + epsilon)
                u = mp.exp(slope*n*epsilon)
                actual = log_f(q, z*u) - log_f(q, z)
                expected = slope*mp.log(1-z**n)
                errors.append(abs(actual-expected))
            assert errors[1] < 40*mp.mpf("1e-5")
            assert errors[1] < errors[0]/45
            records.append({"level": n, "slope": str(slope),
                            "small_normal_error": float(errors[1])})

    # Telescope at rational slopes.  It is a PRODUCT at differing zU^j,
    # never the false equality R(z,U)^b = a finite product off the root.
    telescopes = []
    for n in (2, 3, 5):
        q = mp.exp(TWO_PI_I/n-mp.mpf("0.012"))
        z = mp.mpc("0.31", "0.08")
        for numerator, denominator in ((1, 2), (2, 3), (-1, 2)):
            epsilon = -mp.mpf("0.012")
            u = mp.exp(mp.mpf(numerator)*n*epsilon/denominator)
            norm_log = sum((log_f(q, z*u**(j+1))-
                            log_f(q, z*u**j)
                            for j in range(denominator)), mp.mpc(0))
            length = numerator*n
            if length >= 0:
                finite_log = sum((mp.log(1-z*q**j)
                                  for j in range(length)), mp.mpc(0))
            else:
                finite_log = -sum((mp.log(1-z*q**j)
                                   for j in range(length, 0)), mp.mpc(0))
            assert abs(norm_log-finite_log) < mp.mpf("1e-60")
            telescopes.append({"level": n, "numerator": numerator,
                               "denominator": denominator,
                               "exact_product_error": float(abs(norm_log-finite_log))})
    return records, telescopes


def two_nome_transports():
    records = []
    for h in (mp.mpc("-0.3", "1.1"), mp.mpc("-0.2", "2.0")):
        for x in (mp.mpf("-0.8"), mp.mpf("-1.3")):
            z = mp.exp(x)
            y = mp.exp(TWO_PI_I*x/h)
            base = log_psi(h, x)
            first = mp.exp(log_psi(h, x+h)-base)
            second = mp.exp(log_psi(h, x+TWO_PI_I)-base)
            assert abs(first-(1-z)) < mp.mpf("1e-58")
            assert abs(second-(1-y)) < mp.mpf("1e-58")
            records.append({"H": str(h), "x": str(x),
                            "first_transport_error": float(abs(first-(1-z))),
                            "second_transport_error": float(abs(second-(1-y)))})
    return records


def root_constant_and_source():
    records = []
    for n in range(2, 9):
        for z in (mp.mpf("0.3"), mp.mpc("0.45", "0.1")):
            x = mp.log(z)
            expected = log_root_psi(n, x)
            errors = []
            for radius in (mp.mpf("1e-3"), mp.mpf("1e-5")):
                h = TWO_PI_I/n-radius
                actual = log_psi(h, x)
                errors.append(abs(actual-expected))
            assert errors[1] < 30*mp.mpf("1e-5")
            assert errors[1] < errors[0]/45
            # Independently reconstruct the full norm-root/regulator factor.
            central = z**n
            v = mp.log(1-central)
            log_g = log_d(n, z)-mp.mpf(n-1)/(2*n)*v
            s_period = mp.polylog(2, central)+n*x*v
            rebuilt = log_g+s_period/(TWO_PI_I*n)-mp.mpf(n+1)/(2*n)*v
            assert abs(expected-rebuilt) < mp.mpf("1e-65")
            # The marked x translations, including the second norm law.
            first = mp.exp(log_root_psi(n, x+TWO_PI_I/n)-expected)
            second = mp.exp(log_root_psi(n, x+TWO_PI_I)-expected)
            assert abs(first-(1-z)) < mp.mpf("1e-60")
            assert abs(second-(1-central)) < mp.mpf("1e-60")
            records.append({"level": n, "z": str(z),
                            "small_normal_error": float(errors[1]),
                            "error_ratio": float(errors[0]/errors[1]),
                            "retained_norm_regulator_reconstruction": True,
                            "two_marked_root_transports": True})
    return records


def finite_affine_source():
    records = []
    for n in range(2, 14):
        multiplier = max(2, 3000//n)
        while not sp.isprime(n*multiplier+1):
            multiplier += 1
        prime = int(n*multiplier+1)
        generator = int(sp.primitive_root(prime))
        zeta = pow(generator, (prime-1)//n, prime)
        coefficients = [1]
        for j in range(1, n):
            coefficients.append(coefficients[-1]*
                                pow((1-pow(zeta,j,prime)) % prime,-1,prime) % prime)
        residual = []
        for j in range(n+1):
            current = coefficients[j] if j < n else 0
            previous = coefficients[j-1] if j > 0 else 0
            residual.append((current*(pow(zeta,j,prime)-1)+previous) % prime)
        assert residual == [0]*n+[pow(n,-1,prime)]
        records.append({"level": n, "finite_field_prime": prime,
                        "all_coefficients_checked": n+1,
                        "literal_affine_source": "z^N/N"})
    return records


def exact_accumulating_zeros():
    records = []
    x = mp.mpf("-0.7")
    z = mp.exp(x)
    for k in (2, 3, 5, 8, 13, 21):
        h = (x-TWO_PI_I)/k
        q, qt = mp.exp(h), mp.exp(4*mp.pi**2/h)
        w = qt*mp.exp(TWO_PI_I*x/h)
        assert abs(w-1) < mp.mpf("1e-70")
        # Derivative of (1-w) times the nonvanishing remaining numerator.
        wprime = -(4*mp.pi**2+TWO_PI_I*x)/h**2
        log_nonzero_remainder = -log_f(qt, qt)+log_f(q, z)
        derivative = -wprime*mp.exp(log_nonzero_remainder)
        assert abs(derivative) > 0
        assert abs(q) < 1 and abs(qt) < 1 and abs(z) < 1
        records.append({"k": k, "H_modulus": float(abs(h)),
                        "w_minus_one": float(abs(w-1)),
                        "simple_zero_derivative_modulus": float(abs(derivative))})
    assert records[-1]["H_modulus"] < records[0]["H_modulus"]
    return records


def physical_root_sequence():
    records = []
    for z in (mp.mpf("0.3"), mp.mpc("0.5", "0.2"),
              mp.mpc("-0.55", "0.1")):
        x = mp.log(z)
        radius = abs(z)
        derivative_bound = (4*mp.pi*radius/(1-radius)+
                            4*mp.pi**2*radius/(1-radius)**2)
        for n in (16, 32, 64, 128):
            expected = -mp.polylog(2,z)/(TWO_PI_I/n)-mp.log(1-z)/2
            central = z**n
            # Exact source correction to log D_n in the completed root value.
            source_correction = (mp.polylog(2,central)/(TWO_PI_I*n)+
                                 (x/TWO_PI_I-1)*mp.log(1-central))
            bound = derivative_bound/(12*n)+abs(source_correction)
            error = abs(log_root_psi(n,x)-expected)
            assert error <= bound
            records.append({"level": n, "z": str(z),
                            "logarithmic_error": float(error),
                            "proved_trapezoid_plus_source_bound": float(bound)})
    return records


def symbolic_root_normal_identities():
    eps, n, x = sp.symbols("epsilon n x", nonzero=True)
    h0 = 2*sp.pi*sp.I/n
    dual_log = 4*sp.pi**2/(h0+eps)+2*sp.pi*sp.I*n
    assert sp.cancel(1/dual_log-1/(n*n*eps)-1/(2*sp.pi*sp.I*n)) == 0
    gamma = 1-x/(2*sp.pi*sp.I)
    log_w = (4*sp.pi**2+2*sp.pi*sp.I*x)/(h0+eps)
    assert sp.cancel(log_w-n*x-gamma*dual_log+2*sp.pi*sp.I*n) == 0
    return {"exact_dual_inverse_normal": True,
            "exact_dual_argument_with_integer_log_mark": True}


def main():
    slope, telescopes = exceptional_slope()
    result = {
        "symbolic_root_normal_identities": symbolic_root_normal_identities(),
        "original_fixed_root_expansions": root_expansions(),
        "exceptional_slope_limits": slope,
        "rational_slope_exact_telescopes": telescopes,
        "two_nome_exact_transports": two_nome_transports(),
        "physical_root_constants_and_full_source": root_constant_and_source(),
        "literal_finite_affine_sources": finite_affine_source(),
        "exact_accumulating_simple_zeros": exact_accumulating_zeros(),
        "physical_root_sequence_bounds": physical_root_sequence(),
        "scope": "Actual local Ward atom, whole exceptional normal source and "
                 "two-nome root period. No replacement of the selected knot "
                 "source, whole-word cancellation or volume conjecture is inferred."
    }
    output = Path(__file__).with_name("unfolded_atom_two_nome_source_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "precision_digits": mp.mp.dps,
                      "counts": {key: len(value) for key,value in result.items()
                                 if isinstance(value,list)},
                      "symbolic": result["symbolic_root_normal_identities"],
                      "output": str(output)},indent=2))


if __name__ == "__main__":
    main()
