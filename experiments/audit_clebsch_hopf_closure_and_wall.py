"""Global actual Hopf/current closure and auxiliary Clebsch wall homotopy."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_clebsch_memory_and_actual_r_excursions import cg, lift_two_head
from audit_endpoint_completed_normal_clock_euler import actual_arrows
from audit_high_color_first_normal_r_degree import root_field


def mm(p, *args):
    out = args[0] % p
    for a in args[1:]:
        out = out@a % p
    return out


def eq(a, b, p):
    assert np.array_equal(a % p, b % p)


def inverse_diag(a, p):
    return np.diag([pow(int(a[i, i]), -1, p) for i in range(len(a))])


def ptr(T, g, dv, dw, p):
    return np.einsum("ij,ajbi->ab", g, T.reshape(dv, dw, dv, dw)) % p


def setup(N, root):
    p, eta_root = root_field(N)
    eta = eta_root if root else int(sp.primitive_root(p))
    q = pow(eta, 2, p)
    _, _, Qjet, _, beta = actual_arrows(N, root, q_override=q)
    Q = Qjet.x
    rho = (q-pow(q, -1, p)) % p
    br = lambda j: (pow(q, j, p)-pow(q, -j, p))*pow(rho, -1, p) % p
    K = np.diag([pow(q, N-1-2*j, p) for j in range(N)])
    E, F = [np.zeros((N, N), dtype=np.int64) for _ in range(2)]
    for j in range(N):
        if j:
            E[j-1, j] = rho*rho*br(N-j) % p
        if j<N-1:
            F[j+1, j] = br(j+1)
    S, Si, *_ = cg(N, p)
    d = [1]
    for j in range(N-1):
        d.append(d[-1]*(j+1)*pow(br(j+1), -1, p) % p)
    b = [1]
    for j in range(N):
        b.append(b[-1]*beta[j, min(1, N-1)].x*pow(j+1, -1, p) % p)
    D, Di = np.diag(d), np.diag([pow(x, -1, p) for x in d])
    B = np.diag(b+[1]*(N-1))
    Bi = np.diag([pow(x, -1, p) for x in b]+[1]*(N-1))
    L = mm(p, B, Si, np.kron(D, np.eye(2, dtype=np.int64)))
    Li = mm(p, np.kron(Di, np.eye(2, dtype=np.int64)), S, Bi)

    def M(C):
        return mm(p, L, np.kron(C, np.eye(2, dtype=np.int64)), Li)

    Lt, Lit = np.kron(L, L), np.kron(Li, Li)

    def Mb(C):
        return mm(p, Lt, lift_two_head(C, N), Lit)

    def P(T):
        old = mm(p, Li, T, L)
        return M((old[::2, ::2]+old[1::2, 1::2])*pow(2, -1, p) % p)

    def hom_h(X):
        old = mm(p, Li, X, L)
        out = np.zeros_like(old)
        out[::2, 1::2] = old[::2, 1::2]*pow(2, -1, p) % p
        out[1::2, ::2] = -old[1::2, ::2]*pow(2, -1, p) % p
        return mm(p, L, out, Li)

    def hom_f(Z):
        old = mm(p, Li, Z, L)
        out = np.zeros_like(old)
        a = old[1::2, ::2]*pow(2, -1, p) % p
        out[::2, ::2], out[1::2, 1::2] = a, -a % p
        return mm(p, L, out, Li)

    def wall(T):
        upper = mm(p, Bi[:N+1, :N+1], T[:N+1, :N+1], B[:N+1, :N+1])
        out = np.zeros(2*N+1, dtype=np.int64)
        for i in range(N+1):
            for j in range(N+1):
                out[N+j-i] += (-1)**i*math.comb(N, i)*int(upper[i, j])
        return out % p

    ah = mm(p, L, np.kron(np.eye(N, dtype=np.int64), np.diag([1, -1])), Li)
    af = mm(p, L, np.kron(np.eye(N, dtype=np.int64), np.array([[0, 0], [1, 0]])), Li)
    return p, q, Q, eta, K, E, F, M, Mb, P, hom_h, hom_f, wall, ah, af, L, Li


def ward(K, E, F, Ki, T, p):
    return ((mm(p, K, T, Ki)-T) % p,
            mm(p, (E@T-T@E) % p, Ki),
            (F@T-mm(p, Ki, T, K, F)) % p)


def case(N, root):
    p, q, Q, eta, K, E, F, M, Mb, P, hh, hf, wall, ah, af, L, Li = setup(N, root)
    d = 2*N
    eye = np.eye(N, dtype=np.int64)
    Ki = inverse_diag(K, p)
    km, em, fm, kim = M(K), M(E), M(F), M(Ki)
    coupon = np.ones((N, N), dtype=np.int64)*pow(N, -1, p) % p
    e_mem = M(coupon)
    units = 0
    for i in range(d):
        for j in range(d):
            T = np.zeros((d, d), dtype=np.int64)
            T[i, j] = 1
            X, Z = (ah@T-T@ah) % p, (af@T-T@af) % p
            remainder = (hh(X)+hf(Z)) % p
            eq(T-P(T), remainder, p)
            eq(wall(T), wall(remainder), p)
            assert int(np.trace(e_mem@T)) % p == int(np.trace(e_mem@P(T))) % p
            units += 1
    oldunits = 0
    for i in range(N):
        for j in range(N):
            C = np.zeros((N, N), dtype=np.int64)
            C[i, j] = 1
            T = M(C)
            assert not wall(T).any()
            for wold, wmem in zip(ward(K, E, F, Ki, C, p), ward(km, em, fm, kim, T, p)):
                eq(M(wold), wmem, p)
                assert not wall(wmem).any()
            oldunits += 1

    # Literal two-leg coproduct, never a primitive upper replacement.
    kt = np.kron(K, K)
    kit = np.kron(Ki, Ki)
    et = (np.kron(E, K)+np.kron(eye, E)) % p
    ft = (np.kron(F, eye)+np.kron(Ki, F)) % p
    kmt, kmit, emt, fmt = Mb(kt), Mb(kit), Mb(et), Mb(ft)
    cold = np.array([[1+3*i+5*j+i*j for j in range(N*N)] for i in range(N*N)], dtype=np.int64) % p
    T = Mb(cold)
    for wo, wm in zip(ward(kt, et, ft, kit, cold, p), ward(kmt, emt, fmt, kmit, T, p)):
        eq(Mb(wo), wm, p)

    # Both source pivots are kept as families; frozen ADO gets its row.
    capchecks, nonzero_crosscaps = 0, 0
    for frozen in (False, True):
        g = np.diag([pow(int(K[i, i]), 1-N if frozen else 1, p) for i in range(N)])
        gm = M(g)
        closed = ptr(T, gm, d, d, p)*pow(2, -1, p) % p
        eq(closed, M(ptr(cold, g, N, N, p)), p)
        assert not wall(closed).any()
        # Full four-block cap, including both offdiagonal terms.
        channel = np.zeros((d, d), dtype=np.int64)
        cross = np.zeros_like(channel)
        groups = (list(range(N+1)), list(range(N+1, d)))
        shaped = T.reshape(d, d, d, d)
        for a, ia in enumerate(groups):
            for b, ib in enumerate(groups):
                piece = np.zeros_like(channel)
                for i in ia:
                    for j in ib:
                        piece += int(gm[i, j])*shaped[:, j, :, i]
                channel = (channel+piece) % p
                if a != b:
                    cross = (cross+piece) % p
        eq(channel*pow(2, -1, p), closed, p)
        nonzero_crosscaps += bool(cross.any())
        # Arbitrary extended operator, not restricted to represented C.
        U = np.array([[2+7*i+2*j+i*j*j for j in range(d*d)] for i in range(d*d)], dtype=np.int64) % p
        pu = ptr(U, gm, d, d, p)*pow(2, -1, p) % p
        totalrows = ward(kmt, emt, fmt, kmit, U, p)
        openrows = ward(km, em, fm, kim, pu, p)
        Erow = (kim@gm@em-em@kim@gm) % p
        Frow = (gm@fm-mm(p, km, fm, gm, kim)) % p
        expectedE = mm(p, ptr(U, Erow, d, d, p)*pow(2, -1, p) % p, kim)
        expectedF = mm(p, kim, ptr(U, Frow, d, d, p)*pow(2, -1, p) % p)
        eq(ptr(totalrows[1], gm, d, d, p)*pow(2, -1, p)-openrows[1], expectedE, p)
        eq(ptr(totalrows[2], gm, d, d, p)*pow(2, -1, p)-openrows[2], expectedF, p)
        if not frozen or root:
            assert not expectedE.any() and not expectedF.any()
        else:
            assert Erow.any() and Frow.any()
            delta_over_Z = (1-pow(Q, N, p))*pow(pow(Q, N, p), -1, p) % p
            kn = np.diag([pow(int(K[i, i]), -N, p) for i in range(N)])
            eq(Erow, delta_over_Z*M(E@kn % p), p)
            eq(Frow, -delta_over_Z*M(g@F % p), p)
        capchecks += 1

    # Actual old checked R commutes with the actual tensor action.
    rho = (q-pow(q, -1, p)) % p
    bracket = lambda a: (pow(q, a, p)-pow(q, -a, p))*pow(rho, -1, p) % p
    R = np.zeros((N*N, N*N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            efp, ffp, fact = 1, 1, 1
            for k in range(min(i, N-1-j)+1):
                if k:
                    efp = efp*bracket(N-i+k-1) % p
                    ffp = ffp*bracket(j+k) % p
                    fact = fact*bracket(k) % p
                a, b = i-k, j+k
                value = (pow(q, k*(k-1)//2, p)*pow(rho, k, p)*efp*ffp
                         *pow(fact, -1, p)*pow(eta, (N-1-2*a)*(N-1-2*b), p)) % p
                R[b*N+a, i*N+j] = value
    for generator in (kt, et, ft):
        eq(R@generator, generator@R, p)
    Rm = Mb(R)
    for w in ward(kmt, emt, fmt, kmit, Rm, p):
        assert not w.any()
    closedR = ptr(Rm, km, d, d, p)*pow(2, -1, p) % p
    assert not wall(closedR).any()
    return {"N": N, "root": root, "auxiliary_matrix_units": units,
            "represented_head_units": oldunits, "pivotal_cap_families": capchecks,
            "nonzero_offdiagonal_caps": nonzero_crosscaps, "actual_R_total_Ward": True}


def main():
    cases = [case(N, root) for N in range(2, 6) for root in (False, True)]
    result = {"status": "pass", "cases": cases,
              "scope": "represented old-head Hopf/source closure, not actual high-color R or Gaussian descent"}
    path = Path(__file__).with_name("clebsch_hopf_closure_and_wall_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(cases),
                      "auxiliary_matrix_units": sum(c["auxiliary_matrix_units"] for c in cases),
                      "represented_head_units": sum(c["represented_head_units"] for c in cases),
                      "nonzero_offdiagonal_caps": sum(c["nonzero_offdiagonal_caps"] for c in cases),
                      "results": str(path)}, indent=2))


if __name__ == "__main__":
    main()
