#!/usr/bin/env python3
"""Construct the published twist face pairings and independently check data.

Face pairings preserve vertex order. Gaussian and edge incidence matrices
are computed from these pairings, rather than transcribed inverse matrices.
Finite examples check the uniform algebraic proofs in the companion note.
"""

import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import sympy as sp


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)


def twist_faces(p, parity):
    assert p >= 0 and parity in ["odd", "even"]
    e = lambda j: "e" + str(j)
    f = lambda j: "f" + str(j) if j else e(1)
    faces = [(e(j), e(j + 1), f(j), f(j - 1)) for j in range(1, p + 1)]
    faces.append(("r", "v", "s", "g"))  # U
    if parity == "odd":
        faces += [("g", "s", f(p), "u"), ("u", "r", "v", e(p + 1))]
        signs = [1] * p + [-1, -1, -1]
    else:
        faces += [("s", "g", f(p), "u"), ("u", "v", "r", e(p + 1))]
        signs = [1] * p + [1, -1, -1]
    return faces, signs


def combinatorial_data(faces, signs):
    N = len(faces)
    labels = sorted({x for row in faces for x in row})
    assert len(labels) == 2 * N
    occurrences = defaultdict(list)
    for t, row in enumerate(faces):
        for i, label in enumerate(row):
            occurrences[label].append((t, i))
    assert all(len(x) == 2 for x in occurrences.values())
    vertices = UnionFind((t, v) for t in range(N) for v in range(4))
    local_edges = [(t, a, b) for t in range(N) for a, b in combinations(range(4), 2)]
    edges = UnionFind(local_edges)
    endpoint_corners = UnionFind((t, v, w) for t in range(N) for v in range(4) for w in range(4) if v != w)
    for (t, i), (u, j) in occurrences.values():
        assert signs[t] * (-1)**i == -signs[u] * (-1)**j
        source = [v for v in range(4) if v != i]
        target = [v for v in range(4) if v != j]
        permutation = dict(zip(source, target))
        for v in source:
            vertices.union((t, v), (u, permutation[v]))
        for a, b in combinations(source, 2):
            c, d = sorted([permutation[a], permutation[b]])
            edges.union((t, a, b), (u, c, d))
            endpoint_corners.union((t, a, b), (u, permutation[a], permutation[b]))
            endpoint_corners.union((t, b, a), (u, permutation[b], permutation[a]))
    classes = defaultdict(list)
    for edge in local_edges:
        classes[edges.find(edge)].append(edge)
    groups = sorted(classes.values(), key=lambda group: sorted(group))
    angle_index = {(0, 1): 0, (2, 3): 0, (0, 2): 1, (1, 3): 1, (0, 3): 2, (1, 2): 2}
    incidence = sp.zeros(len(groups), 3 * N)
    for row, group in enumerate(groups):
        for t, a, b in group:
            incidence[row, 3 * t + angle_index[a, b]] += 1
    X = []
    for i in range(4):
        X.append(sp.Matrix(N, len(labels), lambda t, k: int(faces[t][i] == labels[k])))
    face_A = (X[0] - X[1] + X[2]).col_join(X[2] - X[3])
    face_B = sp.zeros(N, N).col_join(sp.diag(*signs))
    r = X[0] * face_A.inv() * face_B
    Qf = -(r + r.T) / 2
    n_vertices = len({vertices.find(x) for x in vertices.parent})
    link_vertices = len({endpoint_corners.find(x) for x in endpoint_corners.parent})
    return {
        "face_A": face_A, "Qf": Qf, "incidence": incidence,
        "n_edges": len(groups), "n_vertices": n_vertices,
        "cusp_euler_characteristic": link_vertices - 6 * N + 4 * N,
    }


def predicted_gaussian(p, parity):
    N, U, V, W = p + 3, p, p + 1, p + 2
    Qf = sp.zeros(N, N)
    for i in range(p):
        for j in range(p):
            Qf[i, j] = min(i + 1, j + 1)
        Qf[i, U] = Qf[U, i] = i + 1
    if parity == "odd":
        Qf[U, U], Qf[U, V], Qf[V, U], Qf[V, V] = p + 2, -sp.Rational(3, 2), -sp.Rational(3, 2), 1
    else:
        Qf[U, U], Qf[U, V], Qf[V, U], Qf[V, V] = p + 1, sp.Rational(1, 2), sp.Rational(1, 2), -1
    Qf[U, W] = Qf[W, U] = 1
    Qf[V, W] = Qf[W, V] = -sp.Rational(1, 2)
    return Qf


