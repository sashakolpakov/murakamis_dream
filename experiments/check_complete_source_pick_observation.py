#!/usr/bin/env python3
"""Check the original simple-pole observation contour and integrable majorant."""
from pathlib import Path
import hashlib
import json
from fractions import Fraction as Fr
from math import factorial

import mpmath as mp


def main():
    mp.mp.dps = 85
    root = Path(__file__).resolve().parents[1]
    maximum_error = mp.mpf(0)
    contour_checks = denominator_checks = residue_checks = reduced_trace_checks = 0

    def check(actual, expected):
        nonlocal maximum_error
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        maximum_error = max(maximum_error, error)
        assert error < mp.mpf("1e-60"), (actual, expected, error)

    for N, cut_index in ((6, 1), (8, 1), (10, 2), (12, 2)):
        m, theta = N//2, mp.pi/N
        nodes = [2*mp.cos((2*a+1)*theta) for a in range(m)]
        sigma = [2*(-1)**a*mp.sin((2*a+1)*theta) for a in range(m)]
        tau = [mp.pi-(2*a+1)*theta for a in range(m)]
        square_factorial = [mp.mpf(1)]
        for j in range(1, m):
            square_factorial.append(
                square_factorial[-1]*(2*mp.sin(j*theta))**2)

        def newton(j, z):
            return mp.fprod(nodes[a]-z for a in range(j))/square_factorial[j]

        complete_coefficients = [newton(j, -2) for j in range(m)]

        def low(z):
            return mp.fsum(newton(j, z)*complete_coefficients[j] for j in range(m))

        values = [low(x) for x in nodes]
        cut = 2*mp.pi*cut_index/N
        height = mp.mpf(3)/25
        corners = [-cut-1j*height, cut-1j*height,
                   cut+1j*height, -cut+1j*height]
        for flow in (mp.mpf(0), mp.mpf(7)/5):
            s = mp.mpf(13)/4
            original = mp.fsum(
                sigma[a]*values[a]*mp.exp(1j*flow*N*tau[a]**2/(4*mp.pi))
                /(s-nodes[a]) for a in range(m) if tau[a] < cut)

            def integrand(z):
                spectral = -2*mp.cos(z)
                return (
                    2*mp.sin(z)*mp.exp(1j*flow*N*z*z/(4*mp.pi))*low(spectral)
                    /((s-spectral)*2*(-1)**m*mp.cos(N*z/2)))

            integral = mp.mpf(0)
            for j in range(4):
                start, stop = corners[j], corners[(j+1) % 4]
                integral += mp.quad(
                    lambda u: integrand(start+u*(stop-start))*(stop-start),
                    [0, mp.mpf(1)/2, 1])
            contour = N*integral/(4*mp.pi*1j)
            check(contour, original)
            contour_checks += 1

            for is_inside, selected_height in (
                    (True, height/2), (False, 2*height)):
                selected_angle = cut/2-1j*selected_height
                s = -2*mp.cos(selected_angle)
                observed = mp.fsum(
                    sigma[a]*values[a]
                    *mp.exp(1j*flow*N*tau[a]**2/(4*mp.pi))
                    /(s-nodes[a]) for a in range(m) if tau[a] < cut)
                carrier = mp.exp(1j*flow*N*selected_angle**2/(4*mp.pi))
                h_over_Q = (carrier*low(s)
                            /(2*(-1)**m*mp.cos(N*selected_angle/2)))
                expected = observed-N*int(is_inside)*h_over_Q
                integral = mp.mpf(0)
                for j in range(4):
                    start, stop = corners[j], corners[(j+1) % 4]
                    integral += mp.quad(
                        lambda u: integrand(start+u*(stop-start))*(stop-start),
                        [0, mp.mpf(1)/2, 1])
                check(N*integral/(4*mp.pi*1j), expected)
                residue_checks += 1

            # Compare the reduced simple-pole residues with the original
            # double-node trace, including all first normals.
            def h(z):
                return (mp.exp(1j*flow*N*mp.acos(-z/2)**2/(4*mp.pi))
                        *low(z))

            h_values = [h(c) for c in nodes]
            h_normals = [mp.diff(h, c) for c in nodes]
            cardinal = [1/mp.fprod(c-d for b, d in enumerate(nodes) if b != a)
                        for a, c in enumerate(nodes)]
            defects = []
            for a, c in enumerate(nodes):
                interpolant_normal = mp.fsum(
                    (mp.fsum(1/(c-nodes[k]) for k in range(m) if k != a)
                     if a == b else cardinal[b]/(cardinal[a]*(c-nodes[b])))
                    *h_values[b] for b in range(m))
                defects.append((h_normals[a]-interpolant_normal)*cardinal[a])
            carrier = mp.exp(1j*mp.pi*flow*(N-1)**2/(4*N))
            eta = (-1)**(N-1)
            for j in range(m):
                original_trace = eta*carrier*mp.fsum(
                    (4-c*c)*(h_normals[a]*newton(j, c)
                             +h_values[a]*mp.diff(lambda z: newton(j, z), c))
                    -c*h_values[a]*newton(j, c)
                    for a, c in enumerate(nodes))
                reduced_residues = mp.fsum(
                    defects[a]/mp.fprod(nodes[a]-nodes[b]
                                        for b in range(j, m) if b != a)
                    for a in range(j, m))
                reduced_trace = (eta*carrier*N*N*(-1)**j
                                 /square_factorial[j]*reduced_residues)
                check(original_trace, reduced_trace)
                reduced_trace_checks += 1

        for s in (mp.mpf(2), mp.mpf(13)/4, mp.mpf(100)):
            for x in nodes:
                assert 1/(s-x) <= N*N/(s+1)
                denominator_checks += 1
        assert 2-nodes[0] >= 4/mp.mpf(N*N)

    majorant = mp.quad(lambda u: 1/(2*mp.cosh(u)+1), [0, 1, 4, mp.inf])
    check(majorant, mp.pi/(3*mp.sqrt(3)))
    # Exact scalar comparisons used in the half-charge contour proof.
    scalar_checks = 0
    comparisons = [
        sum(Fr(6, 5)**j/factorial(j) for j in range(5)) > 3,
        sum(Fr(2, 5)**(2*j)/factorial(2*j) for j in range(4))
        + Fr(2, 5)**8/factorial(8)/(1-Fr(2, 5)**2/90) < Fr(6, 5),
        Fr(1, 2)-Fr(22, 21)**2/24 > Fr(1, 3),
        Fr(1, 3) > Fr(3, 20),
        Fr(1, 3) < Fr(9, 16),
        Fr(3, 16)-Fr(6, 5)/12 == Fr(7, 80),
    ]
    for comparison in comparisons:
        assert comparison
        scalar_checks += 1

    # Independent original physical sums. The ratios below are finite
    # asymptotic diagnostics, not a numerical proof of Theorem 2.
    packet_records = []
    source_values = {}
    for N in (32, 34, 64, 66, 128, 130, 256, 258):
        m, theta = N//2, mp.pi/N
        nodes = [2*mp.cos((2*a+1)*theta) for a in range(m)]
        sine_factorial = [mp.mpf(1)]
        for j in range(1, N):
            sine_factorial.append(sine_factorial[-1]*2*mp.sin(j*theta))
        complete = [mp.mpf(1)]
        for j in range(1, m):
            complete.append(complete[-1]*(nodes[j-1]+2)
                            /(2*mp.sin(j*theta))**2)
        values = [
            mp.fsum(sine_factorial[a+j]
                    /(sine_factorial[a-j]*sine_factorial[j]**2)*complete[j]
                    for j in range(a+1))
            for a in range(m)]
        source_values[N] = nodes, values

    for flow in (mp.mpf(3), mp.mpf(7)/2, mp.mpf(4), mp.mpf(8)):
        saddle = mp.findroot(
            lambda z: flow*z+2j*mp.asinh(mp.tan(z/2))-mp.pi,
            mp.pi/(flow+1j))
        check(flow*saddle+2j*mp.asinh(mp.tan(saddle/2)), mp.pi)
        psi = (4*mp.catalan/mp.pi-saddle/mp.pi
               *mp.quad(lambda u: mp.asinh(mp.tan(saddle*u/2)), [0, 1]))
        action = psi+1j*flow*saddle**2/(4*mp.pi)-1j*saddle/2
        curvature = (mp.sec(saddle/2)-1j*flow)/(2*mp.pi)
        cosine = mp.cos(saddle/2)
        wire = mp.atan(cosine)/mp.pi
        wire_curvature = 2*mp.pi*(1+cosine**2)**2/cosine**3
        edge_amplitude = (mp.sqrt(2*mp.pi)
                          /(4*mp.sin(mp.pi*wire)**2*mp.sqrt(wire_curvature)))
        check(edge_amplitude, 1/(4*mp.sqrt(cosine)))
        assert 0 < saddle.real < mp.pi/3
        assert 0 < -saddle.imag < mp.log(3)/3
        assert abs(cosine) < 1
        for N, (nodes, values) in source_values.items():
            theta = mp.pi/N
            for s in (mp.mpf(3), mp.mpf(5)):
                exact = mp.fsum(
                    2*(-1)**a*mp.sin((2*a+1)*theta)*values[a]
                    *mp.exp(1j*flow*N*(mp.pi-(2*a+1)*theta)**2/(4*mp.pi))
                    /(s-nodes[a]) for a in range(N//2))
                amplitude = (mp.sqrt(2*mp.pi)/(mp.pi*1j)
                             *mp.sin(saddle)*edge_amplitude
                             /((s+2*mp.cos(saddle))*mp.sqrt(curvature)))
                leading = (-1)**(N//2)*amplitude*mp.exp(N*action)/N
                ratio = exact/leading
                assert abs(ratio-1) < mp.mpf(1)/4
                packet_records.append({
                    "N": N, "crossing_time": str(flow), "s": str(s),
                    "exact_over_leading": [mp.nstr(ratio.real, 20),
                                          mp.nstr(ratio.imag, 20)],
                    "N_times_relative_error_diagnostic":
                        mp.nstr(N*abs(ratio-1), 20),
                    "selected_action_real": mp.nstr(action.real, 20),
                })
    dependencies = [
        Path(__file__).resolve(),
        root/"notes/research_complete_source_pick_observation.md",
        root/"notes/research_trace_normal_defect_positive_form.md",
        root/"notes/research_bare_kernel_thin_rectangle.md",
        root/"notes/research_pair_free_boundary_kernel.md",
        root/"notes/research_internal_pair_complete_edge_gap.md",
        root/"notes/research_last_physical_row_riccati.md",
        root/"notes/research_even_complete_low_kernel.md",
        root/"notes/research_pair_half_charge_action_gap.md",
    ]
    result = {
        "status": "passed", "precision_decimal": mp.mp.dps,
        "original_contour_identities": contour_checks,
        "complex_color_residue_identities": residue_checks,
        "original_reduced_trace_identities": reduced_trace_checks,
        "uniform_denominator_comparisons": denominator_checks,
        "integrable_majorant_identities": 1,
        "maximum_relative_error": mp.nstr(maximum_error, 22),
        "exact_scalar_comparisons": scalar_checks,
        "finite_observation_packet_diagnostics": len(packet_records),
        "packet_records": packet_records,
        "scope": "Finite normalization and scalar checks. Packet ratios are diagnostics; all uniform asymptotics have written proofs.",
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = root/"repro/results/research-complete-source-pick-observation.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("sha256", "packet_records")}))


if __name__ == "__main__":
    main()
