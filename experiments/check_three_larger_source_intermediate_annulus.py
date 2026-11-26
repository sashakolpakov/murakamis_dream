#!/usr/bin/env python3
"""Outward bounds for the intermediate input interval of the larger class.

The calculation certifies a full-box original kernel Hessian, the exact
reference-action inequalities, and complete scalar interval coverage. It
does not independently re-prove the source packets used in the note.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


class Jet:
    """Exact first holomorphic derivatives in the two wire variables."""
    def __init__(self, value, dx=0, dy=0):
        self.v, self.x, self.y = acb(value), acb(dx), acb(dy)

    @staticmethod
    def cast(value):
        return value if isinstance(value, Jet) else Jet(value)

    def __add__(self, other):
        q = self.cast(other)
        return Jet(self.v+q.v, self.x+q.x, self.y+q.y)
    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, -self.x, -self.y)

    def __sub__(self, other):
        return self+-self.cast(other)

    def __rsub__(self, other):
        return self.cast(other)+-self

    def __mul__(self, other):
        q = self.cast(other)
        return Jet(self.v*q.v, self.x*q.v+self.v*q.x,
                   self.y*q.v+self.v*q.y)
    __rmul__ = __mul__

    def inverse(self):
        return Jet(1/self.v, -self.x/self.v**2, -self.y/self.v**2)

    def __truediv__(self, other):
        return self*self.cast(other).inverse()

    def __rtruediv__(self, other):
        return self.cast(other)*self.inverse()

    def __pow__(self, power):
        assert power >= 0
        out = Jet(1)
        for _ in range(power):
            out = out*self
        return out

    def sqrt(self):
        root = self.v.sqrt()
        return Jet(root, self.x/(2*root), self.y/(2*root))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--max-cells', type=int, default=20000)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-larger-source-intermediate-annulus.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    started = time.monotonic()

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def interval(lo, hi):
        return arb(a((lo+hi)/2), a((hi-lo)/2))

    pi, ii, sq = arb.pi(), acb(0, 1), arb(21).sqrt()
    rho, D = (5-sq)/2, 5+sq
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    K, alpha = 4*pi/sq, k0.real
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    R, W, H, b, e, A = map(a, [Q(1, 200), Q(9, 1000), Q(57, 10000),
                                Q(9, 50), Q(13, 50), Q(29, 20)])
    Z = rho*a(Q(21, 20))/(1-a(Q(3, 10))*rho)
    C0 = K*(D+a(Q(3, 5)))/(2*(D-a(Q(3, 5)))**2)
    Cref = K*(D+b+e)/(2*(D-b-e)**2)
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    def hessian(z, w):
        xv, yv = (2*pi*ii*(xh+z)).exp(), (2*pi*ii*(xh+w)).exp()
        X, Y = Jet(xv, 2*pi*ii*xv, 0), Jet(yv, 0, 2*pi*ii*yv)
        al, be = 1/X-1, 1/Y-1
        delta = 1-2*(al+be)+(al-be)**2
        root = delta.sqrt()
        U = (1+al-be-root)/2
        Ux = (-2*pi*ii/X)*(1-U)/root
        xx = -Ux/(U*(1-X*U))+2*pi*ii*X*(1-U)/((1-X)*(1-X*U))
        return xx, delta.v

    domain = [(Q(-1, 50), Q(1, 50)),
              (Q(-9, 1000), Q(9, 1000)),
              (Q(-1, 200), Q(1, 200))]
    pending = [(domain, '')]
    cells = []
    visits = 0
    while pending:
        box, address = pending.pop()
        visits += 1
        assert visits <= args.max_cells, 'Explicit visit budget exhausted'
        t, u, v = [interval(*pair) for pair in box]
        jet, delta = hessian(t, acb(u, v))
        tc, uc, vc = [a((lo+hi)/2) for lo, hi in box]
        center = hessian(tc, acb(uc, vc))[0].v
        radii = [arb(0, a((hi-lo)/2)) for lo, hi in box]
        xx = center+jet.x*radii[0]+jet.y*radii[1]+ii*jet.y*radii[2]
        margin = -xx.real-a(Q(47, 5))
        if delta.imag > 0 and margin > 0:
            cells.append({'address': address,
                          'box': [[str(lo), str(hi)] for lo, hi in box],
                          'negative_real_hessian': str(-xx.real),
                          'strict_margin_beyond_47_5': str(margin),
                          'selected_root_margin': str(delta.imag)})
            continue
        axis = max(range(3), key=lambda j: box[j][1]-box[j][0])
        lo, hi = box[axis]
        mid = (lo+hi)/2
        left, right = list(box), list(box)
        left[axis], right[axis] = (lo, mid), (mid, hi)
        pending.extend([(right, address+str(axis)+'1'),
                        (left, address+str(axis)+'0')])

    # Exact prefix-tree coverage independently reconstructs every rectangle.
    tree = {}
    for cell in cells:
        node, reconstructed = tree, list(domain)
        address = cell['address']
        assert len(address) % 2 == 0
        for j in range(0, len(address), 2):
            axis, side = address[j:j+2]
            assert 'leaf' not in node
            assert node.setdefault('axis', axis) == axis
            node = node.setdefault(side, {})
            lo, hi = reconstructed[int(axis)]
            mid = (lo+hi)/2
            reconstructed[int(axis)] = (lo, mid) if side == '0' else (mid, hi)
        assert not node
        node['leaf'] = True
        assert [[str(lo), str(hi)] for lo, hi in reconstructed] == cell['box']

    def cover(node):
        if 'leaf' in node:
            assert set(node) == {'leaf'}
        else:
            assert set(node) == {'axis', '0', '1'}
            cover(node['0'])
            cover(node['1'])
    cover(tree)

    positive('reference point stays in input disk', R-rho*W)
    residual = H+b*rho*W+9*(1+rho)**2*W**2
    positive('reference-to-critical segment stays in input disk',
             R-rho*W-residual/(D-b-e))
    # Both radial envelope derivatives are bounded at the left endpoint W;
    # the full-box negative Hessian then makes them strictly decreasing.
    complex_slope = K*H-2*A*W-5*alpha*W+2*K*R+9*K*(W+R)**2
    real_slope = (K*H-2*A*W+alpha*(2-5*rho)*W
                  +9*K*(1+rho)**2*W**2-a(Q(47, 5))*(W-rho*W))
    positive('complex-output outward envelope slope below -.05',
             -complex_slope-a(Q(1, 20)))
    positive('real-output outward envelope slope below -.05',
             -real_slope-a(Q(1, 20)))

    # Complex-output edge W: exact homogeneous quadratic completion on |w|<=R.
    lam = 3*W/R
    quad = lam*R**2+W**2*K**2*(lam-rho*alpha)/(lam**2-rho**2*K**2)
    complex_error = (C0*H**2+K*H*W+K*Z*H*R+a(Q(2, 25))*K*R**2
                     -(A+5*alpha/2)*W**2+quad+3*K*(W+R)**3)
    positive('complex-output intermediate gap exceeds .0001',
             -complex_error-a(Q(1, 10000)))

    # Real outputs: t=sigma W, v=sigma w. The upper bound below is
    # identical for both sigma, and v traverses the whole signed interval.
    scalar_cells = []
    mesh = 1024
    for j in range(mesh):
        lo = Q(-9, 1000)+Q(18, 1000)*Q(j, mesh)
        hi = Q(-9, 1000)+Q(18, 1000)*Q(j+1, mesh)
        v = interval(lo, hi)
        u, d = abs(v), W-rho*v
        res = H+b*rho*u+9*(1+rho)**2*u**2
        error = (K*H*W-A*W**2
                 +alpha*(2-5*rho)*v*d+9*K*(1+rho)**2*u**2*d
                 -a(Q(47, 10))*d**2
                 +alpha*sq*rho**2*u**2/2+K*H*rho*u
                 +K*b*rho**2*u**2/2+Cref*res**2)
        margin = -error-a(Q(1, 100000))
        assert margin > 0, (j, lo, hi, error)
        scalar_cells.append({'signed_output_interval': [str(lo), str(hi)],
                             'strict_margin_beyond_one_hundred_thousandth': str(margin)})
    assert scalar_cells[0]['signed_output_interval'][0] == '-9/1000'
    assert scalar_cells[-1]['signed_output_interval'][1] == '9/1000'
    assert all(scalar_cells[j]['signed_output_interval'][1]
               == scalar_cells[j+1]['signed_output_interval'][0] for j in range(mesh-1))

    deps = ['notes/research_three_larger_source_intermediate_annulus.md',
            'notes/research_three_larger_phase_class.md',
            'notes/research_three_vertex_real_input_union.md',
            'notes/research_three_vertex_input_rectangle.md',
            'notes/research_three_phase_graph_transform.md',
            'notes/research_three_source_tail_propagation.md']
    result = {'status': 'passed', 'precision_bits': args.precision,
              'scope': 'Original analytic kernel Hessian on the complete auxiliary rectangle and scalar reference-action/monotonicity bounds for W<=|input|<=.02, output disk .005 union real interval +/-.009. Source packets and source-class entrance are separate proved inputs, not re-proved by this checker.',
              'hessian_domain': [[str(lo), str(hi)] for lo, hi in domain],
              'hessian_cells': len(cells), 'hessian_visits': visits, 'cells': cells,
              'scalar_interval_cells': len(scalar_cells), 'scalar_cells': scalar_cells,
              'strict_scalar_comparisons': len(checks), 'checks': checks,
              'constants': {'complex_edge_error': str(complex_error),
                            'complex_outward_slope': str(complex_slope),
                            'real_outward_slope': str(real_slope),
                            'reference_action_constant': str(Cref)},
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
              'elapsed_seconds': time.monotonic()-started}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'hessian_cells',
                     'hessian_visits', 'scalar_interval_cells',
                     'strict_scalar_comparisons', 'elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
