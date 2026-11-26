#!/usr/bin/env python3
"""Certify all nonprincipal fixed-contour rates for the mixed source.

The exact rational contour multipliers are derived in the companion
residue-assembly note. Here every decision uses outward-rounded balls
on an exact rational partition. The corner and omitted endpoint-strip
estimates are elementary and are written separately in the proof.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx

import verify_mixed_two_crossing_horizontal as horizontal


CUT = F(1, 100000)
THRESHOLD = F(9, 8)


def q(x):
    return horizontal.q(x)


def interval(pair):
    return horizontal.interval(pair)


def positive(x):
    return (x+abs(x))/2


def real_j(a, height):
    height = abs(height)
    # A ball near the Li_2 branch point is enclosed by a proved real
    # horizontal modulus, not by selecting a numerical branch there.
    for k in (0, 1):
        if a.contains(k):
            distance = abs(a-k).upper()
            if distance < q(F(1, 4)):
                if distance == 0:
                    return PI*height*(k-q(F(1, 2)))
                error = distance*(10-distance.log())
                return PI*height*(k-q(F(1, 2)))+arb(0, error.upper())
    z = acb(-2*PI*height, 2*PI*a).exp()
    return -z.polylog(2).imag/(2*PI)-PI*height*(1-2*a)/2


def phase(a, b, s, t):
    return (real_j(a+b, s+t)-3*real_j(a, s)
            -6*real_j(b, t)+real_j(2*b, 2*t)
            -PI*(b*s+(a-b-q(F(1, 2)))*t))


def grouped(b, s, t, sign):
    value = (real_j(b, s+t)+3*PI*abs(s)/2
             -6*real_j(b, t)+real_j(2*b, 2*t)
             -PI*b*s+PI*(b+q(F(1, 2)))*t)
    if sign > 0:
        exponent = 2*PI*positive(-2*s-t)
    else:
        exponent = 2*PI*(s+positive(s-t))
    return value+exponent


def x_endpoint(a, t, b, sign):
    s = sign*HX
    value = (real_j(a+b, s+t)-3*real_j(a, s)
             +(2 if b == 0 else 1)*PI*abs(t)
             -PI*(b*s+(a-b-q(F(1, 2)))*t))
    return value-2*PI*(positive(t)+(HX if sign < 0 else 0))


def evaluate(name, box):
    a, u = interval(box[0]), interval(box[1])
    if name.startswith('grouped'):
        sign = -1 if name.endswith('negative') else 1
        s = sign*HX*u
        t = -HY if 'lower' in name else HY
        return grouped(a, s, t, sign)-(2*PI*HY if t > 0 else 0)
    if name.startswith('endpoint'):
        sign = -1 if 'negative' in name else 1
        b = q(F(1, 2)) if 'top' in name else arb(0)
        return x_endpoint(a, HY*(2*u-1), b, sign)
    sx = -1 if 'xnegative' in name else 1
    sy = 1 if 'ypositive' in name else -1
    return (phase(a, u/2, sx*HX, sy*HY)
            -2*PI*((HX if sx < 0 else 0)+(HY if sy > 0 else 0)))


def verify(name, max_boxes):
    first = (CUT, F(1, 2)-CUT) if name.startswith('grouped') else (F(0), F(1))
    original = (first, (F(0), F(1)))
    queue = [(original, 0)]
    count = accepted = deepest = 0
    area = F(0)
    digest = hashlib.sha256()
    largest = None
    while queue:
        box, depth = queue.pop()
        count += 1
        if count > max_boxes:
            raise RuntimeError((name, 'maximum box count exceeded'))
        value = evaluate(name, box)
        if value.is_finite() and value < q(THRESHOLD):
            accepted += 1
            deepest = max(deepest, depth)
            area += (box[0][1]-box[0][0])*(box[1][1]-box[1][0])
            digest.update((repr(box)+'\n').encode())
            upper = value.upper()
            if largest is None or upper > largest:
                largest = upper
            continue
        widths = [b-a for a, b in box]
        axis = int(widths[1] > widths[0])
        middle = sum(box[axis])/2
        for pair in ((box[axis][0], middle), (middle, box[axis][1])):
            child = list(box)
            child[axis] = pair
            queue.append((tuple(child), depth+1))
    expected = (first[1]-first[0])
    if area != expected:
        raise ArithmeticError((name, area, expected))
    print(f'{name}: {accepted} accepted rectangles.', flush=True)
    return {'name': name, 'examined_rectangles': count, 'accepted_rectangles': accepted,
            'maximum_depth': deepest, 'exact_covered_area': str(area),
            'largest_upper_bound': str(largest),
            'accepted_rectangle_sha256': digest.hexdigest()}


def main():
    global PI, HX, HY
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=128)
    parser.add_argument('--max-boxes', type=int, default=1000000)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    horizontal.setup(args.precision)
    PI, HX, HY = horizontal.PI, horizontal.HX, -horizontal.HY
    if not (HX > 0 and HX < HY and HY < q(F(79, 1000))):
        raise ArithmeticError('Exact height enclosure failed')
    names = [f'grouped_{side}_{sign}' for side in ('lower', 'upper')
             for sign in ('negative', 'positive')]
    names += [f'endpoint_{side}_{sign}' for side in ('bottom', 'top')
              for sign in ('negative', 'positive')]
    names += ['horizontal_xnegative_ynegative', 'horizontal_xpositive_ypositive',
              'horizontal_xnegative_ypositive']
    records = [verify(name, args.max_boxes) for name in names]
    result = {'scope': 'Certified nonprincipal fixed-contour phase bounds; '
                       'requires the exact residue assembly and analytic endpoint allowances.',
              'precision_bits': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'horizontal_verifier_sha256': hashlib.sha256(
                  Path(horizontal.__file__).read_bytes()).hexdigest(),
              'threshold': str(THRESHOLD), 'checks': records}
    content = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.', flush=True)
    else:
        print(content)


if __name__ == '__main__':
    main()
