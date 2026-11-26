#!/usr/bin/env python3
"""Finite literal-wire / octahedron-attachment comparison.

The repository is resolved from this script; pass --repo to override it. Only the literal side imports
an existing repository compiler. The other side builds and glues colored
combinatorial octahedra. These finite identities supplement, not prove,
the general topological and analytic theorems.
"""
import argparse
import hashlib
import json
import random
import sys
from collections import defaultdict
from pathlib import Path


def cyc(xs):
    xs = tuple(xs)
    return min(xs[i:] + xs[:i] for i in range(len(xs)))


def turn(x, k=1):
    for _ in range(k):
        x = ('turn', x)
    return x


def product(xs):
    assert xs
    ans = xs[0]
    for x in xs[1:]:
        ans = ('prod', ans, x)
    return ans


def leaf_names(e):
    if e[0] == 'h':
        return [e[1]]
    if e[0] == 'turn':
        return leaf_names(e[1])
    return leaf_names(e[1]) + leaf_names(e[2])


def build(v, left, right, half, edge):
    # P=T^{-1}h is THREE actual quarter turns, not a scalar T.
    factors = [turn(build(w, left, right, half, edge), edge[w])
               for w in left[v]]
    factors += [turn(('h', v), 3)]
    factors += [turn(build(w, left, right, half, edge), edge[w])
                for w in right[v]]
    return turn(product(factors), 2 * half[v])


def main_vertex(a, b):
    return ('m',) + tuple(sorted((a, b)))


def circle(v):
    return ('o', v)


def standard_shades(v, match):
    q = [main_vertex((v, j), match[(v, j)]) for j in range(4)]
    return [cyc((circle(v), q[1], q[2])),
            cyc((circle(v), q[3], q[0]))]


def literal(e, LiteralWires):
    names = leaf_names(e)
    obj = LiteralWires()
    faces = obj.closed_faces(e)
    def rename(v):
        if v[0] == 'circle':
            return circle(names[v[1]])
        a, b = v[1:]
        return main_vertex((names[a[0]], a[1]), (names[b[0]], b[1]))
    out = sorted((color, cyc(tuple(rename(v) for v in face)))
                 for color, face in faces)
    pairs = {((names[a[0]], a[1]), (names[b[0]], b[1]))
             for a, b in obj.match.items()}
    return out, pairs


