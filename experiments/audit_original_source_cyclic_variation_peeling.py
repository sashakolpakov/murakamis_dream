#!/usr/bin/env python3
"""Independent finite checks of the original source's forced cut face."""

from collections import defaultdict
from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_kashaev_crossing import original


def corners(n, a, b, c, d):
    return ((b-a-1) % n, (a-c) % n, (c-d) % n, (d-b) % n)


def supported(n):
    return {(a, b): [(c, d, corners(n, a, b, c, d))
                    for c, d in product(range(n), repeat=2)
                    if sum(corners(n, a, b, c, d)) == n-1]
            for a, b in product(range(n), repeat=2)}


def source_paths(n, width, positions):
    local = supported(n)
    masks = [set() for _ in positions]
    count = 0
    for tail in product(range(n), repeat=width-1):
        initial = (0,) + tuple((j+1) % n for j in tail)
        final = (0,) + tail
        forward = [{initial: 1}]
        for pos in positions:
            next_counts = defaultdict(int)
            for state, multiplicity in forward[-1].items():
                for c, d, _ in local[state[pos], state[pos+1]]:
                    out = state[:pos] + (c, d) + state[pos+2:]
                    next_counts[out] += multiplicity
            forward.append(next_counts)
        count += forward[-1].get(final, 0)
        if final not in forward[-1]:
            continue
        assert tail[0] == 0
        backward = {final}
        for j in range(len(positions)-1, -1, -1):
            pos = positions[j]
            previous = set()
            for state in forward[j]:
                for c, d, ks in local[state[pos], state[pos+1]]:
                    out = state[:pos] + (c, d) + state[pos+2:]
                    if out not in backward:
                        continue
                    previous.add(state)
                    assert state[0] == out[0] == 0
                    if pos == 0:
                        assert ks[1] == 0
                    masks[j].update(i for i, k in enumerate(ks) if k)
            backward = previous
    if 0 in positions and count:
        first, last = positions.index(0), len(positions)-1-positions[::-1].index(0)
        assert 0 not in masks[first]
        assert 1 not in masks[first]
        assert 1 not in masks[last]
        assert 2 not in masks[last]
    return {"N": n, "width": width, "positions": positions,
            "supported_paths": count,
            "forced_zero_corners": [sorted(set(range(4))-s) for s in masks]}


def variation_checks(n):
    checked = 0
    for (a, b), outputs in supported(n).items():
        for c, d, (u, v, t, h) in outputs:
            assert v+t+h == (a-b) % n
            for left, right in product(range(n), repeat=2):
                before = (left-a) % n + (a-b) % n + (b-right) % n
                after = (left-c) % n + (c-d) % n + (d-right) % n
                assert after <= before
                checked += 1
    return checked


def embed(local, width, pos, n):
    return np.kron(np.eye(n**pos, dtype=np.int64),
                   np.kron(local, np.eye(n**(width-pos-2), dtype=np.int64)))


def embed_one(local, width, pos, n):
    return np.kron(np.eye(n**pos, dtype=np.int64),
                   np.kron(local, np.eye(n**(width-pos-1), dtype=np.int64)))


def flat(state, n):
    out = 0
    for j in state:
        out = n*out+j
    return out


