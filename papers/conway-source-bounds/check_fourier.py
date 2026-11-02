#!/usr/bin/env python3
"""Exact finite checks for the full character Fourier functional.

Polynomial division, Laurent expansion, phase arithmetic, and endpoint jets
are computed separately. These bounded checks do not prove a strip estimate,
an asymptotic theorem, or a geometric interpretation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [0]


def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def scale(p, a):
    return trim([a*x for x in p])


def mul(p, q):
    r = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return trim(r)


def derivative(p):
    return trim([k*a for k, a in enumerate(p) if k])


def evaluate(p, x):
    total = 0
    for a in reversed(p):
        total = total*x+a
    return total


def mod_monic(p, modulus):
    assert modulus[-1] == 1
    p = trim(p)
    while len(p) >= len(modulus):
        shift, leading = len(p)-len(modulus), p[-1]
        for j, a in enumerate(modulus):
            p[shift+j] -= leading*a
        p = trim(p)
    return p


def chebyshev_sequences(n):
    # C_k(z)=2 T_k(z/2); U_k(z/2) uses a different constant term.
    c, u = [[2], [0, 1]], [[1], [0, 1]]
    for k in range(1, n):
        c.append(add([0]+c[-1], scale(c[-2], -1)))
        u.append(add([0]+u[-1], scale(u[-2], -1)))
    return c, u


def sign(k):
    return -1 if k % 2 else 1


def laurent(p):
    answer = {}
    for degree, coefficient in enumerate(p):
        for j in range(degree+1):
            exponent = degree-2*j
            answer[exponent] = answer.get(exponent, 0)+coefficient*comb(degree, j)
    return {k: a for k, a in answer.items() if a}


def direct_character(n, h, p, modulus, u):
    character = scale(u[n-h-1], sign(n-h-1))
    remainder = mod_monic(mul(character, p), modulus)
    coefficient = remainder[n-1] if len(remainder) == n else 0
    return sign(n-1)*n*n*coefficient


def fourier_character(n, h, p, wrong_missing_winding=False):
    total = 0
    for r, a in laurent(p).items():
        if (r-h) % n == 0:
            m = (r-h)//n
            weight = 1 if wrong_missing_winding and m == -1 else m+1
            total += sign(m)*weight*a
    return sign(h)*n*n*total


def nodal_character_without_normals(n, h, p):
    # Formal root-grid orthogonality, retaining values but deleting F'.
    total = sum(sign((r-h)//n)*a for r, a in laurent(p).items()
                if (r-h) % n == 0)
    return sign(h)*n*(n-h)*total


def finite_identities():
    counts = {'monomial_identities': 0, 'dense_product_identities': 0,
              'ideal_multiple_identities': 0, 'phase_identities': 0,
              'angular_derivative_identities': 0, 'endpoint_jet_repairs': 0,
              'normal_blind_polynomials': 0, 'two_high_support_exclusions': 0}
    witnesses = []
    for n in range(2, 19):
        c, u = chebyshev_sequences(4*n+5)
        modulus = add(c[n], [2])
        for degree in range(3*n+4):
            p = [0]*degree+[1]
            for h in range(n):
                got = direct_character(n, h, p, modulus, u)
                expected = fourier_character(n, h, p)
                assert got == expected, (n, h, degree, got, expected)
                counts['monomial_identities'] += 1
        factors = [[sign(k)*(k % 5+1) for k in range(n)],
                   [(k % 7)-3 for k in range(n+3)],
                   [1]+[0]*(n-2)+[-2]]
        products = [mul(factors[0], factors[1]),
                    mul(mul(factors[0], factors[1]), factors[2])]
        for p in products:
            for h in range(n):
                assert direct_character(n, h, p, modulus, u) == fourier_character(n, h, p)
                counts['dense_product_identities'] += 1
        for p in [mul(modulus, factors[0]), mul(modulus, products[0])]:
            for h in range(n):
                assert direct_character(n, h, p, modulus, u) == 0
                assert fourier_character(n, h, p) == 0
                counts['ideal_multiple_identities'] += 1

        # A nonzero class invisible to every spectral value. For odd n,
        # the simple factor is included once, the double factors only once.
        if n % 2 == 0:
            distinct = c[n//2]
        else:
            m = (n-1)//2
            distinct = mul([2, 1], add(u[m], scale(u[m-1], -1)))
        blind = [0]*(n-len(distinct))+distinct
        assert len(blind) == n and blind[-1] == 1
        assert mod_monic(mul(distinct, distinct), modulus) == [0]
        assert direct_character(n, n-1, blind, modulus, u) == sign(n-1)*n*n
        counts['normal_blind_polynomials'] += 1

        m = (n-1)//2
        for i in range(m+1, n):
            for j in range(m+1, n):
                assert i+j > n-1
                counts['two_high_support_exclusions'] += 1

        for k in range(n):
            theta_over_pi = Q(2*k+1, n)
            phase = Q(1, 2)-Q(1, 4*n)-Q(n, 4)+Q(n, 4)*(theta_over_pi-1)**2
            target = k+Q(k*(k+1), n)
            assert ((phase-target)/2).denominator == 1
            for eps in (-1, 0, 1):
                assert (eps*(phase-target)/2).denominator == 1
                counts['phase_identities'] += 1
                # Both sides are logarithmic angular derivatives divided by i.
                angular_chirp = eps*Q(n, 2)*(theta_over_pi-1)
                angular_original = -eps*Q(n-1-2*k, 2)
                assert angular_chirp == angular_original
                counts['angular_derivative_identities'] += 1
        for eps in (-1, 0, 1):
            for f0 in (-2, 0, 3):
                # In x=theta/(2*pi), write a=i*eps*pi*n*F(0).
                # First endpoint jets are (-a,a). Repair by -a*x*(1-x).
                a = eps*n*f0
                psi = [0, 1, -1]
                repair = scale(psi, -a)
                f = add([f0], add(repair, scale(mul(psi, psi), 3*n+eps)))
                df = derivative(f)
                assert (evaluate(df, 0), evaluate(df, 1)) == (-a, a)
                repaired = add(f, scale(repair, -1))
                for order in range(3):
                    assert evaluate(repaired, 0) == evaluate(repaired, 1)
                    repaired = derivative(repaired)
                if a:
                    wrong_sign = derivative(add(f, repair))
                    assert evaluate(wrong_sign, 0) != evaluate(wrong_sign, 1)
                counts['endpoint_jet_repairs'] += 1

        if n >= 3:
            p, h = [0, 1], n-1
            actual = direct_character(n, h, p, modulus, u)
            wrong_winding = fourier_character(n, h, p, True)
            wrong_normals = nodal_character_without_normals(n, h, p)
            assert actual == 0 and wrong_winding != actual and wrong_normals != actual
            witnesses.append({'level': n, 'deficit': h, 'polynomial': 'z',
                              'actual': actual, 'nonzero_missing_winding': wrong_winding,
                              'normals_deleted': wrong_normals})
    return counts, witnesses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise RuntimeError('Run without -O; an earlier output has been removed.')
    folder = Path(__file__).resolve().parent
    root = folder.parents[1]
    files = sorted(p for p in folder.rglob('*.tex') if 'build' not in p.parts)
    files += [Path(__file__).resolve(), root/'papers/newton-tangles/main.tex',
              root/'papers/filling-bounds/main.tex']
    def hashes():
        return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    before = hashes()
    counts, witnesses = finite_identities()
    if hashes() != before:
        raise RuntimeError('A checked source changed during the run.')
    record = {'scope': 'Exact bounded finite algebra in integer polynomials and rational phases.',
              'not_proved': ['uniform Fourier tails or complex strip bounds',
                             'variational component inequalities or full-source induction',
                             'geometric or volume conclusions'],
              'levels': [2, 18], 'counts': counts, 'negative_controls': witnesses,
              'source_sha256': before}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'output': str(args.output), **counts,
                      'negative_control_levels': len(witnesses)}))


if __name__ == '__main__':
    main()
