#!/usr/bin/env python3
"""Actual signed face pairs, common canonical lifts and root boundary domains.

The cuboctahedral fixtures use a main edge.  A supplemental octahedral
202/202 pair deliberately makes no one-main-reference realization claim.
The uniform theorem is the written proof, not these finite samples.
"""
import argparse
import itertools
import json
from pathlib import Path
import mpmath as mp
import sympy as S

from audit_actual_q_hahn_negative_clock_boundary import (
    gaussian, literal_h, logdet_trace,
)


def simplify(x):
    return S.simplify(S.expand_complex(x))


def hermitian(n):
    n0, n1, n2, n3 = n
    return S.Matrix([[n0-n3, -n1+S.I*n2], [-n1-S.I*n2, n0+n3]])


def original_fixture(kind, reference):
    """Normalize an actual adjacent reference meridian, without local frames."""
    E = S.Matrix([[0, -1], [1, 0]])
    if kind == 'cuboctahedron':
        rt = S.sqrt(2)
        normals = {}
        for axis in range(3):
            for sign in [-1, 1]:
                n = [S.Integer(1), S.Integer(0), S.Integer(0), S.Integer(0)]
                n[axis+1] = sign*rt
                normals[(axis, sign)] = n
        point = (1-S.I)/rt
        incident = [(0, 1), (1, 1)]
        pairs = []
        for sy, sz in itertools.product([-1, 1], repeat=2):
            for reverse in [False, True]:
                outside = [(1, sy), (2, sz)]
                if reverse:
                    outside.reverse()
                pairs.append((outside[0], (0, 1), (0, -1), outside[1]))
        scope = 'actual cube x-matching; reference at a nonmatching main z-edge'
    else:
        assert kind == 'octahedron'
        normals = {ss: [1/S.sqrt(2), *[x/S.sqrt(2) for x in ss]]
                   for ss in itertools.product([-1, 1], repeat=3)
                   if ss[0]*ss[1]*ss[2] == 1}
        point = S.Integer(1)
        incident = [(1, 1, 1), (1, -1, -1)]
        pairs = [((-1, 1, -1), incident[0], incident[1], (-1, -1, 1))]
        scope = ('supplemental actual right-angled 202/202 face pair; '
                 'reference tangency is not claimed to be a main edge')
    ref, neighbor = incident[reference], incident[1-reference]
    g = S.Matrix([[0, -1], [1, -point]])
    gi = g.inv()
    hs = {key: (gi.conjugate().T*hermitian(n)*gi).applyfunc(simplify)
          for key, n in normals.items()}
    jr = E*hs[ref].conjugate()
    qneighbor = (E*hs[neighbor].conjugate()*jr.conjugate()).applyfunc(simplify)
    assert qneighbor[0, 0] == qneighbor[1, 1] == -1
    assert qneighbor[1, 0] == 0
    tau = simplify(-qneighbor[0, 1])
    assert tau != 0
    # z -> z/tau sends the POSITIVE original adjacent meridian to z+1.
    inverse = S.diag(tau, 1)
    scale = S.sqrt(simplify(tau*S.conjugate(tau)))
    hs = {key: (inverse.conjugate().T*h*inverse/scale).applyfunc(simplify)
          for key, h in hs.items()}
    jr = E*hs[ref].conjugate()
    qs = {key: (E*h.conjugate()*jr.conjugate()).applyfunc(simplify)
          for key, h in hs.items()}
    assert qs[ref] == S.eye(2)
    assert qs[neighbor] == -S.Matrix([[1, 1], [0, 1]])
    br = hs[ref][0, 1]
    assert br in (-1, 1)
    assert simplify(br*(hs[ref][1, 1]+hs[neighbor][1, 1])-1) == 0
    for key, h in hs.items():
        assert simplify(h.det()+1) == 0
        assert h[0, 0].is_nonnegative
        assert simplify(qs[key][1, 0]+h[0, 0]*br) == 0
    patterns = set()
    orientations = set()
    for first, middle, outmiddle, last in pairs:
        P = qs[last]*qs[first].inv()
        for mid in [middle, outmiddle]:
            A = qs[mid]*qs[first].inv()
            B = qs[last]*qs[mid].inv()
            assert simplify(S.trace(A)+2) == 0
            assert simplify(S.trace(B)+2) == 0
            assert simplify(S.trace(P)+2) == 0
            pattern = ''.join('0' if hs[k][0, 0] == 0 else '2'
                              for k in [first, mid, last])
            assert pattern in ['002', '022', '200', '202', '220', '222']
            patterns.add(pattern)
            if pattern in ('200', '002'):
                raw = B if pattern == '200' else A
                eps = simplify(-raw[0, 1])
                assert eps in (-1, 1)
                assert raw == -S.Matrix([[1, eps], [0, 1]])
                orientations.add((pattern, int(eps)))
    return {'kind': kind, 'reference': reference, 'scope': scope,
            'hs': hs, 'qs': qs, 'pairs': pairs, 'patterns': patterns,
            'orientations': orientations}


