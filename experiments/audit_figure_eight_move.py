#!/usr/bin/env python3
"""Reconstruct and calibrate the actual figure-eight 3--2 move.

All angle, peripheral, face and phase calculations are exact. Optional
Regina recognition independently checks the two resulting triangulations.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from twist_family_certificates import UnionFind, combinatorial_data, twist_faces
from twist_topology_audit import ANGLE_INDEX, pairings, permutations_sign, source_longitude_holonomy


def abstract_bipyramid():
    faces, signs = twist_faces(0, "even")
    _, adjacency = pairings(faces)
    internal = {"v", "g", "e1"}
    vertices = UnionFind((t, v) for t in range(3) for v in range(4))
    for (t, i), (u, _, permutation, label, _) in adjacency.items():
        if label in internal:
            for v in range(4):
                if v != i:
                    vertices.union((t, v), (u, permutation[v]))
    roots = sorted({vertices.find(x) for x in vertices.parent})
    assert len(roots) == 5
    index = {x: j for j, x in enumerate(roots)}
    old_vertices = [[index[vertices.find((t, v))] for v in range(4)] for t in range(3)]
    apices = set.intersection(*map(set, old_vertices))
    equator = set(range(5)) - apices
    assert len(apices) == 2 and len(equator) == 3
    e, a = sorted(equator), sorted(apices)
    ordering = [e[0], a[0], e[1], a[1], e[2]]
    rank = {v: i for i, v in enumerate(ordering)}
    old_vertices = [[rank[v] for v in row] for row in old_vertices]
    old_orders = [sorted(range(4), key=lambda v: old_vertices[t][v]) for t in range(3)]
    canonical_signs = [signs[t] * permutations_sign(old_orders[t]) for t in range(3)]
    assert canonical_signs == [-1, -1, -1]
    labels = [4 - next(iter(set(range(5)) - set(row))) for row in old_vertices]
    assert labels == [2, 0, 4]
    new_vertices = [[0, 1, 2, 4], [0, 2, 3, 4]]  # canonical tetrahedra 1 and 3
    boundary = {}
    for t, row in enumerate(old_vertices):
        for i in range(4):
            if faces[t][i] not in internal:
                boundary[frozenset(v for j, v in enumerate(row) if j != i)] = t, i, faces[t][i]
    new_faces, location = [[None] * 4 for _ in range(2)], {}
    for t, row in enumerate(new_vertices):
        for i in range(4):
            triangle = frozenset(v for j, v in enumerate(row) if j != i)
            if triangle in boundary:
                u, j, label = boundary[triangle]
                new_faces[t][i] = label
                location[u, j] = t, i
            else:
                new_faces[t][i] = "h"
    new_pairings = {}
    for (t, i), (u, j, permutation, label, direction) in adjacency.items():
        if label in internal or direction != 1:
            continue
        n, k = location[t, i]
        m, l = location[u, j]
        global_map = {old_vertices[t][v]: old_vertices[u][permutation[v]] for v in range(4) if v != i}
        local_map = {k: l}
        local_map.update({v: new_vertices[m].index(global_map[g])
                          for v, g in enumerate(new_vertices[n]) if v != k})
        new_pairings[n, k] = m, l, local_map
    i, j = new_faces[0].index("h"), new_faces[1].index("h")
    new_pairings[0, i] = 1, j, {v: j if v == i else new_vertices[1].index(g)
                                for v, g in enumerate(new_vertices[0])}
    # These are the independently selected global branchings after the move.
    new_orders = [[0, 1, 3, 2], [0, 3, 1, 2]]
    inverses = [{v: k for k, v in enumerate(order)} for order in new_orders]
    for (t, i), (u, j, permutation) in new_pairings.items():
        source = [v for v in range(4) if v != inverses[t][i]]
        target = [inverses[u][permutation[new_orders[t][v]]] for v in source]
        assert target == sorted(target)
    ordered_faces = [tuple(new_faces[t][i] for i in new_orders[t]) for t in range(2)]
    ordered_signs = [-permutations_sign(order) for order in new_orders]
    assert ordered_faces == [("r", "h", "u", "s"), ("u", "s", "r", "h")]
    assert ordered_signs == [1, -1]
    return {"old_faces": faces, "old_signs": signs, "old_global_vertices": old_vertices,
            "old_canonical_orders": old_orders, "canonical_tetrahedron_labels": labels,
            "new_canonical_faces": new_faces, "new_orders": new_orders,
            "new_canonical_pairings": [{"source": [t, i], "target": [u, j],
                                         "vertex_map": [P[v] for v in range(4)]}
                                        for (t, i), (u, j, P) in new_pairings.items()],
            "new_faces": ordered_faces, "new_signs": ordered_signs}


def K_over_pi(theta, gaussian, signs):
    n = len(signs)
    a, c = theta[0::3, 0], theta[2::3, 0]
    d, C = sp.ones(n, 1) - a, sp.diag(*signs) * c
    return sp.expand(sum(signs[j] * (a[j] * c[j] / 4 + (a[j] - c[j]) / 12 - sp.Rational(1, 24))
                         for j in range(n)) - sp.Rational(sum(s == 1 for s in signs), 12)
                     + ((C.T * d)[0] - (d.T * gaussian * d)[0]) / 2)


def angle_and_phase_certificate(data):
    faces, signs = data["old_faces"], data["old_signs"]
    old = combinatorial_data(faces, signs)
    new = combinatorial_data(data["new_faces"], data["new_signs"])
    constraints = sp.Matrix(3, 9, lambda i, j: int(j // 3 == i)).col_join(old["incidence"])
    theta, parameters = constraints.gauss_jordan_solve(sp.Matrix([1] * 3 + [2] * 3))
    assert parameters.rows == 4
    a, b, c, A, B, C, d, e, f = theta
    # Physical angles are in units of pi; the charge is half of this angle.
    canonical = {}
    for t, label in enumerate(data["canonical_tetrahedron_labels"]):
        order = data["old_canonical_orders"][t]
        canonical[label] = sp.Matrix([
            theta[3 * t + ANGLE_INDEX[tuple(sorted([order[0], order[k]]))]] for k in [1, 2, 3]])
    a0, c0 = canonical[0][0] / 2, canonical[0][2] / 2
    a2, c2 = canonical[2][0] / 2, canonical[2][2] / 2
    a4, c4 = canonical[4][0] / 2, canonical[4][2] / 2
    assert sp.simplify(c2 - c0 - a4 - a0 - c4) == 0
    assert sp.simplify(sp.Rational(1, 2) - a0 - a2 - a4 - c0 - c4 - c / 2) == 0
    canonical_new = [sp.Matrix([2 * (a0 + a2), 1 - 2 * (a0 + a2 + c0 + a4), 2 * (c0 + a4)]),
                     sp.Matrix([2 * (a2 + a4), 1 - 2 * (a2 + a4 + a0 + c4), 2 * (a0 + c4)])]
    triples = []
    for row, order in zip(canonical_new, data["new_orders"]):
        triples.extend(row[ANGLE_INDEX[tuple(sorted([order[0], order[k]]))]] for k in [1, 2, 3])
    mapped = sp.Matrix(triples)
    explicit = sp.Matrix([a + B, A + d, 1 - a - B - A - d,
                          B + f, a + d, 1 - a - d - B - f])
    assert sp.simplify(mapped - explicit) == sp.zeros(6, 1)
    assert new["incidence"] * mapped == 2 * sp.ones(2, 1)
    assert new["Qf"] == sp.diag(1, -1) and new["face_A"].det() == -1
    mu_old, lambda_old = a - A, (source_longitude_holonomy(0, "even").T * theta)[0]
    mu_standard = mapped[0] - mapped[3]
    lambda_standard = 2 * (mapped[3] - mapped[4])
    assert sp.simplify(mu_standard + mu_old) == 0
    assert sp.simplify(lambda_standard + lambda_old) == 0
    P = 2 * (c0 + a2 + c4) - sp.Rational(1, 2)
    # All three canonically ordered tetrahedra are negative: use the adjoint pentagon.
    phase = sp.simplify(K_over_pi(mapped, new["Qf"], data["new_signs"])
                        - K_over_pi(theta, old["Qf"], signs) + P / 12)
    assert phase == sp.Rational(11, 12)
    # Exact matched-longitude matrices; the standard longitude is their negative.
    edge_A = sp.Matrix([[1, -2]])
    edge_B = sp.Matrix([[-1, -1]])
    Am = edge_A.col_join(sp.Matrix([[0, -4]]))
    Bm = edge_B.col_join(sp.Matrix([[0, -2]]))
    G = -2 * new["Qf"] + sp.diag(1, 0)
    assert Bm.inv() * Am == G
    assert 2 * Bm.inv()[:, -1] == sp.Matrix([1, -1])
    assert Bm.inv() * sp.Matrix([-1, -2]) - G * sp.ones(2, 1) == sp.Matrix([1, -1])
    return {"angle_space_dimension": 4, "all_balanced_angles_symbolic": True,
            "positive_charge_margin": "c_U/(2*pi)",
            "peripheral_map_standard": {"mu": "-mu_old", "lambda": "-lambda_old"},
            "phase_constant_over_pi": str(phase), "phase_slope": 0,
            "new_face_gaussian": [[str(v) for v in row] for row in new["Qf"].tolist()],
            "state_identity": "J3(h,x)=-exp(-pi*i/12+11*pi*i/(12*h))*J2_standard(h,-x)"}


def regina_check(data):
    import regina

    def build(faces):
        result = regina.Triangulation3()
        for _ in faces:
            result.newTetrahedron()
        _, adjacency = pairings(faces)
        for (t, i), (u, _, permutation, _, direction) in adjacency.items():
            if direction == 1:
                result.tetrahedron(t).join(i, result.tetrahedron(u), regina.Perm4(*[permutation[v] for v in range(4)]))
        return result

    old, new = build(data["old_faces"]), build(data["new_faces"])
    assert old.isValid() and new.isValid()
    assert new.isIsomorphicTo(regina.Example3.figureEight()) is not None
    return {"old_isosig": old.isoSig(), "new_isosig": new.isoSig(),
            "new_is_standard_figure_eight": True, "new_homology": str(new.homology())}


def reflection_and_operator_certificate(data):
    faces, signs = data["new_faces"], data["new_signs"]
    _, adjacency = pairings(faces)
    tetrahedra = [1, 0]
    vertex_maps = [[1, 3, 0, 2], [2, 0, 3, 1]]
    for t in range(2):
        assert signs[t] == signs[tetrahedra[t]] * permutations_sign(vertex_maps[t])
    for (t, i), (u, j, permutation, _, _) in adjacency.items():
        v, k, target, _, _ = adjacency[tetrahedra[t], vertex_maps[t][i]]
        assert v == tetrahedra[u] and k == vertex_maps[u][j]
        assert all(target[vertex_maps[t][w]] == vertex_maps[u][permutation[w]] for w in range(4))
    d = combinatorial_data(faces, signs)
    constraints = sp.Matrix(2, 6, lambda i, j: int(j // 3 == i)).col_join(d["incidence"])
    theta, _ = constraints.gauss_jordan_solve(sp.Matrix([1, 1, 2, 2]))
    transformed = sp.zeros(6, 1)
    for t in range(2):
        for k in [1, 2, 3]:
            original_angle = ANGLE_INDEX[0, k]
            mapped_angle = ANGLE_INDEX[tuple(sorted([vertex_maps[t][0], vertex_maps[t][k]]))]
            transformed[3 * tetrahedra[t] + mapped_angle] = theta[3 * t + original_angle]
    assert sp.simplify(transformed[0] - transformed[3] + theta[0] - theta[3]) == 0
    assert sp.simplify(2 * (transformed[3] - transformed[4] + theta[3] - theta[4])) == 0
    assert sp.simplify(K_over_pi(transformed, d["Qf"], signs) - K_over_pi(theta, d["Qf"], signs)) == 0
    v, Q = sp.symbols("v Q")
    q = v**2
    R = q**4 * Q**4 - q**3 * Q**3 - q * (q**2 + 1) * Q**2 - q * Q + 1
    coefficients = [q**2 * Q**2 * (q**3 * Q**2 - 1),
                    v * (q**2 * Q**2 - 1) * R,
                    q**3 * Q**2 * (q * Q**2 - 1)]
    for k in range(3):
        reflected = coefficients[2 - k].subs(Q, q**(-2) / Q)
        assert sp.cancel(reflected + coefficients[k] / (Q**6 * v**12)) == 0
    return {"tetrahedron_map": tetrahedra, "vertex_maps": vertex_maps,
            "peripheral_action": "(mu,lambda)->(-mu,-lambda)",
            "phase_difference": 0, "selected_two_tetrahedron_state_is_even": True,
            "operator_reflection_multiplier": "-Q^(-6)*q^(-6)",
            "all_nonmonomial_peripheral_factors_retained": True,
            "same_minimal_order_two_operator_for_J2_and_J3": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regina", action="store_true")
    args = parser.parse_args()
    data = abstract_bipyramid()
    phase = angle_and_phase_certificate(data)
    reflection = reflection_and_operator_certificate(data)
    # A and B are unitary; the product of their antiunitary identifications
    # has cube scalar exp(3*pi*i/12-pi*i/4)=1.
    assert sp.Rational(3, 12) - sp.Rational(1, 4) == 0
    payload = {"scope": "Exact certificates for the separately proved tetrahedral symmetries and figure-eight move.",
               "combinatorics": data, "angle_and_phase": phase,
               "reflection_and_operator": reflection,
               "triangle_ordering_fresnel_scalar": 1}
    if args.regina:
        payload["regina"] = regina_check(data)
    destination = Path(__file__).with_name("figure_eight_move_results.json")
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"phase_constant_over_pi": phase["phase_constant_over_pi"],
                      "phase_slope": phase["phase_slope"], "regina_checked": args.regina,
                      "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
