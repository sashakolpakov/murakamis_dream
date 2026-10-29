#!/usr/bin/env python3
"""Actual pointed figure-eight energy and off-root-circle bulk estimate."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np


def coefficients(Q, Y):
    g = Q**2*Y**2-Q*Y**4+Q*Y**3+Q*Y-Q+Y**2
    return (Y**2*(Q-Y)*(Q*Y**2-1),
            -(Y-1)**2*(Y+1)*g,
            Y**2*(Q*Y-1)*(Q-Y**2),
            Y*(Y+1)*(Q-Y**2)*(Q*Y**2-1))


def actual_period(N, Q):
    # The independently proved original whole-source Newton expression.
    # Exact root zeros are imposed before summing, not approximated by
    # tiny floating factors and then multiplied by large later terms.
    out = []
    for j in range(1, N+1):
        h = 2*mp.cos(2*mp.pi*j/N)
        maximum = N-1 if j == N else min(j, N-j)-1
        t = mp.mpf(1)
        value = mp.mpf(1)
        for k in range(1, maximum+1):
            t *= h-2*mp.cos(2*mp.pi*k/N)
            value += t
        out.append(complex(value))
    return np.array(out)


def actual_system(N):
    Q = mp.exp(2j*mp.pi/N)
    y = actual_period(N, Q)
    M = np.zeros((N, N), complex)
    b = np.zeros(N, complex)
    row_colors = []
    # Actual fixed-small-color initial equations; all full constants,
    # including the final complete coordinate, remain in y.
    for j in range(1, 4):
        M[j-1, j-1] = 1
        b[j-1] = y[j-1]
        row_colors.append(j)
    # Homogenize the original affine C F=D by D T C-D(QY)C.
    # A base-j row contains physical colors j,...,j+3.
    for j in range(1, N-2):
        cm1, c01, cp1, D1 = coefficients(Q, Q**(j+1))
        cm2, c02, cp2, D2 = coefficients(Q, Q**(j+2))
        cs = [-D2*cm1, D1*cm2-D2*c01, D1*c02-D2*cp1, D1*cp2]
        row = j+2
        for i, c in enumerate(cs):
            M[row, j+i-1] = complex(c)
        row_colors.append(j)
    assert len(row_colors) == N
    error = np.linalg.norm(M@y-b)
    assert error < 1e-10*max(1., np.linalg.norm(b)), (N, error)
    return M, b, y, np.array(row_colors)


def case(N):
    M, b, y, rows = actual_system(N)
    gamma = -np.log(2.5)
    columns = np.arange(1, N+1)
    # Evaluate conjugated entries directly through LOCAL ratios.
    L = M*np.exp(gamma*(rows[:, None]-columns[None, :]))
    u = np.exp(gamma*columns)*y
    source = np.exp(gamma*rows)*b
    residual = np.linalg.norm(L@u-source)
    assert residual < 1e-10*max(1., np.linalg.norm(source))
    energy_error = abs(np.vdot(L@u, L@u).real-np.vdot(source, source).real)
    assert energy_error < 1e-9*max(1., np.vdot(source, source).real)

    selected = np.where((columns/N >= .23) & (columns/N <= .27))[0]
    restricted = L[:, selected]
    minimum = np.linalg.svd(restricted, compute_uv=False)[-1]
    assert minimum > 1

    # Full original cutoff equation, with its transition current kept.
    x = columns/N
    cutoff = np.maximum(0., np.minimum(1., np.minimum((x-.23)/.01, (.27-x)/.01)))
    xr = rows/N
    cutoff_rows = np.maximum(0., np.minimum(1., np.minimum((xr-.23)/.01, (.27-xr)/.01)))
    commutator = L*cutoff[None, :]-cutoff_rows[:, None]*L
    left = L@(cutoff*u)
    right = cutoff_rows*source+commutator@u
    assert np.linalg.norm(left-right) < 1e-11*max(1., np.linalg.norm(left))
    # Fixed bandwidth gives the displayed O(1/N) coefficient cutoff bound.
    assert N*np.linalg.norm(commutator, 2) < 614400
    return {'N': N, 'original_pointed_boundary_source_energy': float(np.vdot(source, source).real),
            'weighted_actual_energy_identity_error': float(energy_error),
            'off_root_circle_bulk_minimum_singular_value': float(minimum),
            'cutoff_boundary_current_norm_times_N': float(N*np.linalg.norm(commutator, 2)),
            'initial_actual_colors': [[z.real, z.imag] for z in y[:3]]}


def main():
    mp.mp.dps = 110
    rows = [case(N) for N in [32, 48, 64, 96, 128]]
    data = {'status': 'PASS', 'actual_pointed_energy_and_bulk_families': rows,
            'scope': 'Exact actual source and weighted local coercivity/cutoff identities. End/turning/resonance packets remain; no sharp geometric growth or source-normal uniqueness is inferred from the scalar audit.'}
    Path(__file__).with_name('actual_pointed_a_bulk_agmon_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS 5 actual full-source weighted energies, off-root-circle bulk gaps and retained cutoff currents')


if __name__ == '__main__':
    main()
