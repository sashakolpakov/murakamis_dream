#!/usr/bin/env python3
"""Saddle/source-divisor certificates; model counts are not knot computations.

The extension's global source and geometric inputs remain hypotheses.
These exact checks catch the full-twist factor two, amplitude parity,
coordinate zeros, partial-filling restrictions and slope-ray caveats.
The density-one proof is analytic and is not inferred from finite counts.
"""
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


def implicit_certificate():
    x1, x2, e1, e2 = sp.symbols('x1 x2 e1 e2')
    t1, t2 = sp.symbols('tau1 tau2', nonzero=True)
    a, b, c = sp.symbols('a b c')
    xs, es = (x1, x2), (e1, e2)
    phi = sp.pi*sp.I*(t1*x1*x1+t2*x2*x2)+a*x1**4+b*x1*x1*x2*x2+c*x2**4
    equations = sp.Matrix([sp.diff(phi, x)+sp.pi*sp.I*e*(x-1) for x, e in zip(xs, es)])
    zero = dict.fromkeys(xs+es, 0)
    saddle_derivative = -equations.jacobian(xs).subs(zero).inv()*equations.jacobian(es).subs(zero)
    assert saddle_derivative == sp.diag(1/(2*t1), 1/(2*t2))
    for x, e, eq in zip(xs, es, equations):
        psi = sp.cancel(sp.diff(phi, x)/x)
        assert sp.expand(eq-(x*(psi+sp.pi*sp.I*e)-sp.pi*sp.I*e)) == 0
        assert sp.cancel((sp.pi*sp.I/(psi+sp.pi*sp.I*e)).subs(zero)) in (1/(2*t1), 1/(2*t2))
    return {'implicit_derivative_at_zero': str(saddle_derivative),
            'coordinate_factorization': 'xi_i=epsilon_i times a unit',
            'nonlinear_mixed_phase_included': str(phi)}


def exact_amplitude_models():
    x, y, e, f, n = sp.symbols('x y epsilon1 epsilon2 n')
    xi, yi = e/(2*sp.I+e), f/(2*sp.I+f)
    monomial = x*x*y**4
    pulled = sp.factor(monomial.subs({x: xi, y: yi}))
    unit = sp.cancel(pulled/(e**2*f**4))
    assert sp.cancel(unit-(e+2*sp.I)**(-2)*(f+2*sp.I)**(-4)) == 0
    assert unit.subs({e: 0, f: 0}) != 0
    for amplitude in (monomial, x*x-y*y):
        assert sp.expand(amplitude.subs(x, -x)-amplitude) == 0
        assert sp.expand(amplitude.subs(y, -y)-amplitude) == 0

    difference = sp.cancel(xi**2-yi**2)
    factored = 4*sp.I*(e-f)*(e*f+sp.I*(e+f))/((e+2*sp.I)**2*(f+2*sp.I)**2)
    assert sp.cancel(difference-factored) == 0
    # The second numerator factor cannot vanish at nonzero REAL e,f:
    # its real part is ef. The only real slope divisor is e=f.
    leading = -(e*e-f*f)/4
    ray = difference.subs({e: 1/n, f: 1/(2*n)})
    assert sp.limit(n*n*ray, n, sp.oo) == -sp.Rational(3, 16)
    assert leading.subs({e: 1, f: sp.Rational(1, 2)}) == -sp.Rational(3, 16)
    opposite = difference.subs({e: 1/n, f: -1/n})
    assert leading.subs({e: 1, f: -1}) == 0
    assert sp.limit(n**3*opposite, n, sp.oo) == -sp.I/2
    assert difference.subs(f, e) == 0

    # A nonzero full germ can vanish identically after a partial filling.
    full = y*y
    assert full != 0 and full.subs(y, 0) == 0
    return {'coordinate_monomial_pullback': str(pulled),
            'nonmonomial_divisor_factorization': str(factored),
            'same_sign_diagonal_ray': 'identically exceptional',
            'ray_q_1_2_leading_constant': '-3/16 at order 2',
            'ray_q_1_minus1': 'leading polynomial vanishes but order-3 coefficient -i/2 survives',
            'partial_filling_warning': 'a(x,y)=y^2 restricts identically to zero at y=0'}


