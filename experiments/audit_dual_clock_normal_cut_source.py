"""Exact dual Toeplitz clock source and its derivative/current checks."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.functions.combinatorial.numbers import stirling


def main():
    delta, b, w = sp.symbols("delta b w")
    exact = 0
    rows = []
    for N in range(2, 12):
        n = N - 1
        coeff = [
            sp.rf(N + 1, h) / sp.factorial(h)
            * sum((-1)**r * sp.binomial(r, h) * delta**r
                  for r in range(h, n + 1))
            for h in range(N)
        ]
        P = sum(coeff[h] * b**h for h in range(N))
        for j in range(N):
            value = sum(
                coeff[h] * (-1)**h * sp.rf(j + 1, h) / sp.rf(N + 1, h)
                for h in range(N)
            )
            assert sp.expand(value - (1 + delta)**j) == 0
            exact += 1
            # Euler-weight derivatives are normalized actual cut moments.
            for degree in range(1, 4):
                left = value
                for _ in range(degree):
                    left = (1 + delta) * sp.diff(left, delta) / N
                assert sp.expand(left - sp.Rational(j, N)**degree
                                 * (1 + delta)**j) == 0
                exact += 1
        assert sp.expand(P.subs(b, 0)
                         - sum((-delta)**r for r in range(N))) == 0
        assert sp.expand(P.subs(b, -1)
                         - ((1 + delta)**N - delta**N)) == 0
        exact += 2
        Pw = sp.expand(P.subs(delta, w - 1))
        reverse = sp.cancel(Pw.subs(b, -1 - b)
                            - w**n * Pw.subs(w, 1 / w))
        assert sp.expand(reverse) == 0
        exact += 1
        for degree in range(min(4, N)):
            moment = P
            for _ in range(degree):
                moment = (1 + delta) * sp.diff(moment, delta) / N
            moment = sp.expand(moment.subs(delta, 0))
            closed = sum(
                sp.rf(N + 1, h) / (N**degree * sp.factorial(h))
                * sum(stirling(degree, s, kind=2) * (-1)**s
                      * sp.binomial(s, h) * sp.factorial(s)
                      for s in range(h, degree + 1)) * b**h
                for h in range(degree + 1)
            )
            assert sp.expand(moment - closed) == 0
            assert moment == 0 or sp.degree(moment, b) <= degree
            exact += 1

        current = sp.symbols(f"J0:{N + 1}")
        lhs = sum(w**j * (current[j + 1] - current[j])
                  for j in range(N)) / N
        head = sum(w**j * current[j] for j in range(N)) / N
        rhs = (1 / w - 1) * head + (
            w**(N - 1) * current[N] - current[0] / w) / N
        assert sp.expand(lhs - rhs) == 0
        exact += 1
        rows.append({"N": N, "clock_rows": N, "normal_degree": n,
                     "weyl_identity": True, "endpoints_and_current": True})
    result = {
        "status": "pass",
        "exact_checks": exact,
        "levels": rows,
        "scope": "normalized trace clock co-source; actual on conserving weighted/Green arrays; no off-diagonal average-coupon or Gaussian descent assumed",
    }
    target = Path(__file__).with_name("dual_clock_normal_cut_source_results.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "pass", "exact_checks": exact,
                      "N": [2, 11], "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()

