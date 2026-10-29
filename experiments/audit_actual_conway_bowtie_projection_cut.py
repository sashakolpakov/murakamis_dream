#!/usr/bin/env python3
"""Independent literal-wire bowtie ribbon graph versus geometric cell faces.

The wire/ribbon compiler below does not use prisms or their face maps.
The existing cell compiler is invoked only for the final comparison.
"""
import json
import random
from collections import defaultdict
from pathlib import Path

import sympy as sp

from audit_actual_positive_conway_hyperbolic_volume import (
    Compiler, expand, examples, A, P, T,
)


def canonical_cycle(cycle):
    a = list(cycle); b = a[::-1]
    return min(tuple(r[i:]+r[:i]) for r in (a, b) for i in range(len(r)))


def oriented_cycle(cycle):
    a = list(cycle)
    return min(tuple(a[i:]+a[:i]) for i in range(len(a)))


class LiteralWires:
    """Only original four-port rotation/stack/closure and disk sectors."""
    def __init__(self):
        self.leaves = 0
        self.match = {}

    def join(self, a, b):
        assert a != b and a not in self.match and b not in self.match
        self.match[a] = b; self.match[b] = a

    def compile(self, e):
        if e[0] == 'h':
            i = self.leaves; self.leaves += 1
            return [(i, j) for j in range(4)]
        if e[0] == 'turn':
            ports = self.compile(e[1])
            return ports[1:]+ports[:1]
        lower, upper = self.compile(e[1]), self.compile(e[2])
        self.join(lower[2], upper[1])  # right identity strand
        self.join(lower[3], upper[0])  # left identity strand
        return lower[:2]+upper[2:]

    def vertex(self, terminal):
        return ('main',)+tuple(sorted((terminal, self.match[terminal])))

    def closed_faces(self, e):
        ports = self.compile(e)
        self.join(ports[0], ports[3]); self.join(ports[1], ports[2])
        assert len(self.match) == 4*self.leaves
        rotation = {}
        sectors = defaultdict(list)
        shaded = set()
        for i in range(self.leaves):
            apex = ('circle', i)
            c = [self.vertex((i, j)) for j in range(4)]
            assert len(set(c)) == 4
            rotation[apex] = c
            shaded.add(oriented_cycle((apex, c[1], c[2])))
            shaded.add(oriented_cycle((apex, c[3], c[0])))
            # At each disk corner: next followed by previous is its
            # positively oriented SHADED sector. The identity strip
            # concatenates the two sectors at the paired main segment.
            for j, nxt, previous in [
                    (1, c[2], apex), (2, apex, c[1]),
                    (3, c[0], apex), (0, apex, c[3])]:
                sectors[c[j]].append([nxt, previous])
        for v, pieces in sectors.items():
            assert len(pieces) == 2
            rotation[v] = pieces[0]+pieces[1]
            assert len(set(rotation[v])) == 4
        seen, faces = set(), []
        for v, neighbors in rotation.items():
            for w in neighbors:
                if (v, w) in seen: continue
                start = (v, w); a, b = start; cycle = []
                while True:
                    assert (a, b) not in seen
                    seen.add((a, b)); cycle.append(a)
                    neighbors_b = rotation[b]
                    a, b = b, neighbors_b[(neighbors_b.index(a)-1) % 4]
                    if (a, b) == start: break
                faces.append(oriented_cycle(cycle))
        assert shaded <= set(faces)
        assert len(rotation)-len(seen)//2+len(faces) == 2
        self.rotation = rotation
        return sorted(('S' if face in shaded else 'W', face) for face in faces)


def expression_cases():
    cases = list(examples())
    one = [A, T(A)]
    two = [P(a, b) for a in one for b in one]
    two += [T(e) for e in two]
    cases += [P(a, b) for a in one for b in two]
    cases += [P(a, b) for a in two for b in one]
    rng = random.Random(20261029)
    def random_tree(n):
        if n == 1:
            return T(A) if rng.randrange(2) else A
        k = rng.randrange(1, n)
        out = P(random_tree(k), random_tree(n-k))
        return T(out) if rng.randrange(2) else out
    for n in range(4, 11):
        for _ in range(4):
            k = rng.randrange(1, n)
            cases.append(P(random_tree(k), random_tree(n-k)))
    return list(dict.fromkeys(cases))


