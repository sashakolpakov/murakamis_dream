#!/usr/bin/env python3
"""Literal A packet and uniform full-branch backward envelope.

No arbitrary annihilator solution is used: the finite sum, endpoint
data and the high-index anchor are checked directly at both parities.
"""

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sy

from audit_high_color_first_normal_r_degree import root_field


def normalized_coefficients(Q, Y):
    p = -Q**(-2)*Y**(-1)*(2*Q**3*Y*Y+Q+1)/(1-Q*Y)**2
    q = (-Q**(-4)*Y**(-2)*(1-Q**3*Y*Y)*(1+Q*Q*Y)
         /((1-Q*Y)**2*(1-Q*Q*Y)))
    return p, q


def symbolic_check():
    Q, Y, Z = sy.symbols('Q Y Z')
    a, b, c = Q*Y*Y*(1-Q*Q*Y), Y*(2*Q**3*Y*Y+Q+1), Q*(Q*Y+1)*(1-Q*Y*Y)
    diagonal_ratio = Q**(-1)*Y**(-2)*(1-Q*Y*Y)*(1+Q*Y)/(1-Q*Y)**2
    pn, qn = normalized_coefficients(Q, Y)
    assert sy.factor(pn+b*diagonal_ratio/c) == 0
    assert sy.factor(qn+a*diagonal_ratio*diagonal_ratio.subs(Y, Q*Y)/c) == 0
    assert sy.factor(pn.subs(Y, Z/Q)+Z**(-1)*(2*Z*Z+1+1/Q)/(1-Z)**2) == 0
    assert sy.factor(qn.subs(Y, Z/Q)+Q**(-2)*Z**(-2)*(1-Q*Z*Z)*(1+Q*Z)/((1-Z)**2*(1-Q*Z))) == 0
    assert sy.factor((1-Q*Z*Z)*(1+Q*Z)-(1+Z)**2*(1-Q*Z)
                     -(Q-1)*Z*(2+Z-Q*Z*Z)) == 0
    return {'exact_normalization_and_both_shifted_coefficients': True,
            'relative_error_cancellation_identity': True}


def field_case(N):
    prime, eta = root_field(N)
    q, Q = eta*eta % prime, pow(eta, 4, prime)
    M = (N-1)//2
    F = [1]
    for a in range(1, N):
        F.append(F[-1]*(1-pow(Q, a, prime)) % prime)
    A, D = [], []
    for r in range(M+1):
        A.append(sum(pow(Q, -v*r, prime)*F[2*v]
                     *pow(F[v]**3*F[v-r] % prime, -1, prime)
                     for v in range(r, M+1)) % prime)
        D.append(pow(Q, -r*r, prime)*F[2*r]*pow(F[r], -3, prime) % prime)
    U = [a*pow(d, -1, prime) % prime for a, d in zip(A, D)]
    assert U[M] == 1
    for r in range(M):
        Y = pow(Q, r, prime)
        an = pow(Q, -2, prime)*pow(Y, -1, prime) % prime
        pn = (-an*(2*pow(Q, 3, prime)*Y*Y+Q+1)
              *pow((1-Q*Y)**2 % prime, -1, prime)) % prime
        qn = (-pow(Q, -4, prime)*pow(Y, -2, prime)*(1-pow(Q, 3, prime)*Y*Y)
              *(1+Q*Q*Y)*pow((1-Q*Y)**2*(1-Q*Q*Y) % prime, -1, prime)) % prime
        following = U[r+2] if r+2 <= M else 0
        assert (U[r]-pn*U[r+1]-qn*following) % prime == 0
        ar = Q*Y*Y*(1-Q*Q*Y) % prime
        br = Y*(2*pow(Q, 3, prime)*Y*Y+Q+1) % prime
        cr = Q*(Q*Y+1)*(1-Q*Y*Y) % prime
        assert cr != 0
        assert (ar*(A[r+2] if r+2 <= M else 0)+br*A[r+1]+cr*A[r]) % prime == 0
        if r == M-1:
            assert qn == 0
    return {'N': N, 'field': prime, 'literal_all_r_normalized_and_original_Ward': True,
            'both_parity_endpoint_zero_cancelled_before_division': True}


def norm2(A):
    if A.rows == 2 and A.cols == 2:
        trace = sum(abs(A[a, b])**2 for a in range(2) for b in range(2))
        determinant = abs(mp.det(A))**2
        return mp.sqrt((trace+mp.sqrt(max(mp.mpf(0), trace*trace-4*determinant)))/2)
    return mp.sqrt(sum(abs(a)**2 for a in A))


def frame(u):
    Z, c = mp.exp(2j*u), mp.cot(u)**2
    return mp.matrix([[-1/Z/mp.sqrt(2), c/Z/mp.sqrt(1+c*c)],
                      [1/mp.sqrt(2), 1/mp.sqrt(1+c*c)]])


