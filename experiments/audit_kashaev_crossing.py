#!/usr/bin/env python3
"""Independent exact checks of the original Kashaev crossing.

The original W-symbol, Fourier formula and highest-weight R are evaluated
separately. Finite-field checks supplement the uniform characteristic-zero
proof in notes/kashaev_crossing_and_period_lattice.md.
"""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp


def original(n, p, w):
    ps, bars = [1], [1]
    for j in range(1, n):
        ps.append(ps[-1]*(1-pow(w, j, p)) % p)
        bars.append(bars[-1]*(1-pow(w, -j, p)) % p)

    def symbol(i, j, k, l, a, b, c, d):
        u, v, t, h = ((j-i-a) % n, (i-l-d) % n,
                      (l-k-c) % n, (k-j-b) % n)
        if u+t >= n or v+h >= n:
            return 0
        denominator = ps[u]*bars[v]*ps[t]*bars[h] % p
        return n*pow(w, a-k-j+(v+t)*(t+h), p)*pow(denominator, -1, p) % p

    r = np.zeros((n*n, n*n), dtype=np.int64)
    printed_inverse = np.zeros_like(r)
    for i, j, k, l in product(range(n), repeat=4):
        r[i*n+j, k*n+l] = symbol(i, j, k, l, 1, 0, 0, 0)*pow(w, k+l, p) % p
        printed_inverse[i*n+l, k*n+j] = (
            symbol(i, j, k, l, 0, 0, 0, 1)*pow(w, j+k, p) % p)
    return r, printed_inverse, ps


