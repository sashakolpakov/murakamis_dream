#!/usr/bin/env python3
"""Exact actual fusion kernel and right-Euler/physical-clock relation.

Keeps nilpotent endpoints. The generic-Q check is only a finite kernel
identity, not a generic-Q word or normal-source comparison.
"""

import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import fusion, right_regular
from audit_actual_two_cut_ports import balanced_data


def factorial_kernel(N, p, Q, x):
    fs = [1]
    for a in range(1, N):
        fs.append(fs[-1]*(1-pow(Q, a, p)) % p)
    C = np.zeros((N*N, N*N), dtype=np.int64)
    for a in range(N):
        for j in range(N):
            for u in range(a+1):
                v = j+a-u
                if v < N:
                    C[u*N+v, a*N+j] = (pow(x, u-a, p)*fs[a]*fs[v]
                        *pow(fs[a-u], -1, p)*pow(fs[j], -1, p)) % p
    return C


def check(N, p, Q, root):
    x, y = 3, 7
    C = factorial_kernel(N, p, Q, x)
    I = np.eye(N*N, dtype=np.int64)
    Da = np.diag([pow(Q, a, p) for a in range(N) for _ in range(N)])
    Dj = np.diag([pow(Q, j, p) for _ in range(N) for j in range(N)])
    Ui = np.diag([pow(Q, -a, p) for a in range(N) for _ in range(N)])
    f = np.zeros(N*N, dtype=np.int64)
    f[N:2*N] = 1
    Rf = right_regular(f, N, 0, p)
    top = np.diag([int(a == N-1) for a in range(N) for _ in range(N)])
    lhs = x*(C@Rf-Q*Ui@C@Rf@Da) % p
    bulk = C@(I-Q*Da)@(I-Dj) % p
    endpoint = (1-pow(Q, N, p))*C@(I-Dj)@top % p
    assert np.array_equal(lhs, (bulk-endpoint) % p)
    assert np.array_equal(C@Da@Dj % p, Da@Dj@C % p)
    record = {"N": N, "field": p, "Q": Q, "root": root,
              "kernel_units": N**4, "endpoint_defect_nonzero": bool(endpoint.any())}
    if root:
        literal, Ci, phi, _, _, _, _ = fusion(N, p, Q, [x, y], [0, 0])
        assert phi == 0 and np.array_equal(C, literal)
        A, J, fR = (C@B@Ci % p for B in (Da, Dj, Rf))
        defect = (I-Ui@A) % p
        assert np.array_equal(x*defect@fR % p, (I-Q*A)@(I-J) % p)
        assert np.array_equal(A@J % p, Da@Dj % p)
        assert np.array_equal(A@fR % p, Q*fR@A % p)
        assert np.array_equal(J@fR % p, pow(Q, -1, p)*fR@J % p)
        power = I.copy()
        for _ in range(N):
            power = power@defect % p
        assert not power.any()
        assert not endpoint.any()
        record["root_nilpotent_denominator_checked"] = True
    else:
        assert endpoint.any()
    return record


def main():
    rows = []
    for N in range(2, 10):
        p, _, q, *_ = balanced_data(N)
        rows.append(check(N, p, q*q % p, True))
        rows.append(check(N, 1009, 2, False))
    result = {"status": "PASS", "cases": rows,
              "scope": "Actual root-fusion right-Euler clock identity, nilpotent denominator and truncated generic-Q endpoint defect; no geometric selection."}
    Path(__file__).with_name("actual_fusion_right_euler_clock_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "root_cases": len(rows)//2,
                      "generic_kernel_cases": len(rows)//2}))


if __name__ == "__main__":
    main()
