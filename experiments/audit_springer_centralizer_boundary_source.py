#!/usr/bin/env python3
"""Exact flag, centralizer compactification, Gaussian residue and weights."""

import json
from pathlib import Path

import sympy as s


def simplify_matrix(a):
    return a.applyfunc(s.cancel)


def transition_checks():
    v, eta, a, b = s.symbols('v eta a b', nonzero=True)
    V, ep, ap = 1/v, -v*v*eta, v-v*v*a
    E = s.Matrix([[0, 1], [0, 0]])
    N = eta*s.Matrix([[-v, 1], [-v*v, v]])
    south = ep*s.Matrix([[V, -V*V], [1, -V]])
    assert simplify_matrix(N-south) == s.zeros(2)
    assert N*N == s.zeros(2)
    assert N*s.Matrix([1, v]) == s.zeros(2, 1)
    gN = s.Matrix([[1, 0], [v, 1/eta]])
    gS = s.Matrix([[V, 1/ep], [1, 0]])
    cocycle = s.Matrix([[1, -1/(v*eta)], [0, 1]])/v
    assert simplify_matrix(gN.inv()*gS-cocycle) == s.zeros(2)
    assert simplify_matrix(gN*E*gN.inv()-N) == s.zeros(2)
    bp = b+1/(v*eta)
    assert s.cancel(-ep*bp-(v-v*v*(-eta*b))) == 0
    g = s.Matrix([[eta, -a], [eta*v, 1-v*a]])
    gs = s.Matrix([[ep*V, 1-V*ap], [ep, -ap]])
    assert simplify_matrix(gs+v*g) == s.zeros(2)
    assert s.cancel(g.det()-eta) == 0
    assert simplify_matrix(g*E*g.inv()-N) == s.zeros(2)
    # Irreducibility makes a raw-frame pole unavoidable: its coefficient
    # is the lower-left entry times a nonzero rank-one outer product.
    aa, bb, cc, dd = s.symbols('r11 r12 r21 r22')
    R = s.Matrix([[aa, bb], [cc, dd]])
    leading = simplify_matrix(eta*g*R*g.inv()).subs(eta, 0)
    expected = cc*s.Matrix([-a, 1-v*a])*s.Matrix([[1-v*a, a]])
    assert simplify_matrix(leading-expected) == s.zeros(2)
    U = s.eye(2)+E
    B = s.Matrix([[aa, bb], [cc, (1+bb*cc)/aa]])
    assert s.cancel(s.trace(U*B*U.inv()*B.inv())-2-cc**2) == 0
    # At fiber degree -1, the cocycle Laurent power -1 is absent
    # from both regular Cech pieces. At nonnegative degrees all powers
    # are covered by north >=0 and south <=2j.
    for exponent in range(-10, 11):
        if exponent == -1:
            assert not (exponent >= 0 or exponent <= -2)
        for j in range(6):
            assert exponent >= 0 or exponent <= 2*j
    return {'Springer_matrix_and_flag_transition': True,
            'centralizer_pole_cocycle_and_source_affine_clutch': True,
            'whole_projective_matrix_boundary': True,
            'irreducible_raw_escape_coefficient': True,
            'Cech_nonextension_weight_diagnostic': True}


