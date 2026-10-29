#!/usr/bin/env python3
"""Literal odd-pretzel turns, charge transfer, mixed circles and filling.

No colored-Jones substitution. All finite sources use the original
balanced R, cups, ordinary caps and the full unrestricted marked row.
"""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_crossing_circle_source_and_filling import (
    crossing_circle, ordinary_module, filling_coefficients, power,
)


def apply_pair(state, B, place, N, prime):
    moved = np.moveaxis(state, (place, place+1), (0, 1))
    shape = moved.shape
    moved = (B@moved.reshape(N*N, -1) % prime).reshape(shape)
    return np.moveaxis(moved, (0, 1), (place, place+1))


def literal_source(N, x, prime, boxes):
    s, d = len(boxes), N-1
    state = np.zeros((N,)*(2*s), dtype=np.int64)
    cap = np.zeros_like(state)
    for a in itertools.product(range(N), repeat=s):
        b = [d-a[(i+1) % s] for i in range(s)]
        st = tuple(t for pair in zip(a, b) for t in pair)
        state[st] = pow(N, s, prime)*pow(x, -b[-1]-sum(a[1:]), prime) % prime
    # The marked outer row has NO degree indicator. Its second index
    # remains independent until the genuine total-degree source cuts it.
    for c in itertools.product(range(N), repeat=s):
        for outer in range(N):
            out_d = [d-c[i+1] for i in range(s-1)]+[outer]
            st = tuple(t for pair in zip(c, out_d) for t in pair)
            cap[st] = pow(x, sum(out_d), prime)*pow(N, -s-1, prime) % prime
    for i, B in enumerate(boxes):
        state = apply_pair(state, B, 2*i, N, prime)
    full = int(np.dot(cap.ravel(), state.ravel())) % prime
    forced = 0
    for st in np.ndindex(state.shape):
        if st[0]+st[-1] == d:
            forced += int(cap[st])*int(state[st])
    assert full == forced % prime
    return full


def transfer_source(N, x, prime, boxes):
    s, d, total = len(boxes), N-1, 0
    for h in range(-d, d+1):
        ids = list(range(max(0, h), min(d, d+h)+1))
        value = np.eye(len(ids), dtype=np.int64)
        for B in boxes:
            M = np.array([[pow(x, -2*a+h, prime)*int(B[(a-h)*N+d-b+h, a*N+d-b]) % prime
                           for b in ids] for a in ids], dtype=np.int64)
            value = value@M % prime
        total += sum(pow(x, 2*a, prime)*int(value[i, i]) for i, a in enumerate(ids))
    return pow(x, (s-1)*d, prime)*pow(N, -1, prime)*total % prime


def one_component(s):
    n = 2*s
    matching = {}
    for a, b in [(0, n-1)]+[(2*i-1, 2*i) for i in range(1, s)]:
        matching[a], matching[b] = b, a
    swapped = lambda a: a ^ 1
    other = {swapped(a): swapped(b) for a, b in matching.items()}
    seen, components = set(), 0
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        components += 1
        while stack:
            a = stack.pop()
            if a in seen:
                continue
            seen.add(a)
            stack += [matching[a], other[a]]
    return components


def generic_literal_cases():
    rows = []
    for N, s in ((2, 3), (2, 5), (2, 7), (3, 3), (3, 5), (4, 3)):
        prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
        x = int(K[0, 0])
        rng = np.random.default_rng(152800+10*N+s)
        boxes = []
        for _ in range(s):
            B = np.zeros((N*N, N*N), dtype=np.int64)
            for a, b, c, e in itertools.product(range(N), repeat=4):
                if a+b == c+e:
                    B[c*N+e, a*N+b] = int(rng.integers(0, prime))
            boxes.append(B)
        assert transfer_source(N, x, prime, boxes) == literal_source(N, x, prime, boxes)
        rows.append({'N': N, 'boxes': s, 'generic_actual_integer_degree_source': True,
                     'full_marked_row_equals_forced_degree_only_after_contraction': True})
    return rows


def torus_sign_cases():
    rows = []
    for N in range(2, 10):
        p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
        d, x = N-1, int(K[0, 0])
        cup = np.array([N*pow(x, -b, p) % p if a+b == d else 0
                        for a in range(N) for b in range(N)], dtype=np.int64)
        ell = np.array([pow(x, a, p)*pow(N, -1, p) % p if a+b == d else 0
                        for a in range(N) for b in range(N)], dtype=np.int64)
        mark = np.array([pow(x, b, p)*pow(N, -2, p) % p
                         for a in range(N) for b in range(N)], dtype=np.int64)
        for s in (3, 5, 7):
            state = np.kron(cup, cup).reshape((N,)*4)
            state = apply_pair(state, power(Rp, s, p), 1, N, p)
            actual_four_plat = int(np.dot(np.kron(ell, mark), state.ravel())) % p
            actual_pretzel = transfer_source(N, x, p, [Rm]*s)
            assert actual_pretzel == actual_four_plat
            rows.append({'N': N, 'odd_boxes': s,
                         'original_pretzel_single_crossing_matches_central_four_plat': True})
    return rows


