"""Actual memory-charge clocks with positive/negative first-normal carries."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
import numpy as np

from audit_high_color_first_normal_r_degree import setup


def main():
    records = []
    checks = 0
    for N, r in ((2, 3), (3, 3), (4, 4), (5, 3)):
        p, m, coefficient = setup(N, r)
        w = int(sp.primitive_root(p))
        counts = {"+": {}, "-": {}}
        for negative in (False, True):
            sigma = -1 if negative else 1
            name = "-" if negative else "+"
            for i in range(m + 1):
                a, s = divmod(i, N)
                for j in range(m + 1):
                    limit = min(j, m - i) if negative else min(i, m - j)
                    for k in range(limit + 1):
                        value = coefficient(i, j, k, negative=negative)
                        out2 = i + k if negative else i - k
                        oa, os = divmod(out2, N)
                        carry = oa - a
                        charge = (oa - os) - (a - s)
                        assert k == sigma * (charge - (N + 1) * carry)
                        if value.x:
                            assert carry == 0
                        if value.dx:
                            assert carry in (0, -sigma), (N, r, negative, i, j, k, carry)
                            counts[name][carry] = counts[name].get(carry, 0) + 1
                        phase_charge = pow(w, sigma * charge, p)
                        phase_carry = pow(w, -sigma * (N + 1) * carry, p)
                        assert (phase_charge * phase_carry - pow(w, k, p)) % p == 0
                        if value.dx:
                            actual_difference = value.dx * (pow(w, k, p) - phase_charge) % p
                            expected = 0 if carry == 0 else value.dx * phase_charge * (
                                pow(w, N + 1, p) - 1) % p
                            assert actual_difference == expected
                        checks += 1
            assert counts[name].get(-sigma, 0) > 0
        inverse_blocks = 0
        for total in range(2 * m + 1):
            states = [(i, total - i) for i in range(m + 1)
                      if 0 <= total - i <= m]
            index = {state: i for i, state in enumerate(states)}
            matrices = []
            for negative in (False, True):
                root = np.zeros((len(states), len(states)), dtype=np.int64)
                normal = np.zeros_like(root)
                for col, (i, j) in enumerate(states):
                    limit = min(j, m - i) if negative else min(i, m - j)
                    for k in range(limit + 1):
                        value = coefficient(i, j, k, negative=negative)
                        output = (j - k, i + k) if negative else (j + k, i - k)
                        row = index[output]
                        root[row, col] = value.x
                        normal[row, col] = value.dx
                matrices.append((root, normal))
            (a, da), (b, db) = matrices
            assert np.array_equal(a @ b % p, np.eye(len(states), dtype=np.int64))
            assert np.count_nonzero((da @ b + a @ db) % p) == 0
            inverse_blocks += 1
        records.append({"N": N, "r": r, "prime": p,
                        "nonzero_first_normal_carries": counts,
                        "positive_negative_dual_inverse_blocks": inverse_blocks})
    out = Path(__file__).with_name("actual_memory_clock_and_normal_transfer_results.json")
    out.write_text(json.dumps({"status": "pass", "coefficient_checks": checks,
                              "records": records,
                              "scope": "exact actual root and first-normal transfer clocks; no Gaussian source identification"},
                             indent=2) + "\n")
    print(json.dumps({"status": "pass", "coefficient_checks": checks,
                      "results": str(out)}, indent=2))


if __name__ == "__main__":
    main()

