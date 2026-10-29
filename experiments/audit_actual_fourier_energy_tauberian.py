#!/usr/bin/env python3
"""Check exact actual energy data and the scope of the positive Tauberian criterion."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def actual_figure_eight_energies():
    # The exact root values a_j=Q^j+Q^-j suffice; c_n=1 is the
    # independently proved WHOLE actual figure-eight Newton source.
    roots = {2: [-2], 3: [-1, -1], 4: [0, -2, 0]}
    out = []
    for N, nodes in roots.items():
        def value(X):
            total = basis = 1
            for node in nodes:
                basis *= X-node
                total += basis
            return total
        K = value(2)
        ordinary = [value(node) for node in nodes]
        remainder = sum(v*v for v in ordinary)
        energy = K*K+remainder
        out.append({'N': N, 'actual_K': K, 'ordinary_colors': ordinary,
                    'actual_remainder': remainder, 'actual_energy': energy})
    energies = [v['actual_energy'] for v in out]
    assert energies == [26, 171, 732]
    determinant = energies[0]*energies[2]-energies[1]**2
    assert determinant == -10209
    return {'original_source_values': out, 'cross_level_Hankel_determinant': determinant,
            'scope': 'excludes an automatic raw all-level moment/log-convex inference only'}


def positive_sequence_counterexample():
    lam, t = mp.mpf('.7'), mp.mpf('.001')
    # Even levels >=2 contribute 1/(exp(2t)-1), odd levels >=3
    # have only unit energy; their sum is an analytic term at t=0.
    rows = []
    for t in map(mp.mpf, ('.1', '.01', '.001', '.0001')):
        even = 1/mp.expm1(2*t)
        odd = mp.exp(-3*(lam+t))/(1-mp.exp(-2*(lam+t)))
        scaled = t*(even+odd)
        assert abs(scaled-mp.mpf('.5')) < 2*t
        rows.append({'t': str(t), 't_times_Z': str(scaled)})
    return {'exact_even_part': '1/(exp(2t)-1)',
            'pole_constant': '1/2', 'full_energy_rate_exists': False,
            'approach': rows, 'scope': 'logical positive-sequence example, not a knot'}


def laplace_moment_check():
    rows = []
    for alpha in (mp.mpf('.5'), mp.mpf('1'), mp.mpf('2.5')):
        for k in (0, 1, 2, 4):
            moment = mp.quad(lambda x: mp.exp(-(k+1)*x)*x**(alpha-1)/mp.gamma(alpha),
                             [0, 1, mp.inf])
            target = mp.power(k+1, -alpha)
            assert abs(moment-target) < mp.mpf('1e-25')
            rows.append({'alpha': str(alpha), 'moment_order': k,
                         'positive_Gamma_Laplace_moment': str(moment)})
    # The actual no-dip conclusion is proved by the finite cumulative
    # inequalities in the note, not inferred from these quadratures.
    n, A, L, delta = sp.symbols('n A L delta', positive=True)
    assert sp.simplify(sp.log(n**(A+1)*sp.exp(L*delta*n))/n
                       -(A+1)*sp.log(n)/n-L*delta) == 0
    return rows


def main():
    mp.mp.dps = 70
    out = {'status': 'PASS', 'actual_source_scope_check': actual_figure_eight_energies(),
           'positive_pole_without_full_limit': positive_sequence_counterexample(),
           'positive_measure_moments': laplace_moment_check(),
           'scope': 'Self-contained Tauberian implication; no actual critical singularity '
                    'or cross-level no-deep-dips estimate has been proved.'}
    Path(__file__).with_name('actual_fourier_energy_tauberian_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS exact original energies/Hankel obstruction, positive-pole counterexample and12 Laplace moments')


if __name__ == '__main__':
    main()