def integer_box_diagnostics():
    def square_at_slope(p):
        # xi(1/p)=1/(1+2ip), calculated in exact rational arithmetic.
        denominator = (1+4*p*p)**2
        return Fraction(1-4*p*p, denominator), Fraction(-4*p, denominator)

    rows = []
    for T in (8, 16, 32, 64):
        for sigma1, sigma2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            first = [square_at_slope(sigma1*p) for p in range(T, 2*T+1)]
            second = [square_at_slope(sigma2*p) for p in range(T, 2*T+1)]
            bad = sum(x == y for x in first for y in second)
            assert bad == (T+1 if sigma1 == sigma2 else 0)
            rows.append({'T': T, 'signs': [sigma1, sigma2], 'exceptional_tuples': bad,
                         'total_tuples': (T+1)**2,
                         'exact_fraction': str(Fraction(bad, (T+1)**2))})
    return {'amplitude_model': 'a(x,y)=x^2-y^2; tau1=tau2=i',
            'boxes': rows,
            'scope': 'Exact finite counts in a model; the general density-one theorem is proved separately.'}


def gaussian_absolute_remainder():
    c, e, p, N, x = sp.symbols('c epsilon p N x', nonzero=True)
    xi = e/(2*sp.I*c+e)
    phi = -sp.pi*c*x*x
    action = phi+sp.pi*sp.I*e*(x-1)**2/2
    A = sp.pi*(c-sp.I*e/2)
    B = -sp.pi*sp.I*e
    assert sp.cancel(xi-B/(2*A)) == 0
    assert sp.cancel(action.subs(x, xi)-(sp.pi*sp.I*e/2+B*B/(4*A))) == 0
    # The exact Gaussian integral is sqrt(pi/(NA))*exp(N action(xi))
    # times [xi^2+1/(2NA)]. Its error is absolute at xi=0.
    relative = sp.cancel((1/(2*N*A*xi*xi)).subs(e, 1/p))
    assert sp.cancel(relative-(-2*c*p*p+sp.I*p)/(sp.pi*N)) == 0

    with mp.workdps(80):
        diagnostics = []
        for slope in (-4, 4):
            for level in (20, 40):
                epsilon = mp.mpf(1)/slope
                crit = epsilon/(2j+epsilon)
                aa = mp.pi*(1-1j*epsilon/2)
                stationary = -mp.pi*crit*crit+mp.pi*1j*epsilon*(crit-1)**2/2
                exact = mp.sqrt(mp.pi/(level*aa))*mp.exp(level*stationary)*(crit*crit+1/(2*level*aa))
                # Real-contour integration is independent of the completion formula.
                integral = mp.quad(lambda u: (u*u/level)/mp.sqrt(level)*mp.exp(
                    -mp.pi*u*u+mp.pi*1j*level*epsilon*(u/mp.sqrt(level)-1)**2/2),
                    [-mp.inf, 0, mp.inf])
                error = abs(integral-exact)/abs(exact)
                assert error < mp.mpf('1e-60')
                diagnostics.append({'slope': slope, 'model_level': level,
                                    'relative_integration_error': mp.nstr(error, 8)})
    return {'exact_relative_correction_for_fixed_slope': str(relative),
            'absolute_amplitude': 'xi^2+1/(2NA)',
            'warning': 'The O_p(1/N) coefficient grows like p^2; no joint level/slope limit is claimed.',
            'real_contour_model_checks': diagnostics,
            'scope': 'An elementary Gaussian model, not a Kashaev source or a verification of the global source hypotheses.'}


def main():
    result = {'status': 'PASS', 'implicit_saddle': implicit_certificate(),
              'amplitude_models': exact_amplitude_models(),
              'integer_slope_diagnostics': integer_box_diagnostics(),
              'absolute_stationary_phase_model': gaussian_absolute_remainder(),
              'scope': 'Exact saddle and source-divisor algebra plus explicitly labeled analytic models. The transfer retains the original source/gap/geometry hypotheses; finite counts do not prove general density one or any new knot volume equality.'}
    Path(__file__).with_name('general_long_filling_source_divisor_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS factor-two saddle, coordinate divisor, rational rays, 16 exact slope boxes and 4 absolute-Gaussian checks')


if __name__ == '__main__':
    main()
