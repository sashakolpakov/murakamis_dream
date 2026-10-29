#!/usr/bin/env python3
"""Exact finite quantum shear, actual source frame, clock and normal jet."""

import json
from pathlib import Path

import sympy as s


def symbol(A, v, z):
    n = A.rows-1
    return sum(A[i, j]*s.binomial(n, j)*v**i*z**j
               for i in range(n+1) for j in range(n+1))/(1+v*z)**n


def exact_case(N):
    n = N-1
    q, v, z = s.symbols('q v z', nonzero=True)
    m, M = q**N, -q**N
    U = s.diag(*(q**(N*j-j*(j+1)//2) for j in range(N)))
    Ui = U.inv()
    am, bp = s.zeros(N), s.zeros(N)
    J = s.diag(*range(N))
    for j in range(1, N):
        am[j-1, j] = s.Rational(j, n)
    for j in range(n):
        bp[j+1, j] = s.Rational(n-j, n)
    aa, bb, TT = z/(1+v*z), v/(1+v*z), v*z/(1+v*z)
    lefta, leftb = symbol(U*am*Ui, v, z), symbol(U*bp*Ui, v, z)
    righta = q/m*aa*(1+(q-1)*TT)**(n-1)
    rightb = m/q*bb*(1+(1/q-1)*TT)**(n-1)
    assert s.cancel(lefta-righta) == 0
    assert s.cancel(leftb-rightb) == 0
    assert U*J*Ui == J
    assert U*s.diag(*(q**(2*j) for j in range(N)))*Ui == s.diag(*(q**(2*j) for j in range(N)))
    for j in (0, n):
        P = s.zeros(N); P[j, j] = 1
        assert U*P*Ui == P
    qi = lambda k: sum(q**(k-1-2*r) for r in range(k))
    fact = [s.Integer(1)]
    for k in range(1, N):
        fact.append(fact[-1]*qi(k))
    D, residual = [], []
    for j in range(N):
        choose = fact[n]/(fact[j]*fact[n-j])
        dd = (-1)**j*q**(j*(j+1)//2)/choose
        vv = choose/M**j
        assert s.cancel(dd*U[j, j]*vv-1) == 0
        D.append(dd); residual.append(vv)
    assert U[n, n] == q**(N*n//2)
    # Star algebra and pointed covariance for noncommuting matrix inputs.
    A = am+2*bp+J
    B = J*bp+3*am
    assert U*(A*B)*Ui == (U*A*Ui)*(U*B*Ui)
    ones = s.ones(N, 1)
    phi = s.ones(1, N)/N
    assert (phi*Ui*(U*A*Ui)*U*ones)[0] == (phi*A*ones)[0]
    assert s.trace(U*A*Ui) == s.trace(A)
    return residual, {'level': N, 'literal_coherent_symbols': True,
                       'whole_clock_and_endpoint_probes_fixed': True,
                       'star_and_pointed_covariance': True,
                       'whole_factorial_residual_retained': True}


def main():
    records, jets = [], []
    q = s.symbols('q', nonzero=True)
    for N in range(2, 8):
        residual, record = exact_case(N)
        records.append(record)
        root = s.exp(s.pi*s.I/N)
        n = N-1
        for j, vv in enumerate(residual):
            rootvalue = s.N(vv.subs(q, root), 45)
            assert abs(complex(rootvalue-1)) < 1e-35
            derivative = s.cancel(q*s.diff(vv, q)/vv)
            target = -N*j+s.I*N*sum(s.cot(s.pi*s.Rational(r, N)) for r in range(1, j+1))
            assert abs(complex(s.N(derivative.subs(q, root)-target, 45))) < 1e-35
        top = s.exp(s.pi*s.I*s.Rational(n, 2))
        assert s.simplify(top-s.I**(N+3)) == 0
        jets.append({'level': N, 'all_root_normal_residual_jets': True,
                     'top_phase_exact': True})
    result = {'finite_star_source_cases': records, 'root_phase_and_jets': jets,
              'scope': 'Actual finite source frame and star automorphism only; no geometric intertwiner or selected norm.'}
    target = Path(__file__).with_name('exact_clock_shear_star_automorphism_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'finite_symbol_star_cases': len(records),
                      'root_phase_and_first_jet_levels': len(jets)}))


if __name__ == '__main__':
    main()
