#!/usr/bin/env python3
"""Check the complete-boundary coefficient and its full-sum asymptotic.

Exact symbolic checks cover the algebraic identities. Finite-sum
asymptotic comparisons are diagnostics, not a proof of the uniform
contour estimates in the accompanying note.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def primitive(z):
    x = mp.exp(2j * mp.pi * z)
    return ((mp.polylog(2, 1) - mp.polylog(2, x)) / (2j * mp.pi)
            - 1j * mp.pi * (z*z-z) / 2)


def phase(e, u):
    return (-2*primitive(mp.mpf('.5')-u)-3*primitive(u)
            - primitive(e-u) + 1j*mp.pi*e*u)


def saddle(e):
    z = (1j + mp.sqrt(1-2*mp.exp(2j*mp.pi*e))) / 2
    return mp.atan(z) / mp.pi


def hessian(e, u):
    return -mp.pi*(2*mp.tan(mp.pi*u)+3*mp.cot(mp.pi*u)
                   +mp.cot(mp.pi*(e-u)))


def original_coefficients(N, j, max_jet):
    """Return delta_j (-1)^k b_j^(k)(-2), from the finite products."""
    sine = [mp.mpf(1)]
    for l in range(1, j+1):
        sine.append(sine[-1]*2*mp.sin(mp.pi*l/N))
    jets = [mp.mpf(1)] + [mp.mpf(0)]*max_jet
    values = [jets[k]/sine[j] for k in range(max_jet+1)]
    for l in range(1, j+1):
        d = 2*mp.cos(mp.pi*(2*l-1)/N)+2
        denominator = 4*mp.sin(mp.pi*l/N)**2
        jets = [(d*jets[k]+(k*jets[k-1] if k else 0))/denominator
                for k in range(max_jet+1)]
        carrier = mp.exp(1j*mp.pi*j*l/N)/(sine[l]*sine[j-l])
        for k in range(max_jet+1):
            values[k] += carrier*jets[k]
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dps', type=int, default=80)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-complete-boundary-coefficient-asymptotic.json')
    args = parser.parse_args()
    mp.mp.dps = args.dps
    exact = []

    def identity(name, expression):
        assert sp.simplify(sp.trigsimp(sp.expand_trig(expression))) == 0, name
        exact.append(name)

    x, t, e, u = sp.symbols('x t e u', real=True)
    identity('cosine numerator recurrence',
             4*sp.cos(x+t/2)*sp.cos(x-t/2)-2*sp.cos(2*x)-2*sp.cos(t))
    identity('ordinary-color quadratic derivative',
             sp.diff(-2*sp.cos(t), t, 2).subs(t, 0)-2)
    identity('phase ordinary-color first derivative',
             sp.cot(sp.pi*(sp.Rational(1, 2)-u))-sp.tan(sp.pi*u))
    bu = (2*sp.log(sp.cos(sp.pi*u))+sp.log(sp.sin(sp.pi*(e-u)))
          -3*sp.log(sp.sin(sp.pi*u))+sp.I*sp.pi*e)
    identity('strict horizontal curvature identity',
             sp.diff(bu, u)+sp.pi*(2*sp.tan(sp.pi*u)+3*sp.cot(sp.pi*u)
                                   +sp.cot(sp.pi*(e-u))))
    z, X = sp.symbols('z X')
    identity('selected saddle quadratic',
             (z+sp.I)*(2*z*z-2*sp.I*z+X-1)
             -(2*z**3+(X+1)*z+sp.I*(X-1)))
    k = sp.Symbol('k')
    identity('full coefficient N power', k-2+1-sp.Rational(1, 2)
             -(k-sp.Rational(3, 2)))
    H = sp.Symbol('H', real=True)
    identity('negative alias exponential loss',
             2*sp.pi*e*H-2*sp.pi*H+2*sp.pi*(1-e)*H)
    a = sp.Symbol('a', positive=True)
    identity('upper half-grid kernel', 1/(1+1/a)-a/(1+a))
    identity('lower half-grid remainder', 1/(1+a)-1+a/(1+a))
    N, j, l = sp.symbols('N j l', positive=True)
    identity('literal boundary change-of-basis phase',
             -sp.pi*j/N+sp.pi*j*(l+1)/N-sp.pi*j*l/N)
    U = sp.Symbol('U')
    x_of_u = (5*U**2-2*U+1)/(1+U)**2
    identity('selected exponential boundary equation',
             (1+U)**2*(x_of_u-U)-(1-U)**3)
    z_of_u = -sp.I*(U-1)/(U+1)
    identity('boundary exponential and tangent branches agree',
             1+2*sp.I*z_of_u-2*z_of_u**2-x_of_u)
    identity('literal adjacent delta exponent',
             ((N-1)*j-j*j-((N-1)*(j+1)-(j+1)**2))/(2*N)
             -(-sp.Rational(1, 2)+(j+1)/N))

    rows = []
    branch_rows = []
    for target in (mp.mpf('.20'), mp.mpf('.28'), mp.mpf('.35'), mp.mpf('.42')):
        for N in (100, 101, 200, 201, 400, 401):
            j = int(mp.floor(target*N))
            e = mp.mpf(j)/N
            uc = saddle(e)
            F = phase(e, uc)
            d = -hessian(e, uc)
            fu = (2*mp.log(mp.cos(mp.pi*uc))
                  +mp.log(mp.sin(mp.pi*(e-uc)))
                  -3*mp.log(mp.sin(mp.pi*uc))+1j*mp.pi*e)
            assert abs(fu) < mp.mpf(10)**(-args.dps+10)
            assert 0 < uc.real < min(e, mp.mpf('.25')) and uc.imag > 0
            assert d.real > 0
            branch_rows.append({'N': N, 'j': j, 'zero_lift_error': str(abs(fu)),
                                'critical_height': str(uc.imag),
                                'curvature_real': str(d.real)})
            actual = original_coefficients(N, j, 2)
            amplitude = (mp.sqrt(2*mp.pi)/mp.sqrt(d)
                         /(2*mp.sin(mp.pi*uc))**mp.mpf('1.5')
                         /(2*mp.sin(mp.pi*(e-uc)))**mp.mpf('.5'))
            for order in range(3):
                predicted = (N**(mp.mpf(order)-mp.mpf('1.5'))*amplitude
                             *(mp.tan(mp.pi*uc)/(4*mp.pi))**order*mp.exp(N*F))
                error = abs(actual[order]/predicted-1)
                # A finite-level diagnostic only; the note proves the bound.
                assert N*error < 300, (N, j, order, error)
                rows.append({'N': N, 'j': j, 'jet_order': order,
                             'relative_error': str(error),
                             'N_scaled_relative_error': str(N*error)})
    deps = [
        'notes/research_complete_boundary_coefficient_asymptotic.md',
        'notes/research_mixed_complete_boundary_sum.md',
        'notes/research_mixed_wire_exact_contraction.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'notes/research_uniform_factorial_and_boundary_decay.md',
    ]
    result = {
        'status': 'passed',
        'precision_decimal_digits': args.dps,
        'exact_identity_count': len(exact),
        'exact_identities': exact,
        'critical_branch_diagnostic_count': len(branch_rows),
        'critical_branch_diagnostics': branch_rows,
        'finite_sum_asymptotic_diagnostic_count': len(rows),
        'finite_sum_asymptotic_diagnostics': rows,
        'maximum_N_scaled_relative_error':
            str(max(mp.mpf(row['N_scaled_relative_error']) for row in rows)),
        'scope': ('The written argument proves the whole boundary coefficient '
                  'for every fixed ordinary jet and every compact real index '
                  'interval in (0,1/2), at both parities. Finite comparisons '
                  'diagnose its normalization; they do not prove a mixed-word '
                  'volume theorem or an unspecified complex-index continuation.'),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {f: sha256((ROOT/f).read_bytes()).hexdigest()
                                for f in deps},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'status', 'exact_identity_count', 'critical_branch_diagnostic_count',
        'finite_sum_asymptotic_diagnostic_count', 'maximum_N_scaled_relative_error')}))


if __name__ == '__main__':
    main()
