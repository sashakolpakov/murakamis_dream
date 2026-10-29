#!/usr/bin/env python3
"""Exact finite-field checks of the ORIGINAL figure-eight nodal Ward source.

The source is the proved reduced whole-source identity, with no scalar
renormalization: mu(f)=sum_n |(Q;Q)_n|^2 f(Q^n).  The star on the unit
root is implemented algebraically by Q -> Q^-1.  This does not test a
generic replacement source or infer analytic bounds from numerics.
"""

import json
from pathlib import Path


def prime_divisors(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return ans


def primitive_root(p):
    divs = prime_divisors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in divs):
            return g
    raise AssertionError("no primitive root")


def family(p, N):
    assert (p - 1) % N == 0
    Q = pow(primitive_root(p), (p - 1) // N, p)
    assert pow(Q, N, p) == 1
    assert all(pow(Q, N // ell, p) != 1 for ell in prime_divisors(N))
    roots = [z for z in range(p) if (z * z - z + 1) % p == 0]
    assert len(roots) == 2
    zp, zm = roots
    gap = (zp - zm) % p
    gap_inv = pow(gap, -1, p)
    clocks = [pow(Q, n, p) for n in range(N)]

    def A(z):
        return (2 - z - pow(z, -1, p)) % p

    weights = [1]
    f_plus = 1
    f_minus = 1
    for n in range(1, N):
        f_plus = f_plus * (1 - clocks[n]) % p
        f_minus = f_minus * (1 - pow(clocks[n], -1, p)) % p
        weights.append(f_plus * f_minus % p)
    assert all(weights)
    for n in range(N - 1):
        assert weights[n + 1] == A(clocks[n + 1]) * weights[n] % p
    assert A(1) * weights[-1] % p == 0

    def mu(values):
        return sum(w * v for w, v in zip(weights, values)) % p

    def B(values):
        return [A(clocks[(n + 1) % N]) * values[(n + 1) % N] % p
                for n in range(N)]

    ep = [(z - zm) * gap_inv % p for z in clocks]
    em = [(1 - e) % p for e in ep]
    count = 0
    for j in range(-2, N + 3):
        f = [pow(z, j, p) for z in clocks]
        bf = B(f)
        assert mu([(a - b) % p for a, b in zip(f, bf)]) == 1
        bef = B([e * value % p for e, value in zip(ep, f)])
        lhs = [(value - e * b) % p for value, e, b in zip(bef, ep, bf)]
        rhs = [(Q - 1) * z * b * gap_inv % p
               for z, b in zip(clocks, bf)]
        assert lhs == rhs
        count += 1

    endpoint_plus = (1 - zm) * gap_inv % p
    endpoint_minus = (zp - 1) * gap_inv % p
    assert endpoint_plus == zp * gap_inv % p
    assert endpoint_minus == -zm * gap_inv % p
    assert endpoint_plus and endpoint_minus
    for values, target in [(ep, endpoint_plus), (em, endpoint_minus)]:
        assert mu([(a - b) % p for a, b in zip(values, B(values))]) == target
    for z, e in zip(clocks, ep):
        assert (e * (e - 1) - (z * z - z + 1) * gap_inv**2) % p == 0

    # The commutator is genuinely nonzero, not merely formally allowed.
    assert any((Q - 1) * z * A(Q * z % p) * gap_inv % p for z in clocks)
    return {"p": p, "N": N, "Ward_and_commutator_insertions": count,
            "nonzero_original_endpoints": [endpoint_plus, endpoint_minus]}


def main():
    cases = [family(1009, N) for N in
             [2, 3, 4, 6, 7, 8, 9, 12, 14, 16, 18, 21, 24, 28]]
    result = {
        "status": "PASS",
        "source": "original reduced figure-eight whole-source weights",
        "families": cases,
        "total_exact_insertions": sum(c["Ward_and_commutator_insertions"] for c in cases),
        "scope": "finite identities supplement the analytic Morse/relative-current proof",
    }
    target = Path(__file__).with_name("actual_node_source_ward_results.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(cases)} original-source families; "
          f"{result['total_exact_insertions']} exact Ward/commutator insertions")


if __name__ == "__main__":
    main()
