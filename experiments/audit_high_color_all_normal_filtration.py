#!/usr/bin/env python3
"""Independent actual integral R/source jets through normal order three.

No singular factorial division is used: actual R entries use regular
Gaussian polynomials times [k]!. Shiftwise polynomial membership tests
are nonvacuous at r=8 and normal orders two and three.
"""

import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np

from audit_high_color_first_normal_r_degree import root_field, gauge, span_test


class Jet:
    p = 1009
    order = 3

    def __init__(self, coefficients=0):
        if isinstance(coefficients, Jet):
            self.c = coefficients.c
        elif isinstance(coefficients, int):
            self.c = (coefficients % self.p,)+(0,)*self.order
        else:
            values = tuple(int(v) % self.p for v in coefficients)
            self.c = (values+(0,)*(self.order+1))[:self.order+1]

    def __add__(self, other):
        other = Jet(other)
        return Jet([(a+b) % self.p for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Jet([-a for a in self.c])

    def __sub__(self, other):
        return self+-Jet(other)

    def __rsub__(self, other):
        return Jet(other)+-self

    def __mul__(self, other):
        other = Jet(other)
        return Jet([sum(self.c[j]*other.c[k-j] for j in range(k+1)) % self.p
                    for k in range(self.order+1)])

    __rmul__ = __mul__

    def inverse(self):
        assert self.c[0]
        inv = pow(self.c[0], -1, self.p)
        out = [inv]
        for k in range(1, self.order+1):
            out.append(-inv*sum(self.c[j]*out[k-j] for j in range(1, k+1)) % self.p)
        return Jet(out)

    def __truediv__(self, other):
        return self*Jet(other).inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse()**(-exponent)
        result, base = Jet(1), self
        while exponent:
            if exponent % 2:
                result = result*base
            base = base*base
            exponent //= 2
        return result


def setup(N, r, order=3):
    prime, eta0 = root_field(N)
    Jet.p, Jet.order = prime, order
    alpha = pow(4*N, -1, prime)
    coefficients, binomial = [eta0], 1
    for j in range(1, order+1):
        binomial = binomial*(alpha-j+1)*pow(j, -1, prime) % prime
        coefficients.append(eta0*binomial*((-1)**j) % prime)
    eta = Jet(coefficients)
    q, Q = eta**2, eta**4
    rho = q-q**-1
    m = N*(r+1)-1

    @lru_cache(None)
    def qp(exponent):
        return q**exponent

    @lru_cache(None)
    def etap(exponent):
        return eta**exponent

    @lru_cache(None)
    def Qp(exponent):
        return Q**exponent

    gaussian = [[Jet() for _ in range(m+1)] for _ in range(m+1)]
    gaussian[0][0] = Jet(1)
    for a in range(1, m+1):
        gaussian[a][0] = gaussian[a][a] = Jet(1)
        for k in range(1, a):
            gaussian[a][k] = gaussian[a-1][k]+Qp(a-k)*gaussian[a-1][k-1]
    fac = [Jet(1)]
    for k in range(1, m+1):
        fac.append(fac[-1]*(qp(k)-qp(-k))/rho)
    factors = [qp(k*(k-1)//2)*rho**k*fac[k] for k in range(m+1)]
    inverse_factors = [(-1)**k*qp(-k*(k-1)//2)*rho**k*fac[k] for k in range(m+1)]

    def coefficient(i, j, k, negative=False):
        if negative:
            if k > j or i+k > m:
                return Jet()
            value = inverse_factors[k]*qp(-k*(m-j))*gaussian[m-j+k][k]
            value *= qp(-k*i)*gaussian[i+k][k]
            value *= etap(-(m-2*i)*(m-2*j))
            return value*gauge(N, i)*gauge(N, j)*gauge(N, i+k)*gauge(N, j-k)
        if k > i or j+k > m:
            return Jet()
        value = factors[k]*qp(-k*(m-i))*gaussian[m-i+k][k]
        value *= qp(-k*j)*gaussian[j+k][k]
        value *= etap((m-2*(i-k))*(m-2*(j+k)))
        return value*gauge(N, i)*gauge(N, j)*gauge(N, i-k)*gauge(N, j+k)

    return prime, m, coefficient, gaussian, qp, fac


def actual_shift_filtration(N, r=8, order=3):
    prime, m, coefficient, _, _, fac = setup(N, r, order)
    epsilon = (-1)**m
    fit_cache = {}

    def contains(cE, cF, degree, values):
        if degree < 0:
            return not np.any(values)
        key = cE, cF, degree
        if key not in fit_cache:
            points = [(a, b) for a in range(cE, r+1) for b in range(r-cF+1)]
            vectors = [np.array([pow(a, i, prime)*pow(b, j, prime) % prime
                                 for a, b in points], dtype=np.int64)
                       for i in range(degree+1) for j in range(degree+1-i)]
            fit_cache[key] = span_test(vectors, prime)[0]
        return fit_cache[key](values)

    coefficient_checks = 0
    filtration_tests = 0
    sharp = set()
    for k in range(m+1):
        atrans, btrans = divmod(k, N)
        if atrans > order:
            assert not any(fac[k].c)
            continue
        for s in range(N):
            for t in range(N):
                cE = atrans+int(s < btrans)
                cF = atrans+int(t+btrans >= N)
                if max(cE, cF) > r:
                    continue
                valuation = cE+cF-atrans
                data = [[] for _ in range(order+1)]
                for a in range(cE, r+1):
                    for b in range(r-cF+1):
                        i, j = a*N+s, b*N+t
                        value = coefficient(i, j, k)
                        oa, _ = divmod(i-k, N)
                        ob, _ = divmod(j+k, N)
                        base = math.prod(r-a+1+h for h in range(cE))
                        base *= math.prod(b+h for h in range(1, cF+1))
                        inverse = pow(base % prime, -1, prime)
                        root_parity = epsilon**(oa+ob)
                        for normal in range(order+1):
                            data[normal].append(root_parity*value.c[normal]*inverse % prime)
                        coefficient_checks += order+1
                for normal in range(order+1):
                    values = np.array(data[normal], dtype=np.int64)
                    if normal < valuation:
                        assert not np.any(values), (N, r, k, s, t, normal, "valuation")
                    assert contains(cE, cF, 2*normal-cE-cF, values), (N, r, k, s, t, normal)
                    filtration_tests += 1
                    if k == 0 and s == t == 0 and normal in (2, 3):
                        assert not contains(0, 0, 2*normal-1, values)
                        sharp.add(normal)
    assert sharp == {2, 3}
    return {"N": N, "r": r, "prime": prime,
            "actual_coefficient_jet_checks": coefficient_checks,
            "nonvacuous_shiftwise_PBW_tests": filtration_tests,
            "sharp_normal_orders": sorted(sharp)}


def matrix_series_product(a, b, prime):
    order = len(a)-1
    return [sum((a[j] @ b[k-j] for j in range(k+1)), np.zeros_like(a[0])) % prime
            for k in range(order+1)]


def generators(r):
    e = np.zeros((r+1, r+1), dtype=np.int64)
    f = np.zeros_like(e)
    h = np.diag([r-2*k for k in range(r+1)]).astype(np.int64)
    for k in range(1, r+1):
        e[k-1, k], f[k, k-1] = r-k+1, k
    return e, f, h


def single_PBW_test(r, degree, prime):
    e, f, h = generators(r)
    eye = np.eye(r+1, dtype=np.int64)
    powers = {}
    for name, generator in (("e", e), ("f", f), ("h", h)):
        powers[name] = [eye]
        for _ in range(degree):
            powers[name].append(powers[name][-1] @ generator % prime)
    vectors = [(powers["e"][a] @ powers["h"][b] @ powers["f"][c] % prime).reshape(-1)
               for a in range(degree+1) for b in range(degree+1-a)
               for c in range(degree+1-a-b)]
    return span_test(vectors, prime)[0]


def actual_source_interactions(N, r=8, order=3):
    prime, m, _, gaussian, qp, _ = setup(N, r, order)
    e, f, _ = generators(r)
    tests = {j: single_PBW_test(r, 2*j, prime) for j in range(1, order+1)}
    raw_tests = {j: single_PBW_test(r, j+1, prime) for j in range(order+1)}
    count = 0
    for s in sorted({0, N//2, N-1}):
        for kind, root_generator in (("E", e), ("F", f)):
            matrices = [np.zeros((r+1, r+1), dtype=np.int64) for _ in range(order+1)]
            for a in range(r+1):
                index = a*N+s
                if kind == "E" and a:
                    upper, out = m-index+N, a-1
                    value = qp(-N*(upper-N))*gaussian[upper][N]
                    value *= gauge(N, index)*gauge(N, index-N)*((-1)**(N*r-1))
                elif kind == "F" and a < r:
                    upper, out = index+N, a+1
                    value = qp(-N*(upper-N))*gaussian[upper][N]
                    value *= gauge(N, index)*gauge(N, index+N)
                else:
                    continue
                for j in range(order+1):
                    matrices[j][out, a] = value.c[j]
            assert np.array_equal(matrices[0], root_generator % prime)
            for j in range(order+1):
                assert raw_tests[j](matrices[j].reshape(-1)), (N, s, kind, j, "raw divided")
            eye = np.eye(r+1, dtype=np.int64)
            exponential = [eye]+[np.zeros_like(eye) for _ in range(order)]
            power = [eye]+[np.zeros_like(eye) for _ in range(order)]
            root_exp_inverse = eye.copy()
            root_power = eye.copy()
            factorial = 1
            for n in range(1, r+1):
                power = matrix_series_product(power, matrices, prime)
                root_power = root_power @ (-root_generator) % prime
                factorial = factorial*n % prime
                inverse = pow(factorial, -1, prime)
                exponential = [(a+b*inverse) % prime for a, b in zip(exponential, power)]
                root_exp_inverse = (root_exp_inverse+root_power*inverse) % prime
            interaction = [root_exp_inverse @ coefficient % prime for coefficient in exponential]
            assert np.array_equal(interaction[0], eye)
            for j in range(1, order+1):
                assert tests[j](interaction[j].reshape(-1)), (N, s, kind, j, "source interaction")
                if kind == "F":
                    assert not np.any(interaction[j][2*j+1:, 0]), (N, s, j, "source descendants")
                else:
                    assert not np.any(interaction[j][0, 2*j+1:]), (N, s, j, "dual descendants")
                count += 1
    return {"N": N, "r": r, "prime": prime,
            "actual_source_operator_interaction_jets": count,
            "raw_divided_degree_j_plus_one_and_rotated_degree_2j": True,
            "rotated_source_dual_descendants_at_most_2j_plus_one": True}


def inverse_matrix_check(N=2, r=3, order=3):
    prime, m, coefficient, _, _, _ = setup(N, r, order)
    dimension = (m+1)**2
    positive = [np.zeros((dimension, dimension), dtype=np.int64) for _ in range(order+1)]
    negative = [np.zeros_like(positive[0]) for _ in range(order+1)]
    for i in range(m+1):
        for j in range(m+1):
            column = i*(m+1)+j
            for k in range(min(i, m-j)+1):
                value = coefficient(i, j, k)
                row = (i-k)*(m+1)+j+k
                for normal in range(order+1):
                    positive[normal][row, column] = value.c[normal]
            # coefficient(...,negative=True) uses the checked inverse's
            # input swap; undo it to compare the two UNCHECKED matrices.
            for k in range(min(i, m-j)+1):
                value = coefficient(j, i, k, negative=True)
                row = (i-k)*(m+1)+j+k
                for normal in range(order+1):
                    negative[normal][row, column] = value.c[normal]
    product = matrix_series_product(positive, negative, prime)
    assert np.array_equal(product[0], np.eye(dimension, dtype=np.int64))
    assert not any(np.any(matrix) for matrix in product[1:])
    return {"N": N, "r": r, "matrix_dimension": dimension,
            "actual_full_positive_negative_inverse_through_order": order}


def main():
    crossings = [actual_shift_filtration(N) for N in (2, 3, 4)]
    sources = [actual_source_interactions(N) for N in (2, 3, 4)]
    inverse = inverse_matrix_check()
    result = {"actual_crossing_normal_filtration": crossings,
              "actual_divided_source_rotations": sources,
              "full_crossing_inverse": inverse,
              "scope": "Exact tests through normal order3 supporting uniform all-order proof; no geometric source-current map."}
    target = Path(__file__).with_name("high_color_all_normal_filtration_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "crossing_cases": len(crossings),
                      "coefficient_jet_checks": sum(row["actual_coefficient_jet_checks"] for row in crossings),
                      "shiftwise_PBW_tests": sum(row["nonvacuous_shiftwise_PBW_tests"] for row in crossings),
                      "source_operator_jets": sum(row["actual_source_operator_interaction_jets"] for row in sources),
                      "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
