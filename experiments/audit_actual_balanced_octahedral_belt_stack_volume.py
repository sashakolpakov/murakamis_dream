#!/usr/bin/env python3
"""Literal full-root balanced source words and regular-cell belt covers.

The general mixed-piece collar identification is the written cut proof.
Optional software comparison supplements it and is not the topology proof.
"""
import argparse
import itertools
import json
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path

from audit_actual_reflected_two_circle_octahedral_base import (
    tetrahedral_certificate, DSU, BOWTIES, complex_multiply,
)


def source_level(N):
    import numpy as np
    from audit_actual_two_cut_ports import balanced_data, coproduct, word_matrix
    from audit_actual_pair_casimir_commutant_and_rotated_trace import phi, rotated
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x = N-1, int(K[0, 0])
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    I = np.eye(N*N, dtype=np.int64)
    U0, U1 = I.copy(), O.copy()
    if d == 1:
        L = -U1 % p
    else:
        for _ in range(2, d+1):
            U0, U1 = U1, (O@U1-U0) % p
        L = (-1)**d*U1 % p

    def turn(A):
        return pow(x, d, p)*rotated(A, N, x, p) % p

    z, zs = turn(Rm@L % p), turn(Rp@L % p)
    assert np.array_equal(turn(turn(z)), z)
    assert np.array_equal(turn(turn(Rp)), Rp)
    fp, fm = zs@Rm % p, Rp@z % p
    literal_circle_mirror = None
    if N <= 6:
        mirrored = word_matrix([-2, -1, -1, -2], Rp, Rm, 3, N, p)
        closed = sum((int(pivot[a])*mirrored[a::N, a::N] for a in range(N)),
                     np.zeros_like(I)) % p
        assert np.array_equal(closed, L)
        literal_circle_mirror = True
    # Actual mirror then stack reversal: turn^2 on each factor and reversed order.
    reflected_reversed = turn(turn(Rp))@turn(turn(z)) % p
    assert np.array_equal(fm, reflected_reversed)
    assert np.array_equal(fp@fm % p, zs@z % p)
    assert np.array_equal(fm@fp % p, zs@z % p)
    records = []
    for k in (1, 2, 3):
        power = I.copy()
        for _ in range(k):
            power = power@(zs@z % p) % p
        target = phi(L@power % p, N, pivot, p)
        words = list(itertools.combinations(range(2*k), k))
        for plus in words:
            plus = set(plus)
            product = I.copy()
            for i in range(2*k):
                product = product@(fp if i in plus else fm) % p
            assert np.array_equal(product, power)
            assert phi(L@product % p, N, pivot, p) == target
        records.append({'pieces': 2*k, 'all_balanced_orders': len(words),
                        'literal_original_scalar_mod_prime': int(target)})
    return {'N': N, 'full_physical_reflection_reversal_and_ports': True,
            'literal_negative_circle_full_pivotal_trace': literal_circle_mirror,
            'balanced_words': records}


def belt_cover(n, outer_parity=0):
    assert n>=1 and outer_parity in (0,1)
    _, vertices0, joins0 = tetrahedral_certificate()
    A, B, _ = BOWTIES[0]
    A, B = frozenset(A), frozenset(B)
    vertices = vertices0*n
    joins = []
    for sheet in range(n):
        for t, f, u, g, p in joins0:
            source_face = frozenset(vertices0[t][i] for i in range(4) if i != f)
            target_face = frozenset(vertices0[u][i] for i in range(4) if i != g)
            crossing_disk = source_face == A and target_face == B
            target_sheet = (sheet+int(crossing_disk)) % n
            if crossing_disk and sheet==n-1 and outer_parity:
                # The actual half collar exchanges punctures AND pants triangles.
                # Target cell changes; Y/Z exchange leaves local permutation0132.
                u=(u+4)%8
            joins.append((8*sheet+t, f, 8*target_sheet+u, g, p))
    size = 8*n
    tv = DSU((t, a) for t in range(size) for a in range(4))
    te = DSU((t, a, b) for t in range(size) for a, b in itertools.combinations(range(4), 2))
    lv = DSU((t, a, b) for t in range(size) for a in range(4) for b in range(4) if a != b)
    le = DSU((t, a, f) for t in range(size) for a in range(4) for f in range(4) if a != f)
    adjacency, body = defaultdict(set), defaultdict(set)
    paired = set()
    for t, f, u, g, p in joins:
        assert (t, f) not in paired and (u, g) not in paired
        paired.update(((t, f), (u, g)))
        body[t].add(u); body[u].add(t)
        ids = [a for a in range(4) if a != f]
        for a in ids:
            tv.union((t, a), (u, p[a]))
            le.union((t, a, f), (u, p[a], g))
            adjacency[t, a].add((u, p[a])); adjacency[u, p[a]].add((t, a))
        for a, b in itertools.combinations(ids, 2):
            c, e = sorted((p[a], p[b]))
            te.union((t, a, b), (u, c, e))
            lv.union((t, a, b), (u, p[a], p[b]))
            lv.union((t, b, a), (u, p[b], p[a]))
    assert len(paired) == 4*size
    reached, queue = {0}, deque([0])
    while queue:
        for v in body[queue.popleft()]:
            if v not in reached:
                reached.add(v); queue.append(v)
    assert len(reached) == size
    for edge in te.classes():
        angle, product = Fraction(0), (Fraction(1), Fraction(0))
        for t, a, b in edge:
            if (a, b) in ((0, 1), (2, 3)):
                angle += Fraction(1, 2); shape = (Fraction(0), Fraction(1))
            elif (a, b) in ((0, 2), (1, 3)):
                angle += Fraction(1, 4); shape = (Fraction(1, 2), Fraction(1, 2))
            else:
                angle += Fraction(1, 4); shape = (Fraction(1), Fraction(1))
            product = complex_multiply(product, shape)
        assert angle == 2 and product == (1, 0)
    cusps = tv.classes()
    assert len(cusps) == n+3-outer_parity
    for cusp in cusps:
        reached, queue = {cusp[0]}, deque([cusp[0]])
        while queue:
            for v in adjacency[queue.popleft()]:
                if v not in reached:
                    reached.add(v); queue.append(v)
        assert reached == set(cusp)
        F = len(cusp)
        E = len({le.find((t, a, f)) for t, a in cusp for f in range(4) if a != f})
        V = len({lv.find((t, a, b)) for t, a in cusp for b in range(4) if a != b})
        assert V-E+F == 0
    return {'pieces': n, 'outer_collar_parity':outer_parity,
            'regular_octahedra': 2*n, 'positive_tetrahedra': size,
            'connected': True, 'exact_edges': len(te.classes()),
            'complete_torus_cusps': len(cusps), 'volume': f'{2*n} v8'}, vertices, joins


