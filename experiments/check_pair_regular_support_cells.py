#!/usr/bin/env python3
"""Check the new regular-support representation against original finite jets."""
from pathlib import Path
from fractions import Fraction as Fr
from math import factorial as integer_factorial
import hashlib
import json
import re

import mpmath as mp


def main():
    mp.mp.dps = 75
    counts = {"physical_row_values": 0, "finite_product_identity": 0,
              "original_low_source": 0, "zero_high_source": 0,
              "shifted_Fourier_sum": 0, "shared_face_jump": 0,
              "cell_contour_identity": 0, "block_contour_identity": 0,
              "projected_original_trace": 0,
              "double_pole_interpolation_split": 0,
              "restored_original_normal_rows": 0,
              "Cauchy_projector_and_diagonal": 0,
              "kernel_antiderivative": 0,
              "constant_input_projection": 0,
              "source_summation_by_parts": 0,
              "polynomial_vanishing_moments": 0,
              "termwise_rate_comparisons": 0}
    error_max = mp.mpf(0)

    def check(left, right, kind):
        nonlocal error_max
        err = abs(left-right)/max(1, abs(left), abs(right))
        error_max = max(error_max, err)
        assert err < mp.mpf("1e-55"), (kind, err, left, right)
        counts[kind] += 1

    for N in (4, 6, 8, 10):
        m, theta, eta = N//2, mp.pi/N, (-1)**(N-1)
        nodes = [2*mp.cos((2*a+1)*theta) for a in range(m)]
        repeated_nodes = [2*mp.cos((2*a+1)*theta) for a in range(N)]
        inv_Qprime = [
            1/mp.fprod(c-d for b, d in enumerate(nodes) if b != a)
            for a, c in enumerate(nodes)]
        factorial = [mp.mpf(1)]
        for j in range(1, N):
            factorial.append(factorial[-1]*2*mp.sin(j*theta))

        def ej(j, z):
            return mp.fprod(repeated_nodes[b]-z for b in range(j))/factorial[j]**2

        def low(z):
            return mp.fsum(ej(j, z)*ej(j, -2) for j in range(m))

        def row(a, x):
            return (mp.mpf(2)**(N-1)/N
                    *mp.fprod(mp.sin(mp.pi*(x+mp.mpf(r)/N))
                              for r in range(1, N-a))
                    *mp.fprod(mp.sin(mp.pi*(x+mp.mpf(r)/N))
                              for r in range(1, a+1)))

        def primitive(a, x):
            if a == m:
                return mp.mpf(0)
            return ((-1)**a*row(a, x)*mp.sin(a*theta-mp.pi*x)
                    *mp.cos(a*theta)/mp.cos(mp.pi*x+theta))

        derivative_matrix = [
            [(mp.fsum(1/(c-nodes[k]) for k in range(m) if k != a)
              if a == b else
              inv_Qprime[b]/(inv_Qprime[a]*(c-nodes[b])))
             for b in range(m)] for a, c in enumerate(nodes)]

        def cardinal(x, j):
            v = x-mp.mpf(j)/N
            return mp.sin(mp.pi*N*v)/(N*mp.sin(mp.pi*v))

        def ordinary_row(x, z, left=0):
            return mp.fsum(
                row(a, x)*inv_Qprime[a]
                *mp.fprod(z-nodes[b] for b in range(m) if b != a)
                for a in range(left, m))

        for a in range(m):
            for j in range(N):
                wanted = ej(j, nodes[a]) if j < m else mp.mpf(0)
                check(row(a, mp.mpf(j)/N), wanted, "physical_row_values")
            for x in (mp.mpc(".137", ".09"), mp.mpc(".374", "-.04")):
                quotient = (mp.sin(mp.pi*N*x)/(N*mp.sin(mp.pi*x))
                            *mp.fprod(
                                mp.sin(mp.pi*(x+mp.mpf(r)/N))
                                /mp.sin(mp.pi*(mp.mpf(r)/N-x))
                                for r in range(1, a+1)))
                check(row(a, x), quotient, "finite_product_identity")
                check(primitive(a, x)-primitive(a+1, x),
                      (-1)**a*mp.sin((2*a+1)*theta)*row(a, x),
                      "kernel_antiderivative")
                check(mp.fsum(inv_Qprime[b]*row(b, x)
                              for b in range(a, m)),
                      2*primitive(a, x)/N,
                      "constant_input_projection")

        for j in range(m):
            for degree in range(m-j-1):
                check(mp.fsum(nodes[a]**degree*inv_Qprime[a]
                              *row(a, mp.mpf(j)/N) for a in range(j, m)),
                      0, "polynomial_vanishing_moments")

        sources = {}
        original = {}
        for n in (3, 4):
            carrier = mp.exp(mp.pi*1j*n*(N-1)**2/(4*N))

            def h(z):
                return mp.exp(1j*n*N*mp.acos(-z/2)**2/(4*mp.pi))*low(z)

            hv = [h(c) for c in nodes]
            hp = [mp.diff(h, c) for c in nodes]
            ip_values = [
                mp.fsum(derivative_matrix[a][b]*hv[b] for b in range(m))
                for a in range(m)]
            defects = []
            for a, c in enumerate(nodes):
                ip = ip_values[a]
                defects.append((hp[a]-ip)*inv_Qprime[a])
            weights = [eta*carrier*N*N*defects[a]*inv_Qprime[a]
                       for a in range(m)]
            sources[n] = weights
            original[n] = []
            for j in range(m):
                exact = eta*carrier*mp.fsum(
                    (4-c*c)*(hp[a]*ej(j, c)
                             +hv[a]*mp.diff(lambda z: ej(j, z), c))
                    -c*hv[a]*ej(j, c)
                    for a, c in enumerate(nodes))
                original[n].append(exact)
                interpolated = mp.fsum(weights[a]*row(a, mp.mpf(j)/N)
                                       for a in range(m))
                check(interpolated, exact, "original_low_source")
            for j in range(m, N):
                check(mp.fsum(weights[a]*row(a, mp.mpf(j)/N)
                              for a in range(m)), 0, "zero_high_source")

            # The projected source is evaluated with the literal original
            # Hermite trace, including all omitted-node first normals.
            for x in (mp.mpc(".137", ".09"), mp.mpc(".374", "-.04")):
                bv = [row(a, x) for a in range(m)]
                bp = [
                    mp.fsum(cardinal(x, j)*mp.diff(
                        lambda z: ej(j, z), c) for j in range(N))
                    for c in nodes]
                for left in sorted({0, m//2, m-1}):
                    pv = [bv[a] if a >= left else 0 for a in range(m)]
                    pp = [mp.fsum(derivative_matrix[a][b]*pv[b]
                                  for b in range(m)) for a in range(m)]
                    original_projected = eta*carrier*mp.fsum(
                        (4-c*c)*(hp[a]*pv[a]+hv[a]*pp[a])-c*hv[a]*pv[a]
                        for a, c in enumerate(nodes))
                    source = mp.fsum(weights[a]*bv[a] for a in range(left, m))
                    check(original_projected, source, "projected_original_trace")
                    retained_h = eta*carrier*mp.fsum(
                        (4-nodes[a]**2)*(hp[a]*bv[a]+hv[a]*bp[a])
                        -nodes[a]*hv[a]*bv[a] for a in range(left, m))
                    retained_i = eta*carrier*mp.fsum(
                        (4-nodes[a]**2)*(ip_values[a]*bv[a]+hv[a]*bp[a])
                        -nodes[a]*hv[a]*bv[a] for a in range(left, m))
                    check(retained_h-retained_i, source,
                          "double_pole_interpolation_split")

            for left in sorted({0, m//2, m-1}):
                for j in range(left, m):
                    retained = eta*carrier*mp.fsum(
                        (4-c*c)*(hp[a]*ej(j, c)
                                 +hv[a]*mp.diff(lambda z: ej(j, z), c))
                        -c*hv[a]*ej(j, c)
                        for a, c in enumerate(nodes) if a >= left)
                    correction = eta*carrier*mp.fsum(
                        (4-c*c)*hv[a]*mp.diff(lambda z: ej(j, z), c)
                        for a, c in enumerate(nodes) if a < left)
                    check(retained+correction, original[n][j],
                          "restored_original_normal_rows")

        def retained(n, j, x):
            return mp.fsum(sources[n][a]*row(a, x) for a in range(j, m))

        for n in (3, 4):
            # Exact normal-defect values with their common original scalar
            # absorbed in f; no asymptotic packet is inserted.
            f = [sources[n][a]/inv_Qprime[a] for a in range(m)]
            for left in range(m):
                x = mp.mpc('.231', '.057')
                by_parts = 2*(f[left]*primitive(left, x)+mp.fsum(
                    (f[a]-f[a-1])*primitive(a, x)
                    for a in range(left+1, m)))/N
                check(retained(n, left, x), by_parts,
                      "source_summation_by_parts")

        pair = mp.fsum(original[3][j]*original[4][j] for j in range(m))
        for shift in (mp.mpc(".017", ".03"), mp.mpc(".021", "-.07")):
            shifted_sum = mp.fsum(
                retained(3, 0, shift+mp.mpf(j)/N)
                *retained(4, 0, shift+mp.mpf(j)/N)
                for j in range(N))
            check(shifted_sum, pair, "shifted_Fourier_sum")

        for j in range(m-1):
            for height in (mp.mpf("-.06"), mp.mpf(".04")):
                x = (mp.mpf(j)+mp.mpf(".5"))/N+1j*height
                difference = (retained(3, j, x)*retained(4, j, x)
                              -retained(3, j+1, x)*retained(4, j+1, x))
                b = row(j, x)
                insertion = (sources[3][j]*b*retained(4, j+1, x)
                             +sources[4][j]*b*retained(3, j+1, x)
                             +sources[3][j]*sources[4][j]*b*b)
                check(difference, insertion, "shared_face_jump")

        if N == 4:
            # Direct Cauchy integration checks both the exterior formula
            # and the diagonal residue, using a polynomial input.
            x = mp.mpc(".137", ".09")
            center, radius = nodes[-1], mp.mpf(".3")
            for z in (mp.mpc("1.2", ".2"), center+mp.mpc(".06", ".04")):
                def cauchy_integrand(t):
                    w = center+radius*mp.exp(1j*t)
                    Qw = mp.fprod(w-c for c in nodes)
                    return (ordinary_row(x, w)/(Qw*(z-w))
                            *1j*radius*mp.exp(1j*t))
                integral = mp.quad(cauchy_integrand,
                                   [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi])
                projected = (mp.fprod(z-c for c in nodes)
                             *integral/(2j*mp.pi))
                if abs(z-center) < radius:
                    projected += ordinary_row(x, z)
                check(projected, ordinary_row(x, z, 1),
                      "Cauchy_projector_and_diagonal")

            for low, high in ((0, 0), (1, 1), (0, 1)):
                left = (mp.mpf(low)-mp.mpf(".5"))/N
                right = (mp.mpf(high)+mp.mpf(".5"))/N
                height = mp.mpf(".04")
                corners = [left-1j*height, right-1j*height,
                           right+1j*height, left+1j*height]

                def integrand(x):
                    return (mp.pi*N*mp.cot(mp.pi*N*x)
                            *retained(3, low, x)*retained(4, low, x))

                integral = mp.mpf(0)
                for a in range(4):
                    start, stop = corners[a], corners[(a+1) % 4]
                    integral += mp.quad(
                        lambda s: integrand(start+s*(stop-start))*(stop-start),
                        [0, mp.mpf(".5"), 1])
                expected = mp.fsum(original[3][j]*original[4][j]
                                   for j in range(low, high+1))
                check(integral/(2j*mp.pi), expected,
                      "cell_contour_identity" if low == high
                      else "block_contour_identity")

    root = Path(__file__).resolve().parents[1]
    saddle_record = root/"repro/results/research-internal-pair-three-mixed-packet.json"
    saddle = json.loads(saddle_record.read_text())
    assert saddle["status"] == "certified"
    interval = re.match(
        r"^\[([0-9.]+) \+/- ([0-9.e+-]+)\]",
        saddle["root"]["selected_action"])
    assert interval is not None
    action_upper = Fr(interval.group(1))+Fr(interval.group(2))
    comparisons = (
        4*(1-Fr(1,9)+Fr(1,25)-Fr(1,49))/Fr(22,7)>Fr(23,20),
        sum(Fr(6,5)**j/integer_factorial(j) for j in range(5))>3,
        Fr(3473523,10841600)>Fr(8,25),
        2*(Fr(21,20)+Fr(8,25))==Fr(137,50),
        action_upper<Fr(13,10),
        Fr(13,5)<Fr(137,50),
    )
    for comparison in comparisons:
        assert comparison
        counts["termwise_rate_comparisons"] += 1
    inputs = [
        Path(__file__).resolve(),
        root/"notes/research_pair_regular_support_cells.md",
        root/"notes/research_complete_source_pick_observation.md",
        root/"notes/research_trace_normal_defect_positive_form.md",
        root/"notes/research_physical_normal_defect_packet.md",
        root/"notes/research_positive_three_crossing_cap_seed.md",
        root/"notes/research_internal_pair_three_full_boundary_packet.md",
        saddle_record,
    ]
    result = {"status": "passed", "precision_decimal": mp.mp.dps,
              "counts": counts, "maximum_relative_error": mp.nstr(error_max, 22),
              "scope": "Original finite identities and exact constants for the proved absolute-term obstruction; no bound on the grouped global current is claimed.",
              "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in inputs}}
    output = root/"repro/results/research-pair-regular-support-cells.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "sha256"}))


if __name__ == "__main__":
    main()
