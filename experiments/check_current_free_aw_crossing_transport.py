#!/usr/bin/env python3
"""Finite original-matrix diagnostics for weighted crossing transport.

The angular difference operator is sampled independently of the original
Newton matrices. Fourier reconstruction retains its unreduced degree.
Full values/normals, the free-boundary defect, and terminal forcing are
compared at both level parities. These are normalization checks, not an
asymptotic or a cycle-selection proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_internal_two_crossing_chain import basis_jet, relative


def chebyshev(degree, z, second_kind=False):
    """Evaluate integer-degree polynomials without a hypergeometric solver."""
    if degree == 0:
        return mp.mpf(1)
    previous, current = mp.mpf(1), (2*z if second_kind else z)
    for _ in range(1, degree):
        previous, current = current, 2*z*current-previous
    return current


def difference(level, power, f, t):
    theta = mp.pi / level
    q = mp.exp(1j * theta)
    a = 4 * mp.cos((t-theta)/2)**4 / (mp.sin(t)*mp.sin(t-theta))
    c = 4 * mp.cos((t+theta)/2)**4 / (mp.sin(t)*mp.sin(t+theta))
    return ((2*mp.cos(theta)+a+c)*f(t)
            - q**power*a*mp.exp(-1j*power*t)*f(t-2*theta)
            - q**power*c*mp.exp(1j*power*t)*f(t+2*theta))


def fourier_polynomial(level, power, degree):
    """Reconstruct the even Laurent polynomial L_power[(-2cos t)^degree]."""
    bound = degree + abs(power)
    count = 2*bound + 5
    offset = mp.mpf("0.137")
    ts = [2*mp.pi*(j+offset)/count for j in range(count)]
    values = [difference(level, power,
                         lambda t: (-2*mp.cos(t))**degree, t)
              for t in ts]
    coeffs = {
        k: mp.fsum(values[j]*mp.exp(-1j*k*ts[j]) for j in range(count))/count
        for k in range(-bound, bound+1)
    }
    discarded = []
    for k in (bound+1, bound+2, -bound-1, -bound-2):
        discarded.append(abs(mp.fsum(
            values[j]*mp.exp(-1j*k*ts[j]) for j in range(count))/count))
    maximum = max(discarded + [
        abs(coeffs[k]-coeffs[-k]) for k in coeffs
    ])
    def angular(t):
        return mp.fsum(v*mp.exp(1j*k*t) for k, v in coeffs.items())
    def value(z):
        return coeffs[0] + mp.fsum(
            2*coeffs[k]*chebyshev(k, -z/2) for k in range(1, bound+1))
    def derivative(z):
        return mp.fsum(
            -k*coeffs[k]*chebyshev(k-1, -z/2, True) for k in range(1, bound+1))
    return value, derivative, angular, maximum


def newton_multiplication(level):
    z = mp.matrix(level)
    for j in range(level):
        z[j, j] = 2*mp.cos((2*j+1)*mp.pi/level)
        if j+1 < level:
            z[j+1, j] = -4*mp.sin((j+1)*mp.pi/level)**2
    return z


def v_coefficients(power, q, z):
    if power >= 0:
        previous = (q+1/q)*mp.eye(z.rows)
        if power == 0:
            return previous
        current = 4*q*mp.eye(z.rows)-q*q*z
        for _ in range(1, power):
            previous, current = current, 8*q*mp.eye(z.rows)-q*z*current-q*q*previous
        return current
    previous = (q+1/q)*mp.eye(z.rows)
    current = 4/q*mp.eye(z.rows)-z/q**2
    for _ in range(1, -power):
        previous, current = current, 8/q*mp.eye(z.rows)-z*current/q-previous/q**2
    return current


def green_checks(level):
    theta = mp.pi/level
    c0 = 2*mp.cos(theta)
    def u_cot_u(u):
        if abs(u) < mp.mpf("1e-20"):
            return 1-u**2/3-u**4/45-2*u**6/945
        return u*mp.cot(u)
    def logarithmic_derivative(x):
        return mp.fsum(u_cot_u(theta*(x-k)) for k in range(level))/level
    g0 = logarithmic_derivative(0)
    def primitive(t):
        ell = (level-1)/2-t/(2*theta)
        return -(logarithmic_derivative(ell)-g0)/(2*theta*mp.sin(theta))
    maximum = mp.mpf(0)
    for t in (mp.mpc(".37", ".21"), mp.mpc("-1.1", ".32")):
        maximum = max(maximum, relative(
            difference(level, 0, primitive, t)-c0*primitive(t), 1))
    _, endpoint_derivative = basis_jet(level, c0)
    for j in range((level-2)//2+1):
        t = mp.pi-(2*j+1)*theta
        point = -2*mp.cos(t)
        values, derivatives = basis_jet(level, point)
        maximum = max(maximum,
                      relative(primitive(t), (endpoint_derivative.T*values)[0]),
                      relative(mp.diff(primitive, t)/(2*mp.sin(t)),
                               (endpoint_derivative.T*derivatives)[0]))
    if level % 2:
        values, _ = basis_jet(level, -2)
        maximum = max(maximum,
                      relative(primitive(0), (endpoint_derivative.T*values)[0]))
    return {"N": level, "maximum_green_and_jet_relative_error": mp.nstr(maximum, 16)}


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    for level in range(2, 11):
        crossing, _, _ = original_matrices(level)
        z = newton_multiplication(level)
        ell = z.T
        turn = mp.matrix([[int(i+j == level-1)
                           for j in range(level)] for i in range(level)])
        unit = mp.matrix([1]+[0]*(level-1))
        theta = mp.pi/level
        q = mp.exp(1j*theta)
        eta = (-1)**(level-1)
        kappa = mp.exp(1j*mp.pi*(level-1)**2/(2*level))
        c0 = 2*mp.cos(theta)
        physical = [2*mp.cos((2*j+1)*theta)
                    for j in range((level-2)//2+1)]
        for power in (-3, -2, -1, 0, 1, 2, 3):
            mult = crossing**power
            conjugated = crossing**(-power)*ell*mult
            max_jet = mp.mpf(0)
            max_free = mp.mpf(0)
            max_fourier = mp.mpf(0)
            cases = 0
            for degree in sorted(set((0, 1, level-1))):
                value, normal, angular, polynomial_error = fourier_polynomial(
                    level, power, degree)
                input_vector = z**degree*unit
                target = conjugated*input_vector
                max_fourier = max(max_fourier, polynomial_error)
                for point in physical:
                    basis, derivatives = basis_jet(level, point)
                    max_jet = max(max_jet,
                                  relative(value(point), (basis.T*target)[0]),
                                  relative(normal(point), (derivatives.T*target)[0]))
                    cases += 2
                if level % 2:
                    basis, _ = basis_jet(level, -2)
                    max_jet = max(max_jet,
                                  relative(value(-2), (basis.T*target)[0]))
                    cases += 1
                for point in (mp.mpc(".31", ".17"), mp.mpc("-1.2", ".08")):
                    basis, _ = basis_jet(level, point)
                    source = turn*mult*input_vector
                    transported = turn*mult*target
                    lhs = point*(basis.T*source)[0]-(basis.T*transported)[0]
                    rhs = eta*kappa**power*(2*chebyshev(level, point/2)+2)*c0**degree/level**2
                    max_free = max(max_free, relative(lhs, rhs))
            terminal = turn*mult*unit
            forcing_vector = v_coefficients(power, q, ell)*terminal
            max_terminal = mp.mpf(0)
            for point in (mp.mpc(".23", ".19"), mp.mpc("-1.1", ".14")):
                basis, _ = basis_jet(level, point)
                lhs = point*(basis.T*terminal)[0]-(basis.T*forcing_vector)[0]
                rhs = eta*kappa**power*(2*chebyshev(level, point/2)+2)/level**2
                max_terminal = max(max_terminal, relative(lhs, rhs))
            maximum = max(max_jet, max_free, max_terminal, max_fourier)
            assert maximum < tolerance, (level, power, maximum)
            rows.append({
                "N": level, "power": power, "full_jet_cases": cases,
                "maximum_physical_jet_relative_error": mp.nstr(max_jet, 16),
                "maximum_free_boundary_defect_relative_error": mp.nstr(max_free, 16),
                "maximum_terminal_forcing_relative_error": mp.nstr(max_terminal, 16),
                "maximum_fourier_polynomial_error": mp.nstr(max_fourier, 16),
            })
    green = [green_checks(level) for level in range(2, 11)]
    assert all(mp.mpf(row["maximum_green_and_jet_relative_error"]) < tolerance
               for row in green)
    return rows, green


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, green = run(args.precision)
    record = {
        "status": "pass",
        "scope": "Exact weighted operator, all physical jets, and ordinary "
                 "free-boundary forcing; no coherent-source lower bound.",
        "precision_decimal_digits": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ("check_twist_period_insertion.py",
                         "check_internal_two_crossing_chain.py")
        },
        "checks": rows,
        "logarithmic_green_checks": green,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "level_power_cases": len(rows),
        "physical_jet_cases": sum(row["full_jet_cases"] for row in rows),
        "logarithmic_green_levels": len(green),
        "maximum_error": mp.nstr(max(
            mp.mpf(row[key]) for row in rows
            for key in row if key.startswith("maximum")), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
