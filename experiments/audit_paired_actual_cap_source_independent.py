#!/usr/bin/env python3
"""Independent literal-source test of paired K=1 cap descent and tame bounds."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_cap_wall_fermat_quad_residue import affine_points, data, frames
from audit_actual_rogers_bridge_transport import MixedEntries, crossing, fusion


def exact_cases():
    result = []
    identities = 0
    for N in range(2, 12):
        prime, _, _, Q, *_ = data(N)
        d = N-1
        for delta, a, w in affine_points(N, prime)[:5]:
            assert w == 1
            epsilon = pow(a, N, prime)
            P0, L0 = frames(N, prime, Q, delta, a, 1)
            Pd, Ld = frames(N, prime, Q, Q*delta % prime, a, 1)
            alpha = (1-Q) % prime
            V = [pow(a, 1, prime)*int(Pd[j])*int(P0[d-j])
                 *pow(alpha, -1, prime) % prime for j in range(N)]
            W = [pow(a, d, prime)*int(Ld[j])*int(L0[d-j])
                 *pow(N, -1, prime) % prime for j in range(N)]
            Vop = [pow(a, 1, prime)*int(P0[j])*int(Pd[d-j])
                   *pow(alpha, -1, prime) % prime for j in range(N)]
            Wop = [pow(a, d, prime)*int(L0[j])*int(Ld[d-j])
                   *pow(N, -1, prime) % prime for j in range(N)]
            assert Vop == V[::-1] and Wop == W[::-1]
            for j in range(N):
                left = right = 1
                for r in range(j):
                    left = left*(1-delta*pow(Q, r+2, prime)) % prime
                for r in range(d-j):
                    right = right*(1-delta*pow(Q, r+1, prime)) % prime
                assert V[j] == epsilon*pow(alpha*left*right % prime, -1, prime) % prime
                left = right = 1
                for r in range(j):
                    left = left*(1-delta*pow(Q, r+1, prime)) % prime
                for r in range(d-j):
                    right = right*(1-delta*pow(Q, r, prime)) % prime
                assert W[j] == left*right*pow(N, -1, prime) % prime
                identities += 2
            R = (1-Q*delta)*pow(alpha, -1, prime) % prime
            A = epsilon*pow(N*(1-delta) % prime, -1, prime) % prime
            assert V[d] == R and W[d] == A
            if (1+delta) % prime:
                G = R*(2-epsilon)*pow((1+delta) % prime, -1, prime) % prime
            else:
                assert N % 2
                G = R*N % prime
            assert sum(v*w for v, w in zip(V, W)) % prime == G
            if G:
                vc = np.array(V, dtype=np.int64)
                wr = np.array([value*pow(G, -1, prime) % prime for value in W], dtype=np.int64)
                unit = np.zeros(N, dtype=np.int64)
                unit[d] = 1
                eye = np.eye(N, dtype=np.int64)
                g = (np.outer(vc, unit)+(eye-np.outer(vc, wr))@(eye-np.outer(unit, unit))) % prime
                gi = (eye-np.outer(vc, unit)*pow(R, -1, prime)+np.outer(unit, wr)) % prime
                assert np.array_equal(g@gi % prime, eye)
                assert np.array_equal(gi@g % prime, eye)
                assert np.array_equal(g@unit % prime, vc)
                assert np.array_equal(unit@gi % prime, wr)
                assert int(sp.Matrix(g.tolist()).det()) % prime == R
            for degree in range(2*d+1):
                charge = pow(Q, -1-degree, prime)
                projector = sum(pow(charge, r, prime) for r in range(N))*pow(N, -1, prime) % prime
                assert projector == int(degree == d)
            # Literal deck action leaves both projected normalized sources fixed.
            P0q, L0q = frames(N, prime, Q, delta, a*Q % prime, 1)
            Pdq, Ldq = frames(N, prime, Q, Q*delta % prime, a*Q % prime, 1)
            for j in range(N):
                vq = a*Q*int(Pdq[j])*int(P0q[d-j])*pow(alpha, -1, prime) % prime
                wq = pow(a*Q % prime, d, prime)*int(Ldq[j])*int(L0q[d-j])*pow(N, -1, prime) % prime
                assert vq == V[j] and wq == W[j]
            result.append({"N": N, "actual_Fermat_point": [int(delta), int(a)],
                           "literal_projected_source_and_cosource": True,
                           "both_corner_orientations": True,
                           "exact_K_charge_projector_D_equals_N_minus_1": True,
                           "deck_invariance_and_exact_pairing": True})
    return result, identities


def actual_two_bridge_words():
    result = []
    for N in (2, 3, 4):
        prime, color, q, Q, *_ = data(N)
        E = MixedEntries(N, prime, q)
        d = N-1
        dual = pow(color, -1, prime)*pow(Q, -1, prime) % prime
        C = np.kron(fusion(N, prime, color, E.F), fusion(N, prime, dual, E.F)) % prime
        Ci = np.array(sp.Matrix(C.tolist()).inv_mod(prime)).astype(np.int64)
        R = np.kron(np.kron(np.eye(N, dtype=np.int64), crossing(E, dual, dual, 1)),
                    np.eye(N, dtype=np.int64)) % prime
        B = Ci@R@R@R@C % prime
        row = np.zeros(N**4, dtype=np.int64)
        column = np.zeros(N**4, dtype=np.int64)
        column[(d*N)*N*N+d*N] = 1
        row[(d*N)*N*N+d] = 1
        original = int(row@B@column % prime)
        chosen = []
        for delta, a, _ in affine_points(N, prime):
            P0, L0 = frames(N, prime, Q, delta, a, 1)
            Pd, Ld = frames(N, prime, Q, Q*delta % prime, a, 1)
            V = np.array([a*int(Pd[j])*int(P0[d-j])*pow((1-Q) % prime, -1, prime) % prime
                          for j in range(N)], dtype=np.int64)
            W = np.array([pow(a, d, prime)*int(Ld[j])*int(L0[d-j])*pow(N, -1, prime) % prime
                          for j in range(N)], dtype=np.int64)
            G = int(W@V % prime)
            if not G:
                continue
            w = W*pow(G, -1, prime) % prime
            e = np.zeros(N, dtype=np.int64)
            e[d] = 1
            I = np.eye(N, dtype=np.int64)
            small = (np.outer(V, e)+(I-np.outer(V, w))@(I-np.outer(e, e))) % prime
            small_inverse = (I-np.outer(V, e)*pow(int(V[d]), -1, prime)+np.outer(e, w)) % prime
            full, full_inverse = np.eye(N*N, dtype=np.int64), np.eye(N*N, dtype=np.int64)
            indices = [j*N+d-j for j in range(N)]
            full[np.ix_(indices, indices)] = small
            full_inverse[np.ix_(indices, indices)] = small_inverse
            opposite, opposite_inverse = np.eye(N*N, dtype=np.int64), np.eye(N*N, dtype=np.int64)
            opposite[np.ix_(indices, indices)] = small[::-1, ::-1]
            opposite_inverse[np.ix_(indices, indices)] = small_inverse[::-1, ::-1]
            chosen.append((full, full_inverse, opposite, opposite_inverse, G))
            if len(chosen) == 2:
                break
        first, second = chosen
        Gin = np.kron(first[0], second[0]) % prime
        Gini = np.kron(first[1], second[1]) % prime
        Gout = np.kron(first[0], second[2]) % prime
        Gouti = np.kron(first[1], second[3]) % prime
        transported = Gout@B@Gini % prime
        v = Gin@column % prime
        w = row@Gouti % prime
        assert int(w@transported@v % prime) == original
        # Raw paired co-source has BOTH explicit G factors retained.
        raw = w*(first[4]*second[4] % prime) % prime
        recovered = int(raw@transported@v % prime)*pow(first[4]*second[4] % prime, -1, prime) % prime
        assert recovered == original
        result.append({"N": N, "actual_three_middle_crossing_plat_corner": original,
                       "independent_pair_parameters": True,
                       "marked_and_ordinary_opposite_source_frames": True,
                       "pointwise_original_period_retained_with_full_G_factors": True})
    return result


def norm_cases():
    mp.mp.dps = 80
    rho = mp.mpf(1)/16
    result = []
    for N in (2, 3, 8, 32, 128, 512):
        Q = mp.exp(2j*mp.pi/N)
        maximum_V = maximum_W = mp.mpf(0)
        pairing_error = mp.mpf(0)
        for index in range(16):
            epsilon = rho*mp.exp(2j*mp.pi*index/16)
            delta = mp.exp(mp.log(1-epsilon)/N)
            products = [mp.mpc(1)]
            for j in range(1, N):
                products.append(products[-1]*(1-delta*Q**j))
            R = (1-Q*delta)/(1-Q)
            A = epsilon/(N*(1-delta))
            V = [epsilon*R/(products[j+1]*products[N-1-j]) for j in range(N-1)]+[R]
            W = [(1-delta)*products[j]*products[N-2-j]/N for j in range(N-1)]+[A]
            nv = mp.sqrt(mp.fsum(abs(v)**2 for v in V))
            nw = mp.sqrt(mp.fsum(abs(v)**2 for v in W))
            maximum_V = max(maximum_V, nv)
            maximum_W = max(maximum_W, nw)
            assert nv <= 3 and nw <= 3
            for j in range(N-1):
                reflected = N-2-j
                assert abs(V[j]-V[reflected]) < mp.mpf("1e-65")
                assert abs(W[j]-W[reflected]) < mp.mpf("1e-65")
                ell = min(j+1, N-j-1)
                bound = (mp.pi*rho/4)*mp.exp(2*rho)*mp.mpf(ell)**(-1+2*rho)
                assert abs(V[j]) <= bound and abs(W[j]) <= bound
            G = R*(2-epsilon)/(1+delta)
            pairing_error = max(pairing_error, abs(mp.fsum(v*w for v, w in zip(V, W))-G))
            if index == 0:
                scalar = A/mp.conj(R)
                assert max(abs(w-scalar*mp.conj(v)) for v, w in zip(V, W)) < mp.mpf("1e-65")
                positive = [w*v/G for v, w in zip(V, W)]
                assert all(z.real > 0 and abs(z.imag) < mp.mpf("1e-65") for z in positive)
                expected_norm_squared = abs(R)**2*(2-epsilon)/((1+delta)*A)
                assert abs(nv**2-expected_norm_squared) < mp.mpf("1e-65")
            if index == 0:
                reflection_error = max(abs(w - A/mp.conj(R)*mp.conj(v)) for v, w in zip(V, W))
                assert reflection_error < mp.mpf("1e-65")
                exact_squared_norm = abs(R)**2*(2-epsilon)/((1+delta)*A)
                assert abs(nv**2 - exact_squared_norm) < mp.mpf("1e-65")
                assert max(abs(w/G - mp.conj(v)/nv**2) for v, w in zip(V, W)) < mp.mpf("1e-65")
        assert pairing_error < mp.mpf("1e-65")
        result.append({"N": N, "max_source_norm_on_grid": float(maximum_V),
                       "max_cosource_norm_on_grid": float(maximum_W),
                       "proved_fixed_disc_upper_bound_each": 3,
                       "exact_offcorner_reflection_symmetry": True,
                       "uniform_reflection_tail_bound": True,
                       "exact_pairing_identity_residual": float(pairing_error)})
    return result


def tame_gauge_norms():
    mp.mp.dps = 80
    rows = []
    for N in (2, 3, 8, 32, 128, 512):
        Q = mp.exp(2j*mp.pi/N)
        rho = mp.mpf(1)/16
        largest_g = largest_gi = 0.
        smallest_G = mp.inf
        for index in range(12):
            epsilon = rho*mp.exp(2j*mp.pi*index/12)
            delta = mp.exp(mp.log(1-epsilon)/N)
            products = [mp.mpc(1)]
            for j in range(1, N):
                products.append(products[-1]*(1-delta*Q**j))
            R = (1-Q*delta)/(1-Q)
            A = epsilon/(N*(1-delta))
            V = [epsilon*R/(products[j+1]*products[N-1-j]) for j in range(N-1)]+[R]
            W = [(1-delta)*products[j]*products[N-2-j]/N for j in range(N-1)]+[A]
            G = R*(2-epsilon)/(1+delta)
            smallest_G = min(smallest_G, abs(G))
            assert abs(G-1) < mp.mpf(1)/8
            assert mp.sqrt(mp.fsum(abs(z)**2 for z in V)) <= 3
            assert mp.sqrt(mp.fsum(abs(z)**2 for z in W)) <= 3
            v = np.array([complex(z) for z in V])
            w = np.array([complex(z/G) for z in W])
            e = np.zeros(N, dtype=complex)
            e[-1] = 1
            span, _ = np.linalg.qr(np.column_stack([v, e, w.conj()]))
            gspan = (span+v[:, None]*((1+w[-1])*span[-1, :]-w@span)[None, :]
                     -e[:, None]*span[-1, :][None, :])
            gispan = (span-v[:, None]*span[-1, :][None, :]/complex(R)
                      +e[:, None]*(w@span)[None, :])
            ng = max(1., float(np.linalg.norm(span.conj().T@gspan, 2)))
            ngi = max(1., float(np.linalg.norm(span.conj().T@gispan, 2)))
            largest_g, largest_gi = max(largest_g, ng), max(largest_gi, ngi)
            assert ng <= 15 and ngi <= 8
        rows.append({"N": N, "central_radius": float(rho),
                     "largest_tame_gauge_norm": largest_g,
                     "largest_inverse_norm": largest_gi,
                     "smallest_retained_pairing_G": float(smallest_G)})
    return rows


if __name__ == "__main__":
    families, identities = exact_cases()
    result = {"status": "PASS",
              "scope": "Literal original paired cap source, correct charge projector, both orientations and fixed-disc bounds. Singular-extension equivalence is not inferred.",
              "exact_actual_families": families,
              "literal_formula_identities": identities,
              "actual_two_bridge_pointwise_source_transport": actual_two_bridge_words(),
              "paired_norm_grids": norm_cases(),
              "uniform_tame_gauge_norm_grids": tame_gauge_norms()}
    output = Path(__file__).with_name("paired_actual_cap_source_independent_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(families), "actual paired cap families;", identities,
          "literal formula identities;", len(result["paired_norm_grids"]), "bound grids")
