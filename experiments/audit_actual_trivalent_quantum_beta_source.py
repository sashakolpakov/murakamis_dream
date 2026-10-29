#!/usr/bin/env python3
"""Original trivalent coefficient, norm-corrected cycle, and Barnes remainder.

The numerical integrations are independent checks of the exact rectangle
proof; none supplies the uniform bound or global source selection.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_modular_dilog_circle import log_psi_inside


def B(N, u, v):
    Q = mp.exp(2j*mp.pi/N)
    p = mp.mpc(1)
    total = p
    for k in range(N-1):
        p *= u-Q**k*v
        total += p
    return total


def log_selected_psi(N, z):
    assert 0 < mp.im(z) < 2*mp.pi
    if mp.re(z) < 0:
        return log_psi_inside(N, 1, z)
    cb = .5j*(mp.sqrt(N)+1/mp.sqrt(N))
    lzeta = -mp.pi*1j*(1+2*cb*cb)/6
    return (lzeta+mp.pi*1j*(mp.sqrt(N)*z/(2*mp.pi)-cb)**2
            +log_psi_inside(N, -1, -z))


def exact_polynomial_checks():
    u, v = sp.symbols('u v')
    rows = []
    for N in range(2, 10):
        # The recurrence telescopes algebraically before root evaluation.
        q = sp.symbols('q', nonzero=True)
        p = [sp.Integer(1)]
        for k in range(N):
            p.append(sp.expand(p[-1]*(u-q**k*v)))
        assert sp.expand(sum(q**k*p[k] for k in range(N))*v
                         -(u-1)*sum(p[:N])-1+p[N]) == 0
        rows.append({'N': N, 'simultaneous_boundary_shift_telescoping': True})
    a, t, D, un, vn, gg = sp.symbols('a t D un vn g', nonzero=True)
    lam = un-vn*t
    den = (t-1)*(1-lam)
    # Convert residues from t to a using dt/da=2*pi*i*t.
    integer_res = sp.cancel(D*t/((1-lam)*t)).subs(t, 1).subs(D, 1-un+vn)
    assert sp.cancel(integer_res-1) == 0
    tstar = (un-1)/vn
    norm_res = sp.cancel(D*t/((t-1)*vn*t)).subs(t, tstar).subs(D, 1-un+vn)
    assert sp.cancel(norm_res+1) == 0
    # Exact right/left edge difference; H=t/(1-t).
    edge = sp.cancel((lam-1)*D*t/den-D*t/(1-t))
    assert edge == 0
    r, U, V = sp.symbols('r U V', nonzero=True)
    M = (r-V)*(r-1)/(r*(r-U))
    assert sp.factor(M-1+((1+V-U)*r-V)/(r*(r-U))) == 0
    # Genuine positive signed bipyramid inside the bounded-source chamber.
    ui = -4*sp.I/5
    vi = sp.Rational(1, 100)
    pp = 1+vi-ui
    qq = pp/vi
    HH = ui*qq
    assert sp.simplify(pp+qq-pp*qq-HH) == 0
    assert sp.simplify(pp/HH-sp.I/80) == 0
    assert sp.simplify(qq/HH-5*sp.I/4) == 0
    assert sp.im(pp)>0 and sp.im(qq)>0 and sp.im(HH)<0
    assert abs(ui)+abs(vi) == sp.Rational(81, 100)
    # The first Barnes symbol solves its actual inhomogeneous Ward equation.
    I0 = 1/(1-u+v)
    I1 = -v*(u-v)/(1-u+v)**3
    assert sp.factor(I0-(u-v)*I0-1) == 0
    assert sp.factor(I1-(u-v)*(I1+v*sp.diff(I0, v))) == 0
    return {'eight_boundary_recurrences': rows,
            'integer_residue': True, 'balanced_norm_residue': True,
            'variable_norm_edge_identity': True, 'Frobenius_support_polynomial': True,
            'exact_positive_bipyramid_with_bounded_source': True,
            'two_inhomogeneous_Barnes_symbol_orders': True}


def coefficient_convolution(N, U, V):
    Q = mp.exp(2j*mp.pi/N)
    p = [mp.mpc(1)]
    m = [mp.mpc(1)]
    for k in range(1, N):
        p.append(p[-1]*(-Q**(k-1))/(1-Q**k))
        m.append(m[-1]*Q/(1-Q**k))
    actual = sum(m[b]*p[k]*p[N-1-b-k]*U**b*V**k
                 for b in range(N) for k in range(N-b))
    target = Q**(-(N-1))/N*B(N, Q**2*U, Q*V)
    assert abs(actual-target) < mp.mpf('1e-36')
    return {'N': N, 'full_Psi_coefficient_convolution_error': float(abs(actual-target))}


def balanced_residue(N, u, x):
    h = 2j*mp.pi/N
    v = u*x
    c = mp.log(x)
    lu = mp.log(u)
    tstar = (u**N-1)/v**N
    alpha = mp.log(tstar)/(2j*mp.pi)
    # Select -epsilon<Re alpha<1-epsilon; S is invariant under this change.
    eps = mp.mpf('.13')
    while mp.re(alpha) <= -eps:
        alpha += 1
    while mp.re(alpha) >= 1-eps:
        alpha -= 1
    cstar = c+h*alpha
    ga = mp.exp(alpha*lu+log_selected_psi(N, c)-log_selected_psi(N, cstar))
    vstar = v*mp.exp(h*alpha)
    assert abs(u**N-vstar**N-1) < mp.mpf('1e-35')
    block = ga*B(N, u, vstar)
    constant = block*mp.exp(c*lu/h-log_selected_psi(N, c))
    return block, constant


def barnes_identity(N, u, x):
    h = 2j*mp.pi/N
    v = u*x
    c = mp.log(x)
    lu = mp.log(u)
    eps = mp.mpf('.13')
    lp0 = log_selected_psi(N, c)

    def integrand(y):
        a = -eps+1j*y
        if y >= 0:
            lh = 2j*mp.pi*a-mp.log(1-mp.exp(2j*mp.pi*a))
        else:
            lh = -mp.log(mp.exp(-2j*mp.pi*a)-1)
        return 1j*mp.exp(a*lu+lp0-log_selected_psi(N, c+h*a)+lh)

    integral = mp.quad(integrand, [-55, -16, -5, -1, 0, 1, 5, 16, 55])
    block, constant = balanced_residue(N, u, x)
    D = 1-u**N+v**N
    error = abs(B(N, u, v)-block-D*integral)
    assert error < mp.mpf('1e-20'), error
    # A second, distinct boundary x must give exactly the same A_N(u).
    _, constant2 = balanced_residue(N, u, mp.mpc('.6', '.8'))
    separation_error = abs(constant2/constant-1)
    assert separation_error < mp.mpf('1e-34'), separation_error
    return {'N': N, 'u': str(u), 'x': str(x),
            'Barnes_integral': str(integral), 'retained_norm_factor': str(D),
            'exact_source_cycle_error': float(error),
            'boundary_section_separation_error': float(separation_error),
            'nonzero_balanced_residue_block': str(block)}


def exact_normalizer(N, u):
    h = 2j*mp.pi/N
    x = mp.mpc('.3', '.7')
    _, actual = balanced_residue(N, u, x)
    phi = mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
    target = N/phi*u**N*mp.exp(log_selected_psi(N, h-mp.log(u)))
    error = abs(actual/target-1)
    assert error < mp.mpf('1e-33'), error
    return {'N': N, 'u': str(u), 'exact_central_normalizer_relative_error': float(error),
            'retained_central_factor': 'u^N'}


def main():
    mp.mp.dps = 45
    result = {'status': 'PASS', 'symbolic': exact_polynomial_checks(),
              'original_convolutions': [coefficient_convolution(N, mp.mpc('-.3', '-.8'),
                                                               mp.mpc('.8', '.1'))
                                        for N in range(2, 12)],
              'exact_Barnes_source_cycles': [barnes_identity(N, mp.mpc('.3', '-.9'),
                                                            mp.mpc('.3', '.7'))
                                             for N in [3, 5]],
              'exact_full_Psi_central_normalizers': [exact_normalizer(N, u)
                  for N in [2, 3, 5, 9]
                  for u in [mp.mpc('.7', '-.4'), mp.mpc('0', '-.8'), mp.mpc('1.1', '-.4')]],
              'positive_bipyramid_contraction_obstruction': {
                  'u': '-4i/5', 'v': '1/100',
                  'exact_product_bound': '(|u|+|v|)^a=(81/100)^a',
                  'uniform_original_source_bound': '100/19',
                  'nonzero_limit': '1/(1+4i/5+1/100)',
                  'three_shapes': ['101/100+4i/5', '101+80i', '64-404i/5'],
                  'two_positive_outputs': ['i/80', '5i/4']},
              'scope': ('Original finite trivalent convolution; exact norm-pole residue plus '
                        'uniformly tame Barnes remainder. No automatic global geometric selection.')}
    Path(__file__).with_name('actual_trivalent_quantum_beta_source_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS eight symbolic boundary recurrences, norm-pole residues, ten original '
          'convolutions, two exact Barnes source cycles, twelve exact full-Psi '
          'normalizers and boundary separation checks')


if __name__ == '__main__':
    main()
