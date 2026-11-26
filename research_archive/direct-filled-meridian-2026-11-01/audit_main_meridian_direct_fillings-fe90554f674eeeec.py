#!/usr/bin/env python3
"""Finite algebra checks for the direct crossing-power meridian formula.

Run: python3 experiments/audit_main_meridian_direct_fillings.py
Requires mpmath.  --profile-diagnostic also repeats the archived 80-digit
36-case local profile scan; those observations are not asymptotic proofs.

Polynomial arithmetic and the full complete Newton crossing are adapted from
the companion audit_main_meridian_auxiliary_color_gap.py. The new checks use
quotient powers, a generic spectral trace, and the analytic complete first
normal. Those identities are checked numerically at the stated precision;
the quadratic charge comparison uses exact rational arithmetic. No contour
or first-alias approximation is used for the finite trace comparisons.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import mpmath as mp


def add(a, b):
    out = [mp.mpc(0)] * max(len(a), len(b))
    for k, x in enumerate(a):
        out[k] += x
    for k, x in enumerate(b):
        out[k] += x
    return out


def scale(a, c):
    return [c * x for x in a]


def multiply(a, b):
    out = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def evaluate(a, z):
    out = mp.mpc(0)
    for x in reversed(a):
        out = out * z + x
    return out


def derivative(a):
    return [k * a[k] for k in range(1, len(a))] or [mp.mpc(0)]


def remainder(a, p):
    out = list(a)
    degree = len(p) - 1
    for k in range(len(out) - 1, degree - 1, -1):
        factor = out[k] / p[-1]
        for j in range(degree + 1):
            out[k - degree + j] -= factor * p[j]
    return out[:degree] + [mp.mpc(0)] * max(0, degree - len(out))


def relation(N, s):
    prev, curr = [mp.mpc(2)], [mp.mpc(0), mp.mpc(1)]
    for _ in range(1, N):
        prev, curr = curr, add([mp.mpc(0)] + curr, scale(prev, -1))
    curr = list(curr)
    curr[0] += 2 * mp.cos(2 * mp.pi * s)
    return curr


def newton(N, r):
    out = [mp.mpc(1)]
    for a in range(r):
        node = 2 * mp.cos((2 * a + 1) * mp.pi / N)
        out = scale(multiply(out, [node, -1]),
                    1 / (4 * mp.sin((a + 1) * mp.pi / N) ** 2))
    return out


def raw_product(N, indices):
    out = [mp.mpc(1)]
    for r in indices:
        out = multiply(out, newton(N, r))
    return out


def complete_crossing(N):
    q = mp.exp(mp.j * mp.pi / N)
    out = [mp.mpc(0)]
    for k in range(N):
        out = add(out, scale(newton(N, k), (-q) ** k))
    return scale(out, mp.exp(mp.j * mp.pi * (N - 1) ** 2 / (2 * N)))


def physical_crossing(N, s):
    if s == 0:
        return complete_crossing(N)
    nodes, values = [], []
    kappa = mp.exp(mp.j * mp.pi * (N - 1 + s) ** 2 / (2 * N))
    for r in range(N):
        nodes.append(2 * mp.cos((-2 * r - 1 + 2 * s) * mp.pi / N))
        values.append(kappa * (-1) ** r *
                      mp.exp(mp.j * mp.pi * (r * (r + 1) - 2 * s * r) / N))
    matrix = mp.matrix([[z ** k for k in range(N)] for z in nodes])
    return list(mp.lu_solve(matrix, mp.matrix(values)))


def inverse_mod(a, p):
    N = len(p) - 1
    matrix = mp.matrix(N)
    for k in range(N):
        col = remainder([mp.mpc(0)] * k + a, p)
        for j in range(N):
            matrix[j, k] = col[j]
    return list(mp.lu_solve(matrix, mp.matrix([1] + [0] * (N - 1))))


def power_mod(a, exponent, p):
    base = inverse_mod(a, p) if exponent < 0 else a
    out = [mp.mpc(1)]
    exponent = abs(exponent)
    while exponent:
        if exponent & 1:
            out = remainder(multiply(out, base), p)
        base = remainder(multiply(base, base), p)
        exponent //= 2
    return out


def polynomial_trace(N, p, power, raw):
    return (-1) ** (N - 1) * N * N * remainder(multiply(power, raw), p)[N - 1]


def generic_spectral_trace(N, s, n, raw):
    pprime = derivative(relation(N, s))
    kappa = mp.exp(mp.j * mp.pi * (N - 1 + s) ** 2 / (2 * N))
    terms = []
    for r in range(N):
        z = 2 * mp.cos((-2 * r - 1 + 2 * s) * mp.pi / N)
        eig = kappa * (-1) ** r * mp.exp(
            mp.j * mp.pi * (r * (r + 1) - 2 * s * r) / N)
        terms.append(eig ** n * evaluate(raw, z) / evaluate(pprime, z))
    return (-1) ** (N - 1) * N * N * mp.fsum(terms)


def chirp_grid_trace(N, s, n, raw):
    eta = (-1) ** (N - 1)
    C = mp.exp(mp.j * mp.pi * n * (mp.mpf((N - 1) ** 2) / 4 - s * s / 2) / N)
    terms = []
    for r in range(N):
        tau = 2 * mp.pi * (mp.mpf(N - 1) / 2 + s - r) / N
        terms.append(mp.sin(tau) * evaluate(raw, -2 * mp.cos(tau)) *
                     mp.exp(mp.j * n * N * tau * tau / (4 * mp.pi)))
    return eta * N * C * mp.fsum(terms) / mp.sin(2 * mp.pi * s)


def complete_first_normal(N, n, raw, omit_chirp_normal=False):
    eta = (-1) ** (N - 1)
    C = mp.exp(mp.j * mp.pi * n * (N - 1) ** 2 / (4 * N))
    draw = derivative(raw)
    terms = []
    for r in range(N):
        tau = 2 * mp.pi * (mp.mpf(N - 1) / 2 - r) / N
        z = -2 * mp.cos(tau)
        value, dz = evaluate(raw, z), evaluate(draw, z)
        normal = mp.cos(tau) * value + 2 * mp.sin(tau) ** 2 * dz
        if not omit_chirp_normal:
            normal += mp.j * n * N * tau * mp.sin(tau) * value / (2 * mp.pi)
        terms.append(mp.exp(mp.j * n * N * tau * tau / (4 * mp.pi)) * normal)
    return eta * C * mp.fsum(terms)


def err(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def text_number(x):
    return mp.nstr(x, 18)


def algebra_checks(levels, digits):
    mp.mp.dps = digits
    params = [("0", mp.mpc(0)),
              ("1/4+i/9", mp.mpc(mp.mpf(1)/4, mp.mpf(1)/9)),
              ("3/4+i/11", mp.mpc(mp.mpf(3)/4, mp.mpf(1)/11)),
              ("-3/4+i/13", mp.mpc(-mp.mpf(3)/4, mp.mpf(1)/13))]
    powers = [-6, -2, 2, 6, 10]
    tolerance = mp.mpf(10) ** (-min(50, digits // 2))
    maxima = {k: mp.mpf(0) for k in
              ("crossing_inverse", "generic_spectral_trace", "chirp_grid_trace",
               "complete_first_normal")}
    rows = []
    for N in levels:
        M = (N - 1) // 2
        indices = sorted(set([(), (0,), (M,), (M, M), (M,) * 3,
                              (0, M, M), (M,) * 5]))
        for label, s in params:
            p = relation(N, s)
            crossing = physical_crossing(N, s)
            inverse = inverse_mod(crossing, p)
            inverse_product = remainder(multiply(crossing, inverse), p)
            e = max(abs(v - (1 if k == 0 else 0))
                    for k, v in enumerate(inverse_product))
            maxima["crossing_inverse"] = max(maxima["crossing_inverse"], e)
            assert e < tolerance, ("inverse", N, label, e)
            for n in powers:
                power = power_mod(crossing, n, p)
                for factors in indices:
                    raw = raw_product(N, factors)
                    exact = polynomial_trace(N, p, power, raw)
                    if s == 0:
                        first = complete_first_normal(N, n, raw)
                        checks = {"complete_first_normal": err(exact, first)}
                    else:
                        spectral = generic_spectral_trace(N, s, n, raw)
                        chirp = chirp_grid_trace(N, s, n, raw)
                        checks = {"generic_spectral_trace": err(exact, spectral),
                                  "chirp_grid_trace": err(exact, chirp)}
                    for name, error in checks.items():
                        maxima[name] = max(maxima[name], error)
                        assert error < tolerance, (name, N, label, n, factors, error)
                    rows.append({"N": N, "s": label, "crossing_power": n,
                                 "low_newton_indices": list(factors),
                                 "raw_degree": sum(factors),
                                 "scaled_errors": {k: text_number(v) for k, v in checks.items()}})
    witness_N, witness_n, raw = 2, 2, [mp.mpc(1)]
    p = relation(witness_N, 0)
    exact = polynomial_trace(witness_N, p, power_mod(complete_crossing(witness_N), witness_n, p), raw)
    omitted = complete_first_normal(witness_N, witness_n, raw, True)
    assert abs(exact - omitted) > 1
    return {"precision_decimal_digits": digits,
            "levels": levels, "powers": powers,
            "s_parameters": [label for label, _ in params],
            "scaled_error_tolerance": text_number(tolerance),
            "finite_trace_cases": len(rows),
            "maximum_errors": {k: text_number(v) for k, v in maxima.items()},
            "first_normal_witness": {
                "N": 2, "n": 2, "raw_product": "1",
                "full_trace": text_number(exact),
                "trace_if_chirp_normal_is_omitted": text_number(omitted),
                "absolute_defect": text_number(abs(exact - omitted))},
            "cases": rows}


def rational_string(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def quadratic_checks():
    b = (1, 3)
    slopes = [(8, 64), (-8, 64), (8, -64), (-8, -64),
              (10, 1000), (-1000, 10)]
    charges = [(1, 2), (2, 1), (2, 3)]
    rows = []
    for n in slopes:
        first = sum(Fraction(bi, ni * ni + bi * bi) for bi, ni in zip(b, n))
        for ell in charges:
            actual_gap = sum(Fraction(bi * (li * li - 1), ni * ni + bi * bi)
                             for bi, ni, li in zip(b, n, ell))
            lower = sum(Fraction(bi * (li * li - 1), 2 * ni * ni)
                        for bi, ni, li in zip(b, n, ell))
            assert actual_gap >= lower > 0
            rows.append({"signed_slopes": list(n), "charges": list(ell),
                         "first_drop_divided_by_pi": rational_string(first),
                         "joint_gap_divided_by_pi": rational_string(actual_gap),
                         "proved_lower_bound_divided_by_pi": rational_string(lower)})
    n = (10, 1000)
    first = sum(Fraction(bi, ni * ni + bi * bi) for bi, ni in zip(b, n))
    separate_second = Fraction(3 * b[1], n[1] ** 2 + b[1] ** 2)
    assert separate_second < first
    return {"arithmetic": "exact fractions",
            "model": "Psi=F0-sum_i b_i*tau_i^2/(4*pi), b=(1,3)",
            "exact_formula": "(F0-Re S_ell)/pi=sum_i b_i*ell_i^2/(n_i^2+b_i^2)",
            "checks": rows,
            "unbalanced_local_error_warning": {
                "signed_slopes": list(n),
                "first_total_drop_divided_by_pi": rational_string(first),
                "second_coordinate_alias_gap_divided_by_pi": rational_string(separate_second),
                "scope": "The separate local error bound need not lie below the joint filled exponent; the joint charge gap is still positive."}}


def profile_diagnostic():
    """Repeat the archived local diagnostic; no asymptotic assertion is tested."""
    mp.mp.dps = 80
    rows = []
    for N in (40, 41, 80, 81, 160, 161):
        k = int(mp.mpf('.31') * N)
        centers = [2 * mp.cos((2*j+1)*mp.pi/N) for j in range(k)]
        denominator = mp.fprod(2*mp.sin(j*mp.pi/N) for j in range(1,k+1)) ** 2
        def values(tau):
            z = -2 * mp.cos(tau)
            value, dz = mp.mpc(1), mp.mpc(0)
            for c in centers:
                dz = dz * (c-z) - value
                value *= c-z
            return value/denominator, dz/denominator
        for n in (6, -6, 10):
            normals = []
            for r in range(N):
                tau = 2*mp.pi*(mp.mpf(N-1)/2-r)/N
                value, dz = values(tau)
                normals.append(mp.exp(mp.j*n*N*tau*tau/(4*mp.pi)) * (
                    mp.cos(tau)*value + 2*mp.sin(tau)**2*dz
                    + mp.j*n*N*tau*mp.sin(tau)*value/(2*mp.pi)))
            complete = (-1)**(N-1) * mp.fsum(normals)
            for s in (mp.mpc('.23','.11'), mp.mpc('.72','.09')):
                samples = []
                for r in range(N):
                    tau = 2*mp.pi*(mp.mpf(N-1)/2+s-r)/N
                    value, _ = values(tau)
                    samples.append(mp.sin(tau)*value*mp.exp(mp.j*n*N*tau*tau/(4*mp.pi)))
                moving = (-1)**(N-1)*N*mp.fsum(samples)/mp.sin(2*mp.pi*s)
                error = abs(moving/complete-1)
                rows.append({"N": N, "k": k, "n": n, "s": str(s),
                             "ratio_error": mp.nstr(error,18),
                             "log_error_per_N": mp.nstr(mp.log(error)/N,18)})
    return {"precision": 80,
            "source": "research_archive/main-meridian-profile-2026-11-01/md-direct-filled-root-diagnostic.py",
            "scope": "Optional local numerical diagnostic only; no convergence or whole-knot theorem is inferred.",
            "formula": "Cartan factors divided out; the complete trace uses the exact first normal.",
            "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'main_meridian_direct_fillings_results.json'))
    parser.add_argument('--digits', type=int, default=80)
    parser.add_argument('--levels', default='2,3,4')
    parser.add_argument('--profile-diagnostic', action='store_true')
    args = parser.parse_args()
    if args.digits < 60:
        parser.error('--digits must be at least 60')
    levels = [int(x) for x in args.levels.split(',')]
    if any(N < 2 for N in levels):
        parser.error('all levels must be at least two')
    algebra = algebra_checks(levels, args.digits)
    result = {"scope": "High-precision numerical checks of finite quotient/source identities, and exact rational checks of a quadratic joint-charge model.",
              "limits": "These checks do not prove uniform asymptotics, contour tail bounds, a grouped wire packet, or a whole filled-knot volume theorem.",
              "crossing_normalization": "Full physical Cartan factor retained; complete crossing includes its original Hermite normals.",
              "polynomial_code_origin": "audit_main_meridian_auxiliary_color_gap.py: polynomial arithmetic and full complete Newton crossing; the direct-power/first-normal and quadratic checks are defined here",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "algebra": algebra, "quadratic_joint_charges": quadratic_checks()}
    if args.profile_diagnostic:
        result['optional_profile_diagnostic'] = profile_diagnostic()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({"finite_trace_cases": algebra['finite_trace_cases'],
                      "maximum_errors": algebra['maximum_errors'],
                      "exact_quadratic_cases": len(result['quadratic_joint_charges']['checks']),
                      "optional_profile_cases": len(result.get('optional_profile_diagnostic', {}).get('rows', []))}, sort_keys=True))


if __name__ == '__main__':
    main()
