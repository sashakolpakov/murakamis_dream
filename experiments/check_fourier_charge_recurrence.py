#!/usr/bin/env python3
"""Check a closed charge equation against the original full Newton algebra.

The recurrence coefficients are assembled as finite Laurent polynomials.
The source is computed independently by the original crossing matrix and
Chebyshev multiplication, then evaluated at free colors with first normals.
No asymptotic conclusion is tested here.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_internal_two_crossing_chain import basis_jet


def add(*terms):
    out = {}
    for term in terms:
        for k, v in term.items():
            out[k] = out.get(k, 0) + v
    return out


def scale(p, factor):
    return {k: factor*v for k, v in p.items()}


def multiply(*terms):
    out = {0: mp.mpc(1)}
    for term in terms:
        result = {}
        for k, v in out.items():
            for l, w in term.items():
                result[k+l] = result.get(k+l, 0) + v*w
        out = result
    return out


def coefficients(level):
    theta = mp.pi/level
    q = mp.exp(1j*theta)
    sine = lambda j: {1: q**j/(2*1j), -1: -q**(-j)/(2*1j)}
    cosine = {1: mp.mpf(".5"), -1: mp.mpf(".5")}
    d = multiply(sine(-1), sine(1), sine(-2), sine(2))
    a = scale(multiply(add({0: mp.cos(theta)}, cosine),
                       sine(-2), sine(2)), 4)
    half_square = {1: q**(-1), 0: mp.mpf(2), -1: q}
    b = scale(multiply(half_square, half_square,
                       sine(-3), sine(-4)), mp.mpf(".25"))
    return q, a, b, d


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    channel_rows = []
    for level in range(2, 14):
        crossing, _, _ = original_matrices(level)
        z = mp.matrix(level)
        for j in range(level):
            z[j, j] = 2*mp.cos((2*j+1)*mp.pi/level)
            if j+1 < level:
                z[j+1, j] = -4*mp.sin((j+1)*mp.pi/level)**2
        turn = mp.matrix([[int(i+j == level-1) for j in range(level)]
                          for i in range(level)])
        unit = mp.matrix([1]+[0]*(level-1))
        q, a, b, d = coefficients(level)
        extreme_error = max(abs(b[4]+q**(-9)/16),
                            abs(b[-4]+q**9/16))
        charges = sorted({0, 1, level-1, level, level+2, 2*level+1})
        max_charge = max(charges)+7
        coupons = [unit, -z*unit/2]
        for k in range(1, max_charge):
            coupons.append(-z*coupons[-1]-coupons[-2])
        for power in (-3, -2, -1, 0, 1, 2, 3):
            transform = turn*crossing**power
            packet = [transform*v for v in coupons]
            maximum = extreme_error
            cases = 0
            for w in (mp.mpf(-2), mp.mpc(".37", ".12"),
                      mp.mpc("-1.2", ".17")):
                values, normals = basis_jet(level, w)
                observed = [(values.T*v)[0] for v in packet]
                normal = [(normals.T*v)[0] for v in packet]
                for k in charges:
                    # a is the diagonal numerator before subtracting w*d.
                    da = mp.fsum(v*observed[abs(k+s)] for s, v in d.items())
                    dan = mp.fsum(v*normal[abs(k+s)] for s, v in d.items())
                    terms = [v*observed[abs(k+s)] for s, v in a.items()]
                    derivative_terms = [v*normal[abs(k+s)] for s, v in a.items()]
                    terms.append(-w*da)
                    derivative_terms.append(-da-w*dan)
                    for r, v in b.items():
                        left = k+r-power
                        right = k-r+power
                        terms.extend([
                            -q**(power-2*k)*v*observed[abs(left)],
                            -q**(power+2*k)*v*observed[abs(right)]])
                        derivative_terms.extend([
                            -q**(power-2*k)*v*normal[abs(left)],
                            -q**(power+2*k)*v*normal[abs(right)]])
                    maximum = max(
                        maximum,
                        abs(mp.fsum(terms))/max(1, mp.fsum(map(abs, terms))),
                        abs(mp.fsum(derivative_terms))/
                        max(1, mp.fsum(map(abs, derivative_terms))))
                    cases += 2
            if maximum >= tolerance:
                raise ArithmeticError((level, power, maximum))
            rows.append({"N": level, "power": power,
                         "value_and_normal_checks": cases,
                         "maximum_relative_error": mp.nstr(maximum, 18)})
            if level >= 4:
                original_power = crossing**power
                operator = original_power*z.T*crossing**(-power)
                j = level//2-1
                a_root = 2*mp.cos((2*j+1)*mp.pi/level)
                row, _ = basis_jet(level, a_root)
                endpoint, _ = basis_jet(level, 2*mp.cos(mp.pi/level))
                kappa = mp.exp(1j*mp.pi*(level-1)**2/(2*level))
                carrier_a = (row.T*original_power*unit)[0]
                e_top = mp.matrix([0]*(level-1)+[1])
                e_a = turn*row
                maximum_channel = mp.mpf(0)
                for w in (mp.mpf(-2), a_root, mp.mpc(".37", ".12")):
                    w_basis, _ = basis_jet(level, w)
                    kernel_aw = (row.T*w_basis)[0]
                    divided = mp.matrix(level, 1)
                    for r in range(j, 0, -1):
                        divided[r-1] = (
                            ((z[r, r]-w)*divided[r]-row[r])/
                            (4*mp.sin(r*mp.pi/level)**2))
                    source0 = original_power*w_basis
                    source1 = original_power*turn*divided
                    target1 = carrier_a*e_a-kappa**power*kernel_aw*e_top
                    residual1 = (operator-w*mp.eye(level))*source1-target1
                    maximum_channel = max(
                        maximum_channel,
                        mp.norm(residual1)/max(1, mp.norm(target1)),
                        abs((endpoint.T*source1)[0])/max(1, mp.norm(source1)),
                        abs((endpoint.T*source0)[0]-kappa**power),
                        mp.norm(mp.matrix([source1[r]
                            for r in range(level-1-level//2+2)]))/
                        max(1, mp.norm(source1)))
                if maximum_channel >= tolerance:
                    raise ArithmeticError(("channel", level, power, maximum_channel))
                channel_rows.append({
                    "N": level, "power": power, "free_colors": 3,
                    "maximum_relative_error": mp.nstr(maximum_channel, 18)})
    return {"status": "passed", "precision": precision,
            "cases": len(rows),
            "value_and_normal_checks": sum(r["value_and_normal_checks"] for r in rows),
            "channel_cases": len(channel_rows),
            "rows": rows, "channel_rows": channel_rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__),
        root/"notes/research_current_free_aw_crossing_transport.md",
        root/"experiments/check_twist_period_insertion.py",
        root/"experiments/check_internal_two_crossing_chain.py",
    ]
    result["sha256"] = {str(p.relative_to(root)):
                        hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("rows", "channel_rows", "sha256")}, indent=2))


if __name__ == "__main__":
    main()
