#!/usr/bin/env python3
"""Diagnostics for the independent finite-sum annihilator argument.

Checks an auxiliary generic-q cut lift against the actual root matrices,
global certificates including both finite-sum boundaries, and repairs
for vanishing summation and central specializations. No volume assertion.
"""

import json
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

from audit_kashaev_ado_pointing import color_matrices, reduced_period, WORDS


def field(N):
    prime = next(4*N*k+1 for k in range(10, 1000) if sp.isprime(4*N*k+1))
    generator = int(sp.primitive_root(prime))
    root = pow(generator, (prime-1)//(2*N), prime)
    return prime, generator, root


def scalar_data(N, prime, q, x):
    rho = (q-pow(q, -1, prime)) % prime
    integers = [0]+[(pow(q, k, prime)-pow(q, -k, prime))*pow(rho, -1, prime) % prime
                    for k in range(1, N)]
    factorials = [1]
    for k in range(1, N):
        factorials.append(factorials[-1]*integers[k] % prime)
    e = [0]+[integers[a]*(x*pow(q, 1-a, prime)-pow(x, -1, prime)*pow(q, a-1, prime))
             *pow(rho, -1, prime) % prime for a in range(1, N)]
    positive = [pow(q, k*(k-1)//2, prime)*pow(rho, k, prime)
                *pow(factorials[k], -1, prime) % prime for k in range(N)]
    inverse = [pow(-1, k, prime)*pow(q, -k*(k-1)//2, prime)*pow(rho, k, prime)
               *pow(factorials[k], -1, prime) % prime for k in range(N)]
    return e, positive, inverse


def generic_crossing_inverse(N, prime, q, x):
    e, coefficients, inverses = scalar_data(N, prime, q, x)
    rho = (q-pow(q, -1, prime)) % prime
    factorial = [1]
    pochhammer = [1]
    for a in range(1, N):
        integer = (pow(q, a, prime)-pow(q, -a, prime))*pow(rho, -1, prime) % prime
        factorial.append(factorial[-1]*integer % prime)
        pochhammer.append(pochhammer[-1]*(1-pow(q, 2*a, prime)) % prime)
        rewritten = (pow(q, -a*(a-1)//2, prime)*pochhammer[-1]
                     *pow(1-q*q, -a, prime)) % prime
        assert rewritten == factorial[-1]
    for a in range(N):
        direct = 1
        for k in range(a+1):
            if k:
                direct = direct*e[a-k+1] % prime
            poch_value = 1
            for r in range(k):
                poch_value = poch_value*(1-x*x*pow(q, 2-2*a+2*r, prime)) % prime
            proper = (factorial[a]*pow(factorial[a-k], -1, prime)
                      *pow(-pow(x, -1, prime), k, prime)
                      *pow(q, k*(a-1)-k*(k-1)//2, prime)
                      *pow(rho, -k, prime)*poch_value) % prime
            assert direct == proper
    E = np.zeros((N, N), dtype=np.int64)
    F = np.zeros_like(E)
    for j in range(1, N):
        E[j-1, j] = e[j]
        F[j, j-1] = 1
    nilpotent = np.kron(E, F)
    power = np.eye(N*N, dtype=np.int64)
    theta = np.zeros_like(power)
    inverse = np.zeros_like(power)
    for a, b in zip(coefficients, inverses):
        theta = (theta+a*power) % prime
        inverse = (inverse+b*power) % prime
        power = power@nilpotent % prime
    assert not np.any(power)
    assert np.array_equal(theta@inverse % prime, np.eye(N*N, dtype=np.int64))
    diagonal = np.diag([pow(x, -a-b, prime)*pow(q, 2*a*b, prime) % prime
                        for a, b in product(range(N), repeat=2)]).astype(np.int64)
    diagonal_inverse = np.diag([pow(int(diagonal[j, j]), -1, prime)
                                for j in range(N*N)]).astype(np.int64)
    swap = np.zeros_like(theta)
    for a, b in product(range(N), repeat=2):
        swap[b*N+a, a*N+b] = 1
    positive = swap@diagonal % prime
    positive = positive@theta % prime
    negative = inverse@diagonal_inverse % prime
    negative = negative@swap % prime
    old = color_matrices(N, prime, q, x)
    assert np.array_equal(positive, old[0])
    assert np.array_equal(negative, old[1])
    return old


def cut_entry_by_paths(N, prime, q, x, strands, word, cut_color=0):
    """Literal finite state sum over the proper crossing products."""
    e, positive, inverse = scalar_data(N, prime, q, x)
    total = 0
    writhe = sum(sign for _, sign in word)
    for closed in product(range(N), repeat=strands-1):
        initial = (cut_color,)+closed
        weight = 1
        for a in closed:
            weight = (weight*pow(x, 1-N, prime)*pow(q, 2*a*(N-1), prime)) % prime
        paths = {initial: weight}
        for position, sign in reversed(word):
            following = {}
            for state, previous_weight in paths.items():
                a, b = state[position:position+2]
                start_e = a if sign > 0 else b
                maximum = min(a, N-1-b) if sign > 0 else min(b, N-1-a)
                product_e = 1
                for k in range(maximum+1):
                    if k:
                        product_e = product_e*e[start_e-k+1] % prime
                    if sign > 0:
                        c, d = a-k, b+k
                        scalar = (positive[k]*product_e*pow(x, -c-d, prime)*pow(q, 2*c*d, prime)) % prime
                        pair = (d, c)
                    else:
                        scalar = (inverse[k]*product_e*pow(x, a+b, prime)*pow(q, -2*a*b, prime)) % prime
                        pair = (b-k, a+k)
                    new_state = state[:position]+pair+state[position+2:]
                    following[new_state] = (following.get(new_state, 0)+previous_weight*scalar) % prime
            paths = following
        total = (total+paths.get(initial, 0)) % prime
    return total*pow(x, writhe*(N-1), prime) % prime


def cut_matrix_dense(N, prime, data, strands, word):
    positive, negative, pivotal, theta = data
    eye = np.eye(N, dtype=np.int64)
    value = np.eye(N**strands, dtype=np.int64)
    for position, sign in word:
        crossing = positive if sign > 0 else negative
        if strands == 3:
            crossing = np.kron(crossing, eye) if position == 0 else np.kron(eye, crossing)
        value = value@crossing % prime
    closing = eye
    for _ in range(strands-1):
        closing = np.kron(closing, pivotal)
    value = value@closing % prime
    if strands == 2:
        cut = np.einsum('abcb->ac', value.reshape((N,)*4)) % prime
    else:
        cut = np.einsum('abcdbc->ad', value.reshape((N,)*6)) % prime
    return cut*pow(theta, -sum(sign for _, sign in word), prime) % prime


def cut_lift_check(N):
    prime, generator, root = field(N)
    records = []
    for root_level, q in ((False, generator), (True, root)):
        x = pow(generator, N+7, prime)
        data = generic_crossing_inverse(N, prime, q, x)
        comparisons = 0
        nonscalar_lift_seen = False
        for strands, word in [(2, [(0, 1)]*3), (3, WORDS[0]), (3, WORDS[1]), (3, WORDS[2])]:
            matrix = cut_matrix_dense(N, prime, data, strands, word)
            for color in (0, 1):
                path = cut_entry_by_paths(N, prime, q, x, strands, word, color)
                assert path == int(matrix[color, color])
                comparisons += 1
            scalar = np.array_equal(matrix, int(matrix[0, 0])*np.eye(N, dtype=np.int64) % prime)
            if root_level:
                assert scalar
            else:
                nonscalar_lift_seen |= not scalar
        if root_level:
            anchor = color_matrices(N, prime, q, 1)
            assert reduced_period(N, prime, *anchor, WORDS[0]) == 1
            kashaev_x = pow(q, N-1, prime)
            specialized = color_matrices(N, prime, q, kashaev_x)
            path = cut_entry_by_paths(N, prime, q, kashaev_x, 3, WORDS[0])
            assert path == reduced_period(N, prime, *specialized, WORDS[0])
        records.append({"at_actual_root": root_level,
                        "generic_inverse_series_exact": True,
                        "proper_factorial_and_aligned_Pochhammer_rewrite_exact": True,
                        "path_sum_dense_cut_comparisons": comparisons,
                        "generic_lift_can_be_nonscalar": nonscalar_lift_seen if not root_level else None,
                        "actual_root_scalar_and_anchor_checked": root_level})
    return {"level": N, "finite_field_prime": prime, "records": records}


def toy_global_certificate(N, prime, q, x, gaussian, factorial):
    z = pow(q, N, prime)

    def summand(m, k):
        if not 0 <= k < N:
            return 0
        value = pow(q, gaussian*k*(k-1)//2, prime)*pow(m, k, prime) % prime
        if factorial:
            denominator = 1
            for a in range(1, k+1):
                denominator = denominator*(1-pow(q, 2*a, prime)) % prime
            value = value*pow(denominator, -1, prime) % prime
        return value

    def defect(m, k):
        if factorial:
            return (summand(m, k+1)-summand(q*q*m % prime, k+1)
                    -m*summand(pow(q, gaussian, prime)*m % prime, k)) % prime
        return (summand(m, k+1)-m*summand(pow(q, gaussian, prime)*m % prime, k)) % prime

    def first_annihilation(m, k):
        return (defect(q*m % prime, k)-z*defect(m, k)) % prime

    for k in range(-3, N+3):
        result = first_annihilation(x, k)
        if not factorial:
            result = (first_annihilation(q*x % prime, k)-result) % prime
        assert result == 0

    def total(m):
        return sum(summand(m, k) for k in range(N)) % prime

    def reduced_defect(m):
        if factorial:
            return (total(m)-total(q*q*m % prime)-m*total(pow(q, gaussian, prime)*m % prime)) % prime
        return (total(m)-m*total(pow(q, gaussian, prime)*m % prime)) % prime

    def reduced_first(m):
        return (reduced_defect(q*m % prime)-z*reduced_defect(m)) % prime

    value = reduced_first(x)
    if not factorial:
        value = (reduced_first(q*x % prime)-value) % prime
    assert value == 0
    return True


def boundary_certificates():
    records = []
    for N in (2, 3, 4, 5, 6, 9, 15):
        prime, generic, root = field(N)
        for root_level, q in ((False, generic), (True, root)):
            for gaussian, factorial in product((0, 1), repeat=2):
                assert toy_global_certificate(N, prime, q, 3, gaussian, factorial)
                records.append({"level": N, "at_actual_root": root_level,
                                "quadratic_q_weight": bool(gaussian),
                                "reciprocal_q_factorial": bool(factorial),
                                "global_boundary_and_summed_certificate": True})
    return records


def triangular_support_cases():
    records = []
    for N in (2, 3, 4, 5, 6, 9, 15):
        prime, generic, root = field(N)
        for at_root, q in ((False, generic), (True, root)):
            z = pow(q, N, prime)

            def total(x):
                return sum(pow(x, k, prime) for ell in range(N) for k in range(ell+1)) % prime

            # (T-1)(T-q)(T-q*z)(1-x)^2 annihilates the triangular sum.
            coefficients = [-q*q*z, q+q*z+q*q*z, -(1+q+q*z), 1]
            for x in (2, 3, pow(generic, 4, prime)):
                values = [(1-x*pow(q, j, prime))**2*total(x*pow(q, j, prime) % prime) % prime
                          for j in range(4)]
                assert sum(a*b for a, b in zip(coefficients, values)) % prime == 0
                numerator = (1-x)**2*total(x) % prime
                exact = (N-(N+1)*x+pow(x, N+1, prime)) % prime
                assert numerator == exact
            records.append({"level": N, "at_actual_root": at_root,
                            "support": "0 <= k <= ell < N",
                            "coupled_boundary_sum_and_operator_exact": True})
    return records


def symbolic_moment_and_specialization():
    q, x, w, z = sp.symbols("q x w z")
    N = 4
    coefficients = [q**(k*(k-1)//2)/sp.prod(1-q**(2*a) for a in range(1, k+1))
                    for k in range(N)]
    weighted = sum(coefficient*(x*w)**k for k, coefficient in enumerate(coefficients))

    def defect(value):
        return (value-value.subs(x, q*q*x))/w-x*value.subs(x, q*x)

    def certificate(value):
        g = defect(value)
        return g.subs(x, q*x)-q**N*g

    assert sp.cancel(certificate(weighted)) == 0
    # P=(S-1)*certificate has zero direct summation specialization.
    # Its first nonzero formal moment gives the certificate at S=1.
    repaired = sp.diff((1/w-1)*certificate(weighted), w).subs(w, 1)
    assert sp.cancel(repaired) == 0
    generic_coefficients = [-z/w, 1/w+z*x, z/w-q*x, -1/w]
    vanished = [(1/w-1)*a for a in generic_coefficients]
    assert all(a.subs(w, 1) == 0 for a in vanished)
    extracted = [sp.diff(a, w).subs(w, 1) for a in vanished]
    assert all(sp.cancel(a+b.subs(w, 1)) == 0
               for a, b in zip(extracted, generic_coefficients))
    assert any(a != 0 for a in extracted)
    ordinary = weighted.subs(w, 1)
    original = ordinary-ordinary.subs(x, q*q*x)-x*ordinary.subs(x, q*x)
    assert sp.cancel(original.subs(x, q*x)-q**N*original) == 0

    # A common central factor can erase every coefficient at z=-1.
    # Strip it in the generic identity, before making that evaluation.
    operator_coefficients = [-z, 1+z*x, z-q*x, sp.Integer(-1)]
    multiplied = [(z+1)**3*a for a in operator_coefficients]
    assert all(a.subs(z, -1) == 0 for a in multiplied)
    stripped = [sp.cancel(a/(z+1)**3) for a in multiplied]
    assert any(a.subs(z, -1) != 0 for a in stripped)
    return {"finite_weighted_sum_certificate_exact": True,
            "vanishing_direct_summation_repaired_by_first_moment": True,
            "stripped_central_operator_factor_order": 3,
            "nonzero_after_z_equals_minus_one": True}


def main():
    results = {"scope": "Checks proof ingredients; no efficient minimal operator or volume claim.",
               "actual_cut_lifts": [cut_lift_check(N) for N in (2, 3, 4, 5, 6)],
               "global_boundary_certificates": boundary_certificates(),
               "triangular_support": triangular_support_cases(),
               "moments_and_specialization": symbolic_moment_and_specialization()}
    path = Path(__file__).with_name("finite_sum_annihilator_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"actual_cut_lift_levels": len(results["actual_cut_lifts"]),
                      "global_boundary_cases": len(results["global_boundary_certificates"]),
                      "triangular_support_cases": len(results["triangular_support"]),
                      "symbolic_moment_and_central_repairs": "passed", "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
