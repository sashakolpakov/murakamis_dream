#!/usr/bin/env python3
"""Finite checks of the original odd scalar equation and power-three polynomial.

No sampled numerical inequality is used to certify the asymptotic lower bound.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_odd_run_simple_spectrum_and_marked_kernel import odd_transfer


def relative(a, b):
    return mp.norm(a-b)/(1+mp.norm(a)+mp.norm(b))


def multiply(a, b):
    out = [mp.mpc(0)]*(len(a)+len(b)-1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i+j] += left*right
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    scalar_records, polynomial_records = [], []
    for level in range(2, 13):
        crossing, _, _ = original_matrices(level)
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        for sign in (-1, 1):
            q = mp.exp(sign*mp.pi*1j/level)
            qq = q*q
            clocks = [qq**r for r in range(level)]
            for k in range(1, 6):
                power = sign*(2*k-1)
                column = (crossing**power)[:, 0]
                phi = [mp.mpc(0)]*level
                states = []
                state = mp.matrix([q**(k-1-a) for a in range(k)])
                for j in range(level):
                    if j:
                        state = odd_transfer(k, q, qq**j)*state
                    states.append(state/(-q)**j)
                    phi[(j+1) % level] = column[j]/(kappa**power*(-q)**j)

                def operator(values, first=False):
                    result = []
                    for r, x in enumerate(clocks):
                        previous = values[(r-1) % level]
                        if first:
                            result.append(q/x*values[r]
                                          + (1-qq/x)/q*previous)
                        else:
                            y = x/qq
                            weight = (1-y)*(1-1/y)
                            result.append((x/q+q/x)*values[r]
                                          +weight/q*previous)
                    return result

                # V_(-1)=q^-1 and V_0=1, then the exact Chebyshev recursion.
                channels = [[value/q for value in phi], phi]
                for order in range(1, k):
                    leading = operator(channels[-1])
                    channels.append([a-b for a, b in zip(leading, channels[-2])])
                reconstructed = [channels[k-a] for a in range(k)]
                residual = operator(reconstructed[0], first=True)
                second = reconstructed[1] if k > 1 else [value/q for value in phi]
                maximum = max(abs(a-b)/(1+abs(a)+abs(b))
                              for a, b in zip(residual, second))
                for j in range(level):
                    vector = mp.matrix([row[(j+1) % level]
                                        for row in reconstructed])
                    maximum = max(maximum, relative(vector, states[j]))
                cap = mp.matrix([row[1] for row in reconstructed])
                maximum = max(maximum, relative(
                    cap, mp.matrix([q**(k-1-a) for a in range(k)])))
                assert maximum < tolerance, (level, power, maximum)
                scalar_records.append({
                    "N": level, "power": power,
                    "maximum_relative_error": mp.nstr(maximum, 30)})

            # Build R literally from its ordered finite products, independently
            # of the reversed-coefficient recurrence.
            r_poly = [mp.mpc(0)]*(2*level)
            for j in range(level):
                tail = [mp.mpc(1)]
                for m in range(j+1, level):
                    tail = multiply(tail, [1, -2*qq**m, qq**(2*m)])
                for h, value in enumerate(tail):
                    r_poly[h+1] += qq**j*value
            maximum = max(abs(z) for z in r_poly[:level])
            coefficients = r_poly[level:]
            reverse = [mp.mpc(1), mp.mpc(2)]
            for j in range(1, level-1):
                reverse.append(2*reverse[-1]-(1-qq**(-j))*reverse[-2])
            maximum = max(maximum, relative(
                mp.matrix(coefficients), mp.matrix(list(reversed(reverse)))))
            column = (crossing**(3*sign))[:, 0]
            values = []
            for j in range(level):
                x = qq**(j+1)
                value = mp.polyval(list(reversed(coefficients)), x)
                values.append(value)
                expected = kappa**(3*sign)*(-q)**j*value
                maximum = max(maximum, relative(expected, column[j]))
            norm = mp.fsum(abs(z)**2 for z in column)
            parseval = level*mp.fsum(abs(z)**2 for z in reverse)
            maximum = max(maximum, relative(norm, parseval))
            for x in (mp.mpc(".37", ".21"), mp.mpc("-.8", ".1")):
                value = mp.polyval(list(reversed(coefficients)), x)
                shifted = mp.polyval(list(reversed(coefficients)), qq*x)
                maximum = max(maximum, relative(
                    shifted, (1-x)**2*value+x*(2-x**level)))
            assert maximum < tolerance, (level, sign, maximum)
            polynomial_records.append({
                "N": level, "sign": sign,
                "degree": level-1,
                "original_reflected_source": mp.nstr(norm, 30),
                "maximum_relative_error": mp.nstr(maximum, 30)})
    return scalar_records, polynomial_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    scalar, polynomial = run(args.precision)
    script = Path(__file__)
    dependencies = (
        "check_twist_period_insertion.py",
        "check_internal_vertex_asymptotic.py",
        "check_odd_run_simple_spectrum_and_marked_kernel.py",
        "check_even_run_simple_spectrum_and_marked_kernel.py")
    result = {
        "status": "passed",
        "precision_decimal_digits": args.precision,
        "mpmath_version": mp.__version__,
        "scope": "Original full odd columns and the exact primitive power-three "
                 "polynomial. No asymptotic claim is inferred from this replay.",
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependency_sha256": {
            name: hashlib.sha256(script.with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "scalar_checks": scalar,
        "polynomial_checks": polynomial,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    maximum = max(mp.mpf(row["maximum_relative_error"])
                  for row in scalar+polynomial)
    print(json.dumps({
        "status": "passed", "scalar_cases": len(scalar),
        "polynomial_cases": len(polynomial),
        "maximum_relative_error": mp.nstr(maximum, 22),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
