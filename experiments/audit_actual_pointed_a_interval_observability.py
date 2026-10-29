#!/usr/bin/env python3
"""Finite-interval ORIGINAL source packets and controlled nonnormal Green kernels."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_pointed_a_bulk_agmon import actual_system


def actual_intervals():
    rows_out = []
    for N in [64, 96, 128, 192, 256]:
        M, b, y, rows = actual_system(N)
        columns = np.arange(1, N+1)
        gamma = -np.log(1.5)
        L = M*np.exp(gamma*(rows[:, None]-columns[None, :]))
        u = np.exp(gamma*columns)*y
        ids = np.where((columns/N >= .1) & (columns/N <= .3))[0]
        a, z = columns[ids[0]], columns[ids[-1]]
        # Keep ALL output rows of the restriction, including leakage.
        A = L[:, ids]
        minimum = np.linalg.svd(A, compute_uv=False)[-1]
        assert minimum > .5
        zero = np.zeros_like(u)
        zero[ids] = u[ids]
        h = L@zero
        # Forward stencil j,...,j+3: every other surviving output is
        # an explicit left or right boundary source, not a discarded row.
        interior = (np.arange(N) >= 3) & (rows >= a) & (rows <= z-3)
        assert np.linalg.norm(h[interior]) < 1e-10*max(1., np.linalg.norm(h))
        boundary_columns = np.zeros_like(u)
        boundary_ids = list(ids[:3])+list(ids[-3:])
        boundary_columns[boundary_ids] = u[boundary_ids]
        h_boundary = L@boundary_columns
        h_boundary[interior] = 0
        error = np.linalg.norm(h-h_boundary)
        assert error < 1e-10*max(1., np.linalg.norm(h))
        assert np.linalg.norm(zero) <= 2*np.linalg.norm(h)
        # Explicit left inverse with full outputs reconstructs the SAME
        # actual interval vector. No square Dirichlet inverse is used.
        reconstructed = np.linalg.lstsq(A, h, rcond=None)[0]
        reconstruction_error = np.linalg.norm(reconstructed-u[ids])
        assert reconstruction_error < 1e-11*max(1., np.linalg.norm(u[ids]))
        rows_out.append({'N': N, 'actual_interval_colors': [int(a), int(z)],
                         'full_output_minimum_singular_value': float(minimum),
                         'actual_interval_norm': float(np.linalg.norm(zero)),
                         'retained_boundary_source_norm': float(np.linalg.norm(h)),
                         'boundary_source_identity_error': float(error),
                         'full_output_reconstruction_error': float(reconstruction_error)})
    return rows_out


def nonnormal_green():
    alpha = .2
    A0 = np.array([[1., 3.], [0., 1.]])
    J = np.array([[0., 1.], [0., 0.]])
    eta = np.linalg.svd(A0, compute_uv=False)[-1]-alpha
    assert eta > .1
    mu = eta/8
    kernel = lambda r: (-alpha)**r*(np.eye(2)-3*(r+1)*J) if r >= 0 else np.zeros((2, 2))
    maximum_scaled = 0.
    for r in range(81):
        value = kernel(r)
        maximum_scaled = max(maximum_scaled, np.linalg.norm(value, 2)*np.exp(mu*r))
        assert np.linalg.norm(value, 2) <= 4/eta*np.exp(-mu*r)
        product = A0@value+alpha*kernel(r-1)
        expected = np.eye(2) if r == 0 else np.zeros((2, 2))
        assert np.linalg.norm(product-expected) < 1e-13
    return {'nonnormal_Jordan_block': A0.tolist(), 'proved_symbol_gap': float(eta),
            'explicit_Green_kernel_checks': 81, 'maximum_exponentially_weighted_entry': float(maximum_scaled)}


def shrinking_gap():
    rows = []
    for N in [64, 128, 256, 512, 1024]:
        eta = N**(-1/3)
        alpha = 1-eta
        mu = eta/8
        # Whole-line I-alpha*T: exact one-sided Green coefficients.
        for r in [0, 1, N//4, N, 2*N]:
            exact = alpha**r
            assert exact <= 4/eta*np.exp(-mu*r)
        rows.append({'N': N, 'gap': float(eta), 'uniform_inverse_bound': float(2/eta),
                     'certified_decay_length': float(1/mu)})
    return rows


def wrong_compression():
    rows = []
    for n in [8, 16, 24]:
        T = np.diag(np.ones(n-1), 1)
        compressed = np.eye(n)-2*T
        inverse = np.linalg.inv(compressed)
        assert inverse[0, -1] == 2**(n-1)
        assert np.linalg.norm(inverse, 2) >= 2**(n-1)
        rows.append({'length': n, 'unit_circle_gap': 1,
                     'wrong_boundary_inverse_entry': float(inverse[0, -1])})
    return rows


def main():
    mp.mp.dps = 110
    data = {'status': 'PASS', 'actual_source_intervals': actual_intervals(),
            'nonnormal_resolvent': nonnormal_green(), 'shrinking_gap_family': shrinking_gap(),
            'boundary_condition_caution': wrong_compression(),
            'scope': 'Actual weighted boundary packets and broad operator resolvent estimates. No unproved knot boundary data, geometric component identification or sharp volume upper bound is assumed.'}
    Path(__file__).with_name('actual_pointed_a_interval_observability_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS 5 actual full-source intervals, 81 nonnormal Green entries, '
          '5 shrinking-gap families and 3 boundary-compression checks')


if __name__ == '__main__':
    main()
