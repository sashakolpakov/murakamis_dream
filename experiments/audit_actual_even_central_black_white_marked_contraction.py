#!/usr/bin/env python3
"""Exact paired white/source contractions and the retained physical mark.

Generic finite theta identities and exact root field contractions are
checked separately. No paired projector, positive norm replacement, or
moving-q identification of the original circle/pivot is assumed.
"""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_trivalent_even_central_normal_packet import closed
from audit_actual_trivalent_complete_circle_vertex_kernel import (
    vertex_formula, sources, axis_apply, matrix_power,
)


def cup_pair(highest, q, p, p0=1):
    Q = q*q % p
    fac = [1]
    for a in range(1, highest+1):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    width = highest+1
    cup = np.zeros((width, width), dtype=np.int64)
    cap = cup.copy()
    for a in range(width):
        cup[a, highest-a] = (p0*pow(-pow(q, highest, p), a, p)
            * pow(Q, -a*(a+1)//2, p)*fac[a]*fac[highest-a]
            * pow(fac[highest], -1, p)) % p
    for a in range(width):
        cap[a, highest-a] = pow(int(cup[highest-a, a]), -1, p)
    return cup, cap


def flip(width):
    return (np.eye(width*width, dtype=np.int64)
        .reshape(width, width, width, width)
        .transpose(1, 0, 2, 3).reshape(width*width, width*width))


def dual_vector(value, cap, p):
    result = value.copy()
    for a in range(3):
        result = axis_apply(cap, result, a, p)
    return result.transpose(2, 1, 0)


def generic_theta(j):
    # This field value is deliberately not a root for the displayed modules.
    p, q = 1009, 11
    Q, L, width = q*q % p, 2*j, 2*j+1
    fac = [1]
    for a in range(1, 3*j+2):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    K = np.diag([pow(q, L, p)*pow(Q, -a, p) % p
                 for a in range(width)])
    F = np.zeros((width, width), dtype=np.int64)
    for a in range(width-1):
        F[a+1, a] = (1-pow(Q, a+1, p)) % p
    Ki = np.diag([pow(int(a), -1, p) for a in np.diag(K)])
    Fpair = (np.kron(F, np.eye(width, dtype=np.int64))
             + np.kron(Ki, F)) % p
    h = np.array([(-1)**a*pow(Q, -a*(a+1)//2, p)
        * fac[j+a]*fac[L-a]*pow(fac[j]*fac[L], -1, p) % p
        for a in range(j+1)], dtype=np.int64)
    W = np.zeros((width*width, width), dtype=np.int64)
    for a in range(j+1):
        W[a*width+j-a, 0] = h[a]
    for r in range(1, width):
        W[:, r] = Fpair@W[:, r-1] % p*pow(1-pow(Q, r, p), -1, p) % p
    for a in range(j+1):
        assert W[(j+a)*width+L-a, L] == h[a]
    cup, cap = cup_pair(L, q, p)
    P = flip(width)
    DW = cup.T@W.T % p@np.kron(cap.T, cap.T) % p@P % p
    eta = (-1)**j*pow(Q, -j*(3*j+1)//2, p)*fac[3*j+1]
    eta = eta*pow(fac[j]*fac[2*j+1], -1, p) % p
    assert np.array_equal(DW@W % p, eta*np.eye(width, dtype=np.int64) % p)
    # Independent coefficient convolution in the finite Vandermonde step.
    choose = lambda n, a: fac[n]*pow(fac[a]*fac[n-a], -1, p) % p
    convolution = sum(pow(Q, -(j+1)*a, p)*choose(j+a, a)
                      * choose(2*j-a, j-a) for a in range(j+1)) % p
    assert convolution == pow(Q, -j*(j+1), p)*choose(3*j+1, j) % p
    theta = (W@cup % p).reshape((width,)*3)
    anchor = (-1)**j*pow(q, -j*(j+3), p) % p
    assert int(theta[L, j, 0]) == anchor
    Dtheta = dual_vector(theta, cap, p)
    T = theta.reshape(width*width, width).T@Dtheta.reshape(width*width, width) % p
    assert np.array_equal(K@T % p, eta*np.eye(width, dtype=np.int64) % p)
    qdim = sum(pow(int(a), -1, p) for a in np.diag(K)) % p
    assert int(np.sum(theta*Dtheta) % p) == eta*qdim % p
    return {'j': j, 'prime': p, 'generic_lowest_Clebsch': True,
            'finite_Vandermonde_theta_and_anchor': True,
            'entire_pivotal_cut_and_trace': True}


def circle(O, N, p):
    a, b = np.eye(len(O), dtype=np.int64), O.copy()
    for _ in range(2, N):
        a, b = b, (O@b-a) % p
    return (-1)**(N-1)*b % p


def generic_physical_lift(N):
    p, q = 1009, 11
    Q, d, j = q*q % p, N-1, N//2-1
    t, width = d-j, 2*j+1
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    E, F = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    K = np.diag([pow(q, d, p)*pow(Q, -a, p) % p for a in range(N)])
    for a in range(1, N):
        E[a-1, a] = pow(q, -d-1, p)*(1-pow(Q, d+1-a, p)) % p
        F[a, a-1] = (1-pow(Q, a, p)) % p
    Ep, Fp, Kp = coproduct(E, F, K, 2, N, p)
    W = np.zeros((N*N, width), dtype=np.int64)
    for a in range(t+1):
        W[a*N+t-a, 0] = ((-1)**a*pow(q, -d*a, p)
            * pow(Q, a*(t-1)-a*(a-1)//2, p)
            * fac[j+a]*fac[d-a]*pow(fac[j]*fac[d], -1, p)) % p
    for r in range(1, width):
        W[:, r] = Fp@W[:, r-1] % p*pow(fac[r]*pow(fac[r-1], -1, p), -1, p) % p
    EQ, FQ = np.zeros((width, width), dtype=np.int64), np.zeros((width, width), dtype=np.int64)
    KQ = np.diag([pow(q, 2*j, p)*pow(Q, -r, p) % p for r in range(width)])
    for r in range(1, width):
        EQ[r-1, r] = pow(q, -2*j-1, p)*(1-pow(Q, 2*j+1-r, p)) % p
        FQ[r, r-1] = (1-pow(Q, r, p)) % p
    for physical, ordinary in ((Ep, EQ), (Fp, FQ), (Kp, KQ)):
        assert np.array_equal(physical@W % p, W@ordinary % p)
    return {'N': N, 'prime': p, 'explicit_regular_generic_physical_Clebsch_lift': True}


def root_level(N):
    p, eta, q, E, F, K, pivot, R, Ri = balanced_data(N)
    d, m, j = N-1, N//2, N//2-1
    width, Q, x = 2*j+1, q*q % p, pow(q, d, p)
    imag = pow(eta, N, p)
    sine = lambda a: (pow(q, a, p)-pow(q, -a, p))*pow(2*imag, -1, p) % p
    cosine = lambda a: (pow(q, a, p)+pow(q, -a, p))*pow(2, -1, p) % p
    W, fac = closed(N, q, p)
    Wbar, _ = closed(N, pow(q, -1, p), p)
    for a in range(m+1):
        lift = ((-1)**a*pow(q, -d*a, p)
            * pow(Q, a*(m-1)-a*(a-1)//2, p)
            * fac[j+a]*fac[d-a]*pow(fac[j]*fac[d], -1, p)) % p
        assert lift == W[a*N+m-a, 0]
    cup, cap = cup_pair(d, q, p, N*pow(x, -d, p) % p)
    for a in range(N):
        assert cup[a, d-a] == N*pow(x, a-d, p) % p
        assert cap[a, d-a] == pow(x, a, p)*pow(N, -1, p) % p
    pQ, cQ = cup_pair(2*j, q, p)
    P = flip(N)
    G = np.array([sine(r+1)*pow(sine(1), -1, p) % p
                  for r in range(width)], dtype=np.int64)
    Gi = np.diag([pow(int(a), -1, p) for a in G])
    pi = Gi@Wbar.T % p@P % p
    assert not np.any(pi@W % p)
    gamma = pow(q, 3*m*m-2*m+1, p)*pow(N, -2, p) % p
    DW = pQ.T@W.T % p@np.kron(cap.T, cap.T) % p@P % p
    Dpi = P@np.kron(cup.T, cup.T) % p@pi.T % p@cQ.T % p
    assert np.array_equal(DW, gamma*pi % p)
    assert np.array_equal(Dpi, pow(gamma, -1, p)*W % p)
    labels = [(m+r, j) for r in range(width)]
    Uraw, _, _ = vertex_formula(N, x, p, labels, Wbar)
    _, Vbar, Vmbar = vertex_formula(N, pow(x, -1, p), p, labels, W)
    U = Uraw.copy()
    for a in range(3):
        shape = [1, 1, 1]
        shape[a] = width
        U = U*np.diag(Gi).reshape(shape) % p
    A = int(Uraw[2*j, j, 0])*pow(N, -3, p) % p
    if N == 2:
        assert A == 0 and not np.any(U)
        return {'N': N, 'prime': p, 'degenerate_level_source_zero': True}
    scalar = N**3*A*pow(int(G[j]), -1, p) % p
    Theta = U*pow(scalar, -1, p) % p
    DTheta = dual_vector(Theta, cQ, p)
    assert np.array_equal(pow(N, -6, p)*Vbar % p,
                          pow(gamma, 3, p)*scalar*DTheta % p)
    T = Theta.reshape(width*width, width).T@DTheta.reshape(width*width, width) % p
    assert not np.any(T)
    Abar = pow(q, -2*(1-m*(m-1)), p)*A % p
    B = int(np.sum(Theta*Vmbar) % p)
    assert B == N**4*pow(sine(1), 2, p)*pow(cosine(1), -1, p)*Abar % p
    h0 = 2*N*pow(sine(1), -1, p) % p
    actual = pow(N, -7, p)*pow(h0, 3, p)*int(np.sum(U*Vmbar) % p) % p
    target = 8*N**3*pow(cosine(1), -1, p)*A*Abar % p
    assert actual == target
    # Retain the normal by canceling just the genuine [N] factor.
    residue = (-1)**j*pow(q, -3*j*(j+1)+d, p)*N
    residue = residue*pow((1-pow(Q, j, p))*fac[2*j] % p, -1, p) % p
    anchor = (-1)**j*pow(q, -j*(j+3), p) % p
    normal_trace = (pow(gamma, 3, p)*scalar*scalar*residue
                    * pow((-1)**d*anchor*anchor % p, -1, p)) % p
    assert pow(h0, 3, p)*normal_trace % p == target
    direct = []
    if N <= 8:
        rho = (q-pow(q, -1, p)) % p
        Ep, Fp, Kp = coproduct(rho*rho*E % p, F, K, 2, N, p)
        Ki = np.diag([pow(int(a), -1, p) for a in np.diag(Kp)])
        O = (Fp@Ep+q*Kp+pow(q, -1, p)*Ki) % p
        L = circle(O, N, p)
        c = -(q+pow(q, -1, p)) % p
        projector_after_L = np.eye(N*N, dtype=np.int64)
        for a in range(j+1):
            node = (pow(q, 2*a+1, p)+pow(q, -2*a-1, p)) % p
            if node != c:
                projector_after_L = (projector_after_L
                    @ (O-node*np.eye(N*N, dtype=np.int64)) % p
                    * pow(c-node, -1, p)) % p
        B0 = projector_after_L@L % p
        assert np.array_equal(B0, h0*W % p@pi % p)
        J, ordinary, marked = sources(N, x, p)
        omega = pow(eta, d*d, p)*(-1)**j*pow(q, j*(j+1), p) % p
        for exponents in ((0, 0, 0), (1, -2, 3), (-3, 1, 0)):
            value = J.copy()
            for axis, exponent in enumerate(exponents):
                box = matrix_power(R, exponent, Ri, p)@B0 % p
                assert np.array_equal(box, pow(omega, exponent, p)*B0 % p)
                value = axis_apply(box, value, axis, p)
            z = int(np.sum(marked*value) % p)
            assert int(np.sum(ordinary*value) % p) == 0
            assert z == pow(omega, sum(exponents), p)*target % p
            direct.append({'signed_full_Cartan_powers': list(exponents),
                           'literal_marked_scalar': z})
    return {'N': N, 'prime': p, 'true_G_and_both_pivotal_dual_maps': True,
            'nonzero_ordinary_white_but_zero_effective_cut': True,
            'retained_normal_trace_and_original_mark': True,
            'exact_marked_magnetic_sum': B,
            'positive_marked_scalar_image': actual,
            'literal_complete_circle_and_signed_physical_closures': direct}


def profile(N):
    mp.mp.dps = 85
    m, theta = N//2, mp.pi/N
    s = [mp.mpf(1)]
    for a in range(1, m+1):
        s.append(s[-1]*2*mp.sin(theta*a))
    S = sum(mp.sin(k*theta)*mp.cos(k*theta)
            * (s[m]/s[k]/s[m-k])**4 for k in range(1, m))
    normalized = (16*N**3*S*S/mp.cos(theta)
                  * mp.exp(-2*N*4*mp.catalan/mp.pi))
    assert abs(normalized-1) < 7/N
    return {'N': N, 'normalized_even_marked_prefactor': float(normalized)}


if __name__ == '__main__':
    generic = [generic_theta(j) for j in range(7)]
    physical_lifts = [generic_physical_lift(N) for N in (4, 6, 8, 10)]
    roots = [root_level(N) for N in range(2, 20, 2)]
    profiles = [profile(N) for N in (32, 64, 128, 256)]
    result = {'status': 'PASS', 'generic_finite_theta_evaluations': generic,
              'explicit_generic_physical_lifts': physical_lifts,
              'actual_even_ordinary_and_marked_sources': roots,
              'positive_scalar_prefactor_calibrations': profiles,
              'scope': 'Exact even central paired normal, ordinary white and original marked two-vertex contraction. No paired projector, moving-q source-germ replacement, all-channel sewn sum, or general graph survival assertion.'}
    Path(__file__).with_name('actual_even_central_black_white_marked_contraction_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 7 generic finite theta evaluations/4 physical generic lifts; 9 even paired/source levels; 9 literal signed physical closures; 4 positive prefactors')
