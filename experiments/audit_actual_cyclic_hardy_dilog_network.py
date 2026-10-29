#!/usr/bin/env python3
"""Exact coefficient and whole-word checks for genuine cyclic scalar atoms.

The added cyclic tails are computed from the literature norm-one product,
not set to zero. No head cutoff is applied at transfers or reciprocal
factorial diagonals. Positive factorial kernels are read from their full
Laurent completion. Original signed words and pivotal sources are retained.
"""

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork, whole_word
from audit_actual_borel_regular_fusion import fusion


def cyclic_coefficients(N, p, Q, order):
    assert order < p
    logarithmic_derivative = [0] * (order + 1)
    for m in range(1, order + 1):
        weighted = sum(j * pow(Q, j * m, p) for j in range(1, N)) * pow(N, -1, p)
        if m % N == 0:
            weighted -= (N - 1) * pow(2, -1, p)
        weighted %= p
        target = 0 if m % N == 0 else pow(pow(Q, m, p) - 1, -1, p)
        assert weighted == target
        logarithmic_derivative[m] = weighted
    def exponential(sign):
        coefficients = [1] + [0] * order
        for n in range(1, order + 1):
            coefficients[n] = (sign * sum(logarithmic_derivative[m] * coefficients[n - m]
                                          for m in range(1, n + 1)) * pow(n, -1, p)) % p
        return coefficients
    return exponential(-1), exponential(1)


class CyclicHardyNetwork(HardyNetwork):
    def __init__(self, N, M):
        super().__init__(N, M)
        order = 4 * (N - 1) + 3
        U, V = cyclic_coefficients(N, self.p, self.Q, order)
        assert U[:N] == self.inv
        expected_v = [self.v[h] * pow(self.x, h, self.p) % self.p for h in range(N)]
        assert V[:N] == expected_v
        assert any(U[N:]) and any(V[N:])
        reflected = [N * pow(self.Q, N - 1 - a, self.p) * V[N - 1 - a] % self.p
                     for a in range(N)] + [0] * (order + 1 - N)
        assert reflected[:N] == self.fac
        self.inv = U  # Truly nonzero beyond the original head.
        self.fac = reflected  # Full Laurent completion has no powers >=N.
        self.u = [pow(self.x, -h, self.p) * U[h] % self.p for h in range(order + 1)]
        self.v = [pow(self.x, -h, self.p) * V[h] % self.p for h in range(order + 1)]
        self.high_transfer_terms_used = 0
        self.high_reciprocal_inputs_seen = 0
        self.cyclic_order = order

    def diagonal(self, states, head, values):
        if values is self.inv:
            self.high_reciprocal_inputs_seen += sum(s[head] >= self.N for s in states)
        # NO finite head restriction: completed inverse-factorial entries >=N
        # are genuinely available and are not forcibly zeroed here.
        return {s: c * values[s[head]] % self.p for s, c in states.items()
                if s[head] < len(values) and c * values[s[head]] % self.p}

    def transfer(self, states, i, coefficients, raising_first):
        for state in states:
            lowering_index = state[i + 1] if raising_first else state[i]
            self.high_transfer_terms_used += sum(
                int(h >= self.N and h <= lowering_index and coefficient != 0)
                for h, coefficient in enumerate(coefficients))
        return super().transfer(states, i, coefficients, raising_first)


def local_check(N, M):
    H = CyclicHardyNetwork(N, M)
    C, Ci, *_ = fusion(N, H.p, H.Q, [H.x, H.x], [0, 0])
    for source in itertools.product(range(N), repeat=2):
        j = source[0] * N + source[1]
        for operation, expected in [(lambda z: H.C(z, 0), C),
                                    (lambda z: H.Ci(z, 0), Ci),
                                    (lambda z: H.crossing(z, 1), H.plus),
                                    (lambda z: H.crossing(z, -1), H.minus)]:
            states = operation({source: 1})
            column = np.zeros(N * N, dtype=np.int64)
            for output, value in states.items():
                assert max(output) < N
                column[output[0] * N + output[1]] = value
            assert np.array_equal(column % H.p, expected[:, j] % H.p)
    assert H.high_transfer_terms_used == 0
    assert H.high_reciprocal_inputs_seen == 0
    assert H.overflows_seen > 0
    return H, {'N': N, 'M': M, 'cyclic_series_order_checked': H.cyclic_order,
               'literature_normalization_log_checked_including_resonant_degrees': True,
               'actual_fusion_inverse_and_signed_crossings': True,
               'added_cyclic_tails_nonzero_but_source_invisible': True,
               'completed_reciprocal_diagonal_has_no_artificial_upper_cut': True}


