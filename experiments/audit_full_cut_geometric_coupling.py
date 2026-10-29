#!/usr/bin/env python3
"""Original all-inverse radial cut: phase, profile, Gamma and signs.

The all-level proof is in notes/full_cut_geometric_coupling.md.
These are high precision diagnostics of the exact marked cut functions.
"""

import json
from pathlib import Path

import mpmath as mp


def data(N, j, epsilon=1):
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    u = mp.mpf(j) / N
    terms = [(mp.mpf(k) / N, Q ** (k - j)) for k in range(1, N) if k != j]
    endpoint = mp.exp(-sum(weight * mp.log(1 - root) for weight, root in terms))
    return u, terms, endpoint


def ratio(terms, N, s):
    delta = mp.expm1(s / N)
    return mp.exp(-sum(weight * mp.log1p(delta * root / (root - 1))
                       for weight, root in terms))


def symbol(u, v, epsilon=1):
    q = mp.log(2 * mp.sin(mp.pi * u)) / (2 * mp.pi)
    alpha = v + mp.mpf(1) / 4 + u / 2 - epsilon * 1j * q
    return mp.gamma(alpha) / (mp.gamma(u) * mp.gamma(alpha + 1 - u))


def profile(u, s, epsilon=1):
    if not s:
        return mp.mpc(1)
    q = mp.log(2 * mp.sin(mp.pi * u)) / (2 * mp.pi)
    return mp.exp(-s / 4 + epsilon * 1j * q * s) * (mp.sinh(s / 2) / (s / 2)) ** -u


def endpoint_checks():
    maximum = mp.mpf(0)
    count = 0
    for N in range(2, 31):
        Q = mp.exp(2j * mp.pi / N)
        for epsilon in (1, -1):
            C = mp.exp(-epsilon * 1j * mp.pi * (N - 1) * (N - 2) / (12 * N))
            fac = mp.mpc(1)
            for j in range(1, N):
                fac *= 1 - Q ** (-epsilon * j)
                u, _, endpoint = data(N, j, epsilon)
                predicted = C * fac / N ** (u + mp.mpf(1) / 2)
                maximum = max(maximum, abs(endpoint / predicted - 1))
                count += 1
    assert maximum < mp.mpf("1e-45")
    return {"cases": count, "max_relative_error": float(maximum)}


def profiles():
    rows = []
    for N in (24, 48, 96, 192):
        for j in (N // 4, N // 3, 5 * N // 6):
            for epsilon in (1, -1):
                u, terms, _ = data(N, j, epsilon)
                errors = [abs(ratio(terms, N, s) / profile(u, s, epsilon) - 1)
                          for s in map(mp.mpf, ("0.2", "1", "3", "10"))]
                rows.append({"N": N, "j": j, "epsilon": epsilon,
                             "relative_errors_s_02_1_3_10": list(map(float, errors))})
    return rows


def normalized_moment(N, j, a, epsilon=1):
    u, terms, _ = data(N, j, epsilon)
    v = mp.mpf(a) / N
    power = 1 / (1 - u)
    upper_s = mp.mpf(160)
    upper_y = upper_s ** (1 / power)
    prefactor = mp.sin(mp.pi * u) / mp.pi

    def integrand(y):
        if not y:
            return prefactor * power
        s = y ** power
        weight = (N * mp.expm1(s / N)) ** -u
        return (prefactor * weight * ratio(terms, N, s) * mp.exp(-v * s)
                * power * y ** (power - 1))

    bounds = sorted(set([mp.mpf(0), upper_y] + [min(upper_y, mp.mpf(k) / 2) for k in range(1, 9)]))
    return mp.quad(integrand, bounds)


def moments():
    rows = []
    for N in (24, 48, 96):
        for j, a in ((N // 4, 0), (N // 3, N // 5), (5 * N // 6, N // 5)):
            u, _, _ = data(N, j)
            v = mp.mpf(a) / N
            actual = normalized_moment(N, j, a)
            predicted = symbol(u, v)
            q = mp.log(2 * mp.sin(mp.pi * u)) / (2 * mp.pi)
            x = v + mp.mpf(1) / 4 + u / 2
            lower = mp.sin(mp.pi * u) / mp.pi * x / (x * x + q * q)
            rows.append({"N": N, "j": j, "a": a,
                         "actual_normalized": [float(mp.re(actual)), float(mp.im(actual))],
                         "Gamma_symbol": [float(mp.re(predicted)), float(mp.im(predicted))],
                         "relative_error": float(abs(actual / predicted - 1)),
                         "positive_real_lower_bound": float(lower)})
    return rows


def accretivity():
    rows = []
    for u in map(mp.mpf, ("0.05", "0.25", "0.5", "0.833333333333333333333", "0.95")):
        for v in map(mp.mpf, ("0", "0.3", "1")):
            for epsilon in (1, -1):
                K = symbol(u, v, epsilon)
                q = mp.log(2 * mp.sin(mp.pi * u)) / (2 * mp.pi)
                x = v + mp.mpf(1) / 4 + u / 2
                lower = mp.sin(mp.pi * u) / mp.pi * x / (x * x + q * q)
                assert mp.re(K) >= lower - mp.mpf("1e-45")
                assert abs(mp.im(K)) <= abs(q) / x * mp.re(K) + mp.mpf("1e-45")
                assert epsilon * q * mp.im(K) >= -mp.mpf("1e-45")
                rows.append({"u": float(u), "v": float(v), "epsilon": epsilon,
                             "ReK": float(mp.re(K)), "explicit_lower": float(lower)})
    return rows


def main():
    with mp.workdps(60):
        endpoint = endpoint_checks()
        profile_rows = profiles()
        moment_rows = moments()
        sign_rows = accretivity()
    result = {"status": "PASS", "endpoint_phase": endpoint,
              "scaled_profile": profile_rows, "radial_moments": moment_rows,
              "Gamma_accretivity": sign_rows,
              "scope": "Original radial contractions; no positivity or lower bound for final angular/pivotal source claimed."}
    Path(__file__).with_name("full_cut_geometric_coupling_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "endpoint_phase": endpoint,
                      "profile_cases": len(profile_rows), "radial_integrals": len(moment_rows),
                      "Gamma_sign_cases": len(sign_rows),
                      "N96_moment_relative_errors": [r["relative_error"] for r in moment_rows if r["N"] == 96]}, indent=2))


if __name__ == "__main__":
    main()
