#!/usr/bin/env python3
"""Exact finite checks of Appendix N's local Fourier adapter.

The physical matrix is formed from the displayed coproduct, independently
of the face operator. Finite fields check signs and normalization in a
bounded set of examples; the proof for all complex root levels is written
in the manuscript.
"""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def factors(n):
    return [d for d in range(2, n + 1) if n % d == 0 and prime(d)]


def fields(N):
    result = []
    p = 1 + 2 * N * ((1009 + 2 * N - 2) // (2 * N))
    while len(result) < 2:
        if prime(p):
            divisors = factors(p - 1)
            generator = next(
                g for g in range(2, p)
                if all(pow(g, (p - 1) // d, p) != 1 for d in divisors)
            )
            q = pow(generator, (p - 1) // (2 * N), p)
            assert pow(q, N, p) == p - 1
            assert all(pow(q, 2 * N // d, p) != 1 for d in factors(2 * N))
            result.append((p, q))
        p += 2 * N
    return result


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(A, B, p):
    return [[sum(a * b for a, b in zip(row, col)) % p
             for col in zip(*B)] for row in A]


def scale(A, c, p):
    return [[c * a % p for a in row] for row in A]


def add(A, B, p):
    return [[(a + b) % p for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def evaluate(coefficients, A, p):
    I = identity(len(A))
    out = scale(I, 0, p)
    for c in reversed(coefficients):
        out = add(mul(out, A, p), scale(I, c, p), p)
    return out


def casimir_block(N, s, q, p):
    """Form F_12 Ecal_12 + q K_12 + q^-1 K_12^-1 from its four factors."""
    Q, d = q * q % p, N - 1
    K = [pow(q, d - 2 * i, p) for i in range(N)]
    O = [[0] * N for _ in range(N)]
    for u in range(N):
        v = (s - u) % N
        intermediate = []
        if u:
            intermediate.append((u - 1, v, (pow(Q, -u, p) - 1) * K[v]))
        if v:
            intermediate.append((u, v - 1, pow(Q, -v, p) - 1))
        for a, b, coefficient in intermediate:
            outputs = []
            if a < d:
                outputs.append((a + 1, b, 1 - pow(Q, a + 1, p)))
            if b < d:
                outputs.append((a, b + 1, pow(K[a], -1, p) * (1 - pow(Q, b + 1, p))))
            for r, t, factor in outputs:
                assert r + t == u + v and t == (s - r) % N
                O[r][u] = (O[r][u] + coefficient * factor) % p
        pairK = K[u] * K[v] % p
        O[u][u] = (O[u][u] + q * pairK + pow(q * pairK, -1, p)) % p
    return O


def face_matrix(N, q, p, x, y):
    Q = q * q % p
    T = [[0] * N for _ in range(N)]
    for j in range(N):
        Z = pow(Q, j, p)
        A = -(q * Z + pow(q * Z, -1, p))
        B = 2 - Z - pow(Z, -1, p)
        C = q + pow(q, -1, p) - q * pow(Z, -1, p) - pow(q, -1, p) * Z
        T[j][j] = A % p
        if j:
            T[j - 1][j] = B * (x + y) % p
        else:
            assert B % p == 0
        if j >= 2:
            T[j - 2][j] = C * x * y % p
        else:
            assert C % p == 0
    return T


def chebyshev_annihilator(N, p):
    a, b = [2], [0, 1]
    for _ in range(1, N):
        shifted = [0] + b
        a += [0] * (len(shifted) - len(a))
        a, b = b, [(x - y) % p for x, y in zip(shifted, a)]
    b[0] = (b[0] + 2) % p
    return b


def run():
    rows = []
    for N in range(2, 13):
        d = N - 1
        for p, q in fields(N):
            Q = q * q % p
            chi = chebyshev_annihilator(N, p)
            canonical_errors = 0
            entries = wrong_totals = 0
            for s in range(N):
                x, y = pow(Q, s + 1, p), 1
                b = [-pow(q, -1, p) * x * pow(Q, -u, p) % p for u in range(N)]
                E = [[pow(z, j, p) for j in range(N)] for z in b]
                Ei = [[pow(N, -1, p) * pow(b[r], -j, p) % p for r in range(N)]
                      for j in range(N)]
                assert mul(E, Ei, p) == identity(N)
                O = casimir_block(N, s, q, p)
                T = face_matrix(N, q, p, x, y)
                transformed = [[-pow(q, d * (r - u), p) * O[r][u] % p
                                for r in range(N)] for u in range(N)]
                assert mul(E, T, p) == mul(transformed, E, p)
                assert evaluate(chi, O, p) == [[0] * N for _ in range(N)]
                characteristic = [1]
                for j in range(N):
                    root = -T[j][j] % p
                    out = [0] * (len(characteristic) + 1)
                    for k, c in enumerate(characteristic):
                        out[k] = (out[k] - root * c) % p
                        out[k + 1] = (out[k + 1] + c) % p
                    characteristic = out
                assert characteristic == chi
                # A degree>N multiplier tests the full matrix polynomial adapter.
                f = [3, 7] + [0] * (N - 1) + [11]
                physical = evaluate(f, O, p)
                polynomial = evaluate(f, scale(T, -1, p), p)
                for u in range(N):
                    for r in range(N):
                        H = sum(polynomial[k][j] * pow(b[u], k, p) * pow(b[r], d - j, p)
                                for j in range(N) for k in range(j + 1)) % p
                        base = pow(N, -1, p) * pow(b[r], -d, p) * H % p
                        predicted = base * pow(q, -d * (r - u), p) % p
                        assert predicted == physical[r][u]
                        entries += 1
                        if u + (s - u) % N != r + (s - r) % N:
                            assert predicted == 0
                            wrong_totals += 1
                        residue_phase = base * pow(q, -d * ((r - u) % N), p) % p
                        canonical_errors += residue_phase != predicted
            if N % 2 == 0:
                assert canonical_errors > 0, "The even-level phase control did not discriminate."
            else:
                assert canonical_errors == 0
            rows.append(dict(N=N, prime=p, q=q, residue_blocks=N,
                             polynomial_entries=entries, wrong_total_zeros=wrong_totals,
                             incorrect_residue_phase_mismatches=canonical_errors))
    sources = [Path(__file__).resolve().relative_to(ROOT),
               Path("manuscript/sections/N-uniform-filling-bound.tex")]
    return {
        "scope": "Exact finite-field examples of the written all-level complex-root proof; not an extrapolation proof.",
        "cases": rows,
        "residue_blocks": sum(row["residue_blocks"] for row in rows),
        "polynomial_entries": sum(row["polynomial_entries"] for row in rows),
        "source_sha256": {str(path): hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                          for path in sources},
    }


def main():
    if not __debug__:
        raise RuntimeError("Run without Python optimization; the checker uses assertions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "repro/results/local-face-fourier-current.json")
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"cases", "source_sha256"}}, indent=2))


if __name__ == "__main__":
    main()
