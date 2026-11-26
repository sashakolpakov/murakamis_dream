#!/usr/bin/env python3
"""Check factorial-weighted Green equations against original Newton matrices.

The written proof is in research_elementary_weighted_green_transport.md.
These diagnostics check its exact conjugations, endpoint forcing,
inverse entries, and weighted singular values; they do not certify a
general source asymptotic.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_current_free_aw_crossing_transport import newton_multiplication


def relative(left, right):
    return mp.norm(left-right)/max(mp.mpf(1), mp.norm(left), mp.norm(right))


def run(precision):
    mp.mp.dps = precision
    rows = []
    for level in list(range(2, 19)) + [24, 25]:
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        identity = mp.eye(level)
        x = mp.diag([qq**j for j in range(level)])
        cyclic = mp.zeros(level)
        for j in range(level):
            cyclic[(j+1) % level, j] = 1
        b = -q*x + (identity-qq*x)*cyclic.T
        p = q*newton_multiplication(level)-q*q*x
        upper = mp.zeros(level)
        for j in range(level-1):
            upper[j, j+1] = 1
        factorial = [mp.mpf(1)]
        pochhammer = [mp.mpc(1)]
        for j in range(1, level):
            factorial.append(factorial[-1]*2*mp.sin(mp.pi*j/level))
            pochhammer.append(pochhammer[-1]*(1-qq**j))
        dg = mp.diag([q**(j*j)/pochhammer[j] for j in range(level)])
        dh = mp.diag([q**(j*(j+2))*factorial[j]**2 for j in range(level)])
        db = mp.diag([-q*qq**j for j in range(level)])
        dp = mp.diag([qq**(-j) for j in range(level)])
        bweighted = dg**-1*b*dg
        pweighted = dh**-1*p*dh
        expected = 1/(2*mp.sin(mp.pi/(4*level+2)))
        bmin = mp.eighe(bweighted.H*bweighted, eigvals_only=True)[0]
        pmin = mp.eighe(pweighted.H*pweighted, eigvals_only=True)[0]
        binverse, pinverse = b**-1, p**-1
        maximum = max(
            relative(bweighted, db*(identity-upper)),
            relative(pweighted, dp*(identity-upper.T)),
            relative(1/mp.sqrt(bmin), expected),
            relative(1/mp.sqrt(pmin), expected),
            relative(factorial[-1], level),
            relative(b*dg*mp.matrix([1]*level),
                     mp.mpf((-1)**(level-1))/level*identity[:, level-1]),
            relative(p*dh*mp.matrix([1]*level), identity[:, 0]),
        )
        for j in range(level):
            for k in range(level):
                bp = factorial[k]/factorial[j] if j <= k else 0
                pp = (factorial[j]/factorial[k])**2 if k <= j else 0
                maximum = max(maximum, relative(abs(binverse[j, k]), bp),
                              relative(abs(pinverse[j, k]), pp))
        assert maximum < mp.power(10, -precision//2), (level, maximum)
        rows.append({"N": level, "inverse_entries": 2*level*level,
                     "maximum_relative_error": mp.nstr(maximum, 25),
                     "weighted_inverse_norm": mp.nstr(expected, 25)})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = run(args.precision)
    dependency = Path(__file__).with_name("check_current_free_aw_crossing_transport.py")
    report = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Exact original elementary Green equations and weighted inverse norms; "
                 "no general short-word asymptotic inferred.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
        "checks": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "pass", "levels": len(rows),
                      "inverse_entries": sum(row["inverse_entries"] for row in rows),
                      "maximum_relative_error": str(max(mp.mpf(row["maximum_relative_error"])
                                                        for row in rows)),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
