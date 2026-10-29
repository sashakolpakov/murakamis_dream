#!/usr/bin/env python3
"""Actual generic cups/DW bends and all-input source recoupling columns."""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_generic_six_head_tetrahedral_source import Generic
from audit_actual_ordinary_four_port_recoupling_kernel import factorials
from audit_actual_trivalent_all_channel_marked_contraction import highest_cup_cap
from audit_actual_trivalent_complete_circle_vertex_kernel import axis_apply


def clebsch_highest(A, B, C, q, p):
    """Integer-highest-weight finite coproduct; no half-integer indexing."""
    assert A+B >= C >= abs(A-B) and (A+B-C) % 2 == 0
    Q, m = q*q % p, (A+B-C)//2
    fac = factorials(q, max(A, B, C, A+B+1), p)
    h = [(-1)**s * pow(q, s*(A-2*B+2*m-s-1), p)
         * fac[B-m+s]*fac[A-s]*pow(fac[B-m]*fac[A], -1, p) % p
         for s in range(m+1)]
    W = np.zeros(((A+1)*(B+1), C+1), dtype=np.int64)
    for r, i in itertools.product(range(C+1), range(A+1)):
        j = m+r-i
        if not 0 <= j <= B:
            continue
        value = 0
        for s in range(m+1):
            t = j-m+s
            if not (0 <= t <= j and 0 <= r-t <= i):
                continue
            denominator = fac[s]*fac[m-s]*fac[t]*fac[r-t] % p
            value += h[s]*pow(q, -A*t, p)*pow(Q, s*t, p)*pow(denominator, -1, p)
        W[i*(B+1)+j, r] = fac[i]*fac[j]*value % p
    return W


def bent_map(g, a):
    N, d, q, p = g.N, g.d, g.q, g.p
    result = np.zeros((N*(2*a+1), N), dtype=np.int64)
    for i6, alpha, i2 in itertools.product(range(N), range(2*a+1), range(N)):
        value = sum(int(g.DW[a][alpha, i1*N+i2])*int(g.PV[i1, i6])
                    for i1 in range(N))
        result[i6*(2*a+1)+alpha, i2] = (
            (-1)**d * pow(q, d-2*i2-2*a+2*alpha, p)*value) % p
    return result


def theta_bend(g, a):
    f, d, p, q = g.fac, g.d, g.p, g.q
    return (pow(g.scale, -1, p)*pow(q, a*(2*a-d), p)*f[a]*f[d]
            * pow(f[2*a]*f[d-a], -1, p)) % p


def coefficient_prefactor(g, a, b, c):
    d, f, q, p = g.d, g.fac, g.q, g.p
    r1, r2 = a+b-c, a+c-b
    exponent = -2*a*a-5*c*c+2*a*c+2*b*c+a*d+3*d*c-c+d
    return ((-1)**(d+c)*pow(q, exponent, p)*f[r1]*f[r2]*f[d-a]*f[d-c]
            * f[2*c+1]*pow(f[a]*f[d]*f[d+c+1], -1, p)) % p


def generic_level(N, q=11, p=1009, literal_source=False):
    g = Generic(N, q, p)
    d, fac = g.d, g.fac
    identity = np.eye(N, dtype=np.int64)
    bends, triangles, inputs = 0, 0, 0
    cg_va = {}
    for a in range(N):
        cg_va[a] = clebsch_highest(d, 2*a, d, q, p)
        assert np.array_equal(bent_map(g, a), theta_bend(g, a)*cg_va[a] % p)
        bends += 1
    if literal_source:
        J, _ = g.physical_sources()
    for a, b in itertools.product(range(N), repeat=2):
        right = np.kron(identity, cg_va[a]) @ g.W[b] % p
        accumulated = np.zeros_like(right)
        for c in range(abs(a-b), min(a+b, d)+1):
            final_cg = clebsch_highest(2*c, 2*a, 2*b, q, p)
            projected = np.kron(g.DW[c], np.eye(2*a+1, dtype=np.int64)) @ right % p
            index = int(np.flatnonzero(final_cg[:, 0])[0])
            actual = (int(projected[index, 0])
                      * pow(int(final_cg[index, 0])*g.norm[c] % p, -1, p)) % p
            assert np.array_equal(projected, g.norm[c]*actual*final_cg % p)
            B = g.regular_corner_sum((a, b, c))
            predicted = coefficient_prefactor(g, a, b, c)*B % p
            assert actual == predicted, (N, a, b, c, actual, predicted)
            left = np.kron(g.W[c], np.eye(2*a+1, dtype=np.int64)) @ final_cg % p
            accumulated = (accumulated+actual*left) % p
            # Factored formula independently checks every source and cup factor.
            r, r1, r2 = b+c-a, a+b-c, a+c-b
            kt = ((-1)**r1*pow(q, 2*c+r1*(2*a+1-r1), p)
                  * fac[2*b]*fac[r2]*pow(fac[r]*fac[2*a], -1, p)) % p
            factored = (g.source_corner_factorial((a,b,c))*kt
                        * pow(theta_bend(g,a)*g.norm[c] % p, -1, p)) % p
            assert factored == actual
            if literal_source:
                U = J
                for axis, j in enumerate((a,b,c)):
                    U = axis_apply(g.DW[j], U, axis, p)
                _, cap_b = highest_cup_cap(2*b, q, p)
                M = U.transpose(2,0,1).reshape((2*c+1)*(2*a+1), 2*b+1) @ cap_b.T % p
                clock = np.array([pow(q, -2*a+2*alpha, p) for alpha in range(2*a+1)], dtype=np.int64)
                M = (M.reshape(2*c+1,2*a+1,2*b+1)*clock[None,:,None] % p).reshape(M.shape)
                target = theta_bend(g,a)*projected % p
                assert np.array_equal(M, target), (N,a,b,c,'literal bend')
                inputs += 2*b+1
            triangles += 1
        assert np.array_equal(accumulated, right), (N,a,b,'full Hom reconstruction')
    return {'N': N, 'generic_q_image': q, 'prime': p,
            'full_bend_maps': bends, 'all_admissible_triangle_columns': triangles,
            'literal_source_input_columns': inputs,
            'high_partner_channels_retained': True}


def main():
    levels = [generic_level(N, literal_source=N <= 5) for N in range(2,9)]
    # A second independent generic parameter, not an additional root test.
    second = [generic_level(N, q=2, p=1000003) for N in (3,4,6)]
    result = {'status': 'PASS', 'generic_levels': levels, 'second_generic_parameter': second,
              'proof_scope': 'generic rational all-input source bend and typed Hom coefficient; no norm asymptotic'}
    path = Path(__file__).with_name('actual_generic_tetrahedral_source_as_recoupling_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS',len(levels),'generic levels /',sum(x['all_admissible_triangle_columns'] for x in levels),
          'recoupling columns /',sum(x['literal_source_input_columns'] for x in levels),
          'literal input columns /',len(second),'second-parameter levels')


if __name__ == '__main__':
    main()
