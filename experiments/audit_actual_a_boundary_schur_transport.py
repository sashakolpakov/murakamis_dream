#!/usr/bin/env python3
"""Boundary Schur identities: original source, retained kernel, amplification.

The actual scalar figure-eight sample checks elimination identities, not
root-level pointed uniqueness: that requires the bounded jets in the proof.
The exact rational fixture checks the singular Gram coefficient formula.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_pointed_a_bulk_agmon import actual_system


def actual_source_case(N):
    M, b, y, rows = actual_system(N)
    colors = np.arange(1, N + 1)
    gamma = -np.log(2.5)
    L = M * np.exp(gamma * (rows[:, None] - colors[None, :]))
    u = np.exp(gamma * colors) * y
    f = np.exp(gamma * rows) * b
    P, g = L.conj().T @ L, L.conj().T @ f
    interior = np.where((colors / N >= .23) & (colors / N <= .27))[0]
    boundary = np.setdiff1d(np.arange(N), interior)
    A = P[np.ix_(interior, interior)]
    Pib = P[np.ix_(interior, boundary)]
    Pbb = P[np.ix_(boundary, boundary)]
    H = -np.linalg.solve(A, Pib)
    S = Pbb + Pib.conj().T @ H
    assert np.linalg.norm(g[interior]) == 0
    minimum = np.linalg.eigvalsh(A)[0]
    assert minimum > 1
    scale = max(1., np.linalg.norm(P) * np.linalg.norm(u))
    errors = [np.linalg.norm(u[interior] - H @ u[boundary]),
              np.linalg.norm(S @ u[boundary] - g[boundary]),
              abs(np.vdot(u[boundary], S @ u[boundary]) - np.vdot(f, f))]
    assert max(errors) < 1e-10 * scale, (N, errors, scale)
    # This checks the full quadratic identity, including non-solutions.
    rng = np.random.default_rng(1000 + N)
    v = rng.normal(size=N) + 1j * rng.normal(size=N)
    residual = v[interior] - H @ v[boundary]
    lhs = np.vdot(v, P @ v)
    rhs = np.vdot(residual, A @ residual) + np.vdot(v[boundary], S @ v[boundary])
    assert abs(lhs - rhs) < 1e-11 * max(1., abs(lhs))
    assert np.linalg.eigvalsh(S)[0] > -1e-10 * max(1., np.linalg.norm(S))
    return {"N": N, "interior_colors": len(interior),
            "interior_gram_gap": float(minimum),
            "largest_source_identity_error": float(max(errors)),
            "quadratic_identity_error": float(abs(lhs - rhs))}


def exact_kernel_fixture():
    # Arbitrary positive A, a retained null direction, and nontrivial H.
    A = sp.Matrix([[3, 1], [1, 2]])
    H = sp.Matrix([[1, -2, 3], [2, 1, -1]])
    S = sp.Matrix([[2, -1, 0], [-1, 3, 0], [0, 0, 0]])
    P = A.row_join(-A * H).col_join(
        (-H.T * A).row_join(S + H.T * A * H))
    ub = sp.Matrix([2, -1, 7])
    u = (H * ub).col_join(ub)
    gb = S * ub
    g = sp.zeros(2, 1).col_join(gb)
    beta = (ub.T * S * ub)[0]
    assert P * u == g
    E = H.col_join(sp.eye(3))
    assert P.nullspace() == [(E * S.nullspace()[0]) / (E * S.nullspace()[0])[-1]]
    Rb = sp.Matrix([[1, 2, 0], [3, -1, 0]])
    lam, z = sp.symbols("lam z")
    Q = (S + lam * sp.eye(3)).det().expand()
    D = ((S + lam * sp.eye(3) + z * Rb.T * Rb).row_join(gb)
         .col_join(gb.T.row_join(sp.Matrix([[beta]])))).det().expand()
    quotient = D.coeff(lam, 1).coeff(z, 1) / Q.coeff(lam, 1)
    expected = (ub.T * Rb.T * Rb * ub)[0]
    assert quotient == expected
    assert all(c >= 0 for c in sp.Poly(D, lam, z).coeffs())
    assert all(c >= 0 for c in sp.Poly(Q, lam).coeffs())
    assert sp.simplify(P[2:, 2:] - P[2:, :2] * A.inv() * P[:2, 2:] - S) == sp.zeros(3)
    return {"retained_kernel_dimension": 1, "selected_gram_ratio": int(quotient)}


def exact_rigid_recurrence(n):
    L = sp.eye(n + 1)
    for j in range(1, n + 1):
        L[j, j - 1] = -2
    P = L.T * L
    I, B = list(range(1, n)), [0, n]
    A = P.extract(I, I)
    S = P.extract(B, B) - P.extract(B, I) * A.inv() * P.extract(I, B)
    Dn = sp.Rational(4**n - 1, 3)
    formula = sp.Matrix([[1 + 4**n / Dn, -2**n / Dn],
                         [-2**n / Dn, 1 / Dn]])
    assert S == formula
    gb = sp.Matrix([1, 0])
    assert S.inv() * gb == sp.Matrix([1, 2**n])
    assert S.det() == 1 / Dn
    lam, z = sp.symbols("lam z")
    R = sp.Matrix([[0, 1]])
    Q = (S + lam * sp.eye(2)).det().expand()
    D = ((S + lam * sp.eye(2) + z * R.T * R).row_join(gb)
         .col_join(gb.T.row_join(sp.ones(1)))).det().expand()
    ratio = D.coeff(lam, 0).coeff(z, 1) / Q.coeff(lam, 0)
    assert ratio == 4**n
    return {"steps": n, "exact_selected_energy": int(ratio),
            "boundary_determinant": str(S.det())}


def main():
    mp.mp.dps = 110
    data = {"status": "PASS",
            "actual_source_schur_cases": [actual_source_case(N) for N in [32, 48, 64, 96]],
            "exact_retained_kernel": exact_kernel_fixture(),
            "exact_rigid_boundary_responses": [exact_rigid_recurrence(n) for n in [2, 3, 5, 8]],
            "scope": "Exact elimination and selected boundary period. No broad sharp geometric bound inferred."}
    Path(__file__).with_name("actual_a_boundary_schur_transport_results.json").write_text(
        json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
