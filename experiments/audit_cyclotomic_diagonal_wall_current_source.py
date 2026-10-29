"""Exact audit of the actual cyclotomic wall source and compensated ladder."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from audit_crossing_normal_spectra import J
from audit_high_color_first_normal_r_degree import gauge, root_field, setup


def equal(a, b, p):
    assert np.array_equal(a % p, b % p)


def gaussians(size, Q, p):
    rows = [[1]]
    for a in range(1, size + 1):
        old = rows[-1]
        row = [1] + [0] * (a - 1) + [1]
        for k in range(1, a):
            row[k] = (old[k] + pow(Q, a-k, p) * old[k-1]) % p
        rows.append(row)
    return rows


def audit_color(N):
    p, eta = root_field(N)
    q, Q = pow(eta, 2, p), pow(eta, 4, p)
    rho = (q-pow(q, -1, p)) % p
    size = N * (N+1)
    m = size-1
    rows = gaussians(m, Q, p)
    eye = np.eye(size, dtype=np.int64)
    en = np.eye(N, dtype=np.int64)
    ef = np.zeros((N+1, N+1), dtype=np.int64)
    ff = np.zeros_like(ef)
    hf = np.diag([N-2*R for R in range(N+1)]).astype(np.int64)
    for R in range(N+1):
        if R:
            ef[R-1, R] = N-R+1
        if R<N:
            ff[R+1, R] = R+1
    V = np.zeros((N, N), dtype=np.int64)
    for S in range(N):
        V[(S+1) % N, S] = 1
    D = np.zeros((N, N), dtype=np.int64)
    for S in range(1, N):
        bracket = (pow(q, S, p)-pow(q, -S, p))*pow(rho, -1, p) % p
        D[S, S] = pow(bracket, -1, p)

    def divided(d, raising):
        a = np.zeros((size, size), dtype=np.int64)
        for i in range(size):
            out = i-d if raising else i+d
            if not 0 <= out < size:
                continue
            top = m-i+d if raising else i+d
            exponent = -d*(m-i) if raising else -d*i
            a[out, i] = (pow(q, exponent, p)*rows[top][d]
                         * gauge(N, i)*gauge(N, out)) % p
        return a

    # Normal entries are evaluated in the original integral matrices,
    # rather than supplied from the claimed tensor formulas.
    J.p = p
    qjet = J(q, -q*pow(2*N, -1, p))
    rhojet = qjet-qjet**-1
    Ec = np.zeros((size, size), dtype=np.int64)
    Fc = np.zeros_like(Ec)
    for i in range(size):
        R, S = divmod(i, N)
        if S == 0 and R:
            v = (qjet**(m-i+1)-qjet**(-(m-i+1)))/rhojet
            v *= gauge(N, i)*gauge(N, i-1)
            assert not v.x
            Ec[i-1, i] = v.dx
        if S == N-1 and R<N:
            v = (qjet**(i+1)-qjet**(-(i+1)))/rhojet
            v *= gauge(N, i)*gauge(N, i+1)
            assert not v.x
            Fc[i+1, i] = v.dx
    Ed = divided(N+1, True)
    Fd = divided(N+1, False)
    Et = (Ed @ np.kron(np.eye(N+1, dtype=np.int64), D)
          +rho*(-1)**(N+1)*Ec) % p
    Ft = (-np.kron(np.eye(N+1, dtype=np.int64), D) @ Fd+rho*Fc) % p
    Et_expected, Ft_expected = np.kron(ef, V.T), np.kron(ff, V)
    equal(Et, Et_expected, p)
    equal(Ft, Ft_expected, p)
    equal(Et@Ft-Ft@Et, np.kron(hf, en), p)

    G = np.zeros((size, size), dtype=np.int64)
    selected = []
    for R in range(N+1):
        for S in range(N):
            G[R*N+(S+R) % N, R*N+S] = 1
        selected.append(R*N+R % N)
    P = np.zeros_like(G)
    for i in selected:
        P[i, i] = 1
    P0 = np.zeros_like(en)
    P0[0, 0] = 1
    equal(G@np.kron(ef, en)@G.T, Et, p)
    equal(G@np.kron(ff, en)@G.T, Ft, p)
    equal(G@np.kron(np.eye(N+1, dtype=np.int64), P0)@G.T, P, p)
    equal(P@Et, Et@P, p)
    equal(P@Ft, Ft@P, p)
    A = np.diag([pow(Q, i % N, p) for i in range(size)])
    B = np.diag([pow(Q, i//N, p) for i in range(size)])
    Binv = np.diag([pow(Q, -(i//N), p) for i in range(size)])
    equal(G@A@G.T, Binv@A, p)
    equal(G@B@G.T, B, p)

    invN, inv2N = pow(N, -1, p), pow(pow(2, N, p), -1, p)
    lam = np.array([math.comb(N, R)*inv2N % p for R in range(N+1)],
                   dtype=np.int64)
    eplus = np.ones((N+1, 1), dtype=np.int64)@lam[None, :]
    ehead = np.ones((N, N), dtype=np.int64)*invN % p
    eprod = np.kron(eplus, ehead) % p
    ed = N*P@eprod@P % p
    equal(ed, G@np.kron(eplus, P0)@G.T, p)
    equal(ed@ed, ed, p)
    assert int(np.trace(ed)) % p == 1
    assert int(np.trace(eprod@P)) % p == invN
    # The full source, including its n=N endpoint, is tested entrywise.
    for j in range(N+1):
        ins = np.zeros_like(P)
        if j < N:
            for R in range(N+1):
                ins[R*N+j, R*N+j] = 1
        if j == 0:
            ins[N*N:, N*N:] -= en
        if j == N:
            ins[N*N:, N*N:] += en
        actual = invN*int(np.trace(ed@ins)) % p
        assert actual == invN*lam[j] % p

    # One-sided and compressed source difference: exact all-matrix
    # Cartan co-boundary, with no diagonal discarded.
    delta = (N*eprod@P-ed) % p
    assert not np.diag(delta).any()
    b = np.zeros_like(delta)
    for i in range(size):
        for j in range(size):
            if i != j and delta[i, j]:
                b[i, j] = int(delta[i, j])*pow(i-j, -1, p) % p
    pos = np.diag(np.arange(size, dtype=np.int64))
    equal(pos@b-b@pos, delta, p)

    # Both source-gauge steps are checked independently.
    Fourier = np.array([[pow(Q, S*T, p)*invN % p for T in range(N)]
                        for S in range(N)], dtype=np.int64)
    Fourier_inv = np.array([[pow(Q, -S*T, p) for T in range(N)]
                            for S in range(N)], dtype=np.int64)
    H0 = G@np.kron(np.eye(N+1, dtype=np.int64), Fourier) % p
    H0inv = np.kron(np.eye(N+1, dtype=np.int64), Fourier_inv)@G.T % p
    equal(H0@H0inv, eye, p)
    equal(H0@eprod@H0inv, ed, p)
    av = np.ones(N+1, dtype=np.int64)*pow(N+1, -1, p) % p
    correction = np.ones((N+1, 1), dtype=np.int64)@(av-lam)[None, :] % p
    KF = (np.eye(N+1, dtype=np.int64)+correction) % p
    KFinv = (np.eye(N+1, dtype=np.int64)-correction) % p
    equal(correction@correction, np.zeros_like(correction), p)
    equal(KF@(np.ones((N+1, 1), dtype=np.int64)@av[None, :])@KFinv,
          eplus, p)
    return {"N": N, "prime": p, "high_dimension": size,
            "selected_dimension": N+1, "wall_basis_checks": N+1}


def audit_crossing(N):
    p, m, coefficient = setup(N, N)
    _, eta = root_field(N)
    i, j, k = N, N*(N-1), 1
    value = coefficient(i, j, k)
    outi, outj = i-k, j+k
    expected = (-1)**(N+1)*N*pow(eta, (m-2*outi)*(m-2*outj), p) % p
    assert value.x == 0 and value.dx == expected and value.dx != 0
    counts = {"root_entries": 0, "normal_entries": 0,
              "charged_normal_entries": 0}
    for i in range(m+1):
        R, S = divmod(i, N)
        for j in range(m+1):
            U, T = divmod(j, N)
            for k in range(min(i, m-j)+1):
                val = coefficient(i, j, k)
                Ro, So = divmod(i-k, N)
                Uo, To = divmod(j+k, N)
                dR = Ro+Uo-R-U
                assert dR in (-1, 0, 1)
                assert So+To-S-T == -N*dR
                if val.x:
                    assert dR == 0
                    counts["root_entries"] += 1
                if val.dx:
                    counts["normal_entries"] += 1
                    if dR:
                        counts["charged_normal_entries"] += 1
    assert counts["charged_normal_entries"] > 0
    return {"N": N, "prime": p, "explicit_charged_entry": expected, **counts}


def main():
    colors = [audit_color(N) for N in range(2, 9)]
    crossings = [audit_crossing(N) for N in range(2, 6)]
    output = Path(__file__).with_name("cyclotomic_diagonal_wall_current_source_results.json")
    result = {"status": "pass", "color_cases": colors,
              "actual_crossing_cases": crossings,
              "scope": "exact actual finite source/ladder and charged jets; no geometric pushforward"}
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "color_cases": len(colors),
                      "actual_crossing_cases": len(crossings),
                      "charged_normal_entries": sum(c["charged_normal_entries"] for c in crossings),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
