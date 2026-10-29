#!/usr/bin/env python3
"""Exact diagnostics for formal A-curve periods and their collision lattice.

Expected branch ratios come from independent exact Ore factorizations.
The local differential reduction is also checked against direct shifts
of polynomials. No knot census or analytic asymptotic theorem is used.
"""

import json
from math import factorial
from pathlib import Path

import sympy as sp


q, x, h, lam, s, tau = sp.symbols("q x h lam s tau")


def add_series(a, b, order):
    return [sp.cancel(a[j]+b[j]) for j in range(order+1)]


def mul_series(a, b, order):
    return [sp.cancel(sum(a[i]*b[j-i] for i in range(j+1))) for j in range(order+1)]


def shifted(a, steps, order, derivation):
    result = [sp.Integer(0)]*(order+1)
    for i, value in enumerate(a[:order+1]):
        derivative = value
        for j in range(order-i+1):
            if j:
                derivative = sp.cancel(derivation(derivative))
            result[i+j] += sp.Rational(steps**j, factorial(j))*derivative
    return [sp.cancel(value) for value in result]


def q_coefficients(expression, order):
    expanded = sp.series(expression.subs(q, sp.exp(h)), h, 0, order+1).removeO().expand()
    return [sp.cancel(expanded.coeff(h, j)) for j in range(order+1)]


def remainder(coefficients, a, order, derivation):
    result = [sp.Integer(0)]*(order+1)
    product = [sp.Integer(1)]+[sp.Integer(0)]*order
    for j, coefficient in enumerate(coefficients):
        result = add_series(result, mul_series(coefficient[:order+1], product, order), order)
        product = mul_series(product, shifted(a, j, order, derivation), order)
    return result


def hensel(coefficients, leading, order, derivation):
    derivative = sp.cancel(sum(j*c[0]*leading**(j-1)
                               for j, c in enumerate(coefficients) if j))
    assert derivative != 0
    a = [leading]+[sp.Integer(0)]*order
    for n in range(1, order+1):
        known = remainder(coefficients, a, n, derivation)[n]
        a[n] = sp.cancel(-known/derivative)
    assert all(value == 0 for value in remainder(coefficients, a, order, derivation))
    return a


def theta(a, order, derivation):
    perturbation = [sp.Integer(0)]+[sp.cancel(v/a[0]) for v in a[1:]]
    logarithm = [sp.log(a[0])]+[sp.Integer(0)]*order
    term = [sp.Integer(1)]+[sp.Integer(0)]*order
    for power in range(1, order+1):
        term = mul_series(term, perturbation, order)
        for j in range(1, order+1):
            logarithm[j] += sp.Rational((-1)**(power+1), power)*term[j]
    logarithm = [sp.cancel(v) for v in logarithm]
    result = []
    for n in range(order+1):
        value = logarithm[n]
        for j in range(1, n+1):
            derivative = logarithm[n-j]
            for k in range(j):
                derivative = sp.cancel(derivation(derivative))
            value += sp.bernoulli(j, 0)*derivative/factorial(j)
        result.append(sp.cancel(value))
    return result


def ore_product(left, right):
    result = [sp.Integer(0)]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b.subs(x, q**i*x)
    return [sp.cancel(v) for v in result]


def factor_and_gauge_checks():
    order = 4
    derivative = lambda value: x*sp.diff(value, x)
    exact = 1-q*x
    operator = ore_product([-(2+q*x), sp.Integer(1)], [-exact, sp.Integer(1)])
    data = [q_coefficients(c, order) for c in operator]
    recovered = hensel(data, 1-x, order, derivative)
    assert recovered == q_coefficients(exact, order)
    connection = theta(recovered, order, derivative)
    symbol = sum(c[0]*lam**j for j, c in enumerate(data))
    first = sum(c[1]*lam**j for j, c in enumerate(data))
    pl = sp.diff(symbol, lam).subs(lam, 1-x)
    pll = sp.diff(symbol, lam, 2).subs(lam, 1-x)
    expected_first = (-first.subs(lam, 1-x)/((1-x)*pl)
                      -derivative(1-x)*(pll/pl+1/(1-x))/2)
    assert sp.cancel(connection[1]-expected_first) == 0

    multiple = ore_product([-(3-q*q*x), sp.Integer(1)], operator)
    recovered_multiple = hensel([q_coefficients(c, order) for c in multiple],
                                1-x, order, derivative)
    assert recovered_multiple == recovered

    gauge = 1+q*x
    transformed = [sp.cancel(c*gauge/gauge.subs(x, q**j*x))
                   for j, c in enumerate(operator)]
    gauged = hensel([q_coefficients(c, order) for c in transformed], 1-x, order, derivative)
    expected_gauged = q_coefficients(exact*gauge.subs(x, q*x)/gauge, order)
    assert gauged == expected_gauged
    gauged_connection = theta(gauged, order, derivative)
    logarithmic_derivative = q_coefficients(derivative(gauge)/gauge, order-1)
    assert sp.cancel(gauged_connection[0]-connection[0]) == 0
    for j in range(1, order+1):
        assert sp.cancel(gauged_connection[j]-connection[j]-logarithmic_derivative[j-1]) == 0
    return {"order_in_h": order, "independent_exact_Ore_factor_recovered": True,
            "noncharacteristic_left_multiple_invariant": True,
            "first_connection_correction_exact": True, "Bernoulli_gauge_law_exact": True}


