#!/usr/bin/env python3
"""Actual five-crossing Newton source, two-sided transfer and certified barrier."""

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from flint import arb, acb, ctx


def gaussian_rows(q, nmax):
    rows = [[q*0+1]]
    for n in range(1, nmax+1):
        prev = rows[-1]
        row = []
        for j in range(n+1):
            value = (prev[j] if j < n else 0)+(q**(n-j)*prev[j-1] if j else 0)
            row.append(value)
        rows.append(row)
    return rows


def generic_recurrence():
    t = sp.Symbol('t')
    B = gaussian_rows(t, 8)
    J = [sp.expand(sum(t**(j*(j+1))*c for j, c in enumerate(row))) for row in B]
    for n in range(2, 9):
        assert sp.expand(J[n]-(1+t-t**n+t**(2*n))*J[n-1]+t*(1-t**(n-1))*J[n-2]) == 0
    return {'all_generic_polynomial_indices': list(range(9)),
            'monic_second_order_recurrence_exact': True}


def actual_root_coefficients():
    rows = []
    for N in range(2, 41):
        Q = mp.exp(2j*mp.pi/N)
        t = 1/Q
        Bq, Bt = gaussian_rows(Q, N-1), gaussian_rows(t, N-1)
        direct = [mp.fsum(t**(j*(j+1))*c for j, c in enumerate(row)) for row in Bt]
        recursive = [mp.mpc(1)]
        if N > 1:
            recursive.append(1+t*t)
        for n in range(2, N):
            recursive.append((1+t-t**n+t**(2*n))*recursive[-1]
                             -t*(1-t**(n-1))*recursive[-2])
        worst = mp.mpf(0)
        for n in range(N):
            source = (-1)**n*Q**(-mp.mpf(n*(n+3))/2)*mp.fsum(
                c*Q**(-j*(n+1)) for j, c in enumerate(Bq[n]))
            transformed = (-1)**n*t**(mp.mpf(n*(n+3))/2)*recursive[n]
            scale = max(1, abs(source), abs(transformed))
            worst = max(worst, abs(source-transformed)/scale,
                        abs(direct[n]-recursive[n])/max(1, abs(direct[n])))
        assert worst < mp.mpf('1e-65')
        gauss = mp.fsum((-1)**j*t**(mp.mpf(j*(j+1))/2) for j in range(N))
        assert abs(gauss-direct[-1]) < mp.mpf('1e-65')
        assert abs(direct[-1]) <= N+mp.mpf('1e-60')
        assert abs(direct[-2]) <= mp.mpf(N*N)/2+mp.mpf('1e-60')
        # Exact determinant products appearing in backward transport.
        for n in (1, max(1, N//2), N-1):
            product = mp.fprod(abs(t*(1-t**(ell-1))) for ell in range(n+1, N))
            rhs = mp.fprod(abs(1-t**r) for r in range(n, N-1))
            assert abs(product-rhs) < mp.mpf('1e-65')*max(1, rhs)
        rows.append({'N': N, 'all_original_Newton_coefficients_checked': N,
                     'max_relative_identity_error': float(worst),
                     'terminal_Gauss_abs': float(abs(direct[-1])),
                     'penultimate_abs': float(abs(direct[-2]))})
    return rows


def dominated_initial_branch():
    rows = []
    lower = math.log(1.5)/32
    for N in (64, 128, 256, 512, 1024, 2048):
        t = mp.exp(-2j*mp.pi/N)
        nmax = N//32
        old, now = mp.mpc(1), 1+t*t
        if nmax == 0:
            value = old
        elif nmax == 1:
            value = now
        else:
            for n in range(2, nmax+1):
                old, now = now, (1+t-t**n+t**(2*n))*now-t*(1-t**(n-1))*old
            value = now
        rate = float(mp.log(abs(value))/N)
        assert rate >= lower-2/N
        # Uniform limiting gap on the certified interval, independently sampled.
        min_plus, max_minus = 10., 0.
        for n in range(65):
            z = mp.exp(-2j*mp.pi*n/(64*32))
            D = z*mp.sqrt(z*z-2*z+5)
            lp, lm = (2-z+z*z+D)/2, (2-z+z*z-D)/2
            min_plus = min(min_plus, float(abs(lp)))
            max_minus = max(max_minus, float(abs(lm)))
        assert min_plus >= 1.5 and max_minus <= 2/15
        rows.append({'N': N, 'actual_index': nmax,
                     'actual_coefficient_log_rate': rate,
                     'proved_liminf_lower_bound': lower,
                     'sampled_min_dominant_root': min_plus,
                     'sampled_max_other_root': max_minus})
    return rows


def sturm_and_barrier_certificate():
    v, z = sp.symbols('v z')
    A, B = 2-z+z*z, 1-z
    normA = 4-5*v+2*v*v
    mixed = v*(v**3-5*v**2+9*v-4)
    # Derive the unit-circle reduction rather than insert the polynomial alone.
    numerator = sp.together((1-1/z)*A*A+(1-z)*A.subs(z, 1/z)**2).as_numer_denom()
    relation = z*z-(2-v)*z+1
    rem_num = sp.rem(numerator[0], relation, z)
    rem_den = sp.rem(numerator[1], relation, z)
    reduced = sp.rem(sp.expand(rem_num*sp.invert(rem_den, relation, z)), relation, z)
    assert sp.expand(reduced-mixed) == 0
    P = sp.expand((v**5-1)**2-v*((v**6+v)*normA-v**3*mixed))
    expected = v**10-2*v**9+6*v**8-9*v**7+9*v**6-6*v**5-2*v**4+5*v**3-4*v*v+1
    assert sp.expand(P-expected) == 0
    seq = sp.sturm(P, v)
    def variation(at):
        signs = [int(sp.sign(p.subs(v, at))) for p in seq]
        nonzero = [s for s in signs if s]
        return sum(a != b for a, b in zip(nonzero, nonzero[1:])), signs
    assert variation(sp.Integer(1))[0] == 4
    assert variation(sp.Integer(4))[0] == 3
    lo, hi = sp.Rational(57, 50), sp.Rational(29, 25)
    assert variation(lo)[0] == 4 and variation(hi)[0] == 3
    lo, hi = sp.refine_root(P, lo, hi, eps=sp.Rational(1, 10**35))
    ctx.prec = 180
    def as_arb(q):
        return arb(int(q.p))/int(q.q)
    vv = as_arb(lo).union(as_arb(hi))
    u = (vv.sqrt()/2).asin()/arb.pi()
    # At this maximizer cos(2pi u)>2/5. The equal-modulus-root
    # polynomial 4c^3-6c^2+5c-1 is increasing and positive there.
    assert 1-vv/2 > arb(2)/5
    H = arb(0)
    cells = 4096
    for i in range(cells):
        xx = (u*i/cells).union(u*(i+1)/cells)
        zz = acb(0, -2*arb.pi()*xx).exp()
        lp = (2-zz+zz*zz+zz*(zz*zz-2*zz+5).sqrt())/2
        H += abs(lp).log()*u/cells
    J = -acb(0, 2*arb.pi()*u).exp().polylog(2).imag/(2*arb.pi())
    barrier = H-3*J
    assert barrier > arb('0.5775')
    assert barrier < arb('0.5780')
    return {'Schur_polynomial': str(P),
            'Sturm_variations_at_1_and_4': [variation(sp.Integer(1))[0], variation(sp.Integer(4))[0]],
            'isolated_v_root_lower': str(lo), 'isolated_v_root_upper': str(hi),
            'unique_maximizer_u_ball': str(u), 'positive_branch_integral_ball': str(H),
            'log_sine_primitive_ball': str(J), 'certified_two_boundary_barrier_ball': str(barrier),
            'interval_Riemann_cells': cells,
            'rigorous_coarse_interval': ['0.5775', '0.5780']}


def coupled_source_diagnostics():
    rows = []
    for N in (64, 128, 256, 512):
        t = mp.exp(-2j*mp.pi/N)
        J = [mp.mpc(1), 1+t*t]
        for n in range(2, N):
            J.append((1+t-t**n+t**(2*n))*J[-1]-t*(1-t**(n-1))*J[-2])
        logF = mp.mpf(0)
        absolute_envelope, source = -mp.inf, mp.mpc(0)
        for n in range(N):
            if n:
                logF += mp.log(2*mp.sin(mp.pi*n/N))
            Cn = (-1)**n*t**(mp.mpf(n*(n+3))/2)*J[n]
            term = Cn*mp.exp(2*logF)
            source += term
            absolute_envelope = max(absolute_envelope, mp.log(abs(term))/N)
        assert absolute_envelope <= mp.mpf('.5780')+10*mp.log(N)/N
        rows.append({'N': N, 'actual_complete_source_log_rate': float(mp.log(abs(source))/N),
                     'absolute_Newton_term_envelope_log_rate': float(absolute_envelope),
                     'coefficient_max_log_rate': float(max(mp.log(abs(j))/N for j in J)),
                     'scope': 'Diagnostic finite rates; no limit inferred from these samples.'})
    z, L = sp.symbols('z L')
    coupled = sp.factor((L*L-(2-z+z*z)*L+1-z).subs(L, 1/(1-z)**2)*(1-z)**4)
    assert coupled == -z*z*(z**3-4*z*z+7*z-5)
    assert sp.discriminant(z**3-4*z*z+7*z-5, z) == -23
    return {'finite_original_source_rates': rows,
            'exact_joint_cubic': str(coupled), 'cubic_discriminant': -23}


def main():
    mp.mp.dps = 170
    data = {'status': 'PASS', 'generic_coefficient_recurrence': generic_recurrence(),
            'all_index_original_root_Newton_coefficients': actual_root_coefficients(),
            'dominated_initial_branch': dominated_initial_branch(),
            'rigorous_two_boundary_barrier': sturm_and_barrier_certificate(),
            'coupled_complete_source_and_geometry': coupled_source_diagnostics(),
            'scope': ('Actual two-channel five-crossing source and general two-boundary '
                      'transfer estimate; barrier is above selected volume, no new knot class.')}
    Path(__file__).with_name('actual_multichannel_newton_green_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS generic and all-root Newton recurrences, terminal pointing, '
          'initial coefficient growth, rigorous two-boundary barrier and coupled cubic')


if __name__ == '__main__':
    main()
