#!/usr/bin/env python3
"""Exact identities for the complete adjacent-three-crossing quartics.

This verifies algebra and excluded divisors, not a quantum asymptotic.
The strict representation-volume gap is the written rigidity argument.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_three_crossing_quartic_representation_gap.md"
DEPENDENCY = ROOT / "experiments/check_three_crossing_geometric_branch.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "repro/results/research-three-crossing-quartic-representation-gap.json",
    )
    args = parser.parse_args()
    tau = sp.Symbol("tau")
    v = (tau - 2) ** 2 * (tau**2 - 2 * tau + 2)
    z = 4 - 5 * tau + 4 * tau**2 - tau**3
    h = tau**5 - 7 * tau**4 + 20 * tau**3 - 32 * tau**2 + 30 * tau - 14
    records = []
    for epsilon in (1, -1):
        f = sp.Poly(v - 2 * epsilon * sp.I, tau, extension=sp.I)
        c = 2 * epsilon * sp.I / h
        d = 2 * epsilon * (tau - 1) / h
        q = sp.I * (tau + 1) / (tau - 1)
        expressions = {
            "half_cosine_c": c**2 - (2 - tau) / 4,
            "half_cosine_d": d**2 - (2 - z) / 4,
            "rational_square_root": q**2 + 1 - c**-2 - d**-2,
            "cosine_relation": d - sp.I * (1 - tau) * c,
            "inverse_h_identity": -(2 - tau) * h**2 / 16 - 1,
            "terminal_filling_constant": q * d - c * (1 + tau),
            "terminal_filling_sine": d / c - sp.I * (1 - tau),
            "outer_filling_constant":
                epsilon * c * (q * d + 1 - d**2) / d**2 - d * (1 + z),
            "outer_filling_sine":
                epsilon * c * (q * d + 1) / d**2 - sp.I * (1 - z),
        }
        identity_results = {}
        denominator_results = {}
        for name, expression in expressions.items():
            numerator, denominator = sp.cancel(expression).as_numer_denom()
            remainder = sp.rem(sp.Poly(numerator, tau, extension=sp.I), f)
            gcd = sp.gcd(sp.Poly(denominator, tau, extension=sp.I), f).monic()
            assert remainder.is_zero, (epsilon, name, remainder.as_expr())
            assert gcd.degree() == 0, (epsilon, name, gcd.as_expr())
            identity_results[name] = "zero exact remainder"
            denominator_results[name] = "coprime to quartic"
        factors = {
            "h": h,
            "tau": tau,
            "tau_minus_1": tau - 1,
            "tau_plus_1": tau + 1,
            "tau_minus_2": tau - 2,
            "tau_plus_2": tau + 2,
            "z_minus_2": z - 2,
            "z_plus_2": z + 2,
            "z_minus_6": z - 6,
        }
        gcd_results = {}
        for name, factor in factors.items():
            gcd = sp.gcd(f, sp.Poly(factor, tau, extension=sp.I)).monic()
            assert gcd.degree() == 0, (epsilon, name, gcd.as_expr())
            gcd_results[name] = "1"
        simple = sp.gcd(f, f.diff()).monic()
        assert simple.degree() == 0
        records.append({
            "epsilon": epsilon,
            "quartic": str(f.as_expr()),
            "identities": identity_results,
            "identity_denominators": denominator_results,
            "excluded_factor_gcds": gcd_results,
            "simple_root_gcd": str(simple.as_expr()),
        })

    plus = sp.Poly(v - 2 * sp.I, tau, extension=sp.I)
    minus = sp.Poly(v + 2 * sp.I, tau, extension=sp.I)
    assert sp.gcd(plus, minus).degree() == 0
    # The trace-square test does not silently identify different roots by ±.
    all_roots = sp.Poly(v**2 + 4, tau)
    sign_gcd = sp.gcd(all_roots, sp.Poly(all_roots.as_expr().subs(tau, -tau), tau))
    assert sign_gcd.degree() == 0

    result = {
        "status": "passed",
        "scope": (
            "Exact algebra and regularity of the eight complete quartic "
            "representations. No numerical volume, source-cycle, endpoint-overlap "
            "or asymptotic assertion."
        ),
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "script_sha256": sha(Path(__file__).resolve()),
        "note_sha256": sha(NOTE),
        "root_isolation_checker": str(DEPENDENCY.relative_to(ROOT)),
        "root_isolation_checker_sha256": sha(DEPENDENCY),
        "records": records,
        "quartic_lists_gcd": "1",
        "opposite_root_gcd": str(sign_gcd.as_expr()),
        "identity_count": sum(len(record["identities"]) for record in records),
        "excluded_divisor_count": sum(
            len(record["excluded_factor_gcds"]) for record in records
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "identities": result["identity_count"],
        "excluded_divisors": result["excluded_divisor_count"],
        "output": str(args.output),
        "script_sha256": result["script_sha256"],
    }, indent=2))


if __name__ == "__main__":
    main()
