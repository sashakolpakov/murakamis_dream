#!/usr/bin/env python3
"""Regular meridian centralizers and the original ADO determinant line.

Exact symbolic identities and direct split-field matrix powers.
The global selected knot-period reduction is not asserted.
"""

import json
from functools import cache
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import power
from audit_finite_sum_annihilator import field
from audit_intrinsic_cut_transport import modified_dimension
from audit_sewn_source_corner import root_data


def equal(left, right):
    if isinstance(left, sp.MatrixBase):
        assert (left - right).applyfunc(sp.cancel) == sp.zeros(*left.shape)
    else:
        assert sp.cancel(left - right) == 0


@cache
def power_coefficient(n, M):
    if n == 0:
        return sp.Integer(0)
    return sp.Add(*(M**(n - 1 - 2 * j) for j in range(n)))


def groups_and_frames():
    M, b, bp, r, s, ell = sp.symbols('M b bp r s ell', nonzero=True)
    kappa = M - 1 / M
    mu = sp.Matrix([[M, 1], [0, 1 / M]])

    def C(t):
        return sp.Matrix([[1 + kappa * t, t], [0, 1]])

    equal(C(b) * mu, mu * C(b))
    equal(C(b) * C(bp), C(b + bp + kappa * b * bp))
    equal(C(b) * C(-b / (1 + kappa * b)), sp.eye(2))
    # The projective centralizer has a second component at trace zero.
    exceptional = sp.Matrix([[1, 0], [-2 * sp.I, -1]])
    equal(exceptional * mu.subs(M, sp.I) * exceptional.inv(), -mu.subs(M, sp.I))
    transported = bp + b * (1 + kappa * bp)
    equal(sp.diff(transported, b) / (1 + kappa * transported), 1 / (1 + kappa * b))
    F = sp.Matrix([[r, 1 - r], [s, -kappa - s]])
    Delta = s + kappa * r
    expected = sp.Matrix([[M + s, -kappa - s], [s, 1 / M - s]])
    equal(F.inv() * mu * F, expected)
    moved = sp.Matrix([[r + b * Delta, 1 - r - b * Delta], [s, -kappa - s]])
    equal(C(b) * F, moved)
    cut_coordinate = M / (M + s)
    density = -1 / (Delta * (M + s))
    equal(Delta * sp.diff(density, r) + sp.diff(Delta, r) * density, 0)
    equal(Delta * density, sp.diff(cut_coordinate, s) / cut_coordinate)
    t = sp.symbols('t')
    parabolic_density = density.subs(M, 1)
    primitive_coefficient = -r / (s * (1 + s))
    equal(sp.diff(primitive_coefficient, r), parabolic_density)
    equal(parabolic_density.subs(r, s * t) * s, -1 / (1 + s))
    assert sp.residue(-1 / (1 + s), s, -1) == -1
    assert sp.residue(-1 / (1 + s), s, 0) == 0
    longitude = sp.Matrix([[ell, (ell - 1 / ell) / kappa], [0, 1 / ell]])
    equal(longitude * mu, mu * longitude)
    equal(ell * longitude, C((ell**2 - 1) / kappa))
    h, tau, beta = sp.symbols('h tau beta')
    longitude_section = ((ell**2 - 1) / kappa).subs({M: 1 + h, ell: 1 + tau * h + beta * h**2})
    assert sp.limit(longitude_section, h, 0) == tau
    return {"projective_regular_centralizer_and_group_law_exact": True,
            "trace_zero_extra_projective_component_retained": True,
            "invariant_group_differential_exact": True,
            "framing_quotient_and_cut_coordinate_exact": True,
            "centralizer_density_invariance_and_contraction_exact": True,
            "parabolic_form_exact_and_relative_boundary_required": True,
            "longitude_section_and_regular_cusp_value_exact": True}


def power_and_cover_adapters():
    M, b, r, s = sp.symbols('M b r s', nonzero=True)
    kappa = M - 1 / M
    mu = sp.Matrix([[M, 1], [0, 1 / M]])
    F = sp.Matrix([[r, 1 - r], [s, -kappa - s]])
    C = sp.Matrix([[1 + kappa * b, b], [0, 1]])
    mu_s = sp.Matrix([[M + s, -kappa - s], [s, 1 / M - s]])
    density = -1 / ((s + kappa * r) * (M + s))
    records = []
    for D in range(1, 9):
        u = power_coefficient(D, M)
        equal(mu**D, sp.Matrix([[M**D, u], [0, M**(-D)]]))
        assert u.subs(M, 1) == D
        assert u.subs(M, -1) == (-1)**(D - 1) * D
        kp = M**D - M**(-D)
        equal(kp, kappa * u)
        H = sp.diag(u, 1)
        equal(H.inv() * mu**D * H, mu.subs(M, M**D))
        equal(H.inv() * C * H, sp.Matrix([[1 + kp * b / u, b / u], [0, 1]]))
        Fp = F.subs({M: M**D, s: u * s}, simultaneous=True)
        equal(Fp, u * H.inv() * F)
        equal(mu_s**D, mu_s.subs({M: M**D, s: u * s}, simultaneous=True))
        pulled_density = -u / ((u * s + kp * r) * (M**D + u * s))
        equal(pulled_density, density * (M + s) / (M**D + u * s))
        records.append({"cover_degree": D, "marked_meridian_power_and_regular_value": True,
                        "centralizer_Lie_adapter_and_longitude_scale_exact": True,
                        "framing_and_cut_Jacobian_exact": True})
    return records


