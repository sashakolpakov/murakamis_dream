#!/usr/bin/env python3
"""Exact checks for original cap-channel wall/source-jet extraction.

Checks all four endpoint kernels directly against finite P/L products
over cyclotomic fields, independent of their telescoped derivation.
Checks generic N marked-corner first/second central jets symbolically.
The all-N extraction and uniform bounds are proved in the companion note.
"""

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent


def reduce_cyclotomic(value, q, N):
    numerator, _ = sp.fraction(sp.cancel(value))
    return sp.rem(numerator, sp.cyclotomic_poly(N, q), q)


def table_kernel(N, q, delta, source, target, n):
    d = N - 1
    eps = 1 - delta ** N
    if source == target == 0:
        return 1 if n == 0 else (1 - delta) / (1 - q ** n * delta)
    if source == target == d:
        power = (n + 1) % N
        return eps * (1 - q * delta) / (N * (1 - q) * (1 - q ** power * delta))
    if source == d and target == 0:
        if n == d:
            return (1 - q * delta) / (1 - q)
        return (1 - delta) * (1 - q * delta) / ((1 - q) * (1 - q ** (n + 1) * delta))
    assert source == 0 and target == d
    return eps / (N * (1 - delta)) if n == 0 else eps / (N * (1 - q ** n * delta))


def exact_finite_product_checks():
    q, delta = sp.symbols('q delta')
    count = 0
    levels = [2, 3, 4, 5, 6, 8, 9]
    for N in levels:
        d = N - 1
        for source, target in [(0, 0), (d, d), (d, 0), (0, d)]:
            u_in = delta if source == 0 else q * delta
            u_out = delta if target == 0 else q * delta
            normalization = (1 if source == 0 else 1 - q) * (1 if target == 0 else N)
            degree = (0 if source == 0 else 1) + (0 if target == 0 else d)
            for n in range(N):
                m = (n + target - source) % N
                power = degree + n - m
                assert power in [0, N]
                scalar = 1 if power == 0 else 1 - delta ** N
                direct = (sp.sympify(scalar) / normalization
                          * sp.prod(1 - u_out * q ** j for j in range(m))
                          / sp.prod(1 - u_in * q ** j for j in range(1, n + 1)))
                expected = table_kernel(N, q, delta, source, target, n)
                assert reduce_cyclotomic(direct - expected, q, N) == 0
                value = sp.limit(sp.cancel(expected), delta, 1)
                assert sp.cancel(value - int(n == source)) == 0
                assert (degree + n - m) % N == 0
                count += 1
    return {'levels': levels, 'four_channel_direct_finite_product_identities': count,
            'zero_jets_recover_exact_original_source_target_corners': True,
            'deck_charge_indices_checked': True}


def generic_marked_jets():
    N, q, s, eps = sp.symbols('N q s eps', nonzero=True)
    delta = (1 - eps / N - (N - 1) * eps ** 2 / (2 * N ** 2)
             - (N - 1) * (2 * N - 1) * eps ** 3 / (6 * N ** 3))
    off = eps * (1 - q * delta) / (N * (1 - q) * (1 - s * delta))
    off_series = sp.series(off, eps, 0, 3).removeO().expand()
    assert sp.cancel(off_series.coeff(eps, 1) - 1 / (N * (1 - s))) == 0
    assert sp.cancel(off_series.coeff(eps, 2) - (q - s) / (N ** 2 * (1 - q) * (1 - s) ** 2)) == 0
    marked = eps / (N * (1 - delta)) + eps * q / (N * (1 - q))
    marked_series = sp.series(marked, eps, 0, 3).removeO().expand()
    assert sp.cancel(marked_series.coeff(eps, 0) - 1) == 0
    assert sp.cancel(marked_series.coeff(eps, 1) - q / (N * (1 - q)) + (N - 1) / (2 * N)) == 0
    assert sp.cancel(marked_series.coeff(eps, 2) + (N ** 2 - 1) / (12 * N ** 2)) == 0
    return {'generic_N_first_and_second_marked_source_jets': True,
            'third_delta_term_retained_before_removable_division': True}