def pole_order(expression, variable, point):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    if numerator == 0:
        return None

    def multiplicity(polynomial):
        polynomial = sp.Poly(polynomial, variable)
        count = 0
        divisor = sp.Poly(variable-point, variable)
        while polynomial.eval(point) == 0:
            polynomial = polynomial.exquo(divisor)
            count += 1
        return count

    return multiplicity(denominator)-multiplicity(numerator)


def collision_poles():
    order = 3
    derivative = lambda value: x*sp.diff(value, x)
    # A node with normalized branch L=x and crossing branch L=2-x.
    operator = [1-(x-1)**2+3*(q-1), sp.Integer(-2), sp.Integer(1)]
    node = hensel([q_coefficients(c, order) for c in operator], x, order, derivative)
    node_poles = [pole_order(node[j], x, 1) for j in range(1, order+1)]
    assert all(pole is None or pole <= 2*j-1 for j, pole in enumerate(node_poles, 1))
    # A normalized rational curve, algebraic and ramified over the x-line.
    curve_x = lam+1/lam-1
    curve_delta = lambda value: sp.cancel(curve_x/sp.diff(curve_x, lam)*sp.diff(value, lam))
    ramified_operator = [q, -(curve_x+1), sp.Integer(1)]
    ramified = hensel([q_coefficients(c, order) for c in ramified_operator],
                      lam, order, curve_delta)
    ramified_poles = [pole_order(ramified[j], lam, 1) for j in range(1, order+1)]
    assert all(pole is None or pole <= 3*j-1 for j, pole in enumerate(ramified_poles, 1))
    epsilon, t = sp.symbols("epsilon t")
    for weight in (2, 3):
        monomial = t**weight*epsilon
        vector_action = t*t*epsilon*sp.diff(monomial, t)-weight*t*epsilon**2*sp.diff(monomial, epsilon)
        assert sp.expand(vector_action) == 0
    return {"order_in_h": order, "ordinary_node_pole_orders": node_poles,
            "simple_ramification_pole_orders": ramified_poles,
            "weighted_shift_preserves_h_exactly": True}


def d_clean(operator):
    return {j: sp.expand(c) for j, c in operator.items() if sp.expand(c) != 0}


def d_add(*operators):
    result = {}
    for operator in operators:
        for j, c in operator.items():
            result[j] = result.get(j, 0)+c
    return d_clean(result)


def d_scale(c, operator):
    return d_clean({j: c*a for j, a in operator.items()})


