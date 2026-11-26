#!/usr/bin/env python3
"""Independent replay of the actual six-variable three-chain central currents.

No author module or optimizer is imported. The action uses a reflected
real cap primitive and a negative-frequency retained primitive; the
period map uses cosine/log returns and the wire uses an arcsine lift.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from flint import arb, acb, acb_mat, ctx
from replay_three_cap_wire_complement import positive_primitive
from replay_three_vertex_directed_packet import action

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)
B = [(Q(7, 50), Q(1, 5)), (Q(0), Q(9, 5)), (Q(1, 4), Q(9, 20)),
     (Q(1, 4), Q(9, 20)), (Q(7, 50), Q(1, 5)), (Q(0), Q(9, 5))]


def a(q):
    if isinstance(q, arb):
        return q
    q = Q(q)
    return arb(q.numerator)/q.denominator


def cap(z, tau):
    pi = arb.pi()
    jr = lambda w: positive_primitive(w.real, abs(w.imag))
    value = -jr(arb(1)/2-z+tau/(2*pi))-jr(arb(1)/2-z-tau/(2*pi))-2*jr(z)
    value -= 4*jr(arb(1)/4+tau/(4*pi))+4*jr(arb(1)/4-tau/(4*pi))
    value += -3*tau.real*tau.imag/(2*pi)+tau.imag
    lp, lm = abs((pi*z+tau/2).cos()).log(), abs((pi*z-tau/2).cos()).log()
    dz = lp+lm-2*abs((pi*z).sin()).log()
    dtau = (lp-lm)/(2*pi)-(tau/2).tan().asinh().real/pi-3*tau.imag/(2*pi)
    return value, dz, dtau


def value_gradient(point, heights, both=True):
    pi = arb.pi()
    x, tau, s, t, y, sigma = [acb(a(q), a(h)) for q, h in zip(point, heights)]
    X, Y = (2*pi*I*x).exp(), (2*pi*I*y).exp()
    U, V = (-2*pi*I*s).exp(), (-2*pi*I*t).exp()
    left, lx, ltau = cap(x, tau)
    right, ry, rsigma = cap(y, sigma) if both else (arb(0), arb(0), arb(0))
    value = left+right+(action(s, t, X, Y)-pi*I*(x+y)).real
    px = -2*pi*s.imag+abs(1-X*U).log()-abs(1-X).log()
    py = -2*pi*t.imag+abs(1-Y*V).log()-abs(1-Y).log()
    common = abs(1-U*V).log()
    fs = abs(X).log()+common-abs(1-X*U).log()
    ft = abs(Y).log()+common-abs(1-Y*V).log()
    return value, [lx+px, ltau, fs, ft, ry+py, rsigma]


def domains():
    yh = arb(2).log()/(2*arb.pi())
    h0 = [yh, -Q(24961509, 25000000), Q(0), Q(0), yh, -Q(24961509, 25000000)]
    for axis, end, hs, ht in product((2, 3), (0, 1), (-Q(1, 100), Q(1, 100)), (-Q(1, 100), Q(1, 100))):
        box, h = list(B), list(h0)
        box[axis] = (box[axis][end],)*2
        h[2], h[3] = hs, ht
        yield ('index_side', axis, end, str(hs), str(ht)), box, h, Q(317, 100)
    for hs, ht in product((-Q(1, 100), Q(1, 100)), repeat=2):
        h = list(h0)
        h[2], h[3] = hs, ht
        yield ('alias', str(hs), str(ht)), B, h, Q(1591, 500)
    for axis, end in product((0, 1, 4, 5), (0, 1)):
        box = list(B)
        box[axis] = (box[axis][end],)*2
        yield ('translation_face', axis, end), box, h0, Q(1587, 500)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--artifact', type=Path, default=ROOT/'repro/results/research-three-chain-three-central-currents.json')
    ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-three-chain-three-central-currents-replay.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    d = json.loads(args.artifact.read_text())
    assert d['status'] == 'passed'
    expected = {key: (box, h, target) for key, box, h, target in domains()}
    seen, support = set(), []
    for row in d['support_planes']:
        key = tuple(row['domain'])
        assert key in expected and key not in seen
        seen.add(key)
        box, h, target = expected[key]
        assert [[Q(v) for v in pair] for pair in row['bounds']] == [list(pair) for pair in box]
        assert Q(row['threshold']) == target
        point = list(map(Q, row['support_point']))
        assert all(lo <= z <= hi for z, (lo, hi) in zip(point, box))
        value, gradient = value_gradient(point, h)
        upper = value+sum(max((g*a(lo-z)).upper(), (g*a(hi-z)).upper()) for g, z, (lo, hi) in zip(gradient, point, box))
        assert upper < a(target), (key, upper)
        support.append(str(upper))
    assert len(seen) == 28 and seen == set(expected)
    apoint = list(map(Q, d['angular_support_plane']['support_point']))
    assert len(apoint) == 5 and all(lo <= z <= hi for z, (lo, hi) in zip(apoint, B[:5]))
    yh, pi = arb(2).log()/(2*arb.pi()), arb.pi()
    h0 = [yh, -Q(24961509, 25000000), Q(0), Q(0), yh, -Q(24961509, 25000000)]
    av, ag = value_gradient([*apoint, Q(0)], h0, both=False)
    au = av+sum(max((g*a(lo-z)).upper(), (g*a(hi-z)).upper()) for g, z, (lo, hi) in zip(ag[:5], apoint, B[:5]))
    assert au < a('1.914') and Q(d['angular_support_plane']['threshold']) == Q(957, 500)
    comparisons = []

    def positive(name, margin):
        assert margin > 0, (name, margin)
        comparisons.append({'name': name, 'strict_positive_margin': str(margin)})

    geometry = json.loads((ROOT/'repro/results/research-three-chain-geometric-chamber.json').read_text())
    centers_q = next(r['centers'] for r in geometry['references'] if r['length'] == 3)
    assert centers_q == d['original_period_centers']
    for path, digest in geometry['sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    radius = a(d['complex_newton_radius'])
    assert Q(d['complex_newton_radius']) == Q(1, 10**23)
    positive('old geometric root within new disks', radius-arb(16)/(3*10**25))
    centers = [acb(a(re), a(im)) for re, im in centers_q]
    ts = [acb(arb(z.real, radius), arb(z.imag, radius)) for z in centers]

    def system(values):
        residual, jacobian = [], [[acb(0) for _ in range(3)] for _ in range(3)]
        for j, t in enumerate(values):
            value, diagonal = 3*t-2*pi, acb(3)
            for k in (j-1, j+1):
                u = values[k] if 0 <= k < 3 else acb(0)
                st, ct, su, cu = (t/2).sin(), (t/2).cos(), (u/2).sin(), (u/2).cos()
                radical = (ct*ct+st*st*cu*cu).sqrt()
                value += 2*I*((st*cu+radical)/ct).log()
                diagonal += I*cu/(ct*radical)
                if 0 <= k < 3:
                    jacobian[j][k] = -I*st*su/radical
            residual.append(value)
            jacobian[j][j] = diagonal
        return residual, jacobian

    f0, j0 = system(centers)
    inverse = acb_mat(j0).inv()
    C = [[acb(a(str(inverse[j, k].real.mid().fmpq())), a(str(inverse[j, k].imag.mid().fmpq()))) for k in range(3)] for j in range(3)]
    _, jb = system(ts)
    for row in range(3):
        q = sum(abs(acb(int(row == col))-sum(C[row][k]*jb[k][col] for k in range(3))) for col in range(3))
        r = abs(sum(C[row][k]*f0[k] for k in range(3)))
        positive(f'independent Newton contraction{row}', arb(1)/4-q)
        positive(f'independent Newton self-map{row}', radius*(1-q)-r)
    completed = [acb(0), *ts, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).tan(), (u/2).tan()
        positive(f'original positive edge{j}', (1+tv*tv+uv*uv).sqrt().real-(tv.real**2+uv.real**2).sqrt())
    for j, t in enumerate(ts):
        for k in (j-1, j+1):
            u = ts[k] if 0 <= k < 3 else acb(0)
            st, ct, cu = (t/2).sin(), (t/2).cos(), (u/2).cos()
            radical = (ct*ct+st*st*cu*cu).sqrt()
            positive(f'return{j},{k} normalized square-root branch', (radical/ct).real)
            positive(f'return{j},{k} logarithm branch', ((st*cu+radical)/ct).real)
    wires = []
    for t, u in zip(ts, ts[1:]):
        A, BB = (t/2).cos()**2, (u/2).cos()**2
        wires.append((A*BB/(A+BB)).sqrt().asin()/pi)
    X, Y = [(2*pi*I*x).exp() for x in wires]
    alpha, beta = 1/X-1, 1/Y-1
    delta = 1-2*(alpha+beta)+(alpha-beta)**2
    positive('selected index discriminant', delta.imag)
    U, V = (1+alpha-beta-delta.sqrt())/2, (1-alpha+beta-delta.sqrt())/2
    for name, z in [('U', U), ('V', V)]:
        positive(name+' negative real', -z.real)
        positive(name+' negative imaginary', -z.imag)
    z = [wires[0], ts[0], I*U.log()/(2*pi), I*V.log()/(2*pi), wires[1], ts[2]]
    for j, q in enumerate(z):
        lo, hi = B[j]
        positive(f'critical coordinate{j} lower', q.real-a(lo))
        positive(f'critical coordinate{j} upper', a(hi)-q.real)
    for j in (0, 4):
        positive(f'wire{j} chamber lower', z[j].imag-a('.09'))
        positive(f'wire{j} chamber upper', a('.12')-z[j].imag)
        positive(f'wire{j} face distance', min((z[j].real-a('.14')).lower(), (a('.20')-z[j].real).lower())-a('.0203'))
    for j in (1, 5):
        positive(f'angle{j} chamber lower', -z[j].imag-a('.97'))
        positive(f'angle{j} chamber upper', 1+z[j].imag)
        positive(f'angle{j} face distance', min(z[j].real.lower(), (a('1.8')-z[j].real).lower())-a('.273'))
    for j in (2, 3):
        positive(f'index{j} extraction height', a('.01')-abs(z[j].imag))
        positive(f'index{j} face distance', min((z[j].real-a('.25')).lower(), (a('.45')-z[j].real).lower())-a('.0953'))
    positive('wire boundary gap', (arb(3)/4+pi/5)*a('.0203')**2/2-arb(1)/4000)
    positive('index boundary gap', arb(3)/8*a('.0953')**2-arb(1)/4000)
    positive('angle boundary gap', a('.273')**2/(40*pi)-arb(1)/4000)
    positive('index alias gap', a('3.17')-a('3.182')+2*pi/100)
    critical, _ = value_gradient([q.real for q in z], [q.imag for q in z])
    positive('original action lower bound', critical-a('3.17595'))
    assert -Q(1)-Q(3, 2)+2+2-3 == -Q(3, 2)
    assert d['script_sha256'] == sha256((ROOT/'experiments/check_three_chain_three_central_currents.py').read_bytes()).hexdigest()
    for path, digest in d['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    result = {'status': 'passed', 'precision_bits': args.precision,
              'support_plane_count': 28, 'support_upper_bounds': support,
              'angular_support_upper': str(au), 'exact_domain_cover': True,
              'strict_comparison_count': len(comparisons), 'comparisons': comparisons,
              'critical_action': str(critical), 'critical_coordinates': list(map(str, z)),
              'exact_normalization': 'two cap integrands, retained summand, two index residues, two wire measures, six-dimensional Gaussian give N^-3/2',
              'method': 'Cosine/log original periods, arcsine wires, quadratic index branch, reflected cap and negative-frequency retained action; no author imports.',
              'artifact_sha256': sha256(args.artifact.read_bytes()).hexdigest(),
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': d['dependencies_sha256'] | {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in
                   ['experiments/replay_three_cap_wire_complement.py', 'experiments/replay_three_vertex_directed_packet.py']}}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 28 central+1 angular planes,', len(comparisons), 'strict comparisons; action', critical)


if __name__ == '__main__':
    main()
