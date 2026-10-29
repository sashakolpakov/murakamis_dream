#!/usr/bin/env python3
"""Check removal of finite Dirichlet numerators from the actual network.

Transfers and spectator heads are extended on ALL nonnegative indices,
without an upper head projection. Existing finite factorial/Gaussian
diagonal kernels retain their original support. Entire signed words are
then contracted with the original pivotal source, without re-projecting
between crossings. No geometric source or single Euler branch is assumed.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_crossing_euler_completion import actual_data
from audit_actual_borel_regular_fusion import fusion
from audit_actual_two_cut_ports import word_matrix, partial


class HardyNetwork:
    def __init__(self, N, M):
        data = actual_data(N, M)
        if data is None:
            raise ValueError('undefined original normalization')
        self.N, self.M = N, M
        (self.p, self.q, self.x, self.K, self.pivot, self.plus,
         self.minus, self.twist, self.dimension, self.normalization) = data
        self.Q = self.q * self.q % self.p
        self.fac = [1]
        for j in range(1, N):
            self.fac.append(self.fac[-1] * (1 - pow(self.Q, j, self.p)) % self.p)
        self.inv = [pow(v, -1, self.p) for v in self.fac]
        self.u = [pow(self.x, -h, self.p) * self.inv[h] % self.p for h in range(N)]
        self.v = [pow(-1, h, self.p) * pow(self.Q, h * (h - 1) // 2, self.p)
                  * self.u[h] % self.p for h in range(N)]
        self.diag = [pow(-1, h, self.p) * pow(self.Q, h * (h - 1) // 2, self.p)
                     * pow(self.x, -2 * h, self.p) % self.p for h in range(N)]
        self.diag_inv = [pow(v, -1, self.p) for v in self.diag]
        self.kappa = int(self.plus[0, 0])
        self.overflows_seen = 0
        self.largest_intermediate_index = 0

    def diagonal(self, states, head, values):
        return {s: c * values[s[head]] % self.p for s, c in states.items()
                if s[head] < self.N and c * values[s[head]] % self.p}

    def transfer(self, states, i, coefficients, raising_first):
        result = {}
        for state, c in states.items():
            for h, coefficient in enumerate(coefficients):
                a, b = state[i], state[i + 1]
                a, b = (a + h, b - h) if raising_first else (a - h, b + h)
                # Hardy projection only: NO upper cutoff at N.
                if min(a, b) < 0:
                    continue
                if max(a, b) >= self.N:
                    self.overflows_seen += 1
                self.largest_intermediate_index = max(self.largest_intermediate_index, a, b)
                output = state[:i] + (a, b) + state[i + 2:]
                result[output] = (result.get(output, 0) + c * coefficient) % self.p
        return {s: c for s, c in result.items() if c}

    def C(self, states, i):
        states = self.diagonal(states, i + 1, self.inv)
        states = self.diagonal(states, i, self.fac)
        states = self.transfer(states, i, self.u, False)
        return self.diagonal(states, i + 1, self.fac)

    def Ci(self, states, i):
        states = self.diagonal(states, i + 1, self.inv)
        states = self.transfer(states, i, self.v, False)
        states = self.diagonal(states, i, self.inv)
        return self.diagonal(states, i + 1, self.fac)

    def crossing(self, states, letter):
        i = abs(letter) - 1
        states = self.Ci(states, i)
        if letter > 0:
            states = self.transfer(states, i, self.u, True)
            states = self.diagonal(states, i + 1, self.diag)
        else:
            states = self.diagonal(states, i + 1, self.diag_inv)
            states = self.transfer(states, i, self.v, True)
        states = self.C(states, i)
        scalar = self.kappa if letter > 0 else pow(self.kappa, -1, self.p)
        return {s: c * scalar % self.p for s, c in states.items() if c * scalar % self.p}

    def word(self, initial, letters):
        states = {initial: 1}
        for letter in letters:
            states = self.crossing(states, letter)
            # No head projection is applied here.
        return states

    def tail_branch(self, initial, sign, selected_stages):
        states = {initial: 1}
        operations = [('D', 1, self.inv), ('T', False, self.v),
                      ('D', 0, self.inv), ('D', 1, self.fac)]
        operations += ([('T', True, self.u), ('D', 1, self.diag)] if sign > 0
                       else [('D', 1, self.diag_inv), ('T', True, self.v)])
        operations += [('D', 1, self.inv), ('D', 0, self.fac),
                       ('T', False, self.u), ('D', 1, self.fac)]
        stages = {1: (0, 1), 4 if sign > 0 else 5: (1, 0), 8: (2, 1)}
        nonempty_tail_selections = 0
        for j, (kind, head_or_direction, values) in enumerate(operations):
            states = (self.diagonal(states, head_or_direction, values) if kind == 'D'
                      else self.transfer(states, 0, values, head_or_direction))
            if j in stages:
                stage, head = stages[j]
                if stage in selected_stages:
                    states = {s: c for s, c in states.items() if s[head] >= self.N}
                    nonempty_tail_selections += int(bool(states))
        return states, nonempty_tail_selections


def local_check(N, M):
    H = HardyNetwork(N, M)
    C, Ci, *_ = fusion(N, H.p, H.Q, [H.x, H.x], [0, 0])
    for source in itertools.product(range(N), repeat=2):
        j = source[0] * N + source[1]
        for operator, expected in [(lambda z: H.C(z, 0), C),
                                   (lambda z: H.Ci(z, 0), Ci),
                                   (lambda z: H.crossing(z, 1), H.plus),
                                   (lambda z: H.crossing(z, -1), H.minus)]:
            states = operator({source: 1})
            assert all(max(s) < N for s in states)
            column = np.zeros(N * N, dtype=np.int64)
            for output, value in states.items():
                column[output[0] * N + output[1]] = value
            assert np.array_equal(column % H.p, expected[:, j] % H.p)
    assert H.overflows_seen > 0
    return H, {'N': N, 'M': M, 'actual_fusion_inverse_and_both_signed_crossings': True,
               'nonzero_upper_overflow_routes_retained_before_diagonal_support': H.overflows_seen,
               'largest_intermediate_index': H.largest_intermediate_index}


def whole_word(H, heads, letters):
    N, p = H.N, H.p
    literal = word_matrix(letters, H.plus, H.minus, heads, N, p)
    expected_cut = partial(literal, H.pivot, heads, N, p)
    cut = np.zeros((N, N), dtype=np.int64)
    before = H.overflows_seen
    for source in itertools.product(range(N), repeat=heads):
        states = H.word(source, letters)
        for output, coefficient in states.items():
            assert sum(output) == sum(source)
            assert max(output) < N
            if output[1:] != source[1:]:
                continue
            weight = 1
            for j in source[1:]:
                weight = weight * int(H.pivot[j]) % p
            cut[output[0], source[0]] = (cut[output[0], source[0]] + weight * coefficient) % p
    assert np.array_equal(cut % p, expected_cut % p)
    scalar = int(cut.sum()) * pow(N, -1, p) % p
    external = H.dimension * pow(H.twist, -sum(1 if k > 0 else -1 for k in letters), p) % p
    return {'N': N, 'M': H.M, 'heads': heads, 'word': list(letters),
            'whole_original_one_cut_matrix_equal': True,
            'no_projection_between_signed_crossings': True,
            'integer_degree_conserved': True,
            'actual_normalized_period': scalar * external % p,
            'retained_upper_overflow_routes': H.overflows_seen - before}


def upper_tail_branches():
    branches, nonempty = 0, 0
    for N in range(2, 6):
        for M in [1, 3]:
            H = HardyNetwork(N, M)
            for sign in [-1, 1]:
                for mask in range(1, 8):
                    stages = {j for j in range(3) if mask & (1 << j)}
                    for initial in itertools.product(range(N), repeat=2):
                        output, selected = H.tail_branch(initial, sign, stages)
                        assert not output
                        nonempty += selected
                        branches += 1
    assert nonempty > 0
    return {'exact_nonempty_subset_upper_tail_branch_zero_checks': branches,
            'nonzero_intermediate_tail_selections_before_barrier': nonempty,
            'both_signed_full_crossings_checked': True}


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
    result = {'status': 'PASS', 'local_full_operator_cases': rows, 'whole_original_word_cases': words,
              'all_nonempty_upper_endpoint_stage_subsets': upper_tail_branches(),
              'scope': 'Exact Hardy replacement of finite Dirichlet projectors with existing finite diagonal Euler/Gaussian kernels retained. No removal of Euler endpoint sectors or geometric edge-charge identification.'}
    Path(__file__).with_name('actual_hardy_cauchy_network_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'local_cases': len(rows), 'whole_word_cases': len(words),
                      'actual_support_beyond_head_observed': all(r['largest_intermediate_index'] >= r['N'] for r in rows)}))


if __name__ == '__main__':
    main()