def field_audit(n):
    prime = next(4*n*k+1 for k in range(1, 1000) if sp.isprime(4*n*k+1))
    root = pow(int(sp.primitive_root(prime)), (prime-1)//(4*n), prime)
    q, Q = pow(root, 2, prime), pow(root, 4, prime)
    r, inverse_printed, factorials = original(n, prime, Q)
    conjugate_r, _, _ = original(n, prime, pow(Q, -1, prime))
    swap = np.zeros_like(r)
    for a, b in product(range(n), repeat=2):
        swap[b*n+a, a*n+b] = 1
    plus = swap @ r.T % prime
    minus = inverse_printed.T @ swap * pow(Q, -1, prime) % prime
    conjugate_plus = swap @ conjugate_r.T % prime
    for a, b, c, d in product(range(n), repeat=4):
        assert minus[c*n+d, a*n+b] == (
            pow(Q, c+d-a-b, prime)*conjugate_plus[c*n+d, a*n+b] % prime)
    T, Ti = plus[:n, :n], minus[:n, :n]
    target = np.zeros_like(T)
    target_i = np.zeros_like(T)
    for j in range(n):
        target[0, j] = pow(Q, 1-j, prime)
        target_i[0, j] = pow(Q, -1, prime)
        for k in range(max(1, j), n):
            if not j:
                continue
            choose = factorials[k-1]*pow(factorials[j-1]*factorials[k-j] % prime,
                                         -1, prime) % prime
            target[k, j] = ((-1)**(j-1)*pow(Q, k+(j-1)*(j-2)//2, prime)
                             * choose) % prime
            choose_inverse = choose*pow(Q, -(j-1)*(k-j), prime) % prime
            target_i[k, j] = ((-1)**(j-1)*pow(Q, -j-(j-1)*(j-2)//2, prime)
                               * choose_inverse) % prime
    assert np.array_equal(T, target)
    assert np.array_equal(Ti, target_i)
    assert np.array_equal(T @ Ti % prime, np.eye(n, dtype=np.int64))

    words = [
        (2, [(0, 1)]*3),
        (2, [(0, 1), (0, -1), (0, 1)]),
        (3, [(0, 1), (1, 1), (0, 1), (1, 1)]),
        (3, [(0, 1), (1, -1), (0, 1), (1, -1)]),
        (3, [(1, -1), (0, 1), (1, 1), (0, -1), (0, 1), (1, -1)]),
    ]
    if n <= 4:
        words.append((4, [(2, 1), (1, -1), (0, 1), (2, -1), (1, 1), (0, -1)]))
    records = []
    for width, word in words:
        full = np.eye(n**width, dtype=np.int64)
        peeled = np.eye(n**(width-1), dtype=np.int64)
        for pos, sign in word:
            crossing = plus if sign == 1 else minus
            full = embed(crossing, width, pos, n) @ full % prime
            block = (embed_one(T if sign == 1 else Ti, width-1, 0, n)
                     if pos == 0 else embed(crossing, width-1, pos-1, n))
            peeled = block @ peeled % prime
        source_sum = sum(int(full[flat((0,)+tail, n),
                                  flat((0,)+tuple((j+1) % n for j in tail), n)])
                         for tail in product(range(n), repeat=width-1)) % prime
        peeled_sum = sum(int(peeled[flat((0,)+tail, n),
                                   flat((1,)+tuple((j+1) % n for j in tail), n)])
                          for tail in product(range(n), repeat=width-2)) % prime
        alpha = -q % prime
        writhe = sum(sign for _, sign in word)
        scalar = source_sum*pow(alpha, width-1-writhe, prime) % prime
        peeled_scalar = peeled_sum*pow(alpha, 1+width-2-writhe, prime) % prime
        assert scalar == peeled_scalar
        records.append({"width": width, "word": word, "original_scalar": scalar,
                        "peeled_scalar": peeled_scalar})
    assert records[2]["original_scalar"] != records[3]["original_scalar"]
    return {"N": n, "prime": prime, "actual_inverse_sign_identity": True,
            "q_pascal_and_inverse": True, "whole_words": records}


def main():
    support_cases = [(2, [0]*3), (2, [0]*5), (3, [0, 1, 0, 1]),
                     (3, [1, 0, 1, 0]), (3, [0, 1, 1, 1, 0, 1]),
                     (4, [2, 1, 0, 2, 1, 0])]
    result = {
        "scope": "Finite diagnostics supplement the all-N source-path proof in the note.",
        "local_variation": [{"N": n, "checks": variation_checks(n)} for n in range(2, 8)],
        "source_paths": [source_paths(n, b, word) for n in (3, 5, 7)
                         for b, word in support_cases],
        "fields": [field_audit(n) for n in range(2, 7)],
    }
    path = Path(__file__).with_name("original_source_cyclic_variation_peeling_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS original cyclic variation / forced source faces / exact q-Pascal peeling")
    print(json.dumps({"local_variation_checks": sum(r["checks"] for r in result["local_variation"]),
                      "support_families": len(result["source_paths"]),
                      "field_levels": len(result["fields"]),
                      "whole_word_identities": sum(len(r["whole_words"]) for r in result["fields"])}))


if __name__ == "__main__":
    main()
