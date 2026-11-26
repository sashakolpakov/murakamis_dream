#!/usr/bin/env python3
"""Check signed continuation, logarithmic winding and convex charge gaps.

The proof is in sections 8--9 of research_positive_edge_volume_identity.md.
These finite calculations use signed Bloch--Wigner volumes and the original
periods. The charge comparisons read forty-significant-digit critical
points from the separately verified corridor record.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

import mpmath as mp

from check_positive_edge_volume_identity import (
    bloch_wigner, coordinates, original_shapes, phase, relative,
)


def read_complex(value):
    match = re.fullmatch(r"\(([^ ]+) ([+-]) ([^j]+)j\)", value)
    if not match:
        raise ValueError(value)
    return mp.mpc(match[1], ("-" if match[2] == "-" else "")+match[3])


def square_volume(a, y, reverse=False):
    x = mp.asinh(mp.tan(2*a)*mp.cos(2*y))/2
    z = 1j*mp.exp((2 if reverse else -2)*mp.mpc(x, y))
    w = (z+1)/(1-z) if reverse else (z-1)/(z+1)
    return mp.fsum(bloch_wigner(v) for v in (z, w, -1/z, -1/w))


def angle_vector(edges, real_angles, incidences):
    answer = []
    for index, (v, w) in enumerate(edges):
        sv = real_angles[v] if v >= 0 else mp.mpf(0)
        sw = real_angles[w] if w >= 0 else mp.mpf(0)
        gv, gw = incidences[index]
        answer.extend((sv/4-gw/2, gv/2+sw/4,
                       sv/4+gw/2, gv/2-sw/4))
    return answer


def angle_volume(vector):
    return mp.fsum(square_volume(vector[k], vector[k+1], (k % 4) == 2)
                   for k in range(0, len(vector), 2))


def charges(edges, magnitudes, real_angles, incidences):
    sums = [mp.mpf(0) for _ in magnitudes]
    for (v, w), (gv, gw) in zip(edges, incidences):
        if v >= 0:
            sums[v] += gv
        if w >= 0:
            sums[w] += gw
    return [(-magnitudes[v]*real_angles[v]/2-sums[v])/mp.pi
            for v in range(len(magnitudes))]


def charge_checks(record):
    rows = []
    # Both kinds of retained end, and several shared-vertex dimensions.
    selected = [record["cases"][j] for j in (0, 1, 3, 14)]
    for case in selected:
        values = [read_complex(t) for t in case["angles"]]
        magnitudes = case["magnitudes"]
        size = len(values)
        edges = [(j, j+1) for j in range(size-1)]+[(size-1, -1)]
        if case["kind"] == "corridor":
            edges.insert(0, (-1, 0))
        ss = [t.real for t in values]
        incidences = []
        for v, w in edges:
            t = values[v] if v >= 0 else mp.mpc(0)
            u = values[w] if w >= 0 else mp.mpc(0)
            incidences.append([mp.asinh(mp.tan(t/2)*mp.cos(u/2)).imag,
                               mp.asinh(mp.tan(u/2)*mp.cos(t/2)).imag])
        xx = angle_vector(edges, ss, incidences)
        initial_charges = charges(edges, magnitudes, ss, incidences)
        assert max(abs(c-1) for c in initial_charges) < mp.mpf("1e-36")
        delta = min(mp.pi/4-abs(x) for x in xx)
        kappa = delta*mp.sin(delta)**2/mp.pi
        unit_volume = angle_volume(xx)
        spare = min(mp.mpf(".4"), mp.pi/(4*max(abs(x) for x in xx))-1)
        examples = []
        for scale in (mp.mpf(".5"), mp.mpf(".8"), 1+spare/5, 1+spare/2):
            examples.append(("common_charge", [scale*s for s in ss],
                             [[scale*g for g in pair] for pair in incidences]))
        # Increase each charge by a different amount, without altering s.
        displaced = [pair.copy() for pair in incidences]
        for v in range(size):
            degree = sum(v in edge for edge in edges)
            increase = delta*(v+1)/(8*mp.pi*(size+1))
            for i, edge in enumerate(edges):
                if v in edge:
                    displaced[i][edge.index(v)] -= mp.pi*increase/degree
        examples.append(("distinct_increased_charges", ss, displaced))
        # Outside incidence variables do not change selected charge equations.
        displaced = [pair.copy() for pair in incidences]
        for i, edge in enumerate(edges):
            if -1 in edge:
                displaced[i][edge.index(-1)] += delta/5
        examples.append(("same_charges_changed_outside_incidence", ss, displaced))
        for kind, real_angles, data in examples:
            vector = angle_vector(edges, real_angles, data)
            assert all(abs(x) < mp.pi/4 for x in vector)
            cc = charges(edges, magnitudes, real_angles, data)
            volume = angle_volume(vector)
            linear = mp.pi*mp.fsum(values[v].imag*(cc[v]-1)
                                   for v in range(size))
            remainder = (unit_volume-volume)/2+linear
            quadratic = kappa*mp.fsum((x-y)**2 for x, y in zip(vector, xx))
            assert remainder >= quadratic-mp.mpf("1e-33")
            rows.append({
                "kind": case["kind"], "magnitudes": magnitudes, "comparison": kind,
                "charges": [mp.nstr(c, 30) for c in cc],
                "supporting_plane_remainder": mp.nstr(remainder, 30),
                "proved_quadratic_lower_bound": mp.nstr(quadratic, 30),
            })
    return rows


def continuation_checks(tolerance):
    points = [
        ((".25", "1.1"), (".4", "-.9")),
        ((".6", "2.0"), (".3", ".2")),
        ((".4", "-2.1"), (".2", "1.0")),
        ((".4", ".9"), (".2", "-1.0")),
    ]
    rows = []
    for pp, qq in points:
        p, q = mp.mpc(*pp), mp.mpc(*qq)
        t, u, rt, ru = coordinates(p, q)
        shapes = original_shapes(p, q)
        volume = mp.fsum(bloch_wigner(z) for z in shapes)
        predicted = 2*mp.pi*phase(p, q).real-2*(t.imag*rt.imag+u.imag*ru.imag)
        error = relative(volume, predicted)
        assert error < tolerance and any(z.imag < 0 for z in shapes)
        rows.append({"P": str(p), "Q": str(q), "signed_volume": mp.nstr(volume, 35),
                     "relative_residual": mp.nstr(error, 12)})
    # A genuine logarithmic loop about one pole of f'=sech(2P).
    center, radius, angle = 1j*mp.pi/4, mp.mpf(".2"), mp.mpf(".3")
    p, q = center+radius*mp.exp(1j*angle), mp.mpc(".12", "-.1")
    def integrand(theta, moment):
        displacement = radius*mp.exp(1j*theta)
        current = center+displacement
        return current**moment*(1j*displacement)/mp.cosh(2*current)
    partition = [angle+j*mp.pi/2 for j in range(5)]
    delta_f = mp.quad(lambda theta: integrand(theta, 0), partition)
    delta_primitive = p*delta_f-mp.quad(lambda theta: integrand(theta, 1), partition)
    delta_psi = (-2*(p+q)*delta_f+4*delta_primitive)/mp.pi
    assert relative(delta_f, mp.pi) < tolerance
    assert relative(delta_psi, 2*p-2*q-4*center) < tolerance
    t, u, rt, ru = coordinates(p, q)
    original = 2*mp.pi*phase(p, q).real-2*(t.imag*rt.imag+u.imag*ru.imag)
    continued = (2*mp.pi*(phase(p, q)+delta_psi).real
                 -2*((t+2*delta_f).imag*rt.imag+u.imag*(ru-1j*delta_f).imag))
    error = relative(original, continued)
    assert error < tolerance and abs(delta_psi.real) > mp.mpf(".1")
    return rows, {"phase_monodromy": mp.nstr(delta_psi, 40),
                  "period_monodromy": mp.nstr(delta_f, 40),
                  "paired_volume_relative_residual": mp.nstr(error, 12)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.precision
    source = Path(__file__).parents[1]/"repro/results/research-positive-corridor-completion-root.json"
    charge_rows = charge_checks(json.loads(source.read_text()))
    signed_rows, winding = continuation_checks(mp.power(10, -args.precision//2))
    result = {
        "scope": "Finite checks of the written charge comparison and signed logarithmic continuation.",
        "precision_decimal_digits": args.precision,
        "critical_input_significant_digits": 40,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "critical_input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "charge_comparisons": charge_rows,
        "signed_continuations": signed_rows, "logarithmic_loop": winding,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"charge_comparisons": len(charge_rows),
                      "signed_continuations": len(signed_rows), "logarithmic_loops": 1,
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
