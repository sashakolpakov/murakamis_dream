#!/usr/bin/env python3
"""Finite diagnostics for the simple even-run curve and marked quantum kernel.

Checks polynomial coefficients and cyclic identities directly, including k>N;
compares full source columns with original crossing matrices; and checks the
classical sector labels and all quantum projectors at complex clocks.  These
are finite normalization diagnostics, not proofs of global simplicity or
asymptotic growth.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def relative(a, b):
    if isinstance(a, mp.matrix):
        return mp.norm(a-b)/max(mp.mpf(1), mp.norm(a), mp.norm(b))
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def path(k):
    out = mp.zeros(k)
    for j in range(k-1):
        out[j, j+1] = out[j+1, j] = 1
    return out


def jacobi(k, s):
    out = path(k)
    out[0, 0] += s
    out[k-1, k-1] += 1
    return out


def channel(k, q, r):
    out = (r+1/r)*mp.eye(k)-path(k)
    out[0, 0] -= r
    out[k-1, k-1] -= 1/q
    return out


def p_values(k, x):
    result = [mp.mpc(1)]
    if k:
        result.append(x-1)
    for n in range(2, k+1):
        result.append(x*result[-1]-result[-2])
    return result


def poly_multiply(a, b):
    k = a[0].rows
    out = [mp.zeros(k) for _ in range(len(a)+len(b)-1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out


def poly_value(coefficients, x):
    out = mp.zeros(coefficients[0].rows)
    for coefficient in reversed(coefficients):
        out = x*out+coefficient
    return out


def characteristic(matrix):
    """Newton identities from independently computed matrix powers."""
    k = matrix.rows
    powers = []
    power = mp.eye(k)
    for j in range(1, k+1):
        power = power*matrix
        powers.append(mp.fsum(power[a, a] for a in range(k)))
    coefficients = [mp.mpc(1)]
    for j in range(1, k+1):
        coefficients.append(-mp.fsum(
            coefficients[j-i]*powers[i-1] for i in range(1, j+1))/j)
    return coefficients


def eigenvalues(matrix):
    # mpmath's one-dimensional eig path returns a tuple despite both flags.
    if matrix.rows == 1:
        return [matrix[0, 0]]
    return mp.eig(matrix, left=False, right=False)


def projectors(g, eigenvalues, epsilon):
    k = g.rows
    out = []
    for j, mu in enumerate(eigenvalues):
        projection = mp.eye(k)
        for r, other in enumerate(eigenvalues):
            if r != j:
                projection = projection*(g+epsilon*other*mp.eye(k))
                projection /= epsilon*(other-mu)
        out.append(projection)
    return out


def classical_checks(tolerance):
    parameters = [
        mp.mpc(0), mp.mpc(1), mp.mpc(-1), mp.mpc("0.5"),
        mp.mpc("-0.75"), mp.mpc(0, 1), mp.mpc(0, -1),
        mp.mpc("0.3", "0.4"), mp.mpc("-0.7", "0.6"),
        mp.mpc("0.3", "-0.4"), mp.exp(mp.mpc(0, "0.37")),
    ]
    records = []
    for k in range(1, 7):
        for s in parameters:
            matrix = jacobi(k, s)
            spectrum = eigenvalues(matrix)
            maximum = mp.mpf(0)
            sector_labels = []
            sector_margins = []
            separation = min((abs(a-b) for i, a in enumerate(spectrum)
                              for b in spectrum[i+1:]), default=mp.inf)
            assert separation > tolerance
            for mu in spectrum:
                p = p_values(k, mu)
                vector = mp.matrix(list(reversed(p[:k])))
                maximum = max(
                    maximum, relative(matrix*vector, mu*vector),
                    relative(p[k]-s*p[k-1], 0))
                assert abs(vector[0]) > tolerance
                if mp.im(s) > 0:
                    assert mp.im(mu) > 0
                    radical = mp.sqrt(mu*mu-4)
                    z = min(((mu+radical)/2, (mu-radical)/2), key=abs)
                    radius = abs(z)
                    angle = -mp.arg(z)
                    assert 0 < radius < 1
                    assert 0 < angle < mp.pi
                    sector = int(mp.floor(k*angle/mp.pi))
                    lower = sector*mp.pi/k
                    upper = (2*sector+1)*mp.pi/(2*k)
                    assert lower < angle < upper
                    sector_labels.append(sector)
                    sector_margins.append(min(angle-lower, upper-angle))
                    reconstructed = ((1+z**(2*k+1))
                                     /(z*(1+z**(2*k-1))))
                    maximum = max(maximum, relative(reconstructed, s))
                    lhs = (4*radius**(2*k+1)*mp.sin(2*k*angle)
                           *mp.sin(angle))
                    rhs = (1-radius**2)*(1-radius**(4*k))
                    assert lhs-rhs >= -tolerance
            if mp.im(s) > 0:
                assert sorted(sector_labels) == list(range(k))
            for x in (mp.mpc("0.23", "0.17"), mp.mpc("-0.6", "0.21")):
                p = p_values(k, x)
                maximum = max(maximum, relative(
                    mp.det(x*mp.eye(k)-matrix), p[k]-s*p[k-1]))
            assert maximum < tolerance, (k, s, maximum)
            records.append({
                "channels": k, "s": [mp.nstr(mp.re(s), 22), mp.nstr(mp.im(s), 22)],
                "maximum_relative_error": mp.nstr(maximum, 24),
                "minimum_eigenvalue_separation": mp.nstr(separation, 24),
                "upper_half_plane_sector_labels": sorted(sector_labels),
                "minimum_sector_margin":
                    mp.nstr(min(sector_margins), 24) if sector_margins else None,
            })
    return records


def quantum_checks(tolerance):
    records = []
    for level in range(2, 10):
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        epsilon = (-1)**level
        kappa = q**(mp.mpf((level-1)**2)/2)
        crossing, _, _ = original_matrices(level)
        first = mp.eye(level)[:, 0]
        for k in range(1, 7):
            identity = mp.eye(k)
            efirst, elast = mp.zeros(k), mp.zeros(k)
            efirst[0, 0] = elast[k-1, k-1] = 1
            basic = [identity, -q*path(k)-elast,
                     q*q*(identity-efirst)]
            f = [identity]
            for j in range(level):
                factor = [coefficient*qq**(j*h)
                          for h, coefficient in enumerate(basic)]
                f = poly_multiply(f, factor)
            maximum = relative(f[0], identity)
            coefficient_maximum = mp.mpf(0)
            for h in range(1, level):
                coefficient_maximum = max(coefficient_maximum, mp.norm(f[h]))
            maximum = max(maximum, coefficient_maximum)
            shifted_f = [coefficient*qq**h for h, coefficient in enumerate(f)]
            lhs = poly_multiply(basic, shifted_f)
            rhs = poly_multiply(f, basic)
            maximum = max(maximum, max(relative(a, b) for a, b in zip(lhs, rhs)))
            g_coefficients = [epsilon*f[level+h] for h in range(level+1)]
            g_coefficients[level] -= epsilon*identity
            parameter_records = []
            clocks = [mp.mpc(0), mp.mpc("0.37", "0.19"),
                      mp.mpc("-0.61", "0.23"),
                      mp.exp(mp.mpc(0, "0.41")), mp.mpc(1)]
            physical_projection = None
            for x in clocks:
                g = poly_value(g_coefficients, x)
                classical_j = jacobi(k, x**level)
                if x == 1:
                    mus = [2*mp.cos(mp.pi*j/k) for j in range(k)]
                elif x == 0:
                    mus = [2*mp.cos((2*j+1)*mp.pi/(2*k+1))
                           for j in range(k)]
                else:
                    mus = eigenvalues(classical_j)
                g_characteristic = characteristic(g)
                classical_characteristic = characteristic(-epsilon*classical_j)
                parameter_error = max(relative(a, b) for a, b in zip(
                    g_characteristic, classical_characteristic))
                if x:
                    factors = [channel(k, q, q*qq**j*x)
                               for j in range(level)]
                    backward = identity.copy()
                    for factor in factors:
                        backward = backward*factor
                    expected_shift = epsilon*(x**level+x**(-level))*identity
                    parameter_error = max(
                        parameter_error, relative(backward-expected_shift, g),
                        relative(backward, epsilon*x**(-level)*poly_value(f, x)))
                    hclassical = ((x**level+x**(-level))*identity-classical_j)
                    parameter_error = max(parameter_error, max(
                        relative(a, b) for a, b in zip(
                            characteristic(backward),
                            characteristic(epsilon*hclassical))))
                projections = projectors(g, mus, epsilon)
                parameter_error = max(parameter_error, relative(
                    sum(projections, mp.zeros(k)), identity))
                for j, projection in enumerate(projections):
                    parameter_error = max(
                        parameter_error, relative(projection*projection, projection),
                        relative(mp.fsum(projection[a, a] for a in range(k)), 1),
                        relative(g*projection, -epsilon*mus[j]*projection))
                    for r in range(j):
                        parameter_error = max(
                            parameter_error, relative(projection*projections[r],
                                                      mp.zeros(k)))
                if x:
                    next_g = poly_value(g_coefficients, qq*x)
                    next_projections = projectors(next_g, mus, epsilon)
                    hzero = channel(k, q, q*x)
                    for projection, next_projection in zip(
                            projections, next_projections):
                        parameter_error = max(
                            parameter_error,
                            relative(projection*hzero, hzero*next_projection))
                if x == 1:
                    physical_projection = projections[0]
                assert parameter_error < tolerance, (level, k, x, parameter_error)
                maximum = max(maximum, parameter_error)
                parameter_records.append({
                    "x": [mp.nstr(mp.re(x), 22), mp.nstr(mp.im(x), 22)],
                    "maximum_relative_error": mp.nstr(parameter_error, 24),
                })
            u0 = mp.matrix([q**(k-1-a) for a in range(k)])
            state = u0.copy()
            states = [state.copy()]
            for j in range(1, level):
                d = 4*mp.sin(mp.pi*j/level)**2
                state = mp.lu_solve(channel(k, q, q*qq**j), d*state)
                states.append(state.copy())
            original = crossing**(2*k)*first
            for j, state in enumerate(states):
                maximum = max(maximum, relative(
                    kappa**(2*k)*state[k-1], original[j]))
            endpoint = states[-1]
            marked_pairing = (u0.T*endpoint)[0]
            maximum = max(
                maximum, relative(marked_pairing, epsilon*k*level/q),
                relative(physical_projection,
                         q/(epsilon*k*level)*endpoint*u0.T),
                relative(epsilon*k*level/q*physical_projection[:, k-1], endpoint),
                relative(mp.svd(physical_projection, compute_uv=False)[0],
                         mp.norm(endpoint)/(mp.sqrt(k)*level)))
            gprime = sum((h*g_coefficients[h] for h in range(1, level+1)),
                         mp.zeros(k))
            maximum = max(maximum, relative(
                (u0.T*gprime*endpoint)[0], -level*level/q))
            geometric_sum = mp.fsum(q**(2*a) for a in range(k))
            maximum = max(maximum, relative(
                (q-1/q)*geometric_sum-q**(2*k-1), -1/q))
            assert maximum < tolerance, (level, k, maximum)
            records.append({
                "N": level, "channels": k, "power": 2*k,
                "channels_exceed_level": k > level,
                "low_polynomial_coefficients_checked": level-1,
                "cyclic_polynomial_coefficients_checked": 2*level+3,
                "original_source_colors_checked": level,
                "maximum_relative_error": mp.nstr(maximum, 24),
                "maximum_vanishing_coefficient_norm":
                    mp.nstr(coefficient_maximum, 24),
                "physical_projector_norm":
                    mp.nstr(mp.norm(endpoint)/(mp.sqrt(k)*level), 24),
                "bilinear_marked_pairing":
                    [mp.nstr(mp.re(marked_pairing), 24),
                     mp.nstr(mp.im(marked_pairing), 24)],
                "complex_clock_checks": parameter_records,
            })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    tolerance = mp.power(10, -args.precision//2)
    classical = classical_checks(tolerance)
    quantum = quantum_checks(tolerance)
    script = Path(__file__)
    dependency = script.with_name("check_twist_period_insertion.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Classical complex-sector and eigenvector diagnostics; direct "
                 "polynomial/cyclic identities; quantum characteristic and "
                 "all projector identities through x=0 and physical reset; "
                 "full original crossing columns and bilinear marked "
                 "normalization. No global or asymptotic assertion is "
                 "inferred from these finite checks.",
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "classical_checks": classical, "quantum_checks": quantum,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    maximum = max(mp.mpf(row["maximum_relative_error"])
                  for row in classical+quantum)
    print(json.dumps({
        "status": "pass", "classical_parameter_cases": len(classical),
        "quantum_level_rank_cases": len(quantum),
        "cases_k_greater_than_N": sum(
            row["channels_exceed_level"] for row in quantum),
        "complex_clock_cases": sum(len(row["complex_clock_checks"])
                                   for row in quantum),
        "original_source_colors": sum(
            row["original_source_colors_checked"] for row in quantum),
        "maximum_relative_error": mp.nstr(maximum, 16),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
