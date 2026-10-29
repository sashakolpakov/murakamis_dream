#!/usr/bin/env python3
"""Exact branching/matrix diagnostics for canonical two-bridge triangulations.

SnapPy supplies face pairings and peripheral incidence integers. All branching
constraints and face/edge comparisons below use exact integer/rational algebra.
Numerical canonicalization and shape solving are inputs, not geometric proofs.
This finite diagnostic does not establish a uniform two-bridge theorem.
"""

import argparse
import json
from itertools import permutations
from pathlib import Path

import sympy as sp

from twist_family_certificates import combinatorial_data


ORDERS = tuple(permutations(range(4)))
ANGLE_INDEX = {(0, 1): 0, (2, 3): 0, (0, 2): 1,
               (1, 3): 1, (0, 3): 2, (1, 2): 2}


def parity(order):
    return (-1)**sum(order[i] > order[j]
                     for i in range(4) for j in range(i + 1, 4))


def local_stokes_certificate():
    """Verify the universal six-edge identity used in the independent proof."""
    l01,l02,l03,l12,l13,l23,x0,x2,x3 = sp.symbols(
        "l01 l02 l03 l12 l13 l23 x0 x2 x3")
    phi = sp.Matrix([l23-l13,l23-l03,l13-l03,l12-l02])
    assert phi[0]-phi[1]+phi[2] == 0
    assert sp.expand(phi[2]-phi[3]-(l02+l13-l03-l12)) == 0
    x = [x0,x0+x2,x2,x3]
    psi = [l13-l12,l03-l02,l03-l01,l02-l01]
    stokes = sum((-1)**i*x[i]*psi[i] for i in range(4))
    assert sp.expand(stokes-((l02+l13-l03-l12)*x0
                            -(l01-l02)*(x2-x3))) == 0
    return True


def branchings(gluings, limit):
    """Solve local total-order compatibility, including self-glued faces."""
    n = len(gluings)
    constraints = []
    domains = [set(range(24)) for _ in range(n)]
    for t, (neighbors, maps) in enumerate(gluings):
        for face, u in enumerate(neighbors):
            p = maps[face]
            target = p[face]
            if (t, face) > (u, target):
                continue
            allowed = []
            for order in ORDERS:
                image = tuple(p[v] for v in order if v != face)
                allowed.append({j for j, other in enumerate(ORDERS)
                                if tuple(v for v in other if v != target) == image})
            if t == u:
                domains[t] &= {i for i in range(24) if i in allowed[i]}
            else:
                constraints.append((t, u, allowed))

    def propagate(current):
        changed = True
        while changed:
            changed = False
            for t, u, allowed in constraints:
                a = {i for i in current[t] if allowed[i] & current[u]}
                b = {j for j in current[u]
                     if any(j in allowed[i] for i in a)}
                if not a or not b:
                    return False
                if a != current[t] or b != current[u]:
                    current[t], current[u] = a, b
                    changed = True
        return True

    count = 0

    def visit(current):
        nonlocal count
        if count >= limit or not propagate(current):
            return
        free = [i for i in range(n) if len(current[i]) > 1]
        if not free:
            count += 1
            yield [ORDERS[next(iter(d))] for d in current]
            return
        t = min(free, key=lambda i: len(current[i]))
        for choice in sorted(current[t]):
            copied = [set(d) for d in current]
            copied[t] = {choice}
            yield from visit(copied)
            if count >= limit:
                return

    yield from visit(domains)


def ordered_faces(gluings, orders):
    labels = {}
    for t, (neighbors, maps) in enumerate(gluings):
        for i, u in enumerate(neighbors):
            if (t, i) not in labels:
                label = f"f{len(labels) // 2}"
                labels[t, i] = labels[u, maps[i][i]] = label
    return [tuple(labels[t, i] for i in order)
            for t, order in enumerate(orders)]


def transformed_incidence(raw_rows, orders):
    result = sp.zeros(len(raw_rows), 3 * len(orders))
    for t, order in enumerate(orders):
        for k in (1, 2, 3):
            old = ANGLE_INDEX[tuple(sorted((order[0], order[k])))]
            for row, values in enumerate(raw_rows):
                result[row, 3 * t + k - 1] = values[3 * t + old]
    return result


