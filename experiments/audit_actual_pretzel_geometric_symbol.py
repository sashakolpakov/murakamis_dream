#!/usr/bin/env python3
"""Literal factorial symbol and marked pretzel saddles, not a cycle claim."""

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sy


def poch(a, r, Q):
    return mp.fprod(1-a*Q**j for j in range(r))


def literal_ratios(N):
    mp.mp.dps = 75
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    M, w = (N-1)//2, mp.mpf('-2.3')
    F = [mp.mpc(1)]
    for v in range(1, N):
        F.append(F[-1]*(1-Q**v))
    def term(v, r):
        return (F[2*v]/F[v]**4*poch(Q**(-v), r, Q)*Q**r/F[r]**3
                *poch(q*w, r, Q)*poch(q/w, r, Q))
    count = 0
    for v in range(M+1):
        for r in range(v+1):
            value = term(v, r)
            if v < M:
                ratio = ((1-Q**(2*v+1))*(1-Q**(2*v+2))/(1-Q**(v+1))**4
                         *(1-Q**(-v-1))/(1-Q**(r-v-1)))
                assert abs(term(v+1, r)/value-ratio) < mp.mpf('1e-60')*max(1, abs(ratio))
                count += 1
            if r < v:
                ratio = (Q*(1-Q**(r-v))*(1-q*w*Q**r)*(1-q/w*Q**r)
                         /(1-Q**(r+1))**3)
                assert abs(term(v, r+1)/value-ratio) < mp.mpf('1e-60')*max(1, abs(ratio))
                count += 1
    return {'N': N, 'literal_finite_term_ratio_checks': count}


def symbolic_identities():
    X, Y, w, U = sy.symbols('X Y w U')
    vx = (1+X)**2/((X-1)*(X-Y))
    ry = (1-Y/X)*(1-w*Y)*(1-Y/w)/(1-Y)**3
    a = 2*X/(1+X)-X/(X-1)-X/(X-Y)
    b = Y/(X-Y)
    d = -Y/(X-Y)-w*Y/(1-w*Y)-Y/(w-Y)+3*Y/(1-Y)
    e = -w*Y/(1-w*Y)+Y/(w-Y)
    f = -1-w*Y/(1-w*Y)-Y/(w-Y)
    assert sy.factor(X*sy.diff(vx, X)/vx-a) == 0
    assert sy.factor(Y*sy.diff(vx, Y)/vx-b) == 0
    assert sy.factor(Y*sy.diff(ry, Y)/ry-d) == 0
    assert sy.factor(w*sy.diff(ry, w)/ry-e) == 0
    outer = (w*Y-1)/(w-Y)
    assert sy.factor(w*sy.diff(outer, w)/outer-f) == 0
    assert sy.factor(Y*sy.diff(outer, Y)/outer-e) == 0
    assert sy.factor((vx-1).subs(X, (Y-1)/(Y+3))) == 0
    Rpoly = (1+Y)**2*(w*w+1)+w*(-6*Y*Y+4*Y-6)
    assert sy.factor(((ry-1)*(1-Y)**3).subs(X, (Y-1)/(Y+3))
                     -Y*Rpoly/(w*(Y-1))) == 0
    relation = (w+1/w-6)*(1+Y)**2+16*Y
    expected = ((w-1)**2*((1+U)**2*(w*w+1)-2*(U*U-6*U+1)*w)
                /(w*(w+U)**2))
    assert sy.factor(relation.subs(Y, (U*w+1)/(w+U))-expected) == 0
    aa = sy.factor(a.subs(X, (Y-1)/(Y+3)))
    bb = sy.factor(b.subs(X, (Y-1)/(Y+3)))
    dd = sy.factor(d.subs(X, (Y-1)/(Y+3)))
    det3 = sy.factor(aa*(dd*f-e*e)-bb*bb*f)
    formula3 = -Y*(Y-1)*(Y+3)**2*(w*w-6*w+1)/(4*(w-Y)*(Y+1)**2*(Y*w-1))
    assert sy.factor(det3-formula3) == 0
    det2 = sy.factor(aa*dd-bb*bb)
    formula2 = -Y*Y*(Y+3)**2*(w-1)**2/((w-Y)*(Y+1)**3*(Y*w-1))
    numerator, _ = sy.fraction(sy.factor(det2-formula2))
    assert sy.rem(numerator, Rpoly, w) == 0
    return {'exact_finite_symbol_gradients': True,
            'elimination_with_double_collision_factor_w_minus_one': True,
            'complete_log_Hessian_and_inner_minor': True}


