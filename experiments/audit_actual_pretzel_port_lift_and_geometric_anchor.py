#!/usr/bin/env python3
"""Literal turned ports, reverse cap traversal, and all geometric face maps."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_port_certificate():
    w, U = sp.symbols('w U', nonzero=True)
    k = (w-1)**2/(w+1)**2
    g = lambda z: sp.Matrix([[-2*w/(w+1), z], [-k/z, -2/(w+1)]])
    h = lambda z: g(-w*z)
    A = sp.diag(w, 1/w)
    zero = lambda matrix: all(sp.factor(v) == 0 for v in matrix)
    assert zero(h(1)*g(1)-A)
    a, b = h(U), h(1).inv()
    P = b*a
    assert zero(P-g(1)*g(U).inv())
    Y = (U*w+1)/(w+U)
    J0, C0 = sp.eye(2)-Y*P, Y*sp.eye(2)-P
    Delta = 1-Y*sp.trace(P)+Y*Y
    assert sp.factor(J0.det()-Delta) == 0
    assert sp.factor(C0.det()-Delta) == 0
    assert zero(J0*a-g(1)*J0)
    assert zero(J0*C0+Delta*P)
    assert zero(C0.inv()*b*C0-g(U).inv())
    assert zero(C0.inv()*b*a*b.inv()*C0-g(1))
    return {'exact_four_turned_ports': True, 'actual_disk_product': True,
            'centralizer_and_both_half_Hurwitz_outputs': True}


def gmatrix(w, z):
    k = (w-1)**2/(w+1)**2
    return mp.matrix([[-2*w/(w+1), z], [-k/z, -2/(w+1)]])


def error(A, B):
    return max(abs(A[i, j]-B[i, j]) for i in range(2) for j in range(2))


def act(A, z):
    return (A[0, 0]*z+A[0, 1])/(A[1, 0]*z+A[1, 1])


def physical_cap_case(s):
    mp.mp.dps = 75
    w = mp.mpc('-6.3', '.19')
    chars = [mp.exp(mp.mpc('.025')*(j-(s-1)/2)+1j*(mp.mpf('.11')+mp.mpf('.013')*j))
             for j in range(s-1)]
    chars.append(1/mp.fprod(chars))
    incoming = [None]*s
    incoming[-1] = mp.mpc('1.2', '.07')
    # Product R(B1)...R(Bs) applies the rightmost physical box first.
    for b in range(s-1, 0, -1):
        incoming[b-1] = chars[b]*incoming[b]
    outgoing = [chars[b]*incoming[b] for b in range(s)]
    assert abs(outgoing[0]-incoming[-1]) < mp.mpf('1e-65')
    bottom, top = [], []
    for a, b in zip(incoming, outgoing):
        bottom.append((gmatrix(w, -w*b), gmatrix(w, -w*a)**-1))
        top.append((gmatrix(w, b)**-1, gmatrix(w, a)))
    for b in range(s):
        nxt = (b+1) % s
        assert error(bottom[b][1]*bottom[nxt][0], mp.eye(2)) < mp.mpf('1e-60')
        assert error(top[b][1]*top[nxt][0], mp.eye(2)) < mp.mpf('1e-60')
    return {'s': s, 'every_original_top_and_bottom_cap_matches': True,
            'reverse_operator_traversal_used': True}


def geometric_case(s):
    mp.mp.dps = 85
    alpha = mp.pi/s
    c, r = mp.cos(alpha), 1/mp.sin(alpha)
    rho = mp.sqrt(1/mp.tan(mp.pi/4-alpha/2))
    U, w = mp.exp(2j*alpha), -rho**4
    W = 1/(rho*mp.sin(alpha))
    z = lambda i: r/rho*mp.exp((2*i-1)*1j*alpha)
    upper = lambda i: mp.exp((2*i+1)*1j*alpha)/rho
    lower = lambda i: rho**3*mp.exp((2*i+1)*1j*alpha)
    circle = lambda i: rho*U**i
    reflect_white = lambda v: rho**-2/mp.conj(v)
    A = mp.matrix([[w, 0], [0, 1/w]])
    Y = (U*w+1)/(w+U)
    tol = mp.mpf('1e-65')
    for i in range(s):
        gi, go = gmatrix(w, z(i)), gmatrix(w, z(i+1))
        hi, ho = gmatrix(w, -w*z(i)), gmatrix(w, -w*z(i+1))
        P = gi*go**-1
        assert abs(mp.det(P)-1) < tol and abs(P[0, 0]+P[1, 1]+2) < tol
        assert abs(act(P, circle(i))-circle(i)) < tol
        J = (mp.eye(2)-Y*P)/(1+Y)
        C = (Y*mp.eye(2)-P)/(1+Y)
        assert error(J*C, -P) < tol
        assert error(J*ho, gi*J) < tol
        center = rho/mp.cos(alpha)*mp.exp((2*i+1)*1j*alpha)
        white = mp.matrix([[-rho**2, center/rho**2], [-mp.conj(center), rho**-2]])/mp.tan(alpha)
        assert error(white, go) < tol
        gp, gm = J*go, ho*J**-1
        assert error(gm, J**-1*gi) < tol
        target_minus = [reflect_white(v) for v in (circle(i), lower(i), lower(i-1))]
        source_plus = [circle(i), upper(i-1), upper(i)]
        target_plus = [reflect_white(v) for v in (circle(i), upper(i-1), upper(i))]
        source_minus = [circle(i), lower(i), lower(i-1)]
        for f, points, destinations in ((gp, target_minus, source_plus), (gm, target_plus, source_minus)):
            for point, destination in zip(points, destinations):
                assert abs(act(f, point)-destination) < tol
        # Absolute primitive meridian/longitude translations, not only ratio.
        rotate = mp.matrix([[U**(-mp.mpf(i)/2), 0], [0, U**(mp.mpf(i)/2)]])
        m = mp.matrix([[0, 1], [1, -rho]])*rotate
        Pc, Cc = m*P*m**-1, m*C*m**-1
        assert abs(Pc[1, 0]) < tol and abs(Cc[1, 0]) < tol
        assert abs(Pc[0, 1]/Pc[1, 1]-2j*c*W) < tol
        assert abs(Cc[0, 1]/Cc[1, 1]-(1+1j*c)*W) < tol
        # The actual reverse traversal is an orientation-preserving
        # dihedral isometry, including the retained half-twist gluing.
        F = lambda point: rho*rho/point
        assert abs(F(circle(i))-circle(-i)) < tol
        assert abs(F(upper(i))-lower(-i-1)) < tol
        assert abs(F(lower(i))-upper(-i-1)) < tol
        # Tp_i -> Tm_i swaps its outer labels; after F this is precisely
        # the inverse pairing at disk -i, with the same copy exchange.
        original_plus = (circle(i), upper(i-1), upper(i))
        original_minus = (circle(i), lower(i), lower(i-1))
        reversed_minus = (circle(-i), lower(-i), lower(-i-1))
        reversed_plus = (circle(-i), upper(-i-1), upper(-i))
        for source, target in zip(original_plus, reversed_minus):
            assert abs(F(source)-target) < tol
        for source, target in zip(original_minus, reversed_plus):
            assert abs(F(source)-target) < tol
    assert error(-A, mp.matrix([[rho**4, 0], [0, rho**-4]])) < tol
    return {'s': s, 'white_face_holonomies': s+2,
            'both_shaded_maps_all_three_vertices': 2*s,
            'absolute_auxiliary_meridian_and_disk_longitude': s,
            'oriented_reverse_traversal_preserves_half_twist_pairings': True,
            'oriented_complete_geometric_anchor': True}


def filled_local_case(p, mark):
    mp.mp.dps = 90
    logH = mp.mpc('.021', '.013')
    H = mp.exp(logH)
    L = mp.exp((2j*mp.pi*mark-logH)/(2*p))
    X = (H-L)/(1-H*L)
    Y = (L*L-H)/(L*(H-1))
    Z = (1+Y*Y-(1-Y)**3/(1-Y/X))/Y
    w1 = (Z+mp.sqrt(Z*Z-4))/2
    w = w1 if abs(w1) > 1 else 1/w1
    U = (w*Y-1)/(w-Y)
    z = mp.mpc('1.1', '.08')
    a, b = gmatrix(w, -w*U*z), gmatrix(w, -w*z)**-1
    P = b*a
    beta = -(H-X)*(1-H*X)/(mp.sqrt(H)*(H+1)*(1-X*X))
    C = beta*(P-Y*mp.eye(2))
    assert error(C*P**p, (-1)**(p-mark)*mp.eye(2)) < mp.mpf('1e-65')
    actual = (C**-1*b*C, C**-1*b*a*b**-1*C)
    first, second = a, b
    power = 2*p+1
    for _ in range(abs(power)):
        first, second = ((second, second*first*second**-1) if power > 0
                         else (first**-1*second*first, first))
    assert error(first, actual[0]) < mp.mpf('1e-55')
    assert error(second, actual[1]) < mp.mpf('1e-55')
    return {'p': p, 'unit_mark': mark,
            'SL_spin_and_literal_signed_odd_Hurwitz_power': True}


if __name__ == '__main__':
    symbolic = symbolic_port_certificate()
    caps = [physical_cap_case(s) for s in (3, 5, 7, 9, 25, 51)]
    faces = [geometric_case(s) for s in (3, 5, 7, 9, 25, 27, 51)]
    fillings = [filled_local_case(p, mark) for p in (-11, -7, -3, 3, 7, 11) for mark in (-1, 1)]
    Path(__file__).with_name('actual_pretzel_port_lift_and_geometric_anchor_results.json').write_text(
        json.dumps({'status': 'PASS', 'symbolic_all_port_certificate': symbolic,
                    'literal_reverse_cap_closure': caps,
                    'complete_white_and_both_shaded_face_maps': faces,
                    'actual_signed_filling_relations': fillings,
                    'scope': 'Regular actual diagram lift and complete geometric anchor; no automatic faithfulness or volume equality for deformed fillings.'}, indent=2)+'\n')
    print('PASS exact all-port matrix certificate; 6 literal reverse-cap families; 7 complete white/both-shaded geometric face families; 12 signed filling-spin/Hurwitz cases')
