#!/usr/bin/env python3
"""Exact common-basis and Gram factorizations for wrapped outer operators."""
import argparse
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-wrapped-operator-factorization.json")
    args = ap.parse_args()
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda z: field.from_sympy(sp.sympify(z))
    checks = []

    @lru_cache(maxsize=None)
    def bar(z):
        return cv(sp.conjugate(field.to_sympy(z)))

    def eye(n):
        return [[one if a == b else zero for b in range(n)] for a in range(n)]

    def tr(a):
        return [list(row) for row in zip(*a)]

    def star(a):
        return [[bar(v) for v in row] for row in tr(a)]

    def mul(a, b):
        return [[sum((x * y for x, y in zip(row, col)), zero)
                 for col in zip(*b)] for row in a]

    def diagonal(values):
        return [[values[a] if a == b else zero for b in range(len(values))]
                for a in range(len(values))]

    def scale(a, z):
        return [[z * v for v in row] for row in a]

    def add(a, b):
        return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]

    def inverse_lower(a):
        out = eye(len(a))
        for k in range(len(a)):
            for j in range(len(a)):
                out[j][k] = ((one if j == k else zero) -
                             sum((a[j][ell] * out[ell][k] for ell in range(j)), zero)) / a[j][j]
        return out

    def check(name, value):
        assert value == zero, (name, field.to_sympy(value))
        checks.append(name)

    def matrix(name, a, b):
        for j, (arow, brow) in enumerate(zip(a, b)):
            for k, (av, bv) in enumerate(zip(arow, brow)):
                check(f"{name} ({j},{k})", av - bv)

    levels = [(2, sp.I), (3, (1 + sp.I * sp.sqrt(3)) / 2),
              (4, (1 + sp.I) / sp.sqrt(2)), (6, (sp.sqrt(3) + sp.I) / 2)]
    for n, qe in levels:
        q, ii = cv(qe), cv(sp.I)
        r, degree = q ** -2, n - 1
        p, sine, polys = [one], [one], [[one]]
        for j in range(1, n):
            p.append(p[-1] * (one - r ** j))
            sine.append(sine[-1] * (q ** j - q ** -j) / ii)
            row = [zero] * (j + 1)
            for k, value in enumerate(polys[-1]):
                row[k] += value
                row[k + 1] -= r ** j * value
            polys.append(row)
        tau = [(-1) ** j * r ** (j * (j + 1) // 2) for j in range(n)]
        d = [sum((r ** (-a * h) / p[a] for a in range(n)), zero) / n for h in range(n)]
        check(f"N{n} exact top weight coefficient", d[-1] - one / (n * n))
        for a in range(n):
            check(f"N{n} original weight interpolation {a}",
                  sum((d[h] * r ** (a * h) for h in range(n)), zero) - one / p[a])
        T = [[polys[a][b] if b <= a else zero for b in range(n)] for a in range(n)]
        for a in range(n):
            for b in range(a + 1):
                check(f"N{n} self-inversive polynomial {a},{b}",
                      polys[a][a - b] - tau[a] * bar(polys[a][b]))
        dm = [[d[b - a] if b >= a else zero for b in range(n)] for a in range(n)]
        dw = [[d[n + b - a] if a > b else zero for b in range(n)] for a in range(n)]
        k0, k1, wrap = ([[zero] * n for _ in range(n)] for _ in range(3))
        for a in range(n):
            for b in range(n):
                product = [zero] * (a + b + 1)
                for j, x in enumerate(polys[a]):
                    for k, y in enumerate(polys[b]):
                        product[j + k] += x * y
                k0[a][b] = product[b] / p[a] ** 2
                k1[a][b] = sum((value * d[b - j] for j, value in enumerate(product)
                               if 0 <= b - j < n), zero) / p[a] ** 3
                wrap[a][b] = sum((value * d[n + b - j] for j, value in enumerate(product)
                                 if 0 <= n + b - j < n), zero) / p[a] ** 3
        for name, actual, middle, power in (("three", k0, eye(n), 2),
                                            ("main four", k1, dm, 3),
                                            ("wrapped four", wrap, dw, 3)):
            expected = mul(diagonal([x ** -power for x in p]),
                           mul(T, mul(middle, mul(star(T), diagonal(tau)))))
            matrix(f"N{n} coefficient factorization {name}", actual, expected)

        S = [[q ** (j * ell) /
              (ii ** j * q ** (-j * (j + 1) // 2) * sine[ell] * sine[j - ell])
              if ell <= j else zero for ell in range(n)] for j in range(n)]
        si = inverse_lower(S)
        V = mul(tr(S), diagonal([x * x for x in p]))
        vi = mul(diagonal([x ** -2 for x in p]), tr(si))
        matrix(f"N{n} common original basis inverse", mul(V, vi), eye(n))
        M = [[(-1) ** j * q ** (j * (ell + 1)) * sine[j] /
              (sine[ell] * sine[j - ell]) if ell <= j else zero
              for ell in range(n)] for j in range(n)]
        mi = [[bar(v) for v in row] for row in M]
        matrix(f"N{n} literal negative crossing", mul(M, mi), eye(n))
        powers = {0: eye(n)}
        for j in range(1, 5):
            powers[j] = mul(powers[j - 1], M)
        original = {
            twist: [[q ** (degree * degree) * powers[twist][degree - a][b]
                     for b in range(n)] for a in range(n)]
            for twist in (3, 4)
        }
        matrix(f"N{n} original three carrier",
               mul(V, k0), scale(mul(original[3], V), one / n))
        matrix(f"N{n} original four carrier",
               mul(V, add(k1, wrap)), scale(mul(original[4], V), one / (n * n)))

        gram_basis = diagonal([sine[a] * tau[a] for a in range(n)])
        gram_inverse = diagonal([one / (sine[a] * tau[a]) for a in range(n)])
        L = mul(diagonal([one / x for x in sine]), T)
        matrix(f"N{n} positive three Gram identity",
               mul(gram_basis, mul(k0, gram_inverse)), mul(L, star(L)))
        for name, actual, middle in (("main", k1, dm), ("wrapped", wrap, dw)):
            matrix(f"N{n} four Gram identity {name}",
                   mul(gram_basis, mul(actual, gram_inverse)),
                   mul(diagonal([one / x for x in p]), mul(L, mul(middle, star(L)))))
        dw_power = eye(n)
        for j in range(1, n + 1):
            dw_power = mul(dw_power, dw)
            if j == n - 1:
                check(f"N{n} nonzero nilpotency minor",
                      dw_power[n - 1][0] - one / n ** (2 * (n - 1)))
        matrix(f"N{n} middle nilpotency", dw_power, [[zero] * n for _ in range(n)])
        for a in range(1, n):
            check(f"N{n} nonzero minor diagonal {a}", dw[a][a - 1] - one / (n * n))

        wrapped_original = scale(mul(V, mul(wrap, vi)), n * n)
        u = [(-q ** -1) ** a for a in range(n)]
        for b in range(n):
            check(f"N{n} original left null direction {b}",
                  sum((u[a] * wrapped_original[a][b] for a in range(n)), zero))
        positive_basis_wrap = mul(M, mul(wrapped_original, mi))
        for b in range(n):
            check(f"N{n} last row in positive-three coordinates {b}",
                  positive_basis_wrap[-1][b])
        delta = [p[a] / sine[a] for a in range(n)]
        fourier = [[q ** (-degree * a + 2 * a * b) / cv(sp.sqrt(n))
                    for b in range(n)] for a in range(n)]
        unitary = [[(-q) ** -b / delta[b] if a + b == degree else zero
                    for b in range(n)] for a in range(n)]
        matrix(f"N{n} centered Fourier unitarity",
               mul(fourier, star(fourier)), eye(n))
        matrix(f"N{n} exact Fourier Gram transport",
               scale(mul(unitary, L), cv(sp.sqrt(n))),
               scale(mul(M, fourier), q ** (degree * degree)))
        R = mul(fourier, mul(dw, star(fourier)))
        for a in range(n):
            for b in range(n):
                if a != b:
                    target = (q ** (-degree * (a - b)) *
                              (one / p[a] - one / p[b]) /
                              (n * (one - q ** (2 * (a - b)))))
                else:
                    target = sum((h * d[h] * r ** (a * h)
                                  for h in range(1, n)), zero) / n
                check(f"N{n} original reciprocal-factorial divided difference {a},{b}",
                      R[a][b] - target)
        matrix(f"N{n} exact Fourier circulant transport",
               mul(fourier, mul(add(dm, dw), star(fourier))),
               diagonal([one / x for x in p]))
        matrix(f"N{n} original positive-coordinate wrapped factorization",
               positive_basis_wrap,
               mul(star(M), mul(diagonal([bar(x) for x in p]), mul(M, R))))
        E = mul(diagonal([bar(x) for x in p]), mul(M, mul(R, mi)))
        for a in range(n):
            for b in range(a + 1):
                check(f"N{n} relative insertion strict upper triangle {a},{b}",
                      E[a][b])
        matrix(f"N{n} original wrapped congruence",
               positive_basis_wrap, mul(star(M), mul(E, M)))
        matrix(f"N{n} complete relative four insertion",
               mul(diagonal([bar(x) for x in p]),
                   mul(M, mul(diagonal([one / x for x in p]), mi))), M)
        kernel = [[mul(mi, mi)[a][0]] for a in range(n)]
        matrix(f"N{n} original right null vector",
               mul(wrapped_original, kernel), [[zero] for _ in range(n)])
        frobenius = sum((v * bar(v) for row in dw for v in row), zero)
        check(f"N{n} exact wrapped Frobenius count",
              frobenius - sum((h * d[h] * bar(d[h]) for h in range(1, n)), zero))
        check(f"N{n} exact root-grid Parseval",
              sum((v * bar(v) for v in d), zero) -
              sum((one / (x * x) for x in sine), zero) / n)
        if n == 2:
            check("N2 wrapped trace is nonzero", wrap[0][0] + wrap[1][1] - one / 32)
        for word in ((3, 4), (4, 3, 4), (3, 4, 3, 4)):
            a, b = eye(n), eye(n)
            for twist in word:
                a = mul(a, original[twist])
                b = mul(b, scale(k0 if twist == 3 else add(k1, wrap), n ** (twist - 2)))
            matrix(f"N{n} original mixed word {word}", mul(a, V), mul(V, b))
        print(f"Exact original level {n}: passed", flush=True)

    deps = [
        "notes/research_mixed_wrapped_operator_factorization.md",
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_mixed_conditional_leg_sum.md",
        "notes/research_mixed_wire_exact_contraction.md",
        "notes/research_positive_three_crossing_cycle.md",
    ]
    out = {
        "status": "passed", "levels": [n for n, _ in levels],
        "exact_identity_count": len(checks), "exact_identities": checks,
        "arithmetic": "Exact Q(i,sqrt(2),sqrt(3))",
        "scope": "Original common-basis, separated Gram, rank, null direction and norm-data identities; no global rate bound.",
        "normalization": "A3/kappa and A4/kappa^2 constructed from the literal M/kappa and kappa^2=q^((N-1)^2).",
        "proof_sha256": sha256((ROOT / deps[0]).read_bytes()).hexdigest(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in deps},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print("PASS", len(checks), "exact identities")


if __name__ == "__main__":
    main()
