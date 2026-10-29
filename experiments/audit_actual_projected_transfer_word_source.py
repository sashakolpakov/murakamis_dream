#!/usr/bin/env python3
"""Original projected word: exact degree repair and retained Fourier seams."""

import itertools
import json
from pathlib import Path
from functools import lru_cache

import mpmath as mp
import numpy as np

from audit_actual_projected_transfer_cot_completion import Projected
from audit_exact_factorial_interpolation import factorial as factorial_uncached


@lru_cache(maxsize=None)
def factorial(N, z):
    return factorial_uncached(N, z)


def degree_average(A, N):
    degree = np.array([a+b for a in range(N) for b in range(N)])
    return A*(degree[:, None] == degree[None, :])


def currents(A):
    N = A.N
    Q, x = complex(A.Q), complex(A.x)
    E = np.zeros((N, N), complex)
    for a in range(1, N):
        E[a-1, a] = Q**(-a)-1
    K = np.diag([x*Q**(-a) for a in range(N)])
    return np.kron(E, K)+np.kron(np.eye(N), E)


def physical_sources(A):
    N, d, x = A.N, A.N-1, complex(A.x)
    p = np.zeros(N*N, complex)
    m = np.array([x**b/N**2 for a in range(N) for b in range(N)])
    for a in range(N):
        p[a*N+d-a] = N*x**(a-d)
    return p, m


def matrix_checks():
    rows = []
    for N in range(2, 9):
        A = Projected(N)
        R = A.original()
        E = currents(A)
        assert np.linalg.norm(E@R-R@E) < 1e-10*max(1., np.linalg.norm(R))
        z = mp.mpc('.37', '.1')
        raw = A.matrix(z)
        B = degree_average(raw, N)
        assert np.linalg.norm(B, 2) <= np.linalg.norm(raw, 2)*(1+1e-12)
        assert np.linalg.norm(B) <= np.linalg.norm(raw)*(1+1e-12)
        direct = np.zeros_like(B)
        for a, b in itertools.product(range(N), repeat=2):
            # Recover the exact scalar using the original a,b formula.
            phase = mp.exp((-a-b+z)*mp.log(A.x)+2j*mp.pi*b*(a-z)/N)
            ratio = (factorial(N, b+z)*A.F[a]
                     /(factorial(N, z)*A.F[b]*factorial(N, a-z)))
            r = A.kappa*phase*ratio
            T = a+b
            for c in range(max(0, T-(N-1)), min(N-1, T)+1):
                w = b+z-c
                weight = (mp.sin(mp.pi*w)/(mp.pi*w))**2
                direct[c*N+T-c, a*N+b] = complex(r*weight)
        assert np.linalg.norm(B-direct) < 1e-11*max(1., np.linalg.norm(B))
        # Whole two-head multiplication/projection bound, in the ORIGINAL norm.
        max_scalar = mp.mpf('0')
        for a, b in itertools.product(range(N), repeat=2):
            phase = mp.exp((-a-b+z)*mp.log(A.x)+2j*mp.pi*b*(a-z)/N)
            ratio = (factorial(N, b+z)*A.F[a]
                     /(factorial(N, z)*A.F[b]*factorial(N, a-z)))
            max_scalar = max(max_scalar, abs(A.kappa*phase*ratio))
        operator_bound = mp.exp(2*mp.pi*abs(mp.im(z)))*max_scalar
        assert np.linalg.norm(raw, 2) <= float(operator_bound)*(1+1e-12)
        assert np.linalg.norm(B, 2) <= float(operator_bound)*(1+1e-12)

        half = degree_average(A.matrix(mp.mpf('.5')), N)
        defect = E@half-half@E
        r00 = A.kappa*mp.exp(mp.mpf('.5')*mp.log(A.x))/factorial(N, mp.mpf('-.5'))
        expected = ((A.Q**-1-1)*r00*4/mp.pi**2
                    *(1-A.Q+A.q**-1))
        assert abs(defect[0, N]-complex(expected)) < 1e-11*max(1., abs(complex(expected)))
        assert abs(expected) > mp.mpf('1e-8')

        slices = []
        for k in range(N):
            sl = np.zeros_like(R)
            for a, b in itertools.product(range(N), repeat=2):
                u, v = b+k, a-k
                if min(u, v) >= 0 and max(u, v) < N:
                    sl[u*N+v, a*N+b] = R[u*N+v, a*N+b]
            assert np.array_equal(degree_average(sl, N), sl)
            slices.append(sl)
        assert np.linalg.norm(sum(slices)-R) < 1e-13
        norm2 = np.vdot(R, R).real
        lambdas = []
        for sl in slices:
            projected_lambda = np.vdot(R, sl)/norm2
            support_lambda = np.vdot(sl, sl).real/norm2
            assert abs(projected_lambda-support_lambda) < 1e-13
            lambdas.append(float(support_lambda))
        assert abs(sum(lambdas)-1) < 1e-13

        # The complete actual signed sum and original marked source remain.
        positive_sum = sum(slices)
        negative_sum = A.flip@positive_sum.conj()@A.flip
        negative = A.original(-1)
        assert np.linalg.norm(negative_sum-negative) < 1e-10*max(1., np.linalg.norm(negative))
        p, m = physical_sources(A)
        old = m@negative@R@R@p
        new = m@negative_sum@positive_sum@positive_sum@p
        assert abs(old-new) < 1e-10*max(1., abs(old))
        rows.append({'N': N, 'literal_degree_average_and_sinc_square': True,
                     'original_E_Ward_error': float(np.linalg.norm(E@R-R@E)),
                     'nonzero_off_grid_E_entry': [expected.real.__str__(), expected.imag.__str__()],
                     'source_exact_signed_word_error': float(abs(old-new)),
                     'original_metric_projection_operator_bound': float(operator_bound),
                     'Hurwitz_line_projection_residue_weights': lambdas})

    A = Projected(2)
    p, m = physical_sources(A)
    B = degree_average(A.matrix(mp.mpf('.5')), 2)
    E = currents(A)
    actual = m@(E@B-B@E)@p
    expected = (-16-52j)/(9*mp.pi**2*factorial(2, mp.mpf('-.5')))
    assert abs(actual-complex(expected)) < 1e-12
    return rows, {'N': 2, 'original_full_marked_E_defect': [actual.real, actual.imag],
                  'exact_times_9_pi2_Fhat_minus_half': [-16, -52]}


