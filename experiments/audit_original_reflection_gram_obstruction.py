#!/usr/bin/env python3
"""Original-source reflection Gram obstruction and alternating weave block.

Exact finite fields check the original pivots and zero-framing factors.
The positive/Hermitian obstruction itself is proved over C in the note.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import physical_cap
from audit_actual_two_cut_ports import word_matrix
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def source_case(N, strands):
    p, _, q = field(N)
    Q, x = q*q % p, -pow(q, -1, p) % p
    plus, minus, _, theta = color_matrices(N, p, q, x)
    # The exact original zero-framing normalized braid generators.
    plus = plus*pow(theta, -1, p) % p
    minus = minus*theta % p
    K = np.diag([x*pow(Q, -a, p) % p for a in range(N)]).astype(np.int64)
    identity = np.eye(N**strands, dtype=np.int64)
    word = tuple(range(1, strands))
    W = word_matrix(word, plus, minus, strands, N, p)
    Wi = word_matrix(tuple(-j for j in reversed(word)), plus, minus, strands, N, p)
    assert np.array_equal(W@Wi % p, identity)
    values = [physical_cap(A, [K]*strands, N, p) for A in (identity, W, Wi)]
    assert values == [0, 1, 1]
    reflection_square = (2*identity-W-Wi) % p
    square_source = physical_cap(reflection_square, [K]*strands, N, p)
    assert square_source == -2 % p
    return {"N": N, "strands": strands, "field": p,
            "identity_source": 0, "normalized_unknot_word_source": 1,
            "inverse_word_source": 1, "reflection_square_source": -2}


def weave_case(N):
    p, _, q = field(N)
    Q, x = q*q % p, -pow(q, -1, p) % p
    plus, minus, _, _ = color_matrices(N, p, q, x)
    transfer = np.kron(plus, np.eye(N, dtype=np.int64))@np.kron(np.eye(N, dtype=np.int64), minus) % p
    states = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    indices = [(a*N+b)*N+c for a, b, c in states]
    block = transfer[np.ix_(indices, indices)]
    expected = np.array([[1-Q, 0, 1], [-q, 0, 0],
                         [0, -pow(q, -1, p), 1-pow(Q, -1, p)]], dtype=np.int64) % p
    assert np.array_equal(block, expected)
    assert np.array_equal(transfer[:, indices][[i for i in range(N**3) if i not in indices], :],
                          np.zeros((N**3-3, 3), dtype=np.int64))
    return {"N": N, "field": p, "literal_weight_one_block": True}


def symbolic_block():
    q = sp.symbols('q', nonzero=True)
    lam = sp.symbols('lam')
    Q = q*q
    T = sp.Matrix([[1-Q, 0, 1], [-q, 0, 0], [0, -1/q, 1-1/Q]])
    expected = (lam-1)*(lam**2-(1-Q-1/Q)*lam+1)
    assert sp.factor(T.charpoly(lam).as_expr()-expected) == 0
    return {"characteristic_polynomial": "(lambda-1)(lambda^2-(1-Q-Q^-1)lambda+1)",
            "scope": "Exact symbolic identity; complex positivity conclusions use the all-level proof."}


def main():
    source = [source_case(N, 2) for N in range(2, 13)]
    source += [source_case(N, 3) for N in range(2, 6)]
    source += [source_case(N, 4) for N in (2, 3)]
    weave = [weave_case(N) for N in range(2, 9)]
    result = {"status": "PASS", "original_source_cases": source,
              "alternating_transfer_cases": weave, "symbolic_block": symbolic_block(),
              "scope": "Obstruction to automatic universal original-source reflection positivity and positive weave transfer; no claim against positive scalar identities for a separately proved knot family."}
    Path(__file__).with_name("original_reflection_gram_obstruction_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "source_cases": len(source),
                      "weave_blocks": len(weave)}))


if __name__ == "__main__":
    main()
