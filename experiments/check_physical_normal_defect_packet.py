#!/usr/bin/env python3
"""Check literal first normals and record the whole physical defect profile.

The asymptotic ratios are diagnostics. Uniformity over all physical rows
is established in the written contour proof, not by a finite sample.
"""
from pathlib import Path
import hashlib
import json

import mpmath as mp


def source_rows(level):
    last = (level-1)//2
    nodes = [2*mp.cos((2*a+1)*mp.pi/level) for a in range(last+1)]
    if level % 2:
        nodes[-1] = mp.mpf(-2)
    denominators = [(2*mp.sin(j*mp.pi/level))**2 for j in range(1, last+1)]
    complete = [mp.mpf(1)]
    for j in range(last):
        complete.append(complete[-1]*(nodes[j]+2)/denominators[j])
    values, normals = [], []
    for node in nodes:
        value, normal = mp.mpf(1), mp.mpf(0)
        value_terms, normal_terms = [mp.mpf(1)], [mp.mpf(0)]
        for j in range(last):
            factor = (nodes[j]-node)/denominators[j]
            normal = normal*factor-value/denominators[j]
            value *= factor
            value_terms.append(value*complete[j+1])
            normal_terms.append(normal*complete[j+1])
        values.append(mp.fsum(value_terms))
        normals.append(mp.fsum(normal_terms))
    if level % 2:
        weights = [(-1)**a*mp.sqrt(2-node) for a, node in enumerate(nodes)]
        weights[-1] = mp.mpf((-1)**last)
    else:
        weights = [2*(-1)**a*mp.sin((2*a+1)*mp.pi/level)
                   for a in range(last+1)]
    derivatives = [level/weight for weight in weights]
    differentiation = mp.matrix(last+1)
    for a in range(last+1):
        for b in range(last+1):
            if a != b:
                differentiation[a,b] = derivatives[a]/(
                    derivatives[b]*(nodes[a]-nodes[b]))
        differentiation[a,a] = mp.fsum(
            1/(nodes[a]-nodes[b]) for b in range(last+1) if b != a)
    angles = [mp.pi-(2*a+1)*mp.pi/level for a in range(last+1)]
    if level % 2:
        angles[-1] = mp.mpf(0)
    return nodes, angles, values, normals, derivatives, differentiation


def saddle_data(flow):
    saddle = mp.findroot(
        lambda z: flow*z+2j*mp.asinh(mp.tan(z/2))-mp.pi,
        mp.pi/(flow+1j))
    psi = 4*mp.catalan/mp.pi-saddle/mp.pi*mp.quad(
        lambda u: mp.asinh(mp.tan(saddle*u/2)), [0, 1])
    action = psi+1j*flow*saddle*saddle/(4*mp.pi)-1j*saddle/2
    curvature = (mp.sec(saddle/2)-1j*flow)/(2*mp.pi)
    amplitude = 1/(4*mp.sqrt(mp.cos(saddle/2)))
    return saddle, action, curvature, amplitude


def main():
    # Near the first row, exponentially large cardinal terms cancel to a
    # polynomial-sized derivative. Retain enough precision for that check
    # at the largest level, rather than treating lost digits as an identity.
    mp.mp.dps = 240
    root = Path(__file__).resolve().parents[1]
    data = {}
    errors = []
    derivative_checks = 0
    for level in (32, 33, 64, 65, 128, 129, 256, 257):
        rows = source_rows(level)
        data[level] = rows
        interpolated_normals = rows[-1]*mp.matrix(rows[2])
        for computed, literal in zip(interpolated_normals, rows[3]):
            error = abs(computed-literal)/max(1, abs(computed), abs(literal))
            errors.append(error)
            assert error < mp.mpf("1e-65"), (level, error)
            derivative_checks += 1

    diagnostics = []
    for flow in (mp.mpf(3), mp.mpf(4), mp.mpf(8)):
        saddle, action, curvature, amplitude = saddle_data(flow)
        for level, rows in data.items():
            nodes, angles, values, normals, derivatives, matrix = rows
            phase = [mp.exp(1j*flow*level*t*t/(4*mp.pi)) for t in angles]
            h_values = [u*v for u, v in zip(phase, values)]
            interpolant_normals = matrix*mp.matrix(h_values)
            defects = []
            for a, t in enumerate(angles):
                ratio = t/mp.sin(t) if t else mp.mpf(1)
                literal = phase[a]*(
                    normals[a]+1j*flow*level*ratio*values[a]/(4*mp.pi))
                defects.append((literal-interpolant_normals[a])/derivatives[a])
            prefactor = (mp.sqrt(2*mp.pi)/mp.pi*amplitude/mp.sqrt(curvature))
            if level % 2:
                prefactor *= mp.cos(saddle/2)
            else:
                prefactor *= mp.sin(saddle)/1j
            leading = [
                -(-1)**(level//2)*prefactor/(node+2*mp.cos(saddle))
                *mp.exp(level*action)/level**2 for node in nodes]
            relative = [abs(actual/expected-1)
                        for actual, expected in zip(defects, leading)]
            worst = max(range(len(relative)), key=relative.__getitem__)
            diagnostics.append({
                "level": level,
                "crossing_time": str(flow),
                "physical_rows": len(nodes),
                "worst_row": worst,
                "maximum_relative_packet_error": mp.nstr(relative[worst], 20),
                "level_times_maximum_error": mp.nstr(level*relative[worst], 20),
                "first_row_ratio": [
                    mp.nstr(mp.re(defects[0]/leading[0]), 20),
                    mp.nstr(mp.im(defects[0]/leading[0]), 20)],
                "last_row_ratio": [
                    mp.nstr(mp.re(defects[-1]/leading[-1]), 20),
                    mp.nstr(mp.im(defects[-1]/leading[-1]), 20)],
            })
    dependencies = [
        Path(__file__).resolve(),
        root/"notes/research_physical_normal_defect_packet.md",
        root/"notes/research_complete_source_pick_observation.md",
        root/"notes/research_odd_half_charge_observation.md",
    ]
    result = {
        "status": "passed",
        "precision_decimal": mp.mp.dps,
        "literal_first_normal_identities": derivative_checks,
        "maximum_relative_identity_error": mp.nstr(max(errors), 24),
        "packet_diagnostics": diagnostics,
        "scope": "Independent literal Newton normals agree with ordinary collocation. Whole-row packet ratios are diagnostics; the uniform theorem is proved analytically.",
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = root/"repro/results/research-physical-normal-defect-packet.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ("sha256", "packet_diagnostics")}))
    print(json.dumps({"largest_level_diagnostics":diagnostics[-2:]}))


if __name__ == "__main__":
    main()
