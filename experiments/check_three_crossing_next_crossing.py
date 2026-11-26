#!/usr/bin/env python3
"""Check the original next crossing, its two endpoint recurrences, and phase.

Finite asymptotic comparisons are diagnostics, not premises of a proof.
Negative crossings are applied by triangular solves.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_even_reflected_casimir_insertions import (
    apply_power, norm, original_crossing,
)


ROOT = Path(__file__).resolve().parents[1]


def run(precision):
    mp.mp.dps = precision
    worst = mp.mpf(0)
    counts = {}
    records = []

    def check(name, actual, expected):
        nonlocal worst
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        worst = max(worst, error)
        counts[name] = counts.get(name, 0)+1
        if error > mp.mpf(10)**(-precision//2):
            raise ArithmeticError(f"{name}: {mp.nstr(error, 10)}")

    X, z = sp.symbols("X z")
    d = 2-X-1/X
    polynomial = d*z*z-(3-2*X)*z+1-X
    reciprocal_conjugate = d-(3-2/X)*z+(1-1/X)*z*z
    resultant = sp.factor(sp.resultant(polynomial, reciprocal_conjugate, z))
    expected_resultant = ((X-1)**2/X**4
                          * (X**6-2*X**5+2*X**4-X**3+2*X**2-2*X+1))
    assert sp.simplify(resultant-expected_resultant) == 0
    assert sp.simplify((3-2*X)**2-4*d*(1-X)-(4/X-3)) == 0
    cubic_root = mp.findroot(lambda y:y**3-2*y*y-y+3, -mp.mpf("1.15"))
    peak = mp.acos(cubic_root/2)/(2*mp.pi)

    for N in (2, 3, 4, 5, 6, 7, 16, 17, 32, 33, 64, 65, 128, 129):
        matrix = original_crossing(N)
        unit = [mp.mpc(1)]+[mp.mpc(0)]*(N-1)
        g = [mp.mpf(1)]
        for j in range(1, N):
            g.append(g[-1]*4*mp.sin(mp.pi*j/N)**2)
        for sign in (1, -1):
            q = mp.exp(sign*mp.pi*1j/N)
            Q = q*q
            kappa = mp.exp(sign*mp.pi*1j*(N-1)**2/(2*N))
            alpha = apply_power(matrix, unit, 3*sign)
            gamma = apply_power(matrix, alpha[::-1], sign)
            F = [mp.mpc(1)]
            for j in range(1, N):
                F.append(F[-1]*(1-Q**j))
            check("right_endpoint", gamma[-1], N)
            check("left_endpoint", gamma[0], kappa*alpha[-1])
            for j in range(N):
                value = (3-(1+Q**-1)*Q**-j)*gamma[j]
                if j:
                    value += q*(1-Q**-j)*gamma[j-1]
                if j+1 < N:
                    value += q**-1*4*mp.sin(mp.pi*(j+1)/N)**2*gamma[j+1]
                check("forced_tridiagonal", value, kappa*kappa if j == 0 else 0)

            # An unnormalized form is meaningful even at a small exceptional
            # level at which the left endpoint could vanish.
            y = [(-q)**(-j)*g[j]*gamma[j] for j in range(N)]
            P = [(-q)**r*F[r]*gamma[N-1-r]/N for r in range(N)]
            check("left_initial", y[1], (2-Q**-1)*gamma[0]-kappa*kappa)
            check("right_initial", P[1], 2-Q)
            for j in range(1, N-1):
                dj = 4*mp.sin(mp.pi*j/N)**2
                check("left_recurrence", y[j+1],
                      (3-(1+Q**-1)*Q**-j)*y[j]-dj*(1-Q**-j)*y[j-1])
                check("right_recurrence", P[j+1],
                      (3-(1+Q)*Q**j)*P[j]-dj*(1-Q**j)*P[j-1])

            j0 = max(range(N), key=lambda j:g[j])
            h = [q**(j*(j+2))*g[j] for j in range(N)]
            scalar = alpha[j0]/h[j0]
            error = [alpha[j]-scalar*h[j] for j in range(N)]
            transported_error = apply_power(matrix, error[::-1], sign)
            propagated_main = apply_power(matrix, h[::-1], sign)
            for j in range(N):
                check("transported_decomposition", gamma[j],
                      scalar*propagated_main[j]+transported_error[j])
            records.append({
                "N":N, "crossing_sign":sign,
                "log_norm_over_N_diagnostic":mp.nstr(mp.log(norm(gamma))/N, 30),
                "max_index_over_N_diagnostic":mp.nstr(
                    mp.mpf(max(range(N), key=lambda j:abs(gamma[j])))/N, 30),
                "scaled_max_remainder_diagnostic":mp.nstr(max(abs(x) for x in error)/N, 30),
                "relative_transported_error_diagnostic":mp.nstr(norm(transported_error)/norm(gamma), 30),
                "quarter_log_modulus_over_N_diagnostic":mp.nstr(mp.log(abs(gamma[N//4]))/N, 30),
            })
        print(f"Checked original next crossing at both signs, N={N}.", flush=True)
    path = Path(__file__).resolve()
    dependency = path.with_name("check_even_reflected_casimir_insertions.py")
    return {
        "status":"passed", "precision_decimal_digits":precision,
        "mpmath_version":mp.__version__, "sympy_version":sp.__version__,
        "script_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "dependency_sha256":{str(dependency.relative_to(ROOT)):
            hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "exact_check_counts":counts, "symbolic_checks":2,
        "maximum_relative_residual":mp.nstr(worst, 30),
        "peak_location_diagnostic":mp.nstr(peak, 30),
        "records":records,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=140)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-three-crossing-next-crossing.json")
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Saved {args.output}")
