#!/usr/bin/env python3
"""Certify the mixed two-crossing horizontal phase and its unique maximum.

All decisions use outward-rounded Arb/Acb balls on rational boxes.
The cubic saddle is defined by exact radicals. This verifies a horizontal
phase inequality, not deformation of the original lattice current.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx


LOCAL = ((F(18, 100), F(27, 100)), (F(17, 100), F(27, 100)))
THRESHOLD = F(49, 40)


def q(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def interval(pair):
    return q(pair[0]).union(q(pair[1]))


def setup(precision):
    global PI, X, Y, XS, YS, HX, HY
    ctx.prec = precision
    PI = arb.pi()
    aa, bb = arb(43)/54, (arb(59)/108).sqrt()
    negative_root = -(aa-bb).root(3)-(aa+bb).root(3)-arb(2)/3
    real = (-2-negative_root)/2
    imag = (-1/negative_root-real**2).sqrt()
    X = acb(real, imag)
    Y = 1+2*X+2*X**2
    XS = X.log()/acb(0, 2*PI)
    YS = Y.log()/acb(0, 2*PI)
    HX, HY = XS.imag, YS.imag
    if not (HX > 0 and HY < 0 and HX+HY < 0):
        raise ArithmeticError('Height signs are not certified')


def real_j(a, height):
    height = abs(height)
    zz = acb(-2*PI*height, 2*PI*a).exp()
    return -zz.polylog(2).imag/(2*PI)-PI*height*(1-2*a)/2


def rate(a, b):
    return (real_j(a+b, HX+HY)-3*real_j(a, HX)
            -6*real_j(b, HY)+real_j(2*b, 2*HY)
            -PI*(b*HX+(a-b-q(F(1, 2)))*HY))


def real_cot(a, height):
    return (2*PI*a).sin()/((2*PI*height).cosh()-(2*PI*a).cos())


def real_tan(a, height):
    return (2*PI*a).sin()/((2*PI*height).cosh()+(2*PI*a).cos())


def check_local():
    parts = 16
    worst = None
    for i in range(parts):
        for j in range(parts):
            aa = tuple(LOCAL[0][0]+(LOCAL[0][1]-LOCAL[0][0])*F(i+k, parts)
                       for k in (0, 1))
            bb = tuple(LOCAL[1][0]+(LOCAL[1][1]-LOCAL[1][0])*F(j+k, parts)
                       for k in (0, 1))
            a, b = interval(aa), interval(bb)
            A, B = real_cot(a, HX), real_cot(b, HY)
            C, D = real_cot(a+b, HX+HY), real_tan(b, HY)
            margins = (3*A-C-abs(C), 4*B+2*D-C-abs(C))
            for margin in margins:
                if not margin > q(F(1, 2)):
                    raise ArithmeticError(('Local Hessian bound', aa, bb, margin))
                lower = margin.lower()
                if worst is None or lower < worst:
                    worst = lower
    for coordinate, pair in zip((XS.real, YS.real), LOCAL):
        if not (coordinate > q(pair[0]) and coordinate < q(pair[1])):
            raise ArithmeticError('The saddle is outside the local box')
    xx, yy = XS, YS
    wx = ((2*(PI*(xx+yy)).sin()).log()
          -3*(2*(PI*xx).sin()).log()+acb(0, PI)*yy)
    wy = ((2*(PI*(xx+yy)).sin()).log()
          -6*(2*(PI*yy).sin()).log()
          +2*(2*(2*PI*yy).sin()).log()
          +acb(0, PI)*(xx-yy-q(F(1, 2))))
    if not (abs(wx.imag) < 1 and abs(wy.imag) < 1):
        raise ArithmeticError('Logarithmic lifts not isolated')
    action = rate(XS.real, YS.real)
    if not action > q(F(613, 500)):
        raise ArithmeticError('Selected action lower bound')
    return {'rational_subrectangles': parts**2,
            'hessian_margin_over_pi': str(worst),
            'selected_action_enclosure': str(action),
            'selected_action_lower_bound': '613/500',
            'x': str(XS), 'y': str(YS),
            'logarithmic_gradient_enclosures': [str(wx), str(wy)]}


def inside_local(box):
    return all(a >= c and b <= d for (a, b), (c, d) in zip(box, LOCAL))


def verify_global(max_boxes):
    queue = [(((F(0), F(1)), (F(0), F(1, 2))), 0)]
    examined = accepted = local = depth_max = 0
    area = F(0)
    digest = hashlib.sha256()
    worst = None
    while queue:
        box, depth = queue.pop()
        examined += 1
        if examined > max_boxes:
            raise RuntimeError('Maximum rectangle count exceeded')
        covered = inside_local(box)
        value = None if covered else rate(interval(box[0]), interval(box[1]))
        if covered or (value.is_finite() and value < q(THRESHOLD)):
            accepted += 1
            local += int(covered)
            depth_max = max(depth_max, depth)
            area += (box[0][1]-box[0][0])*(box[1][1]-box[1][0])
            digest.update((repr(box)+':'+str(covered)+'\n').encode())
            if not covered:
                upper = value.upper()
                if worst is None or upper > worst:
                    worst = upper
            continue
        widths = [pair[1]-pair[0] for pair in box]
        axis = int(widths[1] > widths[0])
        midpoint = sum(box[axis])/2
        for pair in ((box[axis][0], midpoint), (midpoint, box[axis][1])):
            child = list(box)
            child[axis] = pair
            queue.append((tuple(child), depth+1))
    if area != F(1, 2):
        raise ArithmeticError(('Coverage area', area))
    return {'examined_rectangles': examined, 'accepted_rectangles': accepted,
            'rectangles_inside_local_box': local, 'maximum_depth': depth_max,
            'exact_covered_area': str(area), 'outside_threshold': str(THRESHOLD),
            'largest_outside_upper_bound': str(worst),
            'accepted_rectangle_sha256': digest.hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=128)
    parser.add_argument('--max-boxes', type=int, default=1000000)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    setup(args.precision)
    local = check_local()
    print('Cubic saddle and local Hessian certified.', flush=True)
    global_result = verify_global(args.max_boxes)
    result = {'scope': 'Certified horizontal phase inequality only; no original-cycle transfer is inferred.',
              'precision_bits': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'local': local, 'global': global_result}
    content = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.', flush=True)
    else:
        print(content)


if __name__ == '__main__':
    main()
