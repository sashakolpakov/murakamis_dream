#!/usr/bin/env python3
"""Source-stationary marked patterns versus independently reconstructed collars.

The local collar theorem has its own audit.  Here a common marked pattern
is solved jointly with the source channel equations, then its contact
points determine the collar without using its claimed eigenratio.
"""
import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_marked_deformed_circle_pattern import fixtures
from audit_actual_deformed_circle_primitive_collar import hmove, threaded
from audit_actual_original_marked_face_coefficient import morse_faces


def error(A, B):
    return mp.norm(A-B)/max(1, mp.norm(A), mp.norm(B))


def cyclic(t, seq):
    return any(tuple(t[j:]+t[:j]) == tuple(seq) for j in range(3))


def oriented_triangles(fx):
    """Actual sphere orientation, seeded by a bounded compactified face."""
    low, up = fx['lower'], fx['upper']
    g = mp.matrix([[1, 0], [-mp.mpf('.07'), 1+mp.mpf('.035')*1j]])
    gi = g**-1
    forms = {low: mp.matrix([[0, 1j], [-1j, 0]]),
             up: mp.matrix([[0, -1j], [1j, 2]])}
    for f, (X, Y, r) in fx['circles'].items():
        X, Y, r = map(mp.mpf, (str(X), str(Y), str(r)))
        forms[f] = mp.matrix([[1, -X-1j*Y], [-X+1j*Y, X*X+Y*Y-r*r]])/r
    centers = {}
    for f, H in forms.items():
        H = gi.transpose_conj()*H*gi
        assert mp.re(H[0, 0]) > 0
        centers[f] = -H[0, 1]/H[0, 0]
    triangles = [list(t) for t in fx['triangles']]
    seed = next(j for j, t in enumerate(triangles) if not {low, up}.issubset(t))
    row = triangles[seed]
    area = mp.im((centers[row[1]]-centers[row[0]])*mp.conj(centers[row[2]]-centers[row[0]]))
    # This expression is minus the usual signed area: clockwise is positive.
    if area < 0:
        row[1], row[2] = row[2], row[1]
    out = {seed: row}
    while len(out) < len(triangles):
        progress = False
        for j, t in enumerate(triangles):
            if j in out:
                continue
            for old in out.values():
                common = set(old) & set(t)
                if len(common) != 2:
                    continue
                a, b = next((old[k], old[(k+1)%3]) for k in range(3)
                            if {old[k], old[(k+1)%3]} == common)
                c = next(v for v in t if v not in common)
                out[j] = [b, a, c]
                progress = True
                break
        assert progress
    return [out[j] for j in range(len(triangles))]


