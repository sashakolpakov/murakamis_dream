#!/usr/bin/env python3
"""Finite exact checks for the signed bipyramid pair and +2 endpoint proofs.

Matrices and homogeneous monomials are constructed separately from the original
three-arrow face operator. Arithmetic is exact in recorded finite fields with
q of exact order 2N. These checks test indexing and polynomial identities, not
the complex norm inequalities, an asymptotic gap, or knot-volume equality.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


def field(N):
    p = int(sp.nextprime(2000))
    while (p-1) % (2*N):
        p = int(sp.nextprime(p))
    q = pow(int(sp.primitive_root(p)), (p-1)//(2*N), p)
    assert pow(q, 2*N, p) == 1
    assert all(pow(q, r, p) != 1 for r in sp.divisors(2*N)[:-1])
    return p, q


def plus(a, b, p):
    n = max(len(a), len(b))
    out = [np.zeros_like(a[0]) for _ in range(n)]
    for k, x in enumerate(a):
        out[k] += x
    for k, x in enumerate(b):
        out[k] += x
    return [x % p for x in out]


def multiply(a, b, p):
    out = [np.zeros_like(a[0]) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x@y) % p
    return out


def run_level(N):
    p, q = field(N)
    d, Q = N-1, q*q % p
    cpow = lambda r: pow(q, r, p)
    c = [(cpow(2*r+1)+cpow(-2*r-1)) % p for r in range(N)]
    aa = lambda r: (2-cpow(2*r)-cpow(-2*r)) % p
    bb = lambda r: (cpow(1)+cpow(-1)-cpow(2*r-1)-cpow(-2*r+1)) % p
    C0, C1 = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        C0[j, j] = c[j]
        if j:
            C0[j-1, j] = C1[j-1, j] = -aa(j) % p
        if j >= 2:
            C1[j-2, j] = -bb(j) % p
    x = sp.Symbol('x')
    chi = sp.Poly(2*sp.chebyshevt(N, x/2)+2, x)
    ch = [int(chi.nth(k)) % p for k in range(N+1)]
    chval = lambda t: sum(h*pow(t, k, p) for k, h in enumerate(ch)) % p
    I = np.eye(N, dtype=np.int64)
    powers = [[I]]
    for r in range(1, N+1):
        powers.append(multiply(powers[-1], [C0, C1], p))
    annihilator = [np.zeros_like(I)]
    for h, power in zip(ch, powers):
        annihilator = plus(annihilator, [h*A % p for A in power], p)
    assert all(not np.any(A) for A in annihilator)

    def fcoeff(t):
        return [sum(ch[k]*pow(t, k-1-r, p) for k in range(r+1, N+1)) % p
                for r in range(N)]

    def numerator(t):
        out = [np.zeros_like(I)]
        for h, power in zip(fcoeff(t), powers):
            out = plus(out, [h*A % p for A in power], p)
        return out

    # Independent homogeneous monomial recursion; no matrix-entry indexing
    # is used to form the four-face coefficient dictionary.
    def homogeneous(t):
        f = fcoeff(t)
        out = {}
        for j in range(N):
            state = {(0, j, 0): 1}  # outer-x, input-middle, outer-y
            for degree in range(N):
                for (a, i, b), value in state.items():
                    key = (a, i, d-j, b)
                    out[key] = (out.get(key, 0)+f[degree]*value) % p
                next_state = {}
                def add(key, value):
                    next_state[key] = (next_state.get(key, 0)+value) % p
                for (a, i, b), value in state.items():
                    add((a, i, b), c[i]*value)
                    if i:
                        add((a+1, i-1, b), -aa(i)*value)
                        add((a, i-1, b+1), -aa(i)*value)
                    if i >= 2:
                        add((a+1, i-2, b+1), -bb(i)*value)
                state = next_state
        return {key: value for key, value in out.items() if value}

    values = sorted(set([2, -2 % p, c[0]]))
    Vs, Hs = {t: numerator(t) for t in values}, {t: homogeneous(t) for t in values}
    coefficient_checks = 0
    for t in values:
        A, H = Vs[t], Hs[t]
        for i in range(N):
            for j in range(i, N):
                for a in range(j-i+1):
                    actual = int(A[a][i, j]) if a < len(A) else 0
                    assert actual == H.get((a, i, d-j, j-i-a), 0)
                    coefficient_checks += 1

    half, M = d//2, N//2-1
    pair_checks = 0
    spectra = [(2, -2 % p), (2, 2), (c[0], c[0])]
    for sigma, tau in spectra:
        top, bottom = Hs[sigma], Hs[tau]
        direct = {}
        for (a, i, cz, l), value in top.items():
            if a or i or l > M:
                continue
            for (sdegree, bi, cy, bz), other in bottom.items():
                j = d-cy
                if bi > half or j < N//2:
                    continue
                alpha, beta = d-(l+cy), d-(cz+bz)
                if 0 <= alpha <= d and 0 <= beta <= d:
                    key = (alpha, beta, bi, sdegree)
                    direct[key] = (direct.get(key, 0)+value*other) % p
        A, B = Vs[sigma][0], Vs[tau]
        for alpha in range(N):
            for beta in range(N):
                for sdegree in range(N):
                    i = alpha+beta-sdegree
                    if not 0 <= i <= half:
                        continue
                    L, U = max(0, beta, N//2-alpha), min(M, d-alpha)
                    actual = sum(int(A[0, l])*int(B[sdegree][i, l+alpha])
                                 for l in range(L, U+1)) % p
                    assert actual == direct.get((alpha, beta, i, sdegree), 0), (
                        N, sigma, tau, alpha, beta, i, sdegree)
                    pair_checks += 1

    current_checks = 0
    intervals = sorted(set([(0, d), (0, M), (M, M),
                            (max(0, N//2-2), min(d, N//2+1))]))
    for sigma, tau in spectra:
        A, B = Vs[sigma][0], Vs[tau]
        for L, U in intervals:
            for i in sorted(set([0, half, d])):
                def bval(row, col, degree):
                    if not (0 <= row < N and 0 <= col < N and 0 <= degree < N):
                        return 0
                    return int(B[degree][row, col])
                def vval(index):
                    return int(A[0, index]) if 0 <= index < N else 0
                cache = {}
                def K(alpha, degree, z):
                    if degree < 0:
                        return 0
                    key = (alpha, degree, z)
                    if key not in cache:
                        cache[key] = sum(pow(z, l, p)*vval(l)*bval(i, l+alpha, degree)
                                         for l in range(L, U+1)) % p
                    return cache[key]
                def clock_A(r, alpha, degree, z):
                    return (2*K(alpha, degree, z)
                            -cpow(2*r)*K(alpha, degree, z*Q % p)
                            -cpow(-2*r)*K(alpha, degree, z*pow(Q, -1, p) % p)) % p
                def clock_B(r, alpha, degree, z):
                    return ((cpow(1)+cpow(-1))*K(alpha, degree, z)
                            -cpow(2*r-1)*K(alpha, degree, z*Q % p)
                            -cpow(-2*r+1)*K(alpha, degree, z*pow(Q, -1, p) % p)) % p
                for alpha in sorted(set([0, 1, N//2, d])):
                    for degree in range(N):
                        for z in sorted(set([1, 2, Q])):
                            forcing = chval(sigma)*(L == 0)*bval(i, alpha, degree)
                            if degree == 0 and L <= i-alpha <= U:
                                forcing -= chval(tau)*pow(z, i-alpha, p)*vval(i-alpha)
                            ends = (-aa(L)*pow(z, L, p)*vval(L-1)*bval(i, L+alpha, degree)
                                    +aa(U+1)*pow(z, U+1, p)*vval(U)
                                    *bval(i, U+1+alpha, degree))
                            diag = (cpow(1)*(1-cpow(2*alpha))*K(alpha, degree, z*Q % p)
                                    +cpow(-1)*(1-cpow(-2*alpha))
                                    *K(alpha, degree, z*pow(Q, -1, p) % p))
                            rhs = (forcing+ends+diag-z*clock_A(1, alpha+1, degree, z)
                                   +clock_A(alpha, alpha-1, degree, z)
                                   +clock_A(alpha, alpha-1, degree-1, z)
                                   +clock_B(alpha, alpha-2, degree-1, z)) % p
                            lhs = (sigma-tau)*K(alpha, degree, z) % p
                            assert lhs == rhs, (N, sigma, tau, L, U, i, alpha, degree, z)
                            current_checks += 1

    # Exact finite coefficient check of the complete c0 endpoint current.
    anchor = Vs[c[0]]
    for a in range(N):
        assert int(anchor[a][0, d]) == ((-1)**d*N*N) % p
    return dict(N=N, prime=p, q=q, exact_order=2*N,
                homogeneous_matrix_coefficients=coefficient_checks,
                literal_adjacent_pair_coefficients=pair_checks,
                root_safe_clock_current_identities=current_checks,
                c0_current_coefficients=N,
                characteristic_annihilation=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(
        '/private/tmp/md-cyclic-signed-pair-and-endpoint-results.json'))
    args = parser.parse_args()
    rows = [run_level(N) for N in range(3, 9)]
    assert Fraction(4, 3)**2*2 < 4
    result = dict(status='passed', script_sha256=hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest(), levels=rows,
        energy_constant_check='(4/3)^2 * 2 < 4, exact rational',
        scope=('Exact finite-field polynomial and original monomial indexing checks. '
               'The continuum norm and all-level inequalities are proved in the note, '
               'not inferred from these cases. No global remainder or volume claim.'))
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='passed', levels=len(rows),
        pair_checks=sum(x['literal_adjacent_pair_coefficients'] for x in rows),
        clock_checks=sum(x['root_safe_clock_current_identities'] for x in rows),
        output=str(args.output))))


if __name__ == '__main__':
    main()
