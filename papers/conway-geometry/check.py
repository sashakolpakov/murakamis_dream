#!/usr/bin/env python3
"""Exact algebra checks for Pyramids, prisms, and complete geometry.

Rational identities and finite endpoint matchings only. This does not prove
convexity, identify a manifold, prove completeness, or verify the imported
stationary-point theorem. Requires SymPy. Run with assertions enabled.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sympy as sp


def clean(matrix):
    return matrix.applyfunc(sp.cancel)


def projective_equal(left, right):
    a, b = list(left), list(right)
    return all(sp.cancel(a[i] * b[j] - a[j] * b[i]) == 0
               for i in range(4) for j in range(i))


def chart(a, b, c):
    """Send a,b,c to 0,infinity,1; None denotes infinity."""
    if a is None:
        return sp.Matrix([[0, c-b], [1, -b]])
    if b is None:
        return sp.Matrix([[1, -a], [0, c-a]])
    if c is None:
        return sp.Matrix([[1, -a], [1, -b]])
    return sp.Matrix([[c-b, -a*(c-b)], [c-a, -b*(c-a)]])


def at(matrix, z):
    if z is None:
        return sp.cancel(matrix[0, 0]/matrix[1, 0])
    return sp.cancel((matrix[0, 0]*z+matrix[0, 1]) /
                     (matrix[1, 0]*z+matrix[1, 1]))


def white(e, r):
    return [sp.diag(1, e), sp.Matrix([[1, e-1], [0, e]]),
            sp.Matrix([[e-r, r*(1-e)], [e-1, 1-e*r]]),
            sp.Matrix([[r, 0], [1-e, e*r]])]


def local():
    e, r = sp.symbols("e r", nonzero=True)
    w = white(e, r)
    s = sp.Matrix([[0, -e*r], [1, -1-e]])
    a = sp.Matrix([[r, -r], [1, e*r-1-e]])
    b = sp.Matrix([[r/e-1-1/e, r], [-1, r]])
    for i, j in [(0, 0), (2, 2), (3, 1)]:
        assert projective_equal(w[i]*s, s.subs(e, 1/e)*w[j])
    odd = [w[0].inv()*b*w[2].inv()*a,
           w[2].inv()*b*w[0].inv()*a,
           w[1].inv()*b*w[3].inv()*a]
    for product, scalar in zip(odd, [-r/e, -r/e, (r-1)/e]):
        assert clean(product-scalar*sp.eye(2)) == sp.zeros(2)
    turn = sp.Matrix([[0, r-1], [1, -1]])
    close = sp.Matrix([[1, -r], [1, -1]])
    for j in range(4):
        assert projective_equal(turn*w[(j+1) % 4],
                                white(1/e, 1-r)[j]*turn)
        assert projective_equal(close*white(1/e, r)[j],
                                w[(2-j) % 4]*close)
    # Exact complete cusp translations, with no numerical phase sampling.
    k = (1+e)/2
    normalize = sp.Matrix([[k, -k], [1, -e]])
    rc = (1+e)**2/(4*e)
    words = [s.inv(), w[2].inv()*w[0], a.inv()*w[0], w[0].inv()*b]
    translations = [e-1, -2*(e+1), -2, 2*e]
    for word, translation in zip(words, translations):
        actual = normalize.inv()*word.subs(r, rc)*normalize
        assert projective_equal(actual, sp.Matrix([[1, translation], [0, 1]]))
    assert sp.cancel(translations[2]-(translations[0]+translations[1]/2)) == 0
    assert sp.cancel(translations[3]-(translations[0]-translations[1]/2)) == 0
    # Replacing the marked odd meridian by the pure one changes the word.
    assert not projective_equal(s.inv().subs(r, rc),
                                (a.inv()*w[0]).subs(r, rc))
    return {"pure_returns": 3, "odd_scalar_returns": 3,
            "turn_and_closure": 8, "complete_translations": 4,
            "half_shear_relations": 2, "wrong_meridian_rejected": True}


def prism():
    a, b, c = sp.symbols("a b c", nonzero=True)
    reciprocal = {a: 1/a, b: 1/b, c: 1/c}
    def reflected(x):
        if isinstance(x, sp.MatrixBase):
            return x.applyfunc(reflected)
        return sp.sympify(x).xreplace(reciprocal)
    p = sp.cancel(1+a-a*(a*b*(1+c)-1-a)/(a*a*b*b*c-a))
    coords = [None, p, 1, a, a*b, a*b*c]
    orders = [(2, 3, 1, 0), (0, 1, 4, 5), (2, 3, 4, 5)]
    phases = [b*c, a*b, a*b*c]
    worlds = []
    for order, phase in zip(orders, phases):
        values = [coords[i] for i in order]
        norm = chart(*values[:3])
        r = at(norm, values[3])
        worlds.append([clean(reflected(norm).adjugate()*w*norm)
                       for w in white(phase, r)])
    triangles = []
    for ids in [(1, 3, 4), (0, 2, 5)]:
        source = [coords[i] for i in ids]
        target = [None if z is None else reflected(z) for z in source]
        triangles.append(clean(chart(*target).adjugate()*chart(*source)))
    top, bottom = triangles
    f, g, out = worlds
    pairs = [(f[1], top), (g[1], top), (out[1], top),
             (f[3], bottom), (g[3], bottom), (out[3], bottom),
             (f[2], g[0]), (out[0], f[0]), (out[2], g[2])]
    assert all(projective_equal(x, y) for x, y in pairs)
    # Reversing only two output labels is not the ordered output map.
    wrong_norm = chart(coords[2], coords[4], coords[3])
    wrong_r = at(wrong_norm, coords[5])
    wrong = clean(reflected(wrong_norm).adjugate() *
                  white(a*b*c, wrong_r)[0] * wrong_norm)
    assert not projective_equal(wrong, f[0])
    return {"independent_phase_identities": 9,
            "wrong_order_rejected": True, "numerical_sampling": False}


PAIRINGS = {"I": [(0, 3), (1, 2)], "U": [(0, 1), (2, 3)],
            "X": [(0, 2), (1, 3)]}


def stack(first, second):
    adj = {i: [] for i in range(8)}
    for u, v in PAIRINGS[first] + [(u+4, v+4) for u, v in PAIRINGS[second]] + [(2, 5), (3, 4)]:
        adj[u].append(v)
        adj[v].append(u)
    exposed = {0: 0, 1: 1, 6: 2, 7: 3}
    seen, output, loops = set(), [], 0
    for start in range(8):
        if start in seen:
            continue
        todo, component = [start], set()
        while todo:
            v = todo.pop()
            if v in component:
                continue
            component.add(v)
            todo.extend(adj[v])
        seen |= component
        ends = sorted(exposed[v] for v in component if v in exposed)
        if not ends:
            loops += 1
        else:
            assert len(ends) == 2
            output.append(tuple(ends))
    key = next(k for k, pairs in PAIRINGS.items()
               if set(output) == {tuple(sorted(x)) for x in pairs})
    return key, loops


def endpoint_checks():
    expected = ["I", "U", "X", "U", "U", "U", "X", "U", "I"]
    for (first, second), result in zip(itertools.product(PAIRINGS, repeat=2), expected):
        assert stack(first, second) == (result, int(first == second == "U"))
    sets = {"A": {"I", "U"}, "B": {"I", "X"}, "C": {"U", "X"}}
    outcomes = {}
    for a, b in itertools.product(sets, repeat=2):
        result = {stack(x, y)[0] for x in sets[a] for y in sets[b]
                  if stack(x, y)[1] == 0}
        assert len(result) >= 2
        outcomes[a+b] = sorted(result)
    # The physical turn's tuple is (old1,old2,old3,old0).
    turn_expected = {"I": "U", "U": "I", "X": "X"}
    for key, pairs in PAIRINGS.items():
        turned = {tuple(sorted(((u-1) % 4, (v-1) % 4))) for u, v in pairs}
        assert turned == {tuple(sorted(x)) for x in PAIRINGS[turn_expected[key]]}
    return {"stack_pairs": 9, "two_choice_products": outcomes,
            "physical_turn_pairs": 3}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Assertions must be enabled; do not use -O.")
    paper = Path(__file__).resolve().parent
    root = paper.parents[1]
    files = sorted(paper.glob("*.tex")) + sorted((paper/"figures").glob("*.tex"))
    files += [Path(__file__).resolve(), root/"papers/newton-tangles/main.tex"]
    def hashes():
        return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in files}
    before = hashes()
    report = {"scope": __doc__, "local": local(), "prism": prism(),
              "endpoint_pairings": endpoint_checks(), "source_sha256": before}
    if hashes() != before:
        raise RuntimeError("A checked source changed during the run.")
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"output": str(args.output),
                      "finite_algebra_checks_completed": True}))


if __name__ == "__main__":
    main()
