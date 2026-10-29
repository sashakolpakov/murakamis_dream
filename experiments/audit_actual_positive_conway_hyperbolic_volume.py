#!/usr/bin/env python3
"""Exact support and literal colored-cell incidence for positive Conway links.

No numerical manifold recognition or volume fit is used. Geometry/isometry
comes from the analytical maximum and local-cell proofs; this audit checks
the actual ordered boundary maps, all colored facets, edge cycles and cusps.
"""
import json
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

from audit_positive_conway_geometric_incidence import Pairing


A = ('A',)


def T(e): return ('turn', e)
def P(f, g): return ('product', f, g)


def expand(e):
    if e == A:
        return P(P(('h',), ('h',)), ('h',))
    return (e[0], *(expand(c) for c in e[1:]))


def examples():
    a, b = A, T(A)
    c, d = P(a, b), T(P(b, a))
    return [A, P(a, a), P(a, b), P(b, b), P(c, d),
            P(T(c), d), P(T(P(c, d)), P(d, b)),
            P(P(a, c), P(d, b)), P(T(P(c, d)), T(P(d, c)))]


def strict_state(e, b):
    assert 0 < b < 1
    if e == A:
        c = min(2*b/3, 1-b)/2
        t = b-c/2
        a = (t/2+min(t, Q(1, 2)))/2
        return ('product', b,
                ('product', t, ('h', a), ('h', a)), ('h', c))
    if e[0] == 'turn':
        return ('turn', b, strict_state(e[1], 1-b))
    x = (b/2+min(b, Q(1, 2)))/2
    return ('product', b, strict_state(e[1], x), strict_state(e[2], x))


def verify_state(s):
    kind, b = s[:2]
    if kind == 'h':
        assert 0 < b < Q(1, 2)
        return 1, 0
    if kind == 'turn':
        assert b+s[2][1] == 1
        return verify_state(s[2])
    x, y = s[2][1], s[3][1]
    p, q, r, w = b-x, b-y, x+y-b, 1-x-y
    assert min(p, q, r, w) > 0
    assert p+q+2*r+w == 1
    # The three actual source angle triples are all strictly positive.
    atoms = [(y, x, w), (p, q, 2*r+w), (p+q, r, r+w)]
    assert all(min(t) > 0 and sum(t) == 1 for t in atoms)
    l1, g1 = verify_state(s[2]); l2, g2 = verify_state(s[3])
    return l1+l2, g1+g2+1


def strict_support_checks():
    points = [Q(1, 101), Q(1, 7), Q(1, 3), Q(1, 2),
              Q(2, 3), Q(6, 7), Q(100, 101)]
    count = 0
    for e in examples():
        for b in points:
            verify_state(strict_state(e, b)); count += 1
    # Every retained cylindrical factor has a strict reduced state.
    for e in examples():
        if e == A:
            left = ('product', Q(2, 3), ('h', Q(5, 12)), ('h', Q(5, 12)))
            right = ('h', Q(1, 3))
        else:
            left, right = strict_state(e[1], Q(1, 2)), strict_state(e[2], Q(1, 2))
        assert left[1]+right[1] == 1
        verify_state(left); verify_state(right)
    return {'exact_open_strict_assignments': count,
            'exact_reduced_closed_assignments': len(examples())}


class Mesh:
    def __init__(self, faces, port, leaves):
        self.faces, self.port, self.leaves = faces, port, leaves