def pattern_problem(fx):
    low, up = fx['lower'], fx['upper']
    finite = sorted(fx['circles'])
    triangles = oriented_triangles(fx)
    matching = [tuple(sorted(e)) for e in fx['matching']]
    edges = sorted({tuple(sorted((t[i], t[j]))) for t in triangles
                    for i, j in ((0, 1), (0, 2), (1, 2))})
    edges.remove(tuple(sorted((low, up))))
    keys = [(f, k) for f in finite for k in range(3) if (f, k) != (fx['fixed'], 0)]
    # Reconstruct algebraic complete data, rather than treating binary floats as exact.
    circles = {}
    for f, row in fx['circles'].items():
        circles[f] = [mp.mpf(str(v)) for v in row]
        for k, v in enumerate(row):
            if abs(v-2**.5) < 1e-14:
                circles[f][k] = mp.sqrt(2)
            elif abs(v-2**-.5) < 1e-14:
                circles[f][k] = mp.sqrt(2)/2
    initial = [circles[f][k] for f, k in keys]
    pairs = []
    for x, y in matching:
        adj = [t for t in triangles if {x, y}.issubset(t)]
        assert len(adj) == 2
        b = next(next(f for f in t if f not in (x, y)) for t in adj
                 if cyclic(t, (x, next(f for f in t if f not in (x, y)), y)))
        c = next(f for t in adj for f in t if f not in (x, y, b))
        pairs.append((x, b, c, y))

    def unpack(values):
        obj = {f: row[:] for f, row in circles.items()}
        for (f, k), value in zip(keys, values):
            obj[f][k] = value
        return obj

    def source_ratios(obj, delta):
        l = {low: mp.mpf(0), up: mp.mpf(0)}
        l.update({f: 1/obj[f][2] for f in finite})
        ratios = []
        for (x, b, c, y), de in zip(pairs, delta):
            x, b, c, y = [l[f] for f in (x, b, c, y)]
            s = mp.sin(mp.pi*de)
            A = x+y
            D = A*A-4*x*y*s*s
            E = lambda q: A+2*q*s*s+2*s*mp.sqrt(q*A+x*y+q*q*s*s)
            ratios.append(E(b)*E(c)/D)
        return ratios

    def equations(values, chi, eps):
        obj = unpack(values)
        delta = values[len(keys):]
        result = []
        for f, g in edges:
            e = (f, g)
            I = mp.cos(2*mp.pi*delta[matching.index(e)]) if e in matching else 1
            if f in (low, up) or g in (low, up):
                line = f if f in (low, up) else g
                v = g if line == f else f
                X, Y, r = obj[v]
                result.append(Y-r*I if line == low else 1-Y-r*I)
            else:
                X, Y, r = obj[f]
                Z, W, t = obj[g]
                result.append((X-Z)**2+(Y-W)**2-r*r-t*t-2*I*r*t)
        result.extend(mp.log(R)-2j*mp.pi*e*de-2j*mp.pi*h
                      for R, de, h, e in zip(source_ratios(obj, delta), delta, chi, eps))
        return result

    def reflection(obj, f, plus=True):
        sign = 1 if plus else -1
        if f == low:
            return -sign*1j*mp.eye(2)
        if f == up:
            return sign*1j*mp.matrix([[1, sign*2j], [0, 1]])
        X, Y, r = obj[f]
        cp, cm = X+sign*1j*Y, X-sign*1j*Y
        return mp.matrix([[cp, r*r-cp*cm], [1, -cm]])/r

    def contact(obj, f, g):
        if f in (low, up) and g in (low, up):
            return mp.matrix([1, 0])
        if f in (low, up) or g in (low, up):
            line = f if f in (low, up) else g
            v = g if line == f else f
            return mp.matrix([obj[v][0]+(1j if line == up else 0), 1])
        X, Y, r = obj[f]
        Z, W, t = obj[g]
        return mp.matrix([(t*(X+1j*Y)+r*(Z+1j*W))/(r+t), 1])

    return locals()


def threepoint(v0, v1, vinf):
    B = mp.matrix([[vinf[0], v0[0]], [vinf[1], v0[1]]])
    a, b = B**-1*v1
    return B*mp.diag([a, b])


