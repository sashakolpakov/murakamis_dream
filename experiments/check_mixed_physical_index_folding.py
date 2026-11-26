#!/usr/bin/env python3
"""Exact original conditional folding, Fourier remainders and cyclic scalars."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_physical_index_folding.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-physical-index-folding.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    specs = [("mixed_conditional_leg_sum", "check"),
             ("mixed_conditional_torus_composition", "check")]
    deps = {}
    for stem, prefix in specs:
        pp = f"notes/research_{stem}.md"
        ss = f"experiments/{prefix}_{stem}.py"
        rr = f"repro/results/research-{stem.replace('_', '-')}.json"
        for p in (pp, ss, rr):
            deps[p] = sha(ROOT/p)
        rec = json.loads((ROOT/rr).read_text())
        assert rec["status"] == "passed" and rec["script_sha256"] == deps[ss]
        inherited = rec.get("dependencies_sha256", rec.get("dependencies", {}))
        assert rec.get("proof_sha256", inherited.get(pp)) == deps[pp]
        for key in ("dependencies", "dependencies_sha256"):
            assert all(sha(ROOT/p) == h for p, h in rec.get(key, {}).items())

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    one, zero = field.one, field.zero
    cv = lambda x: field.from_sympy(sp.sympify(x))
    conj = lambda x: cv(sp.conjugate(field.to_sympy(x)))
    identities = []

    def check(name, value):
        assert value == zero, (name, field.to_sympy(value))
        identities.append(name)

    def product(values):
        ans = one
        for value in values:
            ans *= value
        return ans

    def matmul(A, B):
        return [[sum((A[a][j]*B[j][b] for j in range(len(B))), zero)
                 for b in range(len(B[0]))] for a in range(len(A))]

    def adjoint(A):
        return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]

    def polyprod(A, B):
        result = [zero]*(len(A)+len(B)-1)
        for a, av in enumerate(A):
            for b, bv in enumerate(B):
                result[a+b] += av*bv
        return result

    def evalpoly(A, x):
        result = zero
        for v in reversed(A):
            result = result*x+v
        return result

    words = [(3,), (4,), (3, 4), (3, 4, 3), (3, 3, 3)]
    obstruction = None
    for N, qs in [(2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
                  (4, (1+sp.I)/sp.sqrt(2)), (6, (sp.sqrt(3)+sp.I)/2)]:
        q, D = cv(qs), N-1
        r = q**-2
        P = [product(1-r**j for j in range(1, a+1)) for a in range(N)]
        check(f"N{N} full factorial", P[D]-N)
        B, polynomials = [], []
        for a in range(N):
            pp = [one]
            for j in range(1, a+1):
                pp = polyprod(pp, [one, -r**j])
            polynomials.append(pp)
            B.append(pp+[zero]*(D-a))
            check(f"N{N} physical factorial reflection {a}", P[D-a]*conj(P[a])-N)
        values = [[evalpoly(polynomials[j], r**a) for a in range(N)] for j in range(N)]
        binom = [[P[a]/(P[j]*P[a-j]) if j <= a else zero for j in range(N)] for a in range(N)]
        for a, j in itertools.product(range(N), repeat=2):
            reflected = (-1)**j*r**(-a*j+j*(j-1)//2)*P[a]/P[a-j] if j <= a else zero
            check(f"N{N} reflected zero/support a{a} j{j}", values[j][D-a]-reflected)
            check(f"N{N} coefficient a{a} j{j}", B[a][j]-(-1)**j*r**(j*(j+1)//2)*binom[a][j])
            check(f"N{N} binomial conjugation a{a} j{j}", conj(binom[a][j])-r**(-j*(a-j))*binom[a][j])

        C, folded = [], {}
        for eps in (0, 1):
            CC = [[sum((r**(-a*j)*values[j][a]*values[j][b]/P[j]**(2+eps)
                        for j in range(N)), zero) for b in range(N)] for a in range(N)]
            C.append(CC)
            for a, b in itertools.product(range(N), repeat=2):
                c10 = sum((B[a][j]*values[j][b]/P[j]**(1+eps) for j in range(N)), zero)
                c01 = sum((conj(values[j][a])*conj(binom[b][j])/P[j]**(1+eps) for j in range(N)), zero)
                c11 = sum((B[a][j]*conj(B[b][j])/P[j]**eps for j in range(N)), zero)
                check(f"N{N} left fold eps{eps} a{a} b{b}", c10-CC[D-a][b])
                check(f"N{N} right fold eps{eps} a{a} b{b}", c01-CC[a][D-b])
                check(f"N{N} double fold eps{eps} a{a} b{b}", c11-CC[D-a][D-b])
                for mask, val in [((0, 0), CC[a][b]), ((1, 0), c10), ((0, 1), c01), ((1, 1), c11)]:
                    folded[(eps, *mask, a, b)] = val
                if eps == 0:
                    check(f"N{N} exact three scalar reflection a{a} b{b}",
                          c11-P[a]*conj(P[b])*conj(CC[a][b])/N)

        FF = [[r**(j*k)/cv(sp.sqrt(N)) for k in range(N)] for j in range(N)]
        FFstar, BBstar = adjoint(FF), adjoint(B)
        unitary = matmul(FF, FFstar)
        for a, b in itertools.product(range(N), repeat=2):
            check(f"N{N} Fourier unitary a{a} b{b}", unitary[a][b]-(one if a == b else zero))
        for eps in (0, 1):
            diag = [[one/P[a]**eps if a == b else zero for b in range(N)] for a in range(N)]
            diagbar = [[conj(v) for v in row] for row in diag]
            rotated = matmul(matmul(FF, diagbar), FFstar)
            physical = matmul(matmul(B, diag), BBstar)
            candidate = matmul(matmul(B, rotated), BBstar)
            for a, b in itertools.product(range(N), repeat=2):
                check(f"N{N} reflected coefficient Gram eps{eps} a{a} b{b}", physical[a][b]-C[eps][D-a][D-b])
                check(f"N{N} Fourier reflection remainder eps{eps} a{a} b{b}",
                      candidate[a][b]-P[a]*conj(P[b])*conj(C[eps][a][b])/N)
            if eps:
                middle = [[diag[a][b]-rotated[a][b] for b in range(N)] for a in range(N)]
                assert any(v != zero for row in middle for v in row)
                for a in range(N):
                    check(f"N{N} equal Fourier diagonal a{a}", rotated[a][a]-rotated[0][0])
                check(f"N{N} diagonal norm lower comparison", middle[0][0]-middle[D][D]-(one-one/N))

        dc = [sum((r**(-k*a)/P[a] for a in range(N)), zero)/N for k in range(N)]
        fc = [sum((P[a]*r**(-k*a) for a in range(N)), zero)/N for k in range(N)]
        for k in range(N):
            check(f"N{N} exact reflected weight coefficient k{k}", dc[k]*r**(-k)-conj(fc[k])/N)
        for a in range(N):
            check(f"N{N} d physical value a{a}", evalpoly(dc, r**a)-one/P[a])
            check(f"N{N} f physical value a{a}", evalpoly(fc, r**a)-P[a])
        for xx in (cv(2), cv(1+sp.I)):
            reflected_d = evalpoly(dc, r**-1/xx)
            fsharp = sum((conj(fc[k])*xx**(-k) for k in range(N)), zero)
            check(f"N{N} global reflected d and alias X{field.to_sympy(xx)}", reflected_d*(1+xx**N)-fsharp*(1+xx**N)/N)
        cyclic_inverse = [zero]*N
        for a, b in itertools.product(range(N), repeat=2):
            cyclic_inverse[(a+b) % N] += fc[a]*dc[b]
        for k in range(N):
            check(f"N{N} exact projected inverse k{k}", cyclic_inverse[k]-(one if k == 0 else zero))

        # Literal original normalized crossings, using the original conditional-source normalization.
        Q = q*q
        productQ = [product(1-Q**h for h in range(1, a+1)) for a in range(N)]
        M = [[(-1)**a*q**(a+b*b)*productQ[a]/(productQ[b]*productQ[a-b]) if b <= a else zero
              for b in range(N)] for a in range(N)]
        M2 = matmul(M, M)
        M3 = matmul(M2, M)
        M4 = matmul(M3, M)
        original = {3: [[q**(D*D)*M3[D-a][b] for b in range(N)] for a in range(N)],
                    4: [[q**(D*D)*M4[D-a][b]/N for b in range(N)] for a in range(N)]}
        orbits = [(a, flag) for a in range(D//2+1) for flag in ((0,) if 2*a == D else (0, 1))]
        assert sorted(D-a if flag else a for a, flag in orbits) == list(range(N))
        for word in words:
            folded_sum = zero
            for labels in itertools.product(orbits, repeat=len(word)):
                factors = []
                for j, n in enumerate(word):
                    a, fa = labels[j]
                    b, fb = labels[(j+1) % len(word)]
                    weight = conj(P[b])/N if fb else one/P[b]
                    factors.append(folded[(n-3, fa, fb, a, b)]*weight**(n-3))
                folded_sum += product(factors)
            old = original[word[0]]
            for n in word[1:]:
                old = matmul(old, original[n])
            check(f"N{N} original whole folded cyclic word {word}", folded_sum-sum((old[a][a] for a in range(N)), zero))

        if N == 3:
            value = C[1][1][1]*conj(C[1][1][0]*C[1][0][1])-conj(C[1][0][0]*C[1][1][1])
            check("N3 arbitrary row-column reflection obstruction", value+cv(sp.I*sp.sqrt(3)/3))
            assert value != zero
            obstruction = str(sp.simplify(field.to_sympy(value)))

    X, Y = sp.symbols("X Y", nonzero=True)
    c0 = lambda x, y: 1+(1+x)*(1+y)/(4*x)
    f0 = lambda x: (3-x)/2
    difference = c0(-1/X, -1/Y)-f0(X)*f0(1/Y)*c0(Y, X)/2
    rhs = (X+1)*(Y+1)*(3*X*Y-X-5*Y+3)/(32*Y**2)
    assert sp.cancel(difference-rhs) == 0
    assert sp.cancel(difference.subs({X: 2, Y: 2})) == sp.Rational(27, 128)
    identities.append("N2 physical-only reflection polynomial and nonzero off-grid value")
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "arithmetic": "exact Q(i,sqrt(2),sqrt(3)) and rational polynomial arithmetic",
        "levels": [2, 3, 4, 6], "exact_identity_count": len(identities), "exact_identities": identities,
        "original_words": words, "type_four_row_column_obstruction": obstruction,
        "source_records": len(specs), "proof_sha256": ph, "script_sha256": sh,
        "dependencies_sha256": deps,
        "scope": "Exact physical folding and original scalar/alias transport, pure-three half comparison, and an exact four-type reflection remainder. No mixed-word asymptotic or lower bound.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(identities), "exact identities at levels2,3,4,6")


if __name__ == "__main__":
    main()
