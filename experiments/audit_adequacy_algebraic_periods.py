#!/usr/bin/env python3
"""Exact colored-bracket diagnostics for the adequate-degree argument.

A Temperley--Lieb expansion computes the actual Laurent polynomials;
the proposed degree formula is used only for the final assertions.
Cable state circles and all single-crossing adequacy tests are separate.
"""

from functools import cache
from math import comb
import json
from pathlib import Path

import sympy as sp


def add(target, polynomial, shift=0, coefficient=1):
    for exponent, value in polynomial.items():
        key = exponent+shift
        target[key] = target.get(key, 0)+coefficient*value
        if target[key] == 0:
            del target[key]


def multiply(a, b):
    result = {}
    for exponent, coefficient in a.items():
        add(result, b, exponent, coefficient)
    return result


@cache
def delta_power(exponent):
    result = {0: 1}
    for _ in range(exponent):
        result = multiply(result, {2: -1, -2: -1})
    return result


def identity(strands):
    return tuple(range(strands, 2*strands))+tuple(range(strands))


def append_e(diagram, index, strands):
    x, y = strands+index, strands+index+1
    if diagram[x] == y:
        return diagram, 1
    a, b = diagram[x], diagram[y]
    result = list(diagram)
    result[a], result[b] = b, a
    result[x], result[y] = y, x
    return tuple(result), 0


