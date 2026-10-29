"""Exact Lorentz certificate for the rectified cube and its actual bowtie cell.

This checks a finite example of the general cell proof. It makes no
quantum-asymptotic claim and uses no numerical polyhedron recognition.
"""
from itertools import product, combinations
from pathlib import Path
import json
import sympy as s

rt = s.sqrt(2)


def dot(a, b):
    return s.simplify(-a[0] * b[0] + sum(a[i] * b[i] for i in range(1, 4)))


def canon(a):
    return tuple(s.simplify(x / a[0]) for x in a)


def negative(x):
    return bool(s.simplify(x) < 0)


def audit():
    # The literal ordered NC source, including the opposite white ribbon order.
    black = [(0, 1, 2), (3, 4, 11), (5, 9, 10), (6, 7, 8)]
    white = [(0, 10, 11), (1, 8, 9), (2, 3, 7), (4, 5, 6)]
    rows = black + [tuple(reversed(row)) for row in white]
    endpoints = {e: tuple(v for v, row in enumerate(rows) if e in row) for e in range(12)}
    unseen = {(v, e) for v, row in enumerate(rows) for e in row}
    source_faces = []
    while unseen:
        start = at = min(unseen)
        face = []
        while at in unseen:
            unseen.remove(at)
            v, e = at
            face.append(e)
            w = next(x for x in endpoints[e] if x != v)
            row = rows[w]
            at = (w, row[(row.index(e) + 1) % 3])
        assert at == start
        source_faces.append(tuple(face))
    assert len(source_faces) == 6 and all(len(f) == 4 for f in source_faces)
    source_face_vertices = [set().union(*(set(endpoints[e]) for e in f)) for f in source_faces]
    opposite_faces = []
    pending = set(range(6))
    while pending:
        i = min(pending)
        candidates = [j for j in pending if not source_face_vertices[i] & source_face_vertices[j]]
        assert len(candidates) == 1
        j = candidates[0]
        opposite_faces.append((i, j))
        pending -= {i, j}
    vertex_signs = {v: tuple(-1 if v in source_face_vertices[i] else 1
                            for i, j in opposite_faces) for v in range(8)}
    assert len(set(vertex_signs.values())) == 8
    edge_core = {}
    for e, (v, w) in endpoints.items():
        sv, sw = vertex_signs[v], vertex_signs[w]
        changed = [i for i in range(3) if sv[i] != sw[i]]
        assert len(changed) == 1
        zero = changed[0]
        remaining = [sv[i] for i in range(3) if i != zero]
        edge_core[e] = (zero, *remaining)
    assert len(set(edge_core.values())) == 12

    signs = list(product((-1, 1), repeat=3))
    vertices = {}
    triangles = {}
    squares = {}
    for zero in range(3):
        axes = [i for i in range(3) if i != zero]
        for u, v in product((-1, 1), repeat=2):
            xyz = [s.S.Zero] * 3
            xyz[axes[0]], xyz[axes[1]] = u / rt, v / rt
            vertices[(zero, u, v)] = s.Matrix([1] + xyz)
    for sig in signs:
        n = s.Matrix([rt] + list(sig))
        tri = tuple(k for k, x in vertices.items() if dot(n, x) == 0)
        assert len(tri) == 3
        assert all(dot(n, x) == 0 or negative(dot(n, x)) for x in vertices.values())
        triangles[sig] = (n, tri)
    for v, row in enumerate(rows):
        assert {edge_core[e] for e in row} == set(triangles[vertex_signs[v]][1])
    for axis in range(3):
        for sig in (-1, 1):
            xyz = [s.S.Zero] * 3
            xyz[axis] = rt * sig
            n = s.Matrix([1] + xyz)
            face = tuple(k for k, x in vertices.items() if dot(n, x) == 0)
            assert len(face) == 4 and dot(n, n) == 1
            squares[(axis, sig)] = (n, face)
    assert all(dot(x, x) == 0 for x in vertices.values())
    assert len(vertices) == 12
    incidence_checks = 0
    for n, tri in triangles.values():
        assert dot(n, n) == 1
        for m, face in squares.values():
            if len(set(tri) & set(face)) == 2:
                assert dot(n, m) == 0
                incidence_checks += 1
    assert incidence_checks == 24

    all_vertices = {('core', k): x for k, x in vertices.items()}
    faces = {}
    octahedra = []
    for sig, (n, tri) in triangles.items():
        old = [rt * vertices[k] for k in tri]
        assert all(dot(old[i], old[j]) == -1 for i, j in combinations(range(3), 2))
        new = [sum((old[j] for j in range(3) if j != i), s.zeros(4, 1)) + rt * n
               for i in range(3)]
        for i, x in enumerate(new):
            assert dot(x, x) == 0 and x[0] > 0
            all_vertices[('new', sig, i)] = s.Matrix(canon(x))
        six = old + new
        for i, j in combinations(range(6), 2):
            assert dot(six[i], six[j]) == (-2 if j == i + 3 else -1)
        opp = 2 * n + sum(old, s.zeros(4, 1)) / rt
        assert dot(opp, opp) == 1
        faces[('white_tri', sig)] = (opp, tuple(('new', sig, i) for i in range(3)))
        for i in range(3):
            sh = n + rt * old[i]
            keys = (('core', tri[i]),) + tuple(('new', sig, j) for j in range(3) if j != i)
            assert dot(sh, sh) == 1 and dot(sh, opp) == 0
            faces[('shade', sig, tri[i])] = (sh, keys)
        # Each new vertex opposite i lies in the old square through the other two.
        for i in range(3):
            pair = {tri[j] for j in range(3) if j != i}
            candidates = [m for m, f in squares.values() if pair <= set(f)]
            assert len(candidates) == 1
            assert dot(candidates[0], new[i]) == 0
        octahedra.append(six)

    assert len({canon(x) for x in all_vertices.values()}) == 36
    for key, (m, _) in squares.items():
        members = tuple(k for k, x in all_vertices.items() if dot(m, x) == 0)
        assert len(members) == 8
        faces[('white_polygon', key)] = (m, members)
    assert len(faces) == 38
    for n, members in faces.values():
        assert all(dot(n, all_vertices[k]) == 0 for k in members)
        assert all(negative(dot(n, x)) for k, x in all_vertices.items() if k not in members)

    edges = []
    for (f, (n, v)), (g, (m, w)) in combinations(faces.items(), 2):
        intersection = set(v) & set(w)
        if len(intersection) == 2:
            assert dot(n, m) == 0
            assert (f[0] == 'shade') != (g[0] == 'shade')
            edges.append((f, g, frozenset(intersection)))
        else:
            assert len(intersection) <= 1
    assert len(edges) == 72
    assert len(all_vertices) - len(edges) + len(faces) == 2
    for k in all_vertices:
        assert sum(k in vs for _, _, vs in edges) == 4
    # Each core vertex is exactly one crossing-disk bowtie, with two shaded ends.
    for k in vertices:
        ends = [f for f, (_, vs) in faces.items() if f[0] == 'shade' and ('core', k) in vs]
        assert len(ends) == 2
        sigs = [f[1] for f in ends]
        assert sum(a != b for a, b in zip(*sigs)) == 1

    return {
        'status': 'PASS',
        'core_ideal_vertices': 12,
        'literal_NC_source_face_cycles': source_faces,
        'literal_NC_vertex_signs': vertex_signs,
        'core_right_angle_edges': incidence_checks,
        'canonical_octahedral_attachments': len(octahedra),
        'result_ideal_vertices': len(all_vertices),
        'result_right_angle_edges': len(edges),
        'result_faces': len(faces),
        'result_shaded_triangles': sum(f[0] == 'shade' for f in faces),
        'result_white_faces': sum(f[0] != 'shade' for f in faces),
        'arithmetic': 'Exact Q(sqrt(2)); all supporting inequalities and Gram entries exact.',
        'scope': 'Finite certificate of the cube instance. General topology/completeness and volume additivity are proved in the note; no quantum-growth check.'
    }


if __name__ == '__main__':
    result = audit()
    path = Path(__file__).with_name('actual_nc_graph_rectified_core_geometry_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
