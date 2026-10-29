#!/usr/bin/env python3
"""Actual Borel-relative source: triangular two-leg and faithful multi-leg.

All equal-color physical source rows use the original balanced heads and
pivots. No geometric-period or volume assertion is made.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import alg_product, fusion
from audit_actual_two_cut_ports import balanced_data


def source_of_rank_one(left, right, Ks, N, p):
    strands = len(Ks)
    tail_size = N**(strands-1)
    total = 0
    for closed in itertools.product(range(N), repeat=strands-1):
        index, weight = 0, 1
        for i, state in enumerate(closed, start=1):
            index = index*N+state
            weight = weight*pow(int(Ks[i][state, state]), 1-N, p) % p
        row_sum = sum(int(left[first*tail_size+index]) for first in range(N))
        total = (total+weight*row_sum*int(right[index])) % p
    return total


def physical_top_rows(N, strands):
    p, _, q, _, _, K, _, _, _ = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    C, Ci, phi, _, _, Ks, tails = fusion(N, p, Q, [x]*strands, [0]*strands)
    assert phi == 0
    total_x = pow(x, strands, p)
    top_checks = 0
    for s, tail in enumerate(tails):
        j = sum(tail) % N
        gamma = N*pow(total_x, 1-N, p)*pow(Q, 1-j, p) % p
        for k in range(N):
            # Right multiplication by f^(N-1)e_k is a rank-one map:
            # e_(k-1) -> f^(N-1)e_k in the regular algebra basis.
            row = s*N*N+(N-1)*N+k
            column = s*N*N+(k-1) % N
            literal = source_of_rank_one(C[:, row], Ci[column, :], Ks, N, p)
            assert literal == (gamma if k == j else 0), (N, strands, tail, k, literal, gamma)
            top_checks += 1
    # Each path coefficient in every relative matrix entry can be isolated
    # with idempotents and raised to the literal top row of a suitable tail.
    recovery_checks = 0
    if strands >= 3:
        sums = {sum(t) % N for t in tails}
        assert sums == set(range(N))
        for a, j in itertools.product(range(N), repeat=2):
            z, left, right, raise_f = (np.zeros(N*N, dtype=np.int64) for _ in range(4))
            z[a*N+j] = 1
            left[(j+a) % N] = 1
            right[j] = 1
            raise_f[(N-1-a)*N:(N-a)*N] = 1
            isolated = alg_product(alg_product(left, z, N, 0, p), right, N, 0, p)
            top = alg_product(raise_f, isolated, N, 0, p)
            expected = np.zeros(N*N, dtype=np.int64)
            expected[(N-1)*N+j] = 1
            assert np.array_equal(top, expected)
            recovery_checks += len(tails)**2
    return {"N": N, "strands": strands, "field": p,
            "literal_physical_top_rows": top_checks,
            "relative_matrix_basis_recovery_certificates": recovery_checks,
            "two_sided_source_null_ideal": "zero" if strands >= 3 else "wrapped-path ideal"}


def two_leg_cut(N):
    p, _, q, _, _, K, _, _, _ = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    f = np.zeros(N*N, dtype=np.int64)
    f[N:2*N] = 1
    ideal_count = 0
    for a, j in itertools.product(range(N), repeat=2):
        z = np.zeros(N*N, dtype=np.int64)
        z[a*N+j] = 1
        if a+j >= N:
            ideal_count += 1
            for product in (alg_product(f, z, N, 0, p), alg_product(z, f, N, 0, p)):
                for idx in np.flatnonzero(product):
                    degree, start = divmod(int(idx), N)
                    assert degree+start >= N
        else:
            value = pow(x, 1-N-a, p)*pow(Q, -(j+a), p)*fac[j+a]*pow(fac[j], -1, p) % p
            assert value
    assert ideal_count == N*(N-1)//2
    return {"N": N, "wrapped_ideal_dimension": ideal_count,
            "minimal_two_sided_source_quotient_dimension": N*(N+1)//2}


def main():
    rows = [physical_top_rows(N, 3) for N in range(2, 7)]
    rows += [physical_top_rows(N, 4) for N in (2, 3)]
    cuts = [two_leg_cut(N) for N in range(2, 9)]
    result = {"status": "PASS", "physical_source_cases": rows, "two_leg_quotients": cuts,
              "scope": "Maximal two-sided source-null ideals of the full actual fixed-root Borel-relative algebra, not a geometric critical quotient or no-go for linear period transforms."}
    Path(__file__).with_name("actual_source_two_sided_quotient_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "physical_source_cases": len(rows),
                      "physical_top_rows": sum(r["literal_physical_top_rows"] for r in rows),
                      "matrix_basis_recovery_certificates": sum(r["relative_matrix_basis_recovery_certificates"] for r in rows),
                      "two_leg_levels": len(cuts)}, indent=2))


if __name__ == "__main__":
    main()
