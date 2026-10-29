#!/usr/bin/env python3
"""Actual positive-factorial/Hardy normal residue diagnostics."""

from fractions import Fraction
import json
from pathlib import Path

import mpmath as mp

from audit_actual_cyclic_hardy_dilog_network import cyclic_coefficients, elementary_gates
from audit_actual_hardy_cauchy_network import HardyNetwork


def V_and_A(N, r):
    Q = mp.exp(2j*mp.pi/N)
    logV = mp.mpf(N-1)/(2*N)*mp.log(1-r**N)
    A = -mp.mpf(N-1)/2*r**N/(1-r**N)
    for ell in range(1, N):
        z = Q**ell*r
        logV -= mp.mpf(ell)/N*mp.log(1-z)
        A += mp.mpf(ell)/N*z/(1-z)
    return mp.exp(logV), A


def analytic_checks():
    mp.mp.dps = 75
    delta = mp.mpf(1)/16
    gamma = mp.log(2)+mp.log((1-2*delta)*(1-delta))/4
    assert gamma > mp.mpf('.64')
    rows = []
    for N in (2, 3, 4, 5, 8, 12, 20, 32, 64):
        Q = mp.exp(2j*mp.pi/N)
        fac = [mp.mpc(1)]
        for a in range(1, N):
            fac.append(fac[-1]*(1-Q**a))
        max_relative = mp.mpf(0)
        for j in range(12):
            r = delta*mp.exp(2j*mp.pi*j/12)
            V, A = V_and_A(N, r)
            assert abs(A) <= mp.mpf(N)/60
            H = 1-1/(N-A)
            residual = N-1-A-H/(1-H)
            assert abs(residual) < mp.mpf('1e-65')
            assert mp.mpf(60)/(61*N) <= abs(1-H) <= mp.mpf(60)/(59*N)
            # a/b=r and a=Q*w, so b/w=Q/r.
            ratio = Q/r
            outer = sum(fac[a]*ratio**a for a in range(N))
            pole = N*ratio**(N-1)*V
            relative = abs(outer/pole-1)
            assert relative <= 2*mp.exp(-N*gamma)
            max_relative = max(max_relative, relative)
        rows.append({'N': N, 'pole_bound_and_exact_stationary_identity': True,
                     'maximum_relative_remainder': float(max_relative)})
    return rows


def coefficient_checks():
    rows = []
    for N in range(2, 9):
        H = HardyNetwork(N, 1)
        _, V = cyclic_coefficients(N, H.p, H.Q, 3*N+3)
        # All positive polynomial inputs, including upper overflow.
        output = {}
        for a in range(2*N+1):
            h = N-1-a
            coefficient = (N*pow(H.Q, h, H.p)*V[h] % H.p) if h >= 0 else 0
            expected = H.fac[a] if a < N else 0
            assert coefficient == expected
            if coefficient:
                output[a] = coefficient
        assert all(a >= 0 for a in output)
        # On |z|<|b|, the Hardy kernel has only strictly positive z powers;
        # hence its constant term against this output is exactly zero.
        assert all(a+k != 0 for a in output for k in range(1, 3*N+2))
        # This is not a bare Laurent-input identity: high cyclic coefficients
        # give genuinely nonzero negative diagonal entries.
        negative = [a for a in range(-2*N, 0)
                    if N-1-a < len(V) and V[N-1-a] != 0]
        assert negative
        rows.append({'N': N, 'all_nonnegative_input_channels': 2*N+1,
                     'negative_input_channels_showing_scope': len(negative)})
    return rows


def common_radii(heads, letters):
    rho = delta = Fraction(1, 16)
    gates = elementary_gates(letters)
    initial = Fraction(1, 512**len(gates))
    previous = [initial]*heads
    preceding_F = None
    pairs = 0
    for gate in gates:
        incoming = [rho*r/2 for r in previous]
        if gate[0] == 'transfer':
            num, den = gate[1:]
            incoming[num] = min(incoming[num], rho*incoming[den]/6)
        if preceding_F is not None:
            active, old_input = preceding_F
            assert incoming[active]/old_input == 1/delta
            pairs += 1
        assert all(r < rho*R for r, R in zip(incoming, previous))
        outgoing = [rho*r/2 for r in incoming]
        if gate[0] == 'Fdiag':
            outgoing[gate[1]] = 2*incoming[gate[1]]/(rho*delta)
            assert incoming[gate[1]]/outgoing[gate[1]] < rho
            preceding_F = (gate[1], incoming[gate[1]])
        else:
            preceding_F = None
        if gate[0] == 'Gaussian':
            # A conservative rational placeholder for an arbitrary fixed
            # dilation modulus <=8; the actual e^{-2|xi|} only shrinks it.
            outgoing[gate[1]] = rho*incoming[gate[1]]/16
        assert max(outgoing) <= 1
        previous = outgoing
    return {'heads': heads, 'word': letters, 'simultaneously_admissible_F_residue_pairs': pairs,
            'all_radii_at_most_one': True, 'N_independent': True}


def main():
    result = {'status': 'PASS', 'analytic': analytic_checks(),
              'coefficient': coefficient_checks(),
              'radii': [common_radii(3, [1, -2, 1, -2]),
                        common_radii(4, [1, 2, 3, -2, -1, 3]),
                        common_radii(6, [1, -2, 3, -4, 5, 2, -3, 4])],
              'scope': 'Exact source-preserving normal pushforward, no geometric saddle or whole-period lower bound.'}
    Path(__file__).with_name('positive_factorial_hardy_residue_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'analytic_cases': 12*len(result['analytic']),
                      'coefficient_levels': len(result['coefficient']),
                      'common_radius_words': len(result['radii']),
                      'source_preserving_residue_pairs': sum(r['simultaneously_admissible_F_residue_pairs']
                                                             for r in result['radii'])}))


if __name__ == '__main__':
    main()
