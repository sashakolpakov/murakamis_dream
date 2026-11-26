#!/usr/bin/env python3
"""Check the Newton index interpolation against the original polynomial jets.

These finite high-precision checks supplement the written proof. They
compare a direct Gamma-product continuation (via its exact cyclic formula)
with ordinary polynomial values and derivatives, and check both original
turn and identity pairings. They are not an asymptotic certificate.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def log_factorial(n, z):
    if mp.im(z) > 0:
        return mp.conj(log_factorial(n, mp.conj(z)))
    if mp.im(z) == 0:
        raise ValueError("This diagnostic uses nonreal factorial arguments")
    x = z / n
    w = mp.exp(-2j * mp.pi * x)
    root = mp.exp(2j * mp.pi / n)
    c = mp.log(n) / 2 + 1j * mp.pi * (
        mp.mpf(n) / 12 - mp.mpf(1) / 4 + mp.mpf(1) / (12 * n)
    )
    correction = x * mp.log(1 - w**n)
    correction -= mp.fsum(k * mp.log(1 - w * root**k) for k in range(n)) / n
    correction += 1j * mp.polylog(2, w**n) / (2 * mp.pi * n)
    return 1j * mp.pi * n * x*x / 2 - 1j * mp.pi * (n-1) * x / 2 + c + correction


def gamma_basis(n, x, angle):
    middle = mp.mpf(n-1) / 2 - n*x
    shift = n * angle / (2 * mp.pi)
    return n * mp.exp(-log_factorial(n, middle+shift)
                      -log_factorial(n, middle-shift)
                      -2*log_factorial(n, n*x))


def original_polynomial_jets(n, z):
    value, derivative = mp.mpc(1), mp.mpc(0)
    result = [(value, derivative)]
    for k in range(n-1):
        root = 2 * mp.cos((2*k+1) * mp.pi / n)
        denominator = (2*mp.sin((k+1) * mp.pi / n))**2
        value, derivative = (value*(root-z)/denominator,
                             (derivative*(root-z)-value)/denominator)
        result.append((value, derivative))
    return result


def cardinal(n, x):
    return mp.sin(mp.pi*n*x)/(n*mp.sin(mp.pi*x))


def fourier_coefficients(n, values):
    return [mp.fsum(values[i]*mp.exp(-2j*mp.pi*(mp.mpf(k)-(n-1)/2)*i/n)
                    for i in range(n))/n for k in range(n)]


def run(dps, maximum_level):
    mp.mp.dps = dps
    tolerance = mp.mpf(10)**(-dps+25)
    maximum = mp.mpf(0)
    counts = {"spectral_values": 0, "first_normals": 0,
              "explicit_sine_values": 0, "explicit_cotangent_normals": 0,
              "turn_pairings": 0, "identity_pairings": 0}

    def check(kind, left, right):
        nonlocal maximum
        error = abs(left-right)/(1+abs(right))
        maximum = max(maximum, error)
        if not error < tolerance:
            raise AssertionError(f"{kind}: error {error} exceeds {tolerance}")
        counts[kind] += 1

    points = [mp.mpc("0.17", "0.11"), mp.mpc("0.4", "-0.23"),
              mp.mpc("-0.13", "0.07")]
    for n in range(2, maximum_level+1):
        degree = n-1
        for j in range(degree//2+1):
            angle = mp.pi-(2*j+1)*mp.pi/n
            z = 2*mp.cos((2*j+1)*mp.pi/n)
            jets = original_polynomial_jets(n, z)
            for x in points:
                weights = [cardinal(n, x-mp.mpf(i)/n) for i in range(n)]
                value = mp.fsum(weight*pair[0] for weight, pair in zip(weights, jets))
                check("spectral_values", gamma_basis(n, x, angle), value)
                sine_value = mp.mpf((-1)**(degree+j))/n
                sine_value *= mp.fprod(2*mp.sin(mp.pi*(x+mp.mpf(k)/n))
                                      for k in range(1, j+1))
                sine_value *= mp.fprod(2*mp.sin(mp.pi*(x-mp.mpf(k)/n))
                                      for k in range(j+1, degree+1))
                check("explicit_sine_values", sine_value, value)
                if 2*j == degree:
                    continue  # The odd endpoint is simple; no extra normal is prescribed.
                normal = mp.fsum(weight*pair[1] for weight, pair in zip(weights, jets))
                angular = mp.diff(lambda t: gamma_basis(n, x, t), angle)
                check("first_normals", angular/(2*mp.sin(angle)), normal)
                explicit_angular = -sine_value * mp.fsum(
                    mp.cot(mp.pi*(mp.mpf(k)/n-x))
                    for k in range(j+1, degree-j+1))/2
                check("explicit_cotangent_normals", explicit_angular/(2*mp.sin(angle)), normal)

        left = [pair[0] for pair in original_polynomial_jets(n, mp.mpc("0.31", "0.19"))]
        right = [pair[0] for pair in original_polynomial_jets(n, mp.mpc("-0.27", "0.13"))]
        left_fourier = fourier_coefficients(n, left)
        right_fourier = fourier_coefficients(n, right)
        turn_constant = mp.fsum(left_fourier[k]*right_fourier[degree-k] for k in range(n))
        check("turn_pairings", n*turn_constant, mp.fsum(a*b for a,b in zip(left,right)))
        identity_constant = mp.fsum(
            left_fourier[k]*right_fourier[k]
            *mp.exp(2j*mp.pi*(mp.mpf(k)-mp.mpf(degree)/2)*degree/n)
            for k in range(n))
        check("identity_pairings", n*identity_constant,
              mp.fsum(left[i]*right[degree-i] for i in range(n)))

    return {"scope": "Finite normalized factorial values and full Hermite jets; exact paired-index Fourier identities",
            "decimal_precision": dps, "levels": [2, maximum_level],
            "counts": counts, "maximum_relative_residual": str(maximum),
            "acceptance_tolerance": str(tolerance),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--maximum-level", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.dps, args.maximum_level)
    encoded = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
