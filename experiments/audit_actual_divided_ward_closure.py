#!/usr/bin/env python3
"""Actual divided pivotal caps and weighted universal-R Green currents.

Uses literal integral Gaussian matrices; no guessed primitive Fr coproduct.
Pairs record value and q-log derivative, including both pivotal routes.
"""

import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_finite_sum_annihilator import field
from audit_high_integral_color_frobenius_source import gaussian_Q_dual_factory
from audit_high_color_first_normal_r_degree import setup, root_field
from audit_degree_elevation_complement_wall import modular_inverse
from audit_high_color_all_normal_filtration import setup as all_normal_setup


def add(a, b, p):
    return tuple((x+y) % p for x, y in zip(a, b))


def neg(a, p):
    return tuple(-x % p for x in a)


def sub(a, b, p):
    return add(a, neg(b, p), p)


def mul(a, b, p):
    return a[0] @ b[0] % p, (a[1] @ b[0]+a[0] @ b[1]) % p


def scale(a, x, dx, p):
    return a[0]*x % p, (a[1]*x+a[0]*dx) % p


def kron(a, b, p):
    return np.kron(a[0], b[0]) % p, (np.kron(a[1], b[0])+np.kron(a[0], b[1])) % p


def const(a):
    return a.copy(), np.zeros_like(a)


def eye(n):
    return const(np.eye(n, dtype=np.int64))


def zero(n):
    return const(np.zeros((n, n), dtype=np.int64))


def eq(a, b):
    assert all(np.array_equal(x, y) for x, y in zip(a, b))


def qp(q, exponent, p):
    value = pow(q, exponent, p)
    return value, exponent*value % p


def kp(K, exponent, p):
    diagonal = np.diag(K[0])
    derivative = np.diag(K[1])
    x = np.array([pow(int(a), exponent, p) for a in diagonal], dtype=np.int64)
    dx = np.array([exponent*int(b)*pow(int(a), exponent-1, p) % p
                   for a, b in zip(diagonal, derivative)], dtype=np.int64)
    return np.diag(x), np.diag(dx)


def actual_module(N, r, q, p):
    m = N*(r+1)-1
    d = m+1
    Q = q*q % p
    choose = gaussian_Q_dual_factory(Q, p)
    E, F = [], []
    for a in range(N+1):
        ea, fa = zero(d), zero(d)
        for j in range(d):
            if j >= a:
                upper = m-j+a
                c, dc = choose(upper, a)
                weight, dweight = qp(q, -a*(upper-a), p)
                ea[0][j-a, j] = weight*c % p
                ea[1][j-a, j] = (dweight*c+weight*dc) % p
            if j+a < d:
                upper = j+a
                c, dc = choose(upper, a)
                weight, dweight = qp(q, -a*(upper-a), p)
                fa[0][j+a, j] = weight*c % p
                fa[1][j+a, j] = (dweight*c+weight*dc) % p
        E.append(ea)
        F.append(fa)
    K = (np.diag([pow(q, m-2*j, p) for j in range(d)]).astype(np.int64),
         np.diag([(m-2*j)*pow(q, m-2*j, p) % p for j in range(d)]).astype(np.int64))
    return m, E, F, K


def tensor_divided(E, F, K, n, q, p):
    dimension = len(K[0])**2
    DE, DF = zero(dimension), zero(dimension)
    for k in range(n+1):
        x, dx = qp(q, k*(n-k), p)
        DE = add(DE, scale(kron(E[n-k], mul(E[k], kp(K, n-k, p), p), p), x, dx, p), p)
        x, dx = qp(q, -k*(n-k), p)
        DF = add(DF, scale(kron(mul(kp(K, -k, p), F[n-k], p), F[k], p), x, dx, p), p)
    return DE, DF


