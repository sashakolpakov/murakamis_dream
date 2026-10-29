#!/usr/bin/env python3
"""Independent positive path/TL proof audit, including high ordinary colors.

No knot polynomial, Jones library, recoupling library, or imported trace is
used. Identification with the original cut is audited separately.
"""

import functools
import json
import math
from pathlib import Path

import numpy as np


@functools.lru_cache(None)
def paths(N, m):
    rows = [(0,)]
    for _ in range(m):
        rows = [a+(b,) for a in rows for b in (a[-1]-1, a[-1]+1)
                if 0 <= b <= N-2]
    endpoints = sorted({a[-1] for a in rows})
    return {end: tuple(a for a in rows if a[-1] == end) for end in endpoints}


class PathTL:
    def __init__(self, N, m):
        self.N, self.m = N, m
        self.theta = math.pi/N
        self.q = np.exp(1j*self.theta)
        self.delta = 2*math.cos(self.theta)
        self.mu = [math.sin((a+1)*self.theta)/math.sin(self.theta)
                   for a in range(N-1)]
        assert min(self.mu) > 0
        self.groups = paths(N, m)
        self.identity = {end: np.eye(len(rows), dtype=complex)
                         for end, rows in self.groups.items()}
        self.generators = {}

    def qint(self, r):
        return math.sin(r*self.theta)/math.sin(self.theta)

    def U(self, i):
        assert 1 <= i < self.m
        if i in self.generators:
            return self.generators[i]
        out = {}
        for end, rows in self.groups.items():
            index = {a: j for j, a in enumerate(rows)}
            A = np.zeros((len(rows), len(rows)), dtype=complex)
            for col, a in enumerate(rows):
                if a[i-1] != a[i+1]:
                    continue
                c = a[i-1]
                for b in (c-1, c+1):
                    if 0 <= b <= self.N-2:
                        target = a[:i]+(b,)+a[i+1:]
                        row = index[target]
                        A[row, col] = math.sqrt(self.mu[a[i]]*self.mu[b])/self.mu[c]
            out[end] = A
        self.generators[i] = out
        return out

    def B(self, i, sign=1):
        U = self.U(i)
        positive = {end: self.q**.5*I-self.q**(-.5)*U[end]
                    for end, I in self.identity.items()}
        return positive if sign == 1 else adjoint(positive)

    def trace(self, A):
        return sum(self.mu[end]*np.trace(A[end]) for end in self.groups)

    def word(self, letters, use_U=False):
        A = self.identity
        for letter in letters:
            T = self.U(abs(letter)) if use_U else self.B(abs(letter), 1 if letter > 0 else -1)
            A = multiply(T, A)
        return A

    def JW(self, length, offset=0):
        assert length <= self.N-1
        P = self.identity
        for m in range(1, length):
            U = self.U(offset+m)
            c = self.qint(m)/self.qint(m+1)
            X = multiply(P, multiply(U, P))
            P = {end: P[end]-c*X[end] for end in P}
        return P


def multiply(A, B):
    return {end: A[end]@B[end] for end in A}


def adjoint(A):
    return {end: matrix.conj().T for end, matrix in A.items()}


def distance(A, B):
    return max((np.max(abs(A[end]-B[end])) for end in A), default=0.)


def norm(A):
    return max((np.linalg.norm(M, 2) for M in A.values()), default=0.)


def local_relations():
    rows = []
    for N in range(3, 11):
        A = PathTL(N, 6)
        errors = []
        for i in range(1, 6):
            U = A.U(i)
            errors.extend((distance(U, adjoint(U)),
                           distance(multiply(U, U), {e: A.delta*U[e] for e in U}),
                           distance(multiply(A.B(i), A.B(i, -1)), A.identity)))
        for i in range(1, 5):
            U, V = A.U(i), A.U(i+1)
            errors.append(distance(multiply(U, multiply(V, U)), U))
            B, C = A.B(i), A.B(i+1)
            errors.append(distance(multiply(B, multiply(C, B)), multiply(C, multiply(B, C))))
        for i in range(1, 6):
            for j in range(i+2, 6):
                errors.append(distance(multiply(A.U(i), A.U(j)), multiply(A.U(j), A.U(i))))
        assert max(errors) < 3e-12
        rows.append({'N': N, 'all_path_weights_positive': True,
                     'max_TL_braid_unitary_error': max(errors)})
    return rows


