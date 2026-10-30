#!/usr/bin/env python3
"""Exact original finite channel factors; asymptotic samples are diagnostics only."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_q_hahn_negative_clock_boundary import literal_h


def sine_factorials(N):
    out = [mp.mpf(1)]
    for j in range(1, N):
        out.append(out[-1] * 2 * mp.sin(mp.pi*j/N))
    return out


def matrix(N, a, x, b, y):
    """Original Hermitian tridiagonal, including b=0 and a=0."""
    M = mp.matrix(a)
    th = mp.pi/N
    for n in range(a):
        M[n, n] = b + (x+y)/(2*mp.cos(n*th)*mp.cos((n+1)*th))
        if n:
            sn, cn = mp.sin(n*th), mp.cos(n*th)
            bn = sn**2/(cn**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
            M[n-1, n] = mp.sqrt(bn)*((x+y)*sn+1j*(y-x)*cn)/2
            M[n, n-1] = mp.conj(M[n-1, n])
    return M


def continuants(N, a, x, b, y):
    """All original leading principal determinants, without matrix inversion."""
    th = mp.pi/N
    vals = [mp.mpf(1)]
    for n in range(a):
        diag = b+(x+y)/(2*mp.cos(n*th)*mp.cos((n+1)*th))
        value = diag*vals[-1]
        if n:
            bn = mp.sin(n*th)**2/(mp.cos(n*th)**2
                  * mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
            product = bn*(x*x+y*y-2*x*y*mp.cos(2*n*th))/4
            value -= product*vals[-2]
        vals.append(value)
    return vals


def forced(N, a, x, y):
    Q = mp.exp(2j*mp.pi/N)
    return mp.fprod(x-Q**j*y for j in range(a+1, N-a))


def symbolic_checks():
    x, y, b, c, z = sp.symbols('x y b c z', positive=True)
    A = b+(x+y)/(2*z*z)
    B = ((x+y)**2-4*x*y*z*z)/(16*z**4)
    gap = b*b+(b*(x+y)+x*y)/z**2
    assert sp.factor(A*A-4*B-gap) == 0
    E = x+y+2*b*z*z+2*z*sp.sqrt(b*b*z*z+b*(x+y)+x*y)
    lam = E/(4*z*z)
    assert sp.simplify(lam*lam-A*lam+B) == 0
    Ec = E.subs(b, c)
    assert sp.simplify(16*z**4*lam*lam.subs(b, c)-E*Ec) == 0
    Dxy = (x+y)**2-4*x*y*z*z
    derivative_at_fold = sp.diff(sp.log(E*Ec/Dxy), z).subs(z, 0)
    expected = 2*(sp.sqrt(b*(x+y)+x*y)+sp.sqrt(c*(x+y)+x*y))/(x+y)
    assert sp.simplify(derivative_at_fold-expected) == 0
    assert sp.simplify(E.subs(b, 0).subs(y, 0)-x) == 0
    # The conjugate forced pair removed by one actual integer channel step.
    t = sp.symbols('t', real=True)
    assert sp.expand_complex((x-sp.exp(sp.I*t)*y)
                            *(x-sp.exp(-sp.I*t)*y)).simplify() == x*x+y*y-2*x*y*sp.cos(t)
    return dict(discriminant_recurrence_scalar_cancellation_and_fold_identities=6)


def finite_checks():
    params = [(mp.mpf('1.3'), mp.mpf('.7'), mp.mpf('1.9'), mp.mpf('2.1')),
              (mp.mpf('1.1'), 0, 0, mp.mpf('1.7')),
              (mp.mpf('1.1'), 0, mp.mpf('.8'), mp.mpf('1.7')),
              (0, mp.mpf('.8'), mp.mpf('1.2'), mp.mpf('1.7')),
              (0, 0, mp.mpf('1.2'), mp.mpf('1.7')),
              (mp.mpf('1.7'), mp.mpf('.8'), mp.mpf('1.2'), 0),
              (mp.mpf('1.7'), mp.mpf('1.2'), 0, 0),
              (mp.mpf('1.4'), 0, 0, mp.mpf('1.4'))]
    counts = dict(all_label_circles=0, direct_original_determinants=0,
                  original_Newton_to_determinant=0, single_summand_LDL=0,
                  positive_forced_products=0, adjacent_channel_ratios=0,
                  beta_step_ratios=0, forced_step_ratios=0,
                  maximal_odd_folds=0, maximal_even_folds=0)
    worst = mp.mpf(0)

    def check(actual, expected):
        nonlocal worst
        error = abs(actual-expected)/max(1, abs(expected))
        worst = max(worst, error)
        assert error < mp.mpf('1e-60'), (actual, expected, error)

    for N in range(3, 19):
        d = N-1
        q = mp.exp(1j*mp.pi/N)
        S = sine_factorials(N)
        top = d//2
        for x, b, c, y in params:
            Db, Dc = continuants(N, top, x, b, y), continuants(N, top, x, c, y)
            values = []
            for a in range(top+1):
                beta = S[2*a]/S[a]**2
                P = forced(N, a, x, y)
                s = d-2*a
                Ppositive = mp.fsum(S[s]/(S[j]*S[s-j])*x**(s-j)*y**j for j in range(s+1))
                check(P, Ppositive)
                assert Ppositive > 0 and Db[a] > 0 and Dc[a] > 0
                counts['positive_forced_products'] += 1
                for middle, D in [(b, Db[a]), (c, Dc[a])]:
                    direct = mp.det(matrix(N, a, x, middle, y)) if a else mp.mpf(1)
                    check(D, direct)
                    counts['direct_original_determinants'] += 1
                    if middle == 0 and (x == 0 or y == 0):
                        endpoint = x+y
                        pivot_product = mp.fprod(mp.sin(n*mp.pi/N)/(mp.cos(n*mp.pi/N)
                            *mp.sin((2*n-1)*mp.pi/N)) for n in range(1, a+1))
                        check(D, (endpoint/2)**a*pivot_product)
                        counts['single_summand_LDL'] += 1
                    if middle > 0 and y > 0:
                        U, V = -x/(q*middle), -middle/(q*y)
                        K = q**(a*a)*beta
                        original = literal_h(N, a, U, V)
                        check(original, (-1/q)**a*K*y**(-a)*D)
                        counts['original_Newton_to_determinant'] += 1
                values.append(beta**2*Db[a]*Dc[a]*Ppositive)
                counts['all_label_circles'] += 1
                if a == top:
                    counts['maximal_odd_folds' if N % 2 else 'maximal_even_folds'] += 1
                if a:
                    j = a-1
                    beta_ratio = (2*mp.sin((2*j+1)*mp.pi/N)
                                  *2*mp.sin((2*j+2)*mp.pi/N)
                                  /(2*mp.sin((j+1)*mp.pi/N))**2)
                    check(beta/(S[2*j]/S[j]**2), beta_ratio)
                    pair = x*x+y*y-2*x*y*mp.cos(2*mp.pi*a/N)
                    check(P/forced(N, j, x, y), 1/pair)
                    expected = beta_ratio**2*Db[a]/Db[j]*Dc[a]/Dc[j]/pair
                    check(values[a]/values[j], expected)
                    counts['beta_step_ratios'] += 1
                    counts['forced_step_ratios'] += 1
                    counts['adjacent_channel_ratios'] += 1
    counts['maximum_exact_identity_relative_error'] = str(worst)
    return counts


def integrate(f, start, end):
    if start == end:
        return mp.mpf(0)
    cuts = [start] + [mp.mpf(x) for x in ['.125', '.25', '.375', '.49', '.5', '.75', '.875']
                      if start < mp.mpf(x) < end] + [end]
    return mp.quad(f, cuts)


def circle_rate(mu, x, b, c, y):
    I = lambda v: integrate(lambda t: mp.log(2*mp.sin(mp.pi*t)), mp.mpf(0), v)
    def D(middle):
        def integrand(t):
            co = mp.cos(mp.pi*t)
            E = x+y+2*middle*co**2+2*co*mp.sqrt(middle**2*co**2+middle*(x+y)+x*y)
            return mp.log(E/(4*co**2))
        return integrate(integrand, mp.mpf(0), mu)
    J = integrate(lambda t: mp.log(abs(x-mp.exp(2j*mp.pi*t)*y)), mu, 1-mu)
    return 2*I(2*mu)-4*I(mu)+D(b)+D(c)+J


def rate_diagnostics():
    """Finite errors only: these samples are not a proof of uniform limits."""
    records = []
    with mp.workdps(45):
        patterns = [('positive', '1.3', '.7', '1.9', '2.1'),
                    ('202_equal_outer', '1.4', '0', '0', '1.4'),
                    ('one_outer_zero', '0', '0', '1.2', '1.7'),
                    ('opposite_outer_zero', '1.7', '1.2', '0', '0')]
        for N in [24, 25, 48, 49, 96, 97]:
            S = sine_factorials(N)
            top = (N-1)//2
            for name, *p in patterns:
                x, b, c, y = map(mp.mpf, p)
                Db = continuants(N, top, x, b, y)
                Dc = continuants(N, top, x, c, y)
                for a in sorted({0, N//6, top}):
                    mu = mp.mpf(a)/N
                    value = (2*mp.log(S[2*a]/S[a]**2)+mp.log(Db[a])+mp.log(Dc[a])
                             +mp.log(abs(forced(N, a, x, y))))/N
                    predicted = circle_rate(mu, x, b, c, y)
                    assert mp.isfinite(value) and mp.isfinite(predicted)
                    records.append(dict(N=N, a=a, pattern=name,
                                        normalized_log_error=float(abs(value-predicted))))
    return dict(scope='Diagnostic finite rate errors only; no monotonicity or limit asserted by sampling.',
                samples=records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = 85
    result = dict(status='PASS', precision_digits=mp.mp.dps,
                  symbolic=symbolic_checks(), finite=finite_checks(),
                  rate_diagnostics=rate_diagnostics(),
                  scope='Original finite determinants/Newton polynomials, all-channel sine factors and exact adjacent-channel ratios. Both parities and every allowed zero-pattern class. Rate samples are diagnostic; no coefficient saddle, channel Gaussian, signed sum or external-color claim.')
    target = args.output or Path(__file__).with_name('actual_positive_face_channel_rate_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