@cache
def closure_circles(diagram):
    strands = len(diagram)//2
    parent = list(range(2*strands))

    def root(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def join(a, b):
        parent[root(a)] = root(b)

    for j, partner in enumerate(diagram):
        join(j, partner)
    for j in range(strands):
        join(j, strands+j)
    return len({root(j) for j in range(2*strands)})


def bracket(word, strands):
    expansion = {identity(strands): {0: 1}}
    for crossing in word:
        sign = 1 if crossing > 0 else -1
        index = abs(crossing)-1
        result = {}
        for diagram, polynomial in expansion.items():
            add(result.setdefault(diagram, {}), polynomial, sign)
            following, loop = append_e(diagram, index, strands)
            destination = result.setdefault(following, {})
            if loop:
                add(destination, polynomial, -sign+2, -1)
                add(destination, polynomial, -sign-2, -1)
            else:
                add(destination, polynomial, -sign)
        expansion = {diagram: value for diagram, value in result.items() if value}
    result = {}
    for diagram, polynomial in expansion.items():
        add(result, multiply(polynomial, delta_power(closure_circles(diagram))))
    return result


def cable(word, multiplicity):
    result = []
    for crossing in word:
        base = (abs(crossing)-1)*multiplicity
        tile = [base+index for row in range(multiplicity)
                for index in range(multiplicity+row, row, -1)]
        result.extend(tile if crossing > 0 else [-index for index in reversed(tile)])
    return result


def state_circles(word, strands, state, flip=None):
    diagram = identity(strands)
    internal = 0
    for j, crossing in enumerate(word):
        use_e = (crossing < 0) if state == "A" else (crossing > 0)
        if j == flip:
            use_e = not use_e
        if use_e:
            diagram, loop = append_e(diagram, abs(crossing)-1, strands)
            internal += loop
    return internal+closure_circles(diagram)


def adequate(word, strands, state):
    circles = state_circles(word, strands, state)
    assert all(state_circles(word, strands, state, flip=j) == circles-1
               for j in range(len(word)))
    return circles


def chebyshev_color(word, strands, multiplicity, cached_brackets):
    result = {}
    for r in range(multiplicity//2+1):
        parallel = multiplicity-2*r
        if parallel == 0:
            value = {0: 1}
        else:
            if parallel not in cached_brackets:
                cached_brackets[parallel] = bracket(cable(word, parallel), strands*parallel)
            value = cached_brackets[parallel]
        add(result, value, coefficient=(-1)**r*comb(multiplicity-r, r))
    return result


def quantum_dimension(multiplicity):
    result = {}
    for r in range(multiplicity//2+1):
        add(result, delta_power(multiplicity-2*r),
            coefficient=(-1)**r*comb(multiplicity-r, r))
    return result


def divide_laurent(numerator, denominator):
    A = sp.symbols("A")
    low_n, low_d = min(numerator), min(denominator)
    p = sp.Poly.from_dict({(k-low_n,): v for k, v in numerator.items()}, A)
    q = sp.Poly.from_dict({(k-low_d,): v for k, v in denominator.items()}, A)
    quotient, remainder = sp.div(p, q)
    assert remainder.is_zero
    return {powers[0]+low_n-low_d: int(value) for powers, value in quotient.terms()}


def diagram_check(name, strands, word, maximum_color):
    crossings = len(word)
    vA = adequate(word, strands, "A")
    vB = adequate(word, strands, "B")
    assert vA+vB == crossings+2
    results = []
    cached_brackets = {}
    for color in range(2, maximum_color+1):
        multiplicity = color-1
        word_cable = cable(word, multiplicity)
        cable_vA = adequate(word_cable, strands*multiplicity, "A")
        cable_vB = adequate(word_cable, strands*multiplicity, "B")
        assert cable_vA == multiplicity*vA and cable_vB == multiplicity*vB
        colored = chebyshev_color(word, strands, multiplicity, cached_brackets)
        expected_max = crossings*multiplicity**2+2*multiplicity*vA
        expected_min = -crossings*multiplicity**2-2*multiplicity*vB
        assert max(colored) == expected_max and min(colored) == expected_min
        assert abs(colored[expected_max]) == abs(colored[expected_min]) == 1
        dimension = quantum_dimension(multiplicity)
        assert max(dimension)-min(dimension) == 4*multiplicity
        reduced = divide_laurent(colored, dimension)
        span_A = max(reduced)-min(reduced)
        assert span_A == 2*crossings*color*(color-1)
        fusion_agreement = None
        if strands == 2 and all(crossing == word[0] for crossing in word):
            writhe = sum(1 if crossing > 0 else -1 for crossing in word)
            normalized = {exponent-writhe*multiplicity*(multiplicity+2):
                          (-1)**(multiplicity*writhe)*value
                          for exponent, value in reduced.items()}
            numerator = {}
            for r in range(multiplicity+1):
                highest = 2*multiplicity-2*r
                exponent = writhe*(highest*(highest+2)-4*multiplicity*(multiplicity+2))//2
                add(numerator, {2*highest-4*k: 1 for k in range(highest+1)},
                    exponent, (-1)**(r*writhe))
            fused = divide_laurent(numerator, {2*multiplicity-4*k: 1
                                              for k in range(multiplicity+1)})
            assert normalized == fused
            fusion_agreement = True
        results.append({"color": color, "cable_crossings": len(word_cable),
                        "cable_state_circles": [cable_vA, cable_vB],
                        "unreduced_extreme_A_degrees": [expected_min, expected_max],
                        "reduced_A_span": span_A,
                        "reduced_q_span": span_A//2,
                        "exact_quantum_dimension_division": True,
                        "independent_highest_weight_fusion_trace_agrees": fusion_agreement,
                        "single_crossing_adequacy_checks": 2*len(word_cable)})
    return {"diagram": name, "crossings": crossings,
            "state_circles": [vA, vB], "colors": results}


def local_color_check():
    A = sp.symbols("A", nonzero=True)
    checked_R = sp.Matrix([[A, 0, 0, 0], [0, 0, 1/A, 0],
                           [0, 1/A, A-A**-3, 0], [0, 0, 0, A]])
    e = A*(checked_R-A*sp.eye(4))
    delta = -A**2-A**-2
    assert (e*e-delta*e).applyfunc(sp.simplify).is_zero_matrix
    e1 = sp.kronecker_product(e, sp.eye(2))
    e2 = sp.kronecker_product(sp.eye(2), e)
    assert (e1*e2*e1-e1).applyfunc(sp.simplify).is_zero_matrix
    R1 = sp.kronecker_product(checked_R, sp.eye(2))
    R2 = sp.kronecker_product(sp.eye(2), checked_R)
    assert (R1*R2*R1-R2*R1*R2).applyfunc(sp.simplify).is_zero_matrix
    lam = sp.symbols("lambda")
    assert sp.factor(checked_R.charpoly(lam).as_expr()-(lam-A)**3*(lam+A**-3)) == 0
    return {"fundamental_bracket_relation": True, "Temperley_Lieb_relation": True,
            "braid_relation": True, "generic_color_convention_checked": True}


def main():
    results = {"scope": "Exact adequate-degree diagnostics, not a volume theorem.",
               "local": local_color_check(),
               "diagrams": [diagram_check("T(2,3)", 2, [1]*3, 4),
                            diagram_check("mirror T(2,3)", 2, [-1]*3, 3),
                            diagram_check("T(2,5)", 2, [1]*5, 4),
                            diagram_check("T(2,7)", 2, [1]*7, 3),
                            diagram_check("W(3,2): figure-eight", 3, [1, -2]*2, 3),
                            diagram_check("W(3,4)", 3, [1, -2]*4, 3),
                            diagram_check("W(3,5)", 3, [1, -2]*5, 3)]}
    path = Path(__file__).with_name("adequacy_algebraic_periods_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"diagrams": len(results["diagrams"]),
                      "colored_brackets": sum(len(d["colors"]) for d in results["diagrams"]),
                      "all_exact_checks": "passed", "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
