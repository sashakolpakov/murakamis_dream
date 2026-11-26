#!/usr/bin/env python3
"""Exact finite check of the signed two-row telescope.

Build the original x=0,y=1 Casimir matrix, form its polynomial resolvent
numerator by Chebyshev division, and extract the two required face degrees.
No identity under test is used to build that numerator. These finite checks
do not prove an asymptotic or general closed-source estimate.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


class Field:
    def __init__(self, N):
        self.q = sp.Symbol('q')
        self.mod = sp.Poly(sp.cyclotomic_poly(2*N, self.q), self.q, domain=sp.QQ)
        self.zero, self.one = self.red(0), self.red(1)
        self.powers = [self.red(self.q**j) for j in range(2*N)]

    def red(self, value):
        return sp.Poly(value, self.q, domain=sp.QQ).rem(self.mod)

    def mul(self, a, b):
        return (a*b).rem(self.mod)

    def power(self, j):
        return self.powers[j % len(self.powers)]


def exact_source(N):
    F = Field(N)
    z = sp.Symbol('sigma')
    d, m = N-1, N//2
    chi = sp.Poly(2*sp.chebyshevt(N, z/2)+2, z)
    diagonal = [F.power(2*j+1)+F.power(-2*j-1) for j in range(N)]
    # At x=0,y=1 the genuine Casimir is upper bidiagonal. In the full
    # homogeneous source its row i,column j has y-degree exactly j-i.
    lowering = [F.red(2)-F.power(2*j)-F.power(-2*j) for j in range(N)]
    identity = [[F.one if i == j else F.zero for j in range(N)] for i in range(N)]
    powers = [identity]
    for k in range(1, N):
        old = powers[-1]
        new = [[F.zero for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(i, N):
                value = F.mul(diagonal[i], old[i][j])
                if i+1 < N:
                    value -= F.mul(lowering[i+1], old[i+1][j])
                new[i][j] = F.red(value)
        powers.append(new)
    # V_l is the coefficient of sigma^l in
    # (chi(sigma)-chi(Omega))/(sigma-Omega), formed before any compression.
    V = []
    for ell in range(N):
        matrix = [[F.zero for j in range(N)] for i in range(N)]
        for degree in range(ell+1, N+1):
            coefficient = chi.nth(degree)
            if coefficient:
                P = powers[degree-1-ell]
                for i in range(N):
                    for j in range(i, N):
                        matrix[i][j] += coefficient*P[i][j]
        V.append([[F.red(value) for value in row] for row in matrix])
    endpoint = [[sum(((-2)**ell*V[ell][i][j] for ell in range(N)), F.zero)
                 for j in range(N)] for i in range(N)]
    # Top LEFT: i=0, j=k<m; bottom CROSS: i=k, j=d. These imply
    # c-degrees d-k and k, and y-degrees k and d-k, respectively.
    actual = [sum((F.mul(V[ell][0][k], endpoint[k][d]) for k in range(m)), F.zero)
              for ell in range(N)]
    if N % 2 == 0:
        P = 2*sp.chebyshevt(m, z/2)
        expected, remainder = sp.div(-N*N*P*(P+2*(-1)**(m-1)), z+2, z)
        assert remainder == 0
    else:
        P = sp.chebyshevu(m, z/2)-sp.chebyshevu(m-1, z/2)
        expected = N*N*P*(P+(-1)**(m-1)*N)
    expected = sp.Poly(sp.expand(expected), z)
    for ell, value in enumerate(actual):
        assert F.red(value-expected.nth(ell)).is_zero, (N, ell)
    assert expected.degree() <= d
    return dict(N=N, field_cyclotomic_order=2*N, original_resolvent_coefficients=N,
                exact_polynomial=str(expected.as_expr()),
                sigma_minus_two=str(expected.eval(-2)), sigma_plus_two=str(expected.eval(2)),
                original_face_degrees=dict(c=d,y=d),
                midpoint_row_cut=m-1)


def exact_grading():
    count = 0
    for d in range(1, 7):
        for target in (0, d):
            for u in range(d+1):
                for v in range(d+1):
                    for up in range(d+1):
                        for vp in range(d+1):
                            a,b,c = target-u,up-v,vp
                            p = d-a-b-c
                            if min(a,b,c,p) < 0:
                                continue
                            assert up+vp == u+v+d-target-p
                            if target == 0 and p == 0:
                                assert u == 0 and up+vp == d+u+v
                            count += 1
    return dict(feasible_local_degree_states=count, degrees=list(range(1,7)),
                identity='ell_next=ell+d-target-p',
                scope='Finite grading identities, not a cyclic trace norm bound.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'md-undecorated-cancellation-two-row-telescope-results.json'))
    args = parser.parse_args()
    rows = [exact_source(N) for N in range(3, 13)]
    data = dict(status='passed', arithmetic='Exact rational cyclotomic fields',
                source_construction='Original Casimir powers and polynomial division, before row restriction',
                cases=rows, grading=exact_grading(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                limitations=['Finite algebraic tests do not replace the all-N telescoping proof.',
                             'The two-row specialization is not a full cyclic-source bound.'])
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(dict(status='passed', levels=len(rows),
                         exact_resolvent_polynomial_coefficients=sum(r['original_resolvent_coefficients'] for r in rows),
                         first_two=rows[:2],grading=data['grading']),indent=2))


if __name__ == '__main__':
    main()
