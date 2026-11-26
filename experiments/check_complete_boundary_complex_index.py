#!/usr/bin/env python3
"""Exact grid matching and finite diagnostics for the specified continuation.

The proof of a fixed complex neighborhood, including all revived rows,
is in the companion note. Numerical comparisons do not certify that
neighborhood or any whole mixed-word asymptotic.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_exact_factorial_interpolation import sine_factorial
from check_complete_boundary_coefficient_asymptotic import phase, saddle, hessian

ROOT = Path(__file__).resolve().parents[1]


def continuation(N, e, max_jet=2):
    """The single fixed finite sum, using an exact factorial recurrence."""
    G = sine_factorial(N, N*e)
    sine = mp.mpf(1)
    backward = mp.mpc(1)
    jets = [mp.mpf(1)] + [mp.mpf(0)]*max_jet
    out = [jets[k]/G for k in range(max_jet+1)]
    for l in range(1, N):
        factor = 4*mp.sin(mp.pi*l/N)**2
        d = (mp.mpf(0) if 2*l-1 == N else
             2*mp.cos(mp.pi*(2*l-1)/N)+2)
        jets = [(d*jets[k]+(k*jets[k-1] if k else 0))/factor
                for k in range(max_jet+1)]
        sine *= 2*mp.sin(mp.pi*l/N)
        backward *= 2*mp.sin(mp.pi*(e-mp.mpf(l-1)/N))
        carrier = mp.exp(1j*mp.pi*e*l)*backward/(sine*G)
        for k in range(max_jet+1):
            out[k] += carrier*jets[k]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dps', type=int, default=70)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-complete-boundary-complex-index.json')
    args = ap.parse_args()
    exact, margins, grid = [], [], []

    def identity(name, expression):
        assert sp.factor(expression) == 0, (name, expression)
        exact.append(name)

    def positive(name, expression):
        expression = sp.simplify(expression)
        assert expression.is_positive, (name, expression)
        margins.append({'name': name, 'value': str(expression)})

    z, t, c, d, x = sp.symbols('z t c d x', real=True)
    identity('high-row cubic derivative', sp.diff(z**3-c*z+d, z)-(3*z*z-c))
    identity('high-row cubic value at tangent', (z**3-c*z+d).subs(z, t).subs(d, c*t)-t**3)
    identity('endpoint derivative at pi/5',
             3*(5-2*sp.sqrt(5))-(1+sp.sqrt(5))/4-(59-25*sp.sqrt(5))/4)
    positive('positive endpoint derivative', (59-25*sp.sqrt(5))/4)
    positive('squared endpoint derivative margin', 59**2-25**2*5)
    identity('logarithm lower bound derivative',
             1/(1+x)-4/(2+x)**2-x*x/((1+x)*(2+x)**2))
    positive('golden ratio lower bound', (1+sp.sqrt(5))/2-sp.Rational(8, 5))
    identity('lower log bound at three fifths',
             (2*x/(2+x)).subs(x, sp.Rational(3, 5))-sp.Rational(6, 13))
    positive('first J endpoint stronger than second',
             sp.Rational(1, 10)-sp.Rational(6, 65))
    identity('high-row exponential margin',
             sp.Rational(12, 65)-sp.Rational(1, 6)-sp.Rational(7, 390))
    positive('strict high-row exponential margin', sp.Rational(7, 390))
    N, j = sp.symbols('N j', positive=True)
    identity('complete-boundary exact carrier',
             N*(j/N-j*j/N**2)-j/N-((N-1)*j-j*j)/N)
    Y, U, lam = sp.symbols('Y U lam')
    rr = (1-(1-Y)*lam)/Y
    tt = (1-Y)*lam
    symbol = (1-rr)**3-tt*(1+rr)**2
    classical = ((1-Y)**2*(lam-1)**3
                 -Y*lam*(Y+1-(1-Y)*lam)**2)
    identity('classical operator polynomial',
             sp.cancel(symbol-(1-Y)*classical/Y**3))
    identity('selected boundary branch of the exact operator',
             sp.cancel(symbol.subs(lam, (Y-U)/((Y-1)*U))
                       -((1+U)**2*(Y-U)-(1-U)**3)/U**3))

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    one, zero = field.one, field.zero
    cv = lambda value: field.from_sympy(sp.sympify(value))
    def add(p, q, factor=one):
        return [(p[i] if i < len(p) else zero)
                +factor*(q[i] if i < len(q) else zero)
                for i in range(max(len(p), len(q)))]
    for n, qvalue in ((2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
                      (4, (1+sp.I)/sp.sqrt(2)),
                      (6, (sp.sqrt(3)+sp.I)/2)):
        q, ii = cv(qvalue), cv(sp.I)
        S, E = [one], [[one, zero, zero]]
        for l in range(1, n):
            step = (q**l-q**(-l))/ii
            S.append(S[-1]*step)
            node = q**(2*l-1)+q**(-2*l+1)+2
            E.append([(node*E[-1][k]+(k*E[-1][k-1] if k else zero))/(step*step)
                      for k in range(3)])
        for j in range(n):
            delta = ii**j*q**(-j*(j+1)//2)
            Pj = delta*S[j]
            back = one
            fixed = [zero, zero, zero]
            for l in range(n):
                if l:
                    h = j-l+1
                    back *= (q**h-q**(-h))/ii
                expected = S[j]/S[j-l] if l <= j else zero
                assert back == expected, (n, j, l)
                grid.append(f'N{n} reciprocal factorial truncation j{j} l{l}')
                for k in range(3):
                    fixed[k] += q**(j*l)*E[l][k]*back/(S[l]*S[j])
            for k in range(3):
                # Literal crossing matrix with its common kappa removed.
                original = sum(((-1)**j*q**(j*(l+1))*S[j]/
                                (S[l]*S[j-l])*E[l][k] for l in range(j+1)), zero)
                original *= delta*(-q)**(-j)/Pj
                assert fixed[k] == original, (n, j, k)
                grid.append(f'N{n} original transformed boundary jet j{j} k{k}')
        r = q**-2
        P, poch = one, one
        basis, polynomial = [one], [zero]
        for l in range(n):
            if l:
                P *= 1-r**l
                poch *= 1+q**-1*r**(l-1)
            h = r**l*poch**2/P**3
            assert h == (-q)**(-l)*E[l][0]/P
            grid.append(f'N{n} exact polynomial Newton coefficient l{l}')
            polynomial = add(polynomial, basis, h)
            basis = add(basis, [zero]+basis, -r**l)
        assert sum(polynomial, zero) == one
        grid.append(f'N{n} polynomial scalar at Y1')
        def T(p):
            shifted = [r**i*co for i, co in enumerate(p)]
            return add(shifted, [zero]+shifted, -one)
        def R(p):
            numerator = add(p, T(p), -one)
            assert numerator[0] == zero
            return numerator[1:]
        lhs = polynomial
        for _ in range(3):
            lhs = add(lhs, R(lhs), -one)
        second = polynomial
        for _ in range(2):
            second = add(second, R(second), q**-1)
        lhs = add(lhs, T(second), -r)
        rhs = [-(1+(-1)**n)**2*co/n**3 for co in basis]
        difference = add(lhs, rhs, -one)
        for degree, co in enumerate(difference):
            assert co == zero, (n, degree)
            grid.append(f'N{n} forced polynomial operator coefficient d{degree}')

    rows = []
    with mp.workdps(args.dps):
        for er, ei in (('.20', '.002'), ('.35', '.004'), ('.42', '-.003')):
            e = mp.mpc(er, ei)
            uc = saddle(e)
            f = phase(e, uc)
            amp = (mp.sqrt(2*mp.pi)/mp.sqrt(-hessian(e, uc))
                   /(2*mp.sin(mp.pi*uc))**mp.mpf('1.5')
                   /(2*mp.sin(mp.pi*(e-uc)))**mp.mpf('.5'))
            for n in (24, 25, 48, 49, 96, 97):
                actual = continuation(n, e)
                for k in range(3):
                    predicted = (n**(mp.mpf(k)-mp.mpf('1.5'))*amp
                                 *(mp.tan(mp.pi*uc)/(4*mp.pi))**k*mp.exp(n*f))
                    error = abs(actual[k]/predicted-1)
                    assert n*error < 100, (er, ei, n, k, error)
                    rows.append({'e': [er, ei], 'N': n, 'jet_order': k,
                                 'relative_error': str(error),
                                 'N_scaled_relative_error': str(n*error)})
    deps = [
        'notes/research_complete_boundary_complex_index.md',
        'notes/research_complete_boundary_coefficient_asymptotic.md',
        'notes/research_mixed_complete_boundary_sum.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'notes/research_uniform_factorial_and_boundary_decay.md',
        'experiments/audit_exact_factorial_interpolation.py',
        'experiments/check_complete_boundary_coefficient_asymptotic.py',
    ]
    result = {
        'status': 'passed',
        'precision_decimal_digits': args.dps,
        'exact_identity_count': len(exact), 'exact_identities': exact,
        'exact_positive_margin_count': len(margins), 'exact_positive_margins': margins,
        'physical_grid_identity_count': len(grid), 'physical_grid_identities': grid,
        'complex_asymptotic_diagnostic_count': len(rows),
        'complex_asymptotic_diagnostics': rows,
        'maximum_N_scaled_relative_error':
            str(max(mp.mpf(row['N_scaled_relative_error']) for row in rows)),
        'scope': ('Fixed finite Gamma continuation with exact physical-grid matching. '
                  'Uniform complex asymptotics and control of revived rows are proved '
                  'in the note. Finite comparisons do not certify a neighborhood radius '
                  'or a whole mixed-word volume theorem.'),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'status', 'exact_identity_count', 'exact_positive_margin_count',
        'physical_grid_identity_count', 'complex_asymptotic_diagnostic_count',
        'maximum_N_scaled_relative_error')}))


if __name__ == '__main__':
    main()
