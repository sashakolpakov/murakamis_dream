#!/usr/bin/env python3
"""Actual divided-source dual jets, two clocks and compact source moments."""

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_high_integral_color_frobenius_source import (
    exponential_nilpotent_dual, gaussian_Q_dual_factory, sign)


def string_dual(N, r, s, q, prime, choose):
    m = N*(r+1)-1
    E0 = np.zeros((r+1, r+1), dtype=np.int64)
    E1 = np.zeros_like(E0)
    F0 = np.zeros_like(E0)
    F1 = np.zeros_like(E0)
    beta = [sign(N*k*(k-1)//2+k*s) for k in range(r+1)]
    for k in range(r+1):
        j = k*N+s
        if k:
            upper = m-j+N
            g0, g1 = choose(upper, N)
            exponent = -N*(upper-N)
            prefactor = pow(q, exponent, prime)*beta[k]*beta[k-1] % prime
            E0[k-1, k] = prefactor*g0 % prime
            E1[k-1, k] = prefactor*(g1+exponent*g0) % prime
        if k < r:
            upper = j+N
            g0, g1 = choose(upper, N)
            exponent = -N*(upper-N)
            prefactor = pow(q, exponent, prime)*beta[k]*beta[k+1] % prime
            F0[k+1, k] = prefactor*g0 % prime
            F1[k+1, k] = prefactor*(g1+exponent*g0) % prime
    tau = sign(N*r-1)
    expE0, expE1 = exponential_nilpotent_dual(tau*E0 % prime, tau*E1 % prime, r, prime)
    expF0, expF1 = exponential_nilpotent_dual(F0, F1, r, prime)
    scale = pow(pow(2, r, prime), -1, prime)
    return expF0[:, 0], expF1[:, 0], expE0[0, :]*scale % prime, expE1[0, :]*scale % prime


def actual_clock_case(N):
    r = N
    prime, _, q = field(N)
    Q = q*q % prime
    choose = gaussian_Q_dual_factory(Q, prime)
    head, t, u = 3, 2, 5
    x = t*u % prime
    D = (1+x) % prime
    assert D
    head_weights = [math.comb(N-1, s)*pow(head, s, prime)
                    *pow(pow(1+head, N-1, prime), -1, prime) % prime for s in range(N)]
    mean = r*x*pow(D, -1, prime) % prime
    cases = [(0, 1), (1, 0), (1, 1), (-1, 2), (2, -1)]
    values = {case: [0, 0] for case in cases}
    nonzero_weight_jets = 0
    for s in range(N):
        psi0, psi1, row0, row1 = string_dual(N, r, s, q, prime, choose)
        t_power = np.array([pow(t, k, prime) for k in range(r+1)], dtype=np.int64)
        u_power = np.array([pow(u, k, prime) for k in range(r+1)], dtype=np.int64)
        psi0, psi1 = psi0*t_power % prime, psi1*t_power % prime
        row0, row1 = row0*u_power % prime, row1*u_power % prime
        unit0 = int(row0 @ psi0) % prime
        unit1 = int(row1 @ psi0+row0 @ psi1) % prime
        assert unit0 == pow(D, r, prime)*pow(pow(2, r, prime), -1, prime) % prime
        inverse0 = pow(unit0, -1, prime)
        normalized0 = row0*inverse0 % prime
        normalized1 = (row1*inverse0-row0*unit1*inverse0*inverse0) % prime
        weight0 = normalized0*psi0 % prime
        weight1 = (normalized0*psi1+normalized1*psi0) % prime
        assert int(sum(weight0)) % prime == 1
        assert int(sum(weight1)) % prime == 0
        assert int(np.array(range(r+1), dtype=np.int64) @ weight0) % prime == mean
        if np.any(weight1):
            nonzero_weight_jets += 1
        for a, b in cases:
            f0 = pow(Q, a*s, prime)
            value0 = f0*int(sum(weight0)) % prime
            # Exact q-log derivative, with Z'=2N and Q'=2Q.
            value1 = sum(int(weight1[k])*f0
                         +int(weight0[k])*2*(a*s+N*b*k)*f0
                         for k in range(r+1)) % prime
            expected1 = 2*(a*s+N*b*mean)*f0 % prime
            assert value1 == expected1
            values[(a, b)][0] = (values[(a, b)][0]+head_weights[s]*value0) % prime
            values[(a, b)][1] = (values[(a, b)][1]+head_weights[s]*value1) % prime
    head_mean = pow((1+head*Q)*pow(1+head, -1, prime) % prime, N-1, prime)
    assert values[(1, 0)][0] == head_mean
    assert values[(0, 1)][0] == 1
    # q-log derivative is twice D_Q.
    fr_normal = values[(0, 1)][1]*pow(2*N*r, -1, prime) % prime
    assert fr_normal == x*pow(D, -1, prime) % prime
    return {"N": N, "prime": prime,
            "literal_whole_source_normal_character_cases": len(cases),
            "head_clock_mean": int(head_mean), "Frobenius_normal_clock_mean": int(fr_normal),
            "nonzero_weight_derivative_strings_retained": nonzero_weight_jets,
            "whole_source_derivatives_cancel_only_after_normalization": True}


def compact_source_symbolic():
    t, u, r, M = sp.symbols("t u r M", nonzero=True)
    D = 1+t*u
    E, F, H = t/D, u/D, (1-t*u)/D
    assert sp.cancel(H*H+4*E*F-1) == 0
    J = 2*sp.Matrix([1, t])*sp.Matrix([[1, u]])/D-sp.eye(2)
    assert (J*J-sp.eye(2)).applyfunc(sp.cancel) == sp.zeros(2)
    assert (J*sp.Matrix([1, t])-sp.Matrix([1, t])).applyfunc(sp.cancel) == sp.zeros(2, 1)
    assert (J*sp.Matrix([u, -1])+sp.Matrix([u, -1])).applyfunc(sp.cancel) == sp.zeros(2, 1)
    holonomy = (M+1/M)*sp.eye(2)/2+(M-1/M)*J/2
    assert sp.cancel(holonomy.det()-1) == 0
    assert sp.cancel(sp.trace(holonomy)-M-1/M) == 0
    a = u/D
    assert sp.cancel(1/u/(1+1/(t*u))-(t-t*t*a)) == 0
    berry_t = r*u/D
    assert sp.cancel(-sp.diff(berry_t, u)+r/D**2) == 0
    # Southern theta equals northern theta-r dlogt after reciprocal patch.
    south = r*(t-t*t*a)*(-1/t**2)
    assert sp.cancel(berry_t-south-r/t) == 0
    moment_jacobian = sp.det(sp.Matrix([[sp.diff(t*u/D, t), sp.diff(t*u/D, u)],
                                       [sp.diff(F, t), sp.diff(F, u)]]))
    assert sp.cancel(moment_jacobian-u/D**3) == 0
    density = 1/D**2
    for vt, vu in ((t*t, 1), (-1, -u*u), (2*t, -2*u)):
        assert sp.cancel(sp.diff(density*vt, t)+sp.diff(density*vu, u)) == 0
    exact_moments = []
    for degree in range(1, 9):
        source = sp.Matrix([t**k for k in range(degree+1)])
        row = sp.Matrix([[sp.binomial(degree, k)*u**k/D**degree for k in range(degree+1)]])
        e = sp.zeros(degree+1)
        f = sp.zeros(degree+1)
        h = sp.diag(*[degree-2*k for k in range(degree+1)])
        for k in range(1, degree+1):
            e[k-1, k] = degree-k+1
            f[k, k-1] = k
        assert sp.cancel((row*source)[0]-1) == 0
        for matrix, expected in ((e, E), (f, F), (h, H)):
            assert sp.cancel((row*matrix*source)[0]/degree-expected) == 0
        assert sp.cancel((row*source.diff(t))[0]-degree*u/D) == 0
        C = sp.zeros(degree+1)
        for i, j, coefficient in ((0, degree, 2), (degree, 0, -3),
                                   (degree//2, degree//2, 5), (0, 0, 7)):
            C[i, j] += coefficient
        symbol = (row*C*source)[0]
        left_e = lambda f: sp.diff(f, u)+degree*t/D*f
        right_e = lambda f: -t*t*sp.diff(f, t)+degree*t/D*f
        left_f = lambda f: -u*u*sp.diff(f, u)+degree*u/D*f
        right_f = lambda f: sp.diff(f, t)+degree*u/D*f
        for matrix, left, right in ((e, left_e, right_e), (f, left_f, right_f)):
            assert sp.cancel((row*matrix*C*source)[0]-left(symbol)) == 0
            assert sp.cancel((row*C*matrix*source)[0]-right(symbol)) == 0
        assert sp.cancel((row*(h*C-C*h)*source)[0]
                         -2*(t*sp.diff(symbol, t)-u*sp.diff(symbol, u))) == 0
        assert sp.cancel((row*e*f*C*source)[0]-left_e(left_f(symbol))) == 0
        clock_parameter = sp.Integer(2)
        clock = sp.diag(*[clock_parameter**k for k in range(degree+1)])
        clock_inverse = sp.diag(*[clock_parameter**(-k) for k in range(degree+1)])
        character = ((1+clock_parameter*t*u)/D)**degree
        assert sp.cancel((row*C*clock*source)[0]
                         -character*symbol.subs(t, clock_parameter*t)) == 0
        assert sp.cancel((row*clock*C*source)[0]
                         -character*symbol.subs(u, clock_parameter*u)) == 0
        assert sp.cancel((row*clock*C*clock_inverse*source)[0]
                         -symbol.subs({t: t/clock_parameter, u: clock_parameter*u}, simultaneous=True)) == 0
        exact_moments.append(degree)
    return {"literal_divided_coherent_degrees": exact_moments,
            "compact_source_affine_clutch_exact": True,
            "Berry_connection_and_weight_r_exact": True,
            "meridian_eigenflag_matrix_exact": True,
            "actual_divided_Ward_and_one_sided_source_terms_exact": True,
            "degree_two_matrix_action_transported_without_symbol_multiplicativity": True,
            "whole_clock_dilation_and_source_character_exact": True,
            "source_normal_and_divided_moment_Jacobian": str(moment_jacobian)}


def main():
    result = {"actual_whole_two_clock_cases": [actual_clock_case(N) for N in range(2, 9)],
              "actual_divided_coherent_source_geometry": compact_source_symbolic(),
              "scope": "Actual two-clock/coherent source identities; no identification with both internal knot framing currents or low/high normal periods."}
    target = Path(__file__).with_name("high_color_two_clock_source_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"actual_root_and_first_normal_levels": 7,
                      "whole_character_cases": 35,
                      "exact_coherent_geometry_degrees": 8,
                      "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
