#!/usr/bin/env python3
"""Compare grouped Ward currents with full quotient contractions.

Internal edge indices are summed literally. Local traces use monic
polynomial division, including the double-root normals.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import mpmath as mp

from check_turn_trace_residue_density import (
    convolution, derivative, multiplication, original_polynomials,
    polynomial_value, relative,
)
from check_twist_period_insertion import original_matrices


def divide_linear(polynomial, center):
    quotient = [mp.mpf(0)]*(len(polynomial)-1)
    quotient[-1] = polynomial[-1]
    for k in reversed(range(1, len(polynomial)-1)):
        quotient[k-1] = polynomial[k]+center*quotient[k]
    return quotient


def matchings(edges, index=0, used=frozenset()):
    if index == len(edges):
        yield []
        return
    yield from matchings(edges, index+1, used)
    u, v = edges[index]
    if u not in used and v not in used:
        for tail in matchings(edges, index+1, used | {u, v}):
            yield [(u, v)]+tail


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    cases = [
        {"powers": [1, -3, 2], "edges": [(0, 1), (1, 2)],
         "external": [(0, 0), (0, 1), (2, 2)]},
        {"powers": [1, 3, -1, 5], "edges": [(0, 1), (1, 2), (2, 3)],
         "external": [(0, 0), (3, 1)]},
        {"powers": [1, 3, 5, -1], "edges": [(0, 1), (1, 2), (2, 3)],
         "external": []},
        {"powers": [1, 2, -3, 5], "edges": [(0, 1), (0, 2), (0, 3)],
         "external": [(1, 0), (2, 1), (3, 0)]},
        {"powers": [1, -3], "edges": [], "external": [(0, 0), (1, 0)]},
        {"powers": [1, 0, 3], "edges": [(0, 1), (1, 2)],
         "external": [(0, 0), (2, 1)]},
    ]
    points = [mp.mpc(".31", ".17"), mp.mpc("-.72", ".09"), mp.mpf("-1.4")]
    records = []
    cap_records = []
    determinant_records = []
    for level in range(2, 9):
        eta = (-1)**(level-1)
        sigma = -eta
        s1 = 2*mp.sin(mp.pi/level)
        rho = 1j*s1
        c0 = 2*mp.cos(mp.pi/level)
        relation, basis = original_polynomials(level)
        scale = eta*level**2
        unit = mp.matrix([1]+[0]*(level-1))
        identity = mp.eye(level)
        basis_matrix = mp.matrix([
            p+[mp.mpf(0)]*(level-len(p)) for p in basis]).T
        reversal = mp.matrix([[int(i+j == level-1) for j in range(level)]
                              for i in range(level)])
        turn = basis_matrix*reversal*(basis_matrix**-1)
        basis_multipliers = [multiplication(p, relation) for p in basis]
        h = divide_linear(divide_linear(relation, c0), c0)
        h0 = polynomial_value(h, c0)
        slope = polynomial_value(derivative(h), c0)/h0
        projector = [a/h0 for a in convolution(h, [1+slope*c0, -slope])]
        normal = [a/h0 for a in convolution(h, [-c0, 1])]
        projector += [mp.mpf(0)]*(level-len(projector))
        normal += [mp.mpf(0)]*(level-len(normal))
        turned_projector = list(turn*mp.matrix(projector))
        pw = [polynomial_value(turned_projector, z) for z in points]
        kernels = []
        for z in points:
            matrix = mp.matrix(level)
            for i in range(level):
                matrix += polynomial_value(basis[i], z)*basis_multipliers[i]
            kernels.append(matrix)
        for case_id, case in enumerate(cases):
            powers, edges, external = case["powers"], case["edges"], case["external"]
            ward_matrices = []
            vertex_base = []
            for v, n in enumerate(powers):
                coefficients = [
                    (1-(-1)**n)*projector[i]
                    +n*(level-1+(-1)**n*(level+1))/(2*rho)*normal[i]
                    for i in range(level)]
                wm = multiplication(coefficients, relation)
                ward_matrices.append(wm)
                for endpoint, point in external:
                    if endpoint == v:
                        wm = wm*kernels[point]
                vertex_base.append(wm)
            incident = [[i for i, edge in enumerate(edges) if v in edge]
                        for v in range(len(powers))]
            tables = []
            for v in range(len(powers)):
                table = {}
                for labels in itertools.product(range(level), repeat=len(incident[v])):
                    matrix = vertex_base[v]
                    for label in labels:
                        matrix = matrix*basis_multipliers[label]
                    table[labels] = scale*(matrix*unit)[level-1]
                tables.append(table)
            direct = mp.mpc(0)
            for labels in itertools.product(range(level), repeat=len(edges)):
                direct += mp.fprod(
                    tables[v][tuple(labels[i] for i in incident[v])]
                    for v in range(len(powers)))
            weights = []
            for v, n in enumerate(powers):
                ext = [point for endpoint, point in external if endpoint == v]
                if n % 2:
                    weights.append(2*mp.fsum(pw[point] for point in ext)
                                   +eta*(n*rho+2*(len(ext)-1)*c0))
                else:
                    weights.append(sigma*n*level*rho)
            eligible = [edge for edge in edges
                        if all(powers[v] % 2 for v in edge)]
            edge_weight = s1**2*(level**2-1)/3
            predicted = mp.mpc(0)
            for matching in matchings(eligible):
                used = {v for edge in matching for v in edge}
                predicted += edge_weight**len(matching)*mp.fprod(
                    weights[v] for v in range(len(powers)) if v not in used)
            error = relative(direct, predicted)
            if error >= tolerance:
                raise ArithmeticError((level, case_id, error))
            records.append({"N": level, "case": case_id,
                            "relative_residual": mp.nstr(error, 35)})
        original_crossing, _, _ = original_matrices(level)
        crossing = basis_matrix*original_crossing*(basis_matrix**-1)
        # Whole original three-vertex tree: independent Newton-index sum
        # versus all physical local residues and their matching determinant.
        full_powers = (2, -3, 4)
        full_matrices = [crossing**n for n in full_powers]
        direct_full = mp.mpc(0)
        for i, j in itertools.product(range(level), repeat=2):
            direct_full += (
                scale*(full_matrices[0]*basis_multipliers[i]*unit)[level-1]
                *scale*(full_matrices[1]*basis_multipliers[i]
                        *basis_multipliers[j]*unit)[level-1]
                *scale*(full_matrices[2]*basis_multipliers[j]*unit)[level-1])
        nodes = [2*mp.cos((2*j+1)*mp.pi/level)
                 for j in range((level-1)//2+1)]
        kernel_jets = {}
        for i, z in enumerate(nodes):
            for j, w in enumerate(nodes):
                vz = [polynomial_value(p, z) for p in basis]
                vw = [polynomial_value(p, w) for p in basis]
                dz = [polynomial_value(derivative(p), z) if len(p)>1 else 0
                      for p in basis]
                dw = [polynomial_value(derivative(p), w) if len(p)>1 else 0
                      for p in basis]
                kernel_jets[i, j] = (
                    mp.fsum(a*b for a, b in zip(vz, vw)),
                    mp.fsum(a*b for a, b in zip(dz, vw)),
                    mp.fsum(a*b for a, b in zip(vz, dw)),
                    mp.fsum(a*b for a, b in zip(dz, dw)))
        site_jets = []
        for matrix in full_matrices:
            coefficients = list(matrix*unit)
            slopes = derivative(coefficients)
            local = []
            for j, node in enumerate(nodes):
                value = polynomial_value(coefficients, node)
                if level % 2 and j == (level-1)//2:
                    local.append((value, mp.mpf(0)))
                else:
                    normal_value = polynomial_value(slopes, node)
                    local.append((eta*((4-node**2)*normal_value-node*value),
                                  eta*(4-node**2)*value))
            site_jets.append(local)
        determinant_full = mp.mpc(0)
        for colors in itertools.product(range(len(nodes)), repeat=3):
            monomers = [site_jets[v][colors[v]][0] for v in range(3)]
            normals = [site_jets[v][colors[v]][1] for v in range(3)]
            matrix = mp.matrix(3)
            edge_product = mp.mpf(1)
            for u, v in ((0, 1), (1, 2)):
                k, kx, ky, kxy = kernel_jets[colors[u], colors[v]]
                edge_product *= k
                monomers[u] += normals[u]*kx/k
                monomers[v] += normals[v]*ky/k
                weight = normals[u]*normals[v]*(k*kxy-kx*ky)/k**2
                matrix[u, v] = 1
                matrix[v, u] = -weight
            for v in range(3):
                matrix[v, v] = monomers[v]
            determinant_full += edge_product*mp.det(matrix)
        determinant_error = relative(direct_full, determinant_full)
        if determinant_error >= tolerance:
            raise ArithmeticError(("full determinant", level, determinant_error))
        determinant_records.append({
            "N": level, "powers": list(full_powers),
            "spectral_assignments": len(nodes)**3,
            "relative_residual": mp.nstr(determinant_error, 35)})
        w1 = multiplication([
            2*projector[i]-normal[i]/rho for i in range(level)], relation)
        pwm = multiplication(turned_projector, relation)
        for power in (3, 65):
            a = crossing**power*kernels[0]*unit
            f = turn*a
            hp = scale*a[level-1]
            target = scale*(crossing**(power-1)*kernels[0]*unit)[level-1]
            source = scale*(crossing*f)[level-1]
            current = scale*(w1*f)[level-1]
            expected_current = 2*scale*(pwm*a)[level-1]+1j*eta*s1*hp
            errors = [relative(source, target), relative(current, expected_current)]
            if max(errors) >= tolerance:
                raise ArithmeticError((level, power, errors))
            cap_records.append({"N": level, "power": power,
                                "maximum_relative_residual": mp.nstr(max(errors), 35)})
    return {
        "scope": "Exact finite quotient contraction and normalization diagnostics; no asymptotic gap is inferred from samples.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matching_checks": records,
        "endpoint_cap_checks": cap_records,
        "whole_tree_determinant_checks": determinant_records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    rendered = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
        print(f"Passed {len(result['matching_checks'])} matching contractions and "
              f"{len(result['endpoint_cap_checks'])} cap identities, plus "
              f"{len(result['whole_tree_determinant_checks'])} whole-tree "
              f"determinants; saved {args.output}.")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
