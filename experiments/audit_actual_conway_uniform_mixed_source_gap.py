#!/usr/bin/env python3
"""Full-algebra seed expansion and exact stationary identities for the global gap.

Finite checks retain the repeated-root algebra. The exponential separation
itself is proved by concavity/compactness in the note, not inferred here.
"""
import itertools
import json
from pathlib import Path
import sympy as sp

from audit_actual_pure_conway_auxiliary_color_leaf import (
    root_data, chebyshev_u, coordinates, predicted,
)
from audit_actual_positive_newton_multiplication import (
    mul, add_scaled, reduce_poly, trim,
)


def stationary_identities():
    b, t, y = sp.symbols('b t y', real=True)
    difference = sp.sin(y)*sp.sin(b-t)-sp.sin(t)*sp.sin(b-y)
    assert sp.trigsimp(sp.expand_trig(difference-sp.sin(b)*sp.sin(y-t))) == 0
    sa, ca = sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))
    sin2a = 2*sa*ca
    sin2aminushalfpi = sa**2-ca**2
    ex = sp.simplify(sin2a*ca/(sa*sin2aminushalfpi))
    ez = sp.simplify(sin2aminushalfpi/ca**2)
    assert ex == 2 and ez == 1 and ca**2/sa**2 == sp.Rational(1, 2)
    return {
        'interior_sign_identity': 'sin(y)sin(b-t)-sin(t)sin(b-y)=sin(b)sin(y-t)',
        'F2_free_critical_output': '1/2',
        'F2_free_critical_leaf': 'atan(sqrt(2))/pi',
        'exp_m_input': str(ex), 'exp_m_output': str(ez),
        'exp_g_leaf_derivative': '1/2',
    }


def exact_seeds(N):
    prime, _, _, sine, nodes, basis = root_data(N)
    monic = [1]
    for node in nodes:
        monic = mul(monic, [-node % prime, 1], prime)

    def polynomial(coeffs):
        out = [0]*N
        for c, p in zip(coeffs, basis):
            add_scaled(out, p, c, prime)
        return trim(out)

    def multiply(a, b):
        return reduce_poly(mul(a, b, prime), monic, prime)

    def add(*terms):
        out = [0]
        for term in terms:
            add_scaled(out, term, 1, prime)
        return trim(out)

    actual, core, radical = [], [], []
    for j, u in enumerate(chebyshev_u(N, prime), 1):
        # Independent actual Chebyshev loop, then the genuine turn.
        original = [(-1)**(j-1)*a % prime for a in u]
        actual_coeffs = coordinates(original, basis, prime)[::-1]
        assert actual_coeffs == predicted(N, j, sine, prime)
        core_coeffs = [0]*N
        if j > N//2:
            h = N-j
            for v in range(h, (N-1)//2+1):
                core_coeffs[v] = N*N*sine[2*v]*pow(
                    sine[v]**2*sine[v-h]*sine[v+h] % prime, -1, prime) % prime
        radical_coeffs = [(a-c) % prime for a, c in zip(actual_coeffs, core_coeffs)]
        assert not any(radical_coeffs[:(N+1)//2])
        actual.append(polynomial(actual_coeffs))
        core.append(polynomial(core_coeffs))
        radical.append(polynomial(radical_coeffs))

    pairs_a, pairs_c = {}, {}
    for i, j in itertools.product(range(N), repeat=2):
        assert multiply(radical[i], radical[j]) == [0]
        pairs_a[i, j] = multiply(actual[i], actual[j])
        pairs_c[i, j] = multiply(core[i], core[j])

    count = 0
    for i, j, k in itertools.product(range(N), repeat=3):
        original_seed = multiply(pairs_a[i, j], actual[k])
        core_seed = multiply(pairs_c[i, j], core[k])
        expanded = add(core_seed,
                       multiply(radical[i], pairs_c[j, k]),
                       multiply(radical[j], pairs_c[i, k]),
                       multiply(radical[k], pairs_c[i, j]))
        assert original_seed == expanded
        delta = add(original_seed, [(-x) % prime for x in core_seed])
        delta_coeffs = coordinates(delta, basis, prime)
        assert not any(delta_coeffs[:(N+1)//2])
        count += 1
    return {'N': N, 'prime': prime, 'all_original_three_color_seeds': count,
            'full_radical_pair_products_zero': N*N,
            'seed_error_supported_above_half': True,
            'comparison': 'full polynomial remainder modulo degree-N repeated-root polynomial'}


if __name__ == '__main__':
    rows = [exact_seeds(N) for N in range(3, 12)]
    result = {'status': 'PASS',
              'exact_stationary_identities': stationary_identities(),
              'full_original_seed_expansions': rows,
              'scope': 'Exact all-color seed expansions and support in the full repeated-root algebra, plus the symbolic stationary contradiction. The uniform exponential gap follows from the written strict-concavity, boundary-barrier and compactness proof; finite fields do not test signs or asymptotic dominance.'}
    Path(__file__).with_name('actual_conway_uniform_mixed_source_gap_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS',sum(r['all_original_three_color_seeds'] for r in rows),
          'full-polynomial mixed seeds; exact F2 and alias-stationarity certificates')