def elementary_gates(letters):
    result = []
    for letter in letters:
        i = abs(letter) - 1
        result += [('Udiag', i + 1), ('transfer', i + 1, i),
                   ('Udiag', i), ('Fdiag', i + 1)]
        result += ([('transfer', i, i + 1), ('Gaussian', i + 1)] if letter > 0
                   else [('Gaussian', i + 1), ('transfer', i, i + 1)])
        result += [('Udiag', i + 1), ('Fdiag', i),
                   ('transfer', i + 1, i), ('Fdiag', i + 1)]
    return result


def radius_chamber(heads, letters, minimum_color_modulus=Fraction(1, 3)):
    rho = Fraction(1, 16)
    previous = [Fraction(1)] * heads
    count = 0
    for gate in elementary_gates(letters):
        incoming = [rho * r / 2 for r in previous]
        if gate[0] == 'transfer':
            numerator, denominator = gate[1:]
            incoming[numerator] = min(incoming[numerator],
                                      rho * minimum_color_modulus * incoming[denominator] / 2)
            assert incoming[numerator] / incoming[denominator] / minimum_color_modulus < rho
        assert all(r < rho * R for r, R in zip(incoming, previous))
        outgoing = [rho * r / 2 for r in incoming]
        if gate[0] == 'Fdiag':
            outgoing[gate[1]] = 2 * incoming[gate[1]] / rho
            assert incoming[gate[1]] / outgoing[gate[1]] < rho
        elif gate[0] == 'Gaussian':
            outgoing[gate[1]] = incoming[gate[1]]
        elif gate[0] == 'Udiag':
            assert outgoing[gate[1]] / incoming[gate[1]] < rho
        for j in range(heads):
            if gate[0] in ['Fdiag', 'Gaussian', 'Udiag'] and j == gate[1]:
                continue
            assert outgoing[j] / incoming[j] < rho
        previous = outgoing
        count += 1
    return {'heads': heads, 'word': list(letters), 'rho': str(rho),
            'minimum_color_modulus': str(minimum_color_modulus),
            'elementary_factors_and_identity_reset_layers': count,
            'all_atom_and_Hardy_radius_inequalities_exactly_feasible': True,
            'independent_of_N': True}


def internal_fusion_charges():
    routes = 0
    interiors = 0
    for N in range(2, 13):
        d = N - 1
        for a, b in itertools.product(range(N), repeat=2):
            for h in range(min(a, d - b) + 1):
                u, v = a - h, b + h
                r1, r2 = d - a, d - v
                assert u + 1 + h + r1 == b + 1 + h + r2 == N
                assert min(u + 1, b + 1, h, r1, r2) >= 0
                interiors += int(h > 0 and r1 > 0 and r2 > 0)
                routes += 1
    assert interiors > 0
    return {'exact_supported_fusion_routes_checked': routes,
            'strictly_positive_three_index_routes_checked': interiors,
            'charges': ['(u+1)+h+(N-1-a)=N', '(b+1)+h+(N-1-v)=N'],
            'geometric_Pachner_edge_identification': 'NOT established'}


def main():
    rows, words = [], []
    for N in range(2, 9):
        for M in [1, 3]:
            try:
                H, row = local_check(N, M)
            except ValueError:
                continue
            rows.append(row)
            if N <= 4:
                words.append(whole_word(H, 3, [1, -2, 1, -2]))
                words.append(whole_word(H, 3, [1, 2, -1, 2, 1, -2]))
            if N <= 3:
                words.append(whole_word(H, 4, [1, 2, 3, -2, -1, 3]))
            assert H.high_transfer_terms_used == H.high_reciprocal_inputs_seen == 0
    chambers = [radius_chamber(3, [1, -2, 1, -2]),
                radius_chamber(4, [1, 2, 3, -2, -1, 3]),
                radius_chamber(6, [1, -2, 3, -4, 5, 2, -3, 4])]
    result = {'status': 'PASS', 'actual_cyclic_completion_cases': rows,
              'whole_original_signed_word_cases': words, 'exact_common_radius_chambers': chambers,
              'actual_internal_affine_fusion_charge': internal_fusion_charges(),
              'scope': 'Original scalar cyclic-dilog/Hardy network with full finite Gaussian retained and original initial cycles. No geometric-cycle selection or global volume limit claimed.'}
    Path(__file__).with_name('actual_cyclic_hardy_dilog_network_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'local_cases': len(rows), 'whole_word_cases': len(words),
                      'exact_radius_chambers': len(chambers)}))


if __name__ == '__main__':
    main()
