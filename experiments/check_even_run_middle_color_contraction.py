#!/usr/bin/env python3
"""Check the frozen and original varying even-run contraction matrices.

The interval-uniform estimates are proved in the accompanying note.
These finite checks test channel indexing, Robin parameters and constants;
they do not replace the all-angle or all-level proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def infinity_norm(matrix):
    return max(mp.fsum(abs(matrix[i, j]) for j in range(matrix.cols))
               for i in range(matrix.rows))


def euclidean_norm(matrix):
    return mp.svd(matrix, compute_uv=False)[0]


def channel(k, r, robin):
    out = (r+1/r)*mp.eye(k)
    for i in range(k-1):
        out[i, i+1] = out[i+1, i] = -1
    out[0, 0] -= r
    out[k-1, k-1] -= robin
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    frozen_records = []
    varying_records = []
    two_step_records = []
    for k in range(2, 9):
        block_length = k+1
        delta = mp.mpf(1)/(9*4**(k-1))
        level_bound = 216*block_length*(4*block_length+2)*4**(k-1)
        robins = [mp.mpc(0), mp.mpc(1), mp.mpc(-1), mp.mpc(0, 1),
                  mp.exp(mp.mpc(0, mp.mpf("0.37")))]
        for angle_fraction in [mp.mpf(1)/2, mp.mpf(2)/3, mp.mpf(1),
                               mp.mpf(4)/3, mp.mpf(3)/2]:
            theta = angle_fraction*mp.pi
            w = 2-2*mp.cos(theta)
            for robin in robins:
                matrix = channel(k, mp.exp(-1j*theta), robin)/w
                square = matrix*matrix
                row_loss = 1-mp.fsum(abs(square[0, j]) for j in range(k))
                power_norm = infinity_norm(matrix**block_length)
                comparison = mp.matrix(k, k)
                for i in range(k):
                    for j in range(k):
                        comparison[i, j] = abs(square[i, j])
                comparison_radius = mp.eigsy(comparison, eigvals_only=True)[k-1]
                two_step_gap = mp.mpf(1)/(32*k*k)
                assert infinity_norm(matrix) <= 1+tolerance
                assert row_loss >= mp.mpf(1)/9-tolerance
                assert power_norm <= 1-delta+tolerance
                assert comparison_radius <= 1-two_step_gap+tolerance
                square_norm = euclidean_norm(square)
                assert square_norm <= comparison_radius+tolerance
                if k >= 3:
                    assert comparison[0, 1] >= mp.mpf(1)/16-tolerance
                    for i in range(k-2):
                        assert abs(comparison[i, i+2]-1/w**2) < tolerance
                for j in range(1, k+1):
                    unique_path = (matrix**(j-1))[j-1, 0]
                    assert abs(unique_path-(-1/w)**(j-1)) < tolerance
                frozen_records.append({
                    "channels": k,
                    "angle_over_pi": str(angle_fraction),
                    "robin": [str(mp.re(robin)), str(mp.im(robin))],
                    "first_row_square_loss": mp.nstr(row_loss, 22),
                    "block_norm": mp.nstr(power_norm, 22),
                    "proved_block_upper_bound": mp.nstr(1-delta, 22),
                    "square_comparison_radius": mp.nstr(comparison_radius, 22),
                    "square_euclidean_norm": mp.nstr(square_norm, 22),
                    "proved_square_euclidean_bound": mp.nstr(1-two_step_gap, 22),
                })
        for level in (level_bound, level_bound+1):
            q = mp.exp(mp.pi*1j/level)
            starts = [(level+3)//4, level//2,
                      (3*level)//4-block_length+1]
            input_colors = (0, level//7, level//2)
            for first in starts:
                for input_color in input_colors:
                    lam = mp.exp(-2*mp.pi*1j*input_color/level)
                    product = mp.eye(k)
                    for color in range(first, first+block_length):
                        theta = 2*mp.pi*color/level
                        assert mp.pi/2-tolerance <= theta <= 3*mp.pi/2+tolerance
                        original = channel(
                            k, q*mp.exp(-2*mp.pi*1j*color/level), lam/q)
                        original /= 4*mp.sin(mp.pi*color/level)**2
                        product = original*product
                    bound = 1-delta/2
                    norm = infinity_norm(product)
                    assert norm <= bound+tolerance
                    varying_records.append({
                        "channels": k, "N": level, "first_backward_color": first,
                        "input_color": input_color,
                        "block_norm": mp.nstr(norm, 22),
                        "proved_block_upper_bound": mp.nstr(bound, 22),
                    })
        for level in (2048*k*k, 2048*k*k+1):
            q = mp.exp(mp.pi*1j/level)
            starts = [(level+3)//4, level//2, (3*level)//4-1]
            for first in starts:
                for input_color in (0, level//7, level//2):
                    lam = mp.exp(-2*mp.pi*1j*input_color/level)
                    product = mp.eye(k)
                    for color in (first, first+1):
                        theta = 2*mp.pi*color/level
                        assert mp.pi/2-tolerance <= theta <= 3*mp.pi/2+tolerance
                        original = channel(
                            k, q*mp.exp(-2*mp.pi*1j*color/level), lam/q)
                        original /= 4*mp.sin(mp.pi*color/level)**2
                        product = original*product
                    bound = 1-mp.mpf(1)/(64*k*k)
                    norm = euclidean_norm(product)
                    assert norm <= bound+tolerance
                    two_step_records.append({
                        "channels": k, "N": level, "first_backward_color": first,
                        "input_color": input_color,
                        "two_step_euclidean_norm": mp.nstr(norm, 22),
                        "proved_upper_bound": mp.nstr(bound, 22),
                    })
    return frozen_records, varying_records, two_step_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    frozen, varying, two_step = run(args.precision)
    result = {
        "status": "pass",
        "precision_decimal_digits": args.precision,
        "scope": "Finite normalization and constant checks for frozen channels "
                 "and actual varying physical-input blocks; the uniform "
                 "contraction is established by the written proof.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "frozen_checks": frozen, "varying_checks": varying,
        "two_step_varying_checks": two_step,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "frozen_cases": len(frozen),
        "varying_cases": len(varying), "two_step_cases": len(two_step),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
