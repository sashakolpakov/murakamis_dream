#!/usr/bin/env python3
"""Check the finite-channel two-run source against original matrices.

Every physical color contribution is compared before the final sum.
This is a normalization diagnostic, not an asymptotic certificate.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def relative(a, b):
    return mp.norm(a-b)/max(mp.mpf(1), mp.norm(a), mp.norm(b))


def polynomial_b(channels, r, q):
    out = mp.matrix(channels)
    for i in range(channels):
        for j in range(channels):
            high = channels-1-max(i, j)
            out[i, j] = r**(abs(i-j)+1)*(
                mp.fsum(r**(2*k) for k in range(high+1))
                - r/q*mp.fsum(r**(2*k) for k in range(high)))
    return out


def run_states(level, power):
    sign = 1 if power > 0 else -1
    channels = (abs(power)+1)//2
    q = mp.exp(sign*mp.pi*1j/level)
    qq = q*q
    state = mp.matrix([q**(channels-1-i) for i in range(channels)])
    states = [state.copy()]
    transfers = []
    for color in range(1, level):
        z = qq**color
        transfer = polynomial_b(channels, q*z, q)
        if power % 2 == 0:
            transfer *= 1-1/z
        else:
            diagonal = [1-1/z]*channels
            diagonal[0] = -1/z
            transfer = transfer*mp.diag(diagonal)
        state = transfer*state
        transfers.append(transfer)
        states.append(state.copy())
    return states, transfers


def kron(a, b):
    out = mp.matrix(a.rows*b.rows, a.cols*b.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            for k in range(b.rows):
                for ell in range(b.cols):
                    out[i*b.rows+k, j*b.cols+ell] = a[i, j]*b[k, ell]
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    powers = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    pairs = [(-4, -5), (-5, -4), (-3, -3), (-2, -3),
             (-1, -1), (1, 1), (2, 2), (3, 5),
             (2, -2), (4, -4), (1, -1), (-3, 4)]
    records = []
    for level in range(2, 13):
        top = level-1
        q = mp.exp(mp.pi*1j/level)
        kappa = q**(mp.mpf(top*top)/2)
        crossing, _, _ = original_matrices(level)
        turn = mp.matrix(level)
        for j in range(level):
            turn[j, top-j] = 1
        first = mp.eye(level)[:, 0]
        matrices = {p: crossing**p for p in powers}
        columns = {p: matrices[p]*first for p in powers}
        states = {}
        transfers = {}
        run_error = mp.mpf(0)
        for power in powers:
            states[power], transfers[power] = run_states(level, power)
            recovered = mp.matrix([
                kappa**power*state[state.rows-1] for state in states[power]])
            run_error = max(run_error, relative(recovered, columns[power]))
        assert run_error < tolerance, (level, "run columns", run_error)

        for a, b in pairs:
            state = kron(states[a][0], states[b][0])
            accumulator = mp.mpc(1)
            weighted_accumulator = mp.mpc(1)
            color_error = mp.mpf(0)
            for color in range(level):
                if color:
                    step = kron(transfers[a][color-1], transfers[b][color-1])
                    state = step*state
                    accumulator += state[state.rows-1]
                    weight = 1+1j*mp.mpf(color)/level
                    weighted_accumulator += weight*state[state.rows-1]
                reconstructed = kappa**(a+b)*state[state.rows-1]
                literal = columns[a][color]*columns[b][color]
                color_error = max(color_error, relative(reconstructed, literal))
            literal_word = (matrices[b]*turn*matrices[a]*first)[top]
            transfer_value = kappa**(a+b)*accumulator
            weighted_literal = mp.fsum(
                (1+1j*mp.mpf(j)/level)*columns[a][j]*columns[b][j]
                for j in range(level))
            maximum = max(run_error, color_error,
                          relative(literal_word, transfer_value),
                          relative(weighted_literal,
                                   kappa**(a+b)*weighted_accumulator))
            if b == -a:
                maximum = max(maximum, relative(
                    literal_word, mp.fsum(abs(z)**2 for z in columns[a])))
            assert maximum < tolerance, (level, a, b, maximum)
            records.append({
                "N": level, "powers": [a, b],
                "transfer_dimension": ((abs(a)+1)//2)*((abs(b)+1)//2)+1,
                "colors_checked": level,
                "maximum_relative_error": mp.nstr(maximum, 20),
                "source_modulus": mp.nstr(abs(literal_word), 20),
            })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=130)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = run(args.precision)
    dependency = Path(__file__).with_name("check_twist_period_insertion.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Original full crossing columns, every retained paired color, "
                 "literal J contraction and signed two-run scalar; no "
                 "asymptotic coefficient or geometric rate is tested.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "checks": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "source_cases": len(records),
        "paired_colors": sum(row["colors_checked"] for row in records),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(row["maximum_relative_error"]) for row in records), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
