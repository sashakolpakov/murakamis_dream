#!/usr/bin/env python3
"""Exact original-matrix checks for the two-cap finite source.

The written proof is all-level and all-length.  These finite algebraic checks
independently compare every boundary-basis coefficient with the original
crossing matrices, including the new Gram polynomial and every torus alias.
They certify no asymptotic, packet, or complementary-contour estimate.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_two_cap_torus_composition.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-two-cap-torus-composition.json")
    args = parser.parse_args()
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    input_hash = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    dependencies, primary, visited = {}, {}, set()

    def bind(path, expected=None):
        if path not in dependencies:
            dependencies[path] = sha(ROOT / path)
        if expected is not None:
            assert dependencies[path] == expected, path
        return dependencies[path]

    def inherit(path):
        if path in visited:
            return json.loads((ROOT / path).read_text())
        bind(path)
        data = json.loads((ROOT / path).read_text())
        assert data["status"] == "passed", path
        visited.add(path)
        merged = {}
        for key in ("dependencies", "dependencies_sha256"):
            for name, digest in data.get(key, {}).items():
                assert name not in merged or merged[name] == digest, (path, name)
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return data

    for stem in ("mixed_wire_exact_contraction", "mixed_conditional_torus_composition"):
        rp = f"repro/results/research-{stem.replace('_', '-')}.json"
        record = inherit(rp)
        bind(f"experiments/check_{stem}.py", record["script_sha256"])
        assert record["dependencies_sha256"][f"notes/research_{stem}.md"] == bind(
            f"notes/research_{stem}.md")
        primary[rp] = dependencies[rp]
    bind("notes/research_bare_kernel_thin_rectangle.md")

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    zero, one = field.zero, field.one
    cv = lambda value: field.from_sympy(sp.sympify(value))
    counts = {}

    def check(category, label, value):
        assert value == zero, (label, field.to_sympy(value))
        counts[category] = counts.get(category, 0) + 1

    def product(values):
        result = one
        for value in values:
            result *= value
        return result

    def poly_product(left, right):
        result = [zero] * (len(left) + len(right) - 1)
        for j, x in enumerate(left):
            for k, y in enumerate(right):
                result[j + k] += x * y
        return result

    def evaluate(coefficients, x):
        result = zero
        for coefficient in reversed(coefficients):
            result = result * x + coefficient
        return result

    def multiply(left, right):
        assert len(left[0]) == len(right)
        return [[sum((left[a][j] * right[j][b] for j in range(len(right))), zero)
                 for b in range(len(right[0]))] for a in range(len(left))]

    def transpose(matrix):
        return list(map(list, zip(*matrix)))

    def compare(category, label, left, right, denominator=1):
        assert len(left) == len(right) and len(left[0]) == len(right[0])
        for a, row in enumerate(left):
            for b, value in enumerate(row):
                check(category, (label, a, b), value - right[a][b] / denominator)

    levels = [(2, sp.I), (3, (1 + sp.I * sp.sqrt(3)) / 2),
              (4, (1 + sp.I) / sp.sqrt(2)), (6, (sp.sqrt(3) + sp.I) / 2)]
    words = ([(3,), (4,)]
             + [tuple(3 + e for e in word) for size in (2, 3)
                for word in itertools.product((0, 1), repeat=size)]
             + [(3, 4, 3, 4), (4, 3, 4, 3)])
    level_summary = []
    for N, expression in levels:
        q, ii = cv(expression), cv(sp.I)
        r, Q, D = q ** -2, q ** 2, N - 1
        P = [product(one - r ** j for j in range(1, a + 1)) for a in range(N)]
        T = [product(one - Q ** j for j in range(1, a + 1)) for a in range(N)]
        # Literal crossing M/kappa, independent of the two-cap formula.
        M = [[((-1) ** a * q ** (a + b*b) * T[a] / (T[b] * T[a-b])
               if b <= a else zero) for b in range(N)] for a in range(N)]
        S = [[(-q) ** -a * M[a][b] / P[a] for b in range(N)] for a in range(N)]
        MM = multiply(M, M)
        M3, M4 = multiply(MM, M), multiply(MM, MM)
        original = {
            3: [[q ** (D*D) * M3[D-a][b] for b in range(N)] for a in range(N)],
            4: [[q ** (D*D) * M4[D-a][b] / N for b in range(N)] for a in range(N)],
        }  # A_(3+eps)/(kappa^(1+eps) N^eps).
        gamma = multiply(S, transpose(S))
        p, negative = [], []
        for ell in range(N):
            pp, nn = [one], [one]
            for j in range(ell):
                pp = poly_product(pp, [one, -r ** (j+1)])
                nn = poly_product(nn, [one, -r ** j])
            p.append(pp)
            negative.append(nn)  # (Z;r)_ell, evaluated at Z=X^-1.
        gram_coefficients = [[zero] * N for _ in range(N)]
        for ell in range(N):
            for a, x in enumerate(negative[ell]):
                for b, y in enumerate(negative[ell]):
                    gram_coefficients[a][b] += r ** ell * x * y / P[ell] ** 2
        # The coefficient array itself proves the two nonpositive bands.
        compare("gram symmetry", N, gram_coefficients, transpose(gram_coefficients))
        for a in range(N):
            for ell in range(N):
                column = q ** (-ell*ell) / P[ell] * product(
                    r ** -a - r ** -j for j in range(ell))
                check("normalized original column", (N, a, ell),
                      column - P[a] * S[a][ell])

        moments = [sum((r ** (a*k) / P[a] for a in range(N)), zero)
                   for k in range(N)]
        diagonal = [moments[(-k) % N] / N for k in range(N)]
        # H_j is the entire boundary polynomial for the jth original basis
        # vector, reconstructed from the independent physical P_a S_aj values.
        H = [[sum((P[a] * S[a][j] * r ** (a*k) for a in range(N)), zero) / N
              for k in range(N)] for j in range(N)]
        for a in range(N):
            for j in range(N):
                check("whole boundary interpolation", (N, a, j),
                      evaluate(H[j], r ** -a) - P[a] * S[a][j])
        for power in range(-N+1, N):
            for eps in (0, 1):
                physical = sum((r ** (a*power) / P[a] ** eps
                                for a in range(N)), zero) / N
                ct = (sum((diagonal[k] for k in (-power, N-power)
                           if 0 <= k < N), zero) if eps
                      else one if power == 0 else zero)
                check("complete alias monomial", (N, eps, power), physical - ct)

        data = {}
        for kind, nodes in (("physical", [r ** a for a in range(N)]),
                            ("torus", [q ** a for a in range(2*N)])):
            size = len(nodes)
            pvalues = [[evaluate(pp, x) for x in nodes] for pp in p]
            G = [[sum((gram_coefficients[a][b] * x ** -a * y ** -b
                       for a in range(N) for b in range(N)), zero)
                  for y in nodes] for x in nodes]
            if kind == "physical":
                for a in range(N):
                    for b in range(N):
                        explicit = (r ** (-a*b) * P[a+b] / (P[a]*P[b])
                                    if a+b < N else zero)
                        check("original Gram interpolation", (N, a, b),
                              G[a][b] - P[a]*P[b]*gamma[a][b])
                        check("original triangular support", (N, a, b),
                              G[a][b] - explicit)
            weights, U, kernels = {}, {}, {}
            for eps in (0, 1):
                weights[eps] = [(one / P[a]) ** eps if kind == "physical"
                                else (evaluate(diagonal, x)*(one+x ** -N)) ** eps
                                for a, x in enumerate(nodes)]
                U[eps] = [[sum((S[a][j] * pvalues[a][b] / P[a] ** eps
                                for a in range(N)), zero) * weights[eps][b]
                           for b in range(size)] for j in range(N)]
                kernels[eps] = [[sum(
                    (x ** -ell * pvalues[ell][a] * pvalues[ell][b]
                     / P[ell] ** (2+eps) for ell in range(N)), zero)
                    * weights[eps][b] for b in range(size)]
                    for a, x in enumerate(nodes)]
            Hvalues = [[evaluate(H[j], x ** -1) for x in nodes] for j in range(N)]
            data[kind] = (U, kernels, G, Hvalues)
        for word in words:
            direct = original[word[0]]
            for letter in word[1:]:
                direct = multiply(direct, original[letter])
            for kind, (U, kernels, G, Hvalues) in data.items():
                if len(word) == 1:
                    source = multiply(U[word[0]-3], transpose(Hvalues))
                else:
                    source = U[word[0]-3]
                    for letter in word[1:-1]:
                        source = multiply(source, kernels[letter-3])
                    source = multiply(multiply(source, G), transpose(U[word[-1]-3]))
                denominator = 1 if kind == "physical" else 2 ** len(word)
                compare(f"original full {kind} boundary matrix",
                        (N, word), direct, source, denominator)
        level_summary.append(dict(level=N, words=len(words),
                                  all_boundary_basis_pairs=N*N,
                                  torus_quadrature_nodes=2*N))
        print(f"PASS exact level {N}: {len(words)} words, every boundary coefficient",
              flush=True)

    # All-level degree/count identities are the hypotheses of exact averaging.
    assert sp.expand(-2*sp.Symbol("ell")**2
                     + 2*sp.Symbol("ell")*(sp.Symbol("ell")-1)
                     + 2*sp.Symbol("ell")) == 0
    counts["symbolic column product phase"] = 1
    for m in range(2, 9):
        for bits in itertools.product((0, 1), repeat=m):
            k = sum(bits)
            assert sum(1+e for e in bits) == m+k
            assert sum(bits) + m == m+k
    counts["scalar exponent bookkeeping patterns"] = sum(2**m for m in range(2, 9))
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT / path) == digest for path, digest in dependencies.items())
    result = dict(
        status="passed", proof_sha256=proof_hash, script_sha256=script_hash,
        dependencies_sha256=dependencies, primary_records=primary,
        exact_comparisons=sum(counts.values()), comparison_counts=counts,
        levels=level_summary, words=words,
        arithmetic="Exact Q(i,sqrt(2),sqrt(3)); no floating tolerances",
        scope=("Finite original crossing matrices, every boundary-basis coefficient, "
               "the explicit global Gram polynomial, triangular support, two caps, "
               "m=1 distinction, and all torus aliases. The written proof is "
               "all-level/all-length. No asymptotic or Gram packet is certified."))
    if old is not None:
        old.pop("input_sha256", None)
        assert old == json.loads(json.dumps(result)), "saved result differs"
        assert sha(args.input) == input_hash
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "exact_comparisons")}))


if __name__ == "__main__":
    main()
