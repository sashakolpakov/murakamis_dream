#!/usr/bin/env python3
"""Check the exact logarithmic-factorial representative of the odd Ward coupon.

Full physical values and angular derivatives are compared against the
original Newton polynomial at every node, both parities. Additional
off-grid checks retain the exact period defect and test the stated
interior expansion. These diagnostics do not prove a missing contour
deformation.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_amplified_zero_block_composition import newton_values_and_derivatives, dot
from check_twist_period_insertion import encode


def factorial_log_derivatives(N, z):
    theta = mp.pi / N
    values, derivatives = [], []
    for k in range(N):
        w = z - k
        if abs(w) < mp.power(10, -mp.mp.dps // 2):
            values.append(1 / theta)
            derivatives.append(mp.mpf(0))
        else:
            cot = mp.cot(theta * w)
            values.append(w * cot)
            derivatives.append(cot - theta * w / mp.sin(theta * w) ** 2)
    scale = mp.pi / N ** 2
    return scale * mp.fsum(values), scale * mp.fsum(derivatives)


def ward_function(N, t):
    theta, sigma = mp.pi / N, (-1) ** N
    z = (N - 1) / 2 - t / (2 * theta)
    first, second = factorial_log_derivatives(N, z)
    first_zero = factorial_log_derivatives(N, mp.mpf(0))[0]
    value = sigma * (2 * mp.cos(theta)
                     + 2 * mp.sin(theta) / theta * (first - first_zero))
    derivative = -sigma * mp.sin(theta) / theta ** 2 * second
    return value, derivative


def coefficients(N):
    theta = mp.pi / N
    return [(-1) ** N * 2 * mp.cos(theta)] + [
        (-1) ** (N + k + 1) * mp.sin(theta) / mp.sin(k * theta)
        for k in range(1, N)]


def run(precision):
    mp.mp.dps = precision
    records = []
    for N in range(2, 25):
        c = coefficients(N)
        largest = mp.mpf(0)
        for j in range(N):
            t = mp.pi * (N - 1 - 2 * j) / N
            values, derivatives = newton_values_and_derivatives(N, t)
            polynomial = dot(c, values), dot(c, derivatives)
            interpolated = ward_function(N, t)
            error = max(abs(a - b) / max(1, abs(a), abs(b))
                        for a, b in zip(polynomial, interpolated))
            largest = max(largest, error)
            if error > mp.mpf('1e-50'):
                raise ArithmeticError(('Physical value or normal mismatch', N, j, error))
        records.append({'N': N, 'physical_nodes': N,
                        'maximum_full_jet_relative_error': mp.nstr(largest, 35)})
    periods = []
    for N in (3, 4, 7, 8, 17, 18):
        for t in (mp.mpc('.19', '.23'), mp.mpc('1.2', '-.4')):
            v = ward_function(N, t)[0]
            shifted = ward_function(N, t + 2 * mp.pi)[0]
            z = (N - 1) / 2 - N * t / (2 * mp.pi)
            defect = -2 * (-1) ** N * N * mp.sin(mp.pi / N) * mp.cot(mp.pi * z)
            error = abs(shifted - v - defect) / max(1, abs(shifted), abs(v), abs(defect))
            if error > mp.mpf('1e-50'):
                raise ArithmeticError(('Period defect mismatch', N, t, error))
            periods.append({'N': N, 'angle': encode(t),
                            'relative_error': mp.nstr(error, 35)})
    expansion = []
    for N in (32, 64, 128, 256):
        for t in (mp.mpc(0), mp.mpc('.13', '-.17'), mp.mpc('1.2', '.4')):
            exact = ward_function(N, t)[0]
            model = (-1) ** N * (
                2 * mp.log(N)
                + 2 * (1 + mp.euler - mp.log(mp.pi) + mp.log(mp.cos(t / 2))))
            expansion.append({
                'N': N, 'angle': encode(t),
                'N_squared_error_over_log_N': encode((exact - model) * N ** 2 / mp.log(N)),
            })
    return {
        'scope': ('Exact physical-jet and off-grid period-defect diagnostics; '
                  'finite interior expansion comparisons, not a global contour proof.'),
        'decimal_precision': precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'full_jet_checks': records,
        'period_defect_checks': periods,
        'interior_expansion_checks': expansion,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--precision', type=int, default=100)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    data = run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2) + '\n')
        print(f'Saved {args.output}.')
    else:
        print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()

