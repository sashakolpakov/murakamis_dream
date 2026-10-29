#!/usr/bin/env python3
"""Coherent CLASSICAL 6_1 companion products, not a quantum-A calculation.

The quartic is supplied by the exact classical Newton/peripheral
calculation.  This experiment neither constructs the actual quantum
operator nor identifies a source-selected solution.  It tests the norm
of the whole classical companion product from the half orbit to 1.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import quad


def coefficients(Y):
    """Descending coefficients a_4,...,a_0 of the supplied quartic."""
    return [
        Y**4,
        -Y**8 + Y**7 + 3*Y**4 + 3*Y**3 - 2*Y**2,
        Y**8 - 3*Y**7 - Y**6 + 3*Y**5 + 6*Y**4
        + 3*Y**3 - Y**2 - 3*Y + 1,
        -2*Y**6 + 3*Y**5 + 3*Y**4 + Y - 1,
        Y**4,
    ]


def frobenius(A):
    return mp.sqrt(mp.fsum(abs(A[i, j])**2
                           for i in range(A.rows) for j in range(A.cols)))


def coherent_product(N, dps, start_shift=0):
    """P=T((N-1)/N)...T((N/2+start_shift)/N), rescaled each step."""
    started = time.monotonic()
    with mp.workdps(dps):
        P = mp.eye(4)
        log_scale = mp.mpf(0)
        largest_step = mp.mpf(0)
        start = N//2 + start_shift
        for j in range(start, N):
            Y = mp.exp(2j*mp.pi*j/N)
            a4, a3, a2, a1, a0 = coefficients(Y)
            row = [-a0/a4, -a1/a4, -a2/a4, -a3/a4]
            next_P = mp.matrix(4, 4)
            for k in range(4):
                next_P[0, k], next_P[1, k], next_P[2, k] = (
                    P[1, k], P[2, k], P[3, k])
                next_P[3, k] = mp.fsum(row[i]*P[i, k] for i in range(4))
            scale = frobenius(next_P)
            largest_step = max(largest_step, scale)
            log_scale += mp.log(scale)
            P = next_P/scale

        # The Frobenius normalization alone would already determine the
        # exponential rate: ||P||_2 <= ||P||_F <= 2||P||_2.
        singular = mp.svd(P, compute_uv=False)
        log_operator = log_scale + mp.log(singular[0])
        return {
            "N": N,
            "dps": dps,
            "start_index": start,
            "last_index": N-1,
            "steps": N-start,
            "log_operator_norm": mp.nstr(log_operator, 80),
            "operator_rate": mp.nstr(log_operator/N, 65),
            "frobenius_rate": mp.nstr(log_scale/N, 65),
            "normalized_largest_singular_value": mp.nstr(singular[0], 30),
            "largest_one_step_rescaling": mp.nstr(largest_step, 20),
            "seconds": round(time.monotonic()-started, 3),
            "normalized_matrix": [[[mp.nstr(mp.re(P[i, j]), 85),
                                     mp.nstr(mp.im(P[i, j]), 85)]
                                   for j in range(4)] for i in range(4)],
        }


def paired_precision_case(N):
    low = max(100, math.ceil(N/3))
    high = low + max(64, math.ceil(N/6))
    a = coherent_product(N, low)
    b = coherent_product(N, high)
    with mp.workdps(high):
        error = abs(mp.mpf(a["log_operator_norm"])-mp.mpf(b["log_operator_norm"]))
        matrix_error = max(abs(mp.mpc(*a["normalized_matrix"][i][j])
                               - mp.mpc(*b["normalized_matrix"][i][j]))
                           for i in range(4) for j in range(4))
        assert error < mp.mpf('1e-55'), (N, error)
        assert matrix_error < mp.mpf('1e-55'), (N, matrix_error)
        b["lower_precision"] = low
        b["precision_check_log_norm_error"] = mp.nstr(error, 8)
        b["precision_check_normalized_matrix_error"] = mp.nstr(matrix_error, 8)
    del b["normalized_matrix"]
    return b


def scalar_envelope():
    def value(x):
        Y = np.exp(2j*np.pi*x)
        roots = np.roots(coefficients(Y))
        return float(np.log(max(abs(roots))))
    value_, error = quad(value, .5, 1, points=[5/6], epsabs=2e-10,
                         epsrel=2e-10, limit=500)
    return {"pointwise_spectral_radius_half_integral": value_,
            "quadrature_error_estimate": error}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--levels', nargs='+', type=int,
                        default=[128, 256, 512, 1024])
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name(
                            'six_one_coherent_classical_transfer_results.json'))
    args = parser.parse_args()
    data = {"status": "PASS", "scope": (
        "Classical companion matrices only. No actual quantum annihilator, "
        "original color source, or theorem about the Kashaev invariant is "
        "being computed by this diagnostic."),
        "product_convention": (
            "T((N-1)/N)...T((N/2)/N), with the usual forward companion "
            "for state (u_j,u_{j+1},u_{j+2},u_{j+3})."),
        "spectral_envelope": scalar_envelope(), "products": []}
    for N in args.levels:
        assert N % 2 == 0
        result = paired_precision_case(N)
        data["products"].append(result)
        args.output.write_text(json.dumps(data, indent=2)+'\n')
        print(json.dumps(result, indent=2), flush=True)
    print(json.dumps(data["spectral_envelope"], indent=2), flush=True)


if __name__ == '__main__':
    main()
