#!/usr/bin/env python3
"""Check the original three-crossing recurrence, forcing and factorial profile.

The literal matrix column is computed independently of the scalar recurrence.
Finite profile and endpoint errors are recorded as diagnostics, not used as
proofs of convergence or of an asymptotic error bound.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_even_reflected_casimir_insertions import (
    apply_power, casimir, norm, original_crossing, relative,
)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for level in (12, 13, 24, 25, 48, 49, 96, 97, 144, 145):
        q = mp.exp(mp.pi*1j/level)
        Q = q*q
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        matrix = original_crossing(level)
        first = [mp.mpc(1)]+[mp.mpc(0)]*(level-1)
        alpha = apply_power(matrix, first, 3)
        alpha_one = apply_power(matrix, first, 1)
        beta = [x/kappa**3 for x in alpha]
        sine_squares = [4*mp.sin(mp.pi*j/level)**2 for j in range(level)]
        nodes = [2*mp.cos((2*j+1)*mp.pi/level) for j in range(level)]
        factorial_squares = [mp.mpf(1)]
        for j in range(1, level):
            factorial_squares.append(factorial_squares[-1]*sine_squares[j])
        h = [q**(j*(j+2))*factorial_squares[j] for j in range(level)]
        partial = []
        value = mp.mpc(0)
        maximum = mp.mpf(0)
        for j in range(level):
            value += (-1)**j*q**(-j*(j-1))/factorial_squares[j]
            partial.append(value)
            maximum = max(maximum, relative(beta[j], h[j]*value))
            if j:
                right = q**(2*j+1)*sine_squares[j]*beta[j-1]+(-1)**j*q**(3*j)
                maximum = max(maximum, relative(beta[j], right))
        ca = casimir(alpha, nodes, sine_squares)
        ch = casimir(h, nodes, sine_squares)
        for j in range(level):
            maximum = max(
                maximum,
                relative(ca[j]-q*Q**j*alpha[j], kappa**2/q*alpha_one[j]),
                relative(ch[j]-q*Q**j*h[j], 1/q if j == 0 else 0),
                relative(factorial_squares[j]*factorial_squares[level-1-j], level**2),
            )
        for j in range(level):
            absolute_tail = mp.fsum(1/factorial_squares[l] for l in range(j+1, level))
            reflected_tail = mp.fsum(factorial_squares[m]
                                     for m in range(level-j-2+1))/level**2
            maximum = max(maximum, relative(absolute_tail, reflected_tail))
            assert abs(partial[-1]-partial[j]) <= absolute_tail+tolerance
        assert maximum < tolerance, (level, maximum)

        omega = mp.exp(1j*mp.pi*(mp.mpf(1)/4+mp.mpf(1)/(4*level)-mp.mpf(level)/12))
        main = [omega*x/mp.sqrt(level) for x in h]
        first_high = (7*level+11)//12
        upper_error = max(abs(beta[j]/main[j]-1) for j in range(first_high, level))
        band = [j for j in range(level) if mp.mpf(2)/3 <= mp.mpf(j)/level <= mp.mpf(11)/12]
        center = min(band, key=lambda j: abs(mp.mpf(j)/level-mp.mpf(5)/6))
        flat_error = max(abs(partial[j]/partial[center]-1) for j in band)
        error_norm = norm([x-y for x, y in zip(beta, main)])/norm(main)
        energy_ratio = mp.fsum(abs(x)**2 for x in beta)/(mp.fsum(x*x for x in factorial_squares)/level)
        records.append({
            "N": level, "coefficient_checks": level,
            "maximum_relative_identity_error": mp.nstr(maximum, 25),
            "normalized_endpoint_difference_diagnostic": {
                "real": mp.nstr(mp.re(mp.sqrt(level)*partial[-1]/omega-1), 25),
                "imag": mp.nstr(mp.im(mp.sqrt(level)*partial[-1]/omega-1), 25),
            },
            "upper_interval": "j/N >= 7/12",
            "upper_relative_profile_error_diagnostic": mp.nstr(upper_error, 25),
            "full_relative_vector_error_diagnostic": mp.nstr(error_norm, 25),
            "constant_partial_sum_band": "2/3 <= j/N <= 11/12",
            "band_relative_partial_sum_error_diagnostic": mp.nstr(flat_error, 25),
            "reflected_energy_ratio_diagnostic": mp.nstr(energy_ratio, 25),
        })
        print(f"Checked original three-crossing column at N={level}.", flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=140)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.precision < 120:
        parser.error("Use at least 120 decimal digits for these cancellation-sensitive checks.")
    records = run(args.precision)
    source = Path(__file__).resolve()
    dependency = source.with_name("check_even_reflected_casimir_insertions.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "dependency_sha256": {"experiments/"+dependency.name:
                              hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "scope": "Exact literal matrix, first-order recurrence, reciprocal "
                 "forcing, Casimir forcing and factorial reflection identities. "
                 "All finite asymptotic errors are diagnostics only.",
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "levels": len(records),
        "coefficient_checks": sum(r["coefficient_checks"] for r in records),
        "maximum_relative_identity_error": max(
            (r["maximum_relative_identity_error"] for r in records), key=mp.mpf),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
