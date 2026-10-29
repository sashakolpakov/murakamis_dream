#!/usr/bin/env python3
"""Original ordinary R entry bounds and exact slow/fast recurrence algebra."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def gaussian(q, n, k):
    row = [mp.mpc(1)]
    for a in range(1, n+1):
        row = [(row[b] if b < a else 0)+(q**(a-b)*row[b-1] if b else 0)
               for b in range(a+1)]
    return row[k]


def original_entries():
    mp.mp.dps = 90
    checks, worst = 0, mp.mpf(0)
    for N in (5, 8, 13):
        for s in (mp.mpc(0), mp.mpc('.2', '.1'), mp.mpc('-.15', '.05')):
            q = mp.exp((mp.pi*1j+s)/N)
            rho = q-1/q
            def qi(a):
                return (q**a-q**(-a))/rho
            for j in (2, 3, 4):
                for a in range(j):
                    for h in range(a+1):
                        divided = (q**(h*(h-1)/2)*rho**h
                                   *mp.fprod(qi(a-r) for r in range(h))
                                   *mp.fprod(qi(j-a+r) for r in range(h))
                                   /mp.fprod(qi(r) for r in range(1, h+1)))
                        integral = (q**(mp.mpf(h*(h-1))/2-h*(a-h))
                                    *gaussian(q*q, a, h)
                                    *mp.fprod(q**(j-a+r)-q**(-j+a-r) for r in range(h)))
                        error = abs(divided-integral)/max(1, abs(divided), abs(integral))
                        worst = max(worst, error)
                        assert error < mp.mpf('1e-80')
                        S = abs(s)
                        gauss_bound = 2**j*mp.exp(S*j*j/(2*N))
                        assert abs(gaussian(q*q, a, h)) <= gauss_bound*(1+mp.mpf('1e-80'))
                        checks += 1
    return {'original_divided_to_integral_coefficients': checks,
            'worst_relative_error': str(worst),
            'scope': 'actual positive entries; inverse uses the same exact factorial cancellation'}


def exact_defect_identity(m, r):
    """Symbolic future expansion of the actual recurrence without a_d division."""
    h = sp.Symbol('h')
    g = [[sp.Symbol(f'g_{t}_{i}') for i in range(m)] for t in range(r+1)]
    eps = [sp.Symbol(f'b_{t}') for t in range(1, r+1)]
    base = sp.symbols(f'y0:{m}')
    defects = sp.symbols(f'z0:{r+1}')
    values = list(base)
    for t in range(r+1):
        values.append(sp.expand(defects[t]-sum(g[t][i]*values[t+i] for i in range(m))))
    # Divide original equation only by a_m; every higher coefficient is h*b_t.
    original = sp.expand(defects[0]+h*sum(eps[t-1]*values[m+t] for t in range(1, r+1)))
    alpha = sp.expand(original).coeff(defects[0])
    assert sp.simplify(alpha.subs(h, 0)-1) == 0
    remainder = sp.expand(original-alpha*defects[0])
    assert sp.expand(remainder.subs(h, 0)) == 0
    # The exact backward relation has O(h) coefficients and no leading a_d.
    solved = -remainder/alpha
    residual = sp.cancel(original.subs(defects[0], solved))
    assert residual == 0
    for v in list(base)+list(defects[1:]):
        coefficient = sp.cancel(sp.diff(solved, v))
        assert coefficient.subs(h, 0) == 0
    return {'slow_order': m, 'fast_order': r,
            'exact_absorbed_denominator_at_h0': str(alpha.subs(h, 0)),
            'all_backward_couplings_vanish_at_h0': True}


def barriers():
    rows = []
    C = 3.
    for r in (1, 2, 3, 4):
        for N in (2**20, 2**24, 2**28):
            h = 1/N
            eta = N**(-1/(2*r))
            kappa, lam, gamma = 2*C, 4*C*C, 4*C
            slow_u_slack = mp.expm1(lam*h)-C*kappa*h
            slow_z_ratio = C/kappa+C*h*sum(mp.exp(lam*h*l) for l in range(1, r+1))
            fast_u_ratio = eta+C/gamma
            fast_z_ratio = h*C*gamma*eta+h*C*sum(eta**(-l) for l in range(1, r+1))
            assert slow_u_slack > 0
            assert max(slow_z_ratio, fast_u_ratio, fast_z_ratio) < 1
            rows.append({'N': N, 'fast_order': r,
                         'slow_Z_row_ratio': float(slow_z_ratio),
                         'fast_U_row_ratio': float(fast_u_ratio),
                         'fast_Z_row_ratio': float(fast_z_ratio)})
    return rows


def main():
    out = {'status': 'PASS', 'actual_integral_R_cancellation': original_entries(),
           'exact_defect_systems': [exact_defect_identity(m, r)
                                    for m, r in ((1, 1), (1, 3), (2, 1), (2, 2), (3, 2))],
           'strict_two_boundary_barriers': barriers(),
           'scope': 'Uniform all-color exponential bound and regular-arc fast-mode elimination; '
                    'classical exceptional-set gluing and geometric integral comparison unproved.'}
    Path(__file__).with_name('actual_regular_fast_color_elimination_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS original integral R coefficients, 5 exact slow/fast systems and12 strict barrier families')


if __name__ == '__main__':
    main()