class OctahedronModel:
    def __init__(self, root_side, half_child, edge_child):
        self.match = {}
        self.faces = []
        self.pages = {0: 1, 1: 1}
        self.sectors = {0: [(0, 1)], 1: [(0, 1)]}
        self.cell_edges = [(0, 1)]
        self.cell_dual = []
        p0 = [(0, j) for j in (3, 0, 1, 2)]
        shift = (edge_child + 3 + 2 * half_child) % 4
        h1 = [(1, (j + shift) % 4) for j in range(4)]
        f, g = (p0, h1) if root_side == 'right' else (h1, p0)
        self.join(f[2], g[1]); self.join(f[3], g[0])
        exposed = f[:2] + g[2:]
        self.join(exposed[0], exposed[3]); self.join(exposed[1], exposed[2])
        q = [self.vertex((0, j)) for j in range(4)]
        shades = set(standard_shades(0, self.match) + standard_shades(1, self.match))
        for j in range(4):
            for tri in [(circle(0), q[j], q[(j + 1) % 4]),
                        (circle(1), q[(j + 1) % 4], q[j])]:
                self.faces.append(('S' if cyc(tri) in shades else 'W', tri, 0))
        assert sum(f[0] == 'S' for f in self.faces) == 4
        self.validate_sphere()

    def join(self, a, b):
        assert a != b and a not in self.match and b not in self.match
        self.match[a] = b; self.match[b] = a

    def vertex(self, a):
        return main_vertex(a, self.match[a])

    def insert(self, v, w, side, half_w, edge_w):
        shift = (edge_w + 3 + 2 * half_w) % 4
        u = [(w, (j + shift) % 4) for j in range(4)]
        if side == 'right':
            vfirst, vsecond = (v, 1), (v, 2)
            wfirst, wsecond, outfirst, outsecond = u[1], u[0], u[2], u[3]
        else:
            vfirst, vsecond = (v, 3), (v, 0)
            wfirst, wsecond, outfirst, outsecond = u[3], u[2], u[0], u[1]
        xfirst, xsecond = self.match[vfirst], self.match[vsecond]
        oldC, oldB = self.vertex(vfirst), self.vertex(vsecond)
        assert oldC != oldB
        oldface = cyc((circle(v), oldC, oldB))
        owners = [owner for color, face, owner in self.faces
                  if color == 'S' and cyc(face) == oldface]
        assert len(owners) == 1
        for a in [vfirst, vsecond, xfirst, xsecond]:
            del self.match[a]
        self.join(vfirst, wfirst); self.join(vsecond, wsecond)
        self.join(outfirst, xfirst); self.join(outsecond, xsecond)
        D, A = self.vertex(vfirst), self.vertex(vsecond)
        C, B = self.vertex(outfirst), self.vertex(outsecond)
        rename = {oldC: C, oldB: B}
        kept = []
        for color, face, owner in self.faces:
            if color == 'S' and cyc(face) == oldface:
                continue
            kept.append((color, tuple(rename.get(z, z) for z in face), owner))
        self.faces = kept
        newowner = len(self.cell_edges)
        self.cell_edges.append((v, w)); self.cell_dual.append((owners[0], newowner))
        q = [A, B, C, D]
        shades = {cyc((circle(v), B, C)), cyc((circle(v), D, A)),
                  cyc((circle(w), D, C)), cyc((circle(w), B, A))}
        glued = cyc((circle(v), B, C))
        for j in range(4):
            for tri in [(circle(v), q[j], q[(j + 1) % 4]),
                        (circle(w), q[(j + 1) % 4], q[j])]:
                if cyc(tri) == glued:
                    continue
                self.faces.append(('S' if cyc(tri) in shades else 'W', tri, newowner))
        self.merge_whites()
        self.pages[v] += 1; self.pages[w] = 1
        if side == 'right':
            self.sectors[v].insert(0, (v, w))
        else:
            self.sectors[v].append((v, w))
        self.sectors[w] = [(v, w)]
        self.validate_sphere()

    def merge_whites(self):
        while True:
            edges = defaultdict(list)
            for i, (color, face, _) in enumerate(self.faces):
                if color != 'W':
                    continue
                for a, b in zip(face, face[1:] + face[:1]):
                    edges[tuple(sorted((a, b)))].append((i, a, b))
            pair = next((entries for entries in edges.values() if len(entries) == 2), None)
            if pair is None:
                return
            (i, a, b), (j, c, d) = pair
            assert i != j and (c, d) == (b, a)
            f, g = self.faces[i][1], self.faces[j][1]
            k, l = f.index(b), g.index(a)
            pf, pg = f[k:] + f[:k], g[l:] + g[:l]
            assert pf[-1] == a and pg[-1] == b
            merged = pf + pg[1:-1]
            assert len(merged) == len(set(merged))
            self.faces = [x for t, x in enumerate(self.faces) if t not in (i, j)]
            self.faces.append(('W', merged, -1))

    def validate_sphere(self):
        vertices = {v for _, face, _ in self.faces for v in face}
        edges = defaultdict(list)
        for _, face, _ in self.faces:
            for a, b in zip(face, face[1:] + face[:1]):
                edges[tuple(sorted((a, b)))].append((a, b))
        assert all(len(ds) == 2 and ds[0] == ds[1][::-1] for ds in edges.values())
        assert len(vertices) - len(edges) + len(self.faces) == 2
        assert sum(color == 'S' for color, _, _ in self.faces) == 2 * len(self.pages)

    def check(self, expression, LiteralWires, signs):
        expected, pairs = literal(expression, LiteralWires)
        actual = sorted((color, cyc(face)) for color, face, _ in self.faces)
        assert actual == expected
        assert {(a, b) for a, b in self.match.items()} == pairs
        # Also compare the oppositely oriented projection copy, retaining labels.
        assert sorted((c, cyc(f[::-1])) for c, f in actual) == sorted(
            (c, cyc(f[::-1])) for c, f in expected)
        # The distinguished disk seam is retained once per circle. New cell
        # interfaces are untwisted; their actual face labels remain unchanged.
        shades = {(c, f) for c, f in actual if c == 'S'}
        for v in self.pages:
            first, second = standard_shades(v, self.match)
            assert ('S', first) in shades and ('S', second) in shades
            assert signs[v] in (-1, 0, 1)
        # Match the actual two projection-copy disk identifications, not
        # merely the number of shaded faces. Opposite signs share the odd
        # permutation but retain distinct meridian words in exact_algebra.
        def disk_identifications(fs, matching):
            fs = set(fs)
            records = []
            for v, eps in signs.items():
                if (v, 0) not in matching:
                    continue
                q = [main_vertex((v, j), matching[(v, j)]) for j in range(4)]
                o = circle(v)
                assert ('S', cyc((o, q[1], q[2]))) in fs
                assert ('S', cyc((o, q[3], q[0]))) in fs
                if eps == 0:
                    for copy in ('+', '-'):
                        records.append((v, eps, copy, copy,
                                        ((o, o), (q[1], q[0]), (q[2], q[3]))))
                else:
                    records.append((v, eps, '+', '-',
                                    ((o, o), (q[1], q[3]), (q[2], q[0]))))
                    records.append((v, eps, '+', '-',
                                    ((o, o), (q[3], q[1]), (q[0], q[2]))))
            return records
        assert disk_identifications(actual, self.match) == disk_identifications(
            expected, dict(pairs))
        assert len(self.cell_dual) == len(self.cell_edges) - 1
        degree = defaultdict(int)
        for a, b in self.cell_edges:
            degree[a] += 1; degree[b] += 1
        assert dict(degree) == self.pages
        return len(actual)