def number(x):
    return mp.mpc(str(S.re(x).evalf(110)), str(S.im(x).evalf(110)))


def numerical_fixture(fixture):
    fixture = dict(fixture)
    fixture['mq'] = {key: [[number(q[i, j]) for j in range(2)] for i in range(2)]
                      for key, q in fixture['qs'].items()}
    return fixture


def cube_one_main_witness():
    """Literal four-terminal restoration for the cube x-matching."""
    circles = list(itertools.product([-1, 1], repeat=2))
    index = {yz:i for i,yz in enumerate(circles)}
    terminals = {}
    for sx, sy, sz in itertools.product([-1, 1], repeat=3):
        positive = sx*sy*sz == 1
        terminals[(sx, sy, sz), 1] = (index[sy, sz], 1 if positive else 0)
        terminals[(sx, sy, sz), 2] = (index[sy, sz], 2 if positive else 3)
    matching = {}
    for (vertex, axis), terminal in terminals.items():
        other = list(vertex)
        other[axis] *= -1
        matching[terminal] = terminals[tuple(other), axis]
    assert len(matching) == 16
    for a,b in matching.items():
        assert matching[b] == a and a != b
    # The terminal convention is the actual spherical cube ribbon order.
    rotation, endpoints = {}, {}
    for sx,sy,sz in itertools.product([-1,1],repeat=3):
        v = (sx,sy,sz)
        disk, ey, ez = ('x',sy,sz), ('y',sx,sz), ('z',sx,sy)
        rotation[v] = [disk,ey,ez] if sx*sy*sz == 1 else [disk,ez,ey]
        for edge in rotation[v]: endpoints.setdefault(edge,[]).append(v)
    seen_flags, face_lengths = set(), []
    for first,edges in rotation.items():
        for edge0 in edges:
            if (first,edge0) in seen_flags: continue
            v,edge = first,edge0
            length = 0
            while True:
                assert (v,edge) not in seen_flags
                seen_flags.add((v,edge)); length += 1
                w = next(x for x in endpoints[edge] if x != v)
                ee = rotation[w]
                v,edge = w,ee[(ee.index(edge)-1)%3]
                if (v,edge) == (first,edge0): break
            face_lengths.append(length)
    assert sorted(face_lengths) == [4]*6
    counts = []
    witness = None
    for parity in itertools.product([0, 1], repeat=4):
        local = {}
        for i, odd in enumerate(parity):
            for a,b in ([(0,2),(1,3)] if odd else [(0,1),(2,3)]):
                local[i,a] = (i,b)
                local[i,b] = (i,a)
        seen, count = set(), 0
        for first in matching:
            if first in seen: continue
            count += 1
            todo = [first]
            while todo:
                v = todo.pop()
                if v in seen: continue
                seen.add(v)
                todo.extend([matching[v], local[v]])
        counts.append(count)
        if count == 1 and witness is None:
            witness = list(parity)
    assert witness is not None
    return witness, counts