def matrix_certificate(faces, signs, raw_rows, orders):
    data = combinatorial_data(faces, signs)
    incidence = transformed_incidence(raw_rows, orders)
    n = len(faces)
    # SnapPy lists n edges and then the meridian and preferred longitude.
    assert incidence.rows == n + 2
    assert sorted(map(tuple, data["incidence"].tolist())) == sorted(
        map(tuple, incidence[:n, :].tolist()))
    Gp, Gpp = sp.zeros(n + 2, n), sp.zeros(n + 2, n)
    for j, sign in enumerate(signs):
        Gp[:, j] = incidence[:, 3 * j + (2 if sign == 1 else 1)]
        Gpp[:, j] = incidence[:, 3 * j + (1 if sign == 1 else 2)]
    Aall, Ball = incidence[:, 0::3] - Gp, Gpp - Gp
    G = -2 * data["Qf"] + sp.diag(*[int(s == 1) for s in signs])
    residual = Aall - Ball * G
    return {
        "face_determinant": str(data["face_A"].det()),
        "all_edge_rows_agree": residual[:n, :] == sp.zeros(n, n),
        "preferred_longitude_row_agrees": residual[-1, :] == sp.zeros(1, n),
        "meridian_residual": [str(v) for v in residual[-2, :]],
        "longitude_residual": [str(v) for v in residual[-1, :]],
        "edge_B_rank": Ball[:n, :].rank(),
        "edge_longitude_B_rank": Ball[:n, :].col_join(Ball[-1, :]).rank(),
        "gaussian": [[str(v) for v in row] for row in G.tolist()],
    }


def audit(manifold, limit):
    import snappy

    original = snappy.Manifold(manifold)
    M = original.canonical_retriangulation()
    gluings = M._get_tetrahedra_gluing_data()
    raw = [list(map(int, row)) for row in M.gluing_equations()]
    candidates, singular, certificates = 0, 0, []
    for orders in branchings(gluings, limit):
        candidates += 1
        faces = ordered_faces(gluings, orders)
        # SnapPy's (z,z',z'') use edge pairs (01,02,03); in the
        # literature convention this starting vertex order is negative.
        signs = [-parity(order) for order in orders]
        try:
            certificate = matrix_certificate(faces, signs, raw, orders)
        except sp.matrices.exceptions.NonInvertibleMatrixError:
            singular += 1
            continue
        certificate.update({"orders": orders, "faces": faces, "signs": signs})
        certificates.append(certificate)
        if certificate["all_edge_rows_agree"] and certificate["preferred_longitude_row_agrees"]:
            break
    return {
        "manifold": manifold, "two_bridge_fraction_snappy_convention": original.is_two_bridge(),
        "canonical_isosig": M.triangulation_isosig(decorated=False),
        "tetrahedra": len(gluings), "shape_solution_type_numerical": M.solution_type(),
        "branching_candidates_examined": candidates,
        "singular_face_matrices": singular, "search_limit": limit,
        "certificates": certificates,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifolds", nargs="*", default=["4_1", "5_2", "6_2", "6_3",
                        "7_3", "7_4", "7_5", "7_6", "7_7"])
    parser.add_argument("--limit", type=int, default=10000)
    args = parser.parse_args()
    records = []
    for name in args.manifolds:
        record = audit(name, args.limit)
        records.append(record)
        print(json.dumps({k: record[k] for k in ("manifold", "tetrahedra",
              "branching_candidates_examined", "singular_face_matrices")} |
              {"proper_certificates": len(record["certificates"]),
               "edge_longitude_agreement": any(c["all_edge_rows_agree"] and
                 c["preferred_longitude_row_agrees"] for c in record["certificates"])}),
              flush=True)
    payload = {"scope": "Finite exact matrix diagnostics, not a uniform geometric or two-bridge proof.",
               "universal_local_stokes_identity_exact": local_stokes_certificate(),
               "snappy_version": __import__("snappy").__version__, "records": records}
    Path(__file__).with_name("two_bridge_results.json").write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
