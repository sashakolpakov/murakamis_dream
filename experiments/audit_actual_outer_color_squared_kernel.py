#!/usr/bin/env python3
"""Exact outer-color aliases and full physical traces; numerical contour examples.

The Gaussian examples are supplementary high-precision checks, not proofs of
the source hypotheses or the uniform analytic theorem in the companion note.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi
from audit_actual_crossing_circle_source_and_filling import (
    crossing_circle, ordinary_module,
)


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def step(a, b, sign=1):
    """sign*z*b-a for ascending integer polynomials."""
    c = [0] + [sign*x for x in b]
    c += [0]*max(0, len(a)-len(c))
    for j, x in enumerate(a):
        c[j] -= x
    return trim(c)


def product(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def remainder(a, p):
    a = a[:]
    assert p[-1] == 1
    while len(a) >= len(p):
        shift, coefficient = len(a)-len(p), a[-1]
        for j, value in enumerate(p):
            a[shift+j] -= coefficient*value
        trim(a)
    return a


def alias(N, h, k):
    """F=1 for k=0, F=2*cos(k theta) otherwise; result divided by N^2."""
    out = 0
    for ell in range(-k//N-3, k//N+4):
        frequency = ell*N-h
        if (k == 0 and frequency == 0) or (k > 0 and abs(frequency) == k):
            out += (1-ell)*(-1)**abs((N-1)*ell)
    return out


def exact_polynomial_cases():
    rows = []
    for N in range(2, 25):
        normal = [[2], [0, 1]]
        for _ in range(2, N+1):
            normal.append(step(normal[-2], normal[-1]))
        P = normal[N][:]
        P[0] += 2
        modes = [[2], [0, -1]]
        for _ in range(2, 3*N+1):
            modes.append(step(modes[-2], modes[-1], -1))
        modes[0] = [1]
        circles = [[0], [1], [0, -1]]
        for _ in range(3, N+1):
            circles.append(step(circles[-2], circles[-1], -1))
        count = 0
        for h in range(N):
            for k, f in enumerate(modes):
                r = remainder(product(circles[N-h], f), P)
                actual = (-1)**(N-1)*(r[N-1] if len(r) == N else 0)
                assert actual == alias(N, h, k), (N, h, k, actual)
                if k < N:
                    assert actual == int(h == k)
                count += 1
        rows.append({'N': N, 'exact_integer_mode_color_checks': count})
    return rows


def literal_physical_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, rho = N-1, (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(a), -1, prime) for a in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(N*N, dtype=np.int64)
    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
    loops = [crossing_circle(target, ordinary_module(j, q, prime), q, eta, prime, N)
             for j in range(1, N+1)]
    modes = [2*I % prime, -O % prime]
    for _ in range(2, 2*N+1):
        modes.append((-O@modes[-1]-modes[-2]) % prime)
    modes[0] = I
    count = 0
    for h in range(N):
        for k, f in enumerate(modes):
            actual = phi(loops[N-h-1]@f % prime, N, pivot, prime)
            assert actual == N*N*alias(N, h, k) % prime
            count += 1
    return {'N': N, 'field_prime': prime, 'literal_mixed_circle_colors': N,
            'full_original_marked_trace_checks': count}


def symbolic_kernel():
    z, N, h, e = sp.symbols('z N h e', nonzero=True)
    E = e*sp.exp(sp.I*N*z)
    K = sp.I*N/(E-1)
    squared = -sp.I*N*N/(E-1)**2
    assert sp.simplify(N*K-sp.I*sp.diff(K, z)-squared) == 0
    # Its double-pole principal part retains exactly the original derivative.
    local = -sp.I*N*N/(sp.exp(sp.I*N*z)-1)**2
    principal = sp.series(local, z, 0, 1)
    assert sp.expand(principal.removeO()).coeff(z, -2) == sp.I
    assert sp.expand(principal.removeO()).coeff(z, -1) == N
    return {'closed_contour_integration_by_parts': 'exact symbolic identity',
            'double_pole_coefficient': 'i', 'simple_pole_coefficient': 'N',
            'dangerous_alias_ell_1_coefficient': 0}


def gaussian_checks():
    mp.mp.dps = 110
    rows = []
    for N in (32, 33, 64, 65, 128, 129):
        for D in (mp.mpc(1, 0), mp.mpc(2, -3)):
            theta = [(2*j-(N-1))*mp.pi/N for j in range(N)]
            values = [mp.exp(-N*D*t*t/(4*mp.pi)) for t in theta]
            derivatives = [-N*D*t/(2*mp.pi)*v for t, v in zip(theta, values)]
            source = []
            for h in range(N):
                value = mp.fsum((N-h)*mp.cos(h*t)*v-mp.sin(h*t)*dv
                               for t, v, dv in zip(theta, values, derivatives))
                source.append(value)
            for h in (0, max(1, N//16)):
                predicted = N**mp.mpf('1.5')/mp.sqrt(D)*mp.exp(-mp.pi*h*h/(N*D))
                # Fixed-window Gaussian is the exact infinite-grid model up
                # to exponentially small endpoint and surviving alias terms.
                assert abs(source[h]/predicted-1) < mp.mpf('0.00001')
            start = (N+3)//4
            complement = max(abs(v) for v in source[start:])
            normalized = complement/N**mp.mpf('1.5')
            assert normalized < 2*mp.exp(-mp.mpf('0.015')*N)
            h = N-1
            values_only = N*mp.fsum(mp.cos(h*t)*v for t, v in zip(theta, values))
            assert abs(source[h]) < mp.mpf('0.02')*abs(values_only)
            rows.append({'N': N, 'D': [float(D.real), float(D.imag)],
                         'complete_source_ratio': [float((source[0]*mp.sqrt(D)/N**mp.mpf('1.5')).real),
                                                   float((source[0]*mp.sqrt(D)/N**mp.mpf('1.5')).imag)],
                         'normalized_outer_complement_max': float(normalized),
                         'opposite_endpoint_full_over_value_only': float(abs(source[h]/values_only))})
    return {'decimal_precision': 110,
            'scope': 'Supplementary finite Gaussian-source calibrations, not uniform-theorem evidence.',
            'families': rows}


if __name__ == '__main__':
    data = {'status': 'PASS', 'exact_squared_kernel': symbolic_kernel(),
            'exact_polynomial_alias_cases': exact_polynomial_cases(),
            'literal_physical_cases': [literal_physical_case(N) for N in range(2, 7)],
            'high_precision_gaussian_checks': gaussian_checks(),
            'scope': 'Exact fixed-root source and alias identities, full literal mixed-circle traces '
                     'over finite fields, and labeled numerical examples. Analytic gap hypotheses '
                     'and actual geometric peripheral identification require their separate proofs.'}
    Path(__file__).with_name('actual_outer_color_squared_kernel_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS exact squared kernel, integer Fourier aliases, five full physical levels, '
          'and twelve high-precision all-parity Gaussian families.')
