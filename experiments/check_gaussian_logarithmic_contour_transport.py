#!/usr/bin/env python3
"""Compare translated Gaussian residues with the original full crossing matrix.

The spectator is an unreduced polynomial of degree 2N+1. The two sides
are evaluated independently: original Newton matrices on one side,
explicit residues on translated logarithmic windows on the other.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp

from check_signed_gaussian_ward_endpoint_packet import multiplication, chebyshev_matrices
from check_twist_period_insertion import original_matrices


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    for level in range(2, 9):
        z = multiplication(level)
        identity = mp.eye(level)
        crossing = original_matrices(level)[0]
        eta = (-1)**(level-1)
        q = mp.exp(mp.pi*1j/level)
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        coefficients = [mp.mpc(mp.mpf((-1)**r)/(r+1), mp.mpf(1)/(r+2))
                        for r in range(2*level+2)]
        second_kind = [identity, z]
        while len(second_kind) < len(coefficients):
            second_kind.append(z*second_kind[-1]-second_kind[-2])
        second_coefficients = [mp.mpc(0)]*len(coefficients)
        for r, coefficient in enumerate(coefficients):
            for j in range(r//2+1):
                multiplicity = math.comb(r, j)-(math.comb(r, j-1) if j else 0)
                second_coefficients[r-2*j] += coefficient*multiplicity
        spectator = mp.zeros(level)
        for coefficient, basis in zip(second_coefficients, second_kind):
            spectator += coefficient*basis

        def value_normal(argument):
            value = mp.fsum(a*argument**r for r, a in enumerate(coefficients))
            normal = mp.fsum(r*coefficients[r]*argument**(r-1)
                            for r in range(1, len(coefficients)))
            return value, normal

        norm = mp.mpf(0)
        for j in range(level):
            value, normal = value_normal(2*mp.cos((2*j+1)*mp.pi/level))
            norm = max(norm, abs(value)+(abs(normal) if 2*j+1 != level else 0))

        for power in (-3, -1, 0, 1, 2, 3):
            normalized_crossing = crossing**power/kappa**power
            for steps in sorted({1, 2, level//2, level, level+1}):
                transported = mp.zeros(level)
                for j, (coefficient, basis) in enumerate(zip(second_coefficients, second_kind)):
                    transported += 2*mp.cos(2*mp.pi*steps*(j+1)/level)*coefficient*basis
                first_kind = chebyshev_matrices(z, abs(power*steps))[-1]
                multiplier = (-1)**(power*steps)*q**(power*steps*steps)
                matrix_value = (normalized_crossing*(transported-
                                2*multiplier*first_kind*spectator))[level-1, 0]
                shift = 2j*mp.pi*steps/level

                def residue(index, direction):
                    x = (2*index+1)*mp.pi*1j/level
                    moved = x+direction*shift
                    argument = 2*mp.cosh(moved)
                    differential = 2*mp.sinh(moved)
                    value, normal = value_normal(argument)
                    B = value*differential
                    derivative_B = normal*differential**2+value*argument
                    # The lift of q is fixed; do not take a principal square root of kappa.
                    gaussian = mp.exp(-mp.pi*1j*power*(level-1)**2/(4*level))
                    gaussian *= mp.exp(power*(x-mp.pi*1j)**2/(4j*mp.pi/level))
                    derivative_G = power*(x-mp.pi*1j)/(2j*mp.pi/level)*gaussian
                    return -(derivative_G*B+gaussian*derivative_B)/(level*level)

                current = eta*level*level/2*(
                    mp.fsum(residue(j, -1) for j in range(level))
                    -mp.fsum(residue(j, -1) for j in range(steps, level+steps))
                    +mp.fsum(residue(j, 1) for j in range(level))
                    -mp.fsum(residue(j, 1) for j in range(-steps, level-steps)))
                error = abs(current-matrix_value)/max(1, abs(current), abs(matrix_value))
                bound = 2*min(steps, level)*(abs(power)*(level+2*steps)+6)*norm
                if error > tolerance or abs(current) > bound+tolerance:
                    raise ArithmeticError((level, power, steps, error, current, matrix_value))
                item = {"N": level, "power": power, "lattice_steps": steps,
                        "matrix_residue_relative_error": mp.nstr(error, 30),
                        "current_modulus": mp.nstr(abs(current), 30),
                        "proved_current_bound": mp.nstr(bound, 30)}
                if steps == 1:
                    c0 = 2*mp.cos(mp.pi/level)
                    rho = 2j*mp.sin(mp.pi/level)
                    value, normal = value_normal(c0)
                    if power % 2:
                        direct = eta*(-2*rho*rho*normal+(power*rho-2*c0)*value)
                    else:
                        direct = (-1)**level*power*level*rho*value
                    endpoint_error = abs(current-direct)/max(1, abs(current), abs(direct))
                    if endpoint_error > tolerance:
                        raise ArithmeticError(("four-circle endpoint formula", level, power, endpoint_error))
                    item["one_step_endpoint_relative_error"] = mp.nstr(endpoint_error, 30)
                rows.append(item)
        print(f"Original matrix versus translated Gaussian residues: N={level}.", flush=True)
    return {"scope": "Finite-precision original-matrix/residue comparisons, retaining unreduced spectators and all first normals; the written proof supplies the all-level result.",
            "decimal_precision": precision,
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "checks": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    content = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
        print(f"Saved {args.output}.")
    else:
        print(content)


if __name__ == "__main__":
    main()
