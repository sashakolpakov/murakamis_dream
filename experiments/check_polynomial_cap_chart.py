#!/usr/bin/env python3
"""Finite normalization checks for the polynomial original-cap chart.

Reference matrices are formed by multiplication in the full Newton quotient.
The primitive p3 polynomial is formed independently by its coefficient
recurrence. No large-level or nonvanishing asymptotic is tested.
"""

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import check_one_crossing_gaussian_window as original


def pochhammer(a, Q, count):
    return mp.fprod(1-a*Q**j for j in range(count))


def section(a, b, q, level):
    D, Q = level-1, q*q
    return mp.matrix([
        a**(D-k)*b**k*(-1/q)**k
        *pochhammer(a, Q, k)*pochhammer(b*Q**k, Q, D-k)
        for k in range(level)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path(
        "repro/results/research-polynomial-cap-chart.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-30))
    checks = []

    def check(label, N, actual, expected):
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, N, mp.nstr(error, 20)))
        checks.append({"N": N, "identity": label,
                       "relative_error": mp.nstr(error, 16)})

    for N in range(2, 11):
        M, q, kappa, _ = original.original_matrix(N)
        D, Q = N-1, q*q
        J = mp.matrix(N, N)
        for j in range(N):
            J[j, D-j] = 1
        A = J*M
        parameters = [
            (mp.mpc("0.7", "0.2"), mp.mpc("1.2", "-0.3")),
            (mp.mpc("-0.4", "0.6"), mp.mpc("0.9", "0.1")),
            (mp.mpc(1), Q), (Q, Q), (Q, Q*Q)]
        for a, b in parameters:
            w = section(a, b, q, N)
            target = section(Q*Q/b, Q*Q*a/b, q, N)
            scalar = kappa*q**(D*(D-4))*b**(2*D)
            crossed = M*w
            target_M = section(b/a, b, q, N)
            for j in range(N):
                check("full JM section", N, (A*w)[j],
                      scalar*target[j])
                check("single M character", N, crossed[j],
                      kappa*(a*a/b)**D*(Q/a)**j*target_M[j])
        for j in range(N):
            check("first cap chart", N, section(1, Q, q, N)[j],
                  N if j == 0 else 0)
            check("second cap chart", N, section(Q, Q, q, N)[j],
                  N*Q**D*(-1/q)**j)
            check("third cap chart", N, section(Q, Q*Q, q, N)[j],
                  N*(-q**3)**D if j == D else 0)
            # Compare the first parameter derivative at the original cap.
            left = mp.diff(lambda a: (A*section(a, Q, q, N))[j], 1)
            right = mp.diff(
                lambda a: kappa*q**(D*(D-4))*Q**(2*D)
                *section(Q, Q*a, q, N)[j], 1)
            check("cap parameter jet", N, left, right)
        a, b = parameters[0]
        scalar = mp.mpc(1)
        for _ in range(3):
            scalar *= kappa*q**(D*(D-4))*b**(2*D)
            a, b = Q*Q/b, Q*Q*a/b
        check("three chart scalar", N, scalar, kappa)

        # p_N(x)=sum b_j x^(D-j), with independent Rogers--Szego recurrence.
        coefficients = [mp.mpc(1), mp.mpc(2)]
        for j in range(1, D):
            coefficients.append(
                2*coefficients[j]-(1-Q**(-j))*coefficients[j-1])

        def polynomial(x):
            return mp.polyval(coefficients, x)

        cap = mp.eye(N)[:, 0]
        source = M*(M*(M*cap))
        for j in range(N):
            check("actual three-crossing source", N, source[j],
                  kappa**3*(-q)**j*polynomial(Q**(j+1)))
        check("primitive cap normalization", N, polynomial(Q), 1)
        for x in [mp.mpc(0), mp.mpc("0.3", "0.2"),
                  mp.mpc("-0.4", "0.1"), mp.mpc(1)]:
            check("retained central forcing", N, polynomial(Q*x),
                  (1-x)**2*polynomial(x)+x*(2-x**N))

    here = Path(__file__).resolve()
    dependencies = [
        here.with_name("check_one_crossing_gaussian_window.py"),
        here.with_name("check_complete_boundary_coefficient_transport.py")]
    record = {
        "status": "passed", "precision_digits": args.precision,
        "python": platform.python_version(), "mpmath": mp.__version__,
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependency_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in dependencies},
        "levels": list(range(2, 11)), "finite_identity_count": len(checks),
        "max_relative_error": mp.nstr(max(
            mp.mpf(c["relative_error"]) for c in checks), 20),
        "scope": "Finite exact source/chart diagnostics; no asymptotic inference.",
        "checks": checks}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({k: record[k] for k in [
        "status", "precision_digits", "finite_identity_count",
        "max_relative_error", "script_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
