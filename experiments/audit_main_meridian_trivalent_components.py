#!/usr/bin/env python3
"""Exact finite checks supporting the typed trivalent return comparison.

This standalone runner constructs the complete Newton polynomials and divides
their products by the actual monic relation P_0(z)+Delta. It does not construct
the trace by the proposed old/return formula. SymPy cyclotomic arithmetic then
compares the independently extracted top coefficient with that formula.

Finite algebra tests do not prove the simultaneous clamping inequality, a
uniform source gap, an asymptotic packet, or a volume theorem. The elementary
symbolic identities and the endpoint/type checks are recorded separately.

Requires Python 3 and SymPy. No repository or private-module imports.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations_with_replacement
import json
from math import factorial
from pathlib import Path

import sympy as sp


def monic_chebyshev(n, z):
    previous, current = sp.Integer(2), z
    for _ in range(1, n):
        previous, current = current, sp.expand(z * current - previous)
    return current


def multiplicity(indices):
    answer = factorial(len(indices))
    for count in Counter(indices).values():
        answer //= factorial(count)
    return answer


def exact_level(n):
    z, delta, root = sp.symbols("z Delta root")
    field = sp.QQ.algebraic_field(
        sp.CRootOf(sp.cyclotomic_poly(2*n, root), 0))
    q, zero, one = field.unit, field.zero, field.one
    d, middle = n-1, (n-1)//2
    constant = sp.Poly(1, z, delta, domain=field)
    variable = sp.Poly(z, z, delta, domain=field)
    modulus0 = sp.Poly(monic_chebyshev(n, z)+2, z, delta, domain=field)
    modulus = modulus0 + sp.Poly(delta, z, delta, domain=field)

    # S_k^2 is constructed as a product of 4 sin^2(pi*a/N).
    # T_k=prod(q^a-q^-a)=i^k S_k avoids adjoining a numerical square root.
    squared_factorial, T = [one], [one]
    basis = [constant]
    for a in range(1, n):
        denominator = 2-q**(2*a)-q**(-2*a)
        squared_factorial.append(squared_factorial[-1]*denominator)
        T.append(T[-1]*(q**a-q**(-a)))
        node = q**(2*a-1)+q**(-2*a+1)
        basis.append(
            basis[-1]*(constant.mul_ground(node)-variable)
            .mul_ground(one/denominator))
    assert squared_factorial[d] == field.convert(n*n)

    def trace_coefficients(poly, relation):
        remainder = poly.rem(relation)
        factor = field.convert((-1)**d*n*n)
        return {powers[1]: factor*coefficient
                for powers, coefficient in remainder.rep.to_dict().items()
                if powers[0] == d and coefficient}

    def old_formula(i, j, k):
        # This is mu_ij^(d-k), read only after constructing the quotient trace.
        r = d-k
        return T[i+j]*T[r]/(
            T[i]*T[j]*T[r-i]*T[r-j]*T[i+j-r])

    def return_formula(i, j, k):
        t = i+j+k-(2*n-1)
        denominator = T[i]*T[j]*T[k]*T[t]*T[i-t]*T[j-t]*T[k-t]
        # The seven S indices sum to 4N-2. Hence their T product
        # equals i^(4N-2) times their S product, i.e. its negative.
        Lambda = -field.convert(n*n)/denominator
        return -field.convert((-1)**(i+j+k-d))*Lambda

    counts = Counter()
    samples = {}
    maximum_offset = Fraction(0)
    for indices in combinations_with_replacement(range(n), 3):
        i, j, k = indices
        total = i+j+k
        order_count = multiplicity(indices)
        pair_sums = (i+j, i+k, j+k)
        is_old = max(pair_sums) <= d and total >= d
        is_return = min(pair_sums) >= n and total >= 2*n-1
        strict_old = (
            min(indices) > 0 and max(pair_sums) < d and total > d)

        polynomial = basis[i]*basis[j]*basis[k]
        direct = trace_coefficients(polynomial, modulus)
        complete = trace_coefficients(polynomial, modulus0)
        assert set(direct) <= {0, 1}, ("trace not affine", n, indices, direct)
        assert set(complete) <= {0}, ("complete trace degree", n, indices)
        assert direct.get(0, zero) == complete.get(0, zero)
        assert bool(direct.get(0, zero)) == is_old, ("old support", n, indices)
        assert bool(direct.get(1, zero)) == is_return, (
            "return support", n, indices)
        assert not (is_old and is_return)
        if is_old:
            assert direct == {0: old_formula(i, j, k)}, (
                "old coefficient", n, indices)
        if is_return:
            assert direct == {1: return_formula(i, j, k)}, (
                "return coefficient and sign", n, indices)
        if not (is_old or is_return):
            assert not direct, ("zero tensor sector", n, indices)

        counts["symmetric_triples"] += 1
        counts["ordered_triples_represented"] += order_count
        counts["quotient_trace_identity_checks"] += 1
        counts["old_supported_triples"] += is_old
        counts["return_supported_triples"] += is_return
        counts["zero_triples"] += not (is_old or is_return)
        counts["strict_old_triples"] += strict_old
        high_count = sum(a > middle for a in indices)
        if is_old:
            assert high_count <= 1
            assert direct == complete, ("old-support preservation", n, indices)
            if high_count:
                counts["old_preservation_with_high_index"] += 1
                samples.setdefault("old_high", list(indices))
                if strict_old:
                    counts["strict_old_preservation_with_high_index"] += 1
                    samples.setdefault("strict_old_high", list(indices))
                    if max(indices)*2 > n:
                        counts["strict_old_preservation_above_N_half"] += 1
                        samples.setdefault("strict_old_above_N_half", list(indices))
            if total == d or max(pair_sums) == d:
                counts["old_support_boundary_triples"] += 1

        # Every raw product below degree 2N-1 has unchanged top trace,
        # irrespective of whether it belongs to the old support.
        if total < 2*n-1:
            assert direct == complete, ("raw-degree invariance", n, indices)
            counts["raw_degree_preservation_checks"] += 1

        if is_return:
            assert high_count >= 2
            t = total-(2*n-1)
            a, b, c = [1-Fraction(v, d) for v in indices]
            complement_sum = a+b+c
            assert min(a, b, c) >= 0
            assert complement_sum <= 1-Fraction(1, d)
            assert max(a+b, a+c, b+c) <= 1
            # Explicit comparison of all seven exact factorial arguments
            # with the arguments used in the closed entropy.
            exact_arguments = [Fraction(v, n) for v in
                               (i, j, k, t, i-t, j-t, k-t)]
            limiting_arguments = [
                1-a, 1-b, 1-c, 1-a-b-c, b+c, a+c, a+b]
            offsets = [abs(v-w) for v, w in
                       zip(exact_arguments, limiting_arguments)]
            assert max(offsets) <= Fraction(2, n)
            maximum_offset = max(maximum_offset, *offsets)
            counts["return_d_normalization_checks"] += 1
            if 0 in (a, b, c):
                counts["return_zero_complement_triples"] += 1
                samples.setdefault("return_zero_complement", list(indices))
            if complement_sum == 1-Fraction(1, d):
                counts["return_extreme_sum_triples"] += 1
                # This is exactly the reason N-normalization cannot be
                # inserted literally in the real-domain entropy.
                N_sum = 3-Fraction(total, n)
                assert N_sum == 1+Fraction(1, n)
                samples.setdefault("extreme_sum", {
                    "indices": list(indices),
                    "d_normalized_complement_sum": str(complement_sum),
                    "N_normalized_complement_sum": str(N_sum)})

    # The metric is independently extracted from degree-two products.
    metric_checks = 0
    for i in range(n):
        for j in range(n):
            direct = trace_coefficients(basis[i]*basis[j], modulus)
            expected = {0: one} if i+j == d else {}
            assert direct == expected, ("moving metric", n, i, j)
            metric_checks += 1
    return {
        "N": n,
        "field": "Q[q]/Phi_%d(q)" % (2*n),
        "trace_normalization": "(-1)^(N-1) N^2 [z^(N-1)] remainder",
        "deformation": "formal Delta; exact polynomial arithmetic",
        "counts": dict(sorted(counts.items())),
        "moving_metric_checks": metric_checks,
        "largest_factorial_argument_offset": str(maximum_offset),
        "example_triples": samples,
        "result": "all exact checks passed",
    }


def typed_currying_checks():
    # Tuple (out-left, out-right, in-left, in-right); duality negates color.
    # The actual entry formula has old output (d-a,j), input (k,d-b).
    # The new output is (j,b), input (a,k), giving this permutation.
    def turn(typ):
        a, b, c, d = typ
        return b, -d, -a, c

    types = (
        (1, 1, 1, 1), (-1, -1, -1, -1),
        (1, -1, 1, -1), (-1, 1, -1, 1),
        (-1, 1, 1, -1), (1, -1, -1, 1))

    def moving(typ):
        return typ[0] == typ[1] == typ[2] == typ[3]

    def name(typ):
        out = "".join("+" if a > 0 else "-" for a in typ[:2])
        inp = "".join("+" if a > 0 else "-" for a in typ[2:])
        return inp+" -> "+out

    rows, cycles = [], []
    for typ in types:
        image = turn(typ)
        assert image in types
        assert not (moving(typ) and moving(image))
        state, cycle = typ, []
        for _ in range(4):
            cycle.append(name(state))
            state = turn(state)
        assert state == typ
        rows.append({
            "input_morphism": name(typ),
            "turned_morphism": name(image),
            "input_relation": "moving" if moving(typ) else "constant",
            "output_relation": "moving" if moving(image) else "constant"})
        cycles.append(cycle)
    compatible = 0
    for first in types:
        for second in types:
            if first[:2] != second[2:]:
                continue
            composite = second[:2]+first[2:]
            assert composite in types
            assert moving(first) == moving(second) == moving(composite)
            compatible += 1
    return {
        "derivation": "endpoint permutation from literal currying indices, with dual colors",
        "turn_rows": rows,
        "four_turn_cycles": cycles,
        "compatible_product_pairs_checked": compatible,
        "conclusion": "No physical turn joins two moving-relation vertices.",
        "scope": "These are the six actual Casimir intertwiner types, not arbitrary linear maps.",
    }


def symbolic_checks():
    x = sp.symbols("x", real=True)
    B1, B2, X = sp.symbols("B1 B2 X", real=True)
    output_B = (B1*B2+X**2-1)/(B1+B2)
    proper_difference = ((X-B1)*(X-B2)-1)/(B1+B2)
    assert sp.factor(output_B-X-proper_difference) == 0
    Ysq = (1+B1**2-X**2)*(1+B2**2-X**2)/(B1+B2)**2
    assert sp.factor(Ysq.subs(X**2, 1-B1*B2)-B1*B2) == 0
    assert sp.expand(X**2-B1*B2-(X*(X-B1)+B1*(X-B2))) == 0
    derivative_ratio_g = (2*sp.sin(2*sp.pi*x))**2/(2*sp.sin(sp.pi*x))**4
    derivative_ratio_half = (sp.cos(sp.pi*x)/sp.sin(sp.pi*x))**2
    assert sp.trigsimp(derivative_ratio_g-derivative_ratio_half) == 0
    a, b = sp.symbols("a b", real=True)
    addition = (sp.cos(a)*sp.cos(b)-sp.sin(a)*sp.sin(b))*sp.sin(a+b)
    addition -= sp.cos(a+b)*(sp.cos(a)*sp.sin(b)+sp.cos(b)*sp.sin(a))
    assert sp.trigsimp(sp.expand_trig(addition)) == 0
    return {
        "exact_identities": 5,
        "half_vertex_identity": {
            "checked": "exp(g'(x)) = exp(d/dx [2J(1/2+x)-2J(x)])",
            "normalizing_inputs": "J(0)=J(1/2)=J(1)=0, with real logarithms for 0<x<1/2",
            "deduction": "t(1/2,1/2,x)=g(x), including endpoints by continuity",
        },
        "supporting_gradient": {
            "checked": [
                "B-X=((X-B1)(X-B2)-1)/(B1+B2)",
                "B=0 implies Y^2=B1 B2=1-X^2",
                "X^2-B1 B2=X(X-B1)+B1(X-B2)",
                "the cotangent addition identity used for 0<X<1",
            ],
            "required_analytic_hypotheses": "B1,B2>0, Bi<=X, strict stationary region; not established by finite tests",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=10)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("trivalent_return_comparison_results.json"))
    args = parser.parse_args()
    if args.max_level < 2:
        parser.error("--max-level must be at least 2")
    levels = []
    for n in range(2, args.max_level+1):
        levels.append(exact_level(n))
        print("exact level %d complete" % n, flush=True)
    result = {
        "scope": "Finite exact source, endpoint and type reproduction; not an analytic clamp or asymptotic proof.",
        "construction": "Newton polynomials -> exact division modulo P0+Delta -> normalized top coefficient",
        "coefficient_field_scope": "Identities are invariant under the chosen primitive-root Galois embedding; no positivity is inferred from this field representation.",
        "public_convention_references": [
            "notes/actual_main_meridian_newton_multiplication.md",
            "notes/actual_main_meridian_turn_comparison.md",
            "notes/actual_main_meridian_grouped_wire_packet.md"],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {"sympy": sp.__version__},
        "exact_cyclotomic_levels": levels,
        "typed_physical_currying": typed_currying_checks(),
        "symbolic_identities": symbolic_checks(),
        "numerical_checks": [],
        "result": "all exact checks passed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "output": str(args.output),
        "levels": len(levels),
        "symmetric_cubic_triples": sum(v["counts"]["symmetric_triples"] for v in levels),
        "ordered_cubic_triples_represented": sum(v["counts"]["ordered_triples_represented"] for v in levels),
        "strict_old_high_triples": sum(v["counts"].get("strict_old_preservation_with_high_index", 0) for v in levels),
        "strict_old_triples_above_N_half": sum(v["counts"].get("strict_old_preservation_above_N_half", 0) for v in levels),
        "result": result["result"],
    }, indent=2))


if __name__ == "__main__":
    main()
