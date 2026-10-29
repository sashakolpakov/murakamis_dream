#!/usr/bin/env python3
"""Full physical Newton-turn Gram and entire reflected source words."""
import itertools
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi, rotated


WORDS = [[("T", 2)], [("T", -2), ("F", 0), ("T", 3)],
         [("T", 1), ("F", 0), ("T", -3), ("F", 0), ("T", 2)]]


def mpower(plus, minus, power, prime):
    out = np.eye(len(plus), dtype=np.int64)
    for _ in range(abs(power)):
        out = (plus if power >= 0 else minus)@out % prime
    return out


def field_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x, Q = N-1, int(K[0, 0]), q*q % prime
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(N*N, dtype=np.int64)
    eye = np.eye(N, dtype=np.int64)
    reverse = eye[::-1].copy()
    c = [(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime for j in range(N)]
    Fq, s2, raw, packet = [1], [1], [I], [I]
    for r in range(1, N):
        Fq.append(Fq[-1]*(1-pow(Q, r, prime)) % prime)
        s2.append((-1)**r*pow(Q, -r*(r+1)//2, prime)*Fq[-1]**2 % prime)
        raw.append((c[r-1]*I-O)@raw[-1] % prime)
        packet.append(pow(int(s2[-1]), -1, prime)*raw[-1] % prime)
    ids = [a*N+d-a for a in range(N)]
    middle = [B[np.ix_(ids, ids)] for B in packet]
    for r in range(N):
        assert np.array_equal(pow(x, d, prime)*rotated(packet[r], N, x, prime) % prime,
                              packet[d-r])
    for i, j in itertools.product(range(N), repeat=2):
        assert int((middle[i]@middle[j] % prime)[0, d]) == int(i+j == d)
    # The actual complete-Hom Casimir, not a fitted diagonal matrix.
    B = np.diag(c).astype(np.int64)
    for j in range(1, N):
        B[j-1, j] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    Z = B.T.copy()
    evalZ, evalB = [eye], [eye]
    for r in range(1, N):
        ratio = int(s2[r-1])*pow(int(s2[r]), -1, prime) % prime
        evalZ.append(ratio*((c[r-1]*eye-Z)@evalZ[-1] % prime) % prime)
        evalB.append(ratio*((c[r-1]*eye-B)@evalB[-1] % prime) % prime)
    for r in range(N):
        assert np.array_equal(evalB[r][:, d], eye[:, d-r])
        actual = O@packet[r] % prime
        expected = c[r]*packet[r] % prime
        if r < d:
            expected = (expected+B[r, r+1]*packet[r+1]) % prime
        assert np.array_equal(actual, expected)
    kappa = pow(eta, d*d, prime)
    actualR = sum((pow(-q, r, prime)*A for r, A in enumerate(packet)),
                  np.zeros_like(I)) % prime
    actualRm = sum((pow(-q, -r, prime)*A for r, A in enumerate(packet)),
                   np.zeros_like(I)) % prime
    assert np.array_equal(kappa*actualR % prime, Rp)
    assert np.array_equal(pow(kappa, -1, prime)*actualRm % prime, Rm)
    T = kappa*sum((pow(-q, r, prime)*A for r, A in enumerate(evalZ)),
                  np.zeros_like(eye)) % prime
    Ti = pow(kappa, -1, prime)*sum(
        (pow(-q, -r, prime)*A for r, A in enumerate(evalZ)), np.zeros_like(eye)) % prime
    # Source-independent all-entry sine-binomial / retained half-Fourier kernel.
    sine = [pow(eta, N*r, prime)*pow(q, -r*(r+1)//2, prime)*Fq[r] % prime
            for r in range(N)]
    simple = np.zeros_like(eye)
    inverse_simple = np.zeros_like(eye)
    for i in range(N):
        for j in range(i+1):
            gaussian = Fq[i]*pow(Fq[j]*Fq[i-j] % prime, -1, prime) % prime
            nuj = (-1)**j*pow(q, j*(j+1), prime) % prime
            simple[i, j] = kappa*nuj*pow(-q, i-j, prime)*gaussian % prime
            beta = sine[i]*pow(sine[j]*sine[i-j] % prime, -1, prime) % prime
            assert simple[i, j] == kappa*(-1)**i*pow(q, i*(j+1), prime)*beta % prime
            assert beta == N*pow(sine[j]*sine[i-j]*sine[d-i] % prime, -1, prime) % prime
            inverse_simple[i, j] = (pow(kappa, -1, prime)*(-1)**i
                                    *pow(q, -i*(j+1), prime)*beta) % prime
    assert np.array_equal(T, simple)
    assert np.array_equal(Ti, inverse_simple)
    two, inverse_two = np.zeros_like(eye), np.zeros_like(eye)
    Fc = [(-1)**r*pow(Q, -r*(r+1)//2, prime)*f % prime
          for r, f in enumerate(Fq)]
    nu = [(-1)**j*pow(q, j*(j+1), prime) % prime for j in range(N)]
    for i in range(N):
        for j in range(i+1):
            m = i-j
            two[i, j] = (pow(kappa, 2, prime)*nu[j]**2*pow(-q, m, prime)
                         *Fq[i]**2*pow(Fq[j]**2*Fq[m] % prime, -1, prime)) % prime
            inverse_two[i, j] = (pow(kappa, -2, prime)*pow(nu[j], -2, prime)
                                 *pow(-q, -m, prime)*Fc[i]**2
                                 *pow(Fc[j]**2*Fc[m] % prime, -1, prime)) % prime
    assert np.array_equal(T@T % prime, two)
    assert np.array_equal(Ti@Ti % prime, inverse_two)
    Df, Dfi = np.diag(Fq), np.diag([pow(f, -1, prime) for f in Fq])
    Dnu = np.diag(nu)
    assert np.array_equal(two, kappa*(Df@T % prime)@Dfi@Dnu % prime)
    assert np.array_equal(reverse@Df@reverse % prime, N*Dnu@Dfi % prime)
    assert np.array_equal(T@Ti % prime, eye)
    assert np.array_equal(Ti.T, reverse@Ti@reverse % prime)
    p = np.array([N*pow(x, -b, prime) % prime if a+b == d else 0
                  for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    m = np.array([pow(x, b, prime)*pow(N*N, -1, prime) % prime
                  for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    for word in WORDS:
        A, Abar, Aadj = eye.copy(), eye.copy(), eye.copy()
        for kind, power in word:
            M = reverse if kind == "F" else mpower(T, Ti, power, prime)
            Mc = reverse if kind == "F" else mpower(T, Ti, -power, prime)
            A, Abar = M@A % prime, Mc@Abar % prime
        for kind, power in reversed(word):
            M = reverse if kind == "F" else reverse@mpower(T, Ti, -power, prime)@reverse % prime
            Aadj = M@Aadj % prime
        assert np.array_equal(Aadj, Abar.T)
        vector = A[:, 0]
        final = Aadj@vector % prime
        energy = int(Abar[:, 0]@vector % prime)
        assert int(final[0]) == energy
        actual = sum((int(a)*M for a, M in zip(final, packet)), np.zeros_like(I)) % prime
        assert int(m@(actual@p % prime) % prime) == energy
        assert phi(actual, N, pivot, prime) == int(final[d])
    # Whole positive source calibration, retaining all kappa phases.
    twice = T@T[:, 0] % prime
    target = np.array([pow(kappa, 2, prime)*pow(-q, r, prime)*Fq[r] % prime
                       for r in range(N)], dtype=np.int64)
    assert np.array_equal(twice, target)
    conjugate = Ti@Ti[:, 0] % prime
    assert int(conjugate@twice % prime) == sum(s2) % prime
    # Entire literal reflected complete-circle source, not a single route.
    U0, U1 = I.copy(), O.copy()
    if d == 1:
        LN = -U1 % prime
    else:
        for _ in range(2, d+1):
            U0, U1 = U1, (O@U1-U0) % prime
        LN = (-1)**d*U1 % prime
    z = pow(x, d, prime)*rotated(Rm@LN % prime, N, x, prime) % prime
    zsharp = pow(x, d, prime)*rotated(Rp@LN % prime, N, x, prime) % prime
    zm, zsm = z[np.ix_(ids, ids)], zsharp[np.ix_(ids, ids)]
    za = [int((zm@middle[d-r] % prime)[0, d]) for r in range(N)]
    zc = [int((zsm@middle[d-r] % prime)[0, d]) for r in range(N)]
    norm = sum(a*b for a, b in zip(za, zc)) % prime
    assert phi(zsharp@(Rm@LN % prime) % prime, N, pivot, prime) == norm
    M, expected_energy = d//2, 0
    Fc = [(-1)**r*pow(Q, -r*(r+1)//2, prime)*f % prime
          for r, f in enumerate(Fq)]
    for r in range(M+1):
        A = sum(pow(Q, -v*r, prime)*Fq[2*v]
                *pow(Fq[v]**3*Fq[v-r] % prime, -1, prime)
                for v in range(r, M+1)) % prime
        Ac = sum(pow(Q, v*r, prime)*Fc[2*v]
                 *pow(Fc[v]**3*Fc[v-r] % prime, -1, prime)
                 for v in range(r, M+1)) % prime
        D = pow(Q, -r*r, prime)*Fq[2*r]*pow(Fq[r], -3, prime) % prime
        Dc = pow(Q, r*r, prime)*Fc[2*r]*pow(Fc[r], -3, prime) % prime
        U, Uc = A*pow(D, -1, prime) % prime, Ac*pow(Dc, -1, prime) % prime
        alpha = (N*N*pow(kappa, -1, prime)*(-1)**r*pow(q, 2*r*r+r, prime)
                 *A*pow(Fq[r], -3, prime)*s2[r]) % prime
        assert za[r] == alpha
        expected_energy += N**4*s2[2*r]*pow(s2[r], -4, prime)*U*Uc
    assert not any(za[M+1:])
    assert norm == expected_energy % prime
    return {"N": N, "full_physical_turn_and_Frobenius_Gram": True,
            "complete_Hom_cyclic_transform_and_all_input_twist": True,
            "all_entry_half_Fourier_sine_binomial_and_true_angle_incidence": True,
            "coherent_all_input_two_crossing_elimination_and_typed_factorial_interface": True,
            "original_reflected_source_words": len(WORDS),
            "all_Cartan_and_simple_double_node_phases_retained": True,
            "entire_reflected_complete_circle_source_and_exact_positive_sum": True}


def complex_case(N):
    d, q = N-1, np.exp(1j*np.pi/N)
    Q, x = q*q, q**d
    E = np.zeros((N, N), dtype=complex)
    F = E.copy()
    K = np.diag([x*Q**(-a) for a in range(N)])
    for a in range(N):
        if a:
            E[a-1, a] = Q**(-a)-1
        if a < d:
            F[a+1, a] = 1-Q**(a+1)
    Et = np.kron(E, K)+np.kron(np.eye(N), E)
    Ft = np.kron(F, np.eye(N))+np.kron(np.linalg.inv(K), F)
    Kt = np.kron(K, K)
    O = Ft@Et+q*Kt+q**(-1)*np.linalg.inv(Kt)
    I = np.eye(N*N, dtype=complex)
    c = 2*np.cos((2*np.arange(N)+1)*np.pi/N)
    s2 = np.cumprod(np.r_[1, 4*np.sin(np.arange(1, N)*np.pi/N)**2])
    packet = [I]
    for r in range(1, N):
        packet.append((c[r-1]*I-O)@packet[-1]*(s2[r-1]/s2[r]))
    rng = np.random.default_rng(721+N)
    alpha = rng.normal(size=N)+1j*rng.normal(size=N)
    f = sum(a*A for a, A in zip(alpha, packet))
    fsharp = sum(a.conjugate()*A for a, A in zip(alpha, packet))
    turned = np.empty_like(f)
    for a, b, k, e in itertools.product(range(N), repeat=4):
        turned[a*N+b, k*N+e] = x**(a-e)*f[(d-a)*N+k, b*N+d-e]
    ids = [a*N+d-a for a in range(N)]
    actual = (fsharp@turned)[ids[0], ids[-1]]
    assert abs(actual-np.vdot(alpha, alpha)) <= 1e-7*max(1, np.vdot(alpha, alpha).real)
    Z = np.diag(c)-np.diag(4*np.sin(np.arange(1, N)*np.pi/N)**2, -1)
    bn, T = np.eye(N, dtype=complex), np.zeros((N, N), dtype=complex)
    for r in range(N):
        T += (-q)**r*bn
        if r < d:
            bn = (c[r]*np.eye(N)-Z)@bn*(s2[r]/s2[r+1])
    T *= q**(d*d/2)
    P = np.eye(N)[::-1]
    assert np.linalg.norm(T.conj().T-P@np.linalg.inv(T)@P) <= 1e-8*max(1, np.linalg.norm(T))
    return {"N": N, "original_complex_positive_Gram": float(actual.real),
            "full_matrix_star_residual": float(np.linalg.norm(T.conj().T-P@np.linalg.inv(T)@P))}


def complete_packet_rate_calibration(N):
    mp.mp.dps = max(100, N+32)
    Q, M = mp.exp(2j*mp.pi/N), (N-1)//2
    F, s2 = [mp.mpc(1)], [mp.mpf(1)]
    for r in range(1, N):
        F.append(F[-1]*(1-Q**r))
        s2.append(abs(F[-1])**2)
    terms = []
    for r in range(M+1):
        A = mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r])
                    for v in range(r, M+1))
        D = Q**(-r*r)*F[2*r]/F[r]**3
        terms.append(N**4*s2[2*r]/s2[r]**4*abs(A/D)**2)
    energy = mp.fsum(terms)
    assert energy > 0
    return {"N": N, "log_entire_positive_source_over_N": mp.nstr(mp.log(energy)/N, 20),
            "proved_asymptotic_rate": mp.nstr(4*mp.catalan/mp.pi, 20),
            "scope": "finite calibration; limiting rate is the written envelope/lower proof"}


if __name__ == "__main__":
    exact = [field_case(N) for N in range(2, 11)]
    complex_rows = [complex_case(N) for N in range(2, 9)]
    rate_rows = [complete_packet_rate_calibration(N) for N in (16, 17, 32, 33, 64, 65)]
    output = {"status": "PASS", "full_original_root_levels": exact,
              "independent_complex_positive_star_levels": complex_rows,
              "positive_complete_packet_rate_calibrations": rate_rows,
              "scope": "Exact all-exterior positive Newton-turn metric and typed "
                       "reflected source words; no general sharp-volume energy bound."}
    Path(__file__).with_name("actual_newton_turn_positive_gram_results.json").write_text(
        json.dumps(output, indent=2)+"\n")
    print("PASS 9 full original Newton/turn/star and complete-circle sources; "
          "27 entire reflected words; 7 complex Gram checks; 6 rate calibrations")
