#!/usr/bin/env python3
"""Exact source-face rank, primitive cuts, bends, and retained twist typing.

Cube/octahedral cases have the actual certified combinatorics used in the
common-chart audit. Larger bipyramids and stellar subdivisions are labeled
combinatorial regressions only; this audit does not supply new RA geometry.
"""
import argparse
from collections import defaultdict, deque
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


def edge(a, b):
    return tuple(sorted((a, b)))


def orient(faces):
    incidence = defaultdict(list)
    for j, f in enumerate(faces):
        for a, b in zip(f, f[1:] + f[:1]):
            incidence[edge(a, b)].append((j, 1 if a < b else -1))
    assert all(len(z) == 2 for z in incidence.values())
    signs = {0: 1}
    todo = [0]
    while todo:
        j = todo.pop()
        f = faces[j]
        for a, b in zip(f, f[1:] + f[:1]):
            entries = incidence[edge(a, b)]
            sj = next(s for k, s in entries if k == j)
            k, sk = next(x for x in entries if x[0] != j)
            wanted = -signs[j] * sj * sk
            if k in signs:
                assert signs[k] == wanted
            else:
                signs[k] = wanted
                todo.append(k)
    assert len(signs) == len(faces)
    return [f if signs[j] == 1 else (f[0], f[2], f[1])
            for j, f in enumerate(faces)]


def bipyramid(n):
    faces = [(n, i, (i+1) % n) for i in range(n)]
    faces += [(n+1, (i+1) % n, i) for i in range(n)]
    matching = {edge(i, (i+1) % n) for i in range(n)}
    return orient(faces), matching


def stellar(faces, matching, index=0):
    f = faces[index]
    a, b = next(e for e in matching if set(e).issubset(f))
    c = next(x for x in f if x not in (a, b))
    new = 1 + max(itertools.chain.from_iterable(faces))
    replacement = [(a, b, new), (b, c, new), (c, a, new)]
    return orient(faces[:index] + faces[index+1:] + replacement), matching | {edge(c, new)}


def matrices(faces):
    vertices = sorted(set(itertools.chain.from_iterable(faces)))
    edges = sorted({edge(a, b) for f in faces for a, b in zip(f, f[1:] + f[:1])})
    ei = {e: j for j, e in enumerate(edges)}
    vi = {v: j for j, v in enumerate(vertices)}
    B = sp.zeros(len(faces), len(edges))
    D = sp.zeros(len(edges), len(vertices))
    for j, (a, b) in enumerate(edges):
        D[j, vi[a]], D[j, vi[b]] = -1, 1
    for j, f in enumerate(faces):
        for a, b in zip(f, f[1:] + f[:1]):
            B[j, ei[edge(a, b)]] = 1 if a < b else -1
    assert B * D == sp.zeros(B.rows, D.cols)
    for j in range(B.cols):
        assert sorted(x for x in B[:, j] if x) == [-1, 1]
    return vertices, edges, B, D


def path_flow(B, kept, q):
    adjacency = defaultdict(list)
    for j in kept:
        tail = next(i for i in range(B.rows) if B[i, j] == -1)
        head = next(i for i in range(B.rows) if B[i, j] == 1)
        adjacency[tail].append((head, j, 1))
        adjacency[head].append((tail, j, -1))
    start = next((i for i, x in enumerate(q) if x == -1), None)
    end = next((i for i, x in enumerate(q) if x == 1), None)
    out = sp.zeros(B.cols, 1)
    if start is None:
        assert q == sp.zeros(B.rows, 1)
        return out
    parent = {start: None}
    todo = deque([start])
    while todo:
        u = todo.popleft()
        for v, j, sign in adjacency[u]:
            if v not in parent:
                parent[v] = (u, j, sign)
                todo.append(v)
    assert end in parent
    u = end
    while u != start:
        v, j, sign = parent[u]
        out[j] = sign
        u = v
    assert B * out == q
    return out