def compare_faces(e):
    expanded = expand(e)
    original = LiteralWires()
    expected = original.closed_faces(expanded)
    geometric = Compiler()
    mesh = geometric.closed(expanded)
    vertex_map = {}
    for i, (apex, *corners) in geometric.leaf_data.items():
        vertex_map[geometric.find(apex)] = ('circle', i)
        for j, v in enumerate(corners):
            expected_vertex = original.vertex((i, j))
            geometric_vertex = geometric.find(v)
            assert (geometric_vertex not in vertex_map or
                    vertex_map[geometric_vertex] == expected_vertex)
            vertex_map[geometric_vertex] = expected_vertex
    # Orient the geometric sphere coherently using opposite traversals on
    # shared edges. Fix ONE global choice by the original first shaded face;
    # do not independently reverse individual faces in the comparison.
    faces = [(color, tag, tuple(vertex_map[v] for v in cycle))
             for color, tag, cycle in mesh.faces]
    edge_faces = defaultdict(list)
    for i, (_, _, cycle) in enumerate(faces):
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            edge_faces[tuple(sorted((a, b)))].append(i)
    assert all(len(indices) == 2 for indices in edge_faces.values())
    anchor = next(i for i, (color, tag, _) in enumerate(faces)
                  if color == 'S' and tag == (0, 0))
    desired_anchor = oriented_cycle((('circle', 0), original.vertex((0, 1)),
                                     original.vertex((0, 2))))
    anchor_cycle = faces[anchor][2]
    if oriented_cycle(anchor_cycle) != desired_anchor:
        anchor_cycle = anchor_cycle[::-1]
    assert oriented_cycle(anchor_cycle) == desired_anchor
    oriented = {anchor: anchor_cycle}
    queue = [anchor]
    for i in queue:
        cycle = oriented[i]
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            adjacent = next(j for j in edge_faces[tuple(sorted((a, b)))] if j != i)
            candidate = oriented.get(adjacent, faces[adjacent][2])
            darts = set(zip(candidate, candidate[1:]+candidate[:1]))
            if (b, a) not in darts:
                assert adjacent not in oriented
                candidate = candidate[::-1]
                darts = set(zip(candidate, candidate[1:]+candidate[:1]))
            assert (b, a) in darts
            if adjacent not in oriented:
                oriented[adjacent] = candidate; queue.append(adjacent)
    assert len(oriented) == len(faces)
    actual = sorted((faces[i][0], oriented_cycle(cycle))
                    for i, cycle in oriented.items())
    assert actual == expected
    # Independently extract the geometric rotation at every vertex from
    # those coherently oriented face sectors and compare the literal order.
    rotation_successor = defaultdict(dict)
    for cycle in oriented.values():
        for k, v in enumerate(cycle):
            previous, nxt = cycle[k-1], cycle[(k+1) % len(cycle)]
            assert nxt not in rotation_successor[v]
            rotation_successor[v][nxt] = previous
    for v, successors in rotation_successor.items():
        start = min(successors); order = [start]
        while successors[order[-1]] != start:
            order.append(successors[order[-1]])
            assert len(order) <= 4
        assert len(order) == 4
        assert oriented_cycle(order) == oriented_cycle(original.rotation[v])
    return {'h_leaves': original.leaves,
            'original_main_segment_pairs': len(original.match)//2,
            'compared_colored_face_cycles': len(expected),
            'all_white_cycles_and_all_disk_sectors_match': True,
            'one_global_orientation_fixed_by_first_shaded_triangle': True,
            'every_oriented_face_cycle_matches': True,
            'every_vertex_cyclic_order_matches': True}


def cusp_certificate():
    u = sp.symbols('u', positive=True, real=True)
    E = sp.cancel((1+sp.I*u)**2/(1+u*u))
    Eb = sp.conjugate(E)
    assert sp.simplify(E*Eb) == 1
    W2 = sp.simplify((E-1)*(Eb-1))
    H2 = sp.simplify((E+1)*(Eb+1))
    assert sp.simplify(W2-4*u*u/(1+u*u)) == 0
    assert sp.simplify(H2-4/(1+u*u)) == 0
    # Actual complete shaded inverse and the bottom/top white path.
    mu = E-1
    white_linear = -1/E
    white_bottom = 1+1/E
    white_top = -1-1/E
    longitude = sp.simplify((white_bottom-white_top)/white_linear)
    assert sp.simplify(longitude+2*(E+1)) == 0
    assert sp.simplify(longitude/mu-2*sp.I/u) == 0
    # Oriented area of the two actual primitive generators is exactly
    # the area of TWO rectangles, not a double longitude lattice.
    area = sp.simplify(sp.im(sp.conjugate(mu)*longitude))
    assert sp.simplify(area-8*u/(1+u*u)) == 0
    return {'parameter': 'u=tan(pi x)>0',
            'white_side_squared': str(W2), 'shaded_side_squared': str(H2),
            'primitive_meridian': 'E-1', 'disk_longitude': '-2(E+1)',
            'geometric_cusp_ratio': '2i cot(pi x)',
            'primitive_area': '2 W H',
            'packet_parameter': 'i cot(pi x), half geometric cusp ratio'}


if __name__ == '__main__':
    rows = [compare_faces(e) for e in expression_cases()]
    result = {'status': 'PASS',
              'independent_literal_wire_face_comparisons': rows,
              'exact_complete_crossing_circle_cusp': cusp_certificate(),
              'scope': 'Independent literal main-wire and disk-sector compiler compared against every colored face cycle of the geometric compiler. Closed projection-cut proof is analytical; an auxiliary open Q port is not asserted to be a physical four-punctured sphere, and no deformed global holonomy is inferred.'}
    Path(__file__).with_name('actual_conway_bowtie_projection_cut_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS{len(rows)} independent full colored-face comparisons /exact marked two-rectangle cusp lattice')
