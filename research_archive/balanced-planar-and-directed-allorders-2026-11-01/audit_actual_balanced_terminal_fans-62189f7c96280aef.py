#!/usr/bin/env python3
"""Exact finite checks for the balanced terminal-fan construction.

Uses integer/Fraction arithmetic only. These checks reproduce finite
polynomial, oriented-incidence and endpoint-pairing identities. They do
not test a quantum invariant, a numerical circle packing, a saddle-point
asymptotic, or the analytic volume theorem.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

NVAR = 5

def poly_const(c):
    return {} if not c else {(0,) * NVAR: F(c)}

def var(i):
    v = [0] * NVAR
    v[i] = 1
    return {tuple(v): F(1)}

def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}

def scale(p, a):
    return {m: a*c for m, c in p.items() if a*c}

def mul(p, q):
    out = defaultdict(F)
    for m, a in p.items():
        for n, b in q.items():
            out[tuple(x+y for x, y in zip(m, n))] += a*b
    return {m: c for m, c in out.items() if c}

def square(p):
    return mul(p, p)

def reduce_t_square(p):
    # Variables are A,b,P,t,j, with t^2=Ab+P.
    out = {}
    for mon, coeff in p.items():
        if mon[3] < 2:
            out = add(out, {mon: coeff})
            continue
        m = list(mon)
        m[3] -= 2
        ab = m.copy()
        ab[0] += 1
        ab[1] += 1
        pp = m.copy()
        pp[2] += 1
        out = add(out, reduce_t_square({tuple(ab): coeff,
                                       tuple(pp): coeff}))
    return out

def edge(a, b):
    return tuple(sorted((a, b)))

def rotate(t, a):
    k = t.index(a)
    return t[k:] + t[:k]

class Sphere:
    def __init__(self):
        self.faces = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
        self.matching = {edge(0, 2), edge(1, 3)}
        self.mark = edge(0, 1)

    def incidence(self):
        out = defaultdict(list)
        for t in self.faces:
            for a, b in zip(t, t[1:] + t[:1]):
                out[edge(a, b)].append((a, b))
        return out

    def validate(self):
        inc = self.incidence()
        verts = set(v for t in self.faces for v in t)
        assert len(verts) - len(inc) + len(self.faces) == 2
        assert len(set(frozenset(t) for t in self.faces)) == len(self.faces)
        for directions in inc.values():
            assert len(directions) == 2
            assert directions[0] == directions[1][::-1]
        for t in self.faces:
            assert sum(edge(a, b) in self.matching
                       for a, b in zip(t, t[1:] + t[:1])) == 1
        assert self.mark in inc and self.mark not in self.matching
        self.parities()
        return len(verts)

    def parities(self):
        adj = defaultdict(list)
        for a, b in self.incidence():
            diff = int(edge(a, b) not in self.matching)
            adj[a].append((b, diff))
            adj[b].append((a, diff))
        values = {self.mark[0]: 0}
        queue = deque(values)
        while queue:
            a = queue.popleft()
            for b, diff in adj[a]:
                target = values[a] ^ diff
                if b in values:
                    assert values[b] == target
                else:
                    values[b] = target
                    queue.append(b)
        assert len(values) == len(adj)
        assert values[self.mark[1]] == 1
        return values

    def middle_counts(self):
        out = Counter()
        for t in self.faces:
            pair = next(e for e in self.matching if set(e) < set(t))
            out[next(a for a in t if a not in pair)] += 1
        return out

    def frame(self, x, y):
        ts = [t for t in self.faces if x in t and y in t]
        assert len(ts) == 2 and edge(x, y) in self.matching
        incoming = next(rotate(t, x) for t in ts if rotate(t, x)[2] == y)
        b = incoming[1]
        other = next(t for t in ts if set(t) != set(incoming))
        outgoing = rotate(other, y)
        assert outgoing[2] == x
        return b, outgoing[1], incoming

    def insert(self, x, y):
        before_parity = self.parities()
        before_middle = self.middle_counts()
        b, c, old = self.frame(x, y)
        w = self.validate()
        new = [(x, b, w), (b, y, w), (y, x, w)]
        self.faces.remove(next(t for t in self.faces if set(t) == set(old)))
        self.faces.extend(new)
        self.matching.add(edge(b, w))
        self.validate()
        bp, cp, _ = self.frame(x, y)
        assert (bp, cp) == (w, c)
        # Derive the NEW ordered quartet, do not compare only unordered faces.
        bi, co, _ = self.frame(b, w)
        assert (bi, co) == (y, x)
        new_parity = self.parities()
        assert all(new_parity[v] == val for v, val in before_parity.items())
        assert new_parity[w] == before_parity[b]
        delta = self.middle_counts()
        delta.subtract(before_middle)
        assert {v: k for v, k in delta.items() if k} == {
            b: -1, x: 1, y: 1, w: 1}
        return {"old_quartet": [x, b, y, c],
                "new_quartets": [[x, w, y, c], [b, y, w, x]],
                "new_vertex": w}

def canonical_pairing(p):
    return tuple(sorted(tuple(sorted(e)) for e in p))

I = canonical_pairing([(0, 3), (1, 2)])
X = canonical_pairing([(0, 2), (1, 3)])
H = canonical_pairing([(0, 1), (2, 3)])

def turn(p):
    return canonical_pairing([((a+1) % 4, (b+1) % 4) for a, b in p])

def stack(p, q):
    adj = defaultdict(list)
    for a, b in p:
        adj[('f', a)].append(('f', b))
        adj[('f', b)].append(('f', a))
    for a, b in q:
        adj[('g', a)].append(('g', b))
        adj[('g', b)].append(('g', a))
    for a, b in [(('f', 2), ('g', 1)), (('f', 3), ('g', 0))]:
        adj[a].append(b)
        adj[b].append(a)
    exposed = {('f', 0): 0, ('f', 1): 1, ('g', 2): 2, ('g', 3): 3}
    seen, pairs, internal = set(), [], 0
    for start in adj:
        if start in seen:
            continue
        comp, queue = set(), [start]
        while queue:
            a = queue.pop()
            if a in comp:
                continue
            comp.add(a)
            queue.extend(adj[a])
        seen |= comp
        ends = sorted(exposed[a] for a in comp if a in exposed)
        if not ends:
            internal += 1
        else:
            assert len(ends) == 2
            pairs.append(ends)
    return canonical_pairing(pairs), internal

def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)

def counts(u, v):
    z = (v-u)/2
    m = (z + F(1, 2)).numerator // (z + F(1, 2)).denominator
    L = max(0, -m, ceil_fraction((4-v)/2),
            ceil_fraction((4-u)/2-m))
    j, k = 2*(L+m), 2*L
    return j, k, u+j, v+k

def run():
    checks = []
    def check(name, predicate):
        if not predicate:
            raise AssertionError(name)
        checks.append(name)

    A,b,P,t,j = [var(i) for i in range(NVAR)]
    one = poly_const(1)
    b1 = add(b,A,scale(t,2))
    check("interstice square recurrence",
          not reduce_t_square(add(mul(A,b1),P,scale(square(add(t,A)),-1))))
    bj = add(b,scale(mul(j,t),2),mul(square(j),A))
    jp = add(j,one)
    bjp = add(b,scale(mul(jp,t),2),mul(square(jp),A))
    check("closed fan recurrence",
          not add(bj,A,scale(add(t,mul(j,A)),2),scale(bjp,-1)))
    check("closed normalized square",
          not reduce_t_square(add(mul(A,bj),P,scale(square(add(t,mul(j,A))),-1))))
    x,y,z = var(0),var(1),var(2)
    ap = add(x,y,z)
    for name, middle in [("x",x),("y",y)]:
        diff = add(mul(add(ap,x),add(ap,y)),scale(square(middle),-1))
        check("new-port algebraic balance "+name, all(c >= 0 for c in diff.values()))

    pi_upper = F(22,7)
    check("arctangent lower coefficient", F(18,5)-F(1,36)==F(643,180))
    check("log-ratio coefficient", 1/(1-F(1,64))==F(64,63))
    exact_gap = F(643,180)/pi_upper-F(64,63)
    check("strict balance rational margin", exact_gap==F(3347,27720)>0)
    checks_data = []
    values = [F(0),F(1,7),F(1,2),F(3),F(4),F(13,2),F(97,3)]
    for u in values:
        for v in values:
            a,c,U,V = counts(u,v)
            check("even fan algorithm %s,%s"%(u,v),
                  a >= 0 and c >= 0 and a%2==c%2==0
                  and U>=4 and V>=4 and abs(U-V)<=1)
            checks_data.append({"u":str(u),"v":str(v),"j":a,"k":c})

    sphere = Sphere()
    patches = []
    for _ in range(4):
        for x,y in [(0,2),(2,0),(1,3),(3,1)]:
            patches.append(sphere.insert(x,y))
    check("oriented stellar patches, original matching and protected edge",
          len(patches)==16 and sphere.validate()==20)

    check("odd pairing quarter-turn", turn(X)==X)
    check("odd pair stack", stack(X,X)==(I,0))
    check("identity on left", all(stack(I,p)==(p,0) for p in (I,X,H)))
    check("identity on right", all(stack(p,I)==(p,0) for p in (I,X,H)))
    parity_records = []
    for p in (I,X,H):
        left,right=p,p
        for step in range(1,17):
            left,cl=stack(X,left)
            right,cr=stack(right,X)
            check("no internal component %s %d"%(p,step),cl==cr==0)
            if step%2==0:
                check("even fan retains original local pairing %s %d"%(p,step),
                      left==right==p)
        parity_records.append({"original":[list(a) for a in p],
                               "after_16_left":[list(a) for a in left],
                               "after_16_right":[list(a) for a in right]})
    return {
        "status":"passed",
        "arithmetic":"exact integers and fractions; no floating point",
        "scope":{
            "proved_by_code":["finite polynomial recurrences",
                              "rational balance constants",
                              "oriented stellar patch, perfect matching and even coset",
                              "literal quarter-turn and stack endpoint pairings"],
            "not_proved_by_code":["circle-packing existence or metric completion",
                                  "full quantum source identity or trace normals",
                                  "uniform asymptotics or volume limit"],
            "algorithm_examples":"49 exact rational examples; the all-real algorithm is proved in the note",
            "topological_scope":"16 local stellar insertions in one simple sphere; arbitrary-exterior locality is proved in the note"},
        "check_count":len(checks),
        "checks":checks,
        "rational_gap_lower":str(exact_gap),
        "even_count_examples":checks_data,
        "ordered_patches":patches,
        "pairing_records":parity_records,
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).resolve().with_name("actual_balanced_terminal_fans_results.json"))
    args=parser.parse_args()
    result=run()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":result["status"],"check_count":result["check_count"],
                      "output":str(args.output)}))

if __name__=="__main__":
    main()
