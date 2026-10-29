#!/usr/bin/env python3
"""Check the actual crossing Bloch sum against an oriented diagram cycle.

The proof uses determinant identities, three explicit five-term
boundaries, and a universal four-tetrahedron crossing block. Optional
Regina checks compare its unsimplified face pairing with independently
constructed link complements, not just with homology or volumes.
"""

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import mpmath as mp
import sympy as sp


def chain(vertices):
    if len(set(vertices)) < len(vertices):
        return Counter()
    sign = (-1)**sum(vertices[i] > vertices[j] for i in range(len(vertices))
                     for j in range(i+1, len(vertices)))
    return Counter({tuple(sorted(vertices)): sign})


def combine(*terms):
    answer = Counter()
    for scalar, term in terms:
        for key, value in term.items():
            answer[key] += scalar*value
    return Counter({key: value for key, value in answer.items() if value})


def boundary(vertices):
    return combine(*[((-1)**i, chain(vertices[:i]+vertices[i+1:]))
                     for i in range(len(vertices))])


def chain_certificate():
    a, b, p, pp, s, m, q, r = "a", "b", "p", "p1", "s0", "sM", "sP", "sR"
    T1, T3 = chain([a, p, s, m]), chain([a, p, q, r])
    beta = combine((1, T1), (-1, T3), (-1, chain([b, p, m, r])),
                   (1, chain([b, pp, m, r])), (1, chain([m, r, pp, p])))
    gamma = combine((-1, chain([pp, a, b, m])), (1, chain([pp, a, b, r])),
                    (1, chain([p, a, b, m])), (-1, chain([p, a, b, r])))
    defect = combine((1, T1), (-1, T3), (1, chain([a, p, pp, m])),
                     (-1, chain([a, p, pp, r])))
    certificate = combine((-1, boundary([b, p, pp, m, r])),
                          (1, boundary([a, b, p, pp, m])),
                          (-1, boundary([a, b, p, pp, r])))
    assert not combine((1, beta), (-1, gamma), (-1, defect), (-1, certificate))

    # The four original tetrahedra, before using a whole-tetrahedron
    # meridian transport to replace c,s0,sP by b,sM,sR.
    tetrahedra = [(-1, [p, a, "c", s]), (1, [p, a, "c", q]),
                  (1, [p, a, b, m]), (-1, [p, a, b, r])]
    total = Counter()
    for eps, tet in tetrahedra:
        for i in range(4):
            face = tet[:i]+tet[i+1:]
            if p not in face and "c" in face:
                action = {a: a, "c": b, s: m, q: r}
                face = [action[v] for v in face]
            total = combine((1, total), (eps*(-1)**i, chain(face)))

    def B(v, arc, following):
        return combine((1, chain([p, arc, v])), (-1, chain([p, arc, following])))

    expected = combine((1, B(s, "c", q)), (-1, B(m, b, r)),
                       (-1, B(s, a, m)), (1, B(q, a, r)))
    assert total == expected
    return {"five_term_boundary_certificate_exact": True,
            "five_vertex_boundaries": [[b, p, pp, m, r], [a, b, p, pp, m], [a, b, p, pp, r]],
            "shadow_boundary_identity_exact": True}


def det(u, v):
    return u[0]*v[1]-u[1]*v[0]


def ratio(v0, v1, v2, v3):
    return det(v3, v1)*det(v2, v0)/(det(v3, v0)*det(v2, v1))