def spectral_residue_adapters():
    M, a, b = sp.symbols('M a b', nonzero=True)
    trace = M + 1 / M
    T = sp.Matrix([[0, -1], [1, trace]])
    equal(T**2 - trace * T + sp.eye(2), sp.zeros(2))
    equal((a * sp.eye(2) + b * T).det(), a**2 + trace * a * b + b**2)
    gram = sp.Matrix([[0, 1], [1, trace]])
    assert gram.det() == -1
    epsilon = T.subs(M, 1) - sp.eye(2)
    assert epsilon**2 == sp.zeros(2) and epsilon != sp.zeros(2)
    records = []
    for D in range(1, 11):
        u = power_coefficient(D, M)
        previous = power_coefficient(D - 1, M)
        equal(T**D, u * T - previous * sp.eye(2))
        matrix = sp.Matrix([[1, -previous], [0, u]])
        equal(matrix.det(), u)
        equal((matrix * sp.Matrix([a, b]))[1], u * b)
        equal((matrix * sp.Matrix([a, b]))[1] / u, b)
        equal((a * sp.eye(2) + b * T**D).det(),
              a**2 + (M**D + M**(-D)) * a * b + b**2)
        equal((T.subs(M, 1))**D - sp.eye(2), D * epsilon)
        records.append({"power_degree": D, "spectral_power_determinant_exact": True,
                        "spectral_norm_preserved_by_power_map": True,
                        "residue_and_dual_number_normal_direction_retained": True})
    return records


def normalization_tower():
    M = sp.symbols('M', nonzero=True)

    def eta(n):
        return sp.I**(n + 3)

    records = []
    for D in range(2, 8):
        for N in range(2, 11):
            uD = power_coefficient(D, M)
            uNcover = power_coefficient(N, M**D)
            uDN = power_coefficient(D * N, M)
            equal(uDN, uD * uNcover)
            equal(uDN, power_coefficient(N, M) * power_coefficient(D, M**N))
            assert sp.simplify(eta(D * N) / (eta(D) * eta(N)) - sp.I**((D - 1) * (N - 1))) == 0
            # Retaining eta proves the dimension identity; cancelling it
            # instead proves the paired actual-source identity strictly.
            equal(1 / (D * N * uDN), 1 / (D * uD) / (N * uNcover))
            records.append({"cover_degree": D, "level": N,
                            "original_dimension_phase_exponent_mod_four": ((D - 1) * (N - 1)) % 4,
                            "dimension_and_paired_source_composition_exact": True})
    a, b, c = sp.symbols('a b c', integer=True)
    exponent = (a - 1) * (b - 1) + (a * b - 1) * (c - 1)
    exponent -= (b - 1) * (c - 1) + (a - 1) * (b * c - 1)
    assert sp.expand(exponent) == 0
    return {"three_degree_phase_cocycle_exact": True, "whole_function_identities": records}


def original_dimension_case(N):
    p, generator, q = field(N)
    _, _, _, _, _, _, _, _, _, rho, complete_dimension = root_data(N)
    eta = N * complete_dimension % p
    samples = []
    for exponent in range(1, 50):
        M = pow(generator, exponent, p)
        if pow(M, 2 * N, p) == 1:
            continue
        mu = np.array([[M, 1], [0, pow(M, -1, p)]], dtype=np.int64)
        power_matrix = power(mu, N, p)
        x = -M * pow(q, -1, p) % p
        actual = modified_dimension(N, p, q, x)
        assert actual * int(power_matrix[0, 1]) % p == eta
        kappa = (M - pow(M, -1, p)) % p
        shifted = q * M % p
        kappap = (shifted - pow(shifted, -1, p)) % p
        up = int(power(np.array([[shifted, 1], [0, pow(shifted, -1, p)]], dtype=np.int64), N, p)[0, 1])
        u = int(power_matrix[0, 1])
        assert (up * kappap + u * kappa) % p == 0
        samples.append({"meridian_exponent": exponent,
                        "original_ADO_dimension_times_direct_matrix_power_entry": int(eta),
                        "whole_root_meridian_cocycle_exact": True})
        if len(samples) == 3:
            break
    assert len(samples) == 3
    mu1 = np.array([[1, 1], [0, 1]], dtype=np.int64)
    assert power(mu1, N, p)[0, 1] == N % p
    assert complete_dimension == eta * pow(N, -1, p) % p
    # The next orbit value has a pole: test its normal denominator jet,
    # instead of assigning a separate value to a zero denominator.
    derivative = sum((N - 1 - 2 * j) * pow(q, N - 1 - 2 * j, p) for j in range(N)) % p
    assert derivative == -2 * N * pow(rho, -1, p) % p
    return {"level": N, "prime": p, "matrix_power_samples": samples,
            "complete_whole_value_and_shifted_denominator_jet_exact": True}


def main():
    groups = groups_and_frames()
    covers = power_and_cover_adapters()
    residues = spectral_residue_adapters()
    tower = normalization_tower()
    source = [original_dimension_case(N) for N in range(2, 17)]
    result = {"scope": "Regular geometric centralizer, framing quotient and exact original peripheral normalization; no selected global quantum-period comparison.",
              "centralizer_and_framing": groups, "power_cover_adapters": covers,
              "spectral_power_and_residue_adapters": residues,
              "coherent_normalization_tower": tower, "original_ADO_dimension_checks": source,
              "full_two_variable_actual_normal_density": "Proved separately by audit_full_framing_density.py; not assumed by these peripheral identities."}
    path = Path(__file__).with_name('regular_meridian_centralizer_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"result": str(path), "symbolic_cover_adapters": len(covers),
                      "spectral_residue_adapters": len(residues),
                      "exact_normalization_tower_cases": len(tower['whole_function_identities']),
                      "actual_root_levels": len(source),
                      "direct_original_dimension_matrix_power_checks": sum(len(x['matrix_power_samples']) for x in source)}, indent=2))


if __name__ == '__main__':
    main()
