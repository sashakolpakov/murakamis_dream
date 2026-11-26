#!/usr/bin/env python3
"""Check the exact forced Fourier recurrence of the original mixed pair.

The checks compare original crossing matrices, the mixed Newton formula,
the forced polynomial identity, the explicit inverse operator, and the
third-order recurrence with its terminal normalization. Exact symbolic
checks identify its characteristic curve, discriminant, and the algebraic
curve satisfied by the derivative of the selected boundary action.
Finite growth records illustrate the proved rates; they are not a
proof of a boundary asymptotic or a volume conjecture.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_boundary_crossing_packet_preservation import original_crossings


def factorials(level):
    values = [mp.mpf(1)]
    for a in range(1, level):
        values.append(values[-1] * 2 * mp.sin(mp.pi * a / level))
    return values


def reverse(vector):
    return mp.matrix(list(reversed(list(vector))))


def relative_error(left, right):
    return abs(left - right) / max(1, abs(left), abs(right))


def exact_checks(precision):
    tolerance = mp.power(10, -precision // 2)
    records = []
    for level in range(2, 13):
        top = level - 1
        q = mp.exp(mp.pi * 1j / level)
        big_q = q * q
        products = factorials(level)
        weights = [1 / s**2 for s in products]
        positive, negative = original_crossings(level)
        unit = mp.matrix([1] + [0] * top)
        twice = positive * positive
        original = reverse(negative * negative * reverse(twice * unit))
        gram = twice.H * twice * unit
        gram_error = max(relative_error(a, b) for a, b in zip(original, gram))

        differences = []
        predicted = []
        for j in range(level + 3):
            difference = mp.fsum(
                weights[a] * mp.fprod(1 - big_q**(a + r) for r in range(1, j + 1))
                for a in range(level)
            )
            differences.append(difference)
            if j < level:
                predicted.append(level**2 * q**(-j*j) * difference / products[j]**2)
        source_error = max(relative_error(a, b) for a, b in zip(original, predicted))

        def difference_coefficients(j):
            a = big_q**(j + 1)
            s = 1 + big_q**-1 + big_q**-2
            return (
                (a - 1)**3,
                4*a*a - 3*(1 + big_q**-1)*a + s,
                -a*a + big_q**-1*(3*a - s),
                big_q**-3,
            )

        transformed_recurrence_error = mp.mpf(0)
        for j in range(level):
            terms = [coefficient*differences[j+k]
                     for k, coefficient in enumerate(difference_coefficients(j))]
            transformed_recurrence_error = max(
                transformed_recurrence_error,
                abs(mp.fsum(terms))/max(1, mp.fsum(abs(term) for term in terms)),
            )
        terminal_error = max(
            relative_error(differences[top], level),
            *(abs(differences[j]) for j in range(level, level+3)),
        )
        reconstructed = [mp.mpc(0) for _ in range(level+2)]
        reconstructed[top] = mp.mpf(level)
        for j in reversed(range(top)):
            coefficients = difference_coefficients(j)
            reconstructed[j] = -mp.fsum(
                coefficients[k]*reconstructed[j+k] for k in range(1, 4)
            )/coefficients[0]
        terminal_reconstruction_error = max(
            relative_error(differences[j], reconstructed[j]) for j in range(level)
        )

        def polynomial(x):
            return mp.fsum(weights[a] * x**a for a in range(level))

        points = [mp.mpc(".31", ".27"), mp.mpc("-.6", ".12"), mp.mpf(1)]
        recurrence_error = max(
            relative_error(
                polynomial(x) + (big_q*x - 2)*polynomial(big_q*x)
                + polynomial(big_q**2*x),
                x**level / level**2,
            )
            for x in points
        )
        fourier = [polynomial(big_q**j) for j in range(level)]
        cyclic_error = max(
            relative_error(
                fourier[j] + (big_q**(j+1) - 2)*fourier[(j+1) % level]
                + fourier[(j+2) % level],
                mp.mpf(1) / level**2,
            )
            for j in range(level)
        )

        operator = mp.matrix(level)
        operator[0, top] = 1
        for a in range(1, level):
            operator[a, a] = (1 - big_q**a)**2
            operator[a, a-1] = big_q**a
        determinant_error = relative_error(mp.det(operator), 1)
        forcing = mp.matrix([
            mp.mpc(mp.mpf(a+1)/(level+2), mp.mpf((a*a+3) % 7)/(level+3))
            for a in range(level)
        ])
        solution = mp.matrix([
            weights[a] * (
                level**2*forcing[0]
                + mp.fsum(big_q**(-b)*products[b-1]**2*forcing[b]
                          for b in range(a+1, level))
            )
            for a in range(level)
        ])
        inverse_error = max(
            relative_error(a, b) for a, b in zip(operator*solution, forcing)
        )
        left_bound = max(products[a]**2*abs(solution[a]) for a in range(level))
        right_bound = level**2*abs(forcing[0]) + mp.fsum(
            products[b-1]**2*abs(forcing[b]) for b in range(1, level)
        )
        if left_bound > right_bound * (1 + tolerance):
            raise ArithmeticError(("weighted bound", level, left_bound, right_bound))
        errors = {
            "gram_identity": gram_error,
            "original_source_coefficients": source_error,
            "transformed_third_order_recurrence": transformed_recurrence_error,
            "transformed_terminal_values": terminal_error,
            "transformed_terminal_reconstruction": terminal_reconstruction_error,
            "forced_polynomial_recurrence": recurrence_error,
            "cyclic_fourier_recurrence": cyclic_error,
            "determinant_one": determinant_error,
            "inverse_transport": inverse_error,
        }
        if max(errors.values()) > tolerance:
            raise ArithmeticError((level, errors))
        records.append({
            "N": level,
            "relative_errors": {key: mp.nstr(value, 35) for key, value in errors.items()},
            "weighted_bound_ratio": mp.nstr(left_bound/right_bound, 35),
        })
        print(f"Original mixed source and forced transport checked at N={level}.",
              flush=True)
    return records


def symbolic_checks():
    import sympy as sp

    a, r, x, y, q = sp.symbols("A r X Y Q")
    p = r**3 + (-a*a+3*a-3)*r**2 + (4*a*a-6*a+3)*r + (a-1)**3
    saddle = x*x*y-x-(1-x)**3
    if sp.expand(p.subs({a: y, r: 1-x*y}) + y**3*saddle) != 0:
        raise ArithmeticError("The characteristic substitution failed")
    discriminant = a**6*(4*a**3-32*a*a+48*a-23)
    if sp.expand(sp.discriminant(p, r) - discriminant) != 0:
        raise ArithmeticError("The characteristic discriminant failed")
    if sp.factor(p.subs({a: ((1-x)**3+x)/x**2, r: -(1-x)**3/x})) != 0:
        raise ArithmeticError("The rational parametrization failed")

    # Derive the recurrence independently from the polynomial inside the
    # finite weight identity (28), using the displayed Newton identities.
    g0, g1, g2, g3 = sp.symbols("g0 g1 g2 g3")
    sq = 1 + q**-1 + q**-2
    moments = [
        g0,
        (g0-g1)/a,
        (g0-(1+q**-1)*g1+q**-1*g2)/a**2,
        (g0-sq*g1+q**-1*sq*g2-q**-3*g3)/a**3,
    ]
    derived = sp.expand(a**3*(moments[0]+(q-3)*moments[1]
                             +(3-q*a)*moments[2]-moments[3]))
    expected = ((a-1)**3*g0 + (4*a*a-3*(1+q**-1)*a+sq)*g1
                +(-a*a+q**-1*(3*a-sq))*g2+q**-3*g3)
    if sp.expand(derived-expected) != 0:
        raise ArithmeticError("The third-order recurrence derivation failed")
    if sp.expand(expected.subs({q: 1, g0: 1, g1: r, g2: r*r, g3: r**3})-p) != 0:
        raise ArithmeticError("The commutative symbol failed")

    # Eliminate the stationary variables without suppressing factors at
    # a degenerate point of the full algebraic scheme.
    w, boundary_p, t, c = sp.symbols("w P t c")
    f = x**3 + (y-3)*x*x + 2*x - 1
    g = (1-x*y)*(y+w)*(1+w*y)-w*(1-y)**4
    resultant_x = sp.resultant(f, g, x)
    stationary_resultant = sp.cancel(-resultant_x/(y**3*(y-1)**3))
    if not stationary_resultant.is_polynomial(y, w):
        raise ArithmeticError("The stationary resultant quotient is not polynomial")
    boundary_curve = (
        w*w*(w+1)**4*boundary_p**5
        -4*w*w*(w+1)**2*(3*w+2)*boundary_p**4
        +4*w*w*(w**3+14*w*w+17*w+8)*boundary_p**3
        -4*w*(8*w**3+17*w*w+14*w+1)*boundary_p**2
        +4*w*(w+1)**2*(2*w+3)*boundary_p-(w+1)**4
    )
    resultant_y = sp.resultant(
        stationary_resultant, boundary_p*(1+w*y)-(y+w), y
    )
    if sp.expand(resultant_y+(w+1)**5*boundary_curve) != 0:
        raise ArithmeticError("The boundary-action elimination failed")
    if sp.expand(boundary_curve.subs(w, 1)-16*(boundary_p-1)**5) != 0:
        raise ArithmeticError("The complete boundary specialization failed")
    tangent = sp.Poly(sp.expand(boundary_curve.subs({w: 1+t, boundary_p: 1+c*t})), t)
    if any(tangent.nth(k) != 0 for k in range(5)):
        raise ArithmeticError("A lower-order boundary tangent term survived")
    expected_tangent = (4*c*c+2*c+1)*(4*c**3+6*c*c+5*c+2)
    if sp.expand(tangent.nth(5)-expected_tangent) != 0:
        raise ArithmeticError("The boundary tangent factorization failed")
    selected_y = 1+2*x+2*x*x
    selected_c = (1-selected_y)/(1+selected_y)
    selected_numerator = sp.fraction(sp.cancel(
        4*selected_c**3+6*selected_c**2+5*selected_c+2
    ))[0]
    if sp.rem(selected_numerator, x**3+2*x*x+1, x) != 0:
        raise ArithmeticError("The selected tangent is not on the cubic factor")
    return {
        "third_order_coefficient_derivation": True,
        "commutative_symbol": str(p),
        "stationary_curve_substitution": True,
        "rational_parametrization": True,
        "discriminant": str(discriminant),
        "boundary_action_curve": str(boundary_curve),
        "stationary_resultant_factor": "-Y^3*(Y-1)^3",
        "boundary_resultant_factor": "-(w+1)^5",
        "boundary_tangent_factorization": str(expected_tangent),
        "selected_boundary_tangent": True,
        "arithmetic": "exact rational polynomial identities (SymPy)",
    }


def growth_diagnostics():
    v3 = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
    records = []
    for level in (30, 60, 120, 240, 480, 960):
        products = factorials(level)
        weights = [1/s**2 for s in products]
        period = mp.fsum(weights)
        squared_norm = mp.fsum(w*w for w in weights)
        tail = mp.mpf(0)
        maximum_row_sum = mp.mpf(0)
        for a in reversed(range(level)):
            maximum_row_sum = max(maximum_row_sum, weights[a]*(level**2 + tail))
            if a > 0:
                tail += products[a-1]**2
        records.append({
            "N": level,
            "log_period_over_N": mp.nstr(mp.log(period)/level, 30),
            "log_L2_norm_over_N": mp.nstr(mp.log(squared_norm)/(2*level), 30),
            "log_inverse_norm_over_N": mp.nstr(mp.log(maximum_row_sum)/level, 30),
        })
    return {
        "proved_period_rate": mp.nstr(v3/mp.pi, 35),
        "proved_inverse_norm_rate": mp.nstr(2*v3/mp.pi, 35),
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    result = {
        "scope": "Finite original-algebra identities and exact transport normalization; "
                 "the asymptotic diagnostics do not establish a mixed boundary theorem.",
        "decimal_precision": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "symbolic_checks": symbolic_checks(),
        "exact_checks": exact_checks(args.precision),
        "growth_diagnostics": growth_diagnostics(),
    }
    content = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f"Saved {args.output}.")
    else:
        print(content)


if __name__ == "__main__":
    main()
