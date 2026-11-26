#!/usr/bin/env python3
"""Check the middle Newton Fourier identity against the defining product.

These finite diagnostics include every physical value and first normal at
levels 2--18. The uniform bounds are proved in the accompanying research note.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    mp.mp.dps = 100
    checks = 0
    maximum_error = mp.mpf(0)

    def close(left, right):
        nonlocal checks, maximum_error
        error = abs(left-right) / max(1, abs(left), abs(right))
        assert error < mp.mpf("1e-80"), (left, right, error)
        maximum_error = max(maximum_error, error)
        checks += 1

    for N in range(2, 19):
        L = N-1-N//2
        theta = mp.pi/N
        nodes = [2*mp.cos((2*j+1)*theta) for j in range(N)]
        denominator = mp.fprod((2*mp.sin(j*theta))**2 for j in range(1, L+1))

        def original(z):
            factors = [nodes[j]-z for j in range(L)]
            value = mp.fprod(factors)/denominator
            derivative = -sum((mp.fprod(factors[:j]+factors[j+1:])
                               for j in range(L)), mp.mpf(0))/denominator
            return value, derivative

        coefficients = [
            mp.mpf(1)/N if N % 2 else 4*mp.cos(k*theta)/(N*2*mp.sin(theta))
            for k in range(L+1)]

        def fourier_as_polynomial(z):
            # T_k(-z/2), including its derivative with respect to z.
            value, derivative = coefficients[0], mp.mpf(0)
            before, old_derivative = mp.mpf(1), mp.mpf(0)
            current, current_derivative = -z/2, -mp.mpf(1)/2
            for k in range(1, L+1):
                value += 2*coefficients[k]*current
                derivative += 2*coefficients[k]*current_derivative
                following = -z*current-before
                next_derivative = -current-z*current_derivative-old_derivative
                before, current = current, following
                old_derivative, current_derivative = current_derivative, next_derivative
            return value, derivative

        for z in nodes+[mp.mpf(-2), mp.mpf(2)]:
            expected = original(z)
            actual = fourier_as_polynomial(z)
            close(actual[0], expected[0])
            close(actual[1], expected[1])
        for t in (mp.mpf(0), mp.mpf("0.37"), mp.mpf("1.2"),
                  mp.mpc("0.27", "0.11")):
            actual = sum((coefficients[abs(k)]*mp.exp(1j*k*t)
                          for k in range(-L, L+1)), mp.mpc(0))
            close(actual, original(-2*mp.cos(t))[0])
        coefficient_mass = coefficients[0]+2*sum(coefficients[1:])
        expected_mass = mp.mpf(1) if N % 2 else 1/(N*mp.sin(theta/2)**2)
        close(coefficient_mass, expected_mass)
        assert all(a > 0 for a in coefficients)
        assert coefficient_mass <= N+mp.mpf("1e-90")

    here = Path(__file__).resolve()
    result = {"status": "passed", "precision_decimal_digits": mp.mp.dps,
              "levels": [2, 18], "checks": checks,
              "maximum_relative_error": mp.nstr(maximum_error, 12),
              "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
              "scope": "Defining Newton products versus finite Fourier polynomials, "
                       "including all physical first normals; no asymptotic claim."}
    output = args.output or here.parents[1]/"repro/results/research-middle-newton-fourier-formula.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
