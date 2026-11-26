#!/usr/bin/env python3
"""Original-quotient normalization of the radical alternating observation.

Finite comparisons check both-parity full-node and symmetric chirp formulas.
The uniform exponential estimate is proved in the linked note, not inferred
from these comparisons.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import mpmath as mp

import check_one_crossing_gaussian_window as original
import check_complete_boundary_coefficient_transport as polynomial


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path(
        "repro/results/research-radical-observation-boundary-decay.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-35))
    counts = {}
    largest = mp.mpf(0)

    def equal(label, actual, expected, context):
        nonlocal largest
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, context, mp.nstr(error, 20)))
        largest = max(largest, error)
        counts[label] = counts.get(label, 0)+1

    def evaluate(coefficients, z):
        return mp.polyval(list(reversed(coefficients)), z)

    for N in range(3, 13):
        m, D, eta = N//2, N-1, (-1)**(N-1)
        M, q, kappa, S = original.original_matrix(N)
        nodes = [2*mp.cos((2*a+1)*mp.pi/N) for a in range(N)]
        modulus = [mp.mpc(1)]
        for node in nodes:
            modulus = polynomial.mul(modulus, [-node, 1])
        basis = [[mp.mpc(1)]]
        numerator = [mp.mpc(1)]
        for j in range(1, N):
            numerator = polynomial.mul(numerator, [nodes[j-1], -1])
            basis.append(polynomial.scale(numerator, 1/S[j]**2))

        # The third spectator has unreduced degree greater than N.
        spectators = [[mp.mpc(1)], [mp.mpc(1, 2), mp.mpf(2)/7, 1],
                      [mp.mpf(1), mp.mpc(-2, 1)] + [mp.mpf(0)]*N + [1]]
        for a in range(m):
            derivative = mp.fprod(nodes[a]-nodes[b] for b in range(m) if b != a)
            angle = mp.pi-(2*a+1)*mp.pi/N
            weight = 2*(-1)**a*mp.sin(angle)/N
            if N % 2:
                weight *= 2*mp.sin(angle/2)
            equal("double-node derivative weight", 1/derivative, weight, (N, a))
        for r in range(m):
            assert S[r]**2 <= N+tolerance
            counts["sine-factorial polynomial bound"] = counts.get(
                "sine-factorial polynomial bound", 0)+1

        for n in (-3, 0, 3, 4):
            crossing_coordinates = (M**n)[:, 0]
            crossing = [mp.mpc(0)]*N
            for j in range(N):
                crossing = polynomial.add(crossing, polynomial.scale(
                    basis[j], crossing_coordinates[j]))
            carrier = mp.exp(mp.pi*mp.j*n*(N-1)**2/(4*N))
            crossing_derivative = [j*crossing[j] for j in range(1, len(crossing))]
            for a in range(m):
                angle = mp.pi-(2*a+1)*mp.pi/N
                equal("original Gaussian crossing value", evaluate(crossing, nodes[a]),
                      carrier*mp.exp(mp.j*n*N*angle**2/(4*mp.pi)), (N, n, a))
                equal("original Gaussian crossing normal", evaluate(crossing_derivative, nodes[a]),
                      evaluate(crossing, nodes[a])*mp.j*n*N*angle/(4*mp.pi*mp.sin(angle)),
                      (N, n, a))

            for spectator_index, spectator in enumerate(spectators):
                raw = polynomial.mul(polynomial.mul(crossing, basis[D-m]), spectator)
                remainder = polynomial.remainder(raw, modulus)
                direct = eta*N*N*(remainder[D] if len(remainder)>D else 0)
                if N % 2:
                    expected = carrier*mp.fsum(
                        (-1)**k*mp.cos(mp.pi*k/N)
                        *evaluate(spectator, -2*mp.cos(2*mp.pi*k/N))
                        *mp.exp(mp.j*n*N*(2*mp.pi*k/N)**2/(4*mp.pi))
                        for k in range(-m, m+1))
                    equal("odd midpoint including simple endpoint", direct, expected,
                          (N, n, spectator_index))
                else:
                    star = nodes[m-1]
                    spectator_derivative = [j*spectator[j] for j in range(1,len(spectator))]
                    def derivative_weight(a):
                        return mp.fprod(nodes[a]-nodes[b] for b in range(m) if b != a)
                    def g(a):
                        return evaluate(crossing,nodes[a])*evaluate(spectator,nodes[a])
                    gp = (evaluate(crossing_derivative,star)*evaluate(spectator,star)
                          +evaluate(crossing,star)*evaluate(spectator_derivative,star))
                    expected = (-1)**m*S[m]**2*(mp.fsum(
                        g(a)/((nodes[a]-star)*derivative_weight(a)) for a in range(m-1))
                        +(gp-g(m-1)*mp.fsum(1/(star-nodes[a]) for a in range(m-1)))
                        /derivative_weight(m-1))
                    equal("even midpoint including repeated normal", direct, expected,
                          (N, n, spectator_index))
            for r in range(m):
                def missing(z):
                    return mp.fprod(z-nodes[a] for a in range(r+1, m))

                for spectator_index, spectator in enumerate(spectators):
                    # Literal full polynomial trace: multiplication, remainder,
                    # and top ordinary coefficient, not a value-only trace.
                    raw = polynomial.mul(polynomial.mul(
                        crossing, basis[D-r]), spectator)
                    remainder = polynomial.remainder(raw, modulus)
                    direct = eta*N*N*(remainder[D] if len(remainder)>D else 0)
                    full_nodes = (-1)**r*S[r]**2*mp.fsum(
                        missing(nodes[a])*evaluate(crossing, nodes[a])
                        *evaluate(spectator, nodes[a])/
                        mp.fprod(nodes[a]-nodes[b] for b in range(m) if b != a)
                        for a in range(m))
                    equal("full-node radical observation", direct, full_nodes,
                          (N, n, r, spectator_index))
                    if N % 2:
                        grid = range(-m, m+1)
                        scalar = 2*(-1)**(r+m)*carrier*S[r]**2/N
                    else:
                        grid = range(-m, m)
                        scalar = (-1)**(r+m-1)*carrier*S[r]**2/N
                    terms = []
                    for k in grid:
                        t = 2*k*mp.pi/N if N % 2 else (2*k+1)*mp.pi/N
                        z = -2*mp.cos(t)
                        prefactor = mp.sin(t)
                        if N % 2:
                            prefactor *= mp.sin(t/2)
                        terms.append((-1)**k*prefactor*missing(z)*evaluate(spectator,z)
                                     *mp.exp(mp.j*n*N*t*t/(4*mp.pi)))
                    equal("symmetric alternating original trace", direct,
                          scalar*mp.fsum(terms), (N, n, r, spectator_index))

    # Exact budgets used after fixing h and epsilon in (4).
    comparisons = {
        "horizontal reserve": F(1,4)-F(1,16)-F(1,8),
        "vertical height decay": F(1,2)-F(1,4)-F(1,16),
        "vertical angular reserve": 1-F(1,2),
        "central modulus below three fifths squared": F(3,5)**2-F(1,2)**2-F(1,4)**2,
        "cosh majorant below six fifths": F(6,5)-(1+F(9,50)/(1-F(3,100))),
        "missing factor below three fifths": F(3,5)-(F(2,5)+F(22,7)**2/64),
    }
    assert all(margin>0 for margin in comparisons.values())
    root = Path(__file__).resolve().parents[1]
    paths = [Path(__file__).resolve(),
             root/"notes/research_radical_observation_boundary_decay.md",
             root/"notes/research_high_newton_radical_contraction.md",
             root/"notes/research_network_whole_boundary_decay.md",
             root/"experiments/check_one_crossing_gaussian_window.py",
             root/"experiments/check_complete_boundary_coefficient_transport.py"]
    record = {
        "status": "passed",
        "scope": "Both-parity original-quotient normalizations and exact contour budgets; not a numerical proof of the exponential estimate.",
        "precision_digits": args.precision,
        "levels": [3, 12], "fixed_powers": [-3, 0, 3, 4],
        "counts": counts, "total_finite_checks": sum(counts.values()),
        "largest_scaled_error": mp.nstr(largest, 24),
        "strict_rational_margins": {k: str(v) for k,v in comparisons.items()},
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in paths},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {sum(counts.values())} finite comparisons and {len(comparisons)} rational margins.")
    print(f"Largest scaled error: {mp.nstr(largest, 10)}")
    print(args.output)


if __name__ == "__main__":
    main()
