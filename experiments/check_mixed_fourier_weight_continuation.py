#!/usr/bin/env python3
"""Exact Fourier-weight identities and margins for its full contour comparison.

The uniform exponential statement follows from the written residue proof.
Finite Barnes evaluations independently check its normalization and signs.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import mpmath as mp
import sympy as sp

from audit_exact_factorial_interpolation import sine_factorial

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--dps', type=int, default=70)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-mixed-fourier-weight-continuation.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    mp.mp.dps = args.dps
    symbolic, exact, margins, midpoint, diagnostics = [], [], [], [], []

    def ident(name, expr):
        assert sp.simplify(expr) == 0, (name, sp.simplify(expr))
        symbolic.append(name)

    n, t, a, x, y = sp.symbols('n t a x y', real=True)
    v = a+sp.I*t
    marked_log = sp.I*sp.pi*v/2-sp.I*sp.pi*v*(v+1)/(2*n)
    real_log = sp.re(sp.expand(marked_log))
    ident('left midpoint marked exponential', real_log.subs(a,-sp.Rational(1,2))+sp.pi*t/2)
    ident('right midpoint marked exponential', real_log.subs(a,n-sp.Rational(1,2))-sp.pi*t/2)
    b = sp.symbols('b', positive=True)
    ident('left reciprocal midpoint modulus',
          (b+b**-1)*b/n-(1+b*b)/n)
    ident('right reciprocal midpoint modulus',
          1/((b+b**-1)*b*n)-1/(n*(1+b*b)))
    ident('left midpoint kernel cancels growth',
          ((1+b*b)/n)/(1+b*b)**2-1/(n*(1+b*b)))
    ident('right midpoint kernel cancels growth',
          (1/(n*(1+b*b)))/(1+b*b)**2-1/(n*(1+b*b)**3))
    phi = lambda z: sp.pi*(z-z*z)/2
    ident('upper/lower action reflection',
          sp.re(sp.expand(2*sp.I*phi(x+sp.I*y)))+sp.pi*y*(1-2*x))
    ident('upper rectangle height budget',
          sp.Rational(3,250)*(1+2*sp.Rational(91,250))-sp.Rational(324,15625))
    ident('bottom-side exponential reserve',
          sp.Rational(1,100)-sp.Rational(1,500)-sp.Rational(1,125))

    field = sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3))
    one, zero = field.one, field.zero
    cv = lambda z: field.from_sympy(sp.sympify(z))

    def check(name, value):
        assert value == zero, (name,field.to_sympy(value))
        exact.append(name)

    def poly_eval(coeffs, point):
        val = zero
        for c in reversed(coeffs):
            val = val*point+c
        return val

    roots = [(2,sp.I), (3,(1+sp.I*sp.sqrt(3))/2),
             (4,(1+sp.I)/sp.sqrt(2)), (6,(sp.sqrt(3)+sp.I)/2)]
    for N, qs in roots:
        r = cv(qs)**-2
        P = [one]
        for j in range(1,N):
            P.append(P[-1]*(1-r**j))
        coeffs = [sum((r**(-k*j)/P[j] for j in range(N)),zero)/N
                  for k in range(N)]
        for j in range(N):
            check(f'N{N} original interpolation node {j}',
                  poly_eval(coeffs,r**j)-one/P[j])
        check(f'N{N} forced top coefficient',coeffs[-1]-one/(N*N))
        for k in range(N+1):
            left = (r**(-k)-1)*coeffs[k] if k<N else zero
            if k:
                left += coeffs[k-1]-one/(N*N)
            check(f'N{N} original forcing coefficient {k}',left)
        # Check the cardinal formula away from every physical node.
        for X in (cv(sp.Rational(1,2)),cv(2),cv(sp.I/3)):
            cardinal = (1-X**N)/N*sum(
                (one/(P[j]*(1-X*r**(-j))) for j in range(N)),zero)
            check(f'N{N} whole polynomial cardinal identity at {field.to_sympy(X)}',
                  poly_eval(coeffs,X)-cardinal)

    pi = arb.pi()

    def positive(name, value):
        assert value > 0, (name,value)
        margins.append({'name':name,'enclosure':str(value)})

    positive('left sine endpoint above three quarters',
             (pi*arb(59)/125).sin()-arb(3)/4)
    positive('right sine endpoint above three quarters',
             (pi*arb(91)/125).sin()-arb(3)/4)
    positive('lower rectangle radial bound',
             (-pi*arb(29)/125).exp()-arb(12)/25)
    positive('lower rectangle logarithm',
             (arb(37)/25).log()-arb(39)/100)
    positive('lower rectangle action gap',
             arb(117)/(800*pi)-arb(1)/100)
    positive('upper rectangle reflected radial bound',
             (-pi*arb(3)/125).exp()-arb(23)/25)
    positive('upper rectangle reflected logarithm',
             (arb(48)/25).log()-arb(13)/20)
    positive('upper rectangle adjusted action gap',
             arb(39)/(160*pi)-arb(324)*pi/15625-arb(1)/100)
    bottom_rate = -(1-(-2*pi).exp()).log()
    positive('height one bottom rate below one over five hundred',
             arb(1)/500-bottom_rate)
    positive('relative exponent one over two hundred',
             arb(1)/100-bottom_rate-arb(1)/200)
    positive('fixed derivative exponent reserve',
             arb(1)/200-arb(1)/300)

    def phat(N, value):
        return (mp.exp(mp.pi*1j*value/2-mp.pi*1j*value*(value+1)/(2*N))
                *sine_factorial(N,value))

    # These use the finite Barnes product, independently of the midpoint
    # Gamma-modulus derivation in the written proof.
    for N in (5,6):
        for height in ('-.2','0','.2'):
            h = mp.mpf(height)
            for side in ('left','right'):
                vv = (-mp.mpf('.5') if side=='left' else N-mp.mpf('.5'))+1j*N*h
                actual = abs(1/phat(N,vv))**2
                e = mp.exp(2*mp.pi*N*h)
                predicted = (1+e)/N if side=='left' else 1/(N*(1+e))
                err = abs(actual/predicted-1)
                assert err < mp.mpf(10)**(-args.dps+15),(N,height,side,err)
                midpoint.append({'N':N,'height':height,'side':side,
                                 'relative_error':str(err)})

    points = [mp.mpc('.236','-.116'),mp.mpc('.3','-.052'),
              mp.mpc('.364','.012')]
    for N in (16,17,32,33,64,65):
        r = mp.exp(-2j*mp.pi/N)
        P = [mp.mpc(1)]
        for j in range(1,N):
            P.append(P[-1]*(1-r**j))
        for z in points:
            X = mp.exp(-2j*mp.pi*z)
            d = (1-X**N)/N*sum(1/(P[j]*(1-X*r**(-j))) for j in range(N))
            error = abs(d*phat(N,N*z)-1)
            scaled = error*mp.exp(mp.mpf(N)/200)
            # A diagnostic over these displayed cases, not the universal bound.
            assert scaled < 1,(N,z,error)
            diagnostics.append({'N':N,'z':[str(z.real),str(z.imag)],
                                'relative_error':str(error),
                                'error_times_exp_N_over_200':str(scaled)})
    deps = [
        'notes/research_mixed_fourier_weight_continuation.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'notes/research_mixed_three_conditional_complex_neighbors.md',
        'notes/research_mixed_conditional_leg_sum.md',
        'experiments/audit_exact_factorial_interpolation.py',
    ]
    result = {
        'status':'passed','precision_bits':args.precision,'diagnostic_decimal_digits':args.dps,
        'symbolic_identity_count':len(symbolic),'symbolic_identities':symbolic,
        'exact_finite_identity_count':len(exact),'exact_finite_identities':exact,
        'strict_margin_count':len(margins),'strict_margins':margins,
        'midpoint_barnes_check_count':len(midpoint),'midpoint_barnes_checks':midpoint,
        'complex_comparison_count':len(diagnostics),'complex_comparisons':diagnostics,
        'scope':('Exact reciprocal-factorial Fourier polynomial, its retained forcing, '
                 'midpoint contour normalization, and uniform scalar margins on the '
                 'four-crossing critical rectangle. Finite comparisons are diagnostics; '
                 'the full exponential estimate follows from the written residue proof. '
                 'No mixed-word asymptotic or knot-volume conclusion.'),
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in (
        'status','symbolic_identity_count','exact_finite_identity_count',
        'strict_margin_count','midpoint_barnes_check_count','complex_comparison_count')}))


if __name__=='__main__':
    main()
