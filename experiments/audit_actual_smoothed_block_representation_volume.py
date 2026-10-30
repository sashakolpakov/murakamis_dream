#!/usr/bin/env python3
"""Typed digon cuts, literal collar words and compatible finite corner clusters.

The general topological disk quotient and volume inequality are proved in
the note, not inferred from these fixtures.  No quantum factorization is
tested or assumed.
"""
import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def equal(A, B):
    assert all(sp.expand(x) == 0 for x in A-B), (A, B)


def clean(A):
    return A.applyfunc(sp.expand)


def slinverse(A):
    assert sp.expand(A.det()) == 1
    return sp.Matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])


def circle(X):
    r = sp.Rational(1, 2)
    z = X+sp.I*r
    return clean(sp.Matrix([[z, r*r-z*sp.conjugate(z)], [1, -sp.conjugate(z)]])/r)


def hmove(pair, eps=1):
    A, B = pair
    return (clean(slinverse(A)*B*A), A) if eps == 1 else (B, clean(B*A*slinverse(B)))


def threaded(A, B, M):
    data = [A, B, M]
    for j in (2, 1, 1, 2):
        data[j-1:j+1] = hmove(data[j-1:j+1])
    return data


def transform(M, z):
    return sp.cancel((M[0, 0]*z+M[0, 1])/(M[1, 0]*z+M[1, 1]))


