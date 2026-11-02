#!/usr/bin/env python3
"""Exact finite-field checks of the physical Newton identities.

Requires NumPy and SymPy. The finite levels are regression checks, not a
proof for arbitrary N or verification of the variational limit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sympy import isprime, primitive_root

if not __debug__:
    raise SystemExit("Run without -O: these checks require assertions.")


def check_level(n: int) -> dict:
    # A primitive 4N-th root also fixes the square root of q in kappa.
    modulus = 4 * n
    start = 1 + modulus * ((10000 + modulus - 1) // modulus)
    p = next(k for k in range(start, 30000, modulus) if isprime(k))
    t = pow(int(primitive_root(p)), (p - 1) // modulus, p)
    q, d = t * t % p, n - 1
    Q, ii, x, kappa = q * q % p, pow(t, n, p), pow(q, d, p), pow(t, d*d, p)
    inv = lambda a: pow(int(a) % p, -1, p)
    assert pow(t, modulus, p) == 1 and pow(t, modulus // 2, p) != 1
    assert ii * ii % p == p - 1
    eye = np.eye(n, dtype=np.int64)
    E = np.zeros((n, n), dtype=np.int64)
    F = E.copy()
    K = np.diag([x * pow(Q, -a, p) % p for a in range(n)])
    Ki = np.diag([inv(K[a, a]) for a in range(n)])
    for a in range(1, n):
        E[a-1, a] = (pow(Q, -a, p) - 1) % p
    for a in range(n-1):
        F[a+1, a] = (1 - pow(Q, a+1, p)) % p
    EP = (np.kron(E, K) + np.kron(eye, E)) % p
    FP = (np.kron(F, eye) + np.kron(Ki, F)) % p
    KP, KPi = np.kron(K, K) % p, np.kron(Ki, Ki) % p
    omega = (FP @ EP + q * KP + inv(q) * KPi) % p
    ident = np.eye(n*n, dtype=np.int64)
    zero = np.zeros_like(ident)
    # Each matrix product is reduced before another is taken. At these
    # primes and dimensions its integer entries cannot overflow int64.
    assert 2 * n*n * p*p < np.iinfo(np.int64).max
    for generator in (EP, FP, KP):
        assert np.array_equal((omega @ generator - generator @ omega) % p, zero)
    cup = np.array([n * pow(x,-b,p) % p if a+b == d else 0
                    for a in range(n) for b in range(n)], dtype=np.int64)
    cap = np.array([pow(x,a,p) * inv(n) % p if a+b == d else 0
                    for a in range(n) for b in range(n)], dtype=np.int64)
    for generator in (EP, FP):
        assert not np.any(generator @ cup % p)
        assert not np.any(cap @ generator % p)
    assert np.array_equal(KP @ cup % p, cup)
    assert np.array_equal(cap @ KP % p, cap)
    c = [(pow(q, 2*a+1, p) + pow(q, -2*a-1, p)) % p for a in range(n)]
    sine = [0] + [(pow(q, r, p) - pow(q, -r, p)) * inv(ii) % p for r in range(1, n)]
    factorial = [1]
    basis = [ident]
    for r in range(1, n):
        factorial.append(factorial[-1] * sine[r] % p)
        step = ((c[r-1] * ident - omega) @ basis[-1]) % p
        basis.append(step * inv(sine[r] * sine[r]) % p)
    assert np.array_equal(((c[d] * ident - omega) @ basis[d]) % p, zero)

    def turn(matrix, with_phase=True):
        return np.array([
            [(pow(x, a-e, p) if with_phase else 1)
             * int(matrix[b*n+d-e, (d-a)*n+u]) % p
             for u in range(n) for e in range(n)]
            for a in range(n) for b in range(n)], dtype=np.int64)

    pivot = [pow(int(K[b, b]), 1-n, p) for b in range(n)]

    def trace(matrix):
        return sum(int(matrix[a*n+b, a*n+b]) * pivot[b]
                   for a in range(n) for b in range(n)) * inv(n) % p

    def lincomb(terms):
        result = zero.copy()
        for coefficient, matrix in terms:
            result = (result + int(coefficient) % p * matrix) % p
        return result

    for r in range(n):
        assert np.array_equal(turn(basis[r]), basis[d-r])
        assert trace(basis[r]) == int(r == d)
    for i in range(n):
        for j in range(n):
            actual = basis[i] @ basis[j] % p
            assert trace(actual) == int(i+j == d)
            terms = []
            if i+j < n:
                for r in range(max(i,j), i+j+1):
                    den = (factorial[i] * factorial[j] * factorial[r-i]
                           * factorial[r-j] * factorial[i+j-r])
                    coefficient = factorial[i+j] * factorial[r] * inv(den) % p
                    terms.append((coefficient, basis[r]))
            assert np.array_equal(actual, lincomb(terms)), (n, i, j, "product")

    # Compute circles from their Chebyshev recurrence, independently of
    # the displayed Newton coefficient formulas.
    U = [ident, omega]
    for j in range(2, n):
        U.append((omega @ U[-1] - U[-2]) % p)
    circles = [zero] + [((-1)**(j-1) * U[j-1]) % p for j in range(1,n+1)]
    h = [turn(circle) for circle in circles]
    M = d // 2
    for deficit in range(M+1):
        terms = []
        for v in range(deficit, M+1):
            den = factorial[v]**2 * factorial[v-deficit] * factorial[v+deficit]
            coefficient = n*n * factorial[2*v] * inv(den) % p
            terms.append((coefficient, basis[v]))
        expected = (lincomb(terms) + (-1)**n * h[deficit]) % p
        assert np.array_equal(h[n-deficit], expected), (n, deficit, "core split")
    for j in range(1, n//2+1):
        terms = []
        for r in range(j):
            den = factorial[2*r+1] * factorial[j-r-1]
            coefficient = ((-1)**(j-1+r) * factorial[r]**2
                           * factorial[j+r] * inv(den)) % p
            terms.append((coefficient, basis[d-r]))
        assert np.array_equal(h[j], lincomb(terms)), (n, j, "low circle")

    # The crossing polynomial is checked against both its Hermite data
    # and its actual inverse; matrix turns then test the half-twist rule.
    def polynomial_value_and_derivative(z, exponent):
        value, derivative, B, dB = 0, 0, 1, 0
        for r in range(n):
            coefficient = (pow(kappa, exponent, p) * (-1)**r
                           * pow(q, exponent*r, p) * inv(factorial[r]**2)) % p
            value = (value + coefficient * B) % p
            derivative = (derivative + coefficient * dB) % p
            dB, B = ((c[r]-z)*dB-B) % p, (c[r]-z)*B % p
        return value, derivative

    crossings = {}
    for exponent in (-1, 1):
        crossings[exponent] = lincomb(
            (pow(kappa, exponent, p) * (-1)**r * pow(q, exponent*r, p), basis[r])
            for r in range(n))
        for j in range((n+1)//2):
            value, derivative = polynomial_value_and_derivative(c[j], exponent)
            prescribed = pow(kappa * (-1)**j * pow(q, j*(j+1), p) % p, exponent, p)
            assert value == prescribed, (n, j, "crossing value")
            if not (n % 2 and j == d//2):
                rate = -exponent * (d-2*j) * inv(2*(pow(q,2*j+1,p)-pow(q,-2*j-1,p))) % p
                assert derivative == value * rate % p, (n,j,"crossing normal")
        for v in range(n):
            actual = turn(crossings[exponent] @ turn(basis[v]) % p)
            expected = lincomb(
                (pow(kappa,exponent,p) * (-1)**v * pow(q,exponent*v*(r+1),p)
                 * factorial[v] * inv(factorial[r]*factorial[v-r]), basis[r])
                for r in range(v+1))
            assert np.array_equal(actual, expected), (n,v,exponent,"half twist")
    assert np.array_equal(crossings[1] @ crossings[-1] % p, ident)

    # Concrete failures of value-only reduction and of phase-free turning.
    nilpotent = ident
    for z in dict.fromkeys(c):
        nilpotent = (z*ident-omega) @ nilpotent % p
    assert np.any(nilpotent)
    assert np.array_equal(nilpotent @ nilpotent % p, zero)
    assert any(not np.array_equal(turn(b, False), turn(b)) for b in basis)
    return {"level": n, "prime": p, "primitive_4N_root": t,
            "cup_cap_intertwiner_identities": 6,
            "physical_turns": n, "physical_trace_pairings": n*n,
            "full_products": n*n, "high_color_splits": M+1,
            "low_color_expansions": n//2, "half_twists": 2*n,
            "negative_controls": ["value_only_discards_nonzero_nilpotent", "turn_phase_cannot_be_omitted"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.unlink(missing_ok=True)
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    inputs = [Path(__file__).resolve(), here / "main.tex", here / "figures/tangle-construction.tex"]
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    before = {str(p.relative_to(root)): digest(p) for p in inputs}
    rows = [check_level(n) for n in range(2, 10)]
    assert all(digest(root/p) == h for p,h in before.items())
    report = {"scope": "Exact finite-field physical matrices and polynomial identities at eight levels; not an all-level or variational proof.",
              "levels": rows, "source_sha256": before}
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(f"Eight levels checked: physical turns, traces, products, color splits and half twists. {args.output or ''}")


if __name__ == "__main__":
    main()
