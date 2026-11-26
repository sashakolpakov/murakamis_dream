#!/usr/bin/env python3
"""Enclose one explicit Hessian point; no root solve or finite-source evaluation."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx


def rational(value):
    q = Fraction(value)
    return arb(q.numerator) / q.denominator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    ctx.prec = 192
    point = {
        'e': ['39/100', '-1/50'],
        's': ['49/100', '-3/50'],
        'z': ['23/100', '1/100'],
        'b': ['11/25', '-3/50'],
    }
    values = {name: acb(*(rational(t) for t in pair))
              for name, pair in point.items()}
    e, s, z, b = (values[name] for name in ('e', 's', 'z', 'b'))
    pi, ii = arb.pi(), acb(0, 1)

    def cot(v):
        return (pi*v).cos() / (pi*v).sin()

    pe, ps, pz, pb = (cot(v) for v in (e, s, z, b))
    d, f, j = (cot(v) for v in (e+z, s+z, s+b))
    root = ((pe+ii)**2 + 4).sqrt()
    assert root.real > 0 and root.imag > 0
    sigma = pe + 2*(pe*pe+1)/root

    E0 = (sigma+pe-d).real
    B0 = (pb-j).real
    assert E0 > 0 and B0 > 0
    T0 = (2*ps-f-j).real - j.real**2/B0
    a0 = (3*pz-d-f).real
    be, bs = -d.real, -f.real
    qe, qs, qz = 1-d.imag, -1-f.imag, (3*pz-d-f).imag-1
    assert T0 > 0
    D0 = a0-be**2/E0-bs**2/T0
    assert D0 > 0
    residual = qz-be*qe/E0-bs*qs/T0
    curvature = a0+qe**2/E0+qs**2/T0+residual**2/D0

    S = (-2*pi*ii*s).exp()
    Z = (-2*pi*ii*z).exp()
    B = (-2*pi*ii*b).exp()
    derivative_s = (abs(1-S*Z)*abs(1-S*B)
                    / (abs(Z)*abs(1-S)**2)).log()

    # The point satisfies the proved coordinate, cap, and column bounds.
    assert rational('3/10') < e.real < rational('2/5')
    assert rational('1/5') < s.real < rational('1/2')
    assert rational('11/50') < z.real < rational('1/3')
    assert rational('11/50') < b.real < rational('9/20')
    assert (s+z).real < rational('41/50')
    assert 0 < z.imag < rational('7/500')
    assert rational('-51/1000') < e.imag < rational('-19/1000')
    for value in (s, b):
        assert rational('-13/200') < value.imag < rational('17/250')
    assert sigma.real > pe.real+rational('109/90')
    assert 0 < qe < 1 and -2 < qs < 0
    assert 0 < a0 < rational('299/60')

    # These strict outward comparisons are the claimed obstruction.
    assert curvature > rational('13/2')
    assert derivative_s < -1
    quantities = dict(E0=E0, B0=B0, T0=T0, D0=D0, a0=a0,
                      qe=qe, qs=qs, sigma_real=sigma.real,
                      curvature_over_pi=curvature,
                      real_s_derivative=derivative_s)
    record = {
        'status': 'passed',
        'scope': 'one explicit point, not an optimizer or a word reference',
        'precision_bits': ctx.prec,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'point': point,
        'next_epsilon': 0,
        'positive_real_hessian': True,
        'curvature_over_pi_greater_than': '13/2',
        'real_s_derivative_less_than': '-1',
        'enclosures': {name: str(value) for name, value in quantities.items()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print('passed: one explicit positive-Hessian point; K/pi > 13/2, Re F_s < -1')


if __name__ == '__main__':
    main()
