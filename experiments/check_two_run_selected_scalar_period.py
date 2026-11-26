#!/usr/bin/env python3
"""Check the cap-selected scalar period against the original joined source.

Uses literal even Reynolds sections and the explicit odd polynomial sections
before gcd reduction.  Tests the full tensor affine row independently of its
scalar reduction, at physical and complex auxiliary clock orbits.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_even_run_simple_spectrum_and_marked_kernel import (
    eigenvalues, jacobi, path, poly_multiply, poly_value, projectors, relative,
)
from check_even_run_cyclic_descent import polynomial_transfer
from check_odd_run_simple_spectrum_and_marked_kernel import adjugate, odd_transfer


def tensor(a, b):
    return mp.matrix([
        [a[i//b.rows, j//b.cols]*b[i % b.rows, j % b.cols]
         for j in range(a.cols*b.cols)]
        for i in range(a.rows*b.rows)])


def branch_data(k, central):
    """Track the proved labels from zero; unwrap the normalized psi logarithm."""
    if k == 1:
        return [1+central], mp.mpc(1), mp.mpc(0)
    if central == 1:
        return ([2*mp.cos(mp.pi*j/k) for j in range(k)],
                mp.mpf(1)/k, -mp.log(k))
    if abs(mp.im(central)) < mp.eps**mp.mpf(".7"):
        mus = sorted(eigenvalues(jacobi(k, central)),
                     key=lambda z: mp.re(z), reverse=True)
        psi = (1+central**2-central*mus[0])/(1-central)
        assert mp.re(psi) > 0
        return mus, psi, mp.log(psi)
    for steps in (32, 64, 128, 256, 512):
        previous = [2*mp.cos((2*j+1)*mp.pi/(2*k+1)) for j in range(k)]
        psi_previous = mp.mpc(1)
        logarithm = mp.mpc(0)
        accepted = True
        for step in range(1, steps+1):
            point = central*step/steps
            spectrum = eigenvalues(jacobi(k, point))
            ordered = min(itertools.permutations(spectrum),
                          key=lambda values: mp.fsum(
                              abs(values[j]-previous[j]) for j in range(k)))
            gap = min(abs(previous[i]-previous[j])
                      for i in range(k) for j in range(i))
            if max(abs(ordered[j]-previous[j]) for j in range(k)) >= gap/3:
                accepted = False
                break
            psi = (1+point**2-point*ordered[0])/(1-point)
            ratio = psi/psi_previous
            if abs(mp.arg(ratio)) >= mp.pi/4:
                accepted = False
                break
            logarithm += mp.log(ratio)
            previous, psi_previous = list(ordered), psi
        if accepted:
            return previous, psi_previous, logarithm
    raise AssertionError(("branch continuation not resolved", k, central))


def shifted_coefficients(level, power):
    k = (abs(power)+1)//2
    sign = 1 if power > 0 else -1
    q = mp.exp(sign*mp.pi*1j/level)
    qq = q*q
    first, last = mp.zeros(k), mp.zeros(k)
    first[0, 0] = last[k-1, k-1] = 1
    basic = [mp.eye(k), -q*path(k)-last, q*q*(mp.eye(k)-first)]
    if power % 2:
        basic = poly_multiply([mp.eye(k), -first], basic)
        assert mp.norm(basic[3]) < mp.eps**mp.mpf(".7")
        basic = basic[:3]
    full = [mp.eye(k)]
    for j in range(level):
        full = poly_multiply(full, [coefficient*qq**(j*h)
                                   for h, coefficient in enumerate(basic)])
    epsilon = (-1)**level
    result = [epsilon*full[level+h] for h in range(level+1)]
    result[level] -= epsilon*mp.eye(k)
    return result


def section_orbit(level, power, central, base, coefficients, branch_cache):
    k = (abs(power)+1)//2
    sign = 1 if power > 0 else -1
    q = mp.exp(mp.pi*1j/level)
    qq = q*q
    qs, qqs = q**sign, qq**sign
    epsilon = (-1)**level
    cap = mp.matrix([qs**(k-1-a) for a in range(k)])
    clocks = [(base*qq**j)**sign for j in range(level)]
    inside_central = central**sign
    transfers, seeds, gammas = [], [], []
    if power % 2:
        c = -qs
        psi = None
        for y in clocks:
            transfer = odd_transfer(k, qs, y)
            polynomial_projector_numerator = adjugate(
                2*mp.eye(k)+epsilon*poly_value(coefficients, y))
            cardinal = mp.fsum((y/qqs)**h for h in range(level))/level
            seeds.append(cardinal*polynomial_projector_numerator*cap)
            transfers.append(transfer)
            gammas.append(c)
        section_transfers = transfers
    else:
        key = (k, mp.nstr(inside_central, 35))
        if key not in branch_cache:
            branch_cache[key] = branch_data(k, inside_central)
        mus, psi, logarithm = branch_cache[key]
        c = qs*mp.exp(-logarithm/level)
        section_transfers = []
        for y in clocks:
            p = polynomial_transfer(k, qs, y)
            projection = projectors(
                poly_value(coefficients, y), mus, epsilon)[0]
            cardinal = mp.fsum((y/qqs)**h for h in range(level))/level
            seeds.append(cardinal*projection*cap)
            section_transfers.append(p)
            transfers.append((y-1)*p)
            gammas.append((y-1)*c)
    values = []
    for j in range(level):
        prefix = mp.eye(k)
        total = seeds[j].copy()
        for r in range(1, level):
            prefix = prefix*section_transfers[(j-r) % level]
            total += c**(-r)*prefix*seeds[(j-r) % level]
        values.append(total)
    maximum = mp.mpf(0)
    for j in range(level):
        maximum = max(maximum, relative(
            transfers[j]*values[j], gammas[j]*values[(j+1) % level]))
    if central == 1:
        maximum = max(maximum, relative(values[1], cap))
    return values, transfers, gammas, psi, maximum


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    pairs = [(2, 4), (4, 6), (-4, -6), (4, -6), (-4, 6), (4, -4),
             (4, -5), (-4, 5), (3, 4), (-3, -4), (2, 1), (-2, -1)]
    records = []
    branch_cache = {}
    for level in range(2, 8):
        crossing, _, _ = original_matrices(level)
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        kappa = q**(mp.mpf((level-1)**2)/2)
        powers = {p: crossing**p for pair in pairs for p in pair}
        coefficients = {p: shifted_coefficients(level, p) for p in powers}
        first = mp.eye(level)[:, 0]
        for a, b in pairs:
            k, ell = (abs(a)+1)//2, (abs(b)+1)//2
            signs = [1 if p > 0 else -1 for p in (a, b)]
            reset_order = int(a % 2 == 0)+int(b % 2 == 0)
            dimension = k*ell
            output = mp.zeros(1, dimension)
            output[0, dimension-1] = 1
            original = ((powers[b]*first).T*(powers[a]*first))[0]
            maximum = mp.mpf(0)
            orbit_records = []
            for central in (mp.mpc(1), mp.mpc(-1), mp.exp(mp.mpc(0, ".37"))):
                base = mp.exp(mp.log(central)/level)
                left = section_orbit(
                    level, a, central, base, coefficients[a], branch_cache)
                right = section_orbit(
                    level, b, central, base, coefficients[b], branch_cache)
                av, at, ag, apsi, ae = left
                bv, bt, bg, bpsi, be = right
                section = [tensor(x, y) for x, y in zip(av, bv)]
                matrices = [tensor(x, y) for x, y in zip(at, bt)]
                tau = [x*y for x, y in zip(ag, bg)]
                phi = [(output*vector)[0] for vector in section]
                selected_period = mp.mpc(1)
                for power, sign, psi in ((a, signs[0], apsi), (b, signs[1], bpsi)):
                    if power % 2 == 0:
                        selected_period *= (1-central**sign)/psi
                denominator = 1-selected_period
                assert abs(denominator) > tolerance
                orbit_error = max(ae, be, relative(mp.fprod(tau), selected_period))
                marked_values, green_values = [], []
                full_denominators = []
                for start in range(level):
                    prefix = mp.eye(dimension)
                    accumulator = mp.zeros(1, dimension)
                    scalar_prefix = mp.mpc(1)
                    scalar_sum = mp.mpc(0)
                    for count in range(level):
                        j = (start+count) % level
                        prefix = matrices[j]*prefix
                        accumulator += output*prefix
                        scalar_prefix *= tau[j]
                        scalar_sum += scalar_prefix*phi[(j+1) % level]
                    inv_matrix = mp.eye(dimension)-prefix
                    full_denominators.append(mp.det(inv_matrix))
                    affine = accumulator*inv_matrix**-1
                    marked = (affine*section[start])[0]
                    green = scalar_sum/denominator
                    marked_values.append(marked)
                    green_values.append(green)
                    orbit_error = max(
                        orbit_error, relative(marked, green),
                        relative(prefix*section[start],
                                 selected_period*section[start]),
                        relative((accumulator*section[start])[0], scalar_sum))
                for start in range(level):
                    following = (start+1) % level
                    orbit_error = max(orbit_error, relative(
                        marked_values[start]-tau[start]*marked_values[following],
                        tau[start]*phi[following]))
                if central == 1:
                    reconstructed = kappa**(a+b)*(1+marked_values[1])
                    orbit_error = max(orbit_error, relative(reconstructed, original))
                    # Compute the leading reset jet directly from tensor matrices,
                    # not by differentiating the scalar Green quotient.
                    reset_factors = []
                    rho = (-1)**(2-reset_order)*q**sum(signs)
                    for power, sign, channels in ((a, signs[0], k),
                                                   (b, signs[1], ell)):
                        if power % 2 == 0:
                            reset_factors.append(
                                sign*polynomial_transfer(channels, q**sign, 1))
                            rho *= sign*mp.power(channels, mp.mpf(1)/level)
                        else:
                            reset_factors.append(odd_transfer(channels, q**sign, 1))
                    prefix_jet = tensor(*reset_factors)
                    row_jet = output*prefix_jet
                    for j in range(1, level):
                        prefix_jet = matrices[j]*prefix_jet
                        row_jet += output*prefix_jet
                    scalar_jet = (row_jet*section[0])[0]
                    orbit_error = max(
                        orbit_error,
                        relative(scalar_jet, rho*original/kappa**(a+b)),
                        relative(tensor(*reset_factors)*section[0],
                                 rho*section[1]))
                assert orbit_error < tolerance, (
                    level, a, b, central, orbit_error)
                maximum = max(maximum, orbit_error)
                orbit_records.append({
                    "central_X": [mp.nstr(mp.re(central), 22),
                                  mp.nstr(mp.im(central), 22)],
                    "selected_denominator":
                        [mp.nstr(mp.re(denominator), 24),
                         mp.nstr(mp.im(denominator), 24)],
                    "minimum_full_tensor_denominator_modulus":
                        mp.nstr(min(abs(x) for x in full_denominators), 24),
                    "maximum_relative_error": mp.nstr(orbit_error, 24),
                })
            records.append({
                "N": level, "powers": [a, b], "tensor_dimension": dimension,
                "reset_order": reset_order, "complete_cyclic_orbits": len(orbit_records),
                "maximum_relative_error": mp.nstr(maximum, 24),
                "original_source":
                    [mp.nstr(mp.re(original), 24), mp.nstr(mp.im(original), 24)],
                "orbit_checks": orbit_records,
            })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = run(args.precision)
    script = Path(__file__)
    dependencies = (
        "check_twist_period_insertion.py",
        "check_internal_vertex_asymptotic.py",
        "check_even_run_simple_spectrum_and_marked_kernel.py",
        "check_even_run_cyclic_descent.py",
        "check_odd_run_simple_spectrum_and_marked_kernel.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Original signed joined sources, literal tensor affine "
                 "periods versus their cap-selected scalar Green formula, "
                 "and complete first/second reset coefficients. Holomorphic "
                 "removability and growth are not inferred from these samples.",
        "odd_section_choice": "Explicit polynomial d(X) times the Reynolds "
                              "section, before primitive gcd division.",
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(script.with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "checks": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    maximum = max(mp.mpf(row["maximum_relative_error"]) for row in records)
    print(json.dumps({
        "status": "pass", "signed_pair_cases": len(records),
        "complete_cyclic_orbits": sum(row["complete_cyclic_orbits"] for row in records),
        "first_reset_cases": sum(row["reset_order"] == 1 for row in records),
        "second_reset_cases": sum(row["reset_order"] == 2 for row in records),
        "maximum_relative_error": mp.nstr(maximum, 16),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
