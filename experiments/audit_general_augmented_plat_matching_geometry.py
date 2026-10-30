#!/usr/bin/env python3
"""Literal plat/Conway terminal matchings -> cubic dimer -> full medial faces.

Checks ordered face cycles, not merely Euler counts. A positive metric
certificate is an independent input; no certificate is inferred here.
"""
import json
from collections import defaultdict
from pathlib import Path

from audit_actual_conway_bowtie_projection_cut import (
    LiteralWires, expression_cases, oriented_cycle,
)
from audit_actual_positive_conway_hyperbolic_volume import expand


def terminal_vertex(matching, terminal):
    return ('main',)+tuple(sorted((terminal, matching[terminal])))


def boundary_faces(r, matching):
    """Direct bowtie sectors and original outside strips, without Delta."""
    rotation, sectors, shaded = {}, defaultdict(list), set()
    for i in range(r):
        o = ('circle', i)
        c = [terminal_vertex(matching, (i, j)) for j in range(4)]
        rotation[o] = c
        shaded.add(oriented_cycle((o, c[1], c[2])))
        shaded.add(oriented_cycle((o, c[3], c[0])))
        for j, nxt, previous in [(1, c[2], o), (2, o, c[1]),
                                 (3, c[0], o), (0, o, c[3])]:
            sectors[c[j]].append([nxt, previous])
    for v, pieces in sectors.items():
        assert len(pieces) == 2
        rotation[v] = pieces[0]+pieces[1]
    # Degenerate terminal matches are recorded and cannot be a positive Q.
    if any(len(ns) != len(set(ns)) for ns in rotation.values()):
        return None
    seen, faces = set(), []
    for v, neighbors in rotation.items():
        for w in neighbors:
            if (v, w) in seen: continue
            start = v, w; cycle = []
            while True:
                assert (v, w) not in seen
                seen.add((v, w)); cycle.append(v)
                ns = rotation[w]
                v, w = w, ns[(ns.index(v)-1) % len(ns)]
                if (v, w) == start: break
            faces.append(oriented_cycle(cycle))
    assert shaded <= set(faces)
    return shaded, set(faces)-shaded


def cubic_dictionary(r, matching):
    rotation, endpoints, disk_edges = {}, defaultdict(list), set()
    for i in range(r):
        disk = ('circle', i); disk_edges.add(disk)
        c = [terminal_vertex(matching, (i, j)) for j in range(4)]
        rotation[(i, 0)] = [disk, c[1], c[2]]
        rotation[(i, 1)] = [disk, c[3], c[0]]
    for v, edges in rotation.items():
        assert len(edges) == 3
        assert sum(edge in disk_edges for edge in edges) == 1
        for edge in edges: endpoints[edge].append(v)
    assert len(rotation) == 2*r and len(endpoints) == 3*r
    assert all(len(vs) == 2 for vs in endpoints.values())
    # A loop or repeated triangle corner is a genuine certificate obstruction.
    if any(len(set(vs)) < 2 for vs in endpoints.values()):
        return {'crossing_disks': r, 'degenerate_loop': True}
    if any(len(edges) != len(set(edges)) for edges in rotation.values()):
        return {'crossing_disks': r, 'degenerate_triangle': True}
    seen, faces = set(), []
    for first, edges in rotation.items():
        for edge0 in edges:
            if (first, edge0) in seen: continue
            start = first, edge0; v, edge = start; cycle = []
            while True:
                assert (v, edge) not in seen
                seen.add((v, edge)); cycle.append(edge)
                w = next(w for w in endpoints[edge] if w != v)
                es = rotation[w]
                edge = es[(es.index(edge)-1) % 3]; v = w
                if (v, edge) == start: break
            faces.append(oriented_cycle(cycle))
    original = boundary_faces(r, matching)
    if original is None:
        return {'crossing_disks': r, 'degenerate_medial_rotation': True}
    shaded, white = original
    assert {oriented_cycle(es) for es in rotation.values()} == shaded
    assert set(faces) == white
    # Complement of the matching: actual 2-factor cycle lengths.
    visited, lengths = set(), []
    for first in rotation:
        if first in visited: continue
        vertices = {first}; todo = [first]
        while todo:
            v = todo.pop(); visited.add(v)
            for edge in rotation[v]:
                if edge in disk_edges: continue
                w = next(w for w in endpoints[edge] if w != v)
                if w not in vertices: vertices.add(w); todo.append(w)
        lengths.append(len(vertices))
    return {'crossing_disks': r, 'cubic_vertices': 2*r, 'cubic_edges': 3*r,
            'white_face_cycles': len(faces),
            'all_oriented_medial_faces_match': True,
            'nonmatching_cycle_lengths': sorted(lengths),
            'positive_geometry_not_inferred': True}


