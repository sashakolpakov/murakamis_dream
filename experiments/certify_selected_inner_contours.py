#!/usr/bin/env python3
"""Rigorous Arb enclosure of actual angular contour phase bounds.

Uses the exact one-variable maximum reductions proved in
notes/selected_inner_angular_contour.md. All pass/fail comparisons
are outward-rounded Arb ball comparisons. Floating point values
are printed only after successful proof checks.
"""

import json
from fractions import Fraction
from pathlib import Path

from flint import acb, acb_poly, arb, ctx


ctx.prec = 192
PI = arb.pi()
I = acb(0, 1)


def rational(x):
    x = Fraction(x)
    return arb(x.numerator) / x.denominator


def interval(lo, hi):
    midpoint = (lo + hi) / 2
    radius = (hi - lo) / 2
    return rational(midpoint) + arb(0, 1) * rational(radius)


def constants():
    roots = acb_poly([-1, 0, 1, 1]).roots(tol=1e-48, maxprec=512)
    Y = next(z for z in roots if z.real < 0 and z.imag < 0)
    X = Y / (1 + Y - Y * Y)
    x = X.log() / (2 * PI * I) + 1
    y = Y.log() / (2 * PI * I) + 1
    assert arb('0.86') < x.real < arb('0.88')
    assert arb('0.09') < x.imag < arb('0.10')
    return x, y


X_GEO, Y_GEO = constants()
U_GEO, H_GEO = X_GEO.real, X_GEO.imag


def J_real(z):
    # Only called with strict 0<Re(z)<1; the endpoint formulas below
    # implement the one-sided mark separately, without a branch-cut ball.
    if not (z.real > 0 and z.real < 1):
        return arb('nan')
    X = (2 * PI * I * z).exp()
    P = (PI * PI / 6 - X.polylog(2)) / (2 * PI * I)
    return (P - PI * I / 2 * (z * z - z)).real


def polynomial_phase_imag(x, y):
    return (3 * x + 2 * y - x * x - x * y - y * y).imag


def phase_interior(x, y):
    return 3 * J_real(x) - J_real(y) - J_real(x - y) - PI * polynomial_phase_imag(x, y)


def phase_left(x, tau):
    # Re J(i tau)=-pi |tau|/2 in the one-sided marked strip.
    y = acb(0, tau)
    return 3 * J_real(x) + PI * abs(tau) / 2 - J_real(x - y) - PI * polynomial_phase_imag(x, y)


def phase_right(x, tau):
    # x-y=i(Im x-tau) has the same explicit one-sided boundary value.
    y = acb(x.real, tau)
    return (3 * J_real(x) - J_real(y) + PI * abs(x.imag - tau) / 2
            - PI * polynomial_phase_imag(x, y))


def theta(u, tau):
    return (PI * acb(u, tau)).sin().arg()


def root(x):
    X = (2 * PI * I * x).exp()
    T = 1 / X - 1
    v = (T + (T * T + 4).sqrt()) / 2
    if not (v.real > 0 and v.imag > 0):
        return None
    y = (-v).log() / (2 * PI * I) + 1
    if not (y.real > 0 and (x - y).real > 0):
        return None
    return y


def connector_values(x, y):
    u, h, lam = x.real, x.imag, y.imag
    left = [phase_left(x, arb(0)), phase_left(x, lam)]
    right = [phase_right(x, h), phase_right(x, lam)]
    # If lam>=h, derivative on the right connector is always positive;
    # otherwise it is strictly decreasing, with at most one stationary point.
    if not (lam > h):
        d_lam = theta(u, lam) + PI * (3 * u - rational(Fraction(5, 2)))
        d_h = theta(u, h) + PI * (3 * u - rational(Fraction(5, 2)))
        if not (d_lam < 0 or d_h > 0):
            cot = (PI * u).cot()
            parameter = (PI * (3 * u - rational(Fraction(5, 2)))).tan() / (-cot)
            if not (parameter > -1 and parameter < 1):
                return None
            tau = parameter.atanh() / PI
            # Retain a candidate unless its enclosure lies strictly outside
            # every possible actual connector interval in this cell.
            if not (tau < lam or tau > h):
                right.append(phase_right(x, tau))
    return left, right


