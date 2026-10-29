#!/usr/bin/env python3
"""Proved source/phase identities and diagnostic five-crossing homotopy.

The exact source transform is proved separately. Continuation samples
here are not a certified thimble or uniqueness proof; the later selected
contour construction and Arb certificate supply different arguments.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.special import spence

from audit_finite_sum_annihilator import field


def exact_algebra():
    t = sp.symbols("t")
    B = sp.Matrix([[2, 1], [1, 2]])
    signs = [(1, 1, 1), (1, 1, -1), (-1, 1, -1),
             (1, -1, 1), (-1, -1, 1), (-1, -1, -1)]
    rows = []
    for sx, sy, sd in signs:
        C = sp.Matrix([[3 * sx - sd, sd], [sd, -sy - sd]])
        forcing = sp.Matrix([sp.Rational(3 * sx - sd, 2), sp.Rational(sd - sy, 2)]) + t * sp.Matrix([3, 2])
        determinant = sp.factor((C + t * B).det())
        rows.append({"signs": [sx, sy, sd], "determinant": str(determinant), "forcing": str(forcing)})
    alpha = (2 * sp.sqrt(7) - 5) / 3
    C = sp.Matrix([[4, -1], [-1, 0]])
    v = sp.Matrix([2 * alpha, 1 - alpha])
    assert all(sp.simplify(x) == 0 for x in (C + alpha * B) * v)
    projection = sp.simplify((v.T * (sp.Matrix([2, -1]) + alpha * sp.Matrix([3, 2])))[0])
    assert sp.simplify(projection - (1 - 19 * alpha) / 3) == 0
    assert projection != 0
    X, Y, r = sp.symbols("X Y r")
    f = r ** 3 + r ** 2 + 2 * r + 1
    Yr = r ** 2 + r + 1
    Xr = (r ** 2 + 2 * r + 4) / 5
    assert sp.rem(Yr ** 3 + Yr ** 2 - 1, f, r) == 0
    assert sp.rem(sp.together(Xr * Yr ** 2 + (1 - Xr) * Yr - Xr), f, r) == 0
    assert sp.rem(sp.together((1 - Xr) ** 3 - Xr ** 3 * Yr * (1 - Yr)), f, r) == 0
    a, b, c = sp.symbols("a b c")
    H = sp.Matrix([[3 * a - c, c], [c, -b - c]])
    assert sp.factor(H.det().subs(a, (b * c - 1) / (b + c))) == 3 - 2 * b * c
    return {"infinity_cone_table": rows, "resonant_forcing_projection": str(projection),
            "Riley_and_hessian_identities": "PASS"}


def coefficient_sources():
    cases = 0
    for N in range(2, 27):
        p, _, q = field(N)
        Q = q * q % p
        fac = [1]
        for n in range(1, N):
            fac.append(fac[-1] * (1 - pow(Q, n, p)) % p)
        for n in range(N):
            t = pow(Q, -n - 1, p)
            H = sum(fac[n] * pow(fac[j] * fac[n - j] % p, -1, p) * pow(t, j, p)
                    for j in range(n + 1)) % p
            coefficient = sum(pow(t, j, p) * pow(fac[j] * fac[n - j] % p, -1, p)
                              for j in range(n + 1)) % p
            assert H == fac[n] * coefficient % p
            cases += 1
    return {"finite_field_GF_coefficients": cases, "levels": 25}


def lattice_phases():
    with mp.workdps(65):
        maximum = mp.mpf(0)
        count = 0
        for N in range(2, 25):
            Q = mp.exp(2j * mp.pi / N)
            fac = [mp.mpc(1)]
            for n in range(1, N):
                fac.append(fac[-1] * (1 - Q ** n))
            for n in range(N):
                for j in range(n + 1):
                    x, y = mp.mpf(n) / N, mp.mpf(j) / N
                    actual = Q ** (-n * (n + 2) - j * (n + 1)) * fac[n] ** 3 / (fac[j] * fac[n - j])
                    B = mp.pi * (3 * x + 2 * y - x * x - x * y - y * y)
                    predicted = abs(actual) * mp.exp(1j * N * B - 1j * mp.pi * (3 * x + 2 * y))
                    maximum = max(maximum, abs(actual / predicted - 1))
                    count += 1
        assert maximum < mp.mpf("1e-50")
        return {"cases": count, "max_relative_error": float(maximum)}


def continuation():
    pi = np.pi
    L = lambda z: np.log(2 * np.sin(pi * z))

    def gradient(z, t):
        x, y = z
        return np.array([3 * L(x) - L(x - y) + 1j * t * pi * (3 - 2 * x - y),
                         -L(y) + L(x - y) + 1j * t * pi * (2 - x - 2 * y)])

    def hessian(z, t):
        x, y = z
        c = pi / np.tan(pi * (x - y))
        return np.array([[3 * pi / np.tan(pi * x) - c - 2j * t * pi, c - 1j * t * pi],
                         [c - 1j * t * pi, -pi / np.tan(pi * y) - c - 2j * t * pi]])

    z0 = root(lambda r: gradient(r.astype(complex), 0).real,
              [.78786562, .39393281], tol=1e-12).x.astype(complex)

    def rhs(t, real):
        z = real[:2] + 1j * real[2:]
        x, y = z
        velocity = np.linalg.solve(hessian(z, t), -1j * pi * np.array([3 - 2 * x - y, 2 - x - 2 * y]))
        return np.r_[velocity.real, velocity.imag]

    sol = solve_ivp(rhs, [0, 1], np.r_[z0.real, z0.imag], rtol=2e-12, atol=2e-14,
                    max_step=.001, dense_output=True)
    J = lambda z: (pi * pi / 6 - spence(1 - np.exp(2j * pi * z))) / (2j * pi) - 1j * pi / 2 * (z * z - z)
    rows = []
    for t in np.linspace(0, 1, 1001):
        r = sol.sol(t)
        z = r[:2] + 1j * r[2:]
        x, y = z
        action = 3 * J(x) - J(y) - J(x - y) + 1j * t * pi * (3 * x + 2 * y - x * x - x * y - y * y)
        H = hessian(z, t)
        rows.append({"t": float(t), "x": [float(x.real), float(x.imag)], "y": [float(y.real), float(y.imag)],
                     "gradient_residual": float(np.max(np.abs(gradient(z, t)))),
                     "abs_hessian_determinant": float(abs(np.linalg.det(H))),
                     "critical_action": [float(action.real), float(action.imag)],
                     "max_ReH_eigenvalue": float(np.linalg.eigvalsh(H.real)[-1])})
    last = rows[-1]
    x = complex(*last["x"])
    y = complex(*last["y"])
    X, Y = np.exp(2j * pi * x), np.exp(2j * pi * y)
    assert abs(Y ** 3 + Y ** 2 - 1) < 1e-9
    assert abs(5 * X ** 3 - 7 * X ** 2 + 4 * X - 1) < 1e-9
    return {"status": "DIAGNOSTIC_ONLY_NOT_INTERVAL_CERTIFIED", "samples": rows,
            "min_abs_det": min(r["abs_hessian_determinant"] for r in rows),
            "max_gradient_residual": max(r["gradient_residual"] for r in rows),
            "min_sampled_critical_rate": min(r["critical_action"][0] for r in rows)}


def main():
    result = {"exact_algebra": exact_algebra(), "coefficient_sources": coefficient_sources(),
              "exact_lattice_phase": lattice_phases(), "homotopy_continuation": continuation(),
              "scope": "Exact double source; this homotopy diagnostic alone proves no selected thimble or volume theorem."}
    output = Path(__file__).with_name("selected_angular_source_homotopy_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    h = result["homotopy_continuation"]
    print(json.dumps({"exact_algebra": "PASS", "coefficient_sources": result["coefficient_sources"],
                      "exact_lattice_phase": result["exact_lattice_phase"],
                      "homotopy_status": h["status"], "min_sampled_abs_det": h["min_abs_det"],
                      "min_sampled_critical_rate": h["min_sampled_critical_rate"],
                      "selected_source_status": "NOT_PROVED"}, indent=2))


if __name__ == "__main__":
    main()
