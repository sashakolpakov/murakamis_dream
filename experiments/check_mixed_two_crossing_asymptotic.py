#!/usr/bin/env python3
"""Compare the original mixed source with its proved leading asymptotic.

Every original Newton coefficient is retained. Finite comparisons check
the amplitude, carrier and complex-boundary conventions; they are not
used as proof of the contour bounds or of a geometric identification.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_boundary_crossing_packet_preservation import original_crossings, evaluate
from check_twist_period_insertion import encode


def primitive(z):
    if mp.im(z) >= 0:
        return (1j*(mp.polylog(2, mp.exp(2j*mp.pi*z))-mp.pi**2/6)/(2*mp.pi)
                +1j*mp.pi*(z-z*z)/2)
    return (-1j*(mp.polylog(2, mp.exp(-2j*mp.pi*z))-mp.pi**2/6)/(2*mp.pi)
            -1j*mp.pi*(z-z*z)/2)


def selected_data(angle, base):
    def gradients(x, y):
        first = (mp.log(2*mp.sin(mp.pi*(x+y)))
                 -3*mp.log(2*mp.sin(mp.pi*x))+1j*mp.pi*y)
        second = (mp.log(2*mp.sin(mp.pi*(x+y)))
                  -4*mp.log(2*mp.sin(mp.pi*y))
                  +mp.log(2*mp.cos(2*mp.pi*y)+2*mp.cos(angle))
                  +1j*mp.pi*(x-y-mp.mpf('.5')))
        return first, second
    x, y = mp.findroot(gradients, base, tol=mp.eps*100)
    correction = y*mp.quad(
        lambda v: mp.log((mp.cos(2*mp.pi*y*v)+mp.cos(angle))
                         /(mp.cos(2*mp.pi*y*v)+1)), [0, 1])
    action = (primitive(x+y)-3*primitive(x)-6*primitive(y)+primitive(2*y)
              +correction+1j*mp.pi*(x*y-y*y/2-y/2))
    hxx = mp.pi*mp.cot(mp.pi*(x+y))-3*mp.pi*mp.cot(mp.pi*x)
    hxy = mp.pi*mp.cot(mp.pi*(x+y))+1j*mp.pi
    hyy = (mp.pi*mp.cot(mp.pi*(x+y))-4*mp.pi*mp.cot(mp.pi*y)
           -2*mp.pi*mp.sin(2*mp.pi*y)/(mp.cos(2*mp.pi*y)+mp.cos(angle))-1j*mp.pi)
    density = (mp.exp(1j*mp.pi*y/2)/8*mp.sqrt(mp.sin(mp.pi*(x+y)))
               /(mp.sin(mp.pi*x)**mp.mpf('1.5')*mp.sin(mp.pi*y)**2))
    amplitude = 2*mp.pi*density/mp.sqrt(hxx*hyy-hxy*hxy)
    return x, y, action, amplitude


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=120)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    X = mp.findroot(lambda z:z**3+2*z*z+1, mp.mpc('.1', '.66'))
    Y = 1+2*X+2*X*X
    base = (mp.log(X)/(2j*mp.pi), mp.log(Y)/(2j*mp.pi))
    angles = (mp.mpf(0), mp.mpc('.03', '.01'), mp.mpc('-.07', '.015'))
    data = [selected_data(u, base) for u in angles]
    records = []
    for level in (24, 25, 48, 49, 96, 97):
        crossing, _ = original_crossings(level)
        adjoint = crossing.transpose_conj()
        unit = mp.matrix([1]+[0]*(level-1))
        coefficients = adjoint*(adjoint*(crossing*(crossing*unit)))
        for angle, (_, _, action, amplitude) in zip(angles, data):
            exact = evaluate(level, coefficients, angle)[0]
            ratio = exact/(amplitude*mp.exp(level*action))
            records.append({'N': level, 'angle': encode(angle),
                            'finite_over_leading': encode(ratio),
                            'N_times_relative_error': encode(level*(ratio-1))})
        print(f'Full mixed-source asymptotic recorded at N={level}.', flush=True)
    result = {'scope': 'Original finite source versus the proved Gaussian normalization; '
                       'not a proof of the asymptotic or a volume identification.',
              'decimal_precision': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'critical_data': [{'angle': encode(u), 'x': encode(x), 'y': encode(y),
                                 'action': encode(s), 'amplitude': encode(a)}
                                for u, (x, y, s, a) in zip(angles, data)],
              'comparisons': records}
    content = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f'Saved {args.output}.', flush=True)
    else:
        print(content)


if __name__ == '__main__':
    main()
