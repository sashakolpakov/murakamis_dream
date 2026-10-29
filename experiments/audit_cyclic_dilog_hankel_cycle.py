#!/usr/bin/env python3
"""Check the marked Hankel jump orientation against actual Euler coefficients.

The proof is the slit-domain deformation in the companion note. These
high-precision integrals check phases, signs and both root orientations.
"""

import json
from pathlib import Path

import mpmath as mp


def hankel_coefficient(N, epsilon, a):
    Q = mp.exp(2j * mp.pi / N)
    total = mp.mpc(0)
    for j in range(1, N):
        # r=1+x^N removes every finite branch-end singularity.
        def integrand(x):
            if x == 0:
                if N - 1 - j > 0:
                    return mp.mpc(0)
                r = mp.mpf(1)
                prefactor = mp.mpf(N)
            else:
                r = 1 + x**N
                prefactor = N * x**(N - 1 - j) * r**(-a - 1)
            rest = mp.mpc(1)
            for k in range(1, N):
                if k != j:
                    rest *= mp.exp(-mp.mpf(k) / N *
                                   mp.log(1 - r * Q**(epsilon * (k-j))))
            return prefactor * rest

        integral = mp.quad(integrand, [0, 1, mp.inf])
        total += (mp.sin(mp.pi*j/N) / mp.pi *
                  Q**(epsilon*j*a) * integral)
    return total


def expected_coefficient(N, epsilon, a):
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    fac = mp.mpc(1)
    for k in range(1, a + 1):
        fac *= 1 - Q**k
    return (-1)**a * Q**(a*(a-1)//2) / fac


def main():
    mp.mp.dps = 60
    rows = []
    maximum_error = mp.mpf(0)
    for N in range(2, 8):
        for epsilon in (1, -1):
            for a in range(N):
                got = hankel_coefficient(N, epsilon, a)
                expected = expected_coefficient(N, epsilon, a)
                error = abs(got - expected) / max(1, abs(expected))
                maximum_error = max(maximum_error, error)
                assert error < mp.mpf("1e-40"), (N, epsilon, a, error)
                rows.append({"N": N, "epsilon": epsilon, "a": a,
                             "normalized_absolute_error": str(error)})

    # The opposite-root coefficient has precisely the Q^-a adapter
    # required by the ORIGINAL u polynomial, not a changed physical root.
    for N in range(2, 8):
        Q = mp.exp(2j * mp.pi / N)
        fac = mp.mpc(1)
        for a in range(N):
            if a:
                fac *= 1 - Q**a
            got = Q**(-a) * expected_coefficient(N, -1, a)
            assert abs(got - 1/fac) < mp.mpf("1e-50")

    result = {"status": "PASS", "coefficient_cases": len(rows),
              "max_normalized_absolute_error": str(maximum_error),
              "checks": rows,
              "scope": "Numerical check of exact all-level slit-deformation proof; no knot asymptotic asserted."}
    Path(__file__).with_name("cyclic_dilog_hankel_cycle_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "coefficient_cases", "max_normalized_absolute_error")}, indent=2))


if __name__ == "__main__":
    main()
