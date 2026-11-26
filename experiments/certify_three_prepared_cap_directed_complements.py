#!/usr/bin/env python3
"""Directed output complements of the literal L40 prepared-cap source.

This certificate is upper-only. It does not certify a cap packet or a
four-vertex closing coefficient. Earlier source artifacts are unchanged.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json
import time
from flint import arb, acb, ctx
from certify_three_vertex_bidisk_packet import phase

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)
CHART = {'real': ['-3/500', '7/1000'], 'imaginary': ['-33/8000', '0']}


def scalar(q):
    return arb(q.numerator)/q.denominator if isinstance(q, Q) else arb(q)


def interval(a, b):
    return scalar(a).union(scalar(b))


def mag(z):
    return max(abs(z.lower()), abs(z.upper()))


def outgoing(face, z):
    base = acb(arb(1)/6, arb(2).log()/(2*arb.pi()))
    if face < 2:
        return (base+arb(-6 if face == 0 else 7)/1000
                +I*(-arb(33)/8000+arb(33)/8000*z), I*arb(33)/8000)
    return (base-arb(6)/1000+arb(13)/1000*z
            +I*(-arb(33)/8000 if face == 2 else arb(0)), acb(arb(13)/1000))


def coordinates(key, p):
    kind, k0, k1, region = key
    pi = arb.pi()
    if kind == 'join':
        lo = arb(10135867)/10**8
        dx = arb(2).log()/(2*pi)-lo
        x = acb(arb(7)/50 if k0 == 0 else arb(1)/5, lo+dx*p[0])
        face, swap = k1, False
        ranges = [(Q(0), Q(1, 40), Q(1, 40), Q(9, 20)),
                  (Q(1, 40), Q(9, 20), Q(0), Q(9, 20))]
    else:
        dx = arb(3)/50
        x = acb(arb(7)/50+dx*p[0], interval(Q(10135867, 10**8), Q(10135871, 10**8)))
        face, swap = k0, bool(k1)
        ranges = [(Q(0), Q(1, 40), Q(1, 40), Q(9, 20)),
                  (Q(1, 40), Q(1, 4), Q(0), Q(9, 20)),
                  (Q(9, 20), Q(9, 20), Q(0), Q(9, 20))]
    y, dy = outgoing(face, p[1])
    sl, sr, tl, tr = ranges[region]
    ds, dt = scalar(sr-sl), scalar(tr-tl)
    s, t = scalar(sl)+ds*p[2], scalar(tl)+dt*p[3]
    if swap:
        s, t = t, s
    return x, y, (2*pi*I*x).exp(), (2*pi*I*y).exp(), s, t, dx, dy, ds, dt, swap


def value(key, p):
    x, y, X, Y, s, t, *_ = coordinates(key, p)
    return (phase(acb(s), acb(t), X, Y)-arb.pi()*I*(x+y)).real


def evaluate(key, box):
    p = [interval(a, b) for a, b in box]
    c = [scalar((a+b)/2) for a, b in box]
    widths = [scalar((b-a)/2) for a, b in box]
    x, y, X, Y, s, t, dx, dy, ds, dt, swap = coordinates(key, p)
    pi = arb.pi()
    U, V = (-2*pi*I*s).exp(), (-2*pi*I*t).exp()
    fx = 2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I
    fy = 2*pi*I*t+(1-Y*V).log()-(1-Y).log()-pi*I
    fs = X.log()+(1-U*V).log()-(1-X*U).log()
    ft = Y.log()+(1-U*V).log()-(1-Y*V).log()
    if swap:
        fs, ft = ft, fs
    gradients = [-dx*fx.imag if key[0] == 'join' else dx*fx.real,
                 (dy*fy).real, ds*fs.real, dt*ft.real]
    costs = [w*mag(g) for w, g in zip(widths, gradients)]
    upper = value(key, c)+sum(costs)
    threshold = arb(6471 if key[0] == 'join' else 6455)/10000
    return upper < threshold, costs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=160)
    ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-three-prepared-cap-directed-complements.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    keys = [('join', *k) for k in product(range(2), range(4), range(2))]
    keys += [('complement', *k) for k in product(range(4), range(2), range(3))]
    visited, domains = 0, []
    for key in keys:
        todo = [('', tuple((Q(0), Q(1)) for _ in range(4)))]
        leaves = []
        while todo:
            path, box = todo.pop()
            visited += 1
            try:
                ok, costs = evaluate(key, box)
            except (ValueError, ZeroDivisionError):
                ok, costs = False, None
            if ok:
                leaves.append(path)
                continue
            if costs is not None and all(c.is_finite() for c in costs):
                axis = max(range(4), key=lambda j: float(costs[j].upper()))
            else:
                weights = [.009 if key[0] == 'join' else .06, .013,
                           0 if key[0] == 'complement' and key[-1] == 2 else .45, .45]
                axis = max(range(4), key=lambda j: float(box[j][1]-box[j][0])*weights[j])
            lo, hi = box[axis]
            assert hi-lo > Q(1, 2**24), (key, box)
            mid = (lo+hi)/2
            for side, ends in enumerate(((lo, mid), (mid, hi))):
                child = list(box)
                child[axis] = ends
                todo.append((path+str(2*axis+side), tuple(child)))
            assert visited < 800000, 'Incomplete coverage; no result saved.'
        domains.append({'domain': list(key), 'dimension': 4, 'leaves': leaves})
        print(key, len(leaves), 'visited', visited, flush=True)
    pi, r = arb.pi(), arb(27)/50
    margins = [r-(-2*pi*arb(10135867)/10**8).exp(),
               r-(33*pi/4000).exp()/2,
               (1+r*r).sqrt()-2*r, 1-r-r*pi/4,
               arb(3)/4-arb(7)/8+arb(7)/50,
               arb(1)/6-arb(6)/1000-arb(7)/50,
               arb(1)/5-arb(1)/6-arb(7)/1000]
    assert all(m > 0 for m in margins)
    deps = ['notes/research_three_prepared_cap_directed_complements.md',
            'notes/research_three_prepared_cap_join_vertex.md',
            'notes/research_three_prepared_cap_real_complement.md',
            'notes/research_three_vertex_bidisk_packet.md',
            'experiments/certify_three_vertex_bidisk_packet.py']
    counts = {kind: sum(len(d['leaves']) for d in domains if d['domain'][0] == kind)
              for kind in ('join', 'complement')}
    result = {'status': 'passed', 'precision_bits': args.precision,
              'outgoing_chart': CHART, 'deleted_corner_fraction': '1/40',
              'thresholds': {'join': '6471/10000', 'complement': '6455/10000'},
              'domains': domains, 'domain_count': len(domains),
              'leaf_count': sum(counts.values()), 'leaves_by_kind': counts,
              'visited': visited, 'scalar_margins': [str(m) for m in margins],
              'elapsed_seconds': time.monotonic()-start,
              'scope': 'Upper bounds for original L40 summands on exactly the directed outgoing rectangle; cap currents and nonzero source coefficients remain separate.',
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'domain_count', 'leaves_by_kind', 'visited', 'elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
