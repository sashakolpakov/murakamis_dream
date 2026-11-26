#!/usr/bin/env python3
"""Independent complete-cover replay of the directed L40 complements.

Uses the negative-frequency primitive and sine-log derivatives. No author
module is imported; chart maps, index orders and targets are defined here.
"""
from fractions import Fraction as R
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json
import time
from flint import arb, acb, ctx
from replay_three_vertex_bidisk_packet import action, partition

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)


def a(q):
    return arb(q.numerator)/q.denominator if isinstance(q, R) else arb(q)


def iv(x, y):
    return a(x).union(a(y))


def absupper(z):
    return max(abs(z.lower()), abs(z.upper()))


def data(key, p):
    kind, k0, k1, k2 = key
    pi = arb.pi()
    height = arb(2).log()/(2*pi)
    if kind == 'join':
        span = height-arb(10135867)/10**8
        x = acb(arb(7)/50 if k0 == 0 else arb(1)/5, height-span*(1-p[0]))
        f, swap = k1, False
    else:
        span = arb(3)/50
        x = acb((arb(7)+3*p[0])/50, iv(R(10135867, 10**8), R(10135871, 10**8)))
        f, swap = k0, bool(k1)
    base = acb(arb(1)/6, height)
    if f in (0, 1):
        y = base+arb(13*f-6)/1000-I*33*(1-p[1])/8000
        yp = I*33/8000
    else:
        y = base+(13*p[1]-6)/1000-I*arb(33*(3-f))/8000
        yp = acb(arb(13)/1000)
    if k2 == 0:
        s, t = p[2]/40, (1+17*p[3])/40
        sp, tp = arb(1)/40, arb(17)/40
    elif kind == 'join':
        s, t = (1+17*p[2])/40, arb(9)*p[3]/20
        sp, tp = arb(17)/40, arb(9)/20
    elif k2 == 1:
        s, t = (1+9*p[2])/40, arb(9)*p[3]/20
        sp, tp = arb(9)/40, arb(9)/20
    else:
        s, t = arb(9)/20, arb(9)*p[3]/20
        sp, tp = arb(0), arb(9)/20
    if swap:
        s, t = t, s
    return x, y, (2*pi*I*x).exp(), (2*pi*I*y).exp(), s, t, span, yp, sp, tp, swap


def check(key, box):
    p = [iv(lo, hi) for lo, hi in box]
    center = [a((lo+hi)/2) for lo, hi in box]
    widths = [a((hi-lo)/2) for lo, hi in box]
    pi = arb.pi()
    x, y, X, Y, s, t, xp, yp, sp, tp, swap = data(key, p)
    U, V = (-2*pi*I*s).exp(), (-2*pi*I*t).exp()
    common = (2*(pi*(s+t)).sin()).log()+I*pi*(arb(1)/2-s-t)
    fs = common+X.log()-(1-X*U).log()
    ft = common+Y.log()-(1-Y*V).log()
    fx = 2*pi*I*s+(1-X*U).log()-(1-X).log()-pi*I
    fy = 2*pi*I*t+(1-Y*V).log()-(1-Y).log()-pi*I
    if swap:
        fs, ft = ft, fs
    derivatives = [-xp*fx.imag if key[0] == 'join' else xp*fx.real,
                   (yp*fy).real, sp*fs.real, tp*ft.real]
    xc, yc, XX, YY, sc, tc, *_ = data(key, center)
    upper = (action(sc, tc, XX, YY)-pi*I*(xc+yc)).real
    upper += sum(w*absupper(g) for w, g in zip(widths, derivatives))
    assert upper < arb(6471 if key[0] == 'join' else 6455)/10000, (key, box, upper)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--artifact', type=Path, default=ROOT/'repro/results/research-three-prepared-cap-directed-complements.json')
    ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-three-prepared-cap-directed-complements-replay.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    record = json.loads(args.artifact.read_text())
    assert record['status'] == 'passed'
    assert record['outgoing_chart'] == {'real': ['-3/500', '7/1000'], 'imaginary': ['-33/8000', '0']}
    assert record['deleted_corner_fraction'] == '1/40'
    assert record['thresholds'] == {'join': '6471/10000', 'complement': '6455/10000'}
    expected = {('join', *k) for k in product(range(2), range(4), range(2))}
    expected |= {('complement', *k) for k in product(range(4), range(2), range(3))}
    seen, counts = set(), {'join': 0, 'complement': 0}
    for domain in record['domains']:
        key = tuple(domain['domain'])
        assert key in expected and key not in seen
        seen.add(key)
        assert domain['dimension'] == 4
        for box in partition(domain['leaves'], 4):
            check(key, box)
            counts[key[0]] += 1
    assert seen == expected and len(seen) == record['domain_count']
    assert counts == record['leaves_by_kind'] and sum(counts.values()) == record['leaf_count']
    pi, r = arb.pi(), arb(27)/50
    margins = [r-(-2*pi*arb(10135867)/10**8).exp(), r-(33*pi/4000).exp()/2,
               (1+r*r).sqrt()-2*r, 1-r-r*pi/4,
               arb(3)/4-arb(7)/8+arb(7)/50,
               arb(1)/6-arb(6)/1000-arb(7)/50,
               arb(1)/5-arb(1)/6-arb(7)/1000]
    assert all(m > 0 for m in margins)
    for path, digest in record['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    assert sha256((ROOT/'experiments/certify_three_prepared_cap_directed_complements.py').read_bytes()).hexdigest() == record['script_sha256']
    result = {'status': 'passed', 'precision_bits': args.precision,
              'domain_count': len(seen), 'leaves_by_kind': counts,
              'leaf_count': sum(counts.values()), 'exact_binary_cover': True,
              'scalar_comparisons': len(margins),
              'phase': 'Independent negative-frequency primitive and sine-log derivatives; no author imports.',
              'outgoing_chart': record['outgoing_chart'],
              'elapsed_seconds': time.monotonic()-start,
              'artifact_sha256': sha256(args.artifact.read_bytes()).hexdigest(),
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'independent_helper_sha256': sha256((ROOT/'experiments/replay_three_vertex_bidisk_packet.py').read_bytes()).hexdigest(),
              'dependencies_sha256': record['dependencies_sha256']}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'domain_count', 'leaves_by_kind', 'leaf_count', 'scalar_comparisons']}, indent=2))


if __name__ == '__main__':
    main()