def uniform_bound_constants():
    rho = sp.Rational(1, 16)
    # log bound followed by exp(x)<=1/(1-x), with N>=2.
    delta_constant = 1 / (1 - rho) / (1 - rho / (2 * (1 - rho)))
    assert delta_constant < 2
    assert 4 - 2 * rho > 3
    assert 1 + rho / 2 < 2
    assert 1 + rho + rho / 4 < 2
    assert 4 * rho / 3 < 2
    return {'disk_radius': '1/16', 'all_N_all_four_channels_kernel_bound': 2,
            'central_source_jet_coefficient_bound': '2*16^r',
            'pole_order_p_original_cap_functional_bound': '2N sum_{r=0}^p 16^r ||O_-r||_op',
            'scope': 'Meromorphic descended O(epsilon); individual Puiseux factors require a separate grouping/descent argument.'}


def fixed_cover_source_jets():
    q = sp.symbols('q')
    checked = 0
    for N in [2, 3, 4, 5, 6, 8, 9]:
        d = N - 1
        assert reduce_cyclotomic(sp.prod(1 - q ** k for k in range(1, N)) - N, q, N) == 0
        for r in range(1, N):
            F = sp.prod(1 - q ** k for k in range(1, r + 1))
            minus = sp.prod(1 - q ** (N - k) for k in range(1, r + 1))
            rest = sp.prod(1 - q ** k for k in range(1, d - r + 1))
            assert sp.cancel((1 - q) * sp.prod(1 - q ** k for k in range(2, r + 1)) - F) == 0
            assert reduce_cyclotomic(minus * rest - N, q, N) == 0
            checked += 1
    return {'endpoint_jet_reflection_identities': checked,
            'range_of_explicit_endpoint_jet_table': '0<=r<N',
            'cover_coordinate': 'a; epsilon=a^N',
            'all_r_trace_norm_Cauchy_bound_from_uniform_cap_frame_theorem': '||J_r||_1 <= C^2 (16N)^r',
            'fixed_cover_pole_cost': 'C^2 sum_{r=0}^p (16N)^r ||A_-r||_op',
            'scope': 'No central descent required, but cover pole order p must be fixed; a fixed central pole instead has cover order Np.'}


def primitive_nonzero_coefficient():
    # The coefficient recursion has no zero multiplier on either side.
    # Closure is compatible because prod(Q^n-b)=(-1)^(N-1)(1-b^N).
    q, b = sp.symbols('q b')
    levels = [2, 3, 4, 5, 6, 8, 9]
    for N in levels:
        product = sp.prod(q ** n - b for n in range(N))
        assert reduce_cyclotomic(product - (-1) ** (N - 1) * (1 - b ** N), q, N) == 0
    return {'nonzero_recurrence': '(Q^n-b)c_n=eta Q^(n-1)c_(n-1)',
            'assumptions': 'eta != 0, b^N != 1; full normalized D is invertible',
            'all_cyclic_coefficients_and_actual_d_corner_nonzero': True,
            'not_identified_with_the_specific_global_geometric_exterior': True}


def main():
    result = {'status': 'PASS', 'four_original_cap_channels': exact_finite_product_checks(),
              'generic_marked_central_jets': generic_marked_jets(),
              'uniform_all_N_bounds': uniform_bound_constants(),
              'fixed_cover_pole_scope_and_actual_endpoint_jets': fixed_cover_source_jets(),
              'primitive_actual_cap_retains_wall': primitive_nonzero_coefficient(),
              'scope': 'Exact original cap residue/finite-jet pushforward in the specified basis. No global weak-face coefficient or geometric winding projector asserted.'}
    (HERE / 'actual_cap_pachner_wall_charge_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
