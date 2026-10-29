#!/usr/bin/env python3
"""Exact dual-cell and peripheral-curve diagnostics for the twist face data.

The normal-curve and cellular calculations use rational/integer arithmetic.
Regina, when requested, supplies additional independent recognition checks.
Finite samples are not a proof of all-parameter diagram identifications.
"""

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from twist_family_certificates import UnionFind, combinatorial_data, positive_angles, twist_faces

ANGLE_INDEX = {(0, 1): 0, (2, 3): 0, (0, 2): 1, (1, 3): 1, (0, 3): 2, (1, 2): 2}
BETA_WALKS = {
    "odd": [(0, 0, 1), (2, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 1),
            (0, 3, 2), (1, 3, 0), (0, 2, 0), (2, 2, 0), (1, 1, 0)],
    "even": [(0, 0, 1), (2, 0, 2), (0, 1, 2), (1, 2, 3), (2, 3, 1),
             (0, 3, 2), (1, 3, 1), (0, 2, 0), (2, 1, 0), (1, 0, 1)],
}


def permutations_sign(values):
    return (-1) ** sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))


def pairings(faces):
    occurrences = defaultdict(list)
    for t, row in enumerate(faces):
        for i, label in enumerate(row):
            occurrences[label].append((t, i))
    adjacency = {}
    for label, endpoints in occurrences.items():
        if len(endpoints) == 1:
            continue
        assert len(endpoints) == 2
        (t, i), (u, j) = endpoints
        permutation = {i: j}
        permutation.update(zip([v for v in range(4) if v != i], [v for v in range(4) if v != j]))
        inverse = {w: v for v, w in permutation.items()}
        adjacency[t, i] = u, j, permutation, label, 1
        adjacency[u, j] = t, i, inverse, label, -1
    return occurrences, adjacency


def dual_complex(faces):
    occurrences, adjacency = pairings(faces)
    labels = list(occurrences)
    assert all(len(endpoints) == 2 for endpoints in occurrences.values())
    label_index = {label: j for j, label in enumerate(labels)}
    N = len(faces)
    boundary1 = sp.zeros(N, len(labels))
    tree = []
    tet_components = UnionFind(range(N))
    for label, ((t, _), (u, _)) in occurrences.items():
        j = label_index[label]
        boundary1[t, j] -= 1
        boundary1[u, j] += 1
        if tet_components.find(t) != tet_components.find(u):
            tet_components.union(t, u)
            tree.append(j)
    local_edges = [(t, a, b) for t in range(N) for a, b in combinations(range(4), 2)]
    edge_classes = UnionFind(local_edges)
    for (t, i), (u, j, permutation, _, _) in adjacency.items():
        for a, b in combinations([v for v in range(4) if v != i], 2):
            c, d = sorted([permutation[a], permutation[b]])
            edge_classes.union((t, a, b), (u, c, d))
    groups = defaultdict(list)
    for edge in local_edges:
        groups[edge_classes.find(edge)].append(edge)
    groups = sorted(groups.values(), key=lambda group: sorted(group))
    boundary2 = sp.zeros(len(labels), len(groups))
    words = []
    for column, group in enumerate(groups):
        t, a, b = min(group)
        face = min(v for v in range(4) if v not in [a, b])
        initial = t, a, b, face
        state = initial
        visited = set()
        word = []
        while True:
            assert state not in visited
            visited.add(state)
            t, a, b, face = state
            u, entered, permutation, label, sign = adjacency[t, face]
            word.append((label, sign))
            boundary2[label_index[label], column] += sign
            a, b = sorted([permutation[a], permutation[b]])
            next_face = next(v for v in range(4) if v not in [a, b, entered])
            state = u, a, b, next_face
            if state == initial:
                break
            assert len(visited) <= 6 * N
        assert len(visited) == len(group)
        words.append(word)
    assert boundary1 * boundary2 == sp.zeros(N, len(groups))
    non_tree = [j for j in range(len(labels)) if j not in tree]
    reduced = boundary2[non_tree, :]
    smith = smith_normal_form(reduced, domain=sp.ZZ)
    return {"labels": labels, "index": label_index, "adjacency": adjacency,
            "boundary1": boundary1, "boundary2": boundary2, "tree": tree,
            "smith": [abs(int(smith[i, i])) for i in range(min(smith.shape))],
            "edge_words": words, "edge_groups": groups}


