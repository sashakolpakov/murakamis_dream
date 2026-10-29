"""Exact Clebsch memory, whole source/gauges and universal actual R leakage."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_degree_elevation_actual_head_ward import elev
from audit_endpoint_completed_normal_clock_euler import actual_arrows
from audit_high_color_first_normal_r_degree import root_field, setup


def eq(a, b, p):
    assert np.array_equal(a % p, b % p)


def cg(N, p):
    invN, invn = pow(N, -1, p), pow(N-1, -1, p)
    de = np.zeros((2*N, N+1), dtype=np.int64)
    iota = np.zeros((2*N, N-1), dtype=np.int64)
    m = np.zeros((N+1, 2*N), dtype=np.int64)
    rho = np.zeros((N-1, 2*N), dtype=np.int64)
    for j in range(N+1):
        if j<N:
            de[2*j, j] = 1
        if j:
            de[2*(j-1)+1, j] = 1
    for j in range(N):
        m[j, 2*j] = (N-j)*invN % p
        m[j+1, 2*j+1] = (j+1)*invN % p
        if j:
            rho[j-1, 2*j] = (N-1)*invN % p
        if j<N-1:
            rho[j, 2*j+1] = -(N-1)*invN % p
    for j in range(N-1):
        iota[2*(j+1), j] = (j+1)*invn % p
        iota[2*j+1, j] = -(N-1-j)*invn % p
    S = np.column_stack([de, iota])
    Si = np.vstack([m, rho])
    eq(Si@S, np.eye(2*N, dtype=np.int64), p)
    eq(S@Si, np.eye(2*N, dtype=np.int64), p)
    return S, Si, de, m, iota, rho


def finite_word(N):
    p, q, Q, _, beta = actual_arrows(N)
    S, Si, de, m, iota, rho = cg(N, p)
    eye2 = np.eye(2, dtype=np.int64)

    def M(C):
        return Si@np.kron(C, eye2)@S % p

    C = np.array([[2+3*i+5*j+i*j for j in range(N)] for i in range(N)], dtype=np.int64)
    D = np.array([[7+i+2*j+i*i*j for j in range(N)] for i in range(N)], dtype=np.int64)
    E = np.array([[1+2*i+7*j+i*j*j for j in range(N)] for i in range(N)], dtype=np.int64)
    MC, MD = M(C), M(D)
    eq(MC[:N+1, :N+1], elev(C, p), p)
    eq(M(C@D % p), MC@MD, p)
    defect = (elev(C@D % p, p)-elev(C, p)@elev(D, p)) % p
    eq(defect, MC[:N+1, N+1:]@MD[N+1:, :N+1], p)
    eq(M(E@D@C % p), M(E)@MD@MC, p)

    # Actual whole head and actual whole upper Fr arrow gauges.
    d = [1]
    for j in range(N-1):
        edge = (1-pow(Q.x, j+1, p)) % p
        d.append(d[-1]*(j+1)*pow(edge, -1, p) % p)
    b = [1]
    for j in range(N):
        b.append(b[-1]*beta[j, min(1, N-1)].x*pow(j+1, -1, p) % p)
    dg = np.diag(d)
    di = np.diag([pow(x, -1, p) for x in d])
    bg = np.diag(b+[1]*(N-1))
    bi = np.diag([pow(x, -1, p) for x in b]+[1]*(N-1))
    G = bg@Si@np.kron(dg, eye2)@S % p
    Gi = Si@np.kron(di, eye2)@S@bi % p
    eq(G@Gi, np.eye(2*N, dtype=np.int64), p)

    def T(C):
        return G@M(C)@Gi % p

    upperpsi = np.array([1]*(N+1)+[0]*(N-1), dtype=np.int64)
    upperphi = np.array([pow(N+1, -1, p)]*(N+1)+[0]*(N-1), dtype=np.int64)
    psi, phi = G@upperpsi % p, upperphi@Gi % p
    word = E@D@C % p
    selected = int(phi@T(E)@T(D)@T(C)@psi) % p
    assert selected == int(word.sum())*pow(N, -1, p) % p
    assert int(phi@psi) % p == 1
    # Literal represented pivot/marked-defect relation and explicit 1/2.
    kh = [pow(q.x, N-1, p)*pow(Q.x, -j, p) % p for j in range(N)]
    pivot = np.diag([pow(k, 1-N, p) for k in kh])
    pi = np.diag([pow(int(pivot[j, j]), -1, p) for j in range(N)])
    coupon = np.ones((N, N), dtype=np.int64)*pow(N, -1, p) % p
    marked = pi@coupon % p
    eq(T(pivot)@T(marked), T(coupon), p)
    assert int(np.trace(T(coupon)@T(word)))*pow(2, -1, p) % p == selected
    assert int(np.trace(T(coupon))) % p == 2

    # Every retained Green moment has the auxiliary bit offset.
    Jh = np.diag(np.arange(N, dtype=np.int64))
    aux = np.kron(np.eye(N, dtype=np.int64), np.diag([0, 1]))
    At = Si@aux@S % p
    Jtotal = np.diag(list(range(N+1))+list(range(1, N)))
    eq(M(Jh), Jtotal-At, p)
    for h in range(5):
        eq(M(np.diag([j**h for j in range(N)])),
           np.linalg.matrix_power((Jtotal-At) % p, h), p)
    for w in (2, 3):
        clock = np.diag([pow(w, j, p) for j in range(N)])
        totalclock = np.diag([pow(w, j, p) for j in list(range(N+1))+list(range(1, N))])
        eq(M(clock), totalclock@(np.eye(2*N, dtype=np.int64)+(pow(w, -1, p)-1)*At), p)
        E1 = np.zeros((N+1, N+1), dtype=np.int64)
        for i in range(1, N+1):
            for j in range(1, N+1):
                E1[i, j] = i*int(C[i-1, j-1])*pow(N, -1, p) % p
        eq(elev(clock@C % p, p),
           totalclock[:N+1, :N+1]@(elev(C, p)+(pow(w, -1, p)-1)*E1), p)
    return {"N": N, "prime": p, "full_memory": 2*N,
            "upper": N+1, "lower": N-1, "whole_source": True}


def lift_two_head(R, N):
    out = np.zeros(((2*N)**2, (2*N)**2), dtype=np.int64)
    for row, col in zip(*np.nonzero(R)):
        i, j = divmod(int(row), N)
        k, l = divmod(int(col), N)
        for a in range(2):
            for b in range(2):
                out[(2*i+a)*(2*N)+2*j+b, (2*k+a)*(2*N)+2*l+b] = R[row, col]
    return out


def actual_crossing(N):
    p, m, coefficient = setup(N, 0)
    _, eta = root_field(N)
    q = pow(eta, 2, p)
    S, Si, *_ = cg(N, p)
    R = np.zeros((N*N, N*N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            for k in range(min(i, N-1-j)+1):
                R[(i-k)*N+j+k, i*N+j] = coefficient(i, j, k).x
    Ri = np.array(sp.Matrix(R.tolist()).inv_mod(p)).astype(np.int64)
    st, sti = np.kron(S, S), np.kron(Si, Si)
    full = sti@lift_two_head(R, N)@st % p
    inverse = sti@lift_two_head(Ri, N)@st % p
    eq(inverse@full, np.eye((2*N)**2, dtype=np.int64), p)
    upper = [i*(2*N)+j for i in range(N+1) for j in range(N+1)]
    other = [i for i in range((2*N)**2) if i not in upper]
    up, ui = full[np.ix_(upper, upper)], inverse[np.ix_(upper, upper)]
    product = ui@up % p
    excursion = inverse[np.ix_(upper, other)]@full[np.ix_(other, upper)] % p
    eq(np.eye((N+1)**2, dtype=np.int64)-product, excursion, p)
    leak = int(full[(N+1)*(2*N), 2*N])
    expected_leak = (N-1)*pow(N, -1, p)*pow(eta, (N-1)**2, p)*(pow(q, -(N-1), p)-1) % p
    assert leak == expected_leak and leak
    for j in range(N+1):
        expected = 1+j*(N-j)*pow(N*N, -1, p)*(pow(q, N-1, p)+pow(q, -(N-1), p)-2)
        assert int(product[j*(N+1), j*(N+1)]) == expected % p
    return {"N": N, "prime": p, "actual_nonzero_leak": leak,
            "inverse_pair_diagonals": N+1, "full_excursion_identity": True}


def main():
    words = [finite_word(N) for N in range(2, 9)]
    crossings = [actual_crossing(N) for N in range(2, 7)]
    result = {"status": "pass", "whole_words": words, "actual_R": crossings,
              "scope": "exact auxiliary memory/source; no actual-high-color or Gaussian equivalence"}
    path = Path(__file__).with_name("clebsch_memory_and_actual_r_excursions_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "whole_word_cases": len(words),
                      "actual_R_cases": len(crossings),
                      "actual_inverse_diagonals": sum(c["inverse_pair_diagonals"] for c in crossings),
                      "results": str(path)}, indent=2))


if __name__ == "__main__":
    main()
