#!/usr/bin/env python3
"""Exact checks of the literature crossing on the recoupling lattice.

The finite R and confluent Casimir polynomial are evaluated independently.
Formal lattice fibers use leading coefficients, never a small numerical
parameter. Uniform arguments are in the corresponding research note.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import cyclic_matrices, determinant, power, rank
from audit_kashaev_crossing import cut_braid, original, quantum_group


def solve(matrix, vector, prime):
    work = np.column_stack((matrix, vector)).copy() % prime
    size = len(vector)
    for column in range(size):
        pivot = next(row for row in range(column, size) if work[row, column])
        work[[column, pivot]] = work[[pivot, column]]
        work[column] = work[column]*pow(int(work[column, column]), -1, prime) % prime
        for row in range(size):
            if row != column:
                work[row] = (work[row]-int(work[row, column])*work[column]) % prime
    return work[:, -1]


def evaluate(coefficients, matrix, prime):
    value = np.zeros_like(matrix)
    eye = np.eye(len(matrix), dtype=np.int64)
    for coefficient in reversed(coefficients):
        value = (value@matrix+int(coefficient)*eye) % prime
    return value


def chebyshev(matrix, n, prime):
    before = 2*np.eye(len(matrix), dtype=np.int64)
    current = matrix.copy()
    if n == 0:
        return before
    for j in range(1, n):
        before, current = current, (matrix@current-before) % prime
    return current


def swap(n):
    value = np.zeros((n*n, n*n), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            value[b*n+a, a*n+b] = 1
    return value


def highest_matrices(n, prime, q):
    rho = (q-pow(q, -1, prime)) % prime
    e = np.zeros((n, n), dtype=np.int64)
    f = np.zeros_like(e)
    integers = [(pow(q, j, prime)-pow(q, -j, prime))*pow(rho, -1, prime) % prime
                for j in range(n+1)]
    for j in range(1, n):
        e[j-1, j] = integers[j]*integers[n-j] % prime
        f[j, j-1] = 1
    k = np.diag([pow(q, n-1-2*j, prime) for j in range(n)]).astype(np.int64)
    ki = np.diag([pow(q, -n+1+2*j, prime) for j in range(n)]).astype(np.int64)
    return e, f, k, ki, integers


def tensor_casimir(n, prime, q, e, f, k, ki):
    eye = np.eye(n, dtype=np.int64)
    rho = (q-pow(q, -1, prime)) % prime
    et = (np.kron(e, k)+np.kron(eye, e)) % prime
    ft = (np.kron(f, eye)+np.kron(ki, f)) % prime
    return (rho*rho*ft@et+q*np.kron(k, k)+pow(q, -1, prime)*np.kron(ki, ki)) % prime


def hermite_polynomials(n, prime, q):
    rows, values, inverse_values, simple_rows, simple_values = [], [], [], [], []
    for k in range((n+1)//2):
        c = (pow(q, 2*k+1, prime)+pow(q, -2*k-1, prime)) % prime
        nu = pow(-1, k, prime)*pow(q, k*(k+1), prime) % prime
        row = [pow(c, h, prime) for h in range(n)]
        rows.append(row)
        values.append(nu)
        inverse_values.append(pow(nu, -1, prime))
        simple_rows.append(row[:(n+1)//2])
        simple_values.append(nu)
        if 2*k+1 < n:
            slope = (-nu*(n-1-2*k)
                     *pow(2*(pow(q, 2*k+1, prime)-pow(q, -2*k-1, prime)) % prime,
                          -1, prime)) % prime
            rows.append([0]+[h*pow(c, h-1, prime) % prime for h in range(1, n)])
            values.append(slope)
            inverse_values.append(-slope*pow(nu, -2, prime) % prime)
    matrix = np.array(rows, dtype=np.int64)
    return (solve(matrix, np.array(values), prime),
            solve(matrix, np.array(inverse_values), prime),
            solve(np.array(simple_rows), np.array(simple_values), prime))


def cyclic_quantum(n, prime, q, omega, parameter, b=1):
    eye = np.eye(n, dtype=np.int64)
    x, f, sigma, xi = cyclic_matrices(n, prime, omega, parameter)
    kappa = -q % prime
    rho = (q-pow(q, -1, prime)) % prime
    e = (pow(kappa, -b-1, prime)*(xi-pow(omega, b, prime)*eye)@sigma
         *pow(rho*rho % prime, -1, prime)) % prime
    k = pow(kappa, -b, prime)*xi % prime
    return x, f, e, k


def product_embedding(n, prime, q, omega, count, nilpotent=False):
    eye = np.eye(n, dtype=np.int64)
    kappa = -q % prime
    kt = np.ones((1, 1), dtype=np.int64)
    et = np.zeros((1, 1), dtype=np.int64)
    ft = et.copy()
    xt = kt.copy()
    parameter = 1
    for j in range(1, count+1):
        t = 1 if nilpotent else j+1
        parameter = parameter*t % prime
        x, f, e, k = cyclic_quantum(n, prime, q, omega, t)
        c = pow(kappa, 1-j, prime)
        et = (np.kron(et, k)+np.kron(np.eye(len(kt), dtype=np.int64),
                                    pow(c, -1, prime)*e % prime)) % prime
        ft = (np.kron(ft, eye)+np.kron(power(kt, n-1, prime)
              *pow(int(power(kt, n, prime)[0, 0]), -1, prime) % prime, c*f % prime)) % prime
        kt = np.kron(kt, k) % prime
        xt = np.kron(xt, x) % prime
    unit = np.zeros(n**count, dtype=np.int64)
    unit[0] = 1
    columns = [unit]
    for j in range(1, n):
        columns.append(xt@columns[-1] % prime)
    embedding = np.column_stack(columns)
    x, f, e, k = cyclic_quantum(n, prime, q, omega, parameter, count)
    for old, new in ((et, e), (ft, f), (kt, k)):
        assert not np.any((old@embedding-embedding@new) % prime)
    assert rank(embedding, prime) == n
    rho = (q-pow(q, -1, prime)) % prime
    chi = -(pow(kappa, count-1, prime)+pow(kappa, 1-count, prime)) % prime
    assert not np.any((rho*rho*f@e+q*k+pow(q, -1, prime)*pow(kappa, count, prime)*x-chi*eye) % prime)
    en = (pow(kappa, -count*n, prime)*(1-parameter)
          *pow(parameter*pow(rho, 2*n, prime) % prime, -1, prime)) % prime
    assert np.array_equal(power(e, n, prime), en*eye % prime)
    assert np.array_equal(power(f, n, prime), (1-parameter)*eye % prime)
    return {"factors": count, "nilpotent_fiber": nilpotent,
            "full_E_F_K_embedding_exact": True, "source_Casimir_and_powers_exact": True, "rank": n}


def relative_h(n, prime, q, omega, tau):
    value = np.zeros((n, n), dtype=np.int64)
    for j in range(n):
        value[j, j] = (pow(q, 2*j-1, prime)+pow(q, 1-2*j, prime)) % prime
        value[(j+1) % n, j] = (q*(2-pow(omega, j, prime)-pow(omega, -j, prime))
                                 *(tau if j == n-1 else 1)) % prime
    return value


def relative_check(n, prime, q, omega):
    eye = np.eye(n, dtype=np.int64)
    rho = (q-pow(q, -1, prime)) % prime
    kappa = -q % prime
    s, t = 2, 3
    x1, f1, e1, k1 = cyclic_quantum(n, prime, q, omega, s)
    x2, f2, e2, k2 = cyclic_quantum(n, prime, q, omega, t)
    y2i = power(f2, n-1, prime)*pow(1-t, -1, prime) % prime
    z = np.kron(f1, y2i) % prime
    d = (np.kron(x1, eye)+z) % prime
    xt = np.kron(x1, x2) % prime
    ft = (np.kron(f1, eye)+np.kron(x1, f2)) % prime
    et = (np.kron(e1, k2)+kappa*np.kron(eye, e2)) % prime
    casimir = (rho*rho*ft@et+q*np.kron(k1, k2)
               +pow(q, -1, prime)*kappa*kappa*xt) % prime
    unit = np.zeros(n*n, dtype=np.int64)
    unit[0] = 1
    block = [unit]
    for j in range(1, n):
        block.append(d@block[-1] % prime)
    blocks = [np.column_stack(block)]
    for j in range(1, n):
        blocks.append(xt@blocks[-1] % prime)
    cg = np.hstack(blocks)
    tau = (1-s*t)*pow(1-t, -1, prime) % prime
    h = relative_h(n, prime, q, omega, tau)
    assert not np.any((casimir@cg-cg@np.kron(eye, h)) % prime)
    assert not np.any((chebyshev(h, n, prime)+2*eye) % prime)
    vector = np.zeros(n, dtype=np.int64)
    vector[1] = 1
    krylov = [vector]
    for j in range(1, n):
        krylov.append(h@krylov[-1] % prime)
    assert rank(np.column_stack(krylov), prime) == n
    polynomial = np.array([1], dtype=np.int64)
    for j in range(n):
        node = (pow(q, 2*j-1, prime)+pow(q, 1-2*j, prime)) % prime
        polynomial = np.convolve(polynomial, np.array([-node, 1])) % prime
    c0 = (q+pow(q, -1, prime)) % prime

    def divide_at_node(coefficients):
        quotient = np.zeros(len(coefficients)-1, dtype=np.int64)
        quotient[-1] = coefficients[-1]
        for j in range(len(quotient)-2, -1, -1):
            quotient[j] = (coefficients[j+1]+c0*quotient[j+1]) % prime
        assert (int(coefficients[0])+c0*int(quotient[0])) % prime == 0
        return quotient

    socle = divide_at_node(polynomial)
    unit = np.zeros(n, dtype=np.int64)
    unit[0] = 1
    multiplier = tau*pow(q, n-1, prime)*n*n % prime
    assert np.array_equal(evaluate(socle, h, prime)@vector % prime, multiplier*unit % prime)
    preimage = evaluate(divide_at_node(socle), h, prime)@vector % prime
    assert np.array_equal((h-c0*eye)@preimage % prime, multiplier*unit % prime)
    return {"relative_Casimir_intertwiner_exact": True,
            "minimal_polynomial_degree": n, "nonsemisimple_structure_retained": True,
            "vacuum_socle_multiplier_exact": "tau*q^(N-1)*N^2"}


def nilpotent_hilbert90(n, prime):
    """A split cyclic etale cover over F_p[epsilon]/epsilon^2."""
    a = np.arange(2, n+2, dtype=np.int64) % prime
    b = (np.arange(n, dtype=np.int64)**2+1) % prime
    sa, sb = np.roll(a, -1), np.roll(b, -1)
    sai = np.array([pow(int(v), -1, prime) for v in sa], dtype=np.int64)
    r0 = a*sai % prime
    r1 = (b*sai-a*sb*sai*sai) % prime
    norm0, norm1 = 1, 0
    for u, v in zip(r0, r1):
        norm0, norm1 = norm0*int(u) % prime, (norm0*int(v)+norm1*int(u)) % prime
    assert (norm0, norm1) == (1, 0)
    ai = np.array([pow(int(v), -1, prime) for v in a], dtype=np.int64)
    logarithm = r1*sa*ai % prime
    assert int(np.sum(logarithm)) % prime == 0
    h = np.zeros(n, dtype=np.int64)
    for j in range(n):
        h = (h-j*np.roll(logarithm, -j)*pow(n, -1, prime)) % prime
    assert np.array_equal((h-np.roll(h, -1)) % prime, logarithm)
    corrected1 = a*h % prime
    assert np.array_equal(r0*np.roll(a, -1) % prime, a)
    assert np.array_equal((r0*np.roll(corrected1, -1)+r1*np.roll(a, -1)) % prime, corrected1)
    return {"dual_number_norm_one": True, "explicit_logarithmic_Hilbert90_exact": True}


def pivotal_trace(n, prime, q, casimir, k, positive, negative):
    def spectral(coefficients):
        value = 0
        if n % 2:
            value = sum(int(a)*pow(-2, j, prime) for j, a in enumerate(coefficients)) % prime
        for index in range(n//2):
            c = (pow(q, 2*index+1, prime)+pow(q, -2*index-1, prime)) % prime
            function = sum(int(a)*pow(c, j, prime) for j, a in enumerate(coefficients)) % prime
            derivative = sum(j*int(coefficients[j])*pow(c, j-1, prime)
                             for j in range(1, len(coefficients))) % prime
            value = (value-c*function-(c*c-4)*derivative) % prime
        return value

    eye = np.eye(n, dtype=np.int64)
    matrix_power = np.eye(n*n, dtype=np.int64)
    weight = np.kron(eye, k)
    for degree in range(n):
        coefficients = [0]*n
        coefficients[degree] = 1
        scalar = spectral(coefficients)
        actual = np.einsum('abcb->ac', (matrix_power@weight % prime).reshape(n, n, n, n)) % prime
        assert np.array_equal(actual, scalar*eye % prime)
        matrix_power = matrix_power@casimir % prime
    kappa = -q % prime
    assert spectral([1]) == 0
    assert spectral(positive) == pow(kappa, -1, prime)
    assert spectral(negative) == kappa
    return {"Casimir_monomials_checked": n, "exact_value_and_derivative_functional": True,
            "positive_and_negative_enhancement_phases_exact": True}


def lattice_blocks(n, prime, q, omega, mu, braid, coefficients, a, b):
    """Compare explicit integral CG fibers against the actual finite R."""
    ps = [1]
    for j in range(1, n):
        ps.append(ps[-1]*(1-pow(omega, j, prime)) % prime)
    plus = np.array([[pow(omega, j*h, prime) for h in range(n)]
                     for j in range(n)], dtype=np.int64)
    minus = np.array([[pow(omega, -j*h, prime) for j in range(n)]
                      for h in range(n)], dtype=np.int64)*pow(n, -1, prime) % prime
    frame = minus*np.array(ps)[None, :] % prime
    inverse = np.array([pow(v, -1, prime) for v in ps])[:, None]*plus % prime
    kappa = -q % prime
    c = pow(kappa, -1, prime)
    dc = np.diag([pow(c, j, prime) for j in range(n)]).astype(np.int64)
    dci = np.diag([pow(c, -j, prime) for j in range(n)]).astype(np.int64)
    evaluate_wz = np.array([[pow(omega, (i-j)*h+j*k, prime)
                             for h in range(n) for k in range(n)]
                            for i in range(n) for j in range(n)], dtype=np.int64)
    inverse_wz = np.array([[pow(omega, -(i-j)*h-j*k, prime)
                            for i in range(n) for j in range(n)]
                           for h in range(n) for k in range(n)], dtype=np.int64)*pow(n, -2, prime) % prime
    source = evaluate_wz@np.kron(frame, frame@dc % prime) % prime
    source_inverse = np.kron(inverse, dci@inverse % prime)@inverse_wz % prime
    actual = source@braid % prime
    actual = actual@source_inverse % prime
    tau = (a+b)*pow(b, -1, prime) % prime
    h = relative_h(n, prime, q, omega, tau)
    lambda0 = pow(mu, (n-1)**2, prime)
    for i in range(n):
        ri = (-i) % n or n
        block = np.zeros((n, n), dtype=np.int64)
        for j in range(n):
            no = do = 0
            nl = dl = 1
            for d in range(n):
                if d:
                    for coordinate, slope, numerator in ((i, a+b, True), (j, b, False)):
                        phase = pow(omega, d+coordinate, prime)
                        order = int(phase == 1)
                        lead = slope*pow(n, -1, prime) % prime if order else (1-phase) % prime
                        if numerator:
                            no += order
                            nl = nl*lead % prime
                        else:
                            do += order
                            dl = dl*lead % prime
                order = no-do+int(1 <= d < ri)
                assert order >= 0
                if order == 0:
                    block[j, d] = nl*pow(dl, -1, prime) % prime
        assert determinant(block, prime)
        integral_h = h.copy()
        for row in range(n):
            for column in range(n):
                shift = int(1 <= column < ri)-int(1 <= row < ri)
                if shift > 0:
                    integral_h[row, column] = 0
                elif shift < 0:
                    assert integral_h[row, column] == 0
        actual_block = actual[i*n:(i+1)*n, i*n:(i+1)*n]
        assert not np.any((actual_block@block
                           -lambda0*block@evaluate(coefficients, integral_h, prime)) % prime)
        for other in range(n):
            if other != i:
                assert not np.any(actual[i*n:(i+1)*n, other*n:(other+1)*n])
    return {"direction": [a, b], "integral_blocks_checked": n,
            "actual_crossing_on_special_fiber_exact": True}


def generic_check(n):
    prime = 1009
    mu = int(sp.primitive_root(prime))
    q = mu*mu % prime
    rho = (q-pow(q, -1, prime)) % prime
    e, f, k, ki, integers = highest_matrices(n, prime, q)
    casimir = tensor_casimir(n, prime, q, e, f, k, ki)
    rq = np.zeros((n*n, n*n), dtype=np.int64)
    factorial = [1]
    for j in range(1, n):
        factorial.append(factorial[-1]*integers[j] % prime)
    for a in range(n):
        for b in range(n):
            ec = 1
            for j in range(min(a, n-1-b)+1):
                if j:
                    ec = ec*integers[a-j+1]*integers[n-a+j-1] % prime
                c, d = a-j, b+j
                rq[c*n+d, a*n+b] = (ec*pow(q, j*(j-1)//2, prime)*pow(rho, j, prime)
                    *pow(factorial[j], -1, prime)*pow(mu, (n-1-2*c)*(n-1-2*d), prime)) % prime
    nodes = [(pow(q, 2*n-1-2*j, prime)+pow(q, -2*n+1+2*j, prime)) % prime
             for j in range(n)]
    rows = np.array([[pow(c, h, prime) for h in range(n)] for c in nodes], dtype=np.int64)
    values = np.array([pow(-1, j, prime)*pow(q, -j*(2*n-1-j), prime) % prime
                       for j in range(n)], dtype=np.int64)
    coefficients = solve(rows, values, prime)
    expected = evaluate(coefficients, casimir, prime)*pow(mu, (n-1)**2, prime) % prime
    assert np.array_equal(swap(n)@rq % prime, expected)
    return {"dimension": n, "generic_parameter_prime": prime,
            "noncolliding_Casimir_interpolation_exact": True}


def audit(n):
    prime = next(4*n*j+1 for j in range(1, 1000) if sp.isprime(4*n*j+1))
    primitive = int(sp.primitive_root(prime))
    mu = pow(primitive, (prime-1)//(4*n), prime)
    q, omega = pow(mu, 2, prime), pow(mu, 4, prime)
    e, f, k, ki, _ = highest_matrices(n, prime, q)
    casimir = tensor_casimir(n, prime, q, e, f, k, ki)
    coefficients, inverse_coefficients, semisimple = hermite_polynomials(n, prime, q)
    positive = evaluate(coefficients, casimir, prime)
    negative = evaluate(inverse_coefficients, casimir, prime)
    rq, rqi = quantum_group(n, prime, mu)
    permutation = swap(n)
    braid = permutation@rq % prime
    lambda0 = pow(mu, (n-1)**2, prime)
    assert np.array_equal(lambda0*positive % prime, braid)
    assert np.array_equal(pow(lambda0, -1, prime)*negative % prime, rqi@permutation % prime)
    big_eye = np.eye(n*n, dtype=np.int64)
    assert np.array_equal(positive@negative % prime, big_eye)
    assert not np.any((chebyshev(casimir, n, prime)+2*big_eye) % prime)
    assert np.any((positive-evaluate(semisimple, casimir, prime)) % prime)
    cuts = 0
    if n <= 5:
        r_original, printed_inverse, _ = original(n, prime, omega)
        bk = permutation@r_original.T % prime
        bki = printed_inverse.T@permutation*pow(omega, -1, prime) % prime
        shift = np.roll(np.eye(n, dtype=np.int64), 1, axis=0)
        kappa = -q % prime
        cuts = cut_braid(n, prime, bk, bki, positive, negative,
                         kappa*shift % prime, k, kappa, pow(kappa, -1, prime))
    return {"level": n, "finite_field_prime": prime,
            "positive_and_inverse_R_polynomials_exact": True,
            "derivatives_necessary": True,
            "normalized_polynomial_coefficients": coefficients.tolist(),
            "original_Kashaev_cut_period_checks": cuts,
            "product_embeddings": [product_embedding(n, prime, q, omega, count, nilpotent)
                                   for count in ([2, 3] if n <= 6 else [2])
                                   for nilpotent in (False, True)],
            "relative_Casimir": relative_check(n, prime, q, omega),
            "nilpotent_Hilbert90": nilpotent_hilbert90(n, prime),
            "pivotal_trace": pivotal_trace(n, prime, q, casimir, k, coefficients, inverse_coefficients),
            "lattice_fibers": [lattice_blocks(n, prime, q, omega, mu, braid, coefficients, a, b)
                               for a, b in ((2, 3), (5, 7))]}


def main():
    result = {"scope": "Actual crossing and recoupling lattice comparison; no global regulator-norm theorem.",
              "generic_checks": [generic_check(n) for n in (2, 3, 4, 5, 6, 7)],
              "root_checks": [audit(n) for n in (2, 3, 4, 5, 6, 9, 15)]}
    Path(__file__).with_name("casimir_braiding_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
