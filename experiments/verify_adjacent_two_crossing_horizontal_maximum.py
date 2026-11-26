#!/usr/bin/env python3
"""Rational interval certificate for the shifted adjacent-(2,2) action.

This verifies only the upper horizontal contour: a negative real Hessian
on one fixed rectangle and a strict action gap on its complement. It
does not estimate connecting faces, other height signs, or lattice modes.
Every acceptance decision uses outward rational interval bounds. There
is no optimizer or floating-point special function in the verifier.

Run:
  python3 experiments/verify_adjacent_two_crossing_horizontal_maximum.py \
    --output repro/results/research-adjacent-two-crossing-horizontal-maximum.json
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

if not __debug__:
    raise RuntimeError('Run without -O: the imported interval engine uses assertions')

import verify_conway_two_leaf_block_alias_certificate as arith

I, PI, SCALE = arith.I, arith.PI, arith.S
LOCAL = ((F(3, 50), F(1, 10)), (F(23, 100), F(27, 100)))
REFERENCE = (F(31, 400), F(1, 4))
GAP = F(1, 10000)
SERIES_TERMS = 40


def sqrt_fraction(value):
    value = F(value)
    if value < 0:
        raise ValueError('Negative square-root argument')
    scaled = value.numerator * SCALE * SCALE
    lower = isqrt(scaled // value.denominator)
    upper = lower if lower * lower * value.denominator == scaled else lower + 1
    return I(lower, upper, raw=True)


RX = sqrt_fraction(F(1, 8))
RY = sqrt_fraction(F(1, 7))
RXY = sqrt_fraction(F(1, 56))
RY2 = I(F(1, 7))
LOG2, LOG7 = arith.LOG2, arith.logi(7)
CX = -3 * LOG2 + LOG7 / 2
CY = (3 * LOG2 - LOG7) / 2
C0 = LOG7 / 4


def sin_pi(value):
    value = F(value) % 2
    if value == 0 or value == 1:
        return I(0)
    if value > 1:
        return -arith.sinpi(value - 1)
    return arith.sinpi(value)


def trig_point(value, cosine=False):
    return sin_pi(2 * F(value) + (F(1, 2) if cosine else 0))


def trig_range(interval, cosine=False):
    lo, hi = interval
    values = [trig_point(lo, cosine), trig_point(hi, cosine)]
    offset = F(0) if cosine else F(1, 4)
    # These are all stationary points of sine/cosine on the relevant range.
    first = (2 * (lo - offset)).__floor__() - 1
    last = (2 * (hi - offset)).__ceil__() + 1
    for index in range(first, last + 1):
        point = offset + F(index, 2)
        if lo <= point <= hi:
            values.append(I(1 if index % 2 == 0 else -1))
    return I(min(value.lo for value in values),
             max(value.hi for value in values), raw=True)


def complex_product(left, right):
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def radial_point(radius, coordinate):
    return radius * trig_point(coordinate, True), radius * trig_point(coordinate)


def imaginary_dilog(radius, coordinate):
    z = radial_point(radius, coordinate)
    power = z
    total = I(0)
    for index in range(1, SERIES_TERMS + 1):
        total += power[1] / (index * index)
        power = complex_product(power, z)
    upper_radius = F(radius.hi, SCALE)
    remainder = (upper_radius ** (SERIES_TERMS + 1)
                 / ((SERIES_TERMS + 1) ** 2 * (1 - upper_radius)))
    return total + I(-remainder, remainder)


def log_one_minus(radius, coordinate):
    real, imaginary = radial_point(radius, coordinate)
    squared_norm = (1 - real) ** 2 + imaginary ** 2
    return arith.logi(squared_norm) / 2


def value_and_gradient(x, y):
    value = C0 + CX * x + CY * y
    value += (3 * imaginary_dilog(RX, x)
              + 6 * imaginary_dilog(RY, y)
              - imaginary_dilog(RXY, x + y)
              - imaginary_dilog(RY2, 2 * y)) / (2 * PI)
    sum_log = log_one_minus(RXY, x + y)
    gx = CX - 3 * log_one_minus(RX, x) + sum_log
    gy = (CY - 6 * log_one_minus(RY, y) + sum_log
          + 2 * log_one_minus(RY2, 2 * y))
    return value, gx, gy


def cotangent_real(radius, interval, tangent=False):
    sine = trig_range(interval)
    cosine = trig_range(interval, True)
    denominator = 1 + radius ** 2
    denominator += (2 if tangent else -2) * radius * cosine
    if denominator.lo <= 0:
        raise AssertionError('Interval denominator did not remain positive')
    return 2 * radius * sine / denominator


def interval_absolute_upper(value):
    return F(max(abs(value.lo), abs(value.hi)), SCALE)


def local_hessian_certificate():
    x, y = LOCAL
    total = (x[0] + y[0], x[1] + y[1])
    a = cotangent_real(RX, x)
    b = cotangent_real(RY, y)
    d = cotangent_real(RY, y, tangent=True)
    c = cotangent_real(RXY, total)
    hxx = PI * (c - 3 * a)
    hxy = PI * c
    hyy = PI * (c - 4 * b - 2 * d)
    off_diagonal = interval_absolute_upper(hxy)
    first = -F(hxx.hi, SCALE) - off_diagonal
    second = -F(hyy.hi, SCALE) - off_diagonal
    lower_curvature = min(first, second)
    if lower_curvature <= 2:
        raise AssertionError('The local Hessian bound is too weak')
    # The known exact critical point has y=1/4 and theta=atan(sqrt(7)/5).
    # Verify the two x bounds by monotonicity of tangent on (0,pi/2).
    target = sqrt_fraction(7) / 5
    tangent_left = trig_point(x[0]) / trig_point(x[0], True)
    tangent_right = trig_point(x[1]) / trig_point(x[1], True)
    if not tangent_left.hi < target.lo < target.hi < tangent_right.lo:
        raise AssertionError('The exact stationary point is not bracketed')
    return {
        'rectangle': [[str(v) for v in axis] for axis in LOCAL],
        'hessian_xx': hxx.bounds(), 'hessian_xy': hxy.bounds(),
        'hessian_yy': hyy.bounds(),
        'negative_hessian_lower_bound': str(lower_curvature),
        'stationary_x_bracket_verified': True,
    }


def box_upper(box):
    (xa, xb), (ya, yb) = box
    x, y = (xa + xb) / 2, (ya + yb) / 2
    dx, dy = (xb - xa) / 2, (yb - ya) / 2
    value, gx, gy = value_and_gradient(x, y)
    # The global real Hessian has operator norm <64. Taylor's formula
    # then bounds the quadratic remainder by 32*(dx^2+dy^2).
    return (F(value.hi, SCALE) + interval_absolute_upper(gx) * dx
            + interval_absolute_upper(gy) * dy + 32 * (dx * dx + dy * dy))


def verify(max_boxes):
    local = local_hessian_certificate()
    reference_value = value_and_gradient(*REFERENCE)[0]
    reference_lower = F(reference_value.lo, SCALE)
    # These eight rectangles, together with LOCAL, cover the square exactly.
    xcuts = (F(0), LOCAL[0][0], LOCAL[0][1], F(1, 2))
    ycuts = (F(0), LOCAL[1][0], LOCAL[1][1], F(1, 2))
    queue = [(((xcuts[i], xcuts[i + 1]), (ycuts[j], ycuts[j + 1])), 0)
             for i in range(3) for j in range(3) if (i, j) != (1, 1)]
    records = []
    examined = 0
    maximum_depth = 0
    while queue:
        box, depth = queue.pop()
        examined += 1
        if examined > max_boxes:
            raise RuntimeError('The certificate exceeded the allowed box count')
        upper = box_upper(box)
        if upper < reference_lower - GAP:
            records.append({
                'box': [[str(value) for value in axis] for axis in box],
                'action_upper': str(upper),
                'gap_below_reference_lower': str(reference_lower - upper),
            })
            maximum_depth = max(maximum_depth, depth)
            continue
        if depth >= 24:
            raise RuntimeError(f'Unresolved box at depth 24: {box}')
        axis = 0 if box[0][1] - box[0][0] >= box[1][1] - box[1][0] else 1
        midpoint = sum(box[axis]) / 2
        left, right = list(box), list(box)
        left[axis] = (box[axis][0], midpoint)
        right[axis] = (midpoint, box[axis][1])
        queue.extend(((tuple(left), depth + 1), (tuple(right), depth + 1)))

    area = ((LOCAL[0][1] - LOCAL[0][0]) * (LOCAL[1][1] - LOCAL[1][0]))
    for row in records:
        x, y = [[F(value) for value in axis] for axis in row['box']]
        area += (x[1] - x[0]) * (y[1] - y[0])
    if area != F(1, 4):
        raise AssertionError('The exact rectangular coverage area is incorrect')
    if reference_lower <= F(4, 5):
        raise AssertionError('The reference action lower bound unexpectedly failed')
    return {
        'scope': ('Only the upper shifted horizontal action maximum; '
                  'no connecting-face or lattice-alias estimate'),
        'status': 'completed',
        'outward_interval_scale': str(SCALE),
        'dilogarithm_series_terms': SERIES_TERMS,
        'local_hessian': local,
        'reference_point': [str(v) for v in REFERENCE],
        'reference_action_interval': reference_value.bounds(),
        'proved_exterior_gap': str(GAP),
        'high_x_action_upper': str(F(32525, 65940)),
        'covered_square_area': str(area),
        'accepted_boxes': len(records), 'examined_boxes': examined,
        'maximum_subdivision_depth': maximum_depth,
        'certificate_boxes': records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--max-boxes', type=int, default=50000)
    args = parser.parse_args()
    if args.max_boxes < 8:
        parser.error('--max-boxes must be at least eight')
    if args.output and args.output.exists():
        args.output.unlink()
    result = verify(args.max_boxes)
    paths = (Path(__file__).resolve(), Path(arith.__file__).resolve())
    result['source_sha256'] = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
    }
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(f"Verified {result['accepted_boxes']} boxes; wrote {args.output}")
    else:
        print(encoded)


if __name__ == '__main__':
    main()
