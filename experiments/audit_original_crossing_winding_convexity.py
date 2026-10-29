#!/usr/bin/env python3
"""Exact crossing/source checks for original charged-simplex convexity.

Finite fields verify identities, not inequalities. The concavity proof is
in the accompanying note; the sampled Hessians are diagnostics only.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_kashaev_crossing import original


def corners(n, a, b, c, d):
    return ((b - a - 1) % n, (a - c) % n,
            (c - d) % n, (d - b) % n)


def exact_case(n):
    p = next(4*n*k+1 for k in range(1, 1000)
             if sp.isprime(4*n*k+1))
    primitive = int(sp.primitive_root(p))
    q = pow(primitive, (p-1)//n, p)
    r, printed, fs = original(n, p, q)
    rc, _, _ = original(n, p, pow(q, -1, p))
    swap = np.zeros((n*n, n*n), dtype=np.int64)
    for a, b in product(range(n), repeat=2):
        swap[b*n+a, a*n+b] = 1
    bp = swap @ r.T % p
    bm = printed.T @ swap * pow(q, -1, p) % p
    bc = swap @ rc.T % p
    bars = [1]
    for j in range(1, n):
        bars.append(bars[-1]*(1-pow(q, -j, p)) % p)
    checked = nonzero = 0
    for a, b, c, d in product(range(n), repeat=4):
        u, v, t, h = corners(n, a, b, c, d)
        row, col = c*n+d, a*n+b
        supported = u+v+t+h == n-1
        assert bool(bp[row, col]) == supported
        assert bool(bm[row, col]) == supported
        if supported:
            denominator = fs[u]*bars[v]*fs[t]*bars[h] % p
            predicted = n*pow(q, 1-(t+h)*(u+h), p)
            predicted = predicted*pow(denominator, -1, p) % p
            assert int(bp[row, col]) == predicted
            nonzero += 1
        assert int(bm[row, col]) == (
            pow(q, c+d-a-b, p)*int(bc[row, col]) % p)
        checked += 1
    return {"N": n, "prime": p, "entries": checked,
            "supported_entries": nonzero, "all_identities": True}


def complex_crossing(n):
    q = np.exp(2j*np.pi/n)
    fs = np.ones(n, dtype=complex)
    for j in range(1, n):
        fs[j] = fs[j-1]*(1-q**j)
    bp = np.zeros((n*n, n*n), dtype=complex)
    for a, b, c, d in product(range(n), repeat=4):
        u, v, t, h = corners(n, a, b, c, d)
        if u+v+t+h != n-1:
            continue
        entry = (n*q**(1-(t+h)*(u+h)) /
                 (fs[u]*fs[v].conjugate()*fs[t]*fs[h].conjugate()))
        bp[c*n+d, a*n+b] = entry
        au, av, at, ah = np.array((u, v, t, h), dtype=float)/n
        quadratic = au*au+at*at-av*av-ah*ah
        linear = au+at-av-ah
        phase = -2*np.pi*(at+ah)*(au+ah)-np.pi*quadratic/2+np.pi*linear/2
        predicted = abs(entry)*np.exp(1j*n*phase-1j*np.pi*linear/2+2j*np.pi/n)
        assert np.isclose(entry, predicted, rtol=3e-11, atol=3e-11)
    diagonal = np.array([q**(a+b) for a, b in product(range(n), repeat=2)])
    bm = diagonal[:, None]*bp.conjugate()/diagonal[None, :]
    assert np.allclose(bp@bm, np.eye(n*n), atol=2e-10, rtol=2e-10)
    return bp, bm, fs


def closed_value(n, signs, bp, bm, absolute=False):
    one = np.eye(n)
    w = np.eye(n**3, dtype=complex)
    for position, sign in zip((0, 1, 0, 1), signs):
        local = bp if sign == 1 else bm
        if absolute:
            local = abs(local)
        embedded = np.kron(local, one) if position == 0 else np.kron(one, local)
        w = embedded @ w
    shift = np.roll(one, 1, axis=0)
    scalar = 1 if absolute else -np.exp(1j*np.pi/n)
    pivotal = np.kron(one, np.kron(scalar*shift, scalar*shift))
    closed = (w@pivotal).reshape((n,)*6)
    value = sum(closed[0, a, b, 0, a, b] for a, b in product(range(n), repeat=2))
    return value if absolute else scalar**(-sum(signs))*value


def whole_case(n):
    bp, bm, fs = complex_crossing(n)
    signs_t = (1, 1, 1, 1)
    signs_f = (1, -1, 1, -1)
    kt = closed_value(n, signs_t, bp, bm)
    kf = closed_value(n, signs_f, bp, bm)
    at = closed_value(n, signs_t, bp, bm, True)
    af = closed_value(n, signs_f, bp, bm, True)
    known_f = float(sum(abs(fs)**2))
    assert abs(at.imag) < 1e-8 and at.real > 0
    assert np.isclose(at, af, rtol=1e-10, atol=1e-10)
    assert np.isclose(kf, known_f, rtol=3e-9, atol=3e-9)
    assert not np.isclose(kt, kf, rtol=1e-7, atol=1e-7)
    return {"N": n, "figure_eight": [float(kf.real), float(kf.imag)],
            "trefoil": [float(kt.real), float(kt.imag)],
            "common_absolute_state_sum": float(at.real),
            "actual_source_and_normalization": True}


def concavity_diagnostic():
    rng = np.random.default_rng(288174)
    smallest = float("inf")
    for k in (3, 4):
        for _ in range(1000):
            angles = np.pi*rng.dirichlet(np.ones(k))
            cot = 1/np.tan(angles)
            h = np.diag(cot[:-1])+cot[-1]*np.ones((k-1, k-1))
            eigenvalue = float(np.linalg.eigvalsh(h)[0])
            assert eigenvalue > -1e-9
            smallest = min(smallest, eigenvalue)
    return {"sampled_simplex_hessians": 2000,
            "smallest_sampled_eigenvalue": smallest,
            "scope": "diagnostic; all-angle proof uses cotangent/Cauchy inequality"}


def main():
    result = {"exact": [exact_case(n) for n in (2, 3, 4, 5, 6, 8, 9)],
              "whole_original_sources": [whole_case(n) for n in (2, 3, 4, 5, 6)],
              "concavity": concavity_diagnostic()}
    target = Path(__file__).with_name("original_crossing_winding_convexity_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "exact_levels": len(result["exact"]),
                      "whole_source_pairs": len(result["whole_original_sources"]),
                      "result": str(target)}))


if __name__ == "__main__":
    main()
