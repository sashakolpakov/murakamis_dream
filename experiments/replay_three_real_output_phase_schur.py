#!/usr/bin/env python3
"""Independent exact-cover and unsummed-derivative Schur replay.

No author module or automatic-differentiation implementation is imported.
The original index Schur complement is simplified in stationary U,V;
symbolic partial derivatives and the implicit index equations give its
holomorphic wire derivatives. Exact rational sweeps check the full cover.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time

import sympy as sp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-real-output-phase-schur-replay.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    path = ROOT/'repro/results/research-three-real-output-phase-schur.json'
    record = json.loads(path.read_text())
    assert record['status'] == 'passed'

    # Derive the normalized retained Hessian from the original two-index
    # phase, then differentiate rational functions of stationary roots.
    u, v, c, q = sp.symbols('u v c q')
    X, Y = 1/(1+u-u*v), 1/(1+v-u*v)
    T, root = 1-u*v, 1-u-v
    a, l, r = u*v/T, X*u/(1-X*u), Y*v/(1-Y*v)
    index = sp.Matrix([[a-l, a], [a, a-r]])
    mixed = sp.diag(1/(1-X*u), 1/(1-Y*v))
    direct = sp.diag(X/(1-X)-l, Y/(1-Y)-r)
    original = direct-mixed.T*index.inv()*mixed
    target = sp.Matrix([
        [(1-u)/T*(1/(1-X)+1/(X*X*u*root)), 1/(X*Y*T*root)],
        [1/(X*Y*T*root), (1-v)/T*(1/(1-Y)+1/(Y*Y*v*root))]])
    identities = []
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        assert sp.factor(original[i, j]-target[i, j]) == 0
        identities.append(f'original unsummed Schur entry {i}{j}')
    entries = [sp.factor(c*target[i, j]) for i, j in [(0, 0), (0, 1), (1, 1)]]
    derivatives = [sp.factor(sp.diff(f, variable))
                   for variable in [u, v] for f in entries]
    evaluate = sp.lambdify((u, v, c), entries+derivatives, modules='math', cse=True)
    # The root differential is obtained directly from the two stationarity
    # equations U(1-V)=X^-1-1, V(1-U)=Y^-1-1.
    stationarity = sp.Matrix([[1-v, -u], [-v, 1-u]])
    expected = sp.Matrix([[1-u, u], [v, 1-v]])/root
    assert sp.simplify(stationarity*expected-sp.eye(2)) == sp.zeros(2)
    identities.append('implicit stationary-root inverse')
    homogeneous = {u:-(1+sp.I*sp.sqrt(3))/2,
                   v:-(1+sp.I*sp.sqrt(3))/2,
                   c:-sp.Rational(3, 2)+sp.I*sp.sqrt(3)}
    for f, value in zip(entries, [-5, 2, -5]):
        assert sp.simplify(f.subs(homogeneous)-value) == 0
    identities.append('three homogeneous normalized Hessian entries')
    assert sp.simplify(-5+sp.sqrt(21)-4/(-5-sp.sqrt(21))) == 0
    identities.append('homogeneous correlated Schur cancellation')
    E, B, D = sp.symbols('E B D')
    separate = (4*E+E*E)/(D-B-E)+4*(B+E)/(D*(D-B-E))
    assert sp.factor(separate-((2+E)**2/(D-B-E)-4/D)) == 0
    identities.append('complex-disk quotient subtraction')

    pi, ii = arb.pi(), acb(0, 1)
    sq, rho = arb(21).sqrt(), (5-arb(21).sqrt())/2
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    coefficient = acb(-arb(3)/2, arb(3).sqrt())  # 2 pi i / k0, exactly.

    def rat(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def interval(pair):
        lo, hi = pair
        return arb(rat((lo+hi)/2), rat((hi-lo)/2))

    scalars = []

    def positive(name, value):
        assert value > 0, (name, value)
        scalars.append({'name': name, 'strict_margin': str(value)})

    radius, width, height, b, e = map(rat, ['.005', '.009', '.0065', '.18', '.26'])
    D = 5+sq
    e0 = rat('.1')
    # Evaluate the two separate error terms, not the author's simplified
    # difference of homogeneous quotients.
    disk_error = e0+(4*e0+e0*e0)/(D-b-e0)+4*(b+e0)/(D*(D-b-e0))
    positive('disk outgoing derivative below .16', rat('.16')-disk_error)
    positive('real kernel Hessian defect below .26', e-18*(radius+width))
    positive('real critical contraction below .05', rat('.05')-rho*(b+e)/2)
    positive('real critical disk strict self-map', radius-rho*width-rho*(height+b*radius+e*(radius+width))/2)
    rstar = (rho*(1+e/2)*width+rho*height/2)/(1-rho*(b+e)/2)
    resstar = rho*(height+e*width+(b+e)*rstar)/2
    positive('real critical modulus below .002936', rat('.002936')-rstar)
    positive('critical residual below .00106', rat('.00106')-resstar)
    positive('disk critical strict self-map', radius-rho*radius-rho*(height+b*radius+2*e0*radius)/2)
    Z = rat('1.05')*rho/(1-rat('.3')*rho)
    positive('center-gradient contraction below one', 1-Z)

    domain = [(Q(-9, 1000), Q(9, 1000)),
              (Q(-53, 50000), Q(53, 50000)),
              (Q(-53, 50000), Q(53, 50000))]
    assert record['domain'] == [[str(a), str(b)] for a, b in domain]
    boxes = [[tuple(map(Q, p)) for p in cell['box']] for cell in record['cells']]
    assert len(boxes) == record['cell_count'] == 300
    for box in boxes:
        assert len(box) == 3
        assert all(a <= lo < hi <= b for (lo, hi), (a, b) in zip(box, domain))

    # Independent geometric coverage: sweep every open w slab, then every
    # xi slab, and require eta multiplicity exactly one. Closed boxes then
    # also cover every boundary. No stored binary addresses are used.
    wcuts = sorted({a for box in boxes for a in box[0]})
    assert (wcuts[0], wcuts[-1]) == domain[0]
    slab_count = 0
    for left, right in zip(wcuts, wcuts[1:]):
        wm = (left+right)/2
        active = [box for box in boxes if box[0][0] < wm < box[0][1]]
        xcuts = sorted({a for box in active for a in box[1]})
        assert (xcuts[0], xcuts[-1]) == domain[1]
        for lo, hi in zip(xcuts, xcuts[1:]):
            xm = (lo+hi)/2
            events = {}
            for box in active:
                if box[1][0] < xm < box[1][1]:
                    a, bnd = box[2]
                    events[a] = events.get(a, 0)+1
                    events[bnd] = events.get(bnd, 0)-1
            cuts = sorted(events)
            assert (cuts[0], cuts[-1]) == domain[2]
            multiplicity = 0
            for a, bnd in zip(cuts, cuts[1:]):
                multiplicity += events[a]
                assert multiplicity == 1 and a < bnd
                slab_count += 1
            multiplicity += events[cuts[-1]]
            assert multiplicity == 0

    def phase(z, w):
        X, Y = (2*pi*ii*(xh+z)).exp(), (2*pi*ii*(xh+w)).exp()
        alpha, beta = 1/X-1, 1/Y-1
        disc = 1-2*(alpha+beta)+(alpha-beta)**2
        root = disc.sqrt()
        U, V = (1+alpha-beta-root)/2, (1-alpha+beta-root)/2
        vals = evaluate(U, V, coefficient)
        xx, xy, yy = vals[:3]
        xxu, xyu, yyu, xxv, xyv, yyv = vals[3:]
        # Chain rule through the independent implicit-root inverse above.
        Uz, Vz = -2*pi*ii*(1-U)/(X*root), -2*pi*ii*V/(X*root)
        Uw, Vw = -2*pi*ii*U/(Y*root), -2*pi*ii*(1-V)/(Y*root)
        den = xx-sq
        Bu = yyu-2*xy*xyu/den+xy*xy*xxu/den**2
        Bv = yyv-2*xy*xyv/den+xy*xy*xxv/den**2
        base = yy+sq-xy*xy/den
        return base, Bu*Uz+Bv*Vz, Bu*Uw+Bv*Vw, xx, xy, disc, U, V, X, Y

    pending = [(box, 0) for box in boxes]
    leaves, refinements = 0, 0
    largest = arb(0)
    smallest = None
    while pending:
        box, depth = pending.pop()
        w, xi, eta = map(interval, box)
        z = rho*w+acb(xi, eta)
        _, Bz, Bw, xx, xy, disc, U, V, X, Y = phase(z, w)
        wc, xc, yc = [rat((a+bnd)/2) for a, bnd in box]
        center = phase(rho*wc+acb(xc, yc), wc)[0]
        radii = [arb(0, rat((hi-lo)/2)) for lo, hi in box]
        base = center+(rho*Bz+Bw)*radii[0]+Bz*radii[1]+ii*Bz*radii[2]
        denom = abs(xx-sq)
        perturb = abs(xy)**2*b/(denom*(denom-b))
        upper = abs(base)+perturb
        good = (disc.imag > 0 and radius-abs(z) > 0 and denom > b
                and U.real < 0 and U.imag < 0 and V.real < 0 and V.imag < 0
                and abs(X*U) < 1 and abs(Y*V) < 1 and upper < rat('.15'))
        if not good:
            assert depth < 12, (box, upper)
            axis = max(range(3), key=lambda j: box[j][1]-box[j][0])
            lo, hi = box[axis]
            mid = (lo+hi)/2
            left, right = list(box), list(box)
            left[axis], right[axis] = (lo, mid), (mid, hi)
            pending.extend([(right, depth+1), (left, depth+1)])
            refinements += 1
            continue
        leaves += 1
        largest = max(largest, upper.upper())
        margin = (rat('.15')-upper).lower()
        smallest = margin if smallest is None else min(smallest, margin)

    for f, h in record['dependencies_sha256'].items():
        assert sha256((ROOT/f).read_bytes()).hexdigest() == h, f
    assert sha256((ROOT/'experiments/certify_three_real_output_phase_schur.py').read_bytes()).hexdigest() == record['script_sha256']
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'author_boxes': len(boxes), 'independent_sweep_slabs': slab_count,
        'exact_multiplicity_one_cover': True,
        'independent_refinements': refinements, 'accepted_replay_boxes': leaves,
        'exact_symbolic_identities': identities,
        'scalar_comparisons': scalars,
        'maximum_Schur_plus_incoming_perturbation': str(largest),
        'minimum_margin_below_3_20': str(smallest),
        'method': 'Original unsummed index Schur matrix; symbolic U,V partial derivatives and independent implicit-root Jacobian; centered holomorphic mean-value bounds; exact rational geometric sweep, no author imports.',
        'scope': 'Analytic real-output Schur bound and complex-disk quotient/self-map comparisons only; no source-tail or entrance conclusion.',
        'artifact_sha256': sha256(path.read_bytes()).hexdigest(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic()-start,
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
