#!/usr/bin/env python3
"""Exact marked cap-cover identity on literal actual signed braid tensors.

No selected Gaussian or knot-volume comparison is inferred.  Actual matrices
come from the independently retained half-Cartan/pivot/framing source model.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, embed, partial, word_matrix


def clean(poly, p):
    return {int(k): int(v) % p for k, v in poly.items() if int(v) % p}


def orientation(poly, p):
    out = {}
    for n, value in poly.items():
        out[n+1] = (out.get(n+1, 0)+value) % p
        out[n-1] = (out.get(n-1, 0)-value) % p
    return clean(out, p)


def marked_source(poly, N, p):
    # These are the full odd negative coefficients, not just the nearest band.
    return -sum(v for n, v in poly.items() if n < 0 and n % 2) * pow(N, -1, p) % p


def verify_coefficients(poly, N, p):
    poly = clean(poly, p)
    odd = orientation(poly, p)
    expected = poly.get(0, 0)*pow(N, -1, p) % p
    assert marked_source(odd, N, p) == expected
    largest = max((abs(n) for n in poly), default=0)
    for K in range(largest+2):
        partial_sum = -sum(odd.get(-2*k-1, 0) for k in range(K+1))*pow(N, -1, p) % p
        assert partial_sum == (poly.get(0, 0)-poly.get(-2*K-2, 0))*pow(N, -1, p) % p
    # Euler clock derivatives have zero original and transported cap residues.
    for order in range(1, 5):
        derivative = clean({n: pow(n, order, p)*v for n, v in poly.items()}, p)
        assert marked_source(orientation(derivative, p), N, p) == 0
    return expected


def kernel(T, p, x=1, y=1, xi=1):
    N = T.shape[0]
    out = {}
    for c, d, a, b in itertools.product(range(N), repeat=4):
        value = int(T[c, d, a, b])
        if value:
            n = d-b
            value = value*pow(x, a, p)*pow(y, b, p)*pow(xi, c-a, p) % p
            out[n] = (out.get(n, 0)+value) % p
    return clean(out, p)


def tensor_source(T, N, p, x=1, y=1, xi=1):
    return sum(int(T[c, b, a, b])*pow(x, a, p)*pow(y, b, p)*pow(xi, c-a, p)
               for c, a, b in itertools.product(range(N), repeat=3))*pow(N, -1, p) % p


def actual_tensor(N, strands, word, split, slot):
    p, eta, q, _, _, _, pivot, plus, minus = balanced_data(N)
    A = word_matrix(word[split:], plus, minus, strands, N, p)
    B = word_matrix(word[:split], plus, minus, strands, N, p)
    writhe = sum(1 if x > 0 else -1 for x in word)
    m, imag = N-1, pow(eta, N, p)
    # Literal external line from the actual two-cut tensor implementation.
    external = pow(eta, -writhe*m*(m+2), p)*pow(imag, N+3, p)*pow(N, -1, p) % p
    T = np.zeros((N, N, N, N), dtype=np.int64)
    for b, d in itertools.product(range(N), repeat=2):
        coupon = np.zeros((N, N), dtype=np.int64)
        coupon[b, d] = 1
        X = embed(coupon, slot, strands, N)
        T[:, d, :, b] = external*partial(A@X@B % p, pivot, strands, N, p) % p
    closed = external*partial(A@B % p, pivot, strands, N, p) % p
    assert np.array_equal(closed, sum((T[:, b, :, b] for b in range(N)), np.zeros_like(closed)) % p)
    return p, q, T


def whole_clock_checks(T, N, p, Q):
    # All four port clocks are checked on the full array, not only its diagonal.
    x, y, xi = 2, 3, 5
    arrays = [np.zeros_like(T) for _ in range(4)]
    for c, d, a, b in itertools.product(range(N), repeat=4):
        for target, exponent in zip(arrays, (a, b, c, d)):
            target[c, d, a, b] = int(T[c, d, a, b])*pow(Q, exponent, p) % p
    expected = [kernel(T, p, Q*x % p, y, xi), kernel(T, p, x, Q*y % p, xi),
                kernel(T, p, Q*x % p, y, Q*xi % p),
                clean({n: value*pow(Q, n, p) for n, value in kernel(T, p, x, Q*y % p, xi).items()}, p)]
    for actual, target in zip(arrays, expected):
        assert kernel(actual, p, x, y, xi) == target
        verify_coefficients(kernel(actual, p, x, y, xi), N, p)
    # Clock eta -> r eta is literally a paired output/input second-port clock.
    for r in (2, 3, 5):
        direct = np.zeros_like(T)
        for c, d, a, b in itertools.product(range(N), repeat=4):
            direct[c, d, a, b] = int(T[c, d, a, b])*pow(r, d-b, p) % p
        poly = kernel(T, p, x, y, xi)
        rescaled = clean({n: value*pow(r, n, p) for n, value in poly.items()}, p)
        assert kernel(direct, p, x, y, xi) == rescaled
        verify_coefficients(rescaled, N, p)
    # Independent input couplings and their finite Euler moments remain whole.
    for order in range(4):
        weighted = np.zeros_like(T)
        for c, d, a, b in itertools.product(range(N), repeat=4):
            weighted[c, d, a, b] = int(T[c, d, a, b])*pow(a+2*b, order, p) % p
        poly = kernel(weighted, p, x, y, xi)
        assert verify_coefficients(poly, N, p) == tensor_source(weighted, N, p, x, y, xi)
    return 4+3+4


def actual_case(N, strands, word, split, slot):
    p, q, T = actual_tensor(N, strands, word, split, slot)
    Q = q*q % p
    couplings = [(1, 1, 1), (2, 3, 5), (3, 5, 2)]
    for x, y, xi in couplings:
        poly = kernel(T, p, x, y, xi)
        assert verify_coefficients(poly, N, p) == tensor_source(T, N, p, x, y, xi)
    checks = whole_clock_checks(T, N, p, Q)
    return {"N": N, "strands": strands, "word": list(word), "split": split,
            "second_cut_slot": slot, "whole_coupling_and_clock_checks": checks,
            "original_pivot_halfCartan_framing_peripheral_lines_retained": True,
            "all_bands_and_finite_residue_endpoint_retained": True}


def unknot_and_units(N):
    p, _, q, *_ = balanced_data(N)
    Q = q*q % p
    T = np.zeros((N, N, N, N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        T[b, a, a, b] = 1
    poly = kernel(T, p)
    assert poly == {j: N-abs(j) for j in range(-(N-1), N)}
    G = orientation(poly, p)
    assert verify_coefficients(poly, N, p) == 1
    assert G.get(0, 0) == 0
    assert -G.get(-1, 0)*pow(N, -1, p) % p == 2*pow(N, -1, p) % p
    units = 0
    for c, d, a, b in itertools.product(range(N), repeat=4):
        F = {d-b: 1}
        result = verify_coefficients(F, N, p)
        assert result == (pow(N, -1, p) if d == b else 0)
        units += 1
    whole_clock_checks(T, N, p, Q)
    return {"N": N, "literal_unknot_cap": 1, "nearest_term_only": f"2/{N}",
            "omitted_tail": f"({N}-2)/{N}", "all_port_matrix_units": units}


def symbolic_forms():
    eta, r, N = sp.symbols("eta r N", nonzero=True)
    u, v = eta+1/eta, eta-1/eta
    assert sp.cancel(v*sp.diff(u, eta)/v**2-1/eta) == 0
    assert sp.cancel(sp.diff(u, eta)/v**2-1/(eta**2-1)) == 0
    ur = (r+1/r)*u/2+(r-1/r)*v/2
    vr = (r-1/r)*u/2+(r+1/r)*v/2
    assert sp.cancel(ur-r*eta-1/(r*eta)) == 0
    assert sp.cancel(vr-r*eta+1/(r*eta)) == 0
    assert sp.cancel(ur**2-vr**2-4) == 0
    assert sp.cancel(sp.diff(ur, eta)/vr-1/eta) == 0
    for exponent in range(-8, 9):
        F = eta**exponent
        G = v*F
        DG = eta*sp.diff(G, eta)-u/v*G
        assert sp.cancel(DG-v*eta*sp.diff(F, eta)) == 0
        assert sp.cancel(DG*sp.diff(u, eta)/v**2-sp.diff(G/v, eta)) == 0
        assert sp.cancel(v/vr*((r*eta-1/(r*eta))*(r*eta)**exponent)-v*(r*eta)**exponent) == 0
    # On the marked sheet t=1/u has ramification index one and positive sign.
    t = eta/(1+eta**2)
    assert sp.limit(t/eta, eta, 0) == 1
    assert sp.limit(v/u, eta, 0) == -1
    local_t = sp.Symbol("t")
    inverse_u = 1/local_t
    assert sp.residue(-sp.diff(inverse_u, local_t)/(N*inverse_u), local_t, 0) == 1/N
    assert sp.residue(sp.diff(inverse_u, local_t)/(N*inverse_u), local_t, 0) == -1/N
    # Principal prefix boundary, with all signs and its rational Jacobian.
    s, A0, A1 = sp.symbols("s A0 A1", nonzero=True)
    for sigma in (1, -1):
        k = (s*u+sigma*A0)/(s*u+sigma*A1)
        D = -sigma*s*(k-1)*v
        assert sp.simplify(sp.limit(D, eta, 0)-A0+A1) == 0
        assert sp.simplify(sp.limit(D, eta, sp.oo)-A1+A0) == 0
        jacobian = (k-1)/(A1-A0)
        assert sp.simplify(sp.limit(jacobian/eta, eta, 0)+sigma/s) == 0
        assert sp.residue(jacobian/eta, eta, 0) == 0
    # The actual three-strand figure-eight representation and its third prefix.
    shape = (-1+sp.sqrt(3)*sp.I)/2
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-shape, 1]])
    C = B*A.inv()*B*A*B.inv()
    V, U = B*A, C*B*A
    W = U-V
    cW = sp.simplify(W[1, 0])
    gap = sp.simplify(cW+sp.trace(W))
    r_boundary = sp.simplify((cW+W[0, 0]-W[1, 1]-gap)/(2*cW))
    ellV = sp.simplify(V[1, 1]+(V[0, 0]-V[1, 1])*r_boundary
                       +V[0, 1]+V[1, 0]*r_boundary*(1-r_boundary))
    assert cW == 1
    assert sp.simplify(gap-3-shape) == 0
    assert r_boundary == -2
    assert sp.simplify(ellV-2-3*shape) == 0
    return {"exact_form_and_clock_identities": True, "symbolic_euler_monomials": 17,
            "marked_sheet_uniformizer_order": 1, "marked_infinity_residue_sign": "+1/N",
            "principal_prefix_boundary_zero_residue_both_parities": True,
            "actual_figure_eight_prefix_boundary_exact": True}


def main():
    symbolic = symbolic_forms()
    cases = []
    for N in range(2, 8):
        for word, split in [((1,), 0), ((-1,), 0), ((1, 1, -1), 1)]:
            cases.append(actual_case(N, 2, word, split, 1))
    for N in range(2, 5):
        cases.append(actual_case(N, 3, (1, -2, 1, -2), 2, 2))
    ports = [unknot_and_units(N) for N in range(2, 9)]
    result = {"status": "pass", "symbolic": symbolic, "actual_signed_tensors": cases,
              "literal_unknot_and_all_port_units": ports,
              "scope": "Exact source-preserving orientation cover with whole clocks and finite tails; no whole geometric Gaussian/source identification or asymptotic claim."}
    output = Path(__file__).with_name("identity_cut_orientation_cover_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_signed_tensor_cases": len(cases),
                      "unknot_levels": len(ports),
                      "all_port_matrix_units": sum(item["all_port_matrix_units"] for item in ports),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
