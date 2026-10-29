"""Exact operator, source and normal checks for the controlled Fourier gauge."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_crossing_normal_spectra import J
from audit_high_color_first_normal_r_degree import gauge, root_field


def eq(a, b, p):
    assert np.array_equal(a % p, b % p)


def finite_case(N):
    p, eta = root_field(N)
    q, Q = pow(eta, 2, p), pow(eta, 4, p)
    invN = pow(N, -1, p)
    size = N*(N+1)
    oneR, oneH = np.eye(N+1, dtype=np.int64), np.eye(N, dtype=np.int64)
    eye = np.eye(size, dtype=np.int64)
    A = np.diag([pow(Q, S, p) for S in range(N)])
    Ai = np.diag([pow(Q, -S, p) for S in range(N)])
    Bf = np.diag([pow(Q, R, p) for R in range(N+1)])
    Bif = np.diag([pow(Q, -R, p) for R in range(N+1)])
    B, Bi = np.kron(Bf, oneH), np.kron(Bif, oneH)
    Ah, Aih = np.kron(oneR, A), np.kron(oneR, Ai)
    V = np.zeros((N, N), dtype=np.int64)
    for S in range(N):
        V[(S+1) % N, S] = 1
    Vh = np.kron(oneR, V)
    fourier = np.array([[pow(Q, a*b, p)*invN % p for b in range(N)]
                        for a in range(N)], dtype=np.int64)
    fourier_inv = np.array([[pow(Q, -a*b, p) for b in range(N)]
                            for a in range(N)], dtype=np.int64)
    G = np.zeros((size, size), dtype=np.int64)
    P = np.zeros_like(G)
    for R in range(N+1):
        for S in range(N):
            G[R*N+(S+R) % N, R*N+S] = 1
        P[R*N+R % N, R*N+R % N] = 1
    H = G@np.kron(oneR, fourier) % p
    Hi = np.kron(oneR, fourier_inv)@G.T % p
    eq(H@Hi, eye, p)
    for R in range(N+1):
        for a in range(N):
            for b in range(N):
                assert H[R*N+a, R*N+b] == invN*pow(Q, b*(a-R), p) % p
    eq(H@Ah@Hi, Vh.T, p)
    eq(H@Vh@Hi, Bi@Ah, p)
    eq(P@Vh.T@P, np.zeros_like(P), p)

    e = np.zeros((N+1, N+1), dtype=np.int64)
    f = np.zeros_like(e)
    for R in range(N+1):
        if R:
            e[R-1, R] = N-R+1
        if R<N:
            f[R+1, R] = R+1
    et = np.kron(e, V.T)
    ft = np.kron(f, V)
    eq(H@np.kron(e, oneH)@Hi, et, p)
    eq(H@np.kron(f, oneH)@Hi, ft, p)

    # Both marked complete lifts retain their actual endpoint zero.
    for M in (1, -1):
        x = -M*pow(q, -1, p) % p
        rho = (q-pow(q, -1, p)) % p
        invrho = pow(rho, -1, p)
        Cq = np.diag([pow(q, S, p) for S in range(N)])
        Cqi = np.diag([pow(q, -S, p) for S in range(N)])
        psi_p = fourier@Cq@fourier_inv % p
        psi_m = fourier@Cqi@fourier_inv % p
        psi_ph, psi_mh = np.kron(oneR, psi_p), np.kron(oneR, psi_m)
        E_integral = M*rho*V.T@(Cq-Cqi) % p
        F_integral = invrho*V@(q*Cq-pow(q, -1, p)*Cqi) % p
        actual_integral = [H@np.kron(oneR, a)@Hi % p for a in (E_integral, F_integral)]
        proposed_integral = [M*rho*B@Aih@(psi_ph-psi_mh) % p,
                             invrho*Bi@Ah@(q*psi_ph-pow(q, -1, p)*psi_mh) % p]
        for a, b in zip(actual_integral, proposed_integral):
            eq(a, b, p)
            eq(et@a-a@et, np.zeros_like(a), p)
            eq(ft@a-a@ft, np.zeros_like(a), p)
        Ehead = V.T@(M*Ai-M*oneH) % p
        Fhead = V@(oneH-Q*A) % p
        Khead = x*Ai % p
        assert Ehead[N-1, 0] == 0 and Fhead[0, N-1] == 0
        actual = [H@np.kron(oneR, a)@Hi % p for a in (Ehead, Fhead, Khead)]
        proposed = [B@Aih@(M*Vh-M*eye) % p,
                    Bi@Ah@(eye-Q*Vh.T) % p, x*Vh % p]
        for a, b in zip(actual, proposed):
            eq(a, b, p)
            eq(et@a-a@et, np.zeros_like(a), p)
            eq(ft@a-a@ft, np.zeros_like(a), p)
        diagonal = np.diag([pow(1-Q, S, p)*pow(q, S*(S-1)//2, p) % p
                            for S in range(N)])
        diagonal_inv = np.diag([pow(int(diagonal[S, S]), -1, p) for S in range(N)])
        eq(diagonal@E_integral@diagonal_inv, Ehead, p)
        eq(diagonal@F_integral@diagonal_inv, Fhead, p)

    Rpos = np.diag([i//N for i in range(size)])
    normal_R = -Rpos@Vh.T
    eq(et@normal_R-normal_R@et, -np.kron(e, V.T@V.T), p)
    eq(ft@normal_R-normal_R@ft, np.kron(f, oneH), p)

    # Exact normalized Fr flags, not just the anchor t=u=1.
    for t, u in ((1, 1), (2, 3), (5, 2)):
        norm = pow(1+t*u, N, p)
        psi = np.array([pow(t, R, p) for R in range(N+1)], dtype=np.int64)
        lam = np.array([math.comb(N, R)*pow(u, R, p)*pow(norm, -1, p) % p
                        for R in range(N+1)], dtype=np.int64)
        prod = np.kron(psi[:, None]@lam[None, :],
                       np.ones((N, N), dtype=np.int64)*invN) % p
        ed = N*P@prod@P % p
        assert int(np.trace(ed)) % p == 1
        assert int(np.trace(ed@Vh.T)) % p == 0
        character = pow((1+Q*t*u)*pow(1+t*u, -1, p) % p, N, p)
        assert int(np.trace(ed@Ah)) % p == character
        eq(H@prod@Hi, ed, p)
    return {"N": N, "prime": p, "high_dimension": size,
            "source_flags": 3, "complete_meridian_lifts": 2}


def actual_normal_case(N):
    p, eta = root_field(N)
    q0 = pow(eta, 2, p)
    J.p = p
    q = J(q0, -q0*pow(2*N, -1, p))
    Q = q**2
    r, m = N, N*(N+1)-1
    rows = [[J(1)]]
    for a in range(1, m+1):
        old = rows[-1]
        row = [J(1)]+[J() for _ in range(a-1)]+[J(1)]
        for k in range(1, a):
            row[k] = old[k]+Q**(a-k)*old[k-1]
        rows.append(row)

    def div_entry(i, d, raising):
        out = i-d if raising else i+d
        if not 0 <= out <= m:
            return J()
        top = m-i+d if raising else i+d
        exponent = -d*(m-i) if raising else -d*i
        return q**exponent*rows[top][d]*gauge(N, i)*gauge(N, out)

    tau = (-1)**(N*r-1)
    zeta = pow(q0, 2, p)
    # The whole finite Fourier coefficients are polynomial before
    # normal specialization; no isolated resonant 0/0 is evaluated.
    for ell in range(N):
        coeff = sum(((Q*pow(zeta, ell, p))**s for s in range(N)), J())/N
        assert coeff.x == (1 if ell == N-1 else 0)
        if ell == N-1:
            expected = -(N-1)*pow(2*N, -1, p) % p
        else:
            expected = pow(N*(1-pow(zeta, ell+1, p)), -1, p)
        assert coeff.dx == expected
    checks = 0
    for raising, sign in ((True, -1), (False, 1)):
        for i in range(m+1):
            out = i-N if raising else i+N
            if not 0 <= out <= m:
                continue
            entry = div_entry(i, N, raising)*(tau if raising else 1)
            C_in, C_out = Q**i, Q**out
            comm = entry*(C_in-C_out)
            assert comm.x == 0
            assert comm.dx == sign*C_in.x*entry.x % p
            # The reduced root representative has no normal coupling.
            assert entry*(Q**(i % N)-Q**(out % N)) == J()
            checks += 1

    # The scale-line statement uses the ACTUAL divided source germs,
    # including their head-dependent normal units, not a constant
    # binomial extension off the root.
    cone_checks, nonconstant_units = 0, 0
    Z = Q**N
    for a, b in ((1, 1), (2, 3), (0, 2), (2, 0)):
        source_norms, clock_norms = [], []
        for S in range(N):
            fp, ep = J(1), J(1)
            weights = []
            for R in range(N+1):
                if R:
                    fp *= div_entry((R-1)*N+S, N, False)
                    ep *= tau*div_entry(R*N+S, N, True)
                weights.append(fp*ep*a**(N-R)*b**R
                               /(math.factorial(R)**2*2**N))
            source_norms.append(sum(weights, J()))
            clock_norms.append(sum((w*Z**R for R, w in enumerate(weights)), J()))
        expected_line = pow((a+b)*pow(2, -1, p) % p, N, p)
        assert all(u.x == expected_line for u in source_norms)
        period = source_norms[0]*sum(
            (Q**S*clock_norms[S]/source_norms[S] for S in range(N)), J())/N
        reduced = source_norms[0]*sum((Q**S for S in range(N)), J())/N
        assert period.x == reduced.x == 0
        assert period.dx == reduced.dx == expected_line*pow(N*(1-zeta), -1, p) % p
        nonconstant_units += sum(u.dx != source_norms[0].dx for u in source_norms[1:])
        cone_checks += 1

    # Literal mixed divided coproduct terms retain total degree -N.
    mixed = 0
    if N <= 4:
        for i in range(m+1):
            for j in range(m+1):
                for a in range(1, N):
                    if i<a or j<N-a:
                        continue
                    entry = (q**(a*(N-a))*div_entry(i, a, True)
                             *div_entry(j, N-a, True)*q**(a*(m-2*j)))
                    if not entry.x:
                        continue
                    incoming, outgoing = Q**(i+j), Q**(i+j-N)
                    comm = entry*(incoming-outgoing)
                    assert comm.x == 0
                    assert comm.dx == -incoming.x*entry.x % p
                    mixed += 1
        assert mixed
    return {"N": N, "actual_single_normal_entries": checks,
            "nonzero_mixed_coproduct_entries": mixed,
            "actual_cone_normal_character_checks": cone_checks,
            "nonconstant_source_normal_units": nonconstant_units}


def symbolic_case():
    # Order (Q_R,q,p_R,p_h); the same order is used after the gauge.
    matrix = sp.Matrix([[1, 0, 0, 0], [1, 0, 0, -1],
                        [0, -1, 1, 0], [0, 1, 0, 0]])
    symplectic = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1],
                            [-1, 0, 0, 0], [0, -1, 0, 0]])
    assert matrix.T*symplectic*matrix == symplectic
    velocity = sp.Symbol("v")
    assert matrix*sp.Matrix([0, velocity, 0, 0]) == sp.Matrix([0, 0, -velocity, velocity])
    qR, q, qp = sp.symbols("q_R q q_prime")
    W = q*(qp-qR)
    assert sp.diff(W, qp) == q
    assert -sp.diff(W, q) == qR-qp
    assert sp.diff(W, qR) == -q
    return {"quadratic_symplectic_map": True,
            "geometric_cut_conormal_velocity": True}


def main():
    colors = [finite_case(N) for N in range(2, 9)]
    normal = [actual_normal_case(N) for N in range(2, 7)]
    result = {"status": "pass", "finite_cases": colors,
              "actual_normal_cases": normal, "symbolic": symbolic_case(),
              "scope": "exact current/conormal dictionary; no whole geometric source descent"}
    output = Path(__file__).with_name("controlled_fourier_current_dictionary_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "finite_cases": len(colors),
                      "actual_normal_cases": len(normal),
                      "mixed_coproduct_entries": sum(c["nonzero_mixed_coproduct_entries"] for c in normal),
                      "actual_cone_normal_characters": sum(c["actual_cone_normal_character_checks"] for c in normal),
                      "nonconstant_source_normal_units": sum(c["nonconstant_source_normal_units"] for c in normal),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
