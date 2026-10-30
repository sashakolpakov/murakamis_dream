#!/usr/bin/env python3
"""Focused source characters, six-force inputs and absolute volume anchor.

The Morse region compiler is shared with the independent full-source
coefficient audit.  This audit does not claim a new original-cycle result.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp

from audit_actual_original_marked_face_coefficient import morse_faces
from audit_actual_q_hahn_negative_clock_boundary import literal_h, matrix, rate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'actual_original_boundary_stationary_character_results.json'))
    args = parser.parse_args()
    mp.mp.dps = 90
    maxima = {}

    def check(name, left, right, tol=mp.mpf('1e-70')):
        error = abs(left-right)/max(1, abs(left), abs(right))
        maxima[name] = max(maxima.get(name, mp.mpf(0)), error)
        assert error < tol, (name, mp.nstr(error, 12))

    mark_count = 0
    cup_pair_count = 0
    for N in range(3, 20):
        d = N-1
        q = mp.exp(mp.pi*1j/N)
        for outside, inside in [(mp.mpf('1.3'), mp.mpf('.7')),
                                (mp.mpc('1.2', '.3'), mp.mpc('.8', '-.1'))]:
            i = mp.mpf(d)/2 + N*(mp.log(outside)-mp.log(inside))/(2j*mp.pi)
            j = d-i
            ordinary = mp.exp(mp.pi*1j*d*i/N)/N
            marked = mp.exp(mp.pi*1j*d*j/N)/(N*N)
            cup = N*mp.exp(-mp.pi*1j*d*j/N)
            check('literal_mark_ratio', marked/ordinary,
                  (inside/outside)**d/N)
            check('cup_scalar', cup/(outside/inside)**(mp.mpf(d)/2),
                  N*mp.exp(-mp.pi*1j*d*d/(2*N)))
            check('cap_scalar', ordinary/(outside/inside)**(mp.mpf(d)/2),
                  mp.exp(mp.pi*1j*d*d/(2*N))/N)
            check('physical_scalar_pair',
                  N*mp.exp(-mp.pi*1j*d*d/(2*N))
                  *mp.exp(mp.pi*1j*d*d/(2*N))/N, 1)
            mark_count += 1
            cup_pair_count += 1

    signed_faces = 0
    signed_charts = 0
    for k in range(2, 7):
        mandatory = list(range(1, 2*k-2, 2))
        words = [mandatory,
                 list(reversed(mandatory))+list(range(2*k-1)),
                 list(range(2*k-1))+mandatory+list(reversed(range(2*k-1)))]
        for word in words:
            for marked_cap in range(k):
                chart = morse_faces(k, word, marked_cap)
                v = chart['v']
                for f in range(chart['faces']):
                    index = chart['middle'][f]-chart['turns'][f]
                    assert index == (-2 if f == 0 else 2)
                    twice_nu = (2 if f not in (0, v) else 0)-index
                    twice_nu += 2*((1 if f == v else 0)-(1 if f == 0 else 0))
                    assert twice_nu == 0
                    signed_faces += 1
                signed_charts += 1

    ward_count = 0
    force_rows = []
    for N in (15, 16, 31, 32):
        d = N-1
        a = d//2
        m = d-a
        q = mp.exp(mp.pi*1j/N)
        Q = q*q
        points = {
            '222': (-mp.mpf('1.3'), -mp.mpf('.8')),
            '220': (-mp.mpf('1.3'), N*N*mp.mpc('1.2', '.2')),
            '022': (mp.mpc('1.1', '.3')/(N*N), -mp.mpf('.8')),
            '202': (N*N*mp.mpc('1.2', '.2'),
                    mp.mpf('1.4')/(N*N*mp.mpc('1.2', '.2'))),
            '200': (N*N*mp.mpc('1.2', '.2'), mp.exp(mp.mpf('.4')*1j)),
            '002': (mp.exp(mp.mpf('.3')*1j), mp.mpc('.9', '.3')/(N*N)),
        }
        for typ, (X, Y) in points.items():
            U, V = X/q, Y/q
            H = lambda u, v: literal_h(N, m, u, v)
            h = H(U, V)
            assert abs(h) > mp.mpf('1e-40')
            A0 = Q**d
            check('actual_F_Ward',
                  (1-U)*H(U/Q, V)+U*(1-V)*H(U, V/Q),
                  (1-U*V*Q**(-m))*h)
            check('actual_E_Ward',
                  A0*(U-A0)*H(Q*U, V)+U*(V-A0)*H(U, Q*V),
                  (Q**m*U*V-A0*A0)*h)
            p = mp.diff(lambda t: H(U*mp.exp(t), V), 0)/(N*h)
            r = mp.diff(lambda t: H(U, V*mp.exp(t)), 0)/(N*h)
            if typ == '222':
                u, v = -X, -Y
                expected = (mp.atan(u*mp.sqrt(v)/mp.sqrt(1+u+u*v))/mp.pi,
                            mp.atan(mp.sqrt(v*(1+u+u*v)))/mp.pi)
            elif typ == '220':
                expected = (mp.atan(mp.sqrt(-X))/mp.pi, mp.mpf('.5'))
            elif typ == '022':
                expected = (0, mp.atan(mp.sqrt(-Y))/mp.pi)
            elif typ == '202':
                z = mp.atan(mp.sqrt(X*Y))/mp.pi
                expected = (z, z)
            elif typ == '200':
                expected = (mp.mpf('.5'), mp.mpf('.5'))
            else:
                expected = (0, 0)
            force_rows.append({'N': N, 'type': typ,
                               'force_error': float(max(abs(p-expected[0]), abs(r-expected[1])))})
            ward_count += 2

    ldl_count = 0
    for N in range(3, 24):
        for a in sorted({1, (N-1)//2}):
            Hminus = matrix(N, a, mp.mpf(1), mp.mpf(0))-mp.eye(a)
            theta = mp.pi/N
            pivots = mp.fprod(mp.sin(n*theta)/(mp.cos(n*theta)*mp.sin((2*n-1)*theta))
                             for n in range(1, a+1))
            check('literal_LDL_anchor', mp.det(Hminus), pivots)
            ldl_count += 1

    Lob = lambda t: mp.im(mp.polylog(2, mp.exp(2j*t)))/2
    anchor_count = 0
    angle_count = 0
    for x, b, y in [(mp.mpf(1), mp.mpf(1), mp.mpf(1)),
                    (mp.mpf('1.3'), mp.mpf('.8'), mp.mpf('2.1')),
                    (mp.mpf('.2'), mp.mpf(3), mp.mpf('1.7'))]:
        delta = mp.sqrt(x*b+b*y+y*x)
        angles = [2*mp.atan(t/delta) for t in (x, b, y)]
        check('angle_sum', sum(angles), mp.pi)
        radii = [1/t for t in (x, b, y)]
        for j in range(3):
            R, S, T = radii[j], radii[(j+1)%3], radii[(j+2)%3]
            check('literal_circle_angle', mp.tan(angles[j]/2),
                  mp.sqrt(S*T/(R*(R+S+T))))
            angle_count += 1
        F = mp.log(b)/2+rate(mp.mpf('.5'), x/(2*b), y/(2*b))
        legendre = 2*mp.pi*F-sum(t*mp.log(z) for t, z in zip(angles, (x, b, y)))
        lob = 2*sum(Lob(t/2)+Lob((mp.pi-t)/2) for t in angles)
        check('absolute_Legendre_anchor', legendre, lob)
        anchor_count += 1

    fan_count = 0
    for n in range(3, 10):
        raw = [mp.mpf(2)+(j % 3)/mp.mpf(5) for j in range(n)]
        arcs = [2*mp.pi*t/sum(raw) for t in raw]
        assert max(arcs) < mp.pi
        tri = mp.mpf(0)
        for j in range(1, n-1):
            three_arcs = (sum(arcs[:j]), arcs[j], sum(arcs[j+1:]))
            tri += sum(Lob(t/2) for t in three_arcs)
        check('white_polygon_fan', tri, sum(Lob(t/2) for t in arcs))
        fan_count += 1

    result = {
        'status': 'PASS', 'digits': mp.mp.dps,
        'literal_mark_ratios': mark_count, 'literal_cup_cap_scalar_pairs': cup_pair_count,
        'actual_Morse_charts': signed_charts, 'signed_face_indices_and_zero_marked_forces': signed_faces,
        'actual_large_H_Ward_identities': ward_count,
        'six_type_force_diagnostics': force_rows,
        'original_LDL_anchor_checks': ldl_count,
        'circle_angle_identities': angle_count,
        'absolute_rate_Lobachevsky_comparisons': anchor_count,
        'cyclic_polygon_fan_cancellations': fan_count,
        'max_relative_errors': {name: mp.nstr(value, 14) for name, value in maxima.items()},
        'scope': 'Original mark and signed Morse source, exact large-H force inputs, absolute determinant/volume anchor. Force errors are diagnostics; no original-cycle or full-label asymptotic is tested.'
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
