#!/usr/bin/env python3
"""Audit the original pretzel phase and its marked stationary family.

This verifies local algebra/action, not the intersection of the original
finite residue cycle with a stationary cycle.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def phase(X, Y, w):
    L = lambda z: mp.polylog(2, z)
    return (-6*L(1)-L(X*X)+4*L(X)+L(1/X)-L(Y/X)
            +L(w)+L(1/w)-L(w*Y)-L(Y/w)+3*L(Y))


def gradient(X, Y, w):
    log = mp.log
    return mp.matrix([
        2*log(1-X*X)-4*log(1-X)+log(1-1/X)-log(1-Y/X),
        log(1-Y/X)+log(1-w*Y)+log(1-Y/w)-3*log(1-Y),
        -log(1-w)+log(1-1/w)+log(1-w*Y)-log(1-Y/w),
    ])


def hessian(X, Y, w):
    xx = 2*X/(1+X)-X/(X-1)-X/(X-Y)
    xy = Y/(X-Y)
    yy = -Y/(X-Y)-w*Y/(1-w*Y)-Y/(w-Y)+3*Y/(1-Y)
    yw = -w*Y/(1-w*Y)+Y/(w-Y)
    ww = -1-w*Y/(1-w*Y)-Y/(w-Y)
    return mp.matrix([[xx, xy, 0], [xy, yy, yw], [0, yw, ww]])


def algebraic_elimination():
    X, Y, w, U = sp.symbols('X Y w U')
    vx = (1+X)**2-(X-1)*(X-Y)
    assert sp.factor(vx.subs(X, (Y-1)/(Y+3))) == 0
    yr = (1-Y/X)*(1-w*Y)*(1-Y/w)-(1-Y)**3
    # After the X equation the remaining relation is the displayed
    # quadratic relation between w+w^-1 and Y.
    numerator = sp.factor(yr.subs(X, (Y-1)/(Y+3)))
    relation = w+1/w-6+16*Y/(Y+1)**2
    quotient = sp.factor(numerator/relation)
    assert not quotient.has(w)
    pol = sp.factor((relation.subs(Y, (U*w+1)/(w+U))
                     *w*(U+1)**2*(w+1)**2))
    expected = ((w-1)**2*((U+1)**2*w*w
                         -2*(U*U-6*U+1)*w+(U+1)**2))
    assert sp.factor(pol-expected) == 0
    return {'two_inner_equations_and_complete_outer_factorization': True,
            'excluded_degenerate_factor': '(w-1)^2'}


def stationary_case(s, m):
    alpha = mp.pi*m/s
    eta = 2*mp.asinh(mp.tan(alpha))
    beta = mp.atan(1/mp.cos(alpha))
    w = -mp.exp(eta)
    Y = mp.exp(2j*beta)
    X = (Y-1)/(Y+3)
    assert 0 < mp.arg(Y) < mp.arg(X) < mp.pi
    assert abs(X) < 1 and abs(abs(Y)-1) < mp.mpf('1e-70')
    g = gradient(X, Y, w)
    target = mp.matrix([0, 2j*mp.pi, 2j*alpha])
    assert mp.norm(g-target) < mp.mpf('1e-65')
    assert abs((w*Y-1)/(w-Y)-mp.exp(2j*alpha)) < mp.mpf('1e-65')
    H = hessian(X, Y, w)
    H2 = H[:2, :2]
    det3 = (-Y*(Y-1)*(Y+3)**2*(w*w-6*w+1)
            /(4*(w-Y)*(Y+1)**2*(Y*w-1)))
    det2 = (-Y*Y*(Y+3)**2*(w-1)**2
            /((w-Y)*(Y+1)**3*(Y*w-1)))
    assert abs(mp.det(H)-det3) < mp.mpf('1e-63')*max(1, abs(det3))
    assert abs(mp.det(H2)-det2) < mp.mpf('1e-63')*max(1, abs(det2))
    schur = H[2, 2]-(H[2:3, :2]*(H2**-1)*H[:2, 2:3])[0]
    assert abs(schur-1j*mp.cos(alpha)) < mp.mpf('1e-63')
    for k in range(3):
        def vary(t):
            args = [X, Y, w]
            args[k] *= mp.exp(t)
            return phase(*args)
        assert abs(mp.diff(vary, 0)-g[k]) < mp.mpf('1e-60')
    marked = s*(phase(X, Y, w)-2j*mp.pi*mp.log(Y))-2j*mp.pi*m*mp.log(w)
    lob = lambda t: mp.im(mp.polylog(2, mp.exp(2j*t)))/2
    action = 8*s*(lob(mp.pi/4+alpha/2)+lob(mp.pi/4-alpha/2))
    assert abs(mp.im(marked)-action) < mp.mpf('1e-62')
    return {'s': s, 'winding': m, 'inner_Y_mark': 1,
            'nondegenerate_full_Hessian': True,
            'exact_action_identity_checked': True,
            'candidate_action': mp.nstr(action, 25),
            'radius': mp.nstr(abs(w), 25)}


def literal_phase_case(N):
    q = mp.exp(mp.pi*1j/N)
    Q = q*q
    v, r = (37*N)//100, (21*N)//100
    w = -mp.exp(mp.mpf('1.3'))
    fac = [mp.mpc(1)]
    for a in range(1, 2*v+1):
        fac.append(fac[-1]*(1-Q**a))
    poch = lambda a, n: mp.fprod(1-a*Q**k for k in range(n))
    term = (fac[2*v]/fac[v]**4*poch(Q**(-v), r)*poch(q*w, r)
            *poch(q/w, r)*Q**r/fac[r]**3)
    X, Y = Q**v, Q**r
    residual = mp.log(abs(term))-N*mp.im(phase(X, Y, w))/(2*mp.pi)
    # Finite diagnostic of the correctly calibrated leading modulus,
    # not a claim that these samples prove its uniform expansion.
    assert abs(residual) < 8*mp.log(N)
    return {'N': N, 'literal_v': v, 'literal_r': r,
            'log_modulus_residual': mp.nstr(residual, 16),
            'scope': 'finite interior calibration diagnostic'}


if __name__ == '__main__':
    mp.mp.dps = 85
    cases = [stationary_case(s, m) for s in (3, 5, 7, 9, 15)
             for m in range(1, (s+1)//2)]
    result = {'status': 'PASS', 'algebra': algebraic_elimination(),
              'positive_stationary_family': cases,
              'literal_phase_calibration': [literal_phase_case(N) for N in (64, 128, 256)],
              'scope': 'Exact phase/action/Hessian checks; selected-cycle survival remains unproved.'}
    Path(__file__).with_name('actual_pretzel_winding_phase_and_geometric_saddles_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS complete algebraic elimination; {len(cases)} marked stationary/Hessian/action cases; '
          '3 literal coefficient phase diagnostics. No global-cycle claim.')
