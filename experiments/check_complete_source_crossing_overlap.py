#!/usr/bin/env python3
"""Check physical-source crossing overlaps and record asymptotic diagnostics."""
from pathlib import Path
import hashlib
import json

import mpmath as mp


def physical_source(level):
    """Original Newton sum at each distinct node, with its exact zero retained."""
    last = (level - 1) // 2
    nodes = [2 * mp.cos((2*a+1)*mp.pi/level) for a in range(last+1)]
    denominators = [(2*mp.sin(j*mp.pi/level))**2 for j in range(1, last+1)]
    complete = [mp.mpf(1)]
    for j in range(last):
        complete.append(complete[-1]*(nodes[j]+2)/denominators[j])
    values = []
    for a in range(last+1):
        term = mp.mpf(1)
        terms = [term]
        for j in range(a):
            term *= (nodes[j]-nodes[a])/denominators[j]
            terms.append(term*complete[j+1])
        values.append(mp.fsum(terms))
    angles = [mp.pi-(2*a+1)*mp.pi/level for a in range(last+1)]
    return nodes, angles, values


def main():
    mp.mp.dps = 85
    root = Path(__file__).resolve().parents[1]
    errors = []
    finite_checks = 0

    def check(left, right):
        error = abs(left-right)/max(1, abs(left), abs(right))
        errors.append(error)
        assert error < mp.mpf("1e-65"), (left, right, error)

    gaussian_mass = mp.quad(lambda x: mp.exp(-x*x/(2*mp.pi)), [0, 1, 4, 10, mp.inf])
    check(gaussian_mass, mp.pi/mp.sqrt(2))
    for flow in (0, 1, 3):
        integral = mp.quad(
            lambda x: mp.exp(-(1-1j*flow/2)*x*x/(2*mp.pi)),
            [0, 1, 4, 10, mp.inf])
        check(integral/gaussian_mass, (1-1j*mp.mpf(flow)/2)**(-mp.mpf(1)/2))
    second_moment = mp.quad(
        lambda x: (x*x/(4*mp.pi))**2*mp.exp(-x*x/(2*mp.pi)),
        [0, 1, 4, 10, mp.inf])/gaussian_mass
    check(second_moment, mp.mpf(3)/16)

    for level in (6, 7, 12, 13):
        nodes, angles, values = physical_source(level)
        norm = mp.fsum(v*v for v in values)
        for flow in (1, 3):
            phases = [mp.exp(1j*flow*level*t*t/(4*mp.pi)) for t in angles]
            overlap = mp.fsum(v*v*u for v, u in zip(values, phases))/norm
            phase = overlap/abs(overlap)
            distance = mp.fsum(
                abs((u-phase)*v)**2 for u, v in zip(phases, values))/norm
            check(distance, 2-2*abs(overlap))
            check(mp.fsum(abs(u*v)**2 for u, v in zip(phases, values)), norm)
            finite_checks += 2
        for a, node in enumerate(nodes):
            square_factorial = mp.mpf(1)
            value_term = complete_term = mp.mpf(1)
            terms = [mp.mpf(1)]
            # Independent literal full Newton expression; j>a terms are zero.
            for j in range(1, level):
                previous_node = 2*mp.cos((2*j-1)*mp.pi/level)
                square_factorial *= (2*mp.sin(j*mp.pi/level))**2
                value_term *= previous_node-node
                complete_term *= previous_node+2
                terms.append(value_term*complete_term/square_factorial**2)
            check(mp.fsum(terms), values[a])
            assert values[a] > 0
            finite_checks += 1

    diagnostics = []
    target = (1-3j/2)**(-mp.mpf(1)/2)
    for level in (64, 65, 128, 129, 256, 257, 512, 513):
        _, angles, values = physical_source(level)
        weights = [v*v for v in values]
        norm = mp.fsum(weights)
        times = [level*t*t/(4*mp.pi) for t in angles]
        overlap = mp.fsum(
            w*mp.exp(3j*t) for w, t in zip(weights, times))/norm
        step_distance = mp.sqrt(mp.fsum(
            w*abs(mp.exp(1j*t/level)-1)**2
            for w, t in zip(weights, times))/norm)
        scaled_norm = norm*level**mp.mpf("2.5")*mp.exp(-8*level*mp.catalan/mp.pi)
        diagnostics.append({
            "level": level,
            "norm_prefactor": mp.nstr(scaled_norm, 18),
            "norm_prefactor_limit": mp.nstr(1/(32*mp.sqrt(2)), 18),
            "crossing_three_overlap": [mp.nstr(overlap.real, 18), mp.nstr(overlap.imag, 18)],
            "crossing_three_limit_error": mp.nstr(abs(overlap-target), 18),
            "level_times_small_step_distance": mp.nstr(level*step_distance, 18),
            "small_step_limit": mp.nstr(mp.sqrt(3)/4, 18),
        })
    dependencies = [
        Path(__file__).resolve(),
        root/"notes/research_complete_source_crossing_overlap.md",
        root/"notes/research_bare_kernel_thin_rectangle.md",
        root/"notes/research_complete_source_pick_observation.md",
    ]
    result = {
        "status": "passed", "precision_decimal": mp.mp.dps,
        "gaussian_identities": 5, "finite_source_identities": finite_checks,
        "maximum_relative_identity_error": mp.nstr(max(errors), 24),
        "scope": "Exact finite-source and Gaussian normalizations checked. Convergence entries are diagnostics; the asymptotic theorem has a written proof.",
        "diagnostics": diagnostics,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = root/"repro/results/research-complete-source-crossing-overlap.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("sha256", "diagnostics")}))
    print(json.dumps({"last_two_diagnostics": diagnostics[-2:]}))


if __name__ == "__main__":
    main()
