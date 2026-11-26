#!/usr/bin/env python3
"""Check exact crossing-run Schur systems against the original matrices.

The conjugations use literal original crossing matrices. Continuants
are independently built from finite Chebyshev recurrences, and block
responses are checked by inversion of the complete block matrix.
No asymptotic lower bound is inferred from these diagnostics.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_current_free_aw_crossing_transport import newton_multiplication
from check_rational_word_normalized_cofactor import finite_determinant


def relative(left, right):
    return mp.norm(left-right)/max(mp.mpf(1), mp.norm(left), mp.norm(right))


def block_system(first, later, q, count):
    size = first.rows
    out = mp.zeros(size*count)
    for block in range(count):
        diagonal = first if block == 0 else later
        for i in range(size):
            for j in range(size):
                out[block*size+i, block*size+j] = diagonal[i, j]
            if block+1 < count:
                out[block*size+i, (block+1)*size+i] = -q
                out[(block+1)*size+i, block*size+i] = -q
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    for level in range(2, 11):
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        eta = (-1)**(level-1)
        identity = mp.eye(level)
        crossing, _, _ = original_matrices(level)
        z = newton_multiplication(level)
        x = mp.diag([qq**j for j in range(level)])
        shift = mp.zeros(level)
        for j in range(level):
            shift[(j+1) % level, j] = 1
        k = -q**-1*x**-1+(identity-x**-1)*shift
        b = -q*x+(identity-qq*x)*shift.T
        maximum = max(
            relative(crossing*x**-1*crossing**-1, -q*k),
            relative(crossing**-1*x*crossing,
                     x+q**-1*(x-identity)*shift),
            relative(crossing*k*crossing**-1, q*x-z),
            relative(crossing*b*crossing**-1, k.T),
            relative(x*k-qq*k*x, (q-q**-1)*identity),
        )
        chebyshev = {-2: -identity, -1: mp.zeros(level), 0: identity}
        for m in range(1, 5):
            chebyshev[m] = z*chebyshev[m-1]-chebyshev[m-2]
        p = {m: q**m*(chebyshev[m]-q*chebyshev[m-1]*x)
             for m in range(-1, 5)}
        c = {m: q**m*(chebyshev[m]*k+chebyshev[m-1])
             for m in range(-1, 5)}
        signed_cases = 0
        block_cases = 0
        reflection_cases = 0
        arbitrary_parameter_characteristics = 0
        for m in range(5):
            even = p[m]*p[m-1]**-1
            odd = c[m]*c[m-1]**-1
            negative_even = p[m-1].conjugate()*p[m].conjugate()**-1
            negative_odd = c[m-1].conjugate()*c[m].conjugate()**-1
            for exponent, expected in [
                    (2*m, even), (2*m+1, odd),
                    (-2*m, negative_even), (-2*m-1, negative_odd)]:
                literal = crossing**exponent*x**-1*crossing**(-exponent)
                maximum = max(maximum, relative(literal, expected))
                signed_cases += 1
            for j in range(level):
                maximum = max(maximum,
                              relative(p[m][j, j], qq**(-m*j)),
                              relative(c[m][j, j],
                                       -q**-1*qq**(-(m+1)*j)))
                for column in range(level):
                    if j-column > m or column > j:
                        maximum = max(maximum, abs(p[m][j, column]))
                    if j-column > m+1 or column > j:
                        maximum = max(maximum, abs(c[m][j, column]))
            maximum = max(maximum,
                          relative(finite_determinant(p[m]), eta**m),
                          relative(finite_determinant(c[m]), eta**m))
            if m > 0:
                path = mp.zeros(m)
                for j in range(m-1):
                    path[j, j+1] = path[j+1, j] = 1
                pin = mp.zeros(m)
                pin[0, 0] = 1
                endpoint = mp.eye(m)
                color_green = []
                for color in range(level):
                    r = q*qq**color
                    local = (r+r**-1)*mp.eye(m)-path-r*pin
                    green_local = local**-1
                    color_green.append(green_local)
                    endpoint = green_local*endpoint
                    scalar_u = [mp.mpc(1)]
                    if m > 1:
                        scalar_u.append(r+r**-1)
                    for j in range(2, m):
                        scalar_u.append((r+r**-1)*scalar_u[j-1]-scalar_u[j-2])
                    explicit = mp.matrix(m)
                    for i in range(m):
                        for j in range(m):
                            lo, hi = min(i, j), max(i, j)
                            explicit[i, j] = r**(m-lo)*scalar_u[m-hi-1]
                    maximum = max(maximum, relative(green_local, explicit))
                for color in range(level):
                    maximum = max(maximum, relative(
                        color_green[level-1-color], color_green[color].H))
                positive = (-1)**level*endpoint
                maximum = max(maximum, relative(positive, positive.H),
                              relative((even**-1)[level-1, 0],
                                       q**-1*level**2*endpoint[m-1, m-1]),
                              relative((p[m]**-1)[level-1, 0],
                                       q**-m*level**2*endpoint[0, m-1]))
                eigenvalues = mp.eighe((positive+positive.H)/2, eigvals_only=True)
                assert eigenvalues[0] >= mp.mpf(5)**(-level)*(1-tolerance)
                assert eigenvalues[m-1] <= mp.mpf(m)**(2*level)*(1+tolerance)
                exact_spectrum = sorted(
                    1/(4*mp.sin(mp.pi*(2*j-1)/(4*m+2))**2)
                    for j in range(1, m+1))
                for j in range(m):
                    maximum = max(maximum, relative(
                        eigenvalues[j], exact_spectrum[j]))
                assert eigenvalues[0] >= mp.mpf(1)/4*(1-tolerance)
                assert eigenvalues[m-1] <= mp.mpf((2*m+1)**2)/4*(1+tolerance)
                reflection_cases += 1
                arbitrary_r = mp.mpc(".7", ".2")
                monodromy = mp.eye(m)
                for color in range(level):
                    r = arbitrary_r*qq**color
                    local = (r+r**-1)*mp.eye(m)-path-r*pin
                    monodromy = local**-1*monodromy
                central_r = eta*arbitrary_r**level
                predicted = ((central_r+central_r**-1)*mp.eye(m)
                             -path-central_r*pin)**-1
                for power in range(1, m+1):
                    lhs = monodromy**power
                    rhs = predicted**power
                    maximum = max(maximum, relative(
                        mp.fsum(lhs[j, j] for j in range(m)),
                        mp.fsum(rhs[j, j] for j in range(m))))
                arbitrary_parameter_characteristics += 1
            if level <= 7 and m <= 2:
                systems = [(block_system(-q*k, q*z, q, m+1),
                            odd, m+1)]
                if m > 0:
                    systems.append((block_system(q*z-q*q*x, q*z, q, m),
                                    even, m))
                for system, response, count in systems:
                    inverse = system**-1
                    last = inverse[(count-1)*level:count*level,
                                   (count-1)*level:count*level]
                    maximum = max(maximum,
                                  relative(last, response**-1),
                                  relative(finite_determinant(system), eta**count))
                    block_cases += 1
        e0 = mp.matrix([1]+[0]*(level-1))
        forced = p[1]**-1*e0
        sine_factorial = mp.mpf(1)
        for j in range(level):
            if j:
                sine_factorial *= 2*mp.sin(mp.pi*j/level)
            maximum = max(maximum, relative(
                forced[j], q**(j*(j+2))*sine_factorial**2))
        assert maximum < tolerance, (level, maximum)
        rows.append({
            "N": level,
            "signed_matrix_conjugations": signed_cases,
            "full_block_systems": block_cases,
            "complete_endpoint_reflection_cases": reflection_cases,
            "arbitrary_parameter_characteristic_cases": arbitrary_parameter_characteristics,
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
        "check_rational_word_normalized_cofactor.py",
    ]
    result = {
        "status": "pass",
        "scope": "Original signed crossing conjugations, finite-band "
                 "continuants, exact Schur responses and determinants, "
                 "endpoint reflection positivity and exact spectrum, arbitrary-r "
                 "cyclotomic characteristic identity, and forced inverse column; no general source "
                 "noncancellation estimate is asserted.",
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
        "status": "pass",
        "levels": len(rows),
        "signed_conjugations": sum(r["signed_matrix_conjugations"] for r in rows),
        "full_block_systems": sum(r["full_block_systems"] for r in rows),
        "complete_endpoint_reflection_cases": sum(
            r["complete_endpoint_reflection_cases"] for r in rows),
        "arbitrary_parameter_characteristic_cases": sum(
            r["arbitrary_parameter_characteristic_cases"] for r in rows),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["maximum_relative_error"]) for r in rows), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
