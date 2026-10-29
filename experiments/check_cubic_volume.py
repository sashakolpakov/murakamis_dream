#!/usr/bin/env python3
"""Check the 5_2 dominant-root argument and the specified quantum-curve norm.

Symbolic discriminant/root counts are exact. Quadrature and recurrence values
are numerical evidence; the proof is Theorem 4.2 in the accompanying note.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import quad


CRITICAL_ANGLE = math.acos((3 - math.sqrt(13 + 16 * math.sqrt(2))) / 4)


def coefficients(alpha: float) -> tuple[complex, complex, complex]:
    x = complex(math.cos(alpha), math.sin(alpha))
    b = x**5 - x**4 + 2 * x**2 + 2 * x - 1
    c = -x**7 + 2 * x**6 + 2 * x**5 - x**3 + x**2
    return b, c, x**7


def roots(alpha: float) -> np.ndarray:
    b, c, constant = coefficients(alpha)
    return np.roots([1, b, c, constant])


def symbolic_checks() -> dict[str, object]:
    l, x, u, v = sp.symbols("l x u v")
    b = x**5 - x**4 + 2 * x**2 + 2 * x - 1
    c = -x**7 + 2 * x**6 + 2 * x**5 - x**3 + x**2
    a = l**3 + b * l**2 + c * l + x**7
    assert sp.expand(c - x**7 * b.subs(x, 1 / x)) == 0
    h = x**8 - 6 * x**7 + 11 * x**6 - 12 * x**5 - 11 * x**4 - 12 * x**3 + 11 * x**2 - 6 * x + 1
    discriminant = sp.factor(sp.discriminant(a, l))
    assert sp.expand(discriminant - x**4 * (x - 1) ** 6 * (x + 1) ** 6 * h) == 0
    p = u**4 - 6 * u**3 + 7 * u**2 + 6 * u - 31
    assert sp.expand(h / x**4 - p.subs(u, x + 1 / x)) == 0
    shifted = sp.expand(p.subs(u, v + sp.Rational(3, 2)))
    assert shifted == v**4 - sp.Rational(13, 2) * v**2 - sp.Rational(343, 16)
    assert sp.Poly(p, u).count_roots(-2, 2) == 1
    assert b.subs(x, sp.I) == -4 + 3 * sp.I
    return {
        "self_inversive_identity": True,
        "discriminant": str(discriminant),
        "unit_circle_discriminant_polynomial": str(p),
        "exact_root_count_on_minus2_plus2": 1,
        "b_at_x_i": str(b.subs(x, sp.I)),
        "critical_angle": CRITICAL_ANGLE,
    }


def classical_integral() -> tuple[float, float]:
    def integrand(alpha: float) -> float:
        return math.log(max(abs(roots(alpha))))

    return quad(integrand, 0, CRITICAL_ANGLE, epsabs=1e-9, epsrel=1e-9, limit=200)


def quantum_norm_rate(n: int) -> dict[str, float | int]:
    epsilon = math.log(n + math.e) ** -2
    initial_angle = CRITICAL_ANGLE - epsilon
    step = initial_angle / n
    initial_root = max(roots(initial_angle), key=abs)
    state = np.array([initial_root**2, initial_root, 1], dtype=complex)
    initial_norm = float(np.linalg.norm(state))
    log_norm = math.log(initial_norm)
    state /= initial_norm
    for k in range(n):
        b, c, constant = coefficients(initial_angle - k * step)
        # State order is (f_{k+2}, f_{k+1}, f_k).
        next_state = np.array([
            -b * state[0] - c * state[1] - constant * state[2],
            state[0],
            state[1],
        ])
        norm = float(np.linalg.norm(next_state))
        assert norm > 0
        log_norm += math.log(norm)
        state = next_state / norm
    return {"steps": n, "euclidean_cutoff": epsilon, "h_log_Q": step * log_norm}


def main() -> None:
    integral, error = classical_integral()
    samples = []
    for alpha in (0.05, 0.5, math.pi / 2, CRITICAL_ANGLE - 0.01):
        moduli = sorted(float(abs(root)) for root in roots(alpha))
        assert moduli[0] < 1 < moduli[-1]
        assert abs(moduli[1] - 1) < 1e-9
        samples.append({"alpha": alpha, "root_moduli": moduli})
    result = {
        "status": "exact algebra plus numerical checks; not an assertion about the Jones invariant",
        "symbolic_checks": symbolic_checks(),
        "classical_volume_integral": integral,
        "quadrature_error_estimate": error,
        "sample_root_moduli": samples,
        "quantum_norm_rates": [quantum_norm_rate(n) for n in (128, 512, 2048, 8192, 32768, 131072)],
    }
    destination = Path(__file__).with_name("cubic_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
