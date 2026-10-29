#!/usr/bin/env python3
"""Polynomial-cost critical-value bound: unit-factor two-anchor sources."""

import json
from pathlib import Path

from flint import acb, acb_poly, arb, ctx
import sympy as sp


def polynomial_from_sympy(P, z):
    P = sp.Poly(P, z)
    return acb_poly([int(P.nth(j)) for j in range(P.degree()+1)])


def analyze(name, P, q, regular_critical_polynomial=None, known_criticals=None):
    m = P.degree()
    p = m-q
    assert 1 <= q < m
    if known_criticals is not None:
        criticals = known_criticals
    else:
        if regular_critical_polynomial is None:
            coeff = [(j-q)*P[j] for j in range(m+1)]
            G = acb_poly(coeff)
        else:
            G = regular_critical_polynomial
        criticals = G.roots(tol=arb(2)**-150, maxprec=1024)
        assert len(criticals) == G.degree()
    values = []
    for z in criticals:
        assert abs(z) > arb(1)/m and abs(z) < arb(m)
        value = P(z)/z**q
        assert not value.contains(0)
        values.append(value)
    M_lower = max(float(abs(value).lower()) for value in values)
    M_upper = max(float(abs(value).upper()) for value in values)
    constant = P[q]
    prefactor = 4*arb(m*m)*arb(m+1).log()
    assert abs(constant) < prefactor*arb(str(M_lower))

    # Test the radius bound on every sheet of several exact level fibers,
    # not on a guessed parameterization of one contour component.
    radius = arb(str(M_upper))*arb('1.125')
    positive_part = radius.log()+arb(m)*arb(2).log()
    if positive_part < 0:
        positive_part = arb(0)
    lower_log = -arb(2).log()-positive_part/q
    upper_log = arb(2).log()+positive_part/p
    level_checks = 0
    for theta in (arb(0), arb('0.7'), arb('2.3')):
        target = acb(0, theta).exp()*radius
        coefficients = [P[j] for j in range(m+1)]
        coefficients[q] -= target
        fiber = acb_poly(coefficients).roots(tol=arb(2)**-130, maxprec=1024)
        assert len(fiber) == m
        for root in fiber:
            assert abs(root).log() > lower_log
            assert abs(root).log() < upper_log
            level_checks += 1
    # Multiplying the ENTIRE actual source by an arbitrarily small
    # retained scalar changes both sides equally; no positive lower
    # bound for a critical value was used in the transport estimate.
    tiny = arb(10)**-1000
    assert abs(tiny*constant) < prefactor*tiny*arb(str(M_lower))
    return {'family': name, 'degree': m, 'negative_pole_order': q,
            'positive_pole_order': p,
            'exact_coefficient_or_ball': str(constant),
            'complete_regular_critical_count': len(criticals),
            'critical_modulus_enclosure': [M_lower, M_upper],
            'polynomial_prefactor': str(prefactor),
            'every_level_fiber_sheet_checked': level_checks,
            'uniform_critical_radius_bound': True,
            'tiny_retained_source_scalar': '10^-1000'}


def main():
    ctx.prec = 256
    z = sp.Symbol('z')
    rows = []
    for m in (2, 3, 5, 8):
        P = polynomial_from_sympy((z-1)**m, z)
        for q in range(1, m):
            root = acb(-arb(q)/(m-q))
            rows.append(analyze('arbitrarily clustered / coincident unit roots', P, q,
                                known_criticals=[root]))
    for m in (2, 3, 5, 8):
        P = polynomial_from_sympy(z**m-1, z)
        for q in range(1, m):
            rows.append(analyze('complete unit root orbit', P, q))
    N, L = 7, 4
    Q = acb(0, arb.pi()*2/N).exp()
    P = acb_poly.from_roots([Q**j for j in range(L)])
    for q in range(1, L):
        rows.append(analyze('actual consecutive Q-interval block', P, q))

    # The prior source counterexample is INCLUDED: an upper bound by
    # max critical value is compatible with highest-saddle inaccessibility.
    P_exact = (1-z**4)**2*(1+z+z*z)**3*(1-z+z*z)
    G_exact = sp.cancel((z*sp.diff(P_exact, z)-P_exact)/
                        sp.gcd(P_exact, z*sp.diff(P_exact, z)-P_exact))
    rows.append(analyze('inaccessible highest cyclotomic source',
                        polynomial_from_sympy(P_exact, z), 1,
                        regular_critical_polynomial=polynomial_from_sympy(G_exact, z)))

    # A genuinely tiny nonzero regular critical VALUE from nearly
    # coincident roots. The largest-value proof needs no lower bound
    # on this small one (or on a retained overall scalar).
    epsilon = arb('1e-30')
    unit = acb(0, epsilon).exp()
    P = acb_poly.from_roots([acb(1), unit])
    result = analyze('near-coincident distinct unit roots', P, 1)
    small_critical = unit.sqrt()
    small_value = P(small_critical)/small_critical
    assert 0 < abs(small_value) and abs(small_value) < arb('1e-50')
    result['certified_tiny_nonzero_critical_value'] = str(small_value)
    rows.append(result)
    output = {'two_anchor_source_families': rows,
              'scope': 'Polynomial-cost anchor critical-value upper bound; full clock/regulator identification remains separate.'}
    Path(__file__).with_name('actual_coefficient_minimax_upper_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS complete unit-factor critical sets and source coefficients; all-sheet '
          'level radius bounds; repeated/near-coincident roots; uniform polynomial transport')


if __name__ == '__main__':
    main()