def determinant_identities():
    b1, b2, p1, p2, s1, s2 = sp.symbols("b1 b2 p1 p2 s1 s2")
    a = sp.Matrix([1, 0])
    b = sp.Matrix([b1, b2])
    p = sp.Matrix([p1, p2])
    s = sp.Matrix([s1, s2])
    A = sp.Matrix([[1, 1], [0, 1]])
    U = lambda v: sp.eye(2)+v*sp.Matrix([[-v[1], v[0]]])
    B = U(b)
    c = A.inv()*b
    C = U(c)
    assert (C-A.inv()*B*A).applyfunc(sp.expand) == sp.zeros(2)
    m, q, r, pp = A*s, C*s, B*A*s, A*p
    assert (A*q-r).applyfunc(sp.expand) == sp.zeros(2, 1)
    w0, wm, wq, wr = [det(p, v) for v in (s, m, q, r)]
    pairs = [(ratio(a, p, s, m), wm/w0),
             (ratio(b, p, m, r), wr/wm),
             (ratio(a, p, q, r), wr/wq),
             (ratio(c, p, s, q), wq/w0),
             (ratio(m, r, pp, p), w0*wr/(wm*wq))]
    for left, right in pairs:
        assert sp.cancel(left-right) == 0
    for v, following in ((s, m), (q, r)):
        z = ratio(a, p, v, following)
        extra = ratio(a, p, pp, following)
        assert sp.cancel(extra-z/(z-1)) == 0

    # Keep the generic loxodromic correction; it vanishes by a shape
    # symmetry only at multiplier kappa=1.
    kappa, t, z0, y = sp.symbols("kappa t z0 y")
    following, moved_p = kappa*z0+t, kappa*y+t
    z = (following-y)/(z0-y)
    extra = (following-y)/(moved_p-y)
    assert sp.cancel(extra-z/(z-kappa)) == 0

    # Generic meridian factors use different over/under eigenflags.
    M, t, u, p1, p2, s1, s2 = sp.symbols("M t u p1 p2 s1 s2", nonzero=True)
    A = sp.Matrix([[M, t], [0, 1/M]])
    B = sp.Matrix([[M, 0], [u, 1/M]])
    a, b = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    c = A.inv()*b
    p, s = sp.Matrix([p1, p2]), sp.Matrix([s1, s2])
    C = A.inv()*B*A
    sm, sq, sr, pp = A*s, C*s, B*A*s, A*p
    w0, wm, wq, wr = [det(p, v) for v in (s, sm, sq, sr)]
    for left, right in [(ratio(a, p, s, sm), M*wm/w0),
                        (ratio(b, p, sm, sr), wr/(M*wm)),
                        (ratio(a, p, sq, sr), M*wr/wq),
                        (ratio(c, p, s, sq), wq/(M*w0)),
                        (ratio(sm, sr, pp, p), w0*wr/(wm*wq))]:
        assert sp.cancel(left-right) == 0
    return {"five_cross_ratio_identities_exact": True,
            "two_parabolic_orientation_cancellations_exact": True,
            "generic_affine_multiplier_correction_retained": True,
            "generic_meridian_factors_and_opposite_eigenflags_checked": True}


class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def join(self, a, b):
        self.parent[self.find(a)] = self.find(b)


LOCAL = [(0, 0, 2, 0), (1, 0, 3, 0), (0, 3, 1, 3), (2, 3, 3, 3)]
EPS = [-1, 1, 1, -1]


