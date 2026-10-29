#!/usr/bin/env python3
"""Whole actual source on a denominator-avoiding complex circle.

Finite tests supplement the uniform sparse-ODE and transfer proof.
The candidate 5_2 classical radial integral is only a diagnostic: this
script does not construct its actual quantum operator or certify volume.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import quad

from audit_actual_pointed_a_bulk_agmon import coefficients


def actual_generic_color(j, Q):
    total = term = mp.mpc(1)
    for r in range(1, j):
        term *= Q**j + Q**(-j) - Q**r - Q**(-r)
        total += term
    return total


def homogeneous_row(j, Q):
    cm1, c01, cp1, D1 = coefficients(Q, Q**(j + 1))
    cm2, c02, cp2, D2 = coefficients(Q, Q**(j + 2))
    return [-D2 * cm1, D1 * cm2 - D2 * c01,
            D1 * c02 - D2 * cp1, D1 * cp2]


def circle_case(N):
    J = 1 + (N - 1) // 2
    start = J - 2
    radius = mp.mpf(3) / (2 * N**5)
    roots = 12
    source_maximum = mp.mpf(0)
    denominator_minimum = mp.inf
    error_maximum = mp.mpf(0)
    output = []
    for ell in range(roots):
        s = radius * mp.exp(2j * mp.pi * ell / roots)
        Q = mp.exp(2j * mp.pi / N + 2 * s / N)
        source = [actual_generic_color(j, Q) for j in range(start, start + 3)]
        source_maximum = max(source_maximum, *(abs(z) for z in source))
        state = source[:]
        for j in range(start, N - 2):
            row = homogeneous_row(j, Q)
            denominator_minimum = min(denominator_minimum, abs(row[-1]))
            next_color = -sum(row[i] * state[i] for i in range(3)) / row[3]
            state = state[1:] + [next_color]
        direct = actual_generic_color(N, Q)
        error = abs(state[-1] - direct) / max(1, abs(direct))
        error_maximum = max(error_maximum, error)
        assert error < mp.mpf('1e-70'), (N, ell, error)
        output.append(state[-1])
    original = actual_generic_color(N, mp.exp(2j * mp.pi / N))
    circle_error = abs(sum(output) / roots - original) / max(1, abs(original))
    assert circle_error < mp.mpf('1e-45'), (N, circle_error)
    assert denominator_minimum > mp.mpf(N)**(-40)
    assert source_maximum < N**5
    return {"N": N, "actual_initial_colors": [start, start + 2],
            "whole_source_circle_points": roots,
            "maximum_entire_initial_source": float(source_maximum),
            "minimum_actual_leading_denominator": mp.nstr(denominator_minimum, 14),
            "largest_exact_recurrence_relative_error": mp.nstr(error_maximum, 8),
            "Cauchy_sampling_relative_error": mp.nstr(circle_error, 8)}


def exact_classical_symbols():
    Y, L = sp.symbols('Y L')
    cm, c0, cp, D = coefficients(sp.Integer(1), Y)
    P = Y**2 + Y**(-2) - Y - Y**(-1) - 2
    assert sp.factor((cm + c0 * L + cp * L**2) / cp - (L**2 - P * L + 1)) == 0
    actual_cubic = D * (L - 1) * (cm + c0 * L + cp * L**2)
    assert actual_cubic.coeff(L, 3) != 0 or sp.Poly(actual_cubic, L).degree() == 3
    # Original 5_2 Newton recurrence, followed by the proved classical
    # canonical map. This alone is NOT an actual quantum-operator proof.
    x, t, z = Y + 1/Y, L + 1/L, Y*L + 1/(Y*L)
    u = sp.factor((z + 2)/(x + t))
    e = sp.factor(1/(x - u - 1/u))
    transformed = sp.factor(u*u*e*e + (2 - 1/u + 1/u**2)*u*e + 1 - 1/u)
    candidate = (L**3*Y**7 + L**2*(-Y**7+2*Y**6+2*Y**5-Y**3+Y**2)
                 + L*(Y**5-Y**4+2*Y**2+2*Y-1) + 1)
    assert sp.factor(transformed - (L+Y)**2*candidate /
                     (L**2*(Y-1)**4*(Y+1)**4*(L*Y+1))) == 0
    assert sp.factor(candidate.subs(Y, 1) - (L + 1)**3) == 0
    assert sp.factor(candidate.subs(Y, -1) + (L - 1)**3) == 0
    return {"figure_eight_actual_classical_symbol": "(L-1)(L^2-P(Y)L+1), fixed prefactor retained",
            "five_two_canonical_classical_identity_exact": True,
            "five_two_quantum_operator_verified_here": False}


def nearby_pole_fixture():
    s, epsilon = sp.symbols('s epsilon', nonzero=True)
    # Exact source (s-epsilon) cancels the inside pole, even if epsilon
    # is smaller than every chosen polynomial normal radius.
    actual = (s-epsilon)/(s-epsilon)/s
    truncated = -epsilon/(s-epsilon)/s
    assert sp.residue(actual, s, 0) == 1
    assert sp.residue(truncated, s, 0) == 1
    assert sp.residue(truncated, s, epsilon) == -1
    return {"actual_entire_source_Cauchy_value": 1,
            "constant_truncation_Cauchy_value_enclosing_nearby_pole": 0}


def spectral_integrals():
    def figure_eight(x):
        c = np.cos(2*np.pi*x)
        P = 4*c*c - 2*c - 4
        return np.arccosh(abs(P)/2) if abs(P) > 2 else 0.

    def five_two(x):
        Y = np.exp(2j*np.pi*x)
        coefficients = [Y**7, -Y**7+2*Y**6+2*Y**5-Y**3+Y**2,
                        Y**5-Y**4+2*Y**2+2*Y-1, 1]
        return max(0., float(np.log(np.max(np.abs(np.roots(coefficients))))))

    h4, err4 = quad(figure_eight, .5, 1, points=[2/3], epsabs=1e-11, limit=250)
    v4 = float(2*mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3))))
    assert abs(2*np.pi*h4-v4) < 1e-9
    h5, err5 = quad(five_two, .5, 1, epsabs=2e-10, limit=250)
    return {"figure_eight_half_integral": h4, "figure_eight_volume_scale": 2*np.pi*h4,
            "figure_eight_integral_error_estimate": err4,
            "five_two_candidate_half_integral": h5,
            "five_two_candidate_volume_scale": 2*np.pi*h5,
            "five_two_integral_error_estimate": err5,
            "scope": "Figure-eight calibration numerical supplement; 5_2 is a candidate-symbol diagnostic only."}


def main():
    mp.mp.dps = 160
    data = {"status": "PASS", "actual_source_circles": [circle_case(N) for N in [12, 16, 24, 32, 48]],
            "exact_classical_calculations": exact_classical_symbols(),
            "nearby_pole_source_test": nearby_pole_fixture(),
            "classical_integrals": spectral_integrals(),
            "scope": "Actual source and full singular transfer checked. The general proof is in the note; no broad classical-volume inequality is inferred from these tests."}
    Path(__file__).with_name('actual_macroscopic_a_spectral_upper_bound_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
