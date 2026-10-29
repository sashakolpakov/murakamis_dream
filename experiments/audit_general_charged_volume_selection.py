#!/usr/bin/env python3
"""Capacity/stability scope of the ACTUAL homogeneous charged source."""

import json
from pathlib import Path

import mpmath as mp

from audit_anchor_phase_cycles_and_fusion import bulk_family, verify_charges
from audit_actual_global_charged_bridge_flow import graph_blocks, setup
from audit_actual_hardy_cauchy_network import HardyNetwork


def log_binomial(N, L, k):
    return mp.fsum(mp.log(mp.sin(mp.pi*(L-k+j)/N))
                   -mp.log(mp.sin(mp.pi*j/N)) for j in range(1, k+1))


def actual_feasible_term(N):
    r, d = (N-1)//2, N-1
    H = HardyNetwork(N, 1)
    G = graph_blocks(H, setup(H, 3, [1, -2, 1, 1, -2, -2]),
                     [0, r, r, r, 0, r])
    b = r//2
    # a=c=f=0 in the already proved FULL FUSED source parametrization.
    # Fuse parallel blocks 4,5 FIRST: their complete d-block has
    # coefficient one at every head charge. Its head charge is b.
    # Replacing these two blocks by independent positive magnitudes
    # would undo a cancellation which the statement explicitly retains.
    first, second = G['blocks'][4:6]
    assert (first['tail'], first['head'], first['length']) == (1, 2, r)
    assert (second['tail'], second['head'], second['length']) == (1, 2, r)
    merged = dict(first, length=d, w_exp=0)
    G = dict(G, blocks=G['blocks'][:4]+[merged]+G['blocks'][6:])
    flow = [r+b, 0, 0, b, b, 0, r, 0, 0, r+b, 0, r]
    verify_charges(G, flow)
    log_weight = mp.fsum(log_binomial(N, B['length'], k)
                        for B, k in zip(G['blocks'], flow))
    selected = log_binomial(N, r, b)
    assert abs(log_weight-selected) < mp.mpf('1e-65')
    # A feasible monomial has degree d at each anchor. Its normalized
    # radius weight is therefore invariant even on very unequal radii.
    for scale in (mp.mpf('.01'), mp.mpf('1'), mp.mpf('8')):
        rho = [scale*mp.sin(j+mp.mpf('.37')) for j in range(G['anchor_count'])]
        radial = mp.fsum((B['length']-k)*rho[B['tail']]+k*rho[B['head']]
                        for B, k in zip(G['blocks'], flow))
        assert abs(radial-d*mp.fsum(rho)) < mp.mpf('1e-65')
    return {'N': N, 'r': r, 'selected_head_charge': b,
            'log_feasible_positive_weight': str(selected),
            'actual_exact_coefficient_modulus': N,
            'original_full_source_charges': True,
            'same_term_after_parallel_fusion': True}


def sine_normalization(N, L):
    logs = [log_binomial(N, L, k)-mp.log(mp.binomial(L, k))
            for k in range(L+1)]
    defects = [logs[k-1]+logs[k+1]-2*logs[k] for k in range(1, L)]
    assert defects and min(defects) > 0
    # The gauge making the j=0 factor X+Y stable does not stabilize
    # the next factor X+QY. Both X,Y below lie in the upper half-plane.
    X, Y = mp.e**(mp.j*mp.pi/N), mp.e**(mp.j*(mp.pi-mp.pi/N))
    Q = mp.e**(2*mp.pi*mp.j/N)
    assert X.imag > 0 and Y.imag > 0 and abs(X+Q*Y) < mp.mpf('1e-65')
    return {'N': N, 'L': L,
            'minimum_strict_logconvexity_defect': str(min(defects)),
            'explicit_half_plane_zero_after_first_factor_gauge': True}


def actual_angular_defect(N):
    r, d = (N-1)//2, N-1
    H = HardyNetwork(N, 1)
    G = graph_blocks(H, setup(H, 3, [1, -2, 1, 1, -2, -2]),
                     [0, r, r, r, 0, r])
    theta = [mp.sin(mp.mpf('.43')+j)*mp.mpf('1.7')
             for j in range(G['anchor_count'])]
    X = [mp.e**(mp.j*t) for t in theta]
    logarithmic = [mp.mpc(0)]*len(X)
    incidence = [0]*len(X)
    P, real_amplitude, constant = mp.mpc(1), mp.mpf(1), mp.mpc(1)
    for B in G['blocks']:
        i, j = B['tail'], B['head']
        for ell in range(B['length']):
            a = mp.pi*B['alpha_exp']/N
            b = mp.pi*(B['beta_exp']+2*ell)/N
            left, right = mp.e**(mp.j*a)*X[i], mp.e**(mp.j*b)*X[j]
            L = left-right
            assert abs(L) > mp.mpf('1e-12')
            P *= L
            logarithmic[i] += left/L
            logarithmic[j] -= right/L
            incidence[i] += 1
            incidence[j] += 1
            constant *= 2*mp.j*mp.e**(mp.j*(a+b)/2)
            real_amplitude *= mp.sin((a-b+theta[i]-theta[j])/2)
    source = P*mp.e**(-mp.j*d*mp.fsum(theta))
    defect = [s-2*d for s in incidence]
    rhs = constant*real_amplitude*mp.e**(
        mp.j*mp.fsum(de*t for de, t in zip(defect, theta))/2)
    assert abs(source-rhs) < mp.mpf('1e-65')*max(1, abs(source))
    for value, delta in zip(logarithmic, defect):
        assert abs(value.real-d-mp.mpf(delta)/2) < mp.mpf('1e-65')
    return {'N': N, 'exact_incidence_defects': defect,
            'all_original_anchor_phase_derivatives_checked': True,
            'global_lifted_sine_identity_checked': True}


def main():
    mp.mp.dps = 80
    result = {
        'exact_original_small_levels': [bulk_family(N) for N in (3, 5)],
        'actual_capacity_lower_terms': [actual_feasible_term(N) for N in (3, 5, 7, 9)],
        'stability_and_lorentzian_obstruction':
            [sine_normalization(N, L) for N in (5, 9, 17)
             for L in sorted({2, N//2, N-1})],
        'actual_angular_defect_identity': [actual_angular_defect(N)
                                          for N in (3, 5, 7, 9)],
        'asymptotic_positive_term': [],
        'scope': 'No universal subexponential positive-capacity comparison; not a knot-volume counterexample.'}
    target = mp.catalan/mp.pi
    for N in (17, 33, 65, 129, 257, 513, 1025):
        r = (N-1)//2
        value = log_binomial(N, r, r//2)
        assert abs(value-N*target) < 4*mp.log(N)+10
        result['asymptotic_positive_term'].append({
            'N': N, 'log_positive_weight_over_N': str(value/N),
            'limit_Catalan_over_pi': str(target),
            'log_actual_coefficient_over_N': str(mp.log(N)/N)})
    path = Path(__file__).with_name('general_charged_volume_selection_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS actual source charges/exact coefficients; radius-invariant '
          'exponential positive terms; stability and normalized-sine obstructions')


if __name__ == '__main__':
    main()
