#!/usr/bin/env python3
"""Actual gauge period: exact two-period recursion and selected point 2.

The finite-field tests check exact sources. Numerical moment limits
are diagnostics of the direct all-level proof, not knot-volume tests.
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
    coefficients = [sum(v[r]*v[k-r]*pow(Q, k-r, p) for r in range(k+1)) % p for k in range(N)]
    moments = list(reversed(coefficients))+[0]*(N+3)
    top = moments[0]
    H, R = [1, (1+Q) % p], [0, -2*Q % p]
    for m in range(2*N+1):
        factor = (pow(Q, m+2, p)-Q) % p
        H.append(((1+Q)*H[-1]+factor*H[-2]) % p)
        R.append(((1+Q)*R[-1]+factor*R[-2]) % p)
    checked = 0
    for m in range(N+2):
        assert moments[m] == (H[m]*top+R[m]*pow(N, -1, p)) % p
        assert (moments[m+2]-(1+Q)*moments[m+1]
                +(Q-pow(Q, m+2, p))*moments[m]) % p == 0
        checked += 1
    cyclic = moments[:N]
    for m in range(N):
        residual = (cyclic[(m+2) % N]-(1+Q)*cyclic[(m+1) % N]
                    +(Q-pow(Q, m+2, p))*cyclic[m]) % p
        expected = ((top if m == N-2 else 0)
                    +(-2*Q*pow(N, -1, p) if m == N-1 else 0)) % p
        assert residual == expected

    def mm(A, B):
        return [[sum(A[i][k]*B[k][j] for k in range(2)) % p
                 for j in range(2)] for i in range(2)]

    for X in (0, 1, 2, 3, 5):
        monodromy = [[1, 0], [0, 1]]
        for m in range(N):
            point = X*pow(Q, m, p) % p
            companion = [[0, 1], [-Q*(1-Q*point) % p, (1+Q) % p]]
            monodromy = mm(companion, monodromy)
        assert (monodromy[0][0]+monodromy[1][1]) % p == 2
        assert (monodromy[0][0]*monodromy[1][1]-monodromy[0][1]*monodromy[1][0]) % p == (1-pow(X, N, p)) % p
        if X == 1:
            vector = [moments[0], moments[1]]
            assert any(vector)
            assert not any(sum(monodromy[i][j]*vector[j] for j in range(2)) % p for i in range(2))

    inverse = [pow(coefficients[0], -1, p)]
    for k in range(1, N):
        inverse.append(-sum(coefficients[j]*inverse[k-j] for j in range(1, k+1)) % p)
    meridian_cases = 0
    for r in range(-3, 4):
        shifted = [coefficient*pow(q, r*k, p) % p for k, coefficient in enumerate(coefficients)]
        increment = [sum(shifted[j]*inverse[k-j] for j in range(k+1)) % p for k in range(N)]
        restored = [sum(increment[j]*coefficients[k-j] for j in range(k+1)) % p for k in range(N)]
        assert restored == shifted
        for degree in range(min(5, N)):
            assert restored[N-1-degree] == pow(q, r*(N-1-degree), p)*moments[degree] % p
            meridian_cases += 1
    return {"N": N, "field": p, "exact_moments": checked,
            "retained_cyclic_source_rows": 2, "norm_curve_cases": 5,
            "exact_ordered_meridian_periods": meridian_cases}


def diagnostic(N):
    with mp.workdps(80):
        Q = mp.exp(2j*mp.pi/N)
        gauss = sum((-1)**r*Q**(r*(r-1)//2) for r in range(N))
        c = gauss/N
        H, R = [mp.mpc(1), 1+Q], [mp.mpc(0), -2*Q]
        for m in range(7):
            factor = Q**(m+2)-Q
            H.append((1+Q)*H[-1]+factor*H[-2])
            R.append((1+Q)*R[-1]+factor*R[-2])
        rows = []
        # Independent coefficient reflection, not the moment recurrence.
        for m in range(7):
            moment = mp.mpc(0)
            for r in range(N-m):
                product = mp.mpc(1)
                for a in range(m):
                    product *= 1-Q**(r+1+a)
                moment += (-1)**r*Q**(r*(r-1)//2)*product/N
            assert abs(moment-(H[m]*c+R[m]/N)) < mp.mpf('1e-65')
            rows.append({"degree": m, "algebraic_value": 2**m,
                         "normalized_error": float(abs(moment/c-2**m)),
                         "sqrt_N_times_error": float(mp.sqrt(N)*abs(moment/c-2**m))})
        # Fixed Ore observable (z+1)T+(z^2-2)T^-1+3 has
        # classical value -2 at the selected point (z,T)=(2,-1).
        moments = [H[m]*c+R[m]/N for m in range(3)]
        q = mp.exp(1j*mp.pi/N)
        terms = [(1, 1, 1), (1, 0, 1), (-1, 2, 1), (-1, 0, -2), (0, 0, 3)]
        ore_period = sum(coefficient*q**(shift*(N-1-degree))*moments[degree]
                         for shift, degree, coefficient in terms)
        return {"N": N, "moments": rows,
                "fixed_Ore_symbol_value": -2,
                "fixed_Ore_character_error": float(abs(ore_period/c+2)),
                "scope": "Diagnostic of the proved fixed-degree period limit."}


def main():
    exact = [exact_case(N) for N in range(2, 25)]
    samples = [diagnostic(N) for N in (32, 64, 128, 256)]
    result = {"status": "PASS", "exact_cases": exact,
              "fixed_observable_diagnostics": samples,
              "scope": "Actual local gauge coefficient-period selection of z=2 only. No identification with a knot meridian or geometric knot A-period."}
    Path(__file__).with_name("actual_gauge_critical_evaluation_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_levels": len(exact),
                      "exact_moments": sum(r["exact_moments"] for r in exact),
                      "exact_norm_curve_cases": sum(r["norm_curve_cases"] for r in exact),
                      "exact_ordered_meridian_periods": sum(r["exact_ordered_meridian_periods"] for r in exact),
                      "diagnostic_levels": len(samples)}))


if __name__ == "__main__":
    main()
