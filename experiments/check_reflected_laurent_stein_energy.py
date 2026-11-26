#!/usr/bin/env python3
"""Check the original reflected affine row, its energy and its inertia.

The uniform estimates and all-rank inertia statements are proved in the
research note. These finite computations only check the exact source
normalization, matrix reshaping and constants.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_two_run_monodromy_source_jets import (
    data, monodromy, relative, step, transfer_clock,
)


def affine_matrix(level, channels, clock):
    power = 2*channels
    full = monodromy(level, power, -power, clock, [1]*level, 1/clock)
    size = channels*channels
    upper = full[:size, :size]
    row = full[size, :size]*(mp.eye(size)-upper)**-1
    gram = mp.matrix(channels)
    for a in range(channels):
        for b in range(channels):
            gram[b, a] = row[a*channels+b]
    return gram, mp.det(mp.eye(size)-upper)


def path_data(level, channels, clock):
    endpoint = mp.eye(channels)
    output = mp.zeros(channels)
    select = mp.zeros(channels)
    select[channels-1, channels-1] = 1
    for color in range(level):
        endpoint = step(level, 2*channels, color, clock)*endpoint
        output += endpoint.H*select*endpoint
    return endpoint, output, select


def run(precision):
    mp.mp.dps = precision
    tol = mp.power(10, -precision//2)
    records = []
    maximum = mp.mpf(0)
    for level in range(2, 10):
        q = mp.exp(mp.pi*1j/level)
        Q = q*q
        crossing, _, _ = original_matrices(level)
        for channels in range(1, 5):
            bound = channels*4**(channels*(channels-1)//2+channels-1)
            for kind, clock in (
                ("physical", Q),
                ("unstable", mp.exp(mp.pi*1j/level)),
                ("mixed_test", mp.exp(1j*(mp.pi/3+mp.mpf("0.01"))/level))):
                gram, determinant = affine_matrix(level, channels, clock)
                endpoint, output, select = path_data(level, channels, clock)
                error = max(relative(gram, gram.H),
                            relative(gram-endpoint.H*gram*endpoint, output))
                shifted, _ = affine_matrix(level, channels, Q*clock)
                first = step(level, 2*channels, 0, clock)
                error = max(error, relative(gram, first.H*(shifted+select)*first))
                eigenvalues = mp.eighe((gram+gram.H)/2, eigvals_only=True)
                record = {"N": level, "channels": channels, "clock_kind": kind}
                if kind == "physical":
                    column = crossing**(2*channels)*mp.eye(level)[:, 0]
                    literal = mp.fsum(abs(column[j])**2 for j in range(level))
                    vector = data(level, 2*channels)[2]
                    extracted = 1+(vector.H*gram*vector)[0]
                    error = max(error, relative(endpoint, mp.zeros(channels)),
                                relative(gram, output), relative(extracted, literal))
                    if level >= 2*channels:
                        floor = (mp.mpf(16)**channels
                                 *mp.factorial(channels)**4
                                 /bound**2/level**(4*channels))
                        assert eigenvalues[0] >= floor-tol
                        record["proved_physical_floor"] = mp.nstr(floor, 20)
                    record["original_reflected_source"] = mp.nstr(literal, 20)
                else:
                    classical = transfer_clock(
                        2*channels, mp.mpf(1), clock**level)
                    modes = ([classical[0, 0]] if channels == 1 else
                             mp.eig(classical, left=False, right=False))
                    assert min(abs(abs(z)-1) for z in modes) > mp.mpf("1e-8")
                    stable = sum(abs(z) < 1 for z in modes)
                    positive = sum(z > 0 for z in eigenvalues)
                    negative = sum(z < 0 for z in eigenvalues)
                    assert (positive, negative) == (stable, channels-stable)
                    record["inertia"] = [positive, negative, 0]
                    if kind == "unstable":
                        assert eigenvalues[channels-1] <= -mp.mpf(1)/bound**2+tol
                    elif channels >= 2:
                        assert positive and negative
                        numerator_eigenvalues = mp.eighe(
                            mp.re(determinant)*(gram+gram.H)/2,
                            eigvals_only=True)
                        assert numerator_eigenvalues[0] < 0
                        assert numerator_eigenvalues[channels-1] > 0
                assert error < tol, (level, channels, kind, error)
                maximum = max(maximum, error)
                record["maximum_relative_error"] = mp.nstr(error, 20)
                records.append(record)
    return records, maximum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records, maximum = run(args.precision)
    result = {
        "status": "pass",
        "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Finite original-source/Stein normalization and inertia checks; "
                 "not an asymptotic or all-parameter proof.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {
            "experiments/"+name: hashlib.sha256(
                (Path(__file__).resolve().parent/name).read_bytes()).hexdigest()
            for name in (
                "check_twist_period_insertion.py",
                "check_two_run_monodromy_source_jets.py",
                "check_two_run_source_transfer.py",
                "check_internal_vertex_asymptotic.py",
            )
        },
        "maximum_relative_error": mp.nstr(maximum, 24),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(records),
                      "maximum_relative_error": result["maximum_relative_error"],
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
