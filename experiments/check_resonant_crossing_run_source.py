#!/usr/bin/env python3
"""Check complete original crossing powers from resonant fixed-channel systems."""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_current_free_aw_crossing_transport import newton_multiplication
from check_internal_two_crossing_chain import basis_jet
from check_rational_word_normalized_cofactor import adjugate


def relative(left, right):
    return mp.norm(left-right)/max(mp.mpf(1), mp.norm(left), mp.norm(right))


def channel_matrix(size, r, q, spectral):
    out = (r+r**-1)*mp.eye(size)
    out[0, 0] -= r
    out[size-1, size-1] -= spectral/q
    for j in range(size-1):
        out[j, j+1] = out[j+1, j] = -1
    return out


def transfer_column(level, power, column, q, kappa):
    size = (power+1)//2
    qq = q*q
    root = q*qq**column
    state = mp.matrix([root**(size-a-1) for a in range(size)])
    phase = (kappa*(-1)**column*q**(column*(column+1)))**power
    answer = mp.zeros(level, 1)
    answer[column] = phase
    for j in range(column+1, level):
        weight = 4*mp.sin(mp.pi*j/level)**2
        diagonal = ([weight]*size if power % 2 == 0
                    else [1-qq**(-j)]+[weight]*(size-1))
        state = (channel_matrix(size, q*qq**j, q, qq**(-column))**-1
                 *mp.diag(diagonal)*state)
        answer[j] = phase*state[size-1]
    return answer


def pole_free_source(level, power, q, kappa):
    size = (power+1)//2
    qq = q*q
    state = mp.matrix([q**(size-a-1) for a in range(size)])
    answer = mp.zeros(level, 1)
    answer[0] = kappa**power
    for j in range(1, level):
        r = q*qq**j
        cofactor = (mp.eye(1) if size == 1
                    else adjugate(channel_matrix(size, r, q, 1)))
        polynomial = r**size*cofactor
        if power % 2 == 0:
            step = (1-qq**(-j))*polynomial
        else:
            step = polynomial*mp.diag(
                [-qq**(-j)]+[1-qq**(-j)]*(size-1))
        state = step*state
        answer[j] = kappa**power*state[size-1]
    return answer


def projected_source(level, power, q, kappa, z):
    m = power//2
    identity = mp.eye(level)
    x = mp.diag([q**(2*j) for j in range(level)])
    shift = mp.zeros(level)
    for j in range(level):
        shift[(j+1) % level, j] = 1
    k = -q**-1*x**-1+(identity-x**-1)*shift
    cheb = {-2: -identity, -1: mp.zeros(level), 0: identity}
    for j in range(1, m+1):
        cheb[j] = z*cheb[j-1]-cheb[j-2]
    if power % 2 == 0:
        numerator = q**m*(cheb[m]-q*cheb[m-1]*x)
        denominator = q**(m-1)*(cheb[m-1]-q*cheb[m-2]*x)
    else:
        numerator = q**m*(cheb[m]*k+cheb[m-1])
        denominator = q**(m-1)*(cheb[m-1]*k+cheb[m-2])
    e0 = mp.matrix([1]+[0]*(level-1))
    return (kappa**power/(level*((-1)**(level-1))**m)
            *denominator*adjugate(numerator-denominator)*e0)


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    for level in range(2, 11):
        q = mp.exp(mp.pi*1j/level)
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        crossing, _, _ = original_matrices(level)
        z = newton_multiplication(level)
        for power in range(1, 9):
            reconstructed = mp.zeros(level)
            for column in range(level):
                value = transfer_column(level, power, column, q, kappa)
                for j in range(level):
                    reconstructed[j, column] = value[j]
            maximum = relative(pole_free_source(level, power, q, kappa),
                               reconstructed[:, 0])
            projectors = 0
            if level <= 6 and power <= 4:
                maximum = max(maximum, relative(
                    projected_source(level, power, q, kappa, z),
                    reconstructed[:, 0]))
                projectors = 1
            jets = 0
            for sign in (1, -1):
                predicted = reconstructed if sign == 1 else reconstructed.conjugate()
                literal = crossing**(sign*power)
                maximum = max(maximum, relative(predicted, literal))
                for left, right in [
                        (mp.mpf(-2), z[0, 0]),
                        (mp.mpc(".37", ".12"), mp.mpc("-1.1", ".23"))]:
                    left_jets = basis_jet(level, left)
                    right_jets = basis_jet(level, right)
                    for vl in left_jets:
                        for vr in right_jets:
                            maximum = max(maximum, relative(
                                (vl.T*predicted*vr)[0],
                                (vl.T*literal*vr)[0]))
                            jets += 1
            assert maximum < tolerance, (level, power, maximum)
            rows.append({
                "N": level, "absolute_power": power,
                "signed_full_matrix_entries": 2*level*level,
                "polarized_value_and_normal_cases": jets,
                "independent_adjugate_source_cases": projectors,
                "maximum_relative_error": mp.nstr(maximum, 18),
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = run(args.precision)
    dependencies = [
        "check_twist_period_insertion.py",
        "check_current_free_aw_crossing_transport.py",
        "check_internal_two_crossing_chain.py",
        "check_rational_word_normalized_cofactor.py",
    ]
    result = {
        "status": "pass",
        "scope": "All entries of original signed crossing powers, exact "
                 "resonant source and pole-free transfer, free-boundary "
                 "values and mixed normals; no large-level asymptotic.",
        "precision_decimal_digits": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in dependencies
        },
        "checks": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "level_power_pairs": len(rows),
        "signed_full_matrix_entries": sum(r["signed_full_matrix_entries"] for r in rows),
        "polarized_value_and_normal_cases": sum(
            r["polarized_value_and_normal_cases"] for r in rows),
        "independent_adjugate_source_cases": sum(
            r["independent_adjugate_source_cases"] for r in rows),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["maximum_relative_error"]) for r in rows), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