def cusp_next(adjacency, node, face):
    t, v = node
    assert face != v
    u, j, permutation, _, _ = adjacency[t, face]
    return (u, permutation[v]), j


def curve_arcs(adjacency, walk):
    arcs = []
    for k, (node, exit_face) in enumerate(walk):
        previous, previous_exit = walk[k - 1]
        arrived, entered = cusp_next(adjacency, previous, previous_exit)
        assert arrived == node and entered != exit_face
        arcs.append((node[0], node[1], entered, exit_face))
    return arcs


def curve_chain(complex_, walk):
    chain = sp.zeros(len(complex_["labels"]), 1)
    for (t, _), face in walk:
        _, _, _, label, sign = complex_["adjacency"][t, face]
        chain[complex_["index"][label]] += sign
    assert complex_["boundary1"] * chain == sp.zeros(complex_["boundary1"].rows, 1)
    return chain


def curve_holonomy(faces, signs, adjacency, walk):
    coefficients = sp.zeros(3 * len(faces), 1)
    for t, v, entered, exited in curve_arcs(adjacency, walk):
        lone = next(w for w in range(4) if w not in [v, entered, exited])
        others = [w for w in range(4) if w != v]
        permutation = [others.index(w) for w in [entered, exited, lone]]
        sign = signs[t] * (-1)**v * permutations_sign(permutation)
        angle = ANGLE_INDEX[tuple(sorted([v, lone]))]
        coefficients[3 * t + angle] += sign
    return coefficients


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def arc_coordinates(arc, fraction):
    _, vertex, entered, exited = arc
    others = [w for w in range(4) if w != vertex]
    points = dict(zip(others, [(sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), (sp.Integer(0), sp.Integer(1))]))

    def endpoint(face):
        a, b = [w for w in others if w != face]
        return tuple((1 - fraction) * points[a][k] + fraction * points[b][k] for k in range(2))

    return endpoint(entered), endpoint(exited)


def intersection(signs, adjacency, first, second):
    result = 0
    for a in curve_arcs(adjacency, first):
        for b in curve_arcs(adjacency, second):
            if a[:2] != b[:2]:
                continue
            x, y = arc_coordinates(a, sp.Rational(1, 3))
            u, v = arc_coordinates(b, sp.Rational(2, 3))
            dx = tuple(y[k] - x[k] for k in range(2))
            du = tuple(v[k] - u[k] for k in range(2))
            determinant = cross(dx, du)
            if determinant == 0:
                continue
            offset = tuple(u[k] - x[k] for k in range(2))
            t = cross(offset, du) / determinant
            s = cross(offset, dx) / determinant
            if 0 < t < 1 and 0 < s < 1:
                cusp_orientation = -signs[a[0]] * (-1)**a[1]
                result += cusp_orientation * int(sp.sign(determinant))
    return result


