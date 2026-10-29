#!/usr/bin/env python3
"""Exact local signed-port composition; outer literal path is not inferred."""

import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.combinatorics.free_groups import free_group

from audit_actual_two_cut_ports import balanced_data
from audit_actual_mixed_crossing_circle_preferred_longitude import balanced_ordinary
from audit_actual_crossing_circle_source_and_filling import mixed_check
from audit_actual_complete_source_multiplicity_module import inverse_mod


def zero(A):
    return all(sp.cancel(z) == 0 for z in A) if isinstance(A, sp.MatrixBase) else sp.cancel(A) == 0


def algebra():
    w = sp.symbols('w', nonzero=True)
    c = w+1/w
    a = sp.Matrix([[-1, -1], [0, -1]])
    b = sp.Matrix([[-1, 0], [2-c, -1]])
    A = b*a
    numerator = A-(c-1)*sp.eye(2)
    check = []

    def yes(expr, label):
        assert zero(expr), label
        check.append(label)

    yes(numerator.det()-(2-c), 'regular_crossing_determinant')
    yes(numerator*b-a*numerator, 'positive_Hurwitz_intertwining')
    yes(numerator**2+(2-c)*A.inv(), 'crossing_square_full_central_sign')
    kr = numerator.inv()
    yes(kr*a*kr.inv()-b, 'actual_bent_R_first_output')
    yes(kr*b*kr.inv()-b*a*b.inv(), 'actual_bent_R_second_output')
    ratio = (1-1/w)/(1-w)
    yes(1/ratio+w, 'actual_bent_R_gain_minus_w')

    # Sharp eigenflag identity after the exact Schwarz z -> -z chain rule.
    y, L = sp.symbols('y L', nonzero=True)
    H = (1+y*L)/(L*(L+y))
    Yplus = 1/y
    sharp_eigen_square = (1+Yplus*L)/(1+Yplus/L)
    yes(sharp_eigen_square-1/H, 'full_H_sharp_meridian_square')

    n, m = sp.symbols('n m', real=True)
    A0 = A.subs(w, -1)
    N0 = A0+sp.eye(2)
    yes(N0*N0, 'noncentral_complete_pair_nilpotent_square')
    K = sp.eye(2)-(m+sp.I*n)*N0/2
    yes(K.det()-1, 'complete_arbitrary_signed_stack_determinant')
    yes(K*A0-A0*K, 'complete_outer_centralizer')
    # Exact cusp ratio for the displayed candidate peripheral pair.
    chart = sp.Matrix([[0, 1], [1, sp.Rational(1, 2)]])
    CuspK = sp.simplify(chart*K*chart.inv())
    CuspP = sp.simplify(chart*A0.inv()*chart.inv())
    yes(CuspP[0, 1]/CuspP[0, 0]/CuspK[0, 1]-2*sp.I/(n-sp.I*m),
        'candidate_marked_outer_cusp_ratio_not_a_physical_path_proof')
    return check


def free_words():
    F, alpha, beta, C = free_group('alpha beta C')
    values = [alpha, beta, C]
    for index in (1, 0, 0, 1):
        u, v = values[index:index+2]
        values[index:index+2] = [u**-1*v*u, u]
    P = beta*alpha
    assert values[2] == P**-1*C*P
    # After the actual closing relation [C,P]=1, the two main outputs
    # reduce to C^-1 alpha C, C^-1 beta C. This fact is also checked
    # in the independent full typed-loop audit.
    a, b = beta**-1, alpha**-1
    A = b*a
    assert P == A**-1
    # Main inverse/reversal changes commute with common conjugation.
    transformed = [(C**-1*beta*C)**-1, (C**-1*alpha*C)**-1]
    assert transformed == [C**-1*a*C, C**-1*b*C]
    return {'original_positive_outer_auxiliary_word': str(values[2]),
            'reverse_inverse_dictionary_gives_preferred_word': str(A**-1),
            'common_conjugation_survives_main_inverse_and_reversal': True,
            'scope': 'Exact word algebra in the source-preserving nested-dual main-port dictionary.'}