def prefix(q, r, s):
    (a, b), (c, d) = q
    return -c*r*r/s+(a-d+c/s)*r+d+b*s


def canonical(clock):
    arg = mp.arg(clock)
    if arg <= 0:
        arg += 2*mp.pi
    assert 0 < arg < 2*mp.pi
    return arg/(2*mp.pi)-1j*mp.log(abs(clock))/(2*mp.pi)


def data(fixture, keys, N, alpha, rho):
    first, middle, last = keys
    s = mp.exp(-2j*mp.pi*alpha)-1
    r = N*rho
    ll = [prefix(fixture['mq'][key], r, s) for key in keys]
    assert all(abs(x) > mp.mpf('1e-30') for x in ll)
    X, Y = -ll[0]/ll[1], -ll[1]/ll[2]
    x, y = canonical(X), canonical(Y)
    pattern = ''.join('0' if fixture['hs'][key][0, 0] == 0 else '2' for key in keys)
    limit = []
    for key in keys:
        q = fixture['mq'][key]
        limit.append(q[1][1]+q[0][1]*s if q[1][0] == 0 else -q[1][0]*rho*rho/s)
    X0, Y0 = -limit[0]/limit[1], -limit[1]/limit[2]
    return pattern, X, Y, x, y, X0, Y0


def determinant_one(N, a, X):
    """det(I-X H_-/2), retaining the exact finite complex X."""
    theta = mp.pi/N
    before, now = mp.mpc(1), mp.mpc(1)
    for n in range(a):
        diagonal = 1-X/(2*mp.cos(n*theta)*mp.cos((n+1)*theta))
        if n == 0:
            now = diagonal
        else:
            B = mp.sin(n*theta)**2/(mp.cos(n*theta)**2
                *mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta))
            before, now = now, diagonal*now-X*X*B*before/4
    return now