def octahedron_block():
    vertices = UnionFind((t, v) for t in range(4) for v in range(4))
    edges = UnionFind((t, a, b) for t in range(4) for a, b in combinations(range(4), 2))
    internal = set()
    for t, f, u, g in LOCAL:
        internal |= {(t, f), (u, g)}
        for v in range(4):
            if v != f:
                vertices.join((t, v), (u, v))
        for a, b in combinations([v for v in range(4) if v != f], 2):
            edges.join((t, a, b), (u, a, b))
    V = {vertices.find(item) for item in vertices.parent}
    E = {edges.find(item) for item in edges.parent}
    exterior = [(t, f) for t in range(4) for f in range(4) if (t, f) not in internal]
    boundary_edges = {edges.find((t, a, b)) for t, f in exterior
                      for a, b in combinations([v for v in range(4) if v != f], 2)}
    assert (len(V), len(E), len(exterior), len(boundary_edges)) == (6, 13, 8, 12)
    internal_edges = E-boundary_edges
    assert internal_edges == {edges.find((0, 1, 2))}
    assert sum(edges.find(item) in internal_edges for item in edges.parent) == 4

    north, south = sp.Matrix([0, 0, 1]), sp.Matrix([0, 0, -1])
    P = [sp.Matrix([1, 0, 0]), sp.Matrix([-1, 0, 0])]
    S = [sp.Matrix([0, 1, 0]), sp.Matrix([0, -1, 0])]
    determinants = []
    for t in range(4):
        p, s = P[t//2], S[t % 2]
        determinants.append(int(sp.Matrix.hstack(north-p, south-p, s-p).det()))
    assert determinants == [2*eps for eps in EPS]
    return {"vertices": len(V), "edges": len(E), "boundary_faces": len(exterior),
            "boundary_edges": len(boundary_edges), "internal_edge_valence": 4,
            "ball_shelling_face_counts": [0, 1, 1, 2],
            "oriented_Euclidean_determinants": determinants}


def shadow_pairing(strands, word):
    pairs, initial, current = [], [None]*strands, [None]*strands

    def pair(source, target):
        t, f = source
        u, g = target
        permutation = list(range(4))
        permutation[f], permutation[g] = permutation[g], permutation[f]
        pairs.append((t, f, u, g, permutation))

    def connect(left, right):
        for source, target in zip(left, right):
            pair(source, target)

    for n, (j, sign) in enumerate(word):
        z = 4*n
        for t, f, u, g in LOCAL:
            pair((z+t, f), (z+u, g))
        over_in = [(z, 2), (z+2, 2)]
        over_out = [(z+1, 2), (z+3, 2)]
        under_in = [(z+2, 1), (z+3, 1)]
        under_out = [(z, 1), (z+1, 1)]
        inputs, outputs = (([over_in, under_in], [under_out, over_out]) if sign > 0
                           else ([under_out, over_out], [over_in, under_in]))
        for k in range(2):
            pos = j+k
            if current[pos] is None:
                initial[pos] = inputs[k]
            else:
                connect(current[pos], inputs[k])
            current[pos] = outputs[k]
    assert all(slot is not None for slot in initial), "An unused braid strand"
    for left, right in zip(current, initial):
        connect(left, right)
    used = [face for t, f, u, g, _ in pairs for face in ((t, f), (u, g))]
    assert len(used) == len(set(used)) == 16*len(word)
    signs = [sign*eps for _, sign in word for eps in EPS]
    for t, f, u, g, perm in pairs:
        parity = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        assert signs[t] == -parity*signs[u]
        assert perm[f] == g
    return pairs, signs


def braid_gauss(strands, word):
    current = list(range(strands))
    visits = [[] for _ in range(strands)]
    for n, (j, sign) in enumerate(word, 1):
        left, right = current[j:j+2]
        visits[left].append(sign*n)
        visits[right].append(-sign*n)
        current[j:j+2] = [right, left]
    following = [current.index(i) for i in range(strands)]
    used, components = set(), []
    for i in range(strands):
        if i in used:
            continue
        component, j = [], i
        while j not in used:
            used.add(j)
            component += visits[j]
            j = following[j]
        components.append(component)
    return components


def topology_checks(with_regina):
    if with_regina:
        import regina
    figure = [(0, 1), (1, -1)]*2
    cases = [("unknot_positive", 2, [(0, 1)]),
             ("unknot_negative", 2, [(0, -1)]),
             ("Hopf", 2, [(0, 1)]*2),
             ("trefoil", 2, [(0, 1)]*3),
             ("figure_eight", 3, figure),
             ("weaving_3_4", 3, [(0, 1), (1, -1)]*4),
             ("torus_3_4", 3, [(0, 1), (1, 1)]*4),
             ("weaving_4_3", 4, [(0, 1), (1, -1), (2, 1)]*3),
             ("figure_eight_positive_stabilization", 4, figure+[(2, 1)]),
             ("figure_eight_negative_stabilization", 4, figure+[(2, -1)]),
             ("cancelling_pair", 3, figure+[(0, 1), (0, -1)])]
    records = []
    for name, strands, word in cases:
        pairs, _ = shadow_pairing(strands, word)
        components = braid_gauss(strands, word)
        record = {"name": name, "strands": strands, "word": word,
                  "tetrahedra": 4*len(word), "face_pairs": len(pairs),
                  "components": len(components), "oriented_face_pairing_checked": True}
        if with_regina:
            tri = regina.Triangulation3()
            tets = [tri.newTetrahedron() for _ in range(4*len(word))]
            for t, f, u, g, permutation in pairs:
                tets[t].join(f, tets[u], regina.Perm4(*permutation))
            assert tri.isValid() and tri.isOrientable()
            links = sorted(str(v.linkType()) for v in tri.vertices())
            assert links == sorted(["Link.Sphere"]*2+["Link.Torus"]*len(components))
            independent_link = regina.Link.fromData([s for _, s in word], components)
            independent = independent_link.complement(False)
            iso = tri.isIsomorphicTo(independent)
            assert iso is not None
            record.update({"Regina_valid": True, "vertex_links": links,
                           "independent_unsimplified_complement_isomorphic": True,
                           "homology": str(tri.homology()), "isoSig": tri.isoSig()})
        records.append(record)
    return {"Regina_requested": with_regina, "records": records}


def regulator_check():
    mp.mp.dps = 80
    u = mp.exp(-mp.pi*1j/3)
    A = mp.matrix([[1, 1], [0, 1]])
    B = mp.matrix([[1, 0], [u, 1]])
    C = A**-1*B*A*B**-1*A

    def D(z):
        return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)

    def tet(*vs):
        return D(ratio(*vs))

    def flag(M):
        columns = [mp.matrix([M[0, j]-int(j == 0), M[1, j]-int(j == 1)]) for j in range(2)]
        return max(columns, key=lambda v: abs(v[0])+abs(v[1]))

    records = []
    expected = -2*D(u)
    for rr, ss in ((mp.mpf(2), mp.mpf(3)), (mp.mpc(1, 1), mp.mpf(2)),
                   (mp.mpf(3), mp.mpc(-2, 1))):
        basis = mp.matrix([[rr, 1-rr], [ss, -ss]])
        meridians = [basis**-1*M*basis for M in (A, B, C)]
        states, previous = [], mp.eye(2)
        for M in meridians:
            G = -previous*M*previous**-1
            k, e, f = G[0, 0], G[0, 1], G[1, 0]/G[0, 0]
            states.append((k, e, f))
            previous = mp.matrix([[1, 0], [-k*f, k]])*previous
        initial = list(states)
        p, v = mp.matrix([0, 1]), mp.matrix([1, 0])
        total_beta = total_gamma = mp.mpf(0)
        maximum_local_error = mp.mpf(0)
        for j, sign in [(0, 1), (1, -1), (0, 1), (1, -1)]:
            prefix = mp.eye(2)
            for M in meridians[:j]:
                prefix = M*prefix
            s = prefix*v
            if sign > 0:
                ma, mb = meridians[j:j+2]
                mc = ma**-1*mb*ma
            else:
                mc, ma = meridians[j:j+2]
                mb = ma*mc*ma**-1
            a, b = flag(ma), flag(mb)
            c = ma**-1*b
            sm, sp_, sr = ma*s, mc*s, mb*ma*s
            gamma = sign*(-tet(p, a, c, s)+tet(p, a, c, sp_)
                          +tet(p, a, b, sm)-tet(p, a, b, sr))
            k, e, f = states[j]
            l, g, h = states[j+1]
            aa, bb = -1/k, -1/l
            if sign > 0:
                d = 1-e*h
                cc = 1/d
                U, W = bb, 1/aa
                changed = [(l*d, (d*g+e*(d*l-1/l))/k, k*h/d),
                           (k/d, e/(l*d), l*(d*f+h*(d/k-k)))]
                meridians[j:j+2] = [mc, ma]
            else:
                cc = 1-k*g*f/l
                U, W = aa, 1/bb
                changed = [(l*cc, k*g, f+h/k-f/(l*l*cc)),
                           (k/cc, l*e+g-k*k*g/cc, f/l)]
                meridians[j:j+2] = [ma, mb]
            beta = D(U)+D(cc)+D(W)-D(U*cc)-D(cc*W)
            states[j:j+2] = changed
            maximum_local_error = max(maximum_local_error, abs(beta-gamma))
            total_beta += beta
            total_gamma += gamma
        assert maximum_local_error < mp.mpf("1e-65")
        assert abs(total_gamma-expected) < mp.mpf("1e-65")
        records.append({"frame": [str(rr), str(ss)], "crossing_regulator": str(total_beta),
                        "shadow_cycle_regulator": str(total_gamma),
                        "maximum_local_comparison_error": float(maximum_local_error)})
    return {"scope": "Calibration only; the general statement is the symbolic/cellular argument.",
            "two_regular_tetrahedron_value": str(expected), "records": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--regina", action="store_true")
    args = parser.parse_args()
    result = {"scope": "Classical complete Bloch-class comparison for the actual crossing sum. No quantum volume-limit assertion.",
              "chain_certificate": chain_certificate(),
              "determinants": determinant_identities(),
              "local_octahedron": octahedron_block(),
              "diagram_topology": topology_checks(args.regina),
              "regulator_calibration": regulator_check()}
    Path(__file__).with_name("crossing_fundamental_cycle_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"five_term_certificate": True, "parabolic_determinant_identities": True,
                      "local_octahedron": result["local_octahedron"],
                      "diagram_face_pairings_checked": len(result["diagram_topology"]["records"]),
                      "Regina_exact_isomorphisms": args.regina,
                      "maximum_local_regulator_error": max(r["maximum_local_comparison_error"]
                                                           for r in result["regulator_calibration"]["records"]),
                      "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
