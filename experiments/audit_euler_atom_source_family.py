#!/usr/bin/env python3
"""One Euler-factor source families and literal crossing atomicity.

Actual source coupons use z=x f_RIGHT. Literal R uses a different
nilpotent argument X=q rho^2 E_1 F_2; both are explicitly checked.
No family is declared a knot invariant or assigned a proved volume
limit by these tests.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import fusion, right_regular
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    return out


def eulers(N, p, Q):
    fac, u, v = [1], [1], [1]
    for k in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, k, p)) % p)
        u.append(pow(fac[k], -1, p))
        v.append(pow(-1, k, p)*pow(Q, k*(k-1)//2, p)*u[k] % p)
    return fac, u, v


def rank_mod(A, p):
    rows = [[int(x) % p for x in row] for row in A]
    pivot = 0
    for col in range(len(rows[0])):
        candidate = next((r for r in range(pivot, len(rows)) if rows[r][col]), None)
        if candidate is None:
            continue
        rows[pivot], rows[candidate] = rows[candidate], rows[pivot]
        scale = pow(rows[pivot][col], -1, p)
        rows[pivot] = [x*scale % p for x in rows[pivot]]
        for r in range(pivot+1, len(rows)):
            coeff = rows[r][col]
            if coeff:
                rows[r] = [(x-coeff*y) % p for x, y in zip(rows[r], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def family_case(N):
    p, _, q = field(N)
    Q = q*q % p
    fac, u, v = eulers(N, p, Q)
    g = mul(v, [c*pow(Q, k, p) % p for k, c in enumerate(v)], p)[:N]
    family_cases = 0
    for a in (0, 1, Q, 2, 3):
        a %= p
        ua = [c*pow(a, k, p) % p for k, c in enumerate(u)]
        va = [c*pow(a, k, p) % p for k, c in enumerate(v)]
        wminus, wplus = mul(g, ua, p)[:N], mul(g, va, p)[:N]
        product, total = 1, 1
        for k in range(1, N):
            product = product*(a-pow(Q, k-1, p)) % p
            total = (total+product) % p
        assert wminus[-1] == total*pow(N, -1, p) % p
        aq = a*Q % p
        uaq = [c*pow(aq, k, p) % p for k, c in enumerate(u)]
        jaq = mul(g, uaq, p)[N-1]
        assert jaq == ((Q*a-1)*(a-1)*wminus[-1]
                        +Q*a*(2-pow(a, N, p))*pow(N, -1, p)) % p

        shifted_minus = [c*pow(Q, k, p) % p for k, c in enumerate(wminus)]
        lhs = mul([1, -(1+Q) % p, Q], shifted_minus, p)
        right = mul([1, -a % p], wminus, p)
        for k, value in enumerate(right):
            lhs[k] = (lhs[k]-value) % p
        assert lhs == [0]*N+[(pow(a, N, p)-2)*pow(N, -1, p) % p, wminus[-1]]
        shifted_plus = [c*pow(Q, k, p) % p for k, c in enumerate(wplus)]
        factor = mul([1, -1 % p], mul([1, -Q % p], [1, -a % p], p), p)
        carry = mul(factor, shifted_plus, p)
        for k, value in enumerate(wplus):
            carry[k] = (carry[k]-value) % p
        middle = ((1+a+a*pow(Q, -1, p))*wplus[-1]
                   -a*pow(Q, -1, p)*wplus[-2]) % p
        expected = [0]*N+[-(pow(a, N, p)+2)*pow(N, -1, p) % p,
                          middle, -a*wplus[-1] % p]
        assert carry == expected
        family_cases += 1

    # Uniform source selection for finitely shifted inverse atoms.
    for r in range(min(5, N)):
        a = pow(Q, r, p)
        w = mul(g, [c*pow(a, k, p) % p for k, c in enumerate(u)], p)[:N]
        polynomial = [1]
        for j in range(r):
            polynomial = mul(polynomial, [1, -pow(Q, j, p) % p], p)
        reflected = [c*pow(Q, k, p) % p for k, c in enumerate(v)]
        assert w == mul(polynomial, reflected, p)[:N]
        for m in range(min(5, N-r)):
            expected = sum(coefficient*fac[m+k] for k, coefficient in enumerate(polynomial))
            assert w[N-1-m] == expected*pow(N, -1, p) % p
    assert mul(g, u, p)[N-1] == pow(N, -1, p)
    assert mul(g, [c*pow(Q, k, p) % p for k, c in enumerate(u)], p)[N-1] == Q*pow(N, -1, p) % p
    return {"N": N, "field": p, "parameter_cases": family_cases}


def actual_atom_case(N, M):
    p, _, q = field(N)
    Q = q*q % p
    x = -M*pow(q, -1, p) % p
    rho = (q-pow(q, -1, p)) % p
    fac, u, v = eulers(N, p, Q)
    plus, minus, _, _ = color_matrices(N, p, q, x)
    gauge = np.array([fac[a]*fac[b] % p for a in range(N) for b in range(N)], dtype=np.int64)
    gauge_i = np.array([pow(int(x), -1, p) for x in gauge], dtype=np.int64)
    plus = plus*gauge[:, None]*gauge_i[None, :] % p
    minus = minus*gauge[:, None]*gauge_i[None, :] % p
    E, F = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for a in range(1, N):
        integer = (pow(q, a, p)-pow(q, -a, p))*pow(rho, -1, p) % p
        raw = integer*(x*pow(q, 1-a, p)-pow(x, -1, p)*pow(q, a-1, p))*pow(rho, -1, p) % p
        E[a-1, a] = raw*pow(1-pow(Q, a, p), -1, p) % p
        F[a, a-1] = (1-pow(Q, a, p)) % p
    X = q*rho*rho*np.kron(E, F) % p
    theta, theta_i = np.zeros((N*N, N*N), dtype=np.int64), np.zeros((N*N, N*N), dtype=np.int64)
    power = np.eye(N*N, dtype=np.int64)
    for cu, cv in zip(u, v):
        theta = (theta+cv*power) % p
        theta_i = (theta_i+cu*power) % p
        power = power@X % p
    assert not np.any(power)
    assert np.array_equal(theta@theta_i % p, np.eye(N*N, dtype=np.int64))
    flip = np.zeros_like(theta)
    for a in range(N):
        for b in range(N):
            flip[b*N+a, a*N+b] = 1
    cart = np.diag([pow(x, -a-b, p)*pow(Q, a*b, p) % p for a in range(N) for b in range(N)]).astype(np.int64)
    assert np.array_equal(plus, flip@cart % p@theta % p)

    C, Ci, _, _, _, _, _ = fusion(N, p, Q, [x, x], [0, 0])
    aplus, aminus = np.zeros(N*N, dtype=np.int64), np.zeros(N*N, dtype=np.int64)
    for a in range(N):
        for k in range(N-a):
            aplus[a*N+k] = (pow(-1, k, p)*pow(x, -a-2*k, p)
                            *pow(Q, k*(k-1)//2, p)*pow(fac[a], -1, p)) % p
            aminus[a*N+k] = (pow(-1, k, p)*pow(x, a+2*k, p)
                            *pow(Q, -k*(k-1)//2-k*a, p)*pow(fac[a], -1, p)) % p
    assert np.array_equal(Ci@plus@C % p, right_regular(aplus, N, 0, p))
    assert np.array_equal(Ci@minus@C % p, right_regular(aminus, N, 0, p))
    f = np.zeros(N*N, dtype=np.int64)
    f[N:2*N] = 1
    right_z = x*right_regular(f, N, 0, p) % p
    right_rank = rank_mod(right_z, p)
    atom_rank = rank_mod(X, p)
    if M == 1:
        assert right_rank == N*(N-1)
        assert atom_rank == (N-1)**2
        assert atom_rank != right_rank
    return {"N": N, "M": M, "field": p,
            "literal_R_atom_rank": atom_rank,
            "right_Euler_argument_rank": right_rank,
            "literal_signed_R_relative_coefficients_checked": True}


def diagnostic(N):
    with mp.workdps(100):
        Q = mp.exp(2j*mp.pi/N)
        fac, v = mp.mpc(1), [mp.mpc(1)]
        for k in range(1, N):
            fac *= 1-Q**k
            v.append((-1)**k*Q**(k*(k-1)//2)/fac)
        g = [sum(v[r]*v[k-r]*Q**(k-r) for r in range(k+1)) for k in range(N)]
        added_forward = sum(g[k]*v[N-1-k] for k in range(N))
        return {"N": N, "extra_forward_Euler_log_rate": float(2*mp.pi*mp.log(abs(added_forward))/N),
                "scope": "Diagnostic only; no selected asymptotic or knot equality is proved."}


def main():
    families = [family_case(N) for N in range(2, 25)]
    atoms = [actual_atom_case(N, M) for N in range(2, 8) for M in (1, 3)]
    result = {"status": "PASS", "family_cases": families, "literal_atom_cases": atoms,
              "forward_probe_diagnostics": [diagnostic(N) for N in (8, 16, 32, 64, 128)],
              "scope": "Actual source Euler-factor coupons, exact branch transfer and literal R atomicity; not a new knot invariant or volume theorem."}
    Path(__file__).with_name("euler_atom_source_family_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_levels": len(families),
                      "parameter_cases": sum(r["parameter_cases"] for r in families),
                      "literal_R_cases": len(atoms)}))


if __name__ == "__main__":
    main()
