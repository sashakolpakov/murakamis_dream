#!/usr/bin/env python3
"""Check the original U-inserted trace and its Gaussian normalization.

Small levels compare the original crossing matrix with the complete
physical-node formula. Larger levels compare the exact nodal sum with
the proved leading term. These are finite-precision diagnostics.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_internal_vertex_asymptotic import full_edge_at_trace_nodes


def inserted_nodes(level, degree, power, data):
    eta = (-1) ** (level - 1)
    unit = mp.exp(1j * mp.pi * power * (level - 1)**2 / (4 * level))
    total = mp.fsum(
        t * mp.sin(t) * mp.exp(1j * power * level * t*t / (4 * mp.pi))
        * kernel**degree
        for t, kernel, _ in data
    )
    return 1j * eta * unit * level**2 / mp.pi * total


def original_matrices(level):
    """Use the recorded crossing and Newton multiplication matrices."""
    top = level - 1
    q = mp.exp(1j * mp.pi / level)
    kappa = q ** (mp.mpf(top**2) / 2)
    sine_factorials = [mp.mpf(1)]
    for k in range(1, level):
        sine_factorials.append(sine_factorials[-1] * 2 * mp.sin(mp.pi * k / level))
    crossing = mp.matrix(level)
    z = mp.matrix(level)
    for j in range(level):
        z[j, j] = 2 * mp.cos((2*j + 1) * mp.pi / level)
        if j < top:
            z[j + 1, j] = -4 * mp.sin(mp.pi * (j + 1) / level)**2
        for k in range(j, level):
            crossing[k, j] = (
                kappa * (-1)**k * q**(k*(j + 1))
                * sine_factorials[k] / (sine_factorials[j] * sine_factorials[k-j])
            )
    identity = mp.eye(level)
    basis_matrix = identity.copy()
    complete_value = mp.mpf(1)
    kernel = identity.copy()
    for k in range(top):
        node = 2 * mp.cos((2*k + 1) * mp.pi / level)
        scale = 4 * mp.sin(mp.pi * (k + 1) / level)**2
        basis_matrix = (node * identity - z) * basis_matrix / scale
        complete_value *= (node + 2) / scale
        kernel += complete_value * basis_matrix
    nilpotent = (-1)**top * crossing**(2 * level) - identity
    return crossing, kernel, nilpotent


def encode(value):
    return {"real": mp.nstr(mp.re(value), 30), "imag": mp.nstr(mp.im(value), 30)}


def run(precision):
    mp.mp.dps = precision
    matrix_rows = []
    pairs = [(1, 0), (2, 1), (3, -2)]
    for level in (4, 5, 8, 9):
        crossing, kernel, nilpotent = original_matrices(level)
        data = full_edge_at_trace_nodes(level)
        nilpotence_error = mp.norm(nilpotent * nilpotent)
        if nilpotence_error > mp.mpf("1e-45"):
            raise ArithmeticError("The original-matrix nilpotence diagnostic failed")
        expected_trace = 1j * (-1)**(level-1) * level**2 / mp.sin(mp.pi/level)
        if abs(nilpotent[level-1, 0] - expected_trace) > mp.mpf("1e-45"):
            raise ArithmeticError("The closed inserted-trace normalization failed")
        for degree, power in pairs:
            value = (crossing**power * nilpotent * kernel**degree)[level-1, 0]
            nodal = inserted_nodes(level, degree, power, data)
            relative = abs(value - nodal) / max(1, abs(value), abs(nodal))
            if relative > mp.mpf("1e-45"):
                raise ArithmeticError("The original matrix and nodal insertion disagree")
            matrix_rows.append({
                "N": level, "degree": degree, "power": power,
                "matrix_value": encode(value),
                "nodal_value": encode(nodal),
                "relative_difference": mp.nstr(relative, 30),
                "nilpotence_error": mp.nstr(nilpotence_error, 30),
            })
    asymptotic_rows = []
    for level in (24, 25, 48, 49, 96, 97):
        data = full_edge_at_trace_nodes(level)
        for degree, power in pairs:
            eta = (-1)**(level-1)
            unit = mp.exp(1j * mp.pi * power * (level-1)**2 / (4*level))
            amplitude = 2j * eta * unit * mp.mpf(4)**(-degree) / (degree-1j*power)**mp.mpf("1.5")
            leading = (
                amplitude * mp.mpf(level)**(-mp.mpf(3)*(degree-1)/2)
                * mp.exp(level * degree * 4 * mp.catalan / mp.pi)
            )
            ratio = inserted_nodes(level, degree, power, data) / leading
            asymptotic_rows.append({
                "N": level, "degree": degree, "power": power,
                "finite_over_leading": encode(ratio),
                "N_times_relative_error": encode(level * (ratio - 1)),
            })
        print(f"Checked insertion asymptotics at N={level}.", flush=True)
    return {
        "scope": "Original-matrix and full-node normalization diagnostics; not a substitute for the written proof.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matrix_checks": matrix_rows,
        "asymptotic_checks": asymptotic_rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Saved {args.output}.")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
