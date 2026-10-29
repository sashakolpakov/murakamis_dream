#!/usr/bin/env python3
"""Original post-forced-fusion 4_1 tree source: exact excess entropy and jets."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_alternating_balanced_source import check_actual_block_table
from audit_actual_global_charged_bridge_flow import setup
from audit_actual_forced_source_fusion import coefficient


def block(H, X, Y, a, L):
    out = 1
    for k in range(L):
        out = out*(X-pow(H.Q, k, H.p)*a*Y) % H.p
    return out


def derivative(roots, k, p):
    out = 1
    for j, z in enumerate(roots):
        if j != k:
            out = out*(roots[k]-z) % p
    return out


def field_channels():
    rows = []
    for r in range(1, 7):
        N = 5*r+1
        H = HardyNetwork(N, 1)
        p, Q, d = H.p, H.Q, N-1
        v, w, t = 3*r, 2*r, 4*r
        S = setup(H, 3, [1, -2, 1, -2])
        check_actual_block_table(H, S, (0, v, w, t))
        edges = [dict(u=2, v=0, L=d-v, a=pow(Q, v+1, p), id=0),
                 dict(u=0, v=1, L=v, a=pow(Q, w-v, p), id=1),
                 dict(u=1, v=2, L=w, a=pow(Q, -w-t, p), id=2),
                 dict(u=0, v=2, L=d-t, a=pow(Q, -v, p), id=3),
                 dict(u=2, v=1, L=t, a=1, id=4)]
        fixed_source = coefficient(H, edges, {0:d, 1:w, 2:d})
        assert fixed_source != 0, (N, 'complete original fixed-clock sector')
        loop = H.fac[d]*pow(H.fac[w], -1, p) % p
        first = pow(Q, -w, p)*loop % p
        C_A, C_D = 2, 3
        K_A, K_D = C_A-1, C_D-1
        root_sum = 0
        direct = None
        for ell in range(N):
            C = pow(Q, ell, p)
            A, D = pow(Q, 3*r, p)*C % p, pow(Q, 4*r, p)*C % p
            roots_A = [pow(Q, 2*r+j, p)*C % p for j in range(2*r+1)]
            roots_D = [pow(Q, 4*r+j, p)*C % p for j in range(r+1)]
            sA, sD = derivative(roots_A, r, p), derivative(roots_D, 0, p)
            E = pow(C, d-w, p)
            for e in (edges[0], edges[2], edges[3]):
                vals = [A, C, D]
                E = E*block(H, vals[e['u']], vals[e['v']], e['a'], e['L']) % p
            assert E and sA and sD
            F_A, F_D = (pow(A,N,p)-C_A) % p, (pow(D,N,p)-C_D) % p
            assert K_A*K_D*pow(F_A*F_D, -1, p) % p == 1
            term = K_A*K_D*E*pow(F_A*F_D*sA*sD*N*pow(C,d,p), -1, p) % p
            root_sum = (root_sum+term) % p
            if ell == 0:
                direct = E*pow(sA*sD, -1, p) % p
            assert term*N % p == direct
        assert root_sum == direct
        assert first*root_sum % p
        rows.append({'r': r, 'N': N, 'prime': p,
                     'original_fixed_clock_coefficient_nonzero': int(fixed_source),
                     'all_exact_short_channel_root_labels': N,
                     'central_norms_cancel_exactly': True,
                     'grouped_original_relative_channel': int(first*root_sum % p)})
    return rows


def complex_magnitudes():
    mp.mp.dps = 70
    rows = []
    for r in range(1, 7):
        N, d = 5*r+1, 5*r
        Q = mp.exp(2*mp.pi*1j/N)
        F = lambda k: mp.fprod(1-Q**j for j in range(1,k+1))
        B = lambda X,Y,a,L: mp.fprod(X-Q**j*a*Y for j in range(L))
        A, D = Q**(3*r), Q**(4*r)
        SA = mp.fprod(A-Q**(2*r+j) for j in range(2*r+1) if j != r)
        SD = mp.fprod(D-Q**(4*r+j) for j in range(r+1) if j != 0)
        E = B(D,A,Q**(3*r+1),2*r)*B(1,D,Q**(-6*r),2*r)*B(A,D,Q**(-3*r),r)
        term = Q**(-2*r)*(F(d)/F(2*r))*E/(SA*SD)
        predicted = N**2/abs(F(r))**5
        error = abs(abs(term)/predicted-1)
        assert error < mp.mpf('1e-60')
        rows.append({'N': N, 'direct_relative_channel_modulus': mp.nstr(abs(term),25),
                     'exact_reflection_formula_relative_error': mp.nstr(error,5)})
    J = lambda x: -mp.im(mp.polylog(2,mp.exp(2*mp.pi*1j*x)))/(2*mp.pi)
    rate = -5*J(mp.mpf(1)/5)
    geometric = mp.im(mp.polylog(2,mp.exp(mp.pi*1j/3)))/mp.pi
    assert rate > mp.mpf(26)/35 > mp.mpf(11)/21 > geometric
    return rows, {'tree_channel_rate': mp.nstr(rate,40),
                  'figure_eight_volume_rate': mp.nstr(geometric,40),
                  'rigorous_comparison_in_note_uses_no_decimal_assumption': True}


def jet_obstruction():
    rows = []
    for N in range(4, 18):
        H = HardyNetwork(N, 1)
        p, d = H.p, N-1
        for m in (1,2,3):
            if m >= N:
                continue
            L = N-m
            s = (d+m-1)//m
            trailing = d+m-1-m*s
            assert trailing >= 0 and d+m*s+trailing == 3*d-L
            a = 2
            # X^d already fills the X source. Only constants of B and S^s remain.
            B0, S0 = block(H,0,1,a,L), block(H,0,1,a*pow(H.Q,L,p)%p,m)
            selected = B0*pow(S0,s,p) % p
            assert selected != 0
            # The factor S^s proves every short-root jet below order s is zero.
            short_roots = [a*pow(H.Q,L+j,p)%p for j in range(m)]
            assert len(set(short_roots)) == m
            assert all(block(H,z,1,a*pow(H.Q,L,p)%p,m) == 0 for z in short_roots)
            rows.append({'N': N, 'short_length': m, 'all_short_root_jet_orders_zero_below': s,
                         'selected_larger_charge_coefficient_nonzero': int(selected),
                         'no_full_block_when_m_at_least_two': m >= 2})
    return rows


def main():
    magnitudes, rates = complex_magnitudes()
    data = {'status':'PASS', 'actual_source_and_relative_channels':field_channels(),
            'independent_complex_magnitude_reflection':magnitudes, 'rates':rates,
            'short_root_jet_depth_obstruction':jet_obstruction(),
            'scope': ('The specified exact tree absolute envelope exceeds the volume. '
                      'No aggregate source growth or lower bound follows. Short-root-only '
                      'bounded-depth interpolation fails for unrestricted larger charges.')}
    Path(__file__).with_name('actual_forced_source_tree_entropy_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS six original nonzero source/tree channels, exact magnitudes, excess rate and jet-depth obstruction')


if __name__ == '__main__':
    main()