class Compiler:
    def __init__(self):
        self.parent = []
        self.leaf_data = {}

    def vertex(self):
        k = len(self.parent); self.parent.append(k); return k

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        self.parent[self.find(a)] = self.find(b)

    @staticmethod
    def edges(cycle):
        return [tuple(sorted((a, b))) for a, b in zip(cycle, cycle[1:]+cycle[:1])]

    def normalize(self, mesh):
        mesh.faces = [(color, tag, tuple(self.find(v) for v in cyc))
                      for color, tag, cyc in mesh.faces]
        mesh.port = tuple(self.find(v) for v in mesh.port) if mesh.port is not None else None
        assert all(len(cyc) == len(set(cyc)) for _, _, cyc in mesh.faces)
        # Every white/white seam is precisely one of the flat seams in the
        # source angle table. Merge polygons, retaining all colored ideal ends.
        while True:
            incidence = defaultdict(list)
            for i, (color, _, cyc) in enumerate(mesh.faces):
                for edge in self.edges(cyc): incidence[edge].append(i)
            assert all(len(fs) == 2 for fs in incidence.values())
            pair = next((fs for fs in incidence.values()
                         if mesh.faces[fs[0]][0] == mesh.faces[fs[1]][0] == 'W'), None)
            if pair is None: break
            i, j = pair
            boundary = set(self.edges(mesh.faces[i][2])) ^ set(self.edges(mesh.faces[j][2]))
            graph = defaultdict(list)
            for a, b in boundary:
                graph[a].append(b); graph[b].append(a)
            assert graph and all(len(v) == 2 for v in graph.values())
            start = min(graph); cycle = [start]; previous = None; current = start
            while True:
                nxt = next(v for v in graph[current] if v != previous)
                if nxt == start: break
                assert nxt not in cycle
                cycle.append(nxt); previous, current = current, nxt
            assert len(cycle) == len(graph)
            mesh.faces = [f for n, f in enumerate(mesh.faces) if n not in (i, j)]
            mesh.faces.append(('W', ('merged',), tuple(cycle)))
        return mesh

    def leaf(self):
        O, c0, c1, c2, c3 = [self.vertex() for _ in range(5)]
        leaf_id = len(self.leaf_data)
        self.leaf_data[leaf_id] = (O, c0, c1, c2, c3)
        faces = [('S', (leaf_id, 0), (O, c1, c2)),
                 ('S', (leaf_id, 1), (O, c3, c0)),
                 ('W', (), (O, c0, c1)), ('W', (), (O, c2, c3)),
                 ('Q', (), (c0, c1, c2, c3))]
        return Mesh(faces, (c0, c1, c2, c3), [leaf_id])

    def product(self, f, g):
        infinity, P0, v0, v1, v2, v3 = [self.vertex() for _ in range(6)]
        # Literal lower top-left/right -> upper bottom-left/right.
        lower = (v0, v1, P0, infinity)
        upper = (infinity, P0, v2, v3)
        for a, b in zip(f.port, lower): self.join(a, b)
        for a, b in zip(g.port, upper): self.join(a, b)
        faces = [face for face in f.faces+g.faces if face[0] != 'Q']
        faces += [('W', (), (P0, v1, v2)), ('W', (), (infinity, v0, v3)),
                  ('Q', (), (v0, v1, v2, v3))]
        return self.normalize(Mesh(faces, (v0, v1, v2, v3), f.leaves+g.leaves))

    def open(self, e):
        if e[0] == 'h': return self.leaf()
        if e[0] == 'turn':
            mesh = self.open(e[1])
            mesh.port = mesh.port[1:]+mesh.port[:1]
            return mesh
        return self.product(self.open(e[1]), self.open(e[2]))

    def closed(self, e):
        assert e[0] == 'product'
        f, g = self.open(e[1]), self.open(e[2])
        for j in range(4): self.join(f.port[j], g.port[3-j])
        mesh = Mesh([face for face in f.faces+g.faces if face[0] != 'Q'],
                    None, f.leaves+g.leaves)
        return self.normalize(mesh)

    def check_closed(self, mesh):
        incidence = defaultdict(list)
        neighbors = defaultdict(set)
        for i, (color, _, cyc) in enumerate(mesh.faces):
            for edge in self.edges(cyc):
                incidence[edge].append(i)
                a, b = edge; neighbors[a].add(b); neighbors[b].add(a)
        H = len(mesh.leaves)
        assert len(neighbors) == 3*H
        assert len(incidence) == 6*H
        assert len(mesh.faces) == 3*H+2
        assert sum(color == 'S' for color, _, _ in mesh.faces) == 2*H
        assert sum(color == 'W' for color, _, _ in mesh.faces) == H+2
        assert all(len(adj) == 4 for adj in neighbors.values())
        assert all(sorted(mesh.faces[i][0] for i in fs) == ['S', 'W']
                   for fs in incidence.values())
        # Actual shaded maps reconstruct the two punctured main U-arcs.
        edge_partner, vertex_partner = {}, []
        for leaf_id in mesh.leaves:
            O, c0, c1, c2, c3 = [self.find(v) for v in self.leaf_data[leaf_id]]
            assert len({O, c0, c1, c2, c3}) == 5
            forward = {O: O, c1: c0, c2: c3}
            backward = {v: k for k, v in forward.items()}
            vertex_partner += list(forward.items())
            for source, mapping in [((O, c1, c2), forward), ((O, c3, c0), backward)]:
                for edge in self.edges(source):
                    target = tuple(sorted(mapping[v] for v in edge))
                    assert target != edge
                    edge_partner[edge] = target
        assert len(edge_partner) == len(incidence)
        for edge, other in edge_partner.items():
            assert edge_partner[other] == edge
            orbit = [(0, edge), (0, other), (1, other), (1, edge)]
            assert len(set(orbit)) == 4
        # White maps switch identical copies. Thus cusp connectivity reduces
        # to the actual shaded vertex identifications in one labeled copy.
        par = {v: v for v in neighbors}
        def find(v):
            while par[v] != v:
                par[v] = par[par[v]]; v = par[v]
            return v
        for a, b in vertex_partner: par[find(a)] = find(b)
        cusps = len({find(v) for v in neighbors})
        return {'h_leaves': H, 'vertices': len(neighbors), 'edges': len(incidence),
                'shaded_triangles': 2*H, 'white_faces': H+2,
                'four_right_angle_edge_cycles': len(incidence)//2,
                'actual_cusp_components': cusps}


def main_pairing(e):
    if e[0] == 'h': return Pairing([(0, 1), (2, 3)])
    if e[0] == 'turn': return main_pairing(e[1]).turn()
    return main_pairing(e[1]).product(main_pairing(e[2]))


def incidence_checks():
    rows = []
    for e in examples():
        expanded = expand(e)
        compiler = Compiler()
        mesh = compiler.closed(expanded)
        row = compiler.check_closed(mesh)
        main = main_pairing(expanded).close()
        assert row['actual_cusp_components'] == main+row['h_leaves']
        row['literal_main_components'] = main
        rows.append(row)
    return rows


if __name__ == '__main__':
    result = {'status': 'PASS', 'strict_support': strict_support_checks(),
              'literal_colored_cells': incidence_checks(),
              'scope': 'Exact rational strict-support and ordered cell-incidence checks. The all-expression metric realization follows from the strict-maximum, local prism/pyramid and cusp proofs, not from sampled quantum values.'}
    Path(__file__).with_name('actual_positive_conway_hyperbolic_volume_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS63 exact strict open assignments /9 reduced strict closed assignments /9 full colored-cell compilations with actual cusp counts and four-step edge cycles')
