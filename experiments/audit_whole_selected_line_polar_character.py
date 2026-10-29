#!/usr/bin/env python3
"""Independent scalar connection checks; no knot volume theorem is assumed."""

import json
from pathlib import Path

import sympy as sp


def polar_integration():
    s = sp.symbols('s', nonzero=True)
    checks = []
    for order in range(1, 9):
        coeff = {j: sp.Rational((j + 11) * (-1 if j % 2 else 1), j + 12)
                 for j in range(-order, 5)}
        omega = sum(a * s ** j for j, a in coeff.items())
        primitive = sum(a * s ** (j + 1) / (j + 1)
                        for j, a in coeff.items() if j != -1)
        primitive += coeff.get(-1, 0) * sp.log(s)
        assert sp.cancel(sp.diff(primitive, s) - omega) == 0
        B = sum(-coeff[-r - 1] * s ** (-r) / r
                for r in range(1, order))
        assert sp.expand(primitive - B).coeff(s, -1) == 0
        checks.append({'connection_pole_order': order,
                       'polar_primitive_degree': max(0, order - 1)})
    return checks


def ramification_and_frame():
    s, S = sp.symbols('s S', nonzero=True)
    gauge_checks = 0
    for e in range(1, 7):
        h = s ** e
        assert sp.diff(S / h, s) == -e * S * s ** (-e - 1)
        for nu in (-5, -1, 0, 2, 7):
            g = s ** nu * (1 + 2 * s) / (1 - 3 * s + s ** 2)
            regular = sp.cancel(sp.diff(g, s) / g - nu / s)
            assert sp.denom(regular).subs(s, 0) != 0
            gauge_checks += 1
    return {'ramification_orders': 6,
            'meromorphic_gauges_with_no_higher_polar_part': gauge_checks}


def physical_ray_characters():
    # Define b_r = kappa**r (x_r+i*y_r). Substitution in the primitive
    # makes its REAL part x_r N**(r/e), independently of the root mark.
    N = sp.symbols('N', positive=True)
    x, y = sp.symbols('x y', real=True)
    records = []
    for e in range(1, 6):
        for r in range(1, 2 * e + 2):
            value = (x + sp.I * y) * N ** sp.Rational(r, e)
            rate = sp.simplify(2 * sp.pi * sp.re(value) / N)
            assert sp.simplify(rate - 2 * sp.pi * x * N ** (sp.Rational(r, e) - 1)) == 0
            if r < e:
                assert sp.limit(rate, N, sp.oo) == 0
            elif r == e:
                assert sp.simplify(rate - 2 * sp.pi * x) == 0
            else:
                assert rate.subs(x, 0) == 0
            records.append({'cover_degree': e, 'primitive_degree': r,
                            'rate_power': str(sp.Rational(r, e) - 1)})
    # The e-th coefficient is independent of which e-th root was marked.
    a, b = sp.symbols('a b', real=True)
    assert sp.simplify(2 * sp.pi * sp.re((a + sp.I * b) / (sp.pi * sp.I)) - 2 * b) == 0
    return records


def amplified_unit_and_two_characters():
    h = sp.symbols('h')
    u = 1 + sp.I * (sp.exp(2 * h) - 1)
    F = -sp.pi ** 2 * sp.log(u) / h ** 2
    polar = -2 * sp.I * sp.pi ** 2 / h
    assert sp.limit(h * F, h, 0) == -2 * sp.I * sp.pi ** 2
    assert sp.limit(h ** 2 * sp.diff(F, h), h, 0) == 2 * sp.I * sp.pi ** 2
    assert sp.limit(F - polar, h, 0).is_finite
    assert 2 * sp.im(-2 * sp.I * sp.pi ** 2) == -4 * sp.pi ** 2
    # Verify actual distinct zeros for A=1, B=0, C1=C2=1. At these
    # points the derivative numerator is nonzero, hence dlog has a pole.
    records = []
    for k in range(-4, 5):
        point = 1 / ((2 * k + 1) * sp.pi * sp.I)
        assert sp.simplify(sp.exp(1 / point) + 1) == 0
        assert sp.simplify(-sp.exp(1 / point) / point ** 2) != 0
        records.append(k)
    return {'amplified_unit_leading_norm_shift': '-4*pi**2',
            'two_character_log_derivative_simple_poles_checked': len(records)}


def pointing_and_peripheral_pullback():
    h, M, M0, C = sp.symbols('h M M0 C', nonzero=True)
    # A meridian shift cannot see an h-only character.
    factor = sp.exp(C / h)
    assert factor.subs(M, sp.exp(h) * M) == factor
    assert sp.cancel(sp.diff(factor, h) / factor + C / h**2) == 0
    # Restricting a partial connection before taking the marked path
    # drops a genuine leading polar term.
    potential = (M - M0) / h**2
    assert sp.diff(potential, h).subs(M, M0) == 0
    pulled_full = (sp.diff(potential, h) + sp.diff(potential, M)).subs(M, M0 + h)
    assert sp.cancel(pulled_full - sp.diff(1 / h, h)) == 0
    # Retained Gaussian root phase: nonzero polar character, zero real rate.
    N = sp.symbols('N', integer=True, positive=True)
    polar_phase = -sp.pi**2 / h
    assert sp.simplify(polar_phase.subs(h, sp.pi * sp.I / N) - sp.pi * sp.I * N) == 0
    assert sp.re(polar_phase.subs(h, sp.pi * sp.I / N)) == 0
    return {'h_only_character_preserves_meridian_transport': True,
            'full_peripheral_pullback_retains_extra_character': True,
            'marked_root_phase_has_zero_norm_rate': True}


def main():
    report = {
        'scope': 'Rank-one meromorphic-line criterion, not a construction for knots',
        'polar_integration': polar_integration(),
        'ramification_and_frame': ramification_and_frame(),
        'physical_ray_characters': physical_ray_characters(),
        'nonautomatic_hypotheses': amplified_unit_and_two_characters(),
        'pointing_and_peripheral_pullback': pointing_and_peripheral_pullback(),
        'all_checks_passed': True,
    }
    target = Path(__file__).with_name('whole_selected_line_polar_character_results.json')
    target.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({
        'all_checks_passed': True,
        'polar_integrations': len(report['polar_integration']),
        'frame_checks': report['ramification_and_frame']['meromorphic_gauges_with_no_higher_polar_part'],
        'ray_characters': len(report['physical_ray_characters']),
        'result_file': str(target),
    }, indent=2))


if __name__ == '__main__':
    main()