def geometric_cases():
    patterns = collars = relations = meridians = prefixes = main = 0
    worst = mp.mpf(0)
    records = []
    for fx in fixtures():
        p = pattern_problem(fx)
        R = len(p['matching'])
        for case in range(6):
            eps = [(-1, 0, 1)[(j+case)%3] for j in range(R)]
            chi = [mp.mpf('.0012')*(j+1)*(1+(.3j if case%2 else 0))*(1+case/5)
                   for j in range(R)]
            eq = lambda *v: p['equations'](v, chi, eps)
            values = mp.findroot(eq, tuple(p['initial']+[mp.mpf('.0003')]*(R)),
                                 tol=mp.mpf('1e-42'), maxsteps=20)
            residual = max(abs(v) for v in eq(*values))
            assert residual < mp.mpf('1e-40')
            worst = max(worst, residual)
            obj = p['unpack'](values)
            delta = list(values[len(p['keys']):])
            refl = lambda f, plus=True: p['reflection'](obj, f, plus)
            for f, g in p['edges']:
                if (f, g) in p['matching']:
                    continue
                H = refl(g)*refl(f, False)
                assert abs(mp.det(H)-1) < mp.mpf('1e-38')
                assert abs(H[0, 0]+H[1, 1]+2) < mp.mpf('1e-38')
                main += 1
            for i, (x, b, c, y) in enumerate(p['pairs']):
                Ain, Bin = refl(b)*refl(x, False), refl(y)*refl(b, False)
                Ao, Bo = refl(c)*refl(x, False), refl(y)*refl(c, False)
                P = Bin*Ain
                J = -mp.exp(-2j*mp.pi*delta[i])
                flag = mp.matrix([P[0, 1], J-P[0, 0]]) if abs(P[0, 1]) > abs(P[1, 0]) else mp.matrix([J-P[1, 1], P[1, 0]])
                c1, c2 = p['contact'](obj, x, b), p['contact'](obj, b, y)
                c0, c3 = p['contact'](obj, x, c), p['contact'](obj, c, y)
                C = threepoint(c0, c3, flag)*threepoint(c1, c2, flag)**-1
                # Normalize on the OTHER eigenline, independently of the source ratio.
                other = mp.matrix([P[0, 1], 1/J-P[0, 0]]) if abs(P[0, 1]) > abs(P[1, 0]) else mp.matrix([1/J-P[1, 1], P[1, 0]])
                index = 0 if abs(other[0]) > abs(other[1]) else 1
                C /= (C*other)[index]/other[index]
                index = 0 if abs(flag[0]) > abs(flag[1]) else 1
                Rgeom = (C*flag)[index]/flag[index]
                Rsource = p['source_ratios'](obj, delta)[i]
                for A, B in [(C*Ain*C**-1, Ao), (C*Bin*C**-1, Bo)]:
                    ee = error(A, B)
                    assert ee < mp.mpf('1e-35'), (fx['name'], case, p['pairs'][i], ee)
                    worst = max(worst, ee)
                assert abs(Rgeom/Rsource-1) < mp.mpf('1e-35'), (p['pairs'][i], Rgeom, Rsource)
                collars += 1
                m = mp.exp(-mp.pi*1j*chi[i])
                H = P**-1-mp.eye(2)
                M = m*Rgeom*(1/J-1)**(-eps[i])*C**-1*H**eps[i]
                assert abs(mp.det(M)-1) < mp.mpf('1e-34')
                assert error(M*flag, m*flag) < mp.mpf('1e-34')
                assert abs(2*mp.log((M*flag)[index]/flag[index])+2j*mp.pi*chi[i]) < mp.mpf('1e-34')
                meridians += 1
                ans = threaded(Ain, Bin, M)
                pair = ans[:2]
                if eps[i]:
                    pair = hmove(pair, eps[i])
                for A, B in [(pair[0], Ao), (pair[1], Bo), (ans[2], M)]:
                    ee = error(A, B)
                    assert ee < mp.mpf('1e-33')
                    worst = max(worst, ee)
                    relations += 1
                # Original oriented input/output region paths have the SAME prefix.
                for regions in ((x, b, y), (x, c, y), (x, b, x), (y, c, y)):
                    product = mp.eye(2)
                    for f, g in zip(regions, regions[1:]):
                        product = refl(g)*refl(f, False)*product
                    target = refl(regions[-1])*refl(regions[0], False)
                    assert error(product, target) < mp.mpf('1e-40')
                    prefixes += 1
            patterns += 1
            records.append({'fixture': fx['name'], 'half_twists': eps,
                            'complex_external_parameters': bool(case%2),
                            'maximum_source_stationarity_residual': str(residual)})
    return {'joint_source_stationary_patterns': patterns,
            'independent_contact_point_collars': collars,
            'actual_threading_and_Hurwitz_relations': relations,
            'primitive_auxiliary_eigenlogs': meridians,
            'geometric_main_parabolic_edges': main,
            'original_box_and_cup_prefix_products': prefixes,
            'maximum_relative_error': str(worst), 'samples': records}


