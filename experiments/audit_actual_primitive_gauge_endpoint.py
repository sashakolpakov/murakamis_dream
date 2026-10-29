#!/usr/bin/env python3
"""Exact canonical Hilbert90 gauge endpoint, Ward carry and Gauss period.

Finite-field identities are exact; complex rate samples diagnose the
separately proved finite-Poisson asymptotic. No knot-volume assertion.
"""

import json
from pathlib import Path

import mpmath as mp

from audit_finite_sum_annihilator import field


def exact_case(N):
    p, _, q = field(N)
    Q = q*q % p
    fac, v = 1, [1]
    for r in range(1, N):
        fac = fac*(1-pow(Q, r, p)) % p
        v.append(pow(-1, r, p)*pow(Q, r*(r-1)//2, p)*pow(fac, -1, p) % p)
    coeff = [sum(v[r]*v[k-r]*pow(Q, k-r, p) for r in range(k+1)) % p
             for k in range(N)]
    ward = [0]*(N+2)
    for k, c in enumerate(coeff):
        shifted = c*pow(Q, k, p) % p
        ward[k] = (ward[k]+shifted-c) % p
        ward[k+1] = (ward[k+1]-(1+Q)*shifted) % p
        ward[k+2] = (ward[k+2]+Q*shifted) % p
    expected = [0]*N+[-2*pow(N, -1, p) % p, coeff[-1]]
    assert ward == expected
    gauss = sum(pow(-1, r, p)*pow(Q, r*(r-1)//2, p) for r in range(N)) % p
    assert coeff[-1] == gauss*pow(N, -1, p) % p
    assert sum(coeff) % p == (2*pow(N, -1, p)-coeff[-1]) % p
    return {"N": N, "field": p, "canonical_endpoint": sum(coeff) % p,
            "top_coefficient": int(coeff[-1]), "source_terms_retained": 2}


def diagnostic(N):
    with mp.workdps(65):
        Q = mp.exp(2*mp.pi*1j/N)
        gauss = sum((-1)**r*Q**(r*(r-1)//2) for r in range(N))
        omega = mp.exp(-mp.pi*1j*(N+1)/4-mp.pi*1j/(4*N))
        endpoint = (2-gauss)/N
        return {"N": N, "Gauss_minus_stationary_absolute": float(abs(gauss-mp.sqrt(N)*omega)),
                "scaled_endpoint_modulus": float(mp.sqrt(N)*abs(endpoint)),
                "endpoint_log_modulus_per_N": float(mp.log(abs(endpoint))/N),
                "scope": "Numerical diagnostic of proved finite-Poisson asymptotic."}


def main():
    exact = [exact_case(N) for N in range(2, 31)]
    samples = [diagnostic(N) for N in (8, 16, 32, 64, 128, 256, 512, 1024)]
    result = {"status": "PASS", "exact_cases": exact, "complex_diagnostics": samples,
              "scope": "Actual canonical primitive gauge endpoint only; no knot-invariant or volume identity."}
    Path(__file__).with_name("actual_primitive_gauge_endpoint_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_levels": len(exact),
                      "last_diagnostic": samples[-1]}, indent=2))


if __name__ == "__main__":
    main()
