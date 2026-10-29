#!/usr/bin/env python3
"""Exact face/parity/TU checks for the original one-component routing polytope."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def physical_visits(width, word):
    """Follow original strands through the checked crossing permutation."""
    active = list(range(width))
    successor, count = {}, width
    for j, letter in enumerate(word):
        p, sigma = abs(letter)-1, 1 if letter > 0 else -1
        a, b = active[p:p+2]
        c, e = count, count+1
        count += 2
        successor[a] = (e, j, -sigma)
        successor[b] = (c, j, sigma)
        active[p:p+2] = [c, e]
    for i, node in enumerate(active):
        successor[node] = (i, None, 0)
    visits, node, seen = [], 0, set()
    while node not in seen:
        seen.add(node)
        node, crossing, increment = successor[node]
        if crossing is not None:
            visits.append((crossing, increment))
    assert node == 0 and len(seen) == count
    assert len(visits) == 2*len(word)
    return visits


def source_data(width, word):
    visits = physical_visits(width, word)
    D = len(word)+1
    current = [1]+[0]*(D-1)
    heads, exponents = [], []
    for i, (crossing, eta) in enumerate(visits):
        heads.append(tuple(current))
        exponents.append(visits[i-1][1]-eta)
        current[crossing+1] += eta
    assert current == [1]+[0]*(D-1)
    units = [tuple(int(i == j) for i in range(D)) for j in range(1, D)]
    rows = list(dict.fromkeys(heads+units))
    vertices = [v for v in itertools.product((0, 1), repeat=D)
                if all(0 <= dot(a, v) <= 1 for a in rows)]
    constraints = [(0, a) for a in rows]+[(1, tuple(-x for x in a)) for a in rows]
    # Each constraint is b+a.y>=0. All are integer physical bounds.
    zeros = [sum(1 << i for i, v in enumerate(vertices) if b+dot(a, v) == 0)
             for b, a in constraints]
    full = (1 << len(vertices))-1
    faces, frontier = {full}, [full]
    while frontier:
        old = frontier.pop()
        for zero in zeros:
            new = old & zero
            if new and new not in faces:
                faces.add(new)
                frontier.append(new)
    return D, heads, exponents, rows, vertices, constraints, faces, full


def primitive_outward(q, normals):
    """Integer witness with a selected primitive inward normal g.v=-1."""
    D = len(q)
    chosen = None
    for g in normals:
        pivot = next(i for i, a in enumerate(g) if a)
        # Positive parallel is the sole excluded halfspace configuration.
        parallel = all(q[j]*g[pivot] == q[pivot]*g[j] for j in range(D))
        if not parallel or q[pivot]*g[pivot] < 0:
            chosen = (g, pivot, parallel)
            break
    assert chosen is not None
    g, pivot, parallel = chosen
    assert abs(g[pivot]) == 1
    v0 = [0]*D
    v0[pivot] = -g[pivot]
    kernel = []
    for j in range(D):
        if j == pivot:
            continue
        w = [0]*D
        w[j], w[pivot] = 1, -g[j]*g[pivot]
        kernel.append(w)
    wpos = [0]*D
    if not parallel:
        wpos = next(w for w in kernel if dot(q, w))
        if dot(q, wpos) < 0:
            wpos = [-x for x in wpos]
    count = len(normals)*max(1, D-1)+1
    perturbations = [[sum((t**(j+1))*w[i] for j, w in enumerate(kernel))
                      for i in range(D)] for t in range(1, count+1)]
    multiplier = 0 if parallel else 1+max(0, -min(dot(q, [v0[i]+p[i] for i in range(D)])
                                               for p in perturbations))
    for perturbation in perturbations:
        v = tuple(v0[i]+multiplier*wpos[i]+perturbation[i] for i in range(D))
        if dot(q, v) > 0 and all(dot(a, v) for a in normals):
            assert dot(g, v) == -1
            return g, v
    raise AssertionError('finite hyperplane avoidance failed')


def factorial_action(y, heads, exponents):
    def I(s):
        if s == int(s):
            return mp.mpf(0)
        return -mp.im(mp.polylog(2, mp.exp(2j*mp.pi*s)))/(2*mp.pi)
    return sum(c*I(dot(h, y)) for c, h in zip(exponents, heads))-sum(I(a) for a in y[1:])


def audit_case(width, word):
    D, heads, cs, rows, vertices, constraints, faces, full = source_data(width, word)
    # Exhaust all full-rank-sized minors for these small actual source matrices.
    minors = 0
    for chosen in itertools.combinations(rows, D):
        det = int(sp.Matrix(chosen).det())
        assert det in (-1, 0, 1)
        minors += 1
    outward, transfer_faces, only_heads, examples = 0, 0, 0, []
    for mask in sorted(faces):
        if mask == full:
            continue
        vs = [v for i, v in enumerate(vertices) if mask >> i & 1]
        normals = list(dict.fromkeys(a for b, a in constraints
                                    if all(b+dot(a, v) == 0 for v in vs)))
        active_h = [i for i, h in enumerate(heads)
                    if len({dot(h, v) for v in vs}) == 1 and dot(h, vs[0]) in (0, 1)]
        active_k = [j for j in range(1, D)
                    if len({v[j] for v in vs}) == 1]
        q = tuple(sum(cs[i]*heads[i][j] for i in active_h)-int(j in active_k)
                  for j in range(D))
        assert any(q)
        if active_k:
            assert all(q[j] % 2 for j in active_k)
            transfer_faces += 1
        else:
            only_heads += 1
            expected = [0]*D
            for i in active_h:
                h, value = heads[i], dot(heads[i], vs[0])
                assert cs[i] == (-2 if value == 0 else 2)
                inward = h if value == 0 else tuple(-x for x in h)
                expected = [a-2*b for a, b in zip(expected, inward)]
            assert tuple(expected) == q
        g, v = primitive_outward(q, normals)
        assert dot(g, v) == -1 and dot(q, v) > 0
        outward += 1
        # Keep bounded witnesses for independent analytic phase diagnostics.
        if len(examples) < 4 and max(map(abs, v)) < 10000:
            barycenter = tuple(mp.mpf(sum(w[j] for w in vs))/len(vs) for j in range(D))
            scale = max(map(abs, v))
            direction = tuple(mp.mpf(a)/scale for a in v)
            leading = mp.mpf(dot(q, v))/scale
            base = factorial_action(barycenter, heads, cs)
            residuals = []
            for exponent in (30, 60):
                delta = mp.exp(-exponent)
                point = tuple(a+delta*b for a, b in zip(barycenter, direction))
                difference = factorial_action(point, heads, cs)-base
                residuals.append(abs(difference/(delta*mp.log(delta))-leading))
            assert residuals[1] <= residuals[0]*mp.mpf('.7')+mp.mpf('1e-18')
            examples.append(dict(face_vertex_count=len(vs), q=list(q),
                                 primitive_outward=list(v), selected_normal=list(g),
                                 logarithmic_asymptotic_errors=[float(a) for a in residuals]))
    return dict(width=width, word=list(word), source_dimension=D,
                binary_vertices=len(vertices), proper_faces=outward,
                transfer_endpoint_faces=transfer_faces, head_only_faces=only_heads,
                exact_maximal_minor_checks=minors, phase_examples=examples)


def main():
    mp.mp.dps = 90
    words = [(2, [1]), (2, [1, 1, 1]), (2, [-1, -1, -1]),
             (3, [1, -2, 1, -2]), (3, [-1, 2, -1, 2]),
             (4, [1, 2, 3]), (4, [1, -2, 1, -2, 3])]
    rows = [audit_case(width, word) for width, word in words]
    result = dict(status='PASS', original_signed_routing_cases=rows,
                  scope='Exact face and source-lattice assertions plus local radial action diagnostics; no global contour or knot-volume bound.')
    Path(__file__).with_name('actual_physical_face_outward_action_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', actual_signed_words=len(rows),
                          physical_faces=sum(r['proper_faces'] for r in rows),
                          exact_maximal_minors=sum(r['exact_maximal_minor_checks'] for r in rows),
                          phase_diagnostics=sum(len(r['phase_examples']) for r in rows))))


if __name__ == '__main__':
    main()
