#!/usr/bin/env python3
"""Exact finite-field checks of full integer-power interpolation and folding.

These finite examples test the original Newton crossing polynomial by
independent monic division, including negative powers. They compare it
with value/normal Fourier inversion and the midpoint formula. They do
not prove the analytic interpolation, saddle estimates or volume theorem.
Only Python's standard library is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path

PAPER = Path(__file__).resolve().parent
ROOT = PAPER.parents[1]
INPUTS = [
    "papers/conway-asymptotics/main.tex",
    "papers/conway-asymptotics/factorial.tex",
    "papers/conway-asymptotics/leaf.tex",
    "papers/conway-asymptotics/packet.tex",
    "papers/conway-asymptotics/pure-window.tex",
    "papers/conway-asymptotics/filling.tex",
    "papers/conway-asymptotics/figures/two-lattices.tex",
    "papers/conway-asymptotics/check.py",
    "papers/newton-tangles/main.tex",
    "papers/filling-bounds/main.tex",
    "papers/oscillatory-fillings/main.tex",
    "papers/strict-newton-profiles/main.tex",
    "papers/strict-newton-profiles/syntax.tex",
    "papers/strict-newton-profiles/variation.tex",
    "papers/conway-source-bounds/main.tex",
    "papers/conway-source-bounds/assembly.tex",
    "papers/strict-conway-geometry/main.tex",
    "papers/strict-conway-geometry/deformation.tex",
    "papers/strict-conway-geometry/fillings.tex",
]


def hashes():
    return {s: hashlib.sha256((ROOT / s).read_bytes()).hexdigest()
            for s in INPUTS}


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def prime_roots(order):
    result = []
    k = 1
    while len(result) < 2:
        p = k * order + 1
        if prime(p):
            for a in range(2, p):
                g = pow(a, k, p)
                if pow(g, order, p) == 1 and all(
                        pow(g, j, p) != 1 for j in range(1, order)):
                    result.append((p, g))
                    break
        k += 1
    return result


class Polys:
    def __init__(self, p):
        self.p = p

    def trim(self, a):
        a = [x % self.p for x in a]
        while a and a[-1] == 0:
            a.pop()
        return a

    def add(self, a, b):
        c = [0] * max(len(a), len(b))
        for i, v in enumerate(a):
            c[i] += v
        for i, v in enumerate(b):
            c[i] += v
        return self.trim(c)

    def scale(self, a, t):
        return self.trim([t*x for x in a])

    def sub(self, a, b):
        return self.add(a, self.scale(b, -1))

    def mul(self, a, b):
        if not a or not b:
            return []
        c = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] += x*y
        return self.trim(c)

    def divmod(self, a, b):
        a = self.trim(a[:])
        assert b
        q = [0] * max(0, len(a)-len(b)+1)
        while len(a) >= len(b):
            k = len(a)-len(b)
            v = a[-1]*pow(b[-1], -1, self.p) % self.p
            q[k] = v
            a = self.sub(a, [0]*k + self.scale(b, v))
        return self.trim(q), a

    def inverse(self, a, mod):
        r0, r1, t0, t1 = mod[:], a[:], [], [1]
        while r1:
            q, r = self.divmod(r0, r1)
            r0, r1 = r1, r
            t0, t1 = t1, self.sub(t0, self.mul(q, t1))
        assert len(r0) == 1
        answer = self.scale(t0, pow(r0[0], -1, self.p))
        return self.divmod(answer, mod)[1]

    def power(self, a, n, mod):
        if n < 0:
            a, n = self.inverse(a, mod), -n
        out = [1]
        while n:
            if n % 2:
                out = self.divmod(self.mul(out, a), mod)[1]
            a = self.divmod(self.mul(a, a), mod)[1]
            n //= 2
        return out

    def value(self, a, x):
        y = 0
        for c in reversed(a):
            y = (y*x+c) % self.p
        return y

    def derivative(self, a):
        return self.trim([j*a[j] for j in range(1, len(a))])


def level_check(N, p, g):
    R = Polys(p)
    d = N-1
    q = pow(g, 4, p)  # g has exact order 8N.
    invN = pow(N, -1, p)
    inv2 = pow(2, -1, p)
    w = [pow(q, 2*k+1, p) for k in range(N)]
    c = [(z+pow(z, -1, p)) % p for z in w]
    mod = [1]
    for z in c:
        mod = R.mul(mod, [-z, 1])
    # Actual normalized Newton crossing, not constructed from Hermite data.
    e = [1]
    r = []
    for j in range(N):
        r = R.add(r, R.scale(e, pow(-q % p, j, p)))
        if j < d:
            sine_square = -(pow(q, j+1, p)-pow(q, -(j+1), p))**2 % p
            assert sine_square
            e = R.scale(R.mul(e, [c[j], -1]),
                        pow(sine_square, -1, p))
    # Independent ordinary Chebyshev recurrence.
    U = [[1], [0, 1]]
    for j in range(2, N+1):
        U.append(R.sub(R.mul([0, 1], U[-1]), U[-2]))
    circles = [R.scale(U[j], (-1)**j) for j in range(N)]
    cases = []
    for n in (-3, -2, -1, 0, 1, 2, 3):
        physical = R.power(r, n, mod)
        values = [pow((-1)**k * pow(q, k*(k+1), p) % p, n, p)
                  for k in range(N)]
        normals = [-n*inv2*(d-2*k)*values[k] % p for k in range(N)]
        deriv = R.derivative(physical)
        for k in range(N):
            assert R.value(physical, c[k]) == values[k]
            angular = (w[k]-pow(w[k], -1, p))*R.value(deriv, c[k]) % p
            assert angular == normals[k]
        H = [sum(values[k]*pow(w[k], -a, p) for k in range(N))*invN % p
             for a in range(N)]
        D = [sum(normals[k]*pow(w[k], -a, p) for k in range(N))*invN % p
             for a in range(N)]
        coeff = [H[0]] + [(D[a]+(N-a)*H[a])*invN % p
                          for a in range(1, N)] + [0, 0]
        beta = [(-1)**j*(coeff[j]-coeff[j+2]) % p for j in range(N)]
        rebuilt = []
        for b, circle in zip(beta, circles):
            rebuilt = R.add(rebuilt, R.scale(circle, b))
        assert rebuilt == physical
        # Three explicit even corridor samples; each tested linearly, not
        # reconstructed from the midpoint right side.
        cutoff = N//4
        for example in range(3):
            C = [(h+1)**(example+1) + example for h in range(cutoff+1)]
            lhs = sum(beta[d-h]*C[h] for h in range(cutoff+1)) % p
            rhs = 0
            for k in range(N):
                a = 2*k+1-N
                u = -w[k] % p  # exp(2 pi i z_k)
                chirp = pow(g, n*a*a, p)
                sinh = (u-pow(u, -1, p))*inv2 % p
                cosh = (u+pow(u, -1, p))*inv2 % p
                for h in range(-cutoff, cutoff+1):
                    rhs += chirp*pow(u, h, p)*C[abs(h)] * (
                        (n*a*inv2+h)*sinh+cosh)
            rhs = (rhs * (-1)**d * pow(g, -n*d*d, p) * invN**2) % p
            assert lhs == rhs, (N, p, n, example, lhs, rhs)
        cases.append({"power": n, "normal_nodes": N, "folded_tests": 3})
    return {"level": N, "prime": p, "root_order": 8*N,
            "powers": cases, "odd_simple_node": bool(N % 2)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PAPER / "build" / "check")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    record = output / "summary.json"
    record.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Run without -O: assertions are part of the checks")
    before = hashes()
    results = [level_check(N, p, g) for N in range(2, 13)
               for p, g in prime_roots(8*N)]
    after = hashes()
    if before != after:
        raise RuntimeError("An input changed during verification")
    summary = {
        "verified": True,
        "arithmetic": "exact finite fields, two primes per level",
        "levels": list(range(2, 13)),
        "level_prime_cases": len(results),
        "integer_power_cases": 7*len(results),
        "midpoint_cases": 21*len(results),
        "scope": [
            "original normalized Newton polynomial vs monic powers and inverse",
            "values and first angular normals including parity endpoints",
            "full Fourier-Hermite inversion and ordinary-circle decomposition",
            "folded midpoint derivative including odd signed powers and h=0",
        ],
        "excluded": [
            "all-level proofs from finite samples",
            "complex factorial asymptotics or analytic continuation",
            "wire saddle and whole-charge estimates",
            "nonzero invariant asymptotic and hyperbolic volume identification",
        ],
        "input_hashes": before,
        "records": results,
    }
    record.write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: summary[k] for k in
                      ("verified", "level_prime_cases", "integer_power_cases",
                       "midpoint_cases")}, indent=2))
    print(record)


if __name__ == "__main__":
    main()