def software_diagnostic():
    import snappy
    from spherogram.links.tangles import BraidTangle, Tangle, join_strands

    def circle(sign=1):
        c = BraidTangle([2*sign, sign, sign, 2*sign], 3)
        e = c.adjacent
        join_strands(e[2], e[5])
        return Tangle((2, 2), c.crossings, [e[0], e[1], e[3], e[4]])

    def piece(sign):
        if sign == '+':
            return (BraidTangle([1], 2)*circle()).rotate(1)*BraidTangle([-1], 2)
        # Literal mirror followed by stack reversal. Rotation2 reverses input/output.
        return ((BraidTangle([-1], 2)*circle(-1)).rotate(1)*BraidTangle([1], 2)).rotate(2)

    rows = []
    for word,outer in (('+-',0),('++--',0),('+-+-',0),('+++---',0),
                       ('+',1),('-',-1),('++',2),('+--',3),('++--',-2)):
        tangle = circle()
        if outer:
            tangle=tangle*BraidTangle([1 if outer>0 else -1]*abs(outer),2)
        for sign in word:
            tangle = tangle*piece(sign)
        link = tangle.denominator_closure()
        manifold = link.exterior()
        assert len(link.link_components) == len(word)+3-(outer%2)
        v8 = 4*float(__import__('mpmath').catalan)
        assert abs(float(manifold.volume())-2*len(word)*v8) < 1e-7
        rows.append({'word': word, 'outer_crossing_power':outer,
                     'actual_components': len(link.link_components),
                     'software_volume': float(manifold.volume()),
                     'scope': 'supplemental literal diagram check; geometry proved by cuts'})
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--software', action='store_true')
    parser.add_argument('--software-only', action='store_true',
                        help='Run literal geometry diagnostics without NumPy/source dependencies.')
    args = parser.parse_args()
    result_path = Path(__file__).with_name('actual_balanced_octahedral_belt_stack_volume_results.json')
    if args.software_only:
        results = json.loads(result_path.read_text()) if result_path.exists() else {
            'status': 'SOFTWARE_ONLY_PASS',
            'scope': 'Supplemental literal diagrams only; run default audit for original sources.'}
        results['optional_actual_diagram_diagnostics'] = software_diagnostic()
        result_path.write_text(json.dumps(results, indent=2)+'\n')
        print('PASS 9 literal sign/outer-collar diagrams, components and geometric diagnostics')
        raise SystemExit(0)
    results = {'status': 'PASS', 'original_balanced_sources': [source_level(N) for N in range(2, 9)],
               'exact_regular_cell_covers': [belt_cover(n,a)[0] for n in range(1,9) for a in (0,1)],
               'scope': 'Full physical balanced source and exact positive cyclic belt cells at both outer-collar parities; '
                        'mixed-piece/collar identification is the written reversible cut proof. '
                        'The all-sign/outer-power quantum asymptotic has its separate coherent source audit.'}
    if args.software:
        results['optional_actual_diagram_diagnostics'] = software_diagnostic()
    result_path.write_text(json.dumps(results, indent=2)+'\n')
    print('PASS 7 full physical balanced source levels/196 complete words; '
          '16 exact positive cyclic belt-cell/collar certificates')
