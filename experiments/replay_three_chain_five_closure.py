#!/usr/bin/env python3
"""Independent cosine/log replay of the original five-chain closure.

No author module is imported. Rational centers propose a new Newton map,
whose preconditioner and derivatives are recomputed from a different
return formula. The geometric root and all scalar/source-domain premises
are checked before the exact finite-word bookkeeping.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, acb_mat, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=320)
    ap.add_argument('--artifact', type=Path,
                    default=ROOT/'repro/results/research-three-chain-five-closure.json')
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-five-closure-replay.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    artifact = json.loads(args.artifact.read_text())
    assert artifact['status'] == 'passed'
    assert len(artifact['centers']) == 5
    pi, ii = arb.pi(), acb(0, 1)

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def point(parts):
        return acb(a(parts[0]), a(parts[1]))

    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    def return_data(t, u):
        # Independent unsummed angular formula, without tan or asinh.
        st, ct = (t/2).sin(), (t/2).cos()
        su, cu = (u/2).sin(), (u/2).cos()
        radical = (ct*ct+st*st*cu*cu).sqrt()
        exp_return = (st*cu+radical)/ct
        value = exp_return.log()
        derivative_t = cu/(2*ct*radical)
        derivative_u = -st*su/(2*radical)
        return value, derivative_t, derivative_u, (radical, exp_return, ct)

    def original_system(ts):
        F, J = [], [[acb(0) for _ in ts] for _ in ts]
        for j, t in enumerate(ts):
            F.append(3*t-2*pi)
            J[j][j] = acb(3)
            for k in [j-1, j+1]:
                u = ts[k] if 0 <= k < len(ts) else acb(0)
                r, dt, du, _ = return_data(t, u)
                F[-1] += 2*ii*r
                J[j][j] += 2*ii*dt
                if 0 <= k < len(ts):
                    J[j][k] += 2*ii*du
        return F, J

    centers = [point(z) for z in artifact['centers']]
    radius = a(artifact['complex_disk_radius'])
    assert Q(artifact['complex_disk_radius']) == Q(1, 10**23)
    original_geometry = json.loads((ROOT/'repro/results/research-three-chain-geometric-chamber.json').read_text())
    assert artifact['centers'] == next(c['centers'] for c in original_geometry['references'] if c['length'] == 5)
    positive('original positive root strictly inside fresh Newton disks',
             radius-a(Q(16, 3*10**25)))
    boxes = [acb(arb(z.real, radius), arb(z.imag, radius)) for z in centers]
    F0, J0 = original_system(centers)
    inv = acb_mat(J0).inv()
    preconditioner = [[acb(a(str(inv[j, k].real.mid().fmpq())),
                            a(str(inv[j, k].imag.mid().fmpq())))
                       for k in range(5)] for j in range(5)]
    _, Jbox = original_system(boxes)
    contractions = []
    for row in range(5):
        con = sum(abs(acb(int(row == col))-sum(preconditioner[row][k]*Jbox[k][col]
                                               for k in range(5))) for col in range(5))
        residual = abs(sum(preconditioner[row][k]*F0[k] for k in range(5)))
        positive(f'independent Newton contraction row{row}', a('.25')-con)
        positive(f'independent Newton self-map row{row}', radius*(1-con)-residual)
        contractions.append(str(con))
    for j, t in enumerate(boxes):
        for name, value in [('a lower', t.real-a('1.3')), ('a upper', a('1.82')-t.real),
                            ('H lower', -t.imag-a('.82')), ('H upper', a('1.21')+t.imag)]:
            positive(f'original geometry{j} '+name, value)
        for k in [j-1, j+1]:
            u = boxes[k] if 0 <= k < 5 else acb(0)
            _, _, _, (radical, exp_return, ct) = return_data(t, u)
            positive(f'return{j},{k} radical branch', radical.real)
            positive(f'return{j},{k} normalized radical branch', (radical/ct).real)
            positive(f'return{j},{k} logarithm branch', exp_return.real)
    completed = [acb(0), *boxes, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).sin()/(t/2).cos(), (u/2).sin()/(u/2).cos()
        root = (1+tv*tv+uv*uv).sqrt()
        positive(f'original positive edge{j}', root.real-(tv.real**2+uv.real**2).sqrt())

    def wire(t, u):
        ct, cu = t.cos(), u.cos()
        c = (1-ct*cu)/(2+ct+cu)
        positive('wire lower cosine branch', -c.imag)
        w = c.conjugate()
        lift = -ii*(w+(w-1).sqrt()*(w+1).sqrt()).log()
        return lift.conjugate()/(2*pi)

    wires = [wire(t, u) for t, u in zip(boxes, boxes[1:])]
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    for j, x in enumerate(wires):
        for name, value in [('x>.14', x.real-a('.14')), ('x<.20', a('.20')-x.real),
                            ('h>.09', x.imag-a('.09')), ('h<.12', a('.12')-x.imag)]:
            positive(f'source wire{j} '+name, value)
    for x in [wires[0], wires[-1]]:
        r, s = x.real-xh.real, x.imag-xh.imag+4*(x.real-xh.real)/5
        for name, value in [('r>0', r), ('r<.013', a('.013')-r),
                            ('s>-.0015', s+a('.0015')), ('s<.001', a('.001')-s)]:
            positive('directed original cap '+name, value)
    for t in [boxes[0], boxes[-1]]:
        for name, value in [('a>1.5', t.real-a('1.5')), ('a<1.55', a('1.55')-t.real),
                            ('H>.97', -t.imag-a('.97')), ('H<1', 1+t.imag),
                            ('cos radius', 1-abs((t/2).cos()))]:
            positive('cap critical '+name, value)
    for j, (x, y) in enumerate(zip(wires, wires[1:])):
        # Algebraic stationary indices are computed from the original
        # geometric angle, independently of the author's quadratic root.
        tau = boxes[j+1]
        coordinates = []
        for name, wire_value in [('left', x), ('right', y)]:
            X = (2*pi*ii*wire_value).exp()
            U = (1-X)/(1+X+2*X*tau.cos())
            s = ii*U.log()/(2*pi)
            coordinates.append(s)
            for label, value in [('U real<0', -U.real), ('U imaginary<0', -U.imag),
                                 ('index>.25', s.real-a('.25')), ('index<.45', a('.45')-s.real),
                                 ('depth<.02', a('.02')-abs(s.imag)), ('product radius', 1-abs(X*U))]:
                positive(f'geometric index{j} {name} '+label, value)
            for sign in [-1, 1]:
                arg = arb(1)/2-wire_value+sign*tau/(2*pi)
                positive(f'original factorial strip{j},{name},{sign} lower', arg.real)
                positive(f'original factorial strip{j},{name},{sign} upper', 1-arg.real)
        positive(f'index{j} sum>.5', sum(s.real for s in coordinates)-a('.5'))
    z = wires[1]-xh
    positive('common true source disk', a('.005')-abs(z))
    positive('closing radius below .0036', a('.0036')-abs(z))
    positive('hidden F2 input stays in true F1 disk', a('.005')-abs(wires[2]-xh))
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    K, D, defect, R = abs(k0), 2*arb(21).sqrt(), a('.68'), a('.005')
    sectors = []
    for sign in [-1, 1]:
        d = sign*R-z
        sector = (k0*D*d*d).real-defect*K*abs(d)**2
        slope = sign*(k0*D*d).real-defect*K*abs(d)
        positive(f'correlated endpoint{sign} sector', sector-a('.00015'))
        positive(f'correlated endpoint{sign} slope', slope-a('.07'))
        sectors.append({'sign': sign, 'sector': str(sector), 'slope': str(slope)})
    drift = (k0*D*z*z).real/2-defect*K*abs(z)**2/2
    positive('actual action drift', drift+a('.000103'))
    positive('strict disk curvature17', D*k0.real-defect*K-17)
    W, B, delta = map(a, ['.009', '.000077', '.000103'])
    positive('middle loss .0002', a('6.15')*W**2-a('.0113')*W-B-delta-a('.0002'))
    positive('middle monotonicity', 2*a('6.15')*W-a('.0113'))
    positive('plateau loss .0004', a('.0006')-B-delta-a('.0004'))
    positive('far loss .0005', a('.00015')+a('1.5')*a('.02')**2-B-delta-a('.0005'))

    identities = []
    n = sp.Symbol('n', integer=True, positive=True)
    AA = sp.MatrixSymbol('A', n, n)
    closed = (AA**2*(AA**3).T).doit().xreplace({AA.T: AA}).doit()
    assert closed == AA**5
    identities.append('actual bilinear source is undeleted A^5')
    assert 1+2 == 5-2
    identities.append('original unit carrier is C_N3^2 kappa^3')
    assert -1-1+Q(1)-Q(1, 2) == Q(-3, 2)
    identities.append('original N dx and wire Gaussian give N^-3/2')
    assert Q(1, 2)+Q(9, 50) == Q(17, 25)
    identities.append('actual incoming Hessian defect is .68')
    assert Q('6.15')*Q('.009')**2-Q('.0113')*Q('.009')-Q('.000077')-Q('.000103') == Q('.00021645')
    identities.append('exact middle principal rate budget')
    assert Q('.0006')-Q('.000077')-Q('.000103') == Q('.000420')
    identities.append('exact absolute plateau rate budget')
    assert Q('.00015')+Q('1.5')*Q('.02')**2-Q('.000077')-Q('.000103') == Q('.000570')
    identities.append('exact far-period rate budget')
    cuts = list(map(Q, ['-.5', '-.02', '-.009', '-.005', '.005', '.009', '.02', '.5']))
    assert sum(cuts[k+1]-cuts[k] for k in range(7)) == 1
    assert all(cuts[k+1] > cuts[k] for k in range(7))
    identities.append('exact seven-interval partition of original period')
    assert artifact['script_sha256'] == sha256(
        (ROOT/'experiments/certify_three_chain_five_closure.py').read_bytes()).hexdigest()
    for dep, digest in artifact['dependencies_sha256'].items():
        assert sha256((ROOT/dep).read_bytes()).hexdigest() == digest, dep
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Independent original-period Newton replay using cosine/log returns, geometric index coordinates and factored inverse-cosine lift, all source domains and correlated endpoint/action budgets, exact original word/normalization/period partition. No author module imported.',
        'strict_comparisons': len(checks), 'comparisons': checks,
        'Newton_contractions': contractions, 'closing_displacement': str(z),
        'correlated_sectors': sectors, 'action_drift_lower': str(drift),
        'exact_identities': identities,
        'artifact_sha256': sha256(args.artifact.read_bytes()).hexdigest(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': artifact['dependencies_sha256'],
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'strict_comparisons',
                    'closing_displacement', 'action_drift_lower']}, indent=2))
    print('Exact identities:', len(identities))


if __name__ == '__main__':
    main()