def uniform_homology_certificate(p, complex_):
    """Check the displayed all-p relation pattern, up to row signs/order."""
    labels = complex_["labels"]
    index = complex_["index"]
    tree_labels = [f"e{j}" for j in range(2, p + 2)] + ["r", "s"]
    tree_indices = [index[label] for label in tree_labels]
    forest = UnionFind(range(complex_["boundary1"].rows))
    for j in tree_indices:
        endpoints = [i for i in range(complex_["boundary1"].rows)
                     if complex_["boundary1"][i, j] != 0]
        assert len(endpoints) == 2 and forest.find(endpoints[0]) != forest.find(endpoints[1])
        forest.union(*endpoints)
    assert len({forest.find(i) for i in range(complex_["boundary1"].rows)}) == 1

    def vector(terms):
        result = sp.zeros(len(labels), 1)
        for label, coefficient in terms:
            result[index[label]] += coefficient
        return result

    def canonical(column):
        values = [int(column[j]) for j in range(len(labels)) if j not in tree_indices]
        first = next(value for value in values if value)
        return tuple(values if first > 0 else [-value for value in values])

    if p == 0:
        relations = [vector([("v", -1), ("g", -1)]),
                     vector([("v", 1), ("e1", -2), ("u", 1), ("g", -1)]),
                     vector([("v", 1), ("g", -1), ("e1", -1)])]
    else:
        f = lambda j: f"f{j}" if j else "e1"
        relations = [vector([(f(j), 1), (f(j - 1), -1)]) for j in range(1, p)]
        relations += [vector([(f(p), 1), (f(p - 1), -1), ("g", -1), ("v", 1)]),
                      vector([("g", 1), ("v", -1), (f(p), -1)]),
                      vector([("v", -1), ("g", -1)]),
                      vector([(f(j), 1) for j in range(1, p + 1)] + [("u", 1), ("e1", 2)])]
    assert Counter(canonical(column) for column in relations) == Counter(
        canonical(complex_["boundary2"][:, j]) for j in range(complex_["boundary2"].cols))
    generator = vector([("g", 1), ("v", -1), ("u", -2)]
                       + ([("e1", -2)] if p == 0 else [(f"f{p}", 2)]))
    assert complex_["boundary2"].T * generator == sp.zeros(p + 3, 1)
    return generator


def source_longitude_holonomy(p, parity):
    result = sp.zeros(3 * (p + 3), 1)
    U, V, W = p, p + 1, p + 2
    if parity == "odd":
        for t, angle, coefficient in [(U, 0, 2), (V, 0, -2), (V, 2, 2), (W, 1, -2)]:
            result[3 * t + angle] += coefficient
    else:
        for t, angle, coefficient in [(U, 0, -2), (V, 0, 2), (V, 1, -2), (W, 0, 2)]:
            result[3 * t + angle] += coefficient
    return result