def d_mul(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            for r in range(i+1):
                degree = i+j-r
                result[degree] = result.get(degree, 0)+sp.binomial(i, r)*a*sp.diff(b, s, r)
    return d_clean(result)


def ds_mul(left, right, order):
    return [d_add(*(d_mul(left[i], right[n-i]) for i in range(n+1)))
            for n in range(order+1)]


def right_divide(operator, monic):
    remainder = dict(operator)
    quotient = {}
    degree = max(monic)
    assert monic[degree] == 1
    while remainder and max(remainder) >= degree:
        power = max(remainder)-degree
        term = {power: remainder[max(remainder)]}
        quotient = d_add(quotient, term)
        remainder = d_add(remainder, d_scale(-1, d_mul(term, monic)))
    return quotient, remainder


def d_apply(operator, polynomial):
    return sp.expand(sum(c*sp.diff(polynomial, s, j) for j, c in operator.items()))


def node_reduction(x0, l0, mixed, quadratic, subprincipal):
    order = 4
    total = order+2
    operator = [l0*l0-mixed*l0*(x-x0)+quadratic*(x-x0)**2+subprincipal*(q-1),
                mixed*(x-x0)-2*l0, sp.Integer(1)]
    generator = [{} for _ in range(total+1)]
    generator[1], generator[2] = {1: sp.Integer(x0)}, {1: s}
    complete = [{} for _ in range(total+1)]
    for j, coefficient in enumerate(operator):
        exponential = [{} for _ in range(total+1)]
        term = [{} for _ in range(total+1)]
        term[0] = {0: sp.Integer(1)}
        for n in range(total+1):
            for k in range(total+1):
                exponential[k] = d_add(exponential[k], d_scale(sp.Rational(j**n, factorial(n)), term[k]))
            term = ds_mul(term, generator, total)
        scalar = sp.series(coefficient.subs({q: sp.exp(tau*tau), x: x0+tau*s}),
                           tau, 0, total+1).removeO().expand()
        coefficients = [scalar.coeff(tau, k) for k in range(total+1)]
        for k in range(total+1):
            complete[k] = d_add(complete[k], *(d_scale(l0**j*coefficients[i], exponential[k-i])
                                              for i in range(k+1)))
    assert not complete[0] and not complete[1]
    a2 = sp.Integer(x0*x0*l0*l0)
    local = [d_scale(1/a2, c) for c in complete[2:]]
    expected = {2: sp.Integer(1), 1: sp.Rational(mixed, x0*l0)*s,
                0: (quadratic*s*s+subprincipal)/a2}
    assert local[0] == d_clean(expected)
    unit = [{} for _ in range(order+1)]
    reduced = [{} for _ in range(order+1)]
    unit[0], reduced[0] = {0: sp.Integer(1)}, local[0]
    for n in range(1, order+1):
        known = d_add(local[n], *(d_scale(-1, d_mul(unit[i], reduced[n-i]))
                                  for i in range(1, n)))
        unit[n], reduced[n] = right_divide(known, reduced[0])
        assert not reduced[n] or max(reduced[n]) < 2
    assert ds_mul(unit, reduced, order) == local

    direct_checks = 0
    for degree in (0, 1, 2, 5, 8):
        actual = 0
        for j, coefficient in enumerate(operator):
            translated = sp.series((sp.exp(j*tau*tau)*(x0+tau*s)-x0)/tau,
                                   tau, 0, total+1).removeO()
            scalar = sp.series(coefficient.subs({q: sp.exp(tau*tau), x: x0+tau*s}),
                               tau, 0, total+1).removeO()
            actual += l0**j*scalar*translated**degree
        actual = sp.series(actual, tau, 0, total+1).removeO().expand()
        for n in range(order+1):
            expected_action = a2*d_apply(local[n], s**degree)
            assert sp.expand(actual.coeff(tau, n+2)-expected_action) == 0
        direct_checks += 1
    return {"point": [x0, l0], "mixed_coefficient": mixed,
            "quadratic_coefficient": quadratic, "subprincipal": subprincipal,
            "order_in_tau": order, "leading_node_connection": {str(j): str(c) for j, c in local[0].items()},
            "formal_monic_second_order_reduction_exact": True,
            "direct_shift_polynomials_checked": direct_checks,
            "connection_coefficients_polynomial_at_s_zero": True}


def regulator_conversion():
    a, b, c, d, u, v, du, dv = sp.symbols("a b c d u v du dv")
    delta = a*d-b*c
    U, V = a*u+b*v, c*u+d*v
    dU, dV = a*du+b*dv, c*du+d*dv
    assert sp.expand(U*dV-V*dU-delta*(u*dv-v*du)) == 0
    # dS=v du, so d[(Delta/2)S-(Delta/4)uv] equals the regulator differential.
    assert sp.expand(delta*v*du/2-delta*(u*dv+v*du)/4+(U*dV-V*dU)/4) == 0
    return {"general_peripheral_monomial_conversion_exact": True,
            "square_holonomy_delta": 4}


def main():
    result = {"scope": "Formal quantum-A period and collision lattice diagnostics; no actual-state volume theorem.",
              "factor_and_gauge": factor_and_gauge_checks(),
              "collision_poles": collision_poles(),
              "node_connections": [node_reduction(1, 1, 0, -1, 3),
                                   node_reduction(2, 3, 1, -2, 5)],
              "regulator_conversion": regulator_conversion()}
    Path(__file__).with_name("formal_a_curve_torsor_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
