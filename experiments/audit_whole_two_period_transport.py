#!/usr/bin/env python3
"""Whole two-period transports, actual R coefficients and source lattice.

The operator test retains noninvertible norm-zero transport and the
finite Ward affine source. Actual mixed R entries are evaluated from
the original E matrices, independently of the transport expression.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries


def transport(Q, z, n, p):
    value = 1
    if n >= 0:
        for j in range(n):
            value = value*(1-z*pow(Q, j, p)) % p
        return value
    for j in range(1, -n+1):
        value = value*(1-z*pow(Q, -j, p)) % p
    return pow(value, -1, p)


def signed_cocycle():
    Q, z = sp.symbols("Q z", nonzero=True)
    def t(n, argument):
        if n >= 0:
            return sp.prod(1-argument*Q**j for j in range(n))
        return 1/sp.prod(1-argument*Q**(-j) for j in range(1, -n+1))
    checked = 0
    for m in range(-3, 4):
        for n in range(-3, 4):
            assert sp.cancel(t(m+n, z)-t(m, z)*t(n, Q**m*z)) == 0
            checked += 1
    return {"all_signed_integer_transport_cocycles": checked}


def actual_crossings(N, generic):
    p, generator, root = field(N)
    eta = generator if generic else pow(generator, (p-1)//(4*N), p)
    q = eta*eta % p
    if not generic:
        assert q == root
    Q = q*q % p
    entries = MixedEntries(N, p, q)
    checked = 0
    for alpha1, alpha2 in ((N-1, N-1), (N-2, 2*N-1)):
        x1, x2 = pow(q, alpha1, p), pow(q, alpha2, p)
        for sign in (1, -1):
            common = pow(eta, sign*alpha1*alpha2, p)
            for a in range(N):
                for b in range(N):
                    maximum = min(a, N-1-b) if sign > 0 else min(b, N-1-a)
                    for k in range(maximum+1):
                        n = b+k if sign > 0 else a+k
                        gaussian = transport(Q, Q, n, p)*pow(
                            transport(Q, Q, k, p)*transport(Q, Q, n-k, p) % p, -1, p) % p
                        if sign > 0:
                            phase = pow(-1, k, p)*pow(x1, -b-2*k, p)*pow(x2, -a+k, p)
                            phase *= pow(Q, a*b+(a-b)*k-k*(k+1)//2, p)
                            atom = transport(Q, Q*x1*x1*pow(Q, -a, p) % p, k, p)
                        else:
                            phase = pow(x1, b, p)*pow(x2, a-k, p)*pow(Q, -a*b, p)
                            atom = transport(Q, Q*x2*x2*pow(Q, -b, p) % p, k, p)
                        from_transport = common*phase*gaussian*atom % p
                        from_original = common*entries.direct(x1, x2, a, b, k, sign) % p
                        assert from_transport == from_original
                        checked += 1
    return {"N": N, "generic_q": generic,
            "original_mixed_R_entries_with_marked_common_Cartan": checked,
            "finite_transport_word_equals_actual_matrix": True}


def cyclic_lattice(N):
    p, _, q = field(N)
    Q = q*q % p
    D = np.diag([pow(Q, j, p) for j in range(N)]).astype(np.int64)
    tests = []
    for central in (0, 1, 2, 3):
        Z = np.zeros((N, N), dtype=np.int64)
        for j in range(N-1):
            Z[j+1, j] = 1
        Z[0, N-1] = central
        identity = np.eye(N, dtype=np.int64)
        S = (identity-Z)@D % p
        power = identity.copy()
        for _ in range(N):
            power = power@S % p
        assert np.array_equal(power, (1-central)*identity % p)
        assert np.array_equal(S@power % p, power@S % p)
        if central == 1:
            assert not np.any(power)
            assert np.any(S)
        # Actual truncated Ward polynomial, including the affine top source.
        f, fq, zp, scalar = identity.copy(), identity.copy(), identity.copy(), 1
        for j in range(1, N):
            scalar = scalar*(1-pow(Q, j, p)) % p
            zp = zp@Z % p
            f = (f+pow(scalar, -1, p)*zp) % p
            fq = (fq+pow(Q, j, p)*pow(scalar, -1, p)*zp) % p
        assert scalar == N % p
        assert np.array_equal((fq-(identity-Z)@f) % p, central*pow(N, -1, p)*identity % p)
        tests.append({"central_z_power": central, "whole_norm_holonomy_and_affine_source_exact": True})
    return {"N": N, "actual_root_lattice_tests": tests,
            "norm_zero_not_replaced_by_identity_or_invertible_gauge": True}


def free_two_period_operators():
    p, nz, nw = 1009, 5, 4
    Z, W = np.zeros((nz, nz), dtype=np.int64), np.zeros((nw, nw), dtype=np.int64)
    for j in range(nz-1):
        Z[j+1, j] = 1
    for j in range(nw-1):
        W[j+1, j] = 1
    checked = 0
    for Q, dual in ((2, 3), (5, 7), (11, 13)):
        sigma = np.kron((np.eye(nz, dtype=np.int64)-Z)@np.diag([pow(Q, j, p) for j in range(nz)]),
                        np.eye(nw, dtype=np.int64)) % p
        tau = np.kron(np.eye(nz, dtype=np.int64),
                      (np.eye(nw, dtype=np.int64)-W)@np.diag([pow(dual, -j, p) for j in range(nw)])) % p
        assert np.array_equal(sigma@tau % p, tau@sigma % p)
        checked += 1
    return {"independent_nome_positive_lattice_operator_cases": checked,
            "sigma_tau_commute_before_any_root_relation": True}


def peripheral_adapter(N):
    p, _, q = field(N)
    Q = q*q % p
    cases = []
    for M in (1, 2, 3):
        numerator = sum(pow(M, 2*j, p) for j in range(N)) % p
        denominator, ddenominator = 1, 0
        predicted = 0
        for j in range(1, N):
            weight = M*M*pow(Q, j, p) % p
            factor, derivative = (1-weight) % p, -j*weight % p
            if not factor:
                break
            ddenominator = (ddenominator*factor+denominator*derivative) % p
            denominator = denominator*factor % p
            predicted = (predicted+j*weight*pow(factor, -1, p)) % p
        else:
            assert numerator and denominator
            C = numerator*pow(denominator, -1, p) % p
            dC = -numerator*ddenominator*pow(denominator, -2, p) % p
            assert C == 1 and dC == predicted
            # Retain a common arbitrary marked phase; it cancels only in ratio.
            epsilon = pow(q, N*(1-N)//2, p)*(-1)**(N+1) % p
            actual = epsilon*pow(M, N-1, p)*pow(numerator, -1, p) % p
            transport_lift = epsilon*pow(M, N-1, p)*pow(denominator, -1, p) % p
            assert actual == transport_lift
            if N == 2 and M == 1:
                assert dC == -pow(2, -1, p) % p
            cases.append({"M": M, "exact_adapter_root_value": C,
                          "retained_Q_log_normal_derivative": int(dC),
                          "original_phase_and_peripheral_factor_retained": True})
    # Archimedean real-part identity, from the exact root pairing.
    zeta = complex(np.exp(2j*np.pi/N))
    value = sum(j*zeta**j/(1-zeta**j) for j in range(1, N))
    assert abs(value.real+N*(N-1)/4) < 1e-9
    return {"N": N, "cancelled_whole_peripheral_cases": cases,
            "physical_real_Q_log_normal": -N*(N-1)/4}


def main():
    cocycle = signed_cocycle()
    free = free_two_period_operators()
    crossings = [actual_crossings(N, generic) for N in range(2, 9) for generic in (False, True)]
    lattices = [cyclic_lattice(N) for N in range(2, 12)]
    source = [peripheral_adapter(N) for N in range(2, 10)]
    result = {"status": "pass", "signed_cocycle": cocycle, "free_two_period_lattice": free,
              "actual_crossing_transport_cases": crossings,
              "actual_root_central_lattices": lattices,
              "actual_peripheral_normal_adapters": source,
              "scope": "Original finite-word transport/source preservation; no analytic-completion replacement or volume claim."}
    target = Path(__file__).with_name("whole_two_period_transport_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_R_entries": sum(x["original_mixed_R_entries_with_marked_common_Cartan"] for x in crossings),
                      "central_lattice_cases": sum(len(x["actual_root_lattice_tests"]) for x in lattices),
                      "peripheral_normal_cases": sum(len(x["cancelled_whole_peripheral_cases"]) for x in source),
                      "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
