#!/usr/bin/env python3
"""High-precision checks of the proved actual-gauge normal-form action.

These are diagnostics of the uniform analytic proof, not a knot-volume
or a substitute asymptotic proof. The polynomial comes from the literal
actual Euler coefficients, not from defining it by the dilogarithm.
"""

import json
from pathlib import Path

import mpmath as mp


def case(N):
    with mp.workdps(110):
        Q = mp.exp(2*mp.pi*1j/N)
        w = mp.mpc(0, mp.mpf(1)/4)
        fac, v = mp.mpc(1), [mp.mpc(1)]
        for k in range(1, N):
            fac *= 1-Q**k
            v.append((-1)**k*Q**(k*(k-1)//2)/fac)
        polynomial = [sum(v[r]*v[k-r]*Q**(k-r) for r in range(k+1)) for k in range(N)]
        value = sum(coefficient*w**k for k, coefficient in enumerate(polynomial))
        logarithm = sum((1+Q**a)*w**a/(a*(Q**a-1)) for a in range(1, N))
        exponential = mp.exp(logarithm)
        truncation_error = abs(value-exponential)
        bound = 2*mp.exp(-mp.mpf(N)*mp.log(2)/2)
        assert truncation_error <= bound*(1+mp.mpf('1e-30'))
        coefficient_norm = mp.sqrt(sum(abs(coefficient)**2 for coefficient in polynomial))
        assert coefficient_norm >= mp.sqrt(mp.mpf(15)/16)*abs(value)
        reference_rate = mp.im(mp.polylog(2, w))/mp.pi
        actual_rate = mp.log(abs(value))/N
        return {"N": N, "normal_form_log_modulus_per_N": float(actual_rate),
                "dilogarithm_rate": float(reference_rate),
                "logarithm_of_coefficient_norm_per_N": float(mp.log(coefficient_norm)/N),
                "relative_truncation_error": float(truncation_error/abs(exponential)),
                "N_times_action_error": float(N*abs(mp.log(value/exponential))),
                "scope": "Numerical diagnostic; direct proof supplies the all-level asymptotic."}


def main():
    rows = [case(N) for N in (8, 16, 32, 64, 128, 256)]
    result = {"status": "PASS", "cases": rows,
              "scope": "Actual primitive Hilbert90 gauge polynomial, retained Taylor tail and positive gauge norm. No selected knot or regulator-volume identity."}
    Path(__file__).with_name("actual_hilbert90_gauge_action_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
