#!/usr/bin/env python3
"""Exact closure/coordinate certificates for actual positive Conway runs.

The all-length disk isotopy is proved in the accompanying note. No numerical
manifold recognition or approximate volume is used in this audit.
"""
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_odd_central_cube_reflection_packet import turn


def symbolic_seam():
    x = sp.Symbol('x', real=True)
    y, z = 1-x, sp.Integer(1)
    p, q, r, w = z-x, z-y, x+y-z, 1-x-y
    triples = [(p+r, q+r, w), (p, q, 2*r+w), (p+q, r, r+w)]
    assert triples == [(1-x, x, 0), (1-x, x, 0), (1, 0, 0)]
    assert all(sp.simplify(sum(t)-1) == 0 for t in triples)
    # Multiplication's coefficient at output d cancels formally:
    # s_d*s_d / (s_i*s_(d-i)*s_(d-i)*s_i*s_0).
    # Root symmetry s_(d-i)=N/s_i and s_d=N gives exactly one.
    N, si = sp.symbols('N si', nonzero=True)
    mu = N*N/(si*(N/si)*(N/si)*si)
    assert sp.simplify(mu) == 1
    return {'closure_product_atoms': [list(map(str, t)) for t in triples],
            'full_normal_product_closure_coefficient': '1'}


def disk_certificate(s):
    centers = [4*i for i in range(1, s+1)]
    rectangles = [(centers[0]-3, centers[0]-1)]
    rectangles += [(y+1, y+3) for y in centers]
    # Exact sign of a+b*sqrt(2), b=+-1, at integral a.
    def sign_radical(a, b):
        if b == 1:
            return 1 if a >= 0 or a*a < 2 else -1
        return -1 if a <= 0 or a*a < 2 else 1
    def inside(y, sign, lo, hi):
        return sign_radical(y-lo, sign) > 0 and sign_radical(hi-y, -sign) > 0
    circle_plane_hits = []
    disk_main_hits = []
    for i, y in enumerate(centers):
        lower = [j for j, (lo, hi) in enumerate(rectangles) if inside(y, -1, lo, hi)]
        upper = [j for j, (lo, hi) in enumerate(rectangles) if inside(y, 1, lo, hi)]
        assert lower == [i] and upper == [i+1]
        # Each planar rectangle meets X=0 in its two horizontal sides.
        # Its side is in the circle's spanning disk iff (Y-y)^2<2.
        hits = [j for j, (lo, hi) in enumerate(rectangles)
                for a in (lo, hi) if (a-y)**2 < 2]
        assert hits == [i, i+1]
        circle_plane_hits.append([lower[0], upper[0]])
        disk_main_hits.append(hits)
    assert all((a-b)**2 > 8 for a, b in zip(centers, centers[1:]))
    # The last rectangle disk contains just the upper point of C_s.
    terminal = [(i, sign) for i, y in enumerate(centers) for sign in (-1, 1)
                if inside(y, sign, *rectangles[-1])]
    assert terminal == [(s-1, 1)]
    # Its incident auxiliary disk, after deletion, meets exactly M_(s-1).
    assert [j for j in disk_main_hits[-1] if j != s] == [s-1]
    return {'s': s, 'main_components': s+1, 'auxiliary_components': s,
            'total_components': 2*s+1,
            'circle_plane_rectangle_incidence': circle_plane_hits,
            'terminal_disk_intersections': len(terminal),
            'successive_meridian_insertions': 2*s}


class Pairing:
    """Planar TL2 pairing plus count of already closed main loops."""
    def __init__(self, pairs, loops=0):
        self.pairs, self.loops = tuple(sorted(tuple(sorted(p)) for p in pairs)), loops

    def turn(self):
        # New ports in terms of old: (1,3,0,2).
        inverse = {1: 0, 3: 1, 0: 2, 2: 3}
        return Pairing([(inverse[a], inverse[b]) for a, b in self.pairs], self.loops)

    def product(self, other):
        parent = list(range(8))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def join(a, b):
            parent[find(a)] = find(b)
        for a, b in self.pairs: join(a, b)
        for a, b in other.pairs: join(a+4, b+4)
        join(2, 4); join(3, 5)
        ext = [0, 1, 6, 7]
        groups = {}
        for a in range(8): groups.setdefault(find(a), []).append(a)
        internal = sum(not any(a in ext for a in group) for group in groups.values())
        pairs = [tuple(ext.index(a) for a in group if a in ext)
                 for group in groups.values() if any(a in ext for a in group)]
        assert all(len(p) == 2 for p in pairs)
        return Pairing(pairs, self.loops+other.loops+internal)

    def close(self):
        graph = [set() for _ in range(4)]
        for a, b in self.pairs+((0, 2), (1, 3)):
            graph[a].add(b); graph[b].add(a)
        seen, count = set(), 0
        for a in range(4):
            if a in seen: continue
            count += 1
            queue = [a]
            while queue:
                b = queue.pop()
                if b in seen: continue
                seen.add(b); queue.extend(graph[b]-seen)
        return self.loops+count


def pairing_certificates():
    I, U = Pairing([(0, 2), (1, 3)]), Pairing([(0, 1), (2, 3)])
    assert I.turn().pairs == U.pairs and U.turn().pairs == I.pairs
    out, run = [], I
    for s in range(1, 33):
        run = run.product(U)
        assert run.pairs == U.pairs and run.loops == s-1
        assert run.close() == s and run.turn().close() == s+1
        out.append({'s': s, 'ordinary_main_components': run.close(),
                    'turned_main_components': run.turn().close()})
    return out


def physical_level(N):
    p, eta, q, E, F, K, pivot, _, _ = balanced_data(N)
    d = N-1
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(a), -1, p) for a in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    I = np.eye(N*N, dtype=np.int64)
    previous, circle = I, O.copy()
    for _ in range(2, N): previous, circle = circle, (O@circle-previous) % p
    circle = (-1)**d*circle % p
    pv = [N*pow(q, -d*(d-u), p) % p for u in range(N)]
    h, power = turn(circle, N, p, pv), I.copy()
    rows = []
    for s in range(1, 10):
        power = power@h % p
        cap_closed = turn(power, N, p, pv).reshape(N, N, N, N)
        partial = sum((int(pivot[b])*cap_closed[:, b, :, b] for b in range(N)),
                      np.zeros((N, N), dtype=np.int64)) % p
        assert np.array_equal(partial, pow(N, 2*s, p)*np.eye(N, dtype=np.int64) % p)
        rows.append({'s': s, 'original_all_input_partial_trace': 'N^(2s) I'})
    return {'N': N, 'prime': p, 'full_normal_original_source_checks': rows}


if __name__ == '__main__':
    result = {'status': 'PASS', 'symbolic_closure': symbolic_seam(),
              'disk_coordinate_checks': [disk_certificate(s) for s in range(1, 33)],
              'planar_pairing_checks': pairing_certificates(),
              'original_marked_physical_checks': [physical_level(N) for N in range(2, 11)],
              'scope': 'Exact finite checks supplement the all-length coordinate disk induction. No manifold recognition, volume fit, or general Conway hyperbolicity claim.'}
    Path(__file__).with_name('positive_conway_geometric_incidence_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS symbolic flat closure /32 literal disk-incidence models /32 planar pairing runs /81 all-input original marked closures')
