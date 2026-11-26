#!/usr/bin/env python3
"""Check original phase and finite factors in negative-angle reflection.

The inequalities are proved analytically in the accompanying note.
Finite comparisons check the branches and the exact crossing normalization.
"""
from pathlib import Path
import hashlib
import json

import mpmath as mp

from audit_exact_factorial_interpolation import J, sine_factorial


def main():
    mp.mp.dps = 70
    root = Path(__file__).resolve().parents[1]
    tolerance = mp.mpf("1e-50")
    maximum = mp.mpf(0)
    counts = {"primitive_derivatives": 0, "reflection_derivatives": 0,
              "strict_phase_comparisons": 0, "finite_reflections": 0,
              "exact_density_ratios": 0}

    def check(left, right, group):
        nonlocal maximum
        error = abs(left-right)/max(1, abs(left), abs(right))
        maximum = max(maximum, error)
        assert error < tolerance, (group, left, right, error)
        counts[group] += 1

    def phase(x, t):
        return (-J(mp.mpf(".5")-x+t/(2*mp.pi))
                -J(mp.mpf(".5")-x-t/(2*mp.pi))-2*J(x))

    def finite_B(N, x, t):
        return N/(sine_factorial(N, N*(mp.mpf(".5")-x+t/(2*mp.pi))-.5)
                  *sine_factorial(N, N*(mp.mpf(".5")-x-t/(2*mp.pi))-.5)
                  *sine_factorial(N, N*x)**2)

    def kernel(N, t, u):
        first = second = mp.mpc(1)
        total = first*second
        for j in range(1, N):
            denominator = 4*mp.sin(mp.pi*j/N)**2
            c = 2*mp.cos(mp.pi*(2*j-1)/N)
            first *= (c+2*mp.cos(t))/denominator
            second *= (c+2*mp.cos(u))/denominator
            total += first*second
        return total

    for z in (mp.mpc(".23", ".17"), mp.mpc(".71", "-.38")):
        check(mp.diff(J, z), mp.log(2*mp.sin(mp.pi*z)), "primitive_derivatives")

    examples = [(".08", ".4", ".2"), (".17", "1.2", ".8"),
                (".24", "1.55", ".9"), (".08", "2.5", "1.0")]
    phase_rows = []
    for xi_text, tau_text, height_text in examples:
        xi, tau, height = map(mp.mpf, (xi_text, tau_text, height_text))
        t = tau-1j*height
        c, d = mp.re(mp.cos(t)), mp.im(mp.cos(t))

        def difference(y):
            return mp.re(phase(xi-1j*y, t)-phase(xi+1j*y, t))

        previous = mp.mpf(0)
        for y in map(mp.mpf, (".03", ".12", ".5", "2", "4")):
            R = mp.cos(2*mp.pi*xi)*mp.cosh(2*mp.pi*y)+c
            B = mp.sin(2*mp.pi*xi)*mp.sinh(2*mp.pi*y)
            derivative = mp.arg(R+1j*(d+B))+mp.arg(R+1j*(d-B))
            check(mp.diff(difference, y), derivative, "reflection_derivatives")
            value = difference(y)
            assert previous < value < tau*height/mp.pi
            assert derivative > 0
            counts["strict_phase_comparisons"] += 1
            previous = value
        phase_rows.append({
            "xi": xi_text, "tau": tau_text, "height": height_text,
            "large_height_difference": mp.nstr(previous, 30),
            "proved_limit": mp.nstr(tau*height/mp.pi, 30),
        })

    finite_rows = []
    x = mp.mpc(".18", ".07")
    t = mp.mpc("1.2", "-.8")
    reflected = -mp.re(t)+1j*mp.im(t)
    for N in (4, 5, 8, 9):
        positive = finite_B(N, x, t)
        lower = finite_B(N, mp.conj(x), t)
        negative = finite_B(N, x, reflected)
        check(negative, mp.conj(lower), "finite_reflections")
        eta = (-1)**(N-1)
        for n in (3, 5):
            for u in (mp.mpf(0), mp.mpf(".6")):
                def density(angle, wire):
                    q = mp.exp(-1j*N*angle)
                    return (wire*kernel(N, angle, u)*mp.sin(angle)
                            *mp.exp(1j*n*N*angle**2/(4*mp.pi))*q/(1-eta*q)**2)
                observed = abs(density(reflected, negative)/density(t, positive))
                predicted = abs(lower/positive)*mp.exp(
                    -n*N*mp.re(t)*(-mp.im(t))/mp.pi)
                check(observed, predicted, "exact_density_ratios")
                finite_rows.append({
                    "N": N, "power": n, "outside_angle": str(u),
                    "exact_modulus_ratio": mp.nstr(observed, 30),
                    "scope": "finite normalization check, not a uniform asymptotic",
                })

    dependencies = [
        "experiments/check_internal_pair_negative_angle_reflection.py",
        "experiments/audit_exact_factorial_interpolation.py",
        "notes/research_internal_pair_negative_angle_reflection.md",
        "notes/research_internal_pair_wire_alias_reflection.md",
    ]
    record = {
        "status": "passed", "precision_digits": mp.mp.dps,
        "counts": counts, "maximum_relative_identity_error": mp.nstr(maximum, 30),
        "phase_comparisons": phase_rows, "finite_factor_comparisons": finite_rows,
        "sha256": {filename: hashlib.sha256((root/filename).read_bytes()).hexdigest()
                   for filename in dependencies},
    }
    output = root/"repro/results/research-internal-pair-negative-angle-reflection.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "passed", "counts": counts,
                      "maximum_relative_identity_error": record["maximum_relative_identity_error"]}))


if __name__ == "__main__":
    main()
