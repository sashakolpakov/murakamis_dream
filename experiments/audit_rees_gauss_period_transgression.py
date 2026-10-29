"""Universal differential and marked-function checks for the Rees period map.

The proof is in notes/rees_gauss_period_transgression.md.  These checks
also compare path integrals on the same dilogarithm branches, including
varying meridians and the resolved parabolic chart.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_checks() -> dict[str, bool]:
    U, r, p, N = sp.symbols("U r p N", nonzero=True)
    x, ell = sp.symbols("x ell")
    # One-form coefficients in (dlog U, dlog p, dlog M).
    log_one_minus = -r * U / (1 - r * U)
    d_ell = sp.Matrix([log_one_minus, 0, -2 * N * log_one_minus])
    d_W = x * d_ell - sp.Matrix([x, 0, -2 * N * ell])
    theta_difference = x * (d_ell + sp.Matrix([-1, 0, N]))
    peripheral = sp.Matrix([0, 0, N * (x - 2 * ell)])
    assert all(sp.simplify(a) == 0 for a in theta_difference - d_W - peripheral)

    v, w = sp.symbols("v w")
    h = sp.log(1 + w * v)
    source_dv = h / v
    gauss_dw = -h / w
    assert sp.simplify(sp.diff(source_dv, w) - 1 / (1 + w * v)) == 0
    assert sp.simplify(-sp.diff(gauss_dw, v) - 1 / (1 + w * v)) == 0
    assert sp.limit(source_dv, v, 0) == w
    assert sp.limit(gauss_dw, w, 0) == -v
    t = sp.symbols("t")
    potential = -sum((-t) ** j / sp.Integer(j) ** 2 for j in range(1, 8))
    potential -= sp.log(1 + t) ** 2 / 2
    expected = t - sp.Rational(3, 4) * t**2 + sp.Rational(11, 18) * t**3
    assert sp.series(potential - expected, t, 0, 4).removeO() == 0
    assert sp.simplify((-x / (U * (1 - U))).subs(x, sp.log(U))).limit(U, 1) == 1
    return {
        "fixed_leaf_and_full_peripheral_identity": True,
        "both_resolved_primitives_have_the_same_two_form": True,
        "both_exceptional_divisors_are_removable": True,
        "complete_point_taylor_coefficients": True,
    }


def W(x: mp.mpc, mu: mp.mpc, level: int) -> mp.mpc:
    argument = mp.exp(x - 2 * level * mu)
    return mp.polylog(2, argument) + x * mp.log(1 - argument) - x * x / 2


def path_checks() -> dict[str, int | str]:
    mp.mp.dps = 85
    tolerance = mp.mpf("1e-65")
    max_error = mp.mpf(0)
    fixed = varying = parabolic = 0
    for level in range(2, 10):
        for variant in range(4):
            x0 = mp.mpc("-0.43", "0.06") + variant * mp.mpc("0.015", "0.008")
            dx = mp.mpc("0.09", "0.035")
            mu0 = mp.mpc("0.023", "0.011")
            for dmu in (mp.mpc(0), mp.mpc("0.006", "-0.002")):
                def one_form(s: mp.mpf) -> mp.mpc:
                    x = x0 + s * dx
                    mu = mu0 + s * dmu
                    argument = mp.exp(x - 2 * level * mu)
                    dlog_e_minus_dlog_p = (
                        level * dmu - dx
                        - argument * (dx - 2 * level * dmu) / (1 - argument)
                    )
                    return x * dlog_e_minus_dlog_p

                def boundary(s: mp.mpf) -> mp.mpc:
                    x = x0 + s * dx
                    mu = mu0 + s * dmu
                    ell = mp.log(1 - mp.exp(x - 2 * level * mu))
                    return level * (x - 2 * ell) * dmu

                integral = mp.quad(one_form, [0, 1])
                difference = W(x0 + dx, mu0 + dmu, level) - W(x0, mu0, level)
                difference += mp.quad(boundary, [0, 1])
                error = abs(integral - difference)
                assert error < tolerance, (level, variant, dmu, error)
                max_error = max(max_error, error)
                if dmu:
                    varying += 1
                else:
                    fixed += 1

        for epsilon in (mp.mpf("0.1"), mp.mpf("0.0001"), mp.mpf("1e-20")):
            v, w = epsilon * mp.mpc("0.3", "0.1"), mp.mpc("0.7", "-0.2")
            U = 1 / (1 + w * v)
            x = mp.log(U)
            resolved = -mp.polylog(2, 1 - U) - x * x / 2
            raw = W(x, mp.mpc(0), level) - mp.pi**2 / 6
            error = abs(resolved - raw)
            assert error < tolerance, (level, epsilon, error)
            max_error = max(max_error, error)
            parabolic += 1
    return {
        "fixed_meridian_marked_path_integrals": fixed,
        "varying_meridian_with_peripheral_correction": varying,
        "parabolic_source_branch_cancellations": parabolic,
        "maximum_absolute_error": mp.nstr(max_error, 8),
        "precision_decimal_digits": mp.mp.dps,
    }


def main() -> None:
    result = {"symbolic": symbolic_checks(), "whole_period_paths": path_checks()}
    output = Path(__file__).with_name("rees_gauss_period_transgression_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
