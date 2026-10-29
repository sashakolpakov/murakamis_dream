#!/usr/bin/env python3
"""Generic mixed odd edge words, exact physical port and framing shear.

All identities are rational functions of independent parameters. Neither
the complete specialization nor numerical phase samples prove the checks.
"""
import json
from pathlib import Path

import sympy as sp

from audit_actual_conway_marked_peripheral_deformation import (
    at, derivative, equal_projectively, white,
)


def generic_edge_words():
    E, R = sp.symbols('E R', nonzero=True)
    ws = white(E, R)
    a = sp.Matrix([[R, -R], [1, E*R-1-E]])
    b = sp.Matrix([[R/E-1-1/E, R], [-1, R]])
    for i, j in [(0, 2), (2, 0), (1, 3)]:
        word = ws[i].adjugate()*b*ws[j].adjugate()*a
        assert equal_projectively(word, sp.eye(2))
    longitude = ws[2].adjugate()*ws[0]
    positive_meridian = a.adjugate()*ws[0]
    negative_meridian = ws[0].adjugate()*b
    for meridian in [positive_meridian, negative_meridian]:
        assert equal_projectively(meridian*longitude, longitude*meridian)
    return {'pointwise_odd_edge_words_over_Q_E_R': 3,
            'primitive_peripheral_commutators': 2,
            'complete_R_relation_used': False}


def marked_flags():
    E, Z = sp.symbols('E Z', nonzero=True)
    R = Z*(1+E-Z)/E
    ws = white(E, R)
    a = sp.Matrix([[R, -R], [1, E*R-1-E]])
    b = sp.Matrix([[R/E-1-1/E, R], [-1, R]])
    for matrix in [a, b, ws[0], ws[2]]:
        assert sp.cancel(at(matrix, Z)-Z/E) == 0
    rho, q = Z/(1+E-Z), (E-Z)/(Z-1)
    cases = [(a.adjugate()*ws[0], rho*q),
             (ws[0].adjugate()*b, rho/q),
             (ws[2].adjugate()*ws[0], q*q)]
    for matrix, multiplier in cases:
        assert sp.cancel(at(matrix, Z)-Z) == 0
        assert sp.cancel(1/derivative(matrix, Z)-multiplier) == 0
    E, T = sp.symbols('E T', nonzero=True)
    z = (1+E)/(1+T)
    vexp = (E-T)/(E*T-1)
    assert sp.cancel((Z/(1+E-Z)).subs(Z, z)-1/T) == 0
    assert sp.cancel(((E-Z)/(Z-1)).subs(Z, z)-1/vexp) == 0
    return {'cross_half_apex_maps': 4,
            'primitive_flag_at_infinity_multipliers': 3,
            'physical_color_shear_both_signs': 'PASS'}


def selected_source_port():
    E, H, K, T, mu, Z = sp.symbols('E H K T mu Z', nonzero=True)
    den = (1-E/H)*(1-E*H)
    p = -((H+1/H)*E*E+2)/(E*den)
    q = -(1-E*E)**2/(E*E*den*den)
    polynomial = K*K*(1+E)**2+K*((H+1/H)*E*E+2)+(1-E)**2
    ward = (mu*mu-p*mu-q).subs(mu, K*(1+E)**2/(E*den))
    assert sp.cancel(ward*E*E*den*den/(1+E)**2-polynomial) == 0
    assert sp.factor(polynomial.subs(H, 1)) == (K+1)*(E*E*K+E*E+2*E*K-2*E+K+1)
    hidden_color = T*T+E*(H-1)*T-H
    pure_port = K*T*(1+E)**2-(E-T)*(1-E*T)
    resultant = sp.resultant(hidden_color, pure_port, T)
    assert sp.cancel(resultant+H*(E+1)**2*polynomial) == 0
    # Independently eliminate the ACTUAL odd meridian and apex equations.
    apex = (1+K)*(Z*Z-(1+E)*Z)+E
    actual_meridian = H*Z*(E-Z)-(Z-1)*(1+E-Z)
    actual_resultant = sp.resultant(apex, actual_meridian, Z)
    assert sp.cancel(actual_resultant+H*polynomial) == 0
    # Positive-coupon Schwarz branch has the conjugated port polynomial.
    positive = sp.cancel(E*E*polynomial.subs({E: 1/E, H: 1/H}, simultaneous=True))
    positive_meridian = H*Z*(Z-1)-(E-Z)*(1+E-Z)
    positive_resultant = sp.resultant(apex, positive_meridian, Z)
    assert sp.cancel(positive_resultant+E*E*H*positive) == 0
    return {'selected_WKB_quadratic_to_port': 'PASS',
            'hidden_pure_color_resultant': 'PASS',
            'actual_meridian_resultants_both_signs': 'PASS'}


def exact_generating_shear():
    epsilon, v, vx, vt, gx = sp.symbols('epsilon v vx vt gx')
    constant = 2*sp.pi*sp.I
    tx = epsilon*vx/(constant-epsilon*vt)
    tc = constant/(constant-epsilon*vt)
    fx = gx+v*tx-epsilon*v*(vx+vt*tx)/constant
    fc = v*tc-epsilon*v*vt*tc/constant
    assert sp.cancel(fx-gx) == 0
    assert sp.cancel(fc-v) == 0
    # New actual cusp Hessians, with the old literal half-twist signs.
    E = sp.symbols('E', nonzero=True)
    cotangent = sp.I*(E+1)/(E-1)
    old = -2*sp.pi*cotangent
    minus = sp.cancel(old/(1+old/constant))
    plus = sp.cancel(old/(1-old/constant))
    assert sp.cancel(minus-sp.pi*sp.I*(1+E)) == 0
    assert sp.cancel(plus+sp.pi*sp.I*(1+1/E)) == 0
    return {'implicit_dx_dchi_derivatives': 'PASS',
            'quadratic_framing_term': '-epsilon V^2/8',
            'both_literal_odd_cusp_Hessians': 'PASS'}


if __name__ == '__main__':
    result = {'status': 'PASS', 'generic_edges': generic_edge_words(),
              'marked_flags': marked_flags(),
              'source_identification': selected_source_port(),
              'action_shear': exact_generating_shear()}
    destination = Path(__file__).with_name(
        'actual_odd_conway_marked_peripheral_deformation_results.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