def phase(X, Y, w):
    L = lambda z: mp.polylog(2, z)
    return (-6*L(1)-L(X*X)+4*L(X)+L(1/X)-L(Y/X)
            +L(w)+L(1/w)-L(w*Y)-L(Y/w)+3*L(Y))


def gradients(X, Y, w):
    return (2*mp.log(1-X*X)-4*mp.log(1-X)+mp.log(1-1/X)-mp.log(1-Y/X),
            mp.log(1-Y/X)+mp.log(1-w*Y)+mp.log(1-Y/w)-3*mp.log(1-Y),
            -mp.log(1-w)+mp.log(1-1/w)+mp.log(1-w*Y)-mp.log(1-Y/w))


def hessian(X, Y, w):
    a = 2*X/(1+X)-X/(X-1)-X/(X-Y)
    b = Y/(X-Y)
    d = -Y/(X-Y)-w*Y/(1-w*Y)-Y/(w-Y)+3*Y/(1-Y)
    e = -w*Y/(1-w*Y)+Y/(w-Y)
    f = -1-w*Y/(1-w*Y)-Y/(w-Y)
    return mp.matrix([[a, b, 0], [b, d, e], [0, e, f]])


def lobachevsky(theta):
    return mp.im(mp.polylog(2, mp.exp(2j*theta)))/2


def geometric_case(s, m):
    mp.mp.dps = 80
    alpha = mp.pi*m/s
    eta = 2*mp.asinh(mp.tan(alpha))
    tau = 1/mp.cos(alpha)
    X, Y, w = 1j*tau/(2-1j*tau), (1+1j*tau)/(1-1j*tau), -mp.exp(eta)
    gx, gy, gt = gradients(X, Y, w)
    assert abs(gx) < mp.mpf('1e-65')
    assert abs(gy-2j*mp.pi) < mp.mpf('1e-65')
    assert abs(gt-2j*alpha) < mp.mpf('1e-65')
    H = hessian(X, Y, w)
    K = H[:2, :2]
    d3, d2 = mp.det(H), mp.det(K)
    assert abs(d3) > mp.mpf('1e-20') and abs(d2) > mp.mpf('1e-20')
    assert abs(d3/d2-1j*mp.cos(alpha)) < mp.mpf('1e-60')
    action = s*(phase(X, Y, w)-2j*mp.pi*mp.log(Y))-2j*mp.pi*m*mp.log(mp.mpc(w, 0))
    expected = 8*s*(lobachevsky(mp.pi/4+alpha/2)+lobachevsky(mp.pi/4-alpha/2))
    assert abs(mp.im(action)-expected) < mp.mpf('1e-60')
    Xb, Yb, wb = mp.conj(X), mp.conj(Y), 1/w
    gx, gy, gt = gradients(Xb, Yb, wb)
    assert abs(gx) < mp.mpf('1e-65')
    assert abs(gy+2j*mp.pi) < mp.mpf('1e-65')
    assert abs(gt-2j*alpha) < mp.mpf('1e-65')
    backwards = s*(phase(Xb, Yb, wb)+2j*mp.pi*mp.log(Yb))-2j*mp.pi*m*mp.log(mp.mpc(wb, 0))
    assert abs(mp.im(backwards)+expected) < mp.mpf('1e-60')
    if (s, m) in ((3, 1), (5, 1), (9, 2)):
        full = mp.matrix(2*s+1)
        for i in range(s):
            for a in range(2):
                for b in range(2):
                    full[2*i+a, 2*i+b] = H[a, b]
                full[2*i+a, 2*s] = H[a, 2]
                full[2*s, 2*i+a] = H[2, a]
        full[2*s, 2*s] = s*H[2, 2]
        assert abs(mp.det(full)-s*d2**(s-1)*d3) < mp.mpf('1e-55')*max(1, abs(mp.det(full)))
    return {'odd_boxes': s, 'positive_winding': m,
            'principal_inner_marks': [0, 1], 'reciprocal_inner_marks': [0, -1],
            'nonzero_full_saddle_Hessian': True,
            'formal_imaginary_action': str(expected),
            'Lobachevsky_and_both_marked_actions_match': True}


