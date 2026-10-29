#!/usr/bin/env python3
"""Constrained Rivin angle flow and the actual paired source metric.

The ODE checks are numerical classical diagnostics. The source/cap
checks are exact. Neither establishes the selected quantum volume.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import spence

from audit_actual_peripheral_fusion import inverse_mod
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import dual_data


def symbolic_hessian():
    a, b = sp.symbols("cot_alpha cot_beta")
    c = (1 - a * b) / (a + b)
    H = sp.Matrix([[a + c, c], [c, b + c]])
    assert sp.cancel(H.det() - 1) == 0
    re_tau, im_tau = sp.symbols("Re_tau Im_tau", real=True, nonzero=True)
    boundary = -sp.Matrix([[re_tau**2 + im_tau**2, -re_tau], [-re_tau, 1]]) / (2 * im_tau)
    assert sp.cancel(boundary.det() - sp.Rational(1, 4)) == 0
    aa, ab, bb = sp.symbols("Phi_aa Phi_ab Phi_bb", real=True)
    wedge = (ab + sp.I) * (-ab + sp.I) + aa * bb
    assert sp.expand(wedge - (aa * bb - ab**2 - 1)) == 0
    return {"tetrahedral_negative_Hessian_determinant_exactly_one": True,
            "marked_boundary_volume_Hessian_determinant_exactly_one_quarter": True,
            "boundary_Monge_Ampere_is_exactly_complex_Lagrangian_condition": True,
            "positive_first_diagonal": "sin(beta)/(sin(alpha)*sin(gamma))"}


def volume(theta):
    return float(np.imag(spence(1 - np.exp(2j * theta))).sum() / 2)


def gradient(theta):
    assert np.all(theta > 0) and np.all(theta < np.pi)
    return -np.log(2 * np.sin(theta))


def divergence(reference, theta):
    ratios = reference / theta
    return float(np.sum(ratios - 1 - np.log(ratios)))


def flow_cases(data):
    tets = data["tetrahedra"]
    edge = np.array(data["edge_angle_incidence"], dtype=np.int64)
    local = np.zeros((tets, 3 * tets), dtype=np.int64)
    for j in range(tets):
        local[j, 3 * j:3 * j + 3] = 1
    A = np.vstack((local, edge))
    target = np.r_[np.ones(tets), 2 * np.ones(data["edges"])] * np.pi
    theta_star = np.pi * np.array([a / b for a, b in data["geometric_angles_in_pi_units"]])
    assert np.max(abs(A @ theta_star - target)) < 1e-12
    kernel = sp.Matrix(A.tolist()).nullspace()
    assert len(kernel) == tets + 1
    raw = np.array(sp.Matrix.hstack(*kernel), dtype=float)
    B, _ = np.linalg.qr(raw)
    assert np.max(abs(A @ B)) < 1e-12
    assert np.linalg.norm(B.T @ gradient(theta_star)) < 1e-12
    optimum = volume(theta_star)
    records = []
    for seed in (11, 29, 47):
        rng = np.random.default_rng(seed)
        direction = B @ rng.normal(size=B.shape[1])
        negative = direction < 0
        step = np.min(-theta_star[negative] / direction[negative])
        initial = theta_star + 0.97 * step * direction
        y0 = B.T @ (initial - theta_star)

        def rhs(_, y):
            theta = theta_star + B @ y
            metric = B.T @ (B / theta[:, None]**2)
            return np.linalg.solve(metric, B.T @ gradient(theta))

        def stopped(_, y):
            theta = theta_star + B @ y
            return np.linalg.norm(B.T @ gradient(theta)) - 1e-9

        stopped.terminal = True
        stopped.direction = -1
        result = solve_ivp(rhs, (0, 600), y0, method="DOP853", rtol=2e-10, atol=2e-12,
                           max_step=2, events=stopped, dense_output=True)
        assert result.success
        times = np.linspace(0, result.t[-1], 121)
        theta = theta_star[:, None] + B @ result.sol(times)
        assert np.min(theta) > 0
        assert np.max(abs(A @ theta - target[:, None])) < 1e-11
        values = np.array([volume(x) for x in theta.T])
        distances = np.array([divergence(theta_star, x) for x in theta.T])
        assert np.min(np.diff(values)) > -2e-10
        assert np.max(np.diff(distances)) < 2e-10
        assert np.max(abs(theta[:, -1] - theta_star)) < 1e-7
        for k in (0, 7, 23, 61):
            x = theta[:, k]
            y = B.T @ (x - theta_star)
            velocity = B @ rhs(times[k], y)
            dD = -np.dot((theta_star - x) / x**2, velocity)
            expected = -np.dot(theta_star - x, gradient(x))
            assert abs(dD - expected) < 1e-8
            assert dD <= -(optimum - values[k]) + 1e-8
        records.append({
            "seed": seed, "time": float(result.t[-1]),
            "initial_minimum_angle": float(np.min(initial)),
            "trajectory_minimum_angle": float(np.min(theta)),
            "final_geometric_angle_error": float(np.max(abs(theta[:, -1] - theta_star))),
            "final_volume": float(values[-1]),
            "volume_monotone_and_Bregman_function_nonincreasing": True,
            "exact_linear_constraint_drift_below": 1e-11,
        })
    return {"name": data["name"], "isosig": data["isosig"], "tetrahedra": tets,
            "angle_constraint_rank": int(sp.Matrix(A.tolist()).rank()),
            "tangent_dimension": len(kernel), "geometric_volume": optimum,
            "numerical_regularized_flows": records}


def source_and_cap_cases(N):
    prime, generator, q = field(N)
    Q = q * q % prime
    reflection = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        reflection[N - 1 - a, a] = pow(Q, a + 1, prime)
    assert np.array_equal(mm(prime, reflection, reflection), Q * np.eye(N, dtype=np.int64) % prime)

    def gamma_power(nu):
        endpoint = sum(pow(nu, j, prime) for j in range(N)) % prime
        result = pow(nu, -N * (N - 1) // 2, prime)
        for r in range(1, N):
            ratio = (nu - pow(Q, r, prime)) * pow((1 - pow(Q, r, prime)) % prime, -1, prime) % prime
            result = result * pow(ratio, N - r, prime) % prime
        return result * pow(endpoint, -N, prime) % prime

    records = []
    for kind, x in (("generic", generator), ("complete", pow(q, N - 1, prime))):
        M = -q * x % prime
        nu = M * M % prime
        endpoint = sum(pow(nu, j, prime) for j in range(N)) % prime
        Gamma = pow(M, N - 1, prime) * pow(N * endpoint % prime, -1, prime) % prime
        assert gamma_power(nu) * gamma_power(pow(nu, -1, prime)) % prime == pow(Gamma, N, prime)
        eta = pow(pow(q, N * (1 - N) // 2, prime), 3, prime)
        dimension = eta * pow(M, N - 1, prime) * pow(endpoint, -1, prime) % prime
        assert Gamma == dimension * pow(N * eta % prime, -1, prime) % prime
        gamma = pow(N, -1, prime) if kind == "complete" else 3
        gamma_dual = Gamma * pow(gamma, -1, prime) % prime
        if kind == "complete":
            assert gamma_dual == gamma and Gamma == pow(N, -2, prime)
        B = gamma * reflection % prime
        Bd = gamma_dual * reflection % prime
        Bi, Bdi = inverse_mod(B, prime), inverse_mod(Bd, prime)
        _, _, C, pivot = dual_data(N, prime, q, x, 0)
        cap = mm(prime, Bdi.T, C.T, Bi)
        expected = C * pow(Q * Gamma % prime, -1, prime) % prime
        assert np.array_equal(cap, expected)
        cup = mm(prime, B, inverse_mod(C, prime).T, Bd.T)
        eye = np.eye(N, dtype=np.int64)
        assert np.array_equal(mm(prime, cap, cup), eye)
        assert np.array_equal(mm(prime, cup, cap), eye)
        right_cap = mm(prime, Bi.T, pivot, C, Bdi)
        right_cup = mm(prime, Bd, inverse_mod(C, prime), inverse_mod(pivot, prime), B.T)
        assert np.array_equal(mm(prime, right_cap, right_cup), eye)
        pivot_new = mm(prime, B, pivot, Bi)
        weights = np.sum(cup * right_cap, axis=1) % prime
        assert np.array_equal(weights, np.diag(pivot_new))
        # The correct reflected Gaussian is generally not a scalar times the old cap.
        row, col = next(zip(*np.nonzero(C.T)))
        scalar = int(cap[row, col]) * pow(int(C.T[row, col]), -1, prime) % prime
        assert not np.array_equal(cap, C.T * scalar % prime)
        actual_cut = None
        if N <= 4:
            actual = color_matrices(N, prime, q, x)
            local_change = np.kron(reflection, reflection) % prime
            local_inverse = inverse_mod(local_change, prime)
            positive = mm(prime, local_change, actual[0], local_inverse)
            negative = mm(prime, local_change, actual[1], local_inverse)
            operator = np.eye(N**3, dtype=np.int64)
            for position, sign in WORDS[0]:
                local = positive if sign > 0 else negative
                operator = mm(prime, operator, np.kron(local, eye) if position == 0 else np.kron(eye, local))
            tensor = operator.reshape((N,) * 6)
            closed = np.einsum('abcdbc,b,c->ad', tensor, weights, weights) % prime
            closed = closed * pow(actual[3], -sum(sign for _, sign in WORDS[0]), prime) % prime
            target = reduced_period(N, prime, *actual, WORDS[0])
            assert np.array_equal(closed, target * eye % prime)
            actual_cut = int(target)
        records.append({
            "color": kind, "norm_power_identity_and_complete_phase_checked": True,
            "gamma_pair_is_full_ADO_dimension_over_N_eta": True,
            "actual_transformed_cap_and_cup_equal_the_derived_formulas": True,
            "original_cap_without_operator_transport_is_not_a_scalar_repair": True,
            "closing_weights_recover_transformed_actual_pivot": True,
            "entire_actual_figure_eight_cut": actual_cut,
        })
    return {"level": N, "prime": prime, "records": records}


def main():
    fixture = json.loads(Path(__file__).with_name("rivin_flow_triangulations.json").read_text())
    flows = [flow_cases(data) for data in fixture["triangulations"]]
    assert abs(flows[0]["geometric_volume"] - flows[1]["geometric_volume"]) < 1e-12
    sources = [source_and_cap_cases(N) for N in range(2, 16)]
    result = {
        "scope": "A classical regularized geometric angle flow and exact paired source gluing; no selected quantum-regulator comparison.",
        "exact_local_Hessian": symbolic_hessian(),
        "classical_geometric_flow_diagnostics": flows,
        "exact_source_norm_and_actual_cap_checks": sources,
    }
    output = Path(__file__).with_name("rivin_source_flow_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "result": str(output), "classical_triangulations": len(flows),
        "classical_convergent_flow_runs": sum(len(item["numerical_regularized_flows"]) for item in flows),
        "exact_source_and_cap_cases": sum(len(item["records"]) for item in sources),
        "entire_actual_figure_eight_cuts": sum(record["entire_actual_figure_eight_cut"] is not None
                                               for item in sources for record in item["records"]),
    }), flush=True)


if __name__ == "__main__":
    main()