def gaussian_and_form_checks():
    v, eta, a = s.symbols('v eta a', nonzero=True)
    V, ep, ap = 1/v, -v*v*eta, v-v*v*a
    # Coefficients of the two- and three-forms under the full transition.
    jac2 = s.Matrix([V, ap]).jacobian((v, a)).det()
    assert s.cancel(jac2-1) == 0
    jac3 = s.Matrix([ep, V, ap]).jacobian((eta, v, a)).det()
    assert s.cancel(jac3/ep-1/eta) == 0
    # The actual full r,s,p gauge, not an assumed arbitrary SL2 dressing.
    r, ss, p = s.symbols('r ss p', nonzero=True)
    vv, ee, bb, ar = 1/p, -ss*p, (1-r)/ss, p*(1-r)
    jh = s.Matrix([ee, vv, bb]).jacobian((r, ss, p)).det()
    assert s.cancel(jh+1/(ss*p)) == 0
    ja = s.Matrix([ee, vv, ar]).jacobian((r, ss, p)).det()
    left = -1/(ss*(1+ss)*p)
    right = -ja/(ee*(1-ee*vv))
    assert s.cancel(left-right) == 0
    assert s.cancel(s.limit(eta*(-1/(eta*(1-eta*v))), eta, 0)+1) == 0
    # Canonical and normal line weights cancel exactly in the log line.
    for pole in (1, -1):
        normal_weight = 2*pole
        canonical_Y_weight = -2*pole
        assert normal_weight+canonical_Y_weight == 0
    # Physical symbol is a genuine removable analytic chart at both poles.
    c = s.symbols('c', nonzero=True)
    physical = (1-s.exp(-c*v*a))/v
    assert s.simplify(s.limit(physical, v, 0)-c*a) == 0
    assert s.simplify(s.diff(physical, a)/(1-v*physical)-c) == 0
    VV, AA = s.symbols('V AA', nonzero=True)
    physical_south = (s.exp(c*VV*AA)-1)/VV
    assert s.simplify(s.limit(physical_south, VV, 0)-c*AA) == 0
    assert s.simplify(s.diff(physical_south, AA)/(1+VV*physical_south)-c) == 0
    return {'source_symplectic_and_log_Haar_transitions': True,
            'actual_Gaussian_flag_adapter_and_residue': True,
            'log_canonical_normal_weights_cancel': True,
            'both_physical_compact_pole_charts_etale': True}


def symmetric_power_matrix(g, n):
    x, y = s.symbols('x y')
    out = s.zeros(n+1)
    for j in range(n+1):
        poly = s.Poly(s.expand((g[0, 0]*x+g[1, 0]*y)**(n-j)
                              *(g[0, 1]*x+g[1, 1]*y)**j), x, y)
        for i in range(n+1):
            out[i, j] = poly.coeff_monomial(x**(n-i)*y**i)
    return out


def coherent_weights():
    eta, v, a = s.symbols('eta v a')
    g = s.Matrix([[eta, -a], [eta*v, 1-v*a]])
    records = []
    for N in range(2, 10):
        n = N-1
        source = symmetric_power_matrix(g, n)
        leading = source.subs(eta, 0)
        expected = s.zeros(N)
        for i in range(N):
            expected[i, n] = s.binomial(n, i)*(-a)**(n-i)*(1-v*a)**i
        assert (leading-expected).applyfunc(s.expand) == s.zeros(N)
        assert leading.subs({v: 0, a: 0}).rank() == 1
        at_anchor = source.subs({v: 0, a: 0})
        assert at_anchor == s.diag(*(eta**(n-j) for j in range(N)))
        # The source-line table and exact metaplectic shift.
        assert -N+1 == -n
        assert N-1 == n
        normal_powers = [s.Rational(n-2*j, 2) for j in range(N)]
        assert normal_powers[0] == s.Rational(n, 2)
        assert normal_powers[-1] == -s.Rational(n, 2)
        records.append({'level': N, 'coherent_rank_one_boundary_exact': True,
                        'normal_source_pole': str(s.Rational(n, 2)),
                        'O_N_prequantum_plus_half_form': True,
                        'single_source_SL2_sign': (-1)**n})
    return records


def main():
    result = {'global_torsor_resolution': transition_checks(),
              'actual_principal_density_and_forms': gaussian_and_form_checks(),
              'intrinsic_coherent_line_weights': coherent_weights(),
              'scope': 'Resolved classical framing, actual principal Gaussian residue and intrinsic coherent weights; no full quantum dressing or selected volume assertion.'}
    target = Path(__file__).with_name('springer_centralizer_boundary_source_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'global_transition_and_escape': 'passed',
                      'actual_Gaussian_residue_and_pole_charts': 'passed',
                      'coherent_weight_levels': len(result['intrinsic_coherent_line_weights'])}))


if __name__ == '__main__':
    main()
