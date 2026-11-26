#!/usr/bin/env python3
"""Check literal reflected insertions and record Casimir residual diagnostics.

The original crossing is applied by matrix-vector multiplication. Negative
powers in the literal closing word use triangular solves, not conjugation or
the Gram identity being tested. Finite residuals do not prove an asymptotic
rate, monotonicity, or concentration.
"""

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp


def encode(value):
    return {
        "real": mp.nstr(mp.re(value), 30),
        "imag": mp.nstr(mp.im(value), 30),
    }


def norm(vector):
    return mp.sqrt(mp.fsum(abs(x)**2 for x in vector))


def relative(a, b):
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def original_crossing(level):
    """Literal normalized Newton multiplication matrix of the crossing."""
    d = level-1
    q = mp.exp(mp.pi*1j/level)
    kappa = mp.exp(mp.pi*1j*d*d/(2*level))
    factorials = [mp.mpf(1)]
    for j in range(1, level):
        factorials.append(factorials[-1]*2*mp.sin(mp.pi*j/level))
    matrix = [[mp.mpc(0) for _ in range(level)] for _ in range(level)]
    for i in range(level):
        for j in range(i+1):
            matrix[i][j] = (
                kappa*(-1)**i*q**(i*(j+1))
                *factorials[i]/(factorials[j]*factorials[i-j])
            )
    return matrix


def multiply(matrix, vector):
    return [
        mp.fsum(matrix[i][j]*vector[j] for j in range(i+1))
        for i in range(len(vector))
    ]


def solve(matrix, vector):
    """Apply the actual inverse by solving the lower triangular system."""
    answer = []
    for i in range(len(vector)):
        answer.append(
            (vector[i]-mp.fsum(matrix[i][j]*answer[j] for j in range(i)))
            /matrix[i][i]
        )
    return answer


def apply_power(matrix, vector, power):
    answer = list(vector)
    step = multiply if power >= 0 else solve
    for _ in range(abs(power)):
        answer = step(matrix, answer)
    return answer


def casimir(vector, nodes, sine_squares):
    return [
        nodes[j]*vector[j]-(sine_squares[j]*vector[j-1] if j else 0)
        for j in range(len(vector))
    ]


def polynomial(coefficients, vector, nodes, sine_squares):
    """Coefficients are in increasing order."""
    answer = [mp.mpc(0) for _ in vector]
    for coefficient in reversed(coefficients):
        answer = casimir(answer, nodes, sine_squares)
        answer = [x+coefficient*y for x, y in zip(answer, vector)]
    return answer


def inner(left, right):
    return mp.fsum(mp.conj(a)*b for a, b in zip(left, right))


def geometric_point(k):
    def equations(eta, phi):
        return (
            mp.cosh(2*k*eta)-mp.cos(2*k*phi)-mp.cosh(eta)+mp.cos(phi),
            mp.sinh(2*k*eta)*mp.sinh(eta)+mp.sin(2*k*phi)*mp.sin(phi),
        )
    phi_min, phi_max = 2*mp.pi/(2*k+1), mp.pi/k
    eta, phi = mp.findroot(
        equations, (mp.mpf("0.4")/k, (phi_min+phi_max)/2)
    )
    assert 0 < eta < mp.mpf("0.5")
    assert phi_min < phi < phi_max
    t = phi-1j*eta
    return eta, phi, -2*mp.cos(t)


def evaluate(coefficients, z):
    return mp.fsum(coefficient*z**j
                   for j, coefficient in enumerate(coefficients))


