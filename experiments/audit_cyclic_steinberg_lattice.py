#!/usr/bin/env python3
"""Exact diagnostics for the uniform cyclic/Steinberg lattice calculation.

The characteristic-zero arguments are in notes/cyclic_steinberg_lattice.md.
These checks use finite fields, including even and composite levels. The
Smith-frame check uses first coefficients in a formal parameter, not a
numerically small parameter or an inferred limiting value.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp


def determinant(matrix, prime):
    work = matrix.copy() % prime
    size = len(work)
    value = 1
    for column in range(size):
        pivot = next((j for j in range(column, size) if work[j, column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[[column, pivot]] = work[[pivot, column]]
            value = -value
        coefficient = int(work[column, column])
        value = value*coefficient % prime
        if column+1 < size:
            multipliers = work[column+1:, column]*pow(coefficient, -1, prime) % prime
            work[column+1:, column:] = (
                work[column+1:, column:]
                - multipliers[:, None]*work[column, column:]) % prime
    return value % prime


def rank(matrix, prime):
    work = matrix.copy() % prime
    row = 0
    for column in range(work.shape[1]):
        pivot = next((j for j in range(row, len(work)) if work[j, column]), None)
        if pivot is None:
            continue
        work[[row, pivot]] = work[[pivot, row]]
        work[row] = work[row]*pow(int(work[row, column]), -1, prime) % prime
        if row+1 < len(work):
            work[row+1:] = (work[row+1:]-work[row+1:, column, None]*work[row]) % prime
        row += 1
        if row == len(work):
            break
    return row


def power(matrix, exponent, prime):
    value = np.eye(len(matrix), dtype=np.int64)
    while exponent:
        if exponent % 2:
            value = value@matrix % prime
        matrix = matrix@matrix % prime
        exponent //= 2
    return value


def cyclic_matrices(n, prime, omega, parameter):
    eye = np.eye(n, dtype=np.int64)
    x = np.zeros((n, n), dtype=np.int64)
    for j in range(n):
        x[(j+1) % n, j] = parameter if j == n-1 else 1
    sigma = np.diag([pow(omega, j, prime) for j in range(n)]).astype(np.int64)
    sigma_inverse = np.diag([pow(omega, -j, prime) for j in range(n)]).astype(np.int64)
    y = (eye-x)@sigma_inverse % prime
    x_inverse = power(x, n-1, prime)*pow(parameter, -1, prime) % prime
    return x, y, sigma, x_inverse


def regular_family(n, prime, q, omega):
    eye = np.eye(n, dtype=np.int64)
    rho = (q-pow(q, -1, prime)) % prime
    nilpotent = None
    for parameter in (1, 2, 3):
        x, f, sigma, xi = cyclic_matrices(n, prime, omega, parameter)
        e = (eye-omega*x)@xi % prime
        e = e@sigma*pow(omega*rho*rho % prime, -1, prime) % prime
        k = -pow(q, -1, prime)*xi % prime
        ki = -q*x % prime
        assert not np.any((k@e-omega*e@k) % prime)
        assert not np.any((k@f-pow(omega, -1, prime)*f@k) % prime)
        assert not np.any((e@f-f@e-pow(rho, -1, prime)*(k-ki)) % prime)
        assert not np.any((rho*rho*f@e+q*k+pow(q, -1, prime)*ki+2*eye) % prime)
        assert np.array_equal(power(f, n, prime), (1-parameter)*eye % prime)
        en = (pow(-1, n-1, prime)*(1-parameter)
              * pow(parameter*pow(rho, 2*n, prime) % prime, -1, prime)) % prime
        kn = pow(-1, n-1, prime)*pow(parameter, -1, prime) % prime
        assert np.array_equal(power(e, n, prime), en*eye % prime)
        assert np.array_equal(power(k, n, prime), kn*eye % prime)
        vacuum = np.zeros(n, dtype=np.int64)
        vacuum[0] = 1
        assert not np.any((x+f-eye)@vacuum % prime)
        assert rank(x+f-eye, prime) == n-1
        if parameter == 1:
            nilpotent = e, f, k

    plus = np.array([[pow(omega, j*a, prime) for a in range(n)]
                     for j in range(n)], dtype=np.int64)
    minus = np.array([[pow(omega, -j*a, prime) for j in range(n)]
                      for a in range(n)], dtype=np.int64)*pow(n, -1, prime) % prime
    ps = [1]
    for j in range(1, n):
        ps.append(ps[-1]*(1-pow(omega, j, prime)) % prime)
    frame = minus*np.array(ps, dtype=np.int64)[None, :] % prime
    inverse = np.array([pow(v, -1, prime) for v in ps], dtype=np.int64)[:, None]*plus % prime
    expected_e = np.zeros((n, n), dtype=np.int64)
    expected_f = np.zeros_like(expected_e)
    for j in range(1, n):
        qinteger = (pow(q, j, prime)-pow(q, -j, prime))*pow(rho, -1, prime) % prime
        expected_e[j-1, j] = qinteger*qinteger % prime
        expected_f[j, j-1] = 1
    expected_k = np.diag([pow(q, n-1-2*j, prime) for j in range(n)]).astype(np.int64)
    for old, new in zip(nilpotent, (expected_e, expected_f, expected_k)):
        assert np.array_equal(inverse@old@frame % prime, new)
    vacuum = np.zeros(n, dtype=np.int64)
    vacuum[0] = 1
    assert np.array_equal(inverse@vacuum % prime,
                          np.array([pow(v, -1, prime) for v in ps]))
    return {"regular_relations_casimir_and_powers": True,
            "parameters_checked": [1, 2, 3], "nilpotent_color_exact": True,
            "vacuum_rank_and_whittaker_coordinates_exact": True}


def pointed_factorization(n, prime, omega):
    s, t = 2, 3
    tau = (1-s*t)*pow(1-t, -1, prime) % prime
    eye = np.eye(n, dtype=np.int64)
    x1, y1, _, _ = cyclic_matrices(n, prime, omega, s)
    x2, y2, sigma2, _ = cyclic_matrices(n, prime, omega, t)
    geometric_sum = np.zeros_like(eye)
    for j in range(n):
        geometric_sum = (geometric_sum+power(x2, j, prime)) % prime
    y2_inverse = sigma2@geometric_sum*pow(1-t, -1, prime) % prime
    xt = np.kron(x1, x2) % prime
    yt = (np.kron(x1, y2)+np.kron(y1, eye)) % prime
    z = np.kron(y1, y2_inverse) % prime
    d = (np.kron(x1, eye)+z) % prime
    c = z@np.kron(eye, x2) % prime
    vacuum = np.zeros(n*n, dtype=np.int64)
    vacuum[0] = 1
    block = [vacuum]
    for j in range(1, n):
        block.append(d@block[-1] % prime)
    block = np.column_stack(block)
    blocks = [block]
    for j in range(1, n):
        blocks.append(xt@blocks[-1] % prime)
    recoupling = np.hstack(blocks)
    u, v, _, _ = cyclic_matrices(n, prime, omega, s*t % prime)
    r, b, _, _ = cyclic_matrices(n, prime, omega, tau)
    for old, new in ((xt, np.kron(u, eye)), (yt, np.kron(v, eye)),
                     (d, np.kron(eye, r)), (-c % prime, np.kron(eye, b))):
        assert not np.any((old@recoupling-recoupling@new) % prime)
    assert np.array_equal(recoupling@vacuum % prime, vacuum)
    f = t*(1-s*t)*pow((1-t)**2, -1, prime) % prime
    sign = pow(-1, n*(n-1)**2//2, prime)
    actual = determinant(recoupling, prime)
    assert actual == sign*pow(f, n*(n-1)//2, prime) % prime
    return {"four_intertwiners_and_vacuum": True, "determinant": actual,
            "even_level_sign_retained": True, "dimension": n*n}


def endpoint_chain(n, prime, q, omega, factors):
    """The actual Hopf coproduct with the prescribed endpoint twists."""
    kappa = -q % prime
    eye = np.eye(n, dtype=np.int64)
    u_total = np.ones((1, 1), dtype=np.int64)
    f_total = np.zeros((1, 1), dtype=np.int64)
    w_total = np.ones((1, 1), dtype=np.int64)
    parameter = 1
    for position in range(1, factors+1):
        t = position+1
        parameter = parameter*t % prime
        x, f, _, _ = cyclic_matrices(n, prime, omega, t)
        c = pow(kappa, 1-position, prime)
        a, b = pow(kappa, -position, prime), c
        local_unit = np.zeros(n, dtype=np.int64)
        local_unit[0] = 1
        local_u = kappa*x % prime
        local_f = c*f % prime
        assert not np.any((local_f+a*local_u-b*eye)@local_unit % prime)
        if position > 1:
            assert previous_a == b
        previous_a = a
        f_total = (np.kron(f_total, eye)+np.kron(u_total, local_f)) % prime
        u_total = np.kron(u_total, local_u) % prime
        w_total = np.kron(w_total, x) % prime
    vacuum = np.zeros(n**factors, dtype=np.int64)
    vacuum[0] = 1
    image = [vacuum]
    for j in range(1, n):
        image.append(w_total@image[-1] % prime)
    embedding = np.column_stack(image)
    x, f, _, _ = cyclic_matrices(n, prime, omega, parameter)
    assert rank(embedding, prime) == n
    assert not np.any((f_total@embedding-embedding@f) % prime)
    assert not np.any((u_total@embedding-pow(kappa, factors, prime)*embedding@x) % prime)
    identity = np.eye(n**factors, dtype=np.int64)
    assert np.array_equal(power(f_total, n, prime), (1-parameter)*identity % prime)
    assert np.array_equal(power(u_total, n, prime),
                          pow(kappa, factors*n, prime)*parameter*identity % prime)
    return {"factors": factors, "matched_endpoint_equations_exact": True,
            "Borel_embedding_rank": n, "two_intertwiners_exact": True,
            "central_marks_retained": True}


def smith_frames(n, prime, omega, a, b):
    """Leading coefficients of (4.3) and its explicit integral frames."""
    residues = []
    for i in range(n):
        ri = (-i) % n or n
        residue = np.zeros((n, n), dtype=np.int64)
        frame = np.zeros_like(residue)
        for j in range(n):
            numerator_order = denominator_order = 0
            numerator_lead = denominator_lead = 1
            for d in range(n):
                if d:
                    for coordinate, slope, numerator in ((i, a+b, True), (j, b, False)):
                        phase = pow(omega, d+coordinate, prime)
                        if phase == 1:
                            order = 1
                            lead = slope*pow(n, -1, prime) % prime
                        else:
                            order, lead = 0, (1-phase) % prime
                        if numerator:
                            numerator_order += order
                            numerator_lead = numerator_lead*lead % prime
                        else:
                            denominator_order += order
                            denominator_lead = denominator_lead*lead % prime
                order = numerator_order-denominator_order
                lead = numerator_lead*pow(denominator_lead, -1, prime) % prime
                assert order >= -1
                if order == -1:
                    residue[j, d] = lead
                scaled_order = order+int(1 <= d < ri)
                assert scaled_order >= 0
                if scaled_order == 0:
                    frame[j, d] = lead
        residue_rank = rank(residue, prime)
        assert residue_rank == ri-1
        assert determinant(frame, prime)
        residues.append(residue_rank)
    assert sum(residues) == n*(n-1)//2
    return {"direction": [a, b], "residue_ranks": residues,
            "all_scaled_frames_integral_with_unit_determinant": True,
            "negative_invariant_factors": sum(residues),
            "zero_invariant_factors": n*n-sum(residues)}


def audit(n):
    prime = next(4*n*k+1 for k in range(1, 1000) if sp.isprime(4*n*k+1))
    primitive = int(sp.primitive_root(prime))
    q = pow(primitive, (prime-1)//(2*n), prime)
    omega = q*q % prime
    return {"level": n, "finite_field_prime": prime,
            "regular_family": regular_family(n, prime, q, omega),
            "factorization": pointed_factorization(n, prime, omega),
            "endpoint_chains": [endpoint_chain(n, prime, q, omega, factors)
                                for factors in ([2, 3, 4] if n <= 4 else
                                                [2, 3] if n <= 6 else [2])],
            "smith_frames": [smith_frames(n, prime, omega, a, b)
                             for a, b in ((2, 3), (5, 7))]}


def main():
    results = {"scope": "Diagnostics for uniform local algebra and lattice proofs; no knot-volume claim.",
               "records": [audit(n) for n in (2, 3, 4, 5, 6, 9, 15)]}
    Path(__file__).with_name("cyclic_steinberg_lattice_results.json").write_text(
        json.dumps(results, indent=2)+"\n")
    print(json.dumps(results), flush=True)


if __name__ == "__main__":
    main()