def prove_segment(name, x_from_parameter, limits, include_saddle=False, extra_weight=arb(0)):
    stack = [(Fraction(0), Fraction(1), 0)]
    proven = 0
    deepest = 0
    max_upper = {key: -1e100 for key in limits}
    while stack:
        lo, hi, depth = stack.pop()
        s = interval(lo, hi)
        x = x_from_parameter(s)
        y = root(x)
        values = None
        if y is not None:
            connectors = connector_values(x, y)
            if connectors is not None:
                left, right = connectors
                weight = extra_weight(x) if callable(extra_weight) else extra_weight
                values = {'left': [z + weight for z in left],
                          'right': [z + weight for z in right]}
                if include_saddle:
                    values['saddle'] = [phase_interior(x, y) + weight]
        good = values is not None and all(
            z.is_finite() and z < limits[key]
            for key, entries in values.items() for z in entries)
        if good:
            proven += 1
            deepest = max(deepest, depth)
            for key, entries in values.items():
                max_upper[key] = max(max_upper[key], *(float(z.upper()) for z in entries))
            continue
        if depth >= 24:
            raise RuntimeError(f'Unresolved {name} at dyadic parameter [{lo},{hi}]: {values}')
        middle = (lo + hi) / 2
        stack.append((middle, hi, depth + 1))
        stack.append((lo, middle, depth + 1))
    return {'name': name, 'verified_dyadic_cells': proven, 'maximum_depth': deepest,
            'rigorous_bounds': {key: str(value) for key, value in limits.items()},
            'largest_proven_cell_upper_bounds_float_display_only': max_upper}


def main():
    a, b = rational(Fraction(51, 100)), rational(Fraction(99, 100))
    # This acb enclosure is also a rigorous positive gap for the selected
    # reduced critical value; volume calibration is a separate theorem.
    critical = phase_interior(X_GEO, Y_GEO)
    assert critical > arb('0.45010')
    assert critical < arb('0.45012')
    minimum_upper_height = H_GEO / (100 * (1 - U_GEO))
    assert minimum_upper_height > arb('0.007')
    upper_kernel_bound = critical - 2 * PI * minimum_upper_height
    assert upper_kernel_bound < arb('0.407')
    bounds_upper = {'left': arb('0.200'), 'right': arb('0.445')}
    first = prove_segment('upper_constant_height',
                          lambda s: acb(a + (U_GEO - a) * s, H_GEO), bounds_upper)
    second = prove_segment('upper_sloped_height',
                           lambda s: acb(U_GEO + (b - U_GEO) * s,
                                         H_GEO * (1 - U_GEO - (b - U_GEO) * s) / (1 - U_GEO)),
                           bounds_upper)
    lower = prove_segment('lower_height_minus_0.1',
                          lambda s: acb(a + (b - a) * s, arb('-0.1')),
                          {'left': arb('0.400'), 'right': arb('0.400'), 'saddle': arb('0.400')},
                          include_saddle=True, extra_weight=-PI / 5)
    edge_limits = {'left': arb('0.440'), 'right': arb('0.440'), 'saddle': arb('0.440')}
    vertical = []
    for label, ulo, uhi in [('left', Fraction(5099, 10000), Fraction(5101, 10000)),
                            ('right', Fraction(9899, 10000), Fraction(9901, 10000))]:
        u_box = interval(ulo, uhi)
        h_upper = H_GEO if label == 'left' else H_GEO * (1 - u_box) / (1 - U_GEO)
        vertical.append(prove_segment(f'{label}_upper_vertical_source_box',
                                      lambda s, u=u_box, h=h_upper: acb(u, h * s),
                                      edge_limits, include_saddle=True))
        vertical.append(prove_segment(f'{label}_lower_vertical_source_box',
                                      lambda s, u=u_box: acb(u, -s / 10),
                                      edge_limits, include_saddle=True,
                                      extra_weight=lambda x: 2 * PI * x.imag))
    result = {'status': 'RIGOROUS_ARB_PASS', 'precision_bits': ctx.prec,
              'selected_cubic_critical_rate_enclosure': str(critical),
              'minimum_upper_height_enclosure': str(minimum_upper_height),
              'upper_kernel_phase_bound_given_analytic_outer_maximum': str(upper_kernel_bound),
              'geometric_log_x_enclosure': str(X_GEO), 'geometric_log_y_enclosure': str(Y_GEO),
              'parameter_domain': '0.51<=Re x<=0.99', 'segments': [first, second, lower],
              'vertical_source_boxes': vertical,
              'scope': 'One-dimensional rigorous contour phase bounds after the proved exact maximum reductions; no outer lattice alias or volume calibration asserted.'}
    output = Path(__file__).with_name('selected_inner_contour_certificate.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
