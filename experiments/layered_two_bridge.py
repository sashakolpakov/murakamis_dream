#!/usr/bin/env python3
"""Build the folded four-punctured-sphere layering from an R/L word.

The construction follows the combinatorics in the appendix to
Gueritaud--Futer, arXiv:math/0406242. No hyperbolic solver is used by
layered_gluings(). Punctures keep the four labels 0,1,2,3 throughout
the product region. The ends are folded across opposite edge pairs.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from audit_two_bridge import branchings, ordered_faces, parity
from twist_family_certificates import combinatorial_data


MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def flip_sequence(word):
    assert len(word) >= 2 and set(word) <= {"R", "L"}
    classes = [0, 1]
    for i in range(1, len(word)):
        classes.append(classes[-2] if word[i] == word[i - 1]
                       else 3 - classes[-2] - classes[-1])
    return classes


def layered_gluings(word):
    classes = flip_sequence(word)
    n = 2 * (len(word) - 1)
    gluings = [([-1] * 4, [None] * 4) for _ in range(n)]

    def join(t, i, u, permutation):
        j = permutation[i]
        assert gluings[t][0][i] == gluings[u][0][j] == -1
        gluings[t][0][i], gluings[t][1][i] = u, list(permutation)
        inverse = [permutation.index(v) for v in range(4)]
        gluings[u][0][j], gluings[u][1][j] = t, inverse

    bottom = None
    for i, matching in enumerate(classes[1:-1]):
        next_top = {}
        initial_bottom = {}
        for half, pair in enumerate(MATCHINGS[matching]):
            t = 2 * i + half
            for opposite in range(4):
                if opposite in pair:
                    next_top[opposite] = t, opposite
                elif bottom is None:
                    initial_bottom[opposite] = t, opposite
                else:
                    u, j = bottom[opposite]
                    assert j == opposite
                    join(t, opposite, u, list(range(4)))
        if bottom is None:
            first_bottom = initial_bottom
        bottom = next_top
    for boundary, matching in ((first_bottom, classes[0]), (bottom, classes[-1])):
        # The faces opposite a and b meet at the *other* peripheral edge.
        # Folding fixes that common edge and interchanges a,b.
        for a, b in MATCHINGS[matching]:
            t, i = boundary[a]
            u, j = boundary[b]
            p = list(range(4))
            p[a], p[b] = b, a
            assert p[i] == j
            join(t, i, u, p)
    assert all(u >= 0 for neighbors, _ in gluings for u in neighbors)
    return gluings


def orientation_signs(gluings):
    signs = [None] * len(gluings)
    signs[0] = 1
    pending = [0]
    while pending:
        t = pending.pop()
        neighbors, maps = gluings[t]
        for i, u in enumerate(neighbors):
            value = -signs[t] * parity(maps[i])
            if signs[u] is None:
                signs[u] = value
                pending.append(u)
            else:
                assert signs[u] == value
    assert all(s is not None for s in signs)
    return signs


def regina_triangulation(gluings):
    import regina

    T = regina.Triangulation3()
    for _ in gluings:
        T.newTetrahedron()
    for t, (neighbors, maps) in enumerate(gluings):
        for i, u in enumerate(neighbors):
            if (t, i) < (u, maps[i][i]):
                T.tetrahedron(t).join(i, T.tetrahedron(u), regina.Perm4(*maps[i]))
    return T


def audit(word, limit):
    import snappy

    gluings = layered_gluings(word)
    old_signs = orientation_signs(gluings)
    T = regina_triangulation(gluings)
    M = snappy.Manifold(T.snapPea())
    n, singular, counts, certificate = len(gluings), 0, 0, None
    for orders in branchings(gluings, limit):
        counts += 1
        signs = [s * parity(p) for s, p in zip(old_signs, orders)]
        faces = ordered_faces(gluings, orders)
        try:
            data = combinatorial_data(faces, signs)
        except sp.matrices.exceptions.NonInvertibleMatrixError:
            singular += 1
            continue
        # The edge identity works with either consistent global orientation.
        inc = data["incidence"]
        def edge_check(signs, data):
            Gp, Gpp = sp.zeros(n, n), sp.zeros(n, n)
            for j, sign in enumerate(signs):
                Gp[:, j] = inc[:, 3*j + (2 if sign == 1 else 1)]
                Gpp[:, j] = inc[:, 3*j + (1 if sign == 1 else 2)]
            A, B = inc[:, 0::3] - Gp, Gpp - Gp
            G = -2 * data["Qf"] + sp.diag(*[int(s == 1) for s in signs])
            assert A == B * G
            assert B.rank() == n - T.countVertices()
        edge_check(signs, data)
        certificate = {"orders": orders, "faces": faces, "signs": signs,
                       "face_determinant": str(data["face_A"].det()),
                       "exact_edge_identity": True}
        break
    return {"word": word, "flip_classes": flip_sequence(word), "tetrahedra": n,
            "regina_isosig": T.isoSig(), "valid": T.isValid(),
            "orientable": T.isOrientable(), "ideal_vertices": T.countVertices(),
            "homology": str(T.homology()), "snappy_identification": [str(x) for x in M.identify()],
            "two_bridge_fraction": M.is_two_bridge(), "volume_numerical": float(M.volume()),
            "branchings_examined": counts, "singular_face_matrices": singular,
            "search_limit": limit, "proper_branching_certificate": certificate}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words", nargs="*", default=["RL", "RRL", "RRRL", "RRLR",
                                                       "RLRL", "RLRLRL", "RLRLRLRL"])
    parser.add_argument("--limit", type=int, default=10000)
    args = parser.parse_args()
    records = []
    for word in args.words:
        record = audit(word, args.limit)
        records.append(record)
        print(json.dumps({k: record[k] for k in ("word", "tetrahedra", "ideal_vertices",
              "snappy_identification", "branchings_examined", "singular_face_matrices")} |
              {"proper": record["proper_branching_certificate"] is not None}), flush=True)
    Path(__file__).with_name("layered_two_bridge_results.json").write_text(
        json.dumps({"scope": "Exact folded-layer combinatorics; solver output is numerical, finite samples are not a uniform proof.",
                    "records": records}, indent=2) + "\n")


if __name__ == "__main__":
    main()
