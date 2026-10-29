#!/usr/bin/env python3
"""Actual nilpotent Euler meridian half-step and its retained endpoint.

Exact finite-field identities are checked before truncating degree N.
Complex coefficient checks illustrate separately proved uniform bounds.
No knot-volume assertion or physical-metric fusion estimate is made.
"""

import cmath
import json
import math
from pathlib import Path

from audit_finite_sum_annihilator import field


def convolution(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i+j] = (out[i+j]+av*bv) % p
    return out


def exact_case(N):
    p, _, q = field(N)
    Q = q*q % p
    fac, u, v, A, B = [1], [1], [1], [1], [1]
    for k in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, k, p)) % p)
        u.append(pow(fac[k], -1, p))
        v.append(pow(-1, k, p)*pow(Q, k*(k-1)//2, p)*u[k] % p)
        A.append(A[-1]*(1-pow(q, 2*k-1, p))*pow(1-pow(Q, k, p), -1, p) % p)
        B.append(B[-1]*q*(1-pow(q, 2*k-3, p))*pow(1-pow(Q, k, p), -1, p) % p)
    assert convolution(u, v, p)[:N] == [1]+[0]*(N-1)
    uq = [av*pow(q, k, p) % p for k, av in enumerate(u)]
    vq = [av*pow(q, k, p) % p for k, av in enumerate(v)]
    assert convolution(uq, v, p)[:N] == B
    assert convolution(u, vq, p)[:N] == A
    assert convolution(A, B, p)[:N] == [1]+[0]*(N-1)

    def ward(coefficients, first, second):
        shifted = [av*pow(Q, k, p) % p for k, av in enumerate(coefficients)]
        lhs = convolution([1, -first % p], shifted, p)
        rhs = convolution([1, -second % p], coefficients, p)
        return [(a-b) % p for a, b in zip(lhs, rhs)]

    assert ward(B, 1, q) == [0]*N+[-2*pow(N, -1, p) % p]
    assert ward(A, q, 1) == [0]*N+[2*pow(N, -1, p) % p]
    b1 = sum(B) % p
    bq = sum(av*pow(q, k, p) for k, av in enumerate(B)) % p
    assert b1 == 2*pow(N*(1-q), -1, p) % p
    assert bq == 2*pow(N*(1-pow(q, -1, p)), -1, p) % p
    carry = convolution([av*pow(q, k, p) % p for k, av in enumerate(B)], B, p)
    carry[0] = (carry[0]-1) % p
    carry[1] = (carry[1]+1) % p
    assert not any(carry[:N])
    assert sum(carry[N:]) % p == b1*bq % p != 0

    norm_cases = 0
    for z in (2, 3, 5):
        bottom = top = 1
        for j in range(N):
            bottom = bottom*(1-pow(Q, j, p)*z) % p
            top = top*(1-q*pow(Q, j, p)*z) % p
        assert bottom == (1-pow(z, N, p)) % p
        assert top == (1+pow(z, N, p)) % p
        norm_cases += 1
    return {"N": N, "field": p, "retained_Ward_source": "2*z^N/N",
            "nonzero_endpoint_carry": int(sum(carry[N:]) % p),
            "norm_factor_cases": norm_cases}


def complex_case(N):
    t, a = math.pi/N, 1.0
    inverse_l1, adapter_l1, endpoint = 1.0, 1.0, 1+0j
    for k in range(1, N):
        a *= math.sin((k-.5)*t)/math.sin(k*t)
        b = a*math.sin(t/2)/math.sin((k-.5)*t)
        assert a <= 2/math.sqrt(min(k+1, N-k))+1e-8
        assert b <= math.pi/min(k, N-k)**1.5+1e-8
        inverse_l1 += a
        adapter_l1 += b
        endpoint -= b*cmath.exp(-1j*k*t/2)
    exact = 2/(N*(1-cmath.exp(1j*t)))
    assert abs(endpoint-exact) < 1e-7
    assert inverse_l1 <= 8*math.sqrt(N)
    assert adapter_l1 <= 1+6*math.pi
    assert endpoint.imag >= math.sqrt(2)/(3*math.pi)-1e-8
    carry = abs(endpoint)**2
    return {"N": N, "inverse_coefficient_l1": inverse_l1,
            "adapter_coefficient_l1": adapter_l1,
            "canonical_endpoint": [endpoint.real, endpoint.imag],
            "nonzero_endpoint_carry": carry,
            "scope": "Numerical diagnostics of direct all-level coefficient bounds."}


def main():
    exact = [exact_case(N) for N in range(2, 25)]
    complex_rows = [complex_case(N) for N in (2, 3, 4, 8, 16, 64, 256, 1024, 4096)]
    result = {"status": "PASS", "exact_cases": exact,
              "complex_bound_diagnostics": complex_rows,
              "scope": "Actual right-Euler M->qM adapter, affine central norm factors and nonzero endpoint carry. No selected geometric-period or volume bound."}
    Path(__file__).with_name("actual_euler_meridian_half_step_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_levels": len(exact),
                      "complex_diagnostics": len(complex_rows),
                      "last_endpoint": complex_rows[-1]["canonical_endpoint"]}))


if __name__ == "__main__":
    main()
