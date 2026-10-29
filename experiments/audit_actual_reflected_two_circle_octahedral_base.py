#!/usr/bin/env python3
"""Exact face/edge/cusp certificate; optional literal-diagram software diagnostic."""
import argparse
from collections import defaultdict, deque
from fractions import Fraction
import itertools
import json
from pathlib import Path


SOURCE_PD = [(1,10,2,11),(2,19,3,16),(15,19,10,18),(17,15,18,14),
             (16,3,17,4),(11,4,12,5),(5,8,0,9),(12,7,13,8),
             (6,13,7,14),(9,0,6,1)]
EQUATOR = [2,4,3,5]  # Y+, Z+, Y-, Z-
WHITE = [(0,2,5),(0,3,4),(1,2,4),(1,3,5)]
BOWTIES = [((0,2,4),(0,3,5),{0:0,2:3,4:5}),
           ((1,2,5),(1,3,4),{1:1,2:3,5:4})]


class DSU:
    def __init__(self, keys):
        self.parent = {x:x for x in keys}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[b] = a
    def classes(self):
        out = defaultdict(list)
        for x in self.parent:
            out[self.find(x)].append(x)
        return list(out.values())


def complex_multiply(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def tetrahedral_certificate():
    # The first bow tie uses adjacent ports(0,1),(2,3); quarter-turn
    # of the second uses(3,0),(1,2), giving the octahedral graph.
    lower = [frozenset((0,EQUATOR[0],EQUATOR[1])),
             frozenset((0,EQUATOR[2],EQUATOR[3]))]
    upper = [frozenset((1,EQUATOR[3],EQUATOR[0])),
             frozenset((1,EQUATOR[1],EQUATOR[2]))]
    shaded = set(lower+upper)
    expected_shaded = {frozenset(f) for a,b,_ in BOWTIES for f in (a,b)}
    assert shaded == expected_shaded
    octedges = {tuple(sorted((a,b))) for face in shaded
                for a,b in itertools.combinations(face,2)}
    assert len(octedges) == 12
    assert all(sum(v in e for e in octedges) == 4 for v in range(6))
    vertices = []
    for cell in range(2):
        for j in range(4):
            a,b = EQUATOR[j],EQUATOR[(j+1)%4]
            vertices.append([1,0,a,b] if cell == 0 else [1,0,b,a])
    faces = {}
    for t,v in enumerate(vertices):
        for f in range(4):
            faces[t//4,frozenset(v[i] for i in range(4) if i != f)] = (t,f)
    joins, paired = [], set()
    def pair(a, b, vertex_map):
        assert a not in paired and b not in paired
        t,f = a;u,g = b
        perm = [None]*4;perm[f] = g
        for i in range(4):
            if i != f:
                perm[i] = vertices[u].index(vertex_map[vertices[t][i]])
        assert tuple(perm) == (0,1,3,2)
        joins.append((t,f,u,g,tuple(perm)));paired.update((a,b))
    for cell in range(2):
        for j in range(4):
            t,u = 4*cell+j,4*cell+(j+1)%4
            common = set(vertices[t]) & set(vertices[u])
            f = next(i for i in range(4) if vertices[t][i] not in common)
            g = next(i for i in range(4) if vertices[u][i] not in common)
            pair((t,f),(u,g),{v:v for v in common})
    for w in WHITE:
        fw = frozenset(w)
        pair(faces[0,fw],faces[1,fw],{v:v for v in w})
    for a,b,vm in BOWTIES:
        pair(faces[0,frozenset(a)],faces[1,frozenset(b)],vm)
        pair(faces[1,frozenset(a)],faces[0,frozenset(b)],vm)
    assert len(paired) == 32 and len(joins) == 16
    tv = DSU((t,a) for t in range(8) for a in range(4))
    te = DSU((t,a,b) for t in range(8) for a,b in itertools.combinations(range(4),2))
    lv = DSU((t,a,b) for t in range(8) for a in range(4) for b in range(4) if a != b)
    le = DSU((t,a,f) for t in range(8) for a in range(4) for f in range(4) if a != f)
    adjacent = defaultdict(set)
    for t,f,u,g,p in joins:
        remaining = [a for a in range(4) if a != f]
        for a in remaining:
            tv.union((t,a),(u,p[a]))
            le.union((t,a,f),(u,p[a],g))
            adjacent[t,a].add((u,p[a]));adjacent[u,p[a]].add((t,a))
        for a,b in itertools.combinations(remaining,2):
            x,y = sorted((p[a],p[b]))
            te.union((t,a,b),(u,x,y))
            lv.union((t,a,b),(u,p[a],p[b]))
            lv.union((t,b,a),(u,p[b],p[a]))
    assert len(tv.classes()) == 4 and len(te.classes()) == 8
    edge_rows = []
    for edge in te.classes():
        angle, product = Fraction(0), (Fraction(1),Fraction(0))
        counts = [0,0,0]
        for t,a,b in edge:
            if (a,b) in ((0,1),(2,3)):
                angle += Fraction(1,2);z = (Fraction(0),Fraction(1));counts[0] += 1
            elif (a,b) in ((0,2),(1,3)):
                angle += Fraction(1,4);z = (Fraction(1,2),Fraction(1,2));counts[1] += 1
            else:
                angle += Fraction(1,4);z = (Fraction(1),Fraction(1));counts[2] += 1
            product = complex_multiply(product,z)
        assert angle == 2 and product == (1,0)
        edge_rows.append({'tetrahedral_valence':len(edge),'shape_counts':counts,
                          'angle_over_pi':str(angle),'exact_complex_product':'1'})
    cusp_rows = []
    for cusp in tv.classes():
        seen={cusp[0]};queue=deque(seen)
        while queue:
            for nxt in adjacent[queue.popleft()]:
                if nxt not in seen:seen.add(nxt);queue.append(nxt)
        assert seen == set(cusp)
        F = len(cusp)
        E = len({le.find((t,a,f)) for t,a in cusp for f in range(4) if a != f})
        V = len({lv.find((t,a,b)) for t,a in cusp for b in range(4) if a != b})
        assert F == 8 and V-E+F == 0
        octvertices = {(t//4,vertices[t][a]) for t,a in cusp}
        cusp_rows.append({'ideal_labels':sorted({v for _,v in octvertices}),
                          'octahedral_squares':len(octvertices),'triangles':F,
                          'link_edges':E,'link_vertices':V,'Euler_characteristic':V-E+F,
                          'connected':True,'orientable_from_odd_face_maps':True})
    assert sorted(r['octahedral_squares'] for r in cusp_rows) == [2,2,4,4]
    return {'source_port_bow_ties_give_octahedral_graph':True,
            'paired_faces':len(joins),'all_gluing_permutations':'0132',
            'edges':edge_rows,'four_complete_torus_links':cusp_rows,
            'volume':'8 D(i) = 2 v8'},vertices,joins


def software_diagnostic(vertices, joins):
    # This supplements, and does not replace, the reversible cut reading.
    import regina
    import snappy
    from spherogram.links.tangles import BraidTangle,Tangle,join_strands
    def circle():
        c = BraidTangle([2,1,1,2],3)
        e = c.adjacent
        join_strands(e[2],e[5])
        return Tangle((2,2),c.crossings,[e[0],e[1],e[3],e[4]])
    link = (((BraidTangle([1],2)*circle()).rotate(1))*
            (BraidTangle([-1],2)*circle())).denominator_closure()
    assert len(link.link_components) == 4
    # The PD need only be relabelled if a different software release
    # chooses different oriented starts. This installed version is fixed.
    assert link.PD_code() == SOURCE_PD
    tr = regina.Triangulation3()
    tets = [tr.newTetrahedron() for _ in range(8)]
    for t,f,u,g,p in joins:tets[t].join(f,tets[u],regina.Perm4(*p))
    assert tr.isValid() and tr.isOrientable()
    assert tr.countVertices() == 4
    assert all(v.linkEulerChar() == 0 for v in tr.vertices())
    octman = snappy.Manifold(tr.isoSig())
    actual = link.exterior()
    assert actual.isometry_signature() == octman.isometry_signature()
    return {'literal_auxiliary_braid':[2,1,1,2],'literal_PD':link.PD_code(),
            'components':len(link.link_components),'linking_matrix':link.linking_matrix(),
            'exact_octahedral_triangulation_isosig':tr.isoSig(),
            'source_and_cell_canonical_signature':actual.isometry_signature(),
            'numerical_volume':str(actual.volume()),
            'scope':'software diagnostic, not the topological or metric proof'}


if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--software',action='store_true')
    options=args.parse_args()
    exact,vertices,joins=tetrahedral_certificate()
    result={'status':'PASS','exact_face_edge_cusp_certificate':exact}
    if options.software:result['optional_literal_source_software_diagnostic']=software_diagnostic(vertices,joins)
    Path(__file__).with_name('actual_reflected_two_circle_octahedral_base_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS exact source-port octahedral graph; 16 paired faces; '
          '8 exact edge products/angles; 4 complete torus links'
          + ('; literal PD/software cross-check' if options.software else ''))