def run(precision, levels, ranks):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    points = {k: geometric_point(k) for k in ranks}
    tests = [
        ("uninserted", [1], [1]),
        ("right_casimir", [1], [0, 1]),
        ("two_polynomials", [1, 1+2j, mp.mpf(1)/5], [2, -1, 1j]),
        ("core_colors_2_3", [0, -1], [-1, 0, 1]),
    ]
    records = []
    for level in levels:
        matrix = original_crossing(level)
        nodes = [2*mp.cos((2*j+1)*mp.pi/level) for j in range(level)]
        sine_squares = [4*mp.sin(j*mp.pi/level)**2 for j in range(level)]
        algebra_error = mp.mpf(0)
        for i in range(level):
            for j in range(i+1):
                cm = nodes[i]*matrix[i][j]
                if i and j < i:
                    cm -= sine_squares[i]*matrix[i-1][j]
                mc = nodes[j]*matrix[i][j]
                if j+1 <= i:
                    mc -= sine_squares[j+1]*matrix[i][j+1]
                algebra_error = max(algebra_error, relative(cm, mc))
        for j in range(level):
            algebra_error = max(
                algebra_error, abs(nodes[j]-nodes[level-1-j])
            )
            if j:
                algebra_error = max(
                    algebra_error, abs(sine_squares[j]-sine_squares[level-j])
                )
        assert algebra_error < tolerance, (level, "Casimir algebra", algebra_error)
        first = [mp.mpc(1)]+[mp.mpc(0)]*(level-1)
        for k in ranks:
            alpha = apply_power(matrix, first, 2*k)
            energy = mp.fsum(abs(x)**2 for x in alpha)
            alpha_norm = mp.sqrt(energy)
            eta, phi, z = points[k]
            ca = casimir(alpha, nodes, sine_squares)
            residual = norm([x-z*y for x, y in zip(ca, alpha)])/alpha_norm
            cases = []
            max_error = algebra_error
            for name, p, q in tests:
                pa = polynomial(p, alpha, nodes, sine_squares)
                qa = polynomial(q, alpha, nodes, sine_squares)
                gram = inner(pa, qa)
                turned = list(reversed(qa))
                negative = apply_power(matrix, turned, -2*k)
                literal = polynomial(
                    [mp.conj(x) for x in p], negative, nodes, sine_squares
                )[-1]
                error = relative(literal, gram)
                max_error = max(max_error, error)
                assert error < tolerance, (level, k, name, error)
                prediction = mp.conj(evaluate(p, z))*evaluate(q, z)
                cases.append({
                    "insertion": name,
                    "literal_closing_value": encode(literal),
                    "gram_value": encode(gram),
                    "relative_identity_error": mp.nstr(error, 25),
                    "normalized_moment_diagnostic": encode(gram/energy),
                    "proved_limit": encode(prediction),
                    "moment_difference_diagnostic": encode(gram/energy-prediction),
                })
            records.append({
                "N": level, "k": k, "original_positive_power": 2*k,
                "geometric_eta": mp.nstr(eta, 30),
                "geometric_phi": mp.nstr(phi, 30),
                "geometric_casimir": encode(z),
                "casimir_residual_diagnostic": mp.nstr(residual, 25),
                "maximum_relative_identity_error": mp.nstr(max_error, 25),
                "insertion_checks": cases,
            })
        print(f"Checked literal insertions at N={level}.", flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--levels", type=int, nargs="+",
                        default=[12, 13, 24, 25, 48, 49, 96, 97])
    parser.add_argument("--ranks", type=int, nargs="+", default=[2, 3])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.precision < 70 or min(args.levels) < 2 or min(args.ranks) < 2:
        parser.error("Use precision at least 70, levels at least 2, ranks at least 2.")
    records = run(args.precision, args.levels, args.ranks)
    result = {
        "status": "pass",
        "scope": "Literal original crossing/Casimir identities and inserted "
                 "closing functionals versus the exact Newton Gram pairing. "
                 "Casimir residuals and moment differences are finite diagnostics, "
                 "not assertions of numerical convergence rates or monotonicity.",
        "precision_decimal_digits": args.precision,
        "python_version": platform.python_version(),
        "mpmath_version": mp.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass",
        "cases": len(records),
        "inserted_trace_checks": sum(len(r["insertion_checks"]) for r in records),
        "maximum_relative_identity_error": max(
            (r["maximum_relative_identity_error"] for r in records), key=mp.mpf
        ),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