def mixed_and_filled_cases():
    rows = []
    for N in range(2, 6):
        p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
        d, x, kappa = N-1, int(K[0, 0]), int(Rp[0, 0])
        Q = q*q % p
        target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
        loops = [crossing_circle(target, ordinary_module(j, q, p), q, eta, p, N)
                 for j in range(1, N+1)]
        colors = [N, max(1, N-1), 1]
        boxes = [Rm@loops[j-1] % p for j in colors]
        augmented = transfer_source(N, x, p, boxes)
        assert augmented == literal_source(N, x, p, boxes)
        slopes = [1, -2, 2]
        filled_boxes = [power(Rp, -(2*v+1), p, inverse=Rm) for v in slopes]
        original = transfer_source(N, x, p, filled_boxes)
        assert original == literal_source(N, x, p, filled_boxes)
        coeff = [filling_coefficients(N, q, Q, -2*v, p) for v in slopes]
        expansion = 0
        for j in itertools.product(range(N), repeat=3):
            weight = np.prod([coeff[i][j[i]] for i in range(3)], dtype=object) % p
            circle_boxes = [Rm@loops[j[i]] % p for i in range(3)]
            expansion += int(weight)*transfer_source(N, x, p, circle_boxes)
        expansion = expansion*pow(kappa, -2*sum(slopes), p) % p
        assert expansion == original
        rows.append({'N': N, 'literal_mixed_colors': colors,
                     'original_signed_odd_boxes_and_complete_filling': True,
                     'sole_original_marked_cut_retained': True})
    return rows


def exact_three_base():
    I, rt = sp.I, sp.sqrt(3)
    q = (1+I*rt)/2
    Q, x, rho = sp.expand(q*q), sp.expand(q*q), I*rt
    clean = lambda z: sp.simplify(sp.expand_complex(z))
    N, d = 3, 2
    Ec, F = sp.zeros(N), sp.zeros(N)
    for a in range(1, N):
        Ec[a-1, a] = clean(Q**(-a)-1)
        F[a, a-1] = clean(1-Q**a)
    E = Ec/rho**2
    K = sp.diag(*[clean(x*Q**(-a)) for a in range(N)])
    Ki = K.inv()
    nil = sp.eye(N*N)
    coefficient = sp.Integer(1)
    for k in range(1, N):
        number = clean((q**k-q**(-k))/rho)
        coefficient = clean(coefficient*q**(k-1)*rho/number)
        nil += coefficient*sp.kronecker_product(E**k, F**k)
    H = [d-2*a for a in range(N)]
    cartan = sp.diag(*[clean(q**(ha*hb//2)) for ha in H for hb in H])
    swap = sp.zeros(N*N)
    for a, b in itertools.product(range(N), repeat=2):
        swap[b*N+a, a*N+b] = 1
    R = (swap*cartan*nil).applyfunc(clean)
    Ft = sp.kronecker_product(F, sp.eye(N))+sp.kronecker_product(Ki, F)
    Et = sp.kronecker_product(Ec, K)+sp.kronecker_product(sp.eye(N), Ec)
    O = (Ft*Et+q*sp.kronecker_product(K, K)+q**(-1)*sp.kronecker_product(Ki, Ki)).applyfunc(clean)
    L = O*O-sp.eye(N*N)
    B = (R.inv()*L).applyfunc(clean)
    total, M0 = sp.Integer(0), None
    for h in range(-d, d+1):
        ids = list(range(max(0, h), min(d, d+h)+1))
        M = sp.Matrix([[clean(x**(-2*a+h)*B[(a-h)*N+d-b+h, a*N+d-b])
                        for b in ids] for a in ids])
        D = sp.diag(*[clean(x**(2*a)) for a in ids])
        total += sp.trace(D*M**3)
        if h == 0:
            M0 = M
    expected = sp.Matrix([
        [sp.Rational(9, 2)+3*rt*I/2, -sp.Rational(3, 2)-3*rt*I/2, 0],
        [3, sp.Rational(21, 2)+9*rt*I/2, -sp.Rational(3, 2)+3*rt*I/2],
        [0, -sp.Rational(3, 2)-3*rt*I/2, 9]])
    assert (M0-expected).applyfunc(clean) == sp.zeros(3)
    value = clean(x**(2*d)*total/N)
    assert clean(value-(-189+81*rt*I)) == 0
    # Diagonal similarity leaves these two diagonals fixed. Their ratio
    # has nonzero imaginary part, so no common scalar makes both positive.
    assert clean(sp.im(M0[0, 0]/M0[2, 2])) != 0
    return {'N': N, 'boxes': 3, 'exact_original_complete_base': str(value),
            'all_charge_transfer_and_half_twist_matrix_exact': True,
            'diagonal_positive_gauge_shortcut_fails': True,
            'scope': 'Finite exact source calculation, not asymptotic survival.'}


if __name__ == '__main__':
    for s in range(2, 14):
        assert one_component(s) == (1 if s % 2 else 2)
    output = {'status': 'PASS', 'odd_pretzel_topology': 'odd s has one component; even s has two',
              'generic_full_tensor_sources': generic_literal_cases(),
              'original_one_crossing_sign_calibrations': torus_sign_cases(),
              'mixed_and_signed_filling': mixed_and_filled_cases(),
              'exact_complete_three_box_base': exact_three_base(),
              'scope': 'Arbitrary odd-box original source transfer; no claimed geometric coefficient or positive global base.'}
    Path(__file__).with_name('actual_odd_pretzel_augmented_transfer_source_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 6 generic marked pretzel sources; 24 original sign calibrations; 4 mixed/signed fillings; exact N3 complete base')
