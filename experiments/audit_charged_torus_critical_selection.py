#!/usr/bin/env python3
"""Only-coordinate-pole coefficient sources can miss a unique highest saddle."""

import json
from pathlib import Path

from flint import acb_poly, arb, ctx
import mpmath as mp
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import graph_blocks, segment_coordinates, setup


def rational_example():
    z, X, Y = sp.symbols('z X Y')
    a, b = sp.Rational(91, 100), sp.Rational(9, 200)
    f = 1/z+a*z+b*z*z
    factor = (z-1)*(z+10)*(9*z+10)
    assert sp.cancel(100*z*z*sp.diff(f, z)-factor) == 0
    values = [sp.cancel(f.subs(z, point))
              for point in (sp.Integer(1), sp.Integer(-10), sp.Rational(-10, 9))]
    assert values == [sp.Rational(391, 200), sp.Rational(-47, 10), sp.Rational(-167, 90)]
    assert abs(values[1]) > max(abs(values[0]), abs(values[2]))
    assert all(sp.diff(f, z, 2).subs(z, point) != 0
               for point in (1, -10, sp.Rational(-10, 9)))
    variance = sp.cancel((1+a+4*b)/values[0])
    assert variance == sp.Rational(418, 391)
    H = X*Y**3+a*X**3*Y+b*X**4
    assert sp.cancel(H.subs({X: z, Y: 1})-z*z*f) == 0
    for n in range(1, 5):
        actual = sp.Poly(sp.expand(H**n), X, Y).coeff_monomial(X**(2*n)*Y**(2*n))
        expected = sp.Poly(sp.expand((z*f)**n), z).coeff_monomial(z**n)
        assert actual == expected
    mp.mp.dps = 100
    rows = []
    aa, bb = mp.mpf(91)/100, mp.mpf(9)/200
    for n in (20, 50, 100, 200):
        moment = mp.mpf(0)
        for v in range(n//3+1):
            if (n-3*v) % 2:
                continue
            u = (n-3*v)//2
            moment += mp.factorial(n)/(mp.factorial(u+2*v)*mp.factorial(u)*mp.factorial(v))*aa**u*bb**v
        ratio = moment*mp.sqrt(2*mp.pi*n*mp.mpf(418)/391)/(mp.mpf(391)/200)**n
        assert moment > 0 and abs(ratio-1) < mp.mpf(20)/n
        rows.append({'n': n, 'exact-combinatorial/Gaussian_ratio': str(ratio)})
    return {'critical_points': ['1', '-10', '-10/9'],
            'critical_values': list(map(str, values)),
            'selected_exponential_base': '391/200',
            'unique_highest_regular_critical_modulus': '47/10',
            'variance': str(variance),
            'homogeneous_uniform_charge_identity': True,
            'asymptotic_diagnostics': rows}


def unit_cyclotomic_example():
    z, X, Y = sp.symbols('z X Y')
    P = (1-z**4)**2*(1+z+z*z)**3*(1-z+z*z)
    G = 15*z**8-2*z**7+11*z**6+2*z**5+2*z**3-3*z*z-2*z+1
    repeated = (z-1)*(z+1)*(z*z+1)*(z*z+z+1)**2
    assert sp.expand(z*sp.diff(P, z)-P-repeated*G) == 0
    assert sp.degree(P, z) == 16
    assert sp.degree(sp.gcd(P, G), z) == 0
    assert sp.degree(sp.gcd(G, sp.diff(G, z)), z) == 0
    exact_G = sp.Poly(G, z)
    assert exact_G.count_roots(-sp.oo, sp.oo) == 2
    assert exact_G.count_roots(sp.Rational(59700, 100000),
                               sp.Rational(59701, 100000)) == 1
    assert exact_G.count_roots(sp.Rational(36853, 100000),
                               sp.Rational(36854, 100000)) == 1
    radical = (z**4-1)*(z*z+z+1)*(z*z-z+1)
    assert sp.rem(z**12-1, radical, z) == 0
    R = sp.Rational(1, 3)
    upper = sp.cancel((1+R**4)**2*(1+R+R*R)**2*(1+R*R+R**4)/R)
    assert upper == sp.Rational(103408396, 14348907)
    assert upper < sp.Rational(720671, 100000)
    assert sp.expand(P-(1-z**4)**2*(1+z+z*z)**2*(1+z*z+z**4)) == 0

    ctx.prec = 256
    polynomial = acb_poly([int(sp.expand(G).coeff(z, j)) for j in range(9)])
    roots = polynomial.roots(tol=arb(2)**-180, maxprec=1024)
    assert len(roots) == 8

    def value(w):
        return (1-w**4)**2*(1+w+w*w)**3*(1-w+w*w)/w

    entries = [(root, value(root)) for root in roots]
    entries.sort(key=lambda pair: float(abs(pair[1]).mid()), reverse=True)
    top_root, top = entries[0]
    next_root, next_value = entries[1]
    assert top_root.real > arb('0.59700') and top_root.real < arb('0.59701')
    assert top_root.imag.contains(0)
    assert top.real > arb('7.22573') and top.real < arb('7.22575')
    assert top.imag.contains(0)
    assert next_root.real > arb('0.36853') and next_root.real < arb('0.36854')
    assert next_root.imag.contains(0)
    assert next_value.real > arb('6.82894') and next_value.real < arb('6.82897')
    assert all(abs(val) < arb('1.88') for _, val in entries[2:])
    source_bound = arb(int(sp.numer(upper)))/arb(int(sp.denom(upper)))
    assert source_bound < abs(top)
    # All eight simple regular criticals have been isolated, and no zero
    # of P is included. This is the complete critical-value comparison.
    assert all(abs(top) > abs(val) for _, val in entries[1:])

    P_hom = (Y**4-X**4)**2*(Y*Y+X*Y+X*X)**3*(Y*Y-X*Y+X*X)
    H = X**16*Y**2*P_hom
    assert sp.Poly(H, X, Y).total_degree() == 34
    assert sp.cancel(H.subs({X: z, Y: 1})/z**17-P/z) == 0
    levels = []
    for n in (7, 19, 31):
        N, d = 17*n+1, 17*n
        assert N % 12 == 0
        assert sp.rem(z**N-1, radical, z) == 0
        assert 34*n == 2*d and d == N-1
        levels.append({'n': n, 'N': N, 'source_charge_per_anchor': d,
                       'all_factor_phases_actual_Nth_roots': True,
                       'incidence_defects': [14*n, -14*n],
                       'coordinate_cut_deficits': [n, 15*n]})
    return {'all_regular_critical_root_and_value_balls':
                [{'root': str(root), 'value': str(val), 'modulus': str(abs(val))}
                 for root, val in entries],
            'exact_source_circle_radius': '1/3',
            'exact_source_circle_bound': str(upper),
            'strict_source_circle_vs_unique_highest_gap': str(abs(top)-source_bound),
            'homogeneous_uniform_charge_socle_family': levels,
            'scope': 'Not asserted to be an original braid or fixed-diagram root-interval family.'}


def actual_alternating_defect():
    rows = []
    for width, word in ((3, [1, -2, 1, -2]),
                        (3, [1, -2, 1, 1, -2, -2]),
                        (4, [1, -2, 3]*3)):
        H = HardyNetwork(7, 1)
        S = setup(H, width, word)
        B = len(S['paths'])
        assert B == len(word) and all(len(path) == 1 for path in S['paths'])
        h = [(2*j+1) % H.N for j in range(B)]
        G = graph_blocks(H, S, h)
        mapping, _ = segment_coordinates(H, S, h)
        parents = list(range(G['anchor_count']))

        def root(a):
            while parents[a] != a:
                a = parents[a]
            return a

        for edge in G['blocks']:
            if edge['closure']:
                u, v = root(edge['tail']), root(edge['head'])
                assert u != v
                parents[u] = v
        representatives = {root(j): j for j in range(B)}
        assert len(representatives) == B
        position = {j: representatives[root(j)] for j in range(len(parents))}
        degrees = [0]*B
        for edge in G['blocks']:
            if not edge['closure']:
                degrees[position[edge['tail']]] += edge['length']
                degrees[position[edge['head']]] += edge['length']
        under_counts = [0]*B
        for under_input in S['under']:
            under_counts[position[mapping[under_input][0]]] += 1
        assert under_counts == [1]*B
        tau = [None]*B
        for e, event in enumerate(S['events'][:B]):
            previous = position[mapping[event['input']][0]]
            assert tau[previous] is None
            tau[previous] = e
        visited, v = set(), 0
        while v not in visited:
            visited.add(v)
            v = tau[v]
        assert v == 0 and len(visited) == B
        defects = [value-2*(H.N-1) for value in degrees]
        assert defects == [h[v]-h[tau[v]] for v in range(B)]
        rows.append({'width': width, 'word': word, 'original_clocks': h,
                     'oriented_overevent_return': tau, 'incidence_defects': defects,
                     'one_underencounter_per_remaining_anchor': True})
    return rows


def main():
    result = {'rational_positive_coefficient_example': rational_example(),
              'unit_cyclotomic_factor_example': unit_cyclotomic_example(),
              'actual_alternating_defect_identity': actual_alternating_defect(),
              'conclusion': 'The fixed torus source can miss a unique highest regular critical value; no knot counterexample claimed.'}
    Path(__file__).with_name('charged_torus_critical_selection_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS exact normalized coefficient examples; complete Arb critical-value '
          'certificates; strict source-circle bounds; homogeneous cyclotomic socle levels')


if __name__ == '__main__':
    main()