def quantum_group(n, p, mu):
    s = pow(mu, 2, p)
    ds = (s-pow(s, -1, p)) % p
    ints = [0]+[(pow(s, j, p)-pow(s, -j, p))*pow(ds, -1, p) % p
                for j in range(1, n)]
    factorials = [1]
    for j in range(1, n):
        factorials.append(factorials[-1]*ints[j] % p)
    r = np.zeros((n*n, n*n), dtype=np.int64)
    ri = np.zeros_like(r)
    for a, b in product(range(n), repeat=2):
        ecoefficient = 1
        for k in range(min(a, n-1-b)+1):
            if k:
                ecoefficient = ecoefficient*ints[a-k+1]**2 % p
            coefficient = (pow(s, k*(k-1)//2, p)*pow(ds, k, p)
                           *pow(factorials[k], -1, p)) % p
            inverse_coefficient = (pow(-1, k, p)*pow(s, -k*(k-1)//2, p)
                                   *pow(ds, k, p)*pow(factorials[k], -1, p)) % p
            c, d = a-k, b+k
            r[c*n+d, a*n+b] = (
                coefficient*ecoefficient*pow(mu, (n-1-2*c)*(n-1-2*d), p) % p)
            ri[c*n+d, a*n+b] = (
                inverse_coefficient*ecoefficient*pow(mu, -(n-1-2*a)*(n-1-2*b), p) % p)
    return r, ri


def partial2(a, n, p):
    return np.einsum('abcb->ac', a.reshape(n, n, n, n)) % p


def cut_braid(n, p, bk, bki, bq, bqi, muk, muq, alphak, alphaq):
    eye = np.eye(n, dtype=np.int64)

    def embedded(a, position):
        return np.kron(a, eye) if position == 0 else np.kron(eye, a)

    words = ([(0, 1), (1, -1), (0, 1), (1, -1)],
             [(0, 1), (0, 1), (0, 1), (1, 1)],
             [(0, -1), (0, -1), (0, -1), (1, -1)])
    for word in words:
        output = []
        for positive, negative, pivotal, alpha in (
                (bk, bki, muk, alphak), (bq, bqi, muq, alphaq)):
            value = np.eye(n**3, dtype=np.int64)
            for position, sign in word:
                value = value@embedded(positive if sign > 0 else negative, position) % p
            value = value@np.kron(eye, np.kron(pivotal, pivotal)) % p
            reduced = np.einsum('abcdbc->ad', value.reshape((n,)*6)) % p
            reduced = reduced*pow(alpha, -sum(sign for _, sign in word), p) % p
            assert np.array_equal(reduced, int(reduced[0, 0])*eye % p)
            output.append(reduced)
        assert np.array_equal(*output)
    return len(words)


def audit(n):
    p = next(4*n*k+1 for k in range(1, 1000) if sp.isprime(4*n*k+1))
    primitive = int(sp.primitive_root(p))
    mu = pow(primitive, (p-1)//(4*n), p)
    s, w = pow(mu, 2, p), pow(mu, 4, p)
    r, printed_inverse, ps = original(n, p, w)
    eye = np.eye(n*n, dtype=np.int64)
    assert np.array_equal(r@printed_inverse % p, w*eye % p)

    plus = np.array([[pow(w, i*j, p) for j in range(n)] for i in range(n)], dtype=np.int64)
    minus = np.array([[pow(w, -i*j, p) for j in range(n)] for i in range(n)], dtype=np.int64)
    transformed = np.kron(minus, minus)@r % p
    transformed = transformed@np.kron(plus, plus) % p
    transformed = transformed*pow(n, -2, p) % p
    triangular = np.zeros_like(r)
    for a, b in product(range(n), repeat=2):
        for k in range(min(a, n-1-b)+1):
            c, d = a-k, b+k
            denominator = ps[c]*ps[b]*ps[k] % p
            triangular[c*n+d, a*n+b] = (
                pow(w, 1+c*(b+1), p)*ps[a]*ps[d]*pow(denominator, -1, p) % p)
    assert np.array_equal(transformed, triangular)

    rq, rqi = quantum_group(n, p, mu)
    assert np.array_equal(rq@rqi % p, eye)
    duality = np.zeros((n, n), dtype=np.int64)
    duality_inverse = np.zeros_like(duality)
    for j in range(n):
        coefficient = pow(-1, j, p)*pow(s, j*(j-n), p) % p
        duality[n-1-j, j] = coefficient
        duality_inverse[j, n-1-j] = pow(coefficient, -1, p)
    dual_compared = np.kron(duality, duality)@rq % p
    dual_compared = dual_compared@np.kron(duality_inverse, duality_inverse) % p
    assert np.array_equal(rq.T, dual_compared)
    gs = [ps[j]*pow(1-w, -j, p) % p for j in range(n)]
    ds = [pow(-s, j, p) for j in range(n)]
    gamma = w*pow(mu, -(n-1)**2, p) % p
    row = np.kron(np.array([g*d % p for g, d in zip(gs, ds)]), np.array(gs))
    column = np.kron(np.array([pow(g, -1, p) for g in gs]),
                     np.array([pow(g*d, -1, p) for g, d in zip(gs, ds)]))
    compared = gamma*row[:, None]*rq % p
    compared = compared*column[None, :] % p
    assert np.array_equal(compared, transformed)

    swap = np.zeros_like(r)
    for a, b in product(range(n), repeat=2):
        swap[b*n+a, a*n+b] = 1
    shift = np.roll(np.eye(n, dtype=np.int64), 1, axis=0)
    bk = swap@r.T % p
    bki = printed_inverse.T@swap*pow(w, -1, p) % p
    bq, bqi = swap@rq.T % p, rqi.T@swap % p
    muk = (-s*shift) % p
    muq = np.diag([pow(s, -(n-1-2*j), p) for j in range(n)]).astype(np.int64)
    alphak, alphaq = -s % p, pow(mu, n*n-1, p)
    assert gamma*alphaq % p == alphak
    assert np.array_equal(bk@bki % p, eye)
    assert np.array_equal(partial2(bk@np.kron(np.eye(n, dtype=np.int64), muk) % p, n, p),
                          alphak*np.eye(n, dtype=np.int64) % p)
    assert np.array_equal(partial2(bki@np.kron(np.eye(n, dtype=np.int64), muk) % p, n, p),
                          pow(alphak, -1, p)*np.eye(n, dtype=np.int64) % p)
    assert np.array_equal(np.kron(muk, muk)@bk % p, bk@np.kron(muk, muk) % p)
    cuts = cut_braid(n, p, bk, bki, bq, bqi, muk, muq, alphak, alphaq) if n <= 5 else 0
    return {"level": n, "finite_field_prime": p, "fourier_formula_exact": True,
            "quantum_group_gauge_exact": True, "self_duality_exact": True,
            "enhancement_exact": True,
            "printed_inverse_product": "omega I", "cut_period_checks": cuts}


def characteristic_zero_phase_check():
    n = 2
    ps = [Fraction(1), Fraction(2)]

    def sign(k):
        return Fraction((-1)**(k % 2))

    def symbol(i, j, k, l, a, b, c, d):
        u, v, t, h = (j-i-a) % 2, (i-l-d) % 2, (l-k-c) % 2, (k-j-b) % 2
        if u+t >= 2 or v+h >= 2:
            return Fraction(0)
        return 2*sign(a-k-j+(v+t)*(t+h))/(ps[u]*ps[v]*ps[t]*ps[h])

    r = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    ri = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for i, j, k, l in product(range(2), repeat=4):
        r[i*2+j][k*2+l] = symbol(i, j, k, l, 1, 0, 0, 0)*sign(k+l)
        ri[i*2+l][k*2+j] = symbol(i, j, k, l, 0, 0, 0, 1)*sign(j+k)
    result = [[sum(r[i][k]*ri[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    assert result == [[Fraction(-int(i == j)) for j in range(4)] for i in range(4)]
    return {"level": 2, "arithmetic": "Q", "literal_printed_inverse_product": "-I"}


def main():
    result = {"scope": "Exact crossing and period diagnostics; the uniform proof is in the note.",
              "characteristic_zero_phase": characteristic_zero_phase_check(),
              "records": [audit(n) for n in (2, 3, 4, 5, 6, 9, 15)]}
    Path(__file__).with_name("kashaev_crossing_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
