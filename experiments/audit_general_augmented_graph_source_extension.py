#!/usr/bin/env python3
"""Full physical circle Frobenius/turn/source identities, not distinct-node tests."""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi, rotated


def original_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x, size = N-1, int(K[0, 0]), N*N
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(size, dtype=np.int64)
    zero = np.zeros_like(I)
    circles = [zero, I, -O % prime]
    for _ in range(2, 2*N-1):
        circles.append((-O@circles[-1]-circles[-2]) % prime)
    ids = [a*N+d-a for a in range(N)]
    middle = [A[np.ix_(ids, ids)] for A in circles]
    invN2 = pow(N*N, -1, prime)

    def phimid(A):
        return int(A[0, d])

    def turn(A):
        return pow(x, d, prime)*rotated(A, N, x, prime) % prime

    for h in range(1, N):
        assert np.array_equal(circles[N+h],
                              (circles[N-h]-2*(-1)**N*circles[h]) % prime)
    if not N % 2:
        assert not np.any(circles[N]@circles[N] % prime)
    M = np.array([[int(a+b >= N+1 and (a+b-N-1) % 2 == 0)
                   for b in range(1, N+1)] for a in range(1, N+1)], dtype=np.int64)
    Minv = np.array([[int(a+b == N+1)-int(a+b == N-1)
                      for b in range(1, N+1)] for a in range(1, N+1)], dtype=np.int64)
    assert np.array_equal(M@Minv, np.eye(N, dtype=np.int64))
    for a, b in itertools.product(range(1, N+1), repeat=2):
        assert phimid(middle[a]@middle[b] % prime) == N*N*M[a-1, b-1] % prime
        fusion = sum((circles[a+b-1-2*r] for r in range(min(a, b))), zero) % prime
        assert np.array_equal(circles[a]@circles[b] % prime, fusion)
    dual = [invN2*(circles[N+1-a]-circles[max(N-1-a, 0)]) % prime
            for a in range(1, N+1)]
    for a, b in itertools.product(range(N), repeat=2):
        assert phimid(dual[a][np.ix_(ids, ids)]@middle[b+1] % prime) == int(a == b)
    for a in range(1, N+1):
        assert phi(circles[a], N, pivot, prime) == (N*N if a == N else 0) % prime
    assert np.array_equal(turn(I), turn(turn(turn(I))))
    assert np.array_equal(turn(Rm), Rp)
    p = np.array([N*pow(x, -b, prime) % prime if a+b == d else 0
                  for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    ell = np.array([pow(x, a, prime)*pow(N, -1, prime) % prime if a+b == d else 0
                    for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    mark = np.array([pow(x, b, prime)*invN2 % prime
                     for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    assert np.array_equal(turn(I), np.outer(p, ell) % prime)
    assert int(mark@p % prime) == 1
    z = [turn(Rm@circles[a] % prime) for a in range(1, N+1)]
    rng = np.random.default_rng(29102026+N)

    def coeff(A):
        return np.array([phimid(D[np.ix_(ids, ids)]@A[np.ix_(ids, ids)] % prime)
                         for D in dual], dtype=np.int64)

    def evaluate(beta):
        return sum((int(b)*A for b, A in zip(beta, circles[1:N+1])), zero) % prime

    connector = np.array([[phimid(Da[np.ix_(ids, ids)]@middle[N]
                                  @Db[np.ix_(ids, ids)] % prime)
                           for Db in dual] for Da in dual], dtype=np.int64)
    node_mult = {}
    for k in range(N):
        c = (pow(q, 2*k+1, prime)+pow(q, -2*k-1, prime)) % prime
        node_mult[c] = node_mult.get(c, 0)+1
    assert len(node_mult) == (N+1)//2
    packet_count = 0
    for _ in range(3):
        beta = rng.integers(0, prime, size=N, dtype=np.int64)
        f = evaluate(beta)
        assert np.array_equal(coeff(f), beta)
        out = np.zeros_like(I)
        for D, Za in zip(dual, z):
            c = phimid((Rp@D@f % prime)[np.ix_(ids, ids)])
            out = (out+c*Za) % prime
        assert np.array_equal(out, turn(f))
        assert np.array_equal(turn(turn(f)), f)
        marked = int(mark@(f@p % prime) % prime)
        assert phi(turn(f), N, pivot, prime) == marked
        c0 = (q+pow(q, -1, prime)) % prime
        vals = [0, 1, -c0 % prime]
        for _ in range(2, N):
            vals.append((-c0*vals[-1]-vals[-2]) % prime)
        assert marked == sum(int(b)*v for b, v in zip(beta, vals[1:])) % prime
        # The complete connector is a joint channel sum with multiplicity,
        # not a product of independent marked block values.
        gamma = rng.integers(0, prime, size=N, dtype=np.int64)
        g = evaluate(gamma)
        expected = 0
        for c, multiplicity in node_mult.items():
            values = [0, 1, -c % prime]
            for _ in range(2, N):
                values.append((-c*values[-1]-values[-2]) % prime)
            fv = sum(int(b)*v for b, v in zip(beta, values[1:])) % prime
            gv = sum(int(b)*v for b, v in zip(gamma, values[1:])) % prime
            expected = (expected+N*multiplicity*fv*gv) % prime
        assert phi(circles[N]@f@g % prime, N, pivot, prime) == expected
        # Literal three-vertex path with the bilinear full-circle edge (19).
        h = circles[min(N, 2)]
        vf = np.array([phimid(f[np.ix_(ids, ids)]@A % prime)
                       for A in middle[1:N+1]], dtype=np.int64)
        vg = np.array([phimid(g[np.ix_(ids, ids)]@A % prime)
                       for A in middle[1:N+1]], dtype=np.int64)
        center = np.array([[phimid(h[np.ix_(ids, ids)]@A@B % prime)
                            for B in middle[1:N+1]]
                           for A in middle[1:N+1]], dtype=np.int64)
        tree = int((vf@connector % prime)@center@((connector@vg) % prime) % prime)
        target = circles[N]@circles[N]@f@g@h % prime
        assert tree == phi(target, N, pivot, prime)
        if not N % 2:
            assert tree == 0
        # Two differently nested products/turns, reconstructed only through
        # the open circle resolution; the comparison is full physical.
        direct = turn((f@Rp) % prime)@Rm % prime
        direct = turn(direct@turn(circles[N]) % prime)
        a = evaluate(coeff(f@Rp % prime))
        a = sum((phimid((Rp@D@a % prime)[np.ix_(ids, ids)])*Za
                 for D, Za in zip(dual, z)), zero) % prime
        a = a@Rm % prime
        a = a@turn(circles[N]) % prime
        a = sum((phimid((Rp@D@a % prime)[np.ix_(ids, ids)])*Za
                 for D, Za in zip(dual, z)), zero) % prime
        assert np.array_equal(a, direct)
        assert phi(a, N, pivot, prime) == phi(direct, N, pivot, prime)
        assert int(mark@(a@p % prime) % prime) == int(mark@(direct@p % prime) % prime)
        packet_count += 1
    return {"N": N, "all_full_physical_fusion_and_normal_aliases": True,
            "all_frobenius_pairings_and_sparse_duals": True,
            "open_turn_reconstruction_and_original_closures": packet_count,
            "nested_original_source_circuits": packet_count,
            "joint_complete_connector_and_literal_tree_tests": packet_count}


def norm_cases():
    rows = []
    for N in range(2, 81):
        M = np.array([[int(a+b >= N+1 and (a+b-N-1) % 2 == 0)
                       for b in range(1, N+1)] for a in range(1, N+1)], dtype=float)
        Minv = np.array([[int(a+b == N+1)-int(a+b == N-1)
                          for b in range(1, N+1)] for a in range(1, N+1)], dtype=float)
        sv = np.linalg.svd(M, compute_uv=False)
        assert sv[0] <= (N+1)//2+1e-10
        assert sv[-1] >= .5-1e-10
        assert np.linalg.norm(Minv, 2) <= 2+1e-10
        theta = (2*np.arange((N+1)//2)+1)*np.pi/N
        if N % 2:
            theta = theta[:-1]
        for power in (-10**6, -7, -1, 0, 1, 2, 10**6):
            derivative = (abs(power)*(N-1-2*np.arange(len(theta)))
                          /(4*np.abs(np.sin(theta)))) if len(theta) else np.array([])
            hnorm = 1+(float(np.max(derivative)) if len(derivative) else 0)/N**2
            assert hnorm <= 1+abs(power)/8+1e-9
        rows.append({"N": N, "frobenius_condition": float(sv[0]/sv[-1]),
                     "all_signed_twist_normal_bounds": True})
    return rows


if __name__ == "__main__":
    original = [original_case(N) for N in range(2, 11)]
    norms = norm_cases()
    result = {"status": "PASS", "full_original_source_levels": original,
              "coefficient_and_full_normal_norm_levels": norms,
              "scope": "Exact all-exterior full-Hermite two-port sewing; "
                       "no six-port geometric packet or general sharp volume claim."}
    Path(__file__).with_name("general_augmented_graph_source_extension_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print("PASS 9 full physical circle/Frobenius/source levels; "
          "27 open-port/nested and connector/tree circuits; "
          "79 metric and signed-normal levels")
