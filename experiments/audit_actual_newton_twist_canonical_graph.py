#!/usr/bin/env python3
"""Exact finite Weyl/source/Fricke checks and generic physical normalization."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import inverse_mod, apply_pair
from audit_actual_six_port_deformable_source import generic_module


def kernel(N, q, eta, prime):
    Q, d = q*q % prime, N-1
    kappa = pow(eta, d*d, prime)
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    C, Ci = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(i+1):
            gaussian = fac[i]*pow(fac[j]*fac[i-j] % prime, -1, prime) % prime
            C[i, j] = kappa*(-1)**i*pow(q, i+j*j, prime)*gaussian % prime
            Ci[i, j] = pow(kappa, -1, prime)*(-1)**i*pow(q, j*j-2*i*j-i, prime)*gaussian % prime
    assert np.array_equal(C@Ci % prime, np.eye(N, dtype=np.int64))
    # Full support, both diagonals and the actual generic last-row current.
    for i in range(N):
        X = pow(Q, i, prime)
        for j in range(N):
            Y = pow(Q, j, prime)
            forward_i = C[i+1, j] if i < d else 0
            forward_j = C[i, j+1] if j < d else 0
            backward_j = C[i, j-1] if j else 0
            wall = -q*Y*(1-pow(Q, N, prime))*int(i == d)*int(C[i, j])
            assert ((Q*X-Y)*forward_i-q*Y*(1-Q*X)*C[i, j]-wall) % prime == 0
            assert ((Q*Y-1)*forward_j-q*(X-Y)*C[i, j]) % prime == 0
            assert ((Y-1)*C[i, j]-q*(X-pow(Q, -1, prime)*Y)*backward_j) % prime == 0
    return C, Ci, fac


def root_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d, x = q*q % prime, N-1, int(K[0, 0])
    rho, delta = (q-pow(q, -1, prime)) % prime, (q+pow(q, -1, prime)) % prime
    C, Ci, fac = kernel(N, q, eta, prime)
    kappa = pow(eta, d*d, prime)
    Ec = rho*rho*E % prime
    Et, Ft, Kt = coproduct(Ec, F, K, 2, N, prime)
    Kti = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    Omega = (Ft@Et+q*Kt+pow(q, -1, prime)*Kti) % prime
    ids = [a*N+d-a for a in range(N)]
    Aphys = Omega[np.ix_(ids, ids)]
    Bphys = np.diag([(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime for j in range(N)])
    for j in range(1, N):
        Bphys[j-1, j] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    seed = np.zeros((N*N, N), dtype=np.int64)
    seed[ids, np.arange(N)] = 1
    H = np.zeros((N**3, N), dtype=np.int64)
    power = seed.copy()
    for c in range(N):
        H[np.arange(N*N)*N+c] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = Et@power % prime
    assert np.array_equal(np.kron(np.eye(N, dtype=np.int64), Omega)@H % prime, H@Bphys % prime)
    assert np.array_equal(np.kron(np.eye(N, dtype=np.int64), Rp)@H % prime, H@C.T % prime)
    assert np.array_equal(Aphys@C.T % prime, C.T@Bphys.T % prime)
    P = np.eye(N, dtype=np.int64)[::-1]
    S = P@Ci.T % prime
    Si = C.T@P % prime
    assert np.array_equal(S@Bphys@Si % prime, Bphys.T)
    assert np.array_equal(S@Aphys@Si % prime, Bphys)
    cup = np.array([N*pow(x, a-d, prime) % prime for a in range(N)], dtype=np.int64)
    ell = np.array([pow(x, a, prime)*pow(N, -1, prime) % prime for a in range(N)], dtype=np.int64)
    assert np.array_equal(S@cup % prime, N*pow(kappa, -1, prime)*np.eye(N, dtype=np.int64)[:, 0] % prime)
    assert np.array_equal(ell@Si % prime, kappa*pow(N, -1, prime)*np.eye(N, dtype=np.int64)[d] % prime)
    A, B, T = Bphys.T, Bphys, C
    third, I = Aphys, np.eye(N, dtype=np.int64)
    for left, right, output in ((A, B, third), (B, third, A), (third, A, B)):
        assert not np.any((pow(q, -1, prime)*left@right-q*right@left-rho*(delta*output-8*I)) % prime)
    cubic = (pow(q, -1, prime)*(A@B % prime)@third
             +pow(q, -2, prime)*A@A+q*q*B@B+pow(q, -2, prime)*third@third
             -8*pow(q, -1, prime)*A-8*q*B-8*pow(q, -1, prime)*third
             -(delta*delta-32)*I) % prime
    assert not np.any(cubic)
    assert np.array_equal(T@third@Ci % prime, B)
    assert np.array_equal(T@B@Ci % prime, (8*q*I-q*B@A-q*q*third) % prime)
    # All three physical four-plat generators, with the full marked row.
    cup_full = np.zeros(N*N, dtype=np.int64)
    ell_full, marker = np.zeros(N*N, dtype=np.int64), np.zeros(N*N, dtype=np.int64)
    for a in range(N):
        cup_full[a*N+d-a] = cup[a]
        ell_full[a*N+d-a] = ell[a]
        for b in range(N):
            marker[a*N+b] = pow(x, b, prime)*pow(N, -2, prime) % prime
    top = np.kron(ell_full, marker)
    for word in ((1, -2, 3, 2), (2, -1, 2, 3, -2), (-3, 2, 1, -2, 3)):
        physical = np.kron(cup_full, cup_full)[:, None]
        state = np.eye(N, dtype=np.int64)[:, 0]
        for letter in word:
            physical = apply_pair(Rp if letter > 0 else Rm, physical, abs(letter)-1, 4, N, prime)
            M = C if abs(letter) == 2 else C.T
            if letter < 0:
                M = Ci if abs(letter) == 2 else Ci.T
            state = M@state % prime
        assert int(top@physical[:, 0]) % prime == int(state[d])
    return {'N': N, 'all_entry_Weyl_with_boundaries': True,
            'full_physical_Hom_trace_and_R': True,
            'exact_source_intertwiner_and_three_marked_words': True,
            'quantum_Fricke_and_actual_braid_all_normals': True}


def generic_case(N):
    prime, eta, q, d = 1009, 2, 4, N-1
    Q = q*q % prime
    rho = (q-pow(q, -1, prime)) % prime
    Ec, F, K = generic_module(d, q, prime)
    E = Ec*pow(rho*rho % prime, -1, prime) % prime
    I = np.eye(N, dtype=np.int64)
    series, ep, fp, factorial = np.zeros((N*N, N*N), dtype=np.int64), I.copy(), I.copy(), 1
    for k in range(N):
        if k:
            factorial = factorial*(pow(q, k, prime)-pow(q, -k, prime))*pow(rho, -1, prime) % prime
        coef = pow(q, k*(k-1)//2, prime)*pow(rho, k, prime)*pow(factorial, -1, prime) % prime
        series = (series+coef*np.kron(ep, fp)) % prime
        ep, fp = E@ep % prime, F@fp % prime
    cartan = np.array([pow(eta, (d-2*a)*(d-2*b), prime) for a in range(N) for b in range(N)])
    R = cartan[:, None]*series % prime
    R = R.reshape(N, N, N*N).transpose(1, 0, 2).reshape(N*N, N*N)
    Et, Ft, Kt = coproduct(Ec, F, K, 2, N, prime)
    Kti = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Kti) % prime
    ids = [a*N+d-a for a in range(N)]
    A = O[np.ix_(ids, ids)]
    physical = R[np.ix_(ids, ids)]
    nodes = [(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime for j in range(N)]
    Z = np.diag(nodes)
    for j in range(1, N):
        Z[j, j-1] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    v, columns = I[:, 0], []
    for r in range(N):
        columns.append(v)
        if r < d:
            v = (A-nodes[r]*I)@v*pow(int(Z[r+1, r]), -1, prime) % prime
    V = np.column_stack(columns)
    assert np.array_equal(A@V % prime, V@Z % prime)
    C, Ci, _ = kernel(N, q, eta, prime)
    gamma = (-1)**d*pow(q, -N*d, prime) % prime
    assert np.array_equal(physical@V % prime, gamma*V@C % prime)
    return {'N': N, 'generic_full_Cartan_universal_R': True,
            'actual_gamma_factor_retained': True,
            'generic_finite_wall_current_retained': True}


def classical_certificate():
    X, U, Y, V = sp.symbols('X U Y V', nonzero=True)
    A = X+1/X+(X+1/X-2)/U
    B = X+1/X+(X+1/X-2)*U
    pb = X*U*(sp.diff(A, U)*sp.diff(B, X)-sp.diff(A, X)*sp.diff(B, U))
    C = sp.factor((8+pb-A*B)/2)
    assert sp.factor(C-2+(X-1)**2*(U+1)**2/U) == 0
    assert sp.factor(A*A+B*B+C*C+A*B*C-8*(A+B+C)+28) == 0
    outX, outU = Y+(Y-1)/V, -Y*(1+V)
    jacobian = sp.det(sp.Matrix([[sp.diff(outX, Y), sp.diff(outX, V)],
                                [sp.diff(outU, Y), sp.diff(outU, V)]]))
    assert sp.factor(jacobian*Y*V/(outX*outU)-1) == 0
    ai, bi, ci = [expr.subs({X: Y, U: V}) for expr in (A, B, C)]
    ao, bo, co = [expr.subs({X: outX, U: outU}) for expr in (A, B, C)]
    assert sp.factor(ao-ai) == sp.factor(bo-ci) == sp.factor(co-(8-ai*ci-bi)) == 0
    t, a = sp.symbols('t a', nonzero=True)
    resolved_U = (X-1)**2/(X*(a-2))
    assert sp.limit(A.subs(U, resolved_U), X, 1) == a
    assert sp.limit(B.subs(U, resolved_U), X, 1) == 2
    assert sp.limit(C.subs(U, resolved_U), X, 1) == 4-a
    z = sp.symbols('z')
    mu1, mu2 = -sp.Matrix([[1, 1], [0, 1]]), -sp.Matrix([[1, 0], [z, 1]])
    mu3, mu4 = mu2.inv(), mu1.inv()
    assert mu4*mu3*mu2*mu1 == sp.eye(2)
    assert sp.trace(mu2*mu1) == 2+z and sp.trace(mu3*mu2) == 2
    assert sp.trace(mu3*mu1) == 2-z
    return {'exact_canonical_Fricke_and_inverse_Hurwitz': True,
            'exceptional_cup_curve_resolved': True}


if __name__ == '__main__':
    symbolic = classical_certificate()
    generic = [generic_case(N) for N in range(2, 8)]
    roots = [root_case(N) for N in range(2, 9)]
    result = {'status': 'PASS', 'symbolic_classical_graph': symbolic,
              'generic_physical_normalization_families': generic,
              'literal_root_source_families': roots,
              'scope': 'Exact root rational-word source and parabolic character graph; no generic-meridian A-curve or asymptotic theorem inferred.'}
    Path(__file__).with_name('actual_newton_twist_canonical_graph_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS symbolic canonical/cup certificate; {len(generic)} generic full-Cartan families; '
          f'{len(roots)} literal source/Fricke families and {3*len(roots)} marked four-plat words')