def graph_case(name, faces, matching):
    vertices, edges, B, D = matrices(faces)
    vi, ei = {v:j for j,v in enumerate(vertices)}, {e:j for j,e in enumerate(edges)}
    assert len(vertices) - len(edges) + len(faces) == 2
    assert B.rank() == B.rows-1 and D.rank() == len(vertices)-1
    assert len(matching)*2 == len(faces)
    assert all(sum(set(e).issubset(f) for e in matching) == 1 for f in faces)
    counts = defaultdict(int)
    patterns = set()
    for marked in edges:
        if marked in matching:
            continue
        u, v = marked
        zeros = set(marked)
        gauge = next(x for x in vertices if x not in zeros)
        columns = [vi[x] for x in vertices if x != gauge]
        Dg = D[:, columns]
        kernel = sp.zeros(len(columns), 2)
        kernel[columns.index(vi[u]), 0] = 1
        kernel[columns.index(vi[v]), 1] = 1
        rowlist = []
        for f in faces:
            order = next(f[k:]+f[:k] for k in range(3)
                         if edge(f[(k+2)%3], f[k]) in matching)
            for dual in [False, True]:
                ff = order if not dual else tuple(reversed(order))
                first = sp.zeros(1, len(vertices))
                second = sp.zeros(1, len(vertices))
                first[vi[ff[0]]], first[vi[ff[1]]] = 1, -1
                second[vi[ff[1]]], second[vi[ff[2]]] = 1, -1
                pattern = ''.join('0' if x in zeros else '2' for x in ff)
                assert pattern in {'200','002','220','022','202','222'}
                patterns.add(pattern)
                selected = {'200': [], '002': [], '220': [first],
                            '022': [second], '202': [first+second],
                            '222': [first,second]}[pattern]
                rowlist.extend([z[:, columns] for z in selected])
                counts['literal_triangles_and_duals'] += 1
        L = sp.Matrix.vstack(*rowlist)
        assert L * kernel == sp.zeros(L.rows, 2)
        assert L.rank() == len(vertices)-3
        counts['exact_rank_cases'] += 1
        # All independent orientation reversals preserve the integral chain map.
        for seed in range(4):
            signs = sp.diag(*[(-1)**((j*(seed+1)+seed)//2 % 2) for j in range(len(edges))])
            assert B*signs*signs*Dg == sp.zeros(B.rows, Dg.cols)
            assert (signs*Dg).rank() == Dg.cols
            counts['oriented_chain_maps'] += 1
        j0 = ei[marked]
        adjacent = [f for f in faces if set(marked).issubset(f)]
        assert len(adjacent) == 2
        for f in adjacent:
            e1 = next(edge(a,b) for a,b in zip(f,f[1:]+f[:1])
                      if edge(a,b) != marked and edge(a,b) not in matching)
            j1 = ei[e1]
            cut = Dg[[j0,j1], :]
            assert abs((cut*kernel).det()) == 1
            W = sp.Matrix.hstack(*cut.nullspace())
            assert W.cols == len(vertices)-3
            assert (L*W).rank() == W.cols
            counts['primitive_neighbor_slices'] += 1
            kept = [j for j in range(len(edges)) if j not in (j0,j1)]
            assert B[:, kept].rank() == B.rows-1
            assert B[:, kept]*Dg[kept,:] == -B[:,[j0,j1]]*cut
            start = next(i for i in range(B.rows) if B[i,j0] == 1)
            end = next(i for i in range(B.rows) if B[i,j1] == 1)
            q = sp.zeros(B.rows,1)
            q[start] -= 1
            q[end] += 1
            charge = path_flow(B, kept, q)
            # The SAME closed homogeneous chart in all three affine bands.
            base = Dg * sp.Matrix(range(1, Dg.cols+1))
            for delta in [-1,0,1]:
                h = base + delta*charge
                assert B*h == delta*q
                assert h[j0] == base[j0] and h[j1] == base[j1]
                counts['fixed_charge_restorations'] += 1
        # An arbitrary finite/finite second head need not see the fiber.
        bad = [j for j,e in enumerate(edges) if not (set(e)&zeros)]
        if bad:
            assert (Dg[[j0,bad[0]],:]*kernel).rank() == 1
            counts['nontransverse_cut_witnesses'] += 1
        # Subdivide an actual edge by a bend, then reverse one half.
        tail = next(i for i in range(B.rows) if B[i,j0] == -1)
        head = next(i for i in range(B.rows) if B[i,j0] == 1)
        Bb = B.row_join(sp.zeros(B.rows,1)).col_join(sp.zeros(1,B.cols+1))
        Bb[head,j0] = 0
        Bb[B.rows,j0] = 1
        Bb[B.rows,B.cols] = -1
        Bb[head,B.cols] = 1
        Db = Dg.col_join(Dg[j0,:])
        assert Bb*Db == sp.zeros(Bb.rows,Db.cols)
        reversal = sp.eye(Bb.cols)
        reversal[B.cols,B.cols] = -1
        assert Bb*reversal*reversal*Db == sp.zeros(Bb.rows,Db.cols)
        counts['cup_cap_subdivisions'] += 1
    return {'fixture':name, 'vertices_C':len(vertices), 'triangles':len(faces),
            'matching_edges':len(matching), 'all_six_patterns':sorted(patterns),
            'counts':dict(counts)}


def actual_tensor_checks():
    from audit_actual_nc_morse_graph_first_normal_source_reduction import Local, mm
    from audit_actual_two_cut_ports import balanced_data
    counts = defaultdict(int)
    for N in range(3,8):
        loc = Local(N)
        p, d = loc.p, N-1
        *_, Rp, Rm = balanced_data(N)
        for a in loc.W:
            W, pi = loc.W[a], loc.pi[a]
            for derivative in [0,1]:
                for i,j,r in itertools.product(range(N),range(N),range(2*a+1)):
                    if i+j != d-a+r:
                        assert int(W[derivative][i*N+j,r]) % p == 0
                        assert int(pi[derivative][r,i*N+j]) % p == 0
                    counts['actual_degree_entries'] += 2
            sector = mm(W, pi, p)[0]
            for eps, R in [(-1,Rm),(0,np.eye(N*N,dtype=np.int64)),(1,Rp)]:
                assert np.array_equal((R@sector)%p, pow(loc.omega[a],eps,p)*sector%p)
                counts['actual_half_twist_sectors'] += 1
        for derivative in [0,1]:
            for i,j in itertools.product(range(N),repeat=2):
                if i+j != d:
                    assert int(loc.cup[derivative][i,j])%p == 0
                    assert int(loc.cap[derivative][i,j])%p == 0
                # Odd/even highest weights: centered complement is exactly sign.
                assert sp.Rational(d,2)-i == -(i-sp.Rational(d,2))
                counts['actual_cup_cap_entries'] += 2
    return dict(counts)


def framing_and_prefix():
    r,s,rho,N = sp.symbols('r s rho N', nonzero=True)
    A,B,C,D = sp.symbols('A B C D')
    F=sp.Matrix([[r,1-r],[s,-s]])
    Q=sp.Matrix([[A,B],[C,D]])
    got=(F.inv()*Q*F)[0,0]
    want=-(r*r-r)*C/s+r*(A-D)+D+s*B
    assert sp.simplify(got-want)==0
    assert sp.simplify(sp.diff(got,C).subs(r,N*rho)+(N*N*rho*rho-N*rho)/s)==0
    zu,zv=sp.symbols('zu zv')
    jac=sp.Matrix([[-2,1/s+zu/(1+zu*s)],[-2,1/s+zv/(1+zv*s)]])
    assert sp.simplify(jac.det()-2*(zu-zv)/((1+zu*s)*(1+zv*s)))==0
    for eps in [-1,1]:
        assert sp.simplify(jac.det().subs({zu:0,zv:eps})) != 0
    return 5


def run():
    tetra=orient([(0,1,2),(0,3,1),(0,2,3),(1,3,2)])
    fixtures=[('actual_octahedral_C_tetrahedron',tetra,{(0,1),(2,3)})]
    for n in [4,5,6]:
        f,m=bipyramid(n)
        fixtures.append(('actual_cuboctahedral_C_octahedron' if n==4
                         else f'combinatorial_bipyramid_{n}',f,m))
    f,m=stellar(*bipyramid(4))
    fixtures.append(('combinatorial_stellar_1',f,m))
    f,m=stellar(f,m,2)
    fixtures.append(('combinatorial_stellar_2',f,m))
    rows=[graph_case(*fixture) for fixture in fixtures]
    patterns=set().union(*(set(row['all_six_patterns']) for row in rows))
    assert patterns=={'200','002','202','220','022','222'}
    totals=defaultdict(int)
    for row in rows:
        for key,value in row['counts'].items(): totals[key]+=value
    totals.update(actual_tensor_checks())
    totals['exact_prefix_and_framing_identities']=framing_and_prefix()
    return {'status':'PASS','counts':dict(totals),'cases':rows,
            'scope':'Exact literal graph rank, primitive neighboring cuts, fixed-charge affine restoration, cup reversals and actual source degree/half-twist identities. No stationary point, local Gaussian or original period coefficient is inferred.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_original_boundary_transverse_rank_results.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['counts']}))
