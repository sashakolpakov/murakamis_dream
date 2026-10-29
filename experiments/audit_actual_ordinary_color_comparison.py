#!/usr/bin/env python3
"""Independent finite-field checks of quotient colors and literal cabling.

The fundamental cable and its highest-weight embedding are assembled here,
independently of the positive path model.  All Cartan scalars are retained.
These checks supplement the all-level proof in the companion note.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_kashaev_ado_pointing import color_matrices
from audit_adequacy_algebraic_periods import cable


def field(level):
    p = next(4 * level * t + 1 for t in range(1, 10000)
             if sp.isprime(4 * level * t + 1))
    generator = int(sp.primitive_root(p))
    half = pow(generator, (p - 1) // (4 * level), p)
    return p, half, half * half % p


def inverse(matrix, p):
    n = len(matrix)
    a = np.concatenate((matrix.copy() % p, np.eye(n, dtype=np.int64)), axis=1)
    for j in range(n):
        r = next(r for r in range(j, n) if a[r, j] % p)
        a[[j, r]] = a[[r, j]]
        a[j] = a[j] * pow(int(a[j, j]), -1, p) % p
        for r in range(n):
            if r != j:
                a[r] = (a[r] - int(a[r, j]) * a[j]) % p
    return a[:, n:]


def rank(matrix, p):
    a = matrix.copy() % p
    row = 0
    for col in range(a.shape[1]):
        pivot = next((r for r in range(row, len(a)) if a[r, col]), None)
        if pivot is None:
            continue
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = a[row] * pow(int(a[row, col]), -1, p) % p
        for r in range(row + 1, len(a)):
            a[r] = (a[r] - int(a[r, col]) * a[row]) % p
        row += 1
        if row == len(a):
            break
    return row


def qinteger(a, q, p):
    return (pow(q, a, p) - pow(q, -a, p)) * pow(q - pow(q, -1, p), -1, p) % p


def standard_crossing(j, p, half, q):
    """The unstripped defining R on the j-dimensional highest-weight color."""
    m = j - 1
    factorial = [1]
    for a in range(1, j):
        factorial.append(factorial[-1] * qinteger(a, q, p) % p)
    rho = (q - pow(q, -1, p)) % p
    result = np.zeros((j * j, j * j), dtype=np.int64)
    for a, b in product(range(j), repeat=2):
        ec = 1
        for h in range(min(a, m - b) + 1):
            if h:
                ec = ec * qinteger(a - h + 1, q, p) * qinteger(j - a + h - 1, q, p) % p
            c, d = a - h, b + h
            scalar = (pow(q, h * (h - 1) // 2, p) * pow(rho, h, p)
                      * pow(factorial[h], -1, p) * ec
                      * pow(half, (m - 2 * c) * (m - 2 * d), p)) % p
            result[d * j + c, a * j + b] = scalar
    return result


def local_apply(matrix, j, heads, vectors, p):
    """Apply a fundamental two-head matrix without constructing the whole cable."""
    columns = vectors.shape[1]
    shaped = vectors.reshape((2 ** j, 4, 2 ** (heads - j - 2), columns))
    following = np.einsum('ab,ibkc->iakc', matrix, shaped) % p
    return following.reshape(vectors.shape)


def embedded_local(matrix, j, heads, p):
    return local_apply(matrix, j, heads, np.eye(2 ** heads, dtype=np.int64), p)


def highest_embedding(m, p, q):
    size = 2 ** m
    total_f = np.zeros((size, size), dtype=np.int64)
    total_e = np.zeros_like(total_f)
    total_k = np.zeros_like(total_f)
    for column, state in enumerate(product(range(2), repeat=m)):
        total_k[column, column] = pow(q, m - 2 * sum(state), p)
        for i in range(m):
            if state[i] == 0:
                following = state[:i] + (1,) + state[i + 1:]
                row = sum(bit << (m - r - 1) for r, bit in enumerate(following))
                total_f[row, column] = pow(q, -sum(1 - 2 * bit for bit in state[:i]), p)
            else:
                following = state[:i] + (0,) + state[i + 1:]
                row = sum(bit << (m - r - 1) for r, bit in enumerate(following))
                total_e[row, column] = pow(q, sum(1 - 2 * bit for bit in state[i + 1:]), p)
    embedding = np.zeros((size, m + 1), dtype=np.int64)
    embedding[0, 0] = 1
    for a in range(1, m + 1):
        embedding[:, a] = total_f @ embedding[:, a - 1] % p
    small_f = np.zeros((m + 1, m + 1), dtype=np.int64)
    small_e = np.zeros_like(small_f)
    small_k = np.diag([pow(q, m - 2 * a, p) for a in range(m + 1)]).astype(np.int64)
    for a in range(m):
        small_f[a + 1, a] = 1
        small_e[a, a + 1] = qinteger(a + 1, q, p) * qinteger(m - a, q, p) % p
    assert rank(embedding, p) == m + 1
    for big, small in ((total_e, small_e), (total_f, small_f), (total_k, small_k)):
        assert np.array_equal(big @ embedding % p, embedding @ small % p)
    return embedding, total_k


def cabling_case(level, color):
    p, half, q = field(level)
    m = color - 1
    jmap, ktot = highest_embedding(m, p, q)
    bf = standard_crossing(2, p, half, q)
    bj = standard_crossing(color, p, half, q)
    # U and Jones--Wenzl recursion in the original fundamental tensor basis.
    u = (pow(half, 1, p) * np.eye(4, dtype=np.int64) - bf) * half % p
    projector = np.eye(1, dtype=np.int64)
    for r in range(1, m + 1):
        projector = np.kron(projector, np.eye(2, dtype=np.int64))
        if r > 1:
            local = embedded_local(u, r - 2, r, p)
            ratio = qinteger(r - 1, q, p) * pow(qinteger(r, q, p), -1, p) % p
            projector = (projector - ratio * (projector @ local % p) @ projector) % p
    assert np.array_equal(projector @ projector % p, projector)
    assert np.array_equal(projector @ jmap % p, jmap)
    assert rank(projector, p) == color
    for i in range(m - 1):
        local = embedded_local(u, i, m, p)
        assert not np.any(local @ jmap % p)
        assert not np.any(local @ projector % p)
        assert not np.any(projector @ local % p)
    assert int(np.trace(ktot @ projector) % p) == qinteger(color, q, p)
    jj = np.kron(jmap, jmap) % p
    tile = cable([1], m)
    for sign in (1, -1):
        elementary = bf if sign > 0 else inverse(bf, p)
        word = tile if sign > 0 else list(reversed(tile))
        result = jj.copy()
        for i in reversed(word):
            result = local_apply(elementary, i - 1, 2 * m, result, p)
        expected = jj @ (bj if sign > 0 else inverse(bj, p)) % p
        assert np.array_equal(result, expected)
    # Strip and then restore the scalar independently in the defining family.
    stripped, _, _, _ = color_matrices(color, p, q, pow(q, m, p))
    assert np.array_equal(bj, pow(half, m * m, p) * stripped % p)
    theta = pow(half, m * (m + 2), p)
    assert theta * pow(pow(half, m * m, p), -1, p) % p == pow(q, m, p)
    return {"level": level, "color": color, "fundamental_heads": 2 * m,
            "literal_signed_cable_restriction": True,
            "actual_generator_intertwining": True,
            "JW_image_and_quantum_trace": True,
            "full_Cartan_and_twist_retained": True}


def sparse_cut(dimension, p, positive, negative, pivotal, strands, word, input_index=0):
    out = np.zeros(dimension, dtype=np.int64)
    gates = {}
    for sign, matrix in ((1, positive), (-1, negative)):
        for a, b in product(range(dimension), repeat=2):
            column = matrix[:, a * dimension + b]
            gates[sign, a, b] = [(divmod(int(r), dimension), int(column[r]))
                                  for r in np.flatnonzero(column)]
    for closed in product(range(dimension), repeat=strands - 1):
        initial = (input_index,) + closed
        paths = {initial: 1}
        for i, sign in reversed(word):
            following = {}
            for state, value in paths.items():
                for pair, scalar in gates[sign, state[i], state[i + 1]]:
                    new = state[:i] + pair + state[i + 2:]
                    following[new] = (following.get(new, 0) + value * scalar) % p
            paths = following
        weight = 1
        for a in closed:
            weight = weight * int(pivotal[a, a]) % p
        for a in range(dimension):
            out[a] = (int(out[a]) + weight * paths.get((a,) + closed, 0)) % p
    return out


def knot_permutation(strands, word):
    labels = list(range(strands))
    for i, _ in word:
        labels[i], labels[i + 1] = labels[i + 1], labels[i]
    seen = set()
    i = 0
    while i not in seen:
        seen.add(i)
        i = labels[i]
    return len(seen) == strands


def quotient_case(level):
    p, half, q = field(level)
    words = ((2, [(0, 1)] * 3),
             (2, [(0, -1)] * 3),
             (3, [(0, 1), (1, -1)] * 2),
             (3, [(0, 1)] * 3 + [(1, 1)]),
             (4, [(0, 1), (1, -1), (2, 1)]),
             (4, [(0, 1), (1, -1), (2, 1), (0, -1), (1, 1)]))
    knot_words = [(b, w) for b, w in words if knot_permutation(b, w)]
    comparisons = 0
    for color in range(1, level):
        m = color - 1
        x = pow(q, m, p)
        big, bigi, gp, tad = color_matrices(level, p, q, x)
        small, smalli, _, _ = color_matrices(color, p, q, x)
        projection = np.zeros((color, level), dtype=np.int64)
        projection[:, :color] = np.eye(color, dtype=np.int64)
        pp = np.kron(projection, projection)
        for left, right in ((big, small), (bigi, smalli)):
            assert np.array_equal(pp @ left % p, right @ pp % p)
        eps = pow(-1, m, p)
        ordinary_pivot = np.diag([x * pow(q, -2 * a, p) % p
                                  for a in range(color)]).astype(np.int64)
        assert np.array_equal(gp[:color, :color], eps * ordinary_pivot % p)
        assert tad == eps * x % p
        for b, word in knot_words:
            if level > 5 and b == 4:
                continue
            writhe = sum(sign for _, sign in word)
            assert (writhe - (b - 1)) % 2 == 0
            for a in range(min(color, 2)):
                actual = sparse_cut(level, p, big, bigi, gp, b, word, a)[:color]
                actual = actual * pow(tad, -writhe, p) % p
                ordinary = sparse_cut(color, p, small, smalli, ordinary_pivot, b, word, a)
                ordinary = ordinary * pow(x, -writhe, p) % p
                assert np.array_equal(actual, ordinary)
                assert not np.any(np.delete(actual, a))
                comparisons += 1
        # A separate component is a genuine exclusion: its U-sector can close.
        if color == 1:
            full_link = sparse_cut(level, p, big, bigi, gp, 2, [], 0)[0]
            small_link = sparse_cut(1, p, small, smalli, ordinary_pivot, 2, [], 0)[0]
            assert full_link == 0 and small_link == 1
    # Independently test the M -> -M descent away from the integer-color orbit.
    # The common alpha^2 Cartan scalar has cancelled with zero framing, so
    # these are the literal Laurent reduced cut matrices at x and -x.
    generic_x = int(sp.primitive_root(p))
    colors = [color_matrices(level, p, q, value) for value in (generic_x, -generic_x % p)]
    parity_tests = 0
    for b, word in knot_words:
        if b > 3:
            continue
        writhe = sum(sign for _, sign in word)
        results = []
        for positive, negative, pivotal, twist in colors:
            value = sparse_cut(level, p, positive, negative, pivotal, b, word, 0)
            results.append(value * pow(twist, -writhe, p) % p)
        assert np.array_equal(results[0], results[1])
        parity_tests += 1
    return {"level": level, "all_quotient_colors": level - 1,
            "typed_positive_negative_quotient_maps": True,
            "whole_knot_quotient_cut_comparisons": comparisons,
            "independent_generic_squared_meridian_descent_checks": parity_tests,
            "separate_component_failure_witness": True}


def main():
    quotient = [quotient_case(n) for n in range(2, 9)]
    cabling = [cabling_case(n, j) for n in range(3, 10)
               for j in range(2, min(n - 1, 5) + 1)]
    result = {"status": "PASS", "scope": "Actual quotient and literal cable identification; no volume estimate.",
              "quotient": quotient, "cabling": cabling}
    Path(__file__).with_name("actual_ordinary_color_comparison_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "quotient_levels": len(quotient),
                      "literal_signed_cable_families": len(cabling),
                      "whole_knot_cut_comparisons": sum(r["whole_knot_quotient_cut_comparisons"] for r in quotient)}))


if __name__ == "__main__":
    main()