def global_morse_words():
    """Literal arbitrary-width region walks; no new geometric certificate claimed."""
    charts = products = cups = untouched = 0
    prime = 1009
    imag = next(n for n in range(prime) if (n*n+1)%prime == 0)
    unit = (1, 0, 0, 1)
    def mul(A, B):
        a, b, c, d = A
        e, f, g, h = B
        return ((a*e+b*g)%prime, (a*f+b*h)%prime,
                (c*e+d*g)%prime, (c*f+d*h)%prime)
    def inv(A):
        a, b, c, d = A
        scale = pow((a*d-b*c)%prime, -1, prime)
        return tuple((scale*v)%prime for v in (d, -b, -c, a))
    for k in (2, 3, 4):
        base = list(range(1, 2*k-1, 2))
        for extra in ([], list(range(2*k-1)), list(reversed(range(2*k-1)))):
            boxes = base+extra+base
            chart = morse_faces(k, boxes)
            reflection = {}
            for f in range(chart['faces']):
                X = f*pow(3, -1, prime)%prime
                Y = (f*f+1)*pow(5, -1, prime)%prime
                r = (f+2)*pow(7, -1, prime)%prime
                reflection[f] = tuple(v*pow(r, -1, prime)%prime
                                      for v in (X+imag*Y, r*r-X*X-Y*Y, 1, -X+imag*Y))
            inverse = {f: inv(A) for f, A in reflection.items()}
            gap = list(chart['bottom'])
            for slot, (x, b, c, y) in zip(boxes, chart['circles']):
                assert tuple(gap[slot:slot+3]) == (x, b, y)
                old = gap[:]
                gap[slot+1] = c
                for j in range(2*k):
                    if j in (slot, slot+1):
                        continue
                    assert gap[j:j+2] == old[j:j+2]
                    untouched += 1
                product = unit
                for j in range(2*k):
                    product = mul(mul(reflection[gap[j+1]], inverse[gap[j]]), product)
                    target = mul(reflection[gap[j+1]], inverse[gap[0]])
                    assert product == target
                    products += 1
            assert gap == chart['top']
            for line in (chart['bottom'], chart['top']):
                for j in range(k):
                    a, b, c = line[2*j:2*j+3]
                    word = mul(mul(reflection[c], inverse[b]), mul(reflection[b], inverse[a]))
                    assert word == unit
                    cups += 1
            charts += 1
    return {'exact_field_prime': prime, 'literal_Morse_charts': charts, 'prefix_products': products,
            'unmodified_wire_labels': untouched, 'ordered_cup_cap_words': cups}


def regulator():
    a, b, c, e, da, db, dc, de = sp.symbols('a b c e da db dc de', real=True)
    # Independent real marked-regulator convention u=a+ib, v=c+ie.
    correction = 2*a*e
    dcorrect = sp.diff(correction, a)*da+sp.diff(correction, e)*de
    action = sp.im(2*(c+sp.I*e)*(da+sp.I*db))
    # Schlaefli in these names is dVol=2(Re v dIm u-Re u dIm v).
    dvol = 2*(c*db-a*de)
    assert sp.expand(action-dvol-dcorrect) == 0
    chi, delta, dchi = sp.symbols('chi delta dchi')
    U, V = -2*sp.pi*sp.I*chi, -4*sp.pi*sp.I*delta
    lhs = 2*sp.pi*sp.I*(2*sp.pi*sp.I*delta*dchi)
    rhs = V*sp.diff(U, chi)*dchi/2
    assert sp.simplify(lhs-rhs) == 0
    return {'marked_real_boundary_differential': 1, 'source_peripheral_differential': 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='experiments/actual_complete_core_geometric_deformation_results.json')
    args = ap.parse_args()
    mp.mp.dps = 60
    result = {'status': 'PASS', 'precision_digits': 60,
              'literal_global_words': global_morse_words(),
              'joint_geometry_and_source': geometric_cases(),
              'regulator': regulator(),
              'scope': 'Actual marked checkerboard fixtures solved jointly with source channel stationarity; independent three-contact-point collars; original global Morse prefix/cup relations and retained Hurwitz words; primitive eigenlogs and marked regulator signs. The all-diagram theorem is the analytical assembly, not inferred from these fixtures. No ordinary-color subset or filled-source estimate.'}
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
