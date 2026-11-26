#!/usr/bin/env python3
"""Exact Fourier and original-matrix checks for mixed tangle contraction.

The written q-Vandermonde proof holds at all levels. These diagnostics
compare independent finite Fourier coefficients with literal matrices;
they establish no asymptotic or lower bound for an oscillatory sum.
"""
import argparse
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-mixed-wire-exact-contraction.json')
    args = parser.parse_args()
    identities = []
    u = sp.Symbol('u')
    n, i, j = sp.symbols('n i j', positive=True)
    phase = lambda a: sp.pi*a/2-sp.pi*a*(a+1)/(2*n)
    assert sp.expand(phase(i+j)-phase(i)-phase(j)+sp.pi*i*j/n) == 0
    identities.append('quadratic phase splits into leg terms and a Fourier cross term')
    for word in ((3, 3, 3), (3, 4), (3, 4, 4, 3)):
        m = len(word)
        left = sp.symbols(f'i0:{m}')
        right = sp.symbols(f'j0:{m}')
        original = sum(phase(left[v]+right[v]) if letter == 3
                       else -sp.pi*left[v]*right[v]/n
                       for v, letter in enumerate(word))
        original -= sum(phase(right[v]+left[(v+1) % m]) for v in range(m))
        fourier = sp.pi*sum(right[v]*(left[(v+1) % m]-left[v])
                            for v in range(m))/n
        fourier -= sum(phase(left[v])+phase(right[v])
                       for v, letter in enumerate(word) if letter == 4)
        assert sp.expand(original-fourier) == 0
        identities.append(f'cyclic Fourier phase {word}')

    @lru_cache(None)
    def gaussian(n, k):
        if k < 0 or k > n:
            return sp.Integer(0)
        if k == 0 or k == n:
            return sp.Integer(1)
        return sp.expand(gaussian(n-1, k-1)+u**k*gaussian(n-1, k))

    for j in range(5):
        for k in range(5):
            difference = sum(u**(l*l)*gaussian(j, l)*gaussian(k, l)
                             for l in range(min(j, k)+1))-gaussian(j+k, j)
            assert sp.expand(difference) == 0, (j, k)
            identities.append(f'polynomial Vandermonde j{j} k{k}')

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    one, zero = field.one, field.zero

    def cv(x):
        return field.from_sympy(sp.sympify(x))

    def product(values):
        answer = one
        for value in values:
            answer *= value
        return answer

    def multiply(A, B):
        size = len(A)
        return [[sum((A[i][l]*B[l][j] for l in range(size)), zero)
                 for j in range(size)] for i in range(size)]

    def transpose(A):
        return [list(row) for row in zip(*A)]

    def check(label, value):
        assert value == zero, label
        identities.append(label)

    def compare(label, A, B):
        for j in range(len(A)):
            for k in range(len(A)):
                check(f'{label} entry{j},{k}', A[j][k]-B[j][k])

    levels = [(2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
              (4, (1+sp.I)/sp.sqrt(2)), (6, (sp.sqrt(3)+sp.I)/2)]
    for N, qs in levels:
        q, ii = cv(qs), cv(sp.I)
        Q, r, D = q*q, one/(q*q), N-1
        P = [product(1-r**a for a in range(1, j+1)) for j in range(N)]
        T = [product(1-Q**a for a in range(1, j+1)) for j in range(N)]
        M0 = [[((-1)**j*q**(j+k*k)*T[j]/(T[k]*T[j-k])
                if k <= j else zero) for k in range(N)] for j in range(N)]
        S = [[(-q)**(-j)*M0[j][k]/P[j] for k in range(N)] for j in range(N)]
        gram = [[(Q**(j*k)*P[j+k]/(P[j]**2*P[k]**2)
                  if j+k < N else zero) for k in range(N)] for j in range(N)]
        compare(f'N{N} original cardinal Gram', gram, multiply(S, transpose(S)))

        # Direct Fourier extraction, independent of the matrix/Vandermonde route.
        polynomials = []
        for j in range(N):
            poly = [zero]*j+[one]
            for a in range(j+1, N):
                new = [zero]*(len(poly)+1)
                for l, value in enumerate(poly):
                    new[l] += value
                    new[l+1] -= r**a*value
                poly = new
            assert len(poly) == N
            polynomials.append(poly)
        for j in range(N):
            for k in range(N):
                coefficient = sum((polynomials[j][l]*polynomials[k][D-l]
                                   for l in range(N)), zero)/N
                check(f'N{N} literal Fourier coefficient j{j} k{k}', coefficient-gram[j][k])

        C3 = [[P[i+j] if i+j < N else zero for j in range(N)] for i in range(N)]
        C4 = [[N*P[i+j]/(P[i]*P[j]) if i+j < N else zero
               for j in range(N)] for i in range(N)]
        M2 = multiply(M0, M0)
        M3, M4 = multiply(M2, M0), multiply(M2, M2)
        A3 = [[q**(D*D)*M3[D-i][j] for j in range(N)] for i in range(N)]
        A4 = [[q**(D*D)*M4[D-i][j] for j in range(N)] for i in range(N)]
        compare(f'N{N} original A3 divided by kappa', A3,
                multiply(transpose(S), multiply(C3, S)))
        compare(f'N{N} original A4 divided by kappa squared', A4,
                multiply(transpose(S), multiply(C4, S)))
        for word in ((3, 4), (3, 3, 4), (3, 4, 3, 4)):
            original = {3: A3, 4: A4}[word[0]]
            contracted = {3: C3, 4: C4}[word[0]]
            for letter in word[1:]:
                original = multiply(original, {3: A3, 4: A4}[letter])
                contracted = multiply(multiply(contracted, gram), {3: C3, 4: C4}[letter])
            compare(f'N{N} full mixed word {word}', original,
                    multiply(transpose(S), multiply(contracted, S)))
            check(f'N{N} cyclic word {word}',
                  sum((original[j][j] for j in range(N)), zero)
                  -sum((multiply(contracted, gram)[j][j] for j in range(N)), zero))

        delta = [ii**j*q**(-j*(j+1)//2) for j in range(N)]
        sine = [product((q**a-q**(-a))/ii for a in range(1, j+1)) for j in range(N)]
        for j in range(N):
            check(f'N{N} sine factorial j{j}', P[j]-delta[j]*sine[j])
            for k in range(N-j):
                check(f'N{N} quadratic Gram phase j{j} k{k}',
                      gram[j][k]-sine[j+k]/(delta[j+k]*sine[j]**2*sine[k]**2))
                check(f'N{N} quadratic power4 phase j{j} k{k}',
                      C4[j][k]/N-q**(-j*k)*sine[j+k]/(sine[j]*sine[k]))

    dependencies = ['notes/research_mixed_wire_exact_contraction.md',
                    'notes/research_three_four_source_interface.md',
                    'notes/research_traced_three_vertex_endpoint.md',
                    'notes/research_power_four_finite_source.md']
    result = {
        'status': 'passed', 'exact_identity_count': len(identities),
        'exact_identities': identities, 'finite_levels': [n for n, _ in levels],
        'arithmetic': 'Exact polynomial and Q(i,sqrt(2),sqrt(3)) arithmetic',
        'scope': 'Finite Vandermonde, independent Fourier coefficients, original matrices and mixed-word contractions, and exact quadratic phases. All-level identities have written proofs; no asymptotic or lower bound is checked.',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'exact_identity_count', 'finite_levels')}))


if __name__ == '__main__':
    main()