def peripheral_audit(p, parity):
    faces, signs = twist_faces(p, parity)
    N = len(faces)
    data = combinatorial_data(faces, signs)
    complex_ = dual_complex(faces)
    assert complex_["smith"] == [1] * N
    uniform_homology_certificate(p, complex_)
    marked_meridian_certificate(p, parity)
    adjacency = complex_["adjacency"]
    # U_1: enter s, exit g; V_2: enter g, exit s.
    meridian = [((p, 1), 3), ((p + 1, 2), 1 if parity == "odd" else 0)]
    meridian_hol = curve_holonomy(faces, signs, adjacency, meridian)
    expected_meridian_hol = sp.zeros(3 * N, 1)
    expected_meridian_hol[3 * p] = 1 if parity == "odd" else -1
    expected_meridian_hol[3 * (p + 1)] = -expected_meridian_hol[3 * p]
    assert meridian_hol == expected_meridian_hol
    meridian_chain = curve_chain(complex_, meridian)
    cohomology_equations = complex_["boundary2"].T.col_join(
        sp.Matrix(len(complex_["tree"]), len(complex_["labels"]), lambda i, j: int(j == complex_["tree"][i]))
    ).col_join(meridian_chain.T)
    target = sp.zeros(cohomology_equations.rows, 1)
    target[-1] = 1
    cohomology, parameters = cohomology_equations.gauss_jordan_solve(target)
    assert parameters.rows == 0 and all(value.q == 1 for value in cohomology)
    candidate = [((p + t, v), f) for t, v, f in BETA_WALKS[parity]]
    beta_chain = curve_chain(complex_, candidate)
    beta_hol = curve_holonomy(faces, signs, adjacency, candidate)
    linking = (cohomology.T * beta_chain)[0]
    assert linking == (-3 if parity == "odd" else -2)
    assert intersection(signs, adjacency, meridian, candidate) == (1 if parity == "odd" else -1)
    longitude_chain = beta_chain - linking * meridian_chain
    longitude_certificate, parameters = complex_["boundary2"].gauss_jordan_solve(longitude_chain)
    assert parameters.rows == 0 and all(value.q == 1 for value in longitude_certificate)
    if parity == "odd":
        # The edge at U_01 is the fixed six-letter relation s u v^-1 r u^-1 g^-1.
        column = next(j for j, group in enumerate(complex_["edge_groups"]) if (p, 0, 1) in group)
        assert longitude_chain == -complex_["boundary2"][:, column]
    else:
        assert longitude_chain == sp.zeros(len(complex_["labels"]), 1)
    longitude_hol = beta_hol - linking * meridian_hol
    tetrahedra_constraints = sp.Matrix(N, 3 * N, lambda i, j: int(j // 3 == i))
    constraints = tetrahedra_constraints.col_join(data["incidence"])
    expected = source_longitude_holonomy(p, parity)
    # Explicit uniform certificates, not a fitted linear combination.
    explicit_constraints = sp.zeros(constraints.rows, 1)
    if parity == "odd":
        explicit_constraints[p], explicit_constraints[p + 1], explicit_constraints[p + 2] = 1, 2, -1
        s_row = next(j for j, group in enumerate(complex_["edge_groups"]) if (p, 0, 1) in group)
        explicit_constraints[N + s_row] = -1
    else:
        explicit_constraints[p + 1], explicit_constraints[p + 2] = -1, 1
    assert expected - longitude_hol == constraints.T * explicit_constraints
    assert (explicit_constraints.T * constraints * positive_angles(p, parity))[0] == 0
    match = None
    for orientation in [1, -1]:
        difference = expected - orientation * longitude_hol
        try:
            coefficients, parameters = constraints.T.gauss_jordan_solve(difference)
        except ValueError:
            continue
        coefficients = coefficients.subs({x: 0 for x in parameters})
        constant = (difference.T * positive_angles(p, parity))[0]
        match = orientation, coefficients, constant
        break
    assert match is not None
    orientation, coefficients, constant = match
    relative_candidate = [(t - p, v, face) for (t, v), face in candidate]
    return {
        "p": p, "parity": parity, "tetrahedra": N,
        "H1": "Z", "dual_relation_smith_diagonal": complex_["smith"],
        "meridian_normal_walk": [(t - p, v, face) for (t, v), face in meridian],
        "beta_normal_walk": relative_candidate,
        "meridian_beta_intersection": intersection(signs, adjacency, meridian, candidate),
        "beta_linking_number": int(linking),
        "longitude_orientation_for_source_formula": orientation,
        "source_longitude_branch_correction_over_pi": str(constant),
        "longitude_boundary_certificate": [int(x) for x in longitude_certificate],
        "face_cohomology_generator": {label: int(value) for label, value in zip(complex_["labels"], cohomology) if value != 0},
        "longitude_angle_constraint_coefficients": [str(value) for value in coefficients],
        "exact_peripheral_homology_checks": True,
        "uniform_relation_and_branch_certificates_checked": True,
        "meridian_separates_the_two_marked_edge_germs": True,
    }


def h_triangulation_faces(p, parity):
    faces, _ = twist_faces(p, parity)
    faces = list(faces)
    t, face = (p + 1, 1) if parity == "odd" else (p, 2)
    changed = list(faces[t])
    changed[face] = "s_prime"
    faces[t] = tuple(changed)
    return faces + [("m", "m", "s", "s_prime")]


def marked_meridian_certificate(p, parity):
    """Lift mu to the spherical vertex link of Y and separate the knot germs.

    The small component has 13 local corners, in the fixed body only. This
    checks a constant-size certificate for the actual meridian, not merely
    primitivity in H1(X).
    """
    faces = h_triangulation_faces(p, parity)
    _, adjacency = pairings(faces)
    Z = p + 3
    lifted = [((p, 1), 3), ((p + 1, 2), 1 if parity == "odd" else 0),
              ((Z, 1), 2 if parity == "odd" else 3)]
    isolated = {(t, v): next(w for w in range(4) if w not in [v, entered, exited])
                for t, v, entered, exited in curve_arcs(adjacency, lifted)}
    corners = [(t, v, w) for t in range(len(faces)) for v in range(4) for w in range(4) if v != w]
    components = UnionFind(corners)
    for t in range(len(faces)):
        for v in range(4):
            blocks = [[w for w in range(4) if w != v]]
            if (t, v) in isolated:
                lone = isolated[t, v]
                blocks = [[lone], [w for w in range(4) if w not in [v, lone]]]
            for block in blocks:
                for w in block[1:]:
                    components.union((t, v, block[0]), (t, v, w))
    for (t, face), (u, _, permutation, _, _) in adjacency.items():
        for v, w in combinations([v for v in range(4) if v != face], 2):
            components.union((t, v, w), (u, permutation[v], permutation[w]))
            components.union((t, w, v), (u, permutation[w], permutation[v]))
    assert len({components.find(corner) for corner in corners}) == 2
    selected_germ = (Z, 3, 2) if parity == "odd" else (Z, 2, 3)
    other_germ = (Z, 2, 3) if parity == "odd" else (Z, 3, 2)
    assert components.find(selected_germ) != components.find(other_germ)
    small = {corner for corner in corners if components.find(corner) == components.find(selected_germ)}
    complete_triangles = [(p, 3), (p + 2, 3), (Z, 3 if parity == "odd" else 2)]
    expected = {(t, v, w) for t, v in complete_triangles for w in range(4) if w != v}
    expected |= {(p, 1, 0), (p + 1, 2, 0), (p + 1, 2, 1), (Z, 1, 0)}
    assert small == expected and len(small) == 13


def regina_diagnostics(maximum):
    import regina

    def triangulate(faces):
        result = regina.Triangulation3()
        for _ in faces:
            result.newTetrahedron()
        _, adjacency = pairings(faces)
        for (t, face), (u, _, permutation, _, sign) in adjacency.items():
            if sign == 1:
                result.tetrahedron(t).join(face, result.tetrahedron(u),
                                          regina.Perm4(*[permutation[v] for v in range(4)]))
        return result

    marked_ball = triangulate([("m", "m", "s", "s_prime")])
    assert marked_ball.isValid() and marked_ball.recogniseHandlebody() == 0
    assert marked_ball.countBoundaryTriangles() == 2
    records = []
    for parity in ["odd", "even"]:
        for p in range(maximum + 1):
            faces, _ = twist_faces(p, parity)
            ideal = triangulate(faces)
            assert ideal.isValid() and ideal.isOrientable() and ideal.isIdeal()
            assert ideal.countVertices() == 1 and str(ideal.homology()) == "Z"
            closed = triangulate(h_triangulation_faces(p, parity))
            assert closed.isValid() and closed.countVertices() == 1 and closed.isSphere()
            records.append({"p": p, "parity": parity, "X_is_valid_one_cusp": True,
                            "X_isosig": ideal.isoSig(), "Y_is_S3": True})
    layer_records = []
    for p in range(1, maximum + 1):
        chain = [tuple(faces) for faces in twist_faces(p, "odd")[0][:p]]
        layered = triangulate(chain)
        structure = regina.LayeredSolidTorus.recogniseFromBase(layered.tetrahedron(0))
        assert structure is not None and layered.isSolidTorus()
        cuts = sorted(structure.meridinalCuts(j) for j in range(3))
        assert cuts == [1, p + 1, p + 2]
        assert sorted(structure.topFace(j) for j in range(2)) == [1, 2]
        layer_records.append({"p": p, "meridional_cuts": cuts})
    return {"regina_version": regina.versionString(), "marked_Z_is_a_ball": True,
            "finite_samples_only": True, "triangulations": records,
            "layered_solid_tori": layer_records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=8)
    parser.add_argument("--regina", action="store_true", help="also run optional independent 3-manifold recognition")
    arguments = parser.parse_args()
    assert arguments.max_p >= 0
    records = []
    for parity in ["odd", "even"]:
        for p in range(arguments.max_p + 1):
            records.append(peripheral_audit(p, parity))
    payload = {"scope": "Exact finite diagnostics for the separate uniform topological proof.", "records": records}
    if arguments.regina:
        payload["regina"] = regina_diagnostics(arguments.max_p)
    destination = Path(__file__).with_name("twist_topology_results.json")
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"exact_peripheral_cases_passed": len(records),
                      "maximum_p": arguments.max_p, "regina_checked": arguments.regina,
                      "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
