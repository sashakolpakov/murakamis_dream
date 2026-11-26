#!/usr/bin/env python3
"""Rigorous limiting-phase certificates for the three-crossing terminal.

Requires python-flint. Every successful comparison uses Arb balls and
rational cutoffs. Subdivision terminates only after a covering proof.
This script does not establish a finite-sum contour identity.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
from flint import acb, arb, ctx
ctx.prec = 120
pi = arb.pi()
I = acb(0, 1)
half = arb(1) / 2
k = (arb(7).sqrt() + I) / 4
xs = k.atan() / pi
ts = 2 * k.acos()
hx = xs.imag
ht = -ts.imag
LOCAL = (Q(18, 100), Q(20, 100), Q(27, 100), Q(29, 100))

def rat(x):
    if isinstance(x, Q):
        return arb(x.numerator) / x.denominator
    return arb(x)

def ball(a, b):
    return (rat(a) + rat(b)) / 2 + arb(0, ((rat(b) - rat(a)) / 2).upper())

def hessian(x, t):
    den = (2 * pi * x).cos() + t.cos()
    A = -2 * pi * (2 * pi * x).sin() / den - 4 * pi / (pi * x).tan() - 2 * pi * (2 * pi * x).sin() / ((2 * pi * x).cos() + 1)
    B = -t.sin() / den
    C = -((pi * x + t / 2).tan() + (pi * x - t / 2).tan()) / (4 * pi) + 3 * I / (2 * pi)
    return (A, B, C)

def Ju(z):
    z = acb(z)
    value = -I * pi * (z * z - z) / 2 + I * (2 * I * pi * z).exp().polylog(2) / (2 * pi) - I * pi / 12
    if value.is_finite():
        return value
    rho = abs(z).upper()
    if rho == 0:
        return acb(0)
    if rho < 1 / (2 * pi):
        size = rho * (1 - (2 * pi * rho).log() + 2 * pi) + pi * pi / 6 * rho ** 3 / (3 * (1 - rho * rho))
        return acb(arb(0, size.upper()), arb(0, size.upper()))
    return value

def Js(z, side):
    return Ju(z) if side == 1 else -Ju(-z) - I * pi * z

def jp(z, side):
    if side == -1:
        return jp(-z, 1) - I * pi
    return (1 - (2 * I * pi * z).exp()).log() - I * pi * z + I * pi / 2

def phase(x, t, side):
    p = half + t / (2 * pi)
    m = half - t / (2 * pi)
    b = Js(p, -1) + Js(m, 1) - Js(p - x, -1) - Js(m - x, 1) - 2 * Js(x, side)
    b0 = 2 * Js(half, 1) - 2 * Js(half - x, -side) - 2 * Js(x, side)
    return b + b0 + 3 * I * t * t / (4 * pi) - I * t

def gradient(x, t, side):
    p = half + t / (2 * pi)
    m = half - t / (2 * pi)
    gx = jp(p - x, -1) + jp(m - x, 1) + 2 * jp(half - x, -side) - 4 * jp(x, side)
    gt = (jp(p, -1) - jp(m, 1) - jp(p - x, -1) + jp(m - x, 1)) / (2 * pi) + 3 * I * t / (2 * pi) - I
    return (gx, gt)
M = phase(xs, ts, 1).real

def certify_local(grid=32):
    a, b, c, d = LOCAL
    assert rat(a) < xs.real < rat(b)
    assert rat(c) < ts.real / (2 * pi) < rat(d)
    smallest_determinant = None
    largest_xx = None
    for ix in range(grid):
        for ir in range(grid):
            x = acb(ball(a + (b - a) * ix / grid, a + (b - a) * (ix + 1) / grid), hx)
            t = 2 * pi * acb(ball(c + (d - c) * ir / grid, c + (d - c) * (ir + 1) / grid), -ht / (2 * pi))
            A, B, C = hessian(x, t)
            determinant = A.real * C.real - B.real ** 2
            assert A.real < 0 and determinant > 0
            if smallest_determinant is None or determinant.lower() < smallest_determinant:
                smallest_determinant = determinant.lower()
            if largest_xx is None or A.real.upper() > largest_xx:
                largest_xx = A.real.upper()
    return {'rectangle_in_x_and_t_over_2pi': [str(v) for v in LOCAL], 'subrectangles': grid * grid, 'upper_bound_on_Hxx': str(largest_xx), 'lower_bound_on_determinant': str(smallest_determinant)}

def mapping_affine(p, q, kind, endpoint=None):
    if kind in ('central', 'negative', 'lower'):
        side = -1 if kind == 'lower' else 1
        x = acb(p, side * hx)
        t = acb(2 * pi * q, -ht)
        dirs = ((acb(1), acb(0)), (acb(0), 2 * pi))
        penalty = 2 * pi * hx if kind == 'lower' else arb(0)
        pd = (arb(0), arb(0))
    elif kind in ('outer_positive', 'outer_negative'):
        x = acb(p, hx * q)
        t = acb(2 * pi / 3 * (1 if kind == 'outer_positive' else -1), -ht * q)
        dirs = ((acb(1), acb(0)), (I * hx, -I * ht))
        side = 1
        penalty = arb(0)
        pd = (arb(0), arb(0))
    elif kind in ('wire_upper', 'wire_lower'):
        side = 1 if kind == 'wire_upper' else -1
        x = acb(rat(endpoint), side * hx * q)
        t = acb(2 * pi * p, -ht * q)
        dirs = ((acb(0), 2 * pi), (side * I * hx, -I * ht))
        penalty = 2 * pi * hx * q if side == -1 else arb(0)
        pd = (arb(0), 2 * pi * hx if side == -1 else arb(0))
    else:
        raise ValueError(kind)
    return (x, t, dirs, side, penalty, pd)

def mapping(p, q, kind, endpoint=None):
    if kind in ('bottom_endpoint_upper', 'bottom_endpoint_lower'):
        side = 1 if kind.endswith('upper') else -1
        x = acb(rat(endpoint), side * hx * q)
        t = acb(2 * pi * p, -ht)
        dirs = ((acb(0), 2 * pi), (side * I * hx, acb(0)))
        penalty = 2 * pi * hx * q if side == -1 else arb(0)
        pd = (arb(0), 2 * pi * hx if side == -1 else arb(0))
        return (x, t, dirs, side, penalty, pd)
    if kind in ('outer_lower_positive', 'outer_lower_negative'):
        sign = 1 if kind.endswith('positive') else -1
        x = acb(p, -hx * q)
        t = acb(sign * 2 * pi / 3, -ht * q)
        return (x, t, ((acb(1), acb(0)), (-I * hx, -I * ht)), -1, 2 * pi * hx * q, (arb(0), 2 * pi * hx))
    return mapping_affine(p, q, kind, endpoint)

def bound_affine(box, kind, endpoint, target):
    a, b, c, d = box
    pp = ball(a, b)
    qq = ball(c, d)
    xx, tt, dirs, side, pen, pd = mapping(pp, qq, kind, endpoint)
    direct = phase(xx, tt, side).real - pen
    if direct < target:
        return (direct, 'direct')
    p = rat((a + b) / 2)
    q = rat((c + d) / 2)
    rp = rat((b - a) / 2)
    rq = rat((d - c) / 2)
    x, t, dirs, side, pen, pd = mapping(p, q, kind, endpoint)
    f = phase(x, t, side).real - pen
    gx, gt = gradient(x, t, side)
    (xp, tp), (xq, tq) = dirs
    gp = (gx * xp + gt * tp).real - pd[0]
    gq = (gx * xq + gt * tq).real - pd[1]
    A, B, C = hessian(xx, tt)
    App = (A * xp * xp + 2 * B * xp * tp + C * tp * tp).real
    Apq = (A * xp * xq + B * (xp * tq + xq * tp) + C * tp * tq).real
    Aqq = (A * xq * xq + 2 * B * xq * tq + C * tq * tq).real
    v = f + abs(gp) * rp + abs(gq) * rq + (abs(App) * rp * rp + 2 * abs(Apq) * rp * rq + abs(Aqq) * rq * rq) / 2
    return (v, 'Taylor')

def boundbox(box, kind, endpoint, target):
    if not kind.startswith('nested_'):
        return bound_affine(box, kind, endpoint, target)
    side = 1 if '_upper_' in kind else -1
    sign = 1 if kind.endswith('positive') else -1
    a, b, c, d = box
    pp = ball(a, b)
    qq = ball(c, d)
    xx = acb(rat(endpoint), side * hx * pp * qq)
    tt = acb(sign * 2 * pi / 3, -ht * pp)
    coefficient = 2 * pi * hx if side == -1 else arb(0)
    direct = phase(xx, tt, side).real - coefficient * pp * qq
    if direct < target:
        return (direct, 'direct')
    p = rat((a + b) / 2)
    q = rat((c + d) / 2)
    rp = rat((b - a) / 2)
    rq = rat((d - c) / 2)
    x = acb(rat(endpoint), side * hx * p * q)
    t = acb(sign * 2 * pi / 3, -ht * p)
    f = phase(x, t, side).real - coefficient * p * q
    gx, gt = gradient(x, t, side)
    gp = (side * I * hx * q * gx - I * ht * gt).real - coefficient * q
    gq = (side * I * hx * p * gx).real - coefficient * p
    A, B, C = hessian(xx, tt)
    gxx, gtt = gradient(xx, tt, side)
    xp = side * I * hx * qq
    xq = side * I * hx * pp
    tp = -I * ht
    App = (A * xp * xp + 2 * B * xp * tp + C * tp * tp).real
    Apq = (A * xp * xq + B * tp * xq + gxx * side * I * hx).real - coefficient
    Aqq = (A * xq * xq).real
    v = f + abs(gp) * rp + abs(gq) * rq + (abs(App) * rp * rp + 2 * abs(Apq) * rp * rq + abs(Aqq) * rq * rq) / 2
    return (v, 'Taylor')

def certify(kind, initial, gap, endpoint=None, scale=Q(1)):
    target = M - rat(gap)
    todo = [initial]
    counts = Counter()
    accepted = []
    best = None
    while todo:
        box = todo.pop()
        a, b, c, d = box
        counts['visited'] += 1
        if kind == 'central' and a >= LOCAL[0] and (b <= LOCAL[1]) and (c >= LOCAL[2]) and (d <= LOCAL[3]):
            counts['local'] += 1
            accepted.append({'box': [str(v) for v in box], 'method': 'local Hessian'})
            continue
        value, method = boundbox(box, kind, endpoint, target)
        if value < target:
            counts[method] += 1
            upper = value.upper()
            if best is None or upper > best:
                best = upper
            accepted.append({'box': [str(v) for v in box], 'method': method, 'upper_bound': str(upper)})
            continue
        if counts['visited'] > 50000:
            raise RuntimeError('Subdivision budget exhausted; no certificate produced')
        if b - a >= (d - c) * scale:
            middle = (a + b) / 2
            todo.extend([(a, middle, c, d), (middle, b, c, d)])
        else:
            middle = (c + d) / 2
            todo.extend([(a, b, c, middle), (a, b, middle, d)])
    return {'surface': kind, 'endpoint': str(endpoint) if endpoint is not None else None, 'initial_box': [str(v) for v in initial], 'certified_gap': str(gap), 'counts': dict(counts), 'largest_accepted_upper_bound': str(best), 'cover': accepted}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Write the complete rational-box certificate')
    args = parser.parse_args()
    local = certify_local()
    alpha = arb(3) / 32
    wire_tail = 2 * (Js(2 * alpha, 1) - 4 * Js(alpha, 1)).real
    assert M - wire_tail > arb(19) / 1000
    results = []
    results.append(certify('central', (Q(3, 32), Q(13, 32), Q(0), Q(1, 3)), Q(1, 100000)))
    results.append(certify('negative', (Q(3, 32), Q(13, 32), Q(-1, 3), Q(0)), Q(1, 10)))
    results.append(certify('lower', (Q(3, 32), Q(13, 32), Q(-1, 3), Q(1, 3)), Q(1, 20)))
    for sign in ('positive', 'negative'):
        results.append(certify('outer_' + sign, (Q(3, 32), Q(13, 32), Q(0), Q(1)), Q(1, 1000), scale=Q(1, 3)))
        results.append(certify('outer_lower_' + sign, (Q(3, 32), Q(13, 32), Q(0), Q(1)), Q(1, 1000), scale=Q(1, 3)))
    for endpoint in (Q(3, 32), Q(13, 32)):
        for side in ('upper', 'lower'):
            results.append(certify('wire_' + side, (Q(-1, 3), Q(1, 3), Q(0), Q(1)), Q(1, 1000), endpoint, Q(1, 2)))
            results.append(certify('bottom_endpoint_' + side, (Q(-1, 3), Q(1, 3), Q(0), Q(1)), Q(1, 1000), endpoint, Q(1, 2)))
            for sign in ('positive', 'negative'):
                results.append(certify('nested_' + side + '_' + sign, (Q(0), Q(1), Q(0), Q(1)), Q(1, 1000), endpoint))
    result = {'scope': 'Limiting-phase inequalities only; no finite-sum contour identity', 'precision_bits': ctx.prec, 'selected_wire': str(xs), 'selected_angle': str(ts), 'selected_real_action': str(M), 'real_wire_tail_constant': str(wire_tail), 'local_Hessian': local, 'surfaces': results}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print('Selected real action:', M)
    print('Local negative Hessian:', local['subrectangles'], 'covering rectangles')
    for item in results:
        print(item['surface'], item['endpoint'], 'gap', item['certified_gap'], item['counts'])
    if args.output:
        print('Complete covering certificate:', args.output)
if __name__ == '__main__':
    main()
