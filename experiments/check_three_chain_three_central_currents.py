#!/usr/bin/env python3
"""Outward supporting planes for the original six-variable three-chain core.

No optimizer is used in acceptance. This certifies central currents only;
outer periods, real-index tails and cap remainders remain separate.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from flint import arb, acb, acb_mat, ctx
from certify_three_prepared_central_currents import function as one_cap, primitive

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)
B = [(Q(7, 50), Q(1, 5)), (Q(0), Q(9, 5)),
     (Q(1, 4), Q(9, 20)), (Q(1, 4), Q(9, 20)),
     (Q(7, 50), Q(1, 5)), (Q(0), Q(9, 5))]


def a(q):
    if isinstance(q, arb):
        return q
    q = Q(q)
    return arb(q.numerator)/q.denominator


def full_value_gradient(point, heights):
    pi = arb.pi()
    value, gradient = one_cap(point[:5], [*heights[:4], a(heights[4])-arb(2).log()/(2*pi)])
    y, tau = acb(a(point[4]), a(heights[4])), acb(a(point[5]), a(heights[5]))
    cap = -primitive(arb(1)/2-y+tau/(2*pi))-primitive(arb(1)/2-y-tau/(2*pi))-2*primitive(y)
    cap -= 4*primitive(arb(1)/4+tau/(4*pi))+4*primitive(arb(1)/4-tau/(4*pi))
    cap += 3*I*tau*tau/(4*pi)-I*tau
    lp, lm = (pi*y+tau/2).cos().log(), (pi*y-tau/2).cos().log()
    cy = lp+lm-2*(pi*y).sin().log()
    ct = (lp-lm)/(2*pi)-((tau/2).tan()+1/(tau/2).cos()).log()/pi+3*I*tau/(2*pi)-I
    return value+cap.real, [*gradient[:4], gradient[4]+cy.real, ct.real]


def domains():
    yh, H = arb(2).log()/(2*arb.pi()), Q(24961509, 25000000)
    base = [yh, -H, Q(0), Q(0), yh, -H]
    for axis, end, hs, ht in product((2, 3), (0, 1), (-Q(1, 100), Q(1, 100)), (-Q(1, 100), Q(1, 100))):
        box, h = list(B), list(base)
        box[axis] = (box[axis][end],)*2
        h[2], h[3] = hs, ht
        yield ('index_side', axis, end, str(hs), str(ht)), box, h, Q(317, 100)
    for hs, ht in product((-Q(1, 100), Q(1, 100)), repeat=2):
        h = list(base)
        h[2], h[3] = hs, ht
        yield ('alias', str(hs), str(ht)), B, h, Q(1591, 500)
    for axis, end in product((0, 1, 4, 5), (0, 1)):
        box = list(B)
        box[axis] = (box[axis][end],)*2
        yield ('translation_face', axis, end), box, base, Q(1587, 500)


def geometric_data():
    path = ROOT/'repro/results/research-three-chain-geometric-chamber.json'
    record = json.loads(path.read_text())
    assert record['status'] == 'passed'
    assert 'experiments/check_three_chain_geometric_chamber.py' in record['sha256']
    for name, digest in record['sha256'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    centers = next(r['centers'] for r in record['references'] if r['length'] == 3)
    error = arb(8)/(3*10**25)
    radius = arb(1)/10**23
    assert radius > 2*error
    points = [acb(a(re), a(im)) for re, im in centers]
    ts = [acb(arb(z.real, radius), arb(z.imag, radius)) for z in points]
    pi = arb.pi()
    def system(values):
        residual, jacobian = [], [[acb(0) for _ in range(3)] for _ in range(3)]
        for j, t in enumerate(values):
            f, diagonal = 3*t-2*pi, acb(3)
            for k in (j-1, j+1):
                u = values[k] if 0 <= k < 3 else acb(0)
                v, c, ss = (t/2).tan(), (u/2).cos(), (u/2).sin()
                root = (1+v*v*c*c).sqrt()
                f += 2*I*(v*c).asinh()
                diagonal += I*c*(1+v*v)/root
                if 0 <= k < 3:
                    jacobian[j][k] = -I*v*ss/root
            residual.append(f)
            jacobian[j][j] = diagonal
        return residual, jacobian
    f0, j0 = system(points)
    inverse = acb_mat(j0).inv()
    cdata = [[[str(inverse[j, k].real.mid().fmpq()), str(inverse[j, k].imag.mid().fmpq())]
              for k in range(3)] for j in range(3)]
    preconditioner = [[acb(a(re), a(im)) for re, im in row] for row in cdata]
    _, jbox = system(ts)
    root_checks = [('old original root inside fresh complex disks', radius-2*error)]
    for row in range(3):
        contraction = sum(abs(acb(int(row == col))-sum(preconditioner[row][k]*jbox[k][col] for k in range(3))) for col in range(3))
        displacement = abs(sum(preconditioner[row][k]*f0[k] for k in range(3)))
        root_checks += [(f'fresh period contraction{row}', arb(1)/4-contraction),
                        (f'fresh period self-map{row}', radius*(1-contraction)-displacement)]
    completed = [acb(0), *ts, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).tan(), (u/2).tan()
        root = (1+tv*tv+uv*uv).sqrt()
        root_checks.append((f'original positive edge{j}', root.real-(tv.real**2+uv.real**2).sqrt()))
    assert all(m > 0 for _, m in root_checks)
    wires = [((1-t.cos()*u.cos())/(2+t.cos()+u.cos())).acos()/(2*pi) for t, u in zip(ts, ts[1:])]
    indices = []
    for x in wires:
        X = (2*pi*I*x).exp()
        U = (1-X)/(1+X+2*X*ts[1].cos())
        assert U.real < 0 and U.imag < 0
        indices.append(I*U.log()/(2*pi))
    return [wires[0], ts[0], *indices, wires[1], ts[2]], path, root_checks, centers, cdata


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-three-chain-three-central-currents.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    proposal_path = ROOT/'experiments/data/three_chain_three_central_support_points.json'
    proposals = json.loads(proposal_path.read_text())
    points = proposals['points']
    proposed = {tuple(row['domain']): list(map(Q, row['support_point'])) for row in points}
    assert len(proposed) == len(points) == 28
    saved = []
    for key, bounds, heights, target in domains():
        point = proposed.pop(key)
        assert all(lo <= z <= hi for z, (lo, hi) in zip(point, bounds))
        value, gradient = full_value_gradient(point, heights)
        upper = value+sum(max((g*a(lo-z)).upper(), (g*a(hi-z)).upper()) for g, z, (lo, hi) in zip(gradient, point, bounds))
        assert upper < a(target), (key, upper, target)
        saved.append({'domain': list(key), 'bounds': [[str(lo), str(hi)] for lo, hi in bounds],
                      'support_point': list(map(str, point)), 'threshold': str(target),
                      'support_upper': str(upper)})
    assert not proposed and len(saved) == 28
    angular_point = list(map(Q, proposals['angular_support_point']))
    assert all(lo <= z <= hi for z, (lo, hi) in zip(angular_point, B[:5]))
    angular_value, angular_gradient = one_cap(angular_point, [arb(2).log()/(2*arb.pi()), -Q(24961509, 25000000), Q(0), Q(0), Q(0)])
    angular_upper = angular_value+sum(max((g*a(lo-z)).upper(), (g*a(hi-z)).upper()) for g, z, (lo, hi) in zip(angular_gradient, angular_point, B[:5]))
    assert angular_upper < a('1.914'), angular_upper
    z, geometry_path, root_checks, root_centers, root_preconditioner = geometric_data()
    comparisons = []

    def positive(name, margin):
        assert margin > 0, (name, margin)
        comparisons.append({'name': name, 'strict_positive_margin': str(margin)})

    for name, margin in root_checks:
        positive(name, margin)

    for j, q in enumerate(z):
        lo, hi = B[j]
        positive(f'critical real coordinate{j} lower', q.real-a(lo))
        positive(f'critical real coordinate{j} upper', a(hi)-q.real)
    for j in (0, 4):
        positive(f'wire{j} depth lower', z[j].imag-a('.09'))
        positive(f'wire{j} depth upper', a('.12')-z[j].imag)
        positive(f'wire{j} minimum real-face distance', min((z[j].real-a('.14')).lower(), (a('.20')-z[j].real).lower())-a('.0203'))
    for j in (1, 5):
        positive(f'cap{j} depth lower', -z[j].imag-a('.97'))
        positive(f'cap{j} depth upper', 1+z[j].imag)
        positive(f'cap{j} minimum real-face distance', min(z[j].real.lower(), (a('1.8')-z[j].real).lower())-a('.273'))
    for j in (2, 3):
        positive(f'index{j} depth inside extraction rectangle', a('.01')-abs(z[j].imag))
        positive(f'index{j} minimum real-face distance', min((z[j].real-a('.25')).lower(), (a('.45')-z[j].real).lower())-a('.0953'))
    pi = arb.pi()
    positive('wire final-face loss', (arb(3)/4+pi/5)*a('.0203')**2/2-arb(1)/4000)
    positive('index final-face loss', arb(3)/8*a('.0953')**2-arb(1)/4000)
    positive('angle final-face loss', a('.273')**2/(40*pi)-arb(1)/4000)
    positive('alias rate below3.17', a('3.17')-a('3.182')+2*pi/100)
    value, _ = full_value_gradient([q.real for q in z], [q.imag for q in z])
    positive('actual original critical action above3.17595', value-a('3.17595'))
    positive('initial common height in chamber lower', a('.99846036')-a('.97'))
    positive('initial common height in chamber upper', 1-a('.99846036'))
    positive('initial wire height in chamber lower', arb(2).log()/(2*pi)-a('.09'))
    positive('initial wire height in chamber upper', a('.12')-arb(2).log()/(2*pi))
    deps = ['notes/research_three_chain_three_central_currents.md',
            'notes/research_three_vertex_joint_concavity.md',
            'notes/research_three_chain_geometric_chamber.md',
            'notes/research_three_chain_action_volume_calibration.md',
            'notes/research_homogeneous_wire_complete_cap.md',
            'notes/research_three_prepared_cap_quantified_source.md',
            'experiments/certify_three_prepared_central_currents.py',
            str(proposal_path.relative_to(ROOT)), str(geometry_path.relative_to(ROOT))]
    result = {'status': 'passed', 'precision_bits': args.precision,
              'scope': 'Original six-variable central side/alias/translation bounds and localized normalization; not a full three-chain source theorem.',
              'support_plane_count': len(saved), 'support_planes': saved,
              'angular_support_plane': {'support_point': list(map(str, angular_point)),
                                        'threshold': '957/500', 'support_upper': str(angular_upper)},
              'strict_comparison_count': len(comparisons), 'comparisons': comparisons,
              'critical_coordinates': list(map(str, z)), 'critical_action': str(value),
              'original_period_centers': root_centers, 'complex_newton_radius': '1/100000000000000000000000',
              'rational_preconditioner': root_preconditioner,
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(saved), 'supporting planes,', len(comparisons), 'strict comparisons; action', value)


if __name__ == '__main__':
    main()
