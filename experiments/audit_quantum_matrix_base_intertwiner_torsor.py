#!/usr/bin/env python3
"""Exact noncommutative cover, matrix/base split, phase and source audits."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


@dataclass
class Torus:
    # u^a v^b c^h; uv=c vu. c is a central indeterminate.
    terms: dict[tuple[int, int, int], Fraction]
    prime: int | None = None

    def __post_init__(self):
        self.terms = {m: self.coeff(a) for m, a in self.terms.items()
                      if self.coeff(a)}

    def coeff(self, a):
        a = Fraction(a)
        if self.prime is None:
            return a
        return Fraction(a.numerator * pow(a.denominator, -1, self.prime)
                        % self.prime)

    def __add__(self, other):
        if not isinstance(other, Torus):
            other = scalar(other, self.prime)
        assert self.prime == other.prime
        ans = self.terms.copy()
        for m, a in other.terms.items():
            ans[m] = ans.get(m, 0) + a
        return Torus(ans, self.prime)

    __radd__ = __add__

    def __neg__(self):
        return Torus({m: -a for m, a in self.terms.items()}, self.prime)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Torus):
            other = scalar(other, self.prime)
        assert self.prime == other.prime
        ans = {}
        for (a, b, h), z in self.terms.items():
            for (aa, bb, hh), zz in other.terms.items():
                m = (a + aa, b + bb, h + hh - b * aa)
                ans[m] = ans.get(m, 0) + z * zz
        return Torus(ans, self.prime)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            assert len(self.terms) == 1
            (a, b, h), z = next(iter(self.terms.items()))
            inverse = Torus({(-a, -b, -h - a*b): 1/z}, self.prime)
            return inverse ** (-n)
        ans = scalar(1, self.prime)
        for _ in range(n):
            ans = ans * self
        return ans

    def __eq__(self, other):
        if not isinstance(other, Torus):
            other = scalar(other, self.prime)
        return self.prime == other.prime and self.terms == other.terms

    def theta(self, shear):
        # theta(u)=u, theta(v)=u^shear v; negative powers are allowed.
        ans = scalar(0, self.prime)
        u, v, c = generators(self.prime)
        for (a, b, h), z in self.terms.items():
            ans += z * u**a * (u**shear*v)**b * c**h
        return ans


def scalar(a, prime=None):
    return Torus({(0, 0, 0): Fraction(a)}, prime)


def monomial(a, b, h=0, prime=None):
    return Torus({(a, b, h): Fraction(1)}, prime)


def generators(prime=None):
    return (monomial(1, 0, prime=prime),
            monomial(0, 1, prime=prime),
            monomial(0, 0, 1, prime=prime))


def zero_matrix(n, prime=None):
    return [[scalar(0, prime) for _ in range(n)] for _ in range(n)]


def identity(n, prime=None):
    ans = zero_matrix(n, prime)
    for i in range(n):
        ans[i][i] = scalar(1, prime)
    return ans


def unit(n, i, j, prime=None):
    ans = zero_matrix(n, prime)
    ans[i][j] = scalar(1, prime)
    return ans


def add(a, b):
    return [[x+y for x, y in zip(r, ss)] for r, ss in zip(a, b)]


def mul(a, b):
    n = len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),
                 scalar(0, a[0][0].prime)) for j in range(n)]
            for i in range(n)]


def matrix_scale(a, x, left=True):
    return [[x*z if left else z*x for z in row] for row in a]


def matrix_pow(a, n):
    ans = identity(len(a), a[0][0].prime)
    for _ in range(n):
        ans = mul(ans, a)
    return ans


def matrix_theta(a, shear):
    return [[z.theta(shear) for z in row] for row in a]


def whole_cover_checks():
    records = []
    for N in range(2, 9):
        p, _, q = field(N)
        zeta = q*q % p
        u, v, c = generators(p)
        D, S = zero_matrix(N, p), zero_matrix(N, p)
        Sinv = zero_matrix(N, p)
        for j in range(N):
            D[j][j] = scalar(pow(zeta, j, p), p)
            S[(j+1) % N][j] = scalar(1, p)
            Sinv[j][(j+1) % N] = scalar(1, p)
        I = identity(N, p)
        assert mul(D, S) == matrix_scale(mul(S, D), scalar(zeta, p))
        assert matrix_pow(D, N) == I
        assert matrix_pow(S, N) == I
        K = matrix_scale(D, u)
        E = matrix_scale(S, v)
        Q = scalar(zeta, p)*c
        assert mul(K, E) == matrix_scale(mul(E, K), Q)
        assert matrix_pow(K, N) == matrix_scale(I, u**N)
        assert matrix_pow(E, N) == matrix_scale(I, v**N)
        p0 = zero_matrix(N, p)
        for r in range(N):
            p0 = add(p0, matrix_scale(matrix_pow(D, r), scalar(Fraction(1, N), p)))
        assert p0 == unit(N, 0, 0, p)
        for i in range(N):
            for j in range(N):
                eij = mul(mul(matrix_pow(S, i), p0), matrix_pow(Sinv, j))
                assert eij == unit(N, i, j, p)
        records.append({'level': N, 'whole_variable_quantum_torus_relation': True,
                        'exact_powers_and_all_matrix_units': True})
    return records


def matrix_base_checks():
    records = []
    for n in (2, 3, 5):
        u, v, c = generators()
        # A noncentral diagonal gauge: the finite construction extracts
        # G=V*u^(-1), so the remaining base map is Ad_u theta, not theta.
        V, Vi = identity(n), identity(n)
        V[0][0], Vi[0][0] = u, u**-1
        assert mul(V, Vi) == identity(n)
        for shear in (-2, 0, 3):
            alpha = lambda a: mul(mul(V, matrix_theta(a, shear)), Vi)
            G = zero_matrix(n)
            for i in range(n):
                G = add(G, mul(alpha(unit(n, i, 0)), unit(n, 0, i)))
            expected = matrix_scale(V, u**-1, left=False)
            assert G == expected
            Gi = matrix_scale(Vi, u)
            assert mul(G, Gi) == identity(n)
            for i in range(n):
                for j in range(n):
                    eij = unit(n, i, j)
                    assert mul(alpha(eij), G) == mul(G, eij)
            for value in (u, v, u**-2*v**3*c**-1, u+v):
                a = matrix_scale(identity(n), value)
                theta_residual = u*value.theta(shear)*u**-1
                rhs = mul(mul(G, matrix_scale(identity(n), theta_residual)), Gi)
                assert alpha(a) == rhs
            # theta is an exact automorphism of the quantum torus.
            tu, tv = u.theta(shear), v.theta(shear)
            assert tu*tv == c*tv*tu
            records.append({'matrix_size': n, 'base_shear': shear,
                            'finite_matrix_unit_intertwiner': True,
                            'noncentral_gauge_changes_quantum_base': True})
    return records


def phase_and_source_checks():
    k1, e1, k2, f2 = s.symbols('k1 e1 k2 f2', nonzero=True)
    variables = (k1, e1, k2, f2)
    bracket = lambda F, G: k1*e1*(s.diff(F, k1)*s.diff(G, e1)
                                  - s.diff(F, e1)*s.diff(G, k1)) \
        - k2*f2*(s.diff(F, k2)*s.diff(G, f2)-s.diff(F, f2)*s.diff(G, k2))
    X = -e1*f2
    D = 1-X
    S = s.polylog(2, X)
    # Replace Li_1(z) explicitly so the audit uses the marked log derivative.
    deriv = {z: s.diff(S, z).replace(s.polylog(1, X), -s.log(D))
             for z in variables}
    Sbracket = lambda G: k1*e1*(deriv[k1]*s.diff(G, e1)-deriv[e1]*s.diff(G, k1)) \
        -k2*f2*(deriv[k2]*s.diff(G, f2)-deriv[f2]*s.diff(G, k2))
    assert s.simplify(Sbracket(k1)-k1*s.log(D)) == 0
    assert s.simplify(Sbracket(k2)+k2*s.log(D)) == 0
    assert Sbracket(e1) == Sbracket(f2) == Sbracket(X) == 0
    # The displayed Hamiltonian map preserves the nonzero brackets.
    kp1, kp2 = k1*D, k2/D
    assert s.simplify(bracket(kp1, e1)-kp1*e1) == 0
    assert s.simplify(bracket(kp2, f2)+kp2*f2) == 0
    assert s.simplify(bracket(kp1, kp2)) == 0
    # Check the full six-center map without restricting the two Casimirs.
    ff1, ee2 = s.symbols('f1 e2', nonzero=True)
    six = (k1, e1, ff1, k2, ee2, f2)
    P = s.zeros(6)
    for off in (0, 3):
        kk, ee, ff = six[off:off+3]
        P[off, off+1] = kk*ee
        P[off, off+2] = -kk*ff
        P[off+1, off+2] = 1/kk-kk
    P = P-P.T
    images = s.Matrix((kp1, e1, ff1+f2*k1-f2/(k1*D),
                       kp2, ee2+e1/k2-e1*k2/D, f2))
    jacobian = images.jacobian(six)
    transported = jacobian*P*jacobian.T
    target = P.subs(dict(zip(six, images)), simultaneous=True)
    for row in range(6):
        for col in range(6):
            assert s.cancel(transported[row, col]-target[row, col]) == 0
    for off in (0, 3):
        kk, ee, ff = six[off:off+3]
        kt, et, ft = images[off:off+3]
        assert s.cancel(et*ft-kt-1/kt-(ee*ff-kk-1/kk)) == 0
    J = s.Matrix([[0, 1], [-1, 0]])
    Gamma = s.ones(2)/2
    assert J.det() == 1
    assert s.trace(Gamma*J) == 0
    assert J*Gamma-Gamma*J != s.zeros(2)
    psi, phi = s.ones(2, 1), s.ones(1, 2)/2
    assert (phi*psi)[0] == 1
    assert (phi*J*psi)[0] == 0
    return {'actual_resonant_Hamiltonian_clock_fields': True,
            'full_six_center_time_one_map_is_Poisson': True,
            'both_Casimirs_are_preserved': True,
            'smooth_invertible_transport_can_have_zero_selected_cut': True,
            'selected_source_coupon_residual_is_nonzero': True}


def main():
    result = {'whole_quantum_matrix_cover': whole_cover_checks(),
              'matrix_base_splitting': matrix_base_checks(),
              'phase_and_pointing': phase_and_source_checks(),
              'scope': 'Local exact matrix/base transport and explicit source obstruction; no selected-period or volume assertion.'}
    target = Path(__file__).with_name('quantum_matrix_base_intertwiner_torsor_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'whole_cover_levels': len(result['whole_quantum_matrix_cover']),
                      'noncommutative_split_cases': len(result['matrix_base_splitting']),
                      'phase_and_source': 'passed'}))


if __name__ == '__main__':
    main()