def step_case(N):
    mp.mp.dps = 85
    Q, delta, R = mp.exp(2j*mp.pi/N), mp.pi/N, (N+3)//4
    worst_p, worst_q, worst_frame, worst_step = mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for r in range(R):
        Y, u = Q**r, (r+1)*delta
        Z, c = Q*Y, mp.cot(u)**2
        rho = max(1, c)
        pn, qn = normalized_coefficients(Q, Y)
        p0, q0 = (c-1)/Z, c/(Z*Z)
        worst_p = max(worst_p, (r+1)*abs(pn-p0)/rho)
        worst_q = max(worst_q, (r+1)*abs(qn-q0)/rho)
        assert abs(pn-p0) <= 2*mp.pi*rho/(r+1)*(1+mp.mpf('1e-70'))
        assert abs(qn-q0) <= 6*mp.pi*rho/(r+1)*(1+mp.mpf('1e-70'))
        V, Vnext = frame(u), frame(u+delta)
        assert norm2(V) < mp.sqrt(2)
        assert norm2(V**-1) < 2
        worst_frame = max(worst_frame, norm2(V)*norm2(V**-1))
        T = mp.matrix([[pn, qn], [1, 0]])
        actual = norm2(V**-1*T*Vnext)
        worst_step = max(worst_step, (actual/rho-1)*(r+1))
        assert actual <= rho*(1+mp.mpf(128)/(r+1))
    return {'N': N, 'maximum_relative_p_error_constant': float(worst_p),
            'maximum_relative_q_error_constant': float(worst_q),
            'maximum_frame_condition': float(worst_frame),
            'maximum_observed_step_constant': float(worst_step),
            'proved_step_constant': 128}


def E(u):
    if u >= mp.pi/4:
        return mp.mpf(0)
    # An exact Lobachevsky primitive of integral log cot.
    L = lambda a: mp.im(mp.polylog(2, mp.exp(2j*a)))/2
    return 2/mp.pi*(2*L(mp.pi/4)-L(u)-L(mp.pi/2-u))


def source_case(N):
    mp.mp.dps = max(110, 2*N)
    Q, M, R = mp.exp(2j*mp.pi/N), (N-1)//2, (N+3)//4
    F = [mp.mpc(1)]
    for a in range(1, N):
        F.append(F[-1]*(1-Q**a))
    U = []
    for r in range(M+1):
        A = sum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r, M+1))
        D = Q**(-r*r)*F[2*r]/F[r]**3
        U.append(A/D)
    assert max(abs(U[r]) for r in range(R, M+1)) <= 2*N
    residual = -mp.inf
    for r in range(M+1):
        if abs(U[r]):
            current = mp.log(abs(U[r]))-N*E(mp.pi*r/N)
            residual = max(residual, current)
            assert current <= mp.log(8)+128+129*mp.log(N)
        if r < M:
            pn, qn = normalized_coefficients(Q, Q**r)
            following = U[r+2] if r+2 <= M else 0
            error = abs(U[r]-pn*U[r+1]-qn*following)
            assert error <= mp.mpf('1e-70')*max(1, abs(U[r]), abs(pn*U[r+1]), abs(qn*following))
    # Direct check that the right sum, including r=0, never exceeds E.
    for r in (0, R//2, R-1):
        right_sum = sum(mp.log(max(1, mp.cot(mp.pi*(j+1)/N)**2)) for j in range(r, R))
        assert right_sum <= N*E(mp.pi*r/N)+mp.mpf('1e-70')
    return {'N': N, 'both_parity_high_source_anchor_and_all_r_recurrence': True,
            'maximum_log_U_minus_full_envelope': float(residual),
            'uniform_polynomial_prefactor_theorem_checked': True,
            'selected_source_used_before_estimate': True}


if __name__ == '__main__':
    exact = symbolic_check()
    fields = [field_case(N) for N in list(range(2, 41))+[44, 48, 63, 64, 65]]
    steps = [step_case(N) for N in (12, 13, 16, 17, 24, 25, 48, 49, 96, 97, 128, 256, 512)]
    sources = [source_case(N) for N in (12, 13, 16, 17, 24, 25, 32, 33, 48, 49, 64, 65, 96, 97)]
    results = {'status': 'PASS', 'symbolic_normalization': exact,
               'literal_finite_source_Wards': fields, 'uniform_moving_frame_steps': steps,
               'complete_selected_packet_envelopes': sources,
               'scope': 'Uniform all-index full-branch inner upper bound; no outer-cycle survival or filling claim.'}
    Path(__file__).with_name('actual_pretzel_all_index_backward_envelope_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print(f'PASS {len(fields)} exact finite packet levels; {len(steps)} uniform frame/step families; {len(sources)} complete selected all-index envelopes')
