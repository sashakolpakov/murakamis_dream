#!/usr/bin/env python3
"""Check the exact fourth-cap observation using the full Newton quotient.

The reference crossing is constructed by polynomial multiplication and
reduction, retaining repeated roots. The comparison uses the denominator-free
version of equation (5), so no small-level nonvanishing is assumed.
These finite diagnostics do not test or prove the asymptotic theorem.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

import check_one_crossing_gaussian_window as original


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-positive-fourth-cap-exact-identity.json")
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-35))
    records = []

    for N in range(2, 13):
        base, q0, kappa0, factorial = original.original_matrix(N)
        D, eta = N-1, (-1)**(N-1)
        reversal = mp.matrix([[int(j+k == D) for k in range(N)]
                              for j in range(N)])
        cap = mp.eye(N)[:, 0]
        for sign in (1, -1):
            M = base if sign == 1 else base**-1
            q = q0 if sign == 1 else mp.conj(q0)
            H = M.transpose_conj()*M
            observed = H*H*cap
            gamma = M*reversal*(M**3)*cap
            # gamma_0*y_r, computed without division by gamma_0.
            numerator = [(-q)**(-r)*factorial[r]**2*gamma[r]
                         for r in range(N)]
            for k in range(N):
                expected = eta*q**(-D*(k+1))/factorial[k]*mp.fsum(
                    q**(k*r)*factorial[r+k]/factorial[r]**3
                    *mp.conj(numerator[r]) for r in range(D-k+1))
                error = abs(observed[k]-expected)/max(
                    1, abs(observed[k]), abs(expected))
                if error >= tolerance:
                    raise AssertionError((N, sign, k, mp.nstr(error, 20)))
                records.append({"N": N, "crossing_sign": sign, "index": k,
                                "relative_error": mp.nstr(error, 18)})

    script = Path(__file__).resolve()
    dependencies = [Path(original.__file__).resolve(),
                    Path(original.finite.__file__).resolve()]
    result = {
        "status": "passed",
        "precision_decimal_digits": args.precision,
        "checks": len(records),
        "levels": [2, 12],
        "crossing_signs": [1, -1],
        "maximum_relative_error":
            mp.nstr(max(mp.mpf(row["relative_error"]) for row in records), 18),
        "comparison": "Equation (5), with gamma_0*y_r retained as one numerator",
        "reference": "Polynomial multiplication in the full original Newton quotient",
        "scope": "Finite exact-identity diagnostics; no asymptotic assertion is tested",
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependencies": {
            str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in dependencies},
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("records", "dependencies")}, indent=2))


if __name__ == "__main__":
    main()