def packet(N, a, pattern, X, Y, x, y, X0, Y0):
    q, Q = mp.exp(1j*mp.pi/N), mp.exp(2j*mp.pi/N)
    m = N-1-a
    U, V = X/q, Y/q
    literal = literal_h(N, m, U, V)
    i, j = N*x-mp.mpf('.5'), N*y-mp.mpf('.5')
    sigma, row = i+j, i+j-m
    dual_i, dual_j = (N-1)-j, (N-1)-i
    assert abs(dual_i+dual_j-m-(2*a-row)) < mp.mpf('1e-90')
    A0 = Q**(N-1)
    dual_literal = literal_h(N, m, A0/V, A0/U)
    reciprocal = A0**m*(U*V)**(-m)*literal
    reciprocal_error = abs(dual_literal/reciprocal-1)
    assert reciprocal_error < mp.mpf('1e-75')
    # Full W phase, beyond the bare H reciprocal factor, at the actual lifts.
    original_exponent = -(N-1)*(sigma-m)+(N-1)*i-m*(m-1)
    dual_exponent = -(N-1)*(dual_i+dual_j-m)+(N-1)*dual_i-m*(m-1)
    white_ratio = q**(dual_exponent-original_exponent)*dual_literal/literal
    white_expected = q**((N-1-2*a)*(a-row))
    white_error = abs(white_ratio/white_expected-1)
    assert white_error < mp.mpf('1e-75')
    sine = mp.sin(mp.pi*m/N)**2
    if pattern == '200':
        top = (-1)**m*Q**(m*(m+1)//2)*(U*V)**m
        top *= mp.fprod(1-Q**j/U for j in range(m))
        K = sine*(V-1)/(mp.pi**2*(U/N**2)*V)
        model = top*mp.besselj(0, 2*mp.sqrt(K))
    elif pattern == '002':
        top = mp.fprod(V-Q**j for j in range(m))
        K = (N**2*V)*sine*(1-U)/mp.pi**2
        model = top*mp.besselj(0, 2*mp.sqrt(K))
    elif pattern == '202':
        sins = [mp.mpf(1)]
        for j in range(1, a+1):
            sins.append(sins[-1]*2*mp.sin(mp.pi*j/N))
        poly = mp.fsum((sins[a]/(sins[k]*sins[a-k]))**2*(Q*U*V)**k
                       for k in range(a+1))
        model = (-1)**a*Q**(a*(a-1)//2)*poly
        model *= mp.fprod(U*V-Q**j for j in range(a, m))
    elif pattern in ('220', '022'):
        scalar = mp.mpc(1)
        if pattern == '022':
            A0 = Q**-1
            scalar = (U*V/A0)**m
            U, V = A0/V, A0/U
        model = scalar*V**m*U**(m-a)*gaussian(N, a)*determinant_one(N, a, q*U)
    else:
        assert pattern == '222'
        aa, bb = mp.re(-X0/2), mp.re(-1/(2*Y0))
        da, db = -X/2-aa, -1/(2*Y)-bb
        ld, trace = logdet_trace(N, a, aa, bb, da, db)
        model = V**a*gaussian(N, a)*mp.exp(ld+trace)
        model *= mp.fprod(U*V-Q**j for j in range(a, m))
    assert literal != 0 and model != 0
    return float(N*abs(literal/model-1)), float(reciprocal_error), float(white_error)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = 100
    fixtures = [numerical_fixture(original_fixture(kind, ref))
                for kind in ['cuboctahedron', 'octahedron'] for ref in [0, 1]]
    parity_witness, parity_counts = cube_one_main_witness()
    patterns, orientations, pairs_seen = set(), set(), set()
    totals, heads, auxiliary, branch, domains, corrections = 0, 0, 0, 0, 0, 0
    max_total_error = mp.mpf(0)
    min_physical_margin, min_auxiliary_margin = mp.inf, mp.inf
    for fixture in fixtures:
        patterns.update(fixture['patterns'])
        orientations.update(fixture['orientations'])
        for N, alpha, rho in itertools.product([47, 48, 95, 96],
                map(mp.mpf, ['.02', '.04']), map(mp.mpf, ['.8', '1.25'])):
            for first, middle, outmiddle, last in fixture['pairs']:
                halves = [data(fixture, [first, mid, last], N, alpha, rho)
                          for mid in [middle, outmiddle]]
                pair = '/'.join(row[0] for row in halves)
                pairs_seen.add(pair)
                total_error = abs(halves[0][3]+halves[0][4]-halves[1][3]-halves[1][4])
                max_total_error = max(max_total_error, total_error)
                assert total_error < mp.mpf('1e-90')
                totals += 1
                for pattern, X, Y, x, y, X0, Y0 in halves:
                    assert mp.mpf('.5') < mp.re(x+y) < mp.mpf('1.5')
                    for raw, log in [(X, x), (Y, y)]:
                        i = N*log-mp.mpf('.5')
                        margin = min(mp.re(i/N), 1-mp.re(i/N))
                        min_physical_margin = min(min_physical_margin, margin)
                        assert margin > 0
                        inverse = canonical(1/raw)
                        assert abs((N*inverse-mp.mpf('.5'))+i-(N-1)) < mp.mpf('1e-90')
                        heads += 1
                    T = X*Y
                    if pattern in ['202', '222']:
                        assert mp.re(T) > 0
                        w = mp.exp(mp.pi*1j*(x+y))
                        assert abs(w+mp.sqrt(T)) < mp.mpf('1e-88')
                        branch += 1
                    if pattern == '222':
                        assert mp.re(X) < 0 and mp.re(Y) < 0
                        eta = abs(X/X0-1)+abs(Y0/Y-1)
                        assert eta < mp.mpf('.5')
                    if pattern == '220': assert mp.re(X) < 0
                    if pattern == '022': assert mp.re(Y) < 0
                    if pattern[0] != pattern[1]: assert abs(mp.im(X0)) > 0
                    if pattern[1] != pattern[2]: assert abs(mp.im(Y0)) > 0
                    domains += 1
                    # Finite-r values are tested, not silently replaced by limits.
                    kx = int(pattern[0])-int(pattern[1])
                    ky = int(pattern[1])-int(pattern[2])
                    assert abs(X/(N**kx*X0)-1) < mp.mpf('.5')
                    assert abs(Y/(N**ky*Y0)-1) < mp.mpf('.5')
                    corrections += 2
                    for shift in [0, 1, 3]:
                        a = (N-1)//2-shift
                        sigma = N*(x+y)-1
                        row = sigma-(N-1-a)
                        complement = 2*a-row
                        assert abs(row-(a+N*(x+y-1))) < mp.mpf('1e-90')
                        assert abs((2*(N-1)-sigma)-(N-1-a)-complement) < mp.mpf('1e-90')
                        for z in [row, complement]:
                            if pattern in ['202', '222']:
                                margin = min(mp.re(z/N), 1-mp.re(z/N))
                                assert margin > 0
                            else:
                                margin = abs(mp.im(z/N))
                                assert margin > mp.mpf('.25')
                            min_auxiliary_margin = min(min_auxiliary_margin, margin)
                            auxiliary += 1
    assert patterns == {'002', '022', '200', '202', '220', '222'}
    assert orientations == {('200', -1), ('200', 1), ('002', -1), ('002', 1)}
    assert '202/202' in pairs_seen
    packets = []
    for fixture in fixtures:
        for N in [47, 48, 95, 96]:
            for ashift in [0, 1]:
                a = (N-1)//2-ashift
                for first, middle, outmiddle, last in fixture['pairs']:
                    for mid in [middle, outmiddle]:
                        row = data(fixture, [first, mid, last], N, mp.mpf('.03'), mp.mpf(1))
                        pattern, X, Y, x, y, X0, Y0 = row
                        error, reciprocal_error, white_error = packet(N, a, pattern, X, Y, x, y, X0, Y0)
                        assert error < 25
                        packets.append({'fixture':fixture['kind'], 'reference':fixture['reference'],
                                        'N':N, 'a':a, 'pattern':pattern, 'N_relative_error':error,
                                        'exact_dual_H_error':reciprocal_error,
                                        'exact_full_W_turn_error':white_error})
    result = {'status':'PASS', 'precision_digits':mp.mp.dps,
              'actual_reference_fixtures':len(fixtures),
              'exact_paired_total_checks':totals, 'physical_heads_and_exact_cups':heads,
              'auxiliary_factorial_domain_checks':auxiliary,
              'marked_negative_square_root_checks':branch,
              'simultaneous_half_disk_domain_checks':domains,
              'actual_finite_r_clock_checks':corrections,
              'literal_root_numerator_packets':len(packets),
              'exact_dual_H_and_full_W_turn_checks':len(packets),
              'cube_main_component_parity_witness':parity_witness,
              'literal_parity_component_counts':parity_counts,
              'patterns':sorted(patterns), 'paired_patterns':sorted(pairs_seen),
              'primitive_orientation_cases':sorted(orientations),
              'max_exact_total_error':str(max_total_error),
              'min_physical_scaled_margin':float(min_physical_margin),
              'min_auxiliary_domain_margin':float(min_auxiliary_margin),
              'max_N_packet_relative_error':max(p['N_relative_error'] for p in packets),
              'max_dual_H_error':max(p['exact_dual_H_error'] for p in packets),
              'max_full_W_turn_error':max(p['exact_full_W_turn_error'] for p in packets),
              'fixtures':[{'kind':f['kind'],'reference':f['reference'],'scope':f['scope']} for f in fixtures],
              'packets':packets,
              'scope':'Actual signed geometry and root numerators. Supplemental octahedral202/202 reference is not claimed to be a main edge. No generic normal, finite-color stationarity, or global period tested.'}
    target = args.output or Path(__file__).with_name('actual_original_network_resonant_boundary_chart_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('packets','fixtures')}, indent=2))


if __name__ == '__main__':
    main()
