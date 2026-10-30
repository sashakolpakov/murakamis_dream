"""Exact spectral total derivative versus the original fixed-root matrices."""
import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_small_circle_polynomial_face_insertion import Local, casimir
from audit_actual_braided_two_cut_source_adapter import original_crossings


def symbolic():
    z, w = sp.symbols('z w')
    count = 0
    for N in range(2, 15):
        numerator = 2 * (sp.chebyshevt(N, z / 2) - sp.chebyshevt(N, w / 2))
        actual, remainder = sp.div(numerator, z - w, z)
        assert remainder == 0
        expected = sp.chebyshevu(N - 1, w / 2) + 2 * sum(
            sp.chebyshevt(N - h, z / 2) * sp.chebyshevu(h - 1, w / 2)
            for h in range(1, N))
        assert sp.expand(actual - expected) == 0
        count += 1
    return count


def original_matrices():
    z = sp.symbols('z')
    count = powercount = entries = 0
    for N in range(3, 9):
        loc = Local(N)
        p, q, d = loc.p, loc.q, loc.d
        O = casimir(loc)
        identity = np.eye(N * N, dtype=np.int64)
        powers = [identity]
        for k in range(1, N):
            powers.append(powers[-1] @ O % p)
        cp = sp.Poly(2 * sp.chebyshevt(N, z / 2) + 2, z)
        coefficients = [int(cp.nth(k)) % p for k in range(N + 1)]
        numerators, derivatives = [], []
        for k in range(N):
            c = (pow(q, 2 * k + 1, p) + pow(q, -2 * k - 1, p)) % p
            value = np.zeros_like(identity)
            derivative = np.zeros_like(identity)
            for degree in range(1, N + 1):
                for j in range(degree):
                    exponent = degree - 1 - j
                    value = (value + coefficients[degree] * pow(c, exponent, p)
                             * powers[j]) % p
                    if exponent:
                        derivative = (derivative + coefficients[degree] * exponent
                                      * pow(c, exponent - 1, p) * powers[j]) % p
            numerators.append((c, value))
            derivatives.append(derivative)

        def recover(values):
            result = np.zeros_like(identity)
            for (c, value), derivative, (f, fp) in zip(numerators, derivatives, values):
                result = (result + ((4 - c * c) % p) * (f * derivative + fp * value)
                          - c * f * value) % p
            return result * pow(2 * N * N, -1, p) % p

        for j in range(N):
            values = [(pow(c, j, p), j * pow(c, j - 1, p) % p if j else 0)
                      for c, value in numerators]
            assert np.array_equal(recover(values), powers[j])
            count += 1
            entries += N**4

        _, _, _, crossings = original_crossings(N)
        for eps in (-1, 1):
            actual = identity.copy()
            for k in range(1, 6):
                n = eps * k
                actual = crossings[0 if eps == 1 else 1][0] @ actual % p
                values = []
                for a, (c, value) in enumerate(numerators):
                    h = 2 * a + 1
                    root = (pow(loc.eta, d * d, p) * pow(-1, a, p)
                            * pow(q, a * (a + 1), p)) % p
                    f = pow(root, n, p)
                    # The simple odd node needs only its value. Its arbitrary
                    # derivative is multiplied by 4-c^2=0 in the exact formula.
                    gamma = (-(N - h) * pow(2 * (pow(q, h, p) - pow(q, -h, p)) % p,
                                            -1, p)) % p if h != N else 0
                    values.append((f, n * gamma * f % p))
                assert np.array_equal(recover(values), actual), (N, n)
                powercount += 1
                entries += N**4
    return dict(monomial_identities=count, actual_R_power_identities=powercount,
                original_matrix_entries=entries)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'actual_spectral_total_derivative_source_results.json'))
    args = parser.parse_args()
    result = dict(status='PASS', exact_divided_Chebyshev_identities=symbolic(),
                  original_source=original_matrices(),
                  scope='Exact original fixed-root discrete Hermite total derivative. '
                        'No uniform Fourier bound, generic-q assertion, or cycle selection.')
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
