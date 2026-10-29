"""Exact first normal high-color R: resonant factor and Frobenius PBW degree."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_crossing_normal_spectra import J


def root_field(N):
    p = 1000
    while True:
        p = int(sp.nextprime(p))
        if (p - 1) % (4 * N) == 0:
            break
    g = int(sp.primitive_root(p))
    eta = pow(g, (p - 1) // (4 * N), p)
    return p, eta


def gauge(N, index):
    a, s = divmod(index, N)
    return (-1) ** (N * a * (a - 1) // 2 + a * s)


def setup(N, r):
    p, eta0 = root_field(N)
    J.p = p
    eta = J(eta0, -eta0 * pow(4 * N, -1, p))
    q = eta**2
    Q, rho = q**2, q - q**-1
    m = N * (r + 1) - 1
    G = [[J() for _ in range(m + 1)] for _ in range(m + 1)]
    G[0][0] = J(1)
    for a in range(1, m + 1):
        G[a][0] = G[a][a] = J(1)
        for k in range(1, a):
            G[a][k] = G[a - 1][k] + Q**(a - k) * G[a - 1][k - 1]
    fac = [J(1)]
    for k in range(1, m + 1):
        fac.append(fac[-1] * (q**k - q**-k) / rho)

    def coefficient(i, j, k, negative=False):
        if negative:
            if not (0 <= k <= j and i + k <= m):
                return J()
            ge = q**(-k * (m - j)) * G[m - j + k][k]
            gf = q**(-k * i) * G[i + k][k]
            value = (-1)**k * q**(-k * (k - 1) // 2)
            value *= rho**k * fac[k] * ge * gf
            value *= eta**(-(m - 2 * i) * (m - 2 * j))
            value *= gauge(N, i) * gauge(N, j)
            value *= gauge(N, j - k) * gauge(N, i + k)
            return value
        if not (0 <= k <= i and j + k <= m):
            return J()
        ge = q**(-k * (m - i)) * G[m - i + k][k]
        gf = q**(-k * j) * G[j + k][k]
        value = q**(k * (k - 1) // 2) * rho**k * fac[k] * ge * gf
        a, b = i - k, j + k
        value *= eta**((m - 2 * a) * (m - 2 * b))
        value *= gauge(N, i) * gauge(N, j) * gauge(N, a) * gauge(N, b)
        return value

    return p, m, coefficient


def generators(r, p):
    size = r + 1
    e = np.zeros((size, size), dtype=np.int64)
    f = np.zeros_like(e)
    h = np.diag([r - 2 * k for k in range(size)]).astype(np.int64)
    for k in range(size):
        if k:
            e[k - 1, k] = r - k + 1
        if k < r:
            f[k + 1, k] = k + 1
    eye = np.eye(size, dtype=np.int64)
    return [np.kron(a, eye) % p for a in (e, f, h)] + [
        np.kron(eye, a) % p for a in (e, f, h)]


def span_test(vectors, p):
    # Obtain exact independent original columns and pivot rows once.
    independent, pivots, echelon = [], [], []
    for index, original in enumerate(vectors):
        v = original.copy() % p
        for pivot, old in zip(pivots, echelon):
            v = (v - int(v[pivot]) * old) % p
        nz = np.flatnonzero(v)
        if not len(nz):
            continue
        pivot = int(nz[0])
        v = v * pow(int(v[pivot]), -1, p) % p
        independent.append(index)
        pivots.append(pivot)
        echelon.append(v)
    full = np.column_stack([vectors[i] for i in independent]) % p
    inverse = np.array(sp.Matrix(full[pivots, :].tolist()).inv_mod(p)).astype(np.int64)

    def contains(v):
        c = inverse @ v[pivots] % p
        return np.array_equal(full @ c % p, v % p)

    return contains, len(independent)


def audit_case(N, r):
    p, m, coeff = setup(N, r)
    size = (r + 1)**2
    eye = np.eye(size, dtype=np.int64)
    gs = generators(r, p)
    degree1 = [eye.reshape(-1)] + [a.reshape(-1) for a in gs]
    degree2 = degree1 + [(a @ b % p).reshape(-1) for a in gs for b in gs]
    in1, rank1 = span_test(degree1, p)
    in2, rank2 = span_test(degree2, p)
    blocks = {}
    tail_checks = 0
    tau = (-1)**(N * r - 1)
    kappa = N * (-1)**(N - 1)
    epsilon = (-1)**m
    for i in range(m + 1):
        a, s = divmod(i, N)
        for j in range(m + 1):
            b, t = divmod(j, N)
            for k in range(min(i, m - j) + 1):
                value = coeff(i, j, k)
                outi, outj = i - k, j + k
                oa, os = divmod(outi, N)
                ob, ot = divmod(outj, N)
                if k >= 2 * N:
                    assert value == J()
                if k >= N:
                    expected = 0
                    if i >= N and j + N <= m:
                        expected = kappa * tau * (r - a + 1) * (b + 1)
                        expected *= coeff(i - N, j + N, k - N).x
                    assert value.dx == expected % p, (N, r, i, j, k)
                    tail_checks += 1
                if value.dx:
                    key = (os, ot, s, t)
                    if key not in blocks:
                        blocks[key] = np.zeros((size, size), dtype=np.int64)
                    sign = epsilon**(oa + ob)
                    blocks[key][oa * (r + 1) + ob, a * (r + 1) + b] += sign * value.dx
                    blocks[key] %= p
    nonlinear = 0
    for block in blocks.values():
        v = block.reshape(-1)
        assert in2(v), (N, r, "outside degree two")
        if not in1(v):
            nonlinear += 1
    assert nonlinear > 0
    return {"N": N, "r": r, "prime": p, "head_blocks": len(blocks),
            "PBW_degree1_span": rank1, "PBW_degree2_span": rank2,
            "degree2_necessary_blocks": nonlinear,
            "resonant_tail_coefficients": tail_checks}


def main():
    cases = [audit_case(N, r) for N, r in ((2, 3), (3, 3), (4, 4), (5, 3))]
    output = Path(__file__).with_name("high_color_first_normal_r_degree_results.json")
    output.write_text(json.dumps({"status": "pass", "cases": cases,
                                "scope": "actual first normal R only; no whole current-map assertion"},
                                indent=2) + "\n")
    print(json.dumps({"status": "pass", "cases": len(cases),
                      "head_blocks": sum(x["head_blocks"] for x in cases),
                      "tail_coefficients": sum(x["resonant_tail_coefficients"] for x in cases),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()

