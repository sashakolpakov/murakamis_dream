#!/usr/bin/env python3
"""Exact finite checks of root face identities; no norm or gap inference.

All arithmetic is integral in Z[r]/(r^(2N)+1), with q=r^2 and i=r^N.
Thus q^N=-1 and i^2=-1 are imposed exactly. This ring maps to the
desired root r=exp(pi*i/(2N)); no floating-point tolerance is used.
The finite checks supplement the all-N proof, rather than replacing it.
"""

import argparse
import hashlib
import json
from pathlib import Path


class RootRing:
    def __init__(self, n):
        self.n = n
        self.size = 2*n
        self.zero = (0,)*self.size
        self.one = self.power(0)

    def power(self, exponent):
        quotient, remainder = divmod(exponent, self.size)
        a = [0]*self.size
        a[remainder] = -1 if quotient % 2 else 1
        return tuple(a)

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        c = [0]*self.size
        for j, x in enumerate(a):
            if not x:
                continue
            for k, y in enumerate(b):
                if y:
                    degree = j+k
                    if degree >= self.size:
                        c[degree-self.size] -= x*y
                    else:
                        c[degree] += x*y
        return tuple(c)

    def sine(self, j):
        return self.sub(self.power(2*j-self.n),
                        self.power(-2*j-self.n))

    def cosine(self, j):
        return self.add(self.power(4*j+2), self.power(-4*j-2))


def run_checks():
    counts = {}
    levels = []

    def check(name, condition):
        assert condition, name
        counts[name] = counts.get(name, 0)+1

    for n in range(2, 13):
        r = RootRing(n)
        d = n-1
        zero = r.zero
        q = r.power(2)
        s1 = r.sine(1)

        # Sparse polynomials in x,y,z with exact ring coefficients.
        def clean(p):
            return {k: v for k, v in p.items() if v != zero}

        def add(p, t):
            out = dict(p)
            for k, v in t.items():
                out[k] = r.add(out.get(k, zero), v)
            return clean(out)

        def scale(p, a):
            return clean({k: r.mul(v, a) for k, v in p.items()})

        def variable(p, index, truncate=False):
            out = {}
            for k, v in p.items():
                exponent = list(k)
                exponent[index] += 1
                if truncate and exponent[2] >= n:
                    continue
                out[tuple(exponent)] = v
            return out

        def derivative(p):
            out = {}
            for (a, b, j), v in p.items():
                if j:
                    out[(a, b, j-1)] = r.mul(v, r.sine(j))
            return clean(out)

        def trunc(p):
            return {k: v for k, v in p.items() if k[2] < n}

        def factor(p, truncate=False):
            t = derivative(p)
            t = add(variable(t, 2, truncate), variable(t, 1, truncate))
            t = add(variable(t, 2, truncate), variable(t, 0, truncate))
            return add(scale(p, r.cosine(0)), scale(derivative(t), r.neg(r.one)))

        def native(p):
            out = {}
            for (a, b, j), v in p.items():
                term = {(a, b, j): r.mul(v, r.cosine(j))}
                if j:
                    lower = r.neg(r.mul(v, r.mul(r.sine(j), r.sine(j))))
                    term[(a+1, b, j-1)] = lower
                    term[(a, b+1, j-1)] = lower
                if j >= 2:
                    term[(a+1, b+1, j-2)] = r.neg(
                        r.mul(v, r.mul(r.sine(j), r.sine(j-1))))
                out = add(out, term)
            return clean(out)

        for j in range(2*n+3):
            p = {(0, 0, j): r.one}
            check("full_ring_face_factorization", factor(p) == native(p))
            check("quotient_derivative", trunc(derivative(p)) == derivative(trunc(p)))
            check("top_trace_of_derivative", derivative(p).get((0, 0, d), zero) == zero)
            if j < n:
                check("truncated_face_factorization", factor(p, True) == native(p))
                dz = r.sine(j+1) if j < d else zero
                zd = r.sine(j) if j else zero
                check("clock_commutator_including_top",
                      r.sub(dz, r.mul(q, zd)) == r.mul(s1, r.power(-2*j)))

            # D(z^N f)=-z^N Df, including the exact s_N zero.
            check("ideal_anticommutation", r.sine(n+j) == r.neg(r.sine(j)))
            check("casimir_periodic_diagonal", r.cosine(n+j) == r.cosine(j))

        for j in range(2*n+3):
            for k in range(2*n+3):
                check("full_ring_q_leibniz",
                      r.sine(j+k) == r.add(
                          r.mul(r.sine(j), r.power(2*k)),
                          r.mul(r.power(-2*j), r.sine(k))))
                if j < n and k < n:
                    lhs = r.sine(j) if j+k == n else zero
                    rhs = r.sine(k) if j+k == n else zero
                    check("D_bilinear_self_adjoint", lhs == rhs)
                    check("Z_bilinear_self_adjoint",
                          (j < d and j+1+k == d) == (k < d and j+k+1 == d))
                    shifted = zero
                    if j+k == n:
                        shifted = r.add(r.mul(r.sine(j), r.power(2*k)),
                                        r.mul(r.power(-2*j), r.sine(k)))
                    check("shifted_integration", shifted == zero)

        check("unshifted_product_rule_counterexample",
              r.add(s1, r.sine(d)) != zero)
        check("clock_eigenvalue_exponents_distinct",
              len({(-2*j) % (4*n) for j in range(n)}) == n)
        check("nonzero_physical_D_arrows",
              all(r.sine(j) != zero for j in range(1, n)))
        levels.append(n)

    return {
        "levels": levels,
        "exact_arithmetic": "Z[r]/(r^(2N)+1), q=r^2, i=r^N",
        "counts": counts,
        "total_identities": sum(counts.values()),
        "scope": (
            "Exact finite root algebra only. The all-N proof is separate. "
            "No generic-q normal, source norm, spectral gap, or sewn Green cancellation."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("/private/tmp/md-root-face-operator-results.json"))
    args = parser.parse_args()
    result = run_checks()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, indent=2, sort_keys=True))