def positive_angles(p, parity):
    # Angles are measured in units of pi; all calculations are rational.
    if p == 0:
        aligned = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)] if parity == "odd" else [sp.Rational(1, 6), sp.Rational(2, 3), sp.Rational(1, 6)]
        triples = []
    else:
        epsilon = sp.Rational(1, 12 * (p + 1)**2)
        triples = [[epsilon, 1 - epsilon * (j**2 + 1), epsilon * j**2] for j in range(1, p)]
        if parity == "odd":
            triples.append([sp.Rational(1, 2) - epsilon * (p**2 + 2 * p - 1) / 2,
                            sp.Rational(1, 2) - epsilon * (p - 1)**2 / 2, epsilon * p**2])
            aligned = [sp.Rational(1, 2) + epsilon * p**2 / 2, sp.Rational(1, 3), sp.Rational(1, 6) - epsilon * p**2 / 2]
        else:
            triples.append([sp.Rational(3, 4) - epsilon * (p**2 + 2 * p - 1) / 2,
                            sp.Rational(1, 4) - epsilon * (p - 1)**2 / 2, epsilon * p**2])
            aligned = [sp.Rational(1, 4) + epsilon * p**2 / 2,
                       sp.Rational(2, 3) - epsilon * p**2 / 3,
                       sp.Rational(1, 12) - epsilon * p**2 / 6]
    a, b, c = aligned
    triples += [[a, b, c], [a, b, c], [b, c, a]] if parity == "odd" else [[a, b, c], [a, c, b], [c, b, a]]
    assert all(sum(t) == 1 and all(0 < x < 1 for x in t) for t in triples)
    return sp.Matrix([x for triple in triples for x in triple])


def edge_and_peripheral_matrices(incidence, signs, parity):
    N = len(signs)
    G0 = incidence[:, 0::3]
    Gp = sp.zeros(incidence.rows, N)
    Gpp = sp.zeros(incidence.rows, N)
    for j, sign in enumerate(signs):
        Gp[:, j] = incidence[:, 3 * j + (2 if sign == 1 else 1)]
        Gpp[:, j] = incidence[:, 3 * j + (1 if sign == 1 else 2)]
    Aall, Ball = G0 - Gp, Gpp - Gp
    a_l, b_l = sp.zeros(1, N), sp.zeros(1, N)
    if parity == "odd":
        a_l[0, N - 3], a_l[0, N - 2], a_l[0, N - 1] = 2, -2, 2
        b_l[0, N - 2], b_l[0, N - 1] = 2, 2
    else:
        a_l[0, N - 3], a_l[0, N - 2], a_l[0, N - 1] = -2, 4, 2
        b_l[0, N - 2] = 2
    for omitted in range(Ball.rows):
        selected = [i for i in range(Ball.rows) if i != omitted]
        B = Ball[selected, :].col_join(b_l)
        if B.det() != 0:
            A = Aall[selected, :].col_join(a_l)
            return A, B, Aall, Ball, omitted
    raise AssertionError("No invertible edge/longitude B matrix")


