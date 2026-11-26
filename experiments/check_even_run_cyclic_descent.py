#!/usr/bin/env python3
"""Check the normalized even-run section against the original source.

The tests evaluate whole cyclic orbits, including the singular physical
reset, using polynomial transfer entries.  They test finite identities;
they do not prove the all-level descent theorem or any growth estimate.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_even_run_simple_spectrum_and_marked_kernel import (
    eigenvalues, jacobi, path, poly_multiply, poly_value, projectors, relative,
)


def polynomial_transfer(k, q, x):
    """P(x)=x^{-1} B_k(qx;q), extended polynomially at zero."""
    out = mp.zeros(k)
    for a in range(k):
        for b in range(k):
            gap = abs(a-b)
            top = k-1-max(a, b)
            out[a, b] = q**(gap+1)*x**gap*(
                mp.fsum((q*x)**(2*h) for h in range(top+1))
                -x*mp.fsum((q*x)**(2*h) for h in range(top)))
    return out


def shifted_period_coefficients(level, k, q):
    first, last = mp.zeros(k), mp.zeros(k)
    first[0, 0] = last[k-1, k-1] = 1
    basic = [mp.eye(k), -q*path(k)-last, q*q*(mp.eye(k)-first)]
    full = [mp.eye(k)]
    Q = q*q
    for j in range(level):
        full = poly_multiply(full, [a*Q**(j*h) for h, a in enumerate(basic)])
    epsilon = (-1)**level
    shifted = [epsilon*full[level+h] for h in range(level+1)]
    shifted[level] -= epsilon*mp.eye(k)
    return shifted


def orbit_section(level, k, q, central, coefficients):
    """Literal unnormalized Reynolds sum, with its cardinal seed.

    Central parameters used below are real and in [-1,1]. The distinguished
    eigenvalue is then the largest eigenvalue of the real Jacobi matrix;
    psi is positive, so its normalized logarithm is the real logarithm.
    """
    Q = q*q
    epsilon = (-1)**level
    mus = sorted(eigenvalues(jacobi(k, central)), key=lambda z: mp.re(z),
                 reverse=True)
    if central == 1:
        mus = [2*mp.cos(mp.pi*j/k) for j in range(k)]
        psi = mp.mpf(1)/k
        base = mp.mpf(1)
    else:
        psi = (1+central**2-central*mus[0])/(1-central)
        base = mp.exp(mp.log(mp.mpc(central))/level)
    assert abs(mp.im(psi)) < mp.eps**mp.mpf(".7")
    assert mp.re(psi) > 0
    c = q*mp.exp(-mp.log(psi)/level)
    clocks = [base*Q**j for j in range(level)]
    transfers = [polynomial_transfer(k, q, x) for x in clocks]
    projections = [projectors(poly_value(coefficients, x), mus, epsilon)[0]
                   for x in clocks]
    cap = mp.matrix([q**(k-1-a) for a in range(k)])
    seeds = [mp.fsum((x/Q)**h for h in range(level))/level*projector*cap
             for x, projector in zip(clocks, projections)]
    values = []
    for j in range(level):
        prefix = mp.eye(k)
        total = seeds[j].copy()
        for r in range(1, level):
            prefix = prefix*transfers[(j-r) % level]
            total += c**(-r)*prefix*seeds[(j-r) % level]
        values.append(total)
    return clocks, transfers, projections, values, psi, c


def checks(tolerance):
    records = []
    for level in range(2, 10):
        original, _, _ = original_matrices(level)
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        for k in range(1, 7):
            for sign in (-1, 1):
                q = mp.exp(sign*mp.pi*1j/level)
                Q = q*q
                cap = mp.matrix([q**(k-1-a) for a in range(k)])
                coefficients = shifted_period_coefficients(level, k, q)
                error = relative(polynomial_transfer(k, q, 0), q*mp.eye(k))
                error = max(error, relative(
                    polynomial_transfer(k, q, 1), q*cap*cap.T))
                source = original**(sign*2*k)*mp.eye(level)[:, 0]
                for central in (mp.mpf(1), mp.mpf(".43"), mp.mpf("-.47")):
                    clocks, transfers, projections, values, psi, c = orbit_section(
                        level, k, q, central, coefficients)
                    error = max(error, relative(c**level, -1/psi))
                    for j in range(level):
                        nxt = (j+1) % level
                        error = max(error,
                            relative(projections[j]*values[j], values[j]),
                            relative(transfers[j]*values[j], c*values[nxt]),
                            relative(mp.det(transfers[j]),
                                     q**k*(1-clocks[j])**(k-1)),
                            relative(transfers[j]*projections[j],
                                     projections[nxt]*transfers[j]))
                    period = mp.eye(k)
                    for transfer in transfers:
                        period = transfer*period
                    error = max(error, relative(
                        period*projections[0], -projections[0]/psi))
                    if central == 1:
                        error = max(error, relative(values[1], cap))
                        state = cap.copy()
                        factorial = mp.mpc(1)
                        sampled_energy = mp.mpf(0)
                        for j in range(level):
                            if j:
                                state = (Q**j-1)*transfers[j]*state
                                factorial *= 1-Q**j
                            sample = (-q)**j*mp.power(k, mp.mpf(j)/level)*factorial
                            sample *= values[(j+1) % level]
                            error = max(error, relative(sample, state),
                                        relative(kappa**(sign*2*k)*sample[k-1],
                                                 source[j]))
                            sampled_energy += abs(sample[k-1])**2
                        error = max(error, relative(
                            sampled_energy, mp.fsum(abs(z)**2 for z in source)))
                assert error < tolerance, (level, k, sign, error)
                records.append({
                    "N": level, "channels": k, "signed_power": sign*2*k,
                    "cyclic_orbits": 3, "physical_colors": level,
                    "maximum_relative_error": mp.nstr(error, 24),
                })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    records = checks(mp.power(10, -args.precision//2))
    dependencies = (
        "check_even_run_simple_spectrum_and_marked_kernel.py",
        "check_twist_period_insertion.py", "check_internal_vertex_asymptotic.py",
    )
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Finite identities for the specified even cyclic descent and "
                 "the original source; no all-parameter or asymptotic claim.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {
            "experiments/"+name: hashlib.sha256(
                (Path(__file__).resolve().parent/name).read_bytes()).hexdigest()
            for name in dependencies
        },
        "maximum_relative_error": max(
            (r["maximum_relative_error"] for r in records), key=mp.mpf),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "signed_cases": len(records),
                      "orbits": sum(r["cyclic_orbits"] for r in records),
                      "maximum_relative_error": result["maximum_relative_error"],
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
