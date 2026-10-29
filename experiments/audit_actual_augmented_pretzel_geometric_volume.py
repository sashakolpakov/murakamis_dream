#!/usr/bin/env python3
"""Independent right-antiprism geometry and literal pretzel face gluings.

No hyperbolic census or imported volume-conjecture proof. The face labels
record the exact projection-plane/half-twist changes of the source graph.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp


class UF:
    def __init__(self, labels):
        self.p = {a: a for a in labels}

    def find(self, a):
        if self.p[a] != a:
            self.p[a] = self.find(self.p[a])
        return self.p[a]

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)

    def groups(self):
        out = {}
        for a in self.p:
            out.setdefault(self.find(a), []).append(a)
        return list(out.values())


def face_data(s):
    z = lambda k: ('z', 0, k % s)
    u = lambda sign, k: ('u', sign, k % s)
    faces = {'Wp': [u(1, k) for k in reversed(range(s))],
             'Wm': [u(-1, k) for k in range(s)]}
    for k in range(s):
        faces[f'Q{k}'] = [z(k), u(1, k), z(k+1), u(-1, k)]
        faces[f'Tp{k}'] = [z(k), u(1, k-1), u(1, k)]
        faces[f'Tm{k}'] = [z(k), u(-1, k), u(-1, k-1)]
    edges = {}
    for name, cycle in faces.items():
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            key = tuple(sorted((a, b)))
            edges.setdefault(key, []).append((name, a, b))
    assert len(edges) == 6*s
    assert all(len(v) == 2 and v[0][1:] == tuple(reversed(v[1][1:])) for v in edges.values())
    vertices = sorted(set(a for cycle in faces.values() for a in cycle))
    assert len(vertices) == 3*s and len(faces) == 3*s+2
    return faces, edges, vertices


def is_cyclic_equal(a, b):
    return any(a == b[k:]+b[:k] for k in range(len(b)))


def main_component_count(s, half):
    n = 2*s
    matching = {}
    for a, b in [(0, n-1)]+[(2*k-1, 2*k) for k in range(1, s)]:
        matching[a], matching[b] = b, a
    swap = lambda a: (a ^ 1) if half[a//2] else a
    upper = {swap(a): swap(b) for a, b in matching.items()}
    U = UF(range(n))
    for a in range(n):
        U.union(a, matching[a])
        U.union(a, upper[a])
    return len(U.groups())


def gluing_case(s, half):
    faces, edges, vertices = face_data(s)
    V = UF([(p, a) for p in (0, 1) for a in vertices])
    E = UF([(p, e) for p in (0, 1) for e in edges])
    corners = [(p, a, e) for p in (0, 1) for e in edges for a in e]
    L = UF(corners)
    pairs = []
    for name in ['Wp', 'Wm']+[f'Q{k}' for k in range(s)]:
        pairs.append((0, name, 1, name, {a: a for a in faces[name]}))
    for k in range(s):
        for p in (0, 1):
            target = 1-p if half[k] else p
            vertexmap = {('z', 0, k): ('z', 0, k)}
            for j in ((k-1) % s, k):
                dest = ((2*k-1-j) % s) if half[k] else j
                vertexmap[('u', 1, j)] = ('u', -1, dest)
            pairs.append((p, f'Tp{k}', target, f'Tm{k}', vertexmap))
    used = []
    for p, name, target, targetname, mapping in pairs:
        used += [(p, name), (target, targetname)]
        sourcecycle = faces[name] if p == 0 else list(reversed(faces[name]))
        targetcycle = faces[targetname] if target == 0 else list(reversed(faces[targetname]))
        image = [mapping[a] for a in sourcecycle]
        assert is_cyclic_equal(image, list(reversed(targetcycle)))
        for a in faces[name]:
            V.union((p, a), (target, mapping[a]))
        cycle = faces[name]
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            e, ee = tuple(sorted((a, b))), tuple(sorted((mapping[a], mapping[b])))
            E.union((p, e), (target, ee))
            for endpoint in (a, b):
                L.union((p, endpoint, e), (target, mapping[endpoint], ee))
    assert len(used) == len(set(used)) == 2*len(faces)
    assert all(len(g) == 4 for g in E.groups())
    assert all(len(g) == 4 for g in L.groups())
    cusp_faces, cusp_vertices = {}, {}
    for p in (0, 1):
        for a in vertices:
            root = V.find((p, a))
            cusp_faces[root] = cusp_faces.get(root, 0)+1
    for group in L.groups():
        p, a, edge = group[0]
        root = V.find((p, a))
        cusp_vertices[root] = cusp_vertices.get(root, 0)+1
    assert set(cusp_faces) == set(cusp_vertices)
    # Every cusp link is made of F rectangles, E=2F paired sides,
    # and V=F corners of angle 2pi: Euler characteristic zero.
    assert all(cusp_vertices[root] == F for root, F in cusp_faces.items())
    main = main_component_count(s, half)
    assert len(V.groups()) == s+main
    if not any(half):
        assert main == s
    if all(half):
        assert main == (1 if s % 2 else 2)
    return {'s': s, 'half_twists': list(half), 'circle_cusps': s,
            'main_cusps': main, 'four_right_angles_per_edge': True,
            'oriented_face_gluings_and_flat_torus_links': True}


def lorentz(a, b):
    return -a[0]*b[0]+sum(a[k]*b[k] for k in range(1, 4))


def lobachevsky(theta):
    return mp.im(mp.polylog(2, mp.exp(2j*theta)))/2


def bloch(z):
    return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)


def geometric_case(s):
    mp.mp.dps = 80
    alpha = mp.pi/s
    h = mp.tan(alpha/2)
    r = mp.sqrt(1-h*h)
    b = r*(1-mp.cos(alpha))/(2*h)
    c = r*(1+mp.cos(alpha))/2
    upper = [c, mp.cos(alpha), mp.sin(alpha), b]
    lower = [c, 1, 0, -b]
    top = [h, 0, 0, 1]
    assert abs(lorentz(upper, lower)) < mp.mpf('1e-70')
    assert abs(lorentz(upper, top)) < mp.mpf('1e-70')
    assert lorentz(upper, upper) > 0 and lorentz(top, top) > 0
    vertices = [(r*mp.cos(2*k*alpha), r*mp.sin(2*k*alpha), h) for k in range(s)]
    vertices += [(r*mp.cos((2*k+1)*alpha), r*mp.sin((2*k+1)*alpha), -h) for k in range(s)]
    for X, Y, Z in vertices:
        assert abs(X*X+Y*Y+Z*Z-1) < mp.mpf('1e-70')
        assert mp.cos(alpha)*X+mp.sin(alpha)*Y+b*Z <= c+mp.mpf('1e-70')
    t = mp.tan(mp.pi/4-alpha/2)
    rho = 1/mp.sqrt(t)
    shape1 = (rho**(-2)-mp.exp(-1j*alpha))/(mp.exp(1j*alpha)-mp.exp(-1j*alpha))
    shape2 = (rho**2-mp.exp(-1j*alpha))/(mp.exp(1j*alpha)-mp.exp(-1j*alpha))
    assert abs(shape1-(mp.mpf('.5')+1j*t/2)) < mp.mpf('1e-70')
    assert abs(shape2-(mp.mpf('.5')-1j/(2*t))) < mp.mpf('1e-70')
    beta_plus, beta_minus = mp.pi/4+alpha/2, mp.pi/4-alpha/2
    assert abs(bloch(shape1)-2*lobachevsky(beta_plus)) < mp.mpf('1e-65')
    assert abs(-bloch(shape2)-2*lobachevsky(beta_minus)) < mp.mpf('1e-65')
    antiprism = s*(bloch(shape1)-bloch(shape2))
    formula = 2*s*(lobachevsky(beta_plus)+lobachevsky(beta_minus))
    assert abs(antiprism-formula) < mp.mpf('1e-65')
    if s == 3:
        assert abs(antiprism-8*lobachevsky(mp.pi/4)) < mp.mpf('1e-65')
    return {'s': s, 'explicit_ideal_right_angle_and_support_tests': True,
            'volume_from_oriented_side_tetrahedra': mp.nstr(4*antiprism, 25),
            'antiprism_count': 4, 'formula_checked': True}


if __name__ == '__main__':
    gluings = []
    for s in range(3, 9):
        for half in itertools.product((0, 1), repeat=s):
            gluings.append(gluing_case(s, half))
    for s in range(9, 21):
        for half in ((0,)*s, (1,)*s, tuple(k % 2 for k in range(s))):
            gluings.append(gluing_case(s, half))
    results = {'status': 'PASS', 'geometric_antiprisms': [geometric_case(s) for s in range(3, 21)],
               'literal_half_twist_face_pairings': gluings,
               'scope': 'Exact geometric RHS for the unfilled augmented source; no quantum asymptotics or fixed-knot filling claim.'}
    Path(__file__).with_name('actual_augmented_pretzel_geometric_volume_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print(f'PASS 18 explicit antiprism/volume families; {len(gluings)} literal oriented half-twist face/cusp gluings')
