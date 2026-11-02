#!/usr/bin/env python3
"""Exact finite mask/word/normalization checks, not a geometric proof."""
from argparse import ArgumentParser
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    own = [HERE / "check.py", *HERE.glob("*.tex"), *HERE.glob("figures/*.tex")]
    imports = [
        "papers/conway-geometry/main.tex", "papers/conway-geometry/maps.tex",
        "papers/conway-geometry/completion.tex",
        "papers/conway-fillings/main.tex", "papers/conway-fillings/deformation.tex",
        "papers/marked-fillings/main.tex",
        "papers/strict-newton-profiles/syntax.tex",
        "papers/strict-newton-profiles/variation.tex",
        "papers/strict-newton-profiles/profiles.tex",
    ]
    return sorted(set(own + [ROOT / p for p in imports]))


TYPES = {
    ("L", "L"): "A", ("L", "A"): "A", ("A", "L"): "A",
    ("A", "A"): "A", ("H", "L"): "H", ("L", "H"): "H",
    ("H", "A"): "H", ("A", "H"): "H",
}
TURN = {"L": "H", "H": "L", "A": "A"}
CLOSING = {("A", "A"), ("A", "L"), ("L", "A"),
           ("A", "H"), ("H", "A"), ("L", "H"), ("H", "L")}


def rotate(mask):
    return mask[1:] + mask[:1]


def output_mask(a, b):
    return (a[0], 0, b[2], 0)


def allowed_mask(typ, mask):
    if typ == "L":
        return mask[0] == mask[2] == 0
    if typ == "H":
        return mask[1] == mask[3] == 0
    return mask == (0, 0, 0, 0)


def masks():
    states = {("L", (0, 1, 0, 1))}
    while True:
        new = set(states)
        for typ, mask in states:
            new.add((TURN[typ], rotate(mask)))
        for (ta, ma), (tb, mb) in product(states, repeat=2):
            if (ta, tb) in TYPES:
                new.add((TYPES[ta, tb], output_mask(ma, mb)))
        if new == states:
            break
        states = new
    product_cases = root_cases = 0
    x, y, z = s.symbols("x y z")
    for typ, mask in states:
        assert allowed_mask(typ, mask)
        assert all(mask[j - 1] + mask[j] <= 1 for j in range(4))
    for (ta, ma), (tb, mb) in product(states, repeat=2):
        if (ta, tb) in TYPES:
            out = output_mask(ma, mb)
            assert allowed_mask(TYPES[ta, tb], out)
            assert ma[2] + mb[0] <= 1
            assert s.expand(1 - x - y + x - s.Rational(ma[2], 2)
                            + y - s.Rational(mb[0], 2)
                            - (1 - s.Rational(ma[2] + mb[0], 2))) == 0
            assert s.expand(z - x + x - s.Rational(ma[0], 2)
                            - (z - s.Rational(out[0], 2))) == 0
            assert s.expand(z - y + y - s.Rational(mb[2], 2)
                            - (z - s.Rational(out[2], 2))) == 0
            product_cases += 1
        if (ta, tb) in CLOSING:
            assert all(ma[j] + mb[(2 - j) % 4] <= 1 for j in range(4))
            root_cases += 1
    # A genuine asymmetric H state is lost by a pair-symmetric replacement.
    actual = output_mask((1, 0, 1, 0), (0, 1, 0, 1))
    assert actual == (1, 0, 0, 0) and ("H", actual) in states
    false_symmetric = (actual[0], 0, actual[0], 0)
    assert false_symmetric != actual
    # Replacing full reversal by a one-step rotation pairs two shaded sides.
    ma, mb = (0, 1, 0, 1), (1, 0, 1, 0)
    assert any(ma[j] + mb[(j + 1) % 4] == 2 for j in range(4))
    return {"reachable_states": sorted(states), "product_cases": product_cases,
            "closing_cases": root_cases, "negative_controls": 2}


PAIRINGS = {
    "I": ((0, 3), (1, 2)),
    "U": ((0, 1), (2, 3)),
    "X": ((0, 2), (1, 3)),
}


def stack_pairing(lower, upper):
    # Independent graph tracing of the physical two-strand stack.
    parent = list(range(8))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(i, j):
        parent[find(i)] = find(j)

    for i, j in PAIRINGS[lower]:
        join(i, j)
    for i, j in PAIRINGS[upper]:
        join(i + 4, j + 4)
    join(2, 5)
    join(3, 4)
    exposed = [0, 1, 6, 7]
    groups = {}
    for v in range(8):
        groups.setdefault(find(v), []).append(v)
    internal = sum(not any(v in exposed for v in group) for group in groups.values())
    output = sorted(tuple(i for i, v in enumerate(exposed) if find(v) == root)
                    for root in groups if any(find(v) == root for v in exposed))
    assert all(len(pair) == 2 for pair in output)
    label = next(k for k, pairs in PAIRINGS.items()
                 if sorted(tuple(sorted(p)) for p in pairs) == output)
    return label, internal


