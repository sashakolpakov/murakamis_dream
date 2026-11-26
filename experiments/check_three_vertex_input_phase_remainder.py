#!/usr/bin/env python3
"""Exact Taylor/Cauchy phase bound for the wider-input retained vertex.

Independent coefficient construction: inverses and the selected square
root are solved coefficient by coefficient, without the author's binomial
series or seed solver.  This is a phase estimate, not a new source domain.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import math
import time

from flint import arb, acb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ORDER = 12
KEYS = [(a, n-a) for n in range(ORDER+1) for a in range(n+1)]


class Poly:
    def __init__(self, coefficients=0):
        self.c = dict(coefficients) if isinstance(coefficients, dict) else {(0, 0): acb(coefficients)}

    def __getitem__(self, key):
        return self.c.get(key, acb(0))

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        return Poly({key: self[key]+other[key] for key in KEYS})
    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -v for key, v in self.c.items()})

    def __sub__(self, other):
        return self+(-other if isinstance(other, Poly) else -acb(other))

    def __rsub__(self, other):
        return Poly(other)-self

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = {}
        for (a, b), v in self.c.items():
            for (c, d), w in other.c.items():
                if a+b+c+d <= ORDER:
                    key = (a+c, b+d)
                    out[key] = out.get(key, acb(0))+v*w
        return Poly(out)
    __rmul__ = __mul__

    def inverse(self):
        out = {(0, 0): 1/self[(0, 0)]}
        for i, j in KEYS[1:]:
            value = sum(self[(a, b)]*out.get((i-a, j-b), acb(0))
                        for a in range(i+1) for b in range(j+1) if a+b)
            out[(i, j)] = -value/self[(0, 0)]
        return Poly(out)

    def __truediv__(self, other):
        return self*(other.inverse() if isinstance(other, Poly) else 1/acb(other))

    def __rtruediv__(self, other):
        return Poly(other)*self.inverse()


def selected_root(poly, constant):
    out = {(0, 0): constant}
    for i, j in KEYS[1:]:
        value = sum(out.get((a, b), acb(0))*out.get((i-a, j-b), acb(0))
                    for a in range(i+1) for b in range(j+1)
                    if (a, b) not in ((0, 0), (i, j)))
        out[(i, j)] = (poly[(i, j)]-value)/(2*constant)
    return Poly(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', default='repro/results/research-three-vertex-input-phase-remainder.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    p, ii = arb.pi(), acb(0, 1)
    k0 = 4*p/21*(2*arb(3).sqrt()-3*ii)
    X0 = acb(arb(1)/4, arb(3).sqrt()/4)
    X = X0*Poly({(j, 0): (2*p*ii)**j/math.factorial(j) for j in range(ORDER+1)})
    Y = X0*Poly({(0, j): (2*p*ii)**j/math.factorial(j) for j in range(ORDER+1)})
    alpha, beta = 1/X-1, 1/Y-1
    alpha.c[(0, 0)] = beta.c[(0, 0)] = -ii*arb(3).sqrt()
    delta = 1-2*(alpha+beta)+(alpha-beta)*(alpha-beta)
    root = selected_root(delta, acb(2, arb(3).sqrt()))
    U, V = (1+alpha-beta-root)/2, (1-alpha+beta-root)/2
    ax, by = -2*p*ii/X, -2*p*ii/Y
    Ux, Uy, Vy = ax*(1-U)/root, by*U/root, by*(1-V)/root
    pxx = -Ux/(U*(1-X*U))+2*p*ii*X*(1-U)/((1-X)*(1-X*U))
    pxy = -Uy/(U*(1-X*U))
    pyy = -Vy/(V*(1-Y*V))+2*p*ii*Y*(1-V)/((1-Y)*(1-Y*V))

    # Exact identities justify deleting the identically zero constant
    # coefficient; interval cancellation alone would not justify this.
    xs = (1+sp.I*sp.sqrt(3))/4
    us = (-1-sp.I*sp.sqrt(3))/2
    ds = 2+sp.I*sp.sqrt(3)
    ks = 4*sp.pi/21*(2*sp.sqrt(3)-3*sp.I)
    ux = (-2*sp.pi*sp.I/xs)*(1-us)/ds
    uy = (-2*sp.pi*sp.I/xs)*us/ds
    hxx = -ux/(us*(1-xs*us))+2*sp.pi*sp.I*xs*(1-us)/((1-xs)*(1-xs*us))
    hxy = -uy/(us*(1-xs*us))
    identities = [sp.simplify(hxx+5*ks), sp.simplify(hxy-2*ks)]
    assert identities == [0, 0]

    # Cauchy majorant 64 on radius1/50 is proved independently in the
    # analytic phase-class note.  The discarded tail is summed exactly.
    qx, qy, radius = Q(1, 2), Q(1, 4), Q(1, 50)
    tail_z = Q(64)/radius*(qx**13/(1-qx)-qy**13/(1-qy))/(qx-qy)
    tail_w = Q(64)/radius*qy**12/(1-qy)
    assert tail_z < Q(25, 8) and tail_w < Q(51, 200000)
    r = lambda q: arb(q.numerator)/q.denominator
    rounded = {'xx': (Q(17568, 1000), Q(4627, 1000)),
               'xy': (Q(8058, 1000), Q(4609, 1000)),
               'yy': (Q(8056, 1000), Q(13839, 1000))}
    bounds = []
    for name, series in [('xx', pxx/k0+5), ('xy', pxy/k0-2), ('yy', pyy/k0+5)]:
        assert series[(0, 0)].contains(0)
        series.c[(0, 0)] = acb(0)
        zpart = sum(abs(value)*r(Q(1, 100))**(a-1)*r(Q(1, 200))**b
                    for (a, b), value in series.c.items() if a)
        wpart = sum(abs(value)*r(Q(1, 200))**(b-1)
                    for (a, b), value in series.c.items() if a == 0 and b)
        zbound, wbound = zpart+r(tail_z), wpart+r(tail_w)
        rz, rw = rounded[name]
        assert zbound < r(rz) and wbound < r(rw) and max(rz, rw) < 18
        bounds.append({'entry': name, 'z_polynomial': str(zpart), 'w_polynomial': str(wpart),
                       'z_total': str(zbound), 'w_total': str(wbound),
                       'coefficients': {f'{a},{b}': str(v) for (a, b), v in sorted(series.c.items())}})
    deps = ['notes/research_three_vertex_input_rectangle.md',
            'notes/research_three_phase_graph_transform.md',
            'notes/research_three_vertex_local_composition.md']
    result = {'status': 'passed', 'precision_bits': args.precision,
              'Taylor_total_degree': ORDER, 'exact_center_identities': len(identities),
              'strict_scalar_comparisons': 6, 'exact_tail_comparisons': 2, 'bounds': bounds,
              'Cauchy_radius': str(radius), 'Cauchy_majorant': 64,
              'tail_after_z_factor': str(tail_z), 'tail_after_w_factor': str(tail_w),
              'phase_radii': ['1/100', '1/200'], 'normalized_linear_Hessian_bound': 18,
              'method': 'Independent inverse and square-root coefficient recurrences; factored Cauchy tail.',
              'scope': 'Analytic phase bound. Actual source domain is the separately proved input rectangle, not this larger imaginary input disk.',
              'elapsed_seconds': time.monotonic()-start,
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {name: sha256((ROOT/name).read_bytes()).hexdigest() for name in deps}}
    (ROOT/args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'Taylor_total_degree', 'exact_center_identities', 'strict_scalar_comparisons', 'elapsed_seconds')}, indent=2))
    for item in bounds:
        print(item['entry'], item['z_total'], item['w_total'])


if __name__ == '__main__':
    main()