def adjoint(divided, K, n, C, q, p, kind):
    result = zero(len(C[0]))
    for k in range(n+1):
        if kind == "E":
            term = mul(mul(mul(divided[n-k], C, p), divided[k], p), kp(K, -n, p), p)
            exponent = -k*(n-1)
        else:
            term = mul(mul(mul(mul(divided[n-k], kp(K, -k, p), p), C, p),
                           kp(K, k, p), p), divided[k], p)
            exponent = k*(n-1)
        x, dx = qp(q, exponent, p)
        result = add(result, scale(term, (-1)**k*x % p, (-1)**k*dx % p, p), p)
    return result


def ptr(C, g, d, p):
    values = []
    for order in range(2):
        out = np.zeros((d, d), dtype=np.int64)
        for i in range(d):
            for j in range(d):
                for a in range(d):
                    out[i, j] += C[order][i*d+a, j*d+a]*g[0][a, a]
                    if order:
                        out[i, j] += C[0][i*d+a, j*d+a]*g[1][a, a]
        values.append(out % p)
    return tuple(values)


def cap_case(N, r, generic):
    p, generator, root = field(N)
    q = generator if generic else root
    m, E, F, K = actual_module(N, r, q, p)
    d = m+1
    DE, DF = [], []
    for n in range(N+1):
        a, b = tensor_divided(E, F, K, n, q, p)
        DE.append(a)
        DF.append(b)
    KT = kron(K, K, p)
    # A deterministic dense actual End(V tensor V) test matrix.
    C = const(np.array([[(3*i+7*j+i*j+2) % p for j in range(d*d)]
                        for i in range(d*d)], dtype=np.int64))
    frozen = kp(K, 1-N, p)
    Zclock = kp(K, -N, p)
    tau = (-1)**(N*r-1)
    HFr = scale(sub(mul(E[N], F[N], p), mul(F[N], E[N], p), p), tau, 0, p)
    assert all(not np.any(X-np.diag(np.diag(X))) for X in HFr)
    cut = (C[0][:d, :d].copy(), C[0][d:2*d, d:2*d].copy())
    commutator = sub(mul(HFr, cut, p), mul(cut, HFr, p), p)
    # Exact whole diagonal unit on every retained head entry. No source
    # or matrix coefficient is discarded when the inverse row is taken.
    for i in range(N):
        for j in range(N):
            row, column = r*N+i, j
            lam = (HFr[0][row, row]-HFr[0][column, column]) % p
            dlam = (HFr[1][row, row]-HFr[1][column, column]) % p
            assert lam
            inverse, dinverse = pow(int(lam), -1, p), -int(dlam)*pow(int(lam), -2, p) % p
            assert inverse*commutator[0][row, column] % p == cut[0][row, column]
            assert (inverse*commutator[1][row, column]+dinverse*commutator[0][row, column]) % p == cut[1][row, column]
    if not generic:
        expected_H = np.diag([r-2*(j//N) for j in range(d)]).astype(np.int64) % p
        assert np.array_equal(HFr[0], expected_H)
        correction = (HFr[1] @ cut[0]-cut[0] @ HFr[1]) % p
        wall = np.s_[r*N:(r+1)*N, :N]
        assert np.array_equal(commutator[0][wall], -2*r*cut[0][wall] % p)
        assert np.array_equal((commutator[1]-correction)[wall] % p, -2*r*cut[1][wall] % p)
    for kind, D, DT in (("E", E, DE), ("F", F, DF)):
        ad = lambda X: adjoint(DT, KT, N, X, q, p, kind)
        adcut = lambda X: adjoint(D, K, N, X, q, p, kind)
        eq(ptr(ad(C), K, d, p), adcut(ptr(C, K, d, p)))
        # Exact WHOLE frozen cap commutator, including its derivative.
        actual = sub(ptr(ad(C), frozen, d, p), adcut(ptr(C, frozen, d, p)), p)
        zleft = kron(eye(d), Zclock, p)
        predicted = ptr(sub(mul(zleft, ad(C), p), ad(mul(zleft, C, p)), p), K, d, p)
        eq(actual, predicted)
        if not generic:
            assert not np.any(actual[0])
            # Root adapter scalar chi^-1, z'_qlog=-N H chi^-1.
            leading = kron(eye(d), const(Zclock[1]), p)
            C0 = const(C[0])
            rootcomm = ptr(sub(mul(leading, ad(C0), p), ad(mul(leading, C0, p)), p), K, d, p)[0]
            assert np.array_equal(actual[1], rootcomm)
    # Direct small-generator cap rows, with their q-log derivatives.
    AEtot = adjoint(DE, KT, 1, C, q, p, "E")
    AFtot = adjoint(DF, KT, 1, C, q, p, "F")
    capE = sub(ptr(AEtot, frozen, d, p), adjoint(E, K, 1, ptr(C, frozen, d, p), q, p, "E"), p)
    rE = sub(mul(kp(K, -1, p), mul(frozen, E[1], p), p),
             mul(E[1], mul(kp(K, -1, p), frozen, p), p), p)
    predE = mul(ptr(mul(kron(eye(d), rE, p), C, p), eye(d), d, p), kp(K, -1, p), p)
    eq(capE, predE)
    capF = sub(ptr(AFtot, frozen, d, p), adjoint(F, K, 1, ptr(C, frozen, d, p), q, p, "F"), p)
    rF = sub(mul(frozen, F[1], p), mul(mul(mul(K, F[1], p), frozen, p), kp(K, -1, p), p), p)
    predF = mul(kp(K, -1, p), ptr(mul(kron(eye(d), rF, p), C, p), eye(d), d, p), p)
    eq(capF, predF)
    return {"N": N, "r": r, "generic_q": generic, "prime": p,
            "ordinary_mixed_divided_cap_exact_through_first_normal": True,
            "actual_divided_Cartan_extreme_wall_and_normal_correction_exact": not generic,
            "whole_actual_Cartan_entrywise_wall_unit_and_source_row_exact": True,
            "whole_frozen_clock_adapter_and_cap_rows_exact": True,
            "root_divided_cap_zero_first_normal_commutator_retained": not generic}


def actual_crossing_case(N):
    r = 1
    p, highest, coefficient = setup(N, r)
    same_prime, halfroot = root_field(N)
    assert same_prime == p
    q = halfroot*halfroot % p
    m, E, F, K = actual_module(N, r, q, p)
    d, size = m+1, (m+1)**2
    # setup uses the constant beta frame and delta derivative: transport
    # to the literal integral basis used for the divided cap check.
    beta = [(-1)**(N*a*(a-1)//2+a*s) for a in range(r+1) for s in range(N)]
    components = [zero(size) for _ in range(m+1)]
    for i in range(d):
        for j in range(d):
            for k in range(min(i, m-j)+1):
                value = coefficient(i, j, k)
                row, column = (j+k)*d+i-k, i*d+j
                sign = beta[i]*beta[j]*beta[j+k]*beta[i-k]
                components[k][0][row, column] = sign*value.x % p
                components[k][1][row, column] = -2*N*sign*value.dx % p
    R = zero(size)
    for X in components:
        R = add(R, X, p)
    inv0 = modular_inverse(R[0], p)
    inverse = inv0, -inv0 @ R[1] @ inv0 % p
    negative = [zero(size) for _ in range(m+1)]
    for row in range(size):
        c, dd = divmod(row, d)
        for column in range(size):
            a, b = divmod(column, d)
            k = b-c
            if 0 <= k <= m and dd == a+k:
                for order in range(2):
                    negative[k][order][row, column] = inverse[order][row, column]
    eq(sum_pairs(negative, p), inverse)
    DE, DF = tensor_divided(E, F, K, N, q, p)
    # Test both actual signed crossings and actual divided coproducts.
    for H in (DE, DF):
        for pieces in (components, negative):
            eq(mul(H, sum_pairs(pieces, p), p), mul(sum_pairs(pieces, p), H, p))
            weight = 3
            weighted, current = zero(size), zero(size)
            for k, X in enumerate(pieces):
                weighted = add(weighted, scale(X, pow(weight, k, p), 0, p), p)
                geom = sum(pow(weight, j, p) for j in range(k)) % p
                current = add(current, scale(sub(mul(H, X, p), mul(X, H, p), p), geom, 0, p), p)
            eq(sub(mul(H, weighted, p), mul(weighted, H, p), p), scale(current, weight-1, 0, p))
        # Whole +/-/+ word and a genuinely nonconstant actual moment.
        # p(k)=k0*k1+k2^2, Delta_t p is evaluated at the CURRENT exponent.
        lists = (components, negative, components)
        moment, rhs = zero(size), zero(size)
        for indices in itertools.product(range(m+1), repeat=3):
            Xs = [lists[t][indices[t]] for t in range(3)]
            product = mul(Xs[2], mul(Xs[1], Xs[0], p), p)
            polynomial = indices[0]*indices[1]+indices[2]**2
            moment = add(moment, scale(product, polynomial, 0, p), p)
            for t, k in enumerate(indices):
                Xi = sub(mul(H, Xs[t], p), mul(Xs[t], H, p), p)
                product_current = eye(size)
                for s in range(3):
                    product_current = mul(Xi if s == t else Xs[s], product_current, p)
                for lower in range(k):
                    exponents = list(indices)
                    exponents[t] = lower
                    delta_polynomial = (exponents[1] if t == 0 else exponents[0] if t == 1 else 2*lower+1)
                    rhs = add(rhs, scale(product_current, delta_polynomial, 0, p), p)
        eq(sub(mul(H, moment, p), mul(moment, H, p), p), rhs)
    return {"N": N, "r": r, "actual_full_matrix_dimension": size,
            "signed_weighted_integral_divided_currents_exact": True,
            "whole_three_crossing_Green_finite_difference_exact": True,
            "full_Cartan_beta_and_first_normal_retained": True}


def sum_pairs(values, p):
    result = zero(len(values[0][0]))
    for value in values:
        result = add(result, value, p)
    return result


def actual_closed_wall_return(N):
    p, m, coefficient, _, _, _ = all_normal_setup(N, N, order=N)
    _, eta = root_field(N)
    q = eta*eta % p
    transfer = N*N
    value = coefficient(transfer, 0, transfer)
    expected = pow(N, N, p)*math.factorial(N)*pow(eta, m*(m-2*transfer), p) % p
    assert not any(value.c[:N])
    assert value.c[N] == expected
    ordinary_pivot = pow(q, m-2*transfer, p)
    frozen_pivot = pow(q, (1-N)*(m-2*transfer), p)
    assert expected*ordinary_pivot % p
    assert expected*frozen_pivot % p
    assert frozen_pivot == pow(q, -N*m, p)*ordinary_pivot % p
    return {"N": N, "r": N, "actual_high_color_dimension": m+1,
            "actual_closed_wall_first_nonzero_normal_order": N,
            "full_Cartan_and_both_pivotal_leading_coefficients_exact": True}


def main():
    caps = [cap_case(N, r, generic) for N, r in ((2, 1), (2, 2), (3, 1)) for generic in (False, True)]
    crossings = [actual_crossing_case(N) for N in (2, 3)]
    returning = [actual_closed_wall_return(N) for N in range(2, 6)]
    result = {"actual_integral_cap_cases": caps, "actual_signed_crossing_word_cases": crossings,
              "actual_closed_wall_return": returning,
              "scope": "Exact current/source and pivotal adapters; no geometric Gaussian comparison or volume claim."}
    target = Path(__file__).with_name("actual_divided_ward_closure_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_cap_cases": len(caps),
                      "actual_crossing_word_cases": len(crossings),
                      "actual_closed_wall_return_cases": len(returning), "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
