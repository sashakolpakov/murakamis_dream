#!/usr/bin/env python3
"""Check original even-run inputs, forced Green identities and clock norms.

Small levels use full original matrices and all input columns.  The separate
large-level checks exercise only the short exact channel system at the proved
contraction threshold; they are not source asymptotic tests.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def relative_error(a, b):
    if isinstance(a, mp.matrix):
        return max(relative_error(a[i, j], b[i, j])
                   for i in range(a.rows) for j in range(a.cols))
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def norm_squared(a):
    return mp.fsum(abs(a[i, j])**2
                   for i in range(a.rows) for j in range(a.cols))


def channel(level, power, color, input_color):
    k = abs(power)//2
    sign = 1 if power > 0 else -1
    q = mp.exp(sign*mp.pi*1j/level)
    qq = q*q
    r = q*qq**color
    h = (r+1/r)*mp.eye(k)
    h[0, 0] -= r
    h[k-1, k-1] -= q**-1*qq**-input_color
    for a in range(k-1):
        h[a, a+1] = h[a+1, a] = -1
    return h


def input_vector(level, power, color, value):
    k = abs(power)//2
    sign = 1 if power > 0 else -1
    q = mp.exp(mp.pi*1j/level)
    qs = q**sign
    r = qs**(2*color+1)
    kappa = q**(mp.mpf((level-1)**2)/2)
    mu = kappa*(-1)**color*q**(color*(color+1))
    return mu**power*mp.matrix([r**(k-1-a)*value for a in range(k)])


def fields(level, power, colors, values, last):
    k = abs(power)//2
    first = min(colors)
    out = {j: mp.zeros(k, len(colors)) for j in range(first, last+1)}
    for column, ell in enumerate(colors):
        state = input_vector(level, power, ell, values[column])
        for j in range(ell, last+1):
            if j > ell:
                d = 4*mp.sin(mp.pi*j/level)**2
                state = mp.lu_solve(channel(level, power, j, ell), d*state)
            out[j][:, column] = state
    return out


def backward(level, power, colors, j, field):
    d = 4*mp.sin(mp.pi*j/level)**2
    out = mp.zeros(field.rows, field.cols)
    for column, ell in enumerate(colors):
        out[:, column] = channel(level, power, j, ell)*field[:, column]/d
    return out


def injection(level, power, colors, values, j):
    out = mp.zeros(abs(power)//2, len(colors))
    if j in colors:
        column = colors.index(j)
        out[:, column] = input_vector(level, power, j, values[column])
    return out


def green_errors(level, power, colors, values, data):
    first, last = min(data), max(data)
    errors = []
    for j in range(first, last+1):
        inj = injection(level, power, colors, values, j)
        if j:
            errors.append(relative_error(
                backward(level, power, colors, j, inj), 0*inj))
        errors.append(relative_error(
            norm_squared(inj),
            (abs(power)//2)*abs(values[colors.index(j)])**2
            if j in colors else 0))
        if j == first:
            continue
        previous_inj = injection(level, power, colors, values, j-1)
        errors.append(relative_error(
            backward(level, power, colors, j, data[j]), data[j-1]))
        errors.append(relative_error(
            backward(level, power, colors, j, data[j]-inj)-previous_inj,
            data[j-1]-previous_inj))
    left = first+(last-first)//3
    propagated = data[last]-injection(
        level, power, colors, values, last)
    for j in range(last, left, -1):
        propagated = backward(level, power, colors, j, propagated)
    errors.append(relative_error(propagated, data[left]))
    return max(errors)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    original_records = []
    threshold_records = []
    for level in list(range(4, 13))+[16, 17]:
        crossing, _, _ = original_matrices(level)
        turn = mp.zeros(level)
        for j in range(level):
            turn[j, level-1-j] = 1
        q = mp.exp(mp.pi*1j/level)
        colors = list(range(level))
        for power in (4, -4, 6, -6):
            k = abs(power)//2
            matrix = crossing**power
            all_fields = fields(level, power, colors, [1]*level, level-1)
            observed = mp.matrix([
                [all_fields[j][k-1, ell] for ell in colors]
                for j in colors])
            maximum = relative_error(observed, matrix)
            for ell in (0, level//2, level-1):
                observation = mp.zeros(k)
                product = mp.eye(k)
                observation[0, :] = product[k-1, :]
                for h in range(1, k):
                    product = channel(
                        level, power, level-h, ell)*product
                    observation[h, :] = product[k-1, :]
                maximum = max(maximum,
                              relative_error(mp.det(observation), 1))
            generic = mp.matrix([
                mp.mpc(1+(j % 3)/mp.mpf(7), (-1)**j/mp.mpf(5))
                for j in colors])
            endpoint = mp.zeros(level, 1)
            endpoint[level-1] = 1
            middle = mp.zeros(level, 1)
            middle[level//2] = 1
            forced_middle = mp.lu_solve(matrix, middle)
            for vector in (generic, endpoint, forced_middle):
                weighted_fields = {
                    j: all_fields[j]*mp.diag(vector) for j in colors}
                maximum = max(maximum, green_errors(
                    level, power, colors, list(vector), weighted_fields))
                weights = [mp.fsum(abs(matrix[j, ell])**2 for j in colors)
                           for ell in colors]
                averaged = mp.mpf(0)
                for clock in colors:
                    phase = mp.diag([q**(2*clock*ell) for ell in colors])
                    averaged += norm_squared(matrix*phase*vector)/level
                diagonal = mp.fsum(weights[ell]*abs(vector[ell])**2
                                   for ell in colors)
                reflected = mp.fsum(
                    weights[level-1-ell]*abs(vector[ell])**2 for ell in colors)
                actual_reflected = mp.fsum(
                    weights[ell]*abs((turn*vector)[ell])**2 for ell in colors)
                maximum = max(maximum, relative_error(averaged, diagonal),
                              relative_error(reflected, actual_reflected))
            maximum = max(maximum, relative_error(matrix*forced_middle, middle))
            assert maximum < tolerance, (level, power, maximum)
            original_records.append({
                "N": level, "power": power,
                "original_matrix_entries": level*level,
                "arbitrary_input_cases": 3,
                "maximum_relative_error": mp.nstr(maximum, 24),
                "last_column_weight": mp.nstr(weights[-1], 24),
                "first_column_weight": mp.nstr(weights[0], 24),
            })
    for k in (2, 3):
        for sign in (-1, 1):
            power = sign*2*k
            for level in (2048*k*k, 2048*k*k+1):
                left = (level+3)//4-1
                last = left+6
                colors = list(range(left, last+1))
                values = [mp.mpc(1+j/mp.mpf(11), (-1)**j/mp.mpf(7))
                          for j in range(len(colors))]
                data = fields(level, power, colors, values, last)
                maximum = green_errors(
                    level, power, colors, values, data)
                r = 1-1/mp.mpf(64*k*k)
                beta = 1+mp.pi/level
                margins = []
                for j in range(left+2, last+1, 2):
                    lower = (norm_squared(data[j-2])/r**2
                             +k*abs(values[j-left])**2
                             +k/beta**2*abs(values[j-left-1])**2)
                    energy = norm_squared(data[j])
                    margin = (energy-lower)/max(1, energy)
                    assert margin >= -tolerance, (level, power, j, margin)
                    margins.append(margin)
                left_strict = data[last]-injection(
                    level, power, colors, values, last)
                upper = 4*r**6*norm_squared(left_strict)
                assert norm_squared(data[left]) <= upper*(1+tolerance)
                accumulated = norm_squared(data[left])/r**6
                for nu in range(1, 4):
                    accumulated += k/r**(2*(3-nu))*(
                        abs(values[2*nu])**2
                        +abs(values[2*nu-1])**2/beta**2)
                assert norm_squared(data[last]) >= accumulated*(1-tolerance)
                assert maximum < tolerance, (level, power, maximum)
                threshold_records.append({
                    "N": level, "power": power,
                    "input_colors": colors,
                    "maximum_relative_error": mp.nstr(maximum, 24),
                    "pair_energy_relative_margins":
                        [mp.nstr(x, 24) for x in margins],
                })
    return original_records, threshold_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    original, threshold = run(args.precision)
    script = Path(__file__)
    dependency = script.with_name("check_twist_period_insertion.py")
    report = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Original full-input matrices, exact forced Green/reset "
                 "identities and clock averages; separate short-channel "
                 "energy checks at the proved middle-contraction threshold. "
                 "No asymptotic estimate is inferred from finite checks.",
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "original_matrix_checks": original,
        "threshold_energy_checks": threshold,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    maximum = max(mp.mpf(row["maximum_relative_error"])
                  for row in original+threshold)
    print(json.dumps({
        "status": "pass", "original_matrix_cases": len(original),
        "original_matrix_entries": sum(
            row["original_matrix_entries"] for row in original),
        "threshold_energy_cases": len(threshold),
        "maximum_relative_error": mp.nstr(maximum, 16),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
