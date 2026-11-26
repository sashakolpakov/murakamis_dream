#!/usr/bin/env python3
"""Check the local arbitrary-word source and its finite endpoint identities.

The local system is propagated on every free input column through literal
turns. Comparisons use original crossing matrices, not an annihilator.
No asymptotic estimate is tested.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def error(a, b):
    if not isinstance(a, mp.matrix):
        return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))
    return max(
        error(a[i, j], b[i, j])
        for i in range(a.rows) for j in range(a.cols))


def local_run(level, power, inputs):
    sign = 1 if power > 0 else -1
    channels = (abs(power)+1)//2
    q = mp.exp(mp.pi*1j/level)
    qs = q**sign
    qqs = qs*qs
    kappa = q**(mp.mpf((level-1)**2)/2)
    output = mp.zeros(level, inputs.cols)
    for ell in range(level):
        rell = qs*qqs**ell
        vector = mp.matrix([rell**(channels-1-a)
                            for a in range(channels)])
        diagonal_unit = kappa*(-1)**ell*q**(ell*(ell+1))
        state = diagonal_unit**power*vector*inputs[ell, :]
        for j in range(ell, level):
            if j > ell:
                r = qs*qqs**j
                h = (r+1/r)*mp.eye(channels)
                h[0, 0] -= r
                h[channels-1, channels-1] -= qs**-1*qqs**-ell
                for a in range(channels-1):
                    h[a, a+1] = h[a+1, a] = -1
                w = (1-qqs**j)*(1-qqs**-j)
                weights = [w]*channels
                if power % 2:
                    weights[0] = 1-qqs**-j
                state = h**-1*mp.diag(weights)*state
            output[j, :] += state[channels-1, :]
    return output


def finite_identities(level, crossing, turn):
    q = mp.exp(mp.pi*1j/level)
    qq = q*q
    top = level-1
    kappa = q**(mp.mpf(top*top)/2)
    factorial = [mp.mpc(1)]
    for j in range(1, level):
        factorial.append(factorial[-1]*(1-qq**j))
    gauge = mp.diag(factorial)
    t = mp.zeros(level)
    delta = mp.zeros(level)
    pin = mp.zeros(level)
    pin[top, top] = 1
    for j in range(top):
        t[j+1, j] = 1
        delta[j, j+1] = 1-qq**(j+1)
    identity = mp.eye(level)
    dilation = mp.diag([qq**j for j in range(level)])
    gamma = mp.diag([(-1)**j*q**(j*(j+1)) for j in range(level)])
    exponential = mp.zeros(level)
    for j in range(level):
        exponential += (-q)**j/factorial[j]*t**j
    reflected = gauge**-1*turn*gauge
    epsilon = mp.mpf((-1)**level)
    source = kappa*exponential[:, 0]
    expected_source = mp.zeros(level, 1)
    expected_source[top] = kappa*epsilon/level
    errors = [
        error(gauge**-1*crossing*gauge, kappa*exponential*gamma),
        error(delta*exponential,
              (identity+q*t)*exponential*delta-q*exponential
              +epsilon/level*t**top),
        error(exponential*delta*exponential**-1,
              (identity+q*t)**-1
              *(delta+q*identity-epsilon/level*t**top)),
        error(reflected*dilation*reflected, qq**-1*dilation**-1),
        error(reflected*t*reflected,
              -delta*dilation**-1*(identity-dilation)),
        error(reflected*delta*reflected,
              t*(identity-qq*dilation+pin)**-1),
        error((delta+q*identity)*source, expected_source),
    ]
    size = level//2
    minor = mp.matrix([[crossing[size+i, j] for j in range(size)]
                       for i in range(size)])
    expected = kappa**size
    for i in range(size):
        expected *= (-q)**(size+i)
    for j in range(size):
        expected *= q**(j*j)*(-1)**j*qq**(-j*(j-1)//2)/factorial[j]
    for i in range(size):
        for h in range(i+1, size):
            expected *= qq**(size+h)-qq**(size+i)
    determinant_error = abs(mp.det(minor)/expected-1)
    errors.append(determinant_error)
    return max(errors), size


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    words = [
        ([1], 0, 0), ([-1], 0, 1), ([2, -3], 1, 0),
        ([-4, -5], 0, 0), ([2, -3, 4], 0, 0),
        ([-3, 2, -1, 4], 1, 1), ([1, -2, 1, 3, -2], 0, 1),
        ([1, 1, 1], 1, 0),
    ]
    records = []
    finite_records = []
    for level in range(2, 11):
        crossing, _, _ = original_matrices(level)
        turn = mp.zeros(level)
        for j in range(level):
            turn[j, level-1-j] = 1
        finite_error, rank = finite_identities(level, crossing, turn)
        assert finite_error < tolerance, (level, "finite identities", finite_error)
        finite_records.append({
            "N": level, "middle_cut_rank": rank,
            "maximum_relative_error": mp.nstr(finite_error, 22)})
        powers = {p: crossing**p for word, _, _ in words for p in word}
        for word, right_turn, left_turn in words:
            local = turn.copy() if right_turn else mp.eye(level)
            literal = local.copy()
            for index, power in enumerate(word):
                if index:
                    local = turn*local
                    literal = turn*literal
                local = local_run(level, power, local)
                literal = powers[power]*literal
            if left_turn:
                local = turn*local
                literal = turn*literal
            maximum = error(local, literal)
            assert maximum < tolerance, (level, word, maximum)
            records.append({
                "N": level, "powers_input_to_output": word,
                "right_turn": right_turn, "left_turn": left_turn,
                "free_input_columns": level,
                "coefficient_entries": level*level,
                "maximum_relative_error": mp.nstr(maximum, 22),
                "original_closing_modulus": mp.nstr(abs(literal[level-1, 0]), 22),
            })
    return records, finite_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records, finite = run(args.precision)
    here = Path(__file__)
    dependency = here.with_name("check_twist_period_insertion.py")
    result = {
        "status": "pass",
        "precision_decimal_digits": args.precision,
        "scope": "Full free-input coefficient matrices through up to four "
                 "internal turns; exact finite q-exponential endpoint current, "
                 "pinned turn derivative and nonzero middle-cut Vandermonde. "
                 "No asymptotic claim.",
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "word_checks": records,
        "finite_identity_checks": finite,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    maximum = max(mp.mpf(row["maximum_relative_error"])
                  for row in records+finite)
    print(json.dumps({
        "status": "pass", "word_cases": len(records),
        "coefficient_entries": sum(row["coefficient_entries"] for row in records),
        "finite_identity_levels": len(finite),
        "maximum_relative_error": mp.nstr(maximum, 14),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
