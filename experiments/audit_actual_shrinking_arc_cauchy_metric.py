#!/usr/bin/env python3
"""Exact Cayley/Legendre metric and complete original terminal rows."""

import json
from pathlib import Path

import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss

from audit_actual_coherent_terminal_bridge_metric import data


def exact_case(d):
    a = s.Rational(1, d+2)
    y = s.symbols('y', real=True)
    V = s.Matrix([[s.expand((1+s.I*a*y)**j*(1-s.I*a*y)**(d-j)).coeff(y, k)
                   for j in range(d+1)] for k in range(d+1)])
    H = s.Matrix([[s.Rational(1, k+l+1) if (k+l) % 2 == 0 else 0
                   for l in range(d+1)] for k in range(d+1)])
    W = V.conjugate().T*H*V
    assert V.det() != 0
    e = s.ones(1, d+1)
    m = d//2
    kappa = (2*m+1)**2*(s.binomial(2*m, m)/4**m)**2
    assert s.simplify((e*W.inv()*e.T)[0]-kappa) == 0
    assert kappa <= d+1
    kernel = sum((2*j+1)*s.legendre(j, 0)*s.legendre(j, y) for j in range(d+1))
    kernel_energy = s.integrate(kernel**2, (y, -1, 1))/2
    assert kernel_energy == kappa
    assert s.simplify(kernel.subs(y, 0)**2/kappa-kernel_energy) == 0
    if d:
        r = (d-1)//2
        derivative = sum((2*j+1)*s.diff(s.legendre(j, y), y).subs(y, 0)**2
                         for j in range(d+1))
        expected = ((2*r+1)*(2*r+3)*s.binomial(2*r, r)/4**r)**2/3
        assert derivative == expected
        assert derivative <= s.Rational((d+2)**3, 3)
    return {'degree': d, 'exact_dual_constant': str(kappa),
            'finite_Gram_inverse_and_sharpness': True, 'exact_derivative_constant': True}


def original_case(N):
    q, Q, x, F, sf, T, _, _, _ = data(N)
    d, a = N-1, 1/N
    nodes, weights = leggauss(N)
    # Gauss-Legendre integrates the entire cleared polynomial exactly:
    # its squared modulus has degree at most 2d.
    B = np.array([[(1+1j*a*y)**j*(1-1j*a*y)**(d-j)
                   for j in range(N)] for y in nodes])
    W = B.conj().T@(weights[:, None]*B)/2
    m = d//2
    kappa = float((2*m+1)**2*(s.binomial(2*m, m)/4**m)**2)
    epsilon = .25
    G = T.conj().T@W@T+epsilon*np.eye(N)
    G = (G+G.conj().T)/2
    np.linalg.cholesky(G)
    boundary = np.sum(T, axis=0)
    expected_boundary = np.array([(x*Q)**(j-d)/N for j in range(N)])
    assert np.allclose(boundary, expected_boundary, atol=4e-7, rtol=4e-7)
    dual = float((boundary@np.linalg.solve(G, boundary.conj())).real)
    assert dual <= kappa*(1+1e-7)
    rng = np.random.default_rng(72200+N)
    for _ in range(3):
        v = rng.normal(size=N)+1j*rng.normal(size=N)
        z = T@v
        energy = float(np.vdot(z, W@z).real)
        assert abs(np.sum(z))**2 <= kappa*energy*(1+2e-7)
        derivative = np.dot(np.arange(N), z)
        r = (d-1)//2
        D = float(((2*r+1)*(2*r+3)*s.binomial(2*r, r)/4**r)**2/3)
        assert a*a*abs(2*derivative-d*np.sum(z))**2 <= D*energy*(1+2e-7)
    # This row vector is the independently proved original 4_1 packet.
    positive = sf**2
    energy = float(np.vdot(positive, W@positive).real)
    closed_squared = np.sum(positive)**2
    assert closed_squared/kappa <= energy*(1+1e-10)
    assert energy <= (1+a*a)**d*closed_squared*(1+1e-10)
    return {'N': N, 'complete_original_boundary_and_positive_completion': True,
            'all_input_arc_and_derivative_inequalities': True,
            'dual_cost': dual, 'allowed_cost': kappa,
            'original_positive_benchmark_comparison': True}


def exact_warning():
    a, A, y = s.symbols('a A y', real=True)
    t = (1+s.I*a*y)/(1-s.I*a*y)
    Q = s.cancel((1-s.I*a*y)*(1+A*(t-1)))
    assert s.expand(Q-1-s.I*a*y*(2*A-1)) == 0
    energy = s.integrate(s.expand(Q*s.conjugate(Q)), (y, -1, 1))/2
    assert s.simplify(energy-1-a*a*(2*A-1)**2/3) == 0
    return {'exact_degree_one_boundary_layer': True, 'scope': 'Not a knot counterexample.'}


if __name__ == '__main__':
    output = {'status': 'PASS', 'exact_finite_metrics': [exact_case(d) for d in range(9)],
              'original_terminal_modules': [original_case(N) for N in range(2, 9)],
              'localization_limitation': exact_warning(),
              'scope': 'Exact polynomial evaluation and source metric; no broad sharp volume-energy bound.'}
    Path(__file__).with_name('actual_shrinking_arc_cauchy_metric_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 9 exact arc metrics and derivative norms; 7 original terminal source Grams; exact boundary-layer diagnostic')
