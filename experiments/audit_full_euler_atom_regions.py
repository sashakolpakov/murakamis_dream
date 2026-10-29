#!/usr/bin/env python3
"""Exact full-atom identities and high precision region diagnostics.

The estimates in notes/full_euler_atom_dilog_and_endpoint_regions.md
are the proofs. These checks use the original full scalar polynomials.
"""

import json
from pathlib import Path

import mpmath as mp

from audit_finite_sum_annihilator import field


def mul_linear(poly, a, p):
    out = [0] * (len(poly) + 1)
    for k, c in enumerate(poly):
        out[k] = (out[k] + c) % p
        out[k + 1] = (out[k + 1] - a * c) % p
    return out


def exact_case(N):
    p, _, q = field(N)
    Q = q * q % p
    fac, u, v = [1], [1], [1]
    for k in range(1, N):
        fac.append(fac[-1] * (1 - pow(Q, k, p)) % p)
        u.append(pow(fac[-1], -1, p))
        v.append(pow(-1, k, p) * pow(Q, k * (k - 1) // 2, p) * u[-1] % p)
    assert fac[-1] == N % p
    # Ordinary-polynomial Ward equations, including the degree-N source.
    wu, wv = [0] * (N + 1), [0] * (N + 1)
    for k in range(N):
        wu[k] = (wu[k] + (pow(Q, k, p) - 1) * u[k]) % p
        wu[k + 1] = (wu[k + 1] + u[k]) % p
        wv[k] = (wv[k] + (pow(Q, k, p) - 1) * v[k]) % p
        wv[k + 1] = (wv[k + 1] - pow(Q, k, p) * v[k]) % p
    ni = pow(N, -1, p)
    assert wu == [0] * N + [ni]
    assert wv == [0] * N + [-ni % p]
    # Whole finite-product representations, not evaluation in z^N=0.
    total_u, total_v = [0] * N, [0] * N
    part_u, part_v = [1], [1]
    for k in range(N):
        for j, c in enumerate(part_u):
            total_u[j] = (total_u[j] + c * ni) % p
        for j, c in enumerate(part_v):
            total_v[j] = (total_v[j] + c * ni) % p
        part_u = mul_linear(part_u, pow(Q, -k - 1, p), p)
        part_v = mul_linear(part_v, pow(Q, k, p), p)
    assert total_u == u and total_v == v
    # Exact top-coefficient/source expansions.
    for k in range(N):
        assert u[N - 1 - k] == (pow(-1, k, p) * pow(Q, -k * (k + 1) // 2, p)
                                      * fac[k] * ni) % p
        assert v[N - 1 - k] == pow(Q, k + 1, p) * fac[k] * ni % p
    return {"N": N, "field": p, "source_and_product_and_reverse_checks": "PASS"}


def coefficients(N):
    Q = mp.exp(2j * mp.pi / N)
    fac, u, v = [mp.mpc(1)], [mp.mpc(1)], [mp.mpc(1)]
    for k in range(1, N):
        fac.append(fac[-1] * (1 - Q ** k))
        u.append(1 / fac[-1])
        v.append((-1) ** k * Q ** (k * (k - 1) // 2) / fac[-1])
    return Q, fac, u, v


def value(coeffs, z):
    out = mp.mpc(0)
    for c in reversed(coeffs):
        out = out * z + c
    return out


def numeric_case(N):
    with mp.workdps(140):
        Q, fac, u, v = coefficients(N)
        H = 2j * mp.pi / N
        rows = []
        for t in (mp.mpf("0.08"), mp.mpf(1) / 6, mp.mpf("0.20")):
            z0 = 1 - mp.exp(-2j * mp.pi * t)
            for w in (mp.mpc(0), mp.mpc("0.4", "0.2"), mp.mpc("-0.3", "0.7")):
                zv = z0 * mp.exp(w / mp.sqrt(N))
                zu = mp.conj(z0) * mp.exp(w / mp.sqrt(N))
                predicted_v = mp.sqrt(1 - zv) * mp.exp(mp.polylog(2, zv) / H)
                predicted_u = mp.exp(-mp.log(1 - zu) / 2 - mp.polylog(2, zu) / H)
                error_v = abs(value(v, zv) / predicted_v - 1)
                error_u = abs(value(u, zu) / predicted_u - 1)
                rows.append({"t": float(t), "window": [float(mp.re(w)), float(mp.im(w))],
                             "v_relative_error": float(error_v), "u_relative_error": float(error_u)})
        exterior = []
        for radius in (mp.mpf("1.3"), mp.mpf("1.8"), mp.mpf("2.4")):
            for angle in (mp.mpf(0), mp.pi / 3, mp.pi / 2):
                z = radius * mp.exp(1j * angle)
                predicted_u = z ** (N - 1) / N * (1 - Q ** -1 * fac[1] / z)
                predicted_v = Q * z ** (N - 1) / N * (1 + Q * fac[1] / z)
                exterior.append({"radius": float(radius), "angle": float(angle),
                                 "N2_u_relative_error": float(N * N * abs(value(u, z) / predicted_u - 1)),
                                 "N2_v_relative_error": float(N * N * abs(value(v, z) / predicted_v - 1))})
        transition = []
        for t in (mp.mpf(1) / 6, mp.mpf("0.25"), mp.mpf("0.35")):
            z = 1 - mp.exp(-2j * mp.pi * t)
            transition.append({"t": float(t), "actual_v_rate": float(mp.log(abs(value(v, z))) / N),
                               "dilog_rate": float(mp.im(mp.polylog(2, z)) / (2 * mp.pi)),
                               "top_degree_rate": float(mp.log(abs(z)))})
        fixed_domain = []
        for radius, angle in (("0.6", "1.5"), ("0.8", "0.2"), ("0.8", "2.8"),
                              ("1.0", "0.5"), ("1.0", "2.5"), ("1.1", "0.9"),
                              ("1.15", "1.2"), ("1.18", "1.0")):
            z = mp.mpf(radius) * mp.exp(1j * mp.mpf(angle))
            g = mp.im(mp.polylog(2, z)) / (2 * mp.pi)
            assert g > mp.log(abs(z))
            V = lambda w: mp.sqrt(1 - w) * mp.exp(mp.polylog(2, w) / H)
            predicted_v = V(z)
            zu = mp.conj(z)
            predicted_u = mp.exp(-mp.log(1 - zu) / 2 - mp.polylog(2, zu) / H)
            fixed_domain.append({"radius": float(abs(z)), "angle": float(mp.arg(z)),
                                 "source_gap": float(g - mp.log(abs(z))),
                                 "v_relative_error": float(abs(value(v, z) / predicted_v - 1)),
                                 "u_conjugate_relative_error": float(abs(value(u, zu) / predicted_u - 1)),
                                 "N2_WKB_transport_error": float(N * N * abs((1 - z) * V(Q * z) / V(z) - 1))})
        return {"N": N, "arc_and_complex_windows": rows, "exterior_two_term": exterior,
                "positive_shape_transition": transition, "fixed_open_domain": fixed_domain}


def main():
    exact = [exact_case(N) for N in range(2, 35)]
    numerics = [numeric_case(N) for N in (40, 80, 160, 320)]
    with mp.workdps(60):
        J = lambda t: -mp.im(mp.polylog(2, mp.exp(2j * mp.pi * t))) / (2 * mp.pi)
        B = lambda t: -J(t) - (1 - t) * mp.log(2 * mp.sin(mp.pi * t))
        ts = mp.findroot(B, (mp.mpf("0.17"), mp.mpf("0.25")))
        threshold = {"t_star": str(ts), "R_star": str(2 * mp.sin(mp.pi * ts))}
    # Checks of convergence diagnostics are deliberately limited to the
    # evaluated values. The all-N assertions use the proofs in the note.
    final = numerics[-1]
    max_arc = max(max(x["u_relative_error"], x["v_relative_error"])
                  for x in final["arc_and_complex_windows"])
    assert max_arc < 0.03
    result = {"status": "PASS", "exact_cases": exact, "threshold": threshold,
              "diagnostics": numerics,
              "scope": "Original full atom polynomials; no whole-knot contour or general Stokes exhaustion claimed."}
    output = Path(__file__).with_name("full_euler_atom_regions_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "exact_levels": len(exact),
                      "numerical_levels": len(numerics), "N320_max_arc_relative_error": max_arc,
                      **threshold}, indent=2))


if __name__ == "__main__":
    main()