def audit_reduced_state_conversion(data, signs, p, parity, A, B, omitted):
    N = p + 3
    incidence = data["incidence"]
    Gp = sp.zeros(N, N)
    for j, sign in enumerate(signs):
        Gp[:, j] = incidence[:, 3 * j + (2 if sign == 1 else 1)]
    selected = [i for i in range(N) if i != omitted]
    nu_over_pi = sp.Matrix([2 - sum(Gp[i, j] for j in range(N)) for i in selected] + [2])
    G = B.inv() * A
    c_over_pi = B.inv() * nu_over_pi - G * sp.ones(N, 1)
    expected_c = sp.Matrix([i * (2 * p - i + 1) for i in range(1, p + 1)]
                           + [p**2 + p + (2 if parity == "odd" else 4), -1, 1])
    assert c_over_pi == expected_c
    H = data["Qf"] - sp.diag(*[sp.Rational(1, 2) if sign == 1 else 0 for sign in signs])
    # Columns y'_1,...,y'_p,y'_U,y'_W,x; rows full positive-strip coordinates.
    transform = sp.zeros(N, N)
    for j in range(p):
        transform[j, j] = -1
    transform[p, p] = transform[p + 1, p] = 1 if parity == "odd" else -1
    transform[p + 1, p + 2] = 1
    transform[p + 2, p + 1] = 1
    inversion_gaussian = sp.zeros(N, N)
    for j in range(p):
        inversion_gaussian[j, j] = sp.Rational(1, 2)
    if parity == "even":
        inversion_gaussian[p, p] = sp.Rational(1, 2)
    reduced = transform.T * H * transform + inversion_gaussian
    target = sp.zeros(N, N)
    for i in range(p):
        for j in range(p):
            target[i, j] = min(i + 1, j + 1)
        target[i, p] = target[p, i] = (-1 if parity == "odd" else 1) * (i + 1)
    target[p, p] = p if parity == "odd" else p + 1
    target[p, p + 1] = target[p + 1, p] = sp.Rational(1, 2) if parity == "odd" else -sp.Rational(1, 2)
    target[p + 2, p + 2] = 1 if parity == "odd" else -1
    target[p + 2, p] = target[p, p + 2] = -sp.Rational(1, 2) if parity == "odd" else sp.Rational(1, 2)
    target[p + 2, p + 1] = target[p + 1, p + 2] = -sp.Rational(1, 2)
    assert reduced == target
    expected_W = sp.Matrix([-i * (2 * p - i + 1) for i in range(1, p + 1)]
                           + [p**2 + p + 1 if parity == "odd" else -(p**2 + p + 3), 1, -1])
    assert transform.T * c_over_pi == expected_W
    return {
        "exact_reduced_quadratic_and_linear_terms_checked": True,
        "derived_boundary_quadratic": "x*(x-y_U-y_W)" if parity == "odd" else "x*(y_U-y_W-x)",
        "agreement_with_odd_template_at_x_zero": True,
        "inversion_phase_power": p if parity == "odd" else p + 1,
    }


def main():
    records = []
    for parity in ["odd", "even"]:
        for p in range(9):
            faces, signs = twist_faces(p, parity)
            data = combinatorial_data(faces, signs)
            N = p + 3
            assert data["n_edges"] == N and data["n_vertices"] == 1
            assert data["cusp_euler_characteristic"] == 0
            assert data["Qf"] == predicted_gaussian(p, parity)
            angles = positive_angles(p, parity)
            assert data["incidence"] * angles == 2 * sp.ones(N, 1)
            A, B, Aall, Ball, omitted = edge_and_peripheral_matrices(data["incidence"], signs, parity)
            G = -2 * data["Qf"] + sp.diag(*[int(sign == 1) for sign in signs])
            assert A == B * G
            assert Aall == Ball * G
            p_vector = 2 * B.inv()[:, N - 1]
            expected_p = sp.zeros(N, 1)
            expected_p[N - 3], expected_p[N - 2] = -1, 1
            assert p_vector == expected_p
            conversion = audit_reduced_state_conversion(data, signs, p, parity, A, B, omitted)
            records.append({
                "parity": parity, "p": p, "twist_index": 2 * p + (3 if parity == "odd" else 2),
                "tetrahedra": N, "edge_classes": data["n_edges"],
                "ideal_vertices": data["n_vertices"], "cusp_euler_characteristic": 0,
                "face_matrix_determinant": int(data["face_A"].det()),
                "edge_longitude_B_determinant": int(B.det()),
                "omitted_edge_row": omitted,
                "minimum_explicit_angle_over_pi": str(min(angles)),
                "matrix_and_positive_angle_certificates_exact": True,
                "state_conversion": conversion,
            })
    result = {
        "source_faces": "Ben Aribi--Gueritaud--Piguet-Nakazawa arXiv:1903.09480v5, ordered X_n face equations",
        "scope": "Finite exact diagnostics for the uniform face and angle proofs; no claim that a finite sample proves all p or independently identifies the knot diagram.",
        "records": records,
    }
    Path(__file__).with_name("twist_family_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
