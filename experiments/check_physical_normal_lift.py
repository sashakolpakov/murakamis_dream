#!/usr/bin/env python3
"""Compare the period-increment reconstruction with original Newton matrices."""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_internal_two_crossing_chain import basis_jet
from check_all_color_path_normal_bound import coefficient_data, shifted_rows


def relative(x, y):
    return abs(x-y)/max(1, abs(x), abs(y))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for level in range(2, 13):
        theta = mp.pi/level
        eta = (-1)**(level-1)
        crossing, _, _ = original_matrices(level)
        unit = mp.matrix([1]+[0]*(level-1))
        z = mp.matrix(level)
        for j in range(level):
            z[j, j] = 2*mp.cos((2*j+1)*theta)
            if j+1 < level:
                z[j+1, j] = -4*mp.sin((j+1)*theta)**2
        coupons = [mp.eye(level), -z/2]
        for _ in range(1, 2*level-1):
            coupons.append(-z*coupons[-1]-coupons[-2])
        c0 = 2*mp.cos(theta)
        last = (level-2)//2
        angles = [mp.pi-(2*j+1)*theta for j in range(last+1)]
        jets = [basis_jet(level, -2*mp.cos(t)) for t in angles]
        endpoint, endpoint_derivative = basis_jet(level, c0)
        for power in (-3, -1, 0, 1, 3):
            mult = crossing**power
            carriers = [(v.T*mult*unit)[0] for v, _ in jets]
            for w in (mp.mpf(-2), mp.mpf("-.7"), c0):
                bw, _ = basis_jet(level, w)
                density = mult*bw
                observations = [(c*density)[level-1] for c in coupons]
                delta = [observations[k+level]-eta*observations[k]
                         for k in range(level)]
                recovered = [
                    1j*mp.fsum(delta[k]*mp.exp(1j*k*t)
                               for k in range(level))/(level**2*mp.sin(t))
                    for t in angles]
                f, r, defect = shifted_rows(level, w, last)
                q_endpoint = (endpoint_derivative.T*bw)[0]
                relation = 2*mp.chebyt(level, w/2)+2
                u = []
                for j in range(last+1):
                    if j == 0:
                        u.append(q_endpoint)
                    else:
                        cp0 = -4*theta*mp.sin(theta)
                        cpj = -4*theta*mp.sin((2*j+1)*theta)
                        u.append((cp0*f[j]*q_endpoint+r[j]
                                  +relation*defect[j])/(cpj*f[j]))
                simple = None
                maximum = mp.mpf(0)
                for j, (values, normals) in enumerate(jets):
                    direct_value = (values.T*density)[0]
                    direct_normal = (normals.T*density)[0]
                    gamma = level*angles[j]/(4*mp.pi*mp.sin(angles[j]))
                    maximum = max(
                        maximum, relative(recovered[j], direct_value),
                        relative((u[j]+1j*power*gamma)*recovered[j],
                                 direct_normal))
                if level % 2:
                    m = (level-1)//2
                    a, c, _, _ = coefficient_data(level, m-1)
                    bv, _ = basis_jet(level, -2)
                    carrier_simple = (bv.T*mult*unit)[0]
                    simple = carrier_simple*(
                        (c0+a+c-w)/a*recovered[m-1]/carriers[m-1]
                        -(c/a*recovered[m-2]/carriers[m-2] if m >= 2 else 0))
                    maximum = max(maximum,
                                  relative(simple, (bv.T*density)[0]))
                for k in range(level):
                    terms = []
                    for j, t in enumerate(angles):
                        node = -2*mp.cos(t)
                        real = (4-node**2)*u[j]-node
                        imag = level*t*mp.sin(t)/mp.pi
                        assert imag >= mp.mpf(2)/level-tolerance
                        assert imag <= level+tolerance
                        terms.append(recovered[j]*(
                            (real+1j*power*imag)*mp.cos(k*t)
                            -2*k*mp.sin(t)*mp.sin(k*t)))
                    reconstructed = eta*mp.fsum(terms)+(0 if simple is None else simple)
                    maximum = max(maximum,
                                  relative(reconstructed, observations[k]))
                if maximum >= tolerance:
                    raise ArithmeticError((level, power, w, maximum))
                records.append({
                    "N": level, "power": power, "w": mp.nstr(w, 20),
                    "double_nodes": last+1, "charges": level,
                    "odd_simple_node": bool(level % 2),
                    "maximum_relative_error": mp.nstr(maximum, 18)})
    return {"status": "passed", "precision_digits": precision,
            "source_cases": len(records),
            "charge_reconstructions": sum(r["charges"] for r in records),
            "rows": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.precision)
    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__), root/"notes/research_physical_normal_lift.md",
        root/"notes/research_all_color_path_normal_bound.md",
        root/"experiments/check_all_color_path_normal_bound.py",
        root/"experiments/check_twist_period_insertion.py",
        root/"experiments/check_internal_two_crossing_chain.py",
    ]
    result["sha256"] = {str(p.relative_to(root)):
                        hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("rows", "sha256")}, indent=2))


if __name__ == "__main__":
    main()
