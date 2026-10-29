#!/usr/bin/env python3
"""Actual prefix correction and original positive-source scale audit.

Exact finite fields verify the actual crossing's relative correction.
Numerical positive sums diagnose separately proved source-support and
interval-product scale formulas. No general knot-volume claim.
"""

import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import alg_product
from audit_finite_sum_annihilator import field


def exact_prefix_case(N, M):
    p, _, q = field(N)
    Q, x = q*q % p, -M*pow(q, -1, p) % p
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    d = [pow(-1, k, p)*pow(x, -2*k, p)*pow(Q, k*(k-1)//2, p) % p for k in range(N)]
    actual, actual_inverse, complete = (np.zeros(N*N, dtype=np.int64) for _ in range(3))
    for a, k in itertools.product(range(N), repeat=2):
        complete[a*N+k] = pow(x, -a, p)*d[k]*pow(fac[a], -1, p) % p
        if a+k < N:
            actual[a*N+k] = complete[a*N+k]
            actual_inverse[a*N+k] = (pow(d[a+k], -1, p)*pow(-1, a, p)
                *pow(Q, a*(a-1)//2, p)*pow(x, -a, p)*pow(fac[a], -1, p)) % p
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    assert np.array_equal(alg_product(actual_inverse, actual, N, 0, p), one)
    h = (alg_product(actual_inverse, complete, N, 0, p)-one) % p
    expected = np.zeros_like(h)
    entries = 0
    for a, k in itertools.product(range(1, N), range(N)):
        if a+k >= N:
            r = a+k-N
            expected[a*N+k] = (pow(x, a-2*N, p)*pow(Q, a, p)*fac[k]
                *pow(N*(1-pow(Q, a, p))*fac[r], -1, p)) % p
            entries += 1
    assert np.array_equal(h, expected)
    assert not np.any(alg_product(h, h, N, 0, p))
    return {"N": N, "M": M, "field": p, "wrapped_coefficients": entries,
            "actual_prefix_correction_square_zero": True}


def logsumexp(values):
    peak = max(values)
    return peak+math.log(sum(math.exp(value-peak) for value in values))


def scale_case(N):
    logs = [math.log(2*math.sin(math.pi*j/N)) for j in range(1, N)]
    positive_indices = [j for j in range(1, N) if logs[j-1] > 0]
    r, k = min(positive_indices)-1, max(positive_indices)
    positive_total = sum(max(value, 0) for value in logs)
    a = N-k+r
    selected_h_log = positive_total-math.log(2*N*math.sin(math.pi*a/N))
    upper_h_log = positive_total-math.log(4)
    assert selected_h_log <= upper_h_log+1e-9
    terms, running = [0.0], 0.0
    for value in logs:
        running += 2*value
        terms.append(running)
    full = logsumexp(terms)
    d = int(math.sqrt(N))
    low = logsumexp(terms[:d+1])
    assert low <= math.log(d+1)+d*math.log(4)+1e-9
    saddle = min(N-1, round(5*N/6))
    cutoffs = {}
    for alpha in (.4, .6, .8, .9):
        end = min(N-1, math.floor(alpha*N))
        cutoffs[str(alpha)] = logsumexp(terms[:end+1])/N
    return {"N": N, "prefix_coefficient_rate_lower": selected_h_log/N,
            "prefix_coefficient_rate_upper": upper_h_log/N,
            "original_figure_eight_period_rate": full/N,
            "sublinear_window_rate": low/N,
            "single_bulk_term_rate": terms[saddle]/N,
            "linear_window_rates": cutoffs,
            "scope": "Diagnostics of independently proved interval and support asymptotics."}


def main():
    exact = [exact_prefix_case(N, M) for N in range(2, 17) for M in (1, 3)]
    with mp.workdps(40):
        lam = -mp.quad(lambda t: mp.log(2*mp.sin(t)), [0, mp.pi/6])
        rate = float(2*lam/mp.pi)
    scales = [scale_case(N) for N in (60, 120, 240, 480, 960, 1920)]
    result = {"status": "PASS", "exact_prefix_cases": exact,
              "calibrated_local_rate_Vol_figure_eight_over_2pi": rate,
              "scale_diagnostics": scales,
              "scope": "Actual completion correction and original figure-eight source filtration. No general geometric selection proof."}
    Path(__file__).with_name("source_leading_filtration_scale_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_prefix_cases": len(exact),
                      "exact_wrapped_coefficients": sum(row["wrapped_coefficients"] for row in exact),
                      "reference_rate": rate, "last_scale": scales[-1]}, indent=2))


if __name__ == "__main__":
    main()
