#!/usr/bin/env python3
"""Compare the complete derivative trace with the internal-vertex asymptotic.

This is a numerical normalization check, not a proof of an asymptotic or
of a global contour bound. Both level parities are included by default.
The finite calculation uses every Newton polynomial and every physical
trace node. It does not use the retained wire interval from the proof.

Run from the repository root:
  python3 experiments/check_internal_vertex_asymptotic.py \
    --output repro/results/research-internal-vertex-asymptotic.json
"""

import argparse
import json
from pathlib import Path

import mpmath as mp


def full_edge_at_trace_nodes(level):
    """Return (angle, K(angle,0), angular derivative) at every trace node."""
    top = level - 1
    nodes = [2 * mp.cos((2 * k + 1) * mp.pi / level) for k in range(top)]
    scales = [(2 * mp.sin((k + 1) * mp.pi / level)) ** 2 for k in range(top)]
    complete_values = [mp.mpf(1)]
    for node, scale in zip(nodes, scales):
        complete_values.append(complete_values[-1] * (node + 2) / scale)
    result = []
    for index in range(level):
        angle = 2 * mp.pi * (mp.mpf(top) / 2 - index) / level
        spectral = -2 * mp.cos(angle)
        spectral_derivative = 2 * mp.sin(angle)
        value, derivative = mp.mpf(1), mp.mpf(0)
        kernel, kernel_derivative = mp.mpf(1), mp.mpf(0)
        for k in range(top):
            factor = (nodes[k] - spectral) / scales[k]
            derivative, value = (
                derivative * factor - value * spectral_derivative / scales[k],
                value * factor,
            )
            kernel += value * complete_values[k + 1]
            kernel_derivative += derivative * complete_values[k + 1]
        result.append((angle, kernel, kernel_derivative))
    return result


def stationary_data(degree, power):
    """Compute the proposed saddle, action, and leading coefficient."""
    if degree * degree + power * power < max(1024, 128 * degree):
        raise ValueError("The pair is outside the theorem's stated criterion")
    pi = mp.pi
    initial = -2 * pi * 1j / (degree - 1j * power)
    equation = lambda t: (
        -degree / pi * mp.asinh(mp.tan(t / 2))
        + 1j * power * t / (2 * pi) - 1j
    )
    saddle = mp.findroot(equation, (initial, initial * mp.mpf('1.001')))
    phase = 4 * mp.catalan / pi - saddle / pi * mp.quad(
        lambda s: mp.asinh(mp.tan(s * saddle / 2)), [0, 1]
    )
    action = degree * phase + 1j * power * saddle**2 / (4 * pi) - 1j * saddle
    wire = mp.atan(mp.cos(saddle / 2)) / pi
    wire_hessian = sum(
        -2 * pi * mp.sin(2 * pi * wire) / (mp.cos(2 * pi * wire) + mp.cos(v))
        - 2 * pi / mp.tan(pi * wire)
        for v in (saddle, 0)
    )
    edge_amplitude = mp.sqrt(2 * pi) / (
        4 * mp.sin(pi * wire)**2 * mp.sqrt(-wire_hessian)
    )
    amplitude = (
        1j * mp.sqrt(2 / pi) * mp.sin(saddle) * edge_amplitude**degree
        / mp.sqrt((degree / mp.cos(saddle / 2) - 1j * power) / (2 * pi))
    )
    return saddle, action, amplitude


def complete_trace(level, degree, power, edge_data):
    total = mp.mpc(0)
    for angle, kernel, derivative in edge_data:
        polynomial = kernel**degree
        polynomial_derivative = degree * kernel**(degree - 1) * derivative
        total += mp.exp(1j * power * level * angle**2 / (4 * mp.pi)) * (
            mp.cos(angle) * polynomial
            + mp.sin(angle) * polynomial_derivative
            + 1j * power * level * angle / (2 * mp.pi) * mp.sin(angle) * polynomial
        )
    unit = mp.exp(1j * mp.pi * power * (level - 1)**2 / (4 * level))
    return (-1)**(level - 1) * unit * total, unit


def encode_complex(value):
    return {"real": mp.nstr(mp.re(value), 25), "imag": mp.nstr(mp.im(value), 25)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--levels', default='96,97,192,193,384,385')
    parser.add_argument('--pairs', default='8:32,32:56,64:64,128:0,128:1,128:-7')
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    levels = [int(x) for x in args.levels.split(',')]
    pairs = [tuple(map(int, x.split(':'))) for x in args.pairs.split(',')]
    stationary = {pair: stationary_data(*pair) for pair in pairs}
    rows = []
    for level in levels:
        if level < 3:
            raise ValueError('Levels must be at least three')
        edge_data = full_edge_at_trace_nodes(level)
        for degree, power in pairs:
            saddle, action, amplitude = stationary[degree, power]
            finite, unit = complete_trace(level, degree, power, edge_data)
            leading = (
                unit * mp.mpf(level)**(-mp.mpf(3) * (degree - 1) / 2)
                * amplitude * mp.exp(level * action)
            )
            ratio = finite / leading
            rows.append({
                'level': level, 'degree': degree, 'power': power,
                'finite_over_leading': encode_complex(ratio),
                'level_times_relative_error': encode_complex(level * (ratio - 1)),
            })
        print(f'Computed all {len(pairs)} pairs at level {level}', flush=True)
    result = {
        'scope': 'Numerical comparison of the complete original trace and its proposed leading term; not a proof',
        'decimal_precision': args.precision,
        'stationary_data': [
            {'degree': d, 'power': n, 'saddle': encode_complex(t),
             'action': encode_complex(s), 'amplitude': encode_complex(a)}
            for (d, n), (t, s, a) in stationary.items()
        ],
        'comparisons': rows,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
        print(f'Wrote {args.output}', flush=True)
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
