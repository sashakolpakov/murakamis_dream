"""Actual Frobenius scale/descendant Borel source identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main():
    alpha, u, C, D = sp.symbols("alpha u C D", nonzero=True)
    checks = 0
    levels = []
    for N in range(2, 10):
        e = sp.zeros(N + 1)
        f = sp.zeros(N + 1)
        h = sp.diag(*[N - 2 * k for k in range(N + 1)])
        for k in range(N + 1):
            if k:
                e[k - 1, k] = N - k + 1
            if k < N:
                f[k + 1, k] = k + 1
        ket = sp.ones(N + 1, 1) * alpha**N
        dual = sp.Matrix([[sp.binomial(N, k) * u**k
                           / (alpha**N * (1 + u)**N)
                           for k in range(N + 1)]])
        cut = sp.Matrix([[sp.binomial(N, k) / 2**N for k in range(N + 1)]])
        assert sp.factor((dual * ket)[0] - 1) == 0
        assert sp.factor((dual * h * ket)[0] / N - (1 - u) / (1 + u)) == 0
        assert sp.factor((cut * ket)[0] - alpha**N) == 0
        checks += 3
        for generator, velocity in ((h + 2 * f, 2 * u * (1 + u)),
                                    (e + f, u**2 - 1)):
            ket_derivative = ket.diff(alpha) * alpha + ket.diff(u) * velocity
            dual_derivative = dual.diff(alpha) * alpha + dual.diff(u) * velocity
            assert all(sp.factor(x) == 0 for x in ket_derivative - generator * ket)
            assert all(sp.factor(x) == 0 for x in dual_derivative + dual * generator)
            checks += 2
        levels.append({"N": N, "actual_source_and_dual_fields": True})
    r = 1 / (1 + u) + D * alpha**2
    s = C * alpha**2
    A = 1 / (1 + s)
    jac = sp.diff(r, alpha) * sp.diff(s, u) - sp.diff(r, u) * sp.diff(s, alpha)
    omega = -jac / (s * (1 + s))
    target = -2 * A / (alpha * (1 + u)**2)
    assert sp.factor(omega - target) == 0
    checks += 1
    for velocity, target_r in ((2*u*(1+u), 2*(r-1)),
                                (u**2-1, 2*r-1)):
        assert sp.factor(alpha*sp.diff(r, alpha) + velocity*sp.diff(r, u) - target_r) == 0
        assert sp.factor(alpha*sp.diff(s, alpha) + velocity*sp.diff(s, u) - 2*s) == 0
        divergence = (sp.diff(omega*alpha, alpha) + sp.diff(omega*velocity, u))/omega
        assert sp.factor(divergence - 2*A) == 0
        checks += 3
    output = Path(__file__).with_name("actual_frobenius_borel_torsor_results.json")
    output.write_text(json.dumps({"status": "pass", "exact_checks": checks,
                                "levels": levels,
                                "scope": "actual source/dual Borel and scale-descendant form; no Gaussian current intertwiner assumed"},
                                indent=2) + "\n")
    print(json.dumps({"status": "pass", "exact_checks": checks,
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()

