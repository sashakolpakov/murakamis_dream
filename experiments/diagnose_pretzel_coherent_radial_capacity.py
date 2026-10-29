#!/usr/bin/env python3
"""Coherent original augmented-pretzel base and radial-capacity diagnostics.

All original source normal terms and winding channels are included by
the exact Phi2 formula. Numerical maxima/rates are diagnostics, not an
asymptotic theorem or a rigorous circle supremum certificate.
"""

import argparse
import json
from pathlib import Path

import mpmath as mp


def source_polynomial(N, dps):
    mp.mp.dps = dps
    d, M = N-1, (N-1)//2
    q = mp.exp(mp.pi*1j/N)
    Q, x, kappa = q*q, q**d, mp.exp(mp.pi*1j*d*d/(2*N))
    sine = [mp.mpf(1)]
    for a in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*a/N))
    diag = [q+1/q-q*(1-Q**u)**2-(1-Q**(u+1))**2/q for u in range(M+1)]
    off = [-(1-Q**(u+1))**2 for u in range(M+1)]
    fs = [[mp.mpc(1)]]
    if M:
        fs.append([-diag[0]/off[0], 1/off[0]])
    for v in range(1, M):
        out = [mp.mpc(0)]*(v+2)
        for k, a in enumerate(fs[v]):
            out[k] -= diag[v]*a
            out[k+1] += a
        for k, a in enumerate(fs[v-1]):
            out[k] -= off[v-1]*a
        fs.append([a/off[v] for a in out])
    coefficients = [mp.mpc(0)]*(M+1)
    for v in range(M+1):
        b = N*N*sine[2*v]/sine[v]**4
        for k, a in enumerate(fs[v]):
            coefficients[k] += b*a/kappa
    return q, coefficients


def evaluate(coefficients, z):
    value, derivative = mp.mpc(0), mp.mpc(0)
    for a in reversed(coefficients):
        derivative = derivative*z+value
        value = value*z+a
    return value, derivative


def original_period(N, s, q, coefficients):
    total = mp.mpc(0)
    for j in range(N//2):
        c = q**(2*j+1)+q**(-2*j-1)
        value, derivative = evaluate(coefficients, c)
        total += (4-c*c)*s*derivative*value**(s-1)-c*value**s
    total *= (-1)**(N-1)
    if N % 2:
        total += evaluate(coefficients, -2)[0]**s
    return total


def golden_max(function, left, right, steps=75):
    phi = (mp.sqrt(5)-1)/2
    a, b = right-phi*(right-left), left+phi*(right-left)
    fa, fb = function(a), function(b)
    for _ in range(steps):
        if fa < fb:
            left, a, fa = a, b, fb
            b = left+phi*(right-left)
            fb = function(b)
        else:
            right, b, fb = b, a, fa
            a = right-phi*(right-left)
            fa = function(a)
    theta = (left+right)/2
    return theta, function(theta)


def lobachevsky(theta):
    return mp.im(mp.polylog(2, mp.exp(2j*theta)))/2


def capacity_case(N, s, q, coefficients, grid):
    c = 2-4/mp.cos(mp.pi/s)**2
    R = (-c+mp.sqrt(c*c-4))/2
    def objective(theta):
        w = R*mp.exp(1j*theta)
        return mp.log(abs(evaluate(coefficients, w+1/w)[0]))
    step = 2*mp.pi/grid
    samples = [objective(k*step) for k in range(grid)]
    candidates = []
    for k in range(grid):
        if samples[k] >= samples[(k-1) % grid] and samples[k] >= samples[(k+1) % grid]:
            candidates.append(golden_max(objective, (k-1)*step, (k+1)*step))
    theta, maximum = max(candidates, key=lambda item: item[1])
    value_at_negative = objective(mp.pi)
    period = original_period(N, s, q, coefficients)
    target = 4*s/mp.pi*(lobachevsky(mp.pi/4+mp.pi/(2*s))
                        +lobachevsky(mp.pi/4-mp.pi/(2*s)))
    return {'N': N, 'boxes': s, 'dps': mp.mp.dps, 'angle_grid': grid,
            'classical_candidate_radius': float(R),
            'coherent_circle_capacity_rate': float(s*maximum/N-mp.log(R)),
            'negative_axis_capacity_rate': float(s*value_at_negative/N-mp.log(R)),
            'maximizer_theta_over_pi': float((theta % (2*mp.pi))/mp.pi),
            'original_complete_base_log_modulus_over_N': float(mp.log(abs(period))/N),
            'candidate_antiprism_action_rate': float(target),
            'original_period_real': mp.nstr(mp.re(period), 35),
            'original_period_imaginary': mp.nstr(mp.im(period), 35),
            'scope': 'Coherent exact-source diagnostic; no certified global circle maximum or asymptotic limit.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--levels', type=int, nargs='+', default=[16, 32, 64, 128])
    parser.add_argument('--boxes', type=int, nargs='+', default=[3, 5, 7, 9])
    parser.add_argument('--dps-extra', type=int, default=0)
    parser.add_argument('--output', default='pretzel_coherent_radial_capacity_diagnostics.json')
    args = parser.parse_args()
    rows = []
    for N in args.levels:
        dps = max(120, N)+args.dps_extra
        q, coefficients = source_polynomial(N, dps)
        for s in args.boxes:
            row = capacity_case(N, s, q, coefficients, max(256, 4*N))
            rows.append(row)
            print(f'N={N} s={s} dps={dps} capacity={row["coherent_circle_capacity_rate"]:.12f} '
                  f'axis={row["negative_axis_capacity_rate"]:.12f} '
                  f'period={row["original_complete_base_log_modulus_over_N"]:.12f} '
                  f'target={row["candidate_antiprism_action_rate"]:.12f} '
                  f'theta/pi={row["maximizer_theta_over_pi"]:.9f}', flush=True)
    Path(__file__).with_name(args.output).write_text(json.dumps({
        'status': 'DIAGNOSTIC', 'rows': rows,
        'scope': 'Original complete augmented-pretzel source; all jets/windings retained. No limit or geometric survival proof.'}, indent=2)+'\n')