def run_case(config, LiteralWires):
    full_left, full_right, half, edge, signs, rootside = config
    count = len(half)
    left = {v: [] for v in range(count)}
    right = {v: [] for v in range(count)}
    (left if rootside == 'left' else right)[0] = [1]
    model = OctahedronModel(rootside, half[1], edge[1])
    face_total = model.check(build(0, left, right, half, edge), LiteralWires, signs)
    snapshots = 1; insertions = []
    def check_page_order():
        parent = {}
        for v, ws in left.items():
            for w in ws + right[v]:
                parent[w] = v
        for v in model.pages:
            expected = [(v, w) for w in right[v]]
            if v in parent:
                expected += [(parent[v], v)]
            expected += [(v, w) for w in left[v]]
            assert model.sectors[v] == expected
    check_page_order()
    def visit(v):
        nonlocal face_total, snapshots
        schedule = [(w, 'right') for w in reversed(full_right[v])]
        schedule += [(w, 'left') for w in full_left[v]]
        for w, side in schedule:
            if v == 0 and w == 1:
                continue
            model.insert(v, w, side, half[w], edge[w])
            if side == 'right':
                right[v].insert(0, w)
            else:
                left[v].append(w)
            face_total += model.check(build(0, left, right, half, edge), LiteralWires, signs)
            snapshots += 1; insertions.append((v, w, side))
            check_page_order()
        for w in full_left[v] + full_right[v]:
            visit(w)
    visit(0)
    assert left == full_left and right == full_right
    # Independently retain the physical root half-turn in the closed adapter.
    E = turn(build(1, left, right, half, edge), edge[1])
    P0 = turn(('h', 0), 3)
    original = product([turn(P0), turn(E)])
    adapted = product([P0, turn(E, 2)])
    assert literal(original, LiteralWires) == literal(adapted, LiteralWires)
    return {'circles': count, 'octahedra_per_copy': count - 1,
            'root_side': rootside, 'half_turns': sum(half.values()),
            'inverse_edge_frames': sum(k == 3 for k in edge.values()),
            'left_insertions': sum(s == 'left' for _, _, s in insertions),
            'right_insertions': sum(s == 'right' for _, _, s in insertions),
            'snapshots': snapshots, 'colored_faces_compared': face_total,
            'distinguished_signed_seams': dict(signs)}


def exact_algebra():
    import sympy as s
    E, R, Z = s.symbols('E R Z')
    relation = Z * (1 + E - Z) / E
    W = [s.diag(1, E), s.Matrix([[1, E-1], [0, E]]),
         s.Matrix([[E-R, R*(1-E)], [E-1, 1-E*R]]),
         s.Matrix([[R, 0], [1-E, E*R]])]
    A = s.Matrix([[R, -R], [1, E*R-1-E]])
    B = s.Matrix([[R/E-1-1/E, R], [-1, R]])
    S = s.Matrix([[0, -E*R], [1, -1-E]])
    checks = []
    def zero(name, v):
        assert s.simplify(s.factor(v)) == 0, (name, s.factor(v))
        checks.append(name)
    for i, j, scalar in [(0, 2, -R/E), (2, 0, -R/E), (1, 3, (R-1)/E)]:
        mat = W[i].inv() * B * W[j].inv() * A - scalar * s.eye(2)
        for a in range(2):
            for b in range(2):
                zero(f'odd_edge_{i}_{j}_entry_{a}_{b}', mat[a, b])
    for name, mat in [('A', A), ('B', B)]:
        image = (mat[0, 0]*Z+mat[0, 1])/(mat[1, 0]*Z+mat[1, 1])
        zero(f'{name}_apex', (image-Z/E).subs(R, relation))
    rho = Z/(1+E-Z); Q = (E-Z)/(Z-1)
    for name, mat, desired in [('pure', S.inv(), rho),
                               ('negative', A.inv()*W[0], rho*Q),
                               ('positive', W[0].inv()*B, rho/Q),
                               ('longitude', W[2].inv()*W[0], Q**2)]:
        fixed = (mat[0, 0]*Z+mat[0, 1])/(mat[1, 0]*Z+mat[1, 1])
        zero(name+'_fixed_flag', (fixed-Z).subs(R, relation))
        multiplier = (mat[1, 0]*Z+mat[1, 1])**2/mat.det()
        zero(name+'_multiplier', (multiplier-desired).subs(R, relation))
    x, y, c, p, eps, D = s.symbols('x y c p eps D', real=True)
    tau = x+s.I*y; n = eps-2*p
    psider = s.I*c-s.I*n*tau/(2*s.pi)
    pureU = -2*s.pi*psider
    U = pureU-s.I*eps*tau; V=2*s.I*tau
    zero('primitive_charge_equation', U+p*V+2*s.pi*s.I*c)
    Phi_minus_C = -tau*psider-s.I*eps*tau**2/(4*s.pi)-s.I*n*tau**2/(4*s.pi)+s.I*c*tau
    zero('Legendre_difference', Phi_minus_C+s.I*p*tau**2/(2*s.pi))
    zero('boundary_regulator', s.re(U)*s.im(V)/2-p*s.im(tau**2))
    zero('absolute_volume_cancellation', 2*s.pi*s.re(Phi_minus_C)-s.re(U)*s.im(V)/2)
    cot = 1/D
    cusp = 2*s.I*cot/(1-s.I*eps*cot)
    L2 = s.expand_complex((1+p*cusp)*s.conjugate(1+p*cusp))/s.im(cusp)
    zero('normalized_slope_length', L2-(D**2+n**2)/(2*D))
    zero('threshold_reciprocal', 1/(2*((D**2+n**2)/(2*D)))-D/(D**2+n**2))
    return checks


