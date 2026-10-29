#!/usr/bin/env python3
"""Exact H3 lattice/offset/Gaussian certificate; finite sums are diagnostic.

The symbolic part uses the literal seven-factorial gate and three leaf
ratios. Numerical finite-level convergence is not used to prove the
uniform complex-window theorem.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def exact_calibration():
    x, y, k = sp.symbols('x y k', real=True)
    variables = (x, y, k)
    sa, ca = 2/sp.sqrt(5), 1/sp.sqrt(5)
    s2, c2 = sp.simplify(2*sa*ca), sp.simplify(ca**2-sa**2)
    s3 = sp.simplify(3*sa-4*sa**3)
    c3 = sp.simplify(4*ca**3-3*ca)
    assert s2 == sp.Rational(4, 5)
    assert -s3 == 2/(5*sp.sqrt(5))
    assert sp.simplify(c3/s3) == sp.Rational(11, 2)

    # Rows are (limiting affine argument, factorial multiplicity,
    # exact integer offset, sine at a=atan(2)/pi, cotangent there).
    rows = []
    for v in variables:
        rows += [(2*v, 1, 0, s2, c2/s2),
                 (v, -4, 0, sa, ca/sa)]
    gate = [
        (x+y, 1, 0, s2, c2/s2),
        (1-k, 1, -1, sa, -ca/sa),
        (x, -1, 0, sa, ca/sa),
        (y, -1, 0, sa, ca/sa),
        (1-k-x, -1, -1, s2, -c2/s2),
        (1-k-y, -1, -1, s2, -c2/s2),
        (x+y+k-1, -1, 1, -s3, c3/s3),
    ]
    rows += gate
    gradient_exponentials = [sp.Integer(1)]*3
    hessian_over_pi = sp.zeros(3)
    offset_multiplier = sp.Integer(1)
    unshifted_amplitude = sp.Integer(2)**(-6)
    for arg, multiplicity, shift, sine, cotangent in rows:
        vector = sp.Matrix([sp.diff(arg, v) for v in variables])
        hessian_over_pi += multiplicity*cotangent*(vector*vector.T)
        for j in range(3):
            gradient_exponentials[j] *= (2*sine)**(multiplicity*vector[j])
        offset_multiplier *= (2*sine)**(multiplicity*shift)
        unshifted_amplitude *= sine**sp.Rational(multiplicity, 2)
    assert [sp.simplify(g) for g in gradient_exponentials] == [1, 1, 1]
    A_over_pi = sp.simplify(-hessian_over_pi)
    assert A_over_pi == sp.Rational(25, 4)*(sp.eye(3)+sp.ones(3))
    assert A_over_pi.det() == sp.Rational(15625, 16)
    assert sp.simplify(offset_multiplier) == 4
    b = sp.simplify(unshifted_amplitude*offset_multiplier)
    assert b == sp.Rational(125, 512)
    gaussian_amplitude = sp.simplify((2*sp.pi)**sp.Rational(3, 2)*b /
                                    sp.sqrt(A_over_pi.det()*sp.pi**3))
    assert gaussian_amplitude == sp.sqrt(2)/64

    leaf_amplitude = sp.simplify(sp.sqrt(s2)/(2**sp.Rational(3, 2)*sa**2))
    gate_amplitude = sp.Integer(2)**sp.Rational(-3, 2)
    for _, multiplicity, _, sine, _ in gate:
        gate_amplitude *= sine**sp.Rational(multiplicity, 2)
    gate_amplitude = sp.simplify(gate_amplitude)
    assert leaf_amplitude == sp.sqrt(10)/8
    assert gate_amplitude == 5*sp.sqrt(10)/16
    assert sp.simplify(leaf_amplitude**3*gate_amplitude*4-b) == 0

    # Exact closure t+k=D removes t with coefficient one. The three
    # physical indices i,j,k retain the full integer lattice.
    assert sp.Matrix([[1, 1]]).rank() == 1
    return {
        'critical_point': 'x=y=k=atan(2)/pi; z=1-k',
        'gradient_exponentials': ['1', '1', '1'],
        'negative_hessian_over_pi': str(A_over_pi),
        'determinant_over_pi_cubed': str(A_over_pi.det()),
        'actual_gate_output': 't=N(1-k/N)-1',
        'integer_offset_multiplier': str(sp.simplify(offset_multiplier)),
        'leaf_amplitude': str(leaf_amplitude),
        'unshifted_gate_amplitude': str(gate_amplitude),
        'summand_amplitude': str(b),
        'summed_gaussian_amplitude': str(gaussian_amplitude),
        'primitive_free_lattice': 'Z^3 in the original indices i,j,k',
        'missing_offset_would_change_amplitude_by': 'factor 4',
    }


def J(t):
    return -mp.im(mp.polylog(2, mp.exp(2j*mp.pi*t)))/(2*mp.pi)


def finite_positive_diagnostic(N, F0):
    D, M = N-1, (N-1)//2
    s = [mp.mpf(1)]
    for r in range(1, N):
        s.append(s[-1]*2*mp.sin(mp.pi*r/N))
    leaf = [N*N*s[2*r]/s[r]**4 for r in range(M+1)]
    total, states = mp.mpf(0), 0
    for i in range(M+1):
        for j in range(M+1):
            for k in range(max(0, D-i-j), M+1):
                t = D-k
                assert max(i, j) <= t <= i+j < N
                gate = s[i+j]*s[t]/(s[i]*s[j]*s[t-i]*s[t-j]*s[i+j-t])
                assert gate > 0
                total += leaf[i]*leaf[j]*leaf[k]*gate
                states += 1
    prediction = mp.sqrt(2)/64 * N**mp.mpf('1.5')*mp.exp(N*F0)
    ratio = total/prediction
    return {'N': N, 'positive_states': states,
            'ratio_to_leading_asymptotic': mp.nstr(ratio, 22),
            'N_times_relative_error': mp.nstr(N*(ratio-1), 22),
            'scope': 'finite-level diagnostic, not an asymptotic proof'}


def main():
    certificate = exact_calibration()
    with mp.workdps(70):
        a = mp.atan(2)/mp.pi
        g = J(2*a)-4*J(a)
        m = J(2*a)+J(1-a)-2*J(a)-2*J(1-2*a)-J(3*a-1)
        F0 = 3*g+m
        phase_difference = abs(F0-8*mp.catalan/mp.pi)
        assert phase_difference < mp.mpf('1e-65')
        diagnostics = [finite_positive_diagnostic(N, F0)
                       for N in (5, 8, 20, 21, 40, 41, 80, 81)]
        phase = {'integral_value': mp.nstr(F0, 55),
                 'difference_from_existing_2v8_over_pi_evaluation':
                     mp.nstr(phase_difference, 8),
                 'scope': 'numerical confirmation; exact phase evaluation is an existing seed theorem'}
    result = {'status': 'PASS', 'exact_symbolic_certificate': certificate,
              'phase_diagnostic': phase, 'finite_positive_sum_diagnostics': diagnostics,
              'scope': 'Exact algebraic Hessian, determinant, amplitude and D=N-1 offset certificate. Finite positive sums diagnose the proved asymptotic and do not prove its limit or complex uniformity.'}
    Path(__file__).with_name('actual_conway_complex_window_laplace_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS exact H3 Hessian/offset/amplitude certificate; {len(diagnostics)} finite positive diagnostics (both parities)')


if __name__ == '__main__':
    main()
