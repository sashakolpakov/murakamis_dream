#!/usr/bin/env python3
"""Finite original-source checks for the odd backward selected line.

Checks full matrix coefficients, the cyclic identity, the shifted
characteristic polynomial, the marked projector and the original crossing
column. Numerical simplicity samples do not replace the written sector proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_even_run_simple_spectrum_and_marked_kernel import (
    characteristic, eigenvalues, path, poly_multiply, poly_value, relative,
)


def robin(m, s):
    out = path(m)
    out[0, 0] += s
    return out


def shifted_classical(k, z):
    if k == 1:
        return mp.matrix([[2]])
    out = path(k)
    out[0, 0] += z+1
    out[k-1, k-1] += 1
    out[0, 1] -= z
    return out


def channel(k, q, r):
    out = (r+1/r)*mp.eye(k)-path(k)
    out[0, 0] -= r
    out[k-1, k-1] -= 1/q
    return out


def adjugate(matrix):
    k = matrix.rows
    if k == 1:
        return mp.matrix([[1]])
    out = mp.zeros(k)
    for i in range(k):
        for j in range(k):
            minor = mp.matrix([[matrix[a, b] for b in range(k) if b != i]
                               for a in range(k) if a != j])
            out[i, j] = (-1)**(i+j)*mp.det(minor)
    return out


def odd_transfer(k, q, z):
    if not z:
        return -q*mp.eye(k)
    r = q*z
    out = mp.zeros(k)
    for a in range(k):
        for b in range(k):
            top = k-1-max(a, b)
            out[a, b] = r**(abs(a-b)+1)*(
                mp.fsum(r**(2*h) for h in range(top+1))
                -z*mp.fsum(r**(2*h) for h in range(top)))
    return out*mp.diag([-1/z]+[1-1/z]*(k-1))


def averaged_polynomial_orbit(level, k, q, epsilon, coefficients, u0, base):
    """Evaluate d(x^N) times the actual Reynolds sum, before taking a gcd."""
    Q = q*q
    c = -q
    clocks = [base*Q**j for j in range(level)]
    transfers = [odd_transfer(k, q, x) for x in clocks]
    seeds = []
    for x in clocks:
        cardinal = mp.fsum((x/Q)**h for h in range(level))/level
        matrix = 2*mp.eye(k)+epsilon*poly_value(coefficients, x)
        seeds.append(cardinal*adjugate(matrix)*u0)
    values = []
    for j in range(level):
        prefix = mp.eye(k)
        total = seeds[j].copy()
        for r in range(1, level):
            prefix = prefix*transfers[(j-r) % level]
            total += c**(-r)*prefix*seeds[(j-r) % level]
        values.append(total)
    return transfers, values


def classical_checks(tol):
    records = []
    for m in range(1, 6):
        for s in (mp.mpc(0), mp.mpc(1), mp.mpc(-1), mp.mpc(0, 1),
                  mp.mpc(0, -1), mp.mpc(".3", ".4"),
                  mp.mpc("-.7", ".6"), mp.exp(mp.mpc(0, ".37"))):
            values = eigenvalues(robin(m, s))
            separation = min((abs(a-b) for j, a in enumerate(values)
                              for b in values[j+1:]), default=mp.inf)
            assert separation > tol
            sectors = []
            error = mp.mpf(0)
            if mp.im(s) > 0:
                for value in values:
                    radical = mp.sqrt(value*value-4)
                    z = min(((value+radical)/2, (value-radical)/2), key=abs)
                    angle = -mp.arg(z)
                    matching = [j for j in range(1, m+1)
                                if (2*j-1)*mp.pi/(2*m+1) < angle
                                < 2*j*mp.pi/(2*m+1)]
                    assert len(matching) == 1
                    sectors.append(matching[0])
                    error = max(error, relative(
                        (1-z**(2*m+2))/(z*(1-z**(2*m))), s))
                assert sorted(sectors) == list(range(1, m+1))
            assert error < tol
            records.append({"quotient_rank": m, "parameter": str(s),
                            "sector_labels": sorted(sectors),
                            "maximum_relative_error": mp.nstr(error, 24)})
    return records


def quantum_checks(tol):
    records = []
    for level in range(2, 10):
        crossing, _, _ = original_matrices(level)
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        epsilon = (-1)**level
        for k in range(1, 7):
            for sign in (-1, 1):
                q = mp.exp(sign*mp.pi*1j/level)
                Q = q*q
                identity = mp.eye(k)
                first, last = mp.zeros(k), mp.zeros(k)
                first[0, 0] = last[k-1, k-1] = 1
                basic = [identity, -q*path(k)-last,
                         q*q*(identity-first)]
                odd = poly_multiply([identity, -first], basic)
                error = mp.norm(odd[3])
                odd = odd[:3]
                full = [identity]
                for j in range(level):
                    full = poly_multiply(
                        full, [coefficient*Q**(j*h)
                               for h, coefficient in enumerate(odd)])
                error = max(error, relative(full[0], identity),
                            max(mp.norm(full[h]) for h in range(1, level)))
                shifted = [coefficient*Q**h for h, coefficient in enumerate(full)]
                lhs = poly_multiply(odd, shifted)
                rhs = poly_multiply(full, odd)
                error = max(error, max(relative(a, b) for a, b in zip(lhs, rhs)))
                g_coefficients = [epsilon*full[level+h] for h in range(level+1)]
                g_coefficients[level] -= epsilon*identity
                projector_at_one = None
                for x in (mp.mpc(0), mp.mpc(".37", ".19"),
                          mp.exp(mp.mpc(0, ".41")), mp.mpc(1)):
                    g = poly_value(g_coefficients, x)
                    classical = shifted_classical(k, x**level)
                    error = max(error, max(relative(a, b) for a, b in zip(
                        characteristic(g), characteristic(-epsilon*classical))))
                    projector = adjugate(2*identity+epsilon*g)/(k-(k-1)*x**level)
                    error = max(error, relative(projector*projector, projector),
                                relative(g*projector, -2*epsilon*projector),
                                relative(mp.fsum(projector[a, a] for a in range(k)), 1))
                    if x:
                        factors = [(identity-Q**j*x*first)
                                   *channel(k, q, q*Q**j*x) for j in range(level)]
                        backward = identity.copy()
                        for factor in factors:
                            backward = backward*factor
                        error = max(error, relative(
                            backward-epsilon*(x**level+x**(-level))*identity, g))
                        next_g = poly_value(g_coefficients, Q*x)
                        next_projector = adjugate(2*identity+epsilon*next_g)/(
                            k-(k-1)*x**level)
                        error = max(error, relative(
                            projector*factors[0], factors[0]*next_projector))
                    if x == 1:
                        projector_at_one = projector
                u0 = mp.matrix([q**(k-1-a) for a in range(k)])
                state = u0.copy()
                states = [state.copy()]
                for j in range(1, level):
                    z = Q**j
                    edge = mp.diag([1-1/z]+[(1-z)*(1-1/z)]*(k-1))
                    state = channel(k, q, q*z)**-1*edge*state
                    states.append(state.copy())
                endpoint = states[-1]
                pin = epsilon*q**k*endpoint*mp.eye(k)[0, :]
                error = max(error, relative(endpoint[0], epsilon*q**(-k)),
                            relative(projector_at_one, pin))
                power = sign*(2*k-1)
                literal = crossing**power*mp.eye(level)[:, 0]
                for j in range(level):
                    error = max(error, relative(
                        literal[j], kappa**power*states[j][k-1]))
                reynolds_checked = k <= 3 and level <= 7
                if reynolds_checked:
                    for base in (mp.mpc(1), mp.mpc(".43", ".17")):
                        transfers, values = averaged_polynomial_orbit(
                            level, k, q, epsilon, g_coefficients, u0, base)
                        for j in range(level):
                            error = max(error, relative(
                                transfers[j]*values[j],
                                -q*values[(j+1) % level]))
                        if base == 1:
                            error = max(error, relative(values[1], u0))
                            for j in range(level):
                                error = max(error, relative(
                                    states[j], (-q)**j*values[(j+1) % level]))
                assert error < tol, (level, k, sign, error)
                records.append({"N": level, "channels": k, "power": power,
                                "projector_clocks": 4, "original_source_colors": level,
                                "reynolds_orbits_checked": 2 if reynolds_checked else 0,
                                "maximum_relative_error": mp.nstr(error, 24)})
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    tol = mp.power(10, -args.precision//2)
    classical = classical_checks(tol)
    quantum = quantum_checks(tol)
    maximum = max(mp.mpf(r["maximum_relative_error"]) for r in classical+quantum)
    dependencies = (
        "check_even_run_simple_spectrum_and_marked_kernel.py",
        "check_twist_period_insertion.py", "check_internal_vertex_asymptotic.py",
    )
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Finite original-source, polynomial and projector normalization; "
                 "not an all-parameter or asymptotic proof.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {
            "experiments/"+name: hashlib.sha256(
                (Path(__file__).resolve().parent/name).read_bytes()).hexdigest()
            for name in dependencies
        },
        "maximum_relative_error": mp.nstr(maximum, 24),
        "classical_records": classical, "quantum_records": quantum,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "classical_cases": len(classical),
                      "signed_quantum_cases": len(quantum),
                      "maximum_relative_error": result["maximum_relative_error"],
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
