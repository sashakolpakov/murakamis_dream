#!/usr/bin/env python3
"""Check the original periods and volume of positive negative corridors.

These finite high-precision checks supplement the geometric proofs in
research_negative_corridor_variational_bounds.md and
research_positive_point_marked_completion.md. They cannot establish
the global face assembly or an asymptotic for the quantum source.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_positive_edge_volume_identity import bloch_wigner, phase, relative


def edge_data(t, u):
    a, b = mp.tan(t/2), mp.tan(u/2)
    q = mp.sqrt(1+a*a+b*b)
    rt = mp.asinh(a*mp.cos(u/2))
    ru = mp.asinh(b*mp.cos(t/2))
    aa, cc = (q+a)/(b-1j), (q-a)/(b-1j)
    bb, dd = -(q-b)/(a+1j), -(q+b)/(a+1j)
    shapes = (aa, bb, -1/aa, -1/bb, cc, dd, -1/cc, -1/dd)
    p = mp.atanh((a+1j*b)/(q+1))
    qq = mp.atanh((a-1j*b)/(q+1))
    return a, b, q, rt, ru, shapes, phase(p, qq)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    cases = [
        ('corridor', (4,)), ('corridor', (4, 4)),
        ('corridor', (4, 7)), ('corridor', (4, 4, 4, 4)),
        ('corridor', (6,)), ('corridor', (7,)),
        ('corridor', (6, 6)), ('corridor', (6, 9)),
        ('corridor', (8, 6, 7)), ('corridor', (6, 6, 6, 6)),
        ('pendant', (4,)), ('pendant', (5,)),
        ('pendant', (4, 6)), ('pendant', (5, 8, 6)),
        ('pendant', (4, 4)), ('pendant', (4, 4, 4, 4)),
    ]
    records = []
    for kind, powers in cases:
        size = len(powers)
        # -1 is a complete outside vertex. A corridor has two ends;
        # a pendant has its original degree-one vertex at index zero.
        edges = [(j, j+1) for j in range(size-1)]+[(size-1, -1)]
        if kind == 'corridor':
            edges.insert(0, (-1, 0))
        degrees = [sum(v in edge for edge in edges) for v in range(size)]

        def returns(values):
            sums = [mp.mpc(0) for _ in powers]
            for v, w in edges:
                t = values[v] if v >= 0 else mp.mpc(0)
                u = values[w] if w >= 0 else mp.mpc(0)
                rt = mp.asinh(mp.tan(t/2)*mp.cos(u/2))
                ru = mp.asinh(mp.tan(u/2)*mp.cos(t/2))
                if v >= 0:
                    sums[v] += rt
                if w >= 0:
                    sums[w] += ru
            return sums

        def equations(*values):
            sums = returns(values)
            return tuple(sums[j]+1j*powers[j]*values[j]/2+1j*mp.pi
                         for j in range(size))

        initial = tuple(-2j*mp.pi/(degrees[j]+1j*powers[j]) for j in range(size))
        solution = tuple(mp.findroot(equations, initial,
                                    tol=mp.power(10, -precision+15),
                                    maxsteps=100))
        residual = max(abs(z) for z in equations(*solution))
        assert residual < tolerance
        assert all(-mp.pi < t.real < 0 and t.imag < 0 for t in solution)
        sums = returns(solution)
        primitive_residual = mp.mpf(0)
        for j, t in enumerate(solution):
            # Carrier parity fixes the actual integral slope.
            carrier = powers[j] % 2
            slope = (carrier+powers[j])//2
            meridian = 2*sums[j]-1j*carrier*t
            longitude = 2j*t
            primitive_residual = max(primitive_residual,
                                     abs(meridian+slope*longitude+2j*mp.pi))
        assert primitive_residual < tolerance
        volume = mp.mpf(0)
        action = mp.mpc(0)
        smallest_shape = mp.inf
        smallest_chart_factor = mp.inf
        radial_checks = 0
        for step in range(1, 21):
            scale = mp.mpf(step)/20
            values = tuple(2*mp.atan(scale*mp.tan(t/2)) for t in solution)
            assert all(t.imag < 0 for t in values)
            for v, w in edges:
                t = values[v] if v >= 0 else mp.mpc(0)
                u = values[w] if w >= 0 else mp.mpc(0)
                a, b, q, rt, ru, shapes, psi = edge_data(t, u)
                assert q.real > mp.sqrt(a.real*a.real+b.real*b.real)
                assert all(z.imag > 0 for z in shapes)
                smallest_shape = min(smallest_shape, *(z.imag for z in shapes))
                factors = [q, q+1j, q-1j, q+a, q-a, q+b, q-b,
                           a+1j, a-1j, b+1j, b-1j,
                           (q+b)*(b+1j)/(q*q+1),
                           (q+b)*(b-1j)/(q-1j)**2,
                           2j/(q-1j)]
                smallest_chart_factor = min(smallest_chart_factor,
                                            *(abs(z) for z in factors))
                assert smallest_chart_factor > 0
                radial_checks += 1
                if step == 20:
                    volume += mp.fsum(bloch_wigner(z) for z in shapes)
                    action += psi
        action += mp.fsum(-1j*powers[j]*t*t/(4*mp.pi)-1j*t
                          for j, t in enumerate(solution))
        volume_residual = relative(volume, 2*mp.pi*action.real)
        assert volume_residual < tolerance
        records.append({
            'kind': kind, 'magnitudes': powers,
            'angles': [mp.nstr(t, 40) for t in solution],
            'original_period_residual': mp.nstr(residual, 12),
            'primitive_filling_residual': mp.nstr(primitive_residual, 12),
            'volume': mp.nstr(volume, 40),
            'volume_action_relative_residual': mp.nstr(volume_residual, 12),
            'radial_positive_edge_checks': radial_checks,
            'smallest_sampled_shape_imaginary_part': mp.nstr(smallest_shape, 16),
            'smallest_sampled_chart_factor_modulus': mp.nstr(smallest_chart_factor, 16),
        })
    return {
        'scope': 'Finite original-period, positive-path and volume checks; '
                 'the written proof supplies the marked metric completion.',
        'precision_decimal_digits': precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'volume_dependency_sha256': hashlib.sha256(Path(__file__).with_name(
            'check_positive_edge_volume_identity.py').read_bytes()).hexdigest(),
        'cases': records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'cases': len(result['cases']),
                      'radial_positive_edge_checks': sum(r['radial_positive_edge_checks']
                                                        for r in result['cases']),
                      'output': str(args.output)}))


if __name__ == '__main__':
    main()
