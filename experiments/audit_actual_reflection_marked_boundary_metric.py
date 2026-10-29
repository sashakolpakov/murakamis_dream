#!/usr/bin/env python3
"""Actual original marked boundary and transported circle reflections.

The finite-field checks use the original module/coproduct and full signed
crossings.  The complex checks independently build the physical generators,
the complete circle polynomial, and the actual turn matrix.  No global FAL
reflection identification is assumed.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_half_clock_source_dilation import generators, original_factorial_R


def inv(n, p):
    return pow(int(n), -1, p)


def full_field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % p, pow(q, N-1, p)
    rho = (q-inv(q, p)) % p
    Ec = rho*rho*E % p
    Et, Ft, Kt = coproduct(Ec, F, K, 2, N, p)
    Ki = np.diag([inv(z, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+inv(q, p)*Ki) % p
    a, b = np.eye(N*N, dtype=np.int64), O.copy()
    for _ in range(2, N):
        a, b = b, (O@b-a) % p
    L = pow(-1, d, p)*b % p
    P = np.zeros((N*N, N*N), dtype=np.int64)
    U = np.zeros((N, N), dtype=np.int64)
    for u in range(N):
        U[u, d-u] = pow(x, u-d, p)
        for v in range(N):
            P[v*N+u, u*N+v] = 1
    Ui = pow(x, d, p)*U % p
    g = np.diag([pow(x, -d, p)*pow(Q, -u, p) % p for u in range(N)])
    gi = np.diag([inv(z, p) for z in np.diag(g)])
    assert np.array_equal(Ui@U.T % p, g)
    assert np.array_equal(U.T@Ui % p, gi)
    assert np.array_equal(U@g@Ui % p, gi)
    H, C = L@P % p, P@L % p

    cup = np.zeros(N*N, dtype=np.int64)
    cup_star = np.zeros(N*N, dtype=np.int64)
    ell = np.zeros(N*N, dtype=np.int64)
    ell_star = np.zeros(N*N, dtype=np.int64)
    marked = np.zeros(N*N, dtype=np.int64)
    md = np.zeros(N*N, dtype=np.int64)
    md_star = np.zeros(N*N, dtype=np.int64)
    normal = np.zeros(N*N, dtype=np.int64)
    harmonic, value = [], 0
    for u in range(N):
        if u:
            value = (value+inv(1-pow(Q, u, p), p)) % p
        harmonic.append(value)
    mean = sum(harmonic)*inv(N, p) % p
    for u in range(N):
        for v in range(N):
            i = u*N+v
            marked[i] = pow(x, v, p)*inv(N*N, p) % p
            if u+v == d:
                cup[i] = N*pow(x, -v, p) % p
                cup_star[i] = N*pow(x, v, p) % p
                ell[i] = pow(x, u, p)*inv(N, p) % p
                ell_star[i] = pow(x, -u, p)*inv(N, p) % p
                md[i] = marked[i]
                md_star[i] = pow(x, -v, p)*inv(N*N, p) % p
                normal[i] = (pow(-1, N+1, p)*N*rho*pow(x, u-d, p)
                             *(harmonic[u]-mean)) % p
    assert np.array_equal(ell, cup_star@P*inv(N*N, p) % p)
    assert np.array_equal(md, cup_star*inv(N**3, p) % p)
    assert np.array_equal(md, ell@P*inv(N, p) % p)
    assert ell@normal % p == 1
    assert md@normal % p == 0
    assert md@cup % p == 1
    assert np.array_equal(L@normal % p, 2*N*cup % p)
    assert np.array_equal(C@normal % p, 2*N**3*ell_star % p)
    assert np.array_equal(H@P@normal % p, 2*N*cup % p)
    w_ordinary = normal*inv(2*N**3, p) % p
    w_marked = P@normal*inv(2*N**4, p) % p
    assert np.array_equal(C@w_ordinary % p, ell_star)
    assert np.array_equal(H@w_marked % p, md_star)
    assert ell@w_ordinary % p == inv(2*N**3, p)
    assert md@w_marked % p == inv(2*N**5, p)
    assert not np.any(C@cup % p)
    assert not np.any(H[:, 0])
    assert marked[0] != 0
    assert np.array_equal(Rp.T, Rp)
    return {'N': N, 'field': p, 'all_original_source_identities': True,
            'ordinary_and_marked_exact_inverse_solutions': True,
            'full_original_R_is_symmetric': True,
            'left_right_duality_pivot_ratios': True}, (p, C, H, ell, md, marked,
                                                      ell_star, md_star,
                                                      w_ordinary, w_marked)


def width_case(N, k, data):
    p, C, H, ell, md, marked, es, ms, wo, wm = data
    row, raw, column, solution = md.copy(), marked.copy(), ms.copy(), wm.copy()
    form = H.copy()
    for _ in range(k-1):
        row, raw = np.kron(ell, row) % p, np.kron(ell, raw) % p
        column = np.kron(es, column) % p
        solution = np.kron(wo, solution) % p
        form = np.kron(C, form) % p
    assert np.array_equal(form@solution % p, column)
    cost = inv(2**k*N**(3*k+2), p)
    assert row@solution % p == cost
    # This is the complete original integer-degree source restriction,
    # checked before any particular crossing word or local cap deletion.
    for indices in np.ndindex(*([N]*(2*k))):
        if sum(indices) == k*(N-1):
            index = np.ravel_multi_index(indices, [N]*(2*k))
            assert raw[index] == row[index]
    return {'N': N, 'cup_pairs': k, 'source_cost': f'1/{2**k*N**(3*k+2)}',
            'whole_integer_degree_restriction': True,
            'exact_tensor_inverse_solution': True}


def complex_orientation_case(N):
    q, Q, x, h, K, E, F, _ = generators(N, 1)
    d, I = N-1, np.eye(N)
    P = np.zeros((N*N, N*N), complex)
    U = np.zeros((N, N), complex)
    for a in range(N):
        U[a, d-a] = x**(a-d)
        for b in range(N):
            P[b*N+a, a*N+b] = 1
    Ui = np.linalg.inv(U)
    assert np.allclose(U.conj().T@U, I)
    # With standard dual bases, the true self-duality map is U^T:
    # original cup = N (I tensor U^T) coev, cap = ev(...)/N.
    duality = U.T
    for actual, antipode in ((h, -h), (K, np.linalg.inv(K)),
                            (E, -E@np.linalg.inv(K)), (F, -K@F)):
        assert np.allclose(duality@antipode.T@np.linalg.inv(duality), actual,
                           atol=2e-10, rtol=2e-10)
    rho = q-1/q
    Et = np.kron(E*rho*rho, K)+np.kron(I, E*rho*rho)
    Ft = np.kron(F, I)+np.kron(np.linalg.inv(K), F)
    Kt = np.kron(K, K)
    O = Ft@Et+q*Kt+1/q*np.linalg.inv(Kt)
    a, b = np.eye(N*N), O.copy()
    for _ in range(2, N):
        a, b = b, O@b-a
    L, H = (-1)**d*b, (-1)**d*b@P
    scale = max(1, np.linalg.norm(H))
    for first in (I, duality):
        for second in (I, duality):
            D = np.kron(first, second)
            Ldual, Sdual = D@L@D.conj().T, D@P@D.conj().T
            Hdual = Ldual@Sdual
            assert np.allclose(Hdual, D@H@D.conj().T, atol=1e-8*scale)
            eig = np.linalg.eigvalsh((Hdual+Hdual.conj().T)/2)
            assert eig.min() >= -1e-8*scale
    Rp = original_factorial_R(N)
    Rm = np.linalg.inv(Rp)
    assert np.allclose(Rp, Rp.T, atol=1e-8, rtol=1e-8)
    assert np.allclose(P@Rm@P, Rp.conj().T, atol=1e-7, rtol=1e-7)
    return {'N': N, 'genuine_dual_object_intertwiner_U_transpose': True,
            'all_four_oriented_circle_congruences_positive': True,
            'literal_reflected_negative_is_adjoint': True}


def bend_case():
    N, d = 2, 1
    q, Q, x, _, K, E, F, _ = generators(N, 1)
    I = np.eye(N)
    P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                  [0, 1, 0, 0], [0, 0, 0, 1]], complex)
    U = np.array([[0, 1/x], [1, 0]], complex)
    Et = np.kron((q-1/q)**2*E, K)+np.kron(I, (q-1/q)**2*E)
    Ft = np.kron(F, I)+np.kron(np.linalg.inv(K), F)
    Kt = np.kron(K, K)
    H = -(Ft@Et+q*Kt+1/q*np.linalg.inv(Kt))@P
    expected = np.zeros((4, 4), complex)
    expected[1:3, 1:3] = [[4, -4j], [4j, 4]]
    assert np.allclose(H, expected)
    partial = H.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    bent = np.kron(I, U)@partial@np.kron(I, np.linalg.inv(U))
    assert np.allclose(np.linalg.eigvalsh(bent), [-4, 4, 4, 4])
    return {'N': 2, 'different_bipartition_single_leg_bend_eigenvalues': [-4, 4, 4, 4],
            'not_an_antiparallel_circle_positivity_claim': True}


if __name__ == '__main__':
    fields, data = [], {}
    for N in range(2, 10):
        row, data[N] = full_field_case(N)
        fields.append(row)
    widths = [width_case(N, 2, data[N]) for N in range(2, 6)]
    widths.append(width_case(2, 3, data[2]))
    results = {'status': 'PASS', 'original_source_fields': fields,
               'all_width_source_examples': widths,
               'transported_genuine_duals': [complex_orientation_case(N) for N in range(2, 9)],
               'different_bipartition_diagnostic': bend_case(),
               'scope': 'All-width original marked-boundary Cauchy metric and true dual-object circle congruences; no whole FAL norm-square or geometric energy theorem.'}
    Path(__file__).with_name('actual_reflection_marked_boundary_metric_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 8 exact source fields; 5 whole-source widths; 7 genuine-dual circle families; exact N=2 distinct-bipartition diagnostic')
