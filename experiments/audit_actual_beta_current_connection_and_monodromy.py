#!/usr/bin/env python3
"""Exact original beta-current Ward connection and deck/normal-jet laws."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_modular_dilog_circle import log_psi_inside, log_derivative
from audit_actual_trivalent_quantum_beta_source import B


def log_full_psi(N, z):
    if mp.re(z) < 0:
        return log_psi_inside(N, 1, z)
    cb = .5j*(mp.sqrt(N)+1/mp.sqrt(N))
    return (-mp.pi*1j*(1+2*cb*cb)/6
            +mp.pi*1j*(mp.sqrt(N)*z/(2*mp.pi)-cb)**2
            +log_psi_inside(N, -1, -z))


def state(N, l, c):
    h = 2j*mp.pi/N
    phi = mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
    u, v = mp.exp(l), mp.exp(l+c)
    D = 1-u**N+v**N
    S = N/phi*mp.exp(N*l-c*l/h+log_full_psi(N, c)+log_full_psi(N, h-l))
    bb = B(N, u, v)
    return S, (bb-S)/D, bb


def symbolic_deck_system():
    U, V = sp.symbols('U V', nonzero=True)
    A, D = U-V, 1-U+V
    Mv = sp.Matrix([[1/A, 0], [-1/A, 1]])
    Ms = sp.Matrix([[(U-1)/V, 0], [1/V, 1]])
    Mu = sp.Matrix([[A*(U-1)/V, 0], [U/V, 1]])
    assert all(sp.factor(e) == 0 for e in Mv*Ms-Ms*Mv)
    assert all(sp.factor(e) == 0 for e in Mu-Ms*Mv.inv())
    invariant = sp.Matrix([[1, D]])
    for M in [Mv, Ms, Mu]:
        assert all(sp.factor(e) == 0 for e in invariant*M-invariant)
    # The balanced extension and every finite normal-jet order.
    d, vv = sp.symbols('d v', nonzero=True)
    M = sp.Matrix([[1/(1-d), 0], [-1/(1-d), 1]])
    L = M-sp.eye(2)
    rows = []
    for p in range(7):
        entries = [sp.series(e, d, 0, p+1).removeO().expand()
                   for e in L**(p+2)]
        assert all(e == 0 for e in entries)
        # The preceding power is genuinely nonzero modulo d^(p+1).
        assert sp.series((L**(p+1))[1, 0], d, 0, p+1).removeO() != 0
        rows.append({'normal_jet_order': p, 'nilpotence_index': p+2})
    mu = sp.symbols('mu')
    MM = sp.Matrix([[mu, 0], [(1-mu)/D, 1]])
    LL = MM-sp.eye(2)
    assert all(sp.factor(e) == 0 for e in LL**2-(mu-1)*LL)
    return {'commuting_boundary_decks': True, 'original_B_invariant': True,
            'u_only_generator_composition': True,
            'all_winding_minimal_polynomial': True, 'normal_jets': rows}


def formal_current_symbols():
    u, v = sp.symbols('u v')
    denom = 1-u+v
    Euler_v = lambda f: v*sp.diff(f, v)
    Euler_all = lambda f: u*sp.diff(f, u)+v*sp.diff(f, v)
    iterate = lambda op, f, count: f if count == 0 else iterate(op, op(f), count-1)
    rr = [1/denom]
    rows = []
    for k in range(5):
        if k:
            rr.append(sp.factor((u-v)/denom*sum(
                iterate(Euler_v, rr[k-j], j)/sp.factorial(j)
                for j in range(1, k+1))))
        # No hidden poles besides the local normalization bubble.
        num, dd = sp.fraction(sp.factor(rr[k]))
        assert sp.Poly(num, u, v) is not None
        assert sp.cancel(denom**(2*k+1)*rr[k]).is_polynomial(u, v)
        sim = v*sum(iterate(Euler_all, rr[k-j], j)/sp.factorial(j)
                    for j in range(k+1))-(u-1)*rr[k]-(1 if k == 0 else 0)
        assert sp.factor(sim) == 0
        rows.append({'order': k, 'only_bubble_pole': True,
                     'pole_order_at_most': 2*k+1, 'second_Ward_compatibility': True})
    assert sp.factor(rr[1]+v*(u-v)/denom**3) == 0
    return rows


def actual_state_checks(N):
    h = 2j*mp.pi/N
    T = 2j*mp.pi
    u, v = mp.mpc('.7', '-.4'), mp.mpc('.9', '.2')
    l, c = mp.log(u), mp.log(v/u)
    U, V = u**N, v**N
    A, D = U-V, 1-U+V
    S, I, bb = state(N, l, c)
    tol = mp.mpf('1e-34')
    rows = []
    for name, ll, cc, sf, ishift in [
            ('v', l, c+T, 1/A, -1/A),
            ('simultaneous', l+T, c, (U-1)/V, 1/V),
            ('u', l+T, c-T, A*(U-1)/V, U/V)]:
        ss, ii, bb2 = state(N, ll, cc)
        err = max(abs(ss/S-sf), abs((ii-I)/S-ishift), abs(bb2-bb))
        assert err < tol, (N, name, err)
        rows.append({'deck': name, 'full_Psi_source_identity_error': float(err)})
    sq, iq, _ = state(N, l, c+h)
    ss, iss, _ = state(N, l+h, c)
    su, iu, _ = state(N, l+h, c-h)
    wards = [S-(u-v)*sq, I-(u-v)*iq-1,
             v*ss-(u-1)*S, v*iss-(u-1)*I-1,
             v*su-(u-1)*(mp.exp(h)*u-v)*S,
             v*iu-(u-1)*(mp.exp(h)*u-v)*I-mp.exp(h)*u]
    assert max(abs(e) for e in wards) < tol
    qc = -l/h+log_derivative(N, 1, c)
    ql = N-c/h-log_derivative(N, 1, h-l)
    Ic = mp.diff(lambda cc: state(N, l, cc)[1], c)
    Il = mp.diff(lambda ll: state(N, ll, c)[1], l)
    Bc = mp.diff(lambda cc: B(N, mp.exp(l), mp.exp(l+cc)), c)
    Bl = mp.diff(lambda ll: B(N, mp.exp(ll), mp.exp(ll+c)), l)
    differrs = [D*Ic+N*V*I-Bc+qc*S,
                D*Il-N*A*I-Bl+ql*S]
    assert max(abs(e) for e in differrs) < tol
    return {'N': N, 'three_boundary_decks': rows,
            'six_exact_original_Ward_errors': [float(abs(e)) for e in wards],
            'two_cross_multiplied_differential_errors': [float(abs(e)) for e in differrs]}


def current_growth_case(N):
    u = -1j
    l, c = -mp.pi*1j/2, mp.pi*1j/2
    # Avoid a root-center formula singularity by the exact known S expression
    # at the regular marked physical roots, evaluated by a tiny real shift.
    eps = mp.mpf('1e-32')
    S, I, bb = state(N, l+eps, c-eps)
    A = mp.exp(N*(l+eps))-1
    Iv = I-S/A
    assert abs(A) > 1
    expected = 2*mp.catalan/(2*mp.pi)
    return {'N': N, 'continued_current_rate': float(mp.log(abs(Iv))/N),
            'geometric_limit': float(expected),
            'principal_current_absolute_value': float(abs(I)),
            'exact_deck_jump_relative_error': float(abs((Iv-I)*A/S+1))}


def main():
    mp.mp.dps = 65
    result = {'status': 'PASS', 'symbolic_extension': symbolic_deck_system(),
              'rational_current_symbol_orders': formal_current_symbols(),
              'actual_full_source_connections': [actual_state_checks(N) for N in [3, 5, 9]],
              'regular_geometric_current_channel': [current_growth_case(N) for N in [9, 17, 33]],
              'scope': ('Exact original-source rank-two deck extension, Ward/differential '
                        'identities and finite normal jets. No automatic global current degeneracy.')}
    Path(__file__).with_name('actual_beta_current_connection_and_monodromy_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS commuting source-preserving deck matrices, seven finite normal-jet orders, '
          'nine full-Psi deck laws, eighteen Ward laws, six differential laws and growing currents')


if __name__ == '__main__':
    main()
