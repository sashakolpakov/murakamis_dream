"""Two actual-coordinate matrix shifts, whole tails and coherent Green complex."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field


def clean(f, p):
    return {k: int(v) % p for k, v in f.items() if int(v) % p}


def add(f, g, p, scalar=1):
    out = dict(f)
    for k, v in g.items():
        out[k] = (out.get(k, 0)+scalar*v) % p
    return clean(out, p)


def scale(f, a, p):
    return clean({k: a*v for k, v in f.items()}, p)


def shift(f, a=0, b=0):
    return {(i-a, j-b): v for (i, j), v in f.items()}


def diff(f, axis, p):
    return add(shift(f, a=axis == 0, b=axis == 1), f, p, -1)


def project(f, axis, p):
    out = {}
    for (a, b), v in f.items():
        k = (0, b) if axis == 0 else (a, 0)
        out[k] = (out.get(k, 0)+v) % p
    return clean(out, p)


def primitive(f, axis, p):
    g = add(f, project(f, axis, p), p, -1)
    if not g:
        return {}
    out = {}
    other = sorted({k[1-axis] for k in g})
    for j in other:
        indices = [k[axis] for k in g if k[1-axis] == j]
        lo, hi = min(indices+[0]), max(indices+[0])
        for a in range(lo, hi+1):
            value = -sum(v for k, v in g.items() if k[1-axis] == j and k[axis] >= a)
            if value % p:
                out[(a, j) if axis == 0 else (j, a)] = value % p
    return out


def h0(f, p):
    return primitive(f, 0, p), project(primitive(f, 1, p), 0, p)


def h1(pair, p):
    return scale(primitive(pair[1], 0, p), -1, p)


def d1(pair, p):
    return add(diff(pair[0], 0, p), diff(pair[1], 1, p), p)


def d2(f, p):
    return diff(f, 1, p), scale(diff(f, 0, p), -1, p)


def window(f, N):
    return np.array([[f.get((a, b), 0) for b in range(N)] for a in range(N)], dtype=np.int64)


def kernel(f, x, y, p):
    return sum(v*pow(x, a, p)*pow(y, b, p) for (a, b), v in f.items()) % p


def case(N, root):
    p, eta = root_field(N)
    Q = pow(eta, 4, p) if root else int(sp.primitive_root(p))
    if not root:
        assert pow(Q, N, p) != 1
    invN = pow(N, -1, p)
    A = np.diag([pow(Q, a, p) for a in range(N)])
    U = np.zeros((N, N), dtype=np.int64)
    for a in range(N-1):
        U[a+1, a] = 1
    Iarray = {(a, a): 1 for a in range(N)}
    anchor = {(0, 0): N}
    gamma = h0(add(Iarray, anchor, p, -1), p)
    units = 0
    for a in range(-1, N+1):
        for b in range(-1, N+1):
            f = {(a, b): 1}
            J = window(f, N)
            for eps in (1, -1):
                L, R = (U.T, U) if eps == 1 else (U, U.T)
                endpoint, outside = (N-1, N) if eps == 1 else (0, -1)
                row = np.array([f.get((outside, j), 0) for j in range(N)])
                col = np.array([f.get((i, outside), 0) for i in range(N)])
                erow, ecol = np.zeros_like(J), np.zeros_like(J)
                erow[endpoint, :], ecol[:, endpoint] = row, col
                assert np.array_equal(window(shift(f, a=eps), N), L@J+erow)
                assert np.array_equal(window(shift(f, b=eps), N), J@R+ecol)
                oldrow = 0 if eps == 1 else N-1
                delta_a = int((window(shift(f, a=eps), N)-J).sum())*invN % p
                delta_b = int((window(shift(f, b=eps), N)-J).sum())*invN % p
                assert delta_a == sum(f.get((outside, j), 0)-f.get((oldrow, j), 0) for j in range(N))*invN % p
                assert delta_b == sum(f.get((i, outside), 0)-f.get((i, oldrow), 0) for i in range(N))*invN % p
                for eta_sign in (1, -1):
                    Rb = U if eta_sign == 1 else U.T
                    endb, outb = (N-1, N) if eta_sign == 1 else (0, -1)
                    cb = np.array([f.get((i, outb), 0) for i in range(N)])
                    mixed = L@J@Rb
                    mixed[endpoint, :] += row@Rb
                    mixed[:, endb] += L@cb
                    mixed[endpoint, endb] += f.get((outside, outb), 0)
                    assert np.array_equal(window(shift(f, eps, eta_sign), N), mixed)
            # Physical clocks, whole endpoint powers and ordered Weyl relation.
            ca = clean({(i, j): pow(Q, i, p)*v for (i, j), v in f.items()}, p)
            cb = clean({(i, j): pow(Q, j, p)*v for (i, j), v in f.items()}, p)
            assert np.array_equal(window(ca, N), A@J % p)
            assert np.array_equal(window(cb, N), J@A % p)
            for axis in (0, 1):
                shifted_clock = shift(ca if axis == 0 else cb, a=axis == 0, b=axis == 1)
                sf = shift(f, a=axis == 0, b=axis == 1)
                clock_shifted = clean({(i, j): pow(Q, i if axis == 0 else j, p)*v for (i, j), v in sf.items()}, p)
                assert clean(shifted_clock, p) == scale(clock_shifted, Q, p)
            # Full two-current contraction, including the original 1/N section.
            expected = add(f, {(0, 0): 1}, p, -1)
            assert d1(h0(f, p), p) == expected
            assert h1(d2(f, p), p) == f
            for pair in ((f, {}), ({}, f)):
                x, y = h0(d1(pair, p), p), d2(h1(pair, p), p)
                assert add(x[0], y[0], p) == pair[0]
                assert add(x[1], y[1], p) == pair[1]
            physical_h = tuple(add(x, g, p, -invN) for x, g in zip(h0(f, p), gamma))
            assert d1(physical_h, p) == add(f, Iarray, p, -invN)
            for x, y in ((2, 3), (3, 5)):
                assert kernel(shift(f, 1, -1), x, y, p) == pow(x, -1, p)*y*kernel(f, x, y, p) % p
                assert kernel(ca, x, y, p) == kernel(f, Q*x % p, y, p)
                assert kernel(cb, x, y, p) == kernel(f, x, Q*y % p, p)
            units += 1
    # Actual two-cut identity bookkeeping and original source normalization.
    assert int(window(Iarray, N).sum())*invN % p == 1
    # Restricting to row sums really loses the independent second clock.
    lost = np.zeros((N, N), dtype=np.int64)
    lost[0, 0], lost[0, 1] = 1, -1
    assert not lost.sum(axis=1).any()
    assert (lost@A % p).sum(axis=1).any()
    return {"N": N, "root": root, "matrix_and_tail_units": units,
            "qN_retained": pow(Q, N, p)}


def symbolic_source():
    x, y, z, w = sp.symbols("x y z w")
    f = {(-1, 0): 2, (0, 1): 3, (2, -1): -1, (3, 2): 5}
    F = sum(v*x**a*y**b for (a, b), v in f.items())
    value = sp.residue(sp.residue(F/((x-1)*(y-1)), x, 1), y, 1)
    assert value == sum(f.values())
    N = 4
    C = sp.Matrix(N, N, lambda i, j: 1+2*i+3*j+i*j)
    D = sp.Matrix(N, N, lambda i, j: 2+i+j*j)
    psi = sum(w**j for j in range(N))
    K = sum(C[i, j]*z**i*w**(-j-1) for i in range(N) for j in range(N))
    assert sp.residue(K.subs(z, 1)*psi, w, 0)/N == sum(C)/N
    u = sp.Symbol("u")
    KC = sum(C[i, j]*z**i*u**(-j-1) for i in range(N) for j in range(N))
    KD = sum(D[i, j]*u**i*w**(-j-1) for i in range(N) for j in range(N))
    composed = sp.expand(sp.residue(KC*KD, u, 0))
    assert sp.expand(composed-sum((C*D)[i, j]*z**i*w**(-j-1) for i in range(N) for j in range(N))) == 0
    eta, s = sp.symbols("eta s")
    bandF = 2/eta+3+5*eta**2
    theta = bandF/eta
    transpose_theta = bandF.subs(eta, 1/eta)/eta
    natural_pullback = theta.subs(eta, 1/eta)*(-eta**-2)
    assert sp.simplify(natural_pullback+transpose_theta) == 0
    assert sp.residue(theta, eta, 0) == 3
    assert -sp.residue(theta.subs(eta, 1/s)/s**2, s, 0) == -3
    return {"double_residue": True, "literal_Serre_source": True,
            "kernel_composition": True, "identity_cut_residue_sign": True}


def band_case(N, root):
    p, eta = root_field(N)
    q = pow(eta, 2, p) if root else int(sp.primitive_root(p))

    def involution(f):
        return {(a+mu, b+nu, -mu, -nu): value
                for (a, b, mu, nu), value in f.items()}

    def source(f):
        return sum(v for (a, b, mu, nu), v in f.items() if nu == 0)*pow(N, -1, p) % p

    def evaluate(f, x, y, xi, en):
        return sum(v*pow(x, a, p)*pow(y, b, p)*pow(xi, mu, p)*pow(en, nu, p)
                   for (a, b, mu, nu), v in f.items()) % p

    count = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    mu, nu = c-a, d-b
                    f = {(a, b, mu, nu): 1}
                    tf = involution(f)
                    assert involution(tf) == f
                    assert source(tf) == source(f)
                    for axis in (0, 1):
                        exponent = 2*(a if axis == 0 else b)+(mu if axis == 0 else nu)
                        cf = {k: pow(q, exponent, p) for k in f}
                        ctf = {k: pow(q, 2*(k[0] if axis == 0 else k[1])+(k[2] if axis == 0 else k[3]), p)
                               for k in tf}
                        assert involution(cf) == ctf
                    x, y, xi, en = 2, 3, 5, 7
                    assert evaluate(tf, x, y, xi, en) == evaluate(f, x, y, x*pow(xi, -1, p) % p, y*pow(en, -1, p) % p)
                    shifted = {(a-1, b+1, mu, nu): 1}
                    expected = {(aa-1, bb+1, mm, nn): v for (aa, bb, mm, nn), v in tf.items()}
                    assert involution(shifted) == expected
                    count += 1
    return {"N": N, "root": root, "physical_port_units": count}


def main():
    cases = [case(N, root) for N in range(2, 9) for root in (False, True)]
    bands = [band_case(N, root) for N in range(2, 6) for root in (False, True)]
    result = {"status": "pass", "cases": cases, "global_source": symbolic_source(),
              "band_involution": bands,
              "scope": "exact two-coordinate Green/source map; no single-port Hopf or Gaussian descent"}
    path = Path(__file__).with_name("two_cut_matrix_green_and_coherent_source_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "cases": len(cases),
                      "matrix_and_tail_units": sum(c["matrix_and_tail_units"] for c in cases),
                      "physical_band_units": sum(c["physical_port_units"] for c in bands),
                      "results": str(path)}, indent=2))


if __name__ == "__main__":
    main()
