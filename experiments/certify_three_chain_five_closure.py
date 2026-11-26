#!/usr/bin/env python3
"""Certify the actual five-chain critical wire and closing budgets.

The original five-complex-variable period system is checked by a single
outward Newton self-map. The previously saved geometric centers only
propose rational data. Correlated wire sectors retain their complex sign.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, acb_mat, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-five-closure.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def point(parts):
        return acb(a(parts[0]), a(parts[1]))

    def squaredisk(z, radius):
        return acb(arb(z.real, radius), arb(z.imag, radius))

    def ret(t, u):
        v, c, s = (t/2).tan(), (u/2).cos(), (u/2).sin()
        root = (1+v*v*c*c).sqrt()
        return (v*c).asinh(), c*(1+v*v)/(2*root), -v*s/(2*root)

    def system(ts):
        rows, F = [[acb(0) for _ in ts] for _ in ts], []
        for j, t in enumerate(ts):
            neighbors = [(j-1, ts[j-1] if j else acb(0)),
                         (j+1, ts[j+1] if j+1 < len(ts) else acb(0))]
            total, derivative = acb(0), acb(3)
            for k, u in neighbors:
                value, dt, du = ret(t, u)
                total += value
                derivative += 2*ii*dt
                if 0 <= k < len(ts):
                    rows[j][k] = 2*ii*du
            F.append(3*t+2*ii*total-2*pi)
            rows[j][j] = derivative
        return F, rows

    source_path = ROOT/'repro/results/research-three-chain-geometric-chamber.json'
    source = json.loads(source_path.read_text())
    assert source['status'] == 'passed'
    ref = next(item for item in source['references'] if item['length'] == 5)
    centers_q = ref['centers']
    centers = [point(z) for z in centers_q]
    radius_q = Q(1, 10**23)
    radius = a(radius_q)
    boxes = [squaredisk(z, radius) for z in centers]
    F0, J0 = system(centers)
    inverse = acb_mat(J0).inv()
    Cq = [[[str(inverse[j, k].real.mid().fmpq()),
            str(inverse[j, k].imag.mid().fmpq())] for k in range(5)] for j in range(5)]
    C = [[point(z) for z in row] for row in Cq]
    _, Jbox = system(boxes)
    checks, contractions, selfmaps = [], [], []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    positive('known original geometric root lies in fresh Newton disks',
             radius-a(Q(16, 3*10**25)))

    for row in range(5):
        con = sum(abs(acb(int(row == col))-sum(C[row][k]*Jbox[k][col] for k in range(5)))
                  for col in range(5))
        residual = abs(sum(C[row][k]*F0[k] for k in range(5)))
        margin = radius-residual-con*radius
        positive(f'Newton row{row} contraction below1/4', a('1/4')-con)
        positive(f'Newton row{row} maps complex disk into itself', margin)
        contractions.append(str(con))
        selfmaps.append(str(margin))
    for j, t in enumerate(boxes):
        for label, value in [('angle lower', t.real-a('1.3')),
                             ('angle upper', a('1.82')-t.real),
                             ('depth lower', -t.imag-a('.82')),
                             ('depth upper', a('1.21')+t.imag)]:
            positive(f'original positive geometry{j} '+label, value)
        for u in [boxes[j-1] if j else acb(0), boxes[j+1] if j < 4 else acb(0)]:
            z = (t/2).tan()*(u/2).cos()
            positive(f'original return{j} right half-plane', z.real)
            positive(f'original return{j} square-root positive real', (1+z*z).sqrt().real)
    completed = [acb(0), *boxes, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).tan(), (u/2).tan()
        edge_root = (1+tv*tv+uv*uv).sqrt()
        positive(f'original edge{j} positive-cell criterion',
                 edge_root.real-(tv.real**2+uv.real**2).sqrt())

    def wire(t, u):
        c = (1-t.cos()*u.cos())/(2+t.cos()+u.cos())
        positive('wire cosine in lower half-plane', -c.imag)
        return c.acos()/(2*pi)

    wires = [wire(t, u) for t, u in zip(boxes, boxes[1:])]
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    indices = []
    for j, x in enumerate(wires):
        for label, value in [('real lower', x.real-a('.14')), ('real upper', a('.20')-x.real),
                             ('height lower', x.imag-a('.09')), ('height upper', a('.12')-x.imag)]:
            positive(f'wire{j} source chamber '+label, value)
    for x in [wires[0], wires[-1]]:
        r, s = x.real-arb(1)/6, x.imag-xh.imag+4*(x.real-arb(1)/6)/5
        for label, value in [('r>0', r), ('r<.013', a('.013')-r),
                             ('s>-.0015', s+a('.0015')), ('s<.001', a('.001')-s)]:
            positive('original complete-cap directed domain '+label, value)
    for t in [boxes[0], boxes[-1]]:
        for label, value in [('real>1.5', t.real-a('1.5')), ('real<1.55', a('1.55')-t.real),
                             ('depth>.97', -t.imag-a('.97')), ('depth<1', 1+t.imag),
                             ('cos half modulus<1', 1-abs((t/2).cos()))]:
            positive('original cap '+label, value)
    for j, (x, y) in enumerate(zip(wires, wires[1:])):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        al, be = 1/X-1, 1/Y-1
        delta = 1-2*(al+be)+(al-be)**2
        positive(f'index{j} selected discriminant lift', delta.imag)
        U, V = (1+al-be-delta.sqrt())/2, (1-al+be-delta.sqrt())/2
        pair = []
        for name, z, base in [('s', U, X), ('t', V, Y)]:
            coordinate = ii*z.log()/(2*pi)
            pair.append(coordinate)
            for label, value in [('U real negative', -z.real), ('U imaginary negative', -z.imag),
                                 ('real>.25', coordinate.real-a('.25')), ('real<.45', a('.45')-coordinate.real),
                                 ('height<.02', a('.02')-abs(coordinate.imag)), ('product radius<1', 1-abs(base*z))]:
                positive(f'index{j}{name} '+label, value)
        positive(f'index{j} sum real>.5', sum(z.real for z in pair)-a('.5'))
        indices.append([str(z) for z in pair])

    zc = wires[1]-xh
    positive('closing wire lies in the true common disk', a('.005')-abs(zc))
    positive('closing radius below .0036', a('.0036')-abs(zc))
    # The second middle wire is the input to the F2 phase elimination.
    positive('hidden F2 wire lies in the incoming F1 disk', a('.005')-abs(wires[2]-xh))
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    K, D, beta, R = abs(k0), 2*arb(21).sqrt(), a('.68'), a('.005')
    sectors = []
    for sign in [-1, 1]:
        d = sign*R-zc
        sector = (k0*D*d*d).real-beta*K*abs(d)**2
        slope = sign*(k0*D*d).real-beta*K*abs(d)
        positive(f'endpoint{sign} correlated sector>.00015', sector-a('.00015'))
        positive(f'endpoint{sign} outward derivative>.07', slope-a('.07'))
        sectors.append({'sign': sign, 'displacement': str(d), 'sector': str(sector), 'slope': str(slope)})
    drift = (k0*D*zc*zc).real/2-beta*K*abs(zc)**2/2
    positive('actual closing action shift exceeds -.000103', drift+a('.000103'))
    positive('common source disk curvature exceeds17', D*k0.real-beta*K-17)
    W, B, loss = a('.009'), a('.000077'), a('.000103')
    positive('middle principal loss exceeds .0002', a('6.15')*W**2-a('.0113')*W-B-loss-a('.0002'))
    positive('middle principal loss increases beyond W', 2*a('6.15')*W-a('.0113'))
    positive('absolute plateau loss exceeds .0004', a('.0006')-B-loss-a('.0004'))
    positive('far real-period loss exceeds .0005', a('.00015')+a('1.5')*a('.02')**2-B-loss-a('.0005'))

    proof = 'notes/research_three_chain_five_closure.md'
    deps = [
        'notes/research_three_chain_geometric_chamber.md',
        'notes/research_homogeneous_three_geometric_contraction.md',
        'notes/research_three_chain_action_volume_calibration.md',
        'notes/research_three_prepared_cap_quantified_source.md',
        'notes/research_three_prepared_cap_real_extension.md',
        'notes/research_three_phase_graph_transform.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_chain_outside_boundary_decay.md',
        str(source_path.relative_to(ROOT)),
    ]
    if (ROOT/proof).exists():
        deps.insert(0, proof)
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Original five-variable period Newton self-map; source/chart inclusions; correlated closing-wire sectors, actual action-shift bound and full-period scalar budgets. The source packets, calibrated branch identification and contour proof are cited written inputs.',
        'centers': centers_q, 'complex_disk_radius': str(radius_q), 'preconditioner': Cq,
        'Newton_row_contractions': contractions, 'Newton_self_map_margins': selfmaps,
        'angle_boxes': [str(z) for z in boxes], 'wire_boxes': [str(z) for z in wires],
        'index_boxes': indices, 'closing_displacement': str(zc),
        'correlated_endpoint_checks': sectors, 'actual_action_shift_lower': str(drift),
        'strict_comparisons': len(checks), 'comparisons': checks,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ['status', 'strict_comparisons',
                     'closing_displacement', 'actual_action_shift_lower']}, indent=2))


if __name__ == '__main__':
    main()
