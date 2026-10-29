#!/usr/bin/env python3
"""Compare compact products to the original Faddeev integral, independently.

The complex-b regime has both compact products absolutely convergent. This
does not evaluate either individual product on the unit circle.
"""

import json
from pathlib import Path

import mpmath as mp


def phi_original_integral(b, Z):
    height = mp.mpf("0.2")

    def integrand(t):
        w = t + 1j * height
        return mp.exp(-2j * Z * w) / (4 * mp.sinh(b * w) * mp.sinh(w / b) * w)

    return mp.exp(mp.quad(integrand, [-mp.inf, -8, -2, 0, 2, 8, mp.inf]))


def phi_compact_quotient(b, Z):
    q = mp.exp(2j * mp.pi * b**2)
    q_dual = mp.exp(-2j * mp.pi / b**2)
    numerator_arg = -mp.exp(1j * mp.pi * b**2 + 2 * mp.pi * b * Z)
    denominator_arg = -mp.exp(-1j * mp.pi / b**2 + 2 * mp.pi * Z / b)
    return mp.qp(numerator_arg, q) / mp.qp(denominator_arg, q_dual)


def main():
    mp.mp.dps = 45
    b = mp.sqrt(mp.mpc("0.3", "0.15"))
    completion_checks = []
    for Z in [mp.mpc("-0.4", "0.1"), mp.mpc("0.2", "-0.2"), mp.mpc("0", "0")]:
        direct = phi_original_integral(b, Z)
        compact = phi_compact_quotient(b, Z)
        error = abs(direct / compact - 1)
        assert error < mp.mpf("1e-35")
        completion_checks.append({"Z": str(Z), "relative_error": str(error)})

    max_factorial_error = mp.mpf(0)
    for N in [6, 9, 16]:
        q = mp.exp(2j * mp.pi / N)
        for k in range(N):
            sine_factorial = mp.fprod(2 * mp.sin(mp.pi * j / N) for j in range(1, k + 1))
            phase = (-1j)**k * mp.exp(mp.pi * 1j * k * (k + 1) / (2 * N))
            error = abs(mp.qp(q, q, k) / (phase * sine_factorial) - 1)
            max_factorial_error = max(max_factorial_error, error)
    assert max_factorial_error < mp.mpf("1e-38")
    result = {
        "source_identity": "Andersen--Kashaev arXiv:1109.6295v2, equation (44)",
        "b_squared": "0.3+0.15i",
        "original_integral_vs_compact_quotient": completion_checks,
        "max_root_of_unity_factorial_phase_error": str(max_factorial_error),
        "scope": "Numerical diagnostics; the functional-equation and normalization proof is in notes/custom_literature_equivalence.md.",
    }
    Path(__file__).with_name("local_completion_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
