#!/usr/bin/env python3
"""Check original crossing identities and record Gaussian-limit diagnostics.

Small-level reference matrices use polynomial multiplication in the full
Newton quotient. Larger-level Gaussian and singular-value comparisons are
diagnostics only; the all-level limits and error bounds are proved in the note.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import numpy as np

import check_complete_boundary_coefficient_transport as finite


def data(level):
    q = mp.exp(mp.pi * 1j / level)
    kappa = mp.exp(mp.pi * 1j * (level-1)**2 / (2*level))
    roots = [2*mp.cos(mp.pi*(2*j+1)/level) for j in range(level)]
    factorial = [mp.mpf(1)]
    for j in range(1, level):
        factorial.append(factorial[-1]*2*mp.sin(mp.pi*j/level))
    return q, kappa, roots, factorial


def original_matrix(level):
    q, kappa, roots, factorial = data(level)
    modulus = [mp.mpc(1)]
    for root in roots:
        modulus = finite.mul(modulus, [-root, 1])
    numerator, basis = [mp.mpc(1)], [[mp.mpc(1)]]
    for j in range(1, level):
        numerator = finite.mul(numerator, [roots[j-1], -1])
        basis.append(finite.scale(numerator, 1/factorial[j]**2))
    crossing = [mp.mpc(0)]*level
    for j in range(level):
        crossing = finite.add(
            crossing, finite.scale(basis[j], kappa*(-q)**j))
    matrix = mp.zeros(level)
    for k in range(level):
        column = finite.coordinates(
            finite.remainder(finite.mul(crossing, basis[k]), modulus),
            basis)
        for j in range(level):
            matrix[j, k] = column[j]
    return matrix, q, kappa, factorial


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path(
        "repro/results/research-one-crossing-gaussian-window.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-30))
    exact = []

    def check(label, level, actual, expected):
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, level, mp.nstr(error, 20)))
        exact.append({"N": level, "identity": label,
                      "relative_error": mp.nstr(error, 14)})

    for level in range(2, 11):
        matrix, q, kappa, factorial = original_matrix(level)
        eta, Q = (-1)**(level-1), q*q
        unit = mp.eye(level)[:, 0]
        first = matrix*unit
        second = matrix*first
        inverse = matrix**-1
        lower = mp.zeros(level)
        for j in range(level):
            lower[j, j] = -q**-1*Q**(-j)
            if j:
                lower[j, j-1] = 1-Q**(-j)
            check("first original column", level, first[j],
                  kappa*(-q)**j)
            check("second original column", level, second[j],
                  kappa*kappa*1j**j*q**(mp.mpf(j*(j+3))/2)*factorial[j])
            for k in range(level):
                check("full inverse conjugation", level, inverse[j, k],
                      mp.conj(matrix[j, k]))
                expected = (kappa*(-1)**j*q**(j*(k+1))*factorial[j]
                            /(factorial[k]*factorial[j-k])
                            if k <= j else 0)
                check("original triangular normalization", level,
                      matrix[j, k], expected)
        forced = lower*second
        for j in range(level):
            check("full endpoint forcing", level, forced[j],
                  eta if j == 0 else 0)
        delta = mp.mpf(1)/16
        approximate = mp.matrix([
            second[j] if abs(mp.mpf(j)/level-mp.mpf(5)/6) < delta else 0
            for j in range(level)])
        approximate[0] = kappa*kappa
        discrepancy = inverse*approximate-first
        check("retained exact source pin", level, approximate[0], second[0])
        check("retained exact forcing row", level,
              (lower*approximate)[0], eta)
        for j in range(level):
            if mp.mpf(j)/level < mp.mpf(5)/6-delta:
                check("inverse lower-color discrepancy", level, discrepancy[j],
                      -2j*kappa*(-1)**j*mp.sin(mp.pi*j/level))

    beta = mp.pi/mp.sqrt(3)
    rho = (5-mp.sqrt(21))/2
    gamma = mp.sqrt(21)*beta/2
    d = (5+mp.sqrt(21))*beta/4
    constant = 1/(mp.sqrt(2)*mp.root(3, 4))
    check("Mehler ratio", 0, beta/(2*d), rho)
    check("Mehler quadratic coefficient", 0, gamma/d-1, -rho*rho)
    check("Mehler ground eigenvalue", 0,
          constant*mp.sqrt(mp.pi/d), mp.sqrt(rho))
    check("Gaussian Hilbert-Schmidt normalization", 0,
          mp.sqrt(rho)/(1-rho), 1/mp.sqrt(3))
    rate = 3*mp.im(mp.polylog(2, mp.exp(2j*mp.pi/3)))/(2*mp.pi)
    diagnostics = []
    for level in (24, 25, 48, 49, 96, 97):
        q, kappa, _, factorial = data(level)
        scaled = np.zeros((level, level), dtype=np.complex128)
        for j in range(level):
            for k in range(j+1):
                value = (kappa*(-1)**j*q**(j*(k+1))*factorial[j]
                         /(factorial[k]*factorial[j-k])*mp.exp(-level*rate))
                scaled[j, k] = complex(value)
        singular = np.linalg.svd(scaled, compute_uv=False)
        x = (np.arange(level)-2*level/3)/np.sqrt(level)
        y = (np.arange(level)-level/3)/np.sqrt(level)
        nu = complex(kappa*mp.exp(1j*(2*mp.pi/3-2*mp.pi*level/9)))
        transformed = (scaled*np.exp(-4j*np.pi*np.arange(level)/3)[:, None]
                       *np.exp(-2j*np.pi*np.arange(level)/3)[None, :]/nu)
        limit_grid = (3**(-.25)*np.exp(
            -float(beta)*(x[:, None]**2+y[None, :]**2)
            +(float(beta)+1j*np.pi)*x[:, None]*y[None, :])/np.sqrt(level))
        a = 2.0
        input_vector = np.exp(-a*y*y/2-2j*np.pi*np.arange(level)/3)
        input_vector /= np.linalg.norm(input_vector)
        out_curvature = 2*float(beta)-(float(beta)+1j*np.pi)**2/(a+2*float(beta))
        amplitude = ((a/np.pi)**.25*3**(-.25)
                     *np.sqrt(2*np.pi/(a+2*float(beta))))
        predicted = (nu*amplitude*level**(-.25)
                     *np.exp(4j*np.pi*np.arange(level)/3-out_curvature*x*x/2))
        diagnostics.append({
            "N": level,
            "scaled_hilbert_schmidt_norm": float(np.linalg.norm(scaled)),
            "scaled_top_singular_value": float(singular[0]),
            "squared_second_to_first_ratio": float((singular[1]/singular[0])**2),
            "cell_center_kernel_error": float(np.linalg.norm(transformed-limit_grid)),
            "normalized_gaussian_output_error": float(np.linalg.norm(
                scaled@input_vector-predicted)),
            "cap_rayleigh_quotient": float(
                level*mp.exp(-2*level*rate)/singular[0]**2),
        })
    script = Path(__file__).resolve()
    dependency = Path(finite.__file__).resolve()
    record = {
        "status": "passed",
        "scope": ("Finite original-quotient identities are checked. Larger-level "
                  "Gaussian and singular comparisons are diagnostics, not proofs "
                  "of limits or uniform errors."),
        "exact_decimal_precision": args.precision,
        "asymptotic_diagnostic_arithmetic": "complex128 after high-precision entry evaluation",
        "mpmath_version": mp.__version__,
        "numpy_version": np.__version__,
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependency_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "exact_check_count": len(exact),
        "maximum_exact_relative_error": max(
            (row["relative_error"] for row in exact), key=mp.mpf),
        "exact_checks": exact,
        "limit_constants": {
            "c": mp.nstr(rate, 35), "rho": mp.nstr(rho, 35),
            "top_singular": mp.nstr(rho**mp.mpf(".25"), 35),
            "hilbert_schmidt": mp.nstr(mp.power(3, -mp.mpf(".25")), 35)},
        "asymptotic_diagnostics": diagnostics,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print("Passed", len(exact), "finite identities; recorded",
          len(diagnostics), "Gaussian/singular diagnostics.")
    print("Maximum finite relative error:", record["maximum_exact_relative_error"])
    print(args.output)


if __name__ == "__main__":
    main()
