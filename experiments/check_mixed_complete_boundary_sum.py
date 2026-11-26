#!/usr/bin/env python3
"""Exact normalization diagnostics for complete mixed-word boundary sums.

The all-level proof is algebraic in the companion note. Finite-level
comparisons below are diagnostics, not a lower-asymptotic certificate.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-mixed-complete-boundary-sum.json')
    args = parser.parse_args()
    identities, diagnostics, positivity = [], [], []

    def identity(name, expression):
        assert sp.simplify(sp.expand(expression)) == 0, name
        identities.append(name)

    n = sp.Symbol('N', positive=True)
    phase = lambda j: sp.pi*((n-1)*j-j*j)/(2*n)
    for word in ((3,), (4,), (3, 4), (4, 3), (3, 4, 3), (4, 3, 4, 4)):
        m = len(word)
        i, j = sp.symbols(f'i0:{m}'), sp.symbols(f'j0:{m}')
        ell, rr = sp.symbols('ell rr')
        literal = sum(phase(i[v]+j[v]) if letter == 3
                      else -sp.pi*i[v]*j[v]/n
                      for v, letter in enumerate(word))
        literal -= sum(phase(j[v]+i[v+1]) for v in range(m-1))
        literal -= phase(i[0])+phase(j[-1])
        literal += sp.pi*(i[0]*ell+j[-1]*rr)/n
        claimed = sp.pi*(sum(j[v]*i[v+1] for v in range(m-1))
                         -sum(i[v]*j[v] for v in range(m))
                         +i[0]*ell+j[-1]*rr)/n
        claimed += sp.pi*sum(i[v]**2+j[v]**2-(n-1)*(i[v]+j[v])
                             for v, letter in enumerate(word) if letter == 4)/(2*n)
        identity(f'exact open phase word {word}', literal-claimed)

    A, B, de, du = sp.symbols('A B de du', real=True)
    matrix = sp.Matrix([[B, -B], [-B, A+B]])
    identity('boundary positive Hessian form',
             (sp.Matrix([de, du]).T*matrix*sp.Matrix([de, du]))[0]
             -(A*du**2+B*(de-du)**2))
    identity('optimized boundary Schur curvature', B-B**2/(A+B)-A*B/(A+B))
    z, w = sp.symbols('z w', positive=True)
    identity('boundary critical cubic',
             (w-z)/(z**3*sp.sqrt(1+w*w))-1
             -(w-z-z**3*sp.sqrt(1+w*w))/(z**3*sp.sqrt(1+w*w)))
    u, e = sp.symbols('u e', real=True)
    bu = sp.log(sp.cos(sp.pi*u)**2*sp.sin(sp.pi*(e-u))/sp.sin(sp.pi*u)**3)
    identity('boundary first derivative in e',
             sp.diff(bu, e)-sp.pi*sp.cot(sp.pi*(e-u)))
    identity('boundary second derivative in u',
             sp.diff(bu, u)+sp.pi*(2*sp.tan(sp.pi*u)+3*sp.cot(sp.pi*u)
                                    +sp.cot(sp.pi*(e-u))))
    sv, tv = sp.symbols('s t')
    identity('finite power-four amplitude phase',
             phase(n*sv)+phase(n*tv)
             -n*sp.pi*(sv+tv-sv**2-tv**2)/2+sp.pi*(sv+tv)/2)
    X = sp.Symbol('X')
    identity('actual endpoint stationary factorization',
             (z+sp.I)*(2*z*z-2*sp.I*z+X-1)
             -(2*z**3+(X+1)*z+sp.I*(X-1)))
    ca = sp.Symbol('ca', real=True)
    identity('selected endpoint square-root bound',
             (3-2*ca)**2-(5-4*ca)-4*(1-ca)**2)
    aa, bb = sp.symbols('aa bb', real=True)
    realX, imagX = 1-2*bb-2*aa*aa+2*bb*bb, 2*aa*(1-2*bb)
    identity('unit-circle endpoint constraint',
             realX**2+imagX**2-1
             -4*((aa*aa-bb*(1-bb))**2-bb*(1-bb)))
    identity('endpoint argument comparison',
             (1-2*bb)*(1-aa*aa-bb*bb)-realX
             -(aa*aa*(1+2*bb)-bb*bb*(3-2*bb)))
    rr = sp.Symbol('rr', positive=True)
    identity('endpoint argument comparison after unit-circle constraint',
             ((bb*(1-bb)+rr)*(1+2*bb)-bb*bb*(3-2*bb))
             -(bb*(1-2*bb)+(1+2*bb)*rr))
    alpha = sp.Symbol('alpha')
    zseries = alpha/2-alpha**3/12+sp.I*alpha**4/16
    identity('small-parameter critical quadratic lift',
             sp.series(2*zseries**2-2*sp.I*zseries+sp.exp(sp.I*alpha)-1,
                       alpha, 0, 5).removeO())
    identity('complete-jet reciprocal integral',
             sp.diff(sp.tan(sp.pi*u)/(4*sp.pi), u)-1/(4*sp.cos(sp.pi*u)**2))
    mm, ka, kb = sp.symbols('m a b')
    identity('open Gaussian normalization with complete jets',
             mm/2-3*(mm-1)/2+ka+kb-4+(2*mm+2)-(mm+1)
             -(ka+kb-sp.Rational(3, 2)))

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    one, zero = field.one, field.zero
    cv = lambda value: field.from_sympy(sp.sympify(value))

    def product(values):
        answer = one
        for value in values:
            answer *= value
        return answer

    def multiply(A, B):
        return [[sum((A[i][l]*B[l][j] for l in range(len(B))), zero)
                 for j in range(len(B[0]))] for i in range(len(A))]

    def transpose(A):
        return [list(row) for row in zip(*A)]

    def check(name, expression):
        assert expression == zero, name
        diagnostics.append(name)

    def scalar(left, matrix, right):
        return sum((left[i]*matrix[i][j]*right[j]
                    for i in range(len(left)) for j in range(len(right))), zero)

    levels = [(2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
              (4, (1+sp.I)/sp.sqrt(2))]
    words = ((3,), (4,), (3, 4), (4, 3), (3, 4, 3))
    for N, qvalue in levels:
        q, ii, D = cv(qvalue), cv(sp.I), N-1
        delta = [ii**j*q**(-j*(j+1)//2) for j in range(N)]
        sine = [product((q**a-q**(-a))/ii for a in range(1, j+1)) for j in range(N)]
        P = [product(1-q**(-2*a) for a in range(1, j+1)) for j in range(N)]
        M0 = [[((-1)**j*q**(j*(l+1))*sine[j]/(sine[l]*sine[j-l])
                if l <= j else zero) for l in range(N)] for j in range(N)]
        S = [[(-q)**(-j)*M0[j][l]/P[j] for l in range(N)] for j in range(N)]
        for j in range(N):
            for l in range(j+1):
                check(f'N{N} literal S entry {j},{l}',
                      S[j][l]-q**(j*l)/(delta[j]*sine[l]*sine[j-l]))

        # Polynomial coefficients are stored in w+2, preserving every ordinary jet.
        basis, polynomial = [], [one]
        for l in range(N):
            basis.append([coefficient/sine[l]**2 for coefficient in polynomial])
            d = q**(2*l+1)+q**(-2*l-1)+2
            new = [zero]*(len(polynomial)+1)
            for k, coefficient in enumerate(polynomial):
                new[k] += d*coefficient
                new[k+1] -= coefficient
            polynomial = new
        jets = [[basis[l][k]*factorial(k) if k <= l else zero
                 for l in range(N)] for k in range(N)]
        signed_jets = [[(-1)**k*value for value in jets[k]] for k in range(N)]
        for k in range(N):
            for l in range(N):
                expression = sp.simplify(field.to_sympy(signed_jets[k][l]))
                assert expression.is_nonnegative is True, (N, k, l, expression)
                positivity.append(f'N{N} signed complete jet k{k} l{l}')
        boundary = [[sum((q**(j*l)*signed_jets[k][l]/
                          (sine[l]*sine[j-l]) for l in range(j+1)), zero)/delta[j]
                     for j in range(N)] for k in range(N)]
        for k in range(N):
            for j in range(N):
                check(f'N{N} literal complete boundary derivative k{k} row{j}',
                      (-1)**k*boundary[k][j]-sum((S[j][l]*jets[k][l]
                                                               for l in range(N)), zero))
        gram = [[(sine[j+k]/(delta[j+k]*sine[j]**2*sine[k]**2)
                  if j+k < N else zero) for k in range(N)] for j in range(N)]
        C3 = [[delta[j+k]*sine[j+k] if j+k < N else zero
               for k in range(N)] for j in range(N)]
        C4 = [[N*q**(-j*k)*sine[j+k]/(sine[j]*sine[k]) if j+k < N else zero
               for k in range(N)] for j in range(N)]
        M2 = multiply(M0, M0)
        powers = {3: multiply(M2, M0), 4: multiply(M2, M2)}
        original = {letter: [[q**(D*D)*powers[letter][D-j][k]
                              for k in range(N)] for j in range(N)]
                    for letter in (3, 4)}
        contracted = {3: C3, 4: C4}
        for word in words:
            exact, phase_weight = original[word[0]], contracted[word[0]]
            for letter in word[1:]:
                exact = multiply(exact, original[letter])
                phase_weight = multiply(multiply(phase_weight, gram), contracted[letter])
            for a in range(N):
                for b in range(N):
                    check(f'N{N} original complete mixed word {word} jets {a},{b}',
                          scalar(jets[a], exact, jets[b])
                          -(-1)**(a+b)*scalar(boundary[a], phase_weight, boundary[b]))

    dependencies = ['notes/research_mixed_complete_boundary_sum.md',
                    'notes/research_mixed_wire_exact_contraction.md',
                    'notes/research_traced_three_vertex_endpoint.md']
    result = {
        'status': 'passed', 'symbolic_identity_count': len(identities),
        'symbolic_identities': identities,
        'finite_normalization_diagnostic_count': len(diagnostics),
        'finite_normalization_diagnostics': diagnostics,
        'exact_signed_jet_positivity_count': len(positivity),
        'exact_signed_jet_positivity': positivity,
        'finite_levels': [n for n, _ in levels],
        'arithmetic': 'Exact symbolic identities and Q(i,sqrt(2),sqrt(3)) arithmetic',
        'scope': 'All-level identities are proved in the note. Finite tests diagnose original matrix/complete-jet normalization. No global contour, lower coefficient, or arbitrary mixed-word volume theorem is asserted.',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'symbolic_identity_count',
          'finite_normalization_diagnostic_count', 'exact_signed_jet_positivity_count')}))


if __name__ == '__main__':
    main()
