#!/usr/bin/env python3
"""Exact audits of the color family, its lattice factor and Kashaev point."""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_kashaev_crossing import original


WORDS = ([(0, 1), (1, -1), (0, 1), (1, -1)],
         [(0, 1), (0, 1), (0, 1), (1, 1)],
         [(0, -1), (0, -1), (0, -1), (1, -1)])


def color_matrices(r, p, q, x):
    difference = (q-pow(q, -1, p)) % p
    integers = [0]+[(pow(q, j, p)-pow(q, -j, p))*pow(difference, -1, p) % p
                   for j in range(1, r)]
    evalues = [0]+[integers[j]*(x*pow(q, 1-j, p)-pow(x, -1, p)*pow(q, j-1, p))
                   *pow(difference, -1, p) % p for j in range(1, r)]
    factorial = [1]
    for j in range(1, r):
        factorial.append(factorial[-1]*integers[j] % p)
    positive = np.zeros((r*r, r*r), dtype=np.int64)
    negative = np.zeros_like(positive)
    for a, b in product(range(r), repeat=2):
        ecoefficient = 1
        for k in range(min(a, r-1-b)+1):
            if k:
                ecoefficient = ecoefficient*evalues[a-k+1] % p
            coefficient = (pow(q, k*(k-1)//2, p)*pow(difference, k, p)
                           *pow(factorial[k], -1, p)) % p
            icoefficient = (pow(-1, k, p)*pow(q, -k*(k-1)//2, p)
                            *pow(difference, k, p)*pow(factorial[k], -1, p)) % p
            c, d = a-k, b+k
            positive[c*r+d, a*r+b] = (
                coefficient*ecoefficient*pow(x, -c-d, p)*pow(q, 2*c*d, p) % p)
            negative[c*r+d, a*r+b] = (
                icoefficient*ecoefficient*pow(x, a+b, p)*pow(q, -2*a*b, p) % p)
    swap = np.zeros_like(positive)
    for a, b in product(range(r), repeat=2):
        swap[b*r+a, a*r+b] = 1
    assert np.array_equal(positive@negative % p, np.eye(r*r, dtype=np.int64))
    pivotal = np.diag([pow(x, 1-r, p)*pow(q, -2*j*(1-r), p) % p
                       for j in range(r)]).astype(np.int64)
    return swap@positive % p, negative@swap % p, pivotal, pow(x, 1-r, p)


def reduced_period(r, p, positive, negative, pivotal, theta, word):
    eye = np.eye(r, dtype=np.int64)
    result = np.eye(r**3, dtype=np.int64)
    for position, sign in word:
        crossing = positive if sign > 0 else negative
        crossing = np.kron(crossing, eye) if position == 0 else np.kron(eye, crossing)
        result = result@crossing % p
    result = result@np.kron(eye, np.kron(pivotal, pivotal)) % p
    cut = np.einsum('abcdbc->ad', result.reshape((r,)*6)) % p
    cut = cut*pow(theta, -sum(sign for _, sign in word), p) % p
    assert np.array_equal(cut, int(cut[0, 0])*eye % p)
    return int(cut[0, 0])


def audit(r):
    p = next(4*r*k+1 for k in range(1, 1000) if sp.isprime(4*r*k+1))
    primitive = int(sp.primitive_root(p))
    root = pow(primitive, (p-1)//(4*r), p)
    q, w = pow(root, 2, p), pow(root, 4, p)
    eta = pow(-1, r+1, p)*pow(q, r*(1-r)//2, p) % p
    assert eta == pow(pow(root, r, p), r+3, p)

    def lattice_factor(m):
        polynomial = sum(pow(m, 2*j, p) for j in range(r)) % p
        return eta*pow(m, r-1, p)*pow(polynomial, -1, p) % p

    m = primitive
    x = -pow(q, -1, p)*m % p
    numerator = (q*x-pow(q*x, -1, p)) % p
    denominator = (pow(x, r, p)-pow(x, -r, p)) % p
    original_dimension = (-pow(q, r*(1-r)//2, p)*numerator
                          *pow(denominator, -1, p)) % p
    assert original_dimension == lattice_factor(m)
    generic_ratio = (-pow(q, -1, p)*(pow(q, 2, p)*m*m-1)
                     *pow(m*m-1, -1, p)) % p
    assert lattice_factor(q*m % p)*pow(lattice_factor(m), -1, p) % p == generic_ratio
    assert lattice_factor(1) == eta*pow(r, -1, p) % p
    monodromy = 1
    for j in range(2*r):
        point = m*pow(q, j, p) % p
        ratio = (-pow(q, -1, p)*(pow(q, 2, p)*point*point-1)
                 *pow(point*point-1, -1, p)) % p
        monodromy = monodromy*ratio % p
    assert monodromy == 1

    comparisons = 0
    if r <= 5:
        generic = color_matrices(r, p, q, x)
        assert int(np.trace(generic[2])) % p == 0
        for word in WORDS:
            reduced_period(r, p, *generic, word)
        specialized = color_matrices(r, p, q, pow(q, r-1, p))
        ro, printed_inverse, _ = original(r, p, w)
        swap = np.zeros_like(ro)
        for a, b in product(range(r), repeat=2):
            swap[b*r+a, a*r+b] = 1
        kashaev = (swap@ro.T % p,
                   printed_inverse.T@swap*pow(w, -1, p) % p,
                   (-q*np.roll(np.eye(r, dtype=np.int64), 1, axis=0)) % p,
                   -q % p)
        for word in WORDS:
            assert reduced_period(r, p, *specialized, word) == reduced_period(r, p, *kashaev, word)
            comparisons += 1
    return {"level": r, "finite_field_prime": p,
            "modified_dimension_lattice_exact": True,
            "level_independent_shift_gauge_exact": True,
            "regular_point_value": "eta_r/r", "central_monodromy": 1,
            "kashaev_specialization_comparisons": comparisons}


def main():
    result = {"scope": "Exact algebraic diagnostics; no asymptotic volume assertion.",
              "records": [audit(r) for r in (2, 3, 4, 5, 6, 9, 15)]}
    Path(__file__).with_name("kashaev_ado_pointing_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