def plat_matching(k, boxes):
    """Original vertical 2k-plat, boxes at zero-based adjacent strand slots.

    Half twists are restored by shaded maps, so outside intervals use the
    flat diagram. All original upper/lower caps are retained explicitly.
    """
    parent = {}
    def find(v):
        parent.setdefault(v, v)
        if parent[v] != v: parent[v] = find(parent[v])
        return parent[v]
    def join(a, b): parent[find(a)] = find(b)
    active = [('top', i) for i in range(2*k)]
    for i in range(k): join(active[2*i], active[2*i+1])
    for n, a in enumerate(boxes):
        assert 0 <= a < 2*k-1
        # A cyclic chart: upper left/right are C2,C1; lower are C3,C0.
        join(active[a], (n, 2)); join(active[a+1], (n, 1))
        active[a], active[a+1] = (n, 3), (n, 0)
        find(active[a]); find(active[a+1])
    for i in range(k): join(active[2*i], active[2*i+1])
    groups = defaultdict(list)
    for n in range(len(boxes)):
        for j in range(4): groups[find((n, j))].append((n, j))
    assert all(len(terminals) == 2 for terminals in groups.values())
    matching = {}
    for a, b in groups.values(): matching[a] = b; matching[b] = a
    top_components = {find(('top', i)) for i in range(2*k)}
    free_components = len(top_components-set(groups))
    return matching, free_components


def main_components(matching, parities):
    """Restore actual within-box strands; full twist signs do not enter."""
    local = {}
    for i, odd in enumerate(parities):
        pairs = [(0,2),(1,3)] if odd else [(0,1),(2,3)]
        for a,b in pairs:
            local[(i,a)] = (i,b); local[(i,b)] = (i,a)
    seen, count = set(), 0
    for first in matching:
        if first in seen: continue
        count += 1; todo = [first]
        while todo:
            v = todo.pop()
            if v in seen: continue
            seen.add(v); todo.extend((matching[v], local[v]))
    return count


def main():
    rows = []
    for e in expression_cases():
        wire = LiteralWires(); wire.closed_faces(expand(e))
        rows.append(cubic_dictionary(wire.leaves, wire.match))
    for s in range(3,21):
        e = ('h',)
        for _ in range(s-1): e = ('product', e, ('h',))
        wire = LiteralWires(); wire.closed_faces(e)
        row = cubic_dictionary(wire.leaves, wire.match)
        assert row['nonmatching_cycle_lengths'] == [s, s]
        rows.append(row)
    # Arbitrary-height adjacent boxes at genuine multi-bridge width. These
    # are dictionary tests, not claims that every designated plat is reduced.
    plats = []
    for k in range(2,9):
        odd = list(range(1,2*k-2,2))
        even = list(range(0,2*k-1,2))
        for boxes in [odd+even+odd, odd+even+odd+even+odd,
                      odd+list(reversed(even))+odd]:
            matching, free = plat_matching(k, boxes)
            row = cubic_dictionary(len(boxes), matching)
            row.update(bridges=k, boxes=boxes, unrecorded_free_components=free)
            assert free == 0
            assert main_components(matching, [0]*len(boxes)) == k
            parity = [1]*len(odd)+[0]*(len(boxes)-len(odd))
            components = main_components(matching, parity)
            assert components == 1
            row.update(knot_parity_witness=parity,
                       restored_main_components=components)
            plats.append(row)
    result = {'status': 'PASS', 'actual_conway_dictionary_cases': len(rows),
              'literal_multi_bridge_plat_cases': plats,
              'four_circle_obstruction_to_literal_3b_NC_class': {
                  'r': 4, 'matching_complement_cycles': [4,4],
                  'r_multiple_of_three': False},
              'scope': 'Actual terminal intervals, perfect matching, oriented medial face cycles. Positive right-angled realization remains an independent certificate.'}
    Path(__file__).with_name('general_augmented_plat_matching_geometry_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(rows)} original Conway/dimer comparisons; '
          f'{len(plats)} literal 2k-plat dictionaries, k=2,...,8')


if __name__ == '__main__': main()
