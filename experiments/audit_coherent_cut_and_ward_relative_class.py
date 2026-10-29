#!/usr/bin/env python3
"""Exact audit of the coherent-cut obstruction and E-relative Ward class."""

from __future__ import annotations

from math import factorial
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


def dm(rows, field):
    return DomainMatrix(rows, (len(rows), len(rows[0])), field)


def zeros(n, field):
    return [[field.zero for _ in range(n)] for _ in range(n)]


def same(a, b):
    return a.sub(b).is_zero_matrix


def map_entries(matrix, function):
    return dm([[function(value) for value in row]
               for row in matrix.to_list()], matrix.domain)


def substitute(value, variable, constant):
    # SymPy's FracElement.to_poly compares algebraic 1 to integer 1,
    # so bypass that conversion for fields with ANP coefficients.
    coefficient = value.numer.ring.domain(constant)
    return value.new(value.numer.subs(variable.numer, coefficient),
                     value.denom.subs(variable.numer, coefficient))


def differentiate(value, variable):
    return value.new(
        value.numer.diff(variable.numer) * value.denom
        - value.numer * value.denom.diff(variable.numer),
        value.denom ** 2)


def exp_nilpotent(matrix, parameter, n):
    field = matrix.domain
    ident = DomainMatrix.eye((n, n), field).to_dense()
    result, power = ident, ident
    for j in range(1, n):
        power = power.matmul(matrix)
        result = result.add(power.scalarmul(parameter ** j / field(factorial(j))))
    assert power.matmul(matrix).is_zero_matrix
    return result


def audit_level(n):
    k = QQ.cyclotomic_field(n)
    q = k.from_sympy(k.ext)
    field = k.frac_field("M", "t", "u")
    meridian, t, u = field.gens
    q = field.convert(q, k)
    ident = DomainMatrix.eye((n, n), field).to_dense()
    e = zeros(n, field)
    eps = []
    for a in range(n - 1):
        epsilon = meridian * q ** (-a - 1) - meridian ** -1
        eps.append(epsilon)
        e[a][a + 1] = epsilon
        assert substitute(epsilon, meridian, 1) != field.zero
    e = dm(e, field)
    count = n - 1

    # An arbitrary nonuniform normalized probe minus the exact average.
    r = [field(2 * (a + 1)) / (n * (n + 1)) - field.one / n
         for a in range(n)]
    assert sum(r, field.zero) == field.zero
    b = zeros(n, field)
    diagonal = zeros(n, field)
    prefix = field.zero
    for a in range(n):
        diagonal[a][a] = r[a]
        if a < n - 1:
            prefix += r[a]
            b[a + 1][a] = prefix / eps[a]
    b = dm(b, field)
    assert same(e.matmul(b).sub(b.matmul(e)), dm(diagonal, field))
    count += 1

    # Exact polynomial flow and its literal translation frame.
    gt = exp_nilpotent(e, t, n)
    gmt = exp_nilpotent(e, -t, n)
    gu = exp_nilpotent(e, u, n)
    gtu = exp_nilpotent(e, t + u, n)
    assert same(gt.matmul(gmt), ident)
    assert same(gt.matmul(gu), gtu)
    count += 2
    frame = zeros(n, field)
    derivative = zeros(n, field)
    coefficient = field.one
    for a in range(n):
        frame[a][a] = coefficient
        if a < n - 1:
            derivative[a][a + 1] = field(a + 1)
            coefficient *= eps[a] / field(a + 1)
    frame, derivative = dm(frame, field), dm(derivative, field)
    assert same(frame.matmul(e), derivative.matmul(frame))
    count += 1

    # Actual normalized constant-vector/average-covector projector.
    projector = dm([[field.one / n for _ in range(n)] for _ in range(n)], field)
    assert same(projector.matmul(projector), projector)
    pt = gt.matmul(projector).matmul(gmt)
    assert same(map_entries(pt, lambda value: differentiate(value, t)),
                e.matmul(pt).sub(pt.matmul(e)))
    assert same(gmt.matmul(pt).matmul(gt), projector)
    count += 3
    primitive = pt.scalarmul(t)
    twisted_derivative = map_entries(primitive, lambda value: differentiate(value, t)).sub(
        e.matmul(primitive).sub(primitive.matmul(e)))
    assert same(twisted_derivative, pt)
    assert map_entries(primitive, lambda value: substitute(value, t, 0)).is_zero_matrix
    count += 2

    # A non-covariant general relative cochain, checking L_E delta_E=0
    # by direct finite polynomial integration, rather than just P_t.
    h = zeros(n, field)
    h[0][0] = t ** 2 + 1
    h[0][n - 1] += t
    h[n - 1][0] += meridian * (t + 2)
    h = dm(h, field)
    connection = map_entries(h, lambda value: differentiate(value, t)).sub(
        e.matmul(h).sub(h.matmul(e)))
    integrand = gmt.matmul(connection).matmul(gt)

    def integrate_t(value):
        assert all(exponent[1] == 0 for exponent in value.denom)
        anti = value.numer.ring.from_dict({
            (a, b + 1, c): coefficient / k(b + 1)
            for (a, b, c), coefficient in value.numer.items()
        })
        primitive_value = value.field.new(anti, value.denom)
        return substitute(primitive_value, t, 1) - substitute(primitive_value, t, 0)

    integral = map_entries(integrand, integrate_t)
    h0 = map_entries(h, lambda value: substitute(value, t, 0))
    h1 = map_entries(h, lambda value: substitute(value, t, 1))
    g1 = exp_nilpotent(e, field.one, n)
    gm1 = exp_nilpotent(e, -field.one, n)
    result = integral.sub(gm1.matmul(h1).matmul(g1)).add(h0)
    assert result.is_zero_matrix
    count += 1

    # The omitted cyclic edge is precisely the whole meridian gap.
    last_edge = meridian * q ** (-n) - meridian ** -1
    assert last_edge == meridian - meridian ** -1
    assert substitute(differentiate(last_edge, meridian), meridian, 1) == field(2)
    count += 2
    return {"N": n, "exact_checks": count}


def hessian_checks():
    meridian, s, kappa = sp.symbols("M s kappa", nonzero=True)
    old = sp.diag(0, 0, 2, 3, 5)
    dq = sp.Matrix([0, -1 / (meridian + s), 2, 1, -3])
    new = old + kappa * dq * dq.T
    assert new * sp.Matrix([1, 0, 0, 0, 0]) == sp.zeros(5, 1)
    assert new.rank() == 4
    assert new[:2, :2] == sp.diag(0, kappa / (meridian + s) ** 2)
    return 3


def main():
    levels = [audit_level(n) for n in range(2, 7)]
    results = {
        "status": "all exact checks passed",
        "coherent_hessian_checks": hessian_checks(),
        "finite_levels": levels,
        "finite_exact_checks": sum(row["exact_checks"] for row in levels),
        "scope": (
            "Finite E-Ward currents, polynomial flow, twisted relative "
            "transgression, and coherent-cut rank obstruction. No internal "
            "geometric centralizer chain map or volume estimate is inferred."
        ),
    }
    results["total_exact_checks"] = (
        results["coherent_hessian_checks"] + results["finite_exact_checks"])
    path = Path(__file__).with_name("coherent_cut_and_ward_relative_class_results.json")
    path.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
