#!/usr/bin/env python3
"""Outward bounds for seven formal penalized horizontal copies.

Global concavity is proved in the companion note. Its tangent-plane
bound reduces each whole horizontal to eight rational vertices. This
does not assert that an exact original-cycle decomposition has these
seven terms, nor does it bound its possible vertical/slanted faces.
"""

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

from verify_next_crossing_complex_phase import (
    C, R, PI, IM, exponential,
)


ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def real_box(pair):
    return R(F(pair[0]), F(pair[1]))


def binary_powers(z, maximum):
    """Repeated squaring avoids linear-depth rectangular wrapping."""
    powers = [C(1), z]
    squares = [z]
    while 2**len(squares) <= maximum:
        squares.append(squares[-1]*squares[-1])
    for n in range(2,maximum+1):
        value = C(1)
        for bit, square in enumerate(squares):
            if n & (1 << bit):
                value = value*square
        powers.append(value)
    return powers


def logarithm(z, terms=250):
    assert z.re.lo > 0
    w = (z-1)/(z+1)
    radius = w.radius_upper()
    assert radius < 1
    powers = binary_powers(w,2*terms-1)
    value = sum((2*powers[2*n+1]/F(2*n+1) for n in range(terms)), C(0))
    error = 2*radius**(2*terms+1)/(F(2*terms+1)*(1-radius*radius))
    return value.widen(error)


def dilogarithm(z, terms=400):
    radius = z.radius_upper()
    assert radius < 1
    powers = binary_powers(z,terms)
    value = sum((powers[n]/F(n*n) for n in range(1,terms+1)), C(0))
    error = radius**(terms+1)/(F((terms+1)**2)*(1-radius))
    return value.widen(error)


def principal_log(z):
    if z.re.lo > 0:
        return logarithm(z)
    if z.im.lo > 0:
        return logarithm(-IM*z)+IM*C(PI/2)
    assert z.im.hi < 0, 'The principal log cut must be excluded.'
    return logarithm(IM*z)-IM*C(PI/2)


def principal_li2(z):
    if z.radius_upper() < 1:
        return dilogarithm(z, terms=400)
    assert z.inverse().radius_upper() < 1
    assert z.re.hi < 0 or z.im.lo > 0 or z.im.hi < 0
    return (-dilogarithm(z.inverse(), terms=400)
            -C(PI.square()/6)-principal_log(-z)**2/2)


def J(t):
    assert 0 < t.re.lo <= t.re.hi < 1
    zz = exponential(2*IM*C(PI)*t)
    return IM*C(PI)*(t-t*t)/2+IM*(principal_li2(zz)-C(PI.square()/6))/(2*C(PI))


def log_sine(t):
    zz = exponential(IM*C(PI)*t)
    sine2 = (zz-zz.inverse())/IM
    # Re sin(pi t)>0 on the original open factorial strip.
    return logarithm(sine2)


def phase_and_gradient(x,y,z):
    value = (J(x+y)-J(x)-J(x-z)-3*J(z)-6*J(y)+J(2*y)
             +IM*C(PI)*((x-y)**2-x+y+2*x*z+2*z*z)/2)
    lx, ly, lz = log_sine(x), log_sine(y), log_sine(z)
    lp, ls, l2y = log_sine(x-z), log_sine(x+y), log_sine(2*y)
    gradient = [ls-lx-lp+IM*C(PI)*(x-y-F(1,2)+z),
                ls-6*ly+2*l2y+IM*C(PI)*(y-x+F(1,2)),
                lp-3*lz+IM*C(PI)*(x+2*z)]
    return value, gradient


def run():
    certificate = ROOT/'repro/results/research-three-crossing-closing-action.json'
    root = json.loads(certificate.read_text())
    source = ROOT/'experiments/verify_three_crossing_closing_action.py'
    assert root['status'] == 'passed' and root['script_sha256'] == sha(source)
    dependencies = {str(source.relative_to(ROOT)): sha(source)}
    for name,digest in root['dependency_sha256'].items():
        assert sha(ROOT/name) == digest
        dependencies[name] = digest
    inner = root['root_certificate']
    helper = ROOT/'experiments/verify_next_crossing_complex_phase.py'
    assert inner['script_sha256'] == sha(helper)
    dependencies[str(helper.relative_to(ROOT))] = sha(helper)
    heights = [real_box(root['remaining_color_x']['imaginary']),
               real_box(root['remaining_color_y']['imaginary']),
               real_box(inner['certificates']['selected_saddle']['imaginary'])]
    assert -F(3,40) < heights[0].lo < heights[0].hi < 0
    assert 0 < heights[1].lo < heights[1].hi < F(13,200)
    assert 0 < heights[2].lo < heights[2].hi < F(19,250)
    magnitudes = [-heights[0], heights[1], heights[2]]

    points = {
        (1,1,-1): (499,208,239),
        (1,-1,1): (251,249,140),
        (1,-1,-1): (434,242,220),
        (-1,1,1): (279,252,104),
        (-1,1,-1): (355,250,188),
        (-1,-1,1): (213,271,87),
        (-1,-1,-1): (251,271,169),
    }
    vertices = [(x,y,z) for x in [F(1,10),F(1,2)]
                for y in [F(1,10),F(1,2)]
                for z in [F(1,100),x-F(1,400)]]
    reports = []
    for signs, raw in points.items():
        point = tuple(F(v,1000) for v in raw)
        assert F(1,10)<point[0]<F(1,2) and F(1,10)<point[1]<F(1,2)
        assert F(1,100)<point[2]<point[0]-F(1,400)
        xyz = [C(point[j], signs[j]*heights[j]) for j in range(3)]
        value, gradient = phase_and_gradient(*xyz)
        tangent_upper = max((value.re+sum(
            (gradient[j].re*(vertex[j]-point[j]) for j in range(3)),R(0)
        )).hi for vertex in vertices)
        penalty = 2*PI*sum((magnitudes[j] for j in range(3) if signs[j]<0),R(0))
        upper = tangent_upper-penalty.lo
        assert upper < F(29,20), (signs, upper)
        reports.append({
            'signs':list(signs), 'point':[str(v) for v in point],
            'phase':value.record(),
            'horizontal_gradient':[g.re.record() for g in gradient],
            'global_tangent_upper_bound':str(tangent_upper),
            'formal_fourier_penalty':penalty.record(),
            'penalized_global_upper_bound':str(upper),
        })
    assert len(reports)==7 and len(set(points))==7
    return {
        'status':'passed',
        'method':'Rational outward series plus globally concave tangent planes.',
        'domain':{'x':['1/10','1/2'],'y':['1/10','1/2'],
                  'z_lower':'1/100','x_minus_z_lower':'1/400'},
        'vertices':[[str(v) for v in vertex] for vertex in vertices],
        'common_penalized_upper_bound':'29/20',
        'copies':reports,
        'script_sha256':sha(Path(__file__).resolve()),
        'dependency_sha256':dependencies,
        'height_certificate':str(certificate.relative_to(ROOT)),
        'height_certificate_sha256':sha(certificate),
        'scope':'Seven formal horizontals only; no exact lattice-cycle transfer or vertical-face bound.',
    }


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,
                        default=ROOT/'repro/results/research-three-crossing-formal-horizontals.json')
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('All seven formal horizontal bounds passed.')
    print(f'Saved {args.output}')