def typed_digon_spheres():
    counts = Counter()
    # K4 sphere blocks and zero-volume two-triangle blocks, joined at
    # ordered white pair (0,1).  The ab incidences are genuinely crossed
    # between consecutive blocks; keeping them within blocks is wrong.
    for sizes in ((4, 4), (4, 2), (2, 4, 4), (4, 4, 4), (2, 4, 2, 4)):
        blocks = []
        offset = 0
        for size in sizes:
            blocks.append(list(range(offset, offset+size)))
            offset += size
        edges = []
        for j, b in enumerate(blocks):
            edges.append((b[1], blocks[(j+1) % len(blocks)][0], 'cut'))
            if len(b) == 4:
                edges.extend((b[x], b[y], 'internal') for x, y in
                             ((0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
            else:
                edges.extend([(b[0], b[1], 'internal')]*2)
        degree = Counter(v for a, b, _ in edges for v in (a, b))
        assert all(degree[v] == 3 for v in range(offset))
        white_vertices = 2+sum(size//2 for size in sizes)
        assert white_vertices-len(edges)+offset == 2
        # Every consecutive nonempty proper block interval has exactly
        # TWO crossed edges, both of the same actual source type.
        for mode in ('MAIN', 'MATCHING'):
            matching = set()
            if mode == 'MATCHING':
                matching.update(i for i, (_, _, kind) in enumerate(edges) if kind == 'cut')
                for block in blocks:
                    if len(block) == 4:
                        matching.add(next(i for i, (a, b, _) in enumerate(edges)
                                          if {a, b} == set(block[2:])))
            else:
                for block in blocks:
                    pairs = ((block[0], block[2]), (block[1], block[3])) if len(block) == 4 else ((block[0], block[1]),)
                    for pair in pairs:
                        matching.add(next(i for i, (a, b, kind) in enumerate(edges)
                                          if kind == 'internal' and {a, b} == set(pair)))
            mdeg = Counter(v for i in matching for v in edges[i][:2])
            assert all(mdeg[v] == 1 for v in range(offset))
            counts['typed_spherical_sources'] += 1
            for start in range(len(blocks)):
                for length in range(1, len(blocks)):
                    selected = {v for k in range(length)
                                for v in blocks[(start+k) % len(blocks)]}
                    crossed = [i for i, (a, b, _) in enumerate(edges)
                               if (a in selected) != (b in selected)]
                    assert len(crossed) == 2
                    assert all((i in matching) == (mode == 'MATCHING') for i in crossed)
                    # Closing the cut side uses one new edge and keeps
                    # the full trivalent/matching type at both ports.
                    assert len(selected) % 2 == 0
                    counts['actual_two_edge_cuts'] += 1
    return dict(counts)


def actual_reflection_words():
    I = sp.eye(2)
    lower = -sp.I*I
    upper = sp.I*sp.Matrix([[1, 2*sp.I], [0, 1]])
    P = upper*sp.conjugate(lower)
    H = P+I
    equal(H*H, sp.zeros(2))
    counts = Counter()
    for x, y in product((sp.Rational(-1, 2), sp.Rational(1, 3), sp.Rational(7, 2)),
                        (sp.Rational(-5, 3), sp.Rational(3, 4), sp.Rational(11, 2))):
        Ri, Ro = circle(x), circle(y)
        A, B = clean(Ri*sp.conjugate(lower)), clean(upper*sp.conjugate(Ri))
        Ao, Bo = clean(Ro*sp.conjugate(lower)), clean(upper*sp.conjugate(Ro))
        C = sp.Matrix([[1, y-x], [0, 1]])
        equal(B*A, P)
        equal(C*A*C.inv(), Ao)
        equal(C*B*C.inv(), Bo)
        assert sp.simplify(sp.trace(H*A)-4) == 0
        for p, q in ((x, y), (x+sp.I, y+sp.I)):
            assert sp.simplify(transform(C, p)-q) == 0
            counts['original_shaded_contact_maps'] += 1
        for eps in (-1, 0, 1):
            M = clean(C.inv()*(I+H/2)**eps)
            assert M.det() == 1
            equal(M*P, P*M)
            result = threaded(A, B, M)
            pair = hmove(result[:2], eps) if eps else result[:2]
            equal(pair[0], Ao)
            equal(pair[1], Bo)
            equal(result[2], M)
            counts['literal_threading_Hurwitz_words'] += 1
        # Deleted untwisted box: restored identity auxiliary meridian.
        result = threaded(A, B, I)
        equal(result[0], A)
        equal(result[1], B)
        equal(result[2], I)
        counts['restored_deleted_meridians'] += 1
        # One global r_u, not one independent reflection per block.
        for R, points in ((lower, [x, y]), (upper, [x+sp.I, y+sp.I]),
                          (Ri, [x, x+sp.I]), (Ro, [y, y+sp.I])):
            G = R*sp.conjugate(lower)
            for p in points:
                second = transform(lower, sp.conjugate(p))
                assert sp.simplify(transform(G, second)-p) == 0
                counts['single_second_ball_white_pairings'] += 1
        path = [lower, Ri, upper, Ro, lower]
        pref = I
        for j in range(1, len(path)):
            pref = clean(path[j]*sp.conjugate(path[j-1])*pref)
            equal(pref, path[j]*sp.conjugate(path[0]))
            counts['original_prefix_relations'] += 1
    # Deleted boxes can have a nonparabolic outer product: identity
    # threading does not require a surviving parabolic collar.
    for A, B in ((sp.Matrix([[1, 2], [0, 1]]), sp.Matrix([[1, 0], [3, 1]])),
                 (sp.Matrix([[1, 2], [0, 1]]), sp.Matrix([[1, -2], [0, 1]]))):
        result = threaded(A, B, I)
        for actual, expected in zip(result, (A, B, I)):
            equal(actual, expected)
        counts['nonparabolic_deleted_outer_products'] += 1
    return dict(counts)


def compatible_corner_clusters():
    counts = Counter()
    worst = mp.mpf(0)
    for shift, c in product((mp.mpf('-.7'), mp.mpf('.4'), mp.mpf('2.3')),
                            (mp.mpf('.2'), mp.mpf('.6'))):
        # Actual determinant-one Mobius change.  Renormalization by
        # k(w)=-1/(w-g(infinity)) fixes the common ideal contact.
        g = mp.matrix([[1, shift], [c, 1+c*shift]])
        p = 1/c
        k = mp.matrix([[0, -1], [1, -p]])
        affine = k*g
        assert abs(affine[1, 0]) < mp.mpf('1e-60')
        scale = affine[0, 0]/affine[1, 1]
        width = abs(scale)
        for T in (mp.mpf(4), mp.mpf(40), mp.mpf(400)):
            points = [mp.mpc('-1.2', '.1'), mp.mpc('.3', '.5'), mp.mpc('1.7', '.9')]
            transformed = []
            for z in points:
                a,b,cc,d = affine[0,0],affine[0,1],affine[1,0],affine[1,1]
                den = abs(cc*z+d)**2+abs(cc)**2*T*T
                zz = ((a*z+b)*mp.conj(cc*z+d)+a*mp.conj(cc)*T*T)/den
                height = T/den
                err = abs(height/width-T)
                worst = max(worst, err)
                assert err < mp.mpf('1e-55')
                transformed.append((zz, height))
                counts['finite_incidence_horospheres'] += 1
            for j in (0, 1):
                ell = 2*mp.asinh(abs(points[j+1]-points[j])/(2*T))
                z0,t0 = transformed[j]
                z1,t1 = transformed[j+1]
                exact = mp.acosh(1+(abs(z0-z1)**2+(t0-t1)**2)/(2*t0*t1))
                assert abs(exact-ell) < mp.mpf('1e-55')
                bound = 2*mp.pi*ell*mp.cosh(ell)**2
                assert T*bound < 30
                counts['common_height_short_edge_bounds'] += 1
    # A diagnostic counterexample to the invalid ideal-coalescence
    # shortcut: (0,epsilon,i*epsilon,infinity) has constant shape i.
    def D(z):
        return mp.im(mp.polylog(2,z))+mp.arg(1-z)*mp.log(abs(z))
    vals = []
    for eps in (mp.mpf(1), mp.mpf('.01'), mp.mpf('1e-8')):
        shape = (1j*eps)/eps
        vals.append(D(shape))
        assert vals[-1] > mp.mpf('.9')
        counts['nonvanishing_ideal_coalescence_counterchecks'] += 1
    assert max(vals)-min(vals) < mp.mpf('1e-55')
    return dict(counts) | {'maximum_horosphere_error': str(worst)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'actual_smoothed_block_representation_volume_results.json'))
    args = parser.parse_args()
    mp.mp.dps = 70
    result = {'status': 'PASS', 'precision_digits': mp.mp.dps,
              'typed_cuts': typed_digon_spheres(),
              'actual_source_words': actual_reflection_words(),
              'finite_chain_corners': compatible_corner_clusters(),
              'scope': 'Exact typed block-cut fixtures and original reflection/contact/threading identities; '
                       'finite incidence decorations and a false ideal-coalescence countercheck. '
                       'The general disk quotient, degree, volume inequality and corridor are analytic proofs.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
