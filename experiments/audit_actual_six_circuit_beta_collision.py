#!/usr/bin/env python3
"""Actual signed-normal circuit and coherently summed beta collision audit."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_modular_dilog_circle import psi


def normals(sign):
    e = [sp.eye(9)[:, j] for j in range(9)]
    return [e[1]-e[2], e[2]-e[0], e[0]-e[3], e[2]-e[4],
            e[4]-e[3] if sign > 0 else e[3]-e[4]+e[8],
            e[4]-e[5]-e[8], e[3]-e[6], e[6]-e[5], e[5]-e[7]]


def positive_circuits(columns):
    out = []
    for size in range(2, len(columns)+1):
        for ids in itertools.combinations(range(len(columns)), size):
            ns = sp.Matrix.hstack(*(columns[j] for j in ids)).nullspace()
            if len(ns) != 1:
                continue
            v = ns[0]
            if all(x > 0 for x in v) or all(x < 0 for x in v):
                out.append(list(ids))
    return out


def normal_checks():
    rows = []
    for sign, eta4, expected in [
            (1, -4, [[0, 1], [2, 6], [7, 8], [0, 3, 4, 6]]),
            (-1, -2, [[0, 1], [2, 6], [7, 8], [2, 4, 5, 8]])]:
        cols = normals(sign)
        eta = sp.Matrix([-4, -6, -5, -3, eta4, -1, -2, 0, 0])
        pairings = [(v.T*eta)[0] for v in cols]
        assert max(pairings) <= -1
        frozen = [v.extract([2, 3, 4, 5, 8], [0]) for v in cols]
        circuits = positive_circuits(frozen)
        assert circuits == expected, (sign, circuits)
        rows.append({'sign': sign, 'strict_free_port_pairings': list(map(int, pairings)),
                     'frozen_port_circuits': circuits})

    # The six normals at the three actual shared ports, with internal L,M,T.
    # Order: crossing1 slots7,8; crossing2 slots2,6; crossing3 slots0,1.
    e = [sp.eye(6)[:, j] for j in range(6)]  # C,D,F,L,M,T
    circuit = [e[0]-e[3], e[3]-e[1], e[1]-e[4],
               e[4]-e[2], e[2]-e[5], e[5]-e[0]]
    mat = sp.Matrix.hstack(*circuit)
    assert mat*sp.ones(6, 1) == sp.zeros(6, 1)
    assert mat.rank() == 5
    assert all(mat[:, list(ids)].rank() == 5
               for ids in itertools.combinations(range(6), 5))

    Q, x, C, D, F, L, M, T = sp.symbols('Q x C D F L M T', nonzero=True)
    arguments = [Q**-1*L/(x*C), Q*L/D,
                 Q**-1*M/D, Q*M/F,
                 Q**-1*T/F, T/(x*C)]
    eps = [-1, 1, -1, 1, -1, 1]
    character = sp.factor(sp.prod(a**s for a, s in zip(arguments, eps)))
    assert character == Q**5
    classical = {D: x*C, F: x*C, L: x*C, M: x*C, T: x*C, Q: 1}
    assert all(sp.cancel(a.subs(classical, simultaneous=True)) == 1 for a in arguments)
    exact = {L: Q*x*C, D: Q**2*x*C, M: Q**3*x*C,
             F: Q**4*x*C, T: x*C}
    exact_values = [sp.cancel(a.subs(exact, simultaneous=True)) for a in arguments]
    assert exact_values == [1, 1, 1, 1, Q**-5, 1]
    return rows, {'figure_eight_prefix': [1, -2, 1], 'minimal_circuit_size': 6,
                  'exact_signed_argument_product': str(character),
                  'N5_exact_intersection': [str(a) for a in exact_values]}


def factorials(N):
    Q = mp.exp(2j*mp.pi/N)
    fac = [mp.mpc(1)]
    for k in range(1, N):
        fac.append(fac[-1]*(1-Q**k))
    p = [(-1)**k*Q**(k*(k-1)//2)/fac[k] for k in range(N)]
    return Q, fac, p


def beta(N, u, v):
    _, fac, p = factorials(N)
    return mp.fsum(fac[i+j]/fac[i]*p[j]*u**i*v**j
                   for i in range(N) for j in range(N-i))


def finite_source_checks():
    rows = []
    for N in range(2, 15):
        Q, fac, p = factorials(N)
        v = mp.mpc('.27', '.19')
        u = mp.mpc('-.36', '.21')
        a, b, c = mp.mpc('.13', '.22'), mp.mpc('-.18', '.26'), u
        vn = lambda z: mp.fsum(p[j]*z**j for j in range(N))
        errs = [abs(beta(N, 1, v)-N*vn(v)), abs(beta(N, u, u)-1),
                abs(beta(N, 1, a)*beta(N, 1, b)*beta(N, c, c)
                    -N*N*vn(a)*vn(b))]
        assert max(errs) < mp.mpf('1e-65'), (N, errs)
        # Independently check the all-j orbit-sum step in the proof.
        for j in range(N):
            orbit_sum = mp.fsum(mp.fprod(1-Q**(i+r) for r in range(1, j+1))
                               for i in range(N))
            assert abs(orbit_sum-N) < mp.mpf('1e-65')
        rows.append({'N': N, 'max_collision_source_error': float(max(errs)),
                     'entire_third_current_value': 1})
    return rows


def full_function_checks():
    rows = []
    for N in [2, 3, 5, 8, 13]:
        h = 2j*mp.pi/N
        for z in [mp.mpc('-.71', '.19'), mp.mpc('-.23', '-.31')]:
            t = mp.exp(z)
            pplus, pminus = psi(N, 1, z), psi(N, -1, z)
            errs = [abs(pplus*pminus-(1-t)*(1-t**N)),
                    abs(pplus*psi(N, -1, z-h)-(1-t**N)),
                    abs(psi(N, 1, z+h)*psi(N, -1, z-h)
                        -(1-t**N)/(1-t))]
            assert max(errs) < mp.mpf('1e-65'), (N, z, errs)
            # First U/F pair: its nontrivial complete-turn character.
            R1, R2, lv = mp.mpf('1.7'), mp.mpf('2.3'), z
            pair = lambda w: psi(N, -1, w-mp.log(R1)-h)*psi(N, 1, w-mp.log(R2)+h)
            expected = (1-(mp.exp(lv)/R1)**N)/(1-(mp.exp(lv)/R2)**N)
            assert abs(pair(lv+2j*mp.pi)/pair(lv)-expected) < mp.mpf('1e-65')
            rows.append({'N': N, 'max_exact_product_error': float(max(errs)),
                         'retained_pair_deck_character_nontrivial': True})
    return rows


def dependent_patch_checks():
    # C,D,F,L,M,T, with the exact six raw argument differentials.
    eta = mp.matrix([0, 1, 2, 4, 8, 16])
    e = [mp.eye(6)[:, j] for j in range(6)]
    vectors = [e[3]-e[0], e[3]-e[1], e[4]-e[1],
               e[4]-e[2], e[5]-e[2], e[5]-e[0]]
    eps = [-1, 1, -1, 1, -1, 1]
    slopes = [mp.fdot(v, eta) for v in vectors]
    assert slopes == [4, 3, 7, 6, 14, 16]
    rows = []
    for N in [5, 8, 13]:
        h = 2j*mp.pi/N
        # Small direct collision arguments; their dependencies are preserved
        # because both the initial u_j and translation come from coordinates.
        delta = mp.mpf('.00001')
        coords = mp.matrix([mp.mpc('-0.000001', '.0000002'),
                            mp.mpc('-.000002', '-.0000001'),
                            mp.mpc('-.000003', '.0000001'),
                            mp.mpc('-.000004', '-.0000002'),
                            mp.mpc('-.000005', '.0000003'),
                            mp.mpc('-.000006', '-.0000001')])
        us = [mp.fdot(v, coords) for v in vectors]
        out = [u+2j*delta*sl for u, sl in zip(us, slopes)]
        assert all(mp.im(z) > delta for z in out)
        before_split = mp.fprod(psi(N, s, z) for s, z in zip(eps, out))
        shifted = [z+s*2j*mp.pi if s*mp.im(z) < 0 else z
                   for s, z in zip(eps, out)]
        negative = [j for j, (s, z) in enumerate(zip(eps, out)) if s*mp.im(z) < 0]
        assert negative == [0, 2, 4]
        regular = mp.fprod(psi(N, s, z) for s, z in zip(eps, shifted))
        sector_sum = regular*mp.fsum(
            (-1)**len(ids)*mp.exp(N*mp.fsum(out[j] for j in ids))
            for size in range(len(negative)+1)
            for ids in itertools.combinations(negative, size))
        err = abs(before_split-sector_sum)
        assert err < mp.mpf('1e-65')

        # On the exact port diagonal the WHOLE six-function product is
        # K_N(l) K_N(m) (1-t^N), including all finite shifts.
        lz, mz, tz = [mp.mpc('-.2', '.07'), mp.mpc('-.31', '-.09'), mp.mpc('-.17', '.11')]
        pair1 = psi(N, -1, lz-h)*psi(N, 1, lz+h)
        pair2 = psi(N, -1, mz-h)*psi(N, 1, mz+h)
        pair3 = psi(N, -1, tz-h)*psi(N, 1, tz)
        kn = lambda z: mp.fsum(mp.exp(j*z) for j in range(N))
        raw_error = abs(pair1*pair2*pair3-kn(lz)*kn(mz)*(1-mp.exp(N*tz)))
        assert raw_error < mp.mpf('1e-65')
        rows.append({'N': N, 'dependent_patch_exact_sector_count': 8,
                     'sector_sum_error': float(err), 'raw_polynomial_error': float(raw_error)})
    return rows


def main():
    mp.mp.dps = 90
    normal, six = normal_checks()
    finite = finite_source_checks()
    full = full_function_checks()
    patch = dependent_patch_checks()
    result = {'status': 'PASS', 'single_crossing_normals': normal,
              'actual_six_circuit': six, 'finite_source_collision': finite,
              'exact_full_function_products_and_decks': full,
              'dependent_non_strict_patch': patch,
              'scope': 'Actual original-source contractions and collision fibre values only; no normal-jet, tangential-holonomy or full-period volume bound.'}
    Path(__file__).with_name('actual_six_circuit_beta_collision_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 2 exact normal classifications, actual minimal six-circuit/Q^5 tag, '
          '13 finite-source collision levels, 10 full-Psi products/decks, '
          '3 dependent eight-sector patches and exact raw polynomial sources')


if __name__ == '__main__':
    main()