def pairings():
    expected = {
        ("I", "I"): ("I", 0), ("I", "U"): ("U", 0), ("I", "X"): ("X", 0),
        ("U", "I"): ("U", 0), ("U", "U"): ("U", 1), ("U", "X"): ("U", 0),
        ("X", "I"): ("X", 0), ("X", "U"): ("U", 0), ("X", "X"): ("I", 0),
    }
    actual = {(a, b): stack_pairing(a, b) for a, b in product(PAIRINGS, repeat=2)}
    assert actual == expected
    sets = {"A": {"I", "U"}, "B": {"I", "X"}, "C": {"U", "X"},
            "D": set(PAIRINGS)}
    for a, b in product(sets, repeat=2):
        surviving = {actual[x, y][0] for x in sets[a] for y in sets[b]
                     if actual[x, y][1] == 0}
        assert len(surviving) >= 2
    assert actual["U", "U"] != ("U", 0)
    return {"literal_pairings": {a + b: list(v) for (a, b), v in actual.items()},
            "set_pairs": 16, "negative_controls": 1}


def proj_equal(a, b):
    av, bv = list(a), list(b)
    return all(s.cancel(av[i] * bv[j] - av[j] * bv[i]) == 0
               for i in range(4) for j in range(i))


def W(E, R):
    return [
        s.Matrix([[1, 0], [0, E]]),
        s.Matrix([[1, E - 1], [0, E]]),
        s.Matrix([[E - R, R * (1 - E)], [E - 1, 1 - E * R]]),
        s.Matrix([[R, 0], [1 - E, E * R]]),
    ]


def word_checks():
    E, R, T = s.symbols("E R T", nonzero=True)
    ws = W(E, R)
    S = s.Matrix([[0, -E * R], [1, -1 - E]])
    Sbar = S.subs(E, 1 / E)
    A = s.Matrix([[R, -R], [1, E * R - 1 - E]])
    B = s.Matrix([[R / E - 1 - 1 / E, R], [-1, R]])
    checks = []
    for j, k in [(0, 0), (2, 2), (3, 1)]:
        checks.append(proj_equal(ws[j] * S, Sbar * ws[k]))
    for j, k in [(0, 2), (2, 0), (1, 3)]:
        checks.append(proj_equal(ws[j].inv() * B * ws[k].inv() * A, s.eye(2)))
    turn = s.Matrix([[0, R - 1], [1, -1]])
    closing = s.Matrix([[1, -R], [1, -1]])
    for j in range(4):
        checks.append(proj_equal(turn * ws[(j + 1) % 4],
                                 W(1 / E, 1 - R)[j] * turn))
        checks.append(proj_equal(closing * W(1 / E, R)[j],
                                 ws[(2 - j) % 4] * closing))
    assert all(checks)
    # A different closing corner order does not satisfy the recorded identity.
    assert not proj_equal(closing * W(1 / E, R)[0], ws[1] * closing)
    Z = (1 + E) / (1 + T)
    Rleaf = T * (1 + E)**2 / (E * (1 + T)**2)
    words = [matrix.applyfunc(s.cancel) for matrix in
             [ws[2].inv() * ws[0], S.inv(), A.inv() * ws[0], ws[0].inv() * B]]
    Q = (E * T - 1) / (E - T)
    wanted = [Q**2, 1 / T, Q / T, 1 / (T * Q)]
    for matrix, multiplier in zip(words, wanted):
        mat = matrix.subs(R, Rleaf).applyfunc(s.cancel)
        flag_image = (mat[0, 0] * Z + mat[0, 1]) / (mat[1, 0] * Z + mat[1, 1])
        assert s.cancel(flag_image - Z) == 0
        similarity = s.cancel(mat[1, 0] * Z + mat[1, 1])**2 / s.cancel(mat.det())
        assert s.cancel(similarity - multiplier) == 0
    return {"projective_word_identities": len(checks),
            "peripheral_flag_and_multiplier_pairs": 4, "negative_controls": 1}


def normalizations():
    c, eps, alpha, beta, r, u, v, p = s.symbols(
        "c eps alpha beta r u v p", real=True, nonzero=True)
    tau = 2 * s.I * c / (1 - eps * s.I * c)
    hess = -2 * s.pi * c / (1 - eps * s.I * c)
    assert s.cancel(hess - s.pi * s.I * tau) == 0
    assert s.cancel(-2 * hess - (-2 * s.pi * s.I * tau)) == 0
    # The packet half-ratio cannot replace the primitive ratio in this formula.
    assert s.cancel(hess - s.pi * s.I * tau / 2) != 0
    tau_tilde = alpha + s.I * beta
    V = -2 * s.pi * s.I * r * tau_tilde / (tau_tilde + r)
    assert s.simplify(s.re(V) - 2 * s.pi * r**2 * beta / ((alpha + r)**2 + beta**2)) == 0
    chi = u + s.I * v
    U = -2 * s.pi * s.I * chi
    Vcrit = 2 * s.pi * s.I * (chi - 1) / p
    correction = -s.re(U) * s.im(Vcrit) / 2
    action = 2 * s.pi * s.re(s.pi * s.I * (chi - 1)**2 / (2 * p))
    assert s.expand(correction - action) == 0
    return {"exact_identities": 4, "negative_controls": 1}


def main():
    global s
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Assertions must be enabled; no success record written.")
    import sympy as s
    paths = inputs()
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        raise SystemExit("Missing pinned input: " + ", ".join(missing))
    before = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    result = {"masks": masks(), "endpoint_pairings": pairings(),
              "projective_words": word_checks(), "normalizations": normalizations()}
    assert before == {str(p.relative_to(ROOT)): digest(p) for p in paths}, "Inputs changed"
    record = {
        "scope": "Exact finite mask closure, original endpoint graph, rational projective words and classical normalizations. No proof of variational existence, topology, convexity, completeness, analytic uniformity or volume comparison.",
        "input_sha256": before, "inputs_unchanged": True, "results": result,
        "python": sys.version.split()[0], "sympy": s.__version__,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
