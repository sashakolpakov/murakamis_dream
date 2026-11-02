#!/usr/bin/env python3
"""Bounded exact checks of the quarter-source recurrence and transport identities.

Finite fields compare the literal quantum factorial sum with its stated
recurrence and both terminal walls. Independent rational matrices check
backward conjugation and reconstruction with both source components.
No analytic bound or all-level conclusion is inferred from these tests.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path

PAPER = Path(__file__).resolve().parent
ROOT = PAPER.parents[1]
INPUTS = [
    "papers/quarter-index-asymptotics/main.tex",
    "papers/quarter-index-asymptotics/transport.tex",
    "papers/quarter-index-asymptotics/source.tex",
    "papers/quarter-index-asymptotics/signed.tex",
    "papers/quarter-index-asymptotics/figures/quarter-action.tex",
    "papers/quarter-index-asymptotics/check.py",
    "papers/conway-asymptotics/factorial.tex",
    "papers/conway-asymptotics/leaf.tex",
    "papers/newton-tangles/main.tex",
]


def hashes():
    return {s: hashlib.sha256((ROOT / s).read_bytes()).hexdigest()
            for s in INPUTS}


def roots(order):
    ans, k = [], 1
    while len(ans) < 2:
        p = order*k+1
        if all(p % j for j in range(2, isqrt(p)+1)):
            for a in range(2, p):
                q = pow(a, k, p)
                if pow(q, order, p) == 1 and all(
                        pow(q, j, p) != 1 for j in range(1, order)):
                    ans.append((p, q))
                    break
        k += 1
    return ans


def source_case(N, p, q):
    Q = q*q % p
    M = (N-1)//2
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, p)) % p)

    def src(h, r):
        value = 0
        for v in range(r, M+1):
            den = fac[v]*fac[v-h]*fac[v+h]*fac[v-r] % p
            value += pow(Q, -v*r, p)*fac[2*v]*pow(den, -1, p)
        D = (pow(Q, -r*r, p)*fac[2*r] *
             pow(fac[r]*fac[r-h]*fac[r+h] % p, -1, p)) % p
        assert D
        return value*pow(D, -1, p) % p

    def coeff(h, r):
        Y, H = pow(Q, r, p), pow(Q, h, p)
        def den(Y):
            return (1-Q*Y*pow(H, -1, p))*(1-Q*Y*H) % p
        pp = (-pow(Q, -2, p)*pow(Y, -1, p) *
              ((H+pow(H, -1, p))*pow(Q, 3, p)*Y*Y+Q+1) *
              pow(den(Y), -1, p)) % p
        qq = (-pow(Q, -4, p)*pow(Y, -2, p) *
              (1-Q*Q*Y)*(1-pow(Q, 3, p)*Y*Y)*(1+Q*Q*Y) *
              pow(den(Y)*den(Q*Y % p) % p, -1, p)) % p
        return pp, qq

    tested = []
    for h in range(3):
        for r in range(max(h, N//4-1), min(M-2, N//4+1)+1):
            pp, qq = coeff(h, r)
            assert src(h, r) == (pp*src(h, r+1)+qq*src(h, r+2)) % p
            tested.append([h, r])
        pp, qq = coeff(h, M-1)
        assert qq == 0 and src(h, M) == 1 and src(h, M-1) == pp
    return {"level": N, "prime": p, "recurrence_positions": tested,
            "terminal_colors": 3, "parity": N % 2}


def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]


def neg(A):
    return [[-x for x in row] for row in A]


def sub(A, B):
    return add(A, neg(B))


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def inv(A):
    d = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d
    return [[A[1][1]/d, -A[0][1]/d],
            [-A[1][0]/d, A[0][0]/d]]


I = [[F(1), F(0)], [F(0), F(1)]]


def model(x, e):
    D = [[1+x, F(0)], [F(0), 3+2*x]]
    R = [[F(0), e*(1+x*x)], [e*(2-x), F(0)]]
    gap = D[0][0]-D[1][1]
    X = [[F(0), -R[0][1]/gap], [R[1][0]/gap, F(0)]]
    return D, R, X


def matrix_cases():
    one_steps = 0
    for e in (F(1, 20), F(1, 37), F(1, 100)):
        for x in (F(-1, 5), F(0), F(1, 7), F(1, 3)):
            D, R, X = model(x, e)
            Xp = model(x+e, e)[2]
            direct = mul(mul(inv(add(I, X)), add(D, R)), add(I, Xp))
            correction = mul(inv(add(I, X)),
                             add(mul(D, sub(Xp, X)), mul(R, Xp)))
            assert direct == add(D, correction)
            assert add(sub(mul(D, X), mul(X, D)), R) == [[0, 0], [0, 0]]
            one_steps += 1
    # Direct backward products versus anchored interaction reconstruction.
    # These matrices need not be small: this checks the exact identities.
    products = 0
    for count in (2, 3, 5, 8):
        Ds, Rs = [], []
        for j in range(count):
            D, R, _ = model(F(j, 10), F(1, 13))
            Ds.append(D)
            Rs.append(R)
        G = [None]*(count+1)
        G[-1] = I
        for j in reversed(range(count)):
            G[j] = mul(Ds[j], G[j+1])
        direct = I
        interaction = I
        for j in range(count):
            direct = mul(direct, add(Ds[j], Rs[j]))
            E = mul(mul(inv(G[j]), Rs[j]), G[j+1])
            interaction = mul(interaction, add(I, E))
        reconstructed = mul(G[0], interaction)
        assert direct == reconstructed
        for a, b in ((F(1), F(1, 9)), (F(2, 3), F(-5, 7))):
            A = [[a, F(0)], [b, F(0)]]
            assert mul(direct, A) == mul(reconstructed, A)
        products += 1
    return {"one_step_identities": one_steps,
            "two_channel_products": products,
            "nonzero_two_channel_inputs": 2*products}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PAPER / "build" / "check")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    record = out / "summary.json"
    record.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Run without -O: assertions are required")
    before = hashes()
    sources = [source_case(N, p, q) for N in range(8, 25)
               for p, q in roots(2*N)]
    matrix = matrix_cases()
    after = hashes()
    if before != after:
        raise RuntimeError("Source changed while checking")
    result = {
        "verified": True,
        "scope": [
            "literal finite factorial source versus rational recurrence",
            "both parity terminal walls with all source factors retained",
            "exact backward conjugation with its shifted right basis",
            "two-channel ordered interaction reconstruction",
        ],
        "excluded": [
            "analytic estimates from finite samples",
            "global source dominance or whole filling estimates",
            "a numerical verification of the quantum asymptotic",
        ],
        "level_prime_cases": len(sources),
        "recurrence_positions": sum(len(s["recurrence_positions"]) for s in sources),
        "terminal_wall_cases": sum(s["terminal_colors"] for s in sources),
        "rational_matrices": matrix,
        "records": sources,
        "input_hashes": before,
    }
    record.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: result[k] for k in
                      ("verified", "level_prime_cases", "recurrence_positions",
                       "terminal_wall_cases", "rational_matrices")}, indent=2))
    print(record)


if __name__ == "__main__":
    main()