def mixed_case(s, n, m):
    mp.mp.dps = 75
    k, alpha = (s+n)//2, mp.pi*m/n
    eta, tau = 2*mp.asinh(mp.tan(alpha)), 1/mp.cos(alpha)
    X, Y, w = 1j*tau/(2-1j*tau), (1+1j*tau)/(1-1j*tau), -mp.exp(eta)
    Xb, Yb = mp.conj(X), mp.conj(Y)
    plus, minus = gradients(X, Y, w), gradients(Xb, Yb, w)
    assert abs(k*plus[2]+(s-k)*minus[2]-2j*mp.pi*m) < mp.mpf('1e-60')
    action = (k*(phase(X, Y, w)-2j*mp.pi*mp.log(Y))
              +(s-k)*(phase(Xb, Yb, w)+2j*mp.pi*mp.log(Yb))
              -2j*mp.pi*m*mp.log(mp.mpc(w, 0)))
    expected = 8*n*(lobachevsky(mp.pi/4+alpha/2)+lobachevsky(mp.pi/4-alpha/2))
    assert abs(mp.im(action)-expected) < mp.mpf('1e-55')
    pure_alpha = mp.pi*m/s
    pure = 8*s*(lobachevsky(mp.pi/4+pure_alpha/2)+lobachevsky(mp.pi/4-pure_alpha/2))
    assert expected < pure
    Hp, Hm = hessian(X, Y, w), hessian(Xb, Yb, w)
    assert mp.norm(Hm-Hp.conjugate()) < mp.mpf('1e-60')
    dp, dm = mp.det(Hp[:2, :2]), mp.det(Hm[:2, :2])
    if (s, n, m) in ((5, 3, 1), (7, 3, 1), (9, 5, 1)):
        full = mp.matrix(2*s+1)
        for i in range(s):
            H = Hp if i < k else Hm
            for a in range(2):
                for b in range(2):
                    full[2*i+a, 2*i+b] = H[a, b]
                full[2*i+a, 2*s] = H[a, 2]
                full[2*s, 2*i+a] = H[2, a]
            full[2*s, 2*s] += H[2, 2]
        target = dp**k*dm**(s-k)*n*1j*mp.cos(alpha)
        assert abs(mp.det(full)-target) < mp.mpf('1e-50')*max(1, abs(target))
    return {'source_boxes': s, 'effective_odd_width': n, 'positive_winding': m,
            'number_of_plus_copies': k, 'finite_arrangement_count': math.comb(s, k),
            'formal_mixed_action': str(expected), 'strictly_below_all_plus_action': True,
            'complete_marked_stationarity_and_mixed_Hessian': True}


if __name__ == '__main__':
    finite = [literal_ratios(N) for N in range(3, 21)]
    exact = symbolic_identities()
    cases = [geometric_case(s, m) for s in (3, 5, 7, 9, 11, 15, 21)
             for m in range(1, (s+1)//2)]
    mixed = [mixed_case(s, n, m) for s in (5, 7, 9, 15)
             for n in range(3, s, 2) for m in range(1, (n+1)//2)]
    results = {'status': 'PASS', 'literal_original_factorial_ratios': finite,
               'exact_symbolic_identities': exact, 'all_geometric_windings_tested': cases,
               'mixed_regular_branches_and_strict_interior_gap': mixed,
               'scope': 'Exact finite symbol, marked formal saddles and action only; no original-cycle selection or survival claim.'}
    Path(__file__).with_name('actual_pretzel_geometric_symbol_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print(f'PASS {len(finite)} literal finite levels; exact elimination/Hessian identities; {len(cases)} marked reciprocal saddle pairs; {len(mixed)} mixed branches/interior gaps')
