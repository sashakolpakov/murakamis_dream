#!/usr/bin/env python3
"""Check the source-preserving turn trace in the original full quotient.

The matrix calculation uses monic polynomial division in the power basis.
It does not reconstruct multiplication from values at the reduced spectrum.
Finite checks supplement, rather than replace, the all-level written proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def convolution(left, right):
    result = [mp.mpf(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return result


def polynomial_value(coefficients, z):
    return mp.polyval(list(reversed(coefficients)), z)


def derivative(coefficients):
    return [i*coefficients[i] for i in range(1, len(coefficients))]


def relative(left, right):
    if isinstance(left, mp.matrix):
        return mp.norm(left-right)/max(1, mp.norm(left), mp.norm(right))
    return abs(left-right)/max(1, abs(left), abs(right))


def original_polynomials(level):
    # P_N=2T_N(z/2)+2, computed by the monic Chebyshev recurrence.
    previous, current = [mp.mpf(2)], [mp.mpf(0), mp.mpf(1)]
    for _ in range(2, level+1):
        following = [mp.mpf(0)] + current
        for j, coefficient in enumerate(previous):
            following[j] -= coefficient
        previous, current = current, following
    relation = current[:]
    relation[0] += 2
    basis = [[mp.mpf(1)]]
    for i in range(level-1):
        center = 2*mp.cos((2*i+1)*mp.pi/level)
        scale = 4*mp.sin((i+1)*mp.pi/level)**2
        basis.append([a/scale for a in convolution(basis[-1], [center, -1])])
    return relation, basis


def remainder(polynomial, relation):
    level = len(relation)-1
    value = list(polynomial) + [mp.mpf(0)]*max(0, level-len(polynomial))
    for degree in reversed(range(level, len(value))):
        coefficient = value[degree]
        for j in range(level+1):
            value[degree-level+j] -= coefficient*relation[j]
    return value[:level]


def multiplication(polynomial, relation):
    level = len(relation)-1
    return mp.matrix([
        remainder([mp.mpf(0)]*j+list(polynomial), relation)
        for j in range(level)
    ]).T


def trace(matrix):
    return mp.fsum(matrix[j, j] for j in range(matrix.rows))


def basis_values(level, z):
    values = [mp.mpf(1)]
    for i in range(level-1):
        center = 2*mp.cos((2*i+1)*mp.pi/level)
        scale = 4*mp.sin((i+1)*mp.pi/level)**2
        values.append(values[-1]*(center-z)/scale)
    return values


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    off_node = None
    for level in range(2, 13):
        relation, basis = original_polynomials(level)
        top = level-1
        eta = (-1)**top
        raw_diagonal = [mp.mpf(0)]*(2*top+1)
        for polynomial in basis:
            for j, coefficient in enumerate(convolution(polynomial, polynomial)):
                raw_diagonal[j] += coefficient
        diagonal_matrix = multiplication(raw_diagonal, relation)
        inverse_coefficients = mp.lu_solve(
            diagonal_matrix, mp.matrix([1]+[0]*top))
        inverse_matrix = multiplication(list(inverse_coefficients), relation)
        basis_matrix = mp.matrix([
            polynomial+[mp.mpf(0)]*(level-len(polynomial))
            for polynomial in basis
        ]).T
        reversal = mp.matrix([
            [int(i+j == top) for j in range(level)]
            for i in range(level)
        ])
        turn = basis_matrix*reversal*(basis_matrix**-1)
        errors = [relative(diagonal_matrix*inverse_matrix, mp.eye(level))]
        for degree in range(level):
            monomial = [mp.mpf(0)]*degree+[mp.mpf(1)]
            multiplier = multiplication(monomial, relation)
            expected = eta*level**2 if degree == top else 0
            errors.append(relative(trace(turn*inverse_matrix*multiplier), expected))
            product = remainder(convolution(raw_diagonal, monomial), relation)
            errors.append(relative(trace(turn*multiplier), eta*level**2*product[-1]))
        newton_density = reversal*(basis_matrix**-1)*inverse_matrix*basis_matrix
        errors.append(relative(newton_density, newton_density.T))
        eigenvalues = mp.eigsy((newton_density+newton_density.T)/2,
                              eigvals_only=True)
        signature = [sum(v > 0 for v in eigenvalues),
                     sum(v < 0 for v in eigenvalues)]
        assert signature == [(level+1)//2, level//2]
        inverse_derivative = derivative(list(inverse_coefficients))
        largest_value = mp.mpf(0)
        largest_normal = mp.mpf(0)
        for j in range((top//2)+1):
            node = 2*mp.cos((2*j+1)*mp.pi/level)
            value = polynomial_value(list(inverse_coefficients), node)
            raw_value = polynomial_value(raw_diagonal, node)
            errors.append(relative(value*raw_value, 1))
            largest_value = max(largest_value, value)
            assert value > 0 and value <= 1+tolerance
            is_simple = (level % 2 == 1 and j == top//2)
            if not is_simple:
                normal = polynomial_value(inverse_derivative, node)
                raw_normal = polynomial_value(derivative(raw_diagonal), node)
                errors.append(relative(normal*raw_value+value*raw_normal, 0))
                largest_normal = max(largest_normal, normal)
                assert normal >= -tolerance
                assert normal <= level**2/4+tolerance
        node0 = 2*mp.cos(mp.pi/level)
        expected_second = (level**2-1)/(24*mp.sin(mp.pi/level)**2)
        errors.append(relative(
            polynomial_value(derivative(derivative(raw_diagonal)), node0),
            expected_second))
        angles = [mp.pi*(top-2*j)/level for j in range(level)]
        values = [polynomial_value(list(inverse_coefficients), -2*mp.cos(t))
                  for t in angles]
        normals = [2*mp.sin(t)*polynomial_value(inverse_derivative, -2*mp.cos(t))
                   for t in angles]
        fourier = [mp.fsum(values)/level]
        for frequency in range(1, level):
            sampled_value = mp.fsum(
                values[j]*mp.exp(-1j*frequency*angles[j])
                for j in range(level))/level
            sampled_normal = mp.fsum(
                normals[j]*mp.exp(-1j*frequency*angles[j])
                for j in range(level))/(1j*level)
            fourier.append((1-mp.mpf(frequency)/level)*sampled_value
                           +sampled_normal/level)
        for t in (mp.mpf("0.13"), mp.mpf("1.72"), mp.mpc(".3", ".07")):
            reconstructed = fourier[0]+2*mp.fsum(
                fourier[k]*mp.cos(k*t) for k in range(1, level))
            direct = polynomial_value(list(inverse_coefficients), -2*mp.cos(t))
            errors.append(relative(reconstructed, direct))
        if level == 5:
            t = mp.mpf(".31")
            canonical = polynomial_value(list(inverse_coefficients), -2*mp.cos(t))
            reciprocal = 1/polynomial_value(raw_diagonal, -2*mp.cos(t))
            assert abs(canonical-reciprocal) > mp.mpf("1e-6")
            off_node = {
                "N": level, "angle": str(t),
                "canonical_inverse": mp.nstr(canonical, 35),
                "literal_reciprocal": mp.nstr(reciprocal, 35),
            }
        maximum = max(errors)
        if maximum >= tolerance:
            raise ArithmeticError((level, maximum))
        rows.append({
            "N": level, "signature": signature,
            "maximum_relative_residual": mp.nstr(maximum, 35),
            "largest_physical_value": mp.nstr(largest_value, 35),
            "largest_prescribed_spectral_derivative": mp.nstr(largest_normal, 35),
            "fourier_l1": mp.nstr(abs(fourier[0])
                                +2*mp.fsum(abs(a) for a in fourier[1:]), 35),
        })
    growth = []
    rate = 4*mp.catalan/mp.pi
    for level in (24, 25, 48, 49, 96, 97):
        t = mp.mpf(0) if level % 2 else mp.pi/level
        diagonal = mp.fsum(a*a for a in basis_values(level, -2*mp.cos(t)))
        predicted = 4*level**mp.mpf("1.5")*mp.exp(-level*rate)
        growth.append({
            "N": level,
            "inverse_over_predicted": mp.nstr(1/(diagonal*predicted), 35),
        })
    return {
        "scope": "Full quotient and first-normal identities; finite diagnostics do not prove asymptotics or a geometric localization theorem.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": rows,
        "off_node_representatives": off_node,
        "central_asymptotic_diagnostics": growth,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    rendered = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
        print(f"Passed {len(result['checks'])} full-quotient levels; saved {args.output}.")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
