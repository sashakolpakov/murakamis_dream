#!/usr/bin/env python3
"""Check signed Ward packets against the original crossing and full Hermite data.

The spectral idempotent is constructed from the characteristic polynomial,
not from the Newton coefficient or jet formulas being checked. These finite
precision comparisons supplement the written proof; they are not that proof.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_polynomial_crossing_fourier_trace import crossing_fourier
from check_twist_period_insertion import original_matrices


def multiplication(level):
    z = mp.matrix(level)
    for j in range(level):
        z[j, j] = 2 * mp.cos((2*j+1)*mp.pi/level)
        if j+1 < level:
            z[j+1, j] = -4 * mp.sin((j+1)*mp.pi/level)**2
    return z


def endpoint_projectors(level, z, full_matrix):
    identity = mp.eye(level)
    c0 = 2 * mp.cos(mp.pi/level)
    vector = identity.copy() if full_matrix else identity[:, 0]
    h0 = mp.mpf(1)
    for j in range(1, level-1):
        cj = 2 * mp.cos((2*j+1)*mp.pi/level)
        vector = (z-cj*identity)*vector
        h0 *= c0-cj
    vector /= h0
    xi = (z-c0*identity)*vector
    pi = vector-c0/(4-c0*c0)*xi
    return pi, xi


def chebyshev_matrices(z, largest):
    result = [mp.eye(z.rows)]
    if largest:
        result.append(z/2)
    while len(result) <= largest:
        result.append(z*result[-1]-result[-2])
    return result


def relative(a, b):
    return mp.norm(a-b)/max(1, mp.norm(a), mp.norm(b))


def newton_jets(level, coefficients, node):
    value = coefficients[0]
    derivative = mp.mpf(0)
    basis = mp.mpf(1)
    normal = mp.mpf(0)
    for k in range(1, level):
        cj = 2 * mp.cos((2*k-1)*mp.pi/level)
        scale = 4 * mp.sin(k*mp.pi/level)**2
        normal = ((cj-node)*normal-basis)/scale
        basis = (cj-node)*basis/scale
        value += coefficients[k]*basis
        derivative += coefficients[k]*normal
    return value, derivative


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    matrix_checks = []
    powers = (-5, -3, -2, -1, 0, 1, 2, 3, 4, 5)
    for level in range(2, 11):
        crossing, _, _ = original_matrices(level)
        z = multiplication(level)
        pi, xi = endpoint_projectors(level, z, True)
        q = mp.exp(mp.pi*1j/level)
        rho = q-1/q
        kappa = q**(mp.mpf((level-1)**2)/2)
        cheb = chebyshev_matrices(z, max(level-1, max(abs(n) for n in powers)))
        for n in powers:
            fourier, _, _, _ = crossing_fourier(level, n)
            canonical = fourier[0]*cheb[0]
            shifted = 2*fourier[0]*cheb[0]
            for k in range(1, level):
                component = 2*fourier[k]*(-1)**k*cheb[k]
                canonical += component
                shifted += 2*mp.cos(2*k*mp.pi/level)*component
            canonical /= kappa**n
            shifted /= kappa**n
            actual = crossing**n/kappa**n
            ward = shifted-(-q)**n*2*cheb[abs(n)]*actual
            parity = (-1)**n
            target = (1-parity)*pi+n*(level-1+parity*(level+1))/(2*rho)*xi
            turned = (crossing**-1*ward)[:, 0][::-1]
            turned = mp.matrix(turned)
            unit = mp.eye(level)[:, 0]
            if n % 2:
                target_turn = 2/kappa*mp.matrix(pi[:, 0][::-1])
                target_turn += (level-1-n)*(-1)**level*rho/kappa*unit
            else:
                target_turn = n*level*(-1)**level*rho/kappa*unit
            errors = {
                "canonical_matrix": relative(canonical, actual),
                "full_ward_identity": relative(ward, target),
                "original_half_crossing_and_turn": relative(turned, target_turn),
            }
            if max(errors.values()) > tolerance:
                raise ArithmeticError((level, n, errors))
            matrix_checks.append({"N": level, "power": n,
                                  "relative_errors": {k: mp.nstr(v, 30) for k, v in errors.items()}})
        print(f"Original full-matrix Ward and turn identities: N={level}.", flush=True)

    jet_checks = []
    for level in range(2, 33):
        theta = mp.pi/level
        pi, _ = endpoint_projectors(level, multiplication(level), False)
        turned = list(pi)[::-1]
        coefficients = [(-1)**level*2*mp.cos(theta)] + [
            (-1)**(level+k+1)*mp.sin(theta)/mp.sin(k*theta)
            for k in range(1, level)]
        coefficient_error = relative(mp.matrix(turned), mp.matrix(coefficients))
        worst = coefficient_error
        actual_norm = mp.mpf(0)
        for j in range((level+1)//2):
            alpha = (2*j+1)*theta
            value, derivative = newton_jets(level, turned, 2*mp.cos(alpha))
            expected_value = (-1)**level*(2*mp.cos(theta)+2*mp.sin(theta)*
                                              mp.fsum(mp.cot(r*theta) for r in range(1, j+1)))
            worst = max(worst, abs(value-expected_value)/max(1, abs(expected_value)))
            norm_here = abs(value)
            if j < level//2:
                expected_derivative = (-1)**(level+1)*mp.sin(theta)/(4*mp.sin(alpha))*\
                    mp.fsum(mp.csc(r*theta)**2 for r in range(j+1, level-j))
                worst = max(worst, abs(derivative-expected_derivative)/max(1, abs(expected_derivative)))
                norm_here += abs(derivative)
            actual_norm = max(actual_norm, norm_here)
        bound = 2+2*mp.harmonic((level-1)//2)+mp.mpf(level*level-1)/12
        if worst > tolerance or actual_norm > bound+tolerance:
            raise ArithmeticError((level, worst, actual_norm, bound))
        angles = [(2*j+1)*theta for j in range(level)]
        samples = [newton_jets(level, turned, 2*mp.cos(t)) for t in angles]
        gamma = [mp.fsum(v for v, _ in samples)/level]
        for k in range(1, level):
            values = mp.fsum(v*mp.exp(-1j*k*t) for t, (v, _) in zip(angles, samples))/level
            normals = mp.fsum(-2*mp.sin(t)*d*mp.exp(-1j*k*t)
                              for t, (_, d) in zip(angles, samples))/(1j*level)
            gamma.append(((level-k)*values+normals)/level)
        real_max = mp.mpf(0)
        reconstruction_error = mp.mpf(0)
        for j in range(17):
            t = 2*mp.pi*(mp.mpf(j)+mp.mpf('.137'))/17
            direct, _ = newton_jets(level, turned, 2*mp.cos(t))
            fourier = gamma[0]+2*mp.fsum(gamma[k]*mp.cos(k*t) for k in range(1, level))
            reconstruction_error = max(reconstruction_error, abs(direct-fourier)/max(1, abs(direct)))
            real_max = max(real_max, abs(direct))
        real_bound = level*(2+2*mp.harmonic((level-1)//2))+mp.pi*(level-1)/3
        if reconstruction_error > tolerance or real_max > real_bound+tolerance:
            raise ArithmeticError((level, reconstruction_error, real_max, real_bound))
        jet_checks.append({"N": level, "worst_relative_error": mp.nstr(worst, 30),
                           "actual_full_Hermite_norm": mp.nstr(actual_norm, 30),
                           "proved_upper_bound": mp.nstr(bound, 30),
                           "two_alias_reconstruction_relative_error": mp.nstr(reconstruction_error, 30),
                           "maximum_on_17_off_grid_real_angles": mp.nstr(real_max, 30),
                           "proved_whole_real_bound": mp.nstr(real_bound, 30)})
    print("Independent characteristic-projector coefficients and full jets: N=2,...,32.", flush=True)

    generic_checks = []
    for level in (5, 8):
        q = mp.exp(mp.pi*1j/level+mp.mpf('.013'))
        Q = q*q
        a = mp.mpc('.31', '.27')
        for j in range(level):
            node = q**(2*j+1)+q**(-2*j-1)
            total = mp.mpf(1)
            basis = mp.mpf(1)
            for k in range(1, level):
                cj = q**(2*k-1)+q**(-2*k+1)
                basis *= (cj-node)/(-(q**k-q**(-k))**2)
                total += (1-a)/(1-a*Q**k)*(-q)**k*basis
            product = mp.fprod((a-Q**r)/(1-a*Q**r) for r in range(1, j+1))
            error = abs(total-product)/max(1, abs(product))
            if error > tolerance:
                raise ArithmeticError((level, j, error))
            generic_checks.append({"N": level, "node_index": j,
                                   "relative_error": mp.nstr(error, 30)})
    return {
        "scope": "Finite precision comparisons against the original crossing and a characteristic-polynomial spectral projector. The written proof supplies the all-level statements.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matrix_checks": matrix_checks,
        "projector_coefficient_and_jet_checks": jet_checks,
        "generic_q_finite_summation_checks": generic_checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    content = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f"Saved {args.output}.")
    else:
        print(content)


if __name__ == '__main__':
    main()
