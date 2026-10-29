#!/usr/bin/env python3
"""Positive full-Phi bipyramid geometry, selected Gaussian, and source descent."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp
import numpy as np

from audit_actual_full_psi_scalar_flow_cycle import ScalarFlowGraph, ReducedScalarFlowGraph
from audit_actual_modular_dilog_circle import psi, log_derivative, log_psi_inside


def D(z):
    return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)


def symbolic_certificates():
    x, y = sp.symbols('x y', nonzero=True)
    H = x+y-x*y
    s0, s2, s4 = x/H, H, y/H
    identities = [s0*s2-x, s2*s4-y,
                  1-s0-s4*(1-x), 1-s4-s0*(1-y),
                  1-s2-(1-x)*(1-y),
                  (1-s2)*s0*s4-(1-s0)*(1-s4)]
    assert all(sp.factor(v) == 0 for v in identities)
    # Boundary invariant ring and the internal character.
    r4, r2, r0, U, V, lam = sp.symbols('r4 r2 r0 U V lam', nonzero=True)
    source_rows = []
    for h4, h2, h0 in [(0, 0, 0), (2, 5, 3), (-1, 3, 4), (0, 1, 0)]:
        source = r4**h4*r2**h2*r0**h0
        reduced = sp.factor(source.subs({r4: U/r2, r0: V/r2}))
        delta = h2-h4-h0
        assert sp.factor(reduced-U**h4*V**h0*r2**delta) == 0
        transformed = source.subs({r4: r4/lam, r2: lam*r2, r0: r0/lam}, simultaneous=True)
        assert sp.factor(transformed-lam**delta*source) == 0
        source_rows.append({'orders': [h4, h2, h0], 'internal_character': delta,
                            'descends_to_boundary': delta == 0})
    # Exact boundary difference action on polynomial internal observables.
    q, dd, alpha, c, d, zz = sp.symbols('q D alpha c d z', nonzero=True)
    plus_ratio = (zz+q*dd*c)/(alpha*d)
    twice_ratio = (zz+q*q*dd*c)*(zz+q*dd*c)/(alpha*d)**2
    twice_E = (alpha*d)**2*twice_ratio-alpha*d*q*dd*(q+1)*c*plus_ratio+(q*dd*c)**2
    assert sp.factor(alpha*d*plus_ratio-q*dd*c-zz) == 0
    assert sp.factor(twice_E-zz**2) == 0
    minus_ratio = alpha*d/(zz+dd*c)
    assert sp.factor((zz+dd*c)*minus_ratio-alpha*d) == 0
    return {'six_bipyramid_relations': True, 'source_character_examples': source_rows,
            'exact_boundary_difference_positive_powers': [1, 2],
            'negative_power_source_recurrence': True}


def geometric_case(x, y):
    H = x+y-x*y
    shape = {1: x, 3: y, 2: H, 0: x/H, 4: y/H}
    assert all(mp.im(v) > 0 for v in shape.values())
    a = {j: mp.arg(v)/(2*mp.pi) for j, v in shape.items()}
    c = {j: -mp.arg(1-v)/(2*mp.pi) for j, v in shape.items()}
    beta = {j: mp.mpf('.5')-a[j]-c[j] for j in shape}
    assert min(list(a.values())+list(c.values())+list(beta.values())) > 0
    charge_errors = [a[1]-a[0]-a[2], a[3]-a[2]-a[4],
                     c[1]-c[0]-a[4], c[3]-a[0]-c[4], c[2]-c[1]-c[3]]
    assert max(abs(e) for e in charge_errors) < mp.mpf('1e-55')
    Y, Z = mp.log(abs(y))/(2*mp.pi), mp.log(abs(x))/(2*mp.pi)
    tau = mp.log(abs(H))/(2*mp.pi)
    var = {0: Z-tau, 2: tau, 4: Y-tau, 1: Z, 3: Y}
    phase = lambda j: -mp.polylog(2, shape[j])+4j*mp.pi**2*c[j]*var[j]
    amplitude = lambda j: mp.exp(2*mp.pi*c[j]*var[j]+(a[j]-.5)*mp.log(1-shape[j]))
    grad = (mp.log(1-shape[2])-mp.log(1-shape[0])-mp.log(1-shape[4])
            +mp.log(shape[0])+mp.log(shape[4]))
    assert abs(grad) < mp.mpf('1e-55')
    W = phase(4)+phase(2)+phase(0)-4*mp.pi**2*(Y-tau)*(Z-tau)
    vol2 = D(x)+D(y)
    vol3 = D(H)+D(x/H)+D(y/H)
    assert abs(vol2-vol3) < mp.mpf('1e-55')
    assert abs(mp.im(W)+vol3) < mp.mpf('1e-55')
    gaussian = -2j*mp.pi*(2+sum(shape[j]/(1-shape[j]) for j in [0, 2, 4]))
    assert mp.re(gaussian) > 0
    Pe = 2*(c[0]+a[2]+c[4])-.5
    ratios = []
    for N in [8, 16, 32]:
        cb2 = -(mp.sqrt(N)+1/mp.sqrt(N))**2/4
        def constant(j):
            chi = 4*c[j]*(c[j]+beta[j])-(4*(c[j]-beta[j])+1)/6
            return mp.exp(-mp.pi*1j/12+mp.pi*1j*cb2*chi)
        left = mp.fprod(constant(j)*amplitude(j) for j in [0, 2, 4])
        left *= mp.sqrt(2*mp.pi/gaussian)*mp.exp(N*W/(2j*mp.pi))
        right = mp.exp(mp.pi*1j*cb2*Pe/3)*constant(1)*constant(3)*amplitude(1)*amplitude(3)
        right *= mp.exp(N*(phase(1)+phase(3))/(2j*mp.pi))
        ratio = left/right
        assert abs(abs(ratio)-1) < mp.mpf('1e-50')
        assert N*abs(ratio-1) < 1
        ratios.append({'N': N, 'normal_leading_ratio': str(ratio),
                       'N_times_error': float(N*abs(ratio-1))})
    return {'x': str(x), 'y': str(y), 'five_positive_shapes': {str(j): str(v) for j, v in shape.items()},
            'all_five_positive_angle_charges': True, 'charge_relations_max_error': float(max(abs(e) for e in charge_errors)),
            'real_geometric_saddle': str(tau), 'bipyramid_volume': str(vol2),
            'negative_phase_rate': str(-vol2/(2*mp.pi)),
            'normal_gaussian_coefficient': str(gaussian), 'normalization_checks': ratios}


def actual_source_graph(heads, word):
    G = ReducedScalarFlowGraph(ScalarFlowGraph(heads, word))
    reflected = [j for j in range(len(G.edges)) if j % 9 in [3, 6, 8]]
    gamma_new = G.gamma.copy()
    Vnew = G.V.copy()
    for j in reflected:
        gamma_new += G.V[:, j]
        Vnew[:, j] *= -1
    cap_nodes = {node for a, b, _ in G.caps for node in (a, b)}
    internal = [i for i in range(len(G.gamma)) if i not in cap_nodes]
    assert all(int(gamma_new[i]) == 0 for i in internal)
    triples = []
    for i in internal:
        atom_ids = [j for j in range(len(G.edges)) if G.V[i, j]]
        if len(atom_ids) == 3:
            assert abs(int(G.gamma[i])) == 1
            assert len({int(G.V[i, j]) for j in atom_ids}) == 1
            assert len(set(atom_ids) & set(reflected)) == 1
            new_signs = [int(Vnew[i, j]) for j in atom_ids]
            assert abs(sum(new_signs)) == 1 and len(set(new_signs)) == 2
            triples.append({'vertex': i, 'original_atom_ids': atom_ids,
                            'original_normalized_affine_charge': int(G.gamma[i]),
                            'original_incidence_signs': [int(G.V[i, j]) for j in atom_ids],
                            'reflected_incidence_signs': new_signs})
    assert triples
    # Exact affine flow isomorphism h_F=1-a_F in normalized d=1 units.
    for tau_kind in range(2):
        costs = [sp.Rational((j*3+tau_kind) % 7, 3) for j in range(G.V.shape[1])]
        _, old_flow = G.flow_optimum(costs)
        new_flow = old_flow.copy()
        for j in reflected:
            new_flow[j] = 1-new_flow[j]
        assert np.array_equal(Vnew@new_flow, -gamma_new)
    return {'heads': heads, 'word': word, 'internal_vertices': len(internal),
            'all_internal_unreflected_charges_exactly_zero': True,
            'positive_factorial_atom_ids': reflected, 'actual_trivalent_source_laws': triples}


def positive_factorial_window_reflection():
    rows = []
    for N in range(2, 12):
        s, t, Q = sp.symbols('s t Q', nonzero=True)
        d = N-1
        lhs = N*s**d*sum((Q/(s*t))**h for h in range(N))
        rhs = N*Q**d*t**(-d)*sum((t*s/Q)**a for a in range(N))
        assert sp.expand(lhs-rhs) == 0
        rows.append({'N': N, 'exact_kernel_reflection': True,
                     'retained_scalar_and_field_character': f'{N}*Q^{d}*t^(-{d})'})
    return rows


def full_psi_reflection():
    rows = []
    for N in [3, 5, 8]:
        cb = 1j*(mp.sqrt(N)+1/mp.sqrt(N))/2
        zeta = mp.exp(-mp.pi*1j*(1+2*cb*cb)/6)
        S = mp.mpc('-.3', '-.7')
        # Psi_-(S) is inside the anchored disk; continue Psi_+(-S)
        # horizontally in its regular upper strip, independently of reflection.
        start = mp.mpf('-.4')
        theta = -mp.im(S)
        left_log = log_psi_inside(N, 1, start+1j*theta)
        left_log += mp.quad(lambda rho: log_derivative(N, 1, rho+1j*theta), [start, 0, -mp.re(S)])
        actual = mp.exp(left_log)
        predicted = zeta*mp.exp(mp.pi*1j*(mp.sqrt(N)*S/(2*mp.pi)+cb)**2)*psi(N, -1, S)
        error = abs(actual/predicted-1)
        assert error < mp.mpf('1e-43')
        rows.append({'N': N, 'exact_full_Psi_reflection_relative_error': float(error)})
    return rows


def main():
    mp.mp.dps = 65
    cases = [(mp.mpc('.5', '.7'), mp.mpc('.7', '.6')),
             (mp.mpc('.6', '.4'), mp.mpc('.45', '.8')),
             (mp.exp(mp.pi*1j/3), mp.exp(mp.pi*1j/3))]
    result = {'status': 'PASS', 'symbolic_source_certificates': symbolic_certificates(),
              'positive_bipyramid_families': [geometric_case(x, y) for x, y in cases],
              'original_reduced_source_charge_laws': [actual_source_graph(heads, word) for heads, word in
                  [(2, [1]), (2, [-1]), (4, [2, -1, 3, 2]), (4, [1, 2, -1, 2, 1, -2])]],
              'exact_positive_factorial_window_reflections': positive_factorial_window_reflection(),
              'full_Psi_field_reflection': full_psi_reflection(),
              'scope': 'Selected positive charged full-Phi bipyramid normal cycle and balanced boundary-source transport. Original finite-head adapter not inferred.'}
    Path(__file__).with_name('positive_bipyramid_source_transport_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS six exact bipyramid relations, torus source-descent and difference identities, '
          'three positive geometric families, nine Gaussian/phase checks, four actual source graphs, '
          'ten window reflections and three full-Psi reflection identities')


if __name__ == '__main__':
    main()
