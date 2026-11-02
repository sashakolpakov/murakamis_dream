#!/usr/bin/env python3
"""Bounded checks of spatial conventions and labelled tangle bookkeeping.

The proof of ambient isotopy is written in the paper. Pairings and component
counts are necessary consequences, not a complete tangle invariant.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "build" / "check")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    summary = args.output / "summary.json"
    summary.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Assertions must be enabled; do not use -O or -OO.")
    sources = sorted(HERE.glob("*.tex")) + sorted((HERE / "figures").glob("*.tex"))
    sources += [Path(__file__).resolve(), HERE / "README.md"]
    before = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    spatial = check_spatial()
    pairing = check_pairings()
    normalized = check_normalization()
    after = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    assert before == after, "Source changed during the run"
    record = {
        "scope": "Finite spatial matrices, endpoint/component sewing, and independent junction partitions versus ordered symbolic fusion on bounded expressions",
        "excluded": ["ambient isotopy from endpoint pairings", "all-size termination from samples", "hyperbolic geometry", "quantum or asymptotic estimates"],
        "spatial": spatial,
        "pairings": pairing,
        "normalization": normalized,
        "source_sha256": before,
        "success": True,
    }
    summary.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary": str(summary), "spatial": spatial,
                      "pairings": pairing, "normalization": normalized}, sort_keys=True))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def mv(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(3)) for i in range(3))


IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
T = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
RHO = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
KAPPA = ((1, 0, 0), (0, -1, 0), (0, 0, -1))
TAU = ((-1, 0, 0), (0, 1, 0), (0, 0, -1))
REFLECT = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
PORTS = ((-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1))


def permutation(a):
    return tuple(PORTS.index(mv(a, p)) for p in PORTS)


def check_spatial():
    assert matmul(T, T) == TAU
    assert matmul(TAU, TAU) == IDENTITY
    assert matmul(RHO, T) == matmul(T, KAPPA)
    assert matmul(KAPPA, T) == matmul(T, RHO)
    assert matmul(TAU, T) == matmul(T, TAU)
    assert matmul(matmul(REFLECT, T), REFLECT) == matmul(T, TAU)
    assert permutation(T) == (3, 0, 1, 2)
    assert permutation(RHO) == (1, 0, 3, 2)
    assert permutation(KAPPA) == (3, 2, 1, 0)
    assert permutation(TAU) == (2, 3, 0, 1)
    assert permutation(REFLECT) == permutation(KAPPA)
    assert REFLECT != KAPPA
    # Same displayed permutation and T-conjugacy do not fix orientation.
    det = lambda a: sum(a[0][j] *
                        (a[1][(j + 1) % 3] * a[2][(j + 2) % 3]
                         - a[1][(j + 2) % 3] * a[2][(j + 1) % 3])
                        for j in range(3))
    assert det(REFLECT) == -1 and det(KAPPA) == 1
    return {"matrix_and_port_identities": 12, "wrong_gluing_control": True}


class DSU:
    def __init__(self, labels):
        self.parent = {i: i for i in labels}

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)


@dataclass(frozen=True)
class Pairing:
    pairs: tuple[tuple[int, int], ...]
    circles: int = 0


MATCHINGS = (Pairing(((0, 1), (2, 3))),
             Pairing(((0, 2), (1, 3))),
             Pairing(((0, 3), (1, 2))))
THROUGH = MATCHINGS[2]
CUPS = MATCHINGS[0]


def rotate(p, a):
    perm = permutation(a)
    return Pairing(tuple(sorted(tuple(sorted((perm[i], perm[j]))) for i, j in p.pairs)), p.circles)


def product(p, q):
    labels = [(b, i) for b in (0, 1) for i in range(4)]
    d = DSU(labels)
    for i, j in p.pairs:
        d.union((0, i), (0, j))
    for i, j in q.pairs:
        d.union((1, i), (1, j))
    d.union((0, 2), (1, 1))
    d.union((0, 3), (1, 0))
    external = ((0, 0), (0, 1), (1, 2), (1, 3))
    classes = {d.find(z) for z in labels}
    boundary = {d.find(z) for z in external}
    pairs = tuple((i, j) for i in range(4) for j in range(i + 1, 4)
                  if d.find(external[i]) == d.find(external[j]))
    assert len(pairs) == 2
    return Pairing(pairs, p.circles + q.circles + len(classes - boundary))


def close(p, flag="C"):
    d = DSU(range(4))
    for i, j in p.pairs:
        d.union(i, j)
    for i, j in (THROUGH if flag == "C" else CUPS).pairs:
        d.union(i, j)
    return len({d.find(i) for i in range(4)}) + p.circles


def braid(n):
    return THROUGH if n % 2 == 0 else MATCHINGS[1]


def check_pairings():
    cases = 0
    expanded = [Pairing(p.pairs, c) for p in MATCHINGS for c in range(3)]
    for f, g in itertools.product(expanded, repeat=2):
        assert close(product(rotate(f, T), g)) == close(product(f, rotate(g, T)))
        assert close(product(rotate(f, T), rotate(g, T))) == close(product(f, rotate(g, TAU)))
        assert close(product(f, g)) == close(product(g, f))
        assert close(product(f, g), "D") == close(f, "D") + close(g, "D") - 1
        for a in range(-3, 4):
            rotation = IDENTITY if a % 2 == 0 else RHO
            assert product(braid(a), f) == product(rotate(f, rotation), braid(a))
            cases += 1
    for f in expanded:
        assert close(product(CUPS, f)) == close(f, "D")
        assert close(rotate(f, T), "D") == close(rotate(f, TAU))
    for a, b in itertools.product(range(-5, 6), repeat=2):
        assert product(braid(a), braid(b)) == braid(a + b)
    assert close(braid(0)) == 2
    for s in range(-8, 9):
        assert close(braid(s), "D") == 1
        assert close(braid(s)) == 1 + (s % 2 == 0)
    assert close(product(CUPS, CUPS)) != close(product(THROUGH, CUPS))
    return {"matching_pairs": len(expanded) ** 2,
            "sliding_cases": cases, "integral_fusions": 121,
            "elementary_counts": 17, "zero_is_not_identity_control": True}


# The symbolic reducer below follows the physical moves. The graph construction
# after it uses incidence and bit contraction instead, without invoking it.
@dataclass(frozen=True)
class Leaf:
    labels: frozenset[int]
    weight: int


@dataclass(frozen=True)
class Turn:
    child: object


@dataclass(frozen=True)
class Stack:
    factors: tuple[object, ...]


def rot(e, which):
    if isinstance(e, Leaf):
        return e
    if isinstance(e, Turn):
        nxt = {"rho": "kappa", "kappa": "rho", "tau": "tau"}[which]
        return Turn(rot(e.child, nxt))
    fs = e.factors if which == "rho" else tuple(reversed(e.factors))
    return Stack(tuple(rot(f, which) for f in fs))


def clean(e):
    if isinstance(e, Leaf):
        return e
    if isinstance(e, Turn):
        c = clean(e.child)
        return clean(rot(c.child, "tau")) if isinstance(c, Turn) else Turn(c)
    fs = []
    for f in e.factors:
        z = clean(f)
        fs.extend(z.factors if isinstance(z, Stack) else (z,))
    return fs[0] if len(fs) == 1 else Stack(tuple(fs))


def integral(e):
    return isinstance(e, Turn) and isinstance(e.child, Leaf)


def normalize_open(e):
    e = clean(e)
    if isinstance(e, Leaf):
        return e
    if isinstance(e, Turn):
        return clean(Turn(normalize_open(e.child)))
    e = clean(Stack(tuple(normalize_open(f) for f in e.factors)))
    if not isinstance(e, Stack):
        return e
    if sum(integral(f) for f in e.factors) < 2:
        return e
    fs, labels, weight = [], set(), 0
    for f in e.factors:
        if integral(f):
            assert not labels.intersection(f.child.labels)
            labels.update(f.child.labels)
            weight += f.child.weight
        else:
            fs.append(rot(f, "rho") if weight % 2 else f)
    fs.append(Turn(Leaf(frozenset(labels), weight)))
    return clean(Stack(tuple(fs)))


TABLE = {("L", "L"): "A", ("L", "A"): "A", ("A", "L"): "A",
         ("A", "A"): "A", ("L", "H"): "H", ("H", "L"): "H",
         ("A", "H"): "H", ("H", "A"): "H"}


def kind(e):
    if isinstance(e, Leaf):
        return "L"
    if isinstance(e, Turn):
        return {"L": "H", "H": "L", "A": "A"}[kind(e.child)]
    z = kind(e.factors[0])
    for f in e.factors[1:]:
        z = TABLE[(z, kind(f))]
    return z


def unwrap_low(e):
    assert kind(e) == "L"
    if isinstance(e, Leaf):
        return Turn(e)
    assert isinstance(e, Turn)
    return e.child


def normalize_closed(e):
    old_count = len(leaves(e))
    for _ in range(old_count + 1):
        e = normalize_open(e)
        if integral(e):
            return e, "integral"
        assert isinstance(e, Stack)
        fs = e.factors
        if len(fs) >= 3:
            return e, "strict"
        a, b = map(kind, fs)
        if (a, b) != ("L", "L"):
            assert (a, b) != ("H", "H")
            return e, "strict"
        e = Stack((unwrap_low(fs[0]), rot(unwrap_low(fs[1]), "tau")))
    raise AssertionError("fusion budget exceeded")


def leaves(e):
    if isinstance(e, Leaf):
        return [e]
    if isinstance(e, Turn):
        return leaves(e.child)
    return [z for f in e.factors for z in leaves(f)]


def evaluate(e):
    if isinstance(e, Leaf):
        return rotate(braid(e.weight), T)
    if isinstance(e, Turn):
        return rotate(evaluate(e.child), T)
    p = evaluate(e.factors[0])
    for f in e.factors[1:]:
        p = product(p, evaluate(f))
    return p


def graph_blocks(e):
    assert isinstance(e, Stack)
    nodes, edges, labels = {0: "root"}, [], {}
    fresh = itertools.count(1)

    def attach(z, parent, bit):
        if isinstance(z, Turn):
            attach(z.child, parent, bit ^ 1)
        elif isinstance(z, Leaf):
            v = next(fresh); nodes[v] = "leaf"; labels[v] = z.labels
            edges.append((parent, v, bit ^ 1))
        else:
            v = next(fresh); nodes[v] = "product"; edges.append((parent, v, bit))
            fs = z.factors
            attach(fs[0], v, 0)
            attach(fs[1] if len(fs) == 2 else Stack(fs[1:]), v, 0)

    attach(e.factors[0], 0, 0)
    attach(e.factors[1] if len(e.factors) == 2 else Stack(e.factors[1:]), 0, 0)
    root_edges = [q for q in edges if q[0] == 0]
    assert len(root_edges) == 2
    (_, a, ba), (_, b, bb) = root_edges
    edges = [q for q in edges if q[0] != 0] + [(a, b, ba ^ bb)]
    del nodes[0]
    if len(labels) == 2:
        assert len(edges) == 1
        return [frozenset.union(*labels.values())] if edges[0][2] == 0 else list(labels.values())
    d = DSU(nodes)
    for a, b, bit in edges:
        if nodes[a] == nodes[b] == "product" and bit == 0:
            d.union(a, b)
    direct, ordinary = {}, []
    for a, b, bit in edges:
        if nodes[a] == "leaf": a, b = b, a
        if nodes[b] != "leaf": continue
        if bit:
            ordinary.append(labels[b])
        else:
            direct.setdefault(d.find(a), set()).update(labels[b])
    return ordinary + [frozenset(q) for q in direct.values()]


def random_expression(ids, rng):
    if len(ids) == 1:
        e = Leaf(frozenset(ids), 0)
    else:
        cut = rng.randrange(1, len(ids))
        e = Stack((random_expression(ids[:cut], rng), random_expression(ids[cut:], rng)))
    for _ in range(rng.randrange(4)):
        e = Turn(e)
    return e


def weights(e, values):
    if isinstance(e, Leaf):
        assert len(e.labels) == 1
        return Leaf(e.labels, values[next(iter(e.labels))])
    if isinstance(e, Turn):
        return Turn(weights(e.child, values))
    return Stack(tuple(weights(f, values) for f in e.factors))


def check_normalization():
    rng = random.Random(20261102)
    count = zeros = 0
    for m in range(2, 9):
        for _ in range(24):
            cut = rng.randrange(1, m)
            template = Stack((random_expression(list(range(cut)), rng),
                              random_expression(list(range(cut, m)), rng)))
            expected = set(graph_blocks(template))
            for _ in range(8):
                values = [rng.randrange(-4, 5) for _ in range(m)]
                source = weights(template, values)
                out, status = normalize_closed(source)
                ls = leaves(out)
                assert {l.labels for l in ls} == expected
                assert set().union(*(l.labels for l in ls)) == set(range(m))
                assert sum(map(len, (l.labels for l in ls))) == m
                for leaf in ls:
                    assert leaf.weight == sum(values[i] for i in leaf.labels)
                assert close(evaluate(source)) == close(evaluate(out))
                if status == "strict":
                    assert isinstance(out, Stack)
                    fs = out.factors
                    if len(fs) == 2:
                        assert (kind(fs[0]), kind(fs[1])) not in [("L", "L"), ("H", "H")]
                    else:
                        assert sum(integral(f) for f in fs) <= 1
                        for f in fs: kind(f)
                else:
                    assert len(ls) == 1 and ls[0].weight == sum(values)
                count += 1
                zeros += sum(l.weight == 0 for l in ls)
    return {"ordered_expressions_and_assignments": count, "label_counts": [2, 8],
            "zero_final_blocks_retained": zeros, "random_seed": 20261102,
            "independent_incidence_partition": True}


if __name__ == "__main__":
    main()
