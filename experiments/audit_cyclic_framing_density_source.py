#!/usr/bin/env python3
"""Exact root-source identities for the prefix framing density.

This does not assume Gaussian/source interchange for a knot period.
"""

import json
from pathlib import Path

import sympy as sp


def root_companion_trace():
    lam = sp.symbols('lambda')
    records = []
    for N in range(2, 12):
        # Multiplication by B on k[B]/(B**N-1), independently of a
        # chosen primitive root. Its matrix trace is the full root sum.
        C = sp.zeros(N)
        for j in range(N):
            C[(j + 1) % N, j] = 1
        assert C**N == sp.eye(N)
        resolvent = (C - lam * sp.eye(N)).inv()
        actual = sp.cancel(sp.trace(C * resolvent**2) / N)
        predicted = N * lam**(N-1) / (1-lam**N)**2
        assert sp.cancel(actual - predicted) == 0
        norm = sp.factor((sp.eye(N) - lam * C.inv()).det())
        assert sp.expand(norm - (1-lam**N)) == 0
        records.append({'level': N, 'trace_and_cyclic_norm_verified': True})
    return records


def whole_current():
    Q, lam = sp.symbols('Q lambda', nonzero=True)
    records = []
    theta = lambda f: lam * sp.diff(f, lam)
    for N in range(2, 8):
        factors = [1-lam*Q**(-b) for b in range(N)]
        P = sp.prod(factors)
        log_derivative = sp.cancel(theta(P) / P)
        second = theta(log_derivative)
        actual = sum(Q**b/(Q**b-lam)**2 for b in range(N)) / N
        assert sp.cancel(actual + second/(N*lam)) == 0
        q_current = sum(b*lam*Q**(-b)/(1-lam*Q**(-b)) for b in range(N))
        assert sp.cancel(Q*sp.diff(P,Q)/P - q_current) == 0
        records.append({'level': N, 'whole_normal_current_retained': True})
    return records


def independent_field_chart():
    u = sp.symbols('u')
    rel = sp.Poly(u**2+u+1, u)
    red = lambda f: sp.rem(sp.Poly(sp.expand(f),u),rel).as_expr()
    U = sp.Matrix([[u+1,2*u+1],[1-u,3-u]])
    V = sp.Matrix([[1,1],[-u,1-u]])
    assert red(U.det()-1) == red(V.det()-1) == 0
    cU, cV = U[1,0], V[1,0]
    hU, hV = U[0,0]-U[1,1], V[0,0]-V[1,1]
    W = red(cV*hU-hV*cU)
    J = sp.Matrix([[1,1],[0,1]])
    assert sp.expand(sp.trace(J*U)-sp.trace(U)-cU) == 0
    assert sp.expand(sp.trace(J*V)-sp.trace(V)-cV) == 0
    assert red(sp.trace(J*(V*U-U*V))-W) == 0
    assert W == 2*u+1
    assert red(cV*(u+2)-cU) == 0
    assert red(W*(u+2)+cU**2) == 0  # gamma=-lambda
    chosen_u = (-1+sp.sqrt(3)*sp.I)/2
    lam = sp.simplify(1/(chosen_u+2))
    assert sp.simplify(lam*sp.conjugate(lam)-sp.Rational(1,3)) == 0
    return {'riley_polynomial': 'u**2+u+1', 'W': str(W),
            'lambda_squared_modulus': '1/3', 'gamma_equals_minus_lambda': True,
            'intrinsic_trace_word_formulas_verified': True}


def main():
    report = {
        'scope': 'Exact finite cyclic source on a framing density, not Kashaev Gaussian/source interchange',
        'root_companion': root_companion_trace(),
        'whole_current': whole_current(),
        'actual_prefix_field_calibration': independent_field_chart(),
        'all_checks_passed': True,
    }
    target = Path(__file__).with_name('cyclic_framing_density_source_results.json')
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'all_checks_passed': True,
                      'exact_companion_levels': len(report['root_companion']),
                      'whole_current_levels': len(report['whole_current']),
                      'result_file': str(target)},indent=2))


if __name__ == '__main__':
    main()