def physical_snakes_and_mixed_coupons(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x = N-1, int(K[0, 0])
    cup = np.array([[N*pow(x, -b, prime) % prime if a+b == d else 0
                     for b in range(N)] for a in range(N)], dtype=np.int64)
    cap = np.array([[pow(x, a, prime)*pow(N, -1, prime) % prime if a+b == d else 0
                     for b in range(N)] for a in range(N)], dtype=np.int64)
    I = np.eye(N, dtype=np.int64)
    assert np.array_equal(cup@cap % prime, I)
    assert np.array_equal(cap@cup % prime, I)
    # Reversal is abstract dual ordering, not a checked R crossing.
    reverse = np.zeros((N*N, N*N), dtype=np.int64)
    for a in range(N):
        for b in range(N):
            reverse[b*N+a, a*N+b] = 1
    J = np.kron(cup, cup)@reverse % prime
    EE = reverse@np.kron(cap, cap) % prime
    assert np.array_equal(J@EE % prime, np.eye(N*N, dtype=np.int64))
    assert np.array_equal(EE@J % prime, np.eye(N*N, dtype=np.int64))
    # The unrestricted exterior and original marked pivotal row stay outside.
    size = N*N
    left = np.fromfunction(lambda i, j: 3*i+5*j+7*i*j+11, (size, size), dtype=int).astype(np.int64) % prime
    right = np.fromfunction(lambda i, j: 2*i+13*j+i*j+17, (size, size), dtype=int).astype(np.int64) % prime
    g = np.kron(I, np.diag(pivot))
    before = int(np.trace(g@left@right % prime))*pow(N, -1, prime) % prime
    after = int(np.trace(g@left@J@EE@right % prime))*pow(N, -1, prime) % prime
    assert before == after

    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
    counts = 0
    for j in range(1, N+1):
        ordinary = balanced_ordinary(j, q, N, prime)
        for slot in (0, 1):
            A, B = (target, ordinary) if slot == 0 else (ordinary, target)
            s, t = A['dim'], B['dim']
            checked = mixed_check(A, B, q, eta, prime)
            # Original full unflipped universal R, including half-Cartan.
            U = checked.reshape(t, s, s, t).transpose(1, 0, 2, 3).reshape(s*t, s*t)
            Ui = inverse_mod(U, prime)

            def partial_transpose(M):
                axes = (2, 1, 0, 3) if slot == 0 else (0, 3, 2, 1)
                return M.reshape(s, t, s, t).transpose(axes).reshape(s*t, s*t)

            # Left/right bends use the literal appropriate cup orientation.
            for output, base, C, Ecap in (
                (U, Ui, cup.T if slot == 0 else cup, cap.T if slot == 0 else cap),
                (Ui, U, cup if slot == 0 else cup.T, cap if slot == 0 else cap.T),
            ):
                embed = np.kron(C, np.eye(j, dtype=np.int64)) if slot == 0 else np.kron(np.eye(j, dtype=np.int64), C)
                embed_inverse = np.kron(Ecap, np.eye(j, dtype=np.int64)) if slot == 0 else np.kron(np.eye(j, dtype=np.int64), Ecap)
                actual = embed@partial_transpose(base)@embed_inverse % prime
                assert np.array_equal(actual, output)
                counts += 1
    return {'N': N, 'literal_one_and_two_head_snakes': True,
            'original_unrestricted_marked_exterior_preserved': True,
            'all_ordinary_colors_both_signed_mixed_full_Cartan_coupon_moves': counts}


def regulator_algebra():
    p, aa, bb, m, x, y = sp.symbols('p aa bb m x y', real=True, nonzero=True)
    z, ell = x+sp.I*y, aa+sp.I*bb
    chirp = (z-2*sp.pi*sp.I*m)**2/(4*p)
    filled = sp.expand_complex(chirp).subs({x: -2*p*aa, y: 2*sp.pi*m-2*p*bb})
    assert sp.simplify(sp.im(filled)-2*p*aa*bb) == 0
    assert sp.simplify((-x*bb).subs(x, -2*p*aa)-2*p*aa*bb) == 0
    # Spin cancellation in the PAIRED norm, not in G or v separately.
    u, v = -z/2, sp.pi*sp.I-ell
    correction = -sp.pi*x-2*sp.re(u)*sp.im(v)
    assert sp.simplify(correction+x*bb) == 0
    return {'filled_quadratic_chirp_equals_marked_boundary_correction': True,
            'ordinary_pivot_spin_cancels_only_in_paired_regulator': True,
            'geometric_similarity_logs': 'U=-z, V=-2ell; U+pV=-2*pi*i*m'}


if __name__ == '__main__':
    result = {'status': 'PASS', 'exact_rational_and_complete_matrix_checks': algebra(),
              'exact_free_group_outer_algebra': free_words(),
              'literal_snakes_and_transported_original_mixed_coupons': [physical_snakes_and_mixed_coupons(N) for N in range(2, 8)],
              'marked_spin_and_primitive_filling_chirp': regulator_algebra(),
              'arithmetic': 'Exact root finite fields, SymPy rational functions and free-group normal forms',
              'scope': 'Local R/sharp composition, literal original nested snakes, ALL incident signed mixed '
                       'coupon duality moves, unrestricted marked closure, outer disk word and spin/chirp algebra. '
                       'The written theorem invokes separately proved quantum packet/gap and complete geometric '
                       'face/collar/completion inputs; finite checks do not replace them.'}
    Path(__file__).with_name('actual_belt_stack_typed_character_composition_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS exact R/sharp/stack matrices, outer free words, six original marked snake families, '
          '108 all-color/full-Cartan mixed signed coupon moves, and marked filling/spin algebra.')