def cases():
    rng = random.Random(20261101)
    result = []
    for count in range(2, 10):
        for trial in range(16):
            left = {v: [] for v in range(count)}
            right = {v: [] for v in range(count)}
            rootside = 'left' if trial % 2 else 'right'
            (left if rootside == 'left' else right)[0] = [1]
            for w in range(2, count):
                # Include deep chains, stars, and arbitrary branched trees.
                parent = 1 if trial < 4 else (w-1 if trial < 8 else rng.randrange(1, w))
                side = (left if rng.randrange(2) else right)[parent]
                side.insert(rng.randrange(len(side)+1), w)
            half = {v: rng.randrange(2) for v in range(count)}
            edge = {v: (3 if rng.randrange(2) else 1) for v in range(1, count)}
            signs = {v: (-1, 0, 1)[(v+trial) % 3] for v in range(count)}
            result.append((left, right, half, edge, signs, rootside))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--output', type=Path,
                    default=Path(__file__).with_name('ordered_octahedron_pages_results.json'))
    args = ap.parse_args()
    sys.path.insert(0, str(args.repo/'experiments'))
    from audit_actual_conway_bowtie_projection_cut import LiteralWires
    records = [run_case(config, LiteralWires) for config in cases()]
    algebra = exact_algebra()
    data = {
        'status': 'passed',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'exact finite permutations, combinatorial cell gluing, and SymPy rational identities',
        'scope': 'Finite ordered circle trees only; independent colored octahedron attachment versus the existing literal bowtie compiler. Actual T inverse uses three rotations and physical half-turn decorations are retained. No analytic or general topological theorem is inferred from these cases.',
        'topology_counts': {
            'trees': len(records), 'circle_range': [2, 9],
            'attachment_steps': sum(x['snapshots']-1 for x in records),
            'intermediate_spheres': sum(x['snapshots'] for x in records),
            'colored_face_cycles': sum(x['colored_faces_compared'] for x in records),
            'physical_root_adapter_checks': len(records),
            'left_insertions': sum(x['left_insertions'] for x in records),
            'right_insertions': sum(x['right_insertions'] for x in records),
            'distinguished_seams_final': sum(x['circles'] for x in records),
            'signed_disk_face_identifications_final': 2*sum(x['circles'] for x in records),
            'ordered_page_list_snapshots': sum(x['snapshots'] for x in records)},
        'exact_algebra_count': len(algebra), 'exact_algebra_checks': algebra,
        'unproved_by_runner': ['arbitrary-tree induction', 'existence of the analytic charge path',
                              'uniform complex Gaussian or charge estimates',
                              'geometric completeness or the invariant volume limit'],
        'literal_compiler_sha256': hashlib.sha256((args.repo/'experiments/audit_actual_conway_bowtie_projection_cut.py').read_bytes()).hexdigest(),
        'cases': records}
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': data['status'], **data['topology_counts'],
                      'exact_algebra_checks': len(algebra)}, sort_keys=True))


if __name__ == '__main__':
    main()
