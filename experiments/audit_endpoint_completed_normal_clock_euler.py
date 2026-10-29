"""Actual whole Jackson current, endpoint repair and marked Green carry."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_crossing_normal_spectra import J
from audit_high_color_first_normal_r_degree import gauge, root_field


def actual_arrows(N, normal=False, q_override=None):
    p, eta = root_field(N)
    J.p = p
    q0 = (q_override if q_override is not None else
          (pow(eta, 2, p) if normal else int(sp.primitive_root(p))))
    q = J(q0, -q0*pow(2*N, -1, p) if normal else 0)
    Q = q**2
    m = N*(N+1)-1
    rows = [[J(1)]]
    for a in range(1, m+1):
        old = rows[-1]
        row = [J(1)]+[J() for _ in range(a-1)]+[J(1)]
        for k in range(1, a):
            row[k] = old[k]+Q**(a-k)*old[k-1]
        rows.append(row)
    tau = (-1)**(N*N-1)
    alpha, beta = {}, {}
    for R in range(N+1):
        for S in range(N):
            i = R*N+S
            if R:
                alpha[R, S] = (tau*q**(-N*(m-i))*rows[m-i+N][N]
                               *gauge(N, i)*gauge(N, i-N))
            if R<N:
                beta[R, S] = (q**(-N*i)*rows[i+N][N]
                              *gauge(N, i)*gauge(N, i+N))
    return p, q, Q, alpha, beta


def whole_case(N):
    p, q, Q, alpha, beta = actual_arrows(N)
    Z = pow(Q.x, N, p)
    assert Z != 1
    size = N*(N+1)
    zero = np.zeros((size, size), dtype=np.int64)
    e, f, ed, fd = [zero.copy() for _ in range(4)]
    for (R, S), a in alpha.items():
        e[(R-1)*N+S, R*N+S] = a.x
        ed[R*N+S, (R-1)*N+S] = pow(a.x, -1, p)
    for (R, S), b in beta.items():
        f[(R+1)*N+S, R*N+S] = b.x
        fd[R*N+S, (R+1)*N+S] = pow(b.x, -1, p)
    P0, PN = zero.copy(), zero.copy()
    P0[:N, :N] = np.eye(N, dtype=np.int64)
    PN[-N:, -N:] = np.eye(N, dtype=np.int64)
    eye = np.eye(size, dtype=np.int64)
    assert np.array_equal(ed@e % p, (eye-P0) % p)
    assert np.array_equal(fd@f % p, (eye-PN) % p)
    vals = [pow(Q.x, j, p) for j in range(size)]
    shifted = [Z*a % p for a in vals]
    pole = next(a for a in range(2, p) if all((x+a) % p for x in vals+shifted))
    functions = [(f"t^{k}", lambda t, k=k: pow(t, k, p)) for k in (-3, -1, 0, 1, 2, N+1)]
    functions += [("rational", lambda t: (t*t+3*t+2)*pow(t+pole, -1, p) % p),
                  ("Qdependent", lambda t: (Q.x**3*t*t+Q.x*pow(t, -1, p)) % p)]
    Hhead = np.array([[1+2*i+3*j for j in range(N)] for i in range(N)], dtype=np.int64)
    H = np.kron(np.eye(N+1, dtype=np.int64), Hhead)
    invdelta = pow(1-Z, -1, p)
    remainder_nonzero = 0
    for name, fn in functions:
        g = np.diag([fn(x) for x in vals])
        gs = np.diag([fn(x) for x in shifted])
        actual = (-ed@(e@gs-gs@e)+P0@fd@(f@g-g@f))*invdelta % p
        expected = (g-gs)*invdelta % p
        assert np.array_equal(actual, expected), (N, name)
        offdiag = (-ed@(e@gs@H-gs@H@e)+P0@fd@(f@g@H-g@H@f))*invdelta % p
        correction = (-g@ed@(e@H-H@e)+gs@P0@fd@(f@H-H@f))*invdelta % p
        assert np.array_equal(offdiag, (expected@H+correction) % p), (N, name, "head")
        remainder_nonzero += bool(correction.any())
    assert remainder_nonzero
    marked = 0
    for h in range(4):
        for chirp in (False, True):
            gs = np.diag([((j+N)**h)*pow(pole+shifted[j], -1, p)
                          *(pow(q.x, (j+N)**2, p) if chirp else 1) % p
                          for j in range(size)])
            g = np.diag([(j**h)*pow(pole+vals[j], -1, p)
                         *(pow(q.x, j*j, p) if chirp else 1) % p
                         for j in range(size)])
            actual = (-ed@(e@gs-gs@e)+P0@fd@(f@g-g@f))*invdelta % p
            assert np.array_equal(actual, (g-gs)*invdelta % p)
            marked += 1
    return {"N": N, "prime": p, "whole_functions": len(functions),
            "nonzero_head_corrections": remainder_nonzero,
            "actual_marked_clock_carry_checks": marked}


def normal_case(N):
    p, q, Q, alpha, beta = actual_arrows(N, True)
    ell = [0]
    for S in range(1, N):
        den = (pow(q.x, S, p)-pow(q.x, -S, p)) % p
        summand = (pow(q.x, S, p)+pow(q.x, -S, p))*pow(den, -1, p) % p
        ell.append((ell[-1]-pow(2, -1, p)*summand) % p)
    assert ell[-1] == 0
    logs = 0
    for R in range(1, N+1):
        base = alpha[R, 0].dx*pow(alpha[R, 0].x, -1, p) % p
        for S in range(N):
            a = alpha[R, S]
            assert a.x == N-R+1
            assert (a.dx*pow(a.x, -1, p)-base) % p == ell[S]
            logs += 1
    for R in range(N):
        base = beta[R, 0].dx*pow(beta[R, 0].x, -1, p) % p
        for S in range(N):
            b = beta[R, S]
            assert b.x == R+1
            assert (b.dx*pow(b.x, -1, p)-base) % p == ell[S]
            logs += 1
    # Test every constant head matrix unit in every actual Fr block.
    matrix_units = 0
    for R in range(N+1):
        sigma = 1 if R == 0 else -1
        for S in range(N):
            for T in range(N):
                if R:
                    actual = -(alpha[R, S].dx-alpha[R, T].dx)*pow(alpha[R, S].x, -1, p)
                else:
                    actual = (beta[0, S].dx-beta[0, T].dx)*pow(beta[0, S].x, -1, p)
                assert actual % p == sigma*(ell[S]-ell[T]) % p
                matrix_units += 1
    return {"N": N, "actual_arrow_log_identities": logs,
            "head_matrix_unit_connections": matrix_units}


def symbolic_carry_and_top():
    z, delta, c, t, k = sp.symbols("z delta c t k")
    cases = 0
    for N in range(2, 8):
        polynomial = sp.prod(t-c*z**R for R in range(N+1))
        top = c**(N+1)*z**(N*(N+1)//2)*sp.prod(z**j-1 for j in range(1, N+2))
        assert sp.expand(polynomial.subs(t, c*z**(N+1))-top) == 0
        assert sp.limit((-top/(1-z)).subs(z, 1-delta)/delta**N, delta, 0) == (-1)**N*c**(N+1)*sp.factorial(N+1)
        for R in range(N):
            assert sp.expand(polynomial.subs(t, c*z**(R+1))) == 0
        for h in range(7):
            monomial = k**h
            carry = monomial-monomial.subs(k, k+N)
            cur = monomial
            for _ in range(h+1):
                cur = sp.expand(cur.subs(k, k+N)-cur)
            assert cur == 0
            # Keep a rational clock coefficient at its shifted value.
            g = monomial/(2+t)
            shifted = g.subs({t: z*t, k: k+N}, simultaneous=True)
            residue = sp.limit(delta*((g-shifted)/(1-z)).subs(z, 1-delta), delta, 0)
            assert sp.simplify(residue-carry/(2+t)) == 0
            cases += 1
    return {"top_endpoint_polynomials": 6, "marked_carry_cases": cases}


def main():
    whole = [whole_case(N) for N in range(2, 7)]
    normal = [normal_case(N) for N in range(2, 9)]
    symbolic = symbolic_carry_and_top()
    result = {"status": "pass", "whole_actual_cases": whole,
              "normal_actual_cases": normal, "whole_carry": symbolic,
              "scope": "actual character/normal source current; offdiagonal correction retained"}
    output = Path(__file__).with_name("endpoint_completed_normal_clock_euler_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "whole_actual_cases": len(whole),
                      "normal_actual_cases": len(normal),
                      "head_matrix_units": sum(c["head_matrix_unit_connections"] for c in normal),
                      "actual_marked_clock_carries": sum(c["actual_marked_clock_carry_checks"] for c in whole),
                      **symbolic, "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
