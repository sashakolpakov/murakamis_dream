#!/usr/bin/env python3
"""Actual Euler atoms, cyclic completion, and mixed boundary pentagons.

All algebraic checks are exact over split finite fields. Complex bound
samples are diagnostics of the separately proved uniform estimate.
No selected geometric knot period or volume theorem is asserted.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_peripheral_fusion import module
from audit_cyclic_steinberg_lattice import determinant
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices
from audit_regular_holonomy_braiding import mm
from audit_semicyclic_carry_braiding import positive, swap


class CentralJetPlane:
    """PBW algebra modulo (X^(2N),Y^(2N)); the UV corner is retained."""

    def __init__(self, N, prime, Q):
        self.N, self.p, self.Q = N, prime, Q

    def clean(self, polynomial):
        return {ab: int(c) % self.p for ab, c in polynomial.items()
                if c % self.p and ab[0] < 2 * self.N and ab[1] < 2 * self.N}

    def add(self, *polynomials):
        out = {}
        for polynomial in polynomials:
            for ab, c in polynomial.items():
                out[ab] = (out.get(ab, 0) + int(c)) % self.p
        return self.clean(out)

    def scale(self, polynomial, scalar):
        return self.clean({ab: c * scalar for ab, c in polynomial.items()})

    def multiply(self, left, right):
        out = {}
        for (a, b), v in left.items():
            for (c, d), w in right.items():
                ab = a + c, b + d
                if ab[0] >= 2 * self.N or ab[1] >= 2 * self.N:
                    continue
                out[ab] = (out.get(ab, 0) + v * w * pow(self.Q, -b * c, self.p)) % self.p
        return self.clean(out)

    def product(self, *polynomials):
        out = {(0, 0): 1}
        for polynomial in polynomials:
            out = self.multiply(out, polynomial)
        return out

    def series(self, coefficients, variable):
        if variable == "x":
            return self.clean({(j, 0): c for j, c in enumerate(coefficients)})
        if variable == "y":
            return self.clean({(0, j): c for j, c in enumerate(coefficients)})
        assert variable == "t"  # T=-YX.
        return self.clean({(j, j): c * pow(-1, j, self.p)
                           * pow(self.Q, -j * (j + 1) // 2, self.p)
                           for j, c in enumerate(coefficients)})


def euler_coefficients(N, prime, Q):
    factorials, coefficients = [1], [1]
    for j in range(1, N):
        factorials.append(factorials[-1] * (1 - pow(Q, j, prime)) % prime)
        coefficients.append(pow(-1, j, prime) * pow(Q, j * (j - 1) // 2, prime)
                            * pow(factorials[-1], -1, prime) % prime)
    assert factorials[-1] == N % prime
    assert coefficients[-1] == Q * pow(N, -1, prime) % prime
    for j in range(1, N):
        assert ((pow(Q, j, prime) - 1) * coefficients[j]
                - pow(Q, j - 1, prime) * coefficients[j - 1]) % prime == 0
    assert -pow(Q, N - 1, prime) * coefficients[-1] % prime == -pow(N, -1, prime) % prime
    return coefficients, factorials


def convolution(left, right, length, prime):
    result = [0] * length
    for i, x in enumerate(left):
        for j, y in enumerate(right[:length - i]):
            result[i + j] = (result[i + j] + x * y) % prime
    return result


def literal_cyclic_series(N, prime, Q):
    """Direct expansion of the published finite product, through X^(2N-1)."""
    length = 2 * N
    result = [0] * length
    result[0] = 1
    result[N] = -(N - 1) * pow(2 * N, -1, prime) % prime
    for r in range(1, N):
        exponent = -r * pow(N, -1, prime) % prime
        factor = [1]
        for k in range(1, length):
            factor.append(factor[-1] * (exponent - k + 1) * pow(k, -1, prime)
                          * (-pow(Q, r, prime)) % prime)
        result = convolution(result, factor, length, prime)
    return result


def source_and_pentagon_case(N):
    prime, _, q = field(N)
    Q = q * q % prime
    c, factorials = euler_coefficients(N, prime, Q)
    direct = literal_cyclic_series(N, prime, Q)
    assert direct[:N] == c
    invN = pow(N, -1, prime)
    r0 = sum(k * pow(1 - pow(Q, k, prime), -1, prime)
             for k in range(1, N)) * pow(N, -2, prime) % prime
    harmonic, r = 0, []
    for j in range(N):
        if j:
            harmonic = (harmonic + pow(1 - pow(Q, j, prime), -1, prime)) % prime
        r.append(c[j] * (r0 + invN * harmonic) % prime)
    assert direct[N:] == r
    assert (r[1] - c[1] * r[0]) % prime != 0

    algebra = CentralJetPlane(N, prime, Q)
    Px, Py, Pt = [algebra.series(c, var) for var in ("x", "y", "t")]
    Rx, Ry, Rt = [algebra.series(r, var) for var in ("x", "y", "t")]
    dx, dy, dt = [algebra.series([j * value % prime for j, value in enumerate(c)], var)
                  for var in ("x", "y", "t")]
    drx, dry = [algebra.series([j * value % prime for j, value in enumerate(r)], var)
               for var in ("x", "y")]
    U, V, UV = {(N, 0): 1}, {(0, N): 1}, {(N, N): 1}
    raw_right = algebra.product(Px, Pt, Py)
    raw_left = algebra.product(Py, Px)
    defect = algebra.add(raw_right, algebra.scale(raw_left, -1))
    assert defect and all(a >= N or b >= N for a, b in defect)
    assert defect[N, 1] == invN * pow(1 - Q, -1, prime) % prime
    assert defect[2 * N - 2, 2 * N - 2] == pow(Q, 3, prime) * pow(N, -3, prime) % prime
    assert (N, 0) not in defect

    # Independently verify the normal-order coefficient convolution.
    for a in range(2 * N - 1):
        for b in range(2 * N - 1):
            expected = sum(c[a - k] * c[b - k] * pow(Q, -k, prime)
                           * pow(factorials[k], -1, prime)
                           for k in range(N) if 0 <= a - k < N and 0 <= b - k < N) % prime
            assert raw_right.get((a, b), 0) == expected

    Bx = algebra.add(Px, algebra.product(U, Rx), algebra.scale(algebra.product(V, dx), -invN),
                     algebra.scale(algebra.product(UV, Rx), -1),
                     algebra.scale(algebra.product(UV, drx), -invN))
    Bt = algebra.add(Pt, algebra.scale(algebra.product(U, dt), invN),
                     algebra.scale(algebra.product(UV, Rt), -1))
    By = algebra.add(Py, algebra.scale(algebra.product(U, dy), invN), algebra.product(V, Ry),
                     algebra.product(UV, algebra.add(algebra.scale(dy, -invN), Ry,
                                                     algebra.scale(dry, invN))))
    first = algebra.add(Py, algebra.product(V, Ry))
    last = algebra.add(Px, algebra.product(U, Rx))
    left = algebra.product(first, Bx)
    right = algebra.product(last, Bt, By)
    assert algebra.add(left, algebra.scale(right, -1)) == {}
    missing_corner = algebra.add(Pt, algebra.scale(algebra.product(U, dt), invN))
    wrong = algebra.product(last, missing_corner, By)
    wrong_residual = algebra.add(left, algebra.scale(wrong, -1))
    assert wrong_residual and all(a >= N and b >= N for a, b in wrong_residual)
    ab = next(iter(wrong_residual))
    complement = {(2 * N - 1 - ab[0], 2 * N - 1 - ab[1]): 1}
    detection = algebra.product(complement, wrong_residual).get((2 * N - 1, 2 * N - 1), 0)
    assert detection
    return {
        "level": N, "prime": prime,
        "actual_Euler_shift_source_is_X_to_N_over_N": True,
        "literal_cyclic_product_and_entire_first_coefficient_jet_exact": True,
        "raw_pentagon_has_noncentral_wrap_terms": True,
        "mixed_UV_jet_pentagon_exact": True,
        "omitting_corner_source_fails": True,
        "explicit_PBW_cosource_detects_omitted_corner": int(detection),
    }


def normalization_determinants(N):
    prime, _, q = field(N)
    Q = q * q % prime
    records = []
    for nu in range(1, prime):
        if any(nu == pow(Q, k, prime) for k in range(1, N)):
            continue
        u = (1 - pow(nu, N, prime)) % prime
        X = np.zeros((N, N), dtype=np.int64)
        for j in range(N - 1):
            X[j + 1, j] = 1
        X[0, N - 1] = u
        T = np.eye(N, dtype=np.int64)
        power, coefficient = T.copy(), 1
        vector = [1]
        for j in range(1, N):
            coefficient = coefficient * pow(Q, j - 1, prime) * pow((pow(Q, j, prime) - nu) % prime, -1, prime) % prime
            vector.append(coefficient)
            power = mm(prime, power, X)
            T = (T + coefficient * power) % prime
        expected = pow(nu, N * (N - 1) // 2, prime)
        for j in range(1, N):
            ratio = (1 - pow(Q, j, prime)) * pow((nu - pow(Q, j, prime)) % prime, -1, prime) % prime
            expected = expected * pow(ratio, N - j, prime) % prime
        assert determinant(T, prime) == expected
        factorial = [1]
        for j in range(1, N):
            factorial.append(factorial[-1] * (1 - pow(Q, j, prime) * nu) % prime)
        endpoint = factorial[-1]
        assert endpoint
        gamma_over_a0 = pow(endpoint, -1, prime)
        reflected = [pow(Q, -j, prime) * factorial[N - 1 - j] * gamma_over_a0 % prime
                     for j in range(N)]
        assert reflected == vector
        if nu != 1:
            shifted_nu = Q * nu % prime
            shifted_vector = [1]
            for j in range(1, N):
                shifted_vector.append(shifted_vector[-1] * pow(Q, j - 1, prime)
                                      * pow((pow(Q, j, prime) - shifted_nu) % prime, -1, prime) % prime)
            for j in range(N):
                multiplier = (1 - pow(Q, -j, prime) * nu) * pow(1 - nu, -1, prime) % prime
                assert shifted_vector[j] == vector[j] * multiplier % prime
        for j in range(N):
            source = ((pow(Q, j, prime) - nu) * vector[j]
                      - pow(Q, j - 1, prime) * vector[(j - 1) % N]) % prime
            assert source == (-(1 - u) * gamma_over_a0 % prime if j == 0 else 0)
        records.append({"nu": nu, "central_U": u, "exact_norm_determinant": int(expected),
                        "full_factorial_vector_and_affine_source_reflection_exact": True,
                        "normalized_argument_shift_transport_checked_away_from_source_wall": nu != 1})
        if len(records) == 4:
            break
    assert len(records) == 4
    return {"level": N, "prime": prime, "Cauchy_Vandermonde_normalization_cases": records}


def actual_R_cases(N):
    prime, generator, q = field(N)
    Q, rho = q * q % prime, (q - pow(q, -1, prime)) % prime
    coefficients, _ = euler_coefficients(N, prime, Q)
    records = []
    for kind, x in (("generic", generator), ("Kashaev", pow(q, N - 1, prime))):
        E, F, _ = module(N, prime, q, x)
        M = -q * x % prime
        endpoint = sum(pow(M * M % prime, j, prime) for j in range(N)) % prime
        zeta = pow(q, N * (1 - N) // 2, prime)
        eta = pow(zeta, 3, prime)
        assert endpoint
        expected_dimension = eta * pow(M, N - 1, prime) * pow(endpoint, -1, prime) % prime
        if kind == "generic":
            wall = pow(q, -1, prime) * (pow(x, -1, prime) - Q * x) % prime
            original_dimension = zeta * wall * pow((pow(x, N, prime) - pow(x, -N, prime)) % prime, -1, prime) % prime
            assert expected_dimension == original_dimension
        else:
            assert M == 1 and endpoint == N % prime
            assert expected_dimension == eta * pow(N, -1, prime) % prime
        assert expected_dimension * pow(eta * pow(M, N - 1, prime) % prime, -1, prime) % prime == pow(endpoint, -1, prime)
        Cartan = np.diag([pow(x, -a - b, prime) * pow(Q, a * b, prime) % prime
                          for a in range(N) for b in range(N)]).astype(np.int64)
        for phi in (0, 3):
            source_F = F.copy()
            source_F[0, N - 1] = phi
            argument = np.kron(E, source_F) * (q * rho * rho % prime) % prime
            power = np.eye(N * N, dtype=np.int64)
            polynomial = power.copy()
            for j in range(1, N):
                power = mm(prime, power, argument)
                polynomial = (polynomial + coefficients[j] * power) % prime
            constructed = mm(prime, swap(N), Cartan, polynomial)
            actual = positive(N, prime, q, x, 0, phi)
            assert np.array_equal(constructed, actual)
            if phi == 0:
                assert np.array_equal(constructed, color_matrices(N, prime, q, x)[0])
            records.append({"color": kind, "F_wrap": phi, "entire_actual_crossing_equal": True,
                            "factorial_source_comparison_retains_full_ADO_dimension": True})
    return {"level": N, "prime": prime, "actual_crossings": records}


def complex_bound_diagnostics():
    mp.mp.dps = 50
    records = []
    parameters = [mp.mpc("0.2"), mp.mpc("0.5", "0.7"),
                  mp.mpc("-2", "0.5"), mp.mpc("2", "1")]
    for N in (8, 16, 32, 64, 128, 256):
        for U in parameters:
            L = mp.log(1 - U)
            nu = mp.exp(L / N)
            logarithms = [mp.log(abs((nu - mp.exp(2j * mp.pi * k / N))
                                    / (1 - mp.exp(2j * mp.pi * k / N))))
                          for k in range(1, N)]
            a0_log_modulus = -(N - 1) * L.real / (2 * N)
            a0_log_modulus += sum(mp.mpf(N - k) / N * logarithms[k - 1] for k in range(1, N))
            running, maximum = a0_log_modulus, abs(a0_log_modulus)
            for term in logarithms:
                running -= term
                maximum = max(maximum, abs(running))
            assert mp.isfinite(maximum)
            records.append({"level": N, "central_U": str(U),
                            "maximum_absolute_log_coefficient_ratio": float(maximum),
                            "maximum_divided_by_log_N": float(maximum / mp.log(N))})
    return {"scope": "Complex numerical diagnostics only; the uniform theorem has an independent proof.",
            "cases": records}


def main():
    levels = tuple(range(2, 16))
    sources = [source_and_pentagon_case(N) for N in levels]
    norms = [normalization_determinants(N) for N in levels]
    actual = [actual_R_cases(N) for N in (2, 3, 4, 5, 6, 8, 9, 10, 12)]
    result = {
        "scope": "Actual Euler atoms, anchored cyclic source completion and coefficient bounds; no selected global knot-period comparison.",
        "exact_boundary_pentagons_and_literal_product_jets": sources,
        "exact_normalization_determinants": norms,
        "actual_quantum_group_crossings": actual,
        "complex_bound_diagnostics": complex_bound_diagnostics(),
    }
    output = Path(__file__).with_name("controlled_cyclic_euler_source_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "result": str(output), "exact_mixed_source_pentagon_levels": len(sources),
        "exact_norm_determinants": sum(len(item["Cauchy_Vandermonde_normalization_cases"]) for item in norms),
        "entire_actual_crossings": sum(len(item["actual_crossings"]) for item in actual),
        "complex_coefficient_bound_diagnostics": len(result["complex_bound_diagnostics"]["cases"]),
    }), flush=True)


if __name__ == "__main__":
    main()
