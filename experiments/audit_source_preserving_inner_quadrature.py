#!/usr/bin/env python3
"""Check the exact finite quadrature; no knot/source-transform assumption."""

import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 65


def case(N, n):
    Q = mp.exp(2j * mp.pi / N)
    F = [mp.mpc(1)]
    for k in range(1, N):
        F.append(F[-1] * (1 - Q**k))
    m = N - 1 - n
    delta = mp.mpf(n) / N - mp.mpf("0.5")
    assert delta > 0 and 2 * m <= N - 1

    # Normalize by the literal endpoint; no small exponential divided out
    # in the proof, only a numerical scale used by this diagnostic.
    def h(z):
        z = mp.mpc(z)
        return mp.exp(-1j * mp.pi * z * (z - N + 1) / N) * mp.fprod(
            1 - mp.exp(2j * mp.pi * (z + r) / N)
            for r in range(1, m + 1)
        ) / F[m]

    literal = [
        Q**(-j * (n + 1)) * F[n] / (F[j] * F[n - j])
        for j in range(n + 1)
    ]
    lattice_error = max(abs(h(j) - literal[j]) for j in range(n + 1))
    assert lattice_error < mp.mpf("1e-52")

    vertical_error = mp.mpf(0)
    max_growth_ratio = mp.mpf(0)
    for a in (0, n):
        for t in (mp.mpf("0.2"), mp.mpf("1"), mp.mpf("3.7"), mp.mpf("12")):
            prod = mp.fprod(mp.sqrt(1 + mp.sinh(mp.pi*t/N)**2 /
                                   mp.sin(mp.pi*r/N)**2)
                           for r in range(1, m + 1))
            full = mp.sinh(mp.pi*t)/(N*mp.sinh(mp.pi*t/N))
            assert prod**2 <= full * (1 + mp.mpf("1e-60"))
            for sign in (-1, 1):
                actual = abs(h(a + sign*1j*t))
                predicted = abs(h(a))*mp.exp(
                    mp.pi*(2*a+n-2*N+2)*sign*t/N)*prod
                vertical_error = max(vertical_error,
                                     abs(actual/predicted-1))
                ratio = actual / mp.exp((2*mp.pi-mp.pi*delta)*t)
                max_growth_ratio = max(max_growth_ratio, ratio)
                assert ratio <= 1 + mp.mpf("1e-50")
    assert vertical_error < mp.mpf("1e-50")

    real_integral = mp.quad(h, list(range(n + 1)))
    endpoints = (h(0) + h(n)) / 2

    def correction(t):
        if not t:
            # h(it)-h(-it)-h(n+it)+h(n-it) =
            # 2it [h'(0)-h'(n)] + O(t^2).
            return -(mp.diff(h, 0)-mp.diff(h, n))/mp.pi
        return 1j*(h(1j*t)-h(-1j*t)-h(n+1j*t)+h(n-1j*t)) / mp.expm1(2*mp.pi*t)

    cutoff = mp.mpf(95)/(mp.pi*delta)
    breaks = [mp.mpf(v) for v in (0, 1, 3, 8, 20, 40, 80)]
    breaks = [v for v in breaks if v < cutoff] + [cutoff]
    boundary = mp.quad(correction, breaks)
    tail_bound = 8*mp.exp(-mp.pi*delta*cutoff)/(mp.pi*delta)
    exact_sum = mp.fsum(literal)
    residual = abs(exact_sum-real_integral-endpoints-boundary)
    assert residual <= 100*tail_bound + mp.mpf("1e-33"), (N,n,residual,tail_bound)
    error = abs(exact_sum-real_integral)
    return {
        "N": N, "n": n,
        "lattice_error": float(lattice_error),
        "vertical_identity_error": float(vertical_error),
        "max_endpoint_growth_ratio": float(max_growth_ratio),
        "quadrature_identity_residual": float(residual),
        "proven_truncation_bound": float(tail_bound),
        "normalized_sum_minus_integral": float(error),
        "normalized_error_divided_by_1_plus_log_N": float(error/(1+mp.log(N))),
    }


def main():
    rows = []
    for N, n in ((8,6),(8,7),(13,9),(13,11),(21,14),(21,18)):
        row = case(N,n)
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = {
        "status": "PASS",
        "cases": rows,
        "scope": "Exact finite factorial sum and its entire interpolant; original 5_2 identification and outer/geometric analysis are separate.",
    }
    out = Path(__file__).with_name("source_preserving_inner_quadrature_results.json")
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","cases":len(rows),"output":str(out)}))


if __name__ == "__main__":
    main()

