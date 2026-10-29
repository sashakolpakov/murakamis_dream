"""Exact full-matrix degree elevation and the actual head cut-Ward map."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from audit_endpoint_completed_normal_clock_euler import actual_arrows


def elev(C, p):
    N = len(C)
    out = np.zeros((N+1, N+1), dtype=np.int64)
    invN = pow(N, -1, p)
    for i in range(N+1):
        for j in range(N+1):
            a = (N-i)*int(C[i, j]) if i<N and j<N else 0
            b = i*int(C[i-1, j-1]) if i and j else 0
            out[i, j] = (a+b)*invN % p
    return out


def sl2(r):
    e = np.zeros((r+1, r+1), dtype=np.int64)
    f = np.zeros_like(e)
    h = np.diag([r-2*k for k in range(r+1)])
    for k in range(r+1):
        if k:
            e[k-1, k] = r-k+1
        if k<r:
            f[k+1, k] = k+1
    return e, f, h


def diagonal_inverse(a, p):
    return np.diag([pow(int(a[i, i]), -1, p) for i in range(len(a))])


def case(N, normal):
    p, q, Qjet, _, beta = actual_arrows(N, normal)
    Q = Qjet.x
    invN, invNp = pow(N, -1, p), pow(N+1, -1, p)
    old = np.eye(N, dtype=np.int64)
    K = np.diag([pow(q.x, N-1, p)*pow(Q, -j, p) % p for j in range(N)])
    Ki = diagonal_inverse(K, p)
    KF = np.diag([pow(Q, -j, p) for j in range(N+1)])
    KFi = diagonal_inverse(KF, p)
    F = np.zeros((N, N), dtype=np.int64)
    d = [1]
    for j in range(N-1):
        F[j+1, j] = (1-pow(Q, j+1, p)) % p
        d.append(d[-1]*(j+1)*pow(int(F[j+1, j]), -1, p) % p)
    D, Di = np.diag(d), np.diag([pow(x, -1, p) for x in d])
    s = min(1, N-1)
    b = [1]
    FF = np.zeros((N+1, N+1), dtype=np.int64)
    for j in range(N):
        FF[j+1, j] = beta[j, s].x
        b.append(b[-1]*int(FF[j+1, j])*pow(j+1, -1, p) % p)
    B, Bi = np.diag(b), np.diag([pow(x, -1, p) for x in b])
    Bh = np.zeros_like(K)
    Bf = np.zeros_like(KF)
    for i in range(N):
        for j in range(N):
            if i != j:
                Bh[i, j] = pow(N*(int(K[i, i])-int(K[j, j])), -1, p)
    for i in range(N+1):
        for j in range(N+1):
            if i != j and {i, j} != {0, N}:
                Bf[i, j] = pow((N+1)*(int(KF[i, i])-int(KF[j, j])), -1, p)

    def T(C):
        return B@elev(D@C@Di % p, p)@Bi % p

    eo, fo, ho = sl2(N-1)
    ef, ff, hf = sl2(N)
    assert np.array_equal(elev(old, p), np.eye(N+1, dtype=np.int64))
    identities = 0
    for i in range(N):
        for j in range(N):
            C = np.zeros((N, N), dtype=np.int64)
            C[i, j] = 1
            EC = elev(C, p)
            assert int(np.trace(EC))*invNp % p == int(np.trace(C))*invN % p
            assert int(EC.sum())*invNp % p == int(C.sum())*invN % p
            assert EC[0, N] == EC[N, 0] == 0
            for xo, xf in ((eo, ef), (fo, ff), (ho, hf)):
                assert np.array_equal(elev(xo@C-C@xo, p), (xf@EC-EC@xf) % p)
            for t, u in ((1, 1), (2, 3), (3, 4)):
                po = np.array([pow(t, k, p) for k in range(N)], dtype=np.int64)
                lo = np.array([math.comb(N-1, k)*pow(u, k, p) % p for k in range(N)])
                pf = np.array([pow(t, k, p) for k in range(N+1)], dtype=np.int64)
                lf = np.array([math.comb(N, k)*pow(u, k, p) % p for k in range(N+1)])
                assert int(lf@EC@pf) % p == (1+t*u)*int(lo@C@po) % p
            TC = T(C)
            dk = (K@C@Ki-C) % p
            assert np.array_equal(T(dk), (KF@TC@KFi-TC) % p)
            assert np.array_equal(T(F@C-C@F), (FF@TC-TC@FF) % p)
            hopf = F@C-Ki@C@K@F
            rhs = FF@TC-TC@FF+T(Ki@dk@K@F)
            assert np.array_equal(T(hopf), rhs % p)
            difference = int(C.sum())*invN-int(TC.sum())*invNp
            homotopy = -int(np.trace(Bh@(K@C-C@K)))+int(np.trace(Bf@(KF@TC-TC@KF)))
            assert difference % p == homotopy % p
            identities += 1
    return {"N": N, "root": normal, "matrix_units": identities,
            "actual_whole_Fr_string": s}


def main():
    cases = [case(N, normal) for N in range(2, 9) for normal in (False, True)]
    P = np.diag([1, 0])
    EP = elev(P, 1009)
    assert not np.array_equal(EP@EP % 1009, EP)
    result = {"status": "pass", "cases": cases,
              "scope": "exact cut-current map and source homotopy; not an R algebra map"}
    path = Path(__file__).with_name("degree_elevation_actual_head_ward_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(cases),
                      "matrix_units": sum(c["matrix_units"] for c in cases),
                      "results": str(path)}, indent=2))


if __name__ == "__main__":
    main()