def interval_checks():
    rows = []
    for w in [mp.mpc('.37', '.2'), mp.mpc('-.63', '-.4'), mp.mpf('0'), mp.mpf('1')]:
        actual = mp.quad(lambda t: (1-abs(t))*mp.exp(2j*mp.pi*w*t), [-1, 0, 1])
        expected = (mp.sin(mp.pi*w)/(mp.pi*w))**2 if w else 1
        assert abs(actual-expected) < mp.mpf('1e-60')
        rows.append({'w': str(w), 'triangle_identity_error': float(abs(actual-expected))})
    xi = mp.mpc('.2', '.1')
    for N in [20, 40, 80]:
        actual = (mp.sin(mp.pi*N*xi)/(mp.pi*N*xi))**2
        leading = -mp.exp(-2j*mp.pi*N*xi)/(4*mp.pi**2*N*N*xi*xi)
        assert abs(actual/leading-1) < 3*mp.exp(-2*mp.pi*N*mp.im(xi))
        rows.append({'N': N, 'macroscopic_projection_leading_ratio_error': float(abs(actual/leading-1))})
    # An independent direct finite-sum lower approximation to the exact
    # infinite-column mass, compared to its Plancherel closed form.
    for nu in [mp.mpc('.37', '.2'), mp.mpc('-.63', '-.4'), mp.mpc('.23', 0)]:
        finite = mp.fsum(abs((mp.sin(mp.pi*(nu-c))/(mp.pi*(nu-c)))**2)
                        for c in range(-2000, 2001))
        v = abs(mp.im(nu))
        exact = mp.sinh(2*mp.pi*v)/(2*mp.pi*v) if v else mp.mpf(1)
        assert finite < exact
        assert exact-finite < mp.mpf('.002')
        rows.append({'nu': str(nu), 'complete_projection_column_mass': float(exact),
                     'independent_truncated_sum_error': float(exact-finite)})
    return rows


def main():
    mp.mp.dps = 75
    matrices, source = matrix_checks()
    data = {'status': 'PASS', 'actual_projected_word_families': matrices,
            'full_original_marked_source_witness': source,
            'retained_interval_source': interval_checks(),
            'scope': 'Both outer collars and exact full word are retained. Degree is repairable. Remaining E/current/seam statements concern this density representation, not impossibility of tame projections or a failure of the knot volume bound.'}
    Path(__file__).with_name('actual_projected_transfer_word_source_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS 7 actual signed projected-word families, degree contraction, full E defect, '
          'original marked source, complete-intertwiner projection weights and 10 Fourier interval checks')


if __name__ == '__main__':
    main()
