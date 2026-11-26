#!/usr/bin/env python3
"""Check the actual Hermitian current and its retained boundary observations.

These finite checks reproduce exact operator identities and inertia at
the displayed levels. They do not prove a uniform spectral gap, an
asymptotic residual rate, or an original-source lower bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp

from check_three_crossing_boundary_current import (
    maxnorm, newton_jet, original, rel,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_original_almost_invariance_and_observation.md"
DEPENDENCY = ROOT / "experiments/check_three_crossing_boundary_current.py"


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    categories, counts, records = {}, {}, []

    def check(name, actual, expected):
        error = rel(actual, expected)
        categories[name] = max(categories.get(name, mp.mpf(0)), error)
        counts[name] = counts.get(name, 0) + 1
        assert error < tolerance, (name, error)

    for N in range(2, 11):
        D = N-1
        for sign in (1, -1):
            q, Q, kappa, nodes, sine_squares, M, C, J, B, L1 = original(N, sign)
            I = mp.eye(N)
            X = mp.diag([Q**j for j in range(N)])
            L, T, S = C.T, C-q*X, J*M**3*J
            # Construct A from the original band entries, independently
            # of the factorization whose congruence is being checked.
            A3 = q**-2*(L**2-I)*L1+q**-3*L*C-8*q**-2*L+8*q**-1*I
            A = B*(A3-L)-I
            H = A*B*J
            check("original_pseudo_unitarity", M.H*J*M, J)
            check("original_B_adjoint", B.H, J*B*J)
            check("original_T_adjoint", T.H, J*T*J)
            check("independent_A_factorization", A, B*S*T*S**-1)
            check("H_hermitian", H, H.H)
            check("H_congruence", H, (B*S)*(T*J)*(B*S).H)

            # Numerical inertia verifies the finite fixtures only.
            # The all-level proof uses the nonsingular Hermitian path.
            eigenvalues = mp.eighe((H+H.H)/2, eigvals_only=True)
            plus = sum(value > 0 for value in eigenvalues)
            minus = sum(value < 0 for value in eigenvalues)
            assert (plus, minus) == (N//2, (N+1)//2)
            assert min(abs(value) for value in eigenvalues) > mp.power(10, -precision//3)

            e0 = mp.matrix(N, 1)
            e0[0] = 1
            eD = J*e0
            h, factorial_square = mp.matrix(N, 1), mp.mpf(1)
            for j in range(N):
                if j:
                    factorial_square *= sine_squares[j]
                h[j] = q**(j*(j+2))*factorial_square
            hnorm = mp.sqrt(mp.fsum(abs(value)**2 for value in h))
            v = J*h/hnorm
            check("factorial_right_forcing", T*h, e0/q)
            check("factorial_adjoint_forcing", T.H*J*h, eD/q)
            check("endpoint_solution_norm_one", T*(eD/q), eD)
            residual_norm = mp.sqrt(mp.fsum(abs(value)**2 for value in T.H*v))
            check("adjoint_residual", residual_norm, 1/hnorm)
            check("adjoint_endpoint_overlap", abs(v[D]), 1/hnorm)
            check("adjoint_observation_ratio", abs(v[D])/residual_norm, 1)

            alpha = M**3*e0
            f = J*M**3*J*alpha
            zeta = (-1)**D*kappa**2/q
            check("original_pair_endpoint_current", A*f, zeta*eD)
            green = H**-1*eD
            check("full_source_green_vector", f, zeta*B*J*green)
            check("unturned_cap_green", f[D], -zeta/q*green[0])
            check("unturned_cap_is_known_endpoint", f[D], kappa**3*alpha[D])

            evaluations = []
            for label, w in (
                ("complete_remaining_boundary", mp.mpc(-2)),
                ("nonreal_boundary", mp.mpc(mp.mpf(1)/3, mp.mpf(2)/5)),
                ("double_physical_node", mp.mpc(nodes[0])),
            ):
                values, normals = newton_jet(w, nodes, sine_squares)
                row = mp.matrix([values])
                derivative_row = mp.matrix([normals])
                literal = (row*f)[0]
                normal = (derivative_row*f)[0]
                transformed = (zeta*row*B*J*green)[0]
                transformed_normal = (zeta*derivative_row*B*J*green)[0]
                check("boundary_green_value", literal, transformed)
                check("boundary_green_first_normal", normal, transformed_normal)
                evaluations.append({
                    "point": label,
                    "value_relative_error": mp.nstr(rel(literal, transformed), 25),
                    "normal_relative_error": mp.nstr(rel(normal, transformed_normal), 25),
                })
            records.append({
                "N": N, "crossing_sign": sign,
                "inertia": [plus, minus, 0],
                "minimum_absolute_H_eigenvalue_diagnostic": mp.nstr(
                    min(abs(value) for value in eigenvalues), 25),
                "boundary_checks": evaluations,
            })
        print(f"Checked original Hermitian current at N={N}, both signs.", flush=True)
    return categories, counts, records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-original-almost-invariance-observation.json",
    )
    args = parser.parse_args()
    if args.precision < 70:
        parser.error("Use at least 70 decimal digits.")
    categories, counts, records = run(args.precision)
    source = Path(__file__).resolve()
    result = {
        "status": "pass",
        "precision_decimal_digits": args.precision,
        "python_version": platform.python_version(),
        "mpmath_version": mp.__version__,
        "scope": (
            "Original Hermitian congruence/inertia, full boundary polynomial "
            "and first normals, and exact adjoint residual/endpoint ratio. "
            "Finite eigenvalues are diagnostics, not a uniform spectral-gap "
            "or source-asymptotic assertion."
        ),
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(NOTE.read_bytes()).hexdigest(),
        "dependency_sha256": {
            str(DEPENDENCY.relative_to(ROOT)):
                hashlib.sha256(DEPENDENCY.read_bytes()).hexdigest(),
        },
        "identity_count": sum(counts.values()),
        "category_counts": counts,
        "category_maximum_relative_errors": {
            name: mp.nstr(value, 25) for name, value in categories.items()
        },
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "identity_count": result["identity_count"],
        "maximum_relative_error": mp.nstr(max(categories.values()), 25),
        "output": str(args.output),
        "script_sha256": result["script_sha256"],
    }))


if __name__ == "__main__":
    main()
