#!/usr/bin/env python3
"""Degenerate source angles, nonattained capacity and actual block development."""
import argparse
from collections import defaultdict
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import linprog, root


def rows(triangles, marked):
    faces = sorted(set(f for t in triangles for f in t)-set(marked))
    corners = [(i, j) for i, t in enumerate(triangles) for j, f in enumerate(t) if f not in marked]
    A = np.zeros((len(triangles)+len(faces), len(corners)))
    for k, (i, j) in enumerate(corners):
        A[i, k] = 1
        A[len(triangles)+faces.index(triangles[i][j]), k] = 1
    return faces, corners, A, np.array([1.]*len(triangles)+[2.]*len(faces))


def degenerate_angles():
    base = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    checks = loops = 0
    for inner in ([(2, 3, 4)]*2,
                  [(2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]):
        for level in range(4):
            if level:
                t = inner.pop()
                v = max(f for row in inner+[t] for f in row)+1
                inner += [(t[0], t[1], v), (t[1], t[2], v), (t[2], t[0], v)]
            tri = base+inner
            faces, corners, A, rhs = rows(tri, (0, 1))
            objective = np.array([-1. if i >= len(base) and tri[i][j] in (2, 3) else 0.
                                  for i, j in corners])
            lp = linprog(objective, A_eq=A, b_eq=rhs, bounds=(0, None), method='highs')
            assert lp.success and abs(lp.fun) < 1e-10
            # Independently solve the inner and outer demand systems.
            for part, marks in ((base, (0, 1)), (inner, (2, 3))):
                ff, cc, AA, rr = rows(part, marks)
                sub = linprog(np.zeros(len(cc)), A_eq=AA, b_eq=rr,
                              bounds=(0, None), method='highs')
                assert sub.success
            checks += 1
    # Genuine one-loop spherical triangular cellulations, with a mark-free side.
    inside = [(0, 0, 2)]
    outside = [(0, 0, 3), (0, 1, 3), (1, 0, 3)]
    for level in range(5):
        if level:
            t = inside.pop()
            v = 3+level
            inside += [(t[0], t[1], v), (t[1], t[2], v), (t[2], t[0], v)]
        interior = set(f for t in inside for f in t)-{0}
        assert len(inside) == 2*len(interior)-1
        ff, cc, A, rhs = rows(inside+outside, (0, 1))
        lp = linprog(np.zeros(len(cc)), A_eq=A, b_eq=rhs, bounds=(0, None), method='highs')
        assert not lp.success
        loops += 1
    return {'digon_zero_boundary_LP_and_factor_systems': checks,
            'genuine_loop_cellulations_infeasible': loops}


def spheres():
    tetra = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    yield 'tetrahedron', tetra
    for n in (4, 5, 6):
        yield f'bipyramid_{n}', [(p, j, (j+1)%n) for p in (n, n+1) for j in range(n)]
    tri = tetra[:]
    for v in range(4, 7):
        t = tri.pop()
        tri += [(t[0], t[1], v), (t[1], t[2], v), (t[2], t[0], v)]
        yield f'stacked_{v-3}', tri[:]


def hall_checks():
    cuts = assignments = diskcuts = diskassignments = 0
    for name, tri in spheres():
        edges = sorted({tuple(sorted((t[j], t[(j+1)%3]))) for t in tri for j in range(3)})
        for marked in (edges[0], edges[len(edges)//2], edges[-1]):
            faces, corners, A, rhs = rows(tri, marked)
            for size in range(1, len(faces)):
                for subset in itertools.combinations(faces, size):
                    touch = sum(bool(set(t)&set(subset)) for t in tri)
                    assert touch >= 2*size+1, (name, marked, subset)
                    cuts += 1
            eps = 1/(12*len(tri))
            lp = linprog(np.zeros(len(corners)), A_eq=A, b_eq=rhs,
                         bounds=(eps, None), method='highs')
            assert lp.success
            assignments += 1
        boundary = set(tri[0])
        disk = tri[1:]
        interior = sorted(set(f for t in disk for f in t)-boundary)
        destinations = interior+['boundary']
        labels = [tuple(f if f in interior else 'boundary' for f in t) for t in disk]
        demands = {f: 2 for f in interior} | {'boundary': 1}
        for size in range(1, len(destinations)):
            for subset in itertools.combinations(destinations, size):
                touch = sum(bool(set(t)&set(subset)) for t in labels)
                assert touch > sum(demands[f] for f in subset)
                diskcuts += 1
        A = np.zeros((len(disk)+len(destinations), 3*len(disk)))
        for i, row in enumerate(labels):
            for j, f in enumerate(row):
                A[i, 3*i+j] = 1
                A[len(disk)+destinations.index(f), 3*i+j] = 1
        rhs = [1.]*len(disk)+[demands[f] for f in destinations]
        lp = linprog(np.zeros(3*len(disk)), A_eq=A, b_eq=rhs,
                     bounds=(1/(12*len(disk)), None), method='highs')
        assert lp.success
        diskassignments += 1
    return {'strict_planar_Hall_cuts': cuts, 'relative_positive_assignments': assignments,
            'fixed_boundary_disk_Hall_cuts': diskcuts, 'fixed_boundary_positive_assignments': diskassignments}


def angles(L):
    L = np.asarray(L, dtype=float)
    D = np.sqrt(L[0]*L[1]+L[1]*L[2]+L[2]*L[0])
    return 2*np.arctan2(L, D)


def orient_sphere(tri):
    outer = tri[0]
    oriented = {0: (outer[0], outer[2], outer[1])}
    while len(oriented) < len(tri):
        progress = False
        for j, row in enumerate(tri):
            if j in oriented:
                continue
            for old in list(oriented.values()):
                common = set(old)&set(row)
                if len(common) != 2:
                    continue
                a, b = next((old[k], old[(k+1)%3]) for k in range(3)
                            if {old[k], old[(k+1)%3]} == common)
                c = next(f for f in row if f not in common)
                oriented[j] = (b, a, c)
                progress = True
                break
        assert progress
    return [oriented[j] for j in range(len(tri))]


def F(*L):
    L = list(map(mp.mpf, L))
    D = mp.sqrt(L[0]*L[1]+L[1]*L[2]+L[2]*L[0])
    theta = [2*mp.atan2(l, D) for l in L]
    lob = lambda t: mp.im(mp.polylog(2, mp.exp(2j*t)))/2
    V = 2*mp.fsum(lob(t/2)+lob((mp.pi-t)/2) for t in theta)
    return (V+mp.fsum(t*mp.log(l) for t, l in zip(theta, L) if l))/(2*mp.pi)


def packing(tri, boundary_radii):
    boundary = tri[0]
    interior = sorted(set(f for t in tri for f in t)-set(boundary))
    lfixed = {f: 1/r for f, r in zip(boundary, boundary_radii)}
    disk = tri[1:]
    def unpack(z):
        return dict(lfixed, **{}) | {f: np.exp(v) for f, v in zip(interior, z)}
    def gradient(z):
        l = unpack(z)
        result = dict.fromkeys(interior, -2*np.pi)
        for t in disk:
            for f, a in zip(t, angles([l[f] for f in t])):
                if f in result:
                    result[f] += a
        return np.array([result[f] for f in interior])
    sol = root(gradient, np.ones(len(interior)), tol=1e-11)
    assert max(abs(gradient(sol.x))) < 2e-9
    l = unpack(sol.x)
    r = {f: 1/v for f, v in l.items()}
    a, b, c = boundary
    length = r[a]+r[b]
    along = (length*length+(r[a]+r[c])**2-(r[b]+r[c])**2)/(2*length)
    z = {a: 0j, b: complex(length), c: complex(along, np.sqrt((r[a]+r[c])**2-along*along))}
    oriented = orient_sphere(tri)
    while len(z) < len(r):
        progress = False
        for row in oriented[1:]:
            if sum(f in z for f in row) != 2:
                continue
            a, b, c = next(tuple(row[j:]+row[:j]) for j in range(3)
                           if row[j] in z and row[(j+1)%3] in z)
            length = r[a]+r[b]
            along = (length*length+(r[a]+r[c])**2-(r[b]+r[c])**2)/(2*length)
            height = np.sqrt((r[a]+r[c])**2-along*along)
            z[c] = z[a]+(z[b]-z[a])/abs(z[b]-z[a])*(along+1j*height)
            progress = True
        assert progress
    return r, z, oriented, float(max(abs(gradient(sol.x))))


def geometry_and_marking():
    count = distance = shade = right = marked = 0
    worst = gap = 0.
    samples = []
    for name, tri in spheres():
        for boundary in ((1., 1., 1.), (.7, 1.1, 1.4)):
            r, z, oriented, force = packing(tri, boundary)
            worst = max(worst, force)
            edges = sorted({tuple(sorted((t[j], t[(j+1)%3]))) for t in tri for j in range(3)})
            contacts = {e: (r[e[1]]*z[e[0]]+r[e[0]]*z[e[1]])/(r[e[0]]+r[e[1]]) for e in edges}
            for a, b in itertools.combinations(r, 2):
                slack = abs(z[a]-z[b])-r[a]-r[b]
                if tuple(sorted((a, b))) in edges:
                    assert abs(slack) < 1e-7
                    worst = max(worst, abs(slack))
                else:
                    assert slack > 1e-7
                distance += 1
            for j, row in enumerate(oriented):
                a, b, c = row
                lengths = [r[b]+r[c], r[c]+r[a], r[a]+r[b]]
                center = sum(length*z[f] for length, f in zip(lengths, row))/sum(lengths)
                area2 = abs(np.imag((z[b]-z[a])*np.conj(z[c]-z[a])))
                radius = area2/sum(r[f] for f in row)/2
                # area2=2*area, incircle radius=area/semiperimeter.
                for f in row:
                    err = abs(abs(center-z[f])**2-r[f]**2-radius**2)
                    assert err < 1e-7
                    worst = max(worst, err)
                    right += 1
                te = {tuple(sorted((row[k], row[(k+1)%3]))) for k in range(3)}
                for e, p in contacts.items():
                    power = abs(p-center)**2-radius**2
                    if e in te:
                        assert abs(power) < 1e-7
                    elif j == 0:
                        assert power < -1e-8
                    else:
                        assert power > 1e-8
                    shade += 1
            capacities = []
            for edge in (edges[0], edges[len(edges)//2], edges[-1]):
                p = contacts[edge]
                inv = np.array([[-p, 1], [-1, 0]], complex)
                curv = {}
                for f in r:
                    H = np.array([[1, -z[f]], [-np.conj(z[f]), abs(z[f])**2-r[f]**2]], complex)/r[f]
                    moved = inv.conj().T@H@inv
                    value = float(np.real(moved[0, 0]))
                    if f in edge:
                        assert abs(value) < 1e-7
                        curv[f] = 0.
                    else:
                        assert value > 0
                        curv[f] = value
                val = mp.fsum(F(*(curv[f] for f in t)) for t in tri)-mp.fsum(mp.log(v) for v in curv.values() if v)
                capacities.append(val)
                marked += 1
            delta = float(max(capacities)-min(capacities))
            assert delta < 1e-7
            gap = max(gap, delta)
            count += 1
            samples.append({'sphere': name, 'boundary_radii': boundary,
                            'capacity': str(capacities[0]), 'mark_independence_spread': delta})
    return {'actual_developed_disk_packings': count, 'disk_pair_tests': distance,
            'shaded_contact_supports': shade, 'white_shaded_right_angles': right,
            'adjacent_mark_capacity_values': marked,
            'maximum_geometric_residual': worst, 'maximum_mark_spread': gap, 'samples': samples}


def nonattained_capacity():
    outer = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    inner = [(2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    phi = 2*F(0, 1, 1)
    records = []
    previous = mp.inf
    for scale in map(mp.mpf, ('10', '100', '10000', '1000000')):
        l = {0: 0, 1: 0, 2: 1, 3: 1, 4: scale, 5: scale}
        primal = mp.fsum(F(*(l[f] for f in t)) for t in outer+inner)-2*mp.log(scale)
        excess = primal-2*phi
        assert 0 < excess < previous
        previous = excess
        records.append({'scale': str(scale), 'positive_primal_minus_dual': str(excess)})
    assert previous < mp.mpf('.02')
    assert abs(2*F(0, 0, mp.mpf('3.7'))-mp.log(mp.mpf('3.7'))) < mp.mpf('1e-35')
    return {'nonattained_primal_dual_scales': len(records), 'zero_double_triangle': 1,
            'exact_dual_block_capacity': str(2*phi), 'samples': records}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='experiments/actual_smoothed_source_capacity_blocks_results.json')
    args = ap.parse_args()
    mp.mp.dps = 40
    result = {'status': 'PASS', 'degenerate_angles': degenerate_angles(),
              'strict_Hall': hall_checks(), 'geometry': geometry_and_marking(),
              'nonattainment': nonattained_capacity(),
              'scope': 'Actual loop/digon corner systems, exact planar cut counts versus independent LP, developed simple-block packings and all contact supports, adjacent-mark invariance, and a nonattained primal/dual capacity sequence. No finite quantum factorization, JSJ identification or strict opposite-smoothing comparison.'}
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
