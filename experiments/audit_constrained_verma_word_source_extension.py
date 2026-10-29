#!/usr/bin/env python3
"""Whole two-wall excursion sum and constrained actual-source algebra."""

from collections import defaultdict
from functools import cache
import itertools
import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field
from audit_quantum_matrix_base_intertwiner_torsor import (
    Torus, scalar, generators, identity, mul,
)


def symbolic_word(m):
    delta, w, lam = s.symbols('delta w lambda')
    t = delta*w
    # Nonconstant numerical blocks make different tail visits distinguishable.
    a = [s.Integer(i+2) for i in range(m)]
    b = [s.Integer(2*i+3) for i in range(m)]
    c = [s.Integer(3*i+2) for i in range(m)]
    d = [s.Integer(i+5) for i in range(m)]
    E, F = s.eye(m+1), s.eye(m-1)
    B, C = s.zeros(m+1, m-1), s.zeros(m-1, m+1)
    for i in range(1, m+1):
        E[i, i-1] = -a[i-1]
        if i >= 2:
            B[i, i-2] = b[i-1]
        if i < m:
            C[i-1, i-1] = c[i-1]
            if i >= 2:
                F[i-1, i-2] = -d[i-1]
    Fi = F.inv()
    K = B*Fi*C
    Ei = E.inv()
    series = s.zeros(m+1)
    term = Ei
    for r in range(m//2+1):
        series += (lam*t)**r*term
        term = Ei*K*term
    S = E-lam*t*K
    assert (S*series-s.eye(m+1)).applyfunc(s.expand) == s.zeros(m+1)
    actual = s.eye(2)
    for i in range(m):
        A = s.Matrix([[a[i], lam*w*b[i]], [delta*c[i], d[i]]])
        actual = A*actual
    assert s.expand(actual[0, 0]-series[m, 0]) == 0
    assert s.expand(actual[0, 0].subs(lam, 0)-s.prod(a)) == 0
    assert s.Poly(s.expand(actual[0, 0]), lam).degree() <= m//2
    mixed = s.expand(actual[0, 0]).coeff(delta, 1).coeff(w, 1).subs(lam, 1)
    one_visit = sum(s.prod(a[j+1:])*b[j]*s.prod(d[i+1:j])*c[i]*s.prod(a[:i])
                    for i in range(m) for j in range(i+1, m))
    assert mixed == one_visit
    # Exact 3-block source presentation, including the normal current.
    hh, tt = m+1, m-1
    Zht, Zth, Ztt = s.zeros(hh, tt), s.zeros(tt, hh), s.zeros(tt)
    Kcon = s.BlockMatrix([[E, -w*B, Zht],
                         [-delta*C, F, s.eye(tt)],
                         [Zth, s.eye(tt), Ztt]]).as_explicit()
    U = s.BlockMatrix([[s.eye(hh), Zht, w*B],
                      [Zth, s.eye(tt), -F],
                      [Zth, Ztt, s.eye(tt)]]).as_explicit()
    V = s.BlockMatrix([[s.eye(hh), Zht, Zht],
                      [Zth, s.eye(tt), Ztt],
                      [delta*C, Ztt, s.eye(tt)]]).as_explicit()
    target = s.BlockMatrix([[E, Zht, Zht],
                           [Zth, Ztt, s.eye(tt)],
                           [Zth, s.eye(tt), Ztt]]).as_explicit()
    assert (U*Kcon*V-target).applyfunc(s.expand) == s.zeros(hh+2*tt)
    I0 = s.BlockMatrix([[s.eye(hh)], [Zth], [delta*C]]).as_explicit()
    I1 = s.BlockMatrix([[s.eye(hh)], [Zth], [Zth]]).as_explicit()
    P0 = s.BlockMatrix([[s.eye(hh), Zht, Zht]]).as_explicit()
    P1 = s.BlockMatrix([[s.eye(hh), Zht, w*B]]).as_explicit()
    assert (Kcon*I0-I1*E).applyfunc(s.expand) == s.zeros(hh+2*tt, hh)
    assert (P1*Kcon-E*P0).applyfunc(s.expand) == s.zeros(hh, hh+2*tt)
    assert P0*I0 == P1*I1 == s.eye(hh)
    return {'word_length': m, 'all_excursions_resummed': True,
            'mixed_two_wall_coefficient_exact': True,
            'constrained_unimodular_extension_and_pointing': True}


def rectangular_mul(a, b):
    rows, middle, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == middle
    return [[sum((a[i][j]*b[j][k] for j in range(middle)), scalar(0))
             for k in range(cols)] for i in range(rows)]


def noncommutative_checks():
    u, v, c = generators()
    records = []
    for A in (u+v, u*v+u**-1, scalar(0)):
        B, C, D = u*v, v**-1*u, u+v**-1
        z, one = scalar(0), scalar(1)
        K = [[A, B, z], [C, D, one], [z, one, z]]
        U = [[one, z, -B], [z, one, -D], [z, z, one]]
        V = [[one, z, z], [z, one, z], [-C, z, one]]
        target = [[A, z, z], [z, z, one], [z, one, z]]
        assert mul(mul(U, K), V) == target
        i0, i1 = [[one], [z], [-C]], [[one], [z], [z]]
        p0, p1 = [[one, z, z]], [[one, z, -B]]
        assert rectangular_mul(K, i0) == rectangular_mul(i1, [[A]])
        assert rectangular_mul(p1, K) == rectangular_mul([[A]], p0)
        assert rectangular_mul(p0, i0) == rectangular_mul(p1, i1) == [[one]]
        records.append({'singular_head_allowed': A == 0,
                        'noncommutative_order_and_source_maps_exact': True})
    x, delta, w = s.symbols('x delta w')
    K = s.Matrix([[x, -w, 0], [-delta, 1, 1], [0, 1, 0]])
    assert s.expand(K.det()+x) == 0
    assert (x-delta*w).subs(x, 0) == -delta*w
    return records


def actual_verma_operators(N, b, p, q, M):
    Q, xx = q*q % p, -M*pow(q, -1, p) % p
    bound = b*(N-1)
    states = list(tup for tup in itertools.product(range(bound+1), repeat=b)
                  if sum(tup) <= bound)
    @cache
    def gauss(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return (gauss(n-1, k)+pow(Q, n-k, p)*gauss(n-1, k-1)) % p
    def poch(z, k):
        ans = 1
        for j in range(k):
            ans = ans*(1-z*pow(Q, j, p)) % p
        return ans
    def coefficient(sign, a, bb, k):
        if sign > 0:
            return pow(-1, k, p)*pow(xx, -a-bb-k, p) \
                *pow(Q, a*bb+(a-bb)*k-k*(k+1)//2, p) \
                *gauss(bb+k, k)*poch(M*M*pow(Q, -a, p) % p, k) % p
        return pow(xx, a+bb-k, p)*pow(Q, -a*bb, p) \
            *gauss(a+k, k)*poch(M*M*pow(Q, -bb, p) % p, k) % p
    operators = {}
    for strand in range(b-1):
        for sign in (-1, 1):
            op = {}
            for column in states:
                a, bb = column[strand:strand+2]
                values = {}
                for k in range((a if sign > 0 else bb)+1):
                    pair = (bb+sign*k, a-sign*k)
                    row = column[:strand]+pair+column[strand+2:]
                    value = coefficient(sign, a, bb, k)
                    if value:
                        values[row] = value
                op[column] = values
            operators[(strand, sign)] = op
    return states, operators


def apply_op(op, values, p):
    result = defaultdict(int)
    for column, value in values.items():
        for row, coeff in op[column].items():
            result[row] = (result[row]+coeff*value) % p
    return {row: value for row, value in result.items() if value}


def actual_word_case(N, wall, word):
    b = 3
    if wall == 'root':
        p, _, q = field(N)
        M = 3 if 3 % p else 2
    else:
        p, q = 1009, 2
        M = -pow(q, N, p) % p if wall == 'Weyl' else 3
    Q = q*q % p
    delta = (1-pow(Q, N, p)) % p
    w = (M*pow(Q, -N, p)-pow(M, -1, p)) % p
    states, ops = actual_verma_operators(N, b, p, q, M)
    ishead = lambda row: max(row) < N
    heads = [row for row in states if ishead(row)]
    # Independently track return count through literal actual crossing entries.
    nonzero_excursions = 0
    for start in heads:
        plain, cut = {start: 1}, {start: 1}
        weighted = {(start, 0): 1}
        for step in word:
            op = ops[step]
            plain = apply_op(op, plain, p)
            cut = {row: value for row, value in apply_op(op, cut, p).items()
                   if ishead(row)}
            nxt = defaultdict(int)
            for (column, count), value in weighted.items():
                for row, coeff in op[column].items():
                    extra = int(not ishead(column) and ishead(row))
                    key = row, count+extra
                    nxt[key] = (nxt[key]+coeff*value) % p
            weighted = {key: value for key, value in nxt.items() if value}
        for end in heads:
            counts = {r: value for (row, r), value in weighted.items() if row == end}
            assert counts.get(0, 0) == cut.get(end, 0)
            assert sum(counts.values()) % p == plain.get(end, 0)
            assert all(r <= len(word)//2 for r in counts)
            if not delta or not w:
                assert all(r == 0 for r in counts)
            nonzero_excursions += sum(r > 0 for r in counts)
    return {'level': N, 'braid_strands': b, 'word_length': len(word),
            'wall': wall, 'actual_cut_is_return_count_zero': True,
            'all_actual_paths_resummed': True,
            'nonzero_positive_return_coefficients': nonzero_excursions}


def main():
    symbolic = [symbolic_word(m) for m in range(2, 7)]
    words = [((0, 1), (1, -1), (0, -1), (1, 1)),
             ((1, -1), (0, 1), (1, 1), (0, -1), (1, -1), (0, 1))]
    actual = [actual_word_case(N, wall, word)
              for N in (2, 3) for wall in ('generic', 'root', 'Weyl') for word in words]
    result = {'symbolic_whole_word_cases': symbolic,
              'noncommutative_stable_extension': noncommutative_checks(),
              'actual_balanced_Verma_word_cases': actual,
              'scope': 'Exact pointed constrained source and finite excursion resummation; no geometric phase or volume assertion.'}
    target = Path(__file__).with_name('constrained_verma_word_source_extension_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'symbolic_word_lengths': len(symbolic),
                      'noncommutative_cases': len(result['noncommutative_stable_extension']),
                      'actual_arbitrary_word_cases': len(actual),
                      'nonzero_actual_return_coefficients': sum(
                          a['nonzero_positive_return_coefficients'] for a in actual)}))


if __name__ == '__main__':
    main()
