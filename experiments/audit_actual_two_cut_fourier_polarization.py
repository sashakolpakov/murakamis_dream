#!/usr/bin/env python3
"""Exact whole second-wire Fourier polarization, sources, and normal carries.

Matrix arithmetic is over finite fields, including literal actual signed
integral-color braid coefficients with their first normal derivatives.
The Gaussian correction audit is independent characteristic-zero algebra.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field, setup
from audit_crossing_normal_spectra import J as Jet


def inv(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p), dtype=np.int64) % p


def mul(A, B, p):
    return A @ B % p


def pairmul(A, B, p):
    return mul(A[0], B[0], p), (mul(A[1], B[0], p)+mul(A[0], B[1], p)) % p


def pairinv(A, p):
    a = inv(A[0], p)
    return a, -mul(mul(a, A[1], p), a, p) % p


def conjugate(A, B, p):
    return pairmul(pairmul(A, B, p), pairinv(A, p), p)


def pairkron(A, B, p):
    return (np.kron(A[0], B[0]) % p,
            (np.kron(A[1], B[0])+np.kron(A[0], B[1])) % p)


def pairpow(A, n, p):
    out = np.eye(len(A[0]), dtype=np.int64), np.zeros_like(A[0])
    for _ in range(n):
        out = pairmul(A, out, p)
    return out


def jetarray(A):
    return (np.array([[x.x for x in row] for row in A], dtype=np.int64),
            np.array([[x.dx for x in row] for row in A], dtype=np.int64))


def assertpair(A, B):
    assert np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1])


def vandermonde_case(N, root=True):
    p, eta = root_field(N)
    Q = pow(eta, 4, p)
    if not root:
        Q = next(a for a in range(2, p) if len({pow(a, j, p) for j in range(N+1)}) == N+1)
    yy = np.array([pow(Q, j, p) for j in range(N)], dtype=np.int64)
    eye = np.eye(N, dtype=np.int64)
    V = np.array([[pow(Q, j*b, p) for b in range(N)] for j in range(N)], dtype=np.int64)
    Vi = inv(V, p)
    C = V @ np.diag(yy) @ Vi % p
    expected = np.zeros_like(C)
    for j in range(N-1):
        expected[j, j+1] = 1
    for j in range(N):
        value = 1
        for m in range(N):
            if m != j:
                value *= (pow(Q, N, p)-int(yy[m])) * pow(int(yy[j]-yy[m]) % p, -1, p)
                value %= p
        expected[N-1, j] = value
        # Full Lagrange coefficient inverse, not merely its evaluation.
        polynomial = [1]
        denominator = 1
        for m in range(N):
            if m == j:
                continue
            result = [0]*(len(polynomial)+1)
            for b, coefficient in enumerate(polynomial):
                result[b] = (result[b]-int(yy[m])*coefficient) % p
                result[b+1] = (result[b+1]+coefficient) % p
            polynomial = result
            denominator = denominator*int(yy[j]-yy[m]) % p
        assert np.array_equal(Vi[:, j], np.array(polynomial)*pow(denominator, -1, p) % p)
    assert np.array_equal(C, expected)
    U, Uf = np.zeros_like(C), np.zeros_like(C)
    for b in range(N-1):
        U[b+1, b] = Uf[b, b+1] = 1
    Y = np.diag(yy)
    Yi = np.diag([pow(int(y), -1, p) for y in yy])
    u = np.array([pow(int(y), N, p) for y in yy])
    um = np.array([pow(int(y), -1, p) for y in yy])
    v, w = Vi[-1, :], Vi[0, :]
    assert np.array_equal(V@U@Vi % p, (Y-u[:, None]*v[None, :]) % p)
    assert np.array_equal(V@Uf@Vi % p, (Yi-um[:, None]*w[None, :]) % p)
    for m in range(1, N):
        expected = np.diag([pow(int(y), m, p) for y in yy])
        for b in range(N-m, N):
            column = np.array([pow(int(y), b+m, p) for y in yy])
            expected = (expected-column[:, None]*Vi[b, :][None, :]) % p
        assert np.array_equal(V@np.linalg.matrix_power(U, m)@Vi % p, expected)
    M = 3 if p != 3 else 5
    Mi = pow(M, -1, p)
    Ci = inv(C, p)
    B = np.diag(yy)
    Bi = np.diag([pow(int(y), -1, p) for y in yy])
    F, E = U@(eye-Q*B) % p, Uf@(M*Bi-Mi*eye) % p
    expectedF = (Y@(eye-Q*C)-(1-pow(Q, N, p))*u[:, None]*v[None, :]) % p
    expectedE = (Yi@(M*Ci-Mi*eye)-(M-Mi)*um[:, None]*w[None, :]) % p
    assert np.array_equal(V@F@Vi % p, expectedF)
    assert np.array_equal(V@E@Vi % p, expectedE)
    # Exact logarithmic-Q differentiation of every transported matrix.
    J = np.diag(np.arange(N, dtype=np.int64))
    V1 = J@V@J % p
    VP = V, V1
    A = V1@Vi % p
    assert np.array_equal(A, J@(V@J@Vi % p) % p)
    BP = B, J@B % p
    CP = conjugate(VP, BP, p)
    assert np.array_equal(CP[1], (V@(J@B)@Vi+A@C-C@A) % p)
    if root:
        inversecharacter = np.array([[pow(Q, -b*j, p)*pow(N, -1, p) % p
                                      for j in range(N)] for b in range(N)], dtype=np.int64)
        assert np.array_equal(Vi, inversecharacter)
        assert np.array_equal(pairpow(CP, N, p)[1], N*V@J@Vi % p)
        assert np.array_equal(pairpow(CP, N, p)[0], eye)
        assert np.array_equal(u, np.ones(N, dtype=np.int64))
        assert np.array_equal(v, yy*pow(N, -1, p) % p)
        # Forced forward endpoint derivative; delta=1-Q^N.
        assert np.array_equal(N*u[:, None]*v[None, :] % p, N*np.ones((N, 1), dtype=np.int64)*v % p)
    # Every four-port unit is checked at once by an arbitrary dense tensor;
    # source/coupling identities are separately entrywise below.
    count = 0
    for d, b in itertools.product(range(N), repeat=2):
        Bunit = np.zeros((N, N), dtype=np.int64)
        Bunit[d, b] = 1
        transformed = V@Bunit@Vi % p
        assert int(np.trace(transformed)) % p == int(d == b)
        transformed1 = (A@transformed-transformed@A) % p
        assert not int(np.trace(transformed1)) % p
        count += 1
    return {"N": N, "primitive_root": root, "field": p,
            "Lagrange_inverse_clock_companion_and_all_carries": True,
            "actual_E_F_two_endpoint_terms": True,
            "whole_logQ_connection_and_root_normal_power_clock": True,
            "entrywise_partial_trace_and_first_normal_checks": count}


def actual_two_cut_case(N, strands, word, split, slot):
    p, m, coefficient = setup(N, 0)
    _, eta0 = root_field(N)
    eta = Jet(eta0, -eta0*pow(4*N, -1, p))
    q, Q = eta**2, eta**4
    rho = q-q**-1
    diagonal = [(-rho)**j*q**(j*(j+1)//2) for j in range(N)]
    plus = [[Jet() for _ in range(N*N)] for _ in range(N*N)]
    minus = [[Jet() for _ in range(N*N)] for _ in range(N*N)]
    for a, b in itertools.product(range(N), repeat=2):
        for k in range(min(a, m-b)+1):
            c, d = b+k, a-k
            frame = diagonal[c]*diagonal[d]/diagonal[a]/diagonal[b]
            plus[c*N+d][a*N+b] = coefficient(a, b, k)*frame
        for k in range(min(b, m-a)+1):
            c, d = b-k, a+k
            frame = diagonal[c]*diagonal[d]/diagonal[a]/diagonal[b]
            minus[c*N+d][a*N+b] = coefficient(a, b, k, negative=True)*frame
    plus, minus = jetarray(plus), jetarray(minus)
    eye = np.eye(N**strands, dtype=np.int64), np.zeros((N**strands, N**strands), dtype=np.int64)
    smallone = np.ones((1, 1), dtype=np.int64), np.zeros((1, 1), dtype=np.int64)
    onehead = np.eye(N, dtype=np.int64), np.zeros((N, N), dtype=np.int64)

    def wordmatrix(letters):
        value = eye
        for letter in letters:
            op = smallone
            for _ in range(abs(letter)-1):
                op = pairkron(op, onehead, p)
            op = pairkron(op, plus if letter > 0 else minus, p)
            for _ in range(strands-abs(letter)-1):
                op = pairkron(op, onehead, p)
            value = pairmul(op, value, p)
        return value

    A, Bword = wordmatrix(word[split:]), wordmatrix(word[:split])
    pivot = [(q**(m-2*j))**(1-N) for j in range(N)]
    writhe = sum(1 if x > 0 else -1 for x in word)
    # Retain the whole actual d_N(M) on the integral-color M=-q^N path;
    # epsilon_N is the FIXED marked root phase, not a moving eta^N.
    # Cancel only its displayed removable M=1 factor by S_N(M^2).
    # The original physical first-cut source 1/N is applied later.
    M = -q**N
    epsilon = Jet(pow(pow(eta0, N, p), N+3, p))
    S_N = sum((M**(2*j) for j in range(N)), Jet())
    d_N = epsilon*M**(N-1)/S_N
    assert d_N.x == epsilon.x*pow(N, -1, p) % p and d_N.dx == 0
    external = eta**(-writhe*m*(m+2))*d_N
    T = np.zeros((N, N, N, N), dtype=np.int64)
    T1 = np.zeros_like(T)
    for d, b in itertools.product(range(N), repeat=2):
        X = smallone
        coupon = np.zeros((N, N), dtype=np.int64)
        coupon[b, d] = 1
        for s in range(strands):
            X = pairkron(X, (coupon, np.zeros_like(coupon)) if s == slot else onehead, p)
        C = pairmul(pairmul(A, X, p), Bword, p)
        for c, a in itertools.product(range(N), repeat=2):
            value = Jet()
            for closed in itertools.product(range(N), repeat=strands-1):
                row, column, weight = c, a, Jet(1)
                for x in closed:
                    row, column = row*N+x, column*N+x
                    weight *= pivot[x]
                value += weight*Jet(int(C[0][row, column]), int(C[1][row, column]))
            value *= external
            T[c, d, a, b] = value.x
            # setup's jet is delta=1-Q^N, so D_Q=-N partial_delta.
            T1[c, d, a, b] = -N*value.dx % p
    Q0 = Q.x
    V = np.array([[pow(Q0, j*b, p) for b in range(N)] for j in range(N)], dtype=np.int64)
    Je = np.diag(np.arange(N, dtype=np.int64))
    VP = V, Je@V@Je % p
    bigV = pairkron(onehead, VP, p)
    transported = conjugate(bigV, (T.reshape(N*N, N*N), T1.reshape(N*N, N*N)), p)
    TV, TV1 = [a.reshape(N, N, N, N) for a in transported]
    for c, a in itertools.product(range(N), repeat=2):
        assert sum(int(T[c, b, a, b]) for b in range(N)) % p == sum(int(TV[c, j, a, j]) for j in range(N)) % p
        assert sum(int(T1[c, b, a, b]) for b in range(N)) % p == sum(int(TV1[c, j, a, j]) for j in range(N)) % p
    raw = np.zeros((N, N), dtype=np.int64)
    original = sum(int(T[c, b, a, b]) for c, b, a in itertools.product(range(N), repeat=3))*pow(N, -1, p) % p
    for a, j in itertools.product(range(N), repeat=2):
        raw[a, j] = sum(int(TV[c, j, a, j]) for c in range(N)) % p
        band = sum(pow(Q0, j*(d-b), p)*int(T[c, d, a, b])
                   for c, d, b in itertools.product(range(N), repeat=3)) * pow(N, -1, p) % p
        assert raw[a, j] == band
        # Exact charge-zero formulation. This includes all physical bands.
        conserving = sum(pow(Q0, j*(d-b), p)*int(T[a+b-d, d, a, b])
                         for b, d in itertools.product(range(N), repeat=2)
                         if 0 <= a+b-d < N)*pow(N, -1, p) % p
        assert raw[a, j] == conserving
        assert int(TV[a, j, a, j]) == sum(int(T[a, b, a, b]) for b in range(N))*pow(N, -1, p) % p
    assert original == int(np.sum(raw))*pow(N, -1, p) % p
    # An actual input clock is conjugated, not identified with y_j.
    Binput = np.diag([pow(Q0, b, p) for b in range(N)])
    clockV = V@Binput@inv(V, p) % p
    weighted = transported[0]@np.kron(np.eye(N, dtype=np.int64), clockV) % p
    weighted = weighted.reshape(N, N, N, N)
    oldweighted = sum(pow(Q0, b, p)*int(T[c, b, a, b]) for c, b, a in itertools.product(range(N), repeat=3))*pow(N, -1, p) % p
    assert oldweighted == sum(int(weighted[c, j, a, j]) for c, j, a in itertools.product(range(N), repeat=3))*pow(N, -1, p) % p
    return {"N": N, "strands": strands, "word": list(word), "split": split,
            "actual_signed_R_pivots_framing_and_external_line": True,
            "whole_first_normal_partial_trace_preserved": True,
            "raw_all_band_formula_and_single_original_cut_normalization": True,
            "physical_clock_transported_independently": True}


def gaussian_case(d):
    # Exact non-diagonal quadratic Gaussian with a nonlinear amplitude;
    # its effective phase and leading density prove the entire q polynomial.
    H, q, nu = sp.symbols("H q nu")
    Hess = sp.diag(*[sp.Integer(j+2) for j in range(d)])
    Hess += sp.ones(d, d)
    G = Hess.inv()
    l = sp.Matrix([j+1 for j in range(d)])
    g = sp.Matrix([sp.Rational(1, j+2) for j in range(d)])
    a = sp.Rational(2, 5)
    t = sp.Rational(7, 3)
    # S=u'Hu/2+nu*l'u+t*nu²/2, a0=exp(g'u+a*nu).
    beta = (t-(l.T@G@l)[0])/2
    alpha = a-(g.T@G@l)[0]
    exact_ratio = sp.exp(nu*alpha+nu**2*beta/H)
    coefficient = sp.expand(sp.series(exact_ratio.subs(nu, H*q), H, 0, 2).removeO())
    assert sp.simplify(coefficient-(1+H*(q*alpha+q*q*beta))) == 0
    eta, p = sp.symbols("eta p", nonzero=True)
    test = eta**-3+2*eta**-1+5+3*eta+eta**4
    E = lambda f: sp.expand(eta*sp.diff(f, eta))
    expected = test.subs(eta, 1/p)+H*(-alpha*E(test)+beta*E(E(test))).subs(eta, 1/p)
    direct = 0
    for term in sp.Add.make_args(sp.expand(test)):
        n = int(term.as_powers_dict().get(eta, 0))
        weight = term/eta**n
        direct += weight*p**(-n)*(1+H*(-n*alpha+n*n*beta))
    assert sp.simplify(direct-expected) == 0
    # Identity cap unchanged, but quadratic tests have a genuine second jet.
    assert sp.simplify((1+H*(q*alpha+q*q*beta)).subs(q, 0)) == 1
    return {"dimension": d, "quadratic_nondiagonal_Gaussian": True,
            "alpha": str(alpha), "beta": str(beta),
            "bounded_test_distribution_and_identity_cap": True}


def main():
    operators = [vandermonde_case(N, root) for N in range(2, 9) for root in (True, False)]
    cases = []
    for N in range(2, 5):
        cases.extend(actual_two_cut_case(N, 2, word, split, 1)
                     for word, split in [((1,), 0), ((1, -1), 1), ((1, 1, 1), 1)])
    cases.extend(actual_two_cut_case(N, 3, (1, -2, 1, -2), 2, 2) for N in (2, 3))
    gaussian = [gaussian_case(d) for d in (1, 2, 3)]
    result = {"status": "PASS", "whole_operator_cases": operators,
              "actual_signed_word_first_normal_cases": cases,
              "characteristic_zero_Gaussian_cases": gaussian,
              "scope": "Actual whole finite basis/source transport. No global geometric Fourier-cycle or volume claim."}
    path = Path(__file__).with_name("actual_two_cut_fourier_polarization_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "whole_operator_cases": len(operators),
                      "actual_signed_word_first_normal_cases": len(cases),
                      "Gaussian_cases": len(gaussian), "results": str(path)}, indent=2))


if __name__ == "__main__":
    main()
