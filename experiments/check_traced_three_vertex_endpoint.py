#!/usr/bin/env python3
"""Exact scalar certificates and finite checks for the traced power-three vertex.

Arb proves the scalar inequalities used in the analytic entropy argument.
Independent high-precision matrix calculations check the exact finite identity;
they do not replace its symbolic proof or establish an asymptotic by sampling.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
from flint import acb, arb, ctx


def scalar_certificates():
    ctx.prec = 160
    pi = arb.pi()
    ii = acb(0, 1)

    def J(z):
        z = acb(z)
        return (-ii * pi * (z * z - z) / 2
                + ii * (2 * ii * pi * z).exp().polylog(2) / (2 * pi)
                - ii * pi / 12)

    X = (1 + ii * arb(3).sqrt()) / 4
    j = J(arb(1) / 3).real
    H = -j - arb(2) / 3 * arb(2).log() + 2 * X.polylog(2).imag / pi
    x = acb(arb(1) / 6, arb(2).log() / (2 * pi))
    t = acb(-arb(1) / 4, 3 * arb(3).sqrt() / 4).acos()
    arg1 = arb(1) / 2 - x + t / (2 * pi)
    arg2 = arb(1) / 2 - x - t / (2 * pi)
    b = -J(arg1) - J(arg2) - 2 * J(x)
    F = 2 * b + 3 * ii * t * t / (4 * pi) - ii * t
    gap = arb(2).log() - F.real
    assert j < -arb(1) / 10
    assert H < -arb(47) / 1000
    assert gap > arb(47) / 1000
    assert arb(1) / 20 < arg1.real < 1
    assert arb(1) / 20 < arg2.real < 1
    return {
        "precision_bits": ctx.prec,
        "certified_inequalities": 5,
        "J_one_third": str(j),
        "competing_entropy_H_one_third_one_third": str(H),
        "geometric_phase": str(F),
        "endpoint_minus_geometric_rate": str(gap),
        "first_shifted_argument": str(arg1),
        "second_shifted_argument": str(arg2),
    }


def finite_checks():
    mp.mp.dps = 80
    count = 0
    worst = mp.mpf(0)

    def check(a, b):
        nonlocal count, worst
        error = abs(a - b) / max(1, abs(a), abs(b))
        assert error < mp.mpf("1e-65"), error
        count += 1
        worst = max(worst, error)

    def poch(a, q, k):
        return mp.fprod(1 - a * q ** r for r in range(k))

    for N in range(2, 15):
        D = N - 1
        q = mp.exp(mp.pi * 1j / N)
        Q = q * q
        kap = mp.exp(mp.pi * 1j * D * D / (2 * N))
        S = [mp.mpf(1)]
        for k in range(1, N):
            S.append(S[-1] * 2 * mp.sin(mp.pi * k / N))
        M = mp.matrix(N)
        for j in range(N):
            for k in range(j + 1):
                M[j, k] = kap * (-1) ** j * q ** (j * (k + 1)) * S[j] / (S[k] * S[j-k])
        M3 = M ** 3
        x0 = mp.mpf(1) / 6 + 1j * mp.log(2) / (2 * mp.pi)
        points = [
            (x0, x0),
            (mp.mpf("0.19") + mp.mpf("0.08") * 1j,
             mp.mpf("0.27") + mp.mpf("0.13") * 1j),
            (mp.mpf("0.31") - mp.mpf("0.04") * 1j,
             mp.mpf("0.11") + mp.mpf("0.15") * 1j),
        ]
        for x, y in points:
            X, Y = mp.exp(2j * mp.pi * x), mp.exp(2j * mp.pi * y)
            cx = mp.exp(-1j * mp.pi * D * x) * (1 - X ** N) / N
            cy = mp.exp(-1j * mp.pi * D * y) * (1 - Y ** N) / N
            hx = mp.matrix([mp.sin(mp.pi * N * (x - mp.mpf(j) / N))
                            / (N * mp.sin(mp.pi * (x - mp.mpf(j) / N)))
                            for j in range(N)])
            hy = mp.matrix([mp.sin(mp.pi * N * (y - mp.mpf(j) / N))
                            / (N * mp.sin(mp.pi * (y - mp.mpf(j) / N)))
                            for j in range(N)])
            mx = M * hx
            for i in range(N):
                transformed = (cx * kap * (-q) ** i * X ** i
                               * poch(1 / Q, 1 / Q, i)
                               / poch(X, 1 / Q, i + 1))
                check(mx[i], transformed)
            direct_vector = M3 * hy
            direct = sum(hx[i] * direct_vector[D-i] for i in range(N))
            exact_sum = sum(
                X ** i * Y ** j * poch(1 / Q, 1 / Q, i + j)
                / (poch(X, 1 / Q, i + 1) * poch(Y, 1 / Q, j + 1))
                for i in range(N) for j in range(N-i))
            check(direct, kap * cx * cy * exact_sum)
    return {"levels": [2, 14], "decimal_precision": mp.mp.dps,
            "diagnostics": count, "worst_relative_error": str(worst)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default = Path(__file__).resolve().parents[1] / "repro/results/research-traced-three-vertex-endpoint.json"
    parser.add_argument("--output", type=Path, default=default)
    args = parser.parse_args()
    result = {"status": "passed", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scalar_certificates": scalar_certificates(), "finite_identity_checks": finite_checks()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
