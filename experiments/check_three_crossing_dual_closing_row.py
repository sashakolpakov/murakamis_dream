#!/usr/bin/env python3
"""Finite checks of the original dual closing row, including its first normal.

These verify exact identities and conventions at finitely many levels.
No observation lower bound or asymptotic connection coefficient is asserted.
"""

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

from check_even_reflected_casimir_insertions import original_crossing


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_three_crossing_dual_closing_row.md"
DEPENDENCY = Path(__file__).with_name("check_even_reflected_casimir_insertions.py")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.mpf(10) ** (-precision // 2)
    maximum = mp.mpf(0)
    count = 0

    def check(a, b):
        nonlocal maximum, count
        error = abs(a-b) / max(mp.mpf(1), abs(a), abs(b))
        maximum = max(maximum, error)
        count += 1
        assert error < tolerance, (a, b, error)

    for n in range(2, 11):
        for sign in (1, -1):
            q = mp.exp(sign*mp.pi*1j/n)
            Q = q*q
            kappa = mp.exp(sign*mp.pi*1j*(n-1)**2/(2*n))
            eta = (-1)**(n-1)
            M = mp.matrix(original_crossing(n))
            if sign < 0:
                M = M.conjugate()
            J = mp.matrix(n)
            C = mp.matrix(n)
            d = [2-Q**j-Q**(-j) for j in range(n)]
            c = [q*Q**j+q**(-1)*Q**(-j) for j in range(n)]
            for j in range(n):
                J[j, n-1-j] = 1
                C[j, j] = c[j]
                if j:
                    C[j, j-1] = -d[j]
            L = J*C*J
            L1 = M**-1*L*M
            L2 = M**-2*L*M**2
            predicted = 8*q*mp.eye(n)-q*C*L1-q*q*L
            for i in range(n):
                for j in range(n):
                    check(L2[i, j], predicted[i, j])
            for j in range(1, n):
                check(L2[j-1, j], Q**j*(1-Q**j)**2)
            for w in (-mp.mpf(2), mp.mpc("0.3", "0.2")):
                e, ep = [mp.mpc(1)], [mp.mpc(0)]
                for j in range(n-1):
                    e.append(e[-1]*(c[j]-w)/d[j+1])
                    ep.append((ep[-1]*(c[j]-w)-e[-2])/d[j+1])
                row = mp.matrix([e])*J*M**2
                normal = mp.matrix([ep])*J*M**2
                t0, t1 = mp.mpc(1), w/2
                p0, p1 = mp.mpc(0), mp.mpf(1)/2
                for j in range(1, n):
                    t0, t1, p0, p1 = (
                        t1, w*t1-t0, p1, t1+w*p1-p0,
                    )
                P, derivative = 2*t1+2, 2*p1
                residual = row*(L2-w*mp.eye(n))
                first_normal = normal*(L2-w*mp.eye(n))-row
                for j in range(n):
                    check(residual[j], -eta*kappa**2*P/n**2 if j == 0 else 0)
                    check(first_normal[j],
                          -eta*kappa**2*derivative/n**2 if j == 0 else 0)
                check(row[n-1], kappa**2)
                check(normal[n-1], 0)
    assert 32**2-4*3*128 < 0
    assert (-3)**3+16*(-3)**2+128*(-3)+256 < 0
    assert (-2)**3+16*(-2)**2+128*(-2)+256 > 0
    return {
        "status": "passed",
        "scope": "Finite exact-identity diagnostics; no asymptotic observation claim.",
        "precision": precision,
        "levels": list(range(2, 11)),
        "crossing_signs": [1, -1],
        "identity_checks": count,
        "maximum_relative_residual": mp.nstr(maximum, 30),
        "half_period_polynomial": [1, 16, 128, 256],
        "script_sha256": digest(Path(__file__).resolve()),
        "note_sha256": digest(NOTE),
        "dependency_sha256": {str(DEPENDENCY.relative_to(ROOT)): digest(DEPENDENCY)},
        "python": platform.python_version(),
        "mpmath": mp.__version__,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-three-crossing-dual-closing-row.json")
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "identity_checks", "maximum_relative_residual",
                       "script_sha256")}, indent=2))
    print(f"Saved {args.output}")
