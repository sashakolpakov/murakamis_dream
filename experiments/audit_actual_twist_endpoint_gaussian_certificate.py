#!/usr/bin/env python3
"""Literal original signed-twist source and finite Gaussian certificates."""
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sy

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi


def original_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q = N-1, q*q % prime
    kappa = pow(eta, d*d, prime)
    r, ri = pow(kappa, -1, prime)*Rp % prime, kappa*Rm % prime
    positive, negative = np.eye(N*N, dtype=np.int64), np.eye(N*N, dtype=np.int64)
    rows = []
    for k in range(8):
        expected = 0
        for j in range(N):
            a = pow(q, 2*j+1, prime)
            c, A = (a+pow(a, -1, prime)) % prime, (a-pow(a, -1, prime)) % prime
            nu = (-1)**j*pow(Q, j*(j+1)//2, prime) % prime
            expected += pow(nu, k, prime)*(c-k*(d-2*j)*A*pow(2, -1, prime))
        expected = (-1)**(d+1)*pow(2, -1, prime)*expected % prime
        assert phi(positive, N, pivot, prime) == expected
        # Negative powers have their full, separately built original inverse.
        conjugate_expected = 0
        qi = pow(q, -1, prime)
        for j in range(N):
            a = pow(qi, 2*j+1, prime)
            c, A = (a+pow(a, -1, prime)) % prime, (a-pow(a, -1, prime)) % prime
            nu = (-1)**j*pow(Q, -j*(j+1)//2, prime) % prime
            conjugate_expected += pow(nu, k, prime)*(c-k*(d-2*j)*A*pow(2, -1, prime))
        conjugate_expected = (-1)**(d+1)*pow(2, -1, prime)*conjugate_expected % prime
        assert phi(negative, N, pivot, prime) == conjugate_expected
        rows.append(k)
        positive, negative = r@positive % prime, ri@negative % prime
    f, P = [1], [1]
    for i in range(1, N):
        f.append(f[-1]*(1-pow(Q, i, prime)) % prime)
        P.append(((1-pow(Q, i, prime))**2*P[-1]+pow(Q, i, prime)) % prime)
    for i in range(N):
        convolution = f[i]*sum((-1)**j*pow(Q, j*(j+1)//2, prime)
                               *pow(f[i-j], -1, prime) for j in range(i+1)) % prime
        assert convolution == P[i]
    r4 = np.eye(N*N, dtype=np.int64)
    for _ in range(4):
        r4 = r@r4 % prime
    assert phi(r4, N, pivot, prime) == pow(-q, d, prime)*sum(P) % prime
    qi = pow(Q, -1, prime)
    Pb = [1]
    for i in range(1, N):
        Pb.append(((1-pow(qi, i, prime))**2*Pb[-1]+pow(qi, i, prime)) % prime)
    G, Kpacket = [], []
    T, Ti = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        kval = 0
        for j in range(i+1):
            nu = (-1)**j*pow(Q, j*(j+1)//2, prime) % prime
            gaussian = f[i]*pow(f[j]*f[i-j] % prime, -1, prime) % prime
            kval += nu*gaussian*Pb[d-j]
            T[i, j] = kappa*nu*pow(-q, i-j, prime)*gaussian % prime
            Ti[i, j] = (pow(kappa, -1, prime)*pow(nu, -1, prime)
                        *pow(-q, j-i, prime)*pow(Q, -j*(i-j), prime)*gaussian) % prime
        Kpacket.append(kval % prime)
        G.append(kval*pow(f[i], -1, prime) % prime)
    assert Kpacket[0] == Pb[d]
    assert Kpacket[d] == sum(Pb) % prime
    P_rev = np.eye(N, dtype=np.int64)[::-1].copy()
    vector = T@P_rev@Ti@Ti@Ti[:, 0] % prime
    for i in range(N):
        assert int(vector[i]) == pow(kappa, -2, prime)*pow(-q, i-d, prime)*Kpacket[i] % prime
        if i:
            Y = pow(Q, i, prime)
            B = -(1+Q+Q*Q)+(4+3*Q)*Y-3*Y*Y
            C = Q+Q*Q+Q**3-(1+4*Q)*Y
            D = Q**3*(pow(Q, i-2, prime)-1)
            value = pow(1-Y, 3, prime)*G[i]+B*G[i-1]
            value += C*G[i-2] if i >= 2 else 0
            value += D*G[i-3] if i >= 3 else 0
            assert value % prime == (Q*Q % prime if i == 1 else 0)
    def power(A, n):
        out = np.eye(N, dtype=np.int64)
        for _ in range(n):
            out = A@out % prime
        return out
    B = T@T@P_rev % prime
    Vm = np.eye(N, dtype=np.int64)
    for m in range(8):
        fleft = power(T, 1-m)[:, 0] if m <= 1 else power(Ti, m-1)[:, 0]
        fright = power(Ti, m)[:, 0]
        for h in range(N):
            left = pow(kappa, m, prime)*sum(int(T[h, j])*int(fleft[d-j]) for j in range(h+1)) % prime
            assert left == int(Vm[h, 0])
            nuh = (-1)**h*pow(Q, h*(h+1)//2, prime) % prime
            right = 0
            for j in range(h+1):
                nu = (-1)**(h-j)*pow(Q, (h-j)*(h-j+1)//2, prime) % prime
                gaussian = f[h]*pow(f[j]*f[h-j] % prime, -1, prime) % prime
                eh = pow(nuh, -1, prime)*nu*pow(-q, j-h, prime)*gaussian % prime
                right += eh*int(fright[d-j])
            assert pow(kappa, m, prime)*right % prime == int(Vm[d-h, 0])
        Vm = B@Vm % prime
    if N <= 8:
        rho = (q-pow(q, -1, prime)) % prime
        Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
        Ki = np.diag([pow(int(a), -1, prime) for a in np.diag(Kt)])
        O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
        eye = np.eye(N*N, dtype=np.int64)
        packets = [eye]
        for h in range(1, min(3, d)+1):
            ch = (pow(q, 2*h-1, prime)+pow(q, -2*h+1, prime)) % prime
            step = (2-pow(Q, h, prime)-pow(Q, -h, prime)) % prime
            packets.append(pow(step, -1, prime)*((ch*eye-O)@packets[-1] % prime) % prime)
        physical = eye.copy()
        for k in range(6):
            for h, packet in enumerate(packets):
                expected = 0
                for j in range(N):
                    a = pow(q, 2*j+1, prime)
                    c, Aj = (a+pow(a, -1, prime)) % prime, (a-pow(a, -1, prime)) % prime
                    nu = (-1)**j*pow(Q, j*(j+1)//2, prime) % prime
                    val, derivative = 1, 0
                    for ell in range(h):
                        cell = (pow(q, 2*ell+1, prime)+pow(q, -2*ell-1, prime)) % prime
                        step = (2-pow(Q, ell+1, prime)-pow(Q, -ell-1, prime)) % prime
                        derivative, val = (((cell-c)*derivative-val)*pow(step, -1, prime) % prime,
                                           (cell-c)*val*pow(step, -1, prime) % prime)
                    expected += pow(nu, k, prime)*(val*(c-k*(d-2*j)*Aj*pow(2, -1, prime))+Aj*Aj*derivative)
                expected = (-1)**(d+1)*pow(2, -1, prime)*expected % prime
                assert phi(physical@packet % prime, N, pivot, prime) == expected
            physical = r@physical % prime
    return {"N": N, "literal_signed_powers_and_full_original_phi": rows,
            "actual_fourth_power_Green_endpoint": True,
            "next_actual_reduced_word_and_rank_three_forced_Ward": True,
            "all_run_first_last_endpoint_coordinates": True,
            "full_original_fixed_Newton_insertions": N <= 8}


def gauss(k, N, h=0):
    epsilon = k % 2
    result = mp.mpc(0)
    for m in range(k+1):
        s = mp.mpf(2*m-epsilon)/(2*k)
        if 0 < s < 1:
            a = (1-2*s)*mp.sin(2*mp.pi*s)*mp.sin(mp.pi*s)**(2*h)
            result += (-1)**m*a*mp.exp(-1j*mp.pi*N*(mp.mpf(m)-mp.mpf(epsilon)/2)**2/k)
    return result


def cyclotomic_modes(k):
    order = 8*k
    multiplier = 1
    while not sy.isprime(order*multiplier+1):
        multiplier += 1
    prime = order*multiplier+1
    primitive = int(sy.primitive_root(prime))
    xi = pow(primitive, multiplier, prime)
    assert pow(xi, order, prime) == 1
    assert all(pow(xi, order//p, prime) != 1 for p in sy.primefactors(order))
    epsilon, rank = k % 2, (k-1)//2
    imaginary = pow(xi, 2*k, prime)
    def weight(j):
        r = 2*j-epsilon
        sine = (pow(xi, 4*r, prime)-pow(xi, -4*r, prime))*pow(2*imaginary, -1, prime) % prime
        t = -(pow(xi, 2*r, prime)-pow(xi, -2*r, prime))**2*pow(4, -1, prime) % prime
        a = (k-r)*pow(k, -1, prime)*sine % prime
        return r, t, a
    data = [weight(j) for j in range(1, rank+1)]
    V = sy.Matrix([[pow(t, h, prime) for _, t, _ in data] for h in range(rank)])
    assert int(V.det()) % prime != 0
    inverse = V.inv_mod(prime)
    for N in range(order):
        modes = sy.Matrix([2*(-1)**j*a*pow(xi, -N*r*r, prime) % prime
                           for j, (r, t, a) in enumerate(data, 1)])
        assert all(int(v) % prime != 0 for v in modes)
        moments = []
        for h in range(rank):
            value = 0
            for j in range(k+1):
                r = 2*j-epsilon
                if not 0 < r < 2*k:
                    continue
                r, t, a = weight(j)
                value += (-1)**j*a*pow(t, h, prime)*pow(xi, -N*r*r, prime)
            moments.append(value % prime)
        vector = sy.Matrix(moments)
        assert all(int(v) % prime == 0 for v in V*modes-vector)
        assert all(int(v) % prime == 0 for v in inverse*vector-modes)
    return {"fixed_twist_power": k, "cyclotomic_order": order,
            "finite_field_prime": prime, "primitive_root_image": xi,
            "resolved_mode_count": rank, "all_residue_classes_checked": order,
            "exact_full_moment_vector_and_nonzero_modal_recovery": True}


def calibration(k, N, h=0):
    mp.mp.dps = 90
    q, d = mp.exp(1j*mp.pi/N), N-1
    value = mp.mpc(0)
    for j in range(N):
        a = q**(2*j+1)
        c, A = a+1/a, a-1/a
        nu = (-1)**j*q**(j*(j+1))
        bv, bd = mp.mpc(1), mp.mpc(0)
        for ell in range(h):
            cell = 2*mp.cos((2*ell+1)*mp.pi/N)
            step = 4*mp.sin((ell+1)*mp.pi/N)**2
            bd, bv = ((cell-c)*bd-bv)/step, (cell-c)*bv/step
        value += nu**k*(bv*(c-mp.mpf(k)*(d-2*j)*A/2)+A*A*bd)
    value *= mp.mpf((-1)**(d+1))/2
    epsilon = k % 2
    coefficient = ((-1)**(d+1)*mp.exp(-1j*mp.pi*epsilon/2-1j*mp.pi*k/(4*N))
                   *(-1j*mp.sqrt(k)/2)*mp.exp(1j*mp.pi/4))
    leading = coefficient*N**mp.mpf('1.5')*N**(2*h)/mp.pi**(2*h)/mp.factorial(h)**2*gauss(k, N, h)
    assert abs(value-leading)/N**(1+2*h) < 20*k
    return {"k": k, "h": h, "N": N, "source_over_leading": mp.nstr(value/leading, 20),
            "error_over_N_1plus2h": mp.nstr(abs(value-leading)/N**(1+2*h), 14),
            "scope": "finite calibration; the proof controls the all-level remainder"}


if __name__ == '__main__':
    exact = [original_case(N) for N in range(2, 13)]
    mp.mp.dps = 90
    a1, a2 = mp.mpf(4)/5*mp.sin(mp.pi/5), mp.mpf(2)/5*mp.sin(3*mp.pi/5)
    coefficient_checks = 0
    for N in range(1, 121):
        assert abs(gauss(3, N)+2*mp.sqrt(3)/3*mp.exp(-1j*mp.pi*N/12)) < mp.mpf('1e-80')
        assert abs(gauss(4, N)+mp.exp(-1j*mp.pi*N/4)) < mp.mpf('1e-80')
        target = 2*mp.exp(-1j*mp.pi*N/20)*(-a1+a2*mp.exp(-2j*mp.pi*N/5))
        assert abs(gauss(5, N)-target) < mp.mpf('1e-80')
        assert abs(gauss(5, N)) >= 2*(a1-a2)-mp.mpf('1e-80')
        coefficient_checks += 3
    profiles = [calibration(k, N) for k in (3, 4, 5) for N in (32, 33, 64, 65, 128, 129, 256, 257)]
    profiles += [calibration(k, N, h) for k in (3, 4, 5) for h in (1, 2) for N in (32, 64, 128)]
    modal_certificates = [cyclotomic_modes(k) for k in range(3, 21)]
    output = {"status": "PASS", "original_source_families": exact,
              "explicit_Gaussian_coefficient_checks": coefficient_checks,
              "rigorous_k5_nonzero_formula": "(8/5)sin(pi/5)(1-cos(pi/5))>0",
              "exact_cyclotomic_Gaussian_mode_certificates": modal_certificates,
              "Gaussian_calibrations": profiles,
              "scope": "Fixed-k exact original endpoint and finite nonvanishing certificate; no whole-word survival or geometric claim."}
    Path(__file__).with_name('actual_twist_endpoint_gaussian_certificate_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print(f'PASS {len(exact)} original signed-source families; {coefficient_checks} coefficient checks; '
          f'{len(profiles)} Gaussian endpoint calibrations; '
          f'{sum(c["all_residue_classes_checked"] for c in modal_certificates)} exact cyclotomic modal residue vectors')
