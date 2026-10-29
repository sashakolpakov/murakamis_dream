#!/usr/bin/env python3
"""Exact whole-germ checks for fixed algebraic central normalizations.

The all-level growth theorem is proved in the note. Here levels remain
symbolic: we check canceled germs, algebraic root relations and bounded
jets, rather than inferring a growth law from a finite numerical sample.
"""

import json
from pathlib import Path

import sympy as sp


N = sp.symbols("N", positive=True, integer=True)
M, z, q, Y, y, t = sp.symbols("M z q Y y t")


def whole_germ(expression, central_power=2, order=5):
    pulled = expression.subs({M: sp.exp(y), z: sp.exp(central_power*N*y)})
    return sp.series(pulled, y, 0, order).removeO().expand()


def defining_jet(polynomial, central_power=2, max_order=8):
    pulled = polynomial.subs({M: sp.exp(y), z: sp.exp(central_power*N*y)})
    for order in range(max_order+1):
        coefficient = sp.factor(sp.diff(pulled, y, order).subs(y, 0)/sp.factorial(order))
        if coefficient != 0:
            return order, coefficient
    raise AssertionError("Increase jet budget or check the defining polynomial")


def ado_factor():
    # Clear the harmless M^2 denominator of the fixed algebraic relation.
    relation = Y**2*(z-1)**2*M**2-(M**2-1)**2*z
    order, polynomial = defining_jet(relation)
    assert order == 2
    assert sp.expand(polynomial-(4*N*N*Y*Y-4)) == 0
    assert sp.solve(polynomial, Y) == [-1/N, 1/N]
    selected = (M-M**-1)*sp.exp(N*y)/(sp.exp(2*N*y)-1)
    selected = selected.subs(M, sp.exp(y))
    value = sp.limit(selected, y, 0)
    assert value == 1/N
    germ = sp.series(selected, y, 0, 5).removeO().expand()
    assert sp.cancel(germ.coeff(y, 1)) == 0
    assert sp.cancel(germ.coeff(y, 2)-(1-N*N)/(6*N)) == 0
    plus_factor = whole_germ(1+sp.sqrt(z), order=2)
    assert plus_factor.subs(y, 0) == 2
    return {"first_common_jet_order": order, "residue_polynomial": str(polynomial),
            "specified_root_value": str(value), "second_germ_coefficient": str(sp.factor(germ.coeff(y, 2))),
            "one_plus_M_to_N_value": 2}


def rational_germs():
    cases = [((z-M**3)/(M-1), 2*N-3),
             ((z-1-2*N*(M-1))/(M-1)**2, N*(2*N-1)),
             ((z-M**2)/((q-1)**3*(M-1)), (2*N-2)/(q-1)**3)]
    records = []
    for expression, expected in cases:
        value = sp.cancel(whole_germ(expression, order=2).subs(y, 0))
        assert sp.cancel(value-expected) == 0
        records.append({"fixed_factor": str(expression), "whole_germ_value": str(value)})
    last = cases[-1][1].subs({N: 1/t, q: sp.exp(sp.pi*sp.I*t)})
    leading = sp.simplify(sp.limit(t**4*last, t, 0))
    assert sp.simplify(leading-2*sp.I/sp.pi**3) == 0
    return {"records": records, "last_factor_pole_order_at_t_zero": 4,
            "last_factor_leading_coefficient": str(leading)}


def algebraic_branch_relation():
    # A fifth root on a fixed finite cover; no branch choice is required
    # to derive its common residue relation.
    relation = (q-1)**3*(M-1)*Y**5-(z-M**2)
    order, polynomial = defining_jet(relation)
    assert order == 1
    assert sp.expand(polynomial-((q-1)**3*Y**5-(2*N-2))) == 0
    return {"first_common_jet_order": order, "residue_relation_for_all_five_branches": str(polynomial),
            "root_growth_exponent_from_coefficient_valuations": "4/5"}


def maximal_jet_cancellation():
    supports = [(0, 0), (1, 0), (0, 1), (2, 1), (0, 2)]
    exponents = [a+2*N*b for a, b in supports]
    weights = [sp.cancel(1/sp.prod(value-other for j, other in enumerate(exponents) if j != i))
               for i, value in enumerate(exponents)]
    jets = [sp.factor(sum(c*value**j for c, value in zip(weights, exponents)))
            for j in range(len(supports))]
    assert jets == [0, 0, 0, 0, 1]
    return {"central_Laurent_support": supports, "jets_before_factorials": [str(j) for j in jets],
            "maximal_vanishing_order": 4,
            "scope": "Five fixed monomials with coefficients rational in N=1/t; central exponents are unbounded."}


def main():
    results = {"scope": "Symbolic central-germ diagnostics for the uniform algebraic normalization theorem.",
               "ADO_normalization": ado_factor(), "rational_germs": rational_germs(),
               "algebraic_cover": algebraic_branch_relation(),
               "bounded_central_jets": maximal_jet_cancellation()}
    Path(__file__).with_name("algebraic_central_normalization_results.json").write_text(
        json.dumps(results, indent=2)+"\n")
    print(json.dumps(results), flush=True)


if __name__ == "__main__":
    main()