def markov_relations():
    rows = []
    for N in range(3, 10):
        worst = 0.
        for m in range(1, 6):
            A, B = PathTL(N, m), PathTL(N, m+1)
            words = [[], list(range(1, m)), list(range(m-1, 0, -1)),
                     [i if i % 2 else -i for i in range(1, m)]]
            if m >= 3:
                words.append([1, -2, 1, 2, -1])
            for word in words:
                X, Y = A.word(word), B.word(word)
                lhs0, rhs0 = B.trace(Y), A.delta*A.trace(X)
                lhs1, rhs1 = B.trace(multiply(Y, B.U(m))), A.trace(X)
                worst = max(worst, abs(lhs0-rhs0), abs(lhs1-rhs1))
        assert worst < 2e-10
        rows.append({'N': N, 'prefix_lengths': [1, 2, 3, 4, 5],
                     'both_noncommutative_Markov_trace_max_error': worst})
    return rows


def projections():
    rows = []
    for N in range(3, 11):
        worst = 0.
        for m in range(0, N):
            A = PathTL(N, m)
            P = A.JW(m)
            errors = [distance(P, adjoint(P)), distance(multiply(P, P), P),
                      abs(A.trace(P)-A.qint(m+1))]
            for i in range(1, m):
                errors.append(norm(multiply(P, A.U(i))))
            if m == N-1:
                errors.append(norm(P))
            worst = max(worst, max(errors))
        assert worst < 2e-9
        rows.append({'N': N, 'all_projection_lengths': list(range(N)),
                     'last_ordinary_color': N-1, 'negligible_next_projection_zero': True,
                     'max_projection_trace_annihilation_error': worst})
    return rows


def cable_word(ell, generator):
    assert ell >= 1
    offset = (abs(generator)-1)*ell
    positive = [offset+ell+r-j for r in range(ell) for j in range(ell)]
    return positive if generator > 0 else [-i for i in reversed(positive)]


def colored_case(N, j, b, word):
    ell = j-1
    A = PathTL(N, b*ell)
    P = A.identity
    for r in range(b):
        P = multiply(A.JW(ell, r*ell), P)
    expected = A.qint(j)**b
    trace_error = abs(A.trace(P)-expected)
    full_word = [s for letter in word for s in cable_word(ell, letter)]
    U = A.word(full_word)
    preservation = distance(multiply(U, P), multiply(P, U))
    unitary_error = distance(multiply(U, adjoint(U)), A.identity)
    framing = A.q**(-sum(1 if i > 0 else -1 for i in word)*(j*j-1)/2)
    value = framing*A.trace(multiply(P, U))/A.qint(j)
    bound = A.qint(j)**(b-1)
    assert abs(framing)-1 < 1e-12
    assert trace_error < 1e-8
    assert preservation < 1e-8
    assert unitary_error < 1e-8
    assert abs(value) <= bound+1e-8
    return {'N': N, 'ordinary_color': j, 'braid_width': b, 'word': word,
            'trace_P_expected': expected, 'trace_P_error': trace_error,
            'P_cabled_word_preservation_error': preservation,
            'cabled_word_unitarity_error': unitary_error,
            'zero_framed_reduced_closure_abs': abs(value),
            'proved_bound': bound}


def colored_closures():
    rows = []
    for N in range(3, 8):
        for j in range(2, N):
            for word in ([1, 1, 1], [-1, -1, -1]):
                rows.append(colored_case(N, j, 2, word))
        for j in range(2, min(N, 5)):
            rows.append(colored_case(N, j, 3, [1, -2, 1, -2]))
    return rows


def ordinary_energy_remainder():
    rows = []
    for r in range(1, 7):
        for N in (r+1, r+2, 2*r+3, 4*r+7):
            qints = [math.sin(j*math.pi/N)/math.sin(math.pi/N) for j in range(1, N)]
            direct = sum(t**(2*r) for t in qints)
            exact = N*math.comb(2*r, r)/(4**r*math.sin(math.pi/N)**(2*r))
            relative = abs(direct-exact)/max(1, exact)
            assert relative < 4e-14
            assert exact <= math.comb(2*r, r)*N**(2*r+1)/16**r*(1+1e-12)
            rows.append({'braid_width_minus_one': r, 'N': N,
                         'exact_sine_energy_relative_error': relative})
    return rows


def main():
    data = {'status': 'PASS', 'local_positive_TL_braid_relations': local_relations(),
            'weighted_trace_Markov_words': markov_relations(),
            'all_ordinary_JW_projections_including_highest': projections(),
            'whole_unitary_colored_closures': colored_closures(),
            'exact_polynomial_Planchelel_remainder': ordinary_energy_remainder(),
            'scope': ('Independent positive path algebra only; original-R/quotient/cabling '
                      'identification is separately proved, no Kashaev-color bound inferred.')}
    Path(__file__).with_name('positive_ordinary_color_path_trace_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(f"PASS positive path TL/Markov/JW algebra, {len(data['whole_unitary_colored_closures'])} "
          'full colored closures including j=N-1, and exact sine-energy remainders')


if __name__ == '__main__':
    main()
