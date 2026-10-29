#!/usr/bin/env python3
"""Exact full-Psi deck characters, signs, and actual beta head pullback."""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_modular_dilog_circle import log_psi_inside


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def direct_character_checks():
    mp.mp.dps = 70
    rows = []
    models = [
        ([[2, -1], [-1, 0]], [[-1, 1], [-1, 0]], [1, 1]),
        ([[1, 2], [2, -1]], [[1, 0], [1, -2], [-1, 1]], [1, -1, 1]),
        ([[-1, 0], [0, 1]], [[2, 1], [0, 1], [-1, -1]], [-1, 1, -1]),
    ]
    for N in [2, 3, 6, 9]:
        h = 2j*mp.pi/N
        for number, (C, atoms, signs) in enumerate(models):
            Z = [mp.mpc('-.21', '.17'), mp.mpc('-.13', '-.23')]
            linear = [mp.mpc('0', '.71')+h/2, -h]
            offsets = [-mp.mpf(2)+j*h/2+mp.mpf('.11')*1j for j in range(len(atoms))]

            def log_field(z):
                gaussian = (sum(z[i]*C[i][j]*z[j] for i in range(2) for j in range(2))/2
                            +dot(linear, z))/h
                args = [dot(a, z)+ell for a, ell in zip(atoms, offsets)]
                assert all(mp.re(arg) < 0 for arg in args)
                return gaussian+sum(log_psi_inside(N, eps, arg)
                                    for eps, arg in zip(signs, args))

            X = [mp.exp(N*z) for z in Z]
            A = [mp.exp(N*(dot(a, Z)+ell)) for a, ell in zip(atoms, offsets)]
            characters = []
            for k in range(2):
                value = mp.exp(N*linear[k]+mp.pi*1j*N*C[k][k])
                value *= mp.fprod(X[j]**C[k][j] for j in range(2))
                value *= mp.fprod((1-a)**(-eps*inc[k])
                                 for a, eps, inc in zip(A, signs, atoms))
                characters.append(value)
            for n in [[1, 0], [0, 1], [2, -1], [-1, -2]]:
                translated = [z+2j*mp.pi*k for z, k in zip(Z, n)]
                actual = mp.exp(log_field(translated)-log_field(Z))
                predicted = mp.fprod(c**k for c, k in zip(characters, n))
                error = abs(actual/predicted-1)
                assert error < mp.mpf('1e-58'), (N, number, n, error)
                rows.append({'N': N, 'model': number, 'winding': n,
                             'relative_error': float(error)})
    return rows


def algebraic_checks():
    U, V, A = sp.symbols('U V A', nonzero=True)
    chi_u = sp.cancel(U**2/V*(1-V/U)*(1-1/U))
    chi_v = sp.cancel(1/U/(1-V/U))
    assert sp.factor(chi_u-(U-V)*(U-1)/V) == 0
    assert sp.factor(chi_v-1/(U-V)) == 0
    head = [sp.cancel(chi_u*chi_v), sp.cancel(1/chi_u), sp.cancel(1/chi_v)]
    assert sp.factor(head[0]-(U-1)/V) == 0
    assert sp.factor(head[0]*head[1]*head[2]-1) == 0
    # Head pullback is integral and uses all three head turns, not a pointwise center reset.
    L = sp.Matrix([[1, -1, 0], [1, 0, -1]])
    C = sp.Matrix([[2, -1], [-1, 0]])
    pulled = L.T*C*L
    assert pulled == pulled.T
    assert pulled*sp.ones(3, 1) == sp.zeros(3, 1)
    for n in [sp.Matrix([1, 0, 0]), sp.Matrix([2, -1, 1]), sp.Matrix([-1, 3, 2])]:
        assert (n.T*pulled*n)[0] == ((L*n).T*C*(L*n))[0]
        assert int((n.T*pulled*n)[0]-sum(n[k]*pulled[k, k] for k in range(3))) % 2 == 0
    return {'actual_beta_characters': [str(chi_u), str(chi_v)],
            'literal_three_head_characters': list(map(str, head)),
            'shared_scale_character': 1,
            'pulled_quadratic_matrix': [list(map(int, row)) for row in pulled.tolist()]}


def gaussian_sign_checks():
    checks = []
    for N in range(2, 12):
        h = 2j*mp.pi/N
        eta = mp.mpc('.23', '.19')
        direct = mp.exp(-((eta+2j*mp.pi)**2-eta**2)/(2*h))
        expected = (-1)**N*mp.exp(-N*eta)
        assert abs(direct/expected-1) < mp.mpf('1e-58')
        half = mp.exp(N*h/2)
        assert abs(half+1) < mp.mpf('1e-60')
        checks.append({'N': N, 'odd_gaussian_parity': (-1)**N,
                       'half_step_central_value': -1})
    return checks


def main():
    output = {'status': 'PASS', 'full_function_characters': direct_character_checks(),
              'actual_pullback': algebraic_checks(), 'parity_and_half_steps': gaussian_sign_checks(),
              'scope': 'Exact characters and marked central gluing of specified components; '
                       'no original-source support or geometric selection inferred.'}
    Path(__file__).with_name('actual_full_psi_frobenius_deck_gluing_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 48 direct full-Psi deck turns, ten Gaussian/half-step parity checks, '
          'actual beta characters and literal three-head integral pullback')


if __name__ == '__main__':
    main()
