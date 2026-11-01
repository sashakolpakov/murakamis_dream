#!/usr/bin/env python3
"""Bounded exact checks for the coupled protected spectral bound.

The source vector is built from the original unused spectral products.
The comparison vector is independently built from a polynomial of the
bidiagonal matrix. All spectral polynomial coefficients are compared.
These finite checks do not replace the density or integral inequalities.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sympy as sp


def check(N):
    z = sp.Symbol("z")
    F = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(4*N, z), 0))
    root, one, zero = F.unit, F.one, F.zero
    imag = root**N
    d, M = N-1, N//2-1
    size = M+1

    def sin_half(k):
        return (root**k-root**(-k))/(2*imag)

    def prod(values):
        out = one
        for value in values:
            out *= value
        return out

    def pmul(p, q):
        out = [zero]*(len(p)+len(q)-1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i+j] += a*b
        return out

    nodes = [root**(4*j+2)+root**(-4*j-2) for j in range(N)]
    squared_sines = [4*sin_half(2*j)**2 for j in range(N)]
    U0 = one/sin_half(1)**2
    chi = [one]
    for node in nodes:
        chi = pmul(chi, [-node, one])

    # Independently construct 2(T_N(z/2)+1).
    cheb0, cheb1 = [one], [zero, one/2]
    for k in range(1, N):
        nxt = [zero]*(len(cheb1)+1)
        for j, a in enumerate(cheb1):
            nxt[j+1] += a
        for j, a in enumerate(cheb0):
            nxt[j] -= a
        cheb0, cheb1 = cheb1, nxt
    cheb = [2*a for a in cheb1]
    cheb[0] += 2
    assert chi == cheb

    C = [[sin_half(2)/sin_half(2*(i+j+1))
          for j in range(size)] for i in range(size)]
    A = [[zero for _ in range(size)] for _ in range(size)]
    for j in range(size):
        A[j][j] = nodes[j]
        if j:
            A[j][j-1] = squared_sines[j]

    def apply_A(v):
        return [sum((A[i][j]*v[j] for j in range(size)), zero)
                for i in range(size)]

    counts = Counter()
    for i in range(size):
        for j in range(size):
            ac = sum((A[i][k]*C[k][j] for k in range(size)), zero)
            cat = sum((C[i][k]*A[j][k] for k in range(size)), zero)
            assert ac == cat
            counts["direct_matrix_self_adjoint_entries"] += 1

    e0 = [one]+[zero]*M
    powers = [e0]
    for k in range(1, N+1):
        powers.append(apply_A(powers[-1]))
    for j in range(size):
        assert sum((chi[k]*powers[k][j] for k in range(N+1)), zero) == zero
        counts["full_spectral_polynomial_annihilates_matrix_column"] += 1

    moments = [one]
    for j in range(1, 2*M+1):
        moments.append(moments[-1]
                       * (sin_half(2*j)/sin_half(2*j+1))**2)
    for j in range(2*M+1):
        sj = prod(squared_sines[1:j+1])
        source = [sj/U0]
        for node in nodes[j+1:]:
            source = pmul(source, [-node, one])
        at_two = sum((a*2**k for k, a in enumerate(source)), zero)
        assert at_two == moments[j]
        counts["original_unused_rows_at_two_equal_actual_moments"] += 1
        if j <= M:
            source += [zero]*(N-len(source))
            for ell in range(N):
                comparison = sum(
                    (chi[k]*powers[k-1-ell][j]
                     for k in range(ell+1, N+1)), zero)/U0
                assert source[ell] == comparison
                counts["all_spectral_coefficients_source_vs_matrix_polynomial"] += 1

    assert N-2*M-2 in (0, 1)
    assert 2*M <= N-2
    counts["original_parity_moment_and_tail_cutoffs"] += 1
    counts["full_node_product_vs_Chebyshev"] += 1
    return dict(counts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "cap_coupled_spectral_algebra_results.json"))
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit("Assertions must remain enabled; do not use -O.")
    levels = [3, 4, 5, 6, 7, 8]
    results = {str(N): check(N) for N in levels}
    record = {
        "status": "passed",
        "levels": levels,
        "arithmetic": "Exact cyclotomic fields of order 4N",
        "checks": results,
        "scope": (
            "Original unused spectral products, full Chebyshev polynomial, "
            "sine-Cauchy self-adjointness, actual moments, and every coefficient "
            "of the source/matrix divided-difference identity at both parities."
        ),
        "limits": (
            "These finite algebra checks do not prove a density inequality, "
            "a uniform analytic norm bound, a spectator geometric rate, "
            "or a volume theorem. The written proof supplies the analytic bound."
        ),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "passed", "levels": levels,
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
