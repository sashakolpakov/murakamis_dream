#!/usr/bin/env python3
"""Exact midpoint group/character checks; no quantum volume assertion."""
import json
from itertools import product
from math import gcd
from pathlib import Path
import sympy as sp


def meridians(M, z):
    return sp.Matrix([[M, 1], [0, 1/M]]), sp.Matrix([[M, 0], [-z, 1/M]])


def word(A, B, signs):
    out = sp.eye(2)
    for j, eps in enumerate(signs):
        C = B if j % 2 == 0 else A
        out = out * (C if eps == 1 else C.inv())
        out = out.applyfunc(sp.expand)
    return out


def generic_leading_checks():
    M, z = sp.symbols('M z', nonzero=True)
    A, B = meridians(M, z)
    count = 0
    for m in range(1, 4):
        for signs in product([-1, 1], repeat=2*m):
            W = word(A, B, signs)
            P = sp.Poly(sp.expand(W[1, 1]+(M-1/M)*W[0, 1]), z)
            expected = (-1)**m
            for eps in signs:
                expected *= eps
            assert P.degree() == m and sp.simplify(P.LC()-expected) == 0
            assert sp.Poly(W[0, 1], z).degree() <= m-1
            count += 1
    return count


def midpoint_checks():
    z = sp.symbols('z')
    A, B = meridians(sp.I, z)
    t = -2-z
    cases = []
    for p in range(3, 20, 2):
        m = (p-1)//2
        Uprev, U = sp.Integer(0), sp.Integer(1)
        for _ in range(m):
            Uprev, U = U, sp.expand(t*U-Uprev)
        canonical = sp.Poly(U-Uprev, z)
        assert sp.degree(sp.gcd(canonical.as_expr(), sp.diff(canonical.as_expr(), z)), z) == 0
        power = (A*B)**p+sp.eye(2)
        assert all(sp.rem(sp.expand(v), canonical.as_expr(), z) == 0 for v in power)
        words = 0
        for q in range(1, p, 2):
            if gcd(p, q) != 1:
                continue
            signs = [(-1)**((j*q)//p) for j in range(1, p)]
            W = word(A, B, signs)
            sign = (-1)**sum(eps == -1 for eps in signs)
            P = sp.expand(W[1, 1]+2*sp.I*W[0, 1])
            assert sp.expand(P-sign*canonical.as_expr()) == 0
            assert all(sp.rem(sp.expand(v), P, z) == 0 for v in A*W-W*B)
            words += 1
        cases.append({'p': p, 'degree': m, 'sign_words': words,
                      'simple_midpoint_roots': True,
                      'AB_power_p_equals_minus_I_mod_relation': True})
    return cases


def main():
    data = {'status': 'PASS', 'generic_sign_words': generic_leading_checks(),
            'midpoint': midpoint_checks(),
            'scope': 'Exact group and monic-character inputs; the volume-zero proof is geometric in the note. No quantum transport or survival asserted.'}
    Path(__file__).with_name('two_bridge_midpoint_anchor_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
