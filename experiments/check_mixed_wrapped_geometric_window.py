#!/usr/bin/env python3
"""Exact finite entries for the original relative wrapped insertion."""
import argparse
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_wrapped_geometric_window.md"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-wrapped-geometric-window.json")
    args = ap.parse_args()
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda x: field.from_sympy(sp.sympify(x))
    checks = []

    @lru_cache(maxsize=None)
    def bar(x):
        return cv(sp.conjugate(field.to_sympy(x)))

    def identity(n):
        return [[one if a == b else zero for b in range(n)] for a in range(n)]

    def diagonal(values):
        return [[values[a] if a == b else zero for b in range(len(values))]
                for a in range(len(values))]

    def multiply(a, b):
        return [[sum((x*y for x, y in zip(row, col)), zero)
                 for col in zip(*b)] for row in a]

    def star(a):
        return [[bar(x) for x in col] for col in zip(*a)]

    def inverse(a):
        n = len(a)
        out = identity(n)
        for col in range(n):
            for row in range(n):
                out[row][col] = ((one if row == col else zero) -
                    sum((a[row][j]*out[j][col] for j in range(row)), zero)) / a[row][row]
        return out

    def test(name, value):
        assert value == zero, (name, field.to_sympy(value))
        checks.append(name)

    def matrix(name, a, b):
        for row in range(len(a)):
            for col in range(len(a[row])):
                test(f"{name} {row},{col}", a[row][col]-b[row][col])

    levels = [(2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
              (4, (1+sp.I)/sp.sqrt(2)), (6, (sp.sqrt(3)+sp.I)/2)]
    for n, qe in levels:
        q, imaginary = cv(qe), cv(sp.I)
        r, D = q**-2, n-1
        p, sine, polys = [one], [one], [[one]]
        for a in range(1, n):
            p.append(p[-1]*(one-r**a))
            sine.append(sine[-1]*(q**a-q**-a)/imaginary)
            row = [zero]*(a+1)
            for b, value in enumerate(polys[-1]):
                row[b] += value
                row[b+1] -= r**a*value
            polys.append(row)
        d = [sum((r**(-a*h)/p[a] for a in range(n)), zero)/n
             for h in range(n)]
        c = [zero] + [d[n-k] for k in range(1, n)]
        test(f"N{n} first forced coefficient", c[1]-one/(n*n))
        for k in range(1, n-1):
            test(f"N{n} original forced recurrence {k}",
                 c[k+1]-(one-r**k)*c[k]-one/(n*n))
        for k in range(1, n):
            test(f"N{n} forced prefix {k}",
                 c[k]-p[k-1]*sum((one/p[j] for j in range(k)), zero)/(n*n))
        T = [[polys[a][b] if b <= a else zero for b in range(n)] for a in range(n)]
        Ti = inverse(T)
        shift = [[one if a == b+1 else zero for b in range(n)] for a in range(n)]
        K = [[-r**(b+1) if a > b else zero for b in range(n)] for a in range(n)]
        matrix(f"N{n} backward shift conjugation", multiply(T, multiply(shift, Ti)), K)
        L = multiply(diagonal([one/x for x in sine]), T)
        Li = inverse(L)
        delta = [p[a]/sine[a] for a in range(n)]
        U = [[(-q)**-b/delta[b] if a+b == D else zero for b in range(n)] for a in range(n)]
        dw = [[c[a-b] if a > b else zero for b in range(n)] for a in range(n)]
        E = multiply(diagonal([bar(x) for x in p]),
                     multiply(U, multiply(L, multiply(dw, multiply(Li, star(U))))))
        # Independently form the same insertion in the original crossing basis.
        M = [[(-1)**a*q**(a*(b+1))*sine[a]/(sine[b]*sine[a-b])
              if b <= a else zero for b in range(n)] for a in range(n)]
        Mi = [[bar(x) for x in row] for row in M]
        F = [[q**(-D*a+2*a*b)/cv(sp.sqrt(n)) for b in range(n)] for a in range(n)]
        R = multiply(F, multiply(dw, star(F)))
        original = multiply(diagonal([bar(x) for x in p]), multiply(M, multiply(R, Mi)))
        matrix(f"N{n} original crossing relative insertion", E, original)
        for k in range(n):
            test(f"N{n} original complete column chirp {k}",
                 sum(((-q)**j*M[j][k] for j in range(n)), zero) -
                 (q**(-D*D) if k == D else zero))
        for i in range(n-1):
            for k in range(n):
                target = ((-1)**(i+1)*q**(-i-2)*M[i+1][k+1]
                          if k <= i else zero)
                test(f"N{n} original truncated column chirp {i},{k}",
                     sum(((-q)**j*M[j][k] for j in range(i+1)), zero)-target)
        constant_dw = [[one/(n*n) if a > b else zero for b in range(n)] for a in range(n)]
        constant_E = multiply(diagonal([bar(x) for x in p]),
            multiply(U, multiply(L, multiply(constant_dw, multiply(Li, star(U))))))
        for i in range(n):
            for j in range(n):
                if i >= j:
                    test(f"N{n} strict upper support {i},{j}", E[i][j])
                    continue
                width = j-i
                total = sum(((-1)**h*r**((1-j)*h+h*(h-1)//2) *
                    p[width-1]/(p[h]*p[width-1-h])*c[h+1]
                    for h in range(width)), zero)
                target = -(-q)**-width*r**-j*bar(p[i]**2/p[j])*total
                test(f"N{n} full finite entry {i},{j}", E[i][j]-target)
                prefix = sum((p[width-1]*p[j-1-ell] /
                    (p[width-1-ell]*p[j-1]) for ell in range(width)), zero)
                prefix_entry = (-q)**(-width)*bar(p[i])*prefix / (n*n*(one-r**j))
                test(f"N{n} full finite prefix reduction {i},{j}", E[i][j]-prefix_entry)
                for ell in range(width-1):
                    ratio = ((one-r**(width-1-ell)) /
                             (one-r**(j-1-ell)))
                    sine_ratio = (q**i*(q**(width-1-ell)-q**(-width+1+ell)) /
                                  (q**(j-1-ell)-q**(-j+1+ell)))
                    test(f"N{n} geometric prefix ratio {i},{j},{ell}",
                         ratio-sine_ratio)
                leading = (-q)**-width*bar(p[i])/(n*n*(one-r**j))
                test(f"N{n} exact constant-coefficient reduction {i},{j}",
                     constant_E[i][j]-leading)
                if width == 1:
                    superdiagonal = (imaginary*q**i*bar(p[i]) /
                                     (n*n*(q**(i+1)-q**(-i-1))/imaginary))
                    test(f"N{n} original first superdiagonal {i}", E[i][j]-superdiagonal)
        print(f"N={n}: exact finite entries passed", flush=True)

    inherited = ROOT / "repro/results/research-mixed-wrapped-operator-factorization.json"
    record = json.loads(inherited.read_text())
    assert record["status"] == "passed"
    assert record["proof_sha256"] == sha256((ROOT /
        "notes/research_mixed_wrapped_operator_factorization.md").read_bytes()).hexdigest()
    assert record["script_sha256"] == sha256((ROOT /
        "experiments/check_mixed_wrapped_operator_factorization.py").read_bytes()).hexdigest()
    for name, digest in record["dependencies_sha256"].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    paths = [
        "notes/research_mixed_wrapped_geometric_window.md",
        "notes/research_mixed_wrapped_operator_factorization.md",
        "experiments/check_mixed_wrapped_operator_factorization.py",
        "repro/results/research-mixed-wrapped-operator-factorization.json",
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_positive_three_crossing_cycle.md",
    ]
    result = {
        "status": "passed", "levels": [n for n, _ in levels],
        "arithmetic": "Exact Q(i,sqrt(2),sqrt(3))",
        "exact_identity_count": len(checks), "exact_identities": checks,
        "scope": "Exact full relative-wrap entries and fixed-band normalization; the shrinking-window norm rate is proved analytically, not inferred from finite norms. No coherent original-word estimate.",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_sha256": sha256(PROOF.read_bytes()).hexdigest(),
        "dependencies_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact identities")


if __name__ == "__main__":
    main()
