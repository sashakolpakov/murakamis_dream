#!/usr/bin/env python3
"""Original-matrix normalization of full-period two-run source jets.

The derivatives are taken on the full ordered matrix product. The
reset/extraction formula is used only as the expected result. This is a
finite identity diagnostic, not an asymptotic or noncancellation test.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_two_run_source_transfer import polynomial_b, kron, run_states


def relative(left, right):
    return mp.norm(left-right)/max(mp.mpf(1), mp.norm(left), mp.norm(right))


def data(level, power):
    sign = 1 if power > 0 else -1
    channels = (abs(power)+1)//2
    q = mp.exp(sign*mp.pi*1j/level)
    vector = mp.matrix([q**(channels-1-i) for i in range(channels)])
    even = int(abs(power) % 2 == 0)
    scalar = q if even else -q**channels
    row = vector.T if even else mp.eye(channels)[0, :]
    selected = channels-1 if even else 0
    return channels, q, vector, even, scalar, row, selected


def transfer_clock(power, q, clock):
    channels = (abs(power)+1)//2
    even = abs(power) % 2 == 0
    out = polynomial_b(channels, q*clock, q)
    if even:
        return (1-1/clock)*out
    diagonal = [1-1/clock]*channels
    diagonal[0] = -1/clock
    return out*mp.diag(diagonal)


def step(level, power, color, z):
    _, q, _, _, _, _, _ = data(level, power)
    return transfer_clock(power, q, z*q**(2*color))


def single_monodromy(level, power, z):
    out = mp.eye((abs(power)+1)//2)
    for color in range(level):
        out = step(level, power, color, z)*out
    return out


def trace(matrix):
    return mp.fsum(matrix[j, j] for j in range(matrix.rows))


def classical_pair(a, b, xa, xb):
    return kron(transfer_clock(abs(a), mp.mpf(1), xa),
                transfer_clock(abs(b), mp.mpf(1), xb))


def factor(level, a, b, color, za, zb, weight):
    k = (abs(a)+1)//2
    ell = (abs(b)+1)//2
    dimension = k*ell+1
    top = kron(step(level, a, color, za), step(level, b, color, zb))
    out = mp.matrix(dimension)
    for i in range(dimension-1):
        for j in range(dimension-1):
            out[i, j] = top[i, j]
    for j in range(dimension-1):
        out[dimension-1, j] = weight*top[dimension-2, j]
    out[dimension-1, dimension-1] = 1
    return out


def monodromy(level, a, b, z, weights, zb=None):
    if zb is None:
        zb = z
    dimension = ((abs(a)+1)//2)*((abs(b)+1)//2)+1
    out = mp.eye(dimension)
    for color in range(level):
        out = factor(level, a, b, color, z, zb, weights[color])*out
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    pairs = [(-4, -5), (-5, -4), (-4, -4), (-3, -5),
             (4, 5), (5, 4), (2, 2), (3, 5),
             (-4, 5), (5, -4), (2, -2), (3, -5),
             (1, -1), (-1, -1)]
    records = []
    characteristic_records = []
    for level in range(2, 10):
        top = level-1
        kappa = mp.exp(mp.pi*1j*top*top/(2*level))
        crossing, _, _ = original_matrices(level)
        turn = mp.matrix(level)
        for j in range(level):
            turn[j, top-j] = 1
        first = mp.eye(level)[:, 0]
        powers = set(p for pair in pairs for p in pair)
        matrices = {p: crossing**p for p in powers}
        columns = {p: matrices[p]*first for p in powers}
        states = {p: run_states(level, p)[0] for p in powers}
        # Arbitrary clocks test the characteristic identity away from reset.
        clock = mp.mpc("0.7", "0.2")
        for power in list(range(-8, 0))+list(range(1, 9)):
            exact = single_monodromy(level, power, clock)
            classical = ((-1)**level
                         * transfer_clock(abs(power), mp.mpf(1), clock**level))
            error = mp.mpf(0)
            exact_power = mp.eye(exact.rows)
            classical_power = mp.eye(exact.rows)
            for exponent in range(1, exact.rows+1):
                exact_power *= exact
                classical_power *= classical
                error = max(error, relative(trace(exact_power),
                                            trace(classical_power)))
            parameter = mp.mpc("0.31", "0.19")
            error = max(error, relative(
                mp.det(mp.eye(exact.rows)-parameter*exact),
                mp.det(mp.eye(exact.rows)-parameter*classical)))
            assert error < tolerance, (level, power, "characteristic", error)
            characteristic_records.append({
                "N": level, "power": power, "trace_powers": exact.rows,
                "clock": ["0.7", "0.2"],
                "maximum_relative_error": mp.nstr(error, 20)})
        for a, b in pairs:
            k, qa, va, ea, ca, da, ia = data(level, a)
            ell, qb, vb, eb, cb, db, ib = data(level, b)
            order = ea+eb
            chi = ca*cb
            dim = k*ell+1
            selected = ia*ell+ib
            reset = mp.matrix(dim)
            reset[dim-1, dim-1] = 1
            row = mp.matrix(1, dim)
            paired_row = kron(da, db)
            for j in range(dim-1):
                row[j] = paired_row[j]
            for weighted in (False, True):
                weights = [1+mp.mpc(0, mp.mpf(j)/level) if weighted else 1
                           for j in range(level)]
                literal = mp.fsum(weights[j]*columns[a][j]*columns[b][j]
                                   for j in range(level))
                if not weighted:
                    word = (matrices[b]*turn*matrices[a]*first)[top]
                    assert relative(word, literal) < tolerance
                endpoint = kron(states[a][top], states[b][top])
                expected_vector = mp.matrix(dim, 1)
                for j in range(dim-1):
                    expected_vector[j] = endpoint[j]
                expected_vector[dim-1] = literal/kappa**(a+b)
                expected = mp.factorial(order)*chi*expected_vector*row
                function = lambda z: monodromy(level, a, b, z, weights)-reset
                derivative = mp.diff(function, mp.mpf(1), order)
                error = relative(derivative, expected)
                mixed_function = lambda za, zb: monodromy(
                    level, a, b, za, weights, zb)-reset
                mixed = mp.diff(mixed_function, (1, 1), (ea, eb))
                error = max(error, relative(mixed, expected/mp.factorial(order)))
                for lower in range(order):
                    error = max(error, mp.norm(mp.diff(function, 1, lower)))
                extracted = (kappa**(a+b)/(mp.factorial(order)*chi)
                             * derivative[dim-1, selected])
                error = max(error, relative(extracted, literal))
                if order:
                    # A nonphysical value tests the exact local shear identity.
                    z = 1+mp.mpc("0.0001", "0.0002")
                    full = monodromy(level, a, b, z, weights)
                    upper = full[:dim-1, :dim-1]
                    bottom = full[dim-1, :dim-1]
                    shear_row = bottom*(mp.eye(dim-1)-upper)**-1
                    shear = mp.eye(dim)
                    for j in range(dim-1):
                        shear[dim-1, j] = shear_row[j]
                    diagonal = mp.eye(dim)
                    for i in range(dim-1):
                        for j in range(dim-1):
                            diagonal[i, j] = upper[i, j]
                    error = max(error, relative(shear*full*shear**-1, diagonal))
                if not weighted:
                    za = 1+mp.mpc("0.001", "0.002")
                    zb = 1+mp.mpc("-0.002", "0.001")
                    full = monodromy(level, a, b, za, weights, zb)
                    shifted = monodromy(level, a, b, qa*qa*za, weights, qb*qb*zb)
                    first_factor = factor(level, a, b, 0, za, zb, 1)
                    error = max(error, relative(
                        shifted*first_factor, first_factor*full))
                    for power, clock in ((a, za), (b, zb)):
                        channels, qp, _, _, _, _, _ = data(level, power)
                        error = max(error, relative(
                            mp.det(step(level, power, 0, clock)),
                            (-qp)**channels*(1-clock)**(abs(power)-1)))
                    # The multiplied transport equation is checked at reset too.
                    at_reset = monodromy(level, a, b, 1, weights, 1)
                    shifted_reset = monodromy(level, a, b, qa*qa, weights, qb*qb)
                    reset_factor = factor(level, a, b, 0, 1, 1, 1)
                    error = max(error, relative(
                        shifted_reset*reset_factor, reset_factor*at_reset))
                    quantum_top = full[:dim-1, :dim-1]
                    pair_classical = classical_pair(a, b, za**level, zb**level)
                    top_power = mp.eye(dim-1)
                    classical_power = mp.eye(dim-1)
                    for exponent in range(1, dim):
                        top_power *= quantum_top
                        classical_power *= pair_classical
                        error = max(error, relative(
                            trace(top_power), trace(classical_power)))
                    classical_denominator = mp.det(mp.eye(dim-1)-pair_classical)
                    error = max(error, relative(
                        mp.det(mp.eye(dim-1)-quantum_top), classical_denominator))
                    if order == 0:
                        # Every odd--odd pair has the invariant eigenvalue one.
                        error = max(error, abs(classical_denominator))
                    if order:
                        upper = full[:dim-1, :dim-1]
                        upper_shifted = shifted[:dim-1, :dim-1]
                        h = full[dim-1, :dim-1]*(mp.eye(dim-1)-upper)**-1
                        h_shifted = (shifted[dim-1, :dim-1]
                                     *(mp.eye(dim-1)-upper_shifted)**-1)
                        a0 = first_factor[:dim-1, :dim-1]
                        error = max(error, relative(
                            h_shifted*a0,
                            h-first_factor[dim-1, :dim-1]))
                        # Natural signed leaf and the derivative-free original
                        # source numerator extraction are tested independently.
                        sigma_a = 1 if a > 0 else -1
                        sigma_b = 1 if b > 0 else -1
                        qq = mp.exp(2*mp.pi*1j/level)
                        natural = monodromy(
                            level, a, b, qq**sigma_a, weights, qq**sigma_b)
                        upper_natural = natural[:dim-1, :dim-1]
                        numerator_q = (natural[dim-1, :dim-1]
                            *(mp.eye(dim-1)-upper_natural)**-1)
                        # D_ab(Q^N)=D_ab(1)=1 exactly.
                        reset_vector = kron(va, vb)
                        extracted_value = kappa**(a+b)*(
                            1+(numerator_q*reset_vector)[0])
                        error = max(error, relative(extracted_value, literal),
                                    mp.norm(upper_natural))
                        x = mp.mpc("0.93", "0.04")
                        X = x**level
                        denominator = mp.det(mp.eye(dim-1)-classical_pair(
                            a, b, X**sigma_a, X**sigma_b))
                        natural_x = monodromy(
                            level, a, b, x**sigma_a, weights, x**sigma_b)
                        natural_qx = monodromy(
                            level, a, b, (qq*x)**sigma_a,
                            weights, (qq*x)**sigma_b)
                        numerator_x = (denominator*natural_x[dim-1, :dim-1]
                            *(mp.eye(dim-1)-natural_x[:dim-1, :dim-1])**-1)
                        numerator_qx = (denominator*natural_qx[dim-1, :dim-1]
                            *(mp.eye(dim-1)-natural_qx[:dim-1, :dim-1])**-1)
                        natural_factor = factor(
                            level, a, b, 0, x**sigma_a, x**sigma_b, 1)
                        error = max(error, relative(
                            numerator_qx*natural_factor[:dim-1, :dim-1],
                            numerator_x-denominator
                                *natural_factor[dim-1, :dim-1]))
                assert error < tolerance, (level, a, b, weighted, error)
                records.append({
                    "N": level, "powers": [a, b], "jet_order": order,
                    "dimension": dim, "complex_diagonal_weight": weighted,
                    "selected_channel_one_based": [ia+1, ib+1],
                    "maximum_relative_error": mp.nstr(error, 20),
                })
    return records, characteristic_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records, characteristic_records = run(args.precision)
    here = Path(__file__)
    dependencies = ["check_twist_period_insertion.py",
                    "check_two_run_source_transfer.py"]
    result = {
        "status": "pass",
        "precision_decimal_digits": args.precision,
        "scope": "Full ordered monodromy derivatives, original signed crossing "
                 "columns and literal J scalar, weighted diagonal spectators, "
                 "mixed reset jets, independent-clock cyclic intertwining, "
                 "marked affine transport, all signed run characteristic "
                 "identities, classical pair denominators and derivative-free "
                 "original source extraction; no asymptotic claim.",
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(here.with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "checks": records,
        "characteristic_checks": characteristic_records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "source_cases": len(records),
        "single_run_characteristic_cases": len(characteristic_records),
        "single_run_trace_powers": sum(r["trace_powers"]
                                       for r in characteristic_records),
        "jet_orders": sorted({r["jet_order"] for r in records}),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["maximum_relative_error"])
            for r in records+characteristic_records), 12),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
