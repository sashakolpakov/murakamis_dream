#!/usr/bin/env python3
"""Odd physical Cauchy observation and full original trace normalization.

The reference traces use multiplication and polynomial division in the
original Newton quotient. No asymptotic sample is used as a proof.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_complete_boundary_coefficient_transport import (
    add, mul, scale, remainder, evaluate,
)


def derivative(poly):
    return [j*poly[j] for j in range(1, len(poly))] or [mp.mpc(0)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path,
                        default=Path("repro/results/research-odd-half-charge-observation.json"))
    args = parser.parse_args()
    mp.mp.dps = args.precision
    tolerance = mp.power(10, -args.precision+35)
    maximum = mp.mpf(0)
    counts = {}

    def check(label, observed, expected):
        nonlocal maximum
        error = abs(observed-expected)/max(1, abs(observed), abs(expected))
        maximum = max(maximum, error)
        counts[label] = counts.get(label, 0)+1
        if error >= tolerance:
            raise ArithmeticError((label, observed, expected, error))

    for N in (3, 5, 7, 9, 11):
        m, D = (N-1)//2, N-1
        q = mp.exp(mp.pi*1j/N)
        kappa = mp.exp(mp.pi*1j*D*D/(2*N))
        all_nodes = [2*mp.cos((2*a+1)*mp.pi/N) for a in range(N)]
        nodes = all_nodes[:m+1]
        tau = [mp.pi-(2*a+1)*mp.pi/N for a in range(m+1)]
        tau[-1] = mp.mpf(0)
        S = [mp.mpf(1)]
        for j in range(1, N):
            S.append(S[-1]*2*mp.sin(mp.pi*j/N))
        modulus = [mp.mpc(1)]
        for c in all_nodes:
            modulus = mul(modulus, [-c, 1])
        basis, numerator = [[mp.mpc(1)]], [mp.mpc(1)]
        for j in range(1, N):
            numerator = mul(numerator, [all_nodes[j-1], -1])
            basis.append(scale(numerator, 1/S[j]**2))
        crossing = [mp.mpc(0)]
        for j in range(N):
            crossing = add(crossing, scale(basis[j], kappa*(-q)**j))
        low = [mp.mpc(0)]
        for j in range(m+1):
            low = add(low, scale(basis[j], evaluate(basis[j], -2)))
        low_derivative = derivative(low)

        Q = [mp.mpc(1)]
        for c in nodes:
            Q = mul(Q, [-c, 1])
        Q_derivative = derivative(Q)
        weights = [N/evaluate(Q_derivative, c) for c in nodes]
        check("simple endpoint weight", weights[-1], (-1)**m)
        check("middle sine factorial", S[m]**2, N)
        for a, c in enumerate(nodes[:-1]):
            check("double-node derivative weight",
                  (4-c*c)*evaluate(Q_derivative, c)**2, N*N*(c+2))
            check("ordinary-node weight magnitude", abs(weights[a])**2, 2-c)
        for z in (mp.mpc(".4", "-.2"), mp.mpc("1.1", ".15")):
            check("entire sine polynomial",
                  evaluate(Q, -2*mp.cos(z)),
                  4*(-1)**m*mp.sin(z/2)*mp.sin(N*z/2))

        lagrange = []
        for a, c in enumerate(nodes):
            ell = [mp.mpc(1)]
            for b, other in enumerate(nodes):
                if b != a:
                    ell = mul(ell, [-other, 1])
            lagrange.append(scale(ell, 1/evaluate(Q_derivative, c)))

        def product(first, second):
            return remainder(mul(first, second), modulus)

        def crossing_power(n):
            answer = [mp.mpc(1)]
            factor = crossing if n >= 0 else [mp.conj(z) for z in crossing]
            for _ in range(abs(n)):
                answer = product(answer, factor)
            return answer

        for n in (-3, 0, 3):
            carrier = mp.exp(mp.pi*1j*n*D*D/(4*N))
            h_values = [mp.exp(1j*n*N*t*t/(4*mp.pi))*evaluate(low, c)
                        for t, c in zip(tau, nodes)]
            interpolant = [mp.mpc(0)]
            for value, ell in zip(h_values, lagrange):
                interpolant = add(interpolant, scale(ell, value))
            interp_derivative = derivative(interpolant)
            source = product(crossing_power(n), low)
            source_derivative = derivative(source)
            defects = []
            for a, c in enumerate(nodes):
                check("original quotient physical value",
                      evaluate(source, c), carrier*h_values[a])
                if a < m:
                    factor = mp.exp(1j*n*N*tau[a]**2/(4*mp.pi))
                    hprime = factor*(
                        evaluate(low_derivative, c)
                        +1j*n*N*tau[a]*evaluate(low, c)/(4*mp.pi*mp.sin(tau[a])))
                    check("original quotient first normal",
                          evaluate(source_derivative, c), carrier*hprime)
                    defects.append(hprime-evaluate(interp_derivative, c))
            for j in range(m+1):
                original = N*N*product(source, basis[j])[D]
                normal = mp.fsum((4-c*c)*defects[a]*evaluate(basis[j], c)
                                 for a, c in enumerate(nodes[:-1]))
                top = N*N*interpolant[-1]*basis[j][-1] if j == m else 0
                check("full odd normal-defect trace",
                      original, carrier*(normal+top))
            original_top = N*N*product(source, basis[m])[D]
            check("top trace from ordinary Cauchy observation",
                  original_top, carrier*(-1)**m*mp.fsum(
                      weights[a]*h_values[a] for a in range(m+1)))
            for w in (mp.mpf("3.25"), -2*mp.cos(mp.mpc(".4", "-.25"))):
                observation = mp.fsum(weights[a]*h_values[a]/(w-nodes[a])
                                      for a in range(m+1))
                check("full-node interpolation observation",
                      observation, N*evaluate(interpolant, w)/evaluate(Q, w))

        if N > 7:
            continue
        flow = mp.mpf(7)/5
        cut = (2*((N-1)//4)+1)*mp.pi/N
        height = mp.mpf(3)/25
        corners = [-cut-1j*height, cut-1j*height,
                   cut+1j*height, -cut+1j*height]

        def angular_h(z):
            return mp.exp(1j*flow*N*z*z/(4*mp.pi))*evaluate(low, -2*mp.cos(z))

        for w, inside in ((mp.mpf("3.25"), False),
                          (-2*mp.cos(mp.mpc(".4", "-.25")), False),
                          (-2*mp.cos(mp.mpc(".2", "-.05")), True)):
            retained = mp.fsum(
                weights[a]*angular_h(tau[a])/(w-nodes[a])
                for a in range(m+1) if tau[a] < cut)

            def integrand(z):
                return ((-1)**m*mp.cos(z/2)*angular_h(z)
                        /((w+2*mp.cos(z))*mp.sin(N*z/2)))

            integral = mp.mpc(0)
            for j in range(4):
                start, stop = corners[j], corners[(j+1) % 4]
                integral += mp.quad(
                    lambda r: integrand(start+r*(stop-start))*(stop-start),
                    [0, mp.mpf(".5"), 1])
            observed = N*integral/(4*mp.pi*1j)
            residue = (N*angular_h(mp.acos(-w/2))/evaluate(Q, w)
                       if inside else 0)
            check("sine contour with exact evaluation residue",
                  observed, retained-residue)

    root = Path(__file__).resolve().parents[1]
    dependencies = [
        Path(__file__).resolve(),
        root/"experiments/check_complete_boundary_coefficient_transport.py",
        root/"notes/research_odd_half_charge_observation.md",
        root/"notes/research_pair_half_charge_action_gap.md",
        root/"notes/research_complete_source_pick_observation.md",
    ]
    record = {
        "status": "passed", "precision_decimal": args.precision,
        "identity_counts": counts, "total_identities": sum(counts.values()),
        "maximum_relative_error": mp.nstr(maximum, 30),
        "scope": "Exact finite normalization checks, including original quotient traces, all odd nodes, first normals, and interior/exterior evaluation residues; no asymptotic test.",
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = args.output if args.output.is_absolute() else root/args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({k: v for k, v in record.items() if k != "sha256"}, indent=2))


if __name__ == "__main__":
    main()

