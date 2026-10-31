#!/usr/bin/env python3
"""Exact original physical source versus all actual MAIN two-zero targets.

Finite normalization checks, not a proof of spherical rerouting or any
asymptotic. The source matrices and the homogeneous face construction are
built separately. No optimizer, spectral limit or projected sector occurs.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np

SOURCE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SOURCE_DIR))
from audit_actual_small_circle_polynomial_face_insertion import Local, physical_colors, T
from audit_actual_original_marked_face_coefficient import morse_faces, mul, add, substitute
from audit_actual_braided_two_cut_source_adapter import original_crossings
from research_audit_arbitrary_casimir_top_mark_transport import chi, numerator
from original_source_tensor import apply_pair


def omega_poly(P, loc):
    return {v: -a % loc.p for v, a in T(P, 0, 2, 3, loc).items()}


def source_base(loc, epsilon):
    N, d, p, q = loc.N, loc.d, loc.p, loc.q
    if not epsilon:
        return {(0, i, d-i, 0): 1 for i in range(N)}
    imag = pow(loc.eta, N, p)
    sine = [pow(imag, j, p) * pow(q, -j*(j+1)//2, p) * loc.fac[j] % p
            for j in range(N)]
    # eta^2=q, retaining the actual q^(d^2/2) crossing scalar.
    assert pow(loc.eta, 2, p) == q
    scalar = pow(loc.eta, epsilon*d*d, p)
    H = {}
    for i in range(N):
        for k in range(N-i):
            for ell in range(N-i-k):
                t = d-i-k-ell
                coeff = (scalar * (-1)**(k+ell+1) *
                         pow(q, epsilon*(k*ell-(i+1)*(t+1)), p) * N *
                         pow(sine[i]*sine[k]*sine[ell]*sine[t] % p, -1, p)) % p
                H[(k, i, t, ell)] = coeff
    return H


def divided_coefficients(N, sigma, p):
    coefficients = [0] * N
    for degree, value in enumerate(chi(N)):
        for j in range(degree):
            coefficients[j] = (coefficients[j] + value*pow(sigma, degree-1-j, p)) % p
    return coefficients


def homogeneous_coupon(loc, epsilon, coefficients):
    H = source_base(loc, epsilon)
    out = {}
    for j, value in enumerate(coefficients):
        if value:
            out = add(out, H, loc.p, value)
        if j+1 < len(coefficients):
            H = omega_poly(H, loc)
    assert all(sum(v) == loc.d and min(v) >= 0 for v in out)
    return out


def target_value(chart, local, edge, d, p):
    ordinary = [f for f in range(chart['faces']) if f not in edge]
    position = {f: i for i, f in enumerate(ordinary)}
    value = {(0,)*len(ordinary): 1}
    for H, quartet in zip(local, chart['circles']):
        reduced = {}
        for powers, coefficient in H.items():
            if any(e and f in edge for f, e in zip(quartet, powers)):
                continue
            exponent = [0]*len(ordinary)
            for f, e in zip(quartet, powers):
                if e:
                    exponent[position[f]] += e
            exponent = tuple(exponent)
            if max(exponent, default=0) <= d:
                reduced[exponent] = (reduced.get(exponent, 0)+coefficient) % p
        value = mul(value, reduced, p, cap=d)
    return int(value.get((d,)*len(ordinary), 0))


def run(N, k, slots, variant):
    loc = Local(N)
    p, d = loc.p, loc.d
    chart = morse_faces(k, slots, 0)
    O = -physical_colors(loc)[2] % p
    I = np.eye(N*N, dtype=np.int64)
    rp, rq, _, crossings = original_crossings(N)
    assert (rp, rq) == (p, loc.q)
    assert 16*N*N*p**3 < np.iinfo(np.int64).max
    assert N**(2*k)*p*p < np.iinfo(np.int64).max
    operators, local, epsilons = [], [], []
    for j in range(len(slots)):
        epsilon = (0, 1, -1)[j % 3]
        epsilons.append(epsilon)
        if variant == 0:
            sigma = (2, -2, 0, 3)[j % 4]
            F = numerator(O, sigma, N, p)
            coefficients = divided_coefficients(N, sigma, p)
        else:
            coefficients = [3, 7+j, 11]
            F = (3*I+(7+j)*O+11*(O@O % p)) % p
        if epsilon:
            F = F @ crossings[0 if epsilon > 0 else 1][0] % p
        operators.append(F)
        local.append(homogeneous_coupon(loc, epsilon, coefficients))
    state = np.array([1], dtype=np.int64)
    for _ in range(k):
        state = np.kron(state, loc.cup[0].reshape(-1)) % p
    state = state.reshape((N,)*(2*k))
    for slot, operator in zip(slots, operators):
        state = apply_pair(operator, state, slot, N, p)
    marker = np.array([[pow(loc.x, j, p)*pow(N*N, -1, p) % p
                        for j in range(N)] for i in range(N)], dtype=np.int64)
    closure = np.array([1], dtype=np.int64)
    for j in range(k):
        closure = np.kron(closure, (marker if j == 0 else loc.cap[0]).reshape(-1)) % p
    actual = int(closure @ state.reshape(-1) % p)
    edges = set()
    for x, b, c, y in chart['circles']:
        edges.update(tuple(sorted(e)) for e in [(x,b),(b,y),(x,c),(c,y)])
    assert all(a != b for a, b in edges)
    values = []
    for edge in sorted(edges):
        got = target_value(chart, local, edge, d, p)
        assert got == actual, (N, k, slots, variant, edge, got, actual)
        values.append({'edge': list(edge), 'coefficient': got})
    return dict(N=N, width=k, slots=slots, variant=variant,
                retained_half_twists=epsilons, field=p, physical_top_scalar=actual,
                main_pair_coefficients=values, nonzero=bool(actual))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name("research_arbitrary_main_edge_mark_transport_results.json"))
    args = parser.parse_args()
    cases = []
    for k, slots, levels in [(2, [1,2,1], range(3,7)),
                             (2, [1,0,2,1], range(3,7)),
                             (3, [1,3,2,4,1,3], (3,4))]:
        for N in levels:
            for variant in range(2):
                cases.append(run(N, k, slots, variant))
    result = dict(status='PASS', cases=len(cases),
                  main_pair_coefficients=sum(len(r['main_pair_coefficients']) for r in cases),
                  nonzero_cases=sum(r['nonzero'] for r in cases),
                  even_cases=sum(r['N'] % 2 == 0 for r in cases),
                  odd_cases=sum(r['N'] % 2 == 1 for r in cases),
                  cases_detail=cases,
                  scope='Exact original matrices versus all original MAIN-pair protected-zero coefficients, full V and polynomial coupons with actual signed crossings. No projected-sector transport or asymptotic proof.')
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'cases_detail'}, indent=2))


if __name__ == '__main__':
    main()
