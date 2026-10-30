#!/usr/bin/env python3
"""Original neighboring source quotients and correlated root packet errors.

The convergence checks use actual signed face pairs, including an explicitly
supplemental 202/202 pair. They are local uncontracted checks, not a shared
global contour or a Gaussian reduction.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_matching_edge_antidiagonal_operator_packet import factorials, clebsch, cup
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S, gauss
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from audit_actual_q_hahn_complementary_hard_edge import det_pair, low_series
from audit_actual_q_hahn_resonant_hard_edge import (
    normalized_series, small_second_series, boundary_polynomial, mixed_relative,
)
from audit_actual_original_network_resonant_boundary_chart import (
    original_fixture, numerical_fixture, data,
)


def exact_sources():
    whites = cup_steps = cup_reflections = dual_steps = 0
    for N in range(3, 9):
        loc = Local(N)
        Jet.p = loc.p
        Jet.order = 2
        d = N-1
        z = Jet([loc.q, loc.q])
        Q = z*z
        F = factorials(z, d)
        q0 = Jet(loc.q)
        Fr = factorials(q0, d)
        for a in range(d//2+1):
            m, L, s = d-a, 2*a, d-2*a
            for r in range(L+1):
                total = m+r
                for i in range(max(0, total-d), min(d, total)+1):
                    j = total-i
                    w0 = clebsch(d, a, z, F, i, j, r)
                    U, V = Q**i, Q**j
                    H0 = source_S(N, z, m, U, U*V)/U**m
                    for u, v in ((1, -1), (1, 0), (0, 1)):
                        ii, jj, rr = i+u, j+v, r+u+v
                        if not (0 <= ii <= d and 0 <= jj <= d and 0 <= rr <= L):
                            continue
                        w1 = clebsch(d, a, z, F, ii, jj, rr)
                        U1, V1 = Q**ii, Q**jj
                        H1 = source_S(N, z, m, U1, U1*V1)/U1**m
                        assert w1*H0 == z**(-d*v)*w0*H1
                        whites += 1
                        # The actual dual matrix, not a Hermitian adjoint.
                        def dual(row, x, y):
                            return Jet([int(loc.pi[a][k][row, x*N+y]) for k in range(2)])
                        def expanded(row, x, y):
                            scale = N*z**(-d*d)
                            return (cup(L, z, F, L-row)
                                    *clebsch(d, a, z, F, d-y, d-x, L-row)
                                    /(Jet(loc.gamma[a])*cup(d, z, F, d-y, scale)
                                      *cup(d, z, F, d-x, scale)))
                        assert dual(rr, ii, jj)*expanded(r, i, j) == dual(r, i, j)*expanded(rr, ii, jj)
                        dual_steps += 1
            for x in range(L+1):
                # Reflection-reduced root cup against original finite factorials.
                # exp(pi i*x)=(-1)^x at this actual physical node.
                C = N*(-1)**s*q0**(s*(s+1))/Fr[L]
                expected = C*(-1)**x*q0**((s-1)*x)
                for b in range(1, s+1):
                    expected /= 1-q0**(2*(x+b))
                assert cup(L, q0, Fr, x) == expected
                cup_reflections += 1
                for u in (1, 2):
                    if x+u > L:
                        continue
                    ratio = (-1)**u*z**(u*(L-2*x-1)-u*u)
                    for b in range(1, u+1):
                        ratio *= 1-Q**(x+b)
                    for b in range(u):
                        ratio /= 1-Q**(L-x-b)
                    assert cup(L, z, F, x+u) == ratio*cup(L, z, F, x)
                    cup_steps += 1
    x, L, u, d, i, j, r, v, m = sp.symbols('x L u d i j r v m')
    assert sp.expand((x+u)*(L-x-u-1)-x*(L-x-1)
                     -(u*(L-2*x-1)-u*u)) == 0
    assert sp.expand(-d*(r+u+v)+d*(i+u)-(-d*r+d*i)+d*v) == 0
    return dict(original_white_quotient_value_firstjet_checks=whites,
                literal_dual_neighbor_checks=dual_steps,
                original_generic_cup_steps=cup_steps,
                root_reflection_reduced_cups=cup_reflections,
                symbolic_exponent_identities=2)


def root_cup(N, L, x, physical=False):
    d = N-1
    s = d-L
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    FL = mp.fprod(1-Q**j for j in range(1, L+1))
    C = N*(-1)**s*Q**(s*(s+1)//2)/FL
    out = C*mp.exp(mp.pi*1j*x)*mp.exp(mp.pi*1j*(s-1)*x/N)
    out /= mp.fprod(1-mp.exp(2*mp.pi*1j*(x+j)/N) for j in range(1, s+1))
    return N*q**(-d*d)*out if physical else out


def model_and_relative(N, a, pattern, U, V):
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    m = N-1-a
    ps = mp.fprod(U*V-Q**r for r in range(a, m))
    Ka = gauss(Q, 2*a, a)
    if pattern == '200':
        endpoint = (-1)**m*Q**(m*(m+1)//2)*(U*V)**m
        endpoint *= mp.fprod(1-Q**r/U for r in range(m))
        K = mp.sin(mp.pi*m/N)**2*(V-1)/(mp.pi**2*(U/N**2)*V)
        bessel = mp.hyp0f1(1, -K)
        return endpoint*bessel, normalized_series(N, m, U, V)/bessel
    if pattern == '002':
        endpoint = mp.fprod(V-Q**r for r in range(m))
        K = N*N*V*mp.sin(mp.pi*m/N)**2*(1-U)/mp.pi**2
        bessel = mp.hyp0f1(1, -K)
        return endpoint*bessel, small_second_series(N, m, U, V)/bessel
    if pattern == '220':
        dd = det_pair(N, a, U)
        return V**a*Ka*dd*ps, det_pair(N, a, U, V)/dd
    if pattern == '022':
        A0 = Q**(N-1)
        bb, rr = model_and_relative(N, a, '220', A0/V, A0/U)
        return (U*V/A0)**m*bb, rr
    if pattern == '202':
        return boundary_polynomial(N, a, U*V)*ps, mixed_relative(N, a, U, U*V)
    assert pattern == '222'
    return V**a*Ka*det_pair(N, a, U, V)*ps, mp.mpc(1)


def literal_pair(N, a, halves, delta, directions):
    """One actual W-pi box; constants independent of delta cancel in ratios."""
    d, m, L, s = N-1, N-1-a, 2*a, N-1-2*a
    q = mp.exp(mp.pi*1j/N)
    parts = []
    for row, (di, dj) in zip(halves, directions):
        pattern, X, Y, x, y, _, _ = row
        i, j = N*x-mp.mpf('.5')+di*delta, N*y-mp.mpf('.5')+dj*delta
        U, V = mp.exp(2j*mp.pi*i/N), mp.exp(2j*mp.pi*j/N)
        bb, rr = model_and_relative(N, a, pattern, U, V)
        r = i+j-m
        white = mp.exp(mp.pi*1j*(-d*r+d*i-m*(m-1))/N)*bb
        parts.append((white, rr, i, j, r))
    wi, ri, ii, ji, r = parts[0]
    wo, ro, io, jo, r_out = parts[1]
    assert abs(r_out-r) < mp.mpf('1e-140')
    bend = mp.exp(mp.pi*1j*s*(a-r)/N)*root_cup(N, L, L-r)
    bend /= root_cup(N, d, d-jo, True)*root_cup(N, d, d-io, True)
    return wi*wo*bend, ri*ro


def numerical():
    fixtures = [numerical_fixture(original_fixture(kind, 0))
                for kind in ('cuboctahedron', 'octahedron')]
    selected = {}
    for fixture in fixtures:
        for keys in fixture['pairs']:
            f, mi, mo, l = keys
            halves = [data(fixture, (f, mid, l), 64, mp.mpf('.03'), mp.mpf('1.1'))
                      for mid in (mi, mo)]
            selected.setdefault(tuple(row[0] for row in halves), (fixture, keys))
    assert set(p for pair in selected for p in pair) == {'200','002','220','022','202','222'}
    packets = circles = odd = probes = original_checks = cup_derivatives = 0
    max_source = max_corr = max_odd = max_ratio = max_remainder = mp.mpf(0)
    patterns = set()
    for (fixture, keys) in selected.values():
        f, mi, mo, l = keys
        for N in (32,33,64,65,128,129):
            for defect_step in (0, 1):
                a = (N-1)//2-defect_step
                halves = [data(fixture, (f, mid, l), N, mp.mpf('.03'), mp.mpf('1.1'))
                          for mid in (mi, mo)]
                for row in halves:
                    patterns.add(row[0])
                # Two different literal affine paths, both with one shared channel row.
                for directions in (((1,0),(0,1)), ((1,-1),(-1,1))):
                    bp, rp = literal_pair(N,a,halves,1,directions)
                    bm, rm = literal_pair(N,a,halves,-1,directions)
                    quotient = bp/bm
                    correlation = rp/rm-1
                    max_corr = max(max_corr, N*N*abs(correlation))
                    max_ratio = max(max_ratio, abs(quotient), abs(1/quotient))
                    assert N*N*abs(correlation) < 100
                    kap = 1-mp.exp(mp.pi*1j/N)-mp.mpf('.37')**(N-1)
                    kap += mp.exp(mp.pi*1j/N)*mp.mpf('.63')**(N-1)
                    error = quotient*correlation/kap
                    max_odd = max(max_odd, N*abs(error))
                    assert N*abs(error) < 10000
                    circles += 1
                    odd += 1
                    packets += 4
                    # Small complex normalized-head neighborhoods, not just real shifts.
                    for z in (mp.mpc('.001','.001'), mp.mpc('-.001','.001')):
                        _, rr = literal_pair(N,a,halves,N*z,directions)
                        max_remainder = max(max_remainder, N*abs(rr-1))
                        assert N*abs(rr-1) < 100
                        probes += 1
                # The actual reflected cup, with no loss from separate escaping Gammas.
                r = N*(halves[0][3]+halves[0][4])-1-(N-1-a)
                x = 2*a-r
                s = N-1-2*a
                deriv = mp.pi*1j+(s-1)*mp.pi*1j/N
                deriv += 2*mp.pi*1j/N*mp.fsum(
                    mp.exp(2*mp.pi*1j*(x+j)/N)/(1-mp.exp(2*mp.pi*1j*(x+j)/N))
                    for j in range(1,s+1))
                direct = mp.diff(lambda xx:root_cup(N,2*a,xx),x)/root_cup(N,2*a,x)
                assert abs(direct-deriv) < mp.mpf('1e-140')
                cup_derivatives += 1
        # Independent original full Newton sum comparisons at opposite parities.
        for N in (9,10):
            a=(N-1)//2-1
            for mid in (mi,mo):
                row=data(fixture,(f,mid,l),N,mp.mpf('.03'),mp.mpf('1.1'))
                q=mp.exp(mp.pi*1j/N)
                for u,v in ((0,0),(1,-1),(1,0)):
                    U=row[1]/q*mp.exp(2*mp.pi*1j*u/N)
                    V=row[2]/q*mp.exp(2*mp.pi*1j*v/N)
                    bb,rr=model_and_relative(N,a,row[0],U,V)
                    actual=low_series(q,N,N-1-a,U,V)
                    err=abs(actual/(bb*rr)-1)
                    assert err < mp.mpf('1e-130')
                    max_source=max(max_source,err)
                    original_checks += 1
    return dict(actual_signed_pair_types=[list(p) for p in selected],
                all_six_numerator_types=sorted(patterns),
                original_Newton_sum_identities=original_checks,
                root_packet_values=packets,paired_source_quotients=circles,
                normalized_odd_errors=odd,complex_head_neighborhood_probes=probes,
                exact_escaping_cup_log_derivatives=cup_derivatives,
                maximum_original_source_relative_error=str(max_source),
                maximum_N_squared_correlated_relative_error=str(max_corr),
                maximum_N_scaled_normalized_odd_error=str(max_odd),
                maximum_two_sided_model_quotient=str(max_ratio),
                maximum_N_scaled_product_remainder=str(max_remainder),
                fixture_scope='Original cuboctahedral face pairs plus explicitly supplemental octahedral 202/202. Local products, no global band cycle.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    mp.mp.dps=160
    result=dict(status='PASS',precision_digits=mp.mp.dps,
                exact=exact_sources(),numeric=numerical(),
                scope='Original local source quotients and all-six-type correlated finite root models. No contracted/Gaussian ratio, leading odd coefficient, or period inference.')
    target=args.output or Path(__file__).with_name('actual_correlated_boundary_band_ratio_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
